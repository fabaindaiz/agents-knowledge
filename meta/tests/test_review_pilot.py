"""The reviewer pilot: a fixed diff, the knowledge reviewer alone, and what it opened and named."""

from __future__ import annotations

import json

from meta.tests.support import ROOT, Base, _load

H = _load("harness", ROOT / "evals/harness.py")
R = _load("review_pilot", ROOT / "evals/review.py")


class ReviewPilot(Base):
    def test_the_diff_set_covers_six_notes_both_ways_and_the_neutral_tasks(self) -> None:
        diffs = R.diff_set()
        targets = {d["task"] for d in diffs if d["targets"]}
        self.assertEqual(len(targets), 6)
        self.assertEqual(len({R.H.load_task(t)["notes"][0] for t in targets}), 6)
        self.assertEqual(sum(d["variant"] == "naive" for d in diffs), 6)
        self.assertEqual(sum(d["variant"] == "reference" and bool(d["targets"]) for d in diffs), 6)
        self.assertEqual(sum(not d["targets"] for d in diffs), 3)

    def test_a_workspace_holds_the_change_uncommitted_and_the_arms_index(self) -> None:
        for arm in ("R0", "R2"):
            ws = self.root / arm
            info = R.prepare("contacts-second-source-l1", "naive", arm, ws)
            self.assertTrue(info["diff"].startswith("diff --git"))
            self.assertIn("diff --git", H.git(ws, "diff"))  # applied, not committed
            self.assertEqual((ws / ".agents/knowledge/PHASES.md").exists(), arm == "R2")
            self.assertFalse((ws / ".agents/carrier.toml").exists())  # a release, not the home's own copy

    def test_the_prompt_is_the_reviewers_own_body_and_the_diff(self) -> None:
        prompt = R.prompt("diff --git a/x b/x\n+line\n")
        self.assertIn("You review one change", prompt)
        self.assertNotIn("name: \"knowledge-reviewer\"", prompt)  # the frontmatter is the host's, not the prompt
        self.assertTrue(prompt.rstrip().endswith("```"))

    def test_the_outcomes_are_read_from_the_transcript(self) -> None:
        events = [
            {"type": "assistant", "message": {"content": [
                {"type": "tool_use", "name": "Read", "input": {"file_path": ".agents/knowledge/INDEX.md"}},
                {"type": "tool_use", "name": "Read", "input": {"file_path": ".agents/knowledge/cards/derived-over-chosen-identifiers.md"}},
                {"type": "tool_use", "name": "Read", "input": {"file_path": ".agents/knowledge/cards/in-process-guarantees.md"}}]}},
            {"type": "result", "result": "derived-over-chosen-identifiers: applies, the key is chosen at app/sync.py:12",
             "usage": {"input_tokens": 10, "cache_read_input_tokens": 900, "cache_creation_input_tokens": 90,
                       "output_tokens": 50}, "total_cost_usd": 0.01, "num_turns": 4}]
        path = self.root / "t.jsonl"
        path.write_text("\n".join(json.dumps(e) for e in events))

        out = R.outcomes(path, self.root, ["derived-over-chosen-identifiers"])

        self.assertEqual(out["cards"], ["derived-over-chosen-identifiers", "in-process-guarantees"])
        self.assertTrue(out["target_opened"])
        self.assertTrue(out["target_named"])
        self.assertEqual(out["input_tokens"], 1000)
        self.assertFalse(out["phases_read"])
