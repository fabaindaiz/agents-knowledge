---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-330f16caed
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.23
digest: 34bcc0be3390
kind: method
action: new
target: isolated-review-by-default
lacks: "refused: already in the method"
seen: "2026-09-28"
---

the finding that an isolated review subagent run by default cost several times the session it reviewed is already the method's rule since 0.0.23 (review on request)

## Evidence

Two cost smoke tests of the same six tasks, the reviewer by default against on request
