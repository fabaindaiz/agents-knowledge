---
slug: "persist-inputs-derive-verdicts"
topic: "evolving-contracts"
claim: "Persist what was observed or chosen — and that it was chosen — and derive verdicts and defaults at read time, so a policy or default change reaches everyone who did not choose, and a verdict heals when its cause goes away."
confidence: "reasoned"
phases: ["plan"]
check: "no stored verdict is read back as an input; after a policy change the recomputed answer reaches old records; a default changed in a test build changes nothing for a user who chose, and a stored preference carries its provenance"
about:
  - {do: "Store a flag such as blocked, eligible or high-risk", wrong_when: "the policy will change, or the cause will go away, and the stored verdict will not"}
  - {do: "Persist a user setting or preference", wrong_when: "the default is written to storage, so a later default change cannot tell who chose from who did not"}
rests_on: "Fowler's Event Sourcing; platform user-defaults design (registration domain)"
strength: "practice"
our_evidence: "design occurrences in three repositories"
---

# Persist inputs, derive verdicts

## Why it works

A stored verdict — `blocked`, `eligible`, `high_risk` — is a policy applied once and frozen. It is cheaper to read than to recompute, and it goes stale in two ways that nothing reports:

- **The policy changes.** A widened rule reaches only the records evaluated after the change; every record judged before keeps the old answer.
- **The cause goes away.** A subject who clears the condition, a device that stops being shared, a number that is reassigned — the stored verdict stays, and now needs its own un-verdict path, which is usually missing. Eventually someone who did nothing wrong is stranded.

Storing the raw observation (the observed attribute, the link, the balance) and judging at the decision instant makes both cases correct by construction: the current policy is applied to the current facts, every time.

### Preferences: a stored default is a verdict

The convenient way to save preferences writes every value, defaults included. From then on, the file says "X" for two different people: the one who picked X and the one who never opened the setting. A stored default is the product's answer at the time of writing, kept as if it were the user's input — a verdict frozen in storage. When the product later wants a better default, it has two bad options: overwrite X for everyone, taking the choice away from the first person, or leave it, keeping the second person on the old default forever.

Keeping defaults out of storage (a fallback layer consulted when a key is absent), or storing a flag beside the value that says it was chosen, keeps the two people apart. A new default then reaches exactly those who never chose, and a suggestion the product makes can change a value without counting as the user's decision. The flag holds only if it is written in the same step as its value: a setter that persists eagerly saves the intermediate state when a caller assigns a suggestion and only then clears the flag, and the suggestion is stored as a choice. Assign suggestions through a path that writes both together.

The same separation argues for two neighbours: repair stored data per key, so one malformed value loses that key and not the whole file; and never store live state that the platform owns (whether a window is fullscreen) — read it each time, so a request the platform refused does not leave a stored value lying.

## When it does NOT apply

- **The fact is only knowable at write time.** A property only the original event knows — "this event opened the order" — must be recorded then; it cannot be derived later. Persist at the grain the user acted, not the grain today's reader needs: two gestures logged as one kind cannot be split by any later derivation.
- **Results the users have already seen.** Recomputing with a new rule rewrites what they saw and may have kept. Version the rule by an effective date instead, keeping the old rule for inputs before it, and compare that date with the input's real time, never with a displayed or accelerated one (`derive-state-from-one-clock`).
- **The verdict must be frozen for audit**: "what the policy said at the time" is a record, not a cache. Store both, and mark the stored verdict as history, not as input.
- **Recomputing is expensive and the policy never changes.** Rare in practice; policies are exactly what changes.
- **Settings the user expects frozen at what they saw** — a price, a legal consent version. Snapshot those deliberately.
- **Values with no meaningful default** — they are always a choice.
- **Stores that already layer defaults under choices** by design; then the rule is simply not to copy the default layer into the persisted one.

## What it costs

A recomputation on every read, and the raw input kept — including values the current parser does not recognise yet, because the next policy may. For preferences: a flag per preference, or a layered store, and a migration that must infer intent for files written before the flag existed, whose inference can be wrong.

## Where it came from

A transactional service's abuse controls. A cached boolean verdict about a contact identifier meant that widening the policy would never have reached an identifier already looked up; the raw attribute is now stored and re-judged on every evaluation. A device-graph design wrote the rule down as storing the link and never the verdict, because a stored refusal would need its own reversal path and would eventually strand a customer whose cause had gone away, and it rejected caching a second verdict for the same reason. The boundary case came from the same code: whether an event repeated an earlier one had to be persisted at origin, because only the event that opened the order knows it.

The preferences form came from a second repository (absorbed 2026-09-24 from the retired `store-choices-not-defaults`), a client application whose settings live on the device. It wanted some content to open in a different display mode by default, and found no way to tell a stored default from a stored choice of the same value — and a preference silently overridden is worse than one that was never offered. It added a chosen-flag, and a suggestion changes the mode without setting it. The migration had to infer what was never saved: one value had always been the only default, so a file holding anything else had been set by hand — whoever changed it keeps their choice, whoever never did gets the new behaviour. The same store repairs per key (a wrong-typed value loses that key and keeps the rest) and keeps live window state out of its defaults list, reading it every time.

A third repository, an application with an on-device test suite, gave both forms of the boundary, 2026-10-03 and 2026-10-04. A derivation began to depend on a per-user seed, and recomputing would have rewritten draws users had already seen and kept; the owner chose the seed only going forward, built as a cut-off date. In an accelerated demonstration build, whose virtual dates pass the cut-off within minutes, a demonstration user's later draws changed anyway — the date had been compared with an accelerated time — which was ruled by resetting that user at the next install. Separately, a new feature keyed on the first time each gesture was made could not be derived for two gestures the log records as one kind, because the reader of the day treated them alike; the plan must bump the record's schema or drop those two items.

The client of the preferences form, 2026-09-28: a suggested display mode was assigned through the setter, which marked it chosen and saved the file before the suggestion cleared the flag in memory. The file said chosen, memory said not; on the next launch the suggestion acted as the user's choice, and an automatic switch stopped happening. A probe on a restored user store showed both states, and a guard flag fixed it.

## Literature

- **Fowler, 2005, ["Event Sourcing"](https://martinfowler.com/eaaDev/EventSourcing.html)**: "Capture all changes to an application state as a sequence of events." *Verified 2026-09-23 against the article.* **What we take:** state as a function of facts. **Where we differ:** narrower — it is *decisions* that go stale where facts do not, and a system can keep its ordinary storage and still refuse to store verdicts.
- **Apple, ["About the User Defaults System"](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/AboutPreferenceDomains/AboutPreferenceDomains.html).** Preferences are looked up through a list of domains; the registration domain, which holds the defaults an application registers at launch, is **volatile** and consulted last, below the persistent application domain. *Verified 2026-09-22 against the archived Apple developer page.* **What we take:** defaults as a non-persisted fallback layer — the structural form of the preferences half. **What we add:** the chosen-flag for stores that cannot layer, and the migration that infers it.
- **Not consulted:** the effective-dating and bitemporal literature, for the *results already seen* boundary.

## Evidence

**Reasoned, from three occurrences in one repository and one design occurrence, with its migration, in another**; no incident was counted in either. **2026-10:** a third repository added the effective-date boundary, with one slip it names (an accelerated clock), and a design occurrence of the write-grain boundary; the preferences client added a flag written apart from its value, reproduced on a restored store. Still no rate. What would measure it: at a policy change, count the records whose stored verdict disagrees with the recomputed one. For preferences: in any product that stores all values, count users whose stored value equals the shipped default, then change that default in a test build and count whose experience changes without their having chosen anything.
