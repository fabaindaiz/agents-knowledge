"""The home tool: the build, a release, and carrying it to carriers on the current and the old layout."""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
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

    def test_a_cue_naming_a_product_is_refused(self) -> None:
        (self.home / "meta").mkdir(exist_ok=True)
        (self.home / "meta/product-nouns.txt").write_text("# products\n\nAcmeDB\n")
        nouns = self.R.product_nouns(self.home)
        self.assertEqual(nouns, ["acmedb"])

        def note(cues: list[str]):  # noqa: ANN202
            meta = {"slug": "n", "topic": "t", "claim": "c", "confidence": "measured", "cues": cues}
            return self.R.Note("n", "retired", meta, "", "sources/notes/retired/n.md")

        problems = self.R._note_problems(note(["partial update", "acmedb update"]), nouns)
        self.assertEqual(len(problems), 1)
        self.assertIn("sources/notes/retired/n.md", problems[0])
        self.assertIn("acmedb update", problems[0])
        self.assertIn("say the mechanism", problems[0])
        self.assertEqual(self.R._note_problems(note(["partial update", "dotted path"]), nouns), [])
        self.assertEqual(self.R.product_nouns(self.home / "nowhere"), [])

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
        B.write_checksums(self.agents)

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
        B.write_checksums(self.home / ".agents")
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
        B.write_checksums(repo / ".agents")
        commit(repo, "fork, hidden")

        gathered = self.R.gather([repo], self.root / "out", self.home)

        self.assertIn("knowledge/notes/active/alpha.md: differs from the tagged release", " ".join(gathered["carriers"]["one"]["forked"]))

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
        self.assertIn("# Gather — 1 carriers, 1 not read", text)

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
