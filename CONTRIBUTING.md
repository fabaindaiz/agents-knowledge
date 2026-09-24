# Contributing

This repository is the root of the `agent-guides` bundle. A change here will eventually be
offered to every repository that carries the bundle, so the bar is higher than in an ordinary
docs repository. Please read [`.agents/README.md`](.agents/README.md) before your first change.

## Where a change goes

Choose the destination by what the change is about, not by which file happens to be nearby:

| You want to add or change | It goes in |
|---|---|
| How reviewing, committing, verifying or documenting is done | `.agents/method/` |
| A claim about building software: retries, concurrency, defaults, naming, data shape | `.agents/knowledge/` |
| An idea for a note that is not ready yet | a line in `.agents/tracking/candidates.md` |
| An experiment that would confirm or refute a note | `.agents/tracking/experiments.md` |
| Work on the bundle itself | `.agents/roadmap.md` |
| A fact about one particular repository | **nowhere in this bundle.** It goes in that repository's own `docs/decisions.md` |

## Proposing a knowledge note

A candidate becomes a note only when **all five** of these hold. The full rules are in
[`knowledge/README.md`](.agents/knowledge/README.md):

1. **It changes a decision.** An agent would get this wrong without the note.
2. **It is general.** It still says something when written without any project noun.
3. **The literature was checked first.** Cite only sources you checked against the original,
   and mark anything cited from memory as such. If nothing relevant turned up, write "none
   known".
4. **It has an occurrence.** A measurement, an incident, or a decision it changed.
5. **It is not already here.** A new occurrence or boundary of an existing claim extends that
   note rather than becoming a second one.

A note has six sections: *Why it works*, *When it does NOT apply*, *What it costs*, *Where it
came from*, *Literature*, *Evidence*. **The boundary section is required**, because a heuristic
with no stated boundary gets applied everywhere, including where it is wrong. Set `confidence`
from your own evidence only, never from the literature's.

Every new note must be reachable from the index. List it in `INDEX.md` under its topic, in at
least one phase, and in at least one *about to do* row of its area index.

## Rules for every file in `.agents/`

- **Nothing private, direct or reconstructible** (principle 20). Generalise figures, paraphrase
  quotes, describe code and products by role, and leave out places and people. Run
  `python3 .agents/tools/bundle.py privacy`; the git hook in `.githooks/` blocks a commit while it
  fails (`git config core.hooksPath .githooks`).

- **Write in English**, even when the surrounding repository or conversation uses another
  language.
- **No project, product, organisation or tracker names.** Refer to a repository by kind, or by
  its random id (`python3 .agents/tools/bundle.py carrier-id`), never both together.
- **Keep the provenance header.** Documents carry frontmatter and the tool carries a comment
  block. At minimum it includes `lineage` and `version`.
- **Never reuse or renumber** decisions, principles, artifacts or phases. Other copies cite them.
- **Keep the two fence styles distinct.** Use `~~~text` for a block meant to be copied into an
  agent, and a backtick fence for an example to read. Do not normalise them.
- **Newest first** in chronological files, stable order in indexes.

## Before you open a pull request

Run both commands with Python 3.9 or newer:

```bash
python3 .agents/tools/bundle.py selftest               # the tool's own tests
python3 .agents/tools/bundle.py digest .agents --check # digests and provenance
```

If you changed anything under `method/`, `knowledge/` or `layout.md`, the declared digests
will no longer match, so the change needs a release: bump the versions, update the digests and
add a changelog entry. `bundle.py stamp` does the mechanical part, and the procedure is in
[`method/prompt-sync.md`](.agents/method/prompt-sync.md). If you would rather not cut a
release yourself, say so in the pull request and a maintainer will stamp it.

Files at the repository root (this file, `README.md`, `AGENTS.md`) are not part of the bundle
and do not affect its digest.
