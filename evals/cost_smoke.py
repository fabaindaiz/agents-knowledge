#!/usr/bin/env python3
"""pilot-6, the cost smoke test of release 0.0.22: what carrying the bundle costs, against the predictions
written in `.agents/CHANGELOG.md` [0.0.22] before any run, and how often the working directives were
followed (roadmap `i-5ed7e8-c4b9c7` and `i-5ed7e8-a2f016`). Exploratory; it claims nothing about efficacy.

    python3 evals/cost_smoke.py runs/pilot-6 [--out FILE]

Arms: `minimal`; `bundle` (the bundle with the v21 wiring paragraph); `bundle_v22` (the same bundle with
the 0.0.22 wiring: consult only when a change can be affected, the card first, the repository first).
Task groups: `trivial` (the family of that name), `normal` (every other task), and the discriminating
tasks of pilot-5, whose pass rate must not fall.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from analyze import cost_of, geo_ratio, is_infra_failure, load  # noqa: E402

DISCRIMINATING = ("contacts-second-source-l1", "contacts-second-source-l2", "refund-webhook-l2")
# Written before the run, from `.agents/CHANGELOG.md` [0.0.22] and `meta/roadmap.md` (i-5ed7e8-c4b9c7).
PREDICTIONS = {
    "bundle_v22": {"trivial": (1.2, 1.4), "normal": (1.5, 1.8)},   # .agents/CHANGELOG.md [0.0.22], pilot-6
    "bundle_v23": {"trivial": (1.2, 1.4), "normal": (2.0, 2.3)},   # .agents/CHANGELOG.md [0.0.23], pilot-7
    "bundle_v23b": {"trivial": (1.2, 1.4), "normal": (2.0, 2.3)},  # the same, on the changed candidate, pilot-8
    # pilot-9, registered 2026-10-07 in PROTOCOL.md: the current release as the baseline, and the D2 index split
    # (`meta/reviews/2026-10-05-index-scaling.md`, "The experiment that would decide it").
    "bundle_v29": {"trivial": (1.2, 1.4), "normal": (2.0, 2.3)},
    "bundle_v29_d2": {"trivial": (1.2, 1.4), "normal": (2.0, 2.2)},
    # pilot-10, registered 2026-10-08: release 0.0.30 against pilot-9's 0.0.29 (×1.17 and ×2.22); refuted above the
    # upper end of 0.0.29's interval, the line `prompt-sync.md` 7a and MANIFEST.md hold a release to.
    "bundle_v30": {"trivial": (1.2, 1.23), "normal": (2.2, 2.70)},
}
METRICS = ("cost", "turns", "out_tokens")
ARMS = ("minimal", "bundle", "bundle_v22", "bundle_v23", "bundle_v23b", "bundle_v29", "bundle_v29_d2", "bundle_v30")
CHECK_MENTION = re.compile(r"(?i)\b(verify by|the check|its check|card)\b")


def final_text(run: Path, trial: str) -> str:
    """The last assistant text of a trial's transcript, or the empty string."""
    path = run / "trials" / trial / "transcript.jsonl"
    text = ""
    if not path.is_file():
        return text
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "result" and isinstance(ev.get("result"), str):
            text = ev["result"]
    return text


def called_reviewer(run: Path, trial: str) -> bool:
    """Whether the main session handed anything to the reviewer subagent (0.0.23's fourth prediction)."""
    path = run / "trials" / trial / "transcript.jsonl"
    if not path.is_file():
        return False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "assistant" and not ev.get("parent_tool_use_id"):
            for c in (ev.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("name") in ("Agent", "Task") \
                        and (c.get("input") or {}).get("subagent_type") == "knowledge-reviewer":
                    return True
    return False


def adherence(run: Path, rec: dict) -> dict:
    """What a trial read of the bundle, and whether its report names a check: counted, never judged."""
    reads = (rec.get("trace") or {}).get("reads") or []
    bundle = [r for r in reads if ".agents/" in r]
    return {
        "any_bundle_read": bool(bundle),
        "index": any(r.endswith("knowledge/INDEX.md") for r in bundle),
        "area": any("knowledge/areas/" in r for r in bundle),
        "notes": sum(1 for r in bundle if "knowledge/notes/" in r),
        "mentions_check": bool(CHECK_MENTION.search(final_text(run, rec["trial"]))),
        "reviewer": called_reviewer(run, rec["trial"]),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    run = Path(a.run)
    plan, recs = load(run)
    valid = [r for r in recs if not is_infra_failure(r)]
    groups = {
        "trivial": [t for t, v in plan["tasks"].items() if v["family"] == "trivial"],
        "normal": [t for t, v in plan["tasks"].items() if v["family"] != "trivial"],
    }
    L = [f"# Cost smoke test — {run.name}\n",
         "> **Exploratory.** Cost, turns and output tokens only; nothing here is a claim about efficacy.\n",
         f"Model `{plan['model']}`, {plan['reps']} repetitions, bundle `{plan.get('bundle_version')}` "
         f"(`{plan.get('bundle_digest')}`), isolation: {plan.get('isolation')}. "
         f"{len(valid)} valid trials of {len(recs)}.\n",
         "## Cost against the written predictions\n",
         "Geometric mean of per-task ratios, 95% bootstrap interval over tasks.\n",
         "| Group | Contrast | Metric | Ratio | 95% CI | Tasks | Prediction | Verdict |",
         "|---|---|---|---:|---|---:|---|---|"]
    for group, tasks in groups.items():
        for a_arm, b_arm in (("bundle_v30", "minimal"), ("bundle_v29_d2", "minimal"), ("bundle_v29", "minimal"), ("bundle_v29_d2", "bundle_v29"),
                             ("bundle_v23b", "minimal"), ("bundle_v23", "minimal"), ("bundle_v22", "minimal"), ("bundle", "minimal"), ("bundle_v22", "bundle")):
            for metric in METRICS:
                cell: dict = {}
                for r in valid:
                    cell.setdefault((r["task"], r["condition"]), []).append(cost_of(r)[metric])
                g = geo_ratio(cell, a_arm, b_arm, tasks)
                pred, verdict = "", ""
                if b_arm == "minimal" and metric == "cost" and group in PREDICTIONS.get(a_arm, {}) and g:
                    at_most, refuted_above = PREDICTIONS[a_arm][group]
                    pred = f"≤ ×{at_most} (refuted above ×{refuted_above})"
                    verdict = "holds" if g[0] <= at_most else ("refuted" if g[0] > refuted_above else "neither")
                if g is None:
                    continue
                row = (f"×{g[0]:.2f}", f"[{g[1]:.2f}, {g[2]:.2f}]", str(g[3]))
                L.append(f"| {group} | {a_arm} / {b_arm} | {metric} | {row[0]} | {row[1]} | {row[2]} | {pred} | {verdict} |")
    L += ["", "## Pass rates (hidden tests)\n", "| Task | " + " | ".join(ARMS) + " |", "|---|" + "---:|" * len(ARMS)]
    for task in sorted(plan["tasks"]):
        vals = []
        for arm in ARMS:
            got = [r["success"] for r in valid if r["task"] == task and r["condition"] == arm]
            vals.append(f"{sum(got)}/{len(got)}" if got else "—")
        mark = " (discriminating in pilot-5)" if task in DISCRIMINATING else ""
        L.append(f"| {task}{mark} | " + " | ".join(vals) + " |")
    L += ["", "## Directive adherence, counted from the transcripts (i-5ed7e8-a2f016)\n",
          "Mechanical counts; *mentions a check* is a keyword heuristic on the final message, not a judgement.\n",
          "| Group | Arm | Trials | Read the bundle | Index | Area index | Notes opened (mean) | Mentions a check | Called the reviewer |",
          "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for group, tasks in groups.items():
        for arm in ("bundle", "bundle_v22", "bundle_v23", "bundle_v23b", "bundle_v29", "bundle_v29_d2", "bundle_v30"):
            rs = [adherence(run, r) for r in valid if r["task"] in tasks and r["condition"] == arm]
            if not rs:
                continue
            n = len(rs)
            L.append(f"| {group} | {arm} | {n} | {sum(x['any_bundle_read'] for x in rs)}/{n} | {sum(x['index'] for x in rs)}/{n} | "
                     f"{sum(x['area'] for x in rs)}/{n} | {statistics.fmean(x['notes'] for x in rs):.1f} | "
                     f"{sum(x['mentions_check'] for x in rs)}/{n} | {sum(x['reviewer'] for x in rs)}/{n} |")
    out = "\n".join(L) + "\n"
    if a.out:
        Path(a.out).write_text(out, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
