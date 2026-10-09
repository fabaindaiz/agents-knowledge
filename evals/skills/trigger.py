#!/usr/bin/env python3
"""Does a skill fire on the requests it is for, and stay quiet on the ones near them?

    python3 evals/skills/trigger.py --skill REPO/.claude/skills/NAME/SKILL.md --cases CASES.json
        [--runs N] [--claude-dir REPO/.claude] [--fixture DIR] [--out FILE]

Each case is one request to a fresh, headless session in an empty repository that holds the skill under
test, installed as `.claude/skills/<name>/SKILL.md`; with `--claude-dir`, a copy of a carrier's own `.claude/`
(its other skills, its settings) is installed first, and `--fixture` copies files the requests need. The
session's tool calls are read until the third, or the first write: the `Skill` tool naming this skill as the
first call is a fire (strict), and anywhere in those calls before any write is a lenient fire. Every tool that
writes or runs is refused by a hook rather than hidden, so the model still sees the tools it would choose
between, and a request such as "push everything" does nothing. The machine's own configuration (its global
instructions, plugins and other skills) stays loaded on purpose: that is the competition the skill meets.

Every tool but the few that only read or choose is refused, a connector's included; a shell command runs
only when it reads (`ls`, `cat`, `git status`, ... with no redirection or chaining), and is recorded. A session that never
started or ended in an error before any tool call is an error, left out of every rate, and a few in a row stop
the run. Reading the skill's file counts as invoking it. With `--router`, a skill that asks to run before any
response is looked past (the routed metric). A case marked `"canary": true` names the skill outright: if one
does not fire, the run is invalid, since the setup, not the description, is what failed.

A pass is a strict fire rate of at least 0.8 on the requests that expect it, a misfire rate of at most 0.1 on
the near misses, and at least 0.8 on the cases marked `"owner": true` (the owner's own words) when there are
any (`meta/reviews/2026-10-02-adversarial-review.md`, §3.1; `meta/reviews/2026-10-05-skill-triggers.md`).
A case marked `"ambiguous": true` is run and reported apart, and never decides the pass.
Each rate is printed with its Wilson interval; with `--runs N` every case runs N times. The table of first
calls shows which competitor captured each case. Exit 0 on a pass, 1 on a fail. Cases are held out: none of
them is written into the description it tests. They live in the carrier that runs them, beside its
`LOCAL.md`, because they are its people's own words; cases that mix several repositories' words live outside
every repository, in `~/.config/agent-guides/trigger-cases/` on the machine that runs them: never here.

Before trusting a run, check that the skill's description is in the session's skill listing: a description
the listing truncated or dropped measures nothing.
"""

from __future__ import annotations

import argparse
import re
import json
import math
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
from collections import Counter
from pathlib import Path

FIRE, MISFIRE = 0.8, 0.1
# Every other tool is refused by a hook, a connector's (`mcp__…`) as much as a built-in one: a request such as
# "push everything" must do nothing, through any tool the machine has.
ALLOWED = ("Read", "Grep", "Glob", "Skill", "ToolSearch", "TodoWrite")
# The read-only classifier lives in the bundle tool since 0.0.30, shared with the researcher agent's hook.
def _bundle_tool():  # noqa: ANN202
    import importlib.util
    path = Path(__file__).resolve().parents[2] / "sources" / "bundle" / "tools" / "bundle.py"
    spec = importlib.util.spec_from_file_location("agent_guides_bundle", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("agent_guides_bundle", module)  # a dataclass looks its module up there
    spec.loader.exec_module(module)
    return module


_B = _bundle_tool()
READ_ONLY, WRITING_SHORT, WRITING_LONG = _B.READ_ONLY, _B.WRITING_SHORT, _B.WRITING_LONG
SHORT_BY_COMMAND, LONG_BY_COMMAND, SEPARATORS, QUIET = _B.SHORT_BY_COMMAND, _B.LONG_BY_COMMAND, _B.SEPARATORS, _B.QUIET
shell_words, _writes, read_only = _B.shell_words, _B._writes, _B.read_only
PREAMBLE = {"ToolSearch", "TodoWrite"}  # calls a session may make before choosing; the routed metric looks past them
CALLS = 5  # the lenient metric reads this many tool calls


def tool_calls(lines, limit: int = CALLS) -> list[tuple[str, str]]:  # noqa: ANN001 -- any iterable of stream-json lines
    """(tool name, its target) of the first tool calls in a stream, up to `limit`: the skill for `Skill`, the
    path for `Read`, empty otherwise."""
    calls: list[tuple[str, str]] = []
    for line in lines:
        try:
            event = json.loads(line)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(event, dict) or event.get("type") != "assistant":
            continue
        for block in event.get("message", {}).get("content", []):
            if block.get("type") == "tool_use":
                name = block.get("name")
                key = {"Skill": "skill", "Read": "file_path", "Bash": "command"}.get(name)
                target = str(block.get("input", {}).get(key, "")) if key else ""
                calls.append((name, target if name == "Bash" else target[:200]))  # a command is judged whole
                if len(calls) >= limit:
                    return calls
    return calls


def allowed(call: tuple[str, str]) -> bool:
    return call[0] in ALLOWED or (call[0] == "Bash" and read_only(call[1]))


def hook_decision(payload: dict) -> int:
    """The refusing hook's answer for one tool call: 0 lets it run, 2 refuses it."""
    tool = payload.get("tool_name", "")
    command = str((payload.get("tool_input") or {}).get("command", ""))
    return 0 if allowed((tool, command if tool == "Bash" else "")) else 2


def first_call(lines) -> tuple[str | None, str]:  # noqa: ANN001
    """(tool name, skill name when the tool is `Skill`) of the first tool call in a stream, or (None, "")."""
    calls = tool_calls(lines, 1)
    return calls[0] if calls else (None, "")


def judge(calls: list[tuple[str, str]], name: str, routers: tuple[str, ...] = ()) -> dict[str, bool]:
    """Strict: the first call is this skill. Lenient: this skill among the first calls, before any refused one.
    Routed, with `routers`: the first call past the preamble and the router skills named is this skill.

    The skill is invoked through `Skill`, or its file is read (a host may load a skill that way)."""
    def ours(call: tuple[str, str]) -> bool:
        if call[0] == "Skill":
            return call[1].split(":")[-1] == name
        return call[0] == "Read" and f"/.claude/skills/{name}/" in call[1].replace("\\", "/")

    lenient = False
    for call in calls[:CALLS]:
        if ours(call):
            lenient = True
            break
        if not allowed(call):
            break
    out = {"strict": bool(calls) and ours(calls[0]), "lenient": lenient}
    if routers:
        past = [c for c in calls if not (c[0] in PREAMBLE or (c[0] == "Skill" and c[1].split(":")[-1] in routers))]
        out["routed"] = bool(past) and ours(past[0])
    return out


def should_stop(calls: list[tuple[str, str]], name: str) -> bool:
    """A session has said what it would do once it fired, tried a refused tool, or filled the window."""
    return len(calls) >= CALLS or any(not allowed(c) for c in calls) or (bool(calls) and judge(calls, name)["lenient"])


def session_info(lines) -> dict:  # noqa: ANN001
    """What the session's init event says it loaded: the model, the tools and the skills it listed."""
    for line in lines:
        try:
            event = json.loads(line)
        except (json.JSONDecodeError, TypeError):
            continue
        if isinstance(event, dict) and event.get("type") == "system" and event.get("subtype") == "init":
            return {k: event.get(k) for k in ("model", "tools", "skills", "slash_commands", "claude_code_version")}
    return {}


def session_error(lines, stderr: str = "") -> str | None:  # noqa: ANN001
    """Why a session measured nothing, or None. A session that never started, or ended in an error before any
    tool call, is an error and never a quiet answer: a usage limit hit mid-run would otherwise score every
    remaining near miss as a pass."""
    lines = list(lines)
    if tool_calls(lines, 1):
        return None
    if not session_info(lines):
        return "no init event" + (f": {stderr.strip()[-300:]}" if stderr.strip() else "")
    for line in lines:
        try:
            event = json.loads(line)
        except (json.JSONDecodeError, TypeError):
            continue
        if isinstance(event, dict) and event.get("type") == "result":
            return f"error result: {str(event.get('result'))[:300]}" if event.get("is_error") else None
    return "no result event" + (f": {stderr.strip()[-300:]}" if stderr.strip() else "")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """The Wilson score interval of k successes in n trials, at about 95 % by default."""
    if n == 0:
        return 0.0, 1.0
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return round(max(0.0, centre - half), 3), round(min(1.0, centre + half), 3)


def _rate(rows: list[dict], key: str) -> tuple[float, tuple[float, float]]:
    k = sum(bool(r.get(key)) for r in rows)
    return (round(k / len(rows), 3) if rows else 0.0), wilson(k, len(rows))


def verdict(results: list[dict], gate: str = "strict", max_misfire: float = MISFIRE) -> dict:
    """The rates on the cases that expect the skill and on the near misses, with intervals, and the pass.

    The gate is strict (the skill as the first call) unless `gate="lenient"`: for a skill whose requests point at
    material a session reads first, a fire after reads and before any write counts, for the near misses as much as
    for the expected cases (`meta/reviews/2026-10-07-trigger-eval-adversarial.md`, stage 2b).

    `max_misfire` relaxes only the near misses' bound, where a decision prefers a skill that fires slightly too
    often to one that misses (`d-5ed7e8-7a95b5`).

    A case marked `"ambiguous": true` is labelled by the owner's best guess: it is counted apart, by how often
    the session agreed with the label, and never decides the pass.
    """
    errors = [r for r in results if r.get("error")]
    canaries = [r for r in results if r.get("canary") and not r.get("error")]
    unsure = [r for r in results if r.get("ambiguous") and not r.get("error")]
    results = [r for r in results if not (r.get("ambiguous") or r.get("canary") or r.get("error"))]
    valid = all(r.get("fired") for r in canaries)
    expected = [r for r in results if r["expect"]]
    near = [r for r in results if not r["expect"]]
    owner = [r for r in expected if r.get("owner")]
    fire, fire_interval = _rate(expected, "fired")
    misfire, misfire_interval = _rate(near, "fired")
    lenient, lenient_interval = _rate(expected, "lenient")
    owner_fire, owner_interval = _rate(owner, "fired")
    key = "lenient" if gate == "lenient" else "fired"
    gated_fire, gated_misfire, gated_owner = _rate(expected, key)[0], _rate(near, key)[0], _rate(owner, key)[0]
    passed = valid and gated_fire >= FIRE and gated_misfire <= max_misfire and (not owner or gated_owner >= FIRE)
    return {"fire": fire, "fire_interval": fire_interval, "misfire": misfire, "misfire_interval": misfire_interval,
            "lenient_fire": lenient, "lenient_interval": lenient_interval,
            "owner_fire": owner_fire if owner else None, "owner_interval": owner_interval if owner else None,
            "gate": gate, "max_misfire": max_misfire, "lenient_misfire": _rate(near, "lenient")[0], "passed": passed, "valid": valid, "cases": len(results), "errors": len(errors),
            "canary": {"cases": len(canaries), "fired": sum(bool(r.get("fired")) for r in canaries)},
            "ambiguous": {"cases": len(unsure), "agreed": sum(bool(r.get("fired")) == r["expect"] for r in unsure)}}


def captures(results: list[dict]) -> dict[str, dict[str, int]]:
    """For each request, how often each first call took it: which competitor captured the case."""
    table: dict[str, Counter] = {}
    for r in results:
        table.setdefault(r["request"], Counter())[r["first_call"]] += 1
    return {request: dict(counter) for request, counter in table.items()}


def deny_hook_settings(settings: dict | None) -> dict:
    """The settings with a hook that refuses every tool but the few that only read or choose, keeping the rest
    as they were.

    `--disallowedTools` would remove those tools from what the model sees, which changes the choice being
    measured; a hook refuses the call and leaves the choice alone. It allows by name, so a tool nobody listed,
    a connector's included, is refused."""
    out = json.loads(json.dumps(settings or {}))
    hook = {"matcher": "*", "hooks": [{"type": "command",
                                       "command": f"'{sys.executable}' '{Path(__file__).resolve()}' --hook"}]}
    out.setdefault("hooks", {}).setdefault("PreToolUse", []).append(hook)
    return out


def command(claude: str, request: str, model: str | None = None) -> list[str]:
    return [claude, "-p", request, "--output-format", "stream-json", "--verbose", "--no-session-persistence"] \
        + (["--model", model] if model else [])


def run_case(claude: str, skill: Path, name: str, request: str, timeout: int,
             claude_dir: Path | None = None, fixture: Path | None = None, model: str | None = None,
             session_timeout: int = 300) -> dict:
    """One session on one request: its first tool calls, why it measured nothing if it did not, and what it loaded."""
    work = Path(tempfile.mkdtemp(prefix="trigger-"))
    try:
        subprocess.run(["git", "init", "-q"], cwd=work, check=True)
        if fixture:
            shutil.copytree(fixture, work, dirs_exist_ok=True)
        if claude_dir:
            shutil.copytree(claude_dir, work / ".claude", dirs_exist_ok=True)
        (work / ".claude/skills" / name).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(skill, work / ".claude/skills" / name / "SKILL.md")
        settings_path = work / ".claude/settings.json"
        current = json.loads(settings_path.read_text(encoding="utf-8")) if settings_path.is_file() else None
        settings_path.write_text(json.dumps(deny_hook_settings(current), indent=2), encoding="utf-8")
        with subprocess.Popen(command(claude, request, model), cwd=work, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, text=True) as proc:
            seen: list[str] = []
            watchdog = threading.Timer(session_timeout, proc.kill)  # a session that hangs ends as an error
            watchdog.start()
            try:
                for line in proc.stdout:
                    seen.append(line)
                    calls = tool_calls(seen)
                    if should_stop(calls, name):
                        break
            finally:
                watchdog.cancel()
                proc.kill()
                stderr = proc.stderr.read() if proc.stderr else ""
                proc.wait(timeout=timeout)
        return {"calls": tool_calls(seen), "error": session_error(seen, stderr), "info": session_info(seen)}
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main(argv: list[str] | None = None) -> int:
    if (argv if argv is not None else sys.argv[1:]) == ["--hook"]:  # run by the refusing hook, one tool call on stdin
        try:
            code = hook_decision(json.load(sys.stdin))
        except Exception as error:  # noqa: BLE001 -- a hook that raises exits 1, which the host lets through
            print(f"trigger eval: refused, the hook could not read the call ({error})", file=sys.stderr)
            return 2
        if code:
            print("trigger eval: tools are refused here", file=sys.stderr)
        return code
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True, type=Path, help="the installed SKILL.md under test")
    parser.add_argument("--cases", required=True, type=Path,
                        help="JSON: [{\"request\": ..., \"expect\": true|false, \"owner\": true, \"ambiguous\": true (both optional)}]")
    parser.add_argument("--runs", type=int, default=1, help="how many times each case runs")
    parser.add_argument("--claude-dir", type=Path, help="a carrier's .claude/ folder, copied into each session")
    parser.add_argument("--fixture", type=Path, help="files copied into each session's repository first")
    parser.add_argument("--claude", default=shutil.which("claude") or "claude")
    parser.add_argument("--out", type=Path, help="where to write each run's result and the verdict, as JSON")
    parser.add_argument("--timeout", type=int, default=30, help="seconds to wait for a killed session to exit")
    parser.add_argument("--session-timeout", type=int, default=300, help="seconds before a session is ended as an error")
    parser.add_argument("--model", help="the model every session runs on; pin it, since the listing's budget follows it")
    parser.add_argument("--router", action="append", default=[],
                        help="a skill that asks to run before any response; the routed metric looks past it")
    parser.add_argument("--gate", choices=("strict", "lenient"), default="strict",
                        help="lenient counts a fire after reads, for a skill whose requests point at material to read")
    parser.add_argument("--max-misfire", type=float, default=MISFIRE,
                        help="the near misses' bound; raise it only by a decision (d-5ed7e8-7a95b5)")
    parser.add_argument("--max-errors", type=int, default=3, help="consecutive errors that stop the run")
    args = parser.parse_args(argv)
    text = args.skill.read_text(encoding="utf-8")
    name = next(line.split(":", 1)[1].strip().strip('"') for line in text.split("\n") if line.startswith("name:"))
    results, sessions, streak = [], [], 0
    version = subprocess.run([args.claude, "--version"], capture_output=True, text=True).stdout.strip()
    for case in json.loads(args.cases.read_text(encoding="utf-8")):
        for _ in range(args.runs):
            ran = run_case(args.claude, args.skill, name, case["request"], args.timeout, args.claude_dir, args.fixture,
                           args.model, args.session_timeout)
            calls = ran["calls"]
            judged = judge(calls, name, tuple(args.router))
            first = f"{calls[0][0]}:{calls[0][1]}" if calls and calls[0][1] else (calls[0][0] if calls else "None")
            results.append({**case, "first_call": first, "calls": [f"{t}:{s}" if s else t for t, s in calls],
                            "fired": judged["strict"], "lenient": judged["lenient"], "routed": judged.get("routed"),
                            "error": ran["error"]})
            if ran["info"]:
                sessions.append(ran["info"])
            state = "ERROR" if ran["error"] else ("fire" if judged["strict"] else "quiet")
            print(f"  {state:5} expect={'fire' if case['expect'] else 'quiet':5} {first:24} {case['request']}"
                  + (f"  [{ran['error']}]" if ran["error"] else ""), flush=True)
            streak = streak + 1 if ran["error"] else 0
            if streak >= args.max_errors:
                print(f"stopped: {streak} sessions in a row measured nothing", flush=True)
                break
        if streak >= args.max_errors:
            break
    result = verdict(results, args.gate, args.max_misfire)
    print(f"fire {result['fire']} {result['fire_interval']} (at least {FIRE}), lenient {result['lenient_fire']} "
          f"{result['lenient_interval']}, misfire {result['misfire']} {result['misfire_interval']} (at most {result['max_misfire']})"
          + (f", owner's words {result['owner_fire']} {result['owner_interval']}" if result["owner_fire"] is not None else "")
          + f": {'pass' if result['passed'] else 'fail'} (gate: {result['gate']})"
          + (f"; ambiguous, apart: {result['ambiguous']['agreed']}/{result['ambiguous']['cases']} agreed with the label"
             if result["ambiguous"]["cases"] else "")
          + (f"; canaries {result['canary']['fired']}/{result['canary']['cases']}"
             + ("" if result["valid"] else ", so the run is INVALID") if result["canary"]["cases"] else "")
          + (f"; {result['errors']} errors left out" if result["errors"] else ""))
    if args.router:
        routed = [r for r in results if r["expect"] and not (r.get("error") or r.get("ambiguous") or r.get("canary"))]
        print(f"routed fire, past {', '.join(args.router)}: {sum(bool(r['routed']) for r in routed)}/{len(routed)}")
    for request, taken in captures([r for r in results if not r["fired"] and r["expect"]]).items():
        print(f"  captured: {request!r} -> {taken}")
    if args.out:
        args.out.write_text(json.dumps({"skill": name, "claude_version": version, "model": args.model,
                                        "routers": args.router, "sessions": sessions[:1], "verdict": result,
                                        "captures": captures(results), "results": results},
                                       indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if streak >= args.max_errors:
        return 2
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
