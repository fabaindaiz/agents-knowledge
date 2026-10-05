# Assistant co-author trailers in published history: rewrite or leave

**Date:** 2026-10-05. **Status:** research for an owner decision; nothing was rewritten.

## Findings

- **A rewrite only cleans what branches and tags reach.** The forge keeps old commits viewable by hash (cached views,
  pull-request refs) and purges only sensitive data, so the old trailers persist there indefinitely.
- **Depth sets the cost, not count:** every commit from the first offending one to each tip gets a new hash.
  Rewriting with the recommended tool strips every commit signature, even before the first offender, unless the run is
  limited to that range (tested in a sandbox).
- **The forge maps the assistant's no-reply address to an account and shows it as a co-author on each commit page**;
  the contributors list counts primary authors only, so trailers do not reach it unless a commit is *authored* by that
  address.
- **`.mailmap` and git notes cannot hide a trailer** (`.mailmap` maps author and committer only; the forge stopped
  showing notes long ago).
- **Other machines are the main risk:** a merging pull on a stale clone brings every old commit back; a rebase pull or
  a re-clone recovers cleanly; a moved tag is not updated by a plain fetch.
- **Prevention in 0.0.27 is confirmed** (the committed `attribution` object form is right; the boolean form is rejected
  by older clients, which then skip the whole settings file).

## Recommendation

Leave and document now (a dated entry per repository, about ten minutes each), and run a five-minute read-only
inventory in each (count, first offender, depth, signed commits, any commit authored by the assistant). Rewrite only
where offenders are shallow or a repository is about to go public, at a moment no other machine holds unpushed work.

## The safe procedure, if a rewrite is chosen

Preconditions (every machine pushed, nothing pushing on its own, no open pull requests, protection noted) → read-only
inventory and the server's refs saved → a mirror and a bundle backup outside the repository → the message rewrite in
a fresh clone, range-limited if signed commits precede the first offender → verify (no trailers, same commit count,
identical trees) → push each branch with an explicit lease on its old hash and each moved tag, never a mirror push →
verify the remote from a fresh clone → on every other machine: enable the hooks, fetch with forced tags, rebase local
work onto the new tips or re-clone, never a merging pull → a dated log entry; keep the backup for some weeks.
Estimate: about forty minutes per repository plus five to ten per other machine.

## For the bundle (each priced; next release)

1. A method note on rewriting published history to remove attribution lines (the procedure above), marked under
   review, about forty-five minutes.
2. `bundle.py trailers` accepting rev-list options directly and saying when a flagged commit is already published
   (in 0.0.28).
3. `check-local` warning when the committed settings lack the attribution setting or the hooks path is not set, about
   an hour.
4. Open: whether `trailers` should flag any co-author line in a carrier that declares a sole author (a reported client
   behaviour adds a human-named trailer that the setting does not remove; not reproduced).

## References (verified 2026-10-05)

git documentation: `git-filter-repo` manual and its rationale, `git-filter-branch` (its own warning), `gitmailmap`,
`git-shortlog`, `git-notes`, `git-push`, `git-rebase`, `githooks`, `git-fast-export`; the forge's documentation on
multiple authors, removing sensitive data, contributors, changing a commit message and the activity view, and its
GraphQL schema for commit authors; the Claude Code settings reference; issues in the client's public tracker on
attribution trailers. A sandbox with a bare server and several clones, kept outside the repository.
