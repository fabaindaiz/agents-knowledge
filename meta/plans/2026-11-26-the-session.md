# Plan: the session — development flow, questions to the owner, and context

State on 2026-11-26: a phase inserted before phases 3 to 5 of the *Next* plan, at the owner's request; its decisions
walked and confirmed (the nine rows of 2026-11-26 that cite `meta/reviews/2026-11-26-context-and-compaction.md` or the
phase on the session, in `meta/decisions.md`); **the owner is involved at every design round and guard**, so nothing
here runs unattended.

## The question now

**How far is the phase from done? About fifteen hours of agent time, in three stages, each opened by the owner.**

1. **Before it:** the intermittent `red-check` verdict, then the cut of 0.0.37 with phases 1 and 2.
2. **Design, with the owner:** the plan of the cut and the topic map, then two design rounds (planning that
   measures and proposes its split; persistent delegates).
3. **Build, after each approval:** the cut and the new principle, the live state and the compaction hooks, the
   question rules and their hook, the audit, the probe; then the phase's review.

Note: the coding session reads about 10.1k of its 10.1k cap until the cut lands; the cut makes the room this phase uses.

## Where we are

- **Inputs:** the research on context and compaction, the decisions of 2026-11-26, the earlier rule on questions
  (`d-5ed7e8-0fec6e`), the roadmap items `i-5ed7e8-be0f54`, `-023814`, `-d6ecfe`, `-55e022`, `-4a5e6d`, `-46b707`.
- **Decided:** every choice above; open: what the cut moves, and the topic map, both shown to the owner first.

## Device runs

none: no device or production system is touched in this phase.

## Milestones

- **P0** · the flake fixed and 0.0.37 cut · waiting
- **P1** · the plan of the cut and the topic map approved by the owner · waiting — after P0
- **P2** · the two design rounds walked · waiting — the owner, in session
- **P3** · the build landed and reviewed, only lows left · waiting — after P1 and P2, guards approved one by one
- **P4** · the hooks measured on a real compaction · waiting — the next long session

## Running now

### Before the phase

- T1 the intermittent `red-check` verdict (`i-5ed7e8-33c9b5`) · waiting
- T2 the cut of 0.0.37 · waiting
- → P0

### Design, with the owner

- T3 the plan of the cut: each block of the coding read, its tokens, what it says, where it would move, what could be lost · waiting
- T4 the topic map by mechanism, checked against the notes' occurrences across domains · waiting
- T5 design round: a plan proposes, prices and measures, and proposes its split (`i-5ed7e8-be0f54`, `i-5ed7e8-023814`) · waiting
- T6 design round: persistent delegates (`i-5ed7e8-d6ecfe`) · waiting
- → P1, P2

### Build

- T7 the cut applied with `docs fingerprint`, the new principle, the loop's one line · waiting
- T8 `bundle.py now`, the deducing hook, `PreCompact` and `SessionStart(compact)` in the home · waiting
- T9 `decision-review` writes each answer as it arrives; the question rules; the question-tool hook · waiting
- T10 the audit of where binding text sits (skills' heads, no `paths:` rule) · waiting
- T11 the compaction probe, run on the transcripts already here · waiting
- T12 the research's findings queued as candidates · waiting
- T14 the `brief` skill, over the live state and `bundle.py brief` (`i-5ed7e8-46b707`) · waiting
- T15 the `lanes` skill, from the two design rounds · waiting
- T16 the `ship` and `cut` skills · waiting
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
  the state file leaking private detail (git-ignored, never travels); four new skill descriptions need about 800 characters where 16 remain (the descriptions are trimmed in T7, or the cap is the owner's to raise); T7 and T9 both touch method text (the loop in
  T7, `decision-review` and principle 15 in T9: disjoint files).
- **Spike:** T11's probe on the existing transcripts measures the baseline the hooks are judged against.
- **Fresh read:** before T7, a fresh-context agent reads this plan and the plan of the cut.
- **Lanes, proposed** (`i-5ed7e8-023814` in practice): T3 and T4 are mine, in series, since the topic map feeds the cut. After P1 and P2, three lanes by the files they write: **text** (T7, T10: `prompt-bootstrap.md`, `prompt-context.md` outside principle 15, the skills' heads), **state** (T8, T11: `bundle.py` `now` and the probe, `.claude/hooks/`, `.gitignore`), **questions** (T9: `decision-review`, principle 15, the question-tool hook). T12 and T13 are mine. Opus for the lanes, the smaller model for read-only probes.

## Tasks: the session

| # | Task | State | Milestone | Est. (min) | Actual (min) | Est. (ktok) | Actual (ktok) | Rounds |
|---|---|---|---|---|---|---|---|---|
| 1 | The intermittent `red-check` verdict | waiting | P0 | 30 | | 80 | | 1 |
| 2 | The cut of 0.0.37 | waiting | P0 | 20 | | 60 | | 0 |
| 3 | The plan of the cut | waiting | P1 | 60 | | 150 | | 1 |
| 4 | The topic map by mechanism | waiting | P1 | 45 | | 120 | | 1 |
| 5 | Design round: planning that measures and splits | waiting | P2 | 40 | | 80 | | 0 |
| 6 | Design round: persistent delegates | waiting | P2 | 60 | | 150 | | 0 |
| 7 | The cut, the principle, the loop's line | waiting | P3 | 90 | | 250 | | 2 |
| 8 | Live state and the compaction hooks | waiting | P3 | 120 | | 250 | | 2 |
| 9 | Answers as they arrive, the question rules and hook | waiting | P3 | 60 | | 150 | | 2 |
| 10 | Where binding text sits | waiting | P3 | 30 | | 60 | | 1 |
| 11 | The compaction probe | waiting | P3 | 45 | | 120 | | 1 |
| 12 | The research's candidates queued | waiting | P3 | 15 | | 40 | | 0 |
| 14 | The `brief` skill | waiting | P3 | 60 | | 150 | | 1 |
| 15 | The `lanes` skill | waiting | P3 | 45 | | 120 | | 1 |
| 16 | The `ship` and `cut` skills | waiting | P3 | 60 | | 150 | | 1 |
| 13 | The phase's review | waiting | P3 | 70 | | 450 | | 3 |

Calibration: phase 2's review rounds ran at about twice their estimate, each round's fixes to a new check opening
findings of their own; T8 and T9 build checks of that kind, so their rounds are priced at two and the review at three.
