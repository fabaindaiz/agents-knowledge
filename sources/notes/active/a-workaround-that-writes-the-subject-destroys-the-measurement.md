---
slug: "a-workaround-that-writes-the-subject-destroys-the-measurement"
topic: "measurement"
claim: "On a live system, a workaround that writes the very thing under diagnosis destroys the measurement, because the convenient workaround is usually the candidate fix itself: read-only diagnosis stays read-only until the cause is established, and every probe verifies its target and counts its own writes."
confidence: "reasoned"
phases: ["debug"]
check: "before the cause is named: each probe is read-only, or its writes are listed; the value is read once with nothing else writing; and any probe whose target may not exist verifies the target first"
about:
  - {do: "Diagnose a live system whose state keeps going wrong", wrong_when: "the quickest way to get a reading is to set the suspect value, restart the service or install a missing tool — each of which is the candidate fix"}
  - {do: "Write a probe that reads a value through a control interface", wrong_when: "the probe writes as a side effect, or its intended target does not exist and the write falls through to the subject"}
rests_on: "the probe effect and the Heisenbug: measuring a system alters it (named, their primaries unread)"
strength: "one encyclopaedia article read at the source, whose own primary references were not read; the case here, where the probe is the candidate fix, is in none of it"
our_evidence: "two repositories, two incidents, one of them with a watch of hours after the fix"
boundary: "A state already lost (nothing is left to measure, so the workaround is free) · a reproduction on a copy nobody else depends on · a cause already established, where the workaround is the fix and is applied as one"
cues: ["live system", "production", "read-only session", "probe", "diagnose", "it keeps resetting", "set it by hand", "restart it", "install the tool", "workaround", "intermittent", "disappears when I look", "watcher", "root cause"]
---

# A workaround that writes the subject destroys the measurement

## Why it works

A diagnosis is an argument about a state that went wrong, and that state is the only evidence. What
makes this trap different from ordinary observer effects is that **the convenient workaround and the
candidate fix are the same action**: setting the suspect value by hand, restarting the service,
dropping the missing tool into place. Each of those sounds harmless, and each erases exactly what
would have proved the cause. Worse, the measurement afterwards looks fine, so the investigation
concludes with a fix nobody can tell from a coincidence.

A probe that writes is the same error one level down. A probe whose intended target does not exist
can fall through to the subject itself, and then the reading mixes the defect with the
investigation's own writes — which can only be separated by stopping every probe and watching the
value alone.

## When it does NOT apply

Where the broken state is already gone there is nothing left to destroy, and the workaround is
free. On a copy nobody depends on, write whatever is needed. And once the cause is established,
the workaround is no longer a workaround: it is the fix.

## What it costs

A read-only path for each reading, which sometimes means using what the runtime already provides
instead of installing anything; and a slower investigation, because the cheapest reading is usually
a write.

## Where it came from

Two repositories, independently. In a read-only session against a live device, the fastest way to
download a missing diagnostic tool was to set the resolver by hand — which was the suspected fix, so
the state under observation would have been gone, and placing a binary inside a running image was a
write the session had been told not to make. A fixed read through the language runtime already
present was used instead, and a reboot experiment settled the cause: a boot race, not a
configuration error. In a long-running service, a stored level kept dropping to one fixed value;
the agent's own probes wrote that level, and one probe played a test signal that fell through to the
very output under diagnosis because its intended target did not exist. Two real causes were found,
but the first rounds mixed them with the investigation's writes.

## Literature

**Established for observation, and silent on this case.** The *probe effect* — "an unintended
alteration in system behavior caused by measuring that system" — is the general phenomenon
(verified at the source: the encyclopaedia article, which cites a 2001 conference paper on event
manipulation for nondeterministic shared-memory programs; its own primary reference, J. Gait, "A
probe effect in concurrent programs", *Software — Practice and Experience* 16(3), 1986, was found
only as a bibliographic record, **not read**). The same idea in debugging is the *Heisenbug*, a bug
that appears to vanish when examined, used in the 1985 Tandem report on why computers stop
(bibliographic record only, **not read**; the term predates that use). A 1989 ACM survey on
debugging concurrent programs is quoted secondhand as stating that any attempt to observe a
distributed system may change its behaviour — **secondhand, not verified at the source**.

What the found literature does **not** cover is the case this note is about. The article describes
observation changing timing and says nothing about a workaround applied in order to get a reading;
its nearest remark — that a probe may cause unexpected failures or unexpected fixes — treats those as
side effects rather than as the candidate remedy. That is an absence in one encyclopaedia article, not
a surveyed field: a reader who needs the stronger claim should read the 1986 paper, which this note
has not. **So the general claim is
established and the boundary is ours:** when the probe and the fix are the same action, the cost is
not perturbed timing but a destroyed argument.

## Evidence

**Two incidents, two repositories, 2026-10-15, both on live systems and neither reduced to a
number.** Both are counted elsewhere too, for a different half of what they show, and each of those
notes says so: the first also extends `count-both-sides-and-use-a-control-window` (the control's
margin), the second `a-request-accepted-is-not-an-effect` (a level replaced with no request). What is
counted **here** is the investigator's own writes, and nowhere else. The first was avoided before any write: the read-only instruction held, and the cause was
settled by an experiment (a reboot with both devices powered together) rather than by a reading. In
the second the error was made and then undone: once every probe verified its target and counted its
links before writing, and the probes were stopped while a watcher read the value alone, two causes
separated — a test suite reaching the real system through a missing guard, and a session manager
restoring a value shared by several streams of one program. After the guard, the restore opt-out and
probe hygiene, a passive watcher saw no drop for about two and a half hours.

What would settle it: on the next live diagnosis, record for each probe whether it writes, and
whether the cause was named before or after the first write. A count of diagnoses whose first
reading was a write would say how common the trap is; neither repository has it.
