# The bundle in real sessions: its share of what a session reads, and how often it is consulted

2026-11-26, at the owner's request, under `d-5ed7e8-7b6df4` (usage evidence enters a record only through a
step the owner runs, already generalised, with the raw figure shown to the owner alone and the approval
naming the record). Two named questions, answered from the local session transcripts of this one machine:

1. **What share of what a real session reads is the bundle's?**
2. **How often does a real session actually consult the knowledge base?**

Everything below is **observational**. No session was run twice, so nothing here says whether the bundle
helps; it says what it costs and how much of it is used. The pilots in `evals/` remain the only evidence
about benefit.

## What was read

Twenty-two sessions, in repositories that carry the bundle, on one machine, excluding this repository's own
sessions — a home works *on* the bundle, so its share would measure the wrong thing. One owner's
repositories, so for admission they are **one source** (`sources/README.md`). Transcripts are never
committed and nothing read is quoted here; only counts leave them.

## How an operation is attributed, which is the discussable part

Each tool call is read for the paths it names. A call counts as the bundle's when it names a path under
`.agents/`, or runs the carrier's tool. Within that: the **knowledge base** (`.agents/knowledge/`), the
**tool** (the gate), or the rest of the release. The same calls are counted twice over, once by count and
once weighted by the bytes the call returned, because a single index read returns about six thousand
tokens while a gate run returns four lines: counting operations alone would make the gate look large and
the knowledge small, and it does.

## What it found

| | By operation | By bytes returned |
|---|---:|---:|
| The bundle, all of it | about 13 % (median session) | **about 9 % (median session)** |
| — the gate | about four fifths of that | about 5 % (median); about 7 % pooled over all sessions |
| — **the knowledge base** | about a twelfth of that | **about 1 % (median), at most about 15 %** |

Every other cell in the table is a median over sessions; the gate's share by bytes is the one that
reads differently in each form, so both are given. Reproduced by `bundle.py usage measure` on the same
machine: median by operation 12 %, by bytes 10 %, knowledge by bytes 0.8 % (at most about 15 %), the gate
5.7 % median and 7.1 % pooled, and the same fifteen of twenty-two sessions consulting. Counts drift by a
few operations between runs, since other sessions append to their transcripts while the command reads
them; the ratios do not move, but a figure sitting on a fraction's edge can change the generalised
wording between two runs of the same day.

**Two sessions in three opened the index or a card at least once** (fifteen of twenty-two). The spread
between sessions is wide: the bundle's share runs from none at all to about three quarters of a short
session's file traffic.

So a real session consults, but consults **little**: the knowledge base is around one per cent of what
comes back into context, and most of the bundle's presence is the gate running.

## It is the second such measurement, not the first

A profile of 2026-10-05 already answered a neighbouring question and is recorded in the roadmap: the
bundle's share of a session was **about one sixtieth in sessions that consult it, and about one
seventy-fifth overall**. That measure takes a whole session's tokens as its denominator; this one takes
what file-naming tool calls returned, which is a far smaller denominator, so about nine per cent here and
about two per cent there are not in conflict — they are the same small footprint seen against two
different totals.

What the two together support, and neither does alone, is the direction: **the knowledge base is a small
part of what a real session spends, and the gate is the larger part of the bundle's presence.** A third
measurement that reconciled the two denominators explicitly would be worth more than either.

## What this does to what the project claims

The pilots attribute nearly all of the measured ×2 to the agent opening the index "on nearly every task,
relevant or not" (`evals/REPORT.md`). In real work the knowledge base is about one per cent of returned
bytes. Either synthetic tasks provoke consultation far more than real work does, or the wiring that
consults only on state, a contract, data, security or verification works better than a pilot can see.
Both readings are good news for the cost, and neither was measured until now. Neither replaces a pilot:
without a counterfactual this says nothing about ×2 itself, only about the denominator it is taken over.

## What it does not answer, and what would make it stronger

- **Bytes returned are not tokens**, though they are roughly proportional (about four characters each).
- **The always-loaded wiring is not in it**: about 490 tokens a turn, plus the root instruction file, never
  appear as a tool result. The figures are the *read* cost, not the whole cost.
- **No counterfactual.** Nothing here is evidence of benefit or of harm.
- **One machine, one owner, twenty-two sessions**, and the attribution rule above is a judgement that a
  second reader should check before the figure travels.
- **Stronger would be**: the same measure on a second owner's machine; the wiring counted; and the measure
  repeated after the read was cut from about 10.1k to about 7.1k tokens, which happened the same day and is
  not yet reflected in any of these sessions.

**Not yet in `evals/REPORT.md`.** The owner's ruling of 2026-11-26: this review first, and the generalised
sentence enters the report only once the measure is repeatable as a command and has run a second time.
