# Knowledge base — engineering judgement worth carrying between repositories

## What this is, and what it is not

**This is what does not fit in a repository.** A decision belongs in that repo's
`docs/decisions.md`. An external source that changed a decision belongs in that repo's
`docs/references.md`. **A thing that is true about building this kind of software, and will
be true in the next repository too, belongs here.**

**It is not a textbook and not a pattern catalogue.** Those already exist, the agent has
read them, and that is precisely the problem this file solves:

> A well-read agent will confidently propose the textbook answer. Most of the time the
> textbook is right. The expensive cases are the ones where it is not, and **nothing in the
> agent's training says which case it is in.** That is what these notes are for.

So the content here is not "the patterns". It is **which one, when, and where it stops
working** — the part that is normally in someone's head and leaves with them.

## What earns an entry

An entry earns its place when **it changed a decision, or would change one.** Not because
it is interesting, not because it is true. Interesting-and-true is what a search engine is
for.

Two questions before writing one:

1. **Would an agent get this wrong without it?** If the default behaviour is already
   correct, the note costs attention and buys nothing.
2. **Is it true outside this repository?** State it without a single project noun. If it
   needs *our scheduler*, *the billing table*, *our deploy script* — it is a decision, not knowledge,
   and it belongs in that repo's `decisions.md`.

## The shape of a note

A frontmatter block, a heading, and six sections — **the third section is the one that makes this worth keeping**:

```markdown
---
bundle: agent-guides
lineage: <set by the release tool, never by hand>
version: <set by the release tool, never by hand>
slug: <kebab-case; the file name without .md>
topic: <the area it belongs to — see INDEX.md and its area indexes; a new topic is a real decision, not a label>
claim: <the heuristic, one sentence — the only place the claim is written; the indexes quote it verbatim>
confidence: measured | reasoned | inherited
reach: <when an agent should pull this up, comma-separated: planning, architecture, implementation, review, debugging, verification>
---

# <Title in sentence case>

## Why it works
The mechanism. **Not the authority.** "Because a retry re-executes the effect" is a reason;
"because Fowler says so" is a citation, and an agent cannot reason from a citation.

## When it does NOT apply
The boundary, stated concretely. **Every knowledge base omits this field and every one of
them is dangerous because of it** — a heuristic with no stated boundary is applied
everywhere, including where it is wrong.

## What it costs
Every heuristic costs something: a layer, a dependency, latency, flexibility, a person's
time. A note that claims a free lunch has not been thought through.

## Where it came from
An occurrence, a measurement, or **"judgement, unmeasured"** said plainly. Never imply
evidence you do not have.

## Literature
The published work this rests on, if any. For each: **what it says**, **what we take from
it**, and **where we go further or differ, and why**. A bare link is not an entry — the point
is what it contributes here, and a note whose only support is "everybody knows" should say
that instead of dressing up.

## Evidence
**What was tested here, separately from what the literature establishes.** These are two
different questions and merging them is how a knowledge base overstates itself: the principle
can be fifty years old and our application of it still undemonstrated. Later evidence is added
here with its date (`**2026-09-22 — measured, in …**`), not as a separate update section. End
with the experiment that *would* settle it, concretely enough that someone could run it.
```

The claim is **not repeated under the heading**: the frontmatter `claim:` is its one wording, and the index tables quote it. There is no `status:` field — the folder is the state (see *The lifecycle of a note*). A retired note adds `retired_because:` and, when a better note replaced it, `superseded_by: <slug>`. Each paragraph is one line.

**On `confidence`, and why it is a field rather than a tone.** These notes will be mixed
together in an agent's context, and it has no way to tell which ones were paid for:

| Value | Means | How an agent should treat it |
|---|---|---|
| `measured` | **we** produced a number here, and it is in the note | strongest — argue with it only with a newer number |
| `reasoned` | derived from a mechanism, never tested here | strong, but the boundary case may not have been met yet |
| `inherited` | learned elsewhere, believed, not verified here | weakest — useful as a prior, not as an argument |

**`confidence` describes our evidence, never the literature's.** A note citing a fifty-year-old
principle we have never tested is `reasoned`, not `measured` — the citation belongs under
*Literature*, where its own standing is stated separately. Collapsing the two lets a
well-cited note borrow authority it did not earn, which is the specific way a grounded
knowledge base stops being one.

An unlabelled knowledge base lets a hunch and a measurement carry the same weight, which is
how a good one becomes a liability.

## How it travels

As part of the bundle: the whole `.agents/` folder is copied into another repository's
`.agents/incoming/`, and that repository runs `../method/prompt-update.md` or
`../method/prompt-merge.md`, which triage the notes against what it already has. **It is
offered, never pushed** — the receiving repo is the only one that knows which of these notes
contradicts something it decided on purpose.
