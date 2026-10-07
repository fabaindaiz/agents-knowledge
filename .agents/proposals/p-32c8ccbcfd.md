---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-32c8ccbcfd
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.29
digest: 61942017fec6
kind: method
action: new
target: a-tracker-is-the-roadmaps-source
lacks: the wording in artifact 8 and the adoption table
seen: "2026-10-07"
---

When a host keeps its pending work in an external tracker, the method's roadmap does not duplicate it: it holds only what the tracker cannot (where the work stands, collisions between items, process and tooling items, what is blocked outside), and every item cites the tracker key it belongs to. Artifact 8 and the adoption table should say so, as the guarantee kept and the shape adapted.

## Evidence

Two carriers bootstrapped on 2026-10-05 chose exactly this for their roadmap, against a tracker the whole team uses; the team's ticket rules make the tracker the single place work is registered.
