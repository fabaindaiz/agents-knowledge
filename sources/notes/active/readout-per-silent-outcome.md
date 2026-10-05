---
slug: "readout-per-silent-outcome"
topic: "measurement"
claim: "Where the runtime cannot be watched by those who must fix it, every outcome that would otherwise leave no trace gets a readout with distinct states — not wired, refused, empty, ok — present from the start, the build identity read back from the target among them; and each question put to whoever can see the target names the readout that answers it."
confidence: "reasoned"
applies_if: "The software runs where its developers cannot look: a device they do not hold, a user's machine, a host reached only through someone else. Look for outcomes that succeed or fail without a crash: a handler registered or refused, a store loaded or empty, an input accepted or dropped."
phases: ["implement", "verify", "debug"]
check: "the startup output names every silent outcome with its state before anything happens; the commit and its modified flag are read back from the target; every open question for the remote tester names its readout"
about:
  - {do: "Ship to a device, a user's machine or a host you cannot observe", wrong_when: "a handler was refused, a store loaded empty or an input was dropped, and nothing on the target says so"}
  - {do: "Ask someone who can see the target whether a change works", wrong_when: "the question names no readout, so the answer is an impression of a screen, about a build nobody identified"}
  - {do: "Count what a deliberate policy drops", wrong_when: "a threshold is put on a share the policy removes on purpose, so the check is red by design or loose enough to see nothing"}
rests_on: "Prometheus instrumentation practice; Ewaschuk 2016, *Site Reliability Engineering* ch. 6"
strength: "practice"
our_evidence: "occurrences in two repositories, one read on the real device; no rate"
---

# A readout per silent outcome

## Why it works

On a target nobody can watch, the failures that cost most are the quiet ones. A handler the platform refused to register, a store that loaded empty, a drawing with nothing to draw, a row dropped by a filter: none raises, none crashes, and to the person holding the device the result looks the same as a feature that had nothing to show. Crash reporting does not see them, because from the runtime's point of view nothing failed. Only an explicit readout reports them.

**Distinct states, present from the start.** A line that appears only when something happens cannot tell "worked and had nothing to do" from "never wired". One that shows *not wired*, *refused*, *empty* or *ok* from startup can, and a reader learns the difference without knowing the code. Metrics practice states the same rule: export a zero for every series known in advance, so a missing series is not ambiguous, and report failures beside the total of attempts. Per reason, the same holds: a counter that writes only the buckets that fired cannot show a rule that stopped firing.

**The first silent outcome is which build is running.** An installation time says only that something was installed. The commit and a modified flag, embedded at build time and read back from the target, are the only evidence that the build under test is the one meant, and every other readout is about that build.

**Pair each question with its readout.** Whoever can see the target is rarely the person who wrote the code, and "does it work?" gets an impression. A question that names the readout that answers it — "what does the store line say after a restart?" — gets a datum, and a brief of open questions, each with its readout, is what a remote session runs from.

`report-coverage-before-findings` is the batch-report form of the same rule (zero found against zero looked at); the *fail visible* boundary of `fail-closed-defaults` is its runtime-substitute form (a readout drawn crossed out rather than empty); `detect-by-observation-not-build-flag` governs what a guess about the target may do.

## When it does NOT apply

- **A runtime the developers can watch**, with a debugger, its logs and its screen in reach; there a readout is ordinary logging, and this note adds nothing.
- **Outcomes that announce themselves**: crashes, hangs and assertion failures, which field crash reporting already collects. The readout is for what raises nothing.
- **As a threshold, where a deliberate policy removes a known share.** No threshold is right for a share removed on purpose; the per-reason count ships as a readout, and a person reads it.

## What it costs

A line per outcome where the remote viewer can see it (a startup log, a status screen), designed before the first field run rather than after it; a build step that embeds the identity; questions written with their readouts, which is slower than asking. A readout a user may see must say nothing private.

## Where it came from

An interactive client whose only target its developers cannot observe, first offered at 0.0.20: each handler's registration reported as accepted or refused, a load and save status line per store, a diagram drawn crossed out instead of empty, and a brief of open questions each naming its readout.

A device-bound application, 2026-09-30, read on the real device: the startup log carries one readout per silent outcome — artefacts opened and rejected, the screen geometry with an explicit not-the-target flag, the time to ready — and the build identity (commit and modified flag) read back from the device was the only evidence of which build was running. The threshold boundary came from the same repository: the largest bucket of its drop ledger is a deliberate policy removing about a fifth of the rows, so the count per reason ships as a readout and not as a check. A per-reason counter there that wrote only the buckets that fired is counted in `absence-is-a-third-value`, and a readiness probe that answered ready while every upstream call was refused, in `fail-closed-defaults`; neither is counted again here.

## Literature

- **Prometheus documentation, "Instrumentation" (best practices) and the `absent()` query function.** Avoid missing metrics by exporting a default zero for series known in advance; report failures beside the total of attempts; a counter for every log line; `absent()` exists to alert on an expected series that is missing. *Checked 2026-10-05 against both pages.* **What we take:** distinct states and zeros from the start, as settled practice. **Where we go further:** the target here has no scraper; the readout is read by a person, so it is paired with the question it answers.
- **Ewaschuk (ed. Beyer), 2016, "Monitoring Distributed Systems", ch. 6 of *Site Reliability Engineering*, O'Reilly (sre.google/sre-book).** Errors include implicit failures (a success status with the wrong content) and failures by policy; white-box monitoring is distinguished from black-box. *Checked 2026-10-05 against the chapter.* **What we take:** a silent outcome is an implicit failure, and this note is the white-box choice made where only white-box is possible.
- **Go standard library, `runtime/debug`, `BuildInfo`.** The revision, its time and whether the tree was modified, embedded in the binary and readable at run time. *Checked 2026-10-05 against the package documentation.* **What we take:** build identity as data, offered by a toolchain.
- **Glerum et al., 2009, "Debugging in the (Very) Large: Ten Years of Implementation and Experience", SOSP.** Field reports of crashes, non-fatal assertion failures and hangs from a very large installed base. *Checked 2026-10-05 against the paper.* **What we take:** the contrast — field reporting collects the failures that announce themselves, and none of the ones this note is about.

## Evidence

**Reasoned, from two repositories; no rate.** The second supplied what the first lacked, an answer from the target runtime: the readouts were read on the real device, and the build identity was the only proof of which build ran. Not measured: how many silent failures a readout surfaces that a remote tester's impression would miss. The experiment: in the next field session on a target nobody can watch, put each question once with its named readout and once without, and count the answers that were wrong or unusable in each.
