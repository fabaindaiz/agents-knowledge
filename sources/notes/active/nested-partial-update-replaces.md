---
slug: "nested-partial-update-replaces"
topic: "failure-behaviour"
claim: "In a partial-update API a nested object is usually replaced whole; name the leaves (dotted paths) and assert on the keys of the emitted update, not only on its values."
confidence: "measured"
phases: ["implement", "debug"]
check: "assert on the keys of the emitted update mask, not only on values"
about:
  - {do: "Send a nested object to a partial-update or patch API", wrong_when: "the API replaces the object whole, and the test only checks the values that were sent"}
rests_on: "RFC 7396 / 6902 as contrast"
strength: "standards, not a claim"
our_evidence: "measured in three repositories, per client and per call"
boundary: "APIs with recursive merge semantics, such as JSON Merge Patch (RFC 7396), a deep-merge flag or a configuration key that says it extends · semantics are per API and per call, read or measured, never assumed"
cues: ["patch", "update mask", "field mask", "partial update", "nested object", "dotted path", "set merge", "field-set operator", "update_fields", "merge=true", "nested field partial update", "json merge patch", "put vs patch", "emitted update"]
---

# A nested partial update replaces

## Why it works

"Update" reads as "change what I sent and leave the rest". For top-level fields it usually is. For a nested map, many document stores, ORMs and REST APIs treat the map as one value: the update mask contains the parent key, and every sibling not in the payload is deleted. The request succeeds, the fields you sent are correct, and a test that checks those values passes. What is gone is what you did not send.

The defect is invisible in the values and obvious in the **keys**: an update whose mask is `['parent']` replaces the parent; one whose mask is `['parent.child']` touches one leaf. Asserting on the emitted keys turns the semantics into something a unit test can see without a network.

Layered configuration has the same semantics. A tool's configuration table set at a lower layer is a partial update of the effective configuration, and it usually replaces the inherited table of the same name rather than merging with it: the inherited entries vanish without a message. Tools that merge say so in a key of their own (an *extend* key); where there is none, repeat the inherited entries and say why beside them.

Two companions travel with it: a `None` in the new data must be filtered rather than written (it erases the stored value), and deliberately erasing a field goes through a separate, guarded function rather than through "update with null".

## When it does NOT apply

APIs with recursive merge semantics. **RFC 7396 (JSON Merge Patch)** merges recursively and uses `null` to delete; a deep-merge flag in a document store does the same, and so does a configuration layer whose key says it extends. Semantics are per API and per call — they are read in the documentation or measured, never assumed from the verb: one mapper call can replace a map when given a nested value and touch a single leaf when given a dotted key.

## What it costs

A single update builder that flattens nested data into leaf paths, and tests on its emitted keys. Some ergonomics are lost: callers cannot just pass the object they have.

## Where it came from

A repair job over a document store wrote a nested map as one value. It **destroyed the sibling fields of over a hundred thousand documents**: every sibling vanished together, with no intermediate case — the pattern that showed it was object replacement rather than a bad value. The fix was measured without network by reading the client's update mask: dotted paths gave one entry per leaf (`['parent.child', …]`), the map gave the parent alone (`['parent']`).

A second repository found the mirror image in its test double: the in-memory fake's merge-write replaced nested maps where the real store deep-merges, so tests and production disagreed about the same call.

## Literature

- **[RFC 7396, JSON Merge Patch](https://www.rfc-editor.org/rfc/rfc7396)**, and **[RFC 6902, JSON Patch](https://www.rfc-editor.org/rfc/rfc6902)**, as the contrast (7396: "If the patch is anything other than an object, the result will always be to replace the entire target"; 6902: an array of operations; *verified 2026-09-23 against both RFCs*): two standards with explicit, different nested semantics — which is the point; the semantics are a property of the API, not of the word "patch".
- No general source known for the failure mode itself.

## Evidence

**Measured in one repository:** over a hundred thousand documents affected, and the update masks read offline.

**Measured, 2026-09-22 — the semantics of one client, written down.** For one hosted document store's client library, its own update-mask builder was called offline on three payloads. A nested payload `{'a': {'b': 1}}` produces the mask `['a']` — **the parent field, so the whole map is replaced and its siblings are lost** — while the dotted payload `{'a.b': 1}` produces `['a.b']`. Two keys under one parent behave like the first. In that repository's write layer, the update literals use dotted keys, none carries a non-empty nested map, and the one nested value is an empty map, a deliberate clear: no accidental occurrence there, because where it means merge it writes a dotted path.

**2026-09-28 — layered configuration, one occurrence.** In a real-time signal-processing repository, adding a single per-file exemption table to the project's configuration replaced the build tool's inherited table of the same name, and on the order of a hundred lint errors appeared at once, because the inherited exemptions for tests were gone. Fixed by repeating the inherited entries, with a comment saying why. The tool's own documentation of the behaviour was not checked by the home.

**Measured, 2026-10-04 — a third client, and semantics per call.** In a web service over a document store, written through an object-document mapper and its driver, one run per update path against a disposable store, with a command listener capturing each emitted update: a partial model holding one key of one nested map, sent through the mapper's set call as the service's generic patch endpoint does, emitted the parent key alone, and the sibling was gone; a dotted path through the driver, and a dotted key through the **same** mapper call, emitted the leaf and kept every sibling. The repository had already moved its per-key writes to dotted leaves, but its generic patch endpoint still accepts nested maps and replaces them whole, and its tests patch scalar fields only — the note's *the test only checks the values that were sent*. About ten minutes, most of it starting the container.

The experiment stays queued for every other client in use. Run once per client, it documents the semantics for everyone after.
