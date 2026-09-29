---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-f99c1f6cc1
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.25
digest: 469d45b59078
kind: method
action: extends
target: gather-reads-the-remote-not-a-stale-checkout
lacks: a second occurrence
seen: "2026-09-29"
---

When a carrier's working copy is a history left behind by a rewrite, the session works on a new branch cut from the remote branch, never by resetting the old one: the old branch stays as it was, nothing is destroyed, and the result is pushed to the remote branch, which it extends without rewriting. Moving the old branch is the owner's step, afterwards.

## Evidence

In one meta-session a reset of three stale working copies onto their remotes was refused by the permission layer; a branch cut from each remote carried the update, and each was pushed onto its remote's main branch as a fast-forward. Literature: none.
