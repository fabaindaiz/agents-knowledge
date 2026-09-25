#!/usr/bin/env python3
"""Privacy guard for this repository's Claude Code sessions. Standard library only.

The bundle is published through public carriers, so nothing in it, or in this repository's own
files, may identify a private repository, its owner, organisation, customers or infrastructure, or
any person who uses the bundle. A rule the agent has to remember is a rule it forgets the first time
it did not load the file that states it; this script makes the rule reach every session anyway.

    privacy_guard.py remind   SessionStart / UserPromptSubmit: print the rule into the session
    privacy_guard.py gate     PreToolUse on Bash: block `git commit` / `git push` while
                              `bundle.py privacy` fails (exit 2 feeds the reason back to the agent)

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
# The repository's own files that are published with it, checked with the same rules as the bundle.
ROOT_FILES = ["README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", ".github/workflows/check.yml"]

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
    try:
        payload = json.load(sys.stdin)
    except ValueError:
        payload = {}
    command = str((payload.get("tool_input") or {}).get("command", ""))
    if not GIT_WRITE.search(command):
        return 0
    if not TOOL.exists():
        print("privacy gate: .agents/tools/bundle.py is missing, so nothing can be checked; "
              "refusing the commit rather than letting it through unchecked.", file=sys.stderr)
        return 2
    # Two runs: `--paths` checks the named files instead of the bundle, not in addition to it, so a
    # single call with both silently skipped the bundle (seen 2026-09-24, "privacy over 6 files").
    paths = [str(ROOT / f) for f in ROOT_FILES if (ROOT / f).exists()]
    # The experiment, the release records and the full notes are published with the repository too; the
    # experiment's run outputs are ignored and never checked in.
    for folder in ("evals", "meta", "sources"):
        paths += [str(f) for f in sorted((ROOT / folder).rglob("*"))
                  if f.is_file() and "runs" not in f.relative_to(ROOT / folder).parts and "__pycache__" not in f.parts]
    python = modern_python()
    if python is None:
        print(f"privacy gate: the tools need Python {MINIMUM[0]}.{MINIMUM[1]} or newer and none was found; "
              "refusing the commit rather than letting it through unchecked.", file=sys.stderr)
        return 2
    runs = [[str(ROOT / ".agents")], ["--paths", *paths]]
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
