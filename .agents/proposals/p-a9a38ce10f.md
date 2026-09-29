---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-a9a38ce10f
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.23
digest: 34bcc0be3390
kind: knowledge
action: extends
target: derived-copy-goes-stale-silently
lacks: a second occurrence
seen: "2026-09-28"
---

a test suite that imports the generated copy of a tool tests the previous build, not the source being edited; test the original and let the build check the copy

## Evidence

In a repository whose tools are generated into a release folder, the tests loaded the release copy: edits to the original tool stayed untested until a rebuild, and a rebuild was not allowed while an experiment was reading that folder. Literature: the note's own
