---
slug: "a-request-accepted-is-not-an-effect"
topic: "distributed-correctness"
claim: "A request that a subsystem with its own policy accepts without error — a session manager, a daemon that rereads its configuration, an orchestrator bringing a service up — is not its effect: read the resulting state back after the request and after every event that re-runs the policy, and see that read-back fail on a planted diversion."
confidence: "reasoned"
phases: ["verify"]
check: "the resulting state (what runs, the route taken, the value loaded) is read back after each event that re-runs the policy, and the read-back was seen red on a planted diversion"
about:
  - {do: "Change a running system through a subsystem with its own policy", wrong_when: "success is taken as the effect, or the read-back runs before the policy re-runs"}
rests_on: "end-to-end argument, Saltzer, Reed & Clark 1984; RFC 9110 on 202 Accepted"
strength: "established"
our_evidence: "occurrences in two repositories; no rate"
---

# A request accepted is not an effect

## Why it works

A command that returns success says the request was taken. Whether anything happened is a different fact, owned by the subsystem that took it. Where that subsystem runs a policy of its own (restore what the user chose last time, follow the default device, keep the existing container while its definition looks unchanged, discard a configuration value it cannot parse), the request can be accepted and then dropped, overridden or left beside the old state, with no error and often no log line.

The override need not come at once. A policy re-runs on its own events: a device appears, a daemon restarts, a node is replaced. A read-back done right after the request passes, and the state changes later. So the read-back is repeated after each event that re-runs the policy, not done once.

What is read back is the effect itself, named by what identifies it: the identity of what runs (the image or build the running service reports), the route a stream actually takes, the value the daemon actually loaded (read from the kernel or the process, not from the file that was written). A read-back can fail in its own ways, by reading the wrong object or running before the triggering event, so it is seen to fail once on a planted diversion before it is trusted.

Neighbours in this base: `detect-by-observation-not-build-flag` asks what a device can do; this asks what a request did. `a-check-must-be-seen-to-fail` says a checker's own exit code is not its verdict; here the exit code belongs to the request.

## When it does NOT apply

- **Acceptance means completion by contract**: a synchronous interface whose acknowledgement is the effect, such as a committed transaction. The end-to-end argument itself allows the lower layer to take responsibility there.
- **Every request creates new state by construction**: a deploy that always replaces every instance cannot leave the old one serving, though it can still fail to start the new one.

## What it costs

A read-back after every request and after every event that re-runs the policy, which means knowing those events. The effect often has no cheap observable: a service has to report its own build, a route has to be queried from the subsystem, a loaded value has to be read from the process. And a read-back that is itself never seen to fail is one more green that proves nothing.

## Where it came from

A repository with a real-time signal-processing service, a measurement loop and a browser control panel, four times. An output stream with an explicit target was moved by the session manager to a virtual output the moment that output appeared, because a saved default named it: no error, no log, one channel went silent and a feedback loop formed; the human's ear found it, and the first two fixes failed, one because its check ran before the triggering event, the other because it read the wrong object. A configuration value followed by an inline comment was read whole and silently discarded, and the daemon started anyway; a probe that read the kernel's own list, instead of trusting the restart, caught it. The session manager left a combined output at a low level, which is now set and read back at every start. A volume set on a remote device was read back, and its measured effect differed from the nominal step by about a third.

A self-hosted web service (2026-10): a local redeploy through a container-composition tool did not recreate the API container after its image was rebuilt under the same tag, and the old version kept serving while the command succeeded. It was noticed only because the panel still showed the old interface; a forced recreate fixed it. The repository's update script chains the same command and is presumed affected, not tested. The remedy is the same read-back: after every deploy, observe the identity of what runs, not the command's exit status.

## Literature

- **Saltzer, Reed & Clark, 1984, "End-to-End Arguments in System Design"** (ACM Transactions on Computer Systems 2(4)), on acknowledgement of delivery. *Checked 2026-10-05 against the authors' copy.* Knowing that a message was delivered is of little use; the application wants to know whether the target acted on it, since anything may happen between delivery and action, and the acknowledgement really wanted is "I did it". **What we take:** the claim in its original form. **Where we go further:** the target here is a local subsystem with a policy that can undo the effect later, so the read-back is repeated after each event that re-runs the policy, and the read-back is itself seen to fail.
- **RFC 9110, HTTP Semantics** (Fielding, Nottingham & Reschke, 2022), §15.3.3 "202 Accepted". *Checked 2026-10-05.* The request has been accepted but not completed and might never be acted upon; the response is intentionally noncommittal and ought to point at a status monitor. **What we take:** acceptance and effect are two states, and the protocol tells the client to poll for the second.
- **Kubernetes documentation, "Controllers"**. *Checked 2026-10-05.* Controllers are non-terminating loops that move the current state towards the desired state and report the current state back. **What we take:** in a declarative system writing the desired state is the request, and the effect is the observed status, reached later or not at all, which other loops may keep changing.
- **Vogels, 2008, "Eventually Consistent — Revisited"** (the author's publication). *Checked 2026-10-05.* Defines the inconsistency window and read-your-writes as a guarantee a system may or may not give. **What we take:** a single read straight after a write proves nothing unless that guarantee holds.
- **A desktop audio session manager's documentation of its settings**. *Checked 2026-10-05.* It stores manual routing choices and restores them when devices appear or after a restart, and can treat an explicit target as "follow the default". **What we take:** the first occurrence is documented policy, not a fault; the override fires on a later event.
- **The reference implementation of the container-composition specification**, its documentation of bringing services up. *Checked 2026-10-05.* It recreates a container when the service's configuration or image changed after the container was created. **What we take:** the second occurrence is a divergence of another implementation from the reference, which makes the remedy (observe the running identity) stronger, not tool-specific.

## Evidence

**Reasoned, from occurrences in two repositories:** four in the first (two silent overrides by a session manager's policy, one silently discarded configuration value, one effect a third off its nominal step), each caught only by reading the resulting state back; one in the second, an old container left serving after a successful deploy. No rate. The experiment: for each kind of request a repository sends to a subsystem with its own policy, read the resulting state back after the request and after each policy event, and count the disagreements.
