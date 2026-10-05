---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-2b25ab65ae
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.29
digest: 53522b869add
kind: method
action: extends
target: register-resolves-a-worktree-to-its-repository
lacks: a fix with a test
seen: "2026-10-05"
---

`release.py register` given a temporary worktree of a carrier's branch writes the worktree's path into the machine's manifest, both in the list of carriers and in that carrier's record, so the next read-only command looks for a folder that will be deleted. It should resolve a linked worktree to its main repository's path, or refuse a path outside it.

## Evidence

The second occurrence, in the home's meta-session of 2026-10-05 on another machine: four carriers whose bundle branch was not the checked-out one were updated in scratch worktrees, and registering them added four scratch paths to the list and four records; the manifest was restored by hand from a backup taken before.
