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
