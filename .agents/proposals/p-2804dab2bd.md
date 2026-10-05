---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-2804dab2bd
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.29
digest: 61942017fec6
kind: method
action: new
target: carrier-linters-exclude-the-bundle
lacks: the wording in the bootstrap and update
seen: "2026-10-05"
---

A carrier's own linters and ratchets read the committed `.agents/` like any other code: a lint ratchet over every file counted the bundle's tool as new violations the moment it was committed, and an editor permission rule cannot deny a folder while allowing two files inside it. The bootstrap and update should tell the host to exclude `.agents/` from its linters and ratchets, and give the permission rules as a list of the release's paths.

## Evidence

In one bootstrap the commits that added the bundle failed the host's lint ratchet until a later commit excluded the folder; in another, the permission denies for the release had to be written path by path.
