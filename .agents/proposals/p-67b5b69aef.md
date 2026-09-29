---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-67b5b69aef
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.25
digest: 469d45b59078
kind: method
action: new
target: review-each-carrier-in-execution-before-propagating
lacks: a second occurrence
seen: "2026-09-29"
---

Before a release is carried to repositories that have their own procedures, one read-only agent per carrier reads that carrier's own definitions of work (task tracker, plans, review, commits, logs, gate, audit) beside what the release makes an agent do there, and classifies every meeting point as a conflict in execution, a broken reference, an unstated precedence or a difference of wording only. The release's tests and a carrier's `verify` prove the files; only this reading proves the carrier still works as it defines itself. Stops applying to a release that changes no wording an agent follows and no path a carrier references. Costs one read-only agent per carrier.

## Evidence

In one meta-session a release passed every tool test and every carrier's `verify`, and was already committed in six carriers, when the owner asked whether it contradicted any repository's own procedures. The per-carrier review found no conflict in default behaviour, but a stale line in the always-loaded index that pointed learnings at a removed file, three method passages that could override a repository's commit and history rules when pasted, and, in the carriers not yet updated, audits that the release would turn red and checks it would turn vacuous. A patch release fixed the bundle's part the same day, and each carrier's part was fixed in the commit that carried it. Literature: none consulted; it is an integration test run by reading.
