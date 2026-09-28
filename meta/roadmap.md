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

**State on 2026-09-28.** Release 0.0.22 is on `main` with its tags (`v0.0.20` to `v0.0.22`); CI passed.
Two carriers hold 0.0.22 (this one and one converted on 2026-09-25); one is still on the layout before
0.0.22, and the others are registered below it (*Blocked outside*). The history was rewritten so that the
user is the sole author of every commit and tag (`AGENTS.md`). The history before `v0.0.20` exists only on
the local branch `backup/pre-flatten`, never tagged or pushed.

**The research route, revised on 2026-09-28** against the release's own lessons and the literature added
to `sources/references.md`, *Evidence on context files, skills and sessions*:

1. **Now, no release:** the cost smoke test `i-5ed7e8-c4b9c7` (approved by the user), which also counts
   directive adherence (`i-5ed7e8-a2f016`) on the same transcripts.
2. **0.0.23:** first the method's originals and its generated release, both marked (`i-5ed7e8-c8b508`),
   as an identity transform; then the phased session with a reviewer in a fresh context that runs the
   notes' checks (`i-5ed7e8-863fb1`, `i-5ed7e8-89124e`), the reviewer's generated definition
   (`i-5ed7e8-290fce`, skills per area deferred), merging overlapping notes by principle
   (`i-5ed7e8-d4f710`, `i-5ed7e8-95ac76`), `applies_if` (`i-5ed7e8-d65a4c`), and the cleanups
   (`i-5ed7e8-715654`, `i-5ed7e8-d3ee51`, `i-5ed7e8-0ae753`). The smoke test's decision rule sets whether
   the review is optional on small changes.
3. **0.0.24:** compressing the method's release by build rules over the full originals
   (`i-5ed7e8-16b90a`).
4. **Paused or deferred:** the efficacy studies (`i-5ed7e8-0d9b6a`, `i-5ed7e8-bf5663`; Study 2 would reuse
   a paired design like SWE-Skills-Bench's when resumed); skills per area; the read log
   (`i-5ed7e8-6c2aff`); rules re-stated at phase boundaries (`i-5ed7e8-bc5867`).

**Rules the user set, which every step keeps:** content has at least two forms, marked in every file:
the full original, edited here, and the release, generated from it by code and never edited; compression
is a build rule over the original. Industry formats over home-grown ones. Everything derivable is
generated. Nothing leaves the candidate queue by age. The user is the sole author of commits and tags.

**Waiting on the user:**

1. `i-5ed7e8-ef066e`: review the hand-written boundaries of twelve notes.
2. `i-5ed7e8-543516`: the release page for `v0.0.22`.
3. A session with the other carriers open, for `i-5ed7e8-b83f16`.

**To resume on any machine:** `git pull --tags`; `git config core.hooksPath .githooks`; the machine's
`~/.config/agent-guides/private-terms.txt` and `carriers.toml`; a Python 3.11+ interpreter. Then
`python3 -m unittest discover -s meta/tests -t .`, `python3 .agents/tools/bundle.py verify` and
`python3 meta/tools/release.py check` must pass before anything else.

## Next

Planned for 0.0.23. Its release reuses the build: what is derivable from a note's fields is generated.

- **`i-5ed7e8-c4b9c7` · Cost smoke test of 0.0.22 against its written predictions, with directive
  adherence from the same transcripts.** Exploratory, pre-registered as a dated amendment in
  `evals/PROTOCOL.md`, run `pilot-6`: arms `minimal` and `bundle` with the 0.0.22 wiring line frozen in the
  plan (optionally the v21 wiring too), on the three tasks that discriminated in pilot-5, the neutral task
  and two new trivial tasks; the model and settings of the pilots; two repetitions; a budget of the order
  of pilot-5. It claims nothing about efficacy. *Predictions under test* (`.agents/CHANGELOG.md` [0.0.22]):
  trivial tasks at most 1.2 times `minimal` (refuted above 1.4); normal ones at most 1.5 (refuted above
  1.8); the discriminating tasks still passed. *Decision rule, fixed before the run:* at most 1.5 on normal
  tasks and the phased session of 0.0.23 is designed for adherence and verification, its review optional on
  small changes; above 1.8 and the review in a subagent becomes the default path to save context.
  *Collides with:* `evals/harness.py` (the wiring text per run), the protocol.
- **`i-5ed7e8-c8b508` · The method's originals in `sources/method/`, its release generated by the build,
  and every file marked as original or release.** The notes already have two forms; the method does not:
  `.agents/method/*.md` is edited by hand and is both. Content may exist in more forms (templates, the
  ledger), but these two must be unmistakable: every generated release file carries the generated banner,
  no original does, and `build --check` fails on either mistake. First step of 0.0.23, as an identity
  transform proven against `v0.0.22`; every later change to the method is made in the original.
  *Collides with:* every `Reads:` list (checked on the generated output), `bundle.py` exemptions for
  `SHA256SUMS` and itself, `AGENTS.md`.
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
  pointing at files that moved (its own gate catches them). Also: the privacy rule that fails a record id beside a domain noun reads the bundle's own word *card* as a payment card, so every sentence naming a card and a roadmap item is reworded. *Collides with:* `bundle.py`, its tests.
- **`i-5ed7e8-0ae753` · Trim the update and bootstrap sessions.** The update's `Reads:` names
  `prompt-context.md` §*Which document to run*, which pulls in two subsections it never uses (about 700
  estimated tokens); the bootstrap states the minting instructions twice; `knowledge/OPEN.md` is about
  half of a harvest's load. *Collides with:* the `Reads:` lists and `report --check` budgets.
- **`i-5ed7e8-715654` · Remove the one-time migration and the deprecated `digest` alias.** The migration
  (`meta/migrations/`) and its CI step are deleted in 0.0.23, the tag keeps them; `bundle.py digest
  --check` goes once every carrier's audit calls `verify`. *Collides with:* carriers' audits.
- **`i-5ed7e8-863fb1` · Run the coding session in phases with subagents.** Plan with a small context;
  an optional design review of the plan by a subagent holding only the cards the plan touches; build
  with the full repository and no knowledge loaded; a review of the diff by principle, in a subagent
  that must cite evidence from the repository that a note's precondition holds before it reports a
  finding; fix only the findings; at most two re-reviews of what was fixed, then the user decides; a
  short close that writes the outbox. What it is for: the pilots put the cost in reading notes into
  the main context, which every later turn pays again, and a subagent reads them once and returns a
  verdict. *Prediction:* a normal session at most 1.5 times a session without the bundle, one that
  consults the knowledge at most twice, and the discriminating tasks still passed; *refuted if* the
  review phases cost more than the reading they replace, or a finding without a cited precondition
  appears. Assistants without subagents run the same phases in one context. *Collides with:* the session
  loop and the working invocation, the evaluation protocols (they run with no subagents), and
  `i-5ed7e8-290fce`.
- **`i-5ed7e8-290fce` · Generate the reviewer subagent's definition from the notes' frontmatter.** The
  reviewer of `i-5ed7e8-863fb1` is written by the build from fields every note already has (claim,
  boundary, check, about) and a template in `sources/templates/`, and the bootstrap and the update
  install it in the carrier's `.claude/agents/`. **Skills per area are deferred** (2026-09-28): public
  software-engineering skills gave about one point on average and most gave nothing
  (`sources/references.md`, SWE-Skills-Bench); they wait for a measurement of their own. Supersedes the
  paste-in packaging of `i-5ed7e8-8623a8`. *Collides with:* the carrier's installed artifacts, and
  `i-5ed7e8-08c9f7` (where agent files live).
- **`i-5ed7e8-95ac76` · A principle field that groups overlapping notes, and index rows grouped by it.** The
  pilots found the unit that carries is the principle, not the file (`i-5ed7e8-d4f710`). A `principle`
  field lets the index show one card per principle, with its notes as cases, and lets the experiment
  ablate by principle. Done together with `i-5ed7e8-d4f710`, on the full notes. *Collides with:* the
  build, the templates, and the note shape in the home's `sources/README.md`.
- **`i-5ed7e8-d65a4c` · An `applies_if` precondition per note, naming where its fact is usually
  found.** No pilot trial read the file that held the decisive fact; agents applied the principle by
  default, which is also how the one over-application happened. A precondition with where to look
  should turn applying by default into looking. *Prediction:* more trials read the decisive file, fewer
  over-apply; *refuted if* the reading rate does not rise. *Collides with:* the card columns and the
  reviewer of `i-5ed7e8-863fb1`.
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
  with the mechanism that separates them), made in `sources/notes/`. *Collides with:* the index and
  area tables, and the experiment's ablation, which should remove a principle, not a file.
- **`i-5ed7e8-89124e` · A budget for the reviewer subagent's load.** `bundle.py report --check` holds
  the coding session and the largest index row to a static budget; the reviewer of `i-5ed7e8-863fb1` needs
  its own `Reads:` list and budget. *Waits on:* `i-5ed7e8-863fb1`.
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
- **`i-5ed7e8-e8dc2c` · Measure release 0.0.22 against its written predictions.** Its cost half is
  `i-5ed7e8-c4b9c7` (approved 2026-09-28); the efficacy half stays paused with `i-5ed7e8-0d9b6a`.
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
  Done together with `i-5ed7e8-c4b9c7`, on its transcripts, at no extra cost.
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
  registered in `meta/tracking/carriers.md` below 0.0.22, and the older ones listed there without ids.
  Each receives 0.0.22 from a meta-session that has it open: `release.py splice` converts the layout
  before 0.0.22 and keeps its own fields (checked on a scratch copy of one of them: nothing lost, its
  own fields intact, `verify` green). *Blocked on:* a session with those repositories open.

## Closed by measurement

None yet.

## Done

Only the last release is kept here; the ones before 0.0.22 are in the home's
`meta/archive/method-changelog.md`, and from 0.0.22 in `.agents/CHANGELOG.md`.

- **0.0.22, 2026-09-25: the bundle holds only what a carrier runs, and what it holds is generated.**
  Decided in one session with the user, on the literature and the five pilots, without a new run.
  `.agents/` keeps what a carrier runs; the full notes, templates and literature moved to `sources/`,
  the roadmap, records and release procedures to `meta/`. Each note ships short and its index rows are
  built from its own fields (the migration proved the old tables byte-identical); the area rows
  gained a *Not when* column. Semantic Versioning, git tags, `SHA256SUMS`, Keep a Changelog, `carrier.toml`, an
  outbox per carrier, a derived `Since` column and a generated ledger of every idea already met, an
  `incoming/` check (`i-5ed7e8-c5f622`), Python 3.11. Closes `i-5ed7e8-a89859` (short notes and index rows)
  and `i-5ed7e8-f71f36` (tags and a hashed file per release). The coding session consults the index only when a change touches state, a
  contract, data, security or verification, applies the card first, and lets the repository win over a
  note. Measured statically: `.agents/` from about 0.9 MB to about 0.55 MB; the notes about half; the
  coding session's fixed load from about 12k to about 9k estimated tokens; a harvest from about 28k to
  about 10k. *Predictions, to be measured by `i-5ed7e8-e8dc2c`:* trivial tasks at most 1.2 times the
  cost of `minimal` (refuted above 1.4); the bundle at most 1.5 times on normal tasks and twice on
  critical ones, with the discriminating tasks still passed (refuted above 1.8, or a lower pass rate);
  the watchdog boundary task with the smaller model rising from none passed (refuted if it stays at
  none).
