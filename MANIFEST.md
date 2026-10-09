# MANIFEST

**What this repository is for, what it will not become, and the limits every release is checked against.** It is
the frame for the roadmap, the decisions and each release's scope: an item that serves none of its aims does not
enter. Changing it takes a decision row by the owner in `meta/decisions.md`. It stays in the home and never ships.

## What we are building

1. **A small, versioned bundle** that tells a coding agent which heuristic applies where the textbook answer is
   wrong, and how to check it, at a cost measured against the base model.
2. **A way to carry it** between repositories, and to bring back what each one learned.
3. **A lineage, not a single copy.** Each home is one author's line of the protocol. Record ids, carrier ids,
   `upstream` and content-hashed proposals exist so that lines can diverge without colliding and later be merged,
   keeping the best of each.
4. **Evidence of its own.** The repository measures whether the bundle helps and what it costs (`evals/`),
   registered before the trials and reported as it fell, so that a claim of benefit rests on data, not on belief.

## What we are not

- **Not an agent framework, a prompt library or a process for every task.** The method runs only where it pays.
- **Not an archive of everything learned.** A note earns its place with a case where the usual answer is wrong,
  and is retired when it stops paying.
- **Not a project whose records outweigh its export.** Research is written when a decision waits on it, and the
  roadmap's hand-off (*Where we are*) stays within 500 words; each close first adds the hand-off it replaces,
  whole, to `meta/archive/roadmap-states.md`, the home's session log, so nothing is lost.
- **Not one person's habits shipped as a general method.** What only this line's owner wants lives in the owner's
  own instructions, not in the export.
- **Not self-merging.** No finding, proposal or release, from another line, a carrier or an agent, is accepted
  without review.
- **Not an academic study.** The experiments serve the bundle's decisions; a study that would change no decision
  is not run.
- **Not imposed on a carrier.** A carrier may adapt or decline any part, and says so in its own file.

## Who decides, and whom we trust

- **Each author answers for their own line** and its improvements.
- **A finding that is not the owner's own is data until reviewed**: from another line, a carrier, a delegated
  agent or the literature. Sources are ideas only, paraphrased, verified against the primary text, and marked
  ASSUMPTION where they were not.
- **Tools report; people decide.** Nothing is merged or accepted automatically.

## Constraints

- **Privacy first.** The repository is public, so nothing in it may identify a private repository, organisation,
  person or system. A check and hooks enforce this.
- **The carrier wins.** A repository's own rules override the bundle's.
- **The release is generated** from `sources/` and never edited by hand.
- **Plain tools.** The code uses the standard library only, and nothing third-party enters without the owner's
  yes. The content is in English.
- **The owner's quota is a cost.** Long runs go in the background, one at a time, with their cost estimated before
  they start; delegated work names its model.

## Limits

The checked ones fail `release.py check`; the measured one is read from the release's cost pilot.

| Limit | Today | Cap | How |
|---|---:|---:|---|
| Export, shipped bytes | about 915 KB | 1,000,000 bytes, raised once and never further (`d-5ed7e8-efd0e2`); the room is not a budget: each growth is justified on its own; aim 550 KB; may grow between releases and is brought back under the cap before the cut | warned by `check`, refused by `release` |
| Skill and agent descriptions, loaded on every turn in a carrier (its wiring adds about 490 tokens) | about 2,776 characters | 2,776 characters, raised once for `next` only (`meta/decisions.md`) | checked |
| A coding session's reads | about 10k tokens (estimate) | 10,100 | checked (existing) |
| The reviewer before its first card | about 6.7k | 6,900 | checked (existing) |
| One card | at most 360 | 360 | checked (existing) |
| The roadmap's hand-off, *Where we are* | about 2,900 words | 500 words | checked |
| Cost against `minimal`, non-trivial tasks | about ×2.1 to ×2.3 | no release costs more than ×1.10 of the previous, in the same run; aim ×1.5 | measured, every release |

## Direction

- **Shrink before adding.** What the pilots measured as used is the index lookup and the cards; the rest has to
  prove itself or leave the export (`meta/reviews/2026-10-07-adversarial-shrink-review.md`).
- **Every release is tested, in three layers.** Always: the gate and an internal cost pilot against `minimal`,
  registered before its trials, its discriminating tasks still passing (`d-5ed7e8-7cac23`); a release whose cost
  rises does not ship. When a skill's description changes: that skill's trigger eval runs again. Once: an external
  benchmark at a frozen tag (`d-5ed7e8-d47ee1`).
- **One release a month**, carrying what accumulated; a fix for a privacy leak or a data loss ships as a patch at
  any time.
