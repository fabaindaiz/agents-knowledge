---
slug: "merge-by-shared-fact-not-shared-shape"
topic: "evolving-contracts"
claim: "Merge copies that must agree by contract and whose divergence would be invisible; keep copies that only look alike, especially where merging would hide an error from a symmetric test, and write down why they stay."
confidence: "reasoned"
principle: "same-only-by-a-shared-fact"
applies_if: "Two copies encode one fact that must agree. Look for the contract, schema or document that says they must, and for a test that exercises both copies the same way."
phases: ["plan", "review"]
check: "every kept duplicate has a recorded reason; every merged one has a test that fails if a caller diverges; a behaviour switch reads a field set only where that decision is made"
about:
  - {do: "Remove duplication, or decide to keep it", wrong_when: "the copies look alike but mean different things — or they must agree and nothing checks that they do"}
  - {do: "Reuse a tone, a style or a derived kind to switch a behaviour", wrong_when: "the value was made for another consumer, so a change made for that one silently changes the behaviour"}
rests_on: "DRY (Hunt & Thomas); Metz 2016; for the dual, control coupling and connascence of meaning"
strength: "practice, and in tension"
our_evidence: "occurrences in two repositories, and the dual's in two; no regression rate"
---

# Merge by shared fact, not by shared shape

## Why it works

Two kinds of duplication look the same in a diff. In the first, the copies encode **one fact** — how an object is torn down, how a description becomes objects, which numbers a file carries — and they must agree; any divergence is a bug, and nothing notices it, because each copy works on its own. In the second, the copies only share **a shape** — a loop, a search, a guard — while their semantics differ. Merging the first kind removes a class of silent bug. Merging the second produces a function with modes and parameters that reads worse than either copy, and can do worse: when the copies are tested by a check that is symmetric in them, a shared defect moves both the same way and the check stays green.

So the question is not "is this code repeated?" but "is this knowledge repeated?". Only the answer to the second decides.

**The dual: one field read by two decisions is two facts merged because they coincide today.** When a presentational or derived value — a notice's tone, a derived kind — also switches a behaviour, a change made for one consumer silently changes the other: a status that merely looks like a success closes itself, a new kind of data switches off an unrelated suggestion. Give the behaviour its own explicit field, set only where that decision is made. The question is the same one asked of a field instead of a copy: how many pieces of knowledge does it hold?

## When it does NOT apply

- **When you cannot yet tell fact from shape.** Two occurrences rarely show which; wait for the third, and meanwhile keep the copies and a note.
- **When one copy is generated from the other** — then there is only one source, and the duplication is output.

## What it costs

A judgement at every copy, and a written record for each copy kept on purpose — or the next reader "cleans it up". Merging a fact can force an interface that spans layers; that is sometimes the real cost.

## Where it came from

One repository, an interactive renderer. Merged, because the copies were one fact:
- four ways to leave the running content were four blocks that differed without anyone having decided it — one never discarded a view, only one reset a clock; unified, a live-object counter returns to the same value over repeated cycles;
- three copies of content assembly, one of which was silently left behind when an input form was retired;
- a packer and a metadata writer made to share their functions because keeping them apart had already failed once: one wrote a cell size the sheet did not have;
- an animation's clip and facing read from its samples rather than stored separately, because two records of one fact drift apart.

Kept, and recorded as a decision rather than a backlog item: four small binary searches whose return values mean different things, where the two-direction purity test could not catch an off-by-one because it would shift both directions equally; two placement routines that differ in half a dozen respects, where a many-parameter helper with two callables would read worse than either copy; and a few identical lines per file in widgets that cannot share a parent class under single inheritance.

A second repository, 2026-09-28, gave a clean pair in one change. Content rules written per surface — which items a surface shows, which label they carry — diverged repeatedly, a secondary surface missing a tag and a filter the primary one had; a shadowing rule became one predicate shared by two consumers, with a test asserting that their answers are complementary, after an earlier divergence that had held only by accident (fact). A width split that worked on result rows, copied to a table that only looked the same, made every row of that table wrap and was reverted, because the split depends on what each side measures there (shape).

The dual comes from two occurrences, folded here at 0.0.27 from the queued `one-field-one-decision`. In an interactive client, adding one kind of data to an item changed its derived kind, and so silently switched off an unrelated suggestion; after the decision was split into its own field, a small sample showed every item but one unchanged, and that one restored. In an administration panel, 2026-10-04, a notice's success tone also triggered its auto-close, so a persistent status that merely looked green closed itself after a partial refresh; a dedicated marker set only by the action-success helper, with three tests, decoupled them. A whole-branch review caught it, not the task reviews or the tests.

## Literature

- **Thomas & Hunt, *The Pragmatic Programmer*, 20th anniversary ed. (2019), [Tip 15, DRY](https://pragprog.com/tips/):** "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system." *Verified 2026-09-22 against the publisher's tips page.* **What we take:** the unit is knowledge, not text.
- **Metz, 2016, ["The Wrong Abstraction"](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction):** "duplication is far cheaper than the wrong abstraction". *Verified 2026-09-22 against the blog post.* **What we take:** the cost of merging shape. **Where we go further:** the symmetric-test criterion, which says when a merge also blinds a check.
- **Stevens, Myers & Constantine, 1974, ["Structured Design"](https://doi.org/10.1147/sj.132.0115)**, *IBM Systems Journal* 13(2): coupling, and control coupling as one module steering another's logic with a flag. *Checked 2026-10-05 only through secondary sources and the bibliographic record; the primary text was not reached, so no wording of it is quoted.* **What we take:** the dual's mechanism — a tone or a derived kind read as a flag by a consumer it was not made for.
- **Page-Jones, 1992, ["Comparing Techniques by Means of Encapsulation and Connascence"](https://doi.org/10.1145/130994.131004)**, *Communications of the ACM* 35(9): connascence, where a change to one element requires changing or checking another. *Bibliographic record checked 2026-10-05 against the publisher's listing; the "meaning" form against a secondary catalogue.* **What we take:** two consumers agreeing on one meaning of one value is connascence of meaning.
- **Roberts, *CSS Guidelines*, "JavaScript Hooks".** Do not bind behaviour to a styling class; use a dedicated behaviour hook, or one cannot be changed without the other. *Checked 2026-10-05 against the page.* **What we take:** the dual's second occurrence is this named case.
- **Thomas & Hunt, 2019, Tip 17, "Eliminate Effects Between Unrelated Things".** *Checked 2026-10-05 against the publisher's tips page.* The goal, stated generally. **Where we go further, for the dual:** only the trigger (a derived or presentational value reused as a behaviour switch) and where it was caught (a whole-branch review, not the tests); the rest is textbook, which is why it is a paragraph here and not a note.
- **Sibling in this base:** `same-answer-or-refuse` records the binary-search case as a boundary of equivalence testing.

## Evidence

**Reasoned, from seven occurrences** (four merges, three kept) in the first repository, a fact-and-shape pair in a second, and two occurrences of the dual, in two repositories. The object counter, the cell-size mismatch and the dual's restored item are observations, not a rate. The experiment: over one repository's history, classify every duplication removed or kept as fact or shape, and count the regressions that followed each kind.
