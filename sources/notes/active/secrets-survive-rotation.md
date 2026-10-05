---
slug: "secrets-survive-rotation"
topic: "identity-and-naming"
claim: "Anything persisted that depends on a secret must survive the secret's rotation — store the verified result, not the signed token; key caches by the credential's fingerprint; and name stored things from what survives the rotation, never from the secret."
confidence: "reasoned"
phases: ["plan"]
check: "rotate the secret in a test environment: nothing stored stops verifying, no cache keeps serving"
about:
  - {do: "Store a token, a credential copy or a cache derived from a secret", wrong_when: "rotation is treated as an operation and turns out to be a data migration"}
rests_on: "none known"
our_evidence: "design decisions in one repository; one rotation incident, reproduced, in a second"
boundary: "Tokens meant to expire with the key, such as sessions and short-lived capabilities, and caches meant to be invalidated by rotation, where invalidation is intended"
---

# Persisted state survives secret rotation

## Why it works

Secrets rotate — on schedule, on exposure, on a staff change. Everything derived from one at write time and stored is bound to the version that existed then:

- A **stored signed token** (`<id>.<signature>`) stops verifying the moment the key changes, silently, for every record at once. Verify at the boundary, then store the verified identifier.
- **Copies of a credential** spread into records (one per receipt, per job, per tenant row) are all stranded by a rotation and all have to be found. Store a reference to the one credential, not the credential.
- **A cache keyed by name** keeps serving what the old credential produced. Keyed by a fingerprint of the credential, a rotation invalidates it by construction.
- **A name derived from the secret** renames everything stored under it on rotation, and a cleanup that deletes names no longer listed then deletes what was just written under the new name. Name stored things from what stays true across a rotation — a fixed salt and the item's own identifier — and keep one copy of the secret on the client: a second copy diverges, and an older key in it can win over the one just entered.

The failure is always the same shape: rotation is treated as an operational event, and it turns out to be a data migration nobody planned.

## When it does NOT apply

Tokens meant to expire with the key — sessions, short-lived capabilities — and caches meant to be invalidated by rotation, where invalidation is the intended behaviour.

## What it costs

Verification moves to the boundary, and the verified result is trusted afterwards, which has to be justified. Fingerprint-keyed caches miss once per rotation. A fixed name costs a little confidentiality: someone who can guess an identifier learns that the item is present.

## Where it came from

A transactional service, three occurrences: storing a signed device identifier would have made every stored binding stop verifying after a rotation, so the verified identifier is stored instead; a design with a copy of an integration credential per receipt was rejected because one rotation would strand every copy; and a token-service cache is keyed by credential fingerprint, so a rotation invalidates it by construction.

A second repository, a client that fetches encrypted packages and keeps them decrypted in local storage, 2026-09-24, met the first rotation incident. Package file names were derived from the key; after a rotation the client decrypted every new package into its local file, and the leftover sweep, looking for names no longer listed, deleted that very file, leaving an empty library. Reproduced before fixing, and caught only because the owner asked whether a new key would still update correctly: no test covered rotation. In the same fix, the key lived in two client stores, and an older key in one won over a newly pasted one on the next load. Names now come from a fixed salt and the item identifier, and one store is written by both paths; measured in two browser engines (a rotation, then a reload, then a wrong key followed by the right one).

## Literature

None known that states it this way. It is adjacent to `derived-over-chosen-identifiers`: what is persisted should depend only on what stays true.

## Evidence

**Reasoned, from three design decisions in one repository and one rotation incident in a second** (2026-09-24), reproduced before the fix and its remedy checked in two browser engines; no rate, and the first repository's decisions still have no rotation run. Literature for the derived-name form was not consulted. What would measure it: rotate each secret in a staging environment and count the stored records that stop verifying or the caches that keep serving.
