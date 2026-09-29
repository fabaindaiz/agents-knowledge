---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-4a2be00ec2
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.24
digest: cd6ed6d9889a
kind: method
action: new
target: splice-dry-run-lists-what-it-removes
lacks: nothing
seen: "2026-09-29"
---

The meta-session procedure says the splice's dry run lists what would be written and removed, and the carrier's link-following step depends on that list; the command prints only counts. Either the dry run prints the files it would remove, or the procedure says how to obtain them.

## Evidence

In one meta-session, a dry run over two carriers on the old layout printed "would splice 105 files, remove 13" and nothing else; the thirteen paths were recovered by comparing the carrier's file list with the release's, by hand, to brief the per-carrier step that repoints links. Literature: none.
