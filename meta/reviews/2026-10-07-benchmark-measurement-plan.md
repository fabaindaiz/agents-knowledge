# Measuring performance and cost on external benchmarks: survey and plan

**Date:** 2026-10-07. **Status:** research by a delegated agent, a plan not yet decided; brought in from its scratch
directory. Every source below was read at its abstract or dataset card on
2026-10-07, paraphrased; claims taken from a secondary summary are marked ASSUMPTION.

## 1. Study 2 as it stands

- Plan: five blocks (E real issues from SWE-rebench post-cutoff, primary, two-sided +-10 pp; A competitive
  programming and D code reasoning, non-inferiority at 10 pp; B optimisation, secondary; C architecture,
  exploratory), arms `minimal` / `bundle` / `placebo`, routed controls (plant, decoy), A/A, gates G0-G4,
  forecasts, decision map. Tier 1 alone is about 2,500 confirmatory trials plus about 1,800 pilot trials.
- Blocked by: nothing of section 16 is built (adapters, graders, E's container and firewall, placebo
  pipeline, Study 2 analysis); waits on a budget cap, forecasts and a frozen tag (roadmap `i-5ed7e8-bf5663`,
  paused with Study 1); subscription-only runs (no API key), so throughput and the terms for automated use
  are open (G0.7); the focus moved to cost (`d-5ed7e8-7cac23`).
- Can show: on post-cutoff real issues, benefit / harm / equivalence at 10 pp, and the cost ratio.
  Cannot show: effects under 10 pp; anything about the notes' narrow claim (Study 1's job); other agents or
  vendors; a full bootstrap; method separated from knowledge. Its design predates skills, the reviewer
  subagent, the trigger wording and the cost levers; tools list says "no subagents, skills".

## 2. Benchmarks

| Benchmark | Licence (run locally / keep results) | Tasks | Setup | Per-task cost, Claude Code | Contamination | Use |
|---|---|---|---|---|---|---|
| SWE-rebench leaderboard | CC-BY-4.0 dataset; monthly splits on the hub end 2026_03; the site's window runs to July 2026 (111 tasks / 65 repos), newer tasks' downloadability unchecked | ~160 post-2026-02 on the hub | prebuilt image per task, Docker, large disk | site lists a Claude Code reference at a few dollars and a few million tokens per problem, 93% cached (model unstated) | low for tasks opened after the model's cutoff | primary |
| SWE-bench Pro, public | harness MIT; task content under the 11 upstream repos' licences (copyleft, chosen to deter training) | 731 (v1) / 642 (v2) + 51 hard; Go, Python, JS, TS | images on ghcr.io, anonymous pull; Harbor task format | ASSUMPTION: higher than rebench (harder, longer) | low-moderate (public since 2025, copyleft) | external-validity block, or fallback if the rebench pool is short |
| SWE-bench Verified / Lite / Verified Mini | harness MIT; content from upstream repos | 500 / 300 / 50 | full ~130 GB images; Mini ~5 GB | ~$2-3 (ASSUMPTION) | high: a lab audit in Feb 2026 reported flawed tests and verbatim fixes (ASSUMPTION, secondary sources; primary page refused the fetch) | instrument checks only (controls, probe, A/A), where contamination does not matter |
| SWE-bench-Live | MIT | 3,688 rows; monthly +50; issues to Aug 2025 per the card; some multi-language and Windows | Docker per task | ~$2-3 (ASSUMPTION) | pre-cutoff for current models | excluded (as at Study 2's G0) |
| Multi-SWE-bench | CC0, subject to upstream licences | 1,632; Java, TS, JS, Go, Rust, C, C++ | Docker; ~1.8 GB data | ASSUMPTION ~$2-4 | moderate (2025) | optional language spread, secondary |
| Terminal-Bench 2.0 | Apache-2.0 | 89 | Docker via Harbor, which ships a `claude-code` agent | ASSUMPTION $1-5, some tasks long | moderate (public since late 2025, tests public) | optional "non-SWE agentic" no-harm block, replaces Study 2's A as the unrelated-work test |
| Aider polyglot | Exercism exercises under their open licences; aider's harness | 225, six languages | light, no images | cents to tens of cents | high, near ceiling for frontier models | not useful (ceiling) |

Context files and skills on such benchmarks:

- Gloaguen et al. 2026 (arXiv 2602.11988): SWE-bench Lite (300) and a new 138-instance set from 12 repos with
  developer-written files; Claude Code with Sonnet 4.5 among four agents. Generated files: success -0.5 to -2
  pp, cost +20 to +23%, +2.5 to +3.9 steps. Developer files: +2.4 pp, not significant, cost up to +19%.
- Lulla et al. 2026 (arXiv 2601.20404): 124 PRs in 10 repos, Codex and Claude Code: an AGENTS.md cut median
  runtime by about 29% and output tokens by about 17%, completion comparable.
- Khatri 2026 (arXiv 2607.27250): 17 tasks, 3 repos, Claude Code and Codex, 288 runs: no measurable change in
  correctness, bounded to 10-15 pp by equivalence tests.
- SWE-Skills-Bench (arXiv 2603.15401): public SE skills, mean gain about one point, most none.
- Token spend (arXiv 2604.22750): same task varies up to ~30x in tokens across runs; more spend does not buy
  accuracy past a middle point.

## 3. Plan

### Question, re-scoped

"Does release X keep the base model's success on externally sourced, post-cutoff real issues (non-inferior
at 10 pp), and what does it cost against the base model and against the previous release?" Benefit is a
secondary two-sided reading; the notes' narrow claim stays with Study 1 and its 6-task cost pilot.

### Arms

- `minimal`: the two-line root file from the task's metadata.
- `release`: the frozen tag as a carrier carries it: `.agents/`, the root file's wiring lines, and
  `.claude/` with the three skills and the reviewer subagent installed (their listings are standing cost).
- `lever-k` (at most two): `release` with one lever. Candidates: deferred loading by task complexity
  (triage, widen on failure); script lookup (a tool returns the card for a change, no index read);
  lookup in a subagent; shorter index (D2 measured at x0.97 for the author and x0.91 for the reviewer, so not
  a confirmatory arm). Entry rule, registered: a lever enters only if the standing smoke shows cost vs
  `release` at x0.85 or below with no discriminating Study 1 task lost.
- Dropped for now, with reasons: `placebo` (attribution matters only after a benefit or harm; add then);
  blocks A, B, C, D (the trigger keeps the bundle closed on unrelated small tasks, x0.95-1.17 in pilots
  6, 8, 9; Terminal-Bench is the optional replacement).

Skills: benchmark prompts are one-shot issue fixes, so `close`, `decision-review` and `user-walk` should not
fire; any `Skill` call is recorded as a misfire (predicted 0) and its cost counted. Firing is measured by
`evals/skills/trigger.py`, not here. Reviewer: on request only, so it never runs; an exploratory
`release+review` arm (review before claiming done) on 30 tasks x 2 reps is the only external test of whether a
review converts failures, priced by pilot-7's x8.

### Size (from `evals/power_tost.py`, Beta(0.6, 0.6), 1,000 sims, unclustered)

| Design | P(NI) at 0 | P(NI) at -10 pp | P(harm) at -10 | P(TOST) at 0 |
|---|---:|---:|---:|---:|
| 89 x 3, SD 10/20 pp | 0.91 / 0.86 | 0.06 | 0.86 / 0.74 | 0.82 / 0.72 |
| 120 x 2, SD 10/20 | 0.89 / 0.87 | 0.04 | 0.83 / 0.76 | 0.76 / 0.72 |
| 120 x 3, SD 10/20 | 0.97 / 0.94 | 0.05 | 0.93 / 0.89 | 0.94 / 0.87 |
| 60 x 2 at 15 pp margin | 0.91 / 0.89 | 0.05 | 0.85 / 0.80 | 0.82 / 0.79 |
| 5 pp margin, 300 x 2 | 0.76 | 0.06 | 0.62 | 0.48 |

A 5 pp margin is unaffordable. Recommended confirmatory: 120 tasks x 2 reps (or x3 if the cap allows).
Cost: geometric mean of per-task ratios; pilot-9's paired log-ratio SD was 0.39 on small tasks; at an assumed
0.6 on real issues, 30 tasks give a 95% interval of about x/1.25, 120 tasks x/1.12.

### Predictions and decision rules (to fill before G2)

- H1 success: `release` - `minimal` non-inferior at -10 pp (ITT and per protocol).
- H2 cost: rho(release/minimal) within [1.1, 1.8] on real issues (Study 1's x2.1-2.3 came from small tasks;
  Gloaguen's +20% is the floor for an always-loaded file).
- H3 each lever: non-inferior to `release` at -10 pp and rho(lever/release) upper bound below 1.0; Holm
  across levers.
- Rules: H1 fails -> the release is not tagged as "no worse" and the decision map's Harm row applies; a lever
  meeting H3 ships; rho above 2 weighs against any cell short of Benefit (Study 2 section 14 step 3).

### What runs when

| | Contents | Trials | List-price cost (US dollars, order of magnitude) | Wall time (3 jobs) |
|---|---|---:|---:|---:|
| Every release (standing smoke) | Study 1's 6-task cost pilot, 2 reps (existing) + 24 fresh post-cutoff rebench tasks x 1 rep x {minimal, candidate}; drawn anew each release by seed | 36 + 48 | a few dollars + about a hundred | ~1 h + ~3-4 h |
| Cheaper smoke option | 12 tasks instead of 24 | 36 + 24 | a few dollars + about half a hundred | ~1 h + ~2 h |
| Once (confirmatory) | pilot (A/A 30 x 2; plant and decoy on 30 pre-cutoff Verified Mini or rebench tasks x 2) + 120 x 2 x {minimal, release, up to 2 levers} | ~300 + 480-960 | several hundred + one to a few thousand | ~1.5-3 weeks on a subscription |

Smoke rules: it decides cost only (interval vs the x2.0 line and its refutation, as pilots 6-9); success is
a tripwire (candidate fails 3 or more tasks `minimal` passes with none the other way -> stop and look), never
a verdict. Per-trial cost: ~$2 `minimal`, ~$3 bundle arms, ~10-15 min (ASSUMPTION from the rebench reference
re-priced at the pilots' list prices; G1 measures it).

### Needs the owner's approval

- Nothing from any benchmark enters the repository: only task ids, content hashes, seeds and per-trial
  outcomes; adapters written in-house. Installing a third-party harness (Harbor, Apache-2.0; SWE-bench's MIT
  harness) outside the repository, and pulling the task images (hundreds of GB for 120+ tasks, ASSUMPTION),
  needs the owner's yes.
- The subscription's terms for automated headless runs (G0.7); a budget cap; forecasts.
- Whether to amend Study 2 (draft 3: E-only, cost-first) or register this as its own protocol.
