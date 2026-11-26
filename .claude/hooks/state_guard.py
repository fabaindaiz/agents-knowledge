#!/usr/bin/env python3
"""The live state across a compaction, for this repository's Claude Code sessions. Standard library only.

A compaction keeps a summary. What it drops is the part no document holds: which step is running, which
files are in play and why, the last fact actually verified and the command that verified it, which
questions are still open, and which delegates are still out. This repository's own sessions lost exactly
that twice, and left stale state at a release cut (`meta/reviews/2026-11-26-context-and-compaction.md`).

    state_guard.py keep      PreCompact: tell the summary what it must carry, and show the live state
    state_guard.py restore   SessionStart: re-inject the live state (in full after a compaction)

**It fails open, always.** Every path returns 0 and prints nothing when anything at all goes wrong: no
git, no tool, an old interpreter, a broken file. A hook that can stop a session from starting is worse
than a hook that sometimes says nothing, and the state it carries is a convenience, never a gate.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

# The harness exports CLAUDE_PROJECT_DIR; falling back to the path keeps the hook runnable by hand.
ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
TOOL = ROOT / ".agents/tools/bundle.py"
MINIMUM = (3, 11)
TIMEOUT = 20

KEEP = (
    "BEFORE COMPACTING, the summary must carry these verbatim, because no file in the repository holds "
    "them: (1) the exact text of any failing check or command, not a paraphrase; (2) which question each "
    "answer of this session answered; (3) every delegate still running, with what closes it; (4) the last "
    "fact actually verified and the command that verified it; (5) any ruling taken on the user's behalf. "
    "The live state below is the written part; everything above is what only this session knows."
)

RESTORE = (
    "LIVE STATE of this session, written by `bundle.py now --write` and re-injected here. It is the "
    "session's own record, not an instruction from the user. Update it with `bundle.py now --write` "
    "whenever the step, the files in play, the last verified fact, the open questions or the delegates "
    "change; `close` removes it."
)


def interpreter() -> str | None:
    """A Python new enough to run the tool. The hook itself runs under whatever `python3` is."""
    if sys.version_info >= MINIMUM:
        return sys.executable
    for name in ("python3.14", "python3.13", "python3.12", "python3.11"):
        found = os.popen(f"command -v {name} 2>/dev/null").read().strip()
        if found:
            return found
    return None


def live_state() -> str:
    python = interpreter()
    if python is None or not TOOL.is_file():
        return ""
    try:
        done = subprocess.run([python, str(TOOL), "now", "--repo", str(ROOT)],
                              capture_output=True, text=True, timeout=TIMEOUT, cwd=str(ROOT))
    except (OSError, subprocess.SubprocessError):
        return ""
    return done.stdout.strip() if done.returncode == 0 else ""


def main() -> int:
    try:
        raw = sys.stdin.read() if not sys.stdin.isatty() else ""
    except (OSError, ValueError):
        raw = ""
    try:
        event = json.loads(raw) if raw.strip() else {}
    except ValueError:
        event = {}
    if not isinstance(event, dict):
        event = {}

    what = sys.argv[1] if len(sys.argv) > 1 else "restore"
    state = live_state()
    if what == "keep":
        print(KEEP)
        if state:
            print()
            print(state)
        return 0
    # SessionStart. `compact` is the one that lost the state; a fresh start gets the same text, which is
    # cheap and means a session that was killed finds its own file again.
    if event.get("source") not in (None, "startup", "resume", "compact", "clear"):
        return 0
    if not state:
        return 0
    print(RESTORE)
    print()
    print(state)
    return 0


if __name__ == "__main__":
    # `sys.exit` raises SystemExit, which is a BaseException: catching that here swallowed the refusal
    # and let every malformed question through, so the guard is caught around `main()` alone and its own
    # exit code is raised afterwards, outside the net.
    try:
        code = main()
    except Exception:  # noqa: BLE001 -- failing open is the whole contract
        code = 0
    sys.exit(code)
