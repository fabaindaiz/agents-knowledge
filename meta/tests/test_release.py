"""The home tool: the build, a release, and carrying it to carriers on the current and the old layout."""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
from unittest import mock

from meta.tests.support import BOOTSTRAP, CONTEXT, README, Base, a_proposal, bundle, commit, git, init_repo, old_outbox, release

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

## Notes that share a principle

<!-- generated: principles -->
"""
INDEX = """# Index

| Phase | The question to ask | Notes |
|---|---|---|
| **Plan and design** | What will this touch? | {{notes:plan}} |
| **Review** | What could this remove? | {{notes:review}} |

<!-- generated: about -->

The checks are in the cards.
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
    agents.mkdir(parents=True)
    # The hand-written files of the bundle are originals; the build writes their release copies.
    original = home / "sources/bundle"
    for folder in ("method", "knowledge", "tools", "incoming", "proposals"):
        (original / folder).mkdir(parents=True, exist_ok=True)
    (original / "README.md").write_text(B.dump_frontmatter({"bundle": "agent-guides", "home": "r-aaaaaa", "version": "0.0.0", "released": "2026-01-01"})
                                      + "\n# Guides\n\n## The fields that are this repository's\n\nThey are in carrier.toml.\n\n"
                                        "Reads:\n- knowledge/INDEX.md\n")
    (original / "CHANGELOG.md").write_text("# Changelog\n\n## [Unreleased]\n\n## [0.0.1] - 2026-01-02\n\n### Added\n\n- The start.\n")
    (original / "method/prompt-context.md").write_text(CONTEXT)
    (original / "method/prompt-bootstrap.md").write_text(BOOTSTRAP)
    for session in ("evaluate", "update", "harvest"):
        (original / f"method/prompt-{session}.md").write_text(f"# {session}\n\nReads:\n- method/prompt-{session}.md\n")
    (original / "knowledge/README.md").write_text("# Knowledge\n")
    (original / "incoming/README.md").write_text("# Incoming\n")
    (original / "proposals/README.md").write_text("# Proposals\n")
    (original / "tools/bundle.py").write_text("print('the tool')\n")
    B.write_carrier(agents, {"carrier": "r-aaaaaa", "adopted": "2026-01-01", "upstream": "", "adapted": [], "declined": []})
    sources = home / "sources"
    (sources / "templates/areas").mkdir(parents=True)
    (sources / "templates/areas/one.md").write_text(AREA)
    (sources / "templates/INDEX.md").write_text(INDEX)
    (sources / "templates/knowledge-reviewer.md").write_text(
        '---\nname: "knowledge-reviewer"\ndescription: "Reviews against {{topics}}."\ntools: "Read"\n---\n\nReview.\n\nReads:\n- knowledge/INDEX.md\n')
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
upstream:  "r-aaaaaa"
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
upstream:  "r-aaaaaa"
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
        index = (self.agents / "knowledge/INDEX.md").read_text()

        # The area pages are not shipped since 0.0.30; the index routes to the cards, which carry each note.
        self.assertFalse((self.agents / "knowledge/areas").exists())
        self.assertEqual(B.verify_problems(self.agents), [])
        # The phase table names each note by slug; its one link to the card is in the *about to do* table,
        # so the index the reviewer loads whole does not repeat a link per phase.
        self.assertIn("| **Plan and design** | What will this touch? | `alpha` · `beta` |", index)
        self.assertIn("| **Review** | What could this remove? | `alpha` |", index)
        self.assertIn("| Do alpha | [alpha](cards/alpha.md) | the obvious fails |", index)
        self.assertEqual(index.count("](cards/alpha.md)"), 1)
        card = (self.agents / "knowledge/cards/alpha.md").read_text()
        self.assertIn("**Not when.** When the first case holds · When the second case holds", card)
        self.assertIn("(../notes/active/alpha.md)", card)
        self.assertLess(len(card), 1200)
        self.assertIn("| alpha | run it | minutes |", (self.agents / "knowledge/OPEN.md").read_text())

    def test_a_hand_edit_and_a_stale_source_are_both_caught(self) -> None:
        generated = self.agents / "knowledge/notes/active/alpha.md"
        generated.write_text(generated.read_text() + "\nhand edit\n")
        self.assertIn("knowledge/notes/active/alpha.md", "\n".join(self.R.build(self.home, check=True)))

        self.R.build(self.home)
        source = self.home / "sources/notes/active/beta.md"
        source.write_text(source.read_text().replace("The claim of beta.", "A new claim."))
        problems = "\n".join(self.R.build(self.home, check=True))
        self.assertIn("knowledge/cards/beta.md", problems)
        self.assertIn("knowledge/notes/active/beta.md", problems)

    def test_an_unknown_marker_or_token_is_refused(self) -> None:
        area = self.home / "sources/templates/areas/one.md"
        area.write_text(area.read_text() + "\n<!-- generated: abuot -->\n")
        with self.assertRaisesRegex(self.R.BuildError, "not a marker the build knows"):
            self.R.build(self.home)
        for bad in ("\n<!-- GENERATED: cards x -->\n", "\n{{notes:plan}}\n", "\n  <!-- generated: about -->\n"):
            area.write_text(AREA + bad)
            with self.assertRaisesRegex(self.R.BuildError, "not a marker the build knows"):
                self.R.build(self.home)
        area.write_text(AREA + "\n{{notes: plan}}\n")
        with self.assertRaisesRegex(self.R.BuildError, "not a marker the build knows"):
            self.R.build(self.home)

    def test_every_release_file_is_marked_and_no_original_is(self) -> None:
        self.assertIn(self.R.RELEASE_MARK, (self.agents / "method/prompt-context.md").read_text())
        self.assertNotIn(self.R.RELEASE_MARK, (self.home / "sources/bundle/method/prompt-context.md").read_text())
        for rel in ("README.md", "method/prompt-context.md", "tools/bundle.py"):
            original = (self.home / "sources/bundle" / rel).read_text()
            self.assertEqual(self.R.without_banner(rel, (self.agents / rel).read_text()), original)

        (self.agents / "method/prompt-context.md").write_text(CONTEXT)
        self.assertIn("method/prompt-context.md", "\n".join(self.R.build(self.home, check=True)))
        self.R.build(self.home)
        marked = self.home / "sources/notes/active/alpha.md"
        marked.write_text("<!-- " + self.R.RELEASE_MARK + " by mistake -->\n" + marked.read_text())
        self.assertIn("an original that carries the release banner", "\n".join(self.R.form_problems(self.home)))

    def test_a_hand_written_file_in_the_release_is_stale(self) -> None:
        (self.agents / "method/prompt-extra.md").write_text("# written in the release by hand\n")

        self.assertIn("method/prompt-extra.md: generated by nothing", "\n".join(self.R.build(self.home, check=True)))

    def test_a_principle_names_its_notes_and_needs_two(self) -> None:
        for slug in ("alpha", "beta"):
            path = self.home / f"sources/notes/active/{slug}.md"
            path.write_text(path.read_text().replace('confidence: "reasoned"', 'confidence: "reasoned"\nprinciple: "one-idea"', 1))
        self.R.build(self.home)

        self.assertIn("with [beta](beta.md)", (self.agents / "knowledge/cards/alpha.md").read_text())
        path = self.home / "sources/notes/active/beta.md"
        path.write_text(path.read_text().replace('principle: "one-idea"\n', ""))
        with self.assertRaisesRegex(self.R.BuildError, "carried by one note only"):
            self.R.build(self.home)

    def test_a_principle_that_is_not_a_name_is_refused_not_a_crash(self) -> None:
        path = self.home / "sources/notes/active/alpha.md"
        path.write_text(path.read_text().replace('confidence: "reasoned"', 'confidence: "reasoned"\nprinciple: ["a", "b"]', 1))

        with self.assertRaisesRegex(self.R.BuildError, "kebab-case"):
            self.R.build(self.home)

    def test_a_principle_shared_across_areas_is_listed_whole_in_each(self) -> None:
        (self.home / "sources/templates/areas/two.md").write_text(AREA.replace("One area", "Two area").replace("`t`", "`u`")
                                                                  .replace("cards t", "cards u"))
        for slug, topic in (("alpha", "t"), ("gamma", "u")):
            path = self.home / f"sources/notes/active/{slug}.md"
            if not path.exists():
                path.write_text(full_note(slug).replace('topic: "t"', f'topic: "{topic}"'))
            path.write_text(path.read_text().replace('confidence: "reasoned"', 'confidence: "reasoned"\nprinciple: "cross"', 1))
        self.R.build(self.home)

        self.assertIn("[gamma](gamma.md)", (self.agents / "knowledge/cards/alpha.md").read_text())
        self.assertIn("[alpha](alpha.md)", (self.agents / "knowledge/cards/gamma.md").read_text())

    def test_a_release_file_with_other_line_endings_is_not_up_to_date(self) -> None:
        path = self.agents / "method/prompt-update.md"
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        release().write_checksums(self.agents)

        self.assertIn("method/prompt-update.md", "\n".join(self.R.build(self.home, check=True)))
        self.R.build(self.home)
        self.assertNotIn(b"\r\n", path.read_bytes())

    def test_a_method_skill_that_names_a_model_is_refused(self) -> None:
        # switching the model for a turn misses the whole prompt cache (the cache-safety rule, 0.0.30)
        skill = self.home / "sources/bundle/method/skills/fast/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text('---\nname: "fast"\ndescription: "A skill."\nmodel: "haiku"\n---\n\nBody.\n')
        with self.assertRaisesRegex(self.R.BuildError, "names a model"):
            self.R.build(self.home)

    def test_the_reviewer_definition_needs_its_frontmatter(self) -> None:
        template = self.home / "sources/templates/knowledge-reviewer.md"
        good = template.read_text()
        for bad, error in ((good.split("---\n", 2)[2], "opens with its frontmatter"),
                           (good.replace("tools: \"Read\"\n", ""), "lacks tools"),
                           (good.replace('"Reviews against', '"Reviews "only" against'), "after a value")):
            template.write_text(bad)
            with self.assertRaisesRegex(self.R.BuildError, error):
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
        self.assertIn("(../notes/review/beta.md)", (self.agents / "knowledge/cards/beta.md").read_text())
        self.assertEqual(B.verify_problems(self.agents), [])

    def test_a_refused_note_state_leaves_nothing_half_done(self) -> None:
        roadmap = (self.home / "meta/roadmap.md").read_text()
        with mock.patch.object(self.R, "build", side_effect=self.R.BuildError("a principle refuses it")), \
                self.assertRaises(self.R.BuildError):
            self.R.note_state("alpha", "retired", self.home)
        self.assertTrue((self.home / "sources/notes/active/alpha.md").is_file())
        self.assertFalse((self.home / "sources/notes/retired/alpha.md").exists())
        self.assertEqual((self.home / "meta/roadmap.md").read_text(), roadmap)

    def test_note_state_rewrites_the_homes_links(self) -> None:
        self.R.note_state("alpha", "retired", self.home)

        self.assertIn("../sources/notes/retired/alpha.md", (self.home / "meta/roadmap.md").read_text())
        self.assertFalse((self.agents / "knowledge/notes/active/alpha.md").exists())


class Release(Base):
    def test_the_cut_refuses_over_the_export_cap_and_writes_nothing(self) -> None:
        R = release()
        home = make_home(self.root)
        changelog = home / "sources/bundle/CHANGELOG.md"
        changelog.write_text(changelog.read_text().replace("## [Unreleased]\n", "## [Unreleased]\n\n## [0.0.2] - 2026-02-01\n\n- More.\n"))
        before = git(home, "status", "--porcelain")
        with mock.patch.object(R, "EXPORT_CAP", 10):
            with self.assertRaisesRegex(R.RefusedError, r"the export ships \d+ bytes, over the manifest's cap of 10"):
                R.release("0.0.2", home)
        self.assertEqual(git(home, "status", "--porcelain"), before)
        self.assertEqual(B.bundle_version(home / ".agents"), "0.0.1")
        self.assertIsNone(R.export_over_cap(home, export_cap=10_000_000))
        self.assertIn("git tag -a v0.0.2", R.release("0.0.2", home))
    def test_a_release_names_its_home_and_parent_and_the_home_keeps_its_lineage(self) -> None:
        R = release()
        home = make_home(self.root)
        changelog = home / "sources/bundle/CHANGELOG.md"
        changelog.write_text(changelog.read_text().replace("## [Unreleased]\n", "## [Unreleased]\n\n## [0.0.2] - 2026-02-01\n\n- More.\n"))
        R.release("0.0.2", home)
        for readme in (home / "sources/bundle/README.md", home / ".agents/README.md"):
            front = B.read_frontmatter(readme.read_text())[0]
            self.assertEqual((front["home"], front["parent"], front["version"]), ("r-aaaaaa", "v0.0.1", "0.0.2"))
        self.assertEqual(B.read_carrier(home / ".agents")["lineage"], ["0.0.1 r-aaaaaa 2026-01-02", "0.0.2 r-aaaaaa 2026-02-01"])
        self.assertEqual(R.build(home, check=True), [])
        R.build(home)
        self.assertEqual(B.read_carrier(home / ".agents")["lineage"], ["0.0.1 r-aaaaaa 2026-01-02", "0.0.2 r-aaaaaa 2026-02-01"])

    def test_a_release_must_be_newer_and_described(self) -> None:
        R = release()
        home = make_home(self.root)

        with self.assertRaisesRegex(R.RefusedError, "not newer"):
            R.release("0.0.1", home)
        with self.assertRaisesRegex(R.RefusedError, "no `## \\[0.0.2\\]"):
            R.release("0.0.2", home)
        changelog = home / "sources/bundle/CHANGELOG.md"
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
        B.mint_carrier_id(repo, today="2026-01-05", upstream="r-aaaaaa")
        (repo / ".agents/evaluation-2026-01-05-abcdef.md").write_text("mine\n")

        self.splice(repo)

        agents = repo / ".agents"
        self.assertEqual(B.checksum_problems(agents), [])
        self.assertEqual(B.read_carrier(agents)["adopted"], "2026-01-05")
        self.assertTrue((agents / "evaluation-2026-01-05-abcdef.md").exists())
        self.assertEqual(B.verify_problems(agents), [])

    def test_a_backup_on_or_above_the_carrier_is_refused_and_nothing_is_lost(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, today="2026-01-05", upstream="r-aaaaaa")
        proposal = a_proposal(repo / ".agents")
        for backup in (repo.parent, repo / ".agents", repo):
            with self.assertRaisesRegex(self.R.RefusedError, "backup"):
                self.R.splice(repo, True, backup, root=self.home)
            self.assertTrue(proposal.is_file(), backup)

    def test_an_existing_backup_is_never_overwritten(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, today="2026-01-05", upstream="r-aaaaaa")
        kept = self.root / "backup/one/.agents/kept.md"
        kept.parent.mkdir(parents=True)
        kept.write_text("the only clean copy\n")
        actions = self.splice(repo)
        self.assertIn(f"back up into {(self.root / 'backup/one.2/.agents').resolve()}", actions)
        self.assertIn("one.2", " ".join(self.R.splice_report("one", actions, True, self.root / "backup")))
        self.assertEqual(kept.read_text(), "the only clean copy\n")
        self.assertTrue((self.root / "backup/one.2/.agents/carrier.toml").is_file())

    def test_a_hidden_file_inside_the_bundle_is_named_removed_and_kept_in_the_backup(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, today="2026-01-05", upstream="r-aaaaaa")
        (repo / ".agents/.notes").write_text("mine\n")
        commit(repo, "a hidden note")
        self.assertIn("remove .notes", self.R.splice(repo, False, None, root=self.home))
        self.splice(repo)
        self.assertEqual((self.root / "backup/one/.agents/.notes").read_text(), "mine\n")
        self.assertEqual(B.verify_problems(repo / ".agents"), [])

    def test_an_untagged_home_is_not_carried(self) -> None:
        repo = make_carrier(self.root, "one")
        (self.home / "sources/bundle/method/prompt-context.md").write_text(CONTEXT + "\nunreleased\n")
        self.R.build(self.home)

        with self.assertRaisesRegex(self.R.RefusedError, "not the tagged release"):
            self.splice(repo)

    def release_again(self, version: str) -> None:
        changelog = self.home / "sources/bundle/CHANGELOG.md"
        changelog.write_text(changelog.read_text().replace("## [Unreleased]\n", f"## [Unreleased]\n\n## [{version}] - 2026-01-09\n\n### Added\n\n- More.\n"))
        self.R.release(version, self.home)
        commit(self.home, f"release {version}")
        git(self.home, "tag", "-a", f"v{version}", "-m", version)

    def test_gather_intake_splice_register_align_round_trip(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        agents = repo / ".agents"
        new = a_proposal(agents, "Seen in a repository of this kind.", target="new-idea")
        weak = a_proposal(agents, "Seen once.", target="weak-idea", lacks="refused: already the default behaviour")
        commit(repo, "harvest")

        gathered = self.R.gather([repo], self.root / "out", self.home)
        result = self.R.intake(self.root / "out", "0.0.2", self.home)

        self.assertEqual(gathered["carriers"]["one"]["forked"], [])
        self.assertEqual(result["queued"], ["new-idea"])
        self.assertEqual(sorted(result["received"]), sorted([new.stem, weak.stem]))
        self.assertIn("new-idea — A claim with no project noun.", (self.home / "meta/tracking/candidates.md").read_text())
        self.assertEqual(result["refused"], ["weak-idea"])
        self.assertNotIn("weak-idea", (self.home / "meta/tracking/candidates.md").read_text())
        self.assertIn("`weak-idea` | refused: already the default behaviour", (self.home / "meta/tracking/history.md").read_text())
        ledger = (self.home / "meta/tracking/received.md").read_text()
        self.assertIn(f"| `{new.stem}` | 0.0.2 | queued as `new-idea` |", ledger)
        self.assertNotIn(B.stored_carrier_id(repo), ledger)
        self.assertEqual(self.R.intake(self.root / "out", "0.0.2", self.home)["skipped"], 2)
        self.release_again("0.0.2")
        self.splice(repo)
        self.assertTrue(new.exists() and weak.exists())
        self.assertEqual({pid for pid, _ in B.prune_proposals(agents)}, {new.stem, weak.stem})
        self.assertEqual(list((agents / "proposals").glob("p-*.md")), [])
        commit(repo, "prune")
        self.R.register([repo], "2026-01-10", self.home)
        self.assertEqual(self.R.align([repo], self.home), [])
        # work built in the home after the release does not unalign a carrier that equals its tag
        (self.home / ".agents/method/prompt-update.md").write_text("built after the release\n")
        release().write_checksums(self.home / ".agents")
        self.assertEqual(self.R.align([repo], self.home), [])

    def test_a_worktree_is_remembered_as_its_repository(self) -> None:
        import tomllib

        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        commit(repo, "bundle")
        tree = self.root / "scratch-worktree"
        git(repo, "worktree", "add", "-q", str(tree), "-b", "elsewhere")
        manifest = self.root / "config/agent-guides/carriers.toml"
        manifest.parent.mkdir(parents=True)

        self.R.register([tree], "2026-01-07", self.home, manifest=manifest)

        data = tomllib.loads(manifest.read_text())
        self.assertEqual(data["carriers"], [str(repo.resolve())])
        self.assertEqual([r["path"] for r in data["carrier"]], [str(repo.resolve())])
        self.assertEqual(data["carrier"][0]["name"], "one")

    def test_register_remembers_names_and_paths_only_in_the_local_manifest(self) -> None:
        import tomllib

        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        manifest = self.root / "config/agent-guides/carriers.toml"
        manifest.parent.mkdir(parents=True)
        other = str(self.root / "elsewhere")
        manifest.write_text(f'carriers = ["{other}"]\n')
        registry = (self.home / "meta/tracking/carriers.md")

        self.R.register([repo], "2026-01-07", self.home, manifest=manifest)

        data = tomllib.loads(manifest.read_text())
        self.assertEqual(data["carriers"], [other, str(repo)])
        self.assertEqual([(r["name"], r["version"], r["seen"]) for r in data["carrier"]], [("one", "0.0.1", "2026-01-07")])
        self.assertEqual(data["carrier"][0]["carrier"], B.stored_carrier_id(repo))
        self.assertNotIn(str(repo), registry.read_text())
        self.assertNotIn("| one |", registry.read_text())

    def test_carriers_names_a_bootstrap_with_no_carrier_file_and_records_no_empty_id(self) -> None:
        import tomllib

        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        paused = make_carrier(self.root, "paused")  # started from the template: a release, no carrier.toml yet
        (paused / ".agents/README.md").write_text(README.format(version="0.0.1"))
        manifest = self.root / "config/agent-guides/carriers.toml"
        manifest.parent.mkdir(parents=True)
        manifest.write_text(f'carriers = ["{repo}", "{paused}"]\n')
        out = io.StringIO()

        with mock.patch.object(B, "MANIFEST", manifest), contextlib.redirect_stdout(out):
            code = self.R.main(["carriers"])

        self.assertEqual(code, 0, out.getvalue())
        self.assertIn("paused: not a carrier yet (no carrier.toml)", out.getvalue())
        data = tomllib.loads(manifest.read_text())
        self.assertEqual([r["name"] for r in data["carrier"]], ["one"])
        self.assertEqual(data["carriers"], [str(repo), str(paused)])

    def test_the_local_manifest_is_never_written_inside_a_repository(self) -> None:
        with self.assertRaisesRegex(self.R.RefusedError, "outside every one"):
            self.R.remember([], self.home / "meta/carriers.toml")

    def test_a_fork_with_rewritten_checksums_is_still_named_by_gather(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        note = repo / ".agents/knowledge/notes/active/alpha.md"
        note.write_text(note.read_text() + "\na local edit\n")
        release().write_checksums(repo / ".agents")
        commit(repo, "fork, hidden")

        gathered = self.R.gather([repo], self.root / "out", self.home)

        self.assertIn("knowledge/notes/active/alpha.md: differs from the tagged release", " ".join(gathered["carriers"]["one"]["forked"]))

    def test_a_nearby_privacy_warning_is_listed_but_holds_no_proposal_back(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        rid, noun = "r-" + "4c1d2e", "pay" + "roll service"
        a_proposal(repo / ".agents", f"The findings of {rid} came from\nthe {noun}, generalised.", target="nearby-one")
        commit(repo, "harvest")
        self.R.gather([repo], self.root / "out", self.home)
        result = self.R.intake(self.root / "out", "0.0.2", self.home)
        self.assertEqual(result["queued"], ["nearby-one"])
        self.assertEqual(result["privacy"], [])
        self.assertIn("id-beside-domain-nearby", " ".join(result["privacy_listed"]))
        ran = subprocess.run([sys.executable, str(Path(__file__).resolve().parents[2] / "sources/bundle/tools/bundle.py"), "privacy", "--paths",
                              *map(str, (repo / ".agents/proposals").glob("p-*.md"))], cwd=repo, capture_output=True, text=True)
        code, out = ran.returncode, ran.stdout + ran.stderr
        self.assertEqual(code, 0, out)
        self.assertIn("id-beside-domain-nearby", out)

    def test_a_topic_on_a_note_is_another_occurrence_of_that_note(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        note = next(p.stem for p in (self.home / "sources/notes").rglob("*.md"))
        a_proposal(repo / ".agents", "Seen again here.", target=note, topic="a-corner", action="extends")
        commit(repo, "harvest")
        self.R.gather([repo], self.root / "out", self.home)
        result = self.R.intake(self.root / "out", "0.0.2", self.home)
        self.assertEqual(result["queued"], [])
        self.assertIn(note, " ".join(result["duplicates"]))

    def test_an_intake_that_fails_before_writing_leaves_no_marker(self) -> None:
        (self.root / "out").mkdir()
        (self.root / "out/gather.json").write_text('{"packs": {}}')
        with self.assertRaises(Exception):
            self.R.intake(self.root / "out", "0.0.2", self.home)
        self.assertFalse((self.home / self.R.INTAKE_MARKER).exists())

    def test_a_frontier_reads_as_toml_whatever_its_quotes(self) -> None:
        for text in ('harvested_through = "2026-11-24"\n', "harvested_through = '2026-11-24'\n", 'harvested_through="2026-11-24" # c\n'):
            self.assertEqual(self.R._frontier(text), "2026-11-24", text)
        self.assertEqual(self.R._frontier("not toml = = \n"), "")

    def test_an_interrupted_intake_is_never_run_again_over_its_half_written_records(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        a_proposal(repo / ".agents", "Seen once.", target="new-idea")
        commit(repo, "harvest")
        self.R.gather([repo], self.root / "out", self.home)
        real = self.R._insert_rows
        calls = []

        def interrupted(path, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003
            calls.append(path)
            if path.name == "experiments.md":
                raise KeyboardInterrupt
            return real(path, *args, **kwargs)
        with mock.patch.object(self.R, "_insert_rows", interrupted), self.assertRaises(KeyboardInterrupt):
            self.R.intake(self.root / "out", "0.0.2", self.home)
        with self.assertRaisesRegex(self.R.RefusedError, "interrupted"):
            self.R.intake(self.root / "out", "0.0.2", self.home)
        self.assertEqual((self.home / "meta/tracking/candidates.md").read_text().count("new-idea —"), 1)

    def test_intake_keeps_another_occurrence_and_refuses_what_does_not_read_whole(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        agents = repo / ".agents"
        a_proposal(agents, "A second repository.", target="old-idea", action="extends", claim="Seen again here.", lacks="nothing")
        edited = a_proposal(agents, "Seen once.", target="edited-idea")
        edited.write_text(edited.read_text().replace("Seen once.", "Seen twice."))
        old_outbox(agents, ["| short | K |"])
        commit(repo, "harvest")
        gathered = self.R.gather([repo], self.root / "out", self.home)

        result = self.R.intake(self.root / "out", "0.0.1", self.home)

        queue = (self.home / "meta/tracking/candidates.md").read_text()
        self.assertIn("edited after it was written", " ".join(gathered["carriers"]["one"]["problems"]))
        self.assertIn("edited after it was written", " ".join(result["malformed"]))
        self.assertEqual(result["queued"], ["short"])
        self.assertIn("| short — short | K | not given in the row | (the row gives no evidence) (First seen: not given)", queue)
        self.assertEqual(len(result["received"]), 2)
        self.assertIn("## Offered again, to merge", queue)
        self.assertIn("extends old-idea — Seen again here.", queue.split("## Offered again")[1])

    def test_intake_groups_by_target_and_topic_and_a_pack_carries_the_topic(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        agents = repo / ".agents"
        a_proposal(agents, "A second repository.", target="old-idea", action="extends", claim="Seen again here.", lacks="nothing")
        a_proposal(agents, "Seen once.", target="a-method-file", topic="first-gate", action="extends", claim="A first topic.")
        commit(repo, "harvest")
        other = make_carrier(self.root, "two")
        B.mint_carrier_id(other, upstream="r-aaaaaa")
        self.splice(other)
        a_proposal(other / ".agents", "Seen once.", target="a-method-file", topic="second-gate", action="extends", claim="A second topic.")
        pack = self.root / "pack.tar"
        B.pack_proposals(other / ".agents", pack)

        self.R.gather([repo], self.root / "out", self.home, packs=[pack])
        result = self.R.intake(self.root / "out", "0.0.1", self.home)

        queue = (self.home / "meta/tracking/candidates.md").read_text()
        self.assertEqual(result["queued"], ["a-method-file/first-gate", "a-method-file/second-gate"])
        self.assertEqual(len(result["received"]), 3)
        self.assertIn("extends old-idea — Seen again here.", queue.split("## Offered again")[1])
        self.assertIn("extends a-method-file/first-gate — A first topic.", queue.split("## Offered again")[0])
        self.assertIn("extends a-method-file/second-gate — A second topic.", queue.split("## Offered again")[0])
        self.assertEqual(self.R.slug_of("extends a-method-file/first-gate — A first topic."), "a-method-file/first-gate")

    def test_gather_names_and_intake_refuses_a_proposal_that_fails_privacy_or_warns_unanswered(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        agents = repo / ".agents"
        count = "about " + "4," + "812" + " rows a day"
        a_proposal(agents, "In one repository of this kind, once.", target="clean-idea")
        a_proposal(agents, "Write to " + "jdoe" + "@" + "corp-mail.io" + " for it.", target="leaky-idea")
        a_proposal(agents, f"It handled {count}.", target="unanswered-idea")
        a_proposal(agents, f"It handled {count}. " + "privacy" + "-allow: a generic order of magnitude, the owner said so",
                   target="answered-idea")
        commit(repo, "harvest")

        gathered = self.R.gather([repo], self.root / "out", self.home)
        result = self.R.intake(self.root / "out", "0.0.1", self.home)

        named = " ".join(gathered["carriers"]["one"]["privacy"])
        self.assertIn("FAIL email", named)
        self.assertIn("WARN exact-count", named)
        self.assertIn("privacy", (self.root / "out/gather.md").read_text())
        queue = (self.home / "meta/tracking/candidates.md").read_text()
        self.assertIn("clean-idea", queue)
        self.assertIn("answered-idea", queue)
        self.assertNotIn("leaky-idea", queue)
        self.assertNotIn("unanswered-idea", queue)
        self.assertEqual(len(result["received"]), 2)
        self.assertEqual(len(result["privacy"]), 2, result["privacy"])

    def test_the_home_gathered_as_a_carrier_is_read_for_its_proposals_only(self) -> None:
        a_proposal(self.home / ".agents", "Seen in the home.", target="home-idea")
        (self.home / "sources/bundle/method/prompt-context.md").write_text(CONTEXT + "\nbeing written\n")
        self.R.build(self.home)

        gathered = self.R.gather([self.home], self.root / "out", self.home)

        self.assertEqual(gathered["carriers"]["home"]["forked"], [])
        self.assertEqual([p["target"] for p in gathered["carriers"]["home"]["proposals"]], ["home-idea"])

    def test_a_forked_carrier_is_named_by_gather(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        note = repo / ".agents/knowledge/notes/active/alpha.md"
        note.write_text(note.read_text() + "\na local edit\n")
        commit(repo, "fork")

        gathered = self.R.gather([repo], self.root / "out", self.home)

        self.assertIn("knowledge/notes/active/alpha.md", " ".join(gathered["carriers"]["one"]["forked"]))

    def test_an_old_outbox_becomes_proposals_with_the_ids_gather_gave_them(self) -> None:
        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        old_outbox(repo / ".agents", ["| kept-idea — never gathered | K | nothing | a repository | 2026-01-06 |"])
        commit(repo, "harvest on 0.0.23")
        gathered = self.R.gather([repo], self.root / "out", self.home)
        offered = [p["id"] for p in gathered["carriers"]["one"]["proposals"]]

        actions = self.splice(repo)

        agents = repo / ".agents"
        self.assertIn("convert 1 outbox rows into proposals/", actions)
        self.assertFalse((agents / "tracking").exists())
        self.assertEqual([p.stem for p in (agents / "proposals").glob("p-*.md")], offered)
        self.assertEqual(B.verify_problems(agents), [])

    def test_a_bundle_on_a_branch_not_checked_out_is_found(self) -> None:
        repo = init_repo(self.root / "two")
        commit(repo, "start")
        start = git(repo, "branch", "--show-current").strip()
        git(repo, "switch", "-q", "-c", "agents")
        (repo / ".agents").mkdir()
        (repo / ".agents/README.md").write_text(B.dump_frontmatter({"bundle": "agent-guides", "version": "0.0.3"}) + "\n# Guides\n")
        commit(repo, "the bundle")
        git(repo, "switch", "-q", start)

        self.assertFalse((repo / ".agents").exists())
        self.assertEqual(self.R.bundle_branches(repo), [("agents", "0.0.3")])

    def a_carrier_whose_bundle_is_on_a_branch(self, name: str) -> Path:
        repo = init_repo(self.root / name)
        commit(repo, "start")
        start = git(repo, "branch", "--show-current").strip()
        git(repo, "switch", "-q", "-c", "agents")
        (repo / ".agents").mkdir()
        (repo / ".agents/README.md").write_text(B.dump_frontmatter({"bundle": "agent-guides", "version": "0.0.3"}) + "\n# Guides\n")
        commit(repo, "the bundle")
        git(repo, "switch", "-q", start)
        return repo

    def test_align_reports_it_not_aligned_with_its_branches(self) -> None:
        one = make_carrier(self.root, "one")
        B.mint_carrier_id(one, upstream="r-aaaaaa")
        self.splice(one)
        commit(one, "bundle")
        two = self.a_carrier_whose_bundle_is_on_a_branch("two")

        problems = self.R.align([one], self.home, missing=(two,))

        self.assertIn("two: no bundle on disk; a bundle on agents (0.0.3)", problems)
        self.assertTrue(any(p.startswith("one: ") for p in problems))

    def test_gather_says_not_read(self) -> None:
        one = make_carrier(self.root, "one")
        B.mint_carrier_id(one, upstream="r-aaaaaa")
        self.splice(one)
        commit(one, "bundle")
        two = self.a_carrier_whose_bundle_is_on_a_branch("two")

        self.R.gather([one], self.root / "out", self.home, missing=(two,))

        text = (self.root / "out/gather.md").read_text()
        self.assertIn("two — not read: no bundle on disk", text)
        self.assertIn("# Gather — 1 carrier, 1 not read", text)

    def test_gather_names_a_later_harvest_left_on_a_branch(self) -> None:
        # 0.0.34: fifteen carriers' harvests sat on unmerged branches, so gather read the checkout's old frontier
        # and none of the branch's proposals, and nothing said so.
        one = make_carrier(self.root, "one")
        B.mint_carrier_id(one, upstream="r-aaaaaa")
        self.splice(one)
        commit(one, "bundle")
        start = git(one, "branch", "--show-current").strip()
        git(one, "switch", "-q", "-c", "chore/harvest")
        toml = one / ".agents/carrier.toml"
        toml.write_text(toml.read_text() + 'harvested_through = "2026-11-24"\n')
        (one / ".agents/proposals/p-0123456789.md").write_text("---\nproposal: p-0123456789\n---\n# Proposal: x\n")
        commit(one, "harvest")
        git(one, "switch", "-q", start)

        self.assertEqual(self.R.later_harvests(one), ["chore/harvest: frontier 2026-11-24 (the checkout: none), 1 proposal the checkout lacks"])
        self.R.gather([one], self.root / "out", self.home)
        self.assertIn("a later harvest on chore/harvest", (self.root / "out/gather.md").read_text())

    def test_a_path_that_is_not_a_repository_is_not_read_instead_of_a_traceback(self) -> None:
        one = make_carrier(self.root, "one")
        B.mint_carrier_id(one, upstream="r-aaaaaa")
        self.splice(one)
        commit(one, "bundle")
        plain = self.root / "plain"
        plain.mkdir()

        self.assertEqual(self.R.bundle_branches(plain), [])
        self.R.gather([one], self.root / "out", self.home, missing=(plain,))
        problems = self.R.align([one], self.home, missing=(plain,))

        self.assertIn("plain — not read: no bundle on disk", (self.root / "out/gather.md").read_text())
        self.assertIn("plain: no bundle on disk", problems)

    def test_align_reports_a_carrier_with_no_id_and_checks_the_others(self) -> None:
        one = make_carrier(self.root, "one")
        B.mint_carrier_id(one, upstream="r-aaaaaa")
        self.splice(one)
        commit(one, "bundle")
        bare = make_carrier(self.root, "bare")
        (bare / ".agents/README.md").write_text(README.format(version="0.0.1"))

        problems = self.R.align([one, bare], self.home)

        self.assertIn("bare: no carrier id in carrier.toml", problems)
        self.assertTrue(any(p.startswith("one: ") for p in problems))

    def test_the_commands_hand_the_missing_paths_on(self) -> None:
        one = make_carrier(self.root, "one")
        plain = self.root / "plain"
        plain.mkdir()
        for command in ("align", "gather"):
            argv = [command, str(one), str(plain)] + (["--out", str(self.root / "o")] if command == "gather" else [])
            with mock.patch.object(self.R, command, return_value=[] if command == "align" else {}) as called, \
                    contextlib.redirect_stdout(io.StringIO()) as out:
                code = self.R.main(argv)
            self.assertEqual(code, 0)
            self.assertEqual(called.call_args.kwargs["missing"], (plain.resolve(),))
            self.assertIn("not read: no bundle on disk: plain", out.getvalue())

    def test_a_splice_report_names_every_path_it_removes(self) -> None:
        actions = ["write README.md", "remove method/old.md", "remove tools/gone.py", "write SHA256SUMS"]

        lines = self.R.splice_report("one", actions, write=False, backup=None)

        self.assertEqual(lines[0], "one: would splice 2 files, remove 2")
        self.assertEqual(lines[1:], ["  - method/old.md", "  - tools/gone.py"])

    def test_splice_takes_no_list_of_rows_to_remove(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.R.main(["splice", "--taken", str(self.root)])

    def test_a_legacy_splice_keeps_the_carrier_file_it_already_has(self) -> None:
        repo = make_legacy(self.root, "old")
        own = {"log": "docs/log.md", "harvested_through": "2026-03-01", "harvested_gaps": ["2026-02-01..2026-02-03 unread"]}
        (repo / ".agents" / B.CARRIER_FILE).write_text(B.dump_carrier(own))
        commit(repo, "a carrier file")
        self.splice(repo, allow_dirty=True)
        data = B.read_carrier(repo / ".agents")
        self.assertEqual((data.get("log"), data.get("harvested_through"), data.get("harvested_gaps")),
                         (own["log"], own["harvested_through"], own["harvested_gaps"]))

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
        self.assertIn("convert 1 outbox rows into proposals/", actions)
        self.assertFalse((agents / "tracking").exists())
        (converted,), _ = B.proposals_of(agents)
        self.assertEqual((converted.target, converted.claim, converted.carrier, converted.base), ("mine", "learned here", "r-bbbbbb", "0.0.1"))
        self.assertEqual(B.verify_problems(agents), [])

    def test_an_old_layout_carrier_with_an_id_minted_since_is_converted(self) -> None:
        repo = make_legacy(self.root, "old")
        for path in (repo / ".agents/README.md", repo / ".agents/method/prompt-context.md"):
            path.write_text("\n".join(l for l in path.read_text().split("\n") if not l.startswith("carrier:")))
        B.write_carrier(repo / ".agents", {"carrier": "r-cccccc"})
        commit(repo, "id minted")

        self.splice(repo)

        self.assertEqual(B.read_carrier(repo / ".agents")["carrier"], "r-cccccc")
        (converted,), _ = B.proposals_of(repo / ".agents")
        self.assertEqual(converted.carrier, "r-cccccc")

    def test_lost_does_not_list_outbox_rows_taken_in_or_a_table_a_formatter_respaced(self) -> None:
        repo = make_legacy(self.root, "old")
        base = self.root / "base"
        base.mkdir()
        (base / "tracking").mkdir()
        (base / "tracking/candidates.md").write_text("| Candidate | Kind | Lacks | Evidence | First seen |\n|---|---|---|---|---|\n"
                                                    "| theirs — the release's | K | nothing | there | 2026-01-01 |\n")
        (repo / ".agents/tracking/candidates.md").write_text(
            "| Candidate | Kind | Lacks | Evidence | First seen |\n| --- | --- | --- | --- | --- |\n"
            "| theirs — the release's   | K    | nothing | there | 2026-01-01 |\n"
            "| mine — learned here | K | a second occurrence | here | 2026-01-03 |\n")

        found = self.R.lost(base, {"old": repo / ".agents"}, self.home)
        self.assertEqual([line for _, rel, line in found if rel.startswith("tracking/")], [])

    def test_what_an_old_layout_carrier_added_outside_its_rows_stops_the_conversion(self) -> None:
        repo = make_legacy(self.root, "old")
        (repo / ".agents/tracking/experiments.md").write_text("## Queued\n\n| Note | Experiment | Cost | Would change |\n"
                                                              "|---|---|---|---|\n| alpha | a new experiment | hours | its boundary |\n")
        commit(repo, "queued an experiment")

        with self.assertRaisesRegex(self.R.RefusedError, "neither rows to convert nor held by the home"):
            self.splice(repo)
        self.assertTrue((repo / ".agents/tracking/experiments.md").is_file())

    def test_a_pack_member_whose_id_is_not_its_name_is_not_taken_in(self) -> None:
        import tarfile

        repo = make_carrier(self.root, "one")
        B.mint_carrier_id(repo, upstream="r-aaaaaa")
        self.splice(repo)
        path = a_proposal(repo / ".agents", "Seen once.")
        pack = self.root / "pack.tar"
        with tarfile.open(pack, "w") as archive:
            archive.add(path, arcname="proposals/p-0000000000.md")

        report = self.R.gather([repo], self.root / "out", self.home, packs=[pack])

        self.assertEqual(report["packs"]["pack.tar"]["proposals"], [])
        self.assertIn("not its file name", " ".join(report["packs"]["pack.tar"]["problems"]))

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


class Queue(Base):
    def test_a_queued_candidate_without_its_slug_fails_the_check(self) -> None:
        R = release()
        home = make_home(self.root)
        self.assertEqual(R.queue_problems(home), [])
        queue = home / "meta/tracking/candidates.md"
        queue.write_text(queue.read_text() + "| **A claim in bold, with no slug.** | K | nothing | here | 2026-01-01 | 0.0.1 |\n")

        self.assertIn("does not open with its slug", "\n".join(R.queue_problems(home)))


class TrackingSlugs(Base):
    def test_a_slug_claimed_as_a_file_must_name_one_and_a_gone_one_is_not_a_false_positive(self) -> None:
        R = release()
        home = make_home(self.root)
        notes = home / "sources/notes/active"
        notes.mkdir(parents=True, exist_ok=True)
        (notes / "a-real-note.md").write_text("---\nslug: a-real-note\n---\n")
        track = home / "meta/tracking"
        (track / "history.md").write_text(
            "| Candidate | Where it went |\n|---|---|\n"
            "| `a-real-note` | **admitted as a note at 0.0.1** |\n"
            "| `an-invented-one` | **admitted as a note at 0.0.1** |\n"
            "| `a-refused-idea` | refused: a preference |\n"
            "| `folded-idea` | **folded** into `a-real-note` |\n")
        (track / "experiments.md").write_text("| Note | Experiment | Cost | Would change |\n|---|---|---|---|\n"
                                             "| a-real-note | run it | x | y |\n| a-ghost-note | run it | x | y |\n")
        (track / "retired.md").write_text("| Date | Note | W | E | R |\n|---|---|---|---|---|\n"
                                          "| 2026-01-01 | [vanished](../../sources/notes/retired/vanished.md) | s | e | r |\n")

        problems, warnings = R.tracking_slug_problems(home)

        self.assertEqual(len(problems), 2, problems)
        self.assertTrue(any("an-invented-one" in p for p in problems), problems)
        self.assertTrue(any("vanished.md" in p for p in problems), problems)
        self.assertEqual(len(warnings), 1, warnings)
        self.assertIn("a-ghost-note", warnings[0])


class Ledger(Base):
    def test_nothing_is_discarded_by_age_and_the_ledger_names_every_idea_met(self) -> None:
        R = release()
        home = make_home(self.root)
        for n in (2, 3, 4):
            changelog = home / "sources/bundle/CHANGELOG.md"
            changelog.write_text(changelog.read_text().replace("## [Unreleased]\n", f"## [Unreleased]\n\n## [0.0.{n}] - 2026-02-0{n}\n\n- More.\n"))
            R.release(f"0.0.{n}", home)
            commit(home, f"release 0.0.{n}")
            git(home, "tag", "-a", f"v0.0.{n}", "-m", f"0.0.{n}")
        history = home / "meta/tracking/history.md"
        history.write_text(history.read_text() + "\n| Candidate | Where it went |\n|---|---|\n| `dropped-idea` | dropped: the default already does it |\n")
        R.build(home)

        ledger = (home / "meta/tracking/INDEX.md").read_text()

        self.assertEqual(R.funnel(home)["by_releases_waited"], {"3": 1})
        self.assertFalse(hasattr(R, "triage"))
        self.assertIn("- `old-idea` — K, since 0.0.1", ledger)
        self.assertIn("- `dropped-idea` — dropped: the default already does it", ledger)
        self.assertIn("- `gone` — superseded", ledger)
        self.assertEqual(R.build(home, check=True), [])
        history.write_text(history.read_text() + "| `another` | refused |\n")
        self.assertIn("meta/tracking/INDEX.md", "\n".join(R.build(home, check=True)))


class Cut(Base):
    """The cut as a build rule: the original keeps the full block, the release ships the short one."""

    def setUp(self) -> None:
        super().setUp()
        self.R = release()
        self.home = make_home(self.root)
        self.original = self.home / "sources/bundle/method/prompt-bootstrap.md"
        self.built = self.home / ".agents/method/prompt-bootstrap.md"

    def block(self, full: str, short: str, name: str = "") -> None:
        self.original.write_text(self.original.read_text()
                                 + f"\n<!-- release: short{' ' + name if name else ''} -->\n{full}\n"
                                   f"<!-- release: as -->\n{short}\n<!-- /release -->\n")

    def ledger(self, *rows: str) -> None:
        (self.home / self.R.CUT_LEDGER).write_text(
            "# Ledger of the cut\n\n" + self.R.CUT_LEDGER_HEADER + "\n|---|---|---|---|\n" + "".join(r + "\n" for r in rows))

    def test_the_short_form_ships_and_the_full_one_stays_in_the_home(self) -> None:
        self.block("**Never** fold another session's work, in five rounds.", "**Never** fold another session's work.")
        self.ledger("| sources/bundle/method/prompt-bootstrap.md | * | five | dropped: the rounds are in §21.4 |")
        self.R.build(self.home)

        self.assertIn("in five rounds", self.original.read_text())
        self.assertNotIn("in five rounds", self.built.read_text())
        self.assertIn("**Never** fold another session's work.", self.built.read_text())
        self.assertNotIn("release: short", self.built.read_text())
        self.assertEqual(self.R.build(self.home, check=True), [])

    def test_an_empty_short_form_is_a_home_only_block(self) -> None:
        self.block("Only for the home.", "")
        self.ledger("| sources/bundle/method/prompt-bootstrap.md | * | only | dropped: home only |")
        self.R.build(self.home)

        self.assertNotIn("Only for the home.", self.built.read_text())

    def test_a_drop_with_no_ledger_row_fails_the_build(self) -> None:
        self.block("The gate runs on every `intermediate` tree.", "The gate runs.", name="commit-split")
        with self.assertRaisesRegex(self.R.BuildError, "commit-split.*every"):
            self.R.build(self.home)
        self.ledger("| sources/bundle/method/prompt-bootstrap.md | commit-split | every | dropped: in the topic |")
        with self.assertRaisesRegex(self.R.BuildError, "intermediate"):
            self.R.build(self.home)
        self.ledger("| sources/bundle/method/prompt-bootstrap.md | commit-split | every | dropped: in the topic |",
                    "| sources/bundle/method/prompt-bootstrap.md | commit-split | `intermediate` | kept at the topic |")
        self.R.build(self.home)
        self.assertEqual(self.R.build(self.home, check=True), [])

    def test_a_malformed_or_unclosed_marker_is_refused(self) -> None:
        self.original.write_text(self.original.read_text() + "\n<!-- release: shrt -->\nx\n")
        with self.assertRaisesRegex(self.R.BuildError, "not a marker the build knows"):
            self.R.build(self.home)
        self.original.write_text(self.original.read_text().replace("release: shrt", "release: short"))
        with self.assertRaisesRegex(self.R.BuildError, "has no"):
            self.R.build(self.home)

    def test_a_skill_ships_its_release_description_and_the_home_installs_the_full_one(self) -> None:
        skill = self.home / "sources/bundle/method/skills/close/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text('---\nname: close\ndescription: "The long description, with every trigger phrase."\n'
                         'release_description: "The short one."\n---\n\n# Close\n')
        self.R.build(self.home)
        shipped = (self.home / ".agents/method/skills/close/SKILL.md").read_text()

        self.assertIn('description: "The short one."', shipped)
        self.assertNotIn("release_description", shipped)
        self.assertNotIn("every trigger phrase", shipped)
        B.install_skills(self.home, self.home / ".agents")
        installed = (self.home / ".claude/skills/close/SKILL.md").read_text()
        self.assertIn("every trigger phrase", installed)
        self.assertNotIn("release_description", installed)
        self.assertEqual(B.installed_skill_problems(self.home, self.home / ".agents"), [])


class Manifest(Base):
    """`MANIFEST.md`'s checked limits: the export does not grow, the descriptions every turn loads, the hand-off."""

    def tree(self) -> Path:
        root = self.root / "home"
        skill = root / ".agents/method/skills/close/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("---\nname: close\ndescription: Close the session.\n---\n\nBody.\n")
        (root / ".agents/README.md").write_text("A bundle.\n")
        (root / "meta").mkdir()
        (root / "meta/roadmap.md").write_text("# Roadmap\n\n## Where we are\n\nOne two three.\n\n## Next\n\n" + "word " * 900)
        return root

    def test_a_tree_within_every_limit_passes(self) -> None:
        R = release()
        self.assertEqual(R.manifest_problems(self.tree(), export_cap=10_000), [])

    def test_each_description_has_the_cap_of_its_kind(self) -> None:
        R = release()
        root = self.tree()
        skill = root / ".agents/method/skills/close/SKILL.md"
        skill.write_text("---\nname: close\ndescription: " + "x" * 751 + "\n---\n\nBody.\n")
        self.assertIn("close", "\n".join(R.manifest_problems(root, export_cap=10_000, descriptions_cap=10_000)))
        skill.write_text("---\nname: close\ndescription: " + "x" * 750 + "\n---\n\nBody.\n")
        self.assertEqual(R.manifest_problems(root, export_cap=10_000, descriptions_cap=10_000), [])
        other = root / ".agents/method/skills/unknown/SKILL.md"
        other.parent.mkdir(parents=True)
        other.write_text("---\nname: unknown\ndescription: Short.\n---\n\nBody.\n")
        self.assertIn("no kind", "\n".join(R.manifest_problems(root, export_cap=10_000, descriptions_cap=10_000)))

    def test_each_limit_crossed_fails(self) -> None:
        R = release()
        root = self.tree()
        self.assertIn("descriptions", "\n".join(R.manifest_problems(root, export_cap=10_000, descriptions_cap=5)))
        (root / "meta/roadmap.md").write_text("## Where we are\n\n" + "word " * 501 + "\n## Next\n")
        self.assertIn("hand-off", "\n".join(R.manifest_problems(root, export_cap=10_000)))
        # a heading with trailing spaces or CRLF is still read, and a missing section is a problem, never a pass
        (root / "meta/roadmap.md").write_text("## Where we are  \r\n\r\n" + "word " * 501 + "\r\n## Next\r\n")
        self.assertIn("hand-off", "\n".join(R.manifest_problems(root, export_cap=10_000)))
        (root / "meta/roadmap.md").write_text("# Roadmap\n\n## Next\n")
        self.assertIn("no *Where we are*", "\n".join(R.manifest_problems(root, export_cap=10_000)))

    def test_check_warns_and_passes_over_the_export_cap(self) -> None:
        R = release()
        root = self.tree()
        self.assertNotIn("export", "\n".join(R.manifest_problems(root, export_cap=10)))
        message = R.export_over_cap(root, export_cap=10)
        self.assertRegex(message, r"^the export ships \d+ bytes, over the manifest's cap of 10; shrink it before the cut$")
        self.assertIsNone(R.export_over_cap(root, export_cap=10_000))

    def test_check_prints_the_export_overrun_as_a_warn_not_a_problem(self) -> None:
        R = release()
        home = make_home(self.root)
        with mock.patch.object(R, "EXPORT_CAP", 10):
            problems, notes = R.check(home)
        self.assertTrue([n for n in notes if "WARN" in n and "the export ships" in n])
        self.assertFalse([p for p in problems if "the export ships" in p])


class PrivacyRatchet(Base):
    """`check` reads the home's records against the baseline (`d-5ed7e8-af36e9`), and the release holds no warning."""

    WARNED = "It took " + "1," + "017" + " runs to see it."

    def test_a_new_warning_in_the_records_fails_and_a_known_one_is_counted(self) -> None:
        R = release()
        home = make_home(self.root)
        roadmap = home / "meta/roadmap.md"
        roadmap.write_text(roadmap.read_text() + "\n" + self.WARNED + "\n")

        problems, _ = R.check(home)
        self.assertTrue([p for p in problems if "meta/roadmap.md" in p and "exact-count" in p and "new" in p], problems)

        fingerprint = B.privacy_fingerprint("meta/roadmap.md", "exact-count", self.WARNED)
        (home / "meta/tracking/privacy-baseline.txt").write_text("# baseline\n" + fingerprint + "\n")
        problems, notes = R.check(home)
        self.assertFalse([p for p in problems if "exact-count" in p], problems)
        self.assertTrue([n for n in notes if "1 known" in n], notes)

    def test_a_stale_fingerprint_is_reported_not_failed(self) -> None:
        R = release()
        home = make_home(self.root)
        gone = B.privacy_fingerprint("meta/roadmap.md", "exact-count", "a line no longer there")
        (home / "meta/tracking/privacy-baseline.txt").write_text(gone + "\n")

        problems, notes = R.check(home)

        self.assertFalse([p for p in problems if "baseline" in p], problems)
        self.assertTrue([n for n in notes if "1 stale" in n], notes)

    def test_a_fingerprint_not_in_the_base_version_of_the_baseline_fails(self) -> None:
        # Shrink-only, enforced: against its version at the merge-base, the baseline may lose lines, never gain.
        R = release()
        home = make_home(self.root)
        git(home, "branch", "-M", "main")
        roadmap, baseline = home / "meta/roadmap.md", home / "meta/tracking/privacy-baseline.txt"
        roadmap.write_text(roadmap.read_text() + "\n" + self.WARNED + "\n")
        known = B.privacy_fingerprint("meta/roadmap.md", "exact-count", self.WARNED)
        baseline.write_text("# baseline\n" + known + "\n")
        commit(home, "docs: the baseline")
        git(home, "switch", "-q", "-c", "work")
        problems, _ = R.check(home)
        self.assertFalse([p for p in problems if "baseline" in p], problems)

        leak = "It took " + "2," + "345" + " runs to see it."
        roadmap.write_text(roadmap.read_text() + leak + "\n")
        added = B.privacy_fingerprint("meta/roadmap.md", "exact-count", leak)
        for how, text in (("hand-added", "# baseline\n" + known + "\n" + added + "\n"),
                          ("rewritten", "\n".join(sorted([known, added])) + "\n")):
            with self.subTest(how=how):
                baseline.write_text(text)
                problems, _ = R.check(home)
                self.assertTrue([p for p in problems if "privacy-baseline.txt" in p and "version at the base" in p], problems)
                self.assertFalse([p for p in problems if "a new warning" in p], problems)

        baseline.write_text("")  # shrunk to nothing: allowed, the warning is new again
        problems, _ = R.check(home)
        self.assertFalse([p for p in problems if "privacy-baseline.txt" in p and "version at the base" in p], problems)

    def test_any_warning_in_the_release_fails_whatever_the_baseline(self) -> None:
        R = release()
        home = make_home(self.root)
        readme = home / "sources/bundle/knowledge/README.md"
        readme.write_text(readme.read_text() + "\n" + self.WARNED + "\n")
        R.build(home)
        fingerprint = B.privacy_fingerprint("knowledge/README.md", "exact-count", self.WARNED)
        (home / "meta/tracking/privacy-baseline.txt").write_text(fingerprint + "\n")

        problems, _ = R.check(home)

        self.assertTrue([p for p in problems if "knowledge/README.md" in p and "release" in p
                         and not p.startswith("privacy: " + str(home))], problems)


class CommitCommand(Base):
    """`release.py commit -m MSG FILE...` (`d-5ed7e8-f61f95`): the gate on its own exit status, then only the
    named files committed, everything else left as it was."""

    PASS = (("tests", [sys.executable, "-c", "print('ran 3 tests: OK')"]),
            ("check", [sys.executable, "-c", "print('home check: passed')"]))

    def setUp(self) -> None:
        super().setUp()
        self.R = release()
        self.repo = init_repo(self.root / "repo")
        for name in ("a.md", "b.md", "c.md"):
            (self.repo / name).write_text(f"{name} one\n")
        commit(self.repo, "docs: start")

    def call(self, files: list[str], gate=None, message: str = "docs: a", stale=lambda root: []) -> tuple[int, str]:  # noqa: ANN001
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = self.R.commit_files(message, files, self.repo, gate=gate or self.PASS, stale=stale)
        return code, out.getvalue()

    def test_only_the_named_files_are_committed_and_the_rest_is_left_as_it_was(self) -> None:
        for name in ("a.md", "b.md", "c.md"):
            (self.repo / name).write_text(f"{name} two\n")
        git(self.repo, "add", "c.md")  # staged by someone else: stays staged, uncommitted

        code, out = self.call(["a.md"])

        self.assertEqual(code, 0, out)
        self.assertEqual(git(self.repo, "show", "--name-only", "--format=%s", "HEAD").split(), ["docs:", "a", "a.md"])
        status = git(self.repo, "status", "--porcelain").splitlines()
        self.assertEqual(sorted(status), [" M b.md", "M  c.md"])

    def test_a_failing_step_refuses_the_commit_and_prints_its_tail(self) -> None:
        (self.repo / "a.md").write_text("a two\n")
        # The output says OK; only the exit status says otherwise, and the status is what is read.
        failing = (("tests", [sys.executable, "-c", "import sys; print('\\n'.join(f'line {i}' for i in range(100))); "
                                                     "print('boom: one test failed'); sys.exit(1)"]),
                   ("check", [sys.executable, "-c", "print('home check: passed')"]))
        before = git(self.repo, "rev-parse", "HEAD")

        code, out = self.call(["a.md"], gate=failing)

        self.assertEqual(code, 1, out)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), before)
        self.assertIn("boom: one test failed", out)
        self.assertNotIn("line 3\n", out)  # the tail, not the whole output
        self.assertIn("tests", out)
        self.assertEqual(git(self.repo, "status", "--porcelain").splitlines(), [" M a.md"])

    def test_every_step_runs_and_each_failure_is_named(self) -> None:
        (self.repo / "a.md").write_text("a two\n")
        both = (("tests", [sys.executable, "-c", "import sys; print('red one'); sys.exit(1)"]),
                ("check", [sys.executable, "-c", "import sys; print('red two'); sys.exit(3)"]))

        code, out = self.call(["a.md"], gate=both)

        self.assertEqual(code, 1, out)
        self.assertIn("red one", out)
        self.assertIn("red two", out)

    def test_an_empty_list_is_refused(self) -> None:
        with self.assertRaises(self.R.RefusedError):
            self.call([])
        with self.assertRaises(self.R.RefusedError):
            self.call(["a.md"], message="  ")

    def test_a_release_file_is_refused_while_the_build_is_stale(self) -> None:
        (self.repo / ".agents").mkdir()
        (self.repo / ".agents/x.md").write_text("x\n")
        ran = []
        gate = (("tests", [sys.executable, "-c", f"open({str(self.root / 'ran')!r}, 'w').write('1')"]),)

        with self.assertRaises(self.R.RefusedError) as caught:
            self.call([".agents/x.md"], gate=gate, stale=lambda root: ["x.md: differs from its build"])

        self.assertIn("build", str(caught.exception))
        self.assertFalse((self.root / "ran").exists(), ran)  # refused before the gate runs
        code, out = self.call([".agents/x.md"], gate=gate)
        self.assertEqual(code, 0, out)

    def test_the_gate_reads_what_is_committed_not_the_working_tree(self) -> None:
        # The named file's new text is in the export; an unnamed change and an untracked file are not.
        (self.repo / "a.md").write_text("a two\n")
        (self.repo / "b.md").write_text("b unfinished\n")
        (self.repo / "u.md").write_text("untracked\n")
        seen = {}

        def stale(root: Path) -> list[str]:
            seen.update(root=root, a=(root / "a.md").read_text(), b=(root / "b.md").read_text(),
                        u=(root / "u.md").exists())
            return []
        where = self.root / "cwd"
        gate = (("tests", [sys.executable, "-c", f"import os; open({str(where)!r}, 'w').write(os.getcwd())"]),)

        code, out = self.call(["a.md"], gate=gate, stale=stale)

        self.assertEqual(code, 0, out)
        self.assertNotEqual(Path(seen["root"]).resolve(), self.repo.resolve())
        self.assertEqual((seen["a"], seen["b"], seen["u"]), ("a two\n", "b.md one\n", False))
        self.assertEqual(Path(where.read_text()).resolve(), Path(seen["root"]).resolve())
        self.assertFalse(Path(seen["root"]).exists())  # the export is removed afterwards
        self.assertEqual(sorted(git(self.repo, "status", "--porcelain").splitlines()), [" M b.md", "?? u.md"])

    def test_a_stale_export_refuses_and_leaves_the_index_as_it_was(self) -> None:
        (self.repo / "a.md").write_text("a two\n")
        (self.repo / "c.md").write_text("c two\n")
        git(self.repo, "add", "c.md")
        before = git(self.repo, "rev-parse", "HEAD")

        with self.assertRaises(self.R.RefusedError) as caught:
            self.call(["a.md"], stale=lambda root: ["x.md: differs from its build"])

        self.assertIn("build", str(caught.exception))
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), before)
        self.assertEqual(sorted(git(self.repo, "status", "--porcelain").splitlines()), [" M a.md", "M  c.md"])

    def test_sources_committed_without_their_built_release_are_refused(self) -> None:
        home = make_home(self.root / "h")
        readme = home / "sources/bundle/knowledge/README.md"
        readme.write_text(readme.read_text() + "\nA new line.\n")
        self.R.build(home)  # the working tree is current; what is named is not
        out = io.StringIO()
        with contextlib.redirect_stdout(out), self.assertRaises(self.R.RefusedError) as caught:
            self.R.commit_files("docs: x", ["sources/bundle/knowledge/README.md"], home, gate=self.PASS)
        self.assertIn("build", str(caught.exception))
        with contextlib.redirect_stdout(out):
            code = self.R.commit_files("docs: x", ["sources/bundle/knowledge/README.md", ".agents"], home, gate=self.PASS)
        self.assertEqual(code, 0, out.getvalue())

    def test_a_file_changed_in_the_same_second_at_the_same_size_is_exported_as_it_is(self) -> None:
        # Racy git: an index whose stat data the file still matches (same size, same second) trusts the old blob.
        # A scratch index copied from the real one carried that data, and the export held the stale file
        # (`i-5ed7e8-33c9b5`); an index read from HEAD carries none, so the named file is hashed as it is.
        (self.repo / "a.md").write_text("a two\n")
        git(self.repo, "add", "a.md")
        (self.repo / "a.md").write_text("a 2nd\n")
        seen = {}

        def stale(root: Path) -> list[str]:
            seen["a"] = (root / "a.md").read_text()
            return []

        code, out = self.call(["a.md"], stale=stale)

        self.assertEqual(code, 0, out)
        self.assertEqual(seen, {"a": "a 2nd\n"})
        self.assertEqual(git(self.repo, "show", "HEAD:a.md"), "a 2nd\n")

    def test_a_change_staged_but_not_named_is_neither_gated_nor_committed(self) -> None:
        # `git commit -- FILES` commits HEAD plus FILES: the gate reads the same, so a staged source cannot
        # make a release named alone look current while the commit holds a stale one.
        (self.repo / "a.md").write_text("a two\n")
        (self.repo / "c.md").write_text("c two\n")
        git(self.repo, "add", "c.md")
        seen = {}

        def stale(root: Path) -> list[str]:
            seen.update(a=(root / "a.md").read_text(), c=(root / "c.md").read_text())
            return []

        code, out = self.call(["a.md"], stale=stale)

        self.assertEqual(code, 0, out)
        self.assertEqual(seen, {"a": "a two\n", "c": "c.md one\n"})
        self.assertEqual(git(self.repo, "show", "HEAD:c.md"), "c.md one\n")
        self.assertEqual(sorted(git(self.repo, "status", "--porcelain").splitlines()), ["M  c.md"])

    def test_a_named_file_deleted_or_renamed_leaves_the_export_and_the_commit(self) -> None:
        (self.repo / "b.md").unlink()
        (self.repo / "c.md").rename(self.repo / "d.md")
        seen = {}

        def stale(root: Path) -> list[str]:
            seen.update(b=(root / "b.md").exists(), c=(root / "c.md").exists(), d=(root / "d.md").read_text())
            return []

        code, out = self.call(["b.md", "c.md", "d.md"], stale=stale)

        self.assertEqual(code, 0, out)
        self.assertEqual(seen, {"b": False, "c": False, "d": "c.md one\n"})
        self.assertEqual(sorted(git(self.repo, "ls-files").split()), ["a.md", "d.md"])
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")

    def test_a_repository_with_no_commit_yet_commits_the_named_files(self) -> None:
        fresh = init_repo(self.root / "fresh")
        (fresh / "a.md").write_text("a\n")
        (fresh / "b.md").write_text("b\n")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = self.R.commit_files("docs: a", ["a.md"], fresh, gate=self.PASS, stale=lambda root: [])
        self.assertEqual(code, 0, out.getvalue())
        self.assertEqual(git(fresh, "ls-files").split(), ["a.md"])

    def test_every_step_reads_the_scratch_index_and_it_is_removed_on_every_way_out(self) -> None:
        # Inside the export git reads the scratch index, so a newly named file is tracked there
        # (`privacy --tracked` reads `git ls-files`); the index goes with the export, a refusal included.
        (self.repo / "new.md").write_text("new\n")
        listed, index = self.root / "listed", self.root / "index-path"
        probe = ("import os, subprocess; "
                 f"open({str(listed)!r}, 'w').write(subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout); "
                 f"open({str(index)!r}, 'w').write(os.environ.get('GIT_INDEX_FILE', ''))")
        for code_out in (0, 1):
            with self.subTest(exit=code_out):
                gate = (("check", [sys.executable, "-c", probe + f"; raise SystemExit({code_out})"]),)
                code, out = self.call(["new.md"], gate=gate)
                self.assertEqual(code, code_out, out)
                self.assertIn("new.md", listed.read_text().split())
                self.assertTrue(index.read_text(), "GIT_INDEX_FILE is not set for the step")
                self.assertFalse(Path(index.read_text()).exists())
                git(self.repo, "reset", "-q", "--soft", "HEAD~1") if code_out == 0 else None
                git(self.repo, "reset", "-q") if code_out == 0 else None
        seen = {}

        def refuse(root: Path) -> list[str]:
            seen["index"] = root.parent / "index"
            seen["existed"] = seen["index"].exists()
            return ["x.md: differs from its build"]
        with self.assertRaises(self.R.RefusedError):
            self.call(["new.md"], stale=refuse)
        self.assertTrue(seen["existed"])
        self.assertFalse(seen["index"].exists())

    def test_the_command_line_takes_a_message_and_files(self) -> None:
        with mock.patch.object(self.R, "commit_files", return_value=0) as called:
            self.assertEqual(self.R.main(["commit", "-m", "docs: b", "b.md", "c.md"]), 0)
        self.assertEqual(called.call_args.args[:2], ("docs: b", ["b.md", "c.md"]))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(self.R.main(["commit", "-m", "docs: b"]), 2)


class Dequeue(Base):
    """`release.py dequeue SLUG VERDICT --release X.Y.Z --reason TEXT` (`i-5ed7e8-655151`): a queued row moves to
    the history with its verdict, in the history's own form, and the ledger is rebuilt."""

    def setUp(self) -> None:
        super().setUp()
        self.R = release()
        self.home = make_home(self.root)
        self.queue = self.home / "meta/tracking/candidates.md"
        self.history = self.home / "meta/tracking/history.md"
        self.queue.write_text(self.queue.read_text()
                              + "| new-idea — a second idea | M | an occurrence | elsewhere | 2026-01-02 | 0.0.1 |\n")

    def test_the_row_leaves_the_queue_and_the_history_gains_its_line_newest_first(self) -> None:
        lines = self.R.dequeue("old-idea", "refused", "0.0.2", "one occurrence, and textbook", self.home)

        self.assertNotIn("old-idea", self.queue.read_text())
        self.assertIn("new-idea", self.queue.read_text())
        history = self.history.read_text()
        self.assertIn("## Taken out of the queue for the release 0.0.2\n\n| Candidate | Where it went |\n|---|---|\n"
                      "| `old-idea` | **refused at 0.0.2**: one occurrence, and textbook |\n", history)
        self.assertLess(history.index("0.0.2"), history.index("## First"))
        self.assertIn("old-idea", (self.home / "meta/tracking/INDEX.md").read_text())
        self.assertTrue(any("old-idea" in line for line in lines), lines)

    def test_a_second_row_of_the_same_release_joins_its_section(self) -> None:
        self.R.dequeue("old-idea", "refused", "0.0.2", "textbook", self.home)
        self.R.dequeue("new-idea", "admitted", "0.0.2", "as the note `alpha`", self.home)

        history = self.history.read_text()
        self.assertEqual(history.count("## Taken out of the queue for the release 0.0.2"), 1)
        self.assertIn("| `old-idea` | **refused at 0.0.2**: textbook |\n| `new-idea` | **admitted at 0.0.2**: as the note `alpha` |",
                      history)
        self.assertNotIn("| new-idea", self.queue.read_text())

    def test_an_unknown_slug_verdict_or_release_is_refused_and_nothing_written(self) -> None:
        before = (self.queue.read_text(), self.history.read_text())
        for args in (("no-such-idea", "refused", "0.0.2", "why"), ("old-idea", "liked", "0.0.2", "why"),
                     ("old-idea", "refused", "next", "why"), ("old-idea", "refused", "0.0.2", "  ")):
            with self.subTest(args=args), self.assertRaises(self.R.RefusedError):
                self.R.dequeue(*args, root=self.home)
        self.assertEqual((self.queue.read_text(), self.history.read_text()), before)

    HAND = ("# History\n\n## Taken out of the queue for the release 0.0.2\n\nWritten by hand, before the command.\n\n"
            "| Candidate | Where it went |\n|---|---|\n| `gone-idea` | **extended**, applying the queued row: in its note |\n\n"
            "## First\n\nnothing\n")

    def test_the_release_s_hand_written_section_is_joined_not_doubled(self) -> None:
        self.history.write_text(self.HAND)

        self.R.dequeue("old-idea", "refused", "0.0.2", "textbook", self.home)

        history = self.history.read_text()
        self.assertEqual(history.count("## Taken out of the queue"), 1, history)
        self.assertIn("| `gone-idea` | **extended**, applying the queued row: in its note |\n"
                      "| `old-idea` | **refused at 0.0.2**: textbook |\n", history)

    def test_an_older_by_the_release_heading_is_joined_too(self) -> None:
        self.history.write_text(self.HAND.replace("for the release", "by the release"))
        self.R.dequeue("old-idea", "refused", "0.0.2", "textbook", self.home)
        self.assertEqual(self.history.read_text().count("## Taken out of the queue"), 1)

    def test_a_hand_written_bold_verdict_still_queued_fails_the_check(self) -> None:
        # The history's hand-written form, `**extended**, ...`, under the release's section, read as the command's.
        self.history.write_text(self.HAND.replace("gone-idea", "old-idea"))
        problems = self.R.answered_still_queued(self.home)
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("extended at 0.0.2", problems[0])

    def test_a_row_answered_by_the_command_and_still_queued_fails_the_check(self) -> None:
        self.R.dequeue("old-idea", "fixed", "0.0.2", "the tool now refuses it", self.home)
        self.assertEqual(self.R.answered_still_queued(self.home), [])
        self.queue.write_text(self.queue.read_text() + "| old-idea — back by hand | K | x | y | 2026-01-01 | 0.0.1 |\n")

        self.assertIn("old-idea", "\n".join(self.R.answered_still_queued(self.home)))

    def test_the_command_line(self) -> None:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), mock.patch.object(self.R, "ROOT", self.home):
            code = self.R.main(["dequeue", "old-idea", "dropped", "--release", "0.0.2", "--reason", "superseded"])
        self.assertEqual(code, 0, out.getvalue())
        self.assertIn("| `old-idea` | **dropped at 0.0.2**: superseded |", self.history.read_text())


class Received(Base):
    def test_only_the_last_two_releases_keep_their_verdicts(self) -> None:
        R = release()
        meta = self.root / "meta"
        (meta / "tracking").mkdir(parents=True)
        rows = [("p-aaaaaaaaaa", "0.0.9", "queued as a long verdict"), ("p-bbbbbbbbbb", "0.0.10", "admitted into x"),
                ("p-cccccccccc", "0.0.11", "folded into y")]
        (meta / "tracking/received.md").write_text("# Received\n\n" + B.RECEIVED_HEADER + "\n|---|---|---|\n"
                                                   + "".join(f"| `{a}` | {b} | {c} |\n" for a, b, c in rows))
        page = R.render_received(meta)
        self.assertIn("| `p-aaaaaaaaaa` | 0.0.9 | — |", page)  # older: the id still prunes, the verdict stays home
        self.assertIn("admitted into x", page)
        self.assertIn("folded into y", page)
        self.assertNotIn("a long verdict", page)


class Open(Base):
    def test_a_waiting_candidate_ships_as_its_slug_and_kind(self) -> None:
        R = release()
        meta = self.root / "meta"
        (meta / "tracking").mkdir(parents=True)
        (meta / "tracking/candidates.md").write_text(
            "# Candidates\n\n| Candidate | Kind | Lacks | Evidence | Seen | Since |\n|---|---|---|---|---|---|\n"
            "| a-long-slug — a claim written out at length | K | a second repository with real numbers | x | 2026-01-01 | 0.0.1 |\n")
        page = R.render_open(meta)
        self.assertIn("| `a-long-slug` | K |", page)
        self.assertNotIn("a claim written out at length", page)  # recognised by slug; the home keeps the rest
        self.assertNotIn("a second repository", page)


class ShippedChangelog(Base):
    def test_the_shipped_changelog_starts_at_the_oldest_carriers_version(self) -> None:
        R = release()
        text = ("# Changelog\n\nIntro.\n\n## [Unreleased]\n\n- next\n\n## [0.0.3] - 2026-01-03\n\n- three\n\n"
                "## [0.0.2] - 2026-01-02\n\n- two\n\n## [0.0.1] - 2026-01-01\n\n- one\n")
        shipped = R.trim_changelog(text, "0.0.2")
        for kept in ("Intro.", "## [Unreleased]", "- three", "## [0.0.2]", "- two"):
            self.assertIn(kept, shipped)
        self.assertNotIn("- one", shipped)
        self.assertIn("sources/bundle/CHANGELOG.md", shipped)  # where the earlier versions are
        self.assertEqual(R.trim_changelog(text, None), text)  # no carrier registered: nothing cut


class ShippedTool(Base):
    ROOT = Path(__file__).resolve().parents[2]

    def test_the_shipped_tool_has_no_comments_but_its_mark(self) -> None:
        import tokenize
        R = release()
        with (self.ROOT / ".agents/tools/bundle.py").open("rb") as f:
            comments = [t.string for t in tokenize.tokenize(f.readline) if t.type == tokenize.COMMENT]
        self.assertEqual([c for c in comments if not c.startswith("#!") and R.RELEASE_MARK not in c], [])

    def test_the_shipped_tool_parses_to_the_same_tree_as_its_original(self) -> None:
        import ast
        original = (self.ROOT / "sources/bundle/tools/bundle.py").read_text(encoding="utf-8")
        shipped = (self.ROOT / ".agents/tools/bundle.py").read_text(encoding="utf-8")
        self.assertEqual(ast.dump(ast.parse(original)), ast.dump(ast.parse(shipped)))

    def test_a_hash_inside_a_string_survives(self) -> None:
        R = release()
        src = '#!/usr/bin/env python3\n# whole line\nx = "# not a comment"  # a comment\n\ny = 1\n'
        self.assertEqual(R.strip_comments(src), '#!/usr/bin/env python3\nx = "# not a comment"\n\ny = 1\n')


class UnattendedRule(Base):
    """Both built prompts carry the shared unattended rule in their pre-flight, with every choice it may never take."""

    ROOT = Path(__file__).resolve().parents[2]
    NEVER = {"prompt-harvest.md": ("a privacy warning or allowance", "step 3's candidate list",
                                   "a delete outside an approved table", "a merge or push"),
             "prompt-update.md": ("a privacy warning or allowance", "step 5's approval",
                                  "a delete outside an approved table", "a merge or push")}

    def test_the_harvest_and_the_update_state_the_unattended_rule_before_they_start(self) -> None:
        for name in ("prompt-harvest.md", "prompt-update.md"):
            text = (self.ROOT / ".agents/method" / name).read_text(encoding="utf-8")
            start = text.index("\n## Before you start")
            end = text.find("\n## ", start + 1)
            preflight = " ".join(text[start:end if end != -1 else None].split())
            with self.subTest(prompt=name):
                self.assertIn("**Unattended run (no one to answer).**", preflight)
                self.assertIn("`unattended: <question> -> <default>`", preflight)
                self.assertIn("Never take a choice that needs the human's yes", preflight)
                for choice in self.NEVER[name]:
                    self.assertIn(choice, preflight)
                self.assertIn("Record it as pending and leave it unwritten. Stop rules still stop.", preflight)
                if name == "prompt-harvest.md":
                    self.assertIn("unless the run is unattended", preflight)

    def test_bundle_updates_alone_are_nothing_to_harvest_and_each_harvest_entry_has_its_own_title(self) -> None:
        harvest = " ".join((self.ROOT / ".agents/method/prompt-harvest.md").read_text(encoding="utf-8").split())
        update = " ".join((self.ROOT / ".agents/method/prompt-update.md").read_text(encoding="utf-8").split())
        for text in (harvest, update):
            self.assertIn("only the bundle's own updates", text)
        self.assertIn('new entry "harvest through', harvest)
        self.assertIn("its own `tools/bundle.py export`", update)


class CheckRunsRedCheck(Base):
    """`release.py check` runs `red-check` over the merge-base with main to HEAD, when in git (d-5ed7e8-8c417c)."""

    def test_outside_git_it_is_skipped(self) -> None:
        problems, notes = release().red_check_problems(self.root)
        self.assertEqual(problems, [])
        self.assertTrue([n for n in notes if "red-check" in n and "skipped" in n], notes)

    def test_a_branch_s_untested_fix_is_a_problem(self) -> None:
        repo = init_repo(self.root / "r")
        (repo / ".agents").mkdir()
        (repo / ".agents/carrier.toml").write_text('carrier = "r-aaaaaa"\n[red_check]\ncode = ["tools/**"]\ntests = ["tests/test_*.py"]\n')
        (repo / "tools").mkdir()
        (repo / "tools/bundle.py").write_text("# " + bundle.RED_CHECK_MARK + "\n")
        commit(repo, "chore: start")
        git(repo, "branch", "-M", "main")
        git(repo, "switch", "-q", "-c", "work")
        (repo / "tools/calc.py").write_text("X = 1\n")
        commit(repo, "fix: x is one")
        problems, notes = release().red_check_problems(repo)
        self.assertEqual(len(problems), 1, (problems, notes))
        self.assertIn("red-check", problems[0])

    def test_on_main_itself_the_commits_since_the_last_tag_are_judged(self) -> None:
        # After a fast-forward the merge-base with main is HEAD: the last tag reachable from HEAD is the base.
        repo = init_repo(self.root / "m")
        (repo / ".agents").mkdir()
        (repo / ".agents/carrier.toml").write_text('carrier = "r-aaaaaa"\n[red_check]\ncode = ["tools/**"]\ntests = ["tests/test_*.py"]\n')
        (repo / "tools").mkdir()
        (repo / "tools/bundle.py").write_text("# " + bundle.RED_CHECK_MARK + "\n")
        commit(repo, "chore: start")
        git(repo, "branch", "-M", "main")
        git(repo, "tag", "-a", "v0.0.1", "-m", "0.0.1")
        (repo / "tools/calc.py").write_text("X = 1\n")
        commit(repo, "fix: x is one")
        problems, notes = release().red_check_problems(repo)
        self.assertEqual(len(problems), 1, (problems, notes))
        self.assertTrue([n for n in notes if "v0.0.1" in n], notes)

    def _main_with_a_fix(self, name: str) -> Path:
        repo = init_repo(self.root / name)
        (repo / ".agents").mkdir()
        (repo / ".agents/carrier.toml").write_text('carrier = "r-aaaaaa"\n[red_check]\ncode = ["tools/**"]\ntests = ["tests/test_*.py"]\n')
        (repo / "tools").mkdir()
        (repo / "tools/bundle.py").write_text("# " + bundle.RED_CHECK_MARK + "\n")
        commit(repo, "chore: start")
        git(repo, "branch", "-M", "main")
        return repo

    def test_a_detached_head_at_main_is_judged_as_main(self) -> None:
        # How CI checks out: a detached HEAD whose merge-base with main is HEAD itself.
        repo = self._main_with_a_fix("d")
        git(repo, "tag", "-a", "v0.0.1", "-m", "0.0.1")
        (repo / "tools/calc.py").write_text("X = 1\n")
        commit(repo, "fix: x is one")
        git(repo, "checkout", "-q", "--detach", "HEAD")
        problems, notes = release().red_check_problems(repo)
        self.assertEqual(len(problems), 1, (problems, notes))
        self.assertTrue([n for n in notes if "v0.0.1" in n], notes)

    def test_only_a_release_tag_is_the_base(self) -> None:
        repo = self._main_with_a_fix("t")
        git(repo, "tag", "-a", "v0.0.1", "-m", "0.0.1")
        (repo / "tools/calc.py").write_text("X = 1\n")
        commit(repo, "fix: x is one")
        git(repo, "tag", "-a", "nightly", "-m", "not a release")
        self.assertEqual(release().review_base(repo)[1], "v0.0.1")

    def test_on_main_with_no_release_tag_check_says_nothing_was_judged(self) -> None:
        repo = self._main_with_a_fix("n")
        (repo / "tools/calc.py").write_text("X = 1\n")
        commit(repo, "fix: x is one")
        R = release()
        self.assertEqual(R.review_base(repo)[0], None)
        problems, notes = R.red_check_problems(repo)
        self.assertEqual(problems, [])
        self.assertTrue([n for n in notes if "red-check" in n and "no base" in n and "judged nothing" in n], notes)
        _, notes = R.baseline_growth(repo)
        self.assertTrue([n for n in notes if "baseline" in n and "no base" in n and "judged nothing" in n], notes)
