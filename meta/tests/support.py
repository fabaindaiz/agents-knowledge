"""What every test module shares: the two tools, loaded from their files, and a throwaway folder.

The carrier tool (`.agents/tools/bundle.py`) and the home tool (`meta/tools/release.py`) are scripts,
not packages, so they are loaded by path. Run the suite from the repository root with

    python3 -m unittest discover -s meta/tests -t .
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]


def _load(name: str, path: Path):  # noqa: ANN202 -- a module
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


bundle = _load("bundle", ROOT / "sources/bundle/tools/bundle.py")  # the original; the build checks its release copy


def release():  # noqa: ANN201 -- a module; loaded lazily, it does not exist before the home tool does
    return _load("release", ROOT / "meta/tools/release.py")


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True).stdout


def init_repo(repo: Path) -> Path:
    repo.mkdir(parents=True, exist_ok=True)
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "t@example.com")
    git(repo, "config", "user.name", "t")
    git(repo, "config", "commit.gpgsign", "false")
    git(repo, "config", "tag.gpgsign", "false")
    return repo


def commit(repo: Path, message: str = "commit") -> str:
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "--allow-empty", "-m", message)
    return git(repo, "rev-parse", "HEAD").strip()


README = """---
bundle: "agent-guides"
version: "{version}"
released: "2026-01-01"
---

# Guides

Reads:
- knowledge/INDEX.md
"""

CONTEXT = """# Context

## Engineering standards

### 20. Nothing private travels, directly or by reconstruction

Nothing private.
"""

BOOTSTRAP = """# Bootstrap

Reads:
- method/prompt-context.md §Engineering standards

## The session loop

Work.

Reads:
- method/prompt-bootstrap.md §The session loop
- knowledge/INDEX.md
"""

NOTE = """---
slug: "{slug}"
topic: "t"
claim: "A claim."
confidence: "reasoned"
check: "a check"
boundary: "when not"
---

# {slug}

## Why it works

Because.
"""


def make_bundle(root: Path, version: str = "0.0.1") -> Path:
    """A minimal bundle in the 0.0.22 layout, checksummed, with a carrier file of its own."""
    agents = root / ".agents"
    for folder in ("method", "knowledge/notes/active", "proposals", "incoming", "tools"):
        (agents / folder).mkdir(parents=True, exist_ok=True)
    (agents / "README.md").write_text(README.format(version=version))
    (agents / "CHANGELOG.md").write_text("# Changelog\n\n## [Unreleased]\n\n## [0.0.1] - 2026-01-01\n\n### Added\n\n- The start.\n")
    (agents / "method/prompt-context.md").write_text(CONTEXT)
    (agents / "method/prompt-bootstrap.md").write_text(BOOTSTRAP)
    for session in ("evaluate", "update", "harvest"):
        (agents / f"method/prompt-{session}.md").write_text(f"# {session}\n\nReads:\n- method/prompt-{session}.md\n")
    (agents / "agents").mkdir(parents=True, exist_ok=True)
    (agents / "agents/knowledge-reviewer.md").write_text('---\nname: "knowledge-reviewer"\n---\n\nReview.\n\nReads:\n- knowledge/INDEX.md\n')
    (agents / "knowledge/INDEX.md").write_text(
        "# Index\n\n- [a-check](notes/active/a-check.md)\n- [absence](notes/active/absence.md)\n")
    for slug in ("a-check", "absence"):
        (agents / f"knowledge/notes/active/{slug}.md").write_text(NOTE.format(slug=slug))
    (agents / "proposals/README.md").write_text("# Proposals\n")
    (agents / "proposals/RECEIVED.md").write_text(f"# Received\n\n{bundle.RECEIVED_HEADER}\n|---|---|---|\n")
    (agents / "incoming/README.md").write_text("# Incoming\n")
    (agents / "tools/bundle.py").write_text("print('same everywhere')\n")
    bundle.write_carrier(agents, {"carrier": "r-abcdef", "adopted": "2026-01-01", "upstream": "", "adapted": [], "declined": []})
    bundle.write_checksums(agents)
    return agents


# The outbox of 0.0.22 and 0.0.23, as a carrier on those releases holds it: what conversion reads.
OLD_OUTBOX = {
    "tracking/candidates.md": "# Candidates this repository offers\n\n| Candidate | Kind | Lacks | Evidence | First seen |\n|---|---|---|---|---|\n",
    "tracking/experiments.md": "# Experiments run in this repository\n\n| Date | Note | Where | What was run | Result | Verdict |\n|---|---|---|---|---|---|\n",
}


def old_outbox(agents: Path, candidates: list[str] = (), experiments: list[str] = ()) -> None:
    """Writes the outbox of 0.0.23 into a bundle, with the given rows."""
    (agents / "tracking").mkdir(parents=True, exist_ok=True)
    for rel, rows in (("tracking/candidates.md", candidates), ("tracking/experiments.md", experiments)):
        (agents / rel).write_text(OLD_OUTBOX[rel] + "".join(r + "\n" for r in rows))


def a_proposal(agents: Path, evidence: str = "In one repository of this kind, once.", **fields: str) -> Path:
    """One proposal written by the tool, under the fixture's carrier id."""
    values = {"kind": "knowledge", "target": "a-thing", "claim": "A claim with no project noun.", "seen": "2026-01-02",
              "lacks": "a second occurrence", **fields}
    return bundle.write_proposal(agents, bundle.Proposal(evidence=evidence, **values))


class Base(unittest.TestCase):
    def setUp(self) -> None:
        # Resolved, because macOS keeps the temporary folder behind a symlink (`/var` -> `/private/var`).
        self.root = Path(tempfile.mkdtemp()).resolve()
        # No test reads this machine's private terms, carriers or assistant settings: they are not the fixture's.
        environment = mock.patch.dict(os.environ, {"XDG_CONFIG_HOME": str(self.root / "config"),
                                                   "AGENT_GUIDES_USER_SETTINGS": str(self.root / "no-user-settings.json")})
        environment.start()
        self.addCleanup(environment.stop)
        self.addCleanup(shutil.rmtree, self.root)
