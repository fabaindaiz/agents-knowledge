---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-0ddd2bc888
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.27
digest: 6e4d974b1cce
kind: method
action: extends
target: a-filtered-gate-cannot-block
lacks: "nothing: an occurrence in the home"
seen: "2026-10-05"
---

A coordinator that chains a commit on a gate is as exposed to the filter trap as a delegate: the home piped its own check through a tail filter, the pipe returned the filter's status, and a commit landed while the check reported stale generated files. The rule already admitted for carriers holds for the home's own sessions, at the same moment: when the commit command is typed.

## Evidence

The bundle's home, during a release meta-session: the check reported three generated files stale after an intake, the output was read only after the commit landed, and a follow-up commit regenerated them. Caught by reading the output, not by the chain. A delegate in another repository made the same slip the same day and recorded it.
