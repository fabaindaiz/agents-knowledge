# Plan: the next session — everything that is pending, in the order it should be taken

Written 2026-11-26 at the owner's instruction: leave a complete plan for the next session and execute
nothing of it now. It is the one place to start from; it points at the two plans that already exist rather
than restating them.

## The question now

**What is left, and what of it can be done without the owner's quota?** Four lanes. Three of them run with
no credentials at all; the fourth, the only one that can move the figure a sceptic reaches first, needs a
trial and therefore the owner's word and quota.

The honest ordering is not the cheapest first. A sceptical reader meets the evidence before anything else,
so lane E is first in importance and lane R is first in time, because it is an hour and clears two warnings
that fire on every gate run.

## Where we are

- **Built this release and merged into `plan/next-phases`:** T7 and T10 (the cut as a build rule, the coding
  read from about 10.1k to about 6.9k tokens), T8 (the live state and the compaction hooks), T9 (answers
  written as they arrive, the question rules and their hook), T11 (the compaction probe and its baseline),
  T12 (the research's candidates queued), `usage measure` over local transcripts. Three commits are not
  pushed.
- **Not built:** T14 to T18 and T13 of `meta/plans/2026-11-26-the-session.md`, about nine and a half agent
  hours by that plan's own table, plus the budget drop that closes the phase.
- **The evidence** is registered in `meta/reviews/2026-11-26-weak-points-before-presenting.md`, rows A1 to A7
  and B1 to B7, and its fix is planned in `meta/plans/2026-11-27-discriminating-tasks.md`.
- **Two frame figures are stale**, found on 2026-11-26 while reviewing what is pending: `MANIFEST.md` says
  the hand-off runs to about 2.9k words where it is a little over four hundred, and that the export is about 1.0 MB where it is
  about 1.16 MB — **about 95 % of the cap**. The second is the one that matters: there is little room left
  before `release` refuses a cut.

## Device runs

none. No device or production system is touched. The one trial this plan contemplates is lane E's, and it
is the owner's decision at the end of its own plan, not a step here.

## Milestones

- **N1** · the records true and the two stale frame figures corrected · **done 2026-11-27** (`4fc5032`, `198d74b`)
- **N2** · the phase finished: T14 to T18, T13, and the coding budget lowered · waiting
- **N3** · the discriminating set built and the new contrast registered · waiting — its own plan
- **N4** · the page rewritten against the presentation research · waiting
- **N5** · the release cut, and only when the owner says the version is closed · waiting

## Running now

### Lane R · the records and the claims · no credentials · about an hour

Writes `evals/README.md`, `evals/REPORT.md` (heads only), `meta/decisions.md`, `meta/tracking/experiments.md`,
`MANIFEST.md`.

- **R1 B3: the two stale headers.** `evals/README.md` and the head of `evals/REPORT.md` say "five exploratory
  pilots"; the body runs to twelve plus the reviewer runs. Rewrite both from the body, counting, not
  remembering.
- **R2 B7: the two orphan slugs** in `meta/tracking/experiments.md` that name no note, candidate or answered
  idea. Resolve or remove; the check warns on every run until they go.
- **R3 B6, the cheap half: the five decision rows naming an enforcing file that no longer exists.** Point each
  at what enforces it today, or lower its rung honestly. The other twenty-nine rows, whose reason no person
  confirmed, are a decision walk and are **not** in this lane.
- **R4 The two stale `MANIFEST.md` figures.** Recompute both from `release.py report` and write them with the
  date of the measurement. Changing `MANIFEST.md` takes a decision row by the owner, so this lands as a
  proposal in the same message, not as a silent edit.
- **R5 B2: the cadence promise.** The frame promises one release a month; the real cadence is roughly two a
  week. Either the promise changes to what is done, or it says why the burst is temporary and when it ends. A
  promise nobody keeps reads as rung 3 and behaves as rung 0. **The owner decides which**; the lane writes the
  row he chooses.

### Lane P · finishing the phase · no credentials · about nine and a half agent hours

Writes `sources/bundle/knowledge/`, `sources/bundle/method/skills/`, `sources/bundle/tools/bundle.py`,
`meta/tests/`. Disjoint from lane R and lane C; **not disjoint from itself**, so its tasks run in series or
split by the files below.

- **P1 T17 `seen_in` on every note, and the cross-domain requests the router must reach**, the clock case
  first. Writes `sources/bundle/knowledge/`. 105 min.
- **P2 T14 the `brief` skill**, over the live state and `bundle.py brief`. Writes a new skill and the tool.
  60 min.
- **P3 T15 the `lanes` skill and `bundle.py lanes check`**, from the two design rounds already walked.
  105 min.
- **P4 T16 the `ship` and `cut` skills.** 60 min.
- **P5 T18 the `plan` skill, `bundle.py plan calibrate`, and the unattended mode's design round** — the
  design round runs inside this task, with the owner. 165 min.
- **P6 T13 the phase's review by severity**, three rounds priced, over everything lanes R and P wrote.
  70 min.
- **P7 The coding budget.** `BUDGETS["coding"]` is about 10.1k against a measured read of about 6.9k. Lower it to about
  7.4k — the phase's last step, deliberately last so the cut cannot be undone silently. Minutes.

### Lane E · the evidence · the only lane that needs the owner's quota, and only at its end

Writes `evals/` alone. **Its plan is `meta/plans/2026-11-27-discriminating-tasks.md`** and is not restated
here: D1 to D3 (why three of sixteen discriminated, and the design rule that follows), B1 to B3 (ten
discriminating tasks and boundary tasks at distance, graders seen to fail and pass), C1 and C2 (the new
primary contrast registered before any trial, and the run priced for the owner). About thirteen agent hours
by its table, nearer four by this month's calibration.

**What it fixes:** A2, A3, A5, and part of A4. **What it cannot fix:** A1, the cost above the bound, which
needs a run; A6, the general-performance study, which has no data and should either be run or stop being
cited; A7, which nothing fixes and which must be stated wherever the real-session figures appear.

### Lane C · the page · no credentials · about two hours

Writes the adoption artifact alone, and nothing in the repository.

- **C1 Rewrite the page against the six recommendations** of `meta/reviews/2026-11-26-how-to-present-the-method.md`:
  the problem and the audience above the fold with the evidence figure out of the opening; the cost and the
  "not for you" section moved up beside the central idea; the evidence section in the shape of a decision
  record — claim, method, result with its interval, what it cannot show, the decision it supports; cut to one
  screen per section with the cards on their own page; split by what the reader came for; and an adoption path
  that opens with the smallest real trial, its measured token cost, and how to remove the bundle again.
- **C2 Do not quote a conversion figure.** The research looked and found only vendor blogs. Inventing one
  would be the exact kind of claim this project exists to refuse.

## The owner's

- [at R4, R5] **the two frame decisions**: the corrected figures, and whether the cadence promise changes or
  explains itself. Both need a decision row in `meta/decisions.md`.
- [at P5] **the unattended mode's design round**, inside T18, as decided on 2026-11-26.
- [at lane E, M2 and M4] **the design rule**, then **the new primary contrast and its budget cap**, each
  before anything is built or run on it.
- [at lane E, M5] **the trial itself.** Credentials and quota are the owner's; no trial starts without that
  word.
- [at N5] **the release.** It is cut only when the owner says the version is closed.

## Needs, risks and the fresh read

- **Needs from unmerged work:** none. Everything lanes R, P and C touch is on `plan/next-phases`, and lane E
  touches only `evals/`.
- **Risks:**
  - *Lane P's six tasks are the same shape as the four that already overran their review rounds.* The phase's
    own calibration priced review rounds at two and they took one; P6 is priced at three and should be left
    there until a round proves otherwise.
  - *Lane R quietly becomes a decision walk.* R3 is five rows, not thirty-four. The twenty-nine unconfirmed
    reasons are their own session and are named here so that they are not swept into an hour's work.
  - *Lane C rewrites the page into marketing.* The research's one measured finding is that shorter and
    non-marketing reads more easily; the test is that every adjective in the evidence section has been
    replaced by a number, a sample and a limit.
  - *The export is at about 95 % of its cap*, so any lane that adds shipped text can push the cut over it.
    `release.py report` is read before and after lane P, and the cut shrinks before anything is added.
  - *Four lanes at once exceed the three-agent limit.* The split below respects it.
- **Fresh read:** before lane P starts, a fresh-context agent reads `meta/plans/2026-11-26-the-session.md`
  and this plan and states which of T14 to T18 the cut of 0.0.38 already changed.

## The split, and its price

Three agents at most, by disjoint file sets. Lane R and lane C write nothing the others write; lane P writes
the bundle's sources; lane E writes `evals/` alone.

| Lane | Model | Files it writes | Est. (min) | Est. (ktok) |
|---|---|---|---:|---:|
| R · records and claims | the smaller model | `evals/*.md` heads, `meta/decisions.md`, `meta/tracking/experiments.md`, `MANIFEST.md` | 60 | about 80 |
| P · the phase | the larger model, in the main thread | `sources/bundle/`, `meta/tests/` | 565 | about 1.1k |
| E · the evidence | the larger model, delegated | `evals/` | 825 | about 1.3k |
| C · the page | the smaller model, delegated | the artifact alone | 120 | about 150 |

## Tasks

| # | Task | State | Milestone | Est. (min) | Actual (min) | Est. (ktok) | Actual (ktok) | Rounds |
|---|---|---|---|---|---|---|---|---|
| R1 | The two stale experiment headers | done | N1 | 30 | 12 | 40 | — | 0 |
| R2 | The two orphan slugs | done | N1 | 10 | 25 | 10 | — | 1 |
| R3 | The five stale enforcers | done | N1 | 15 | 18 | 20 | — | 0 |
| R4 | The frame's figures, with their dates | done | N1 | 15 | 14 | 20 | — | 1 |
| R5 | The cadence promise | done | N1 | 15 | 4 | 15 | — | 1 |
| P1 | T17 `seen_in` and cross-domain requests | waiting | N2 | 105 | | 250 | | 1 |
| P2 | T14 the `brief` skill | waiting | N2 | 60 | | 150 | | 1 |
| P3 | T15 the `lanes` skill and `lanes check` | waiting | N2 | 105 | | 270 | | 1 |
| P4 | T16 the `ship` and `cut` skills | waiting | N2 | 60 | | 150 | | 1 |
| P5 | T18 the `plan` skill and the unattended mode | waiting | N2 | 165 | | 400 | | 1 |
| P6 | T13 the phase's review by severity | waiting | N2 | 70 | | 450 | | 3 |
| P7 | The coding budget lowered | waiting | N2 | 10 | | 15 | | 0 |
| E1 | Lane E, whole | waiting | N3 | 825 | | ~1.3k | | — |
| C1 | The page against the six recommendations | waiting | N4 | 120 | | 150 | | 2 |

About twenty-six agent hours by this table, over every lane. **Calibration, measured on 2026-11-26 across six
tasks:** wall time came in at a quarter to a third of estimate, and a delegated lane at a fifth, so the honest
expectation is nearer seven to nine hours. The estimates are left as made so the comparison stands.

## What this plan deliberately does not do

It does not run a trial, cut a release, push anything, or change a figure in the frame without a decision
row. It does not take the twenty-nine unconfirmed decision reasons, which are their own session. And it does
not claim that finishing it makes the bundle demonstrably useful: lanes R, P and C make the project honest
and legible, and only lane E, followed by a run the owner authorises, can make the central claim testable.

## Lane R as it ran, 2026-11-27

Estimated an hour; took about one hour and ten minutes, and two of its five tasks were not what the plan
said they were.

- **R2 was not bad data.** Both orphan slugs name experiments on **rules of the method**, not on notes, and
  the column they sit in is headed *Note*. They are now written `method:<name>`, which the slug pattern
  already passes over — a red run proved that a guard for it would be dead code, and the guard was deleted
  before it was committed. The convention is stated in the file's own header and in the shipped `OPEN.md`.
- **R3 was not stale data either.** Four of the five rows are a **superseded** decision naming the list its
  own successor deleted, and the fifth names two proposals pruned after they were received. The check now
  exempts a superseded or deprecated row's enforcer, exactly as it already exempted its reason, and the
  fifth row points at `meta/tracking/received.md`. Seen to fail first.
- **R4 grew.** Four of the five figures in the limits table were wrong, not two, and the export turned out
  to sit at about 95 % of its cap. Every figure now carries its measurement date (`d-5ed7e8-f5564d`).
- **What this says about the register.** Two of five rows in `meta/reviews/2026-11-26-weak-points-before-presenting.md`
  described the symptom a check printed rather than the defect behind it. A row of that register is a lead,
  not a diagnosis, and the next lane should expect the same.
