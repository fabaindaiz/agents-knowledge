---
slug: "refusal-must-not-read-like-an-answer"
topic: "failure-behaviour"
claim: "A function given an input it cannot answer for refuses out of band — an exception, an exit status, an absent or error variant — instead of returning a well-formed value the caller cannot tell from an answer; and a consensus is taken only over the inputs whose evidence of presence passed."
confidence: "reasoned"
applies_if: "A lookup, a fingerprint, a parser, a tool call or a measurement can meet an input outside its domain: nothing to read, a name it does not know, a target it could not reach, a channel with no signal. Look at what it returns on that input, and at how the caller reads its exit status and its error stream."
phases: ["implement", "tests", "review", "debug"]
check: "for each kind of input outside the domain — empty, unknown name, unreachable target, no signal — a test or the gate sees the call refuse, never return a plausible value"
about:
  - {do: "Write a lookup, a fingerprint, a parser or a measurement that can be given something it cannot answer for", wrong_when: "it answers a default (the first item, the root, zero, the hash of nothing) that reads like a real result"}
  - {do: "Call a command-line tool or a remote client from glue code and read its output", wrong_when: "its error text arrives on standard output, or its exit status is dropped, so a failure is parsed as data"}
  - {do: "Take a median, a vote or any consensus over several sources", wrong_when: "sources with no signal are counted, and outvote the ones that answered once they are half or more"}
rests_on: "the semipredicate problem (Norvig 1992); Shore 2004, fail fast; Hampel 1971, the breakdown point"
strength: "well established"
our_evidence: "occurrences in four repositories; no rate"
cues: ["return default", "return none", "return 0", "raise error", "exit status", "subprocess.run", "stderr", "stdout parse", "median", "vote", "lookup not found", "empty list", "first item", "hash of empty", "check=true"]
---

# A refusal must not read like an answer

## Why it works

Some failures are not lost but disguised. The hash of empty input is a valid digest; the first frame of a sheet is a valid frame; zero is a valid count; a client's "device offline" message is a valid string. A function that returns one of these for an input it could not handle gives its caller, and the reviewer looking at the output, a plausible result — and it does so exactly in the cases where the input was wrong: a typo in a name, a path that held nothing, a target that did not answer. Nothing fails, and the wrong answer travels on as data.

The remedy is old and has a name: a function whose failure signal is also a valid return value has the semipredicate problem, and the cure is to signal failure **out of band** — an exception, an exit status the caller checks, an absent or error variant in the return type. In glue code the out-of-band signal usually exists and is dropped on the way: a tool that prints its errors on standard output, a helper that swallows the exit status, a bare handler that turns any exception into an empty result. Read the exit status and the transport's own error markers as a refusal, and keep "could not ask" apart from "absent" (`absence-is-a-third-value`).

**A consensus inherits the problem.** A median or a vote over every source counts the ones that had nothing to say, and a silent source returns whatever its method yields on noise. Once silent sources are half or more they decide the answer — the median's breakdown point is one half — and below that they still pull it. So screen each source's evidence of presence first (a level above the floor, two independent halves that agree) and take the consensus over the sources that pass; "the median is robust" is no reason to skip the screen. With too few left, the consensus itself refuses.

The cheapest enforcement is in the gate: one check per kind of reference that fails on a name the data uses and the lookup does not know, before it ships. `fail-closed-defaults` is the boot-configuration form of the same move (a missing setting answered with a working value), and `report-coverage-before-findings` names "a lookup falls through to a default" as one cause of a blind report; this note is the form at every function boundary.

## When it does NOT apply

- **A default for an unknown input that is the documented contract and visible as such.** A special-case object whose behaviour is the same in every context, or a fallback named in the interface and shown in the output, is an answer, not a disguise.
- **A runtime nobody can watch, where a refusal would only make the feature disappear.** There, fail visible with a substitute that names what is missing, and fail the gate on the same condition (`fail-closed-defaults`).

## What it costs

A check per kind of reference in the gate — about a minute of validation in one occurrence — and call sites that must now handle a refusal, which turns silent wrong output into visible failures somebody has to fix. Glue code grows exit-status and error-stream handling. A consensus loses the sources it screens out, and needs a rule for when too few remain.

## Where it came from

A data-analysis repository, 2026-09-22: a fingerprint over a path that held no documents returned the hash of empty input, which looks like any valid digest. It now refuses with an exit code.

A renderer whose visuals are data files, 2026-09-28: an animation lookup answered the first frame for a clip name its sheet lacked, and most of the data files carried the same misspelt name, drawing whatever happened to come first on the sheet. Nothing noticed, because the picture looked right. The same pass found four more of the family: a misspelt parent fell back to the root with only a console line; a reference to an effect node of the wrong kind painted nothing; a value track naming a missing node or property was ignored; and a documented command-line value the tool could not parse rendered nothing without a word. Each now fails the gate, and the data fix was pixel-identical. A code-review agent reading the lookup found the first; a documentation rewrite that checked each claim against the code found the rest.

The tool-glue form, in a device-bound application repository, 2026-09-28: a device-bridge client printed its offline error on standard output, the text was read as a device serial, and one device was counted as two. A settings read over a dropping connection reported every key as absent. An is-it-installed helper swallowed the exit status and reported the package missing, sending the reader to reinstall over a connectivity failure. A lock-held check matched a history section of a status dump and could only ever answer yes. In the same repository's measurement scripts, a bare handler turned a decoding error into zero entries, and a misremembered field name returned zero entries; the second was caught only because zero was implausible.

The consensus form, in a real-time signal-processing repository, 2026-09-28: in a multi-channel timing instrument, a channel that had stopped playing picked up another channel's harmonic and returned the cleanest result of the batch, with the smallest spread; each channel's relative level is now checked, and a silent channel is reported as not playing. A consensus took the median of arrival times over every channel, including those the microphone could not hear; with most of them unheard, noise set the median and the heard channels, which agreed closely with each other, were rejected. It is now taken over the channels whose two independent halves agree. A check written to catch a false absence itself reported no destination for every stream, because it read an identifier on the wrong object.

## Literature

- **Norvig, 1992, *Paradigms of Artificial Intelligence Programming*, Morgan Kaufmann, ch. 4.** Defines semipredicates (a failure value, otherwise a useful value), calls them error-prone where the failure value could be meaningful, and in ch. 5 returns to a matcher that cannot tell "failed" from "matched with no bindings". *Checked 2026-10-05 against the author's published text.* The general name and the families of remedy (exceptions, a status returned beside the value, option and result types) are the standard ones. **What we take:** the mechanism is known, and so is its cure. **Where we go further:** the forms the occurrences found — glue code that drops the out-of-band signal it had, and a consensus that counts the silent — and the gate check that makes each fail.
- **Shore, 2004, "Fail Fast", *IEEE Software* 21(5), pp. 21–25.** A failure should be immediate and visible; returning a default for a missing configuration key produces failures far from their cause; catch-all handlers belong only in one global handler that reports. *Checked 2026-10-05 against the article.* **What we take:** the debugging argument, and the bare-handler occurrence above is his warning.
- **Hampel, 1971, ["A General Qualitative Definition of Robustness"](https://doi.org/10.1214/aoms/1177693054)**, *Annals of Mathematical Statistics* 42(6). Introduces the breakdown point, the share of contaminated inputs an estimator tolerates before it can be carried arbitrarily far. *Checked 2026-10-05 against the abstract; the median's breakdown point of one half, the maximum, against a secondary source.* **What we take:** a majority of silent sources sets a median, by definition. **Where we go further:** below one half the median is still displaced (reasoned from the definition, not cited), so presence is screened first.
- **Fowler, 2003, *Patterns of Enterprise Application Architecture*, "Special Case".** A deliberate well-formed substitute for a missing value, fitting only where the special behaviour is the same everywhere. *Checked 2026-10-05 against the catalogue page.* **What we take:** the boundary above, not a contradiction.
- **Siblings in this base:** `fail-closed-defaults` (configuration at boot), `absence-is-a-third-value` ("could not ask" is not "absent"), `report-coverage-before-findings` (a lookup's default makes a report blind).

## Evidence

**Reasoned, from occurrences in four repositories; no rate.** Each occurrence is a defect found by reading or by an implausible number, not by a measurement of how often the disguise happens; in one, a whole family of the same defect turned up in one pass, and the gate check that now refuses each costs about a minute. What would measure it: in one repository, feed every lookup, parser and tool call within the gate's reach one input from each class outside its domain — empty, unknown name, unreachable target, no signal — and count those that return a well-formed value instead of refusing.
