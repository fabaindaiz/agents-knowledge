# What the bundle makes an agent load, and what it costs

**Date:** 2026-10-07. **Status:** analysis by a delegated agent, read-only, of pilot-9's 36 transcripts and the
reviewer pilot's; bears on release 0.0.30's focus (`d-5ed7e8-7cac23`). Exploratory: two runs per task cell, the
owner's global instructions loaded in every arm, and a cost split that assumes each read is cached once and
re-read on every later call.

## Units

`release.py report` estimates tokens as characters over four. The transcripts show reading the index raised the
next call's cache write by about 9,400 tokens (the split index by about 6,100): about 2.8 characters per token
for this text, so the report runs about 1.4 times low. Below, tokens are measured ones. Each trial's cost is
reproduced exactly by list prices (input 2, one-hour cache write 4, cache read 0.2, output 10, per million).

## Always loaded

| Item | Tokens, about |
|---|---:|
| The pilots' wiring paragraph | 190 |
| A carrier's wiring (knowledge line, privacy, precedence) | 490 |
| The three method skills' descriptions in the listing | 750 |
| The reviewer agent's description | 155 |

The pilots' first-call context grew by about 340 tokens with the bundle, under one percent of a trial's cost. In
a carrier the always-loaded part is about 1,400 tokens per turn, small per session. The pilots did not install the
skills, so the listing was not measured there.

## Loaded on demand, and how often pilot-9 read it (non-trivial tasks, 8 trials per arm)

| Item | Tokens, about | Read |
|---|---:|---|
| The knowledge index | 8,900 | 8 of 8 (`bundle_v29`), 7 of 8 (split); none on trivial tasks |
| An area index | 8,000 to 12,700 | never |
| A card (51 of them) | 330 | about 1.5 per trial |
| A full note | 1,200 | once in all |
| The coding invocation's reads (session loop, standards, privacy principle) | 14,200 | not exercised |
| A method prompt | 7,500 to 45,000 | never |
| A method skill's body | 1,200 to 2,000 | not installed |
| The reviewer (its body and its own index read) | 9,600 | never called |

## Pilot-9: the bundle against `minimal` on non-trivial tasks

The bundle took a trial from about 10.8 to 15 turns and roughly doubled its estimated cost.

- **The extra turns:** reading the bundle about 2.6 (index 1, cards 1.5), searches 0.6, repository reads 0.5,
  edits 0.4. **Test runs stayed at one per trial in every arm**: the bundle added no verification.
- **The extra cost by cause:**
  - the index, written once and re-sent on about seven later calls: about 44% of the extra, a quarter of the
    arm's cost;
  - extra output: about a quarter of the extra (reasoning about 4.5 times longer, the final message about three
    times);
  - cards and the note: 4%;
  - the rest, about a quarter: extra reads and searches, and the base context re-sent on extra turns.
- **The neutral task**, one no note concerns, read the whole index every time and gained nothing: it passed
  without the bundle. The index was about two thirds of its extra.

## The reductions it ranks

1. **A lookup-only index**, action and slug only: about a quarter of today's size, saving about a third of the
   extra, about 18% of the arm's cost (predicted, not measured).
2. **Defer the index until a risk signal** (stored state, retries, merging data, money, authentication), or search
   it for the action instead of reading it whole. Trivial tasks already skip it.
3. **Shorter output after cards**: one line per card checked, reasoning only on cards that apply. It might halve the
   extra output, about 7% of the arm.
4. **Not moving verification into a subagent**: the bundle adds no verification to move. A reviewer call costs
   about twice the whole measured extra, so only a much leaner or cheaper subagent could pay off.
5. **Slimming what every turn pays for.** The coding invocation's reads, if a session makes them, cost about as much
   as the whole measured extra (a projection; the pilots did not exercise them). Moving the session loop into a skill
   loaded on demand saves most of it. Shorter skill descriptions and wiring save under one percent per task, but on
   every task, trivial ones included.

Card size is not worth touching.
