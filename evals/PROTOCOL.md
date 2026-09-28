# Does the bundle change what an agent does? — experiment protocol

**Pre-registration for roadmap item `i-5ed7e8-0d9b6a`.** This file is written, and committed, before any
confirmatory data exist. Every later change is appended to *Deviations* with its date and reason; nothing
above that section is edited after the first confirmatory trial runs.

This directory is not part of the bundle. It lives at the repository root, does not travel to carriers,
and is not listed in the bundle's `SHA256SUMS`.

## The question

The bundle claims that its knowledge notes change an agent's decision where the textbook answer is wrong.
Three controlled studies of repository context files found no reliable gain in task success and a cost
increase of about a fifth (Gloaguen et al. 2026, arXiv 2602.11988; Khatri 2026, arXiv 2607.27250), or an
efficiency gain with correctness unmeasured (Lulla et al. 2026, arXiv 2601.20404). One ablation found
curated skills no better than length-matched irrelevant text (arXiv 2607.07504); another found focused
skills clearly better than none (SkillsBench, arXiv 2602.12670). The prior is therefore a small effect or
none, and a real cost.

None of those studies can answer the bundle's claim, for reasons this design corrects:

| Weakness in the prior studies | What this protocol does instead |
|---|---|
| Tasks are bug fixes judged by tests that encode no design judgment, so a note could only help by accident | Tasks are built so that the judgment *is* the outcome, and the hidden tests check its consequence |
| No placebo: "more context" cannot be separated from "this content" | Two placebo arms: the bundle with only the relevant notes removed, and an irrelevant note of matched length in the always-on channel |
| No oracle: a null cannot be split into "the content does not help" and "the agent never found it" | An oracle arm, and a read trace per trial |
| One run per task and condition, or order fixed | Several repetitions, randomised and interleaved order, the task as the unit of analysis |
| Power not computed, or computed after the fact | Sample size fixed from a pilot before the confirmatory run; the minimum detectable effect is reported |
| Only helpful cases | Boundary tasks, where applying the note is the mistake, and neutral tasks, where no note applies |
| Configuration of the experimenter leaks into every arm | A clean configuration directory, a workspace outside every repository, a sandbox with no network and no home directory |

**Scope.** What is tested is the knowledge base as a carrier routes to it: an `AGENTS.md` that sends the
agent to `.agents/knowledge/INDEX.md`. The method's session loop, the paste-in invocations and the skills
are not under test here. The claim that can come out of this experiment is conditional: *on a task where
a note applies, does carrying the bundle change the outcome, and is it the note's content that does it?*
How often a note applies in real work is a different question, and this design does not answer it.

## Hypotheses

| Id | Contrast (A − B) | Family | Prediction if the bundle works as claimed | Role |
|---|---|---|---|---|
| H1 | `bundle` − `ablated` | judgment | positive | **primary**: the content, with the length, structure and routing held fixed |
| H2 | `bundle` − `minimal` | judgment | positive | the effect of carrying the bundle, as a carrier does |
| H3 | `oracle` − `oracle_placebo` | judgment | positive | the content, when it is certainly in context |
| H4 | `oracle` − `bundle` | judgment | ≥ 0 | what routing loses |
| H5 | `minimal` − `none` | judgment | ≈ 0 | replication of the prior studies' null for a minimal file |
| H6 | `bundle` − `ablated` | boundary | ≥ 0, within the margin | the note is not over-applied |
| H7 | `bundle` − `minimal` | boundary | ≥ 0, within the margin | the bundle does no harm where the note's boundary holds |
| H8 | `oracle` − `oracle_placebo` | boundary | ≥ 0, within the margin | over-application when the note is certainly read |
| H9 | `bundle` − `minimal` | neutral | within the margin | no harm on ordinary work |
| C1 | `bundle` / `minimal`, cost, turns, tokens, time | all | reported, no prediction | the price |

## What each pattern means

This table is the answer to "if there is an improvement, is it the context?". It is fixed now so that the
reading cannot be chosen after the numbers are seen.

| Pattern | Reading |
|---|---|
| H1 > 0 | the content of the notes changes outcomes, with everything else about the bundle held equal |
| H1 ≈ 0, H2 > 0 | carrying a large bundle changes outcomes, but not through the relevant note: priming, extra care, extra tokens. The notes are not what works |
| H1 ≈ 0, H3 > 0, H4 > 0 | the content helps when read, but the agent does not find it: the routing (index, `AGENTS.md`, skills) is the defect, which bears directly on packaging the method as skills |
| H1 ≈ 0, H3 ≈ 0 | the content does not change this model's decisions even when certainly in context: the notes are not useful to it, or it already knows them (check the `none` baseline) |
| H6, H7 or H8 < 0 | the note is over-applied past its stated boundary: the boundary section does not do its job |
| H9 < 0 or C1 high with H1 ≈ 0 | the bundle costs more than it returns on ordinary work |
| `none` passes a judgment task in every pilot repetition | the note fails its own admission criterion 1 ("an agent would get this wrong without it") for this model; recorded against the note |

A difference smaller than the minimum detectable effect is **not** evidence of no effect. A null is stated
only as a bound: "the effect is within ±10 percentage points" when the equivalence test (TOST) supports it,
and otherwise "not detected, and effects below the MDE could not have been".

## Conditions

Every arm starts from the same repository. Arms other than `none` add an `AGENTS.md` and a one-line
`CLAUDE.md` that imports it (`@AGENTS.md`, the bridge `sources/layout.md` documents).

| Arm | `AGENTS.md` | `.agents/` | What it isolates |
|---|---|---|---|
| `none` | absent | absent | the unaided agent |
| `minimal` | the repository's test command, two lines | absent | the realistic baseline every other arm is built on |
| `bundle` | `minimal` plus a routing paragraph to `knowledge/INDEX.md` | the whole bundle | the treatment, as a carrier holds it |
| `ablated` | identical to `bundle` | the bundle with the task's target notes deleted, and every line that names them removed (about 1% of its size) | the placebo for H1: same length, structure, method and routing |
| `oracle` | `minimal` plus the target notes' full text | absent | the content, certainly in context |
| `oracle_placebo` | `minimal` plus one irrelevant note | absent | the placebo for H3 |

The placebo note is chosen by a mechanical rule, so the experimenter does not choose it: the active note
from the other knowledge area whose text length is closest to the target notes' combined length
(`harness.py`, `pick_placebo`). The pilot's placebos are within 3% of their targets' length.
*Amended 2026-09-25: what the `bundle` arm carries, and how it is identified, from release 0.0.22; see
Deviations.*

Neutral tasks run `none`, `minimal` and `bundle` only.

## Tasks

### Families

- **Judgment.** A realistic request in a small repository, where a plausible, textbook-shaped solution
  passes the visible tests and violates a requirement the repository itself states. The hidden tests check
  the consequence (a customer charged once, a field another service owns left intact), never the wording or
  the technique.
- **Boundary.** A request where one note's *When it does NOT apply* holds: applying the note is the mistake,
  and the hidden tests check the consequence of not applying it.
- **Neutral.** Ordinary work that no note bears on.

### The rules every task meets

1. **The requirement is the repository's, not the note's.** A reviewer who has never seen the bundle,
   given only the task's repository, prompt and hidden tests, must agree that the tested behaviour follows
   from what the repository states. The argument is written in the task's `fairness` field, and a task no
   reviewer accepts is withdrawn before the confirmatory run.
2. **The prompt names no technique and no failure.** It is written as a request a colleague would make.
3. **The hidden tests have been seen to fail and to pass.** `harness.py check` requires that they fail on the
   starting state and on a `naive/` overlay (the plausible wrong answer), pass on a `reference/` overlay,
   and that the visible tests pass on the start and the reference.
4. **The naive answer is not a strawman.** It is the answer the `none` arm produces in the pilot, or
   something as plausible; a task whose naive overlay the pilot never produces is reviewed.
5. **Synthetic and public.** No task is derived from a private repository, and none restates an occurrence
   written in a note: a note's own origin would make the task in-sample.
6. **Frozen by hash.** The plan records each task's tree hash, and `run` refuses a task that changed.

### Authorship and the conflict of interest

The bundle's maintainers are evaluating their own bundle, and the pilot's tasks were written by an
assistant session that had read the notes. For the confirmatory set:

- tasks are written from each note's `claim` and boundary only, by an author who does not open the note's
  body, and preferably by someone who does not maintain the bundle;
- the fairness review (rule 1) is done by a reviewer, human or a model from another family, who never sees
  the bundle;
- which notes get tasks is decided by a rule, not by preference: every active note whose claim a hidden
  test can check in a small repository, listed here before tasks are written, with the notes left out and
  why;
- the set, the list and this protocol are committed before the first confirmatory trial.

### Sizes

| Family | Confirmatory target | Why |
|---|---|---|
| judgment | 30 tasks | 80% power for a 20 pp effect at 3 repetitions (see *Sample size*) |
| boundary | 10 tasks | enough to see over-application of 20 pp or more; H6 to H8 are secondary |
| neutral | 10 tasks | cost and harm on ordinary work |

At most two tasks per note, so no note carries the result; tasks that share a note are one cluster in the
bootstrap.

## The agent

- Claude Code in print mode, one session per trial, the model and effort fixed in the plan; the CLI version,
  model id and bundle digest recorded in `plan.json`, and the init event of every session kept.
- **Isolation.** A dedicated configuration directory (`CLAUDE_CONFIG_DIR`) holding credentials only — no
  `CLAUDE.md`, rules, skills, agents, plugins or settings, checked before every run; auto memory off; the
  environment rebuilt from an allowlist; the workspace a fresh copy under the system temporary directory,
  with no instruction file and no repository above it; no git history but one starting commit.
- **Sandbox.** Bash runs in Claude Code's sandbox, which must start (`failIfUnavailable`), with no network and
  no read of the home directory; Read and Edit are allowed inside the workspace only; web tools are denied.
  Any access outside the workspace is logged per trial and listed in the report.
- **Tools.** Bash, Read, Edit, Write, Glob and Grep. No subagents, MCP servers or skills, in every arm.
- **Limits.** 60 turns and 30 minutes per trial, the same in every arm.
- **Manipulation check.** `harness.py probe` asks one tool-less session per arm to list the headings of the
  instructions it received; it runs before the pilot and before the confirmatory run, and its answers are
  kept.

## Procedure

1. **Pilot** (exploratory, never reported as a result). The four tasks in `tasks/`, every arm, two
   repetitions. It validates the harness end to end, measures cost per trial, estimates the baseline rates
   and the variance of per-task differences, and shows which naive answers the agent actually produces.
2. **Size.** `power.py`, with the baseline distribution fitted to the pilot, fixes the number of judgment
   tasks and repetitions. The result is written under *Deviations* before the confirmatory tasks exist.
3. **Calibration** on the `none` arm only, with its own seeds, never on the arms being compared. A judgment
   task the `none` arm passes in every calibration run is set aside: it is reported, with its note, as
   evidence against the note's admission criterion 1, and it is excluded from H1 to H5.
4. **Confirmatory run.** `harness.py plan` freezes the schedule (randomised and interleaved: within each
   repetition, every task-arm pair appears once in shuffled order), the settings and the hashes. The
   repository must be clean at the commit that holds this protocol and the tasks.
5. **Analysis.** `analyze.py`, unchanged from the commit in step 4. Anything computed beyond it is labelled
   exploratory in the report.

## Outcomes

- **Primary:** the hidden tests pass on the final state of the workspace (`success`), whatever the exit
  reason.
- **Secondary:** the repository's visible tests still pass; `pass^k` (every repetition passes).
- **Cost:** `total_cost_usd`, turns, output tokens and wall time from the session's result event.
- **Process:** whether the index and the target notes were read; any access outside the workspace.

## Analysis plan

- **Unit.** The task. Repetitions are averaged per task and arm; every contrast is the mean over tasks of
  the paired per-task difference (Miller 2024, arXiv 2411.00640).
- **Primary test.** H1 with a two-sided sign-flip randomisation test on the per-task differences (exact
  up to 16 tasks), a 95% t interval, and a 95% bootstrap interval that resamples clusters of tasks sharing
  a note. α = 0.05.
- **Secondary.** H2 to H9 with the same statistics, Holm-corrected as one family.
- **Equivalence.** TOST with a margin of ±10 percentage points, used for every "no effect" or "no harm"
  statement.
- **Minimum.** A contrast over fewer than 8 tasks, or with no variation at all, is described and not
  tested: no interval, no p-value, no equivalence claim.
- **Cost.** The geometric mean over tasks of the ratio of per-task means, with a bootstrap interval.
- **Exclusions.** Only infrastructure failures: a trial with no result event and no tool call (the session
  never ran). It is re-run once; each one is listed in the report. Nothing is excluded for an outcome.
- **Sensitivity.** H1 again with a timeout or an error exit counted as a failure.
- **Exploratory, labelled so.** Success in `bundle` split by whether a target note was read — correlational,
  since the agents that read it may differ; H3 is the causal version.

## Sample size

`python3 evals/power.py` with its default U-shaped baseline (Beta(0.6, 0.6)) and a per-task effect
spread of 10 pp, α = 0.05, paired t-test:

| Effect | Repetitions | 10 tasks | 20 tasks | 30 tasks | 40 tasks | 60 tasks |
|---:|---:|---:|---:|---:|---:|---:|
| 10 pp | 3 | 0.11 | 0.19 | 0.30 | 0.40 | 0.54 |
| 20 pp | 3 | 0.27 | 0.60 | 0.79 | 0.89 | 0.97 |
| 20 pp | 5 | 0.45 | 0.78 | 0.93 | 0.98 | 1.00 |
| 30 pp | 3 | 0.51 | 0.89 | 0.97 | 0.99 | 1.00 |

So the design detects an effect of about 20 percentage points, not 10. That matches the question: a note
that changes a decision should change it often. A smaller true effect can be missed, and the report says so
in its MDE column. The pilot replaces these assumptions with measured ones.

Trial count at the targets: judgment 30 × 6 arms × 3 repetitions = 540; boundary 10 × 6 × 3 = 180;
neutral 10 × 3 × 3 = 90; about 810 trials. Their cost is measured in the pilot before the run is approved.

## Stopping and deviations

- No interim look at a contrast. The run stops early only for an infrastructure problem, and then resumes
  from the frozen plan.
- A change of model, CLI version or bundle digest in the middle of a run voids the run: a new plan is
  written, and both are reported.
- Every deviation from this protocol is appended below, dated, with its reason, and repeated in the report.

## Threats to validity

| Threat | Mitigation | What remains |
|---|---|---|
| The maintainers evaluate their own bundle | pre-registration, mechanical placebo and note selection, blind fairness review, tasks by another author | the tasks still come from the notes' claims: the result is conditional on relevance |
| Synthetic, small repositories | realistic requests, stated requirements, naive answers taken from the pilot | a real repository offers more distraction and more competing documentation |
| One agent, one model | recorded; the harness takes the model as a parameter | the result holds for that model and version only |
| The routing tested is one paragraph in `AGENTS.md` | the same paragraph in `bundle` and `ablated` | a carrier's fuller `CLAUDE.md` or the paste-in invocation might route better or worse |
| The ablation also removes lines of other notes that name a target | counted per trial (`prepared.ablation`) | about 1% of the bundle differs besides the target notes |
| The always-on channel in `oracle` is stronger than on-demand reading | H4 measures exactly that gap | — |
| Grading by hidden tests misses quality | the primary claim is about consequences, which tests can check | style, clarity and design quality are not measured |

## Reporting

The report is `analyze.py`'s output plus a written reading, and it includes: every trial, including
timeouts and error exits; the per-task table; each contrast with its interval, p-value, MDE and equivalence
verdict; cost; the manipulation and contamination checks; every deviation; the tasks set aside at
calibration and the notes they bear on; and this section's threats. Results are written as rates and
ratios. Transcripts stay in the run directory, which is not committed.

The verdict feeds the bundle through its own channels, not by editing it: a note's `confidence` moves by
the knowledge base's lifecycle (`sources/README.md`), and anything that changes the method goes
to `meta/roadmap.md` or `meta/tracking/candidates.md`.

## Deviations

- **2026-09-24, pilot only — configuration isolation.** No separate login or API key was available, so the
  pilot reuses the machine's logged-in configuration (`--config-dir default`) with user settings excluded
  (`--setting-sources project,local`), skills disabled and auto memory off, instead of a dedicated clean
  configuration directory. The manipulation probe run before the pilot showed the `none` arm receiving no
  instructions at all, the user-level instruction file included, and every other arm receiving exactly its
  own. The confirmatory run uses a clean directory, or this mode only with the same probe result recorded.
- **2026-09-24, pilot stage — task difficulty.** The first pilot tasks stated the decisive fact beside the
  code the agent edits, and some prompts hinted at the answer; the unaided frontier model then passed
  every judgment trap. Rule 1 (the requirement belongs to the repository) stands, and a sixth task rule is
  added: **the decisive fact is not adjacent to the edited code and the prompt does not hint at it.** Each
  judgment trap is built at two distances: L1, the fact only in code, in another module, with no prose;
  L2, the fact only in documentation or configuration elsewhere in the repository, among distractors.
  The original tasks are kept as L0 and reported separately. The confirmatory set uses L1 and L2.
- **2026-09-25 — scope of this study.** The tasks this protocol prescribes are written from the notes'
  claims, and the hidden tests check those claims, so the study measures instruction transfer: whether a
  note's content reaches a decision where it applies. It cannot say whether carrying the bundle changes
  an agent's performance on work in general. That question has its own protocol, `PROTOCOL-general.md`
  (roadmap item `i-5ed7e8-bf5663`), with tasks from external benchmarks. Nothing in this protocol changes.
- **2026-09-25 — the bundle from release 0.0.22.** The shipped notes are now short (claim, mechanism,
  boundary, cost). The full note text the `oracle` and `oracle_placebo` arms inject, and that `pick_placebo`
  measures, is read from `sources/notes/`, so the placebo picks and the oracle text are unchanged: checked
  identical for all 26 tasks whose placebo is picked automatically. The bundle is identified by its version
  and the sha256 of `.agents/SHA256SUMS`; `plan.json` keeps that hash under `bundle_digest` and adds
  `bundle_version`. The `bundle` and `ablated` arms' content did change: short notes, cards with a *Not when*
  column, the trigger wording in the invocation, and retired notes and the home's records (roadmap,
  tracking, literature) no longer shipped. A run from now on measures 0.0.22, not the v0.0.21 the pilots
  carried. The hypotheses, arms and analysis are unchanged.
- **2026-09-28, exploratory — pilot-6, the cost smoke test of 0.0.22.** Registered before any trial. It
  measures cost, turns and output tokens only, and claims nothing about efficacy (roadmap
  `i-5ed7e8-c4b9c7`). *Arms:* `minimal`; `bundle` (0.0.22 with the v21 wiring paragraph, `ROUTING`); and a
  new arm, `bundle_v22`, the same bundle with the 0.0.22 wiring (`ROUTING_V22`: consult only when a change
  touches state, a contract, data, security or verification; the card before the note; the repository
  before the note). Both texts are frozen in the plan. *Tasks:* the three that discriminated in pilot-5
  (`contacts-second-source-l1`, `contacts-second-source-l2`, `refund-webhook-l2`), the neutral
  `inventory-csv-export`, and two tasks of a new family, `trivial`, where the 0.0.22 wiring says to
  consult nothing (`cli-help-typo`, `report-label-rename`; both graders seen to fail and pass). The
  pilots' model, two repetitions, the pilots' configuration isolation (`--config-dir default`, degraded,
  as in the first deviation above). *Predictions* (`.agents/CHANGELOG.md` [0.0.22]): `bundle_v22` /
  `minimal` cost at most ×1.2 on trivial tasks (refuted above ×1.4), at most ×1.5 on the others (refuted
  above ×1.8), and the three discriminating tasks still passed under `bundle_v22`. *Decision rule for
  0.0.23:* at most ×1.5 on the others, and the phased session is designed for adherence and verification,
  its review optional on small changes; above ×1.8, and the review in a subagent becomes the default path.
  *Directive adherence* (`i-5ed7e8-a2f016`) is counted on the same transcripts: bundle reads per arm and
  task group, and whether the final report mentions a check. Analysis: `evals/cost_smoke.py`.
- **2026-09-28, exploratory — pilot-7, the cost of the 0.0.23 candidate.** Registered before any trial, as
  pilot-6 was, on the same six tasks, model, repetitions and isolation. *Arms:* `minimal` and a new arm,
  `bundle_v23`: the release candidate with the 0.0.23 wiring (`ROUTING_V23`: reviews go to the
  `knowledge-reviewer` subagent, installed in the workspace's `.claude/agents/` as the bootstrap installs it).
  **Every arm has the subagent tool**, as a carrier's session has it, so the tool alone does not separate the
  arms; the tool list is frozen in the plan. *Predictions* (`.agents/CHANGELOG.md` [0.0.23]): `bundle_v23` /
  `minimal` cost at most ×1.2 on trivial tasks (refuted above ×1.4), at most ×2 on the others (refuted
  above ×2.3), and the three discriminating tasks passed at least 4 of 6 times (refuted at 3 of 6 or fewer).
  *Decision:* refuted, and the candidate is not tagged until the cause is found and fixed; holding, it is
  tagged after the adversarial review. Analysis: `evals/cost_smoke.py`.
- **2026-09-28, pilot-7 as run.** Two rounds of fixes were built into `.agents/` during the run, and the
  harness copied the live bundle into each workspace: six of the eight `bundle_v23` trials on the
  non-trivial tasks ran on the frozen candidate (`420ac5200289`), two on a later build. Reported apart in
  `REPORT.md` §4.9; the verdict is the same over both. From this date the harness records each trial's
  bundle digest and refuses a trial whose bundle is not the plan's.
- **2026-09-28, exploratory — pilot-8, the changed 0.0.23 candidate.** Registered before any trial, on
  pilot-7's six tasks, model, repetitions, isolation and tools (the subagent tool in every arm), with a new
  seed. *Arms:* `minimal` and `bundle_v23b`: the candidate changed after pilot-7, whose wiring
  (`ROUTING_V23B`) has the author look the change up in the index and open only the cards it links, and
  run the `knowledge-reviewer` subagent, installed as in `bundle_v23`, only when asked; the task prompts
  never ask. *Predictions* (`.agents/CHANGELOG.md` [0.0.23], unchanged from pilot-7 but for the fourth):
  cost at most ×1.2 on trivial tasks (refuted above ×1.4) and at most ×2 on the others (refuted above
  ×2.3); the three discriminating tasks passed at least 4 of 6 times (refuted at half or fewer); at most
  one of the 12 `bundle_v23b` trials calls the reviewer. *Decision:* holding, 0.0.23 is tagged; refuted,
  it is not, and the result goes to the user before anything else changes.
- **2026-09-28, pilot-8 as decided.** The cost prediction was refuted (×2.34 against a line at ×2.3), the
  other three held. The result went to the user, who decided to tag 0.0.23 anyway, with the refutation
  stated in its changelog: a deviation from the registered decision, taken explicitly. The tagged release
  adds unmeasured wording fixes (`REPORT.md` §4.10).
