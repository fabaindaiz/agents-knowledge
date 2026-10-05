# What the bundle weighs in real sessions

**Date:** 2026-10-05. **Answers:** `i-5ed7e8-a437c6`. **Status:** measured once, by a prototype kept outside the
repository (to become `evals/session_profile.py`, with its test on a fabricated transcript).

**Prediction, written before it ran (roadmap):** in sessions that consult the bundle its reads are under a tenth of
input tokens, and under a fiftieth over all sessions.

**Method.** The client's transcripts on one machine, main and subagent, about three weeks of them: some sixty-five
sessions with usage, tens of thousands of API calls, about 10^10 input tokens. Numbers only leave the script (no
content, path, project name or prompt; sessions numbered by start time). Input counts input, cache creation and
cache reads once per response. A bundle read is a file-read result on a `.agents/` path or a reading shell command
naming one; its size is characters/4; its *carried share* counts it once per later call until the next compaction
(the primary measure, fixed before the run). "Consulting" is a session with at least one such read.

## Result: confirmed on both halves, with a thin second margin and an unpredicted tail

| Pooled carried share of input | chars/4 (declared) | at the measured rate |
|---|---|---|
| Sessions that consult the bundle | about 1/60 | about 1/45 |
| All sessions (the 1/50 line) | about 1/75 | about 1/55 |
| All sessions, counting the bundle tool's own output too | about 1/65 | about 1/45 (over the line) |
| All sessions outside the home | about 1/135 | about 1/95 |

- The median consulting session sits near 1/75; **a tail of short sessions reaches up to about a third**, with no
  card read, only method and carrying files: by their file kinds, update sessions, not consultations.
- **What the cost is made of:** method files and carrying files (changelog, carrier record, incoming, proposals)
  about three quarters; indexes about a quarter; cards and notes about one fiftieth. An index was opened about
  twelve times per card opened. The knowledge reviewer was never invoked in the period; the bundle's skills twice
  against about a hundred other skill calls.
- **Characters / 4 undercounts bundle text by about 1.4×:** large single reads of bundle files measured about 2.9
  characters per token from the next call's usage (other tool output about 2.2–2.4). `bundle.py report`'s absolute
  token figures and budgets are therefore about 1.4× low; relative comparisons stand.

## What it means

1. **`i-5ed7e8-1ac328` matters less outside the pilots:** the pilots' ×2.3 came from repositories smaller than the
   index. The bigger lever is what update sessions read and compressing the method (`i-5ed7e8-16b90a`).
2. A new candidate: update-like sessions where the bundle reaches a third of input — check whether the update
   procedure reads whole method files it could skip.
3. Relabel `report`'s tokens as an estimate at chars/4, or move to a measured rate and re-baseline every budget
   (a separate decision).

## Limits

Token sizes are estimates (a bound from usage deltas, not a tokenizer); the carried share is an upper estimate; reads
are detected from command text; small fixed overheads (hooks, listings) are not counted; "consulting" mixes consults
and updates; one machine, three weeks, one person, a handful of very large sessions.
