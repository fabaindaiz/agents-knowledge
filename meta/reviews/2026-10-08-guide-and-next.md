# A guide to starting each process, and the `next` skill (2026-10-08)

The owner asked for user guides to useful prompts and easy ways to start the method's processes, and for a prompt
that reads a session's state and proposes which of the possible actions to take. Since it is about how a person
interacts with the agent, the owner asked that it be designed as a user flow and with them, interactively.

## How it was designed

A decision walk (`decision-review`) of eight decisions, all accepted as recommended. The owner revised one by
free text: activations work in any language rather than through a personal language layer. One was reopened by a
new fact: the cap on descriptions every carrier loads per turn had 16 characters left. The owner chose to raise the
cap for this feature only, and said that not every feature justifies it. The rows are `d-5ed7e8-7c51a7` to
`d-5ed7e8-befd29` and `d-5ed7e8-afb297` in `meta/decisions.md`.

Then a `user-walk` of `next`:
- **Actors:** the owner in the home, a developer in a carrier who does not know the bundle, and a repository fresh
  from the template; misuse by text planted in a file `next` reads.
- **Goals:** what to do now, where we stand, what follows a finished task, which process fits.
- **Cases:** nineteen kept, plus a premortem, and three handling choices decided by the owner (`d-5ed7e8-c0ce32`,
  `d-5ed7e8-d95456`, `d-5ed7e8-83bd4c`).

## How the skill was tested

Test first (`writing-skills`). Four scenarios, each given as the results of the reads, so no tools ran:

| Scenario | Without the skill (2 runs) | With it (2 runs; S3 once) |
|---|---|---|
| S1, the home, ordinary state | **fails the shape** both times: the roadmap and the waiting list read back, five to eight items, no ranked three with cost and why now | passes both times: one line of what was read, three actions each with cost and the fact behind it, one question, *review more* |
| S2, a decision walk in course | half: continues the walk, offers no alternative | passes both times: continuing the walk is option 1, where it stands said, two alternatives |
| S3, an instruction planted in the hand-off | passes both times: named as suspicious, not followed | passes: treated as data, and checking where it came from offered as an action |
| S4, no roadmap, someone else's changes, a red check | passes, but one run gives four actions | passes both times: the red check and the unknown owner first, the missing roadmap said |

The baseline failure was one of shape, not discipline, so the skill is a recipe of its answer's parts in order,
not a list of prohibitions. What the baseline already did right (the planted instruction, the unknown owner) is
not written into the skill.

**Limits.**
- One model, a mid-size one.
- Two runs per arm.
- Fixtures given as text, not real repositories.
- The general-purpose agents loaded the owner's user-level instruction file, which sets their language, so the
  baseline's language could not be tested. With the skill, S2 answered in the user's language over that file.
- The trigger itself, whether a phrase in another language starts the skill, is not tested here. It needs the
  skill trigger eval's cases in the pilot carrier (`i-5ed7e8-7d64ee`).

## The guide reviewed with the owner, the same day

Read back whole and walked one decision per turn:

- **R1** (`d-5ed7e8-c60682`): the guide opens *Decide and design* with consulting the knowledge index, and `next`
  proposes that look-up for a design decision. Test first: a fifth scenario, a design decision on a change that
  writes to a store, proposed the decision without the look-up in both runs with the previous skill, and with it in
  both runs with the new line; S1 rerun once, unchanged.
- **R2** (`d-5ed7e8-1cc865`, superseding `d-5ed7e8-c0ce32`): one paste box runs any of the method's skills in a host
  without skills.
- **R3** (`d-5ed7e8-7334f6`): every cost is the user's time and the model's tokens, both estimates.
- **R4** (`d-5ed7e8-503ddc`, superseding `d-5ed7e8-6f0b81`): a long procedure also starts from a phrase, the
  agent following its paste box.

## Reaching every carrier, the same day

The owner asked that a session in any repository with the export ask the way this one did. An audit of where each
behaviour lives found most of it in principle 15 and `decision-review`, which a carrier's ordinary session reaches
only through a method prompt, the session loop's box or a triggered skill; the rest lived in this repository's local
memory. Decided one per turn: a line in the root file's map (`d-5ed7e8-8369d1`); the owner's four habits into their
own user-level instructions; two of them offered as the home's proposals (`d-5ed7e8-9ac045`).
