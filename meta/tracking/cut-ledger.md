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
