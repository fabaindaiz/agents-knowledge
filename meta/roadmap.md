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

## Next

Planned for 0.0.23. Its release reuses the build: what is derivable from a note's fields is generated.

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
- **`i-5ed7e8-290fce` · Generate Claude Code subagent definitions and Agent Skills from the notes'
  frontmatter.** The reviewer of `i-5ed7e8-863fb1` and a skill per area can be written by the build
  from the fields every note already has (claim, boundary, check, about), so none is written by hand.
  Supersedes the paste-in packaging of `i-5ed7e8-8623a8`. *Collides with:* `i-5ed7e8-08c9f7` (where
  skills live), the carrier's installed artifacts, and every `Reads:` list.
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
  one week, each needing a meta-session, and one carrier already trails. Batch releases on a cadence;
  the discard half of this item shipped in 0.0.22 (`release.py triage`). *Collides with:*
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

- **`i-5ed7e8-e8dc2c` · Measure release 0.0.22 against its written predictions.** The release was
  adopted on the literature and the pilots, without a new run; its predictions are in
  `.agents/CHANGELOG.md` and under *Done* below. *Waits on:* the user's decision to fund a run.
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
- **`i-5ed7e8-bc5867` · Remove from the invocations the prose that hooks and the tool already
  enforce.** The working invocation states rules that the privacy hook, `bundle.py verify` and `ids`
  enforce; a directive enforced in code can be one line. Adherence falls as instructions multiply.
  *Waits on:* `i-5ed7e8-a2f016`, which says which directives are followed.
- **`i-5ed7e8-a2f016` · Measure adherence to each directive of the working invocation from the pilot
  transcripts.** The transcripts of the pilots are on the machine that ran them (never committed); a
  script can count, per directive, how often it was followed (the check of a card run and reported, the
  brief written) with no new run. *Waits on:* nothing but time; home-only, in `evals/`.
- **`i-5ed7e8-ca6ce3` · Evaluate MADR for decision records**, the most used format for architecture
  decision records, against the method's own decisions table. *Waits on:* `i-5ed7e8-8236cb`.
- **`i-5ed7e8-7425a6` · Signed release tags.** `SHA256SUMS` shows that a copy is the release it says it
  is, not who published it. *Waits on:* a second person publishing releases.
- **`i-5ed7e8-aca224` · A host-side record-id and renumbering check in every carrier's audit.**
  `bundle.py ids` checks record ids for format, prefix and duplicates; each carrier's audit should
  call it over its own records, and check that principles, artifacts and phases are never
  renumbered. *Waits on:* one carrier adopting it first.

## Blocked outside

- **`i-5ed7e8-b83f16` · Offer the current release to the carriers not reached.** They are listed
  in `meta/tracking/carriers.md`, the older ones without ids, plus `r-a2f271`, registered at 0.0.20.
  Each receives 0.0.22 from a meta-session that has it open (`release.py splice` converts the old
  layout and keeps its own fields). *Blocked on:* a session with those repositories open.

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
  outbox per carrier, a derived `Since` column and the three-release discard rule in code, an
  `incoming/` check (`i-5ed7e8-c5f622`), Python 3.11. Closes `i-5ed7e8-a89859` (short notes and index rows)
  and `i-5ed7e8-f71f36` (tags and a hashed file per release), and the discard half of
  `i-5ed7e8-3fa5c5`. The coding session consults the index only when a change touches state, a
  contract, data, security or verification, applies the card first, and lets the repository win over a
  note. Measured statically: `.agents/` from about 0.9 MB to about 0.55 MB; the notes about half; the
  coding session's fixed load from about 12k to about 9k estimated tokens; a harvest from about 28k to
  about 10k. *Predictions, to be measured by `i-5ed7e8-e8dc2c`:* trivial tasks at most 1.2 times the
  cost of `minimal` (refuted above 1.4); the bundle at most 1.5 times on normal tasks and twice on
  critical ones, with the discriminating tasks still passed (refuted above 1.8, or a lower pass rate);
  the watchdog boundary task with the smaller model rising from none passed (refuted if it stays at
  none).
