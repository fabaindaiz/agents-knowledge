---
slug: "a-rewrite-cleans-only-what-refs-reach"
topic: "evolving-contracts"
claim: "Rewriting published history removes a line only from what branches and tags still reach: the forge keeps the old commits by hash and any clone that merges brings them back, so a published line is left and documented, and a rewrite, when chosen, is range-limited, leased and followed on every other machine."
confidence: "reasoned"
phases: ["plan", "review"]
check: "before any rewrite: every machine has pushed, the server's refs and a mirror are saved, the range starts at the first offending commit, each branch is pushed with a lease on its old hash, and every other clone rebases or re-clones instead of merging"
about:
  - {do: "Remove an attribution line, or any other line, from commits already pushed", wrong_when: "the old commits are assumed gone once the branch is rewritten, or another machine still holds unpushed work and merges the old history back"}
rests_on: "git-filter-repo's manual and the forge's documentation on removing data and on commit pages"
strength: "documented behaviour, tried in a sandbox"
our_evidence: "one repository rewritten once to this rule; the rest of the procedure from a sandbox, no second rewrite"
boundary: "A repository nobody else has cloned and the forge has not shown · a secret, which is rotated first and purged through the forge's own procedure, whatever the cost"
---

# A rewrite cleans only what refs reach

## Why it works

A history rewrite gives every commit from the first rewritten one to each tip a new hash. The old commits do not vanish: the forge keeps them viewable by hash (cached views, references kept for pull requests) and purges only what its sensitive-data procedure is asked to purge, and every clone that still holds them brings them back the first time it merges instead of rebasing. So the cost of a rewrite is set by its depth and by the number of other machines, not by how many lines it removes, and the gain is partial: the branches look clean, the old commits stay reachable to anyone who has their hash.

For an attribution line that is a poor trade. The line is a record of how the commit was made, not a secret, and leaving it — with a dated entry in the repository saying so, and the setting that stops new ones — costs minutes. Where a rewrite is still chosen (the offenders are a few commits deep, or the repository is about to go public), it is done when no other machine holds unpushed work: the server's refs and a mirror saved, the message rewrite run in a fresh clone and limited to the range from the first offender (the default rewrite strips every signature, even before it), the trees verified identical, each branch pushed with a lease on its old hash and each moved tag pushed explicitly, never a mirror push, and every other machine fetching with forced tags and rebasing or re-cloning.

## When it does NOT apply

A repository nobody else has cloned and the forge has not shown: rewriting it is local, and cheap.

A secret is a different case: it is rotated first, because the old commits stay reachable, and purged through the forge's own procedure whatever the rewrite costs.

## What it costs

Leaving a line: a dated entry and a read-only inventory, about ten minutes per repository. A rewrite: about forty minutes per repository plus five to ten per other machine, and a window in which nobody else pushes.

## Where it came from

The bundle's home rewrote its own history once to remove attribution lines its commits carried. Three carriers later held published commits with the same line; the research of 2026-10-05 tried the procedure in a sandbox with a bare server and several clones, and found that the forge still showed the old commits by hash, that a merging pull on a stale clone restored every one, and that a plain fetch does not update a moved tag.

## Literature

- **git-filter-repo's manual and its rationale; git-filter-branch's own warning against itself.** The recommended rewrite tool, and why it replaced the old one. *Opened 2026-10-05 by the research agent.*
- **The forge's documentation on removing sensitive data, on commit authors and on changing a commit message.** Old commits stay viewable by hash until a purge is requested; a co-author trailer is shown on the commit's page. *Opened 2026-10-05 by the research agent.*
- **git's `gitmailmap` and `git-notes`.** A mailmap maps authors and committers only, so it cannot hide a trailer, and the forge no longer shows notes. *Opened 2026-10-05 by the research agent.*

## Evidence

⚠ **Under review since 2026-10-05:** admitted at 0.0.29 on one repository's rewrite and a sandbox, by the owner's decision to publish it marked; it awaits a carrier's rewrite or its declining one, at the 0.0.30 harvest.

**Reasoned, from one rewrite and a sandbox.** The home's rewrite and the sandbox are the only occurrences; no carrier has rewritten yet, and the published lines in three carriers were left and documented by decision (`d-5ed7e8-808dc7`).
