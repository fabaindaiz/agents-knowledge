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

**On 2026-10-07, everything pending was reviewed with the owner** (`d-5ed7e8-a65c26` to `d-5ed7e8-9f3502`): the next
release's scope is `i-5ed7e8-855c42`, preceded by the index pilots and the skill trigger eval; four delivered items
left *Next*; the compression's blocker was found shipped since 0.0.23; the other machine's work is `i-5ed7e8-61171e`.

**State on 2026-10-05, at the close of 0.0.29, on a second machine.** Release 0.0.29 is tagged and **pushed with its
tag**: the decision-record design (`meta/reviews/2026-10-05-decision-records.md`, `meta/decisions.md`), the
owner's decisions on the research of the same day (`i-5ed7e8-54cb3f`: one deferred, the rest applied), and one
carrier's proposals that had waited since 0.0.25. A read-only review of every reachable carrier against the
unpublished release found five defects, fixed before it was carried (the release was cut again under the same
version, its tag never having left the machine); two more found while carrying are fixed under *Unreleased*. It
reached four carriers, each on a new branch cut from its integration branch, for a pull request the owner opens
(`release.py align`: the home and four aligned); their main checkouts still hold 0.0.25 until those merge. The
carriers this machine shares with the first one hold newer work there, unpushed, and were not reached; two
repositories the owner named had no bundle on any branch (bootstrapped later the same day, below). Waiting on
the owner: the pull requests of the six carriers' branches, which are pushed (the two bootstraps' onto their
ticket branch, merged after it); the proposed rows each carrier's log now shows; and a credentials ticket in the two
bootstrapped repositories. On 2026-10-07 those six carriers' `close` and `decision-review` skills were mapped onto the
ticket cycle their team shares (`meta/reviews/2026-10-07-host-ticket-cycle.md`), the four updated ones installing the
skills then, and pushed on the same branches.

**Later the same day:** the two repositories with no bundle were bootstrapped, each on a branch cut from an
unmerged ticket branch that holds its gate, so their pull requests merge after it; both registered at 0.0.29
(seven carriers on it from this machine, each equal to the tag file for file). `release.py align` no longer
passes once the home builds anything unreleased, since it compares with the home's working release rather
than the tag (a proposal of this repository); the alignment was checked by hand against the tag.

**What went wrong this session:** the release was carried as "ready" before each carrier's own audit had run
over it, and the review then found it would turn one carrier's gate red and leave three carriers' enforcer
checks silently reading the wrong cell; the migration dated rows by committer date, which a history rewrite had
reset; `register` wrote scratch worktree paths into the manifest again (restored from a backup); the shell did
not split a variable holding several paths, twice, and one `rm` ran before the writes it was meant to follow (in
a scratch worktree, recovered).

**State on 2026-10-05, at the close of 0.0.28.** A fresh-context review of 0.0.27, run before anything was
published, found four important defects (a traceback that blocked pushes, a trailers check that read published
history and advised rewriting it, a count that undercounted recurrences, and the home not applying its own
attribution setting) and ten minor ones; a second review of the fixes found four more. 0.0.28 carries all of them,
the three skills' descriptions reworded from the trigger research, and what the day's eight research documents made
actionable at once (`meta/reviews/2026-10-05-*.md`); the rest waits for the owner (`i-5ed7e8-54cb3f`). The
carriers on this machine took 0.0.28 except the one the owner is working on from another machine.

**State on 2026-10-05, at the close of 0.0.27.** Release 0.0.27 is tagged, and with 0.0.28 merged into `main` and pushed with both tags. It took in two hundred and twenty-one proposals from eight carriers, every
one harvested in the same session, transcripts included, with a verdict the owner reviewed theme by theme
(`meta/tracking/history.md`): seven notes admitted after a literature step, twenty-four grown, eight queued
candidates folded, method changes in eight themes the owner reviewed one by one (plus two rulings taken
before them: the review offered, attribution as a setting), seventy-eight refusals recorded. It also put the
maintainer's own way of deciding into the method, measured from every transcript on this machine
(`meta/reviews/2026-10-05-working-practices.md`): four question modes and the example rule in principle 15,
and the skills `decision-review` and `user-walk`. The coding session measures 9,882 of its 10,100-token
budget; the reviewer 6,566 of 6,900, after the index's phase table stopped repeating card links (a build
rule). Every carrier on this machine took 0.0.27 on its harvest branch, unpushed (*Waiting on the user*);
the two whose checkouts were held by live sessions were updated in scratch worktrees of those branches.
The template's `main` holds 0.0.28 with both tags, pushed.

**What went wrong this session**, each now a proposal of this repository or a carrier's: the home piped
its own check through a filter before a commit (stale generated files landed; fixed by the next commit);
a gather read checkouts held by live sessions on other branches (a pack from a worktree closed it);
adding private carriers' names to the machine's term list turned one carrier's own audit red; two
delegates were stopped by the stall watchdog while waiting on long gates, and one carrier's gate hung under
the load of many parallel agents; a delegate briefly switched a live session's checkout and switched it
back; one carrier's update commit was made without a visible gate chain and its gate was re-run green
afterwards; the owner's profile could not be installed by an agent (a self-modification refused by the
permission layer).

**State on 2026-10-03, at the close of 0.0.26.** Release 0.0.26 is tagged. It took in one carrier's
first harvest and the home's own proposals (sixty-six, every verdict in `meta/tracking/history.md`),
the method changes that harvest asked for, published on one carrier's evidence and marked to be
reviewed at the exit of the redesign's phase 1, and that phase itself: the method's skills, installed
as a base plus the carrier's `LOCAL.md`, with `close` first, and the bookkeeping a close runs as
commands. The verbatim evidence of the private carrier's proposals was rewritten before intake, so
no product of it enters this repository. It reached the two carriers the owner named; the others stay
on 0.0.25 (*Blocked outside*). The coding session measures 9,897 of its 10,100-token budget.

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

1. **The carriers' branches**, as listed in *Waiting on the user* (the home and the template are pushed).
2. **`i-5ed7e8-578c22`:** trigger evals for `decision-review` and `user-walk`, and for `close` after its
   trigger changed, in a pilot carrier, with held-out phrasings in the owner's words.
3. **`i-5ed7e8-cc0b86`:** queue the experiments the five other new notes name.
4. **Cost:** `i-5ed7e8-a437c6`, then `i-5ed7e8-1ac328`; then compressing the method's release by build
   rules (`i-5ed7e8-16b90a`).
5. **Paused or deferred:** the efficacy studies (`i-5ed7e8-0d9b6a`, `i-5ed7e8-bf5663`); the read log
   (`i-5ed7e8-6c2aff`); rules re-stated at phase boundaries (`i-5ed7e8-bc5867`).

**Rules the user set, which every step keeps:** content has at least two forms, marked in every file:
the full original, edited here, and the release, generated from it by code and never edited; compression
is a build rule over the original. Industry formats over home-grown ones. Everything derivable is
generated. Nothing leaves the candidate queue by age. The user is the sole author of commits and tags. A
prediction is written before a measurement, and a refuted one is stated, not moved. Where a local
checkout and its remote disagree after a rewrite, the remote is the record. Carriers are updated only when the owner asks, and only
the ones named; a session never offers to update another repository's `.agents/` on its own. Questions run in
modes (principle 15): a decision review one decision per turn, everything at once before the owner leaves.

**The template repository** a new project starts from holds 0.0.28 on its `main`, pushed with its tag, with no
`carrier.toml`; it is refreshed from the tag by `prompt-sync.md` Phase 3 step 6, when its clone is open here.

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

**Waiting on the user** (at the close of 0.0.28; the owner closed the session in this repository only):

1. **The carriers' branches**: eight carriers hold their harvest, records close and 0.0.27/0.0.28 on a branch
   named for the session's harvest, committed and unpushed; merging and pushing each is the owner's call. One
   carrier the owner is working on from another machine holds 0.0.27 staged and uncommitted on that branch, and
   its local copy is stale: leave it until that machine has pushed. Two carriers' checkouts are used by live
   sessions on other branches.
2. **Install the updated profile** on each machine (an agent may not write the user-level instruction file): the
   install block of the profile guide in the personal configuration repository; and the `attribution` setting
   where a machine lacks it.
3. **This machine's client** runs a version whose background time limit applies to interactive sessions; a later
   version lifts it. Keep the machine on mains power with the lid open during long meta-sessions.
4. **Published commits carrying the attribution trailer** in three carriers: leave and document, or rewrite per
   repository (`meta/reviews/2026-10-05-attribution-in-published-history.md`).
5. **The research decisions** of `i-5ed7e8-54cb3f`, and the review of one-carrier changes, `i-5ed7e8-94f262`.
6. Carriers' own open items recorded in their roadmaps for the owner: a worktree with a day of uncommitted work,
   backup branches, an unanswered request about owner-grantable exceptions, a demo build recorded on a device, a
   phase whose records close waits for its own session, a timing test still absolute in one carrier.
7. `i-5ed7e8-ef066e` and `i-5ed7e8-543516`, as before. One repository holds a bundle with no `carrier.toml` (a
   paused bootstrap).

## Next

Items still here that 0.0.23 shipped move to *Done* at its close.

- **The adversarial review of initialisation, the method and the bundle's organisation (2026-10-02).**
  `meta/reviews/2026-10-02-adversarial-review.md` holds the evidence, the findings and the settled
  design answers. The redesign runs in phases, one release each at most, and a phase that its pilot
  shows costs more than it saves stops there. Phase 0, a user-level profile of the maintainer's standing
  rules, is done outside the bundle: it is personal, so it never enters `.agents/`. The phases and the
  items beside them:

- **`i-5ed7e8-855c42` · Release 0.0.30: the decided scope, after its pilots and the trigger eval.** Decided by the
  owner on 2026-10-07, one block at a time (`d-5ed7e8-a65c26` to `d-5ed7e8-9f3502` in `meta/decisions.md`). First,
  with the owner's account: pilot-9's index arm and a reviewer pilot (`d-5ed7e8-220ad3`), and the skill trigger eval
  (`i-5ed7e8-578c22`, `d-5ed7e8-07da79`). Then the meta-session: seven tool fixes (the proposals for align against the
  tag, mint naming the home, register resolving a worktree, new entry reading a log's own format and a `log` field in
  `carrier.toml`, plus `i-5ed7e8-29e484` and `i-5ed7e8-715654`); eight method changes under review (close stopping at
  ready for review, a plan as a working artifact, the tracker as the roadmap's source, criteria and tasks mapped both
  ways, carrier linters excluding the bundle, a privacy answer rewriting the proposal, and in `prompt-sync` the branch
  question and the carrier's audit in the pre-carry review); and `i-5ed7e8-2aabb5`, `i-5ed7e8-94f262`,
  `i-5ed7e8-8236cb` (scoped) and `i-5ed7e8-705aa8` (scoped); and the skill catalogue a complex task reads (`d-5ed7e8-0372b4`, `d-5ed7e8-4c80c1`; proposals `p-480f968069` as updated by `p-1070df9806`), whose carrier `LOCAL` lists are written in Phase 2; and the review turn's format for plans and decision walks (`d-5ed7e8-292961`, `d-5ed7e8-0fec6e`, `d-5ed7e8-d0cfa3`; proposals `p-b102eeae6f` as updated by `p-f76353b351`). The `[Unreleased]` fixes ride with it. *Collides with:*
  the coding session's budget (about 145 tokens left), every carrier's update, and `i-5ed7e8-16b90a`.
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
  about half an hour with a planted test. *Collision:* the hook's other checks.
- **`i-5ed7e8-94f262` · Review the method changes published on one carrier's evidence (0.0.26 and 0.0.27).**
  Each is marked *one carrier's evidence* in `.agents/CHANGELOG.md` and `meta/tracking/history.md`: keep it
  where a second carrier's entries or harvest show it acting, rework it where they show friction, withdraw
  it where nothing used it. *When:* at the next release that takes in harvests from carriers on 0.0.27.
  *Collision:* the coding session's budget, if any is withdrawn from the session loop.
- **`i-5ed7e8-cc0b86` · Queue the experiments the five other new 0.0.27 notes name.** Only two of the
  seven admitted notes had their experiment queued in `meta/tracking/experiments.md`. *Collision:* none.
- **`i-5ed7e8-2aabb5` · The bootstrap's opening questions ask the initialisation's objectives.** It contradicts
  itself today (do not read before asking, and detect first), and across the initialisations reviewed
  only one asked the purpose first. Settle the order by repository kind: ask first in an empty one; in
  an existing one, a short read of at most about five minutes, then propose an objective to confirm. Ask
  what the initialisation must deliver, how deep, and which questions its research must answer; write
  research to the repository as it lands; accept by a first real task. *Collision:* the bootstrap's
  budget, and phase 5.
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
- **`i-5ed7e8-29e484` · `bundle.py verify` enforces the carrier record.** Offered at 0.0.24 as
  `verify-enforces-the-carrier-record`, and confirmed in that meta-session: three carriers reached there
  held the empty `upstream` that means "this is the home", and the function that refuses a carrier id held
  by two repositories in scope is defined and never called. Call it from `verify`, flag an empty `upstream`
  outside the home, and have `carrier-id --mint` stop defaulting `upstream` to the home's value.
  *Collision:* every carrier's gate runs `verify`, so a carrier with a copied identity turns red on update;
  the changelog says how to fix one.
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
  `Reads:` lists that name those headings. **Scoped for 0.0.30** (`d-5ed7e8-6d16cd`): artifacts 1 and 5 and the bootstrap's checklists, the coding session saying "root file", the log named by the `log` field with its default kept. Measured on 2026-10-07: no `Reads:` list and no carrier names those headings, and the skills path it lists is already right.
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
  with:* the `Reads:` lists, which name exact headings. **Scoped for 0.0.30** (`d-5ed7e8-9f3502`): only rules restated in more than one prompt; long examples wait for `i-5ed7e8-16b90a`, which keeps every original whole.
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

## Blocked outside

- **`i-5ed7e8-61171e` · The other machine's checklist: what its next session does first.** `git pull --tags`; carry 0.0.29
  (then 0.0.30) to the carriers only that machine holds and to the three it shares with this one, whose newer work is
  unpushed there; bring the cost profile script into `evals/`; leave and document the published attribution lines in
  the three carriers that hold them. *Blocked on:* a session on that machine.

- **`i-5ed7e8-b83f16` · Offer the current release to the carriers not reached.** At the close of 0.0.26,
  every carrier but two stays on 0.0.25 (`meta/tracking/carriers.md`): the release reached only the
  ones the owner named. At the close of 0.0.25,
  one registered carrier, `r-a2f271` at 0.0.20, found on no branch of any repository on the machine that
  ran it. It gets the release from a session where it is open, or through its own `incoming/`, converted
  by hand first if its release has no tag, as 0.0.24's changelog says; then it adds the three root-file
  lines of the bootstrap's Phase 4 and installs the reviewer. *Blocked on:* a session with it open.
  **At the close of 0.0.29** (on the second machine), not reached: `r-419136`, `r-098980` and `r-7c8794`, whose
  newer work is on the first machine and unpushed; `r-1190d3`, `r-81be2b` and `r-cef56f`, reviewed against the
  release but left out of this session by the owner; and every carrier only the first machine holds.

## Closed by measurement

- **0.0.22's wiring, summary before note, keeps normal tasks at most ×1.5 of `minimal`** (`i-5ed7e8-c4b9c7`, predicted
  in `.agents/CHANGELOG.md` [0.0.22]): **refuted** by pilot-6, 2026-09-28, at ×2.8 [2.0, 3.3] over four
  tasks. The trivial-task half of the prediction held (×1.0). Kept so the same packaging is not proposed as
  a saving again; what replaces it is `i-5ed7e8-1a57cc` and the phased session.

## Done

Only the last release is kept here; the ones before 0.0.22 are in the home's
`meta/archive/method-changelog.md`, and from 0.0.22 in `.agents/CHANGELOG.md`.

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
