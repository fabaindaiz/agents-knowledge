
# Index — when to read which note, and how to check it holds

**This file is the mechanism.** The notes are read on demand; this is what decides which one, and what to run to show that the heuristic was respected. Keep it scannable, or nothing below it gets read.

Every note in `notes/active/` and `notes/review/` is reachable from here and every listed note exists — checked by the build, because a dead pointer in an index is worse than an index nobody wrote.

This file is the entry point: the phase guide for every note, and a route to the area index that holds each note's check. There is no cap on notes; what is bounded is attention.

**A note marked ⚠ review** sits in `notes/review/`: its evidence or its admission is disputed and a verdict is pending. Use it, and say in the report that it is under review. The folder a note sits in is its state — `README.md`, *The state of a note*.

## How an agent uses this index during a task

0. **Only when the change touches state, a contract, data, security or verification.** A typo, a text or a local rename consults nothing: the index costs a session only when it can change a decision.
1. **At the start**, find the phase you are in under *By phase of work*: it names the notes whose cards, in the area index, may apply.
2. **Before a design decision**, look up the action under *By what you are about to do*, in the area index (`areas/behaviour.md`, `areas/evidence.md`). The third column is the case where the default answer is wrong. If it matches, apply the note's card: its claim, *Not when* (where it stops applying) and its check. **Open the full note only when you cannot tell whether its boundary holds here.**
3. **When this repository states an invariant that contradicts a note, the repository wins.** Follow it, and say in the report which note gave way and why: that is evidence the note's boundary is incomplete.
4. **Before claiming the work is done**, run the check of every card you relied on, and say in the report which ones ran and what they showed. A heuristic that was read but not checked is an opinion that happened to be nearby.
5. **When the work contradicts a note** — a measurement, a test, an incident — do not quietly work around it. Say so in the changelog entry; the harvest records it in this repository's outbox, and the home reviews the note, revising or retiring it, never ignoring it.

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

Each area index lists every note's two answers. A note is `measured` only when a number came from running the method in a repository and was written down at the time — which is the only way a note earns it; its `confidence` field says which it is. The rest are honest `reasoned` notes; each one's full note, in the home repository, names the experiment that would settle it, and `OPEN.md` lists those still waiting to be run.

## Keeping it usable

What is bounded is attention, not the number of notes: every note is reachable (under its topic, in at least one phase above, and in at least one *about to do* row of its area), and the build refuses one that is not. A learning not yet admitted is a row in `../tracking/candidates.md`, this repository's outbox; `OPEN.md` lists the ones the home is still waiting on.

## What is deliberately not here

- **Retired notes.** They stay in the home repository and never ship.
- **Patterns the agent already knows.** Clean architecture, DI, repository pattern, the standard library. If the default behaviour is already right, a note costs attention and buys nothing.
- **Anything that needs a project noun to state.** That is a decision; it belongs in that repository's `docs/decisions.md`.
- **The rituals of how work is done** — the session loop, committing, reviewing, documenting. That is the method, in `../method/`. A claim about what a check or a tool can and cannot tell you is knowledge, and the method points to it.
