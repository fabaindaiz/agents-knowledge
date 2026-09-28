# Roadmap — how this bundle itself improves

**What is planned for the method and the knowledge base, and what each item will collide
with.** Not a promise: a ledger of accepted work on the bundle, in the same five states the
method uses for a repository's roadmap. Work on a *repository* goes in that repository's
roadmap; this file is only about `.agents/` itself.

Newest first within each state. Each item names its **collision** — what it will touch that
something else depends on — because that is what decides its order.

| State | Means |
|---|---|
| **Next** | accepted, and nothing blocks it |
| **Later** | accepted, waiting on something named |
| **Blocked outside** | depends on a decision or a party outside the bundle |
| **Closed by measurement** | was proposed, and a number said no — kept so it is not proposed again |
| **Done** | shipped in a named version; kept one release, then removed |

## Where we are

**Read this first when resuming.** Updated at the close of every meta-session.

**State on 2026-09-28, at the close of 0.0.23.** Release 0.0.23 is tagged (`v0.0.23`) and this
repository is aligned on it, with the reviewer installed in `.claude/agents/`. The other carriers were not
open in this session and stay on their versions (*Blocked outside*, `i-5ed7e8-b83f16`, which says what
each needs). The history before
`v0.0.20` exists only on the local branch `backup/pre-flatten`, never tagged or pushed.

**What 0.0.23 measured** (`evals/REPORT.md` §4.8–4.10, all exploratory, same six tasks and model):

| Run | Wiring | Non-trivial tasks, cost against unaided | Discriminating tasks passed |
|---|---|---:|---|
| pilot-6 | 0.0.22 (summary first) | ×2.78 | 5 of 6 |
| pilot-7 | reviewer subagent by default | ×8.15 | 5 of 6 |
| pilot-8 | cards by the author, reviewer on request (tagged) | ×2.34 | 6 of 6 |

Trivial tasks cost the same as without the bundle in all three. pilot-8 missed its cost line (×2.3) by a
small margin; the user decided to tag, and the changelog says so. Cutting the main thread's cost below ×2
is `i-5ed7e8-1ac328`, the first item of *Next*.

**The route from here:**

1. **Next release:** `i-5ed7e8-1ac328` (cost), measured with a pilot on the same tasks, a prediction written
   first; the harness now refuses a trial whose bundle is not the plan's.
2. **0.0.24:** compressing the method's release by build rules over the full originals
   (`i-5ed7e8-16b90a`).
3. **Paused or deferred:** the efficacy studies (`i-5ed7e8-0d9b6a`, `i-5ed7e8-bf5663`); skills per area;
   the read log (`i-5ed7e8-6c2aff`); rules re-stated at phase boundaries (`i-5ed7e8-bc5867`).

**Rules the user set, which every step keeps:** content has at least two forms, marked in every file:
the full original, edited here, and the release, generated from it by code and never edited; compression
is a build rule over the original. Industry formats over home-grown ones. Everything derivable is
generated. Nothing leaves the candidate queue by age. The user is the sole author of commits and tags. A
prediction is written before a measurement, and a refuted one is stated, not moved.

**This machine's record of its carriers.** From 2026-09-28 the local manifest
(`~/.config/agent-guides/carriers.toml`) holds, beside its list of paths, one record per carrier with its
id, name, path and version, written by `release.py register` and `release.py carriers`; the tool refuses
to write it inside a repository, and the names of private carriers are in the local private-terms list,
so a leak of one fails the privacy check. Nothing of it is committed.

**Waiting on the user:**

1. `i-5ed7e8-ef066e`: review the hand-written boundaries of twelve notes.
2. `i-5ed7e8-543516`: the release pages for `v0.0.22` and `v0.0.23`.
3. A session with the other carriers open, for `i-5ed7e8-b83f16`.

## Next

Items still here that 0.0.23 shipped move to *Done* at its close.

- **`i-5ed7e8-1ac328` · Cut the main thread's cost of a consulting session below twice the unaided one.**
  0.0.23 was tagged at ×2.34 on the non-trivial tasks (pilot-8, `evals/REPORT.md` §4.10), past its own line
  of ×2.3, by the user's decision. The author now reads `knowledge/INDEX.md` whole (about 22 thousand
  characters, carried in every later turn) to reach one or two cards, and takes about half as many calls
  again as without the bundle. Candidates, each with a prediction before measuring: an entry file that
  holds only the *about to do* lookup, the phase guide moved out; the card's check run once, not re-read.
  Measured with the same six tasks. *Collides with:* the INDEX template, `render_index`, the coding budget.
- **`i-5ed7e8-ef066e` · Review the hand-written boundary of the twelve notes whose section is prose.**
  The card of 31 notes quotes their own bold lead-ins; twelve had none, so a `boundary:` was written for
  them, once, by the session that migrated them (listed by `grep -l '^boundary:' sources/notes/active/*`).
  *Waits on:* the user's review. *Collides with:* nothing but those fields.
- **`i-5ed7e8-543516` · Publish the release page for each tag**, with its CHANGELOG section, so a reader
  who does not clone sees what changed. *Waits on:* a machine with the forge's CLI, or the web.
- **`i-5ed7e8-d3ee51` · Close the residual gaps the adversarial review of 0.0.22 left open.** Two rounds
  fixed every blocking finding; still open, each reproduced: a release's own `incoming/*.md` is not
  flagged by `verify --release` (it is never copied, so low); the list of refused configuration and
  instruction files can never be complete; the YAML subset agrees with PyYAML only as far as
  `check_yaml.py` in CI proves it; a carrier converted from the old layout may keep its own documents
  pointing at files that moved (its own gate catches them). The *card* false positive was fixed in 0.0.23.
  Left open by the adversarial review of 0.0.23, each reproduced and none reached by a current file: the
  banner goes in as a heading in a `.md` whose first line is a thematic break with no closing `---`, and
  shifts a Python encoding line after a shebang; `note-state` moves the file before the principle check
  refuses, so a refused move is left half done; the steps 3 and 4 of the session loop still cite full notes
  as background; the working invocation's `Reads:` does not reach the *Done* checklist it asks to be run
  before every report (older than 0.0.23; adding it costs the coding session more than its budget allows). *Collides with:* `bundle.py`, `release.py`, their tests.
- **`i-5ed7e8-0ae753` · Trim the update and bootstrap sessions.** The update's `Reads:` names
  `prompt-context.md` §*Which document to run*, which pulls in two subsections it never uses (about 700
  estimated tokens); the bootstrap states the minting instructions twice; `knowledge/OPEN.md` is about
  half of a harvest's load. *Collides with:* the `Reads:` lists and `report --check` budgets.
- **`i-5ed7e8-715654` · Remove the one-time migration and the deprecated `digest` alias.** The migration
  (`meta/migrations/`) and its CI step are deleted in 0.0.23, the tag keeps them; `bundle.py digest
  --check` goes once every carrier's audit calls `verify`. *Collides with:* carriers' audits.
- **`i-5ed7e8-d65a4c` · An `applies_if` precondition per note, naming where its fact is usually
  found.** No pilot trial read the file that held the decisive fact; agents applied the principle by
  default, which is also how the one over-application happened. A precondition with where to look
  should turn applying by default into looking. *Prediction:* more trials read the decisive file, fewer
  over-apply; *refuted if* the reading rate does not rise. 0.0.23 shipped the field and the card's
  *Applies if* line, filled for four notes; the others wait. *Collides with:* the card columns.
- **`i-5ed7e8-8236cb` · Make `AGENTS.md` the root artifact of the method.** The artifact list in
  `method/prompt-context.md` names a root `CLAUDE.md` as the source, puts the per-change log under
  `.claude/logs/` and skills under `.claude/skills/`, while the layout survey, *Three agents, one
  source*, and this repository treat `AGENTS.md` as the source and the logs as assistant-neutral
  documents. *Collides with:* artifacts 1, 3 and 5, the bootstrap's checklists, and every carrier's
  `Reads:` lists that name those headings.
- **`i-5ed7e8-d4f710` · Review overlapping notes as principles.** The efficacy pilots found that
  removing one note did not remove its principle: agents used `merge-by-shared-fact-not-shared-shape`
  in place of `derived-over-chosen-identifiers`, and `order-writes-by-failure-residue` in place of
  `retry-over-irreversible-effect`. A verdict on every overlapping pair (merge, supersede, or keep both
  with the mechanism that separates them), made in `sources/notes/`. 0.0.23 shipped the `principle`
  field and named these two pairs' principles, keeping both notes of each; the verdict to merge or
  supersede is still open. *Collides with:* the index and area tables, and the experiment's ablation,
  which should remove a principle, not a file.
- **`i-5ed7e8-08c9f7` · Update the layout survey for the shared `.agents/` namespace and the assistants
  it omits.** At least one assistant now scans `.agents/skills/` in every directory, and a dependency
  tool uses `.agents/` with a manifest and a lockfile; the survey (`sources/layout.md`) compares three
  drafts and misses both. *Collides with:* the survey and `prompt-context.md`, *Three agents, one
  source*.
- **`i-5ed7e8-1e9567` · Resolve the persistent privacy warnings.** The same warnings print on every
  run and none changes; a warning that is always there stops being read. Reword each line or, where the
  user explicitly decides it may stay, mark it with a reason. *Collides with:* nothing but the warned
  lines.
- **`i-5ed7e8-3fa5c5` · A release cadence.** The method moved through about two dozen versions in
  one week, each needing a meta-session, and one carrier already trails. Batch releases on a cadence.
  The discard half of this item is closed without a discard: by the user's decision of 2026-09-25
  nothing leaves the queue by age, and the generated ledger `meta/tracking/INDEX.md` keeps every idea
  already met in view, so a meta-session does not create it again. *Collides with:*
  `meta/method/prompt-sync.md` §*The cycle*.
- **`i-5ed7e8-973bd7` · Run the cheapest queued experiments** in `meta/tracking/experiments.md`, one
  per note that has none. *Collides with:* the notes' `confidence`, which moves in both directions.
- **`i-5ed7e8-705aa8` · Clean up the duplicated prose that remains in the method.** The worked
  examples are still long, and a few rules are still restated in more than one prompt. *Collides
  with:* the `Reads:` lists, which name exact headings.
- **`i-5ed7e8-13a8be` · Keep the private-terms list of each machine complete.** `bundle.py
  privacy` checks the names in `~/.config/agent-guides/private-terms.txt`, which never travels; a
  private name missing from it is caught only by the generic rules. *Collides with:* nothing in the
  bundle; it is the one list that must never enter it. Each machine's owner adds the names of private
  repositories, organisations, products and people.

## Later

- **`i-5ed7e8-16b90a` · Compress the method's release by build rules over its full originals, with a
  preservation check.** Planned as 0.0.24. The original is never cut: parts marked in it as rationale,
  example or history (with Markdown comment markers) are left out of the release by the build, and a check
  fails if any imperative sentence, numbered rule, `Reads:` list, paste block or heading a `Reads:` names is
  missing from the release. The markings follow an inventory made by code and approved first. Grounded in
  `sources/references.md` (SkillReducer). *Waits on:* `i-5ed7e8-c8b508`. *Collides with:* the budgets.
- **`i-5ed7e8-e8dc2c` · Measure release 0.0.22 against its written predictions.** Its cost half ran as
  pilot-6 on 2026-09-28 (`i-5ed7e8-c4b9c7`, *Closed by measurement*); the efficacy half stays paused with
  `i-5ed7e8-0d9b6a`.
- **`i-5ed7e8-0d9b6a` · Measure whether the bundle changes what an agent does, and whether its
  content is the cause.** Five exploratory pilots are in the home repository's `evals/REPORT.md`: the
  cost overhead is established, a content effect is seen on few tasks and is not significant. Paused by
  the user's decision of 2026-09-25: the bundle proceeds on the literature and the pilots, and every
  change carries a written prediction. The confirmatory run waits on new tasks by another author,
  ablation by principle, and boundary tasks at distance. *Waits on:* a budget and the user's decision;
  it will measure the packaging that ships then (0.0.22 or later), not v21. *Collides with:* every
  packaging change, and the notes' `confidence`.
- **`i-5ed7e8-bf5663` · Measure whether carrying the bundle changes general performance, on tasks
  nobody chose to suit it.** The protocol is the home repository's `evals/PROTOCOL-general.md`, draft 2.
  Paused with `i-5ed7e8-0d9b6a`. *Waits on:* a budget cap, forecasts and the freeze, now of a version
  tag. *Collides with:* the default routing to the knowledge index, which 0.0.22 changed (it is
  consulted only when a change touches state, a contract, data, security or verification).
- **`i-5ed7e8-6c2aff` · Log which bundle files sessions read, locally, and prune what no session
  opens.** A hook that records only paths inside `.agents/`, in a file never committed, aggregated by
  the harvest; a note no session opened over many sessions is a candidate to merge or retire. *Waits
  on:* 0.0.23's phased session, which changes what is read.
- **`i-5ed7e8-bc5867` · Re-state the key rules at the boundaries of a session's phases**, instead of
  trimming the prose that hooks and the tool enforce. Reformulated 2026-09-28: a factorial study found no
  effect of a configuration file's size, position or structure, and adherence falling with every function
  generated in the session; and frontier models now hold far more simultaneous instructions
  (`sources/references.md`). The phases of `i-5ed7e8-863fb1` are where rules are re-stated. *Waits on:*
  `i-5ed7e8-863fb1`, and the adherence count of `i-5ed7e8-c4b9c7`.
- **`i-5ed7e8-a2f016` · Measure adherence to each directive of the working invocation from transcripts.**
  First counts in pilot-6 (`evals/cost_smoke.py`): the trigger was followed on every trivial trial; a check
  was named in the final report in only a quarter of the other trials under either wiring. A finer count
  (which card's check ran) waits for the phased session's review, which records it.
- **`i-5ed7e8-ca6ce3` · Evaluate MADR for decision records**, the most used format for architecture
  decision records, against the method's own decisions table. *Waits on:* `i-5ed7e8-8236cb`.
- **`i-5ed7e8-7425a6` · Signed release tags.** `SHA256SUMS` shows that a copy is the release it says it
  is, not who published it. *Waits on:* a second person publishing releases.
- **`i-5ed7e8-aca224` · A host-side record-id and renumbering check in every carrier's audit.**
  `bundle.py ids` checks record ids for format, prefix and duplicates; each carrier's audit should
  call it over its own records, and check that principles, artifacts and phases are never
  renumbered. *Waits on:* one carrier adopting it first.

## Blocked outside

- **`i-5ed7e8-b83f16` · Offer the current release to the carriers not reached.** Every carrier
  registered in `meta/tracking/carriers.md` below 0.0.23, and the older ones listed there without ids.
  Each receives the current release from a meta-session that has it open. First `release.py carriers`
  shows, on this machine only, which repository each id is. A carrier on the layout before 0.0.22 is
  converted only after `release.py gather` and `intake`, with `splice --taken` naming that gather (the
  guard now also refuses a carrier the gather did not reach); its `check-local` reports no `SHA256SUMS`,
  which that layout never had, until the splice writes one. A carrier on 0.0.22 whose outbox rows were
  already taken in at 0.0.23's intake keeps them when spliced without that gather: its next harvest
  offers them again, and intake lists them under *Offered again*, not twice in the queue. Both then
  install the reviewer and rewrite the root file's knowledge line (0.0.23's changelog says how, since
  their live update procedure predates it). *Blocked on:* a session with those repositories open.

## Closed by measurement

- **0.0.22's wiring, summary before note, keeps normal tasks at most ×1.5 of `minimal`** (`i-5ed7e8-c4b9c7`, predicted
  in `.agents/CHANGELOG.md` [0.0.22]): **refuted** by pilot-6, 2026-09-28, at ×2.8 [2.0, 3.3] over four
  tasks. The trivial-task half of the prediction held (×1.0). Kept so the same packaging is not proposed as
  a saving again; what replaces it is `i-5ed7e8-1a57cc` and the phased session.

## Done

Only the last release is kept here; the ones before 0.0.22 are in the home's
`meta/archive/method-changelog.md`, and from 0.0.22 in `.agents/CHANGELOG.md`.

- **0.0.23, 2026-09-28: one lookup reaches one card, and both forms of the bundle are marked.** The
  method, the READMEs and the tool are originals in `sources/bundle/`, and every release file carries a
  generated banner that `build --check` enforces in both directions (`i-5ed7e8-c8b508`; the identity
  build proved the ten moved files byte-identical to 0.0.22's). Each note ships a card, linked from the
  index by phase and by what you are about to do (`i-5ed7e8-1a57cc`); notes may carry `principle`
  (`i-5ed7e8-95ac76`) and `applies_if`. The coding session runs in phases; a reviewer subagent, generated
  from a template (`i-5ed7e8-290fce`) with its own load budget (`i-5ed7e8-89124e`), reviews a diff in a
  fresh context **on request only** (`i-5ed7e8-863fb1`). Measured before the tag (`evals/REPORT.md`
  §4.8–4.10): pilot-6 refuted 0.0.22's cost; pilot-7 refuted the first candidate, which reviewed by
  default, at about ×8; pilot-8 measured the tagged design at ×2.34 on the non-trivial tasks, past its
  line of ×2.3, with the other three predictions holding, and the user decided to tag it
  (`i-5ed7e8-1ac328` takes the cost on). Three adversarial review rounds; their residue is in
  `i-5ed7e8-d3ee51`. The migration and its CI step were removed (`i-5ed7e8-715654`, alias kept).
