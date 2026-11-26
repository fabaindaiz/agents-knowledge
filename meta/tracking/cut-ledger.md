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
| sources/bundle/method/prompt-bootstrap.md | step-4-preserve | every | dropped: the list of invariant kinds (the rendered output, the emitted file, the token stream, or for prose *every* number, identifier and link target) goes; the rule to name the invariant and compare it byte for byte stays, and the card `validate-each-transformation-run` carries the general form |
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
