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

**Read this first when resuming.** Rewritten at every close, within 500 words (`MANIFEST.md`); the hand-off it replaces is first added whole to `meta/archive/roadmap-states.md`, the home's session log.

**State on 2026-10-08, close: `main` holds the 0.0.31 intake, the guide with `next`, and the home's `.claude/`
reviewed**, each merged by fast-forward and pushed. `v0.0.30` on `293766f` is the last tag; 0.0.31 is open.

**Done since 0.0.30's close:**
- Phase 2 carried to nine carriers (`meta/reviews/2026-10-08-carrying-0.0.30.md`); one more by its owner, unmerged.
- **The 0.0.31 intake** (`meta/reviews/2026-10-08-pilot-and-carrier-intake.md`): 18 proposals; a pilot's four entered
  as the home's own (`d-5ed7e8-67a443`); three of one carrier's held until `i-5ed7e8-74d789`.
- **A guide to starting each process, and the `next` skill** (`meta/reviews/2026-10-08-guide-and-next.md`), designed
  with the owner and tested first; the description cap raised by exactly `next`'s description (`d-5ed7e8-afb297`).
- **Every carrier's root map** gains a line sending the user's decisions to principle 15 (`d-5ed7e8-8369d1`); it
  reaches each carrier at its next update.
- **The home's `.claude/` reviewed with the owner:** the method's skills installed (`d-5ed7e8-482d59`); privacy over
  every tracked file through `bundle.py privacy --tracked`, used by the hook and CI (`d-5ed7e8-cb5a1f`); the reminder at
  start and after compaction (`d-5ed7e8-6f0e89`); permissions that catch accidental edits only, from the next session
  (`d-5ed7e8-2ca3ef`).
- Three home proposals waiting for the next intake: `p-580c209938`, `p-a112d996ee`, `p-7e912173fa`.

**Next, in order:**
1. **Execute `meta/reviews/2026-10-08-plan-0.0.31-tools.md`** subagent-driven: ten tasks, a branch each; the
   tool items and `i-5ed7e8-c390fa`'s rest (`d-5ed7e8-b99290` to `d-5ed7e8-6e5d82`). About ten hours.
2. The trigger eval's cases in several languages, in the pilot carrier (`i-5ed7e8-7d64ee`); then `i-5ed7e8-fca056`.
3. At the release: the verdicts on the carrier's ten rows and the three new proposals.

**Waiting on the owner:**
- The twelve `unconfirmed:` reasons in `meta/decisions.md`.
- Whether a template carries a pointer to the knowledge index before its bootstrap (recommended: one line in each
  template's read-me).
- Whether the release defect gets a patch release now (`i-5ed7e8-c390fa`).
- Judges and time for the follow-up experiment.
- The carriers' 0.0.30 branches; the hand-carried carrier's pull request; the credentials ticket; the `proposed` rows
  in carriers' logs; each assistant's terms for automated runs.

**To continue on another machine:** `git pull --tags`; then `i-5ed7e8-61171e`, which now also copies the owner's four
new user-level instruction lines. On this machine, a temporary copy of `next` sits at the user level: delete it once
0.0.31 is installed.

**What went wrong** (`bundle.py count`; each the first of its kind unless said):
- A delegation named a scratch folder the researcher's hook refuses; citations stayed at abstracts (`i-5ed7e8-460736`).
- `align` printed one line and checked nothing (`i-5ed7e8-e44264`).
- **Second incident:** worktree isolation refused git on the main working copy, the owner's own `!` command included
  (`i-5ed7e8-2d3b47`).
- I declined a merge the owner authorized, citing a host default; `AGENTS.md` now says the owner's word suffices.
- Fresh reviews caught wrong counts, a recoverable pilot description, and an `allow` that cannot override a `deny`.

## Standing rules and facts

**Rules the user set, which every step keeps:** content has at least two forms, marked in every file:
the full original, edited here, and the release, generated from it by code and never edited; compression
is a build rule over the original. Industry formats over home-grown ones. Everything derivable is
generated. Nothing leaves the candidate queue by age. The user is the sole author of commits and tags. A
prediction is written before a measurement, and a refuted one is stated, not moved. Where a local
checkout and its remote disagree after a rewrite, the remote is the record. Carriers are updated only when the owner asks, and only
the ones named; a session never offers to update another repository's `.agents/` on its own. Questions run in
modes (principle 15): a decision review one decision per turn, everything at once before the owner leaves.

**Templates** (not carriers, no `carrier.toml`): two template repositories are open on this machine; both were
refreshed to 0.0.30 and tagged `v0.0.30` on 2026-10-08, the knowledge template from 0.0.28 and a second one
scaffolded the same day from empty. Each is refreshed from the tag by `prompt-sync.md` Phase 3 step 6, when its
clone is open here.

**This machine's record of its carriers** is the local manifest (`~/.config/agent-guides/carriers.toml`),
never committed; the names of private carriers are in the local private-terms list. The history before
`v0.0.20` exists only on a local backup branch, never tagged or pushed.

## Next

Items still here that 0.0.23 shipped move to *Done* at its close.

- **`i-5ed7e8-c390fa` · Fix what carrying 0.0.30 found.** From `meta/reviews/2026-10-08-carrying-0.0.30.md`:
  the product noun in one note's lookup cues (and a build scan of the cues for product nouns); a changelog heading
  for layout changes a carrier's audit reads, and `prompt-sync.md`'s run of each carrier's audit made a precondition
  of the cut; `prompt-update.md` 3b naming the fourth Phase 4 line; `new entry` across languages and with
  ` / `-separated labels; `install-skills` honouring `declined`; the base-branch rules and side-by-side worktrees in
  `prompt-sync.md`; `log` set by the update. *Estimate:* a patch release before 0.0.31 if the owner wants the one
  waiting carrier unblocked (the cue alone, under an hour), the rest in 0.0.31: about half a day and 1e5 to 1e6
  tokens, with tests. *Collides with:* the one carrier whose branch waits on the cue.
- **`i-5ed7e8-307d02` · Carriers stop re-checking the release's internals in their own audits.** Six carrier audits
  re-check the index and note layout that `bundle.py verify` owns, and each layout change breaks them all. Offer
  each carrier, at its next update, to drop those checks and rely on `verify`; or ship a documented,
  stable `bundle.py knowledge-check --json` they can call. *Estimate:* a proposal in 0.0.31, then one change per
  carrier at its update; small each. *Collides with:* six carriers' audits and their tests.
- **`i-5ed7e8-7d64ee` · A user guide to activating each process in any language, and a `next` skill that advises
  the session's next actions.** Designed with the owner in a decision walk (`d-5ed7e8-7c51a7` to
  `d-5ed7e8-befd29`): `method/guide.md` in four blocks, each entry its intent phrase, command or paste box, what
  happens and its cost; `method/skills/next/SKILL.md` reading git, the hand-off, the last log entry and the
  seconds-long checks, then three ranked actions with *review more* opening the full menu. **Still to write:** the
  trigger eval's cases for `next` and the other skills in several languages, in the pilot carrier. **A local copy of `next` sits at the owner's user level until 0.0.31 is installed there: delete it
  then**, since it is a derived copy that goes stale. *Estimate:* about a day, with the trigger cases.
  *Collides with:* `skills/README.md`, `install-skills`, the skill trigger eval.
- **`i-5ed7e8-2d3b47` · In an isolated worktree, work on the main working copy goes through ExitWorktree or a
  fast-forward push, never a command handed back to the owner.** The second incident of the host's worktree isolation
  refusing git aimed at the main working copy, on 2026-10-08, the owner's own `!` command included. Done for this
  repository in `AGENTS.md` (*The owner's word is the authorization*); left: whether the method's `close` skill and
  `prompt-sync.md` say the same for every carrier. *Estimate:* a few lines and a proposal. *Collides with:* nothing.
- **`i-5ed7e8-cce629` · A test that reads `argparse` help fails under Python 3.14's coloured help.**
  `test_skills.Count.test_a_line_repeated_word_for_word_is_counted_and_flagged_never_subtracted` filters help lines
  by `startswith("count ")`, which colour codes break; the suite passes with `NO_COLOR=1`, and fails on `main` too.
  Strip the codes in the test, or build the parser with colour off. *Estimate:* minutes. *Collides with:* nothing.
- **`i-5ed7e8-1dd18c` · The update names how the release is replaced where edits are denied, and one checked command
  replaces a release-only folder.** From a carrier's first update to 0.0.30 (`meta/reviews/2026-10-08-pilot-and-carrier-intake.md`,
  findings 6 and 7): a carrier's edit denies leave a shell copy as the only way to replace `.agents/`, which
  `prompt-update.md` never says, and `bundle.py export` refuses a non-empty folder, so a template refresh is three
  steps by hand. `export --replace` removes exactly the files the previous `SHA256SUMS` lists, refuses anything else
  there, and serves both. *Estimate:* about 3 hours with three tests (replace clean, refuse a foreign file, drop a file
  the new release no longer lists) and five lines of `prompt-update.md`. *Collides with:* `p-de14564c12`, held in its
  carrier until `i-5ed7e8-74d789` lands.
- **`i-5ed7e8-74d789` · `privacy` recognises a quote of the bundle's own text or a tool message, and an owner's
  answer reaches intake.** A proposal about the bundle quotes its procedure or its tool's messages, and each quote is a
  WARN; an owner who answers them in the carrier's log leaves the proposals held, since intake reads only
  `privacy-allow:` on the line. The `quote` rule stops warning on a quote that appears verbatim in a shipped file or a
  tool message. *Estimate:* about 3 hours with tests. *Collides with:* three of one carrier's proposals held at the
  0.0.31 intake, which enter at the next gather once this lands, with no edit in the carrier.
- **`i-5ed7e8-e44264` · `align` names a listed carrier with no bundle on disk and checks the rest instead of
  stopping.** With no argument, `align` takes the manifest's list and stops at the first path without `.agents/`
  (`no bundle in [...]`), so a carrier whose bundle sits on an unmerged branch hides every other carrier's state;
  given that carrier's worktree instead, it reports it aligned although its integration branch has no bundle yet.
  It should report such a carrier as not aligned with the branches that hold a bundle (`bundle_branches`), and go
  on. *Estimate:* about an hour with a test. *Collides with:* `B.workspace`, which other commands share.
- **`i-5ed7e8-460736` · The researcher's refusal names its scratch folder and the command shape it accepts, and a
  host's job scratch is accepted too.** At the 0.0.31 intake, four delegated researchers had all but two of their
  shell calls refused: the delegating session named a scratch folder outside the system temporary folder the hook accepts, and
  the agents wrote loops, variables and `mkdir`, which the shell parser refuses; the refusal names neither the
  folder nor the shape, so three of the four fell back to summarising fetches and most citations stayed at their
  abstracts. Keep the hook's limits (reads, and `curl` with no upload flags into a scratch outside the repository);
  print the resolved folder and the accepted shape on refusal; accept the host's job scratch folder when one is set
  and lies outside the repository; tell the delegating session, in `agents/researcher.md`, not to name another
  folder. *Estimate:* about 2 hours with tests. *Collides with:* `research_allowed` and its tests.

- **`i-5ed7e8-fca056` · Cursor and Copilot support: the bundle writes and checks each assistant's surfaces from
  one source, and its efficacy is measured with their CLIs.** Scoped by the owner (`d-5ed7e8-0ff9eb`): research in
  0.0.30 (`meta/reviews/2026-10-08-cursor-copilot-support.md`). **Levels 1 and 2 shipped in 0.0.30 as experimental**
  (`d-5ed7e8-1e7a9a`, superseding `d-5ed7e8-0ff9eb`): the capability table corrected, the bootstrap neutral,
  `bundle.py surfaces` generating and checking Cursor's and Copilot's copies of `.claude/rules/` and `.claude/agents/`
  and Copilot's pointer. **Left:** the six canaries the document lists (does the Cursor IDE read `CLAUDE.md`, do
  Claude-format hooks run in the Cursor CLI on Linux, does Copilot load both a `.claude/agents/` and a
  `.github/agents/` agent of one name, …), then hooks for the surfaces that lack the import; `memory-diff` and `turns`
  for the other assistants' stores; a review bot's file, if the owner uses one; each carrier's migration of its
  hand-written rules, at its update; two limits the home's own copies show: the researcher's Claude model and its hook do not carry
  over (Cursor inherits the session's model, and `readonly` may stop its `curl` downloads, leaving it the fetch tool),
  so it is cheaper and fenced only in Claude Code. The home lists both assistants in `surfaces` since 2026-10-08.
  Level 3: an adapter per CLI in `evals/harness.py`, the same Claude model, a fresh home per trial, pilot-12's three
  tasks; Cursor documents no cost per run. *Blocked for level 3 on the owner:* installing both CLIs, a key and a
  token, and each account's terms for automated runs. *Collides with:* every carrier's update (a migration of its
  hand-written rules, compared with their sources first), `install-skills`, the reviewer's template, and the
  harness.

- **The adversarial review of initialisation, the method and the bundle's organisation (2026-10-02).**
  `meta/reviews/2026-10-02-adversarial-review.md` holds the evidence, the findings and the settled
  design answers. The redesign runs in phases, one release each at most, and a phase that its pilot
  shows costs more than it saves stops there. Phase 0, a user-level profile of the maintainer's standing
  rules, is done outside the bundle: it is personal, so it never enters `.agents/`. The phases and the
  items beside them:

- **`i-5ed7e8-578c22` · Trigger evals for `decision-review` and `user-walk`, and for `close` after its
  trigger change.** 0.0.27 shipped both skills and changed `close`'s triggers (a push is no longer one;
  the close is offered before a push that ends a plan) without a trigger eval. Run `evals/skills/trigger.py`
  in a pilot carrier with held-out phrasings in the owner's own words: fire at least four in five, misfire at
  most one in ten; near misses "execute the plan", "write tests for this function", "push", and a plain
  bug report (which must not fire `user-walk`); and check that a
  general brainstorming skill does not shadow `decision-review` on a request to review an existing spec.
  *Collision:* the skills' descriptions, which every carrier's `LOCAL.md` may override. **Runs before 0.0.30 and again after it** (`d-5ed7e8-07da79`).
- **`i-5ed7e8-54cb3f` · Act on the research of 2026-10-05** — **decided 2026-10-05** for 0.0.29, one per turn (`d-5ed7e8-bb201c` to `d-5ed7e8-ef5760` in `meta/decisions.md`): 2, 3, 4, 5, 6 and 7's tool changes applied; **1 deferred** until pilot-9's index arm and a reviewer pilot (the reviewer has room for about three more notes); still open: bring the cost profile script into `evals/` (it is not on this machine), re-weigh `i-5ed7e8-1ac328` against `i-5ed7e8-16b90a` (the update sessions and the method's size are the bigger lever), leave and document the published attribution lines in the three carriers that hold them (from the machine that has them), and run the trigger eval (`i-5ed7e8-578c22`); on 2026-10-07 the index pilots and the trigger eval were set before 0.0.30,
  and what lives on the other machine moved to `i-5ed7e8-61171e`. Each was a decision for the owner, each
  priced in its document under `meta/reviews/2026-10-05-*.md`:
  1. *Index shape* (`index-scaling`): make `INDEX.md` the lookup alone and move the phase guide to a generated
     `PHASES.md` (reviewer from about 6.6k to 3.7k tokens), measured through pilot-9 and a reviewer-only pilot; no
     topic slicing yet.
  2. *Cost* (`bundle-cost-in-sessions`): the prediction of `i-5ed7e8-a437c6` held (about 1/60 in sessions that
     consult the bundle, 1/75 overall); bring the profile script into `evals/`, re-weigh `i-5ed7e8-1ac328` against
     `i-5ed7e8-16b90a`, and decide whether `report` keeps chars/4 (about 1.4× low for bundle text).
  3. *Review evidence* (`review-panels`): narrow the offered review's evidence sentence; a proof per finding; each
     review records confirmed findings, tokens and minutes; the per-area candidate's gap restated; the experiment.
  4. *Long runs* (`long-runs-and-delegates`): the delegate subsection, one line in `prompt-sync.md`, three lines per
     brief; keep the machine awake during long meta-sessions.
  5. *Timing* (`timing-in-the-gate`): the note's threshold paragraph and one paragraph in principle 18.
  6. *Published trailers* (`attribution-in-published-history`): leave and document, or rewrite per repository with
     the procedure; a method note; `check-local` checks the attribution setting and the hooks path.
  7. *Triggers* (`skill-triggers`): `trigger.py`'s changes and the eval protocol, with the owner labelling the
     ambiguous cases.
- **`i-5ed7e8-89ec30` · Refuse a commit chained on a gate whose output goes through a filter.** The second occurrence in
  this repository (0.0.25 committed and pushed a stale release folder; on 2026-10-05 a commit landed with three
  generated files stale), each time the gate's status was the filter's. The rule is in the close skill and the
  bootstrap; it does not act at the moment the command is typed. *Remedy:* the session hook that already guards
  `git commit` refuses a command where a gate's output is piped before `&& git commit`, unless `pipefail` is set;
  about half an hour with a planted test. *Collision:* the hook's other checks. *Again on 2026-10-07:* the unit tests piped into `tail` before
  `&&` in a chained commit; they passed, so nothing landed red. See `i-5ed7e8-bd65a0`, which removes the typed chain.
- **`i-5ed7e8-e09738` · The eval instruments' findings deferred at the close of 2026-10-07.** *Half done on 2026-10-08:* `review.py` now records a failed session as an error and retries it on resume; a command is judged whole. Left: standard error not drained, canaries all errored, a stopped run's verdict, the harness hash on resume. An isolated review of
  the code merged that night (a mid-size model) found, besides the three fixed before the merge: `evals/review.py`
  scores a session that exited in error as a valid trial and never retries an errored one on resume (high, medium;
  checked against the data: no trial of `review-1` or `review-2` crashed or timed out, but three, all `R2`, reached
  the turn limit without naming the target; D2 was read with and without them, `evals/REPORT.md` §4.13); `trigger.py` judges a command cut to 200 characters, does not drain standard error,
  calls a run valid when every canary errored, and prints a verdict for a run stopped by errors (low); the
  harness's frozen hash is not checked when a run resumes (low). A possible gap, an overlay's new file missing from
  the reviewer's diff, was checked: no diff adds a file. *Remedy:* each under a test, before the next pilot run.
- **`i-5ed7e8-bd65a0` · A home command that runs the gate and commits the named files.** Two frictions recur in the
  typed chain `tests && check && git add && git commit`: a gate piped through a filter (`i-5ed7e8-89ec30`, four
  occurrences in the archived hand-offs) and an edit chained into the same command as `git`, which the privacy hook
  refuses whole so the edit never lands (twice, the last two sessions). *Remedy:* `release.py commit -m MSG FILE...`
  runs the tests and `check` on their own exit status, prints the failures, and commits only the named files; the
  root file's checks section names it as the one way to commit here. About an hour with tests. *Collision:*
  `i-5ed7e8-89ec30`, the privacy hook.
- **`i-5ed7e8-94f262` · Review the method changes published on one carrier's evidence (0.0.26 and 0.0.27).**
  Each is marked *one carrier's evidence* in `.agents/CHANGELOG.md` and `meta/tracking/history.md`: keep it
  where a second carrier's entries or harvest show it acting, rework it where they show friction, withdraw
  it where nothing used it. *When:* at the next release that takes in harvests from carriers on 0.0.27. *Not
  triggered in 0.0.30* (2026-10-08): no carrier's harvest was taken in; it waits for 0.0.31's.
  *Collision:* the coding session's budget, if any is withdrawn from the session loop.
- **`i-5ed7e8-cc0b86` · Queue the experiments the five other new 0.0.27 notes name.** Only two of the
  seven admitted notes had their experiment queued in `meta/tracking/experiments.md`. *Collision:* none.
- **`i-5ed7e8-3a8f87` · Redesign phase 2: bases for verify, commit and state-review, and an audit
  library v1.** The three procedures every carrier rewrote by hand become bases; the structural checks
  carriers keep re-implementing (document paths, decision enforcers that resolve, a research index,
  planted-failure coverage) become a small library a carrier's audit imports. *Collision:* phase 1's
  install command; each carrier's audit. **Next after 0.0.30** (decided 2026-10-07): six carriers now carry their own commit, verify and state-review skills to draw the bases from.
- **`i-5ed7e8-46b707` · Redesign phase 3: the router, brief and lookup, and budgets measured by a
  pilot.** A generated block in the root file routes a request to a skill, a card or a document;
  `bundle.py brief` and `bundle.py lookup` replace hand-run greps. The new budgets are set by a pilot's
  measurements, not predicted. *Collision:* `i-5ed7e8-1ac328`, the main thread's cost.
- **`i-5ed7e8-4a5e6d` · Redesign phase 4: the method jobs as skills, and the reference split.**
  Harvest, update and bootstrap become skills that load only their own steps; the shared reference
  splits so a session reads what its job needs. *Collision:* `i-5ed7e8-0ae753`, `i-5ed7e8-705aa8`.
- **`i-5ed7e8-f542de` · Redesign phase 5: the bootstrap interview, optional skills and hooks.** The
  interview of `i-5ed7e8-2aabb5` as a skill; optional skills named as seams a third-party skill
  plugin fills only if installed, its version recorded in `carrier.toml`; hooks offered, never required.
  Skill evals are allowed as a capped exception while the efficacy studies stay paused. *Collision:*
  `i-5ed7e8-0d9b6a`.
- **`i-5ed7e8-211d11` · A faster intake lane for proposals at the home**, in parallel with the phases.
  The second-repository bar holds most proposals indefinitely; a lane for method changes and
  extensions with counts, decided per release, keeps the queue moving without lowering the bar for new
  notes. *Collision:* `i-5ed7e8-3e6760`.
- **`i-5ed7e8-408166` · The privacy check sees an identifier beside a description.** It matches nouns
  line by line, so a carrier id placed next to a description of that carrier's findings passed it in a
  public file; the review caught it, and history was rewritten. Flag any carrier id within a few lines
  of prose about a carrier, and plant that case in its tests. *Collision:* `i-5ed7e8-1e9567`.
- **`i-5ed7e8-5df552` · A topic slug for proposals that extend a method file.** A proposal that extends
  a method file takes the file's name as its slug, so `intake` collapses every such proposal of a release
  into one candidate per file (eight to `prompt-bootstrap` at 0.0.26), and a refused one is recorded under
  that name; 0.0.26 recorded them by id by hand. Give `propose` a topic slug beside the file, and have
  `intake` key on it. *Collision:* the proposal format, and every carrier's harvest.
- **`i-5ed7e8-a4c2b2` · The home's pre-commit hook runs `release.py build --check`.** It runs only the
  privacy gate, so a commit whose release folder is behind its sources passed it at the close of 0.0.25
  (and was pushed, because the check that failed was piped through a filter; proposal
  `a-filtered-gate-cannot-block`). Add the build check to the hook and plant a stale generated file to see
  it refuse. *Collision:* every commit here gets slower by one build check.
- **`i-5ed7e8-3e6760` · What makes a release productive: the criteria for the first minor release.** *Kept by the owner on 2026-10-07:* 0.0.30 ships under its own number, with everything pending; 0.1.0 is the first monthly release that meets all five, each checked at the cut. Today criterion 3 fails (the pilots measure about ×2.1 to ×2.3) and 0.0.30 resets criterion 4 (a `log` field in `carrier.toml`). How the bundle is
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
  `Reads:` lists that name those headings. **Scoped for 0.0.30** (`d-5ed7e8-6d16cd`): artifacts 1 and 5 and the bootstrap's checklists, the coding session saying "root file", the log named by the `log` field with its default kept. Measured on 2026-10-07: no `Reads:` list and no carrier names those headings, and the skills path it lists is already right. *Scope done in 0.0.30, unreleased (2026-10-08):* artifacts 1 and 5, the bootstrap's checklist and Phase 3, and the session loop saying "the root file". Left outside the scope: principles 1, 2, 4 and 5, the first-pass summary, the ids paragraph, the audit's header, the adoption table and the harvest examples still say `CLAUDE.md` (about a dozen lines of `prompt-context.md`), left for 0.0.31 by the owner on 2026-10-08.
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
  with:* the `Reads:` lists, which name exact headings. **Scoped for 0.0.30** (`d-5ed7e8-9f3502`): only rules restated in more than one prompt; long examples wait for `i-5ed7e8-16b90a`, which keeps every original whole. *Scope done in 0.0.30, unreleased (2026-10-08):* `meta/reviews/2026-10-08-duplicated-rules.md`; three restatements removed from evaluate, four disagreeing copies fixed, and the three disagreements the owner decided (`d-5ed7e8-1f2a69`, `-f12c89`, `-8e6a07`) applied.
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
  `sources/references.md` (SkillReducer). Its precondition, the method's originals in `sources/` with a release the build generates (`i-5ed7e8-c8b508`), shipped in 0.0.23, so it waits on nothing; it goes before `i-5ed7e8-1ac328` (`d-5ed7e8-4a03d2`). *Collides with:* the budgets.
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
- **`i-5ed7e8-ca6ce3` · Evaluate MADR for decision records** — **closed 2026-10-05**: done, more widely, by
  the decision-record review (`meta/reviews/2026-10-05-decision-records.md`, rows in `meta/decisions.md`),
  carried to 0.0.29 by `i-5ed7e8-1bc188`. It did not wait on `i-5ed7e8-8236cb`, which collides with artifacts
  1, 3 and 5, not 6.
- **`i-5ed7e8-bf017b` · Scope decision rows by path when a log outgrows one read.** The ADR practice of
  naming the paths a decision governs, so an agent opens only the rows its change touches (declined for now,
  `d-5ed7e8-c59752`). *Reopens when:* a carrier's log passes a few hundred rows and a session is seen not to
  read it whole, or a harvest finds a decision broken because its row was not read.
- **`i-5ed7e8-7425a6` · Signed release tags.** `SHA256SUMS` shows that a copy is the release it says it
  is, not who published it. *Waits on:* a second person publishing releases.
- **`i-5ed7e8-aca224` · A host-side record-id and renumbering check in every carrier's audit.**
  `bundle.py ids` checks record ids for format, prefix and duplicates; each carrier's audit should
  call it over its own records, and check that principles, artifacts and phases are never
  renumbered. *Waits on:* one carrier adopting it first.

- **`i-5ed7e8-d60fb0` · One external benchmark run at a frozen tag (`d-5ed7e8-d47ee1`).** 60 post-cutoff
  SWE-rebench tasks, two repetitions, `minimal` against the release, through the harness framework installed outside
  every repository, with an adapter written here; capped per sitting, images pruned. *First:* its own protocol in
  `evals/`, registered before any trial; the owner checks the subscription's terms for automated runs and creates
  the token. *After:* 0.0.30, so the frozen tag carries its cost levers. Plan: `meta/reviews/2026-10-07-benchmark-measurement-plan.md` §4.

## Blocked outside

- **`i-5ed7e8-61171e` · The other machine's checklist: what its next session does first.** `git pull --tags`; carry 0.0.29
  (then 0.0.30) to the carriers only that machine holds and to the three it shares with this one, whose newer work is
  unpushed there; bring the cost profile script into `evals/`; leave and document the published attribution lines in
  the three carriers that hold them; add to that machine's user-level instruction file the four conversation lines
  added here on 2026-10-08 (record ids with a name table; interaction designed as a flow with the owner; delegation
  priced, on the cheapest model; findings reported as they fall). *Blocked on:* a session on that machine.

- **`i-5ed7e8-b83f16` · Offer the current release to the carriers not reached.** At the close of 0.0.26,
  every carrier but two stays on 0.0.25 (`meta/tracking/carriers.md`): the release reached only the
  ones the owner named. At the close of 0.0.25,
  one registered carrier was found on no branch of any repository on the machine that ran it. Each gets
  the release from a session where it is open, or through its own `incoming/`, converted by hand first if
  its release has no tag, as 0.0.24's changelog says; then it adds the three root-file lines of the
  bootstrap's Phase 4 and installs the reviewer. *Blocked on:* a session with it open.
  **At the close of 0.0.29** (on the second machine), not reached: three carriers whose newer work is
  unpushed on the first machine, three the owner left out of that session after their review, and every
  carrier only the first machine holds. **At the close of 0.0.30**, none was reached: the owner deferred
  phase 2. Which carrier is which lives in each machine's local manifest, never here. **On 2026-10-08** the owner
  carried 0.0.30 by hand into one carrier: registered at 0.0.30 from its bundle branch, whose pull request is
  unmerged, so its integration branch holds no bundle yet and `align` over the manifest stops at it
  (`i-5ed7e8-e44264`).

## Closed by measurement

- **0.0.22's wiring, summary before note, keeps normal tasks at most ×1.5 of `minimal`** (`i-5ed7e8-c4b9c7`, predicted
  in `.agents/CHANGELOG.md` [0.0.22]): **refuted** by pilot-6, 2026-09-28, at ×2.8 [2.0, 3.3] over four
  tasks. The trivial-task half of the prediction held (×1.0). Kept so the same packaging is not proposed as
  a saving again; what replaces it is `i-5ed7e8-1a57cc` and the phased session.

## Done

Only the last release is kept here; the ones before 0.0.22 are in the home's
`meta/archive/method-changelog.md`, and from 0.0.22 in `.agents/CHANGELOG.md`.

- **0.0.30, 2026-10-08: the month's pending work, measured beside 0.0.29, with experimental Cursor and Copilot
  support.** Closed: `i-5ed7e8-855c42` (Release 0.0.30: the decided scope, after its pilots and the trigger eval); `i-5ed7e8-2aabb5` (The bootstrap's opening questions ask the initialisation's objectives); `i-5ed7e8-29e484` (`bundle.py verify` enforces the carrier record); `i-5ed7e8-715654` (Remove the one-time migration and the deprecated `digest` alias). Scope done with a remainder kept in *Next*: `i-5ed7e8-8236cb`, `i-5ed7e8-705aa8`, `i-5ed7e8-fca056`. Described in
  `.agents/CHANGELOG.md`.
- **Closed at the review of 2026-10-07**, each already delivered: `i-5ed7e8-1bc188` (0.0.29), `i-5ed7e8-191d2a`
  (redesign phase 1, 0.0.26), `i-5ed7e8-a437c6` (measured on 2026-10-05, the prediction held) and `i-5ed7e8-87ffc2`
  (the template's id after the middle dot, 0.0.27).
- **0.0.29, 2026-10-05: decision records a tool reads, records that never leave a carrier, and the research
  decided.** `i-5ed7e8-1bc188` and `i-5ed7e8-54cb3f` (one item deferred). Described in `.agents/CHANGELOG.md`.
- **0.0.28, 2026-10-05: the fixes of two fresh-context reviews of 0.0.27, before either was published.**
  Described in `.agents/CHANGELOG.md`.
- **0.0.27, 2026-10-05: the maintainer's way of deciding, and eight carriers' harvests taken in.** Two
  hundred and twenty-one proposals, seven notes admitted, the question modes and two skills. Described in
  `.agents/CHANGELOG.md`.
- **0.0.26, 2026-10-03: the method's skills, and one carrier's first harvest taken in.** Phase 1 of
  the redesign (`i-5ed7e8-191d2a`) and sixty-six proposals; the carrier tracking now holds every
  carrier this machine runs (`i-5ed7e8-4fea65`). Described in `.agents/CHANGELOG.md`.
