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

A pass is a strict fire rate of at least 0.8 on the requests that expect it, a misfire rate of at most 0.1 on
the near misses, and at least 0.8 on the cases marked `"owner": true` (the owner's own words) when there are
any (`meta/reviews/2026-10-02-adversarial-review.md`, §3.1; `meta/reviews/2026-10-05-skill-triggers.md`).
A case marked `"ambiguous": true` is run and reported apart, and never decides the pass.
Each rate is printed with its Wilson interval; with `--runs N` every case runs N times. The table of first
calls shows which competitor captured each case. Exit 0 on a pass, 1 on a fail. Cases are held out: none of
them is written into the description it tests. They live in the carrier that runs them, beside its
`LOCAL.md`, because they are its people's own words: never here.

Before trusting a run, check that the skill's description is in the session's skill listing: a description
the listing truncated or dropped measures nothing.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

FIRE, MISFIRE = 0.8, 0.1
REFUSED = ["Bash", "Edit", "Write", "NotebookEdit", "WebFetch", "WebSearch", "Agent", "Workflow"]
WRITES = {"Edit", "Write", "NotebookEdit"}
CALLS = 3  # the lenient metric reads this many tool calls


def tool_calls(lines, limit: int = CALLS) -> list[tuple[str, str]]:  # noqa: ANN001 -- any iterable of stream-json lines
    """(tool name, skill name when the tool is `Skill`) of the first tool calls in a stream, up to `limit`."""
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
                calls.append((name, str(block.get("input", {}).get("skill", "")) if name == "Skill" else ""))
                if len(calls) >= limit:
                    return calls
    return calls


def first_call(lines) -> tuple[str | None, str]:  # noqa: ANN001
    """(tool name, skill name when the tool is `Skill`) of the first tool call in a stream, or (None, "")."""
    calls = tool_calls(lines, 1)
    return calls[0] if calls else (None, "")


def judge(calls: list[tuple[str, str]], name: str) -> dict[str, bool]:
    """Strict: the first call is this skill. Lenient: this skill among the first calls, before any write."""
    def ours(call: tuple[str, str]) -> bool:
        return call[0] == "Skill" and call[1].split(":")[-1] == name

    lenient = False
    for call in calls[:CALLS]:
        if call[0] in WRITES:
            break
        if ours(call):
            lenient = True
            break
    return {"strict": bool(calls) and ours(calls[0]), "lenient": lenient}


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


def verdict(results: list[dict]) -> dict:
    """The rates on the cases that expect the skill and on the near misses, with intervals, and the pass.

    A case marked `"ambiguous": true` is labelled by the owner's best guess: it is counted apart, by how often
    the session agreed with the label, and never decides the pass.
    """
    unsure = [r for r in results if r.get("ambiguous")]
    results = [r for r in results if not r.get("ambiguous")]
    expected = [r for r in results if r["expect"]]
    near = [r for r in results if not r["expect"]]
    owner = [r for r in expected if r.get("owner")]
    fire, fire_interval = _rate(expected, "fired")
    misfire, misfire_interval = _rate(near, "fired")
    lenient, lenient_interval = _rate(expected, "lenient")
    owner_fire, owner_interval = _rate(owner, "fired")
    passed = fire >= FIRE and misfire <= MISFIRE and (not owner or owner_fire >= FIRE)
    return {"fire": fire, "fire_interval": fire_interval, "misfire": misfire, "misfire_interval": misfire_interval,
            "lenient_fire": lenient, "lenient_interval": lenient_interval,
            "owner_fire": owner_fire if owner else None, "owner_interval": owner_interval if owner else None,
            "passed": passed, "cases": len(results),
            "ambiguous": {"cases": len(unsure), "agreed": sum(bool(r.get("fired")) == r["expect"] for r in unsure)}}


def captures(results: list[dict]) -> dict[str, dict[str, int]]:
    """For each request, how often each first call took it: which competitor captured the case."""
    table: dict[str, Counter] = {}
    for r in results:
        table.setdefault(r["request"], Counter())[r["first_call"]] += 1
    return {request: dict(counter) for request, counter in table.items()}


def deny_hook_settings(settings: dict | None) -> dict:
    """The settings with a hook that refuses every tool that writes or runs, keeping the rest as they were.

    `--disallowedTools` would remove those tools from what the model sees, which changes the choice being
    measured; a hook refuses the call and leaves the choice alone."""
    out = json.loads(json.dumps(settings or {}))
    hook = {"matcher": "|".join(REFUSED),
            "hooks": [{"type": "command", "command": "echo 'trigger eval: tools are refused here' >&2; exit 2"}]}
    out.setdefault("hooks", {}).setdefault("PreToolUse", []).append(hook)
    return out


def command(claude: str, request: str) -> list[str]:
    return [claude, "-p", request, "--output-format", "stream-json", "--verbose", "--no-session-persistence"]


def run_case(claude: str, skill: Path, name: str, request: str, timeout: int,
             claude_dir: Path | None = None, fixture: Path | None = None) -> list[tuple[str, str]]:
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
        with subprocess.Popen(command(claude, request), cwd=work, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                              text=True) as proc:
            seen = []
            try:
                for line in proc.stdout:
                    seen.append(line)
                    calls = tool_calls(seen)
                    if len(calls) >= CALLS or any(c[0] in WRITES for c in calls) or (calls and judge(calls, name)["lenient"]):
                        break
            finally:
                proc.kill()
                proc.wait(timeout=timeout)
        return tool_calls(seen)
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True, type=Path, help="the installed SKILL.md under test")
    parser.add_argument("--cases", required=True, type=Path,
                        help="JSON: [{\"request\": ..., \"expect\": true|false, \"owner\": true, \"ambiguous\": true (both optional)}]")
    parser.add_argument("--runs", type=int, default=1, help="how many times each case runs")
    parser.add_argument("--claude-dir", type=Path, help="a carrier's .claude/ folder, copied into each session")
    parser.add_argument("--fixture", type=Path, help="files copied into each session's repository first")
    parser.add_argument("--claude", default=shutil.which("claude") or "claude")
    parser.add_argument("--out", type=Path, help="where to write each run's result and the verdict, as JSON")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args(argv)
    text = args.skill.read_text(encoding="utf-8")
    name = next(line.split(":", 1)[1].strip().strip('"') for line in text.split("\n") if line.startswith("name:"))
    results = []
    for case in json.loads(args.cases.read_text(encoding="utf-8")):
        for _ in range(args.runs):
            calls = run_case(args.claude, args.skill, name, case["request"], args.timeout, args.claude_dir, args.fixture)
            judged = judge(calls, name)
            first = f"{calls[0][0]}:{calls[0][1]}" if calls and calls[0][1] else (calls[0][0] if calls else "None")
            results.append({**case, "first_call": first, "calls": [f"{t}:{s}" if s else t for t, s in calls],
                            "fired": judged["strict"], "lenient": judged["lenient"]})
            print(f"  {'fire' if judged['strict'] else 'quiet':5} expect={'fire' if case['expect'] else 'quiet':5} "
                  f"{first:24} {case['request']}", flush=True)
    result = verdict(results)
    print(f"fire {result['fire']} {result['fire_interval']} (at least {FIRE}), lenient {result['lenient_fire']} "
          f"{result['lenient_interval']}, misfire {result['misfire']} {result['misfire_interval']} (at most {MISFIRE})"
          + (f", owner's words {result['owner_fire']} {result['owner_interval']}" if result["owner_fire"] is not None else "")
          + ": " + ("pass" if result["passed"] else "fail")
          + (f"; ambiguous, apart: {result['ambiguous']['agreed']}/{result['ambiguous']['cases']} agreed with the label"
             if result["ambiguous"]["cases"] else ""))
    for request, taken in captures([r for r in results if not r["fired"] and r["expect"]]).items():
        print(f"  captured: {request!r} -> {taken}")
    if args.out:
        args.out.write_text(json.dumps({"skill": name, "verdict": result, "captures": captures(results),
                                        "results": results}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
