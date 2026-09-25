
# Index — when to read which note, and how to check it holds

**This file is the mechanism.** The notes are read on demand; this is what decides which one, and what to run to show that the heuristic was respected. Keep it scannable, or nothing below it gets read.

Every note in `notes/active/` and `notes/review/` is reachable from here and every listed note exists — checked by the repository's audit, because a dead pointer in an index is worse than an index nobody wrote.

This file is the entry point: the phase guide for every note, and a route to the area index that holds each note's check. There is no cap on notes — the reason is in `README.md`, *Keeping it usable*.

**A note marked ⚠ review** sits in `notes/review/`: its evidence or its admission is disputed and a verdict is pending. Use it, and say in the report that it is under review; its *Evidence* section opens with the reason. The folder a note sits in is its state — `README.md`, *The lifecycle of a note*.

## How an agent uses this index during a task

1. **At the start**, find the phase you are in under *By phase of work* and skim the claims of the notes it lists. Open a note only when its claim touches what you are about to do.
2. **Before a design decision**, look up the action under *By what you are about to do*, in the area index (`areas/behaviour.md`, `areas/evidence.md`). The third column is the case where the default answer is wrong — if it matches, read the note.
3. **Before claiming the work is done**, run the *Verify by* check of every note you relied on (in its area index), and say in the report which ones ran and what they showed. A heuristic that was read but not checked is an opinion that happened to be nearby.
4. **When the work contradicts a note** — a measurement, a test, an incident — do not quietly work around it. Record it in `../tracking/experiments.md`; a note that is contradicted by evidence goes to review, and is revised or retired, never ignored.

## By phase of work

| Phase | The question to ask | Notes |
|---|---|---|
| **Plan and design** | What will this touch that already depends on it, and what happens under retries, a second instance, a crash, an abuser? | {{notes:plan}} |
| **Design a dataset, a population or a model** | Could any row, filter or feature know something that did not exist yet at its instant? | {{notes:dataset}} |
| **Implement** | What does this code do when a value is missing, a clause is lost, a side call fails, a nested object is sent? | {{notes:implement}} |
| **Write tests** | Would this test fail if the code were wrong, against the real dependency? | {{notes:tests}} |
| **Review** | Which constraint, switch or cap could this diff have removed without any test noticing? | {{notes:review}} |
| **Verify and report** | Does the number mean what the sentence says, measured where it is claimed? | {{notes:verify}} |
| **Debug or investigate** | Is the discrepancy in the world, in the join, in the clock or in the environment? | {{notes:debug}} |

## The areas, and where each check lives

Each note is under exactly one topic, and each topic in one area. The area index holds the topic tables with their *Verify by* checks, the *about to do* rows, and how well founded each note is.

| Area | Index | Topics |
|---|---|---|
| What the system does | [areas/behaviour.md](areas/behaviour.md) | `distributed-correctness` · `failure-behaviour` · `evolving-contracts` · `time-and-control` · `adversarial-controls` · `identity-and-naming` |
| What the data and the checks tell you | [areas/evidence.md](areas/evidence.md) | `data-correctness` · `measurement` · `verification` |

## How well founded is any of this

**Read this before weighting a note.** The two axes are independent and confusing them is the main way a knowledge base misleads:

| | What it means |
|---|---|
| **The claim** | how well the general principle is established — usually by the literature each note cites |
| **Our application** | whether *we* demonstrated it here — usually not |

Each area index lists every note's two answers. A note is `measured` only when a number came from running the method in a repository and was written down at the time — which is the only way a note earns it; its `confidence` field says which it is. The rest are honest `reasoned` notes; each one's *Evidence* section names the experiment that would settle it, and `../tracking/experiments.md` is where those experiments are queued.

## Keeping it usable

What is kept bounded is attention, not the number of notes; the rules, and why there is no cap, are in `README.md` under *The lifecycle of a note*. In short: every note is reachable (under its topic, in at least one phase above, and in at least one *about to do* row of its area); an index that stops being readable in one pass is split by area; a new occurrence, number or boundary extends the note it belongs to; every harvest closes with a review that ends in verdicts; and a learning that has not passed admission waits as a line in `../tracking/candidates.md`.

## Retired

Retired notes are kept in `notes/retired/` and leave the tables above; `../tracking/retired.md` is the chronological log of each retirement and its evidence.

## What is deliberately not here

- **Patterns the agent already knows.** Clean architecture, DI, repository pattern, the standard library. If the default behaviour is already right, a note costs attention and buys nothing.
- **Anything that needs a project noun to state.** That is a decision; it belongs in that repository's `docs/decisions.md`.
- **The rituals of how work is done** — the session loop, committing, reviewing, documenting. That is the method, in `../method/`. A claim about what a check or a tool can and cannot tell you is knowledge, and the method points to it.
