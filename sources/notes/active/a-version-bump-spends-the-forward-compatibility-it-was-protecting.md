---
slug: "a-version-bump-spends-the-forward-compatibility-it-was-protecting"
topic: "evolving-contracts"
claim: "Readers that ignore unknown fields let a record format gain fields with no version change; bumping a version that readers compare for equality makes every older reader refuse the whole record, every kind when one version covers all, so bump only for a change an old reader must not ignore, version each record kind, and treat held-but-unreadable as its own state."
confidence: "reasoned"
phases: ["plan"]
check: "an older reader given a new record still reads every kind it knows; a writer that cannot read an existing once-only record refuses to create another"
about:
  - {do: "Bump a format version, or add a field to a shipped record", wrong_when: "readers compare the version for equality, or a writer reads unreadable as absent"}
rests_on: "must-ignore and version substitution, W3C TAG 2007, RFC 6709; TLS version intolerance, RFC 8446"
strength: "established"
our_evidence: "occurrences in two repositories; no rate"
cues: ["schema_version", "version bump", "format version", "add field", "unknown fields", "ignore unknown", "version equality", "older reader", "record format", "backward compatible", "protocol version", "json field", "unsupported version", "once-only"]
---

# A version bump spends the forward compatibility it was protecting

## Why it works

A format whose readers ignore what they do not know can grow: a new field is skipped by every old reader and used by every new one, and no version number has to change. That tolerance is the format's whole capacity to evolve.

A version field that readers compare for equality is the opposite rule. The moment it is bumped, every older reader refuses the whole record, including the parts it understood. When one version covers every kind of record, the bump made for one kind refuses all of them. So a bump **spends** the tolerance the format was built on, and the cost is invisible when it is paid: it appears only when an old reader meets a new record, which for an artefact shipped inside an application, a downgrade or a second device on an older build, is later and somewhere else.

The refusal then meets a second defect. A writer that reads "I could not read it" as "it is not there" creates again what should exist once: a genesis event, a singleton, an initial record. Unreadable is a state of its own, between present and absent (`absence-is-a-third-value`), and a writer of a once-only record asks whether one is held at all, read or not, before creating it.

So: bump only for a change an old reader must not ignore; scope the version to the record kind it describes; and keep "held but unreadable" distinct from "absent" in every writer.

## When it does NOT apply

- **The change alters what an old reader already understands** (a security meaning, a unit): then refusing is correct, and a must-understand mark on the new item, or a major version with a stated substitution rule, refuses only what it must.
- **Readers apply a substitution rule** (any record with the same major version is accepted): a minor bump spends nothing.

## What it costs

A version per record kind, so more versions to keep and to test. Discipline when adding a field: it must be safe to ignore, or it is a breaking change made visible. And a writer that refuses to create on an unreadable record stops instead of carrying on, which on an old build means a feature that does not work until the build is updated.

## Where it came from

A repository with rebuilt data artefacts added two new field types over time without a version bump, deliberately, on the strength of must-ignore. An earlier codec bump had been accepted on the reasoning that it cost nothing at the time, and it stopped costing nothing once the artefacts shipped inside the application, where an old reader meets a new record. The repository recorded it as a decision ageing badly rather than as a mistake.

A client application keeps an append-only event log with one global schema version. A debug build older than the stored rows read every row of every kind as unknown, concluded that there was no genesis event, and appended a second one; a device test expected one and found two. A fresh-context review found it as a deferred minor before any public release. The fix is a version per kind, and the creating code asks whether a genesis row is held at all. Nothing was lost; it would have reached users through any downgrade, or a second device on an older build.

## Literature

- **W3C TAG, Orchard (ed.), 2007, "Extending and Versioning Languages: Strategies"** (editorial draft finding). *Checked 2026-10-05.* States Must Ignore Unknowns as good practice, and requires a substitution model for version identifiers for forward-compatible evolution, such as accepting any document with the same major version; a must-ignore default with an explicit must-understand mark is the selective form. It is an unapproved draft, cited for its statement of the practice. **What we take:** the mechanism and the boundary.
- **RFC 6709, Design Considerations for Protocol Extensions** (IAB: Carpenter, Aboba & Cheshire, 2012), §4.1 and §4.7. *Checked 2026-10-05.* A version field must come with a stated behaviour for unknown versions; assumed backward compatibility works only if old implementations accept higher versions without discarding them; where an extension is security-relevant, silent discard is unsatisfactory and must-understand marks are used. **What we take:** the claim and its boundary.
- **RFC 8446, TLS 1.3** (Rescorla, 2018), §4.1.2. *Checked 2026-10-05.* Many servers rejected a hello with a version higher than they supported, so TLS 1.3 freezes the legacy version field and negotiates in an extension. **What we take:** the cost of an equality-compared version is real enough that a major protocol stopped bumping its version field.
- **RFC 9170, Long-Term Viability of Protocol Extension Mechanisms** (IAB: Thomson & Pauly, 2021), §2. *Checked 2026-10-05.* Mechanisms that are not exercised are the ones that fail; version negotiation is tested for real only after deployment. **What we take:** the cost is invisible when it is paid, because the old reader's version path was never exercised.
- **Protocol Buffers, "Language Guide (proto3)"**, on updating a message type and unknown fields. *Checked 2026-10-05.* Adding fields is wire-safe; old binaries ignore new fields and keep them as unknown fields. **What we take:** must-ignore as the default of a widely used format with no message-level version at all.
- **Apache Avro specification, "Schema Resolution", "Object Container Files", "Single-object encoding"**. *Checked 2026-10-05.* A writer's field absent from the reader's schema is ignored, and the writer's schema travels with the data, per file or as a fingerprint per record. **What we take:** the per-kind remedy: the version that matters is the one attached to the record.

**Where we go further:** the literature states must-ignore and the need for a substitution rule. It does not treat a bump as a budget that is spent, invisibly until an old reader meets a new record, nor the duplicate a writer creates when it reads unreadable as absent.

## Evidence

**Reasoned, from occurrences in two repositories:** a codec bump whose cost appeared only once artefacts shipped inside an application; and one global version whose bump made an older build refuse every record kind and create a duplicate once-only record. No rate. The experiment: for each versioned record format in a repository, read a record from the newest writer with the oldest reader still in use, and record whether it reads the kinds it knows or refuses the whole record.
