#!/usr/bin/env python3
"""The reviewer pilot: does the knowledge reviewer find the card a change needs, and what does reading cost it?

    python3 evals/review.py plan RUN --model M [--reps K] [--seed S] [--config-dir D]
    python3 evals/review.py run RUN
    python3 evals/review.py report RUN

Each trial gives the `knowledge-reviewer` its own instructions and one fixed diff, applied uncommitted to a fresh
copy of a task's repository, in one headless session with the reviewer's tools. Two arms: `R0`, the current
release's index; `R2`, the index split of design D2 (`harness.d2_index`). The diffs are the naive and the reference
overlay of six tasks, one per target note, and the reference overlay of three tasks no note concerns. The outcomes
are read from the transcript: which cards it opened, whether it opened and named the target card, whether it read
`PHASES.md`, and the input tokens it spent. Registered in `PROTOCOL.md` before any trial. Standard library only;
it reuses the harness and never changes it, so a run of the harness can be resumed under its frozen hash.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import random
import statistics
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness as H  # noqa: E402

ARMS = ("R0", "R2")
ALL_ARMS = ("R0", "R2", "RC")  # RC: the current release with the check phase shortened (d-5ed7e8-8174a8)
SHORT_CHECKS = (
    "5. **One check per applicable card, then stop when every card has its verdict.** Batch your first reads\n"
    "   in one message. A check that needs a planted fault, a scratch copy or a new test is not run here: it comes back\n"
    "   as a finding, the test the author must write. Stop when each card you opened is applied, excluded or\n"
    "   overridden, with its evidence; do not look further for the author.\n")
TARGET_TASKS = ("contacts-second-source-l1", "refund-webhook-l1", "delivery-email-once-l1",
                "recommendations-kill-switch-l1", "settings-notification-preferences-l1", "api-page-size-limit-l1")
NEUTRAL_TASKS = ("inventory-csv-export", "cli-help-typo", "report-label-rename")
REVIEWER_TOOLS = ["Read", "Grep", "Glob", "Bash"]
CARD = re.compile(r"knowledge/cards/([\w-]+)\.md")


def diff_set() -> list[dict]:
    """Every diff the pilot reviews: each target task's naive and reference overlay, each neutral task's reference."""
    out = []
    for task in TARGET_TASKS:
        notes = H.load_task(task)["notes"]
        out += [{"task": task, "variant": v, "targets": notes} for v in ("naive", "reference")]
    out += [{"task": task, "variant": "reference", "targets": []} for task in NEUTRAL_TASKS]
    return out


def prepare(task_id: str, variant: str, arm: str, ws: Path) -> dict:
    """A fresh copy of the task's repository with the overlay applied and not committed, and the arm's bundle."""
    task = H.load_task(task_id)
    shutil.copytree(Path(task["dir"]) / "repo", ws, ignore=shutil.ignore_patterns("__pycache__"))
    H.copy_bundle(ws)
    agents = ws / ".agents"
    # A release as a carrier holds it: the home's own files (its carrier file, its proposals) are not part of it.
    (agents / "carrier.toml").unlink(missing_ok=True)
    for p in (agents / "proposals").glob("p-*.md"):
        p.unlink()
    info: dict = {}
    if arm == "R2":
        info["d2"] = H.d2_index(agents)
    H.git(ws, "init", "-q")
    H.git(ws, "add", "-A")
    H.git(ws, "commit", "-q", "-m", "start")
    H.overlay(Path(task["dir"]) / variant, ws)
    info["diff"] = H.git(ws, "diff", "--", ".", ":(exclude).agents")
    return info


def prompt(diff: str, arm: str = "R0") -> str:
    """The reviewer's own instructions, without the frontmatter the host reads, and the change to review; for `RC`,
    the check step shortened and nothing else changed."""
    text = (H.BUNDLE / "agents" / "knowledge-reviewer.md").read_text()
    body = text.split("\n---\n", 1)[1] if text.startswith("---") else text
    if arm == "RC":
        step = re.search(r"^5\. \*\*Run each applicable card's check\*\*.*?(?=^6\. )", body, re.S | re.M)
        if step is None:
            raise RuntimeError("the reviewer's check step was not found; the RC arm cannot be built")
        body = body[:step.start()] + SHORT_CHECKS + body[step.end():]
    return body.strip() + "\n\nThe change to review, as `git diff` (applied, not committed, in this repository):\n\n```diff\n" \
        + diff.rstrip() + "\n```\n"


def outcomes(transcript: Path, ws: Path, targets: list[str]) -> dict:
    """What the reviewer opened, whether it found and named the target card, and the input it paid for."""
    trace = H.parse_transcript(transcript, ws)
    final, usage, result, first_card = "", {}, {}, None
    for line in transcript.read_text(errors="replace").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "result":
            final, usage, result = ev.get("result") or "", ev.get("usage") or {}, ev
        if ev.get("type") == "assistant" and first_card is None:
            msg = ev.get("message") or {}
            if any(b.get("type") == "tool_use" and CARD.search(json.dumps(b.get("input", {})))
                   for b in msg.get("content", [])):
                # the context the reviewer held when it chose its first card: what reading the index cost it
                u = msg.get("usage") or {}
                first_card = sum(u.get(k, 0) for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))
    cards = []
    for read in trace["reads"]:
        m = CARD.search(read)
        if m and m.group(1) not in cards:
            cards.append(m.group(1))
    return {"cards": cards, "target_opened": any(t in cards for t in targets),
            "target_named": any(t in final for t in targets),
            "phases_read": any(r.endswith("knowledge/PHASES.md") for r in trace["reads"]),
            "index_read": any(r.endswith("knowledge/INDEX.md") for r in trace["reads"]),
            "input_tokens": sum(usage.get(k, 0) for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")),
            "first_card_context": first_card,
            "output_tokens": usage.get("output_tokens", 0), "cost": result.get("total_cost_usd"),
            "turns": result.get("num_turns"), "final": final[:4000], "outside": trace["outside"]}


def session_failure(invoke: dict, events: list[dict]) -> str | None:
    """Why a session measured nothing, or None: a timeout, no result event, or an error result other than the
    registered turn limit, which is the design's and a valid trial (`evals/REPORT.md` §4.13)."""
    if invoke.get("timed_out"):
        return "the session timed out"
    results = [e for e in events if e.get("type") == "result"]
    if not results:
        return "no result event"
    last = results[-1]
    if last.get("subtype") == "error_max_turns":
        return None
    if last.get("is_error") or str(last.get("subtype", "")).startswith("error"):
        return f"the session ended in {last.get('subtype') or 'an error'}"
    return None


def done_trials(lines: list[str]) -> set[str]:
    """The trials a resume skips: those with a result, never one that errored, which runs again."""
    out = set()
    for line in lines:
        if line.strip():
            rec = json.loads(line)
            if not rec.get("harness_error"):
                out.add(rec["trial"])
    return out


def cmd_plan(args) -> int:
    run = Path(args.run)
    if (run / "plan.json").exists():
        raise SystemExit(f"{run}/plan.json exists: a plan is frozen once written")
    cfg = args.config_dir if args.config_dir == H.DEFAULT_CONFIG else str(Path(args.config_dir).expanduser())
    claude = H.claude_bin(None)
    arms = tuple(a for a in args.arms.split(",") if a) if getattr(args, "arms", None) else ARMS
    if unknown := [a for a in arms if a not in ALL_ARMS]:
        raise SystemExit(f"unknown arms {unknown}: one of {ALL_ARMS}")
    trials = [{**d, "arm": arm, "rep": rep} for rep in range(args.reps) for d in diff_set() for arm in arms]
    rng = random.Random(args.seed)
    for rep in range(args.reps):
        block = [t for t in trials if t["rep"] == rep]
        rng.shuffle(block)
        trials = [t for t in trials if t["rep"] != rep] + block
    for i, t in enumerate(trials):
        t["order"], t["trial"] = i, hashlib.sha256(f"{args.seed}:{i}:{t['task']}:{t['variant']}:{t['arm']}".encode()).hexdigest()[:10]
    sums = H.BUNDLE / "SHA256SUMS"
    plan = {"created": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "model": args.model, "effort": None,
            "claude": claude, "claude_version": subprocess.run([claude, "--version"], capture_output=True, text=True).stdout.strip(),
            "config_dir": cfg, "seed": args.seed, "reps": args.reps, "max_turns": args.max_turns, "timeout_s": args.timeout,
            "tools": REVIEWER_TOOLS, "arms": list(arms), "bundle_digest": hashlib.sha256(sums.read_bytes()).hexdigest()[:12],
            "module_hash": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16],
            "harness_hash": hashlib.sha256((HERE / "harness.py").read_bytes()).hexdigest()[:16], "trials": trials}
    run.mkdir(parents=True, exist_ok=True)
    (run / "plan.json").write_text(json.dumps(plan, indent=1))
    print(f"review plan: {len(trials)} trials, {len(diff_set())} diffs x {len(arms)} arms x {args.reps}; bundle {plan['bundle_digest']}")
    return 0


def cmd_run(args) -> int:
    run = Path(args.run)
    plan = json.loads((run / "plan.json").read_text())
    if hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16] != plan["module_hash"]:
        raise SystemExit("evals/review.py changed since the plan was frozen; write a new plan")
    done = set()
    if (run / "results.jsonl").exists():
        done = done_trials((run / "results.jsonl").read_text().splitlines())
    pending = [t for t in plan["trials"] if t["trial"] not in done]
    print(f"{len(done)} done, {len(pending)} to run", flush=True)
    for tr in pending:
        base = H.workspace_base(None) / f"review-{tr['trial']}"
        if base.exists():
            shutil.rmtree(base)
        ws = base / "ws"
        rec = {**tr}
        try:
            info = prepare(tr["task"], tr["variant"], tr["arm"], ws)
            digest = hashlib.sha256((ws / ".agents/SHA256SUMS").read_bytes()).hexdigest()[:12]
            if tr["arm"] in ("R0", "RC") and digest != plan["bundle_digest"]:
                raise RuntimeError(f"the bundle is {digest}, the plan froze {plan['bundle_digest']}")
            settings = base / "settings.json"
            settings.write_text(json.dumps(H.trial_settings(ws), indent=1))
            art = run / "trials" / tr["trial"]
            art.mkdir(parents=True, exist_ok=True)
            rec["invoke"] = H.invoke(plan, ws, prompt(info["diff"], tr["arm"]), settings, art / "transcript.jsonl",
                                     plan["max_turns"], plan["timeout_s"], tools=REVIEWER_TOOLS)
            events = [json.loads(l) for l in (art / "transcript.jsonl").read_text().splitlines() if l.strip().startswith("{")] \
                if (art / "transcript.jsonl").is_file() else []
            if failure := session_failure(rec["invoke"], events):
                raise RuntimeError(failure)
            rec["out"] = outcomes(art / "transcript.jsonl", ws, tr["targets"])
            rec["d2"] = info.get("d2")
        except Exception as e:  # an infrastructure failure: recorded, never dropped
            rec["harness_error"] = repr(e)
        with open(run / "results.jsonl", "a") as f:
            f.write(json.dumps(rec) + "\n")
        o = rec.get("out") or {}
        print(f"{tr['order']:3d} {tr['arm']} {tr['task']:38s} {tr['variant']:9s} cards={len(o.get('cards', []))} "
              f"target={'opened' if o.get('target_opened') else '-'}/{'named' if o.get('target_named') else '-'} "
              f"in={o.get('input_tokens')} {rec.get('harness_error', '')}", flush=True)
        shutil.rmtree(base, ignore_errors=True)
    return 0


def cmd_report(args) -> int:
    run = Path(args.run)
    recs = [json.loads(l) for l in (run / "results.jsonl").read_text().splitlines() if l.strip()]
    ok = [r for r in recs if r.get("out") and not r.get("harness_error")]
    lines = ["# Reviewer pilot", "", f"{len(ok)} valid trials of {len(recs)}.", "",
             "| Arm | Diffs | Target opened (naive) | Target named (naive) | Target named (reference) | Cards on neutral (mean) "
             "| Read PHASES.md | Input tokens (mean) |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    means = {}
    for arm in ARMS:
        rs = [r for r in ok if r["arm"] == arm]
        naive = [r for r in rs if r["variant"] == "naive"]
        refs = [r for r in rs if r["variant"] == "reference" and r["targets"]]
        neutral = [r for r in rs if not r["targets"]]
        means[arm] = sum(r["out"]["input_tokens"] for r in rs) / len(rs) if rs else 0
        frac = lambda xs, k: f"{sum(r['out'][k] for r in xs)}/{len(xs)}"  # noqa: E731
        lines.append(f"| {arm} | {len(rs)} | {frac(naive, 'target_opened')} | {frac(naive, 'target_named')} | "
                     f"{frac(refs, 'target_named')} | "
                     f"{(sum(len(r['out']['cards']) for r in neutral) / len(neutral)) if neutral else 0:.1f} | "
                     f"{frac(rs, 'phases_read')} | {means[arm]:.0f} |")
    if means.get("R0"):
        lines += ["", f"R2 / R0 input tokens: ×{means['R2'] / means['R0']:.2f} by the arms' means."]
    pairs: dict = {}
    for r in ok:
        pairs.setdefault((r["task"], r["variant"], r["rep"]), {})[r["arm"]] = r["out"]
    both = [v for v in pairs.values() if "R0" in v and "R2" in v]
    for key, label in (("cost", "estimated cost (primary)"), ("input_tokens", "cumulative input"),
                       ("first_card_context", "context at the first card")):
        ratios = [v["R2"][key] / v["R0"][key] for v in both if v["R0"].get(key) and v["R2"].get(key)]
        if ratios:
            geo = math.exp(sum(math.log(x) for x in ratios) / len(ratios))
            lines.append(f"R2 / R0 {label}: ×{geo:.2f}, geometric mean of {len(ratios)} paired diffs, "
                         f"median ×{statistics.median(ratios):.2f}.")
    (run / "report.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("run")
    p.add_argument("--model", required=True)
    p.add_argument("--reps", type=int, default=2)
    p.add_argument("--seed", type=int, default=20261008)
    p.add_argument("--config-dir", default=H.DEFAULT_CONFIG)
    p.add_argument("--max-turns", type=int, default=30)
    p.add_argument("--arms", default="", help=f"comma-separated, of {ALL_ARMS} (default: {','.join(ARMS)})")
    p.add_argument("--timeout", type=int, default=900)
    for name in ("run", "report"):
        sub.add_parser(name).add_argument("run")
    a = ap.parse_args(argv)
    return {"plan": cmd_plan, "run": cmd_run, "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
