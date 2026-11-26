# Ledger of the cut — every item a short release form drops

The cut of the coding read is a build rule, never an edit that removes text from an original
(`d-5ed7e8-9f47b1`). An original keeps its full block; the release ships the short form written beside
it; and **every normative word, number, inline code span, link target or record id the short form drops
has a row here**, saying *kept at X* or *dropped: why*. `release.py build` fails while one is missing,
so the ledger cannot fall behind the cut.

It stays in the home: it is how a release was made, not what a carrier runs.

**Reading a row.** *File* is the original, as the build names it. *Block* is the name on its
`<!-- release: short NAME -->` marker, or `*` for every block of that file. *Item* is the word, number,
code span, link target or id itself, as the build reports it (a `|` inside one is written `\|`).
*Verdict* opens with `kept at ` — where a reader still finds the fact — or `dropped: ` and the reason
the owner approved.

| File | Block | Item | Verdict |
|---|---|---|---|
| sources/bundle/method/prompt-bootstrap.md | loop-opening | each | dropped: the heading *Three phases, and what each one loads* goes; the three phases and what each loads are still named, one after the other, in the short form |
| sources/bundle/method/prompt-bootstrap.md | step-4-preserve | every | kept at the short form: the owner restored the invariant kinds on 2026-11-26, reading that a rule which says to capture something is weaker than one that says what to capture, for an agent new to the repository |
| sources/bundle/method/prompt-bootstrap.md | step-8 | each | kept at the `close` skill §*4. Count, never remember*: the sentence sending every answer to its home, and the one telling the counter to read every hit and count a copied event once, travel with the routing table and the counting procedure, which the short form names |
| sources/bundle/method/prompt-bootstrap.md | working-safely-rules | not | kept at `method/topics/environment.md` §*Splitting commits after the fact*: the clause saying the split tool makes the copy this rule denies exists travels with the procedure, the only thing that uses the exception |
| sources/bundle/method/prompt-bootstrap.md | research-phase-2 | only | dropped: the rationale that the five-minute re-check is the only thing keeping a *blocked outside* entry blocked out of habit; the obligation to re-check stays |
| sources/bundle/method/prompt-context.md | standards-intro | every | kept at the same block: the sentence that stated this of every standard is rewritten to state it of each standard, which says the same of all of them |
| sources/bundle/method/prompt-context.md | privacy-wins-and-holds | `privacy-allow: <reason>` | kept at `bundle.py privacy --help`, which the short form names; the marker is also still written out in the override sentence of `AGENTS.md` in every carrier Phase 4 wires, and the check prints it on every allowance |
| sources/bundle/method/prompt-context.md | privacy-wins-and-holds | none | kept at `bundle.py privacy --help`: the sentence saying no allowance is silent, because every run lists them all, travels with the override it qualifies |
| sources/bundle/method/prompt-context.md | privacy-wins-and-holds | nothing | dropped: the clause requiring that no current record depend on an obsolete detail before it is deleted; the short form keeps the obsolescence condition itself, and the rule that privacy wins over record-keeping is unchanged |
| sources/bundle/method/prompt-bootstrap.md | step-0 | each | dropped: the lead-in that counted the four rules of the brief and said each was learned from its opposite; all four rules are kept in the short form, two of them in full as the plan of the cut requires |
| sources/bundle/method/prompt-bootstrap.md | step-0 | any | dropped: the gather list's clause about a document naming a file you should confirm still exists, and the rule that anything longer than six lines gets skimmed; the obligation to re-check what is stale, and the six-line limit, both stay |
| sources/bundle/method/prompt-bootstrap.md | step-0 | should | dropped: the same clause, which said a stale document may name a file you should confirm still exists; *what is stale* still says anything that must be re-checked before it can be trusted |
| sources/bundle/method/prompt-bootstrap.md | step-4-preserve | any | kept at `../knowledge/notes/active/validate-each-transformation-run.md`, which the short form still names: the sentence generalising the rule to any tool that rewrites an artefact is the card's own claim |
| sources/bundle/method/prompt-bootstrap.md | step-8 | any | kept at the `close` skill §*2. The documents, true again*: the question about any document you did not open is a row of the table the short form points at |
| sources/bundle/method/skills/close/SKILL.md | description | documents true again, the changelog entry, counted frictions, local memory, the hand-off, gate, commits, remote | dropped from the shipped description: the list of what the skill runs; it is the skill's own body, read once the skill is loaded. The triggers kept are closing or wrapping up a session, ending a phase and leaving everything ready for another machine; the exclusions kept are a pause with no commits, a bare commit or push and finishing selected items |
| sources/bundle/method/skills/close/SKILL.md | description | closing a device or debug session, an app or a dialog | kept in the shipped description: the owner restored both exclusions on 2026-11-26. An exclusion is what stops a skill firing where it does not belong, and that is dearer to discover than a missing trigger, since you learn of it only after it has fired |
| sources/bundle/method/skills/close/SKILL.md | description | before a push that ends a plan with no close yet, ask once whether to close first | kept in the shipped description: **this is a trigger, not a rule, and the first reading had it wrong.** It is what loads the skill before a push that ends a plan; left in the body alone it can never fire, because a body is read only once its skill has loaded. Found by the controller's re-read, not by the lane that wrote the row |
| sources/bundle/method/skills/decision-review/SKILL.md | description | go through its decisions, proposals or open questions again, reconsider one and its implications, say what is left to decide, or decide before planning | dropped from the shipped description: the alternative phrasings of the same trigger; reviewing a spec, design or plan's decisions before anything is built is kept |
| sources/bundle/method/skills/decision-review/SKILL.md | description | a run's opening questions (the pre-flight) | kept in the shipped description, reworded as the questions a run asks once before it starts: that mode is this method's own, so it is exactly the confusion a carrier can make |
| sources/bundle/method/skills/user-walk/SKILL.md | description | something not working, jumping, hidden or slow; a usability or interaction change (controls, keys, menus, animations); a flow to design around the user; what someone meets when a step is slow or cut off | dropped from the shipped description: the examples of the trigger; what a person does or meets in the app is kept as the trigger itself |
| sources/bundle/method/skills/user-walk/SKILL.md | description | testing with real people, or reviewing decisions | kept in the shipped description: the owner restored both exclusions on 2026-11-26, with the other skills' |
| sources/bundle/method/skills/edit-docs/SKILL.md | description | audit, structure, style, copy, mechanics | dropped from the shipped description: the names of the editing levels, which the skill's body lists |
| sources/bundle/method/skills/next/SKILL.md | description | the user has already named the task | kept at the same description, reworded as *not when the task is already named* |
