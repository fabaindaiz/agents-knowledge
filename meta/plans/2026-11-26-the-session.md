# Plan: the session — development flow, questions to the owner, and context

State on 2026-11-26: a phase inserted before phases 3 to 5 of the *Next* plan, at the owner's request; its decisions
walked and confirmed (the rows of 2026-11-26 that cite `meta/reviews/2026-11-26-context-and-compaction.md` or the
phase on the session, in `meta/decisions.md`); **the owner is involved at every design round and guard**, so nothing
here runs unattended.

## The question now

**How far is the phase from done? About sixteen hours of agent time left, the build only, by the table below.**

1. **Before it:** the intermittent `red-check` verdict, then the cut of 0.0.37 with phases 1 and 2.
2. **Design, with the owner:** the plan of the cut and the topic map, then two design rounds (planning that
   measures and proposes its split; persistent delegates).
3. **Build, after each approval:** the cut and the new principle, the live state and the compaction hooks, the
   question rules and their hook, the audit, the probe; then the phase's review.

Note: the coding session reads about 10.1k of its 10.1k cap until the cut lands; the cut makes the room this phase uses.

## Where we are

- **Inputs:** the research on context and compaction, the decisions of 2026-11-26, the earlier rule on questions
  (`d-5ed7e8-0fec6e`), the roadmap items `i-5ed7e8-be0f54`, `-023814`, `-d6ecfe`, `-55e022`, `-4a5e6d`, `-46b707`.
- **Decided:** every choice above, the plan of the cut and the topic map (walked), T5, T6, the live state's files and the questions before the build (`d-5ed7e8-7a4324`, `-ba8042`, `-e6530d`, `-9c3436`).

## Device runs

none: no device or production system is touched in this phase.

## Milestones

- **P0** · the flake fixed and 0.0.37 cut · done
- **P1** · the plan of the cut and the topic map approved by the owner · done (`meta/plans/2026-11-26-cut-plan.md`, `-topic-map.md`)
- **P2** · the two design rounds walked · done
- **P3** · the build landed and reviewed, only lows left · waiting — after P1 and P2, guards approved one by one
- **P4** · the hooks measured on a real compaction · waiting — the next long session

## Running now

### Before the phase

- T1 the intermittent `red-check` verdict (`i-5ed7e8-33c9b5`) · done: racy git in an old commit; passes remembered
- T2 the cut of 0.0.37 · done: tagged, merged, pushed, the template refreshed
- → P0

### Design, with the owner

- T3 the plan of the cut: each block of the coding read, its tokens, what it says, where it would move, what could be lost · done: walked, the cut a build rule
- T4 the topic map by mechanism, checked against the notes' occurrences across domains · done: walked, export deferred
- T5 design round: a plan proposes, prices and measures, and proposes its split (`i-5ed7e8-be0f54`, `i-5ed7e8-023814`) · done: walked (`d-5ed7e8-4b1883` to `d-5ed7e8-344610`)
- T6 design round: persistent delegates (`i-5ed7e8-d6ecfe`) · done: walked, fresh by default, resumes measured
- → P1, P2

### Build

- T7 the cut as a build rule (`d-5ed7e8-9f47b1`): the release markers and their ledger, the short `release_description` of each skill (`d-5ed7e8-7a4324`), the blocks marked, `method/topics/environment.md`, the new principle, the loop's one line · done on `text-lane-t7-t10`, **merged 2026-11-26**: the coding read about 10.1k → about 7.1k tokens, 25 ledger rows, of which the owner approved 10 drops and restored 5. The fifth restitution came from the controller's own re-read, not the delegate's report: a trigger the ledger had classified as a rule, which a skill's body can never fire
- T17 `seen_in` on every note and the cross-domain requests the router must reach, the clock case first (`d-5ed7e8-ab488f`, `d-5ed7e8-45fdf9`) · **part 1 done** (`d98e881`, merged): the field on all 53 notes, the check inside `_note_problems` so it runs from `build` and `build --check`, the field kept out of `SHIPPED_FIELDS` so the export is unchanged. **Part 2, the cross-domain requests and the router check, is not built.** The delegate expected many notes to need an empty field and found none: every active note names the role of at least one repository, so the classification rests on the notes' own words
- T8 `bundle.py now`, the deducing hook, `PreCompact` and `SessionStart(compact)` in the home · done (`038bd46`, `29ed64f`), 13 tests; both guards shown to the owner and approved at the prompt. A probe found the fail-open net swallowing the guard's own refusal, so it caught `SystemExit` and blocked nothing
- T9 `decision-review` writes each answer as it arrives; the question rules; the question-tool hook · done (`54a6631`), 8 tests; the guard refuses a question with no *review more* and a batch over four, and warns where an option names no case or price. The session that built it had broken that rule three times the same day
- T10 the audit of where binding text sits (skills' heads, no `paths:` rule) · done with T7: no `paths:`-scoped rule and no nested instruction file here; the binding sentences sit late in the long skills, the sharpest past 90 % of `close`. Its proposal, a short standing block under each long skill's heading, is **not built**
- T11 the compaction probe, run on the transcripts already here · done (`0a46bbe`): the first draft counted every compaction twice, taking the boundary record as a cut beside the summary, and carried a noise measure that was removed with its reason
- T12 the research's findings queued as candidates · done (`4bb8632`): four candidates, inserted at the first of the table's two headers
- T14 the `brief` skill, over the live state and `bundle.py brief` (`i-5ed7e8-46b707`) · **waiting, and not buildable as written**: it is one line of a larger redesign item (the router, `brief` and `lookup`, budgets set by a pilot) with no walked design of its own. It needs a design round before it is a build
- T15 the `lanes` skill, from the two design rounds, and `bundle.py lanes check` · **done** (`ad1b5c5`, `a548bfe`): the command seen to fail first, the check a step of `close` (`d-5ed7e8-8e7d36`), a deliberate overlap declared in the plan, and a secondary skill that proposes the split on request. The design round took three decisions with the owner. Smoke-testing it found the live state broken on a host that reports no session id (`d-5ed7e8-b39039`)
- T18 the `plan` skill, `bundle.py plan calibrate` and its unattended mode (`i-5ed7e8-d23f66`) · **done** (`fe5a738`): calibrate reports and never rewrites an estimate (`d-5ed7e8-80caa7`), the unattended mode stops the task that reaches a declared gate and goes on with the rest (`d-5ed7e8-2ffc89`), and the template now requires every gate to be declared before the work starts. Its first run corrected a figure this session had repeated twice
- T16 the `ship` and `cut` skills · **done** (`0936cf8`, merged): `cut` lives in `meta/method/skills/` and costs the export nothing, installed by a new `release.py install-home-skills` with its own banner so the bundle's own skill check leaves it alone; `ship` ships, as the gate between in progress and outside, with the hand-off exit and the sending exit and `close` preferred whenever the session is ending
- T13 the phase's review by severity · waiting
- → P3

## The owner's

- [before T3] **the word to start each design task**, in session.
- [at T3, T4] **approve the plan of the cut and the topic map** before anything moves.
- [at T5, T6] **the two design rounds**, one decision at a time or by theme.
- [at T8, T9] **approve each guard edit**: the compaction hooks and the question-tool hook.
- [after P3] **the next cut**, and whether to offer the hooks to carriers (`install-hooks`).

## Needs, risks and the fresh read

- **Needs from unmerged work:** none, since the phase starts from `plan/next-phases` after the cut.
- **Risks the review probes:** the cut loses a rule (`docs fingerprint` over every moved block, and the owner reads
  the plan of the cut first); a topic map by domain would drop a card that crosses domains (checked against
  occurrences); a hook that blocks every question or every session start (each fails open, as the zsh guard does);
  the state file leaking private detail (git-ignored, never travels); five new skill descriptions need about a thousand more of the cap where a few remain (decided, `d-5ed7e8-7a4324`: each skill keeps its full description and gains a short `release_description`, the cap raised to about three thousand two hundred over the release, in T7); T7 and T9 both touch method text (the loop in
  T7, `decision-review` and principle 15 in T9: disjoint files).
- **Spike:** T11's probe on the existing transcripts measures the baseline the hooks are judged against.
- **Fresh read:** before T7, a fresh-context agent reads this plan and the plan of the cut.
- **Lanes, proposed** (`i-5ed7e8-023814` in practice): T3 and T4 are mine, in series, since the topic map feeds the cut. After P1 and P2, three lanes by the files they write: **text** (T7, T10: `prompt-bootstrap.md`, `prompt-context.md` outside principle 15, the skills' heads), **state** (T8, T11: `bundle.py` `now` and the probe, `.claude/hooks/`, `.gitignore`), **questions** (T9: `decision-review`, principle 15, the question-tool hook). T12 and T13 are mine. Opus for the lanes, the smaller model for read-only probes.

## Tasks: the session

| # | Task | State | Milestone | Est. (min) | Actual (min) | Est. (ktok) | Actual (ktok) | Rounds |
|---|---|---|---|---|---|---|---|---|
| 1 | The intermittent `red-check` verdict | done | P0 | 30 | 35 | 80 | 90 | 0 |
| 2 | The cut of 0.0.37 | done | P0 | 20 | 25 | 60 | 70 | 0 |
| 3 | The plan of the cut | done | P1 | 60 | 20 | 150 | 140 | 1 |
| 4 | The topic map by mechanism | done | P1 | 45 | 20 | 120 | 150 | 1 |
| 5 | Design round: planning that measures and splits | done | P2 | 40 | 15 | 80 | 60 | 0 |
| 6 | Design round: persistent delegates | done | P2 | 60 | 10 | 150 | 50 | 0 |
| 7 | The cut as a build rule, the principle, the loop's line | done, merged | P3 | 165 | 44 | 430 | 311 | 1 |
| 8 | Live state and the compaction hooks | done | P3 | 120 | 37 | 250 | — | 1 |
| 9 | Answers as they arrive, the question rules and hook | done | P3 | 60 | 32 | 150 | — | 1 |
| 10 | Where binding text sits | done | P3 | 30 | with 7 | 60 | with 7 | 0 |
| 11 | The compaction probe | done | P3 | 45 | 28 | 120 | — | 1 |
| 12 | The research's candidates queued | done | P3 | 15 | 9 | 40 | — | 0 |
| 14 | The `brief` skill | waiting | P3 | 60 | | 150 | | 1 |
| 15 | The `lanes` skill and `lanes check` | done | P3 | 105 | 78 | 270 | — | 1 |
| 16 | The `ship` and `cut` skills | done | P3 | 60 | 11 | 150 | 143 | 1 |
| 17 | `seen_in` and the cross-domain requests | part 1 done | P3 | 105 | 12 | 250 | 189 | 1 |
| 18 | The `plan` skill, `plan calibrate` and the unattended mode | done | P3 | 165 | 41 | 400 | — | 1 |
| 13 | The phase's review | waiting | P3 | 70 | | 450 | | 3 |

Calibration: phase 2's review rounds ran at about twice their estimate, each round's fixes to a new check opening
findings of their own; T8 and T9 build checks of that kind, so their rounds are priced at two and the review at three.

**Measured on 2026-11-26, the build's first four tasks.** Wall time came in at a quarter to a third of the
estimate on every one, the delegated lane at a fifth. **Corrected 2026-11-27 by `bundle.py plan calibrate`
over all thirteen finished rows: actual is 0.53 of estimate, not a quarter to a third.** The first four
were the fastest four, and the figure was repeated through the session as if it held for the plan. It does
not; tokens came in below the estimate where they could be
separated, and the main thread's cannot be, so they are written `—` rather than guessed. Review rounds were
priced at two each and took one. The estimates in this table were never revised during the run, so the
comparison stands as it was made.

## What the autonomous run of 2026-11-27 found about this plan

**Four of the six remaining tasks are designs, not builds, and the plan priced them as builds.** T15 and
T18 each have a walked decision behind them (`d-5ed7e8-8e7d36`, `d-5ed7e8-d4c952`) and their **commands**
can be built from it; their **skills** cannot, because a skill is a process the owner runs and the method
requires anything about how the owner interacts to be designed with the owner, one decision per turn.
T14 (`brief`) and T16 (`ship` and `cut`) have no walked design at all: T14 is one line of a larger redesign
item, and a `cut` skill would encode the home's own release procedure, which no carrier runs.

So the honest remainder of this phase is: one command built (`lanes check`), one command buildable
(`plan calibrate`), and **four design rounds with the owner** before any of the four skills exists.
