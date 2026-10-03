---
slug: "test-double-fidelity"
topic: "verification"
claim: "A test double that accepts more than the real dependency makes the test pass against a fiction; check its fidelity rather than assuming it, and make tests fail closed on the real network."
confidence: "reasoned"
phases: ["tests"]
check: "a contract test runs the fake and the real dependency on the same cases; tests cannot open sockets"
about:
  - {do: "Write a fake, a stub or a mock for a dependency", wrong_when: "the double accepts more than the real thing, or the test can still reach the real network"}
rests_on: "*Software Engineering at Google* ch. 13; Fowler's ContractTest"
strength: "practice"
our_evidence: "occurrences; no rate"
boundary: "Pure-function tests with no double · doubles generated from the real implementation, or contract-tested against it on the same cases"
---

# Test double fidelity

## Why it works

A fake is a second implementation of the dependency's semantics, written quickly by someone who needed a test to pass. Wherever it is more permissive than the real thing — it ignores a projection, merges where the real one replaces, accepts a call the real one rejects — the test asserts against a world production does not have. The test is green, it does assert, and it is wrong. This is different from low-quality coverage: the assertion is present; the ground under it is fictional.

The failure has recognisable forms:

- **Ignored arguments.** A fake that ignores a field mask returns the whole document, so a test "proves" a code path production can never reach.
- **Different semantics.** A fake that replaces nested maps where the real store deep-merges, or the reverse.
- **The wrong method stubbed.** The stub overrides a method the code no longer calls; it is never consulted, and the test asserts the absence of the behaviour it is named for.
- **Errors swallowed by the code under test.** The code's own handling catches the failure the double caused, and the suite passes for the wrong reason.

The companion rule is about the other direction of infidelity. When the test configuration can point at real endpoints, **deny network sockets by default**: a test that slips its mock does not error, it succeeds against production — and in a system with physical or financial effects, it performs them. The guard itself needs a test, because an untested safety mechanism quietly stops working.

## When it does NOT apply

Pure-function tests with no double. Doubles generated from the real implementation, or contract-tested against it on the same cases.

**Blaming the harness on "it passes alone".** A harness is a double of the target too, and on a long-running one under load most surprises are the harness. But test pollution and real races also pass alone, so before convicting it: rerun the failure alone and again after the test that preceded it, look for state an earlier test left changed, and ask whether review can find an input that reaches the suspected race. On a fresh, idle harness the code is the first suspect.

## What it costs

Contract tests that run fake and real on the same inputs — the real side needs an emulator or the network — or faithfully re-implementing semantics such as projections and merges in the fake, which is real work.

## Where it came from

A transactional service, five occurrences: an in-memory store fake that ignored field masks, so a fixture reached a gate production could not; the same fake replacing nested maps where the real store deep-merges; a stub on a method the code no longer called; a synchronous stub standing in for an asynchronous method, which broke several tests and left half of a change unverified; and suites that passed because the code's own error handling swallowed a wiring failure. The same repository denies sockets in tests because a test that slipped its mock would perform real effects outside the test, and tests the guard against a reserved documentation address. An evaluation of that repository named the gap between the store and its double (indexes, contention) as its blind class.

## Literature

- **Trenk & Bly, ["Test Doubles"](https://abseil.io/resources/swe-book/html/ch13.html)**, ch. 13 of Winters, Manshreck & Wright (eds.), 2020, *Software Engineering at Google*: fidelity is the property that matters ("how closely the behavior of a test double resembles the behavior of the real implementation"), and "a fake must have its own tests". *Verified 2026-09-23 against the chapter.* **What we take:** fidelity as a named, testable property.
- **Fowler, 2011, ["ContractTest"](https://martinfowler.com/bliki/ContractTest.html)**: keep testing against the double, and periodically run separate contract tests against the real service that "check that all the calls against your test doubles return the same results as a call to the external service would." *Verified 2026-09-23 against the page; earlier wording here said "the same tests against both", which the page does not say.* **What we take:** the mechanism for checking fidelity.

## Evidence

**2026-09-28 — two more occurrences, in two repositories.** In the bundle's home, a check written for an input that arrives from elsewhere passed its test against a hand-built fixture and failed on every real instance of that input: the fixture lacked a list the real input carries, and an adversarial review found it before the release was tagged. In an interactive client, the local server a build was tested against differed from the production host in what it did to every response and in what the platform granted each origin. One mechanism: a double holds what its author thought of. Still no rate.

**2026-10-03 — two more, in an app repository with an on-device test suite.** The surface a rendering test draws on is a double: a test for gaps in scaled artwork passed on the test's own background and missed hundreds of gap pixels the production background showed, and two brightness tests measured the test window's background instead of the app's. Both now draw on the production background. The boundary above comes from the same repository, folded from the queued `suspect-the-harness-first`: about ten infrastructure incidents across nine sessions each first looked like a code failure (a graphics stall, a device-not-found that was a timeout, zero tests run, capture and suite timeouts that passed alone), four first readings of an observation were corrected by a system dump or a recording, and twice in the same period a failure that passed alone was not the harness: one test left a preference changed, and one race was real. The folded row held the first repository's occurrences: in an interactive client, several surprises in two days traced to the harness rather than the code — its clock state, the timing of injected input, what a capture included, a first measurement taken while still warming up. Luo et al., FSE 2014, on flaky tests, and Gyori et al., ISSTA 2015, on state-polluting tests, are cited from the proposal and *not checked against the source*.

**Reasoned: the occurrences are counted, the rate is not.** What would measure it: run each fake's test cases against the real dependency in an emulator and count the disagreements.
