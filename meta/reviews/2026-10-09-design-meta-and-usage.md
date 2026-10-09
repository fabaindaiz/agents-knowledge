# Design: meta processes in carriers, and consented local usage data (2026-10-09)

Decided with the owner one question per turn; research in
[`2026-10-09-usage-data-research.md`](2026-10-09-usage-data-research.md). Both parts enter 0.0.31 (owner, M4), as task
T7 of [`2026-10-09-plan-0.0.31-release.md`](2026-10-09-plan-0.0.31-release.md).

## Part 1: what a carrier knows about the meta processes

| # | Decision |
|---|---|
| M1 | Ship `method/meta.md` and a read-only `bundle.py home` (the home this release came from, its parent tag, this carrier's lineage, what waits in `proposals/` and `incoming/`). Local information only. |
| M2 | `upstream` keeps only the home's id, never its URL. Any home, including one that diverged, may run a meta-session; its lineage is recorded so lines can be reunified later (`prompt-merge.md`). |
| M2b | The README's frontmatter carries `home` (the id of the home that built the release) and `parent` (the tag it was cut from); `carrier.toml` keeps a `lineage` list that every update appends to. **Not per file**: about 50 bytes on each of ~124 shipped files is ~6 KB per release that repeats what `SHA256SUMS` and the README already say, and the shipped tool carries no comments to hold it. |
| M3 | `meta.md` explains that home repositories exist, what they do, what they hold that a carrier does not (`meta/`, `sources/`, `release.py`, the ledger), how a carrier interacts with one (proposals out; releases, `incoming/` and splices in), and summarises every meta process a carrier takes part in (gather, intake, release, splice, prune, register, align, harvest), so a carrier prepares its harvests and the steps before a home consumes them. Opening a home is cloning a home repository at a tag and recording its lineage; no command. |
| M4 | All of it in 0.0.31. |

## Part 2: consented local usage data

The purpose, stated to the user in their language: **everything stays local, and it serves to improve how they use the
tool**: calibrating agent cost estimates, seeing which steps of the method cost them most, and remembering their
preferences.

| # | Decision |
|---|---|
| U1 | **Outside every repository, per user.** Consent in `~/.config/agent-guides/consent.toml`; data in the user state directory: `$XDG_STATE_HOME/agent-guides/<carrier-id>/` (`~/.local/state/...`; macOS `~/Library/Application Support/agent-guides/`; Windows `%LOCALAPPDATA%\agent-guides\`). No ignore rule is needed, so nothing can be committed by mistake. |
| U2 | Four categories, each consented separately, none pre-selected: **agent costs** (task kind, model, estimate and actual tokens, tool calls, duration; no content), **method frictions** (counts only: gate failures, *review more* picks, steps repeated or skipped), **learned preferences** (one paraphrased line and its why per preference; content, so each one is shown before it is stored), **usefulness ablation** (preferences on or off per session, with the outcome counts; needs preferences). |
| U3 | **Levels plus fine-tuning**: `level = none | counts | full`, each category overridable, retention configurable; the default is `none`. `bundle.py usage show | set | forget` views, changes and erases everything. |
| U4 | **Asked once per machine, the first time something would write** (a close, a delegated agent's return), in the conversation, in the user's language; unanswered means nothing is stored and it is not asked again that session; asked again only when a release adds a category. A new user is unambiguous: no `consent.toml` means *never asked*, the same as `none`; `usage show` on a fresh machine says *never configured, nothing stored, no file in this repository is usage data*. `privacy` fails if a file with a usage-data name is tracked or staged. |
| U5 | **Only figures the user approves leave.** The data never leaves the machine; at a harvest the agent shows a local aggregate (estimate error, frictions per step, the ablation's result) and the user decides whether a generalised figure enters a proposal as Evidence, under principle 20 like any other. Preferences never leave, not even summarised. |
| U6 | **Read at session start, capped.** At level `full`, `bundle.py usage brief` prints at most 2 KB, most-used first, skipping what the assistant's own memory already holds; the ablation alternates on and off per session and records which. |
| U7 | **90 days; preferences renewed by use.** Costs and frictions are deleted after 90 days; a preference expires 90 days after it was last applied or confirmed; the close lists those expiring within 7 days to confirm or let go. |
| U8 | **A protocol registered before the first measurement** (`evals/PROTOCOL-usage.md`): on against off, at least 20 sessions per arm; repeated instructions and corrections per session, and tokens; preferences are kept on by default if repeats fall without tokens rising more than 10%, otherwise turned off by default; a preference never applied in 90 days is a candidate to stop storing. `bundle.py usage report` prints the comparison. |

## How and why each thing is stored

- **Only the tool writes.** Every record goes through `bundle.py usage add <category>`, which checks the consent for that
  category first and writes nothing without it; an agent never edits the files by hand.
- **Append-only JSON lines**, one file per category, each record with its date, category, schema version and, for a
  preference, its source (*stated* by the user or *inferred* by the agent and confirmed).
- **Minimised at the door.** A preference is a paraphrase about how the user works, never code, a path, a name, a
  project noun or a quote; `usage add` runs the generic privacy rules and this machine's private terms over it and
  refuses what fails, even though it never leaves.
- **Why each category exists** is written next to it in `consent.toml`'s comments and in `usage show`, so the user reads
  the purpose where they read the data.

## Budget

ASSUMPTION, to be measured at build: `meta.md` about 5 KB, the usage section of the method about 2 KB, the tool's new
code about 8–10 KB once its comments are stripped. The export is at 888 KB against a 913 KB cap: about 15–17 KB of the
25 KB margin. If the cap would be passed, the method's prose is reduced again before anything is cut from this design.

## Records

| # | Decision id |
|---|---|
| M1 | d-5ed7e8-f7f903 |
| M2 | d-5ed7e8-4b636a |
| M2b | d-5ed7e8-916f40 |
| M3 | d-5ed7e8-57185b |
| M4 | d-5ed7e8-389b56 |
| U1 | d-5ed7e8-6092cd |
| U2 | d-5ed7e8-3c8298 |
| U3 | d-5ed7e8-669ed5 |
| U4 | d-5ed7e8-bebef9 |
| U5 | d-5ed7e8-86f7fa |
| U6 | d-5ed7e8-55617b |
| U7 | d-5ed7e8-5f4555 |
| U8 | d-5ed7e8-adbd1f |
