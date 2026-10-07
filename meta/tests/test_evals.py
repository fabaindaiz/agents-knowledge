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
        for moved in ("## By phase of work", "## The areas, for browsing", "## How well founded is any of this"):
            self.assertNotIn(moved, index)
            self.assertIn(moved, phases)
        self.assertIn("PHASES.md", index)  # the index still says where the rest went
        self.assertLess(len(index), len(before) * 0.75)
        self.assertEqual(index.split("## By what you are about to do", 1)[1].strip(),
                         before.split("## By what you are about to do", 1)[1].split("\n## ", 1)[0].strip())
        self.assertGreater(info["index_chars"], 0)
        self.assertEqual(bundle.checksum_problems(agents), [])  # the copy still verifies as a release
