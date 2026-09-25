"""The industry formats the carrier tool reads and writes: YAML frontmatter, TOML, SHA256SUMS, SemVer."""

from __future__ import annotations

import os
import tomllib

from meta.tests.support import Base, bundle, make_bundle


class Frontmatter(Base):
    def test_what_the_tool_writes_it_reads_back(self) -> None:
        data = {"slug": "a", "claim": 'say "no" — here\\there', "phases": ["plan", "review"],
                "about": [{"do": "x, y", "wrong_when": "z: w"}], "empty": []}

        block, body = bundle.split_frontmatter(bundle.dump_frontmatter(data) + "\n# Body\n")

        self.assertEqual(bundle.parse_frontmatter(block), data)
        self.assertEqual(body, "\n# Body\n")

    def test_plain_scalars_comments_and_null_read_as_yaml_reads_them(self) -> None:
        block = "slug:   a-slug                   # a comment\nforked_at: null\nset: [context, sync]\nmap: {lineage: g-1, kind: text}\n"

        self.assertEqual(bundle.parse_frontmatter(block),
                         {"slug": "a-slug", "forked_at": None, "set": ["context", "sync"], "map": {"lineage": "g-1", "kind": "text"}})

    def test_a_plain_scalar_yaml_would_type_or_refuse_must_be_quoted(self) -> None:
        for value in ("1.", "+1.", "01.", "2026-09-25 10:00:00 Z", "2026-09-25T10:00:00 +05:00", "1_2:30", "21", "1.0", "yes", "Off", "2026-01-01", "0x1F", "1:20", ".inf", "a: b", "a:", "- x", "? x", "=", "<<",
                      "a\tb", "[, a]"):
            with self.subTest(value=value), self.assertRaises(bundle.FrontmatterError):
                bundle.parse_frontmatter(f"claim: {value}\n")
        with self.assertRaises(bundle.FrontmatterError):
            bundle.parse_frontmatter("phases:\n  - a\n- b\n")

    def test_a_block_list_of_quoted_strings_folds_across_lines(self) -> None:
        block = 'adapted:                        # local\n  - "one line\n    continued"\n  - "two"\ndeclined:  []\n'

        self.assertEqual(bundle.parse_frontmatter(block), {"adapted": ["one line continued", "two"], "declined": []})

    def test_features_outside_the_subset_are_refused(self) -> None:
        for block in ("a: &anchor x\n", "a: |\n  text\n", "  nested: x\n", "a: 1\na: 2\n", 'a: "open\n'):
            with self.subTest(block=block), self.assertRaises(bundle.FrontmatterError):
                bundle.parse_frontmatter(block)

    def test_invisible_characters_are_escaped_when_written(self) -> None:
        text = bundle.dump_frontmatter({"claim": "a\u202eb"})

        self.assertNotIn("\u202e", text)
        self.assertEqual(bundle.parse_frontmatter(bundle.split_frontmatter(text)[0])["claim"], "a\u202eb")


class CarrierFile(Base):
    def test_the_carrier_file_round_trips_through_tomllib(self) -> None:
        data = {"carrier": "r-abcdef", "adopted": "2026-01-01", "upstream": "", "harvested_through": "2026-02-01",
                "adapted": ['a "quoted" line\\with a backslash', "ünïcode"], "declined": []}

        bundle.write_carrier(self.root, data)

        self.assertEqual(tomllib.loads((self.root / "carrier.toml").read_text()), data)
        self.assertEqual(bundle.read_carrier(self.root), data)

    def test_a_value_that_is_not_a_string_or_a_list_of_strings_is_refused(self) -> None:
        (self.root / "carrier.toml").write_text("carrier = 3\n")

        with self.assertRaises(bundle.RefusedError):
            bundle.read_carrier(self.root)


class Checksums(Base):
    def test_the_file_is_gnu_text_format_in_byte_order(self) -> None:
        agents = make_bundle(self.root)
        lines = (agents / "SHA256SUMS").read_text().splitlines()

        self.assertTrue(all(bundle.CHECKSUM_LINE.match(line) for line in lines))
        paths = [line.split("  ", 1)[1] for line in lines]
        self.assertEqual(paths, sorted(paths, key=str.encode))
        self.assertNotIn("carrier.toml", paths)
        self.assertNotIn("tracking/candidates.md", paths)
        self.assertIn("incoming/README.md", paths)

    def test_a_fresh_bundle_verifies(self) -> None:
        self.assertEqual(bundle.checksum_problems(make_bundle(self.root)), [])

    def test_a_changed_a_missing_and_an_unlisted_file_are_each_named(self) -> None:
        agents = make_bundle(self.root)
        (agents / "knowledge/notes/active/a-check.md").write_text("edited\n")
        (agents / "tools/bundle.py").unlink()
        (agents / "method/prompt-extra.md").write_text("# new\n")

        problems = "\n".join(bundle.checksum_problems(agents))

        self.assertIn("knowledge/notes/active/a-check.md: changed", problems)
        self.assertIn("tools/bundle.py: listed in SHA256SUMS and missing", problems)
        self.assertIn("method/prompt-extra.md: not in SHA256SUMS", problems)

    def test_the_carriers_own_files_may_change(self) -> None:
        agents = make_bundle(self.root)
        (agents / "tracking/candidates.md").write_text("anything\n")
        (agents / "evaluation-2026-01-01-abcdef.md").write_text("report\n")
        bundle.write_carrier(agents, {"carrier": "r-bbbbbb"})

        self.assertEqual(bundle.checksum_problems(agents), [])

    def test_a_path_listed_twice_or_outside_the_bundle_is_refused(self) -> None:
        agents = make_bundle(self.root)
        sums = agents / "SHA256SUMS"
        first = sums.read_text().splitlines()[0]
        sums.write_text("0" * 64 + "  " + first.split("  ", 1)[1] + "\n" + sums.read_text())
        self.assertIn("listed twice", "\n".join(bundle.checksum_problems(agents)))
        sums.write_text("0" * 64 + "  ./README.md\n")
        self.assertIn("normal form", "\n".join(bundle.checksum_problems(agents)))
        sums.write_text("0" * 64 + "  ../outside.md\n")
        self.assertIn("outside the bundle", "\n".join(bundle.checksum_problems(agents)))

    def test_a_crlf_checkout_is_named_as_such(self) -> None:
        agents = make_bundle(self.root)
        path = agents / "method/prompt-context.md"
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))

        self.assertIn("CRLF", "\n".join(bundle.checksum_problems(agents)))

    def test_sha256sum_agrees_with_the_tool(self) -> None:
        import shutil
        import subprocess

        agents = make_bundle(self.root)
        tool = shutil.which("sha256sum") or shutil.which("shasum")
        if tool is None:
            self.skipTest("no sha256sum or shasum on this machine")
        args = [tool, "-c", "SHA256SUMS"] if tool.endswith("sha256sum") else [tool, "-a", "256", "-c", "SHA256SUMS"]

        self.assertEqual(subprocess.run(args, cwd=agents, capture_output=True).returncode, 0)


class Versions(Base):
    def test_precedence_follows_semver(self) -> None:
        ordered = ["0.0.9", "0.0.10", "0.1.0-alpha", "0.1.0-alpha.1", "0.1.0-alpha.beta", "0.1.0-beta.2",
                   "0.1.0-beta.11", "0.1.0-rc.1", "0.1.0", "1.0.0"]

        self.assertEqual(sorted(reversed(ordered), key=bundle.semver_key), ordered)
        self.assertEqual(bundle.semver_key("1.0.0+build.7"), bundle.semver_key("1.0.0"))

    def test_what_is_not_semver_is_refused(self) -> None:
        for bad in ("21", "1.0", "01.0.0", "1.0.0-", "v1.0.0.0"):
            with self.subTest(bad=bad), self.assertRaises(bundle.RefusedError):
                bundle.semver_key(bad)

    def test_the_changelog_is_sliced_by_version(self) -> None:
        (self.root / "CHANGELOG.md").write_text(
            "# Changelog\n\n## [Unreleased]\n\n## [0.0.10] - 2026-03-01\n\nten\n\n## [0.0.9] - 2026-02-01\n\nnine\n\n"
            "## [0.0.8] - 2026-01-01\n\neight\n")

        since = bundle.changelog_since(self.root, "0.0.8")

        self.assertIn("ten", since)
        self.assertIn("nine", since)
        self.assertNotIn("eight", since)
        self.assertLess(since.index("ten"), since.index("nine"))


class Incoming(Base):
    def test_an_empty_incoming_passes(self) -> None:
        self.assertEqual(bundle.incoming_problems(make_bundle(self.root)), [])

    def test_each_refused_kind_is_named(self) -> None:
        agents = make_bundle(self.root)
        offered = agents / "incoming/.agents"
        (offered / "tools").mkdir(parents=True)
        (offered / "tools/bundle.py").write_text("print('the tool')\n")
        (offered / "hooks").mkdir()
        (offered / "hooks/run.sh").write_text("echo\n")
        (offered / "settings.json").write_text("{}\n")
        (offered / "note.md").write_text("plain \u200b hidden\n")
        (offered / "exec.md").write_text("text\n")
        os.chmod(offered / "exec.md", 0o755)
        (offered / "link.md").symlink_to(agents / "README.md")

        problems = "\n".join(bundle.incoming_problems(agents))

        self.assertNotIn("incoming/.agents/tools/bundle.py", problems)
        for expected in ("hooks/run.sh: assistant", "hooks/run.sh: a script", "settings.json: assistant",
                         "U+200B", "exec.md: has an executable bit", "link.md: a symbolic link"):
            self.assertIn(expected, problems)

    def test_evasions_by_case_name_kind_and_place_are_refused(self) -> None:
        agents = make_bundle(self.root)
        offered = agents / "incoming/release"
        for rel, text in {"Settings.JSON": "{}", "Hooks/x.md": "x", ".Github/workflows/ci.yml": "x", "CLAUDE.md": "x",
                          "sub/AGENTS.md": "x", "x.pyc": "x", "run.command": "x", ".mcp.json": "{}", "Makefile": "all:",
                          "deep/down/tools/bundle.py": "x", "filler.md": "a\u3164b"}.items():
            (offered / rel).parent.mkdir(parents=True, exist_ok=True)
            (offered / rel).write_text(text)
        (offered / "tools").mkdir()
        (offered / "tools/bundle.py").write_text("the tool\n")
        (offered / "utf16.md").write_bytes("text".encode("utf-16"))

        problems = "\n".join(bundle.incoming_problems(agents))

        for rel in ("Settings.JSON", "Hooks", ".Github", "CLAUDE.md", "AGENTS.md", "x.pyc", "run.command", ".mcp.json",
                    "Makefile", "deep/down/tools/bundle.py: a script", "U+3164", "utf16.md: not UTF-8"):
            self.assertIn(rel, problems)
        self.assertNotIn("release/tools/bundle.py: a script", problems)

    def test_bidirectional_controls_anywhere_in_the_bundle_are_found(self) -> None:
        agents = make_bundle(self.root)
        (agents / "method/prompt-context.md").write_text("safe \u202e txet\n")

        found = bundle.invisible_characters(agents, bundle.shipped(agents))

        self.assertEqual(len(found), 1)
        self.assertIn("U+202E", found[0])


class Outbox(Base):
    def test_a_fresh_outbox_passes_and_a_changed_header_is_named(self) -> None:
        agents = make_bundle(self.root)
        self.assertEqual(bundle.outbox_problems(agents), [])

        (agents / "tracking/candidates.md").write_text("| Candidate | Lacks |\n|---|---|\n")

        self.assertIn("tracking/candidates.md", "\n".join(bundle.outbox_problems(agents)))
