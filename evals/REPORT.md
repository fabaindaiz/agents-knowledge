# Does an engineering-judgment bundle change what a coding agent does? A pilot study

**Status: exploratory pilots complete (five runs); confirmatory run not started.** This report records the pilot runs of the experiment
pre-registered in [`PROTOCOL.md`](PROTOCOL.md) (roadmap item `i-5ed7e8-0d9b6a`). Nothing here is a
confirmatory result. It is written as it happens, including what went wrong in the instrument, and
it is updated after every run; the changelog at the end dates each revision.

**What this study can and cannot say.** Every task here was written from a note: `task.json` names its
target note, the hidden test checks that note's claim, the tasks' author had read the notes, and the
`oracle` arm is given the note in full. So a pass in a note-carrying arm measures, in part, whether an
instruction reached a decision on a task built to reward it. This study measures **instruction
transfer**. It says nothing about whether carrying the bundle makes the agent better or worse at work
in general. That question is Study 2 ([`PROTOCOL-general.md`](PROTOCOL-general.md), roadmap item
`i-5ed7e8-bf5663`), on tasks from external benchmarks with no task, grader or rule derived from the notes.

## Abstract

Repository instruction files are now common, but controlled studies find that they do not improve task
success and raise inference cost by about a fifth. This bundle makes a narrower claim: that its knowledge
notes change an agent's decision in the cases where the textbook answer is wrong. We built a harness that
tests that claim with hidden-test graders, six arms that separate the notes' content from context length
and from routing, and task families where a note should help, where it should be ignored, and where it is
irrelevant; we ran five exploratory pilots (612 trials, two models, 27 tasks).

**On tasks where the decisive fact sat beside the code, the frontier model never needed the notes** (it
passed all 216 such trials, in every arm); this was a design error of ours, since it measured whether the agent
reads the file it edits. **Moving the fact elsewhere in the repository broke the ceiling on 3 of 16 tasks:**
there, the arms that carried the bundle or the note passed 17 of 18 trials (`bundle`, `ablated`, `oracle`)
and the arms that carried neither passed 1 of 18, while a length-matched irrelevant note did
nothing. The agents did not find the fact; they applied the note's principle by default. With so few
discriminating tasks nothing is statistically significant (the smallest attainable p-value is 0.25). The
pre-registered primary contrast, the bundle against the bundle without the target note, was null because
the notes overlap: neighbouring notes carried the same principle. A smaller model showed one clean content
effect, one failure the notes did not fix, one over-application a note caused against its own stated
boundary, and weaker routing to the notes. **Carrying the bundle cost about 2.1 to 2.3 times as much per
task for the frontier model in every pilot, and about 1.6 times for the smaller one**, confirmed after we found and corrected an instrument defect that had produced one
spurious finding, now withdrawn.

## 1. Question

The bundle's knowledge base claims to hold *which heuristic applies, when, and where it stops
working*: the part an agent's training does not tell it. Its admission rule requires, of every note,
that "an agent would get this wrong without it". The question for this study is conditional:

> On a task where a note applies, does carrying the bundle change the outcome, and is it the note's
> content that changes it — rather than the extra context, a general push toward caution, or the
> method the bundle also carries?

How often a note applies in real work is a separate question, which this design does not answer.

## 2. Related work

| Study | Design | Tasks | Arms | Runs per cell | Primary metric | Result |
|---|---|---|---|---|---|---|
| Gloaguen et al. 2026, arXiv 2602.11988 | controlled | 138 niche-repository tasks + 300 SWE-bench Lite | none / LLM-generated file / developer file | 1 | hidden tests | no significant change (developer files +2.4 pp, p = 0.21); cost +20 to 23%; for the one Claude agent, developer files 73.2% → 70.3% |
| Khatri 2026, arXiv 2607.27250 | controlled, paired | 17 PRs from 3 repositories | none / always-on / selective wiki | 3 | hidden tests | no difference (Claude 53.3 / 55.6 / 55.6%); equivalence bound under 10 pp, but its own power analysis puts the detectable effect near 30 pp |
| Lulla et al. 2026, arXiv 2601.20404 | controlled, paired | 113 usable PRs from 10 repositories | with / without AGENTS.md | 1 | wall time, tokens | median time −28.6%, output tokens −16.6%; **correctness not measured** |
| SkillsBench, arXiv 2602.12670 | controlled | 84 tasks | none / curated skills / self-generated skills | several | pass rate | curated skills 33.9% → 50.5%; self-generated gave nothing |
| Skill-component ablation, arXiv 2607.07504 | controlled | — | full skills / length-matched irrelevant text | — | pass rate | full skills no better than the length-matched placebo (−0.8 pp, p = 0.50) |
| **This pilot** | controlled, paired, randomised order | 11 synthetic tasks: 8 judgment, 2 boundary, 1 neutral | none / minimal / bundle / ablated / oracle / oracle-placebo | 2 | hidden tests on the consequence of the decision | see *Results* |

Two gaps in that literature shaped the design. First, every prior study grades bug fixes or feature
PRs with tests that encode behaviour, not design judgment, so a note that changes a decision can only
show up by accident. Second, only one study used a placebo, and none used an oracle, so a null could
not be split into "the content does not help" and "the agent never read it".

## 3. Method

The full protocol, fixed before the confirmatory run, is [`PROTOCOL.md`](PROTOCOL.md). In brief:

**Arms.** Every arm starts from the same repository.

| Arm | Instructions the agent receives | Isolates |
|---|---|---|
| `none` | nothing | the unaided agent |
| `minimal` | a two-line `AGENTS.md` with the test command | the realistic baseline |
| `bundle` | `minimal` + a paragraph routing to the knowledge index + the whole `.agents/` bundle (about 220k tokens on disk, read on demand) | the treatment |
| `ablated` | identical to `bundle`, with the task's target notes deleted and every line naming them removed (about 1% of the bundle) | the placebo for the content, with length, structure and routing held |
| `oracle` | `minimal` + the target note's full text, always loaded | the content when it is certainly read |
| `oracle_placebo` | `minimal` + one irrelevant note of matched length (within 3%), chosen by a mechanical rule | the placebo for `oracle` |

**Tasks.** Each task is a small repository, a request written as a colleague would write it, and a
hidden grader the agent never sees. In a *judgment* task a plausible, textbook-shaped solution passes
the visible tests and violates a requirement the repository states (a customer charged twice when a
retried call times out after the charge applied; a nested settings object replaced whole, erasing
fields another service owns; a kill switch that leaves two of four entry points live). In a *boundary*
task a note's own *When it does NOT apply* holds, so applying the note is the mistake (a watchdog
that must start without its alert URL; a regulator-mandated audit log that must not be best-effort).
A *neutral* task is ordinary work. Every grader is required, by `harness.py check`, to fail on the
starting code and on a naive overlay, and to pass on a reference overlay, and the naive overlay must
fail by assertion rather than by an import error.

**Agent.** Claude Code in print mode (one release of its 2.1 series, the same in every run), one session per trial, with the model fixed per run;
tools Bash, Read, Edit, Write, Glob and Grep; no subagents, MCP servers or skills; 50 turns and 20
minutes per trial. Each trial runs in a fresh workspace under the system temporary directory, with no
instruction file and no repository above it, Bash inside Claude Code's sandbox with no network and no
read of the home directory, and user-level settings excluded. A manipulation probe (one tool-less
session per arm, asked to list the headings of the instructions it received) confirmed that `none`
received no instructions at all and every other arm exactly its own.

**Analysis.** The task is the unit; repetitions are averaged per task and arm, and every contrast is
a paired per-task difference, tested with a sign-flip randomisation test and reported with its
interval, minimum detectable effect and equivalence verdict (±10 pp). A contrast over fewer than
8 tasks, or with no variation at all, is described and not tested. Cost is the geometric mean ratio
of per-task means.

**Runs so far.**

| Run | Model | Tasks | Repetitions | Trials | Instrument | Estimated cost, order of magnitude (API prices) |
|---|---|---|---:|---:|---|---:|
| pilot-1 | Sonnet 5 | 4 | 2 | 42 | permission defect (§4.2) | a few dollars |
| pilot-2 | Sonnet 5 | 11 | 2 | 126 | permission defect (§4.2) | about ten dollars |
| pilot-3 | Haiku 4.5 | 11 | 2 | 126 | corrected | a few dollars |
| pilot-4 | Sonnet 5 | 11 | 2 | 126 | corrected | about ten dollars |
| pilot-5 | Sonnet 5 | 16 (the eight traps at L1 and L2) | 2 | 192 | corrected | under twenty dollars |

The runs used a subscription, so the cost figures are Claude Code's own estimates at API prices, not
an amount paid; a trial costs cents. Costs are compared as ratios throughout.

## 4. Results

### 4.1 The manipulation took

In every bundle-carrying trial the agent opened the knowledge index (pilot-2: 22 of 22 in `bundle`,
20 of 20 in `ablated`) and, in `bundle`, read the target note in 17 of 22 trials; it read about two
notes per trial on average and at most three. No `ablated` trial could read a target note, and none
did. No trial in any arm accessed a path outside its workspace.

### 4.2 An instrument defect, found by the pilot

The first two runs used Claude Code's `dontAsk` permission mode with the sandbox's automatic approval
of Bash. That combination **refused Bash commands that write files** (heredocs, in-place edits,
copies), and the agent then worked around the refusal or reported that it could not run its tests.
The refusal rate was not the same across arms:

| Pilot-2 arm | Trials with at least one refused command |
|---|---:|
| none | 4 of 22 |
| minimal | 4 of 22 |
| bundle | 10 of 22 |
| ablated | 12 of 20 |
| oracle | 6 of 20 |
| oracle_placebo | 7 of 20 |

The bundle-carrying arms attempted more of the refused commands, largely because the notes they read
ask for checks such as watching a test fail after deliberately breaking the code, which the agent
did with an in-place edit. So in those two runs the arms differed not only in what the agent was told
but in what it was allowed to do. This does not change the primary outcome (every judgment trial
passed in every arm), but it confounds the secondary outcomes below, and it is exactly the kind of
difference a confirmatory run must not contain. The harness now uses `acceptEdits` under the same
sandbox, a probe confirmed that file-writing commands succeed and that the home directory stays
unreadable, and every trial now records its refused tool calls, which the report tabulates per arm.
Pilots 3 and 4 repeat the runs with the corrected instrument. **Pilot-4 confirms the correction:** no
tool call was refused in any of its 126 trials.

### 4.3 Success: a ceiling

| Pilot-2, hidden tests passed | none | minimal | bundle | ablated | oracle | oracle_placebo |
|---|---:|---:|---:|---:|---:|---:|
| judgment (8 tasks × 2) | 16/16 | 16/16 | 16/16 | 16/16 | 16/16 | 16/16 |
| boundary (2 tasks × 2) | 4/4 | 4/4 | 4/4 | 3/4 | 4/4 | 4/4 |
| neutral (1 task × 2) | 2/2 | 2/2 | 2/2 | — | — | — |

Pilot-1 (4 tasks) was the same: 41 of 42 trials passed, and pilot-4, with the corrected instrument, passed
all 126. **The unaided model avoided every judgment
trap in every repetition.** Every pre-registered contrast on the judgment family is therefore exactly
zero with no variation, and by the protocol's rule it is described, not tested: no interval and no
equivalence claim can be made from data with no variance. Under the protocol's own calibration rule,
a judgment task the `none` arm passes in every run is set aside and recorded against its note's
admission criterion ("an agent would get this wrong without it"): for this model, that is all eight
tasks and the eight notes behind them.

That reading has to be qualified, and the qualification is a design error of ours, not a property of
real repositories. The protocol requires the tested requirement to be stated in the repository, so that
the grader tests a good decision and not obedience to a note. We met that rule in the easiest possible
way: repositories of three or four files, where the fact that makes the trap avoidable sits in a
docstring of the file the agent must edit, or of its neighbour (the transport retries on timeout; the
provider delivers each event at least once; other services write these fields). Several prompts also
pointed at the answer (*using the service's transport like every other outbound call*; *re-running an
import must not create duplicates*). A note exists for what the agent does not see; these tasks put it
in front of the agent, so they measured whether the agent reads the file it is editing, which a strong
model always does. **What the pilot shows is only this: when the relevant fact is stated beside the
code, this model does not need the note to act on it.** It is not evidence that the notes are
unnecessary where the fact is harder to find.

The correction (pilot-5) keeps the fairness rule and makes distance a controlled variable: each
judgment trap is rebuilt at level L1, where the fact is only in code in another module, with no prose,
and at level L2, where it is only in distant documentation or configuration, among distractors, in a
repository of a few dozen files. Prompts at both levels carry no hint.

### 4.4 Cost: about twice as much per task

| Pilot-2, ratio of per-task means (95% bootstrap interval) | Judgment, 8 tasks | Boundary, 2 tasks | Neutral, 1 task |
|---|---|---|---|
| estimated cost, `bundle` / `minimal` | ×2.13 [1.94, 2.36] | ×2.49 [2.35, 2.63] | ×2.51 |
| turns, `bundle` / `minimal` | ×1.37 [1.25, 1.48] | ×1.36 [1.24, 1.50] | ×1.62 |
| output tokens, `bundle` / `minimal` | ×1.60 [1.42, 1.82] | ×1.74 [1.46, 2.08] | ×2.35 |
| wall time, `bundle` / `minimal` | ×1.54 [1.37, 1.77] | ×1.69 [1.49, 1.90] | ×1.93 |
| estimated cost, `minimal` / `none` | ×0.99 [0.88, 1.07] | ×0.97 [0.95, 0.99] | ×0.95 |
| estimated cost, `oracle` / `minimal` (medians) | ×1.28 | | |

Relative to the median `minimal` trial in pilot-2, the median `bundle` trial cost about 2.3 times as much, `ablated` about 2.6 times, and `oracle` about 1.3 times. The overhead comes from what the agent reads (the index, an area index and about two
notes), not from the always-loaded instructions: `oracle`, which always loads a full note, costs about
a quarter more than `minimal`, and `ablated` costs as much as `bundle`. This is larger than the
overhead Gloaguen et al. measured for a single always-on file (+20 to 23%). **It is not an artefact of
the refused-command defect:** pilot-4, with no refused command in any arm, measured `bundle` / `minimal`
at ×2.27 [1.99, 2.66] in cost, ×1.45 [1.33, 1.60] in turns and ×1.70 [1.48, 2.03] in wall time on the
judgment tasks, the same as pilot-2 within its interval.

### 4.5 Secondary observations, with their confounds

**Over-application of fail-closed defaults.** Across pilots 1 and 2 the watchdog boundary task
failed twice in 20 trials: the agent made the watchdog refuse to start without its alert URL, which the
repository says it must never do. Both failures were in arms that did **not** contain the relevant note
(`oracle_placebo` once, `ablated` once); the arms that contained it (`bundle`, `oracle`) passed all
eight of their trials. That is the direction the note's boundary section predicts, but two events are
not evidence of anything, and both failing arms are placebos that carry other engineering prose, so
"the placebo text primes caution" is as good an explanation as "the note prevents it".

**Failing visible tests left behind — withdrawn: it was the instrument.** In pilots 1 and 2, 7 of the 8
order-charging trials in `bundle` or `ablated` ended with a failing test the agent had added itself, and
in all seven one of the agent's commands had been refused (§4.2); in the transcripts read in full, that
command was the one that would have run the suite. With the corrected instrument (pilot-4) the visible
suite passed at the end of every trial in every arm (16 of 16 judgment trials per arm). The observation
is withdrawn: it measured the defect, not the bundle. It stays here because a pilot that hides what it
got wrong teaches nothing about how the confirmatory run could get it wrong.

The fail-closed over-application above did not recur in pilot-4 (0 failures in 24 boundary trials).

### 4.6 A weaker model: Haiku 4.5 on the same tasks (pilot-3)

With the corrected instrument and the same eleven L0 tasks, the smaller model fails where the frontier
model did not, and the failures are real: in every failing trial inspected, the agent wrote the
textbook answer the task was built around (the shop customer number used as the contact id; the
shipment email allowed to fail the shipment, with a test the agent wrote asserting that it does; the
watchdog refusing to start without its alert URL although the README says it must always start).

| Pilot-3, hidden tests passed | none | minimal | bundle | ablated | oracle | oracle_placebo |
|---|---:|---:|---:|---:|---:|---:|
| judgment (8 tasks × 2) | 12/16 | 12/16 | 14/16 | 12/16 | 15/16 | 12/16 |
| boundary (2 tasks × 2) | 2/4 | 2/4 | 2/4 | 2/4 | 1/4 | 2/4 |
| neutral (1 task × 2) | 2/2 | 2/2 | 2/2 | — | — | — |

Six of the eight judgment tasks were passed in every arm and do not discriminate. The two that do:

- **Shipment email (best-effort side channels): a clean content effect on one task.** It passed 2 of 2
  in `bundle` and in `oracle`, the two arms that contain the note, and 0 of 2 in each of the four arms
  that do not, `ablated` and `oracle_placebo` included. For this task, it is the content, not the
  length and not a push toward care.
- **Second contact source (derived identifiers): the note does not rescue it.** It failed in every arm,
  including `bundle`, and passed once in 2 in `oracle`, where the note is certainly in context.

| Pilot-3 contrast (judgment, 8 tasks) | A − B | 95% CI (t) | p (sign-flip) | MDE at 80% |
|---|---:|---|---:|---:|
| **primary**: `bundle` − `ablated` | +12.5 pp | [−17.1, +42.1] | 1.000 | 35.0 pp |
| `bundle` − `minimal` | +12.5 pp | [−17.1, +42.1] | 1.000 | 35.0 pp |
| `oracle` − `oracle_placebo` | +18.8 pp | [−12.4, +49.9] | 0.500 | 36.8 pp |
| `oracle` − `bundle` | +6.2 pp | [−8.5, +21.0] | 1.000 | 17.5 pp |

None of this is significant, and it could not be: one or two tasks out of eight carry all of the
difference, and the minimum detectable effect is about 35 points. The direction is the one the
bundle's claim predicts, and it rests on one task.

**Boundary tasks: the note caused an over-application, once, and did not prevent one.**

- The watchdog task failed in all 12 trials, in every arm, with or without the fail-closed note. The
  note's boundary section, which names this case, did not change it.
- The audit-log task failed once, in `oracle`, where the best-effort note is always loaded: the agent
  made the regulator-mandated audit write optional and said in its final message that it was
  following "the best-effort side-channel pattern" from its instructions. The note's own *When it
  does NOT apply* lists exactly this case (a legally required log). It is one trial, and it is the
  first observation in this study of a note's content causing the error its boundary warns against.

**Routing is weaker for the smaller model.** In `bundle`, Haiku opened the knowledge index in 14 of 22
trials (Sonnet: 22 of 22) and read the target note in 9 (Sonnet: 17 to 19). Every judgment trial in
which it read the target note passed (7 of 7), against 7 of 9 in which it did not; that split is
correlational, but together with `oracle` > `bundle` it points at routing as a limit for smaller models.

**Cost.** `bundle` / `minimal` ×1.57 [1.17, 2.11] in estimated cost on the judgment tasks: less than for
Sonnet, consistent with Haiku reading less of the bundle.

**Instrument notes from this run.** In five trials, spread across arms, the agent tried to read the
user-level git configuration in order to commit its work; the sandbox and the permission rules blocked
every attempt, and the configuration was verified unchanged afterwards. Because Claude Code passes the
logged-in account's identity to the session, run transcripts contain it; they are kept out of the
repository. In six trials of all runs the agent committed its own work, which emptied the recorded diff
(grading was unaffected, since it runs on the final workspace); the harness now diffs against the
starting commit.

### 4.7 Moving the decisive fact away from the code (pilot-5)

The same frontier model, the corrected instrument, and the eight judgment traps rebuilt at two distances
(§4.3): L1, the fact only in code or data elsewhere; L2, the fact only in distant documentation or
configuration, among distractors. A blind reviewer, given only each task's prompt, repository and grader,
judged 11 of the 16 fair and 5 fair with a caveat, none unfair and none over-asserting; it also found two
construction errors of ours (a convention left in the edited file; a test hook left in production code),
both fixed before the run.

| Pilot-5, judgment tasks passed | none | minimal | bundle | ablated | oracle | oracle_placebo |
|---|---:|---:|---:|---:|---:|---:|
| L1 (8 tasks × 2) | 14/16 | 14/16 | 16/16 | 15/16 | 16/16 | 14/16 |
| L2 (8 tasks × 2) | 13/16 | 12/16 | 16/16 | 16/16 | 16/16 | 12/16 |

**Distance breaks the ceiling, on three tasks of sixteen.** The unaided model now fails the second
contact source at L1 and at L2 (0 of 4) and the refund webhook at L2 (1 of 2). On those three tasks the
pattern is the same: the arms that carry the bundle or the note pass, the arms that carry neither fail.

| Task | none | minimal | oracle_placebo | bundle | ablated | oracle |
|---|---:|---:|---:|---:|---:|---:|
| contacts-second-source-l1 | 0/2 | 0/2 | 0/2 | 2/2 | 1/2 | 2/2 |
| contacts-second-source-l2 | 0/2 | 0/2 | 0/2 | 2/2 | 2/2 | 2/2 |
| refund-webhook-l2 | 1/2 | 0/2 | 0/2 | 2/2 | 2/2 | 2/2 |

| Pilot-5 contrast (judgment, 16 tasks) | A − B | 95% CI (t) | p (sign-flip) | MDE at 80% | Within ±10 pp |
|---|---:|---|---:|---:|---|
| **primary**: `bundle` − `ablated` | +3.1 pp | [−3.5, +9.8] | 1.000 | 8.8 pp | yes |
| `bundle` − `minimal` | +18.8 pp | [−2.7, +40.2] | 0.250 | 28.2 pp | no |
| `oracle` − `oracle_placebo` | +18.8 pp | [−2.7, +40.2] | 0.250 | 28.2 pp | no |
| `oracle` − `bundle` | 0 | — | 1.000 | — | no |
| `minimal` − `none` | −3.1 pp | [−9.8, +3.5] | 1.000 | 8.8 pp | yes |

With three tasks improving and none worsening, the smallest p-value the exact sign-flip test can give is
0.25, so nothing here is significant, and the minimum detectable effect for `bundle` − `minimal` is about
28 points. What the numbers can say: the direction is consistent (3 better, 0 worse, in both the
`bundle` and the `oracle` comparisons), and the placebo of matched length did nothing (`oracle_placebo`
equals `minimal`), so on these tasks **extra text does not help; this content does.**

**The primary contrast is null for a reason that is a finding in itself: the notes overlap.** `ablated`
removes the target note, yet it passed 5 of 6 trials on the three discriminating tasks. The transcripts
say why: with the target note gone, the agent used a neighbouring note that carries the same principle —
`merge-by-shared-fact-not-shared-shape` for the colliding identifiers, `order-writes-by-failure-residue`
(which covers acknowledging an at-least-once delivery) for the redelivered refund. In one trial the agent
did not open any note at all and used the one-line claim in the area index. So the bundle encodes its
principles redundantly, and removing one note does not remove the principle. That makes the pre-registered
H1 the wrong test for this bundle: "±10 pp" here bounds the value of one note *given the rest of the
bundle*, not the value of the content. It also bears on the knowledge base's own rule that overlapping
claims are merged: the overlap is real, and it is what kept `ablated` passing.

**The mechanism is not discovery.** No trial in any arm read the file that holds the decisive fact (the
integration documentation, the sample exports, the schedule). The arms that passed did not find the fact;
they applied the principle by default — namespacing identifiers from two sources, making a
redelivered-event handler idempotent — because a note told them the textbook answer fails here. The one
`ablated` trial that failed shows the other side: the agent noticed that the two id spaces might overlap,
said it could not tell from the code, and left it. This is the bundle's claim working as written, and it
is also its risk: a principle applied without checking whether the fact holds is exactly how the
audit-log over-application in §4.6 happened. Pilot-5 had no boundary tasks at L1 or L2, so it cannot
measure that risk; the confirmatory set must.

**Routing and cost.** `bundle` opened the index in 32 of 32 trials and read the target note in 27. The
cost of carrying the bundle was the largest yet: ×2.32 [2.16, 2.50] in estimated cost, ×1.59 in turns and
×1.73 in wall time against `minimal`; `oracle`, which buys the same success rate on these tasks, loads one
note and nothing else.

## 5. Discussion

**Where this pilot agrees with the prior studies.** On tasks whose requirements are visible where the
agent works, context files do not change success for a strong model, and they cost more. Our overhead
(about 2.1 to 2.3 times the estimated cost per task for the frontier model and 1.6 times for the smaller
one, 1.3 to 1.6 times the turns) is larger than the
fifth measured for a single always-on file, because this bundle is consulted, not only loaded: the agent
opens an index, an area index and about two notes on nearly every task, relevant or not.

**Where it adds something they could not see.** The prior studies graded behaviour that tests encode and
had no placebo and no oracle. Here, on the three tasks where the unaided model did fail, the content made
the difference and length did not: `oracle` passed where `oracle_placebo`, a note of the same length
about something else, failed exactly like `minimal`. That is the first direct evidence for the bundle's
narrow claim — a note changes a decision the agent otherwise gets wrong — and it is thin: three tasks, one
model, two repetitions, no significance.

**How it works, and why that is double-edged.** The agents did not find the missing fact; they acted as
if it were true because a note said the textbook answer fails in that kind of situation. When the note's
situation holds, that is the value the bundle promises. When it does not, it is the over-application the
notes' boundary sections exist to prevent, and the one over-application a note caused (the smaller model
making a mandatory audit log best-effort, citing the note) happened despite a boundary section naming that
exact case. The pilot measured the benefit at distance and the harm only at L0; the harm at distance is
unmeasured.

**What the pilot suggests for the bundle**, as hypotheses for the confirmatory run and the roadmap, not as
conclusions:

- *The claim does the work.* In one discriminating trial the one-line claim in an area index sufficed; in
  most, one note was read. The full evidence and literature sections are what makes the bundle expensive
  to consult. A short card per note (claim, boundary, check), with the full note on demand, might keep the
  benefit and cut the cost.
- *The notes overlap, and that is load-bearing.* Removing one note did not remove its principle. Either
  the overlap is merged, as the knowledge base's own rules require, or it is kept and named; in both cases
  the unit of evaluation should be the principle, not the file.
- *Routing is model-dependent.* The frontier model read the index in every trial; the smaller one in about
  two thirds, and the note in about two fifths. A packaging that surfaces the right note without a
  lookup (a skill chosen by description, a path-scoped rule) would matter more for smaller models.
- *The boundary sections are not enough on their own.* One over-application caused by a note, and one trap
  (the watchdog) the smaller model fell into in every arm, note or not.

**What must change before a confirmatory run.**

1. Tasks at L1 and L2 only, written by someone who has not read the notes, reviewed blind, with boundary
   tasks at the same distances.
2. Ablation by principle, not by file: remove every note whose claim overlaps the target's, with the
   overlap decided by a rule written before the run (for instance, every note the pilot's `ablated`
   agents used in its place).
3. Enough discriminating tasks: only 3 of 16 discriminated at L1/L2 with this model. At that rate, a
   confirmatory set able to detect 20 points needs well over the 30 tasks the protocol planned, or tasks
   screened on the `none` arm to be ones the unaided agent fails (calibration, §*Procedure* in the
   protocol).
4. A second model family, since everything here is one vendor's models.

## 6. Threats to validity

| Threat | Status after five pilots |
|---|---|
| The maintainers built and graded the tasks after reading the notes | present; a blind review of the L1/L2 tasks found them fair or fair with caveats, but authorship stays with us |
| Task difficulty set by the experimenter | the main lesson: the L0 tasks were too easy by construction, and only 3 of 16 L1/L2 tasks discriminated |
| The `ablated` control leaks the principle through overlapping notes | found in pilot-5; the primary contrast is uninformative until ablation is by principle |
| One model family, one agent, one CLI release | present |
| Instrument defects | two found and corrected (refused commands; diffs lost to agent commits); one produced a spurious finding, withdrawn |
| Small samples | no contrast is significant; the smallest attainable p-value with three discriminating tasks is 0.25 |
| Boundary risk at distance unmeasured | present: no L1/L2 boundary tasks yet |
| The logged-in identity reaches the agent | contained: transcripts stay local, and attempts to use it outside the workspace were blocked |
| Subscription-based runs | costs are Claude Code's estimates at API prices, compared as ratios |

## 7. Conclusion so far

The bundle does not make a strong model better where the answer is in front of it, and it roughly doubles
the cost of every task. Where the decisive fact is out of sight, on the few tasks where that made the
unaided model fail, the bundle's content — not its length — turned failures into passes, by making the
agent apply a principle it would otherwise have missed; the same mechanism produced one failure of the
kind the notes warn against. The evidence for the benefit is directional and small, the evidence for the
cost is solid, and the evidence on harm is almost absent. The confirmatory run described in §5 is what
would turn this into an answer.

## Reproducing

```bash
python3 evals/harness.py check
python3 evals/harness.py plan evals/runs/NAME --model MODEL --reps 2 --config-dir default --max-turns 50 --timeout 1200 --seed SEED
python3 evals/harness.py probe evals/runs/NAME
python3 evals/harness.py run evals/runs/NAME --jobs 3
python3 evals/analyze.py evals/runs/NAME --exploratory
```

Seeds used: pilot-1 20260924, pilot-2 20260925, pilot-3 20260926, pilot-4 20260927, pilot-5 20260928. Run directories
(transcripts, diffs, per-run reports) stay local and are not committed.

## Changelog of this report

- **2026-09-25** — scope stated at the top: this study measures instruction transfer, because its tasks are written from the notes; the general-performance question moved to Study 2 (`PROTOCOL-general.md`, `i-5ed7e8-bf5663`).
- **2026-09-24** — session closed: the per-note evidence is recorded in `.agents/tracking/experiments.md` and the follow-up work in `.agents/roadmap.md` (the confirmatory run under `i-5ed7e8-0d9b6a`; overlapping notes under `i-5ed7e8-d4f710`; per-note summaries under `i-5ed7e8-a89859`; skills packaging under `i-5ed7e8-8623a8`).
- **2026-09-24** — first version: pilots 1 and 2, the instrument defect, pilots 3 and 4 started.
- **2026-09-24** — pilot-5 (distance) added; abstract, discussion, threats and conclusion rewritten over all five pilots; two figures in the abstract recomputed from the data after a first draft misstated them.
- **2026-09-24** — pilot-3 (Haiku 4.5) added: one task with a clean content effect, one note-caused over-application, weaker routing; two instrument notes.
- **2026-09-24** — pilot-4 added: the instrument correction holds, the red-tests observation is withdrawn, the cost overhead is confirmed.
- **2026-09-24** — §4.3 corrected: the ceiling is attributed to the task design (facts adjacent to the code, hints in prompts), not to real repositories; pilot-5 with distance levels L1 and L2 added.
