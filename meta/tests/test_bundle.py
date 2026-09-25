"""The carrier tool: verify, the local step, links, sessions, ids, privacy and the workspace.

Every planted leak is assembled at run time, so this file's own source never holds the leak it plants:
the home's check reads this file with the same rules.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import math
from pathlib import Path

from meta.tests.support import NOTE, Base, bundle, make_bundle

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
            "outbox": lambda a: (a / "tracking/candidates.md").write_text("no table\n"),
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
        for rel in B.OUTBOX:
            (agents / rel).unlink()

        self.assertEqual(B.verify_problems(agents, release=True), [])
        self.assertNotEqual(B.verify_problems(agents), [])
        B.write_carrier(agents, {"carrier": "r-bbbbbb"})
        self.assertIn("another repository's own file", "\n".join(B.verify_problems(agents, release=True)))

    def test_the_real_bundle_exported_verifies_as_a_release(self) -> None:
        """A release as it travels: the home's own bundle, exported, with no outbox and no carrier file."""
        real = Path(__file__).resolve().parents[2] / ".agents"
        out = self.root / "release"

        B.export(real, out)

        self.assertFalse((out / "carrier.toml").exists())
        self.assertFalse((out / "tracking").exists())
        self.assertEqual(B.verify_problems(out, release=True), [])

    def test_what_a_carrier_never_publishes_is_not_privacy_checked(self) -> None:
        agents = make_bundle(self.root)
        (agents / "evaluation-2026-01-01-abcdef.md").write_text("Cloned from https://git" + "hub.com/" + "jdoe/ledger.\n")
        (agents / "incoming/offered.md").write_text("Write to " + "jdoe" + "@" + "corp-mail.io\n")

        self.assertEqual(B.verify_problems(agents), [])

    def test_hidden_and_stray_files_are_named(self) -> None:
        agents = make_bundle(self.root)
        (agents / "method/.evil.md").write_text("hidden\n")
        (agents / "tracking/prompt-override.md").write_text("stray\n")
        (agents / "evaluation-x.py").write_text("stray\n")
        (agents / ".DS_Store").write_text("a file browser's\n")

        problems = "\n".join(B.verify_problems(agents))

        self.assertIn("method/.evil.md: a hidden file", problems)
        self.assertIn("tracking/prompt-override.md: not a file", problems)
        self.assertIn("evaluation-x.py: not a file", problems)
        self.assertNotIn(".DS_Store", problems)

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
        plant(agents / "tracking/candidates.md", "| a-thing — a claim | K | a second occurrence | here | 2026-01-02 |")

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
        self.assertEqual(set(sessions), {"coding", "consult", "evaluate", "bootstrap", "update", "harvest"})
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
        self.assertIn("no private terms checked", report.terms)

    def test_each_rule_fails_on_its_planted_leak(self) -> None:
        for rule, line in self.PLANTED.items():
            with self.subTest(rule=rule):
                agents = make_bundle(self.root / rule)
                plant(agents / "method/prompt-context.md", line)

                report = B.privacy_check(agents)

                self.assertEqual(self.rules(report), [rule], report.findings)

    def test_the_outbox_is_read_too(self) -> None:
        agents = make_bundle(self.root)
        plant(agents / "tracking/candidates.md", self.PLANTED["email"])

        self.assertEqual(self.rules(B.privacy_check(agents)), ["email"])

    def test_a_code_name_fails_in_the_evidence_and_nowhere_else(self) -> None:
        agents = make_bundle(self.root)
        name = "settle" + "Amount"
        plant(agents / "knowledge/notes/active/absence.md", f"## Why it works\n\nThe field `{name}` held it.\n\n## Evidence\n\n"
                                                            f"The field `{name}` held it.\n\n## Literature\n\nThe field `{name}` held it.")
        plant(agents / "tracking/candidates.md", f"The field `{name}` held it.")

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
        plant(agents / "tracking/candidates.md", "It failed 7 " + "of 12 runs over 12" + ',480 rows: "the queue was never drained at all".')

        report = B.privacy_check(agents)

        self.assertEqual(sorted(self.rules(report, "WARN")), ["exact-count", "n-of-m", "quote"])
        self.assertEqual(report.failures, [])

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

    def test_the_outbox_is_reset_to_its_templates(self) -> None:
        agents = make_bundle(self.root)
        plant(agents / "tracking/candidates.md", "| a | K | b | c | 2026-01-01 |")

        code, out = run("outbox", "--reset", str(agents))

        self.assertEqual(code, 0)
        self.assertEqual((agents / "tracking/candidates.md").read_text(), B.OUTBOX_TEMPLATES["tracking/candidates.md"])
