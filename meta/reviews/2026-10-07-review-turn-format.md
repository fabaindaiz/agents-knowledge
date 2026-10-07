# How a plan and an interactive review talk to the human

**Date:** 2026-10-07. **Status:** research; walked with the owner the same day, who chose every recommendation
and then replaced the two fixed answers by one entry into a tree of modes (`meta/decisions.md`, d-5ed7e8-88e016 to
d-5ed7e8-0fec6e); carried to release 0.0.30 by proposal `p-b102eeae6f`.

## The request, generalised

The owner asked to standardise the two moments where the method learns most from the human, building a plan
and walking decisions interactively:

1. When a plan is built, the agent offers the skills it judges relevant, says how each would be used, and
   lets the human choose.
2. The human is the final reviewer and holds the knowledge to decide; the agent explains, gives examples and
   guides, because the human does not share its context and must take the time to read and understand
   everything asked.
3. No wall of text: several short pieces, each with an example, a question, and a check that it was
   understood.
4. Two answers are always on offer: "explain this more, I do not understand it" and "I think something here
   is wrong".

## What the method already says

`prompt-context.md` §15 and the `decision-review` skill already require: one decision per turn, plain words in
the human's language, two or three options each shown by a concrete case at the same fidelity, priced in the
repository's units, with what it forecloses, the recommendation first with a reason for every option, and a
free-text answer that overrides the options.

| Asked | In the method today |
|---|---|
| Offer relevant skills when a plan is built | no; *Skills from elsewhere* is a moment table no session reads at its start (proposal `p-480f968069`) |
| The human is the final reviewer; the agent explains because the human lacks its context | implied (*theirs* versus *yours*), never stated as a duty to explain |
| Short pieces rather than one long message | partly: "a question is never buried inside a long report"; no length or shape for the turn itself |
| Check that the explanation was understood | no |
| "Explain more" and "something is wrong" always offered | no; only the free-text override |

## What the literature says (sources: ideas only, paraphrased)

- **Chunk and check** (health-literacy practice, several public health services' guidance): give two or three
  key points at a time and check understanding before the next. **Teach-back**: ask the person to say back, in
  their own words, what they understood; the guidance cites large shares of spoken information being forgotten
  or recalled wrongly. ASSUMPTION: the figures and outcome claims come from secondary summaries, not from the
  primary trials.
- **Plain-language and web-writing guidance** (public style guides): readers scan rather than read, so long
  runs of prose are broken into short sections with descriptive headings, lists and tables. ASSUMPTION: the
  reading-share figures quoted there come from secondary summaries.
- **Human–agent planning studies** (preprints, 2024–2026): people readily trust a plan that merely looks
  plausible; a shared, editable plan representation lets them verify it before it runs; a user's ability to
  check what the agent understood is named a condition of working together. ASSUMPTION: read as abstracts and
  search summaries only.

What this changes for the method: an explanation the human reads is not evidence it was understood, and a plan
that reads well is not evidence it was checked. A check that costs the human one click, placed after the part
that is easiest to misread, catches the misreading before it becomes a recorded decision.

## Constraints of the host

The assistant's question tool takes one to four questions per call and two to four options per question, and
always adds a free-text answer. Two fixed answers therefore take half of a question's options; offered as
options on every question, they leave room for two real options only.

## Sources

- Chunk and check, and teach-back: guidance pages of public health services (Scotland's national health
  service, New South Wales' clinical excellence commission, Tasmania's health department).
- Plain-language guidance: public style and accessibility guides.
- Human–agent communication and co-planning: arXiv 2412.10380, 2507.22358, 2502.00640, 2605.23023.

## Adversarial review, the same day (a delegated agent, read-only)

Sources are ideas only, paraphrased; ASSUMPTION marks a claim read only as an abstract or a summary.

**Literature.**

- *Progressive disclosure* puts the rare material one labelled level away and warns against more than two
  levels (ASSUMPTION, a practitioner's essay seen through summaries). The tree of modes is two levels; a third
  would not fit.
- *Choice overload*: a meta-analysis of some fifty experiments found a mean effect near zero with high variance.
  A later re-analysis found it where the task is hard, the set complex, preferences uncertain and the goal is to
  save effort, which is the setting of a skills table offered before a plan.
- *Teach-back*: a systematic review of twenty studies found nearly all reporting benefit. Few were of high
  quality, none measured fidelity, outcomes were mostly immediate, and the barriers named are time and the
  asker's confidence. Teach-back is spoken free recall; a multiple-choice check is recognition, a weaker test.
  No primary source was found for the worry that it feels patronising.
- *Comprehension and attention checks* change the behaviour that follows them. Multiple-choice lures can be
  remembered later as true.
- *Clarifying questions* help when they are good and harm when they are mediocre. Language models mostly
  under-clarify (ASSUMPTION, a summary). Help offered only on demand is underused in interactive learning tools.
- *Over-trust*: explanations raise acceptance of an assistant's advice whether it is right or wrong. Forcing
  functions (the person reasons before accepting) cut over-reliance but are disliked. Committing to a
  provisional answer before seeing the assistant's lowers blind agreement at no time cost. Asking people to
  analyse a plan's assumptions cut over-reliance on execution plans (ASSUMPTION, an abstract).
- *Long sessions*: the best-known decision-fatigue result is confounded. Engagement with coding agents falls as
  a task goes on (ASSUMPTION, an abstract).

**Where the format fails, most severe first.**

1. *The check tests the agent's own framing.* The agent writes the right answer and the distractors, so a
   misreading by the agent is confirmed by the human, and weak distractors make the check guessable.
2. *Acceptance costs one click; scrutiny costs two and a round trip.* With the recommendation first, the easy
   path is agreement. Every decision of this format's own walk records the recommendation chosen.
3. *"Review more" will be rarely used, and its batched case is undefined.* Picked on one of four batched
   questions, it arrives together with answers to questions that may depend on it. It means nothing on pre-flight
   defaults or fact questions.
4. *The block limit squeezes out what §15 requires* (a case per option at the same fidelity, its price, what it
   forecloses). Cutting it unevenly is the nudge §15 forbids.
5. *A skills multi-select meets the question tool's four options*, and a long table with costs invites ticking
   the recommended rows.
6. *Frequency and pull of the check*: "after a long explanation" has no threshold, and quizzing an expert on
   their own domain may push answers toward what the agent seems to want.
7. *Stale wording*: d-5ed7e8-292961 and the proposal's text still name the superseded fixed answer, to be
   corrected at intake, since the home never edits a proposal.

**How to measure it.**

- Count from transcripts (`bundle.py turns`) per walk: the share of "review more" picks by mode, of
  recommendations accepted, of free-text overrides, of checks and wrong picks. Compare with the decisions log's
  superseded rows before and after the format.
- A guessability test: a fresh agent without context answers each check.
- A seeded-error pilot: a false assumption planted in a spec, walked with and without the format.
- Lines per review turn, to see whether the block rule holds.

**Wording it proposes.** The check's distractors are the consequences of the other real options plus *none of
these*, and a wrong pick reopens the decision. The block limit counts prose only, and option cases go in the
options or a table, never cut. "Review more" goes on decision questions only; in a batch it re-asks that
question and its dependants; an irreversible decision shows its assumptions unasked. The skills offer has at
most four, with the rest named in one line.
