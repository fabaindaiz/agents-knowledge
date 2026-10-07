# Choosing among many skills, and the catalogue a complex task reads

**Date:** 2026-10-07. **Status:** research by a delegated agent, read-only; bears on `d-5ed7e8-2ec5dd` and
proposal `p-480f968069` (the catalogue), and on the skill trigger eval. Sources are ideas only, paraphrased.
ASSUMPTION marks a figure read through a summary or an abstract; every recent preprint's figure is one, and none
is replicated.

## What is known

- **The host drops descriptions when many skills are installed** (the assistant's skills documentation, read in
  full). The skill listing gets about one percent of the context window. Past that, descriptions are dropped,
  the least used skills first, and each skill's description and `when_to_use` are capped at about one and a half
  thousand characters. A setting raises the budget, and per-skill overrides can turn a skill off or show its
  name only. On a machine with over a hundred general-purpose skills, many show as a bare name. The method's
  three skills are rarely used, so they are the most at risk.
- **Accuracy falls with library size** (ASSUMPTION, a preprint on synthetic skills). Selection stays near
  perfect up to a couple of dozen skills, falls fast past about fifty, and reaches a fifth at two hundred.
  Similar-sounding competitors cost the most; with none, selection was perfect.
- **Retrieving tools first beats listing them all** (ASSUMPTION, two preprints and a vendor's engineering note).
  Retrieval roughly triples selection accuracy over an all-in-prompt baseline, at half the tokens; a vendor's
  deferred tool search raised accuracy by a quarter on one model and by a tenth on a newer one. The commonest
  error is choosing between similarly named tools. One vendor advises keeping under about twenty functions in
  view at once.
- **No study measures a static catalogue file against descriptions alone.** The nearest evidence is that
  choosing a category first held accuracy where a flat list fell, by a wide margin on a small model and about a
  tenth on a large one (ASSUMPTION). Loading all of some two hundred skills scored the same as loading none, at
  more tokens; offering the top three was the useful setting (ASSUMPTION).
- **Description guidance.** One vendor's guidance asks for third person, what the skill does and when to use
  it, specific key terms, a short cap, and evaluations on several models. An open skill-format guide asks for
  about twenty queries, half near misses, three runs each, a train and validation split, and a few iterations.
  It notes that agents skip skills for tasks they believe they can do alone, which explains process skills
  under-firing. Better tool descriptions raised success modestly but added steps and made some cases worse
  (ASSUMPTION).

## Where the catalogue design is weak, most severe first

1. **The trigger is itself a selection.** "Complex" is judged at the start, but an unknown cause or the number
   of steps often shows only after exploring. Meanwhile "any one of five" signals fires on most ordinary work,
   adding a question where the owner's rule is to decide alone what is reversible.
2. **Three routers can disagree.** Skill descriptions demand to run first, the method has its moment table, and
   the catalogue adds a third, with no rule on which wins.
3. **The listing budget makes the catalogue load-bearing, and it goes stale.** Names a carrier lists drift from
   what is installed.
4. **Its own rows are near twins.** Executing a plan, driving subagents and parallel dispatch overlap; so do a
   code review request and the bootstrap's fresh-context review, and `close` and finishing a branch. Near twins
   were the main cause of wrong picks above.
5. **Offering many invites over-use.** Gains were larger with two or three skills than with four or more
   (ASSUMPTION, skills injected rather than offered).
6. **"Measurable" is half true.** The trigger eval counts a skill tool call; a read of the catalogue is a file
   read, and judging a signal is still the model's.
7. **Token cost is small** (a thousand or two per read); the cost is the extra turns with the human.

## What it recommends for 0.0.30

1. **A single signal routes straight to its skill.** An unknown cause goes to systematic debugging, independent
   parts to parallel dispatch. The catalogue is read on two or more signals, and again when a plan is written or
   the work passes its third committable step.
2. **Offer at most three**, one line each with why it fits, the skipped ones named in a line. Ask only when the
   choice is not reversible; otherwise state it and proceed.
3. **Resolve conflicts in the rows.** Each row says what separates it from its neighbours. One sentence says the
   method's order wins over a description demanding to run first. A check fails when a skill a carrier lists is
   not installed, or its description is missing from the listing.
4. **Shrink the pool and measure.** Advise carriers to turn off, or show by name only, skills that do not fit,
   the best-supported lever. Measure the catalogue against descriptions alone in the trigger eval (a catalogue
   read counted as a fire; one case per signal, two-signal cases, multi-step but trivial near misses; three runs)
   before claiming it helps.

## Consequence now, for the trigger eval

The eval runs on a machine whose listing drops descriptions. Stage 1 must first confirm the three skills'
descriptions are in the listing (the eval's own precondition). Where they are not, the run measures the budget,
not the description.

## Sources

The assistant's skills documentation and skill-authoring best practices; a vendor's engineering note on
advanced tool use; another vendor's function-calling guide; an open skill-format guide on optimising
descriptions; arXiv 2601.04748, 2505.03275, 2503.01763, 2602.14878 and a 2026 skill-retrieval preprint.
