#!/usr/bin/env python3
"""The pre-registered analysis of a run of the bundle-efficacy experiment. Standard library only.

    python3 evals/analyze.py RUN [--out RUN/report.md] [--exploratory]

Everything here is fixed by PROTOCOL.md before data exist: the unit of analysis is the task, every
contrast is paired within task, the primary contrast is named once, the secondary ones are
Holm-corrected, and a null is reported as a bound, never as "no effect". Nothing is excluded except
infrastructure failures, which are counted and listed.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import statistics
from pathlib import Path

PRIMARY = ("bundle", "ablated", "judgment")
SECONDARY = [
    ("bundle", "minimal", "judgment"),
    ("oracle", "oracle_placebo", "judgment"),
    ("oracle", "bundle", "judgment"),
    ("minimal", "none", "judgment"),
    ("bundle", "ablated", "boundary"),
    ("bundle", "minimal", "boundary"),
    ("oracle", "oracle_placebo", "boundary"),
    ("bundle", "minimal", "neutral"),
]
COST_CONTRASTS = [("bundle", "minimal"), ("bundle", "none"), ("minimal", "none")]
EQUIVALENCE_MARGIN = 0.10  # TOST margin on a success-rate difference, pre-registered
MIN_TASKS = 8  # below this many tasks in a family, a contrast is described, never tested
ALPHA = 0.05
BOOT = 10000
SEED = 20260924

# two-sided 95% t quantiles; beyond 30 degrees of freedom the normal value is used
T975 = [None, 12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.160,
        2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086, 2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052,
        2.048, 2.045, 2.042]
T95 = [None, 6.314, 2.920, 2.353, 2.132, 2.015, 1.943, 1.895, 1.860, 1.833, 1.812, 1.796, 1.782, 1.771,
       1.761, 1.753, 1.746, 1.740, 1.734, 1.729, 1.725, 1.721, 1.717, 1.714, 1.711, 1.708, 1.706, 1.703,
       1.701, 1.699, 1.697]


def tq(table, df):
    if df < 1:
        return float("nan")
    return table[df] if df < len(table) else (1.960 if table is T975 else 1.645)


def is_infra_failure(rec: dict) -> bool:
    """No result event and no tool call: the session never ran (auth, API, CLI crash)."""
    tr = rec.get("trace") or {}
    return tr.get("result") is None and not tr.get("tool_calls")


def load(run: Path):
    plan = json.loads((run / "plan.json").read_text())
    recs = [json.loads(l) for l in (run / "results.jsonl").read_text().splitlines() if l.strip()]
    return plan, recs


def cluster_of(plan, task):
    notes = plan["tasks"][task]["notes"]
    return notes[0] if notes else task


def cells(recs, key=lambda r: r["success"]):
    out = {}
    for r in recs:
        out.setdefault((r["task"], r["condition"]), []).append(key(r))
    return out


def paired(cell, a, b, tasks):
    return {t: statistics.fmean(cell[(t, a)]) - statistics.fmean(cell[(t, b)])
            for t in tasks if (t, a) in cell and (t, b) in cell}


def sign_flip_p(ds: list[float]) -> float:
    """Two-sided randomisation test of mean zero: flip each task's sign. Exact up to 16 tasks."""
    n = len(ds)
    if n == 0:
        return float("nan")
    obs = abs(sum(ds))
    if n <= 16:
        hits = sum(1 for signs in itertools.product((1, -1), repeat=n)
                   if abs(sum(s * d for s, d in zip(signs, ds))) >= obs - 1e-12)
        return hits / 2 ** n
    rng = random.Random(SEED)
    hits = sum(1 for _ in range(20000) if abs(sum(d if rng.random() < .5 else -d for d in ds)) >= obs - 1e-12)
    return (hits + 1) / 20001


def cluster_boot(d: dict, clusters: dict) -> tuple[float, float]:
    """Percentile CI of the mean paired difference, resampling clusters of tasks (tasks sharing a note)."""
    by = {}
    for t, v in d.items():
        by.setdefault(clusters[t], []).append(v)
    keys = list(by)
    if len(keys) < 2:
        return (float("nan"), float("nan"))
    rng = random.Random(SEED)
    means = []
    for _ in range(BOOT):
        vals = [v for k in (rng.choice(keys) for _ in keys) for v in by[k]]
        means.append(statistics.fmean(vals))
    means.sort()
    return means[int(0.025 * BOOT)], means[int(0.975 * BOOT) - 1]


def contrast(cell, plan, a, b, family):
    tasks = [t for t, v in plan["tasks"].items() if v["family"] == family]
    d = paired(cell, a, b, tasks)
    ds = list(d.values())
    n = len(ds)
    row = {"a": a, "b": b, "family": family, "n_tasks": n}
    if n == 0:
        return row
    mean = statistics.fmean(ds)
    sd = statistics.stdev(ds) if n > 1 else float("nan")
    se = sd / math.sqrt(n) if n > 1 else float("nan")
    if n < MIN_TASKS or sd == 0:
        # Too few tasks, or no variation at all: an interval here would be a statement the data cannot make.
        se = float("nan")
    row.update({
        "mean_a": statistics.fmean(statistics.fmean(cell[(t, a)]) for t in d),
        "mean_b": statistics.fmean(statistics.fmean(cell[(t, b)]) for t in d),
        "diff": mean, "sd": sd, "se": se,
        "ci_t": (mean - tq(T975, n - 1) * se, mean + tq(T975, n - 1) * se) if not math.isnan(se) else None,
        "ci_boot": cluster_boot(d, {t: cluster_of(plan, t) for t in d}) if n >= MIN_TASKS else (float("nan"), float("nan")),
        "p": sign_flip_p(ds) if n >= MIN_TASKS else float("nan"),
        "descriptive_only": n < MIN_TASKS,
        "mde80": 2.80 * se,
        "tost_equivalent": (not math.isnan(se) and mean - tq(T95, n - 1) * se > -EQUIVALENCE_MARGIN
                            and mean + tq(T95, n - 1) * se < EQUIVALENCE_MARGIN),
        "better": sum(1 for x in ds if x > 0), "worse": sum(1 for x in ds if x < 0), "tied": sum(1 for x in ds if x == 0),
        "per_task": d,
    })
    return row


def holm(rows):
    ps = sorted((r["p"], i) for i, r in enumerate(rows) if r.get("n_tasks") and not math.isnan(r["p"]))
    m = len(ps)
    running = 0.0
    for rank, (p, i) in enumerate(ps):
        running = max(running, min(1.0, (m - rank) * p))
        rows[i]["p_holm"] = running


def pass_hat_k(vals: list[bool], k: int) -> float:
    n, c = len(vals), sum(vals)
    if n < k:
        return float("nan")
    return math.comb(c, k) / math.comb(n, k)


def cost_of(r):
    res = (r.get("trace") or {}).get("result") or {}
    usage = res.get("usage") or {}
    return {"cost": res.get("total_cost_usd"), "turns": res.get("num_turns"),
            "out_tokens": usage.get("output_tokens"), "wall": (r.get("invoke") or {}).get("wall_s")}


def geo_ratio(cellc, a, b, tasks):
    logs = []
    for t in tasks:
        va = [x for x in cellc.get((t, a), []) if x]
        vb = [x for x in cellc.get((t, b), []) if x]
        if va and vb:
            logs.append(math.log(statistics.fmean(va) / statistics.fmean(vb)))
    if not logs:
        return None
    rng = random.Random(SEED)
    boots = sorted(statistics.fmean(rng.choice(logs) for _ in logs) for _ in range(BOOT))
    return (math.exp(statistics.fmean(logs)), math.exp(boots[int(.025 * BOOT)]), math.exp(boots[int(.975 * BOOT) - 1]), len(logs))


def fmt(x, pct=False):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "—"
    return f"{x * 100:+.1f} pp" if pct else f"{x:.3f}"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--out")
    ap.add_argument("--exploratory", action="store_true", help="label the whole report exploratory (pilot runs)")
    a = ap.parse_args(argv)
    run = Path(a.run)
    plan, recs = load(run)
    infra = [r for r in recs if is_infra_failure(r)]
    valid = [r for r in recs if not is_infra_failure(r)]
    L = []
    w = L.append
    w(f"# Bundle efficacy — {run.name}\n")
    if a.exploratory:
        w("> **Exploratory.** This run is a pilot: it validates the harness and estimates variance. "
          "Nothing in it is a confirmatory result.\n")
    w("## Setup, as frozen in the plan\n")
    w(f"- Model `{plan['model']}`, effort `{plan.get('effort')}`, {plan['claude_version']}, max turns "
      f"{plan['max_turns']}, timeout {plan['timeout_s']} s, {plan['reps']} repetitions, seed {plan['seed']}")
    w(f"- Bundle `{plan['bundle_digest']}`, repository `{plan['repo_head'][:10]}`"
      f"{' (DIRTY: results are not attributable to a commit)' if plan['repo_dirty'] else ''}, harness `{plan['harness_hash']}`")
    fam = {}
    for t, v in plan["tasks"].items():
        fam.setdefault(v["family"], []).append(t)
    w(f"- Tasks: " + ", ".join(f"{k} {len(v)}" for k, v in sorted(fam.items())))
    w(f"- Trials planned {len(plan['trials'])}, recorded {len(recs)}, infrastructure failures excluded "
      f"{len(infra)}{': ' + ', '.join(r['trial'] for r in infra) if infra else ''}\n")

    # manipulation and contamination checks
    w("## Did the manipulation take, and did anything leak\n")
    w("| Condition | Trials | Read INDEX | Read a target note | Read any note | Outside-workspace access | Trials with a tool denied | Timeouts | Max-turn or error exits |")
    w("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for cond in ["none", "minimal", "bundle", "ablated", "oracle", "oracle_placebo"]:
        rs = [r for r in valid if r["condition"] == cond]
        if not rs:
            continue
        def rd(r, pred):
            return any(pred(x) for x in r["trace"]["reads"])
        idx = sum(rd(r, lambda x: "knowledge/INDEX.md" in x) for r in rs)
        tgt = sum(rd(r, lambda x, r=r: any(n in x for n in plan["tasks"][r["task"]]["notes"])) for r in rs)
        anyn = sum(rd(r, lambda x: "knowledge/notes/" in x) for r in rs)
        out = sum(bool(r["trace"]["outside"]) for r in rs)
        to = sum(bool(r["invoke"]["timed_out"]) for r in rs)
        err = sum(bool(((r["trace"]["result"] or {}).get("subtype") or "success") != "success") for r in rs)
        den = sum(bool(r["trace"].get("denials")) for r in rs)
        w(f"| {cond} | {len(rs)} | {idx} | {tgt} | {anyn} | {out} | {den} | {to} | {err} |")
    w("\nA tool denial is an instrument defect when its rate differs between arms: the arms then differ in what the agent could do, "
      "not only in what it was told.")
    w("\nA target-note read in `ablated` is impossible by construction; in `none` and `minimal` any `.agents` read "
      "or outside access is contamination and is listed below.\n")
    leaks = [r for r in valid if r["trace"]["outside"]]
    for r in leaks[:20]:
        w(f"- `{r['trial']}` {r['task']} {r['condition']}: {r['trace']['outside'][:3]}")

    cell = cells(valid)
    w("\n## Success by task and condition (hidden tests; mean over repetitions)\n")
    conds = ["none", "minimal", "bundle", "ablated", "oracle", "oracle_placebo"]
    w("| Task | Family | " + " | ".join(conds) + " |")
    w("|---|---|" + "---:|" * len(conds))
    for t, v in sorted(plan["tasks"].items(), key=lambda kv: (kv[1]["family"], kv[0])):
        vals = []
        for c in conds:
            x = cell.get((t, c))
            vals.append(f"{sum(x)}/{len(x)}" if x else "")
        w(f"| {t} | {v['family']} | " + " | ".join(vals) + " |")

    levels = sorted({v.get("level", "L0") for v in plan["tasks"].values() if v["family"] == "judgment"})
    if len(levels) > 1 or levels != ["L0"]:
        w("\n## Judgment tasks by distance of the decisive fact (L0 beside the code, L1 in code elsewhere, L2 in distant docs or config)\n")
        w("| Level | Tasks | " + " | ".join(conds) + " |")
        w("|---|---:|" + "---:|" * len(conds))
        for lv in levels:
            ts = [t for t, v in plan["tasks"].items() if v["family"] == "judgment" and v.get("level", "L0") == lv]
            row = []
            for c in conds:
                xs = [x for t in ts for x in cell.get((t, c), [])]
                row.append(f"{sum(xs)}/{len(xs)}" if xs else "")
            w(f"| {lv} | {len(ts)} | " + " | ".join(row) + " |")

    w("\n## Secondary: the repository's visible tests still pass at the end (the agent's own tests included)\n")
    vcell = cells(valid, key=lambda r: bool(r["grade"]["visible"]["passed"]))
    w("| Family | " + " | ".join(conds) + " |")
    w("|---|" + "---:|" * len(conds))
    for f, ts in sorted(fam.items()):
        row = []
        for c in conds:
            xs = [x for t in ts for x in vcell.get((t, c), [])]
            row.append(f"{sum(xs)}/{len(xs)}" if xs else "")
        w(f"| {f} | " + " | ".join(row) + " |")

    w("\n## Reliability: pass^k (every repetition passes)\n")
    w("| Family | " + " | ".join(conds) + " |")
    w("|---|" + "---:|" * len(conds))
    for f, ts in sorted(fam.items()):
        row = []
        for c in conds:
            vs = [pass_hat_k(cell[(t, c)], plan["reps"]) for t in ts if (t, c) in cell]
            vs = [x for x in vs if not math.isnan(x)]
            row.append(f"{statistics.fmean(vs):.2f}" if vs else "")
        w(f"| {f} | " + " | ".join(row) + " |")

    w("\n## Contrasts (paired within task; the task is the unit)\n")
    prim = contrast(cell, plan, *PRIMARY)
    secs = [contrast(cell, plan, *c) for c in SECONDARY]
    holm(secs)
    w("| | Contrast | Family | Tasks | A | B | A − B | 95% CI (t) | 95% CI (cluster bootstrap) | p (sign-flip) | p (Holm) | MDE at 80% | Within ±10 pp (TOST) | Tasks better / worse / tied |")
    w("|---|---|---|---:|---:|---:|---:|---|---|---:|---:|---:|---|---|")
    for tag, r in [("**primary**", prim)] + [("secondary", r) for r in secs]:
        if not r.get("n_tasks"):
            w(f"| {tag} | {r['a']} − {r['b']} | {r['family']} | 0 | | | | | | | | | | |")
            continue
        ci = r["ci_t"]
        w(f"| {tag} | {r['a']} − {r['b']} | {r['family']} | {r['n_tasks']} | {r['mean_a']:.2f} | {r['mean_b']:.2f} | "
          f"{fmt(r['diff'], True)} | {'[' + fmt(ci[0], True) + ', ' + fmt(ci[1], True) + ']' if ci else '—'} | "
          f"[{fmt(r['ci_boot'][0], True)}, {fmt(r['ci_boot'][1], True)}] | {fmt(r['p'])} | {fmt(r.get('p_holm'))} | "
          f"{fmt(r['mde80'], True)} | {'—' if r['descriptive_only'] else ('yes' if r['tost_equivalent'] else 'no')} | {r['better']} / {r['worse']} / {r['tied']} |")
    w(f"\nA contrast over fewer than {MIN_TASKS} tasks is descriptive only: no interval, no p-value, no equivalence claim.")
    w("\nRead a contrast only against its MDE: a difference smaller than the MDE is not evidence of no effect, and "
      "\"within ±10 pp\" is the only form in which a null may be stated.\n")

    w("## Cost (geometric mean ratio of per-task means, 95% bootstrap CI)\n")
    cc = {k: cells(valid, key=lambda r, k=k: cost_of(r)[k]) for k in ("cost", "turns", "out_tokens", "wall")}
    w("| Ratio | Family | Tasks | Cost (USD) | Turns | Output tokens | Wall time |")
    w("|---|---|---:|---|---|---|---|")
    for a_, b_ in COST_CONTRASTS:
        for f, ts in sorted(fam.items()):
            parts, n = [], 0
            for k in ("cost", "turns", "out_tokens", "wall"):
                g = geo_ratio(cc[k], a_, b_, ts)
                if g:
                    n = g[3]
                    parts.append(f"×{g[0]:.2f} [{g[1]:.2f}, {g[2]:.2f}]")
                else:
                    parts.append("—")
            if n:
                w(f"| {a_} / {b_} | {f} | {n} | " + " | ".join(parts) + " |")

    w("\n## Exploratory: success in `bundle` by whether a target note was read\n")
    w("Correlational only: an agent that reads the note may differ from one that does not. The causal comparison "
      "is `oracle` against `oracle_placebo`.\n")
    for f in ("judgment", "boundary"):
        rs = [r for r in valid if r["condition"] == "bundle" and r["family"] == f]
        yes = [r["success"] for r in rs if any(n in x for x in r["trace"]["reads"] for n in plan["tasks"][r["task"]]["notes"])]
        no = [r["success"] for r in rs if r["success"] is not None and not any(n in x for x in r["trace"]["reads"] for n in plan["tasks"][r["task"]]["notes"])]
        w(f"- {f}: read {sum(yes)}/{len(yes)} passed; not read {sum(no)}/{len(no)} passed")

    w("\n## Sensitivity: a timeout or an error exit counted as a failure\n")
    sens = [dict(r, success=r["success"] and not r["invoke"]["timed_out"]
                 and ((r["trace"]["result"] or {}).get("subtype") or "success") == "success") for r in valid]
    ps = contrast(cells(sens), plan, *PRIMARY)
    if ps.get("n_tasks"):
        w(f"- Primary contrast under this rule: {fmt(ps['diff'], True)}, 95% CI [{fmt(ps['ci_t'][0], True) if ps['ci_t'] else '—'}, "
          f"{fmt(ps['ci_t'][1], True) if ps['ci_t'] else '—'}], p {fmt(ps['p'])}")
    text = "\n".join(L) + "\n"
    out = Path(a.out) if a.out else run / "report.md"
    out.write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
