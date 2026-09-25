"""The home tool: the build, a release, and carrying it to carriers on the current and the old layout."""

from __future__ import annotations

import contextlib
import io
from pathlib import Path

from meta.tests.support import BOOTSTRAP, CONTEXT, Base, bundle, commit, git, init_repo, release

B = bundle

AREA = """# One area

## By topic

### `t`
A topic.

<!-- generated: cards t -->

## By what you are about to do

<!-- generated: about -->

## How well founded is each note

<!-- generated: founded -->
"""
INDEX = """# Index

| Phase | The question to ask | Notes |
|---|---|---|
| **Plan and design** | What will this touch? | {{notes:plan}} |
| **Review** | What could this remove? | {{notes:review}} |

The checks are in [areas/one.md](areas/one.md).
"""
FULL = """---
slug: "{slug}"
topic: "t"
claim: "The claim of {slug}."
confidence: "reasoned"
phases: [{phases}]
check: "a check for {slug}"
about:
  - {{do: "Do {slug}", wrong_when: "the obvious fails"}}
rests_on: "A paper"
strength: "well established"
our_evidence: "reasoned"
{extra}---

# {slug}

## Why it works

The mechanism.

## When it does NOT apply

{boundary}

## What it costs

Something.

## Where it came from

A repository.

## Literature

A paper, 1970.

## Evidence

Measured once.
"""
BOLD = "- **When the first case holds.** Then no.\n- **When the second case holds**: then no either."
CANDIDATES = """# Candidates

| Candidate | Kind | Lacks | Evidence | First seen | Since |
|---|---|---|---|---|---|
| old-idea — an idea that waited | K | a second occurrence | somewhere | 2026-01-01 | 0.0.1 |
"""
EXPERIMENTS = """# Experiments

## Queued

| Note | Experiment | Cost | Would change |
|---|---|---|---|
| alpha | run it | minutes | the confidence |

## Run

| Date | Note | Where | What was run | Result | Verdict |
|---|---|---|---|---|---|
"""
CARRIERS = "# Carriers\n\n| Carrier | Version | Aligned on |\n|---|---|---|\n"


def full_note(slug: str, phases: str = '"plan"', boundary: str = BOLD, extra: str = "") -> str:
    return FULL.format(slug=slug, phases=phases, boundary=boundary, extra=extra)


def make_home(root: Path) -> Path:
    """A home repository: full notes, templates, records, a bundle built from them, released as 0.0.1."""
    home = init_repo(root / "home")
    agents = home / ".agents"
    for folder in ("method", "knowledge", "tools", "incoming", "tracking"):
        (agents / folder).mkdir(parents=True, exist_ok=True)
    (agents / "README.md").write_text(B.dump_frontmatter({"bundle": "agent-guides", "version": "0.0.0", "released": "2026-01-01"})
                                      + "\n# Guides\n\n## The fields that are this repository's\n\nThey are in carrier.toml.\n\n"
                                        "Reads:\n- knowledge/INDEX.md\n")
    (agents / "CHANGELOG.md").write_text("# Changelog\n\n## [Unreleased]\n\n## [0.0.1] - 2026-01-02\n\n### Added\n\n- The start.\n")
    (agents / "method/prompt-context.md").write_text(CONTEXT)
    (agents / "method/prompt-bootstrap.md").write_text(BOOTSTRAP)
    for session in ("evaluate", "update", "harvest"):
        (agents / f"method/prompt-{session}.md").write_text(f"# {session}\n\nReads:\n- method/prompt-{session}.md\n")
    (agents / "knowledge/README.md").write_text("# Knowledge\n")
    (agents / "incoming/README.md").write_text("# Incoming\n")
    (agents / "tools/bundle.py").write_text("print('the tool')\n")
    B.write_carrier(agents, {"carrier": "r-aaaaaa", "adopted": "2026-01-01", "upstream": "", "adapted": [], "declined": []})
    B.reset_outbox(agents)
    sources = home / "sources"
    (sources / "templates/areas").mkdir(parents=True)
    (sources / "templates/areas/one.md").write_text(AREA)
    (sources / "templates/INDEX.md").write_text(INDEX)
    for state in ("active", "review", "retired"):
        (sources / "notes" / state).mkdir(parents=True)
    (sources / "notes/active/alpha.md").write_text(full_note("alpha", '"plan", "review"'))
    (sources / "notes/active/beta.md").write_text(full_note("beta", boundary="In prose, when it does not hold.",
                                                            extra='boundary: "When it does not hold"\n'))
    (sources / "notes/retired/gone.md").write_text('---\nslug: "gone"\nclaim: "An old claim."\nretired_because: "superseded"\n---\n\n# gone\n')
    (home / "meta/tracking").mkdir(parents=True)
    (home / "meta/tracking/candidates.md").write_text(CANDIDATES)
    (home / "meta/tracking/experiments.md").write_text(EXPERIMENTS)
    (home / "meta/tracking/carriers.md").write_text(CARRIERS)
    (home / "meta/tracking/history.md").write_text("# History\n\n## First\n\nnothing\n")
    (home / "meta/roadmap.md").write_text("# Roadmap\n\nSee [alpha](../sources/notes/active/alpha.md).\n")
    R = release()
    R.release("0.0.1", home)
    commit(home, "release 0.0.1")
    git(home, "tag", "-a", "v0.0.1", "-m", "0.0.1")
    return home


def make_carrier(root: Path, name: str) -> Path:
    repo = init_repo(root / name)
    (repo / ".agents").mkdir()
    commit(repo, "empty")
    return repo


LEGACY_README = """---
bundle:    agent-guides
lineage:   g-aaaaaa/main
ancestry:  [g-aaaaaa]
version:   1
forked_at: null
digest:    "000000000000"
released:  2026-01-01
upstream:  ""
contains:
  method:    m-aaaaaa v1
  knowledge: k-aaaaaa v1
adopted:   "2025-12-01"
carrier:   r-bbbbbb
adapted:                        # local
  - "Spanish in the conversation, English in the repository; technical terms
    stay untranslated"
  - "the gate is one command"
declined:  []
---

# Old guides
"""
LEGACY_METHOD = """---
method:    test
set:       [context]
lineage:   m-aaaaaa/main
version:   1
upstream:  ""
adopted:   "2025-12-01"
adapted:                        # local
  - "Spanish in the conversation, English in the repository; technical terms
    stay untranslated"
  - "the gate is one command"
declined:  []
---

# Old context
"""


def make_legacy(root: Path, name: str) -> Path:
    repo = init_repo(root / name)
    agents = repo / ".agents"
    for folder in ("method", "tracking", "knowledge/notes/active"):
        (agents / folder).mkdir(parents=True)
    (agents / "README.md").write_text(LEGACY_README)
    (agents / "method/prompt-context.md").write_text(LEGACY_METHOD)
    (agents / "method/prompt-sync.md").write_text("# sync\n")
    (agents / "roadmap.md").write_text("# Roadmap\n")
    (agents / "tracking/candidates.md").write_text("| Candidate | Kind | Lacks | Evidence | First seen |\n|---|---|---|---|---|\n"
                                                   "| mine — learned here | K | a second occurrence | here | 2026-01-03 |\n")
    commit(repo, "legacy bundle")
    return repo


class Build(Base):
    def setUp(self) -> None:
        super().setUp()
        self.R = release()
        self.home = make_home(self.root)
        self.agents = self.home / ".agents"

    def test_a_released_home_is_built_verified_and_checked(self) -> None:
        self.assertEqual(self.R.build(self.home, check=True), [])
        self.assertEqual(B.verify_problems(self.agents), [])
        self.assertEqual(B.bundle_version(self.agents), "0.0.1")

    def test_a_shipped_note_is_short_and_carries_its_card(self) -> None:
        text = (self.agents / "knowledge/notes/active/alpha.md").read_text()
        meta, body = B.read_frontmatter(text)

        self.assertEqual(meta["boundary"], "When the first case holds · When the second case holds")
        self.assertEqual(set(meta), {"slug", "topic", "claim", "confidence", "check", "boundary"})
        self.assertIn("## What it costs", body)
        for gone in ("## Where it came from", "## Literature", "## Evidence"):
            self.assertNotIn(gone, body)
        self.assertFalse((self.agents / "knowledge/notes/retired").exists())

    def test_the_tables_come_from_the_notes(self) -> None:
        area = (self.agents / "knowledge/areas/one.md").read_text()
        index = (self.agents / "knowledge/INDEX.md").read_text()

        self.assertIn("| [alpha](../notes/active/alpha.md) | The claim of alpha. | When the first case holds · When the second"
                      " case holds | a check for alpha |", area)
        self.assertIn("| [beta](../notes/active/beta.md) | The claim of beta. | When it does not hold | a check for beta |", area)
        self.assertIn("| Do alpha | [alpha](../notes/active/alpha.md) | the obvious fails |", area)
        self.assertIn("| alpha | A paper — **well established** | reasoned |", area)
        self.assertIn("| **Plan and design** | What will this touch? | [alpha](notes/active/alpha.md) · [beta](notes/active/beta.md) |", index)
        self.assertIn("| **Review** | What could this remove? | [alpha](notes/active/alpha.md) |", index)
        self.assertIn("| alpha | run it | minutes |", (self.agents / "knowledge/OPEN.md").read_text())

    def test_a_hand_edit_and_a_stale_source_are_both_caught(self) -> None:
        generated = self.agents / "knowledge/notes/active/alpha.md"
        generated.write_text(generated.read_text() + "\nhand edit\n")
        self.assertIn("knowledge/notes/active/alpha.md", "\n".join(self.R.build(self.home, check=True)))

        self.R.build(self.home)
        source = self.home / "sources/notes/active/beta.md"
        source.write_text(source.read_text().replace("The claim of beta.", "A new claim."))
        problems = "\n".join(self.R.build(self.home, check=True))
        self.assertIn("knowledge/areas/one.md", problems)
        self.assertIn("knowledge/notes/active/beta.md", problems)

    def test_an_unknown_marker_or_token_is_refused(self) -> None:
        area = self.home / "sources/templates/areas/one.md"
        area.write_text(area.read_text() + "\n<!-- generated: abuot -->\n")
        with self.assertRaisesRegex(self.R.BuildError, "not a marker the build knows"):
            self.R.build(self.home)
        area.write_text(AREA + "\n{{notes: plan}}\n")
        with self.assertRaisesRegex(self.R.BuildError, "not a marker the build knows"):
            self.R.build(self.home)

    def test_a_card_needs_exactly_one_boundary(self) -> None:
        both = self.home / "sources/notes/active/gamma.md"
        both.write_text(full_note("gamma", extra='boundary: "twice"\n'))
        with self.assertRaisesRegex(self.R.BuildError, "both bold lead-ins"):
            self.R.build(self.home)
        both.write_text(full_note("gamma", boundary="Only prose here."))
        with self.assertRaisesRegex(self.R.BuildError, "needs a `boundary:`"):
            self.R.build(self.home)

    def test_a_note_in_review_is_marked_where_it_is_routed(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            changes = self.R.note_state("beta", "review", self.home)

        self.assertIn("rewrote", " ".join(changes)) if "beta" in (self.home / "meta/roadmap.md").read_text() else None
        self.assertIn("[beta](../notes/review/beta.md) ⚠ review", (self.agents / "knowledge/areas/one.md").read_text())
        self.assertEqual(B.verify_problems(self.agents), [])

    def test_note_state_rewrites_the_homes_links(self) -> None:
        self.R.note_state("alpha", "retired", self.home)

        self.assertIn("../sources/notes/retired/alpha.md", (self.home / "meta/roadmap.md").read_text())
        self.assertFalse((self.agents / "knowledge/notes/active/alpha.md").exists())


class Release(Base):
    def test_a_release_must_be_newer_and_described(self) -> None:
        R = release()
        home = make_home(self.root)

        with self.assertRaisesRegex(R.RefusedError, "not newer"):
            R.release("0.0.1", home)
        with self.assertRaisesRegex(R.RefusedError, "no `## \\[0.0.2\\]"):
            R.release("0.0.2", home)
        changelog = home / ".agents/CHANGELOG.md"
        changelog.write_text(changelog.read_text().replace("## [Unreleased]\n", "## [Unreleased]\n\n## [0.0.2] - 2026-02-01\n\n- More.\n"))
        self.assertIn("git tag -a v0.0.2", R.release("0.0.2", home))
        self.assertEqual(B.bundle_version(home / ".agents"), "0.0.2")


class Carry(Base):
    def setUp(self) -> None:
        super().setUp()
        self.R = release()
        self.home = make_home(self.root)

    def splice(self, repo: Path, **kwargs) -> list[str]:  # noqa: ANN003
        return self.R.splice(repo, True, self.root / "backup", root=self.home, **kwargs)

    def test_a_new_carrier_receives_the_release_and_keeps_its_own_files(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, today="2026-01-05")
        (repo / ".agents/evaluation-2026-01-05-abcdef.md").write_text("mine\n")

        self.splice(repo)

        agents = repo / ".agents"
        self.assertEqual(B.checksum_problems(agents), [])
        self.assertEqual(B.read_carrier(agents)["adopted"], "2026-01-05")
        self.assertTrue((agents / "evaluation-2026-01-05-abcdef.md").exists())
        self.assertEqual(B.verify_problems(agents), [])

    def test_an_untagged_home_is_not_carried(self) -> None:
        repo = make_carrier(self.root, "one")
        (self.home / ".agents/method/prompt-context.md").write_text(CONTEXT + "\nunreleased\n")
        self.R.build(self.home)

        with self.assertRaisesRegex(self.R.RefusedError, "not the tagged release"):
            self.splice(repo)

    def test_gather_intake_splice_register_align_round_trip(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo)
        self.splice(repo)
        outbox = repo / ".agents/tracking/candidates.md"
        row = "| new-idea — learned in one | K | a second occurrence | a repository | 2026-01-06 |"
        no = "| weak-idea — did not pass | K | refused: already the default behaviour | a repository | 2026-01-06 |"
        outbox.write_text(outbox.read_text() + row + "\n" + no + "\n")
        commit(repo, "harvest")

        gathered = self.R.gather([repo], self.root / "out", self.home)
        result = self.R.intake(self.root / "out", "0.0.1", self.home)

        self.assertEqual(gathered["carriers"]["one"]["forked"], [])
        self.assertEqual(result["queued"], ["new-idea"])
        self.assertIn("new-idea", (self.home / "meta/tracking/candidates.md").read_text())
        self.assertEqual(result["refused"], ["weak-idea"])
        self.assertNotIn("weak-idea", (self.home / "meta/tracking/candidates.md").read_text())
        self.assertIn("`weak-idea` | refused: already the default behaviour", (self.home / "meta/tracking/history.md").read_text())
        self.splice(repo, taken=result["taken"]["one"])
        self.assertNotIn("new-idea", outbox.read_text())
        self.R.register([repo], "2026-01-07", self.home)
        self.assertEqual(self.R.align([repo], self.home), [])

    def test_a_fork_with_rewritten_checksums_is_still_named_by_gather(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo)
        self.splice(repo)
        note = repo / ".agents/knowledge/notes/active/alpha.md"
        note.write_text(note.read_text() + "\na local edit\n")
        B.write_checksums(repo / ".agents")
        commit(repo, "fork, hidden")

        gathered = self.R.gather([repo], self.root / "out", self.home)

        self.assertIn("knowledge/notes/active/alpha.md: differs from the tagged release", " ".join(gathered["carriers"]["one"]["forked"]))

    def test_intake_keeps_another_occurrence_and_pads_short_rows(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo)
        self.splice(repo)
        outbox = repo / ".agents/tracking/candidates.md"
        outbox.write_text(outbox.read_text() + "| Extends old-idea — seen again here | K | nothing | a second repository | 2026-01-08 |\n"
                          "| short | K |\n")
        commit(repo, "harvest")
        self.R.gather([repo], self.root / "out", self.home)

        result = self.R.intake(self.root / "out", "0.0.1", self.home)

        queue = (self.home / "meta/tracking/candidates.md").read_text()
        self.assertEqual(result["queued"], ["short"])
        self.assertIn("| short | K |  |  |  | 0.0.1 |", queue)
        self.assertIn("## Offered again, to merge", queue)
        self.assertIn("Extends old-idea — seen again here", queue.split("## Offered again")[1])

    def test_a_forked_carrier_is_named_by_gather(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo)
        self.splice(repo)
        note = repo / ".agents/knowledge/notes/active/alpha.md"
        note.write_text(note.read_text() + "\na local edit\n")
        commit(repo, "fork")

        gathered = self.R.gather([repo], self.root / "out", self.home)

        self.assertIn("knowledge/notes/active/alpha.md", " ".join(gathered["carriers"]["one"]["forked"]))

    def test_a_carrier_on_the_old_layout_is_converted_and_keeps_its_own_fields(self) -> None:
        repo = make_legacy(self.root, "old")

        actions = self.splice(repo)

        agents = repo / ".agents"
        own = B.read_carrier(agents)
        self.assertEqual(own["carrier"], "r-bbbbbb")
        self.assertEqual(own["adopted"], "2025-12-01")
        self.assertEqual(own["adapted"], ["Spanish in the conversation, English in the repository; technical terms stay untranslated",
                                          "the gate is one command"])
        self.assertEqual(own["harvested_through"], "2026-01-03")
        self.assertFalse((agents / "roadmap.md").exists())
        self.assertFalse((agents / "method/prompt-sync.md").exists())
        self.assertIn("remove roadmap.md", actions)
        self.assertEqual(B.verify_problems(agents), [])

    def test_old_headers_that_disagree_are_refused(self) -> None:
        repo = make_legacy(self.root, "old")
        context = repo / ".agents/method/prompt-context.md"
        context.write_text(context.read_text().replace('"the gate is one command"', '"another gate"'))

        with self.assertRaisesRegex(self.R.RefusedError, "disagree"):
            self.R.legacy_own_fields(repo / ".agents")

    def test_a_carrier_outside_the_workspace_is_not_written(self) -> None:
        inside, outside = make_carrier(self.root, "inside"), make_carrier(self.root, "outside")

        with self.assertRaises(B.OutsideWorkspaceError):
            self.splice(outside, scope=[inside])


class Funnel(Base):
    def test_a_candidate_is_due_after_three_releases_and_discarded_into_history(self) -> None:
        R = release()
        home = make_home(self.root)
        for n in (2, 3, 4):
            changelog = home / ".agents/CHANGELOG.md"
            changelog.write_text(changelog.read_text().replace("## [Unreleased]\n", f"## [Unreleased]\n\n## [0.0.{n}] - 2026-02-0{n}\n\n- More.\n"))
            R.release(f"0.0.{n}", home)
            commit(home, f"release 0.0.{n}")
            git(home, "tag", "-a", f"v0.0.{n}", "-m", f"0.0.{n}")
            self.assertEqual(R.funnel(home)["discard_due"], [] if n < 4 else ["old-idea"])

        queue = home / "meta/tracking/candidates.md"
        queue.write_text(queue.read_text().rstrip("\n") + "\n| old-idea — the same slug, newer | K | a number | here | 2026-02-04 | 0.0.4 |\n")
        self.assertEqual(R.triage(apply=True, root=home), ["old-idea"])
        self.assertIn("the same slug, newer", queue.read_text())
        self.assertNotIn("an idea that waited", (home / "meta/tracking/candidates.md").read_text())
        self.assertIn("`old-idea`", (home / "meta/tracking/history.md").read_text())
