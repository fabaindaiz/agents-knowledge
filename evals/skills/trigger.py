#!/usr/bin/env python3
"""Does a skill fire on the requests it is for, and stay quiet on the ones near them?

    python3 evals/skills/trigger.py --skill REPO/.claude/skills/NAME/SKILL.md --cases CASES.json [--out FILE]

Each case is one request to a fresh, headless session in an empty repository that holds only the skill
under test, installed as `.claude/skills/<name>/SKILL.md`. The session's first tool call is the answer:
the `Skill` tool naming this skill is a fire, anything else (another tool, or none) is not. The session
is stopped there, and every tool that writes or runs is refused, so a request such as "push everything"
does nothing. The machine's own configuration (its global instructions, plugins and other skills)
stays loaded on purpose: that is the competition the skill meets in real sessions.

A pass is a fire rate of at least 0.8 on the requests that expect it and a misfire rate of at most 0.1
on the near misses (`meta/reviews/2026-10-02-adversarial-review.md`, §3.1). Exit 0 on a pass, 1 on a
fail. Cases are held out: none of them is written into the description it tests. They live in the
carrier that runs them, beside its `LOCAL.md`, because they are its people's own words: never here.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FIRE, MISFIRE = 0.8, 0.1
REFUSED = ["Bash", "Edit", "Write", "NotebookEdit", "WebFetch", "WebSearch", "Agent", "Workflow"]


def first_call(lines) -> tuple[str | None, str]:  # noqa: ANN001 -- any iterable of stream-json lines
    """(tool name, skill name when the tool is `Skill`) of the first tool call in a stream, or (None, "")."""
    for line in lines:
        try:
            event = json.loads(line)
        except (json.JSONDecodeError, TypeError):
            continue
        if event.get("type") != "assistant":
            continue
        for block in event.get("message", {}).get("content", []):
            if block.get("type") == "tool_use":
                name = block.get("name")
                return name, str(block.get("input", {}).get("skill", "")) if name == "Skill" else ""
    return None, ""


def verdict(results: list[dict]) -> dict:
    """The fire rate on the cases that expect the skill, the misfire rate on the others, and the pass."""
    expected = [r for r in results if r["expect"]]
    near = [r for r in results if not r["expect"]]
    fire = round(sum(r["fired"] for r in expected) / len(expected), 3) if expected else 0.0
    misfire = round(sum(r["fired"] for r in near) / len(near), 3) if near else 0.0
    return {"fire": fire, "misfire": misfire, "passed": fire >= FIRE and misfire <= MISFIRE,
            "cases": len(results)}


def run_case(claude: str, skill: Path, name: str, request: str, timeout: int) -> tuple[str | None, str]:
    work = Path(tempfile.mkdtemp(prefix="trigger-"))
    try:
        subprocess.run(["git", "init", "-q"], cwd=work, check=True)
        (work / ".claude/skills" / name).mkdir(parents=True)
        shutil.copyfile(skill, work / ".claude/skills" / name / "SKILL.md")
        cmd = [claude, "-p", request, "--output-format", "stream-json", "--verbose", "--no-session-persistence",
               "--disallowedTools", *REFUSED]
        with subprocess.Popen(cmd, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True) as proc:
            seen = []
            try:
                for line in proc.stdout:
                    seen.append(line)
                    if first_call([line])[0] is not None:
                        break
            finally:
                proc.kill()
                proc.wait(timeout=timeout)
        return first_call(seen)
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True, type=Path, help="the installed SKILL.md under test")
    parser.add_argument("--cases", required=True, type=Path, help="JSON: [{\"request\": ..., \"expect\": true|false}]")
    parser.add_argument("--claude", default=shutil.which("claude") or "claude")
    parser.add_argument("--out", type=Path, help="where to write each case's result and the verdict, as JSON")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args(argv)
    text = args.skill.read_text(encoding="utf-8")
    name = next(line.split(":", 1)[1].strip().strip('"') for line in text.split("\n") if line.startswith("name:"))
    results = []
    for case in json.loads(args.cases.read_text(encoding="utf-8")):
        tool, skill = run_case(args.claude, args.skill, name, case["request"], args.timeout)
        fired = tool == "Skill" and skill.split(":")[-1] == name
        results.append({**case, "first_call": f"{tool}:{skill}" if skill else str(tool), "fired": fired})
        print(f"  {'fire' if fired else 'quiet':5} expect={'fire' if case['expect'] else 'quiet':5} "
              f"{results[-1]['first_call']:24} {case['request']}", flush=True)
    result = verdict(results)
    print(f"fire {result['fire']} (at least {FIRE}), misfire {result['misfire']} (at most {MISFIRE}): "
          + ("pass" if result["passed"] else "fail"))
    if args.out:
        args.out.write_text(json.dumps({"skill": name, "verdict": result, "results": results}, indent=2,
                                       ensure_ascii=False) + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
