---
slug: "absence-is-a-third-value"
topic: "failure-behaviour"
claim: "Keep \"absent\" distinct from false, from empty and from unreadable, and route every reader of a missing field, the query engine included, through one meaning stated once."
confidence: "reasoned"
phases: ["implement"]
check: "count records missing the field; every reader (query, worker, view) gives them the same meaning, and a malformed value refuses instead of reading as absent"
about:
  - {do: "Read a boolean or optional field from a schemaless store, an API or a configuration file", wrong_when: "each reader collapses \"missing\" into its own value, or a malformed value is read as absent"}
rests_on: "SQL three-valued logic"
strength: "settled"
our_evidence: "occurrences in at least six repositories; no count"
boundary: "Fields the schema requires at write time, where making absence impossible is the fix"
cues: ["is none", "is null", "missing field", "optional field", "default false", "get with default", "null vs empty", "isnull", "coalesce", "key missing", "undefined", "not set", "schemaless", "exists clause"]
---

# Absence is a third value

## Why it works

A boolean read from a schemaless store, an optional API field or a sparse log has three states: true, false, and never written. Code collapses the third into one of the others by default — `get(field, False)`, `if not doc.get(field)` — and the collapse is invisible until the distinction matters:

- **It destroys denominators.** "What share of users opted in?" needs the users for whom the question was answered; counting "not recorded" as "no" deflates the rate.
- **The engine and the code disagree.** A query filtering `field == false` skips documents where the field is missing, while the application reads missing as false — or, worse, as the dangerous value. Whatever is left implicit fails open on one side. With more readers it multiplies: a not-equal query matches the documents that lack the field, a worker defaults it to the safe value, a view to the dangerous one, so one record is *did nothing* to the component that ran it and *wrote something* to the one that decides what may be undone. Name the meaning of absence once, in one predicate that only an explicit value passes, and route every reader, the query included, through it.
- **"No document" and "document without these fields" become the same empty value**, and code that only means to tolerate missing fields also tolerates a missing record — then writes derived state for an entity that never existed.
- **A log that records only one outcome** implies the others do not happen. A per-reason counter that writes only the reasons that fired cannot show a rule that stopped firing: absent is not zero. Declare every reason up front and write its zero.
- **Malformed and unreadable are not absent.** A loader that skips a value of the wrong type turns a typo into a missing setting, and for an optional feature *missing* is the legitimate way to say *off*: the typo ships as a disabled feature, with no error. A format that retypes values on its own makes this common (a YAML 1.1 loader reads an unquoted `10:30` as the base-60 integer 630 and `09:30` as text). A reader that cannot read a record, because it is newer or the wrong shape, and treats it as missing lets a writer create again what should exist once. A value present but malformed refuses, at boot for configuration, naming the key and never the value, which may be a secret; an unreadable record is reported as unreadable; an explicit empty or null is given a meaning on purpose; and a parser is tested with values from every lexical class the format retypes, not only the ones a developer would type.

Keeping absence explicit — an optional type, a tri-state, an explicit `false` written at creation, a separate "not found" — makes the question "what does missing mean here?" answered once, on purpose.

## When it does NOT apply

Fields required by the schema at write time. That is the real fix (make absence impossible), and where it is available the tri-state is unnecessary. Likewise the lexical-class tests are not needed where the format does not retype values (JSON, environment strings, a YAML 1.2 core schema) or a schema names each key's type.

It does **not** stop at fields. A reference whose target has gone is a third state between "present" and "empty by choice", and collapsing it into either lies: shown as empty it hides what was lost, dropped silently it cannot be seen or removed. Keep with each reference the last label seen for its target, so a dangling one can still be displayed and taken out.

## What it costs

Optional or tri-state types wherever a value crosses a boundary; writing `false` explicitly; backfilling existing records so query filters and code agree. One schema or explicit type check per optional key, and an operator who never quoted a value now meets a refusal at boot.

## Where it came from

A transactional service: a client-reported flag kept three-valued on purpose, because collapsing absent into false would have deflated the rate it fed; an equality filter that skipped documents missing a status flag while the rest of the code read missing as the restrictive value, so leaving the meaning implicit failed open on one side; a read option that returned "no document" and "document without these fields" as the same empty value, so a refused registration wrote derived state for an account that never existed; and an access history that recorded only one kind of refusal, and so implied that only that kind ever happened.

A client application that keeps users' lists on the device met the reference form. An empty list and a list whose items the build no longer has are two different silences: a menu with no entries because content is missing cannot be told from a menu that failed to load, so the first says in words that it is empty and the second falls back to the whole library. An ordering that does not contain the current item is not an order, and falls back too. Later each list kept the last name seen for every id, so an item whose file was deleted still shows, dimmed, named and removable — checked with a probe: the missing row drawn dimmed, its name surviving a reload, the order holding the one item that remains.

A release tool met it in a lookup, reproduced by an adversarial review on 2026-09-28: a table of what each repository offered defaulted a missing key to an empty list, so a repository a gathering step never reached read as one reached that offered nothing. The guard before a conversion tested only for the missing value, passed, and the conversion deleted that repository's unsent records, which survived only in a backup. The fix keeps "not reached" distinct from "nothing found" all the way to the guard.

## Literature

SQL's `NULL` and three-valued logic are the standard statement that unknown is not false. No specific paper known on the query-engine / application disagreement. A document store's own documentation states that a not-equal query also selects documents without the field (checked by a carrier, 2026-10-04). The YAML 1.1 integer type defines base 60 with a pattern that a leading zero escapes, and YAML 1.2 removed many of those implicit typing rules (checked by a carrier, 2026-10-04). Prometheus's instrumentation guidance says to export a zero for every series known in advance, so that a missing series is not ambiguous (checked 2026-10-05). **Sibling in this base:** `absent-constraint-widens` — there absence widens a query; here absence changes a meaning.

## Evidence

**2026-10-03 — a template's empty default, in the bundle's home.** Four carriers on an old layout held their own fields in several headers; one header kept the template's empty lists while the others held between seven and fourteen recorded decisions. Settling them as two peer values would have taken the empty lists and erased every decision; "never filled" was kept apart from "deliberately empty" up to the step that merged them, and the full lists were carried.

**2026-09-22 — malformed is not absent, in an edge service.** A fail-open rule, that a change in the shape of the remote answer must never disable the fleet, was implemented for absent fields only. Most of the probed type changes still raised, reached the same handler and disabled the device; a separate branch for an unreadable answer was the fix. This folds the queued `tolerant-of-absent-is-not-tolerant-of-malformed`.

**2026-10-01 — a counter that writes only what fired, in a repository building data artefacts.** A per-rule drop ledger written into each built artefact listed only the rules that had dropped something, so the case it existed for, a rule silently no longer firing, showed nothing. It was found by building a sample and reading its metadata, not by a test.

**2026-10-03 — unreadable read as absent, in a client application.** An older build read every row of an append-only log as unknown, concluded that its genesis event did not exist, and appended a second one. The version half of this occurrence is `a-version-bump-spends-the-forward-compatibility-it-was-protecting`.

**2026-10-04 — four readers of one flag, and a loader that swallowed a malformed value, in a web service.** A job's free-form payload carried a boolean deciding whether it acted on a remote host or only simulated. The lookup of the last job that wrote used a not-equal filter, which matches jobs without the field; the worker defaulted it to simulate; the rollback rules and two templates defaulted it to real. Only hand-made or older records lacked it. One predicate, real only when the flag is explicitly false, now serves the query, the worker, the service and the views, with a test that a flagless job is a simulation everywhere and a count of stored jobs without the flag before deploying. In the same service an optional clock-time key was read by a YAML 1.1 loader that dropped any non-string value: every unquoted time with an hour from 10 to 23, more than half the day, became an integer, was skipped, and the schedule never ran, while unit tests written with early-morning times passed. A whole-branch review found it by reading. The key now refuses a non-string value at boot, naming only the key; what an empty value should mean is still open there.

**Reasoned, from occurrences in at least six repositories** (the reference form, observed with a probe but not counted; the lookup form, reproduced and fixed with a test; the loader form, measured on the repository's own loader). What would measure it: for each boolean in a schemaless store, count documents where it is missing, and compare what the query layer and each reader conclude for them.
