# Where the reviewer's cost comes from

**Date:** 2026-10-07. **Status:** analysis by a delegated agent, read-only, of the reviewer pilot's 60 transcripts
and pilot-9's 36 (`evals/REPORT.md` §4.11, §4.12). It bears on `d-5ed7e8-c3ebf0` (D2 measured again) and on
`i-5ed7e8-1ac328` (a consulting session's cost). Exploratory: one model, 15 diffs, two repetitions.

## Price

Each trial's estimated cost is reproduced exactly by list prices per million tokens of two for input, four for a
one-hour cache write, a fifth of one for a cache read and ten for output. It is a list-price estimate, not a bill.

## The reviewer's input, by arm (means)

| | `R0` | `R2` |
|---|---:|---:|
| API calls | 12.0 | 12.3 |
| Context of the first call (the fixed prefix) | about 15,400 | about 15,400 |
| Context of the last call | about 32,600 | about 29,700 |
| Cumulative input | about 360,000 | about 329,000 |
| Cache read / cache write / uncached input | 94% / 6% / under 0.1% | 94.5% / 5.5% / under 0.1% |
| Output (of which reasoning) | about 6,100 (2,900) | about 6,000 (3,100) |
| Estimated cost | ×1 | ×0.91 |

**What each part costs in `R0`**, since a part enters once and is re-sent with every later call:

| Part | Share of cumulative tokens | Share of estimated cost |
|---|---:|---:|
| The fixed prefix | about half | about a quarter |
| The knowledge index | about a fifth | about a fifth |
| The assistant's earlier turns | about a fifth | about a fifth |
| Output | none | over a quarter |
| Searches, cards, repository reads | a few percent | small |

- **The prefix is already small**: four tools, no connector, no skill. Most of it is read from a cache shared
  across sessions, and only the instructions, the diff and the environment are written per trial.
- **The largest tool result is the index**, about 6,900 tokens; about 4,400 in `R2`.
- **About two thirds of the calls come after the last card is opened**, holding about three quarters of the
  cumulative input and over half the cost. They are mostly the reviewer running each card's check, which its
  instructions require. Each extra call adds about 33,000 input tokens and a fairly constant cost (r near 0.95).

## The levers, estimated on `R0`

1. **Fewer calls in the check phase**: one check per card, or the check returned as a test to write, and the first
   reads batched. Halving the calls after the last card would save about a quarter of the cost and over a third of
   the tokens; batching the early reads two or three calls more. This assumes the per-call slope is the marginal
   cost, and it says nothing of what the checks contribute as evidence.
2. **The index**: about a fifth of the cost. D2 saved 7 to 9 percent; an index reduced to its lookup table has a
   ceiling near a fifth.
3. **The cache's lifetime** (ASSUMPTION, not checked whether the host lets it be chosen): every cache write is at
   the one-hour rate, about two fifths of the cost; a five-minute lifetime would save about a seventh without
   changing behaviour.

Smaller or unmeasured levers: a custom, shorter system prompt saves about a quarter of the tokens but under a
tenth of the cost, since the prefix is read cheaply from cache; less reasoning effort, about a fourteenth; a cheaper
model, in proportion to price if the calls stay the same, quality unmeasured.

## Which metric

For `R2` against `R0`, cumulative tokens and estimated cost agree (×0.91 by means, ×0.95 and ×0.94 by geometric
mean of the 15 paired diffs). For comparing levers they disagree: the prefix is about half the tokens but a
quarter of the cost, output none of the tokens but over a quarter of the cost, cache writes a sixteenth of the
tokens but two fifths of the cost. Estimated cost should be the primary metric, with tokens beside it.

A second, post-hoc reading (not registered): the context the reviewer held when it chose its first card had a
median near 27,000 tokens in `R0` and 23,400 in `R2` (×0.87). Even on the quantity the original estimate was made
for, the split does not reach ×0.6, because the fixed prefix and the diff outweigh the index.

## The author's side (pilot-9)

The bundle roughly doubles the author's estimated cost. The index explains about a third of the overhead, extra
output about a quarter, the assistant's earlier turns about a fifth, and the prefix re-sent over more calls the
rest. D2 lowers the index's share but spends a little more on searches. The author's prefix is larger than the
reviewer's (more tools, the owner's global instructions loaded in every arm).
