# Contributing

This repository is the home of the `agent-guides` bundle. A change here will eventually be offered
to every repository that carries the bundle, so the bar is higher than in an ordinary docs
repository. Read [`AGENTS.md`](AGENTS.md) for the map of `.agents/`, `meta/` and `sources/` before
your first change.

## Where a change goes

| You want to add or change | It goes in |
|---|---|
| How reviewing, committing, verifying or documenting is done | `.agents/method/` |
| A claim about building software: retries, concurrency, defaults, naming, data shape | a full note in `sources/notes/active/` |
| How the index around the notes reads | `sources/templates/` |
| An idea for a note that is not ready yet | a row in `meta/tracking/candidates.md` |
| An experiment that would confirm or refute a note | `meta/tracking/experiments.md` |
| Work on the bundle itself | `meta/roadmap.md` |
| A fact about one particular repository | **nowhere here.** It goes in that repository's own `docs/decisions.md` |

**Never edit the generated files** (`.agents/knowledge/notes/**`, `INDEX.md`, `areas/*.md`, `OPEN.md`,
`SHA256SUMS`). They are written by `python3 meta/tools/release.py build` from `sources/`.

## Proposing a knowledge note

A candidate becomes a note only when **all five** of these hold; the full rules are in
[`sources/README.md`](sources/README.md):

1. **It changes a decision.** An agent would get this wrong without the note.
2. **It is general.** It still says something when written without any project noun.
3. **The literature was checked first.** Cite only sources you checked against the original, and
   mark anything cited from memory as such. If nothing relevant turned up, write "none known".
4. **It has an occurrence.** A measurement, an incident, or a decision it changed.
5. **It is not already here.** A new occurrence or boundary of an existing claim extends that note
   rather than becoming a second one.

A full note has six sections: *Why it works*, *When it does NOT apply*, *What it costs*, *Where it came
from*, *Literature*, *Evidence*; only the first three ship. **The boundary section is required**: a
heuristic with no stated boundary gets applied everywhere, including where it is wrong. Its
frontmatter is YAML, strings double-quoted:

| Field | Holds |
|---|---|
| `slug`, `topic`, `claim` | the file name, the topic that places it in an area index, the claim in one sentence |
| `confidence` | `measured`, `reasoned` or `inherited`, from your own evidence only, never the literature's |
| `phases` | one or more of `plan`, `dataset`, `implement`, `tests`, `review`, `verify`, `debug` |
| `check` | how to verify the note was followed |
| `about` | `[{do, wrong_when}]`: the *about to do* rows that route to it |
| `rests_on`, `strength`, `our_evidence` | its main source, how strong that is (optional), and what backs it here |
| `boundary` | only when *When it does NOT apply* is prose; otherwise its bold lead-ins are the boundary |
| `retired_because`, `superseded_by` | for a retired note |

The build lists a note under its topic and phases, and in its *about to do* rows, so every note is
reachable. Move a note between states with `release.py note-state SLUG active|review|retired`,
never by hand.

## Rules for every file

- **Nothing private, direct or reconstructible** (principle 20). Generalise figures, paraphrase
  quotes, describe code and products by role, and leave out places and people. The git hook in
  `.githooks/` blocks a commit while `bundle.py privacy` fails (`git config core.hooksPath .githooks`).
- **Write in English** in `.agents/`, `meta/` and `sources/`.
- **No project, product, organisation or tracker names.** Refer to a repository by kind, or by its
  random id, never both together.
- **Never reuse or renumber** decisions, principles, artifacts or phases. Other copies cite them.
- **Keep the two fence styles distinct**: `~~~text` for a block to copy into an agent, a backtick
  fence for an example to read.
- **Newest first** in chronological files, stable order in indexes.

## Before you open a pull request

With Python 3.11 or newer:

```bash
python3 meta/tools/release.py build                    # regenerate .agents/ from sources/
python3 -m unittest discover -s meta/tests -t .        # the tools' tests
python3 meta/tools/release.py check                    # verify, build --check, privacy, links, budgets
pip install pyyaml && python3 meta/tools/check_yaml.py # every frontmatter reads the same through PyYAML
```

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
(`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `build:`, `chore:`; `!` or `BREAKING CHANGE:` for a
breaking change).

A change under `sources/` or `.agents/method/` changes the bundle, so it reaches carriers only in a
release. **Releases are cut by a meta-session** (`meta/method/prompt-sync.md`): the version, the dated
`CHANGELOG.md` section and the tag. A pull request leaves the version alone and adds its entry under
`## [Unreleased]` in `.agents/CHANGELOG.md`.
