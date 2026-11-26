#!/usr/bin/env python3
"""Privacy guard for this repository's Claude Code sessions. Standard library only.

The bundle is published through public carriers, so nothing in it, or in this repository's own
files, may identify a private repository, its owner, organisation, customers or infrastructure, or
any person who uses the bundle. A rule the agent has to remember is a rule it forgets the first time
it did not load the file that states it; this script makes the rule reach every session anyway.

    privacy_guard.py remind   SessionStart (which fires again after a compaction): print the rule into the session
    privacy_guard.py gate     PreToolUse on Bash: block `git commit` / `git push` while
                              `bundle.py privacy` fails (exit 2 feeds the reason back to the agent); then,
                              under zsh, refuse a command that expands a spaced variable unquoted
                              (`bundle.py shell-check --hook`, d-5ed7e8-1d383e)

The user may override one finding, and only on their explicit instruction: the agent writes
`privacy-allow: <reason>` on that line, and `bundle.py privacy` lists every such allowance on every
run, so an override is never silent.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# The tools need Python 3.11 or newer (`tomllib`); this hook itself stays runnable by an older `python3`,
# because it is what a machine's default interpreter runs, and it looks for a newer one to run them.
MINIMUM = (3, 11)
TOOL = ROOT / ".agents/tools/bundle.py"

REMINDER = (
    "PRIVACY RULE (enforced; applies whether or not you loaded AGENTS.md): nothing written to this "
    "repository or to .agents/ may identify, directly or by cross-referencing, a private repository, "
    "its owner, organisation, customers, users or infrastructure, or any person. Generalise figures to "
    "ratios or orders of magnitude, paraphrase quotes, replace code/schema/product names with roles, "
    "drop locations, time zones and personal context; changelogs and history are not exempt, and "
    "sensitive or obsolete detail may be deleted. Run `python3 .agents/tools/bundle.py privacy` before "
    "committing; commits and pushes are blocked while it fails. Override a finding only when the user "
    "explicitly instructs it, with `privacy-allow: <reason>` on that line."
)

# Any shell line that names git and a commit or a push: quoted, wrapped in `bash -c`, with global options
# or a path. Broad on purpose: a line that is not a commit costs one privacy run, and blocks nothing unless
# the check fails.
GIT_WRITE = re.compile(r"\bgit\b.*\b(commit|push)\b", re.DOTALL)


def modern_python() -> str | None:
    """The first interpreter at `MINIMUM` or newer: this one, a versioned `python3.N`, or a common install."""
    names = [sys.executable, *(shutil.which(f"python3.{minor}") for minor in range(20, MINIMUM[1] - 1, -1)),
             shutil.which("python3"), "/opt/homebrew/bin/python3", "/usr/local/bin/python3"]
    probe = f"import sys; sys.exit(sys.version_info < {MINIMUM})"
    for name in names:
        if name and os.path.isfile(name) and subprocess.run([name, "-c", probe], capture_output=True).returncode == 0:
            return name
    return None


def remind() -> int:
    print(REMINDER)
    return 0


def gate() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except ValueError:
        payload = {}
    command = str((payload.get("tool_input") or {}).get("command", "")) if isinstance(payload, dict) else ""
    # The privacy gate first: it refuses whatever stopped it deciding. The zsh check only after it passes.
    return privacy_gate(command) or shell_gate(raw)


def shell_gate(raw: str) -> int:
    """Under zsh, refuse a command that assigns a variable words with spaces and expands it unquoted. A lint on the
    agent's own command, not a privacy guard: when it cannot run (no tool, an older one, no interpreter) it lets the
    call through, since refusing then would stop every command, the one that repairs it included."""
    python = modern_python() if TOOL.exists() else None
    if python is None:
        return 0
    result = subprocess.run([python, str(TOOL), "shell-check", "--hook"], input=raw, capture_output=True, text=True)
    if result.returncode == 2 and result.stderr.startswith("shell-check:"):
        print(result.stderr.strip(), file=sys.stderr)
        return 2
    return 0


def privacy_gate(command: str) -> int:
    if not GIT_WRITE.search(command):
        return 0
    if not TOOL.exists():
        print("privacy gate: .agents/tools/bundle.py is missing, so nothing can be checked; "
              "refusing the commit rather than letting it through unchecked.", file=sys.stderr)
        return 2
    # Two runs: the bundle as a tree, and every other file git tracks (`--tracked`), so a new published file
    # is checked without a list to keep; one call with both would read only the files.
    python = modern_python()
    if python is None:
        print(f"privacy gate: the tools need Python {MINIMUM[0]}.{MINIMUM[1]} or newer and none was found; "
              "refusing the commit rather than letting it through unchecked.", file=sys.stderr)
        return 2
    runs = [[str(ROOT / ".agents")], ["--tracked", "--repo", str(ROOT)]]
    results = [subprocess.run([python, str(TOOL), "privacy", *args], capture_output=True, text=True)
               for args in runs]
    if all(r.returncode == 0 for r in results):
        return 0
    # The failures first, from every run: a long list of warnings used to push them out of the message.
    output = "".join(r.stdout + r.stderr for r in results)
    failures = [line for line in output.splitlines() if " x " in line or line.startswith("  x ")]
    print("privacy gate: `bundle.py privacy` failed, so this git command is blocked. Fix each finding "
          "(generalise, paraphrase or delete). Only if the user explicitly instructs an exception, add "
          "`privacy-allow: <reason>` on that line.\n\n" + "\n".join(failures)[:6000], file=sys.stderr)
    return 2


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    sys.exit({"remind": remind, "gate": gate}.get(mode, lambda: 2)())
