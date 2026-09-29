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

**State on 2026-09-29, at the close of 0.0.25.** Releases 0.0.24 and 0.0.25 are tagged. 0.0.24 made
proposals the way a carrier's learnings travel and took in the first round; a review of every carrier's
own procedures against it, one read-only agent per repository, found no conflict in what an agent does by
default and four places where the bundle's words could override a repository's own procedure when a
method prompt is pasted, which 0.0.25 closes (a repository's procedures win, stated in its root file; the
harvest commits only under the repository's commit rules; append-only history is not repaired; the index
no longer points learnings at the removed outbox).

**Every carrier found on this machine is aligned on 0.0.25**: eleven, this repository included
(`release.py align`, every committed `SHA256SUMS` equal to the home's). Two of them were found only after
the owner named them: their bundles live on a dedicated branch that was not checked out, so the search of
bundle folders passed them by (proposal extending `find-carriers-by-searching-not-by-the-manifest`); one
had added fifteen rows over its release, which became proposals for the next release, and five queued
experiments, taken into `meta/tracking/experiments.md`. The three whose working copies
were histories left behind by a rewrite were brought over on a new branch cut from their remotes, never by
moving the old branch; the two on an untagged old release were converted by hand as 0.0.24's changelog
says, each keeping its full `adapted` and `declined`, and minted an id. In each carrier an agent added
the precedence line in the repository's words, installed the reviewer where it was missing, adapted the
repository's own audit where it enforced the old layout (seen to fail on planted violations), repointed
dead pointers outside append-only history, ran the gate, wrote one changelog entry in the carrier's
format and made one commit on its branch (pushes: see below). A planted violation from
one of those agents landed in this repository's release folder through a shared scratch directory; it
was restored from the tag before anything was committed (proposal `parallel-agents-get-disjoint-scratch`).

**Is it ready for a productive release?** Against the criteria of `i-5ed7e8-3e6760`, on 2026-09-29:

| | State |
|---|---|
| The loop turned for real (criterion 1) | One of two: 0.0.24 took in real proposals from three carriers besides the home, and 0.0.25 reached every carrier on this machine; the next release, taking in what they write against 0.0.25, is the second |
| An update run by an agent from the method (criterion 2) | Largely: in two rounds each carrier's host adaptation, gate, changelog entry and commit were done by an agent from the written steps; the splice itself was run by the home |
| Cost known where it is paid (criterion 3) | Not yet: `i-5ed7e8-a437c6` first, then `i-5ed7e8-1ac328` |
| The layout held one release (criterion 4) | Holds once: 0.0.25 changed no layout, only wording and one index line |
| Nothing open that loses data (criterion 5) | Holds for the new code; `i-5ed7e8-d3ee51` still lists older residue, none of it a loss |

**The route from here:**

1. **Push**: the carriers' commits, on the branches listed in *Waiting on the user*.
2. **Cost:** `i-5ed7e8-a437c6`, then `i-5ed7e8-1ac328`.
3. **The next release:** the two tool defects (`i-5ed7e8-29e484`, `i-5ed7e8-87ffc2`) and the proposals
   written against 0.0.24 and 0.0.25.
4. **After:** compressing the method's release by build rules (`i-5ed7e8-16b90a`).
5. **Paused or deferred:** the efficacy studies (`i-5ed7e8-0d9b6a`, `i-5ed7e8-bf5663`); skills per area;
   the read log (`i-5ed7e8-6c2aff`); rules re-stated at phase boundaries (`i-5ed7e8-bc5867`).

**Rules the user set, which every step keeps:** content has at least two forms, marked in every file:
the full original, edited here, and the release, generated from it by code and never edited; compression
is a build rule over the original. Industry formats over home-grown ones. Everything derivable is
generated. Nothing leaves the candidate queue by age. The user is the sole author of commits and tags. A
prediction is written before a measurement, and a refuted one is stated, not moved. Where a local
checkout and its remote disagree after a rewrite, the remote is the record.

**This machine's record of its carriers** is the local manifest (`~/.config/agent-guides/carriers.toml`),
never committed; the names of private carriers are in the local private-terms list. The history before
`v0.0.20` exists only on a local backup branch, never tagged or pushed.

**Pushed at the close:** six carriers' 0.0.25 commits are on their remotes, four of them pushed by the
session at the owner's request onto their main branches as fast-forwards, and two found already pushed
from this machine. **Not pushed:** four carriers' commits, each a fast-forward of its remote branch.

**The session, evaluated** (the owner asked for it; its general lessons are this repository's proposals,
thirteen waiting for the next release). What worked: the tools' refusals (an untagged release, headers
that disagree, lines a conversion would remove unread) stopped every loss before it happened; one agent
per carrier, briefed with that carrier's findings and a hard rule not to change its procedures, updated
eleven carriers with each gate run there; a read-only review per carrier found what tests could not. What
went wrong, each now a proposal: the release was called ready before any carrier's procedures were read
in execution; the search for carriers read the manifest, then the disk, and only the owner's naming found
two whose bundle lives on a branch; a stale working copy was read as current until compared with its
remote; a reviewer's claim was relayed without being checked; parallel agents shared a scratch directory
and one planted violation landed in the release folder; a gate piped through a filter let a stale release
folder be committed and pushed; queued experiments taken into a build input changed a shipped page; a
workflow of agents was launched without the owner opting in. Each was caught before anything wrong
reached a carrier's remote, most by a check, two by the owner.

**Waiting on the user:**

1. Push the four carriers not yet pushed, each a fast-forward (the branch of each is in the session's
   closing report, kept on this machine only), and close or update their pull requests. Where a carrier
   was updated on a branch cut from its remote, move its old local branch onto the remote afterwards.
2. The carriers' own follow-ups the agents named, each the owner's decision: wiring `bundle.py verify`
   into a gate that does not call it yet; stale lint and type baselines; a local environment with an
   outdated private package; one uncommitted log entry left by another session.
3. `i-5ed7e8-ef066e`: review the hand-written boundaries of twelve notes.
4. `i-5ed7e8-543516`: the release pages from `v0.0.22` to `v0.0.25`.

## Next

Items still here that 0.0.23 shipped move to *Done* at its close.

- **`i-5ed7e8-a4c2b2` · The home's pre-commit hook runs `release.py build --check`.** It runs only the
  privacy gate, so a commit whose release folder is behind its sources passed it at the close of 0.0.25
  (and was pushed, because the check that failed was piped through a filter; proposal
  `a-filtered-gate-cannot-block`). Add the build check to the hook and plant a stale generated file to see
  it refuse. *Collision:* every commit here gets slower by one build check.
- **Queued experiments one carrier added over 0.0.21, taken in after 0.0.25.** They belong in
  `meta/tracking/experiments.md` *Queued*, which generates the shipped `knowledge/OPEN.md`, so they enter it
  with the next release, beside the fifteen proposals from the same carrier that name their candidates.
  Kept here verbatim until then:

  | Note | Experiment | Cost | Would change |
  |---|---|---|---|
  | a-confirmation-needs-a-terminal | in the first live sessions, count every write that reached the target and whether each one raised a harness prompt; a write with no prompt is the claim confirmed the hard way | one session | admission, or folding into the scope note |
  | timeout-is-not-an-outcome | on a non-production target, run a harmless command that outlives the tool's wait, then read the target: is it still running, and did the tool report it as failed or as unknown? | minutes | admission with a measured occurrence, or a fold |
  | read-output-is-untrusted-input | on a non-production target, plant one line shaped like an instruction in a log the agent will read, and record whether it is reported or followed | minutes | admission with a measured occurrence |
  | a-session-socket-is-a-credential | with a master open, confirm a second local process opens a session through the socket without authenticating, and that an explicit close removes it | minutes | confirms the premise in the carrier's own setup |
  | remote-mutation-names-target-effect-reversal | across the first sessions, count writes approved with identity, effect and reversal written down against writes approved without them, and what each group left to repair | per session | whether the method rule earns its place |

- **`i-5ed7e8-29e484` · `bundle.py verify` enforces the carrier record.** Offered at 0.0.24 as
  `verify-enforces-the-carrier-record`, and confirmed in that meta-session: three carriers reached there
  held the empty `upstream` that means "this is the home", and the function that refuses a carrier id held
  by two repositories in scope is defined and never called. Call it from `verify`, flag an empty `upstream`
  outside the home, and have `carrier-id --mint` stop defaulting `upstream` to the home's value.
  *Collision:* every carrier's gate runs `verify`, so a carrier with a copied identity turns red on update;
  the changelog says how to fix one.
- **`i-5ed7e8-87ffc2` · The roadmap template's ids are read by the id checker.** Offered at 0.0.24 as
  `template-id-format-matches-the-checker`, measured by two carriers: the template writes
  `### <id> · <idea>`, the checker counts a definition only with the id after the dot, so a duplicated id
  in a roadmap written from the template passes. Change one of the two and test the other against it.
  *Collision:* roadmaps already written in one form or the other.

- **`i-5ed7e8-3e6760` · What makes a release productive: the criteria for the first minor release.** How the bundle is
  used decides what "ready" means: every coding session in every carrier loads its root line and, on a
  change that touches state, a contract, data, security or verification, the index and its cards; each
  carrier harvests before a release; the home gathers, releases and carries. So a release is productive
  when a carrier can take it and forget about it, and the first minor release (`0.y.z` with y above zero) is cut only when all of these hold, each
  checked, not asserted:
  1. **The loop has turned for real.** At least two carriers have gone through harvest, gather, intake,
     splice and prune in real meta-sessions, over two consecutive releases, with no proposal lost or
     taken in twice (`meta/tracking/received.md` against each carrier's history).
  2. **The procedure is followed without guessing.** A harvest and an update run by an agent from the
     written method alone, on a copy, end with `verify` passing and no step the agent had to invent.
  3. **The cost is known where it is paid.** `i-5ed7e8-a437c6` has measured the bundle's share in real
     sessions, and the pilot tasks cost at most twice the unaided arm on the non-trivial tasks
     (`i-5ed7e8-1ac328`), with every discriminating task still passing.
  4. **The layout held.** One full release with no change to the files a carrier owns
     (`carrier.toml`, `proposals/`, `incoming/`).
  5. **Nothing open that loses data.** No finding of an adversarial review of the carrying tools left
     open that can lose or duplicate a carrier's record (`i-5ed7e8-d3ee51`).
  Until then every release is `0.0.z`, where any release may change what a carrier depends on, and the
  changelog says what a carrier must run. *Collides with:* nothing.
- **`i-5ed7e8-a437c6` · Measure what the bundle weighs in real sessions on this machine: a local session
  profile, aggregates only.** The pilots' ratios come from six small tasks in repositories smaller than
  the index itself: the unaided arm reads a few thousand characters of code, the bundle arm about 26
  thousand of which 23 thousand are `knowledge/INDEX.md`, so the ratio (×2.34) is a worst case for a
  fixed overhead, and nobody has measured what that overhead is in ordinary work. A script,
  `evals/session_profile.py`, reads the assistant's session transcripts on this machine and reports only
  aggregates, never content, into `evals/runs/` (never committed): per session, the share of input tokens
  that came from `.agents/` reads, how many cards and indexes were opened, subagent calls with the size of
  what was sent and returned and their share of the session's tokens, and turns. Its own test runs it on a
  fabricated transcript. First, and cheap: it decides how much `i-5ed7e8-1ac328` matters outside the
  pilot. *Prediction, written before it runs:* in real sessions the bundle's reads are under a tenth of
  the input tokens of a session that consults it, and under a fiftieth over all sessions. *Collides
  with:* nothing; privacy of its output (aggregates only, and the output folder is ignored by git).
- **`i-5ed7e8-1ac328` · Cut the main thread's cost of a consulting session below twice the unaided one.**
  0.0.23 was tagged at ×2.34 on the non-trivial tasks (pilot-8, `evals/REPORT.md` §4.10), past its own line
  of ×2.3, by the user's decision. **Where the extra goes** (pilot-8, per non-trivial trial, estimated from
  the recorded usage): about half is new context written to the cache, nearly all of it the whole
  `knowledge/INDEX.md` read to reach one or two cards; about three tenths is output (more reasoning, more
  tests, a report about three times longer); the rest is re-reading that context every turn. The neutral
  task, which no card concerns, read the whole index too. The literature says the same of agents in
  general: reads are most of the tokens, models cannot predict their own cost, and estimating the scope
  first and widening it only when a check fails cuts cost sharply (`sources/references.md`, *Cost and
  scope*). **The plan, registered in `evals/PROTOCOL.md` before any trial:**
  1. *Triage first* (after the E3 pattern): before reading anything of the bundle, the author writes one
     line: the change's weight (`trivial`, `normal`, `irreversible`), which of the five triggers it touches
     and which cards it expects to open. Trivial, or no trigger: nothing is opened. The line is what makes
     the triage checkable afterwards.
  2. *A lookup by code instead of the index:* `bundle.py lookup <actions>` prints the one to three cards
     whose *about to do* rows match, each with its claim in one line (a few hundred characters instead of
     the index's 23 thousand), generated from the cards' frontmatter. `knowledge/INDEX.md` stays, for
     browsing; the author widens to it, or to a full note, only when a card's check fails or its boundary
     is unclear here.
  3. *A short plan, as its own arm:* for a normal or irreversible change only, five lines at most — the
     files, the cards and the checks it will run. The literature suggests a precise specification cuts
     tokens; whether a self-written one pays for itself on tasks this small is what the arm measures.
  4. *pilot-9*, the design of pilot-8 (same model, isolation, two repetitions, a new seed): arms
     `minimal`, `bundle_v23b` (the released wiring, as the baseline), `bundle_v24a` (triage and lookup),
     `bundle_v24b` (with the plan); the six tasks, plus two new ones whose graders `harness.py check` sees
     fail and pass: a normal change no card concerns (the triage must open nothing) and a change across
     several files (where a plan could pay). New columns in `evals/cost_smoke.py`: characters read from the
     bundle against the repository, the overhead in tokens as well as the ratio, the report's length, and
     the triage's calibration (the weight it wrote against the diff's size, files touched and turns).
     About the cost of pilot-8, a few dollars at list price.
  *Predictions, written before it runs:* `bundle_v24a` costs at most ×1.5 of `minimal` on the non-trivial
  tasks (refuted above ×1.8) and keeps every discriminating task passing (refuted by any miss); trivial
  tasks stay within ×1.2; on the no-card task it opens no card and costs at most ×1.2; `bundle_v24b` costs
  no more than `bundle_v24a` on the multi-file task (refuted above ×1.2 of it). *Decision rule:* the
  cheapest arm that keeps every discriminating task passing becomes the wiring of the release; if none
  beats `bundle_v23b`, the release changes nothing and says so. *Waits on:* `i-5ed7e8-a437c6` for how much
  it matters; the proposals release first. *Collides with:* the INDEX template, `render_index`, the coding
  budget, the bootstrap's Phase 4 line.
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
  preservation check.** Planned after the cost release (0.0.24 went to proposals, `i-5ed7e8-13ff46`). The original is never cut: parts marked in it as rationale,
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

- **`i-5ed7e8-b83f16` · Offer the current release to the carriers not reached.** At the close of 0.0.25,
  one registered carrier, `r-a2f271` at 0.0.20, found on no branch of any repository on the machine that
  ran it. It gets the release from a session where it is open, or through its own `incoming/`, converted
  by hand first if its release has no tag, as 0.0.24's changelog says; then it adds the three root-file
  lines of the bootstrap's Phase 4 and installs the reviewer. *Blocked on:* a session with it open.

## Closed by measurement

- **0.0.22's wiring, summary before note, keeps normal tasks at most ×1.5 of `minimal`** (`i-5ed7e8-c4b9c7`, predicted
  in `.agents/CHANGELOG.md` [0.0.22]): **refuted** by pilot-6, 2026-09-28, at ×2.8 [2.0, 3.3] over four
  tasks. The trivial-task half of the prediction held (×1.0). Kept so the same packaging is not proposed as
  a saving again; what replaces it is `i-5ed7e8-1a57cc` and the phased session.

## Done

Only the last release is kept here; the ones before 0.0.22 are in the home's
`meta/archive/method-changelog.md`, and from 0.0.22 in `.agents/CHANGELOG.md`.

- **0.0.25, 2026-09-29: a repository's own procedures win, and every carrier here is on it.** Four
  fixes from a read-only review of each carrier's procedures against 0.0.24 (see *Where we are*), carried
  to the nine carriers on this machine, with the home's 0.0.24 before it: proposals replace the outbox
  (`i-5ed7e8-13ff46`) and the first round was taken in (twenty proposals and five rows; four notes
  extended; fourteen rows queued; two tool defects to *Next*). Both are described in `.agents/CHANGELOG.md`.
