# Do stored preferences help? — ablation protocol

**Pre-registration for the usage ablation (design decision `d-5ed7e8-adbd1f`).** This file is written, and
committed, before any measurement exists. Every later change is appended to *Deviations* with its date and
reason; nothing above that section is edited after the first session is recorded.

This directory is not part of the bundle. It lives at the repository root, does not travel to carriers, and
is not listed in the bundle's `SHA256SUMS`. The data it measures is the user's own, local and consented
(`bundle.py usage show`); nothing here leaves the machine except a figure the user approves at a harvest.

## The question

A user who consents to the `full` level lets the tool store paraphrased preferences and apply them at each
session's start (`bundle.py usage brief`). Does that reduce how often the user must repeat an instruction,
and at what token cost? Context files have been reported to add cost without a reliable gain (see
`PROTOCOL.md`), so the prior is a small effect or none, and the cost is measured, not assumed.

## Design

| Element | Fixed now |
|---|---|
| Arms | `on`: `usage brief` prints the stored preferences and the session applies them. `off`: `usage brief` prints `(ablation: off)` and withholds them |
| Assignment | alternated per session by `usage brief` itself, from the last recorded arm; the agent does not choose |
| Unit | one coding session that ran `usage brief` |
| Recorded at close | `usage add ablation arm=<on\|off> repeats=N corrections=N ktok=N`, by the close |
| Size | at least 20 sessions per arm before any verdict; `bundle.py usage report` prints `insufficient data` below that |

## What is counted

Two readers given the same transcript must count the same. The counts are the user's side only.

- **Repeated instruction.** A user message that gives an instruction, or states a preference, the user
  already gave earlier in this session or in a previous one, whether in the same words or not. One count per
  message, however many instructions it repeats. A reminder the agent asked for does not count.
- **Correction.** A user message that rejects or reverses something the agent just did or said (an
  undone edit, "no, not that", a redone step). A new requirement, a changed mind about the task and an answer
  to a question the agent asked do not count. A message that is both a correction and a repeat counts once
  in each.
- **ktok.** The session's total tokens in thousands, input and output, as the host reports them at close.

The count is made at close from the transcript, by the agent, and listed to the user, who may change it.

## Verdict rule

Computed by `bundle.py usage report` from the records, the rule fixed here:

- `keep on` if the mean repeated instructions per session fall in `on` against `off` **and** the mean ktok in
  `on` is at most 110% of the mean ktok in `off`;
- otherwise `turn off by default`.

Corrections are reported beside it and decide nothing. A preference never applied in 90 days is a candidate to
stop storing, whatever the verdict.

## Threats

| Threat | Handling |
|---|---|
| The user knows the arm (the brief prints it) and may behave differently | Unavoidable and stated: a single-user trial cannot blind the person. Counts are of messages, not judgments of effort |
| Carry-over: a preference applied in an `on` session shapes habits in the next `off` one | Alternation keeps arms adjacent; carry-over biases the contrast toward zero, never toward a false gain |
| Small n: 20 sessions per arm is one user's weeks | The verdict is a default for that user, not a finding about users; a close call is reported as such |
| Sessions differ in task and length | ktok is reported per session beside the mean; no adjustment is made, and the spread is shown |
| The agent counting its own corrections | The count is listed to the user at close, who may change it |
| Preferences stored during the trial change the `on` arm | Reported: the number of preferences stored at each session is part of the record's context, not of the verdict |

## Deviations

None yet.
