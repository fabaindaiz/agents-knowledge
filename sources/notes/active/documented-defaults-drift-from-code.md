---
slug: "documented-defaults-drift-from-code"
topic: "evolving-contracts"
claim: "A reference that lists settings, keys or defaults drifts from the code that reads them, in both directions; rewrite it from the reader, then hold every documented table to every key the reader reads, optional ones and their defaults included, both ways, as a gate check seen to fail."
confidence: "measured"
phases: ["review"]
check: "a gate check compares each documented key table with the keys the reader reads, both directions and defaults included, and was seen red on a renamed key"
about:
  - {do: "Document a setting, a key table or a default", wrong_when: "the reference is written apart from the reader, or only required keys are checked"}
rests_on: "Rabkin & Katz 2011, static extraction of configuration options"
strength: "measured at research scale"
our_evidence: "measured in three repositories; occurrences in a fourth"
cues: ["config reference", "default value", "env var table", "readme settings", "config keys", "document option", "settings.py", "yaml config", "renamed key", "docs table", "optional keys", "config schema", "defaults documented", "os.environ.get"]
---

# Documented defaults drift from code

## Why it works

A reference of settings is written beside the code, not from it, and each is changed on its own schedule. It drifts in both directions: a key documented that nothing reads, a key read that nothing documents, a default that was right once, a unit or a name that changed. A reference written from an earlier reference inherits its errors and adds its own. Nothing fails when it drifts: the code reads what it reads, and the reader of the document acts on what it says.

Three moves close it. **Rewrite from the reader**: every claim in the reference checked in the code that reads the key, not in the previous document. **Hold the tables to the reader**: a check that extracts the keys the reader actually reads and compares them with each documented table, both ways, so a key renamed in the code is reported as documented-but-unread and as read-but-undocumented. **Cover every key**: optional keys and their defaults included. A check over the required keys only protects the boot, not the document, and the optional keys (tunables, flags with defaults) are exactly the ones that drift.

The check is seen to fail before it is trusted (`a-check-must-be-seen-to-fail`): its extractor can miss a whole class of key silently, and printing what it found is how that shows.

Generating the reference from the code is the alternative where the reference has no hand-written prose; neither the occurrences nor the literature found settle which is better.

## When it does NOT apply

- **Readers that compute their key names** at run time, by string building or renaming a subset: extraction misses them. Recover the patterns where possible, or keep a written procedure for that part.
- **Examples that are not executable**: a prose example stays a written procedure, assembled and run by hand. An example written as an executable session can be held by the gate.

## What it costs

A check bound to how the reader is written, which breaks when the reader is refactored; tables that keep one shape so they can be parsed; and a document rewritten from the code once, which is slow and finds more than anyone expected.

## Where it came from

A hardware-bound service corrected about a dozen drifted defaults in a configuration reference in one audit: a number, a unit, a removed field, a renamed option.

A research repository (2026-09-26): a parameter reference printed, beside each parameter, the value from the sample configuration file, and a reader took it for the default. Two parallel readers of one open-source server disagreed whether a feature was on; reading the initializer and the function that consumes the value, in the tagged release, settled it: the flag was on, and its thresholds made it do nothing.

A renderer whose content is data files (2026-09-28): rewriting a format reference from the code found tens of contradictions across a handful of documents written from earlier documents: a key the schema does not take, a statement that unknown top-level keys are ignored where the schema fails them, wrong defaults, a parameter documented that nothing applies. A new audit check compares each documented table with the keys the schema or the reading function takes, and was seen to fail on altered copies, a renamed key reported in both directions. Its first draft silently missed every key containing a digit, caught only by printing what the extractor found, an occurrence of `report-coverage-before-findings`.

A web service (2026-10-04) had a structural audit that failed when a setting read without a default was missing from the committed configuration template. When the template was rewritten against the code, about a third of the settings the code reads were absent from it, all optional, and the template grew by about half. The audit had been green on its rule throughout; the rewrite found it, not the check. That bounds the remedy: a gate check works only over every setting the code reads.

## Literature

- **Rabkin & Katz, 2011, ["Static Extraction of Program Configuration Options"](https://doi.org/10.1145/1985793.1985812)** (ICSE 2011, pp. 131–140). *Checked 2026-10-05 against the full text.* In seven open-source programs, every program documented options that do not exist and left many read options undocumented; documentation is updated apart from the code and options removed by a rewrite stay documented. Their static extraction of the keys a program reads was more accurate than the human documentation in most of the programs, and was more often right where the two disagreed. The largest source of their analysis' errors was option names built by string manipulation. They also note that programs often substitute a default for a bad value silently. **What we take:** the drift in both directions, the remedy (hold the reference to the reader's keys), and the computed-keys boundary. **Where we go further:** the check runs in the gate, over optional keys too, and is seen to fail; and the occurrences show the undocumented class is the optional settings.
- **Python documentation, `doctest`**. *Checked 2026-10-05.* Its first listed use is checking that a module's documented examples still work as documented. **What we take:** the examples boundary is narrower than "examples cannot be checked": executable examples can.
- **Thomas & Hunt, 2019, *The Pragmatic Programmer*, 20th anniversary edition, Tip 13 "Build Documentation In, Don't Bolt It On"**. *Checked 2026-10-05 against the publisher's tips page.* Background only: documentation written apart from code is less likely to be correct and current.

Siblings in this base: `copied-instruction-claims-its-origin` (a copy starts false; this drifts from true), and `fail-closed-defaults` and `refusal-must-not-read-like-an-answer`, for the silently substituted default.

## Evidence

**Measured in three repositories:** about a dozen drifted defaults in one audit; tens of contradictions in a reference rewritten from its reader, and a check seen red in both directions on a renamed key; about a third of the settings the code reads missing from a template a required-keys check kept green. **One occurrence in a fourth:** a sample value read as the default, and a feature documented on that did nothing. Not measured: whether the check, once in the gate, keeps the drift at zero. The experiment: in a repository with the check, count the drift found by a full rewrite from the reader a release or more later.
