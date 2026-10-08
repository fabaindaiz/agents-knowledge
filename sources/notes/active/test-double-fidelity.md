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
cues: ["mock", "stub", "fake", "monkeypatch", "patch", "magicmock", "responses", "vcr", "contract test", "network access", "socket", "test fixture", "httpx mock", "return_value", "side_effect"]
---

# Test double fidelity

## Why it works

A fake is a second implementation of the dependency's semantics, written quickly by someone who needed a test to pass. Wherever it is more permissive than the real thing — it ignores a projection, merges where the real one replaces, accepts a call the real one rejects — the test asserts against a world production does not have. The test is green, it does assert, and it is wrong. This is different from low-quality coverage: the assertion is present; the ground under it is fictional.

The failure has recognisable forms:

- **Ignored arguments.** A fake that ignores a field mask returns the whole document, so a test "proves" a code path production can never reach.
- **Different semantics.** A fake that replaces nested maps where the real store deep-merges, or the reverse.
- **The wrong method stubbed.** The stub overrides a method the code no longer calls; it is never consulted, and the test asserts the absence of the behaviour it is named for.
- **Errors swallowed by the code under test.** The code's own handling catches the failure the double caused, and the suite passes for the wrong reason.
- **A neutral default on the interface.** An interface method given a default that answers "nothing" lets every double inherit that answer while the real implementation answers something. Leave it abstract, so each double must answer; the main fake can derive its answer from its own data.
- **The original object kept.** An in-memory store hands back the object it was given; the real one hands back its own representation (a timestamp without its zone, truncated to its precision), so a comparison that never matches against the real store matches against the double.
- **One shape for every answer.** A double that returns a body for every call cannot show that the client fails on a specified empty success; a local server that answers exactly as the specification says can.

**The harness and the development runtime are doubles too.** A harness health check that asks only whether an emulator answers passes one whose guest clock is hours behind the host, and every reader that filters by time then sees nothing while the actions land: check the harness clock against the host before such a run (`derive-state-from-one-clock`). A headless renderer is a double of the screen — stub font metrics, no colour, no animation — so a constant calibrated against it is calibrated against fiction: carry the datum on something that is not a pixel (an accessibility description the test can read), move the arithmetic into a pure function, and measure an animation over a recording. And the editor's runtime is a double of each export target: an export audit asks what the engine does differently per target and measures each answer on the real export.

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

**2026-10 — six more forms, in four repositories.** The app repository above, again: a harness health check passed an emulator whose guest clock was hours behind the host, several times within days; a device run hung after the host had slept, a measurement run was lost, and after a snapshot restore an end-to-end walk read no events while its taps landed. It is written in that repository's device guide, not yet in its health check. A device-bound application: a settings-callback double recorded a value while the real callback changed the display density, the entire cause of a defect, so the test could not fail; and in one session three green-but-blind rendering cases — colour, animation, and where a line breaks, the stub metrics laying text out at about two and a half times the font size — a second repository for the rendered surface as a double. The no-default rule was then applied on purpose to a new data method, so every one of several doubles had to answer it. The interactive client whose local server is counted above, 2026-09-25: an audit of export-only behaviour found the browser target playing audio as decoded samples by default, so the reported position ran about a second behind, froze after each seek, and decoded memory grew about sevenfold over a handful of items; the same pass found a request with no timeout and a delete that fails on one desktop system while the file is held open. A web service, 2026-10-01: a cache keyed on a remote timestamp missed on every run because the store returns timestamps without their zone and truncated, a defect that appeared only in the test against a real database (the comparison is counted in `same-answer-or-refuse`); and its panel client failed on every bodyless success, which contract tests against a specification-faithful local server caught and a double returning a body for everything would not have (counted in `retry-over-irreversible-effect`).

**Reasoned: the occurrences are counted, the rate is not.** What would measure it: run each fake's test cases against the real dependency in an emulator and count the disagreements.
