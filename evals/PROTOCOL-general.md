# Study 2 — does carrying the bundle change a coding agent's general performance? — protocol

**Status: draft 2, for review. Not frozen; no Study 2 data exist.** This is the plan: the question, the
competing explanations, falsifiable hypotheses, the task blocks, the controls that make the test severe,
the gates each stage must pass, the analysis, the forecasts and what each result would mean. It becomes a
pre-registration when gate G2 (§10) is passed: from then on nothing above *Deviations* is edited, and
every change is appended there with its date and reason. §20 lists what changed from draft 1, and why.

Like [`PROTOCOL.md`](PROTOCOL.md), this directory is not part of the bundle and does not travel to carriers.

## 0. Summary

| Block | Measures | Source (not written by the bundle's authors) | Grading | Tasks × reps | Role |
|---|---|---|---|---|---|
| **E** Real issues | the work a carrier actually does | SWE-rebench, Python tasks whose fix was opened on or after 2026-02-01 | fail-to-pass and pass-to-pass tests, on a fresh image | all eligible (≈ 150–167) × 3 | **primary**: benefit or harm |
| **A** Competitive programming | algorithmic problem solving, any correct solution | LiveCodeBench Pro, contests with published test data | local judge, full tests, time and memory limits | 120 × 3 | confirmatory: no harm |
| **D** Code reasoning | predicting what real code does, without running it | SWE-Flux, perturbed variants | exact match on a schema | 120 × 5 | confirmatory: no harm |
| **B** Algorithm design with a score | optimisation quality, continuous | ALE-Bench | official scorer, performance | 36 × 3 | secondary |
| **C** Architecture by consequence | whether a design absorbs later change | SlopCodeBench, with a fixed second agent | hidden tests of later checkpoints | 12 × 2 | exploratory pilot |

Three arms: `minimal` (control), `bundle` (the bundle plus the two lines a carrier's bootstrap writes) and
`placebo` (the same, with the knowledge base replaced by off-task software-engineering notes of the same
shape and size). **Block E decides whether the bundle helps or hurts ordinary work** (two-sided, ±10 pp
equivalence band). **Blocks A and D decide whether it harms work it has nothing to say about**
(non-inferiority, margin 10 pp). Before any confirmatory trial, two *routed* controls must show that
content reached through the index can move the outcome in either direction, and an A/A run must show
the instrument stays quiet when there is nothing to find. The pilot's treatment contrasts stay hidden
until the end.

## 1. Why a second study

Study 1 ([`PROTOCOL.md`](PROTOCOL.md), [`REPORT.md`](REPORT.md)) asked whether a note's content changes a
decision where the textbook answer is wrong. Its tasks were written from the notes: every task names its
target note (`task.json`, field `notes`), the hidden test checks that note's claim, the author of the tasks
had read the notes, and the `oracle` arm receives the note in full. A pass in a note-carrying arm partly
measures whether an instruction reached a decision, on a task built to reward that instruction. Pilot-5
states the mechanism: the agents *did not find the fact; they applied the principle by default*.

That question (**instruction transfer**) is legitimate, and Study 1 keeps answering it. It cannot answer
the question that decides whether a repository should carry the bundle: **does the agent do better or worse
work in general, on work nobody chose to suit the bundle, and at what price?** Study 2 asks that. It shares
no task with the notes and does not replace Study 1.

## 2. The question, the estimands, the scope

> When a repository carries the bundle, wired in the way a carrier's bootstrap wires it, does the agent's
> success on externally sourced, objectively graded work change, and at what cost?

**The treatment.** The whole `.agents/` bundle at one frozen version tag, plus the two lines the bootstrap
writes into a carrier's root file ([`prompt-bootstrap.md`](../.agents/method/prompt-bootstrap.md),
phase 4), in this fixed wording:

~~~text
- Before a design decision or before claiming done, consult `.agents/knowledge/INDEX.md` and read only the notes it points to for the task.
- Nothing written into `.agents/` or any file that leaves this repository may identify, directly or by reconstruction, a private repository, its people or its users; `python3 .agents/tools/bundle.py privacy .agents` checks it.
~~~

*Amended 2026-09-25.* From release 0.0.22 the bundle ships short notes and cards, not the full notes;
the treatment is identified by its version tag and the sha256 of `.agents/SHA256SUMS` (the plan keys
`bundle_version` and `bundle_digest`). The bootstrap's wiring now names a trigger (a change touching state,
a contract, data, security or verification) and the card; the wording above is the draft's, and the
verbatim lines are taken from the frozen release's bootstrap, phase 4, at G2. Any run measures 0.0.22 or
later, not v0.0.21, which Study 1's pilots carried.

This wording is not Study 1's `ROUTING` paragraph, whose framing ("where the textbook answer … is wrong")
no carrier receives. The rest of a real bootstrap is out of scope, because it rewrites a repository's
whole instruction layer and cannot be reproduced over 150 external repositories: the repository-specific
rules, the audits and hooks, and the method's paste-in session prompts. **Every conclusion is scoped to
"the bundle plus its two wiring lines".** The method reaches the agent only if the agent chooses to read
`method/`, which is recorded.

**Estimands, per block b and model:**

- **Δ_b** = mean over the block's task population of [P(success | `bundle`) − P(success | `minimal`)].
  The population is the block's frame (§7). In D it is the items of the framed repositories, with the
  repositories treated as fixed.
- **Δ'_b** = the same for `bundle` − `placebo`. **Π_b** = the same for `placebo` − `minimal`.
- **ρ_b** = geometric mean over tasks of the ratio of mean cost, `bundle` / `minimal`.
- **In B**, success is replaced by the problem's performance score (§7.B).

**Out of scope:** how often a note applies in real work beyond what E shows; other agents and other
vendors' models (§18); code quality judged by anyone's taste.

## 3. Competing explanations, and what each predicts

A weak test predicts only a direction; a strong one predicts a range the data could contradict (Meehl
1967, 1990). Four explanations are on the table, and each forbids some outcomes.

| Explanation | Mechanism | E | A, D (unrelated work) | Cost ρ_E | `placebo` |
|---|---|---|---|---|---|
| **T0 Irrelevance** | the content bears on judgment calls ordinary work rarely meets; the agent pays to consult it and otherwise ignores it | *Equivalent* | non-inferior | > 1 | Π ≈ 0 |
| **T1 General uplift** (the belief of someone installing it) | the notes, and the method when read, make the agent more careful: it tests and checks more and catches more of its own mistakes | ***Benefit*** (≥ 10 pp) | non-inferior | > 1 | Π ≈ 0 |
| **T2 Context cost** (Du et al. 2025; Hong et al. 2025; Shi et al. 2023) | a large corpus the agent is told to consult uses turns, time and attention, and distracts | ***Harm*** | ***Harm*** where consulting it happens | > 1 | Π ≈ Δ (volume, not content) |
| **T3 The bundle's own claim** | a note helps where its situation holds; otherwise nothing happens | *Equivalent*, or a benefit under 10 pp concentrated where a note applies | non-inferior | > 1 | Π ≈ 0 |

What the confirmatory data can and cannot separate:

- ***Equivalent* in E, with no harm in A and D,** refutes T1 and T2 at the 10 pp scale. It does not
  separate T0 from T3; only the exploratory subgroup in E (§4) and Study 1 bear on that.
- ***Benefit* in E** refutes T0 and T2. The attribution rule (§5) rules volume in or out, and the
  subgroup hints at T1 against T3.
- ***Harm* anywhere** refutes T0, T1 and T3 for that block. The attribution rule then separates volume
  (T2) from content.
- **T2 is testable in A and D only as far as the agent consults the bundle there.** Budgets are
  generous, so T2's specific form, *harm through budget exhaustion*, is tested through the exhaustion
  rate per arm (§4, H-exh). The harm test itself does not depend on that mechanism.

## 4. Hypotheses

Each hypothesis states its contrast, its prediction, the result that refutes it, and its severity: the
probability that the planned run refutes it if it is false (Mayo 2018). The severity figures come from
`python3 evals/power_tost.py`, on effects measured as realised means, across per-task effect SDs of
10, 20 and 30 pp. §11 gives the tables, and the analysis script's simulation mode replaces them at G0.
Verdict names are defined in §5.

### Family P, primary: E decides benefit or harm (α = 0.05, alone in its family)

| Id | Contrast | Prediction (T0, T3) | Refuted by | Severity, 120 tasks × 3 reps (E will have more) |
|---|---|---|---|---|
| **H-E** | Δ_E | *Equivalent* within ±10 pp. T1 predicts *Benefit*; T2 predicts *Harm* | *Benefit* or *Harm* | P(*Harm* \| −10 pp) = 0.82–0.93; P(*Benefit* \| +10) = 0.83–0.93; P(*Equivalent* \| 0) = 0.77–0.93; P(*Equivalent* \| ±10) ≤ 0.06 |

### Family N, confirmatory: no harm on unrelated work

"No harm on unrelated work" means both A and D are non-inferior. That is an intersection-union claim, so
each test runs at one-sided α = 0.05 with no correction.

| Id | Contrast | Prediction | Refuted by | Severity, 120 tasks |
|---|---|---|---|---|
| **H-A** | Δ_A | *Non-inferior* (margin −10 pp) | the one-sided 95% lower bound at or below −10 pp | P(*Non-inferior* \| 0) = 0.89–0.97; P(*Non-inferior* \| −10) = 0.04–0.06 |
| **H-D** | Δ_D, 5 reps | *Non-inferior* (margin −10 pp) | as H-A | P(*Non-inferior* \| 0) ≥ 0.98; P(*Non-inferior* \| −10) ≤ 0.06 |

A two-sided test of A and D, with Holm across the two, labels any *Harm* or *Benefit* there. The
severity of that label: P(*Harm* \| −10 pp) = 0.74–0.88 in A and 0.94–0.98 in D.

### Secondary (each labelled; none overrides a primary verdict)

| Id | Contrast | Prediction | Refuted by |
|---|---|---|---|
| **H-cost** | ρ_E and ρ_A | ρ_E ∈ [1.1, 2.0] and ρ_A ∈ [1.0, 2.5]. The fixed cost of reading the bundle is a smaller share of a 45-minute repository task than of Study 1's small tasks, where it was ×2.1 to ×2.3 | the 95% interval entirely outside the predicted range |
| **H-B** | Δ_B, paired Hodges–Lehmann shift in performance | *Non-inferior* (margin −100 points) | the one-sided 95% lower bound at or below −100 |
| **H-attr** | the attribution ratio R_b = Π_b / Δ_b, in any block with a *Benefit* or *Harm* | T2: R near 1; content: R near 0 | classification by the rule in §5 |
| **H-exh** | the budget-exhaustion rate, `bundle` − `minimal`, per block | T2 predicts higher in `bundle`; the others predict no difference | a significant difference in the direction opposite to the prediction |
| **H-haiku** | H-E, H-A and H-cost for Haiku 4.5 | *Equivalent* and *Non-inferior*; ρ below Sonnet 5's (Study 1: 1.6 against 2.3) | as the Sonnet 5 hypotheses, as a separate family |

### Exploratory (labelled; never used for a verdict)

**E subgroup.** A frozen keyword classifier, fixed in this protocol before the pilot, applied to each
task's issue text and gold patch. A task counts as *note-relevant* if either one matches, case-folded, any
of these terms:

~~~text
retry, retries, idempot, timeout, duplicate, deduplic, at-least-once, redeliver, partial update, patch semantics, merge, upsert, identifier collision, namespace, fallback, default value, fail open, fail closed, kill switch, feature flag, cache invalidation, stale, clock, timezone, as-of, rotation, sanitiz, escape
~~~

Δ_E is then compared between note-relevant and other tasks. A benefit counts as "concentrated" if the
note-relevant Δ exceeds the other tasks' Δ by at least 10 pp and the interaction interval excludes 0.
That is a hypothesis for a later study, not a finding.

The other exploratory analyses:

- **Per protocol:** Δ among `bundle` trials that opened the index.
- **Mediation:** tokens read from `.agents/`, as a mediator of Δ and Π.
- **Heterogeneity:** the share of tasks where `bundle` did worse and where it did better (SkillsBench
  found 13 of 87 tasks worse with curated skills), and Δ by difficulty tier.
- **Reliability and cost:** pass^3 per arm (Yao et al. 2024), and success against cost as a Pareto plot
  (Kapoor et al. 2024).
- **Contamination:** the ceiling mass, meaning the share of tasks `minimal` passes every time, per block.
- **Block C** in full.

## 5. Verdict rules

Fixed now, so no reading is chosen after the data are seen (Lakens, Scheel & Isager 2018). Here d is the
per-task paired difference; the intervals come from the cluster-robust test of §12, by inversion, so that
a test and its interval never disagree.

| Verdict | Rule |
|---|---|
| **Benefit** | the two-sided test is significant at its family's level and mean d > 0 |
| **Harm** | the two-sided test is significant at its family's level and mean d < 0 |
| **Equivalent** (E) | not significant, and the 90% interval lies inside (−10, +10) pp |
| **Non-inferior** (A, D; B with −100 points) | the one-sided 95% lower bound lies above −margin |
| **Inconclusive** | none of the above. Reported as "not detected; effects up to the interval's bound could not be excluded", never as "no effect" |

A significant result whose 90% interval also lies inside (−10, +10) pp is reported as *Benefit (trivial)*
or *Harm (trivial)*. It counts as *Benefit* or *Harm* for forecast scoring, and as "no effect of practical
size" in the decision map.

**Both analyses must agree.** *Equivalent* and *Non-inferior* hold only if they hold by intention-to-treat
(ITT, every trial) and per protocol (PP, `bundle` trials that opened `INDEX.md`, against every `minimal`
trial), as the CONSORT extension for non-inferiority and equivalence trials asks (Piaggio et al. 2012).
If ITT supports the verdict and PP does not, it is reported as "holds only by intention-to-treat", which
means "carrying it does no harm, but reading it may". Uptake, the share of `bundle` trials that opened the
index, is reported beside every verdict.

**The attribution rule** applies only to blocks with a *Benefit* or *Harm*. R_b = Π_b / Δ_b, with a
cluster-bootstrap 95% interval.

- **Mostly volume and routing (T2):** the interval's lower bound is above 0.5.
- **Mostly content:** the interval's upper bound is below 0.5.
- **Unresolved:** otherwise.

No note is sent to review on this evidence alone. A content harm is a lead for Study 1-style tests of the
notes the transcripts show were applied.

**Multiplicity.** Family P is H-E alone at α = 0.05. Family N is an intersection-union claim, needing no
correction. Its two-sided labels use Holm across A and D. The secondary hypotheses form their own
families, with Holm within each. Haiku is a separate family.

**The smallest effect of interest, and why 10 pp.** Lakens (2022) asks for the justification in writing:

1. **Resources.** About 120 tasks per block is what one round can afford. Khatri (2026) reaches the same
   size for 10 pp at 80% power. Effects under 10 pp can still reach significance, and they are reported,
   but they carry no verdict of practical size.
2. **Literature.** Context-file studies bound the effect to within about 10 pp (Khatri 2026, with TOST)
   or found no significant change (Gloaguen et al. 2026). Curated skills were reported at +16.6 pp
   (SkillsBench). Effects of the size claimed for such material are at or above 10 pp.
3. **Practical.** Carrying the bundle has an overhead in cost (ρ > 1 in every prior measurement) and in
   maintenance (releases, alignment across carriers). A change under 10 points would not move a
   decision to carry it or not, whatever the exact ratio, and a change of 10 points or more would.

## 6. Arms

| Arm | Root file (`AGENTS.md`, with `CLAUDE.md` = `@AGENTS.md`) | `.agents/` | Isolates |
|---|---|---|---|
| `minimal` | a two-line template filled from the benchmark's metadata: what the workspace is and the command that runs its tests | absent | the realistic baseline |
| `bundle` | `minimal` + the two wiring lines (§2), verbatim | the bundle at the frozen version tag, scrubbed (below) | the treatment |
| `placebo` | identical to `bundle`, byte for byte | the same tree, with `knowledge/` replaced (below) | the content of the knowledge base, with volume, wiring, method and index lookup held |

**Dropped from Study 1, with reasons.** `none`: four pilots found `minimal` equal to `none` in success,
and in cost (×0.99). `ablated`, `oracle` and `oracle_placebo`: they need a target note, and these tasks
have none by design.

**The scrub, identical in `bundle` and `placebo`.** Every line naming the efficacy experiment (Study 1 or
Study 2, their roadmap items, `evals/`) is removed from `CHANGELOG.md` and `tracking/`, the files that
still ship from 0.0.22 (the roadmap and the method changelog no longer do). The number of lines removed is
recorded. This keeps the agent from learning it is under evaluation. The frozen version tag is cut before
any Study 2 record exists.

**How the placebo is built** (by a frozen, published procedure, not by choice):

- **What is replaced.** Everything under `knowledge/`: the index, the area indexes and the notes.
  Everything else (`method/`, `tools/`, `README.md`, `CHANGELOG.md`, `tracking/`) stays identical to
  `bundle`, so `bundle` − `placebo` isolates the knowledge base's content and nothing else. Whether
  `SHA256SUMS` is regenerated over the placebo tree is fixed at G0.
- **The notes.** Off-task software-engineering notes, in the bundle's note template (claim, when it
  applies, when it does NOT apply, how to verify), each matched to a real note's length within ±3% in
  tokens. The index keeps its tables, phases and "about to do" rows, filled with the placebo notes. The
  two wiring lines therefore describe the placebo as accurately as they describe the bundle.
- **Topics.** Chosen by rule: software areas that none of the five blocks touches (for example GPU
  shader pipelines, mobile layout and accessibility, embedded interrupt timing, spreadsheet formula
  engines, print typesetting). A topic is admitted only if none of its key terms appears in any framed
  task's text, which is checked by script at G0.
- **No generic advice.** A note may not carry advice that transfers to any task: nothing on testing,
  verification, error handling or reading code carefully. The check at G0 is a blind reviewer given the
  placebo notes and a sample of 30 framed tasks, who must find no note applicable to any task.
- **Generation.** The notes are written by a fixed model with a fixed prompt and seed. The prompt, the
  topic list and the output are committed with the plan.

**What the placebo still cannot hold equal:** how much the agent reads. The notes are plausible and in
format, so reading should be comparable, but reading volume is recorded per trial and reported beside Π
and Δ'.

**Routed controls, pilot only (§9.1):**

- `bundle+plant` is `bundle` with one extra note, listed in the index, holding a correct hint for the
  task.
- `bundle+decoy` is the same, with a misleading hint.

These test the delivery path itself: routing line, index, note.

## 7. The blocks

**Common rules:**

- **Selection by a seeded script from a frame fixed at G2.** No task is picked by hand, and no task is
  filtered on any agent's outcome: filtering on the baseline would bias the estimand (regression to the
  mean) and adds a researcher choice. Difficulty is set only through the benchmark's metadata, and the
  one adjustment rule allowed (A's tier mix) is written below.
- **The pilot and the controls use tasks disjoint from the confirmatory set.** Where the post-cutoff
  pool is too small to spare any (E), they use pre-cutoff tasks from the same source. Contamination does
  not matter for an instrument check.
- **The environment is validated before sampling.** A task whose reference solution does not pass here,
  or whose tests are flaky (the gold solution run 3 times does not pass all 3), is removed and listed.
  This is an instrument check, not an outcome filter.
- **Allowed paths.** No network during a trial, except the model API. Reads and writes are allowed in
  the workspace, the language runtime and its installed packages, and the system temporary directory.
  Anything else is denied and logged. HAL found agents looking up answers when this was open (Kapoor et
  al. 2025).
- **Budgets.** Identical across arms and generous, so consulting the bundle is not punished by an
  artificial cap. Running out of budget counts as a failure and is tabulated per arm (H-exh).
- **The `minimal` root file** comes from one template per block, filled from the benchmark's metadata.
  It is never written by hand.

### E — Real issues (primary)

- **Source.** SWE-rebench (Badertdinov et al. 2025), dataset `nebius/SWE-rebench-leaderboard` (CC-BY-4.0).
  Python tasks mined continuously, validated by execution, with a prebuilt image per task.
- **Frame.** Every task in the monthly splits dated 2026-02 onward that are published at G2. At G0 that
  was 167 tasks across 112 repositories (splits `2026_02` and `2026_03`). `created_at` is the date the
  fix was opened, which is what matters for contamination: a fix opened after both cutoffs cannot have
  been memorised. After validation, every eligible task is used, and each repository is a cluster.
- **Excluded source.** SWE-bench-Live, whose Python set ends in September 2025 (checked at G0), and
  SWE-bench Verified, whose tests, statements and contamination are documented problems (Aleithan et al.
  2024; Wang et al. 2025; Liang et al. 2025).
- **Pilot and controls.** 40 tasks from SWE-rebench's pre-cutoff pool, drawn by the same script.
- **Environment.**
  - The task's image. Its git history is checked per trial (`git log --all` and `git tag` show only the
    base commit), because the two images inspected at G0 were sanitised but locally rebuilt images may
    not be.
  - Pre-existing agent files are removed in every arm, and the removal is recorded: `AGENTS.md`,
    `CLAUDE.md`, `.claude/`, `.agents/`, `.cursor*`, `.github/copilot*`.
  - The arm's files are committed as a setup commit. The hidden tests are absent.
- **Grading.**
  - The agent's patch is extracted against the setup commit, excluding the arm's files.
  - The patch is applied to a fresh copy of the image, test files are restored to the task's versions,
    and FAIL_TO_PASS and PASS_TO_PASS are run.
  - Test files are defined by path pattern: `tests/`, `test_*.py`, `*_test.py`, `conftest.py`, and the
    task's listed test files.
  - Because grading happens on a fresh image, the injected `.agents/` cannot break PASS_TO_PASS, and
    neither can linters or doctest collection over the tree.
  - A differential re-check of passing patches is exploratory. Weak tests pass wrong patches (Wang et
    al. 2025), and the bundle may change the shape of patches.
- **Calibration.** Sonnet 5 scores about 57% on a recent SWE-rebench window, inside the useful band.
- **Budget.** 100 turns, 45 minutes.

### A — Competitive programming (no harm)

- **Source.** LiveCodeBench Pro (Zheng et al. 2025): Codeforces problems with difficulty, time and
  memory limits. The problems are gated (the terms must be accepted). The test-case dataset holds, per
  problem, a checker and full input and answer files. The local judge (LightCPVerifier, AGPL-3.0) runs
  in Docker.
- **Frame.** Problems in the 2024 Q4 to 2025 Q2 splits whose test data are published (contest ids up to
  about 2121, mid-2025). Tiers: easy (≤ 2000) and medium (2000–3000), in equal numbers, stratified by
  split.
- **Tier rule, fixed now.** If the pilot's `minimal` pass rate is above 75%, the confirmatory frame is
  medium only. If it is below 25%, easy only. Otherwise the mix stays. Nothing else about A may change
  after the pilot.
- **Contamination.** Every framed problem predates both models' training cutoffs. Memorised problems sit
  at the ceiling, where no effect can register, so **contamination biases Δ_A toward zero, which favours
  *Non-inferior***. It is reported as such, with A's ceiling mass beside its verdict. A non-inferiority
  claim on a contaminated block is weaker than on a clean one, and the report says so.
- **Workspace.** `problem.md`, the sample tests, a compiler and an interpreter. The agent writes
  `solution.cpp` or `solution.py`.
- **Grading.** Accepted on every test, by the checker, within the limits. Grading is serial, on an
  otherwise idle machine, so a time-limit verdict is never noise from concurrent load.
- **Controls.** The hint is the key idea from the official editorial, cached before the pilot. Only
  problems with a cached editorial are eligible for the control sample.
- **Budget.** 60 turns, 30 minutes.

### D — Code reasoning (no harm)

- **Source.** SWE-Flux (Taherkhani et al. 2026; repository under MIT): 480 questions over 12 Python
  repositories, in categories such as control flow, loops, program state, data flow, exceptions and
  invariants. Answers are JSON objects matching a per-item template, scored by exact match against
  oracles from instrumented runs. It ships a perturbation module.
- **Frame.** Items for which the perturbation module produces a variant. The variant is scored, not the
  original, which counters memorisation. 120 items are stratified by repository and category. The 12
  repositories are fixed, so the estimand is over their items, and no cluster correction is made across
  repositories.
- **Checks at G0.** The paper appeared on 2026-09-23 and is not peer-reviewed, so the oracle is
  re-derived on every *sampled perturbed variant*, by running the instrumentation. An item whose oracle
  does not reproduce is removed.
- **Tools.** `Read`, `Glob`, `Grep` and `Write`, and no `Bash`, in every arm. The benchmark's own
  evaluation is read-only. With execution, output prediction becomes running the code.
- **Answers.** Validated against the template's schema and normalised (key order, whitespace, number
  formatting) before the exact match. Format failures are counted per arm, since a longer context might
  cause them.
- **Budget.** 30 turns, 15 minutes. **5 reps**, because trials are cheap.
- **Contamination.** The snapshots date from late 2024 to mid 2025, before Sonnet 5's cutoff. The
  perturbed variants limit memorisation; the bias toward zero, if any, is reported as in A.

### B — Algorithm design with a score (secondary)

- **Source.** ALE-Bench (Imajuku et al. 2025): 40 AtCoder Heuristic Contest problems (AHC001 to AHC046),
  with offline scoring and performance computed from the stored rank-to-performance map. Code is under
  Apache-2.0 and data under CC BY-ND 4.0: run locally, statements never republished.
- **The 2026 contests are excluded.** Their system-test inputs are not public, so performance cannot be
  reproduced (checked at G0).
- **Frame.** 36 problems. The other 4 are the pilot.
- **Metric.** The problem's performance. A trial with no valid submission, or that runs out of budget,
  scores the floor (0).
- **Estimator.** The paired Hodges–Lehmann shift, robust to those floors.
- **Status.** Secondary, fixed now. It is not decided at G1 from an 8-problem estimate of spread.
- **Budget.** 100 turns, 60 minutes.

### C — Architecture measured by consequence (exploratory pilot)

Taste is not graded. Design is judged by what it costs someone else to change it later, the logic of the
two-phase trial in Borg et al. (2025), with an agent in the second phase.

- **Source.** SlopCodeBench (Orlanski et al. 2026; runner and problems under MIT): 36 problems and 196
  checkpoints, specifications of external behaviour only, and tests that re-run earlier checkpoints.
  The tests are public in the benchmark's repository. 20 problems were public before Sonnet 5's cutoff,
  so the pilot uses the problems published after it.
- **Stage 1 (the treatment).** The arm's agent implements checkpoints 1 and 2.
- **Stage 2 (the measurement).** `AGENTS.md`, `CLAUDE.md` and `.agents/` are removed from the Stage 1
  output. One frozen agent (Sonnet 5, `minimal`, fixed settings, never told the arm) then implements the
  remaining checkpoints.
- **Outcome.** The pass rate over the Stage 2 checkpoints, regressions included.
- **Secondary outcomes.** Stage 2 cost, and the benchmark's deterministic erosion and verbosity
  metrics.
- **Controlling for Stage 1 correctness.** The Stage 1 pass rate is a covariate, and a sensitivity
  analysis keeps only Stage 1 codebases that passed.
- **Size.** 12 problems × 3 arms × 2 reps, to learn whether the instrument has signal. Block C gets its
  own pre-registration if it does. The published cost is of the order of ten dollars per problem at
  the top model's prices.

## 8. The agent and its isolation

Inherited from Study 1 (`PROTOCOL.md`, *The agent*), with these changes:

- **Configuration.** A dedicated configuration directory holding credentials only. The pilot's reuse of
  the logged-in configuration (Study 1's deviation) is not repeated.
- **Model and CLI.** The model id, effort level and Claude Code version are fixed in the plan, installed
  from a pinned package, and checked on every trial's init event.
- **Blocks A, B, C and D** run in Claude Code's sandbox, as in Study 1, with no network.
- **Block E** runs Claude Code inside the task's container, adapted from the official reference
  container (`.devcontainer/init-firewall.sh` in Claude Code's repository):
  - Egress is denied by default. The allowlist holds only the model API, plus the two sign-in hosts if a
    subscription token is used.
  - The reference's GitHub ranges, ssh and host-network rules are removed, and DNS is restricted to the
    resolver.
  - `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` and the auto-updater is off.
  - Web tools are disabled explicitly in every block, since a server-side tool would pass an allowlist
    that admits the API.
- **Tools.** `Bash`, `Read`, `Edit`, `Write`, `Glob` and `Grep` (D excepted, §7.D). No subagents, MCP
  servers, skills or web tools.
- **Order.** Randomised and interleaved: within each repetition, every task-arm pair appears once in
  shuffled order, so drift over the weeks of a run hits every arm equally.
- **Errors.** Rate-limit, overload and API errors are infrastructure failures whatever the number of
  tool calls already made, so a limit that hits the longer arm more often is not scored as a harm.

## 9. The controls that make the test severe

A test is severe only if it would probably have failed were the claim false (Mayo 2018). For "no effect"
and "no harm" claims, that means showing the instrument sees an effect when one exists, through the same
path the treatment uses.

### 9.1 Routed controls: content reached through the index can move the outcome

- **Arms.** In the pilot, on 40 tasks of A and 40 of E, each with 3 reps:
  - `bundle+plant` against `bundle`. The planted note is a correct hint: the editorial's key idea in A,
    the files the gold patch changes in E.
  - `bundle+decoy` against `bundle`. The planted note is a misleading hint written as confidently: the
    key idea of another problem in the same tier in A; in E, files from the same repository that are
    disjoint from the gold patch's files.
- **Delivery.** The note is reachable only through `INDEX.md`, like every real note, so the controls
  test delivery as well as grading.
- **Predictions.** At least +20 pp for the plant and at least −15 pp for the decoy.
- **Pass rule.** A one-sided test at α = 0.05 in the predicted direction. At 40 × 3, the probability of
  passing is 0.96 for a realised +20 pp and above 0.8 for −15 pp.
- **If any of the four fails:** G1 fails, the study stops, and the delivery path or the instrument is
  fixed before any confirmatory trial. Nothing is downgraded or reinterpreted. This one consequence is
  the same in §9.1, §10 and §14.
- **What the controls do not show.** A decoy the agent dismisses shows scepticism, not insensitivity.
  That is why the decoy's hint must be as specific and confident as the plant's, and why a failed decoy
  still stops the study: without it, harm detection is unproven.

### 9.2 A/A: the instrument stays quiet when there is nothing to find

- **In the pilot.** `minimal` against `minimal-b`, identical but under another label, on the pilot's A
  and E tasks. Expected: not significant.
- **On simulated data, at G0,** the frozen analysis script must show four things:
  - Size: it rejects in 3% to 7% of 1,000 null datasets shaped like the design.
  - Equivalence error: P(*Equivalent* | Δ = ±10 pp realised) ≤ 0.06.
  - Non-inferiority error: P(*Non-inferior* | Δ = −10 pp realised) ≤ 0.06.
  - Recovery: it recovers a planted 10 pp effect with its intended power, under the real cluster
    structure (Kohavi, Tang & Xu 2020).

### 9.3 Manipulation check: the treatment was delivered

- **Recorded per trial,** for `bundle`, `placebo` and the controls: whether `INDEX.md` was opened, which
  notes were read, whether `method/` was read, and an estimate of the tokens read from `.agents/`.
- **Used for** the PP analysis (§5), the mediation analysis, and the uptake line beside every verdict.
- **The probe.** `harness.py probe` confirms, before the pilot and before the confirmatory run, that
  each arm loads exactly its instructions.

### 9.4 Allocation and integrity checks (sample ratio mismatch)

Checked after the run and before unblinding. A block that fails is void, not reinterpreted.

- **Missing trials.** Completed trials per arm are within 2% of the plan, and missingness does not
  differ between arms (Fisher's exact test, p > 0.01; Fabijan et al. 2019).
- **Infrastructure failures.** Under 3% per arm, and not different between arms by the same test.
  Rates are compared by test, not as a ratio, which trips on noise at low counts.
- **Constancy.** The CLI version and model id are the same in every init event.
- **No escape.** No network access and no path outside those allowed (§7), by a deterministic scan of
  every transcript. E additionally checks git history per trial.
- **An interrupted run.** If a model or CLI change voids a run partway, complete repetitions before the
  change may be analysed as a planned reduced design (fewer repetitions). That rule is fixed now. The
  incomplete repetition is discarded.

### 9.5 Blinding

- **Grading** is automatic in every block, so it is blind by construction.
- **Arm labels** in the run records are opaque codes. The key is written at plan time into a file the
  analysis does not read.
- **The limit of blinding.** The G3 manipulation tables reveal which code is `minimal`, since it never
  reads `.agents/`. That is acceptable only because the analysis script is frozen at G2 and cannot be
  steered by what anyone sees.
- **The pilot is blinded too.** G1's report contains only the controls, the A/A contrast, uptake, cost,
  infrastructure rates and the *spread* (not the mean) of the `bundle` − `minimal` differences. The
  treatment means are computed but withheld until G4.

## 10. Procedure and gates

A gate that fails stops the study at that point. The failure is recorded, and the study resumes only when
the cause is fixed. Nothing is reinterpreted.

| Gate | Stage | Conditions for approval |
|---|---|---|
| **G0 Instrument** | adapters, graders, containers, placebo, analysis code | (1) Every grader is seen to pass and to fail: the reference passes, an empty or trivial submission fails, and flaky tasks are removed (§7). (2) The placebo matches file lengths within ±3%, its topics pass the term check, and the blind reviewer finds no applicable note (§6). (3) The scrub is applied and counted, and the frozen version tag predates any Study 2 record. (4) The probe shows each arm loading exactly its instructions. (5) Isolation is verified by a probe trial per block, including E's egress rules. (6) The analysis script passes the simulation checks of §9.2. (7) Licences and terms are checked: the benchmarks, the judge, the AHC data (not republished), and the subscription's terms for automated use. (8) SWE-Flux oracles reproduce on the sampled variants. (9) `harness.py check` and the tools' tests pass |
| **G1 Pilot** | disjoint tasks: A 40 and E 40 with arms `minimal`, `minimal-b`, `bundle`, `placebo`, `bundle+plant`, `bundle+decoy` × 3 reps; D 30 and B 4 with `minimal`, `bundle`, `placebo` × 2 reps; the C pilot | (1) All four routed controls pass (§9.1). (2) A/A is quiet (§9.2). (3) A's tier rule is applied (§7.A). (4) Infrastructure failures are under 3%. (5) Cost per trial is measured, and the tier follows mechanically from the budget cap the user set before the pilot (§17). (6) The blinded G1 report (§9.5) is written. No size, family or rule changes on the strength of the pilot, except (3) and (5) |
| **G2 Freeze** (pre-registration) | before the first confirmatory trial | (1) This protocol is final. (2) The task lists (ids and hashes), seeds, placebo, scrub and templates are committed. (3) The analysis code is committed and has passed §9.2. (4) The forecasts (§13) are filled in and committed. (5) One commit holds all of it and is tagged, and **the tag is pushed to the repository's remote before the first confirmatory trial**, so it serves as a timestamp. The user performs the push. (6) The budget is explicitly approved by the user |
| **G3 Run validity** | after the run, before unblinding | every check in §9.4 passes. The manipulation tables are written |
| **G4 Analysis** | after G3 | the frozen script runs on coded data, the verdict tables are written, then the key is opened. Every deviation is listed. Anything computed beyond the script is labelled exploratory (Wagenmakers et al. 2012) |

No interim look at a confirmatory contrast. The run stops early only for an infrastructure problem, or
when the approved budget runs out. It then ends at the last complete repetition, which is analysed as a
reduced design (§9.4).

## 11. Sample size and severity

The sample size rests on the smallest effect of interest (§5), with a sensitivity analysis (Lakens 2022).
The figures below come from `python3 evals/power_tost.py`. The outcome is binary; the baseline is
U-shaped, Beta(0.6, 0.6); effects are realised means; the margin is ±10 pp; each row is 1,500
simulations. They ignore clustering, which the analysis script's simulation mode adds at G0.

**E, two-sided at α = 0.05, 120 tasks × 3 reps** (E will have about 150 or more, which only helps):

| Per-task effect SD | Realised Δ | P(significant) | P(*Harm*) | P(*Equivalent* declared) |
|---:|---:|---:|---:|---:|
| 10 pp | 0 | 0.04 | 0.02 | 0.93 |
| 10 pp | −10 pp | 0.93 | 0.93 | 0.06 |
| 20 pp | 0 | 0.05 | 0.02 | 0.85 |
| 20 pp | −10 pp | 0.89 | 0.89 | 0.04 |
| 30 pp | 0 | 0.06 | 0.03 | 0.77 |
| 30 pp | −10 pp | 0.82 | 0.82 | 0.05 |

**A, 120 × 3, and D, 120 × 5.** Non-inferiority is one-sided at 0.05. The harm label is two-sided at
the Holm level (0.025 for the first test).

| Block | Per-task effect SD | P(*Non-inferior* \| 0) | P(*Non-inferior* \| −10 pp) | P(*Harm* label \| −10 pp) |
|---|---:|---:|---:|---:|
| A | 10 / 20 / 30 pp | 0.97 / 0.93 / 0.89 | 0.06 / 0.04 / 0.05 | 0.88 / 0.82 / 0.74 |
| D | 10 / 20 pp | 1.00 / 0.98 | 0.05 / 0.06 | 0.98 / 0.94 |

**Controls, 40 × 3, one-sided at 0.05** (per-task effect SD 15 pp): P(pass) = 0.96 at a realised
±20 pp and about 0.8 at ±15 pp.

How to read this:

- **The error rates of the claims stay near the nominal 0.05.** P(*Equivalent* | ±10 pp) and
  P(*Non-inferior* | −10 pp) are 0.04 to 0.06.
- **Their severity is 0.74 to 0.98,** depending on how much the effect varies between tasks. The
  literature suggests 20 to 30 pp of variation for material of this kind (SkillsBench: 13 of 87 tasks
  worse, the rest better). The lower figures are therefore the planning figures.
- **For a fixed number of trials, adding tasks and adding repetitions give similar power.** Tasks are
  preferred, because the estimand is over tasks and three repetitions give pass^3. D takes 5 repetitions
  only because its trials are cheap.
- **A margin of 5 pp would need well over 200 tasks per block.** That is not affordable in one round.

## 12. Analysis plan

1. **Unit.** The task. Repetitions are averaged per task and arm. Every contrast is the mean over tasks
   of the paired per-task difference (Miller 2024).
2. **Inference, one method for tests and intervals.**
   - A cluster-robust paired t with a small-sample correction (CR2), G − 1 degrees of freedom, and
     intervals obtained by inverting the test.
   - Clusters: the repository in E (about 110 clusters) and the contest in A. In D the repositories are
     fixed strata, so the unit is the item, and in B the problem.
   - A block with fewer than 30 clusters uses a wild cluster bootstrap (Webb weights) for both the test
     and the interval, and says so.
3. **Verdicts** by §5, ITT and PP, with Holm where §5 names it.
4. **Secondary.**
   - H-cost: the geometric mean ratio of per-task mean cost, total tokens including cache reads and
     writes, output tokens, tool calls (comparable across agents: Khatri 2026), turns and wall time.
   - H-B: the Hodges–Lehmann shift with its interval.
   - H-attr: R with a cluster-bootstrap interval.
   - H-exh: the difference in exhaustion rates.
5. **Sensitivity** (beside the primary, never replacing it).
   - The cluster sign-flip randomisation test.
   - A mixed-effects logistic model with random intercepts for task within cluster.
   - Budget exhaustion excluded rather than counted as failure.
   - Infrastructure exclusions put back in (Simmons et al. 2011).
   - For E: without tasks whose issue text contains a code block matching the gold patch's added lines
     (an automatic rule).
6. **Exploratory.** Listed in §4, and labelled.
7. **Missing data.** ITT. An infrastructure failure is re-run once. One that persists is excluded and
   listed. Every other outcome, including timeouts and errors, counts as a failure.

## 13. Expected results: the forecast register

Forecasts are recorded before G2, as probabilities, and scored after unblinding with the Brier score
(Brier 1950). The point is not to be right. A null that matches the forecasts means something different
from one that contradicts them (DellaVigna, Pope & Vivalt 2019). METR collected forecasts the same way
before its trial (Becker et al. 2025).

The drafting session's forecasts were made before any Study 2 data and revised after the G0 checks. The
blank columns are for the user and for independent forecasters (another model family is welcome), each
filled in without seeing the others.

| Outcome | Drafting session | User | Independent 1 | Independent 2 |
|---|---:|---:|---:|---:|
| E: *Benefit* / *Harm* / *Equivalent* / *Inconclusive* | 0.10 / 0.10 / 0.55 / 0.25 | | | |
| A: *Non-inferior* (ITT and PP) | 0.80 | | | |
| A: *Harm* label | 0.10 | | | |
| D: *Non-inferior* (ITT and PP) | 0.85 | | | |
| D: *Harm* label | 0.07 | | | |
| B: *Non-inferior* | 0.65 | | | |
| ρ_E within [1.1, 2.0] | 0.65 | | | |
| ρ_A within [1.0, 2.5] | 0.75 | | | |
| all four routed controls pass at the first pilot | 0.55 | | | |
| uptake in E ≥ 80% of `bundle` trials open the index | 0.85 | | | |

The reasons behind these forecasts:

- **A and D:** the knowledge base excludes algorithms and patterns the agent already knows (its own
  `INDEX.md`, *What is deliberately not here*). Harm through reading is the only likely effect, and
  generous budgets make it small.
- **E:** real issues sometimes touch failure handling, retries or partial updates, where a note applies,
  so benefit and harm are about equally likely. Mixed effects make *Inconclusive* likelier than in A.
- **ρ_E:** the fixed reading overhead is a smaller share of a long repository task than of Study 1's
  small ones.
- **Controls:** the decoy is the likeliest to fail, because a capable agent may check a misleading hint
  against the code and reject it.

## 14. Decision map: what each result means for the bundle

Fixed now. The consequences go through the bundle's own channels (`meta/roadmap.md`, `meta/tracking/`), never by
editing the body as a side effect. Read in order: controls, then E, then unrelated work, then cost.

**Step 0.** If any routed control failed at G1, there is no confirmatory run and no verdict. The
instrument or the delivery path is fixed first.

**Step 1 × Step 2.** E's verdict against unrelated work (A and D; "no harm" means both are
*Non-inferior*):

| E \ unrelated work | No harm (A and D non-inferior) | *Harm* label in A or D | Neither (inconclusive) |
|---|---|---|---|
| ***Benefit*** | carrying it helps ordinary work at no measured cost elsewhere: the strongest case for carrying it. Next, a method-only arm to separate the method from the notes | helps real work, hurts unrelated work: route by relevance (skills chosen by description, path-scoped rules), not always | helps real work; harm elsewhere not excluded: carry it, and re-test unrelated work with more tasks |
| ***Equivalent*** | carrying it neither helps nor hurts, and costs more. Options, in order: carry it only where a note applies (T3's case, which only Study 1 can test), or **stop carrying it by default**. The choice goes to the roadmap with the cost figures | no value on real work, and harm elsewhere: **stop routing to it by default**; keep it available on demand | no value on real work, harm not excluded: as the cell to the left, with a note that harm was not excluded |
| ***Harm*** | carrying it hurts ordinary work. Apply the attribution rule (§5): volume → shrink what is consulted (index, cards before notes) and re-test; content → Study 1-style tests of the notes the transcripts show were applied; unresolved → both | hurts everywhere: stop routing to it by default until a re-test shows otherwise | as the cell to the left |
| ***Inconclusive*** | no decision about benefit; no harm on unrelated work. Report the bounds; a later round decides whether a larger E is worth it | no decision about benefit; harm on unrelated work: route by relevance, not always | nothing decided; report the bounds, make no claim |

**Step 3, cost, applied to every cell:**

- **ρ_E above 2.0:** cost weighs against any cell short of *Benefit*.
- **ρ_E below 1.1:** the overhead is negligible, and "stop carrying it" in the *Equivalent* row softens
  to "no reason to carry or to remove".

**Findings that do not change a cell on their own:**

- Every secondary verdict (B, Haiku, attribution in a *Benefit* block).
- The E subgroup.
- A *Benefit* label in A or D. It is unexpected, since the notes contain nothing algorithmic. Its
  mechanism is examined first (more testing, longer runs), and it is recorded as a hypothesis for
  replication.

## 15. Threats to validity

Organised by the four types in Shadish, Cook & Campbell (2002), as used in software engineering (Wohlin
et al. 2012). Each threat is tied to the result it would affect.

| Type | Threat | Mitigation | What remains, and which result it affects |
|---|---|---|---|
| Statistical conclusion | too few tasks for a 10 pp margin; effects that vary widely across tasks | 120 × 3 or more, severity simulated at SDs up to 30 pp, TOST and NI, a cluster-robust t | effects under 10 pp are not decided (all verdicts) |
| Statistical conclusion | forking paths from the pilot | pilot blinded; sizes, families, subgroup rule, tier rule and B's status fixed now | only the two mechanical G1 rules remain |
| Internal | drift of the model or CLI over weeks | pinned and checked per trial; interleaved order; the rule for an interrupted run | a silent server-side model change would hit every arm equally |
| Internal | rate limits that hit the costlier arm more | counted as infrastructure whatever the tool calls; integrity checks per arm | a block that fails is void |
| Internal | the injected files break the repository's own tests (E) | grading on a fresh image, arm files excluded from the patch | none known |
| Internal | the agent games the grader | tests absent, test files restored, fresh-image grading, transcript scan, git-history check | gaming by a route nobody anticipated |
| Internal | the agent learns it is being evaluated | the scrub (§6), identical in both bundle arms | the agent may still infer it from the task shape, in every arm |
| Construct (cause) | the treatment is not a full bootstrap | the bootstrap's own two wiring lines, verbatim; conclusions scoped to them | a fully bootstrapped carrier might route better or worse |
| Construct (cause) | `placebo` does not hold reading volume equal | in-format off-task notes; reading volume recorded; mediation analysis | the attribution rule separates content from volume only as far as reading is comparable |
| Construct (effect) | tests measure behaviour, not design quality | no judge by design (Zheng et al. 2023; Panickssery et al. 2024); design only through consequences (C) | design quality is not measured confirmatorily this round |
| Construct (effect) | weak tests pass wrong patches (E) | pass-to-pass tests too; differential re-check, exploratory | inflates both arms, and biases Δ only if the bundle changes the shape of patches |
| External | contamination in A, B and D | E entirely after both cutoffs; perturbed D items; bias stated as toward zero; ceiling mass reported | A and D non-inferiority is weaker evidence than it would be on fresh problems |
| External | one agent, one vendor, two models; Python-only E | recorded | the result holds for Claude Code with these models (§18) |
| Conflict of interest | the maintainers evaluate their own bundle | external task sources, selection by script, automatic grading, blinded pilot and analysis, pre-registration with a pushed timestamp, published forecasts | the choice of benchmarks is ours; it is argued here before any data |

## 16. What must be built before G0

This is engineering; it does not change the design.

1. **Task adapters** per source, which materialise a workspace (A, B, D) or a container (E) from the
   benchmark's record, with the `minimal` template filled from metadata.
2. **Graders.**
   - A: the LiveCodeBench Pro checker and judge, run serially.
   - B: the ALE-Bench scorer and performance map.
   - D: schema validation, normalisation and exact match.
   - E: fresh-image grading with test-file restoration.
   - C: the SlopCodeBench checkpoint tests.
3. **Container execution for E**: the adapted firewall, the removal of pre-existing agent files, the
   setup commit, patch extraction, and the git-history check.
4. **The placebo pipeline**: topic check, generation with a frozen prompt, length matching within ±3%,
   index construction, and the blind-reviewer packet.
5. **The scrub**, applied identically to both bundle arms, with its count recorded.
6. **Arms in `harness.py`**: the new wiring lines for `bundle` and `placebo`, `bundle+plant`,
   `bundle+decoy` and `minimal-b`; opaque arm codes; per-block tool lists (no `Bash` in D), budgets and
   allowed paths.
7. **Manipulation metrics**: index opened, notes read, method read, and tokens read from `.agents/`.
8. **`analyze.py` for Study 2**:
   - verdicts by §5, in ITT and PP;
   - the cluster-robust t (CR2) and the wild cluster bootstrap;
   - Holm and non-inferiority;
   - Hodges–Lehmann for B;
   - the attribution ratio;
   - the integrity checks of §9.4;
   - the blinded G1 report;
   - a simulation mode that passes §9.2.
9. **The frame scripts**: frame, seeds, stratification and disjoint pilot samples, written to lists
   committed at G2.
10. **An editorial cache for A's controls**, fetched before the pilot and stored offline.

## 17. Cost and scale

Study 1's trials cost cents each at API prices. Here, E is a real repository with a 45-minute budget and
B runs up to an hour. The pilot measures cost per trial per block and arm.

**The tier rule, mechanical.** Before the pilot, the user sets a budget cap. After the pilot, the tier is
the largest one whose projected cost, the measured cost per trial × the planned trials × 1.2, fits under
the cap. No other consideration enters.

| Tier | Contents | Confirmatory trials |
|---|---|---:|
| 1 | E (≈ 160 × 3 arms × 3) + A (120 × 3 × 3) | ≈ 2,500 |
| 2 | tier 1 + D (120 × 3 × 5) + B (36 × 3 × 3) | ≈ 4,650 |
| 3 | tier 2 + H-haiku on E and A | ≈ 7,200 |

The pilot adds roughly 1,800 trials, dominated by the A and E controls, and runs in every tier. Block C's
pilot is part of G1, not a tier. Throughput on a subscription is limited, so a run takes weeks;
interleaving (§8) keeps that from biasing any arm. **Data sharing:** per-trial outcomes (task id, arm
code, success, cost, uptake) may be published after G4. Transcripts never are, because they carry the
logged-in account's identity.

## 18. What this study cannot conclude, and what would extend it

- **It cannot say the notes are wrong or useless.** A null on general work is compatible with a real,
  narrow benefit (T3). Study 1 is where that is tested, and it needs its own repairs (`REPORT.md`, §5).
- **It cannot generalise beyond Claude Code with these two models.** The natural extension is another
  agent that reads `AGENTS.md` (the bundle claims to be agent-neutral), with a model from another vendor.
- **It cannot separate the method from the knowledge, nor test a full bootstrap.** A `method-only` arm
  is the follow-up if E shows a benefit.
- **A and D test harm on contaminated problems,** which biases toward non-inferiority. Fresh competitive
  programming with public tests would remove that bias, when a source publishes them.
- **A single hard problem is not evidence.** Block D replaces the original idea of "one hard
  code-reasoning problem" with 120 items, because one binary outcome can refute nothing. A worked hard
  case can illustrate the report; it carries no weight.

## 19. References

Methodology:

- Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review* 78(1):1–3.
- DellaVigna, S., Pope, D., Vivalt, E. (2019). Predict science to improve science. *Science* 366(6464):428–429.
- Fabijan, A. et al. (2019). Diagnosing sample ratio mismatch in online controlled experiments. *KDD '19*, 2156–2164.
- Gelman, A., Loken, E. (2013). The garden of forking paths. Manuscript; *American Scientist* 102(6), 2014.
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics* 6(2):65–70.
- Kohavi, R., Tang, D., Xu, Y. (2020). *Trustworthy Online Controlled Experiments*. Cambridge University Press.
- Lakens, D. (2017). Equivalence tests: a practical primer. *Social Psychological and Personality Science* 8(4):355–362.
- Lakens, D., Scheel, A. M., Isager, P. M. (2018). Equivalence testing for psychological research: a tutorial. *AMPPS* 1(2):259–269.
- Lakens, D. (2022). Sample size justification. *Collabra: Psychology* 8(1):33267.
- Mayo, D. G. (2018). *Statistical Inference as Severe Testing*. Cambridge University Press.
- Meehl, P. E. (1967). Theory-testing in psychology and physics. *Philosophy of Science* 34(2):103–115; (1990) *Psychological Inquiry* 1(2):108–141.
- Nosek, B. A. et al. (2018). The preregistration revolution. *PNAS* 115(11):2600–2606.
- Piaggio, G. et al. (2012). Reporting of noninferiority and equivalence randomized trials (CONSORT extension). *JAMA* 308(24):2594–2604.
- Popper, K. (1959). *The Logic of Scientific Discovery*.
- Ralph, P. et al. (2021). ACM SIGSOFT Empirical Standards for Software Engineering Research, arXiv 2010.03525 (experiments; registered reports).
- Shadish, W. R., Cook, T. D., Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*.
- Simmons, J. P., Nelson, L. D., Simonsohn, U. (2011). False-positive psychology. *Psychological Science* 22(11):1359–1366.
- Wagenmakers, E.-J. et al. (2012). An agenda for purely confirmatory research. *Perspectives on Psychological Science* 7(6):632–638.
- Wohlin, C. et al. (2012). *Experimentation in Software Engineering*. Springer.

Evaluation of models and agents:

- Becker et al. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. arXiv 2507.09089.
- Bjarnason, Silva, Monperrus (2026). On randomness in agentic evals. arXiv 2602.07150.
- Heineman et al. (2025). Signal and noise. arXiv 2508.13144.
- Kapoor et al. (2024). AI agents that matter. arXiv 2407.01502; (2025) Holistic Agent Leaderboard, arXiv 2510.11977.
- Madaan et al. (2024). Quantifying variance in evaluation benchmarks. arXiv 2406.10229.
- Miller, E. (2024). Adding error bars to evals. arXiv 2411.00640.
- Panickssery, Bowman, Feng (2024). LLM evaluators recognize and favor their own generations. arXiv 2404.13076.
- Yao et al. (2024). τ-bench. arXiv 2406.12045.
- Zheng et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. arXiv 2306.05685.
- Zhu et al. (2025). Establishing best practices for building rigorous agentic benchmarks. arXiv 2507.02825.

Context, instruction files and skills:

- Du et al. (2025). Context length alone hurts LLM performance despite perfect retrieval. arXiv 2510.05381.
- Gloaguen et al. (2026). Evaluating AGENTS.md. arXiv 2602.11988.
- Hong, Troynikov, Huber (2025). Context rot. Chroma research report.
- Huang (2026). Do LLM-generated skills make better AI data scientists? arXiv 2607.07504.
- Khatri (2026). Do context files help coding agents? arXiv 2607.27250.
- Li et al. (2026). SkillsBench. arXiv 2602.12670. The current version has 87 tasks; Study 1's report cites an earlier count of 84.
- Liu et al. (2024). Lost in the middle. *TACL*; arXiv 2307.03172.
- Lulla et al. (2026). On the impact of AGENTS.md files on the efficiency of AI coding agents. arXiv 2601.20404.
- Shi et al. (2023). Large language models can be easily distracted by irrelevant context. arXiv 2302.00093.

Task sources and environment:

- Aleithan et al. (2024). SWE-Bench+. arXiv 2410.06992.
- Badertdinov et al. (2025). SWE-rebench. arXiv 2505.20411; dataset `nebius/SWE-rebench-leaderboard`.
- Borg et al. (2025). Echoes of AI. arXiv 2507.00788.
- Imajuku et al. (2025). ALE-Bench. arXiv 2506.09050.
- Liang et al. (2025). The SWE-Bench illusion. arXiv 2506.12286.
- Orlanski et al. (2026). SlopCodeBench. arXiv 2603.24755.
- Taherkhani et al. (2026). SWE-Flux. arXiv 2609.28449.
- Wang (You) et al. (2025). Are "solved issues" in SWE-bench really solved correctly? arXiv 2503.15223.
- Zhang et al. (2025). SWE-bench goes live! arXiv 2505.23419 (checked at G0; excluded).
- Zheng et al. (2025). LiveCodeBench Pro. arXiv 2506.11928.
- Claude Code's reference development container and firewall script (`.devcontainer/` in its repository), and its network-configuration documentation.

The figures quoted from task sources (sizes, dates, calibration scores, licences) were read from their
pages and registries on 2026-09-24, in the availability checks of G0, and are re-read at G0 proper. The
model cutoffs (Sonnet 5: January 2026; Haiku 4.5: July 2025 for training data) are Anthropic's published
values.

## 20. Changes from draft 1

Draft 1 was reviewed adversarially by a separate session with no part in its design, and its data sources
were checked (the G0 availability checks). What changed, and why:

| Change | Reason |
|---|---|
| E is the sole primary; A and D test non-inferiority; B is secondary, fixed now | A, B and D are blocks the bundle says it has nothing to offer. Predicting *Equivalent* there was not a risky prediction, and a conjunctive "no effect" rested on blocks chosen to be irrelevant. E is also the only block after both cutoffs |
| The treatment uses the bootstrap's two wiring lines, verbatim, not Study 1's `ROUTING` | Study 1's paragraph is not what a carrier receives. Conclusions are now scoped to "the bundle plus its two wiring lines" |
| The placebo is off-task software-engineering notes in the bundle's format; only `knowledge/` is replaced; the attribution rule is numeric | A non-computing placebo would be dropped after one read and could not reproduce reading, so it could not detect T2. The old rows "placebo harms equally" had no operational rule |
| Routed controls (a planted note reachable only through the index) sized 40 × 3; one consequence for failure, stated everywhere | the draft-1 controls were underpowered (roughly 0.2–0.6 to pass), inserted hints directly, which bypasses the delivery path under test, and carried three contradictory failure consequences |
| The pilot is blinded; tier, sizes, B's status, the E subgroup rule and A's tier rule are fixed now | the draft-1 pilot exposed the treatment contrasts while choices that set the confirmatory design were still open |
| Severity is computed on realised effects, at the families' levels, over effect SDs of 10–30 pp | the draft-1 figures used nominal effects shrunk by clipping, ignored Holm, and assumed a narrow effect spread |
| A cluster-robust t for tests and intervals; D with fixed repositories; B by problem | a percentile bootstrap under-covers with few clusters and could disagree with a sign-flip test |
| *Equivalent* and *Non-inferior* must hold by ITT and per protocol | ITT alone makes equivalence easier when uptake is low (CONSORT, non-inferiority extension) |
| E is graded on a fresh image; pre-existing agent files are removed; test files are defined by pattern; flaky tasks are removed | the injected bundle could break the repository's own tests and show up as harm |
| H-cost predicts an interval; the smallest effect of interest no longer rests on ρ ≈ 2 | Study 1's ratio came from small tasks; the fixed reading overhead is a smaller share of repository-scale work |
| The decision map covers every combination and includes "stop carrying it by default" | draft 1 left the modal outcome and several combinations unmapped, and presumed T3 |
| E uses SWE-rebench only; A uses contests with published tests (mid-2025 and earlier); B drops the 2026 contests; D validates oracles on the perturbed variants; the RepoReasoner fallback is dropped | G0 checks: SWE-bench-Live's Python set ends in September 2025; LiveCodeBench Pro's test data end mid-2025 and carry no editorials; the 2026 contests' system-test inputs are not public; RepoReasoner has no licence |
| Contamination is stated as a bias toward zero, with the ceiling mass reported | memorised problems sit at the ceiling, where no effect can show |
| Rate-limit errors are infrastructure failures; rules for an interrupted run and for running out of budget; A graded serially | feasibility problems must not silently change the design or read as harm |
| The scrub of evaluation references; the `minimal` root file from a template; the tag pushed before the first trial; data-sharing and licence checks | evaluation awareness, a researcher choice, the timestamp's validity, and missing registered-report items |

## Deviations

None yet.
