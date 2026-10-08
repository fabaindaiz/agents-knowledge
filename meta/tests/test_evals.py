"""The efficacy experiment's harness: the arms pilot-9 adds, and the D2 index it builds for one of them."""

from __future__ import annotations

import shutil

from meta.tests.support import ROOT, Base, _load, bundle

H = _load("harness", ROOT / "evals/harness.py")


class Pilot9Arms(Base):
    def test_the_two_arms_exist_and_run_on_every_family_the_bundle_runs_on(self) -> None:
        for arm in ("bundle_v29", "bundle_v29_d2"):
            self.assertIn(arm, H.CONDITIONS)
            for family in ("judgment", "boundary", "neutral", "trivial"):
                self.assertIn(arm, H.FAMILY_CONDITIONS[family], family)
            self.assertEqual(H.ROUTINGS[arm], H.ROUTING_V23B)  # the 0.0.29 wiring is 0.0.23's, unchanged

    def test_the_d2_index_keeps_the_lookup_and_moves_the_rest_to_phases(self) -> None:
        agents = self.root / ".agents"
        shutil.copytree(ROOT / ".agents", agents, ignore=shutil.ignore_patterns("__pycache__", "proposals", "carrier.toml"))
        before = (agents / "knowledge/INDEX.md").read_text()

        info = H.d2_index(agents)

        index = (agents / "knowledge/INDEX.md").read_text()
        phases = (agents / "knowledge/PHASES.md").read_text()
        self.assertIn("## By what you are about to do", index)
        for moved in ("## By phase of work", "## The topics", "## How well founded is any of this"):
            self.assertNotIn(moved, index)
            self.assertIn(moved, phases)
        self.assertIn("PHASES.md", index)  # the index still says where the rest went
        self.assertLess(len(index), len(before) * 0.75)
        self.assertEqual(index.split("## By what you are about to do", 1)[1].strip(),
                         before.split("## By what you are about to do", 1)[1].split("\n## ", 1)[0].strip())
        self.assertGreater(info["index_chars"], 0)
        self.assertEqual(bundle.checksum_problems(agents), [])  # the copy still verifies as a release

    def test_a_d2_trial_is_checked_against_the_release_it_was_built_from(self) -> None:
        # pilot-9's first plan: d2_index rewrites SHA256SUMS, so the digest check refused every D2 trial.
        import hashlib
        frozen = hashlib.sha256((H.BUNDLE / "SHA256SUMS").read_bytes()).hexdigest()[:12]
        for arm in ("bundle_v29", "bundle_v29_d2"):
            ws = self.root / arm
            info = H.prepare(H.load_task("cli-help-typo"), arm, ws)
            self.assertEqual(H.release_digest(ws, info), frozen, arm)


class TaggedReleaseArm(Base):
    """pilot-11: the previous release, taken whole from its tag, beside the candidate in the same run."""

    def test_the_tagged_arm_holds_the_release_its_tag_holds(self) -> None:
        import subprocess
        if subprocess.run(["git", "-C", str(ROOT), "rev-parse", "-q", "--verify", "refs/tags/v0.0.29"], capture_output=True).returncode:
            self.skipTest("the tag v0.0.29 is not in this clone")
        H = _load("harness", ROOT / "evals/harness.py")
        tree = H.tag_bundle("v0.0.29")
        self.assertEqual(H._bundle_tool().bundle_version(tree), "0.0.29")
        ws = self.root / "ws"
        task = H.load_task("cli-help-typo")
        info = H.prepare(task, "bundle_v29tag", ws)
        self.assertEqual(H._bundle_tool().bundle_version(ws / ".agents"), "0.0.29")
        self.assertIn(H.ROUTING_V23B.strip(), (ws / "AGENTS.md").read_text())
        self.assertTrue((ws / ".claude/agents/knowledge-reviewer.md").is_file())
        self.assertEqual(info["condition"], "bundle_v29tag")
