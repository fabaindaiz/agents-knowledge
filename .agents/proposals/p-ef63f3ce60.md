---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-ef63f3ce60
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.25
digest: 469d45b59078
kind: method
action: new
target: check-a-relayed-claim-before-reporting-it
lacks: a second repository
seen: "2026-09-29"
---

A claim about another repository's state, relayed from a delegated agent or inferred from an incomplete search, is checked first-hand before it is told to the owner or put into another agent's brief: a status line, a branch listing or a file read costs seconds, and a wrong claim sends the next agent, or the owner, to act on something that is not there. Stops applying to a claim the reporting agent verified and quoted with its evidence. Costs one read per claim.

## Evidence

In one meta-session two claims went out unchecked: a reviewer's statement that a file held the owner's uncommitted work, repeated into an update agent's brief (the uncommitted file was another one, which that agent found and protected), and two carriers declared not on the machine because a search of bundle folders missed them, which the owner corrected by naming them as the first to update. Literature: none.
