"""The carrier tool: verify, the local step, links, sessions, ids, privacy and the workspace.

Every planted leak is assembled at run time, so this file's own source never holds the leak it plants:
the home's check reads this file with the same rules.
"""

from __future__ import annotations

import ast
import contextlib
import hashlib
import io
import json
import math
import re
import shutil
import subprocess
from unittest import mock
from pathlib import Path

from meta.tests.support import NOTE, ROOT, Base, a_proposal, bundle, git, init_repo, make_bundle, old_outbox

B = bundle


def run(*argv: str) -> tuple[int, str]:
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = B.main(list(argv))
    return code, out.getvalue()


def plant(path: Path, text: str) -> None:
    path.write_text(path.read_text() + "\n" + text + "\n")


class Verify(Base):
    def test_a_fresh_bundle_verifies(self) -> None:
        agents = make_bundle(self.root)

        self.assertEqual(B.verify_problems(agents), [])
        code, out = run("verify", str(agents))
        self.assertEqual(code, 0, out)
        self.assertIn("0.0.1 verified", out)

    def test_each_kind_of_problem_fails_it(self) -> None:
        cases = {
            "checksum": lambda a: plant(a / "method/prompt-context.md", "edited"),
            "link": lambda a: (plant(a / "method/prompt-context.md", "[gone](gone.md)"), B.write_checksums(a)),
            "proposal": lambda a: (a / "proposals/p-0123456789.md").write_text("no header\n"),
            "old outbox": lambda a: old_outbox(a),
            "foreign proposal": lambda a: (a_proposal(a), B.write_carrier(a, {"carrier": "r-bbbbbb"})),
            "carrier": lambda a: (a / "carrier.toml").unlink(),
            "invisible": lambda a: (plant(a / "method/prompt-context.md", "hidden \u202e text"), B.write_checksums(a)),
            "incoming": lambda a: (a / "incoming/settings.json").write_text("{}\n"),
            "session": lambda a: ((a / "method/prompt-harvest.md").write_text("# no reads\n"), B.write_checksums(a)),
        }
        for name, damage in cases.items():
            with self.subTest(name=name):
                agents = make_bundle(self.root / name)
                damage(agents)

                self.assertNotEqual(B.verify_problems(agents), [], name)

    def test_a_bundle_from_before_semver_gets_one_line_saying_how_to_update(self) -> None:
        agents = make_bundle(self.root)
        (agents / "README.md").write_text("---\nbundle: agent-guides\nlineage: g-aaaaaa/main\nversion: 21\n---\n# Old\n")

        problems = B.verify_problems(agents)

        self.assertEqual(len(problems), 1)
        self.assertIn("before 0.0.22", problems[0])

    def test_a_release_as_it_arrives_verifies_without_carrier_files(self) -> None:
        agents = make_bundle(self.root)
        (agents / "carrier.toml").unlink()

        self.assertEqual(B.verify_problems(agents, release=True), [])
        self.assertNotEqual(B.verify_problems(agents), [])
        B.write_carrier(agents, {"carrier": "r-bbbbbb"})
        a_proposal(agents)
        problems = "\n".join(B.verify_problems(agents, release=True))
        self.assertIn("carrier.toml: another repository's own file", problems)
        self.assertIn("proposals/p-", problems)

    def test_the_real_bundle_exported_verifies_as_a_release(self) -> None:
        """A release as it travels: the home's own bundle, exported, with no proposals and no carrier file."""
        real = Path(__file__).resolve().parents[2] / ".agents"
        out = self.root / "release"

        B.export(real, out)

        self.assertFalse((out / "carrier.toml").exists())
        self.assertFalse((out / "tracking").exists())
        self.assertEqual(sorted(p.name for p in (out / "proposals").iterdir()), ["README.md", "RECEIVED.md"])
        self.assertEqual(B.verify_problems(out, release=True), [])

    def test_a_release_carrying_what_incoming_refuses_fails_even_with_its_own_checksums(self) -> None:
        real = Path(__file__).resolve().parents[2] / ".agents"
        out = self.root / "release"
        B.export(real, out)
        (out / "CLAUDE.md").write_text("instructions\n")
        (out / "tools/evil.py").write_text("print()\n")
        (out / "u16.md").write_bytes("text".encode("utf-16"))
        B.write_checksums(out)

        problems = "\n".join(B.verify_problems(out, release=True))

        self.assertIn("u16.md: not UTF-8", problems)
        (out / "u16.md").unlink()
        B.write_checksums(out)
        problems = "\n".join(B.verify_problems(out, release=True))
        self.assertIn("CLAUDE.md: assistant", problems)
        self.assertIn("tools/evil.py: a script", problems)

    def test_what_a_carrier_never_publishes_is_not_privacy_checked(self) -> None:
        agents = make_bundle(self.root)
        (agents / "evaluation-2026-01-01-abcdef.md").write_text("Cloned from https://git" + "hub.com/" + "jdoe/ledger.\n")
        (agents / "incoming/offered.md").write_text("Write to " + "jdoe" + "@" + "corp-mail.io\n")

        self.assertEqual(B.verify_problems(agents), [])

    def test_hidden_and_stray_files_are_named(self) -> None:
        agents = make_bundle(self.root)
        (agents / "method/.evil.md").write_text("hidden\n")
        (agents / "proposals/prompt-override.md").write_text("stray\n")
        (agents / "proposals/deeper").mkdir()
        (agents / "proposals/deeper/p-0123456789.md").write_text("stray\n")
        (agents / "proposals/.DS_Store").write_bytes(b"\x00\x00\x00\x01Bud1" + bytes(24))
        (agents / "tracking").mkdir()
        (agents / "tracking/notes.md").write_text("stray\n")
        (agents / "evaluation-x.py").write_text("stray\n")
        (agents / ".DS_Store").write_bytes(b"\x00\x00\x00\x01Bud1" + bytes(24))
        (agents / "method/.DS_Store").write_text("anything but a file browser's\n")

        problems = "\n".join(B.verify_problems(agents))

        self.assertIn("method/.evil.md: a hidden file", problems)
        self.assertIn("proposals/prompt-override.md: not a proposal file", problems)
        self.assertIn("proposals/deeper/p-0123456789.md: not a proposal file", problems)
        self.assertNotIn("proposals/.DS_Store", problems)
        self.assertIn("tracking/notes.md: not a file", problems)
        self.assertIn("evaluation-x.py: not a file", problems)
        self.assertIn("method/.DS_Store: a hidden file", problems)
        self.assertNotIn("\n.DS_Store", "\n" + problems)

    def test_a_carrier_file_without_an_id_or_with_an_unknown_key_fails(self) -> None:
        agents = make_bundle(self.root)
        B.write_carrier(agents, {"adoptd": "2026-01-01"})

        problems = "\n".join(B.verify_problems(agents))

        self.assertIn("missing or not `r-`", problems)
        self.assertIn("unknown key `adoptd`", problems)

    def test_digest_is_a_deprecated_alias(self) -> None:
        agents = make_bundle(self.root)

        code, out = run("digest", str(agents), "--check")

        self.assertEqual(code, 0)
        self.assertIn("deprecated", out)


class LocalStep(Base):
    def test_a_release_offered_in_incoming_is_not_a_change_of_ours(self) -> None:
        repo = self.root / "one"
        agents = make_bundle(repo)
        (agents / "incoming/README.md").write_text("another release's readme\n")

        self.assertEqual(B.check_local(repo), [])

    def test_only_the_carriers_own_files_changed_is_local(self) -> None:
        repo = self.root / "one"
        agents = make_bundle(repo)
        a_proposal(agents)

        self.assertEqual(B.check_local(repo), [])

    def test_a_note_edited_and_committed_is_still_named(self) -> None:
        """Git status saw only uncommitted edits; the checksums see a committed one too."""
        repo = self.root / "one"
        agents = make_bundle(repo)
        plant(agents / "knowledge/notes/active/absence.md", "a local edit")

        self.assertEqual(len(B.check_local(repo)), 1)
        self.assertEqual([n for n, _ in B.check_local_all([repo, self.root / "two" if make_bundle(self.root / "two") else None])], ["one"])


class Links(Base):
    def test_a_link_to_a_missing_file_is_named(self) -> None:
        agents = make_bundle(self.root)
        plant(agents / "method/prompt-context.md", "See [gone](../knowledge/notes/gone.md#part).")

        problems = B.link_problems(agents)

        self.assertEqual(len(problems), 1, problems)
        self.assertIn("links to ../knowledge/notes/gone.md#part, which does not exist", problems[0])

    def test_a_link_out_of_the_bundle_is_named(self) -> None:
        """In the home it would find the full notes; in a carrier it finds nothing."""
        agents = make_bundle(self.root)
        plant(agents / "method/prompt-context.md", "The [full note](../../sources/notes/active/x.md).")

        problems = B.link_problems(agents)

        self.assertEqual(len(problems), 1, problems)
        self.assertIn("outside the bundle", problems[0])

    def test_what_is_not_a_relative_pointer_is_not_checked(self) -> None:
        agents = make_bundle(self.root)
        plant(agents / "method/prompt-context.md", (
            "[web](https://example.com/x) [mail](mailto:a@example.com) [here](#anchor)"
            " `[code](gone.md)` [ok](prompt-bootstrap.md#bootstrap)\n"
            "\n~~~text\n[paste](gone.md)\n~~~\n\n```\n[example](gone.md)\n```"))
        (agents / "incoming/offered.md").write_text("[x](gone.md)\n")
        (agents / "evaluation-2026-01-01.md").write_text("[x](gone.md)\n")

        self.assertEqual(B.link_problems(agents), [])

    def test_an_active_or_review_note_no_index_links_to_is_named(self) -> None:
        agents = make_bundle(self.root)
        for state in ("active", "review"):
            (agents / f"knowledge/notes/{state}").mkdir(exist_ok=True)
            (agents / f"knowledge/notes/{state}/orphan-{state}.md").write_text(NOTE.format(slug=f"orphan-{state}"))

        problems = B.reachability_problems(agents)

        self.assertEqual(len(problems), 2, problems)
        self.assertTrue(problems[0].startswith("knowledge/notes/active/orphan-active.md"))


class Sessions(Base):
    DOC = "---\nx: 1\n---\n# Top\n\n## A\n\none\n\n### A.1\n\ntwo\n\n```text\n## B\n```\n\n## B\n\nthree\n"

    def test_a_section_runs_to_the_next_heading_of_its_level(self) -> None:
        path = self.root / "doc.md"
        path.write_text(self.DOC)

        self.assertEqual(B.section(path, "A"), "## A\n\none\n\n### A.1\n\ntwo\n\n```text\n## B\n```\n\n")
        self.assertEqual(B.section(path, "B"), "## B\n\nthree\n")
        self.assertIsNone(B.section(path, "C"))

    def test_the_sessions_are_the_carriers_and_read_from_the_methods_reads_lists(self) -> None:
        agents = make_bundle(self.root)

        sessions, missing = B.sessions_of(agents)

        self.assertEqual(missing, [])
        self.assertEqual(set(sessions), {"coding", "consult", "evaluate", "bootstrap", "update", "harvest", "review"})
        self.assertEqual(sessions["coding"], [("method/prompt-bootstrap.md", "The session loop"), ("knowledge/INDEX.md", None)])
        self.assertEqual(B.reads_lists("Reads:\n- a.md §One §Two, with a comma\n\nReads:\n- b.md\n"),
                         [[("a.md", "One"), ("a.md", "Two, with a comma")], [("b.md", None)]])

    def test_a_heading_the_file_does_not_have_fails_the_check(self) -> None:
        agents = make_bundle(self.root)

        problems = B.session_problems(agents, {"s": [("method/prompt-context.md", "Nowhere"), ("method/prompt-none.md", None)]})

        self.assertEqual(len(problems), 2, problems)

    def test_the_report_counts_files_folders_sessions_and_budgets(self) -> None:
        agents = make_bundle(self.root)
        context = (agents / "method/prompt-context.md").read_text()

        data = B.report(agents, {"s": [("method/prompt-context.md", None)]})

        self.assertEqual(data["total"]["files"], len(B.shipped(agents)))
        self.assertEqual(data["folders"]["knowledge/notes/active"]["files"], 2)
        self.assertEqual(data["sessions"]["s"]["tokens_estimate"], math.ceil(len(context) / 4))
        self.assertEqual(B.budget_problems(agents), [])
        code, out = run("report", str(agents), "--json")
        self.assertIn("folders", json.loads(out))

    def test_the_reviewers_load_counts_its_own_definition(self) -> None:
        agents = make_bundle(self.root)

        parts = B.sessions_of(agents)[0]["review"]

        self.assertEqual(parts[0], ("agents/knowledge-reviewer.md", None))
        self.assertIn(("knowledge/INDEX.md", None), parts)

    def test_a_card_the_index_does_not_link_is_unreachable(self) -> None:
        agents = make_bundle(self.root)
        (agents / "knowledge/cards").mkdir()
        (agents / "knowledge/cards/orphan.md").write_text("# orphan\n")

        self.assertIn("knowledge/cards/orphan.md: a card", "\n".join(B.reachability_problems(agents)))

    def test_a_coding_session_over_its_budget_fails_the_check(self) -> None:
        agents = make_bundle(self.root)
        (agents / "knowledge/INDEX.md").write_text("x" * 4 * (B.BUDGETS["coding"] + 1))

        self.assertIn("coding session", "\n".join(B.budget_problems(agents)))


class CarrierIds(Base):
    def test_a_minted_id_is_random_typed_and_stored_in_the_carrier_file(self) -> None:
        repo = self.root / "one"
        (repo / ".agents").mkdir(parents=True)

        minted = B.mint_carrier_id(repo, today="2026-01-01")

        self.assertRegex(minted, r"^r-[0-9a-f]{6}$")
        self.assertEqual(B.read_carrier(repo / ".agents")["carrier"], minted)
        self.assertEqual(B.read_carrier(repo / ".agents")["adopted"], "2026-01-01")
        with self.assertRaises(B.RefusedError):
            B.mint_carrier_id(repo)

    def test_a_missing_or_malformed_id_is_refused_with_what_to_do(self) -> None:
        repo = self.root / "one"
        agents = make_bundle(repo)
        B.write_carrier(agents, {"adopted": "2026-01-01"})
        with self.assertRaisesRegex(B.RefusedError, "carrier-id --mint"):
            B.repo_carrier_id(repo)
        B.write_carrier(agents, {"carrier": "r-xyz"})
        with self.assertRaises(B.RefusedError):
            B.repo_carrier_id(repo)

    def test_a_bundle_copied_with_its_id_is_refused(self) -> None:
        one, two = self.root / "one", self.root / "two"
        make_bundle(one), make_bundle(two)

        with self.assertRaisesRegex(B.RefusedError, "both store"):
            B.carrier_ids([one, two])


class RecordIds(Base):
    def test_a_record_id_is_typed_carrier_scoped_and_derived(self) -> None:
        minted = B.record_id("d", "Keep the port out of the id.", "r-abcdef")

        self.assertRegex(minted, r"^d-abcdef-[0-9a-f]{6}$")
        self.assertEqual(minted[-6:], hashlib.sha256(b"Keep the port out of the id.").hexdigest()[:6])
        self.assertEqual(B.record_id("i", "  one\n two\tthree ", "r-abcdef"), B.record_id("i", "one two three", "r-abcdef"))
        with self.assertRaises(B.RefusedError):
            B.record_id("x", "text", "r-abcdef")

    def test_the_command_takes_the_carrier_from_the_repository(self) -> None:
        repo = self.root / "one"
        make_bundle(repo)

        code, out = run("id", "d", "two", "words", "--repo", str(repo))

        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), B.record_id("d", "two words", "r-abcdef"))

    def write(self, name: str, text: str) -> Path:
        path = self.root / name
        path.write_text(text)
        return path

    def test_a_record_defined_twice_is_named_and_a_citation_may_repeat(self) -> None:
        one = self.write("one.md", "| d-abcdef-111111 | a decision |\n\nSee d-abcdef-111111, and again d-abcdef-111111.\n")
        two = self.write("two.md", "## 2026-01-01 · s-abcdef-222222 — a session\n\n| d-abcdef-111111 | the same, again |\n")

        errors, warnings, counts = B.record_id_check([one, two], "r-abcdef")

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("defined twice", errors[0])
        self.assertEqual((counts["definitions"], counts["citations"]), (3, 2))

    def test_a_malformed_id_is_named_and_the_first_scheme_is_not(self) -> None:
        path = self.write("log.md", "| d-abcdef-12345 | a digit dropped |\n| D-ABCDEF-123456 | a case changed |\n"
                                    "| d-abcdef-017 | the first scheme |\n\nnot an id: re-run, i-th, s-curve\n")

        errors, _, counts = B.record_id_check([path], "r-abcdef")

        self.assertEqual(len(errors), 2, errors)
        self.assertEqual(counts["legacy"], 1)

    def test_a_definition_under_another_carriers_id_is_a_warning_and_fences_are_examples(self) -> None:
        path = self.write("log.md", "| d-fedcba-333333 | copied from elsewhere |\n\n~~~text\n| d-abcdef-5 |\n~~~\n")

        errors, warnings, _ = B.record_id_check([path], "r-abcdef")

        self.assertEqual((errors, len(warnings)), ([], 1))


class Privacy(Base):
    PLANTED = {
        "email": "Write to " + "jdoe" + "@" + "corp-mail.io" + " for access.",
        "home-path": "The script lived in " + "/Us" + "ers/jdoe/src/tool.",
        "forge-url": "Cloned from https://git" + "hub.com/" + "jdoe/ledger.",
        "chosen-id": "Tracked as " + "PAY" + "-1042" + " in the board.",
        "currency": "It saved " + "$" + "12" + ",400" + " a month.",
        "timezone": "Runs at 03:00 " + "UTC" + "-3" + " every night.",
        "version-pin": "Pinned to " + "somelib" + "==" + "2.4.1" + " since then.",
        "id-beside-domain": "r-" + "4c1d2e" + " is the " + "pay" + "ments service.",
    }

    @staticmethod
    def rules(report, level: str = "FAIL") -> list[str]:  # noqa: ANN001
        return [f.rule for f in report.findings if f.level == level]

    def test_a_clean_bundle_passes(self) -> None:
        report = B.privacy_check(make_bundle(self.root))

        self.assertEqual(report.findings, [])
        self.assertTrue(report.partial)

    def test_the_terms_read_are_counted_and_fingerprinted(self) -> None:
        terms = self.root / "terms.txt"
        terms.write_text("# private\nZeta\n  alpha \nzeta\n\n")

        code, out = run("privacy", str(make_bundle(self.root)), "--terms", str(terms))

        fingerprint = hashlib.sha256("alpha\nzeta".encode()).hexdigest()[:8]
        self.assertEqual(code, 0, out)
        self.assertIn(f"private terms: 2 read from {terms}, list {fingerprint}", out)
        self.assertNotIn("partial", out)

    def test_no_terms_list_is_a_warning_never_a_silent_pass(self) -> None:
        code, out = run("privacy", str(make_bundle(self.root)))

        self.assertEqual(code, 0, out)  # a warning, not a failure
        self.assertIn("! WARN partial: no private-terms list on this machine", out)
        self.assertIn("1 WARN", out.strip().split("\n")[-1])
        self.assertIn("partial", out.strip().split("\n")[-1])

    def test_each_rule_fails_on_its_planted_leak(self) -> None:
        for rule, line in self.PLANTED.items():
            with self.subTest(rule=rule):
                agents = make_bundle(self.root / rule)
                plant(agents / "method/prompt-context.md", line)

                report = B.privacy_check(agents)

                self.assertEqual(self.rules(report), [rule], report.findings)

    def test_a_payment_card_beside_an_id_fails_and_the_bundles_card_does_not(self) -> None:
        rid = "r-" + "4c1d2e"
        for wording, rule in (("a card issuing platform", ["id-beside-domain"]), ("prepaid cards", ["id-beside-domain"]),
                              ("debit-card settlement", ["id-beside-domain"]), ("card-present sales", ["id-beside-domain"]),
                              ("its knowledge card", [])):
            with self.subTest(wording=wording):
                agents = make_bundle(self.root / wording.replace(" ", "-"))
                plant(agents / "method/prompt-context.md", f"{rid} runs {wording}.")

                self.assertEqual(self.rules(B.privacy_check(agents)), rule)

    def test_a_proposal_is_read_too(self) -> None:
        agents = make_bundle(self.root)
        a_proposal(agents, self.PLANTED["email"])

        self.assertEqual(self.rules(B.privacy_check(agents)), ["email"])

    def test_a_code_name_fails_in_the_evidence_and_nowhere_else(self) -> None:
        agents = make_bundle(self.root)
        name = "settle" + "Amount"
        plant(agents / "knowledge/notes/active/absence.md", f"## Why it works\n\nThe field `{name}` held it.\n\n## Evidence\n\n"
                                                            f"The field `{name}` held it.\n\n## Literature\n\nThe field `{name}` held it.")
        a_proposal(agents, f"The field `{name}` held it.")

        report = B.privacy_check(agents)

        self.assertEqual(self.rules(report), ["code-identifier"] * 2, report.findings)

    def test_the_homes_records_are_scoped_as_in_a_bundle(self) -> None:
        """`meta/tracking/` is evidence and `sources/references.md` is literature, read by path."""
        name = "settle" + "Amount"
        (self.root / "meta/tracking").mkdir(parents=True)
        (self.root / "sources").mkdir()
        evidence = self.root / "meta/tracking/candidates.md"
        evidence.write_text(f"The field `{name}` held it.\n")
        references = self.root / "sources/references.md"
        references.write_text(self.PLANTED["version-pin"] + "\n")
        prose = self.root / "meta/roadmap.md"
        prose.write_text(f"The field `{name}` held it.\n")

        report = B.privacy_check(paths=[evidence, references, prose])

        self.assertEqual([(f.rule, Path(f.where.split(":")[0]).name) for f in report.findings],
                         [("code-identifier", "candidates.md")])

    def test_this_bundles_versions_and_named_standards_are_not_pins(self) -> None:
        agents = make_bundle(self.root)
        plant(agents / "method/prompt-context.md", "The release 0.0.22, tag v0.0.22, follows Semantic Versioning 2.0.0 "
                                                  "and Keep a Changelog 1.1.0.")

        self.assertEqual(B.privacy_check(agents).findings, [])

    def test_literature_is_exempt_from_versions_counts_and_quotes(self) -> None:
        agents = make_bundle(self.root)
        pin = self.PLANTED["version-pin"]
        plant(agents / "knowledge/notes/active/absence.md", f"## Literature\n\n{pin} Read 4 " + "of 7 " + "of 12" + ",345 pages.")
        (agents / "references.md").write_text(f"{pin}\n")
        plant(agents / "knowledge/notes/active/a-check.md", f"## What it costs\n\n{pin}")

        report = B.privacy_check(agents)

        self.assertEqual([(f.rule, f.where.split(":")[0]) for f in report.findings],
                         [("version-pin", "knowledge/notes/active/a-check.md")])

    def test_warnings_are_advisory(self) -> None:
        agents = make_bundle(self.root)
        a_proposal(agents, "It failed 7 " + "of 12 runs over 12" + ',480 rows: "the queue was never drained at all".',
                   lacks="refused: already the default behaviour here")

        report = B.privacy_check(agents)

        self.assertEqual(sorted(self.rules(report, "WARN")), ["exact-count", "n-of-m", "quote"])
        self.assertEqual(report.failures, [])

    def test_a_standards_number_is_not_a_count(self) -> None:
        agents = make_bundle(self.root)
        plant(agents / "knowledge/notes/active/absence.md", "Unlike RFC 7396 / 6902 and ISO 8601, it read 7" + ",396 rows.")

        report = B.privacy_check(agents)

        self.assertEqual([f.rule for f in report.findings], ["exact-count"])

    def test_a_private_term_fails_and_is_not_repeated(self) -> None:
        terms = self.root / "config/agent-guides/private-terms.txt"
        terms.parent.mkdir(parents=True)
        terms.write_text("Zebra" + "corp\n\n")
        agents = make_bundle(self.root / "b")
        plant(agents / "method/prompt-context.md", "Built for " + "ZEBRA" + "CORP" + " last year.")

        report = B.privacy_check(agents)

        self.assertEqual(self.rules(report), ["private-term"])
        self.assertNotIn("ebra", " ".join(f.match for f in report.findings))
        with self.assertRaises(B.RefusedError):
            B.privacy_check(agents, terms_file=self.root / "no-such-terms.txt")

    def test_inside_a_repository_its_own_name_is_no_leak_of_itself(self) -> None:
        own, remote, other = "Quiet" + "fox", "Amber" + "gate", "Zebra" + "corp"
        terms = self.root / "config/agent-guides/private-terms.txt"
        terms.parent.mkdir(parents=True)
        terms.write_text(f"{other}\n{own}\n{remote}\n")
        repo = init_repo(self.root / own.lower())
        git(repo, "remote", "add", "origin", f"git@example.com:someone/{remote}.git")
        agents = make_bundle(repo)
        plant(agents / "method/prompt-context.md", f"The {own} rules, as {remote} keeps them.")
        (repo / "README.md").write_text(f"# {own}\n")
        (self.root / "elsewhere.md").write_text(f"About {own}.\n")

        report = B.privacy_check(agents)

        self.assertEqual(report.failures, [])
        said = "\n".join(report.notes())
        self.assertIn("lines 2, 3 of the terms file skipped inside the repository they name", said)
        self.assertNotIn(own.lower(), said.lower())
        with self.subTest("another private term still fails there"):
            plant(agents / "method/prompt-context.md", f"Built for {other}.")
            self.assertEqual(self.rules(B.privacy_check(agents)), ["private-term"])
        with self.subTest("a proposal leaves the repository, so it keeps every term"):
            agents = make_bundle(init_repo(self.root / "two" / own.lower()))
            a_proposal(agents, f"Seen once in {own}.")
            self.assertEqual(self.rules(B.privacy_check(agents)), ["private-term"])
        with self.subTest("a file outside the repository keeps every term"):
            report = B.privacy_check(paths=[repo / "README.md", self.root / "elsewhere.md"])
            self.assertEqual([f.where for f in report.failures], [f"{self.root / 'elsewhere.md'}:1"])
        with self.subTest("the home publishes what it holds, so it keeps every term"):
            home = init_repo(self.root / "three" / own.lower())
            for rel in ("sources/bundle/tools/bundle.py", "meta/tools/release.py"):
                (home / rel).parent.mkdir(parents=True)
                (home / rel).write_text("")
            plant(make_bundle(home) / "method/prompt-context.md", f"The {own} rules.")
            self.assertEqual(self.rules(B.privacy_check(home / ".agents")), ["private-term"])

    def test_a_waiver_suppresses_its_line_and_is_listed(self) -> None:
        agents = make_bundle(self.root)
        marker = "<!-- privacy-" + "allow: the maintainer asked, 2026-01-01 -->"
        plant(agents / "method/prompt-context.md", self.PLANTED["email"] + " " + marker)
        plant(agents / "method/prompt-context.md", self.PLANTED["currency"] + " <!-- privacy-" + "allow: -->")

        report = B.privacy_check(agents)

        self.assertEqual(sorted(self.rules(report)), ["allow-without-reason", "currency"])
        self.assertEqual(len(report.allowances), 1)

    def test_what_is_not_a_leak_is_not_reported(self) -> None:
        agents = make_bundle(self.root)
        plant(agents / "method/prompt-context.md", "\n".join([
            "Mail t" + "@" + "example.com, see https://git" + "hub.com/owner/repo and " + "/Us" + "ers/you/code.",
            "SHA" + "-256, UTF" + "-16, RFC" + "-2119 and ESD-TR-73-51 are citations; " + "`awk '{print $1}'` is a shell.",
            "Released 2026-09-24 at 10:00; " + "r-" + "abcdef" + " is the payments example; about 9 % and hundreds a month.",
        ]))

        self.assertEqual(B.privacy_check(agents).findings, [])

    def test_the_tools_pass_their_own_check(self) -> None:
        root = Path(__file__).resolve().parents[2]
        paths = [root / ".agents/tools/bundle.py", root / "meta/tools/release.py", Path(__file__)]

        self.assertEqual(B.privacy_check(paths=paths).failures, [])


class Workspace(Base):
    def test_the_declared_workspace_wins_and_the_manifest_is_the_fallback(self) -> None:
        one = self.root / "one"
        make_bundle(one)
        manifest = self.root / "carriers.toml"
        manifest.write_text(f'carriers = ["{one}"]\n')

        self.assertEqual(B.workspace([str(one)], manifest).repos, [one])
        self.assertEqual(B.workspace([], manifest).repos, [one])
        self.assertFalse(B.workspace([], manifest).declared)

    def test_a_command_that_writes_never_infers_its_scope(self) -> None:
        one = self.root / "one"
        make_bundle(one)
        manifest = self.root / "carriers.toml"
        manifest.write_text(f'carriers = ["{one}"]\n')

        with self.assertRaises(B.UndeclaredScopeError):
            B.workspace([], manifest, writing=True)

    def test_an_empty_outside_list_says_whether_it_means_anything(self) -> None:
        one, two = self.root / "one", self.root / "two"
        make_bundle(one), make_bundle(two)
        manifest = self.root / "carriers.toml"
        manifest.write_text(f'carriers = ["{one}", "{two}"]\n')

        self.assertEqual(B.outside(B.workspace([str(one)], manifest), manifest), [str(two)])
        self.assertIn("scope taken from the manifest", B._scope_report(B.workspace([], manifest), "written")[0])

    def test_a_path_that_carries_no_bundle_is_refused(self) -> None:
        (self.root / "plain").mkdir()

        with self.assertRaises(B.NotACarrierError):
            B.workspace([str(self.root / "plain")], None)


class ChangelogCommand(Base):
    def test_it_prints_what_changed_since_a_version(self) -> None:
        agents = make_bundle(self.root)

        code, out = run("changelog", "--since", "0.0.0", str(agents))

        self.assertEqual(code, 0)
        self.assertIn("## [0.0.1]", out)

    def test_a_proposal_is_written_listed_and_never_rewritten(self) -> None:
        agents = make_bundle(self.root)

        code, out = run("propose", "--tree", str(agents), "--kind", "knowledge", "--target", "a-thing", "--claim",
                        "A claim.", "--evidence", "Seen once.", "--lacks", "a second occurrence", "--seen", "2026-01-02")

        self.assertEqual(code, 0, out)
        path = next((agents / "proposals").glob("p-*.md"))
        text = path.read_text()
        self.assertTrue(text.startswith("---\n# bundle-proposal:"))
        meta, body = B.read_frontmatter(text)
        self.assertEqual((meta["carrier"], meta["base"], meta["proposal"]), ("r-abcdef", "0.0.1", path.stem))
        self.assertEqual(meta["digest"], hashlib.sha256((agents / "SHA256SUMS").read_bytes()).hexdigest()[:12])
        self.assertIn("## Evidence\n\nSeen once.", body)
        self.assertEqual(B.verify_problems(agents), [])
        code, again = run("propose", "--tree", str(agents), "--kind", "knowledge", "--target", "a-thing", "--claim",
                          "A claim.", "--evidence", "Seen once.", "--lacks", "a second occurrence", "--seen", "2026-01-02")
        self.assertEqual(code, 2, again)
        self.assertIn("already proposed", again)
        code, listed = run("proposals", str(agents))
        self.assertIn(f"{path.stem}  knowledge", listed)
        self.assertIn("waiting for the home", listed)

    def test_a_proposal_from_a_file_keeps_what_a_shell_would_rewrite(self) -> None:
        agents = make_bundle(self.root)
        draft = self.root / "draft.md"
        draft.write_text("A default of `$(none)` widens the scope.\n\n## Evidence\n\nThe field `limit` was `None`, twice.\n")

        code, out = run("propose", "--tree", str(agents), "--kind", "knowledge", "--target", "a-thing", "--from", str(draft))

        self.assertEqual(code, 0, out)
        (found,), _ = B.proposals_of(agents)
        self.assertEqual((found.claim, found.evidence), ("A default of `$(none)` widens the scope.", "The field `limit` was `None`, twice."))
        draft.write_text("No heading here.\n")
        code, out = run("propose", "--tree", str(agents), "--kind", "knowledge", "--target", "other", "--from", str(draft))
        self.assertEqual(code, 2, out)
        self.assertIn("no `## Evidence` heading", out)

    def test_an_incomplete_proposal_is_refused_before_it_is_written(self) -> None:
        agents = make_bundle(self.root)

        with self.assertRaisesRegex(B.RefusedError, "verdict"):
            a_proposal(agents, kind="experiment", verdict="maybe", where="a service")
        self.assertEqual(list((agents / "proposals").glob("p-*.md")), [])

    def test_a_hand_edited_proposal_is_named(self) -> None:
        agents = make_bundle(self.root)
        path = a_proposal(agents)
        path.write_text(path.read_text().replace("lacks: a second occurrence", "lacks: \"\""))
        (agents / "proposals/p-0000000000.md").write_text(path.read_text())

        problems = "\n".join(B.verify_problems(agents))

        self.assertIn("`lacks` is empty", problems)
        self.assertIn("p-0000000000.md: its `proposal` field is", problems)

    def test_the_old_outbox_becomes_one_proposal_per_row_and_nothing_is_lost(self) -> None:
        agents = make_bundle(self.root)
        old_outbox(agents, ["| extends absence — a new boundary | K | nothing | a service, twice | 2026-01-03 |",
                            "| weak-idea — too narrow | M | refused: already the default | here | 2026-01-04 or earlier |"],
                   ["| 2026-01-05 | a-check | a batch job | planted a fault | the check failed | confirms |"])
        self.assertIn("convert its rows", "\n".join(B.verify_problems(agents)))

        code, out = run("proposals", "--from-outbox", str(agents))

        self.assertEqual(code, 0, out)
        self.assertFalse((agents / "tracking").exists())
        found, problems = B.proposals_of(agents)
        self.assertEqual(problems, [])
        by_target = {p.target: p for p in found}
        self.assertEqual(set(by_target), {"absence", "weak-idea", "a-check"})
        self.assertEqual((by_target["absence"].action, by_target["absence"].claim), ("extends", "a new boundary"))
        self.assertEqual(by_target["weak-idea"].lacks, "refused: already the default")
        self.assertEqual((by_target["weak-idea"].seen, by_target["weak-idea"].evidence),
                         ("2026-01-04", "here (First seen: 2026-01-04 or earlier)"))
        self.assertEqual((by_target["a-check"].kind, by_target["a-check"].verdict, by_target["a-check"].evidence),
                         ("experiment", "confirms", "the check failed"))
        self.assertEqual(B.verify_problems(agents), [])

    def test_an_aligned_table_and_rows_after_a_blank_line_are_all_converted(self) -> None:
        agents = make_bundle(self.root)
        (agents / "tracking").mkdir()
        (agents / "tracking/candidates.md").write_text(
            "# Candidates this repository offers\n\n"
            "| Candidate                  | Kind | Lacks   | Evidence | First seen |\n"
            "| -------------------------- | ---- | ------- | -------- | ---------- |\n"
            "| first-idea — one           | K    | nothing | here     | 2026-01-02 |\n\n"
            "| second-idea — two          | M    | nothing | there    | 2026-01-03 |\n")

        written = B.convert_outbox(agents)

        self.assertEqual(len(written), 2)
        self.assertEqual(sorted(p.target for p in B.proposals_of(agents)[0]), ["first-idea", "second-idea"])

    def test_text_that_is_not_a_row_stops_the_conversion_before_anything_is_removed(self) -> None:
        agents = make_bundle(self.root)
        old_outbox(agents, ["| kept — a claim | K | nothing | here | 2026-01-02 |"])
        plant(agents / "tracking/candidates.md", "A note the carrier wrote under the table.")

        with self.assertRaisesRegex(B.RefusedError, "would be removed unread"):
            B.convert_outbox(agents)

        self.assertTrue((agents / "tracking/candidates.md").is_file())
        self.assertEqual(list((agents / "proposals").glob("p-*.md")), [])

    def test_every_row_shape_becomes_a_proposal_that_reads_whole(self) -> None:
        agents = make_bundle(self.root)
        old_outbox(agents, ["| **Extends** `absence` — a new boundary | k | nothing | a service | 2026-01-02 |",
                            "| **A claim in bold, with no slug at all.** | K / M | a number | a tool | 2026-01-03 |",
                            "| undated — a claim | K | nothing | somewhere | once, long ago |"],
                   ["| 2026-01-05 | a-check | a batch job | planted a fault | ratio a|b held | confirms |",
                    "| 2026-01-05 | a-check | a service with a queue | planted a fault | it failed | confirms |",
                    "| 2026-01-05 | a-check | a command-line tool | planted a fault | it passed | falsifies |"])

        B.convert_outbox(agents)

        found, problems = B.proposals_of(agents)
        self.assertEqual(problems, [])
        self.assertEqual(len(found), 6)
        by = {(p.target, p.where): p for p in found}
        self.assertEqual(by[("absence", "")].action, "extends")
        bold = next(p for p in found if p.target.startswith("a-claim-in-bold"))
        self.assertEqual(bold.kind, "knowledge")
        self.assertIn("Kind: K / M", bold.evidence)
        undated = next(p for p in found if p.target == "undated")
        self.assertEqual(undated.seen, "unknown")
        self.assertIn("First seen: once, long ago", undated.evidence)
        with mock.patch.object(B.datetime, "date", wraps=B.datetime.date) as later:
            later.today.return_value = B.datetime.date(2030, 1, 1)
            self.assertEqual(B.row_proposal("tracking/candidates.md", ["undated — a claim", "K", "nothing", "somewhere",
                                                                      "once, long ago"], "r-abcdef").id, undated.id)
        piped = by[("a-check", "a batch job")]
        self.assertEqual((piped.evidence, piped.verdict), ("ratio a | b held", "confirms"))
        self.assertEqual(by[("a-check", "a command-line tool")].verdict, "falsifies")
        self.assertEqual(B.verify_problems(agents), [])

    def test_a_table_that_is_not_utf8_or_holds_a_heading_is_never_converted_wrong(self) -> None:
        agents = make_bundle(self.root)
        old_outbox(agents, ["| x — ## Evidence | K | nothing | here | 2026-01-02 |"])
        B.convert_outbox(agents)
        found, problems = B.proposals_of(agents)
        self.assertEqual((problems, found[0].claim), ([], "\\## Evidence"))

        latin = make_bundle(self.root / "latin")
        old_outbox(latin)
        with (latin / "tracking/candidates.md").open("ab") as f:
            f.write("| caf\u00e9 - a claim | K | nothing | here | 2026-01-02 |\n".encode("latin-1"))
        with self.assertRaisesRegex(B.RefusedError, "not UTF-8"):
            B.convert_outbox(latin)
        self.assertTrue((latin / "tracking/candidates.md").is_file())

    def test_a_proposal_edited_after_it_was_written_is_named_and_never_pruned(self) -> None:
        agents = make_bundle(self.root)
        path = a_proposal(agents, "Seen once.")
        path.write_text(path.read_text().replace("Seen once.", "Seen five times."))
        (agents / "proposals/RECEIVED.md").write_text(
            f"# Received\n\n{B.RECEIVED_HEADER}\n|---|---|---|\n| `{path.stem}` | 0.0.2 | queued as `a-thing` |\n")

        self.assertIn("edited after it was written", "\n".join(B.verify_problems(agents)))
        self.assertEqual(B.prune_proposals(agents), [])
        self.assertTrue(path.exists())

    def test_header_values_read_back_as_written(self) -> None:
        for value in ("del \x7f here", "next \x85 line", "tag \U000e0041 char", "zero\u200bwidth", "refused: a reason"):
            with self.subTest(value=ascii(value)):
                block = B.dump_frontmatter({"where": value}, plain=True)
                self.assertEqual(B.read_frontmatter(block + "\n")[0]["where"], value)
                self.assertTrue(block.isascii() or "\u200b" not in block)

    def test_prune_removes_only_what_the_release_lists_as_received(self) -> None:
        agents = make_bundle(self.root)
        heard, waiting = a_proposal(agents), a_proposal(agents, target="another")
        (agents / "proposals/RECEIVED.md").write_text(
            f"# Received\n\n{B.RECEIVED_HEADER}\n|---|---|---|\n| `{heard.stem}` | 0.0.2 | queued as `a-thing` |\n")

        code, out = run("proposals", "--prune", str(agents))

        self.assertEqual(code, 0, out)
        self.assertIn(f"{heard.stem}: queued as `a-thing`", out)
        self.assertFalse(heard.exists())
        self.assertTrue(waiting.exists())

    def test_a_pack_carries_proposals_and_nothing_else(self) -> None:
        import tarfile

        agents = make_bundle(self.root)
        path = a_proposal(agents)
        pack = self.root / "pack.tar"

        code, out = run("proposals", "--pack", str(pack), str(agents))

        self.assertEqual(code, 0, out)
        self.assertEqual(B.read_pack(pack), {path.name: path.read_text()})
        evil = self.root / "evil.tar"
        with tarfile.open(evil, "w") as archive:
            archive.add(agents / "tools/bundle.py", arcname="proposals/../../tools/bundle.py")
        with self.assertRaisesRegex(B.RefusedError, "not a proposal file"):
            B.read_pack(evil)
        twice = self.root / "twice.tar"
        with tarfile.open(twice, "w") as archive:
            archive.add(path, arcname=f"proposals/{path.name}")
            archive.add(path, arcname=path.name)
        with self.assertRaisesRegex(B.RefusedError, "twice"):
            B.read_pack(twice)


class OldInterpreter(Base):
    """Under a Python older than 3.11 each tool refuses in one line, before an import that needs 3.11 fails."""

    TOOLS = (ROOT / "sources/bundle/tools/bundle.py", ROOT / "meta/tools/release.py")

    def test_the_version_check_comes_before_every_import_but_sys(self) -> None:
        for path in self.TOOLS:
            with self.subTest(tool=path.name):
                body = ast.parse(path.read_text(encoding="utf-8")).body
                check = next(i for i, node in enumerate(body) if isinstance(node, ast.If) and "version_info" in ast.unparse(node.test))
                imports = [i for i, node in enumerate(body) if isinstance(node, (ast.Import, ast.ImportFrom))
                           and not (isinstance(node, ast.ImportFrom) and node.module == "__future__")
                           and not (isinstance(node, ast.Import) and [a.name for a in node.names] == ["sys"])]
                self.assertLess(check, min(imports), "an import runs before the version check")
                self.assertIn("python3.11", ast.unparse(body[check]), "the refusal says how to run a 3.11+ interpreter")

    def test_an_old_interpreter_is_refused_in_one_line(self) -> None:
        def version(exe: str) -> tuple[int, int]:
            out = subprocess.run([exe, "-c", "import sys; print(*sys.version_info[:2])"], capture_output=True, text=True).stdout
            return tuple(int(x) for x in out.split()) if out.strip() else (99, 0)

        old = next((exe for exe in (shutil.which(n) for n in ("python3.9", "python3.10", "/usr/bin/python3")) if exe and version(exe) < (3, 11)), None)
        if old is None:
            self.skipTest("no Python older than 3.11 on this machine")
        for path in self.TOOLS:
            with self.subTest(tool=path.name):
                result = subprocess.run([old, str(path), "--help"], capture_output=True, text=True)

                said = (result.stdout + result.stderr).strip()
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("Traceback", said)
                self.assertEqual(len(said.split("\n")), 1, said)
                self.assertIn(".".join(map(str, version(old))), said)
                self.assertIn("python3.11", said)


class MethodTemplates(Base):
    def test_every_record_heading_the_method_templates_is_read_as_a_definition_by_ids(self) -> None:
        # Three carriers wrote a roadmap heading as the template showed it, and `ids` did not read it.
        text = (ROOT / "sources/bundle/method/prompt-context.md").read_text(encoding="utf-8")
        headings = [line for line in text.split("\n") if line.startswith("#") and "-<repo6>-<content6>" in line]
        self.assertGreaterEqual(len(headings), 3)
        for number, line in enumerate(headings):
            with self.subTest(heading=line):
                path = self.root / f"record-{number}.md"
                path.write_text(re.sub(r"\b([dis])-<repo6>-<content6>", r"\1-abcdef-123456", line) + "\n")

                errors, _, counts = B.record_id_check([path], None)

                self.assertEqual((errors, counts["definitions"]), ([], 1))


class UserDenies(Base):
    """A deny rule in the user's own assistant settings reaches every repository: it merges with the project's."""

    def a_repo(self, denies: list[str]) -> Path:
        repo = init_repo(self.root / "repo")
        make_bundle(repo)
        (repo / "docs").mkdir()
        (repo / "docs/guide.md").write_text("# Guide\n")
        (repo / ".env").write_text("A=1\n")
        git(repo, "add", "-A")
        git(repo, "commit", "-q", "-m", "start")
        (self.root / "user-settings.json").write_text(json.dumps({"permissions": {"deny": denies}}))
        return repo

    def test_a_user_deny_that_covers_a_committed_file_is_warned(self) -> None:
        repo = self.a_repo(["Read(./.env)", "Edit(docs/**)", "Read(~/.ssh/id_*)", "Bash(rm *)", "Edit(/docs/**)"])

        with mock.patch.dict("os.environ", {"AGENT_GUIDES_USER_SETTINGS": str(self.root / "user-settings.json")}):
            warnings = B.user_deny_warnings(repo)
            code, out = run("verify", str(repo / ".agents"))

        self.assertEqual(len(warnings), 2, warnings)
        self.assertIn("Read(./.env)", warnings[0])
        self.assertIn("Edit(docs/**)", warnings[1])
        self.assertIn("docs/guide.md", warnings[1])
        self.assertTrue(all("merge" in w for w in warnings))
        self.assertEqual(code, 0, out)  # a warning, never a failure
        self.assertIn("! user deny `Edit(docs/**)`", out)

    def test_an_absolute_rule_reaches_the_repository_and_none_without_settings(self) -> None:
        repo = self.a_repo(["Edit(/" + str(self.root) + "/repo/docs/*.md)"])

        with mock.patch.dict("os.environ", {"AGENT_GUIDES_USER_SETTINGS": str(self.root / "user-settings.json")}):
            self.assertEqual(len(B.user_deny_warnings(repo)), 1)
        self.assertEqual(B.user_deny_warnings(repo), [])  # the fixture's default: no user settings file


def git_commit(repo: Path, message: str) -> None:
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "--no-verify", "-m", message)


class PrivacyCommits(Base):
    """A leak in a commit message, or in a line a commit adds, is published by the push, whatever the tree holds."""

    def test_messages_and_added_lines_are_read_and_older_lines_are_not(self) -> None:
        repo = init_repo(self.root / "repo")
        (repo / "notes.md").write_text("# Notes\n\n" + Privacy.PLANTED["currency"] + "\n")
        git_commit(repo, "docs: start")
        (repo / "notes.md").write_text((repo / "notes.md").read_text() + Privacy.PLANTED["home-path"] + "\n")
        git_commit(repo, "docs: a line\n\n" + Privacy.PLANTED["email"])

        code, out = run("privacy", "--commits", "HEAD~1..HEAD", "--repo", str(repo))

        failed = [line for line in out.split("\n") if line.startswith("  x FAIL ")]
        self.assertEqual(code, 1, out)
        self.assertEqual(len(failed), 2, out)
        self.assertTrue(any("message:3 email" in line for line in failed), out)
        self.assertTrue(any("notes.md:4 home-path" in line for line in failed), out)
        self.assertIn("privacy over 1 commits", out)

    def test_a_clean_range_passes_and_a_bad_range_is_refused(self) -> None:
        repo = init_repo(self.root / "repo")
        (repo / "notes.md").write_text("# Notes\n\n" + Privacy.PLANTED["currency"] + "\n")
        git_commit(repo, "docs: start")
        (repo / "notes.md").write_text((repo / "notes.md").read_text() + "A plain line.\n")
        git_commit(repo, "docs: a plain line")

        self.assertEqual(run("privacy", "--commits", "HEAD~1..HEAD", "--repo", str(repo))[0], 0)
        self.assertEqual(run("privacy", "--commits", "HEAD", "--repo", str(repo))[0], 1)  # the root commit added the leak
        self.assertEqual(run("privacy", "--commits", "nothing..HEAD", "--repo", str(repo))[0], 2)

    def test_a_path_with_a_space_a_quote_or_a_backslash_is_read(self) -> None:
        # git writes such a path in a patch header with a trailing tab, or C-quoted; read back as a path,
        # `git show` exited 128 and the traceback blocked every push.
        repo = init_repo(self.root / "repo")
        (repo / "start.md").write_text("# Start\n")
        git_commit(repo, "docs: start")
        names = ["my file.md", 'say "hi".md', "back\\slash.md"]
        for name in names:
            (repo / name).write_text("# A file\n\nA plain line.\n" + Privacy.PLANTED["home-path"] + "\n")
        git_commit(repo, "docs: three awkward names")

        code, out = run("privacy", "--commits", "HEAD~1..HEAD", "--repo", str(repo))

        failed = [line for line in out.split("\n") if line.startswith("  x FAIL ")]
        self.assertEqual(code, 1, out)
        for name in names:
            self.assertTrue(any(f":{name}:4 home-path" in line for line in failed), (name, out))
        self.assertEqual(len(failed), 3, out)

    def test_a_git_failure_is_a_one_line_refusal(self) -> None:
        repo = init_repo(self.root / "repo")
        (repo / "a.md").write_text("A line.\n")
        git_commit(repo, "docs: start")
        failing = subprocess.CalledProcessError(128, ["git"], stderr="fatal: a broken object\n")

        with mock.patch.object(B, "_commit_files", side_effect=failing):
            code, out = run("privacy", "--commits", "HEAD", "--repo", str(repo))

        self.assertEqual(code, 2, out)


class PrePush(Base):
    """The home's pre-push hook reads the commits being pushed, and blocks the push on a FAIL."""

    def setUp(self) -> None:
        super().setUp()
        self.repo = init_repo(self.root / "repo")
        (self.repo / ".agents/tools").mkdir(parents=True)
        shutil.copy(ROOT / "sources/bundle/tools/bundle.py", self.repo / ".agents/tools/bundle.py")
        git_commit(self.repo, "chore: the tool")
        subprocess.run(["git", "init", "-q", "--bare", str(self.root / "remote.git")], check=True)
        git(self.repo, "remote", "add", "origin", str(self.root / "remote.git"))
        git(self.repo, "push", "-q", "origin", "HEAD:refs/heads/main")
        git(self.repo, "fetch", "-q", "origin")

    def push(self, ref: str = "HEAD:refs/heads/main") -> subprocess.CompletedProcess:
        return subprocess.run(["git", "-C", str(self.repo), "-c", f"core.hooksPath={ROOT / '.githooks'}", "push", "origin", ref],
                              capture_output=True, text=True)

    def test_a_leaking_commit_is_not_pushed_and_a_clean_one_is(self) -> None:
        (self.repo / "a.md").write_text("A line.\n")
        git_commit(self.repo, "docs: a line\n\n" + Privacy.PLANTED["email"])

        blocked = self.push()
        new_branch = self.push("HEAD:refs/heads/other")
        git(self.repo, "commit", "-q", "--amend", "--no-verify", "-m", "docs: a line")
        passed = self.push()

        self.assertNotEqual(blocked.returncode, 0, blocked.stdout + blocked.stderr)
        self.assertIn("FAIL", blocked.stdout + blocked.stderr)
        self.assertNotEqual(new_branch.returncode, 0, new_branch.stdout + new_branch.stderr)
        self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)

    def test_an_attribution_trailer_is_not_pushed(self) -> None:
        (self.repo / "a.md").write_text("A line.\n")
        git_commit(self.repo, "docs: a line\n\n" + Trailers.ASSISTANT)

        blocked = self.push()

        self.assertNotEqual(blocked.returncode, 0, blocked.stdout + blocked.stderr)
        self.assertIn("attribution", blocked.stdout + blocked.stderr)


class Trailers(Base):
    """A commit message that credits an assistant: the user is the sole author of every commit."""

    ASSISTANT = "Co-" + "Authored-By: Claude Opus <noreply" + "@" + "anthropic.com>"
    GENERATED = "\U0001f916 Generated with [Claude Code](https://claude.com/claude-code)"

    def a_repo(self, *messages: str) -> Path:
        repo = init_repo(self.root / "repo")
        for number, message in enumerate(messages):
            (repo / f"f{number}.md").write_text(f"{number}\n")
            git_commit(repo, message)
        return repo

    def test_an_assistant_trailer_or_a_generated_line_fails_and_a_person_does_not(self) -> None:
        repo = self.a_repo("chore: start", "feat: a\n\n" + self.ASSISTANT, "feat: b\n\n" + self.GENERATED,
                           "feat: c\n\nCo-" + "Authored-By: Jane Roe", "build: files generated with release.py build",
                           "fix: d\n\nThe line it added was generated with care.")

        found = B.trailer_problems(repo, "HEAD~5..HEAD")[0]
        code, out = run("trailers", "HEAD~3..HEAD", "--repo", str(repo))

        self.assertEqual([sha_line.split(" ", 1)[1] for sha_line in found], ["feat: a: " + self.ASSISTANT, "feat: b: " + self.GENERATED])
        self.assertEqual(code, 0, out)  # the last three carry none

    def test_the_default_range_is_the_last_twenty_commits_without_an_upstream(self) -> None:
        repo = self.a_repo("chore: start", "feat: a\n\n" + self.ASSISTANT, *[f"chore: {n}" for n in range(19)])

        code, out = run("trailers", "--repo", str(repo))
        older = run("trailers", "--repo", str(self.a_repo_with_more(repo)))[0]

        self.assertEqual(code, 1, out)
        self.assertIn("the last 20 commits", out)
        self.assertEqual(older, 0)

    def test_without_an_upstream_only_commits_on_no_remote_are_read_and_published_ones_are_not_advised_rewritten(self) -> None:
        # A new branch with no upstream read the last twenty commits, published ones included, and advised
        # amending or rebasing them.
        repo = self.a_repo("chore: start", "feat: a\n\n" + self.ASSISTANT)
        subprocess.run(["git", "init", "-q", "--bare", str(self.root / "remote.git")], check=True)
        git(repo, "remote", "add", "origin", str(self.root / "remote.git"))
        git(repo, "push", "-q", "origin", "HEAD:refs/heads/main")
        git(repo, "fetch", "-q", "origin")
        git(repo, "switch", "-q", "-c", "topic")
        (repo / "topic.md").write_text("topic\n")
        git_commit(repo, "feat: topic")

        code, out = run("trailers", "--repo", str(repo))

        self.assertEqual(code, 0, out)
        self.assertIn("1 commits", out)
        self.assertIn("on no remote", out)

        (repo / "late.md").write_text("late\n")
        git_commit(repo, "feat: late\n\n" + self.ASSISTANT)
        code, out = run("trailers", "--repo", str(repo))

        self.assertEqual(code, 1, out)
        self.assertIn("not yet pushed", out)
        self.assertIn("published", out)
        self.assertNotIn("before pushing", out)

    def test_rev_list_options_are_a_range_and_a_published_commit_is_named_so(self) -> None:
        # `trailers --all` was rejected by the argument parser; only `trailers -- --all` worked. A flagged
        # commit already on a remote was advised amended like one not yet pushed.
        repo = self.a_repo("chore: start", "feat: a\n\n" + self.ASSISTANT)
        subprocess.run(["git", "init", "-q", "--bare", str(self.root / "remote.git")], check=True)
        git(repo, "remote", "add", "origin", str(self.root / "remote.git"))
        git(repo, "push", "-q", "origin", "HEAD:refs/heads/main")
        git(repo, "fetch", "-q", "origin")
        git(repo, "switch", "-q", "-c", "feature")
        (repo / "late.md").write_text("late\n")
        git_commit(repo, "feat: late\n\n" + self.ASSISTANT)

        code, out = run("trailers", "--all", "--repo", str(repo))
        between = run("trailers", "origin/main..feature", "--repo", str(repo))

        self.assertEqual(code, 1, out)
        published = [line for line in out.split("\n") if "feat: a:" in line]
        unpushed = [line for line in out.split("\n") if "feat: late:" in line]
        self.assertEqual(len(published), 1, out)
        self.assertIn("published", published[0])
        self.assertIn("origin/main", published[0])
        self.assertNotIn("published", unpushed[0])
        self.assertIn("1 already published", out)
        self.assertIn("owner's decision", out)
        self.assertEqual(between[0], 1, between[1])
        self.assertNotIn("feat: a:", between[1])

    def a_repo_with_more(self, repo: Path) -> Path:
        (repo / "more.md").write_text("more\n")
        git_commit(repo, "chore: one more")  # the attribution is now the 21st commit back
        return repo
