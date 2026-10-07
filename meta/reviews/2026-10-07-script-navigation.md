# Navigating the bundle with scripts where no judgement is needed

**Date:** 2026-10-07. **Status:** research by a delegated agent, read-only, with a prototype kept outside the
repository; bears on release 0.0.30's focus (`d-5ed7e8-7cac23`). Figures from pilot-9 and the reviewer pilot.

## Which steps a script can take

| Step | Class |
|---|---|
| Record ids, privacy, trailers, `verify`, a changelog entry's skeleton, a session's reads | deterministic, already in `bundle.py` |
| The closing checklist | mostly deterministic: count, memory diff, ids, trailers and verify could run as one command; wording the entry is judgement |
| Reading the index to find the card for a change | fuzzy lookup: a script narrows the rows, the model picks among a few. **The main cost target** |
| Opening a card once chosen | deterministic: a lookup can print its boundary and check inline |
| Whether a card applies, or its boundary excludes it | judgement |
| Running a card's check | judgement and execution: every one of the 51 checks is prose that needs a test or a planted fault against the carrier's own code, so none can be run by a script |
| Setting up a check's scratch copy | deterministic: worktree, copy, plant, test, clean up |

## The prototype

`lookup` ranks the index's lookup rows and the cards against a change's text, its files or its diff, and prints
one to three rows: the action, the card's path and when the textbook answer is wrong. With `--cards` it also prints
each card's boundary and check, about three percent of the index's size. Notes carry no machine-readable cues today;
the minimal field that makes the lookup work is a `cues` list per note, the words a change or its diff would
contain, copied into the release at build.

| Query | Without cues, top 3 | With cues, top 3 |
|---|---:|---:|
| The task's prompt (26 targeted tasks) | 8 of 26 | 22 of 26 |
| The task's diff (52 diffs) | 27 of 52 | 47 of 52 |

**The figures with cues are contaminated:** the cues were written after reading the prompts, so they are an upper
bound. A run with every task-suggestive term removed fell to about half, which is too harsh. True recall is between.
On trivial or neutral tasks the lookup always returns something, so the wiring's "skip when trivial" must still
decide.

## What it would save

- **The author.** The index is read at the first call or two and re-sent on about seven more. Replacing it with a
  lookup's half-thousand tokens saves about a quarter of the bundle arm's cost, and moves the bundle-to-minimal
  ratio from about ×2.2 toward ×1.7 on paper. It saves no turn, since the lookup replaces the read one for one. D2
  delivered a third of its predicted saving, so a realistic figure is ×1.8 to ×1.9.
- **The reviewer.** About two thirds of its calls come after its last card: about half read and search the
  repository (judgement), an eighth run code or tests, a tenth set up scratch copies, a fifth are directory
  plumbing. A lookup by diff saves about a sixth. A scratch command saves about a tenth to a seventh. Returning each
  check as a test to write is still the larger lever (about a quarter).

## Risks, and two designs that avoid them

- **A missed card costs the pass.** The discriminating tasks passed every time with the bundle and rarely without
  it. Authors opened a tenth of a card on average yet passed, so the index's "wrong when" column probably does the
  work, and the lookup prints it.
- **The model may ignore the script** and read the index anyway; this has to be counted.
- **No recall risk:** a list of the action phrases only (about a tenth of the index), the model choosing by
  meaning, then expanding its picks. It saves about a tenth net, since it adds a call, but "wrong when" is out of
  view while choosing.
- **No adherence risk:** a prompt-submit hook that runs the lookup and injects the rows. No turn, no decision.

## How to measure it

1. **Offline gate first:** cues written blind by someone who has not seen the tasks, plus new held-out prompts;
   recall at three of at least nine in ten.
2. **An author arm** that runs the lookup, opens only the cards it prints, and reads the index only if none fits,
   on pilot-9's six tasks, registered before any trial. Cost at most ×0.85 of the release on non-trivial tasks,
   refuted above ×0.95; discriminating passes equal; adherence counted from the transcripts.
3. **Optionally a hook arm**, and **a reviewer arm** with the lookup by diff and the scratch command, cost primary,
   recall as the guard.
