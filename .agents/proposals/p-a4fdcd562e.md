---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-a4fdcd562e
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.23
digest: f8718e4c1fde
kind: knowledge
action: extends
target: derived-over-chosen-identifiers
lacks: a second occurrence
seen: "2026-09-28"
---

An identifier derived from a record's content must cover every field that tells two records apart, and nothing that changes with when or where it is computed: a hash over a subset merges distinct records into one, and a hash that takes a fallback such as today's date gives the same record a new identity each day, so it is taken in twice. Stops applying when identity is assigned once and stored. Costs listing the fields that distinguish records, and a test that computes the id on two days.

## Evidence

In one release tool, two rows that differed only in evidence or place shared an id and the second was dropped; after the fix, a row with no date took the conversion day as its date, so a gather and a later conversion gave it different ids. Both reproduced by an adversarial review and fixed with a test each. Literature: the note's own.
