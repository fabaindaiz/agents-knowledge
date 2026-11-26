# Plan: enough discriminating tasks to be able to find an effect

Written 2026-11-26 to be executed in the next session, at the owner's instruction: take the discriminating
set to ten, and decide there whether twenty is worth its run. **Nothing in this plan runs a trial**; the run
needs the owner's credentials and quota and is its own decision at the end.

## The question now

**The experiment cannot produce a significant result, whatever the effect is.** The contrast is an exact
sign-flip test over paired per-task differences, so with *k* tasks all moving one way the smallest
two-sided p-value is 2/2^k: 0.25 at three tasks, 0.031 at six, 0.002 at ten. The pre-registered analysis
plan refuses to test a contrast over fewer than eight tasks. The set has three.

And the three are weaker than the count suggests: **two of them are the same trap** at two distances, so
there are two independent traps, not three.

## Where we are

- **Inputs:** `evals/REPORT.md` (the pilots, the ceiling, the null primary contrast), `evals/PROTOCOL.md`
  (the registered plan), `meta/reviews/2026-11-26-weak-points-before-presenting.md` rows A2 to A5.
- **The task set today:** 29 task directories — 8 judgment traps, each with an L1 and an L2 distance
  variant, plus 2 boundary, 1 neutral and 2 trivial. Of the 16 distance variants, **3 discriminated**; the
  other 13 passed in every arm, so they measured nothing.
- **The hit rate is the whole problem.** Writing more variants of the same kind would need about fifty to
  reach ten discriminating, at the observed rate of roughly one in five. The first task is therefore not
  to write tasks.

## Device runs

none. No device or production system is touched. The trial run itself is deferred to its own decision.

## Milestones

- **M1** · why the three discriminated, and the rest did not · waiting
- **M2** · the design rule that follows, written into the protocol as an amendment · waiting
- **M3** · ten discriminating tasks built and dry-checked against `harness.py check` · waiting
- **M4** · the new primary contrast registered, before any trial · waiting
- **M5** · the owner decides whether to run, and at ten or twenty · waiting

## Running now

### Lane A · diagnosis, then design

- **D1 Read the three that worked against the thirteen that did not.** For each of the sixteen distance
  variants: where the decisive fact sits, how far from the edited file, whether any path from the prompt
  reaches it, what the naive solution gets wrong, and whether a model could pass by ordinary care. Output is
  a table, one row per variant, and a stated rule for what makes a variant discriminate. *Read-only.*
- **D2 Write the rule into `evals/PROTOCOL.md` as a dated amendment**, below the untouched registered text,
  so that a later reader sees the design changed and when. The two traps that discriminate are named as
  the seed cases.
- **D3 Decide what counts as independent.** Two distances of one trap are two rows and one trap. The
  amendment states whether the analysis treats them as one unit or two, and argues it; the count of ten is
  ten by that definition, not ten directories.

### Lane B · building

- **B1 Build to ten discriminating candidates** by the rule from D2, preferring new traps over new distances
  of old ones, so that the count is independent. Each is a repository fixture, a prompt, visible tests,
  hidden tests, a naive solution and a reference solution, in the shape `evals/tasks/<id>/` already uses.
- **B2 Add boundary tasks at distance.** There are two boundary tasks and both sit beside the code, so the
  shape where a note misfires at distance is unmeasured — the gap row A5. At least two, by the same rule.
- **B3 `python3 evals/harness.py check`** must see every new task's graders fail on the naive solution and
  pass on the reference. A task whose graders do not do both is not a task.

### Lane C · what the run will claim

- **C1 Register the new primary contrast before any trial.** The pre-registered one was null for a stated
  reason: deleting the target note leaves its principle in neighbouring notes. The contrast that fits is the
  bundle against the two-line instruction file, on discriminating tasks. It is registered, with its stopping
  rule and its budget cap, before a single trial.
- **C2 Price the run and put it to the owner**: arms × tasks × repetitions, in trials, with an order of
  magnitude in tokens and money, and the wall time. The owner's quota is a cost.

## The owner's

- [at M2] **approve the design rule** that says what makes a variant discriminate, before ten tasks are built on it.
- [at M3] **ten or twenty**, decided against the priced run, not before it.
- [at M4] **approve the new primary contrast** and its budget cap, before any trial.
- [at M5] **the run itself**: credentials and quota are the owner's, and no trial starts without that word.

## Needs, risks and the fresh read

- **Needs from unmerged work:** none. This plan touches only `evals/`.
- **Risks the review must probe:**
  - *The rule is fitted to three cases and does not generalise.* Test: build the first three tasks by the
    rule, dry-check them, and have a fresh-context reader predict which would discriminate before any run.
  - *The new tasks are easier, not more discriminating* — a task where every arm fails measures as little as
    one where every arm passes. Test: the naive solution must fail the hidden tests and the reference must
    pass, which `harness.py check` enforces.
  - *Ten tasks written by the same hand share its blind spot.* Test: at least a third of the new traps come
    from defects a real repository actually shipped, not from a note read backwards. This is row A4, and it
    is the part that makes the set credible to someone who did not write it.
  - *The amendment quietly rewrites the registered plan.* Test: the registered text is not edited; the
    amendment is dated and sits below it, and the report states which analysis each figure used.
- **Spike:** D1 is the spike. If no rule survives it, the honest outcome is to say the design cannot be
  fixed by more tasks of this kind, and that is a finding worth the day.
- **Fresh read:** before B1, a fresh-context agent reads this plan and D1's table and says whether the rule
  follows from the evidence.

## Tasks

| # | Task | State | Milestone | Est. (min) | Actual (min) | Est. (ktok) | Actual (ktok) | Rounds |
|---|---|---|---|---|---|---|---|---|
| D1 | Why three discriminated and thirteen did not | waiting | M1 | 90 | | 200 | | 1 |
| D2 | The design rule, as a dated amendment | waiting | M2 | 45 | | 100 | | 1 |
| D3 | What counts as an independent task | waiting | M2 | 30 | | 60 | | 1 |
| B1 | Build to ten discriminating candidates | waiting | M3 | 420 | | 600 | | 2 |
| B2 | Boundary tasks at distance | waiting | M3 | 120 | | 180 | | 1 |
| B3 | Graders seen to fail and pass | waiting | M3 | 45 | | 60 | | 0 |
| C1 | Register the new primary contrast | waiting | M4 | 45 | | 80 | | 1 |
| C2 | Price the run for the owner | waiting | M5 | 30 | | 40 | | 1 |

About thirteen agent hours by this table. **Calibration, from the four tasks measured on 2026-11-26:** wall
time ran at a quarter to a third of estimate and the delegated lane at a fifth, so the honest expectation is
nearer four hours; the estimates are left as made, so the comparison stands.

**What this plan deliberately does not do.** It does not run a trial, change a figure in the frame, or
touch the claim that the bundle helps. Ten tasks make an effect *findable*; they do not make it exist.
