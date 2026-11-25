# Plan: <the work, in a few words>

<!-- The template of a plan whose state is shown as a page (`d-5ed7e8-09facc`). Keep these sections and their order;
`python3 .agents/tools/bundle.py plan page <this file>` renders them, never by hand. Republish the page at a pause, at
a close, and when the owner asks. A section with nothing to say keeps its heading and says "none". -->

State on YYYY-MM-DD: <one or two lines: what the owner has in hand now, and where each lane stands>.

## The question now

**<The answer to the question that matters to the owner now, in one line: how far from the next thing they can
try.>**

1. **<step>**: <state and what is left, with its estimate>.
2. **<step>**: <...>.

Note: <what that gives the owner, and what comes after it>.

## Where we are

- **<area or lane>:** <where it stands, with the commits that hold it>.

## Device runs

| Version | What ran | Result | What it is |
|---|---|---|---|
| <the version tried> | <the suite or check> | <passed/total> | <the cause, and the fix's state> |

## Milestones

- **<id>** · <what the owner can try> · <done | running | waiting | blocked> — <what is done, what is left, its estimate>.

## Running now

### <Lane A · its subject>

- <task> · <state>
- → <the milestone this lane reaches>

## The owner's

- [<when: now | when you like | before X | to decide>] **<the thing>**: <what it takes from the owner>.

## Tasks: <group>

| # | Task | State | Milestone | Est. (min) | Actual (min) |
|---|---|---|---|---|---|
| 1 | <task> | <done | running | waiting | blocked> | <id> | <estimate> | <actual, once landed> |

Calibration: <the ratio the earlier plans measured, actual over estimate, or "uncalibrated">.
