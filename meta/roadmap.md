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

**State on 2026-11-26: a pre-release close on one machine; the final close and the first minor continue on
another.** 0.0.37 (phases 1 and 2 of the *Next* plan, the `red-check` flake fixed) and 0.0.38 (one carrier's harvest of
twenty-five proposals and the home's twelve received; nothing a session follows changed) are cut, tagged, merged to
`main` and pushed; the template is at 0.0.38. The carrier whose harvest was taken in got 0.0.38 in its harvest
worktree, committed there under its own gate, **not pushed**: its owner integrates that branch.

**The phase on the session** (`meta/plans/2026-11-26-the-session.md`) is designed, every round with the owner: the plan
of the cut and the topic map (`meta/plans/2026-11-26-cut-plan.md`, `-topic-map.md`: the cut is a build rule that keeps
every original whole, `d-5ed7e8-9f47b1`; topic export deferred, `i-5ed7e8-17f776`), T5 (a `plan` skill that measures
and proposes its split, `lanes check`), T6 (fresh delegates by default), the live state's files (one per session in the
common git folder), and the build's questions (short skill descriptions derived for the release, `d-5ed7e8-7a4324`;
guards shown tested before the owner approves each; the text lane delegated; a push per milestone). **Not built:** T7 to
T18 and T13, about sixteen agent hours, by the plan's table.

**The first minor.** The carrier proposed a plan for it, read and priced in
`meta/reviews/2026-11-26-harvest-and-a-proposed-minor.md`: stale against 0.0.36 and 0.0.37, a third overlapping the
phase, its record-format change resetting criterion 4 of `i-5ed7e8-3e6760`; its A/B pilot is the proposed validation,
not run.

**Settled on 2026-11-26, on the other machine, before the build:** the first minor's scope (the phase whole first,
the minor after, `d-5ed7e8-12cb12`); both rulings of `i-5ed7e8-44591b` (`d-5ed7e8-79ed41`, `d-5ed7e8-79a26e`); the
unattended mode's design round runs inside T18 (`d-5ed7e8-385da4`). **Waiting on the owner:** each guard's approval
during the build; the private-terms list remains the owner's alone.

**First step next session:** the build, at T7 as decided (the text lane delegated in its own worktree, T8, T9 and T11
in the main thread with each guard shown tested before approval).

**To continue on another machine:** `git pull --tags`, then `git switch plan/next-phases`; enable the hooks
(`git config core.hooksPath .githooks`), keep this machine's private-terms list, Python 3.11 or newer. The carrier's
proposals and its plan are not needed there: their reading is in the review above. Nothing waits on this machine but
that carrier's unpushed harvest commit, which belongs to its own repository.

## Standing rules and facts

**Rules the user set, which every step keeps:** content has at least two forms, marked in every file:
the full original, edited here, and the release, generated from it by code and never edited; compression
is a build rule over the original. Industry formats over home-grown ones. Everything derivable is
generated. Nothing leaves the candidate queue by age. The user is the sole author of commits and tags. A
prediction is written before a measurement, and a refuted one is stated, not moved. Where a local
checkout and its remote disagree after a rewrite, the remote is the record. Carriers are updated only when the owner asks, and only
the ones named; a session never offers to update another repository's `.agents/` on its own. Questions run in
modes (principle 15): a decision review one decision per turn, everything at once before the owner leaves. Findings are reported as they fall, candidly, in a form comparable to a
published study. A long background agent is announced with its estimate of time, tokens and model, then compared with
its actual. Usage data stays on its machine; only a generalised figure the owner approves enters a record.

**Templates** (not carriers, no `carrier.toml`): two template repositories are open on this machine; both were
refreshed to 0.0.30 and tagged `v0.0.30` on 2026-10-08, the knowledge template from 0.0.28 and a second one
scaffolded the same day from empty. Each is refreshed from the tag by `prompt-sync.md` Phase 3 step 6, when its
clone is open here.

**This machine's record of its carriers** is the local manifest (`~/.config/agent-guides/carriers.toml`),
never committed; the names of private carriers are in the local private-terms list. The history before
`v0.0.20` exists only on a local backup branch, never tagged or pushed.

## Next

- **`i-5ed7e8-44591b` · Two rulings of the owner before the first minor** (`meta/reviews/2026-11-26-harvest-and-a-proposed-minor.md`).
  *Settled by the owner on 2026-11-26, at the opening questions of the build.* (1) An optional table **does** reset
  criterion 4, against the recommendation: `d-5ed7e8-79ed41`, written into the criterion. (2) The A/B pilot **may** send a
  private carrier's code to another provider as oracle and judge, after a protocol registered in `evals/` with a budget
  cap and only on tasks that carrier's owner approves one by one: `d-5ed7e8-79a26e`. Nothing left open here.

- **`i-5ed7e8-592937` · A domain word beside a record id fails the privacy check while records are written.** Counted
  2026-11-26: three incidents in one session (decision and roadmap rows naming a kind of loop, a kind of device and a
  controlling role), each reworded by hand after a commit was refused; no earlier entry mentions it. A writer of
  records does not see the rule until the check fails. **Proposed:** `bundle.py id` (or the decision-row writer) runs
  the `id-beside-domain` rule over the row it mints for, before the row is written, and prints the word to replace.
  *Estimate:* 30 min, 80k tokens. *Collides with:* nothing.
- **`i-5ed7e8-c7e6b2` · A delegated draft of method text broke the rule on the two forms: the second incident.** The rule
  (compression is a build rule on the original; text is never moved out of an original to shrink the release) was
  corrected by the owner on 2026-09-28 and again on 2026-11-26, when a delegated plan of the cut proposed deleting and
  moving text in `sources/` and this session did not catch it. A delegate does not load the owner's standing rules
  unless its brief carries them. **Proposed:** the delegate-brief form in the `brief` skill (T14) carries, for any
  brief that drafts or plans changes to `sources/`, the two-forms rule in one line. *Estimate:* 10 min inside T14.
  *Collides with:* T14.

- **`i-5ed7e8-d23f66` · An unattended mode that keeps the normal flow and spends the owner's attention once.** The owner's
  suggestion, 2026-11-26: before leaving, the session asks every pending question at once and starts the plan; a
  question that arises later is parked for the owner's return, never asked while away, and the session continues
  whatever needs no new validation, stopping a task only where its next step waits on a parked answer. The flow is the
  normal one; only the interactions are batched. **Fits:** the `plan` skill (`d-5ed7e8-4b1883`) as a mode, the live
  state (`bundle.py now`, the parked questions surviving a compaction), the question rules (T9), and the owner's own
  standing rule to ask everything before working alone. **Open for its design round:** what counts as needing new
  validation (the guards, the user-visible, the owner's content), how a parked question records the work it blocks, and
  how the return is reported. *Scheduled by the owner on 2026-11-26* (`d-5ed7e8-385da4`): the design round runs
  **inside T18**, once the `plan` skill, the live state and the question rules exist, not before the build.
  *Estimate:* a design round, then about 60 min and 150k tokens inside T18. *Collides with:* T9, T18.

- **`i-5ed7e8-837b2c` · A pilot cohort: which carriers adopt each release first, and serve as the local test beds.**
  *Chosen by the owner on 2026-11-26.* The rule: a carrier enters the cohort on **commits in the last thirty days and
  number of authors**, measured by reading each listed repository, and the owner narrows the set by hand. Eight were
  chosen. **Where the list lives:** the machine's own configuration, in a file of its own beside the carriers manifest,
  never here — a cohort ranked by activity is a description of each repository, which this repository may not write
  beside a carrier id. It is not in the manifest itself because `release.py register` and `release.py carriers` rewrite
  that file with a fixed set of keys (`meta/tools/release.py`, the manifest writer) and would drop any flag added by
  hand. **What follows:** every carrier in the cohort is six releases behind, so each needs the releases carried into it
  before its first harvest; that carry is what criterion 1 of `i-5ed7e8-3e6760` counts. **What it does not give:** they
  are one owner's repositories, so for admission they remain **one source**, whatever their number
  (`sources/README.md`). *Estimate:* the carry, about 15 min per carrier plus each one's own gate. *Collides with:* the
  phase's build, which the owner put first (`d-5ed7e8-12cb12`).

Items still here that 0.0.23 shipped move to *Done* at its close.

- **`i-5ed7e8-7cb101` · Three more routine skills, after the phase on the session.** `carry` (the release into carriers:
  gather, the one table, splice, prune, each carrier's gate, register, align), `review-rounds` (severity rounds with a
  fresh-context reviewer, until only lows, capped), `research` (a dated document, primary sources, each claim's
  strength, readers in parallel). Ranked from a keyword count of the owner's turns (rough, not incidents); each
  repeats a procedure done by hand several times. *Estimate:* about 45 min each; each description needs room in the
  descriptions' cap. *Collides with:* `meta/method/prompt-sync.md` (carry), the close skill (review rounds).
- **`i-5ed7e8-1914cd` · A delegate's isolated worktree begins at an older commit than the branch it was cut from: eight lanes of
  2026-11-25 and -26.** Each started at the remote main or the last pushed head, not at the local branch, and had to
  run `git checkout --detach <sha>` first, which every brief carried after the first time; one lane's `reset` was
  refused and it used `checkout`. Say it once in the method's delegation rule (the brief names the commit to start
  from), or have the merging session push the branch first where pushing is allowed. *Estimate:* one sentence in
  `prompt-sync.md` *Worktrees*, 5 min. *Collides with:* the coding budget if it went into §*Long runs and delegates*.
- **`i-5ed7e8-33c9b5` · What is left of the intermittent `red-check` verdict: two lows and one decision.** **The
  verdict itself is explained and closed (2026-11-26):** the judged commit's own code built its scratch index as a
  copy of the real one, so git trusted a file changed in the same second at the same size (racy git) and exported the
  old blob, about once in fifteen runs; a later commit had already replaced the copy with an index read from HEAD,
  and `red-check` now remembers a pass by commit, so an old commit is never judged again. Left, low: a test helper
  imported through `sys.path` is not recognised as test support; `shell-check` does not see a loop variable taking a
  quoted list's words; `bundle.py ids` does not flag a roadmap item id cited and defined nowhere (2026-11-26: a hand-off cited an item whose row a refused command never wrote). **A decision for the owner:** the privacy baseline's fingerprint includes the path
  (`d-5ed7e8-af36e9`), so a known line moved to another file, as every close moves the hand-off into the archive,
  reads as new until reworded. Recommendation: keep the path and reword figures when archiving.
  *Estimate:* the two lows, 30 min, 80k tokens. *Collides with:* nothing.
- **`i-5ed7e8-516d7a` · The 0.0.36 plan: the eight decisions of the 0.0.35 walk, task by task** (`d-5ed7e8-5dc49a`). Each task
  lands on its own with its review, by severity (`d-5ed7e8-6db1f7`), and carries its estimate in what is measured:
  agent wall minutes, tokens, review rounds, with the actual written beside it (`d-5ed7e8-9dc00d`). Calibration so
  far: this home's delegations ran at about a tenth to a fifth of their time estimate and near their token one.

  | # | Task | Decision | Est. wall | Est. tokens | Rounds | Actual |
  |---|---|---|---|---|---|---|
  | 1 | The development flow's map in `guide.md`: each step's input, output and closing check | `d-5ed7e8-cbb288` | 20–40 min | 80k | 1–2 | ~10 min main thread; round 1: 4 medium, 3 low (~0.5 min, ~70k tokens); `0685a27`, `da1b5af` |
  | 2 | A carrier's practices into the skills: the plan's dependency table and stop rule, review focus, priced spike; the plan's fresh read; the classified red; a merge-commit hook; at close, rulings promoted, merged worktrees offered for removal, roles, proposed copy | `d-5ed7e8-21f670` | 60–90 min | 250k | 2–3 | ~15 min main thread; round 1 (with task 1's round 2): 5 medium, 4 low (~2 min, ~85k tokens); `1e58405` and the fix |
  | 3 | Re-review by severity, hard stop at five, a fix's own pass (`prompt-bootstrap.md`, §21.4) | `d-5ed7e8-6db1f7` | 10–20 min | 50k | 1 | ~6 min main thread; review shared with 4 |
  | 4 | Estimates in measured units with the calibration shown (§21.1, the bootstrap, the ledger column) | `d-5ed7e8-9dc00d` | 15–30 min | 60k | 1 | ~8 min main thread; with 3: 3 review rounds (2 medium, then 1 medium, then low only, listed), ~1 min and ~55k tokens each; `e2c1f89`, `85d0389`, `09e2a92`, `538099e` |
  | 5 | The spec format (shape B): a template and `bundle.py spec` with tests; then the pilot on a carrier's real feature, which the owner names | `d-5ed7e8-cb0531` | 60–90 min + pilot | 250k | 2 | template and check ~15 min main thread, test first (5 red, then green); round 1: 4 medium, 4 low, fixed test first (the anchor check deferred, low); round 2 pending; the pilot waits on the owner's choice of feature |
  | 6 | The documentation skill and `bundle.py docs fingerprint` and `docs lint`, standard library only | `d-5ed7e8-3a85e8` | 90–120 min | 300k | 2–3 | ~25 min main thread, test first (7 red, then green), lint run on nine real documents (one false positive found and fixed); round 1: 6 medium, 9 low, fixed test first (4 red, then green); low deferred: setext headings; round 2: 9 medium (with task 9's), fixed test first; round 3: 1 medium (step-order key), fixed test first; round 4: 1 medium (a loose list split), fixed with its test beside the fix (red not seen); round 5: 1 medium (lazy numbering), fixed test first (red, then green); round 6, on the owner's word past the cap: none |
  | 7 | `bundle.py usage measure`, per machine, the approval naming its record, a refusal leaving its trace; first trial on three blocked candidates | `d-5ed7e8-7b6df4` | 60–90 min | 250k | 2 | ~15 min main thread, test first (5 red, then green); round 1: 2 medium, 4 low, fixed with tests beside the fix (red not seen); round 2: 2 medium, 2 low, fixed test first; round 3 pending; the first trial waits on the owner |
  | 8 | `meta/tracking/machines.md` and `bundle.py machine`, and the close's step for what lives only on this machine | `d-5ed7e8-5751b6` | 45–75 min | 200k | 2 | ~20 min main thread, test first (5 red, then green); round 1: 3 medium, 4 low, fixed test first (5 more red, then green), ~2 min, ~78k tokens; round 2: 1 medium, 2 low, fixed with tests beside the fix (red not seen); round 3: 4 low, fixed test first; round 4: covered by the whole-branch review and its re-review, no scoped round of its own |
  | 9 | The plan page: `plan.md`'s fixed sections, `bundle.py plan page` on an anonymised template of the layout a carrier wrote by hand, republished at pause, close and on request; it reads task 4's estimate and actual columns | `d-5ed7e8-09facc` | 60–90 min | 250k | 2 | ~25 min main thread, test first (4 red, then green); round 1: 9 medium (lanes, states, ratio, slots, sections, bold, and three in the fix rounds), 10 low, fixed test first (6 red, then green); low deferred: forget's report of dropped measures, a lone `[carrier]` table; round 2: 3 medium, 2 low, fixed test first; round 3: covered by the whole-branch review and its re-review, no scoped round of its own |

  The whole-branch review (fresh context, ~5 min, ~1e5 tokens): 3 medium (the plan template could not hold §21.1's needs, risks, spike, fresh read, tokens and rounds; `skills/README.md` lacked `edit-docs`, the spec and the fresh read; the fresh read's and the estimate's scope read "a large plan" against the decisions' "every plan"), 5 low; all fixed, the tool's ones test first (red, then green); round 2: 1 medium (the close skill still said "a large plan"), fixed (text only, no red possible), checked by a search of the method for the phrase, now absent; 1 low left (the roadmap template's "for a large item" is about items, not plans).

  Then 0.0.36 is checked against the first minor's criteria (`i-5ed7e8-3e6760`). *Collides with:* tasks 1 and 2
  write the same skills, so they run in that order, not at once; 5, 6 and 9 share the template folder; 9 follows 4.
- **`i-5ed7e8-b9628b` · The harvest and update texts leave steps an agent guesses: criterion 2 of the first minor, run on copies.**
  On 2026-11-25 two agents ran a harvest and an update on disposable copies of two carriers, from `prompt-harvest.md`
  and `prompt-update.md` alone; both ended with `verify` passing and nothing of the carrier's own lost, but the
  harvest guessed about ten steps and the update about twelve. About half come from having no one to ask; the text has
  no rule for an unattended run (take the defaults and say so). The rest are gaps. *Harvest:* step 3 says a delegated
  agent writes nothing, while the last rule says never leave a refusal unwritten; no way to tell an old outbox is
  there; no carrier-side way to find a branch holding a later harvest (`gather` is the home's); "the last date read"
  when only the records were read; whether a harvest writes a log entry. *Update:* how the release reaches
  `incoming/` when no home is at hand; whether the live or the incoming procedure is followed; step 4 points at
  `prompt-harvest.md`, which its `Reads:` omits; the decisions migration needs `--migrate --write` and says nothing of
  a log's "open" section; the root-file lines "Phase 4 names" live in another document; `new entry` and `id s` mint
  different ids; nothing for a host other than Claude Code. The owner chose to record them and cut 0.0.36
  (`d-5ed7e8-e09f5f`). *Estimate:* the text fixes 45 min wall, 150k tokens, one round; the re-run on fresh copies
  30 min, 250k tokens. *Collides with:* the update and harvest sessions' token budgets.
- **`i-5ed7e8-a3a0a1` · Private channels for what does not travel between machines: research, then a pilot.** The owner's
  note at `d-5ed7e8-5751b6`: the manifest, the private-terms list and the agent's local memory never travel
  through a public repository; which private channels could carry them (a private configuration repository, an
  encrypted file, the owner's own sync) is to be researched and explored, then tried as a pilot. Nothing private
  is written anywhere before the owner chooses. *Estimate:* a research round, about 20 min wall and 100k tokens.
- **`i-5ed7e8-151456` · Push and merge what 0.0.34 left on branches.** **Done on 2026-11-25 at the owner's word,
  but for four:** the home's `main` and the tag, the template's `main` and tag, and nine carriers' `main`
  fast-forwarded and pushed; four carriers' harvest branches pushed as branches and not merged, because each sits
  on feature or integration work not yet on `main`, so a fast-forward would carry that work too. Three carriers
  refuse an agent's push in their own settings: their branches wait for the owner to push them. Each merge of a
  pushed branch follows that carrier's own flow. *Estimate:* minutes per carrier, the owner's hands.
- **`i-5ed7e8-cfd663` · What the phase-2 agents changed in carriers' own files, for the owner to read.** A pause rule
  rewritten in one carrier's local override of the close skill and its root file (to the two kinds); an empty
  decision status filled from the commit that wrote the row, in the carrier where the fixed `decisions` first read
  it; a repository settings file given the empty attribution setting; a carrier's audit exempting the docs map the
  close skill names; a root file's note count corrected. Left to each owner, unfixed: a carrier's own pause skill
  that now sits beside the close skill's with no precedence; a carrier that jumped from 0.0.25 with no skills
  section and no researcher; a test importing a package its requirements do not declare, so a fresh environment
  fails; a gate whose ratchet baseline is ignored, so a worktree cannot run it; a gate that checks trailers but
  not the author; a sibling path an audit reads that a worktree cannot resolve. *Estimate:* one read per carrier.
- **`i-5ed7e8-a6b77f` · Split the home's own commands out of the shipped tool, by who runs them.** The owner's
  proposal of 2026-11-24 (`p-7b6ae101bc`): what only the home runs lives in a file of its own that does not
  travel, so a carrier's copy is smaller to carry, to checksum and to keep in step, and the home's half has
  somewhere to grow without charging every carrier for it. This supersedes the next step of `i-5ed7e8-ee9f86`,
  whose count classified by *which file names a command* and returned zero: that measure cannot separate the two,
  because the home's own procedures are themselves described in files a carrier receives and reads. The measure
  that can is which session actually invokes a command, and the one bound taken that day puts the home's
  exclusive code at roughly four to six per cent of the file, with a further five per cent that a call graph
  reaches from no command at all. **Do the measure before the split**, command by command, and review the code as
  it is traced: the owner asked for improvements the export would gain, and a reading that is already walking
  every command is where they will be found. *Estimate:* half a session for the trace and the review, a session
  for the split itself. *Collides with:* `verify`, which checksums one tool; every session file that names a
  command; and the carriers, for which this is a breaking change in the shape of what they hold.
- **`i-5ed7e8-74cbcd` · The gate's own cost is measured, and a redundant check can be retired.** The owner's
  proposal of 2026-11-24 (`p-19e2887fcf`): the gate is the step between finishing a task and closing it, it is
  chained to every commit, and it only ever grows — every incident adds a check and nothing retires one, so a
  rung exists for adding a control and none for removing it. Four gates measured that day ran on the order of a
  minute or two each over suites of several hundred to a thousand tests, and no repository's history shows a
  check ever removed. The work: a counted run over one suite giving, per check, when it was last red and how many
  of its failures another check already catches first; then a retirement rung written beside the addition one.
  Read the literature on test-suite minimisation and on obsolete and flaky tests first, which has standard
  measures for this. Bears on the queued candidate about a gate stopping at its first red step: a check after
  that step is green by omission, so it looks useful and is never exercised. *Estimate:* a session for the
  measurement, and the rung is a paragraph. *Collides with:* the enforcement ladder, which today only adds.

- **`i-5ed7e8-23e94e` · Re-examine the export cap once the changelog can be archived again.** The cap was
  raised to 1,250,000 bytes on 2026-11-24 (`d-5ed7e8-929f2a`) after the alternative — archiving the oldest
  changelog sections into the home — was rejected on a tool defect, `i-5ed7e8-5e0415`, and not on its merits.
  When that defect is fixed the alternative returns: the changelog is 59,339 bytes, about 6% of the release,
  and `proposals/RECEIVED.md` already keeps only the last two releases' verdicts, with the rest in the home's
  ledger, so the shape is proven in the bundle. *Estimate:* nothing to build; a re-reading at the release after
  the defect is fixed. *Collides with:* `i-5ed7e8-5e0415`, which it waits on, and any carrier reading
  `--since` across the archived boundary.

- **`i-5ed7e8-dfae87` · 0.1.0, the first stable release, aimed at this month.** The owner's objective: a stable
  release in October 2026. 0.0.32 stays a patch (`d-5ed7e8-3110f3`) and is the first of the two releases in a row
  that break no format which the minor asks for; **what points at the minor is 0.0.32's own proposals and
  explorations**, the three items below among them. The release that cuts the first minor writes what the layout, the carrier
  file's fields and the tools' command names then guarantee, and the carriers it reaches share one version.
  *Estimate:* the policy paragraph and a migration note, about an hour, at the release that qualifies, plus the
  three items. *Collides with:* `CHANGELOG.md`'s own statement of SemVer §4, and every carrier's `--since`
  comparison.
- **`i-5ed7e8-d6ecfe` · Persistent delegates: an agent kept open that receives tasks one at a time.** The harness
  already allows it (a spawned delegate stays addressable, a listing shows what is active, a fork inherits the
  parent's context), so what is missing is the method: when a warm delegate pays against a fresh one, how state is
  handed to it, what a multi-task brief must carry that a one-task brief does not, how it is closed, and what a
  check could verify. It would let planning be split instead of every task being planned and launched up front, and
  it keeps the context of linked tasks. Researched 2026-10-15 (`meta/reviews/`); the design round with the owner
  comes before any text. *Estimate:* a design round and about half a session to write. *Collides with:*
  `prompt-context.md` §*Long runs and delegates*, which 0.0.32 has just changed for delegates
  (`d-5ed7e8-6069fe`), and the delegate-brief bullet.
- **`i-5ed7e8-023814` · The session proposes the split itself, after a thinking step.** The owner asked for
  parallelising to be something the session offers, not something they have to ask for — and for the method to
  carry the *reasoning* that reaches it, not only the rule. The step, as it worked in practice on 2026-10-15:
  list the remaining work; group it by the **files each piece writes**; split only where those sets are disjoint
  and nothing downstream waits on the piece; say why it is split that way, which model each piece gets and what
  it is expected to cost; name what cannot be split and why (the same files, a generated artefact two pieces
  would rebuild, a step the next one depends on). Three batches ran that way in one session — research,
  bookkeeping, review — and the only collisions avoided were file collisions. What is missing is the method
  text, where it lives (`prompt-context.md` beside delegation, or the plan's own procedure), and a check: a
  session that delegated, with no split stated, is the thing to measure. It belongs with `i-5ed7e8-55e022`
  (cost) and `i-5ed7e8-d6ecfe` (warm against fresh delegates), since the three answer one question — what a
  session spends and on what. *Estimate:* a design round and about half a session to write. *Collides with:*
  the delegation paragraphs of `prompt-context.md` and the batch and ledger candidates already queued.
- **`i-5ed7e8-55e022` · Cost as a principle, with a check.** Today the bundle holds four scattered candidates
  (a delegation priced before it starts, a plan's cost ledger, a remaining budget re-ordering the plan, a board of
  what is active) and no principle. What the owner asks for: optimising tokens, recommending how to shape tasks,
  reading the window and the kind of context available, and treating the launching of agents as a priced decision —
  as one numbered principle with something a tool can measure. Researched 2026-10-15 (`meta/reviews/`).
  *Estimate:* a design round, then a principle and its check. *Collides with:* the principles' numbering, the
  coding session's token budget (about 215 tokens of room), and the four candidates, which the principle absorbs or
  leaves as occurrences.
- **`i-5ed7e8-7e0dd7` · Traditional development and the method in one repository.** A session that uses no agent,
  or uses one without this method, changes files, takes decisions, edits procedures and merges work without minting
  an id, writing a log entry or passing the gate; today that surfaces as a red check nobody can close, or as drift
  nobody notices. The repository must hold both modes without either damaging the other or the method's purpose.
  It is the one item of the three that can break the protocol from outside. Researched 2026-10-15
  (`meta/reviews/`); it builds on the candidate that a convention only one party follows degrades to a suggestion.
  *Estimate:* a design round, then the enforcement change and its check. *Collides with:* the git hooks, the gate,
  `bundle.py ids`, `decisions`, `docs-drift`, the append-only log and the checksum manifest.

- **`i-5ed7e8-f0680a` · Parallelisation only where it lowers cost, measured.** The owner's
  short-term objective, stated 2026-10-15: improve how tasks run in parallel, **bounded to cost
  optimisation** rather than to speed. So the pilot's question is not how many agents can run at
  once but which splits pay for themselves — a delegated reading on a cheap model against the same
  reading done in the main thread, with the price quoted before the launch and compared after.
  *Estimate:* unknown until the cost pilot (`d-5ed7e8-5b183e`) has numbers; this item is its
  acceptance criterion. *Collides with:* the cost pilot, which it scopes.
- **`i-5ed7e8-be0f54` · A plan proposes decisions, prices risks and measures before executing.** The
  owner's second objective, same day: more autonomous **plan generation** — the agent proposes the
  decisions a piece of work needs, names its risks, and measures what it can before executing — on
  the condition that the plan is always shown for validation and follows the standing guidelines.
  The autonomy asked for is in the *preparation*, not in the execution: the owner was explicit that
  continuous supervision has worked better than autonomous work (see the same day's close), so what
  this item buys is a better-prepared decision, not an unattended one. *Estimate:* a procedure and
  a skill change; the measuring half is the expensive part and is where the plan earns its keep.
  *Collides with:* the planning documents a carrier keeps, and the pre-review the long skills open
  with.

- **`i-5ed7e8-36d9b1` · `user-walk` reaches its trigger gate.** 0.0.31's eval left it at a lenient fire of 0.58 and the owner's own words at 0.29, its cases taken by a debugging and a brainstorming skill that ask to run first, a
  longer description gaining nothing (`meta/reviews/2026-10-09-trigger-eval-and-audits-0.0.31.md`). Try a routing line in a carrier's root file (what a person does or meets in the app goes to `user-walk`, which opens with its pre-review), measured with the same cases. *Estimate:* an hour and a run of about ten minutes.
  *Collides with:* the root file's budget, the `user-walk` description.
- **`i-5ed7e8-6cf312` · `bundle.py new entry` refuses a missing log in one line, and the home names its session
  log.** **Half done on 2026-11-24:** this repository now names its session log, and the file exists with its first entry. The other half stands and is worse than recorded — asked to write into a log that does not exist, the command does not refuse in one line, it raises an unhandled error and prints a traceback. Today it raises a traceback; the home keeps its hand-offs in `meta/archive/roadmap-states.md`, which the
  close skill's step 3 does not know. *Estimate:* an hour with a test. *Collides with:* `new entry`, the close skill.
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
- **`i-5ed7e8-94f262` · Review the method changes published on one carrier's evidence (0.0.26 and 0.0.27).**
  Each is marked *one carrier's evidence* in `.agents/CHANGELOG.md` and `meta/tracking/history.md`: keep it
  where a second carrier's entries or harvest show it acting, rework it where they show friction, withdraw
  it where nothing used it. *When:* at the next release that takes in harvests from carriers on 0.0.27. *Not
  triggered in 0.0.30* (2026-10-08): no carrier's harvest was taken in; it waits for 0.0.31's.
  *Collision:* the coding session's budget, if any is withdrawn from the session loop.
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
     (`carrier.toml`, `proposals/`, `incoming/`). **An optional field counts** (`d-5ed7e8-79ed41`): 0.0.37's
     `[red_check]` table restarted the count, so the earliest release that can meet this one is the first whose
     predecessor changed none of those files.
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
- **`i-5ed7e8-688897` · Residuals of the 0.0.22 and 0.0.23 adversarial reviews, none of which can lose a carrier's record.**
  From `i-5ed7e8-d3ee51` (`d-5ed7e8-c11cbb`), each reproduced there (the `verify --release` one was already fixed by 0.0.2x and is pinned by a test since phase 1; `install-skills` over a hand edit fixed in phase 1, though a `SKILL.md` whose line endings git converts to CRLF no longer matches its hash and is refused): a refused-files list that can never be complete; the YAML subset proven against PyYAML only by
  `check_yaml.py`; a converted carrier's own links to moved files (its gate catches them); the banner in a `.md` opening
  with an unclosed thematic break and after a shebang's encoding line; the session loop's steps 3 and 4 citing full
  notes; the working invocation's `Reads:` not reaching the *Done* checklist (over the coding budget). From the 0.0.36 adversarial review: `install-skills` overwrites a hand-edited `SKILL.md` that keeps its banner, which `verify` flags only before the install. *Estimate:* the
  first and the banner, 20–30 min wall, 80k tokens, one round; the text ones wait on the budget. *Collides with:* nothing.
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
- **`i-5ed7e8-d4f710` · Review overlapping notes as principles.** **The owner's direction, 2026-11-26 (`d-5ed7e8-caf7f3`):** complementary cards are merged into one with several boundaries, as part of the cleanup. The efficacy pilots found that
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

- **`i-5ed7e8-17f776` · Topic-based export, deferred (`d-5ed7e8-66e39b`).** The export stays whole. **Reopens when** the `seen_in`
  field (`d-5ed7e8-ab488f`) shows a topic whose occurrences sit in one domain with two or more independent sources; then a
  carrier declines a topic in its `carrier.toml`, never by inference from its domain. *Estimate:* 45 min, 100k
  tokens. *Collides with:* nothing.

- **`i-5ed7e8-cd4d28` · `privacy --commits` and `--tracked` can excuse a quote with the working tree's own text.**
  A WARN only. *Estimate:* about an hour with a test. *Collides with:* the `quote` rule.
- **`i-5ed7e8-8fd079` · `align` still stops on a malformed carrier id, and skips the name-collision check for
  missing paths.** A hand-edited id stops it; the collision check is not applied to a path with no bundle.
  *Estimate:* about an hour. *Collides with:* `B.workspace`.
- **`i-5ed7e8-33d69a` · The cut measures the export before `set_version` and `build`.** Also tidy `manifest_problems`'
  unused `export_cap` and the `release()` docstring. *Estimate:* under an hour. *Collides with:* the cut.
- **`i-5ed7e8-91dfa5` · `export --replace`: `copyfile` follows a symlink at a listed destination path.**
  *Estimate:* about an hour with a test. *Collides with:* `export --replace`.
- **`i-5ed7e8-551b78` · `install-skills`: the skip logic lives in two places, and "an installed copy is kept" is
  said of a hand-written `SKILL.md`.** *Estimate:* about an hour. *Collides with:* `install-skills`.
- **`i-5ed7e8-198d1a` · `new entry`: the exactly-half boundary is untested, and the message should say "another
  language or format".** *Estimate:* under an hour. *Collides with:* `new entry`.
- **`i-5ed7e8-754e07` · `prompt-sync.md` Phase 2's intro also gates what is carried, yet sits in Phase 2.**
  *Estimate:* minutes of prose. *Collides with:* the cut.
- **`i-5ed7e8-0abe37` · The suite prints argparse usage for `test_bundle.py`'s `run("digest", ...)`.** Output noise,
  pre-existing. *Estimate:* minutes. *Collides with:* nothing.
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

- **`i-5ed7e8-88cd88` · One carrier's 0.0.34 update is spliced and verified but not committed.** Its gate is red
  on a concurrency test that fails about three runs in four on its own last commit, in a clean export with no
  splice, so the update did not cause it; the commit rule forbids committing on red. The splice, the prune, the
  refreshed skills and the changelog entry are uncommitted in its harvest worktree. What unblocks it: the test
  fixed first, or the owner's word for a red commit marked as such. Carriers registered below 0.0.34 and not on
  this machine are reached from the machine that holds them.

- **`i-5ed7e8-9a72da` · The method has never been validated against a carrier of another owner.** Every carrier of
  this bundle belongs to one owner, so agreement between carriers on a method rule measures the reach of that
  owner's global instruction file, not the rule's generality (`d-5ed7e8-5663c8`). Seven queued method rules rest on
  that agreement alone. What unblocks it: a repository of another owner running the method, or a measured effect of
  one of those rules in a single carrier. *Estimate:* nothing to build; it is a fact about the evidence, re-read at
  each admission. *Collides with:* `sources/README.md` §1 and every method candidate's *Lacks*.

- **0.0.31 carried to three more carriers on 2026-10-09** (the owner named them; each on its 0.0.30 branch with `main` merged in, then fast-forwarded to `main` and pushed). All three are registered and aligned (one's feature branch took `main` by a merge). Each update was then finished with the owner the same day: root-file wiring (`usage brief`, principle 15, the guide), decisions logs migrated to the Status column with the check in each gate, permission rules per 0.0.31 (two needed the owner's authorization to edit a settings file), `/next` run headless, and four proposals harvested from one carrier for the next intake. The rest of this machine's carriers (nine, two with no bundle on disk) wait until the owner names them.
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
  unmerged, so its integration branch holds no bundle yet and `align` over the manifest names it as not
  aligned with the branch that holds the bundle (`i-5ed7e8-e44264`, done).

**At the close of 0.0.33**, none of the 23 carriers reachable on this machine was spliced: the owner
  deferred phase 2 so the cut would land the same day, and the release is carried to them in the session that
  also carries 0.0.34. Two carriers hold a bundle older than the one before last — one on 0.0.25 and one on
  0.0.26 — and neither records an obstacle: nobody opened a meta-session over them. one repository holds a
  release and has never minted a carrier id, so it is not a carrier and offers nothing; another has the bundle on
  two branches that were never merged while its integration branch advanced two months without it, so `gather`
  reads no bundle on disk for it. Both wait on the owner. Every carrier only the other machine holds
  is reached from there, with its own session. *Blocked on:* a session with each open, and for the last two, the
  owner's word.

## Closed by measurement

- **`i-5ed7e8-25fd85` · `lineage` is not left unwritten by an update; closed 2026-11-25 by reading.** Every one of
  the sixteen carriers spliced to 0.0.34 records `0.0.34` with the home and the day: `proposals --prune` appends
  it, and the phase-2 report that raised the item read the field before the prune ran. No carrier lists 0.0.33,
  which is correct: none took it apart from 0.0.34.

- **0.0.22's wiring, summary before note, keeps normal tasks at most ×1.5 of `minimal`** (`i-5ed7e8-c4b9c7`, predicted
  in `.agents/CHANGELOG.md` [0.0.22]): **refuted** by pilot-6, 2026-09-28, at ×2.8 [2.0, 3.3] over four
  tasks. The trivial-task half of the prediction held (×1.0). Kept so the same packaging is not proposed as
  a saving again; what replaces it is `i-5ed7e8-1a57cc` and the phased session.

## Done

- **2026-11-26: two items phase 1 finished but left in *Next*, found at the next session's start**: `memory-diff` from a worktree (lane B, `9331e02`) and the update and bootstrap reads trimmed (lane A, `5924e91`). The items, whole:
  - **`i-5ed7e8-11e17f` · `memory-diff` from a linked worktree reads the repository's memory.** It reads the
    worktree's own, empty, folder; `--memory` is the workaround. *Estimate:* an hour with a test. *Collides with:*
    `memory-diff`, `close`.
  - **`i-5ed7e8-0ae753` · Trim the update and bootstrap sessions.** The update's `Reads:` names
    `prompt-context.md` §*Which document to run*, which pulls in two subsections it never uses (about 700
    estimated tokens); the bootstrap states the minting instructions twice; `knowledge/OPEN.md` is about
    half of a harvest's load. *Collides with:* the `Reads:` lists and `report --check` budgets.

- **2026-11-26: the two guard wirings applied at the owner's word** at the close: the zsh check in the command hook and `build --check` on an export of the index in the pre-commit hook, each probed live. The items, whole:
  - **`i-5ed7e8-4cf7df` · Under zsh, an unquoted list variable in the agent's own command, three incidents.** Counted in the **2026-11-26: the check is built and tested; its wiring into the guard waits for the owner's approval of the edit** (`meta/plans/2026-11-26-phase-2-guards/`).
    session log: twice on 2026-11-25 in the 0.0.34 work, and once more at the 0.0.35 close, within the hour the
    ladder gained a sentence about it (`prompt-context.md`). The text did not hold, which is the ladder's own
    prediction. What would: the host's command hook refuses a command that expands an unquoted variable holding
    spaces where zsh is the shell, naming the fix (an argument vector, or `${=var}`), with a test of each form.
    Received as `p-069d110c27`. *Estimate:* 30–45 min wall, 100k tokens, one review round. *Collides with:* the
    privacy guard, the other command hook, which must keep running first.
  - **`i-5ed7e8-a4c2b2` · The home's pre-commit hook runs `release.py build --check`.** It runs only the **2026-11-26: the check is built and tested; its wiring into the guard waits for the owner's approval of the edit** (`meta/plans/2026-11-26-phase-2-guards/`).
    privacy gate, so a commit whose release folder is behind its sources passed it at the close of 0.0.25
    (and was pushed, because the check that failed was piped through a filter; proposal
    `a-filtered-gate-cannot-block`). Add the build check to the hook and plant a stale generated file to see
    it refuse. *Collision:* every commit here gets slower by one build check.

- **2026-11-26: phase 2's tool lanes** (`meta/plans/2026-11-26-next-phase-2.md`): `bundle.py red-check` (`d-5ed7e8-8c417c`), the privacy ratchet (`d-5ed7e8-af36e9`), `release.py commit` and `release.py dequeue`. The items, whole:
  - **`i-5ed7e8-468621` · A fix's test written beside it, so its red is never seen: three incidents in one session.**
    In the 0.0.36 plan's review rounds, three fixes went in with their test in the same command, so the test was never
    seen failing, against §18's "say which red each test showed"; the roadmap's plan table names each. The sentence
    was loaded and did not hold. What would: the controller sends the test and its run as one command and the fix as
    the next, never both at once, and a fix commit whose test was not seen red says so in its message. Next step: a
    `bundle.py` check that a `fix` commit touching code also touches a test is cheap but proves nothing about the order.
    *Estimate:* the habit, nothing; a check, 20–30 min wall, 60k tokens, one review round. *Collides with:* nothing.
  - **`i-5ed7e8-655151` · Moving a candidate row to the history is done by hand at every release.** Second
    occurrence, counted: 0.0.31 and 0.0.32 both moved rows between `meta/tracking/candidates.md` and `history.md`
    by hand, and 0.0.32 shipped nine answers whose rows a reviewer had to find — the release had left them queued.
    A `release.py` subcommand that takes a slug, a verdict and a release, removes the row and writes the history
    line would make it one checked command, and a check could refuse a release that ships an answer whose row is
    still queued. *Estimate:* about two hours with tests. *Collides with:* `candidates.md`, `history.md` and the
    ledger the build generates.
  - **`i-5ed7e8-89ec30` · Refuse a commit chained on a gate whose output goes through a filter.** The second occurrence in
    this repository (0.0.25 committed and pushed a stale release folder; on 2026-10-05 a commit landed with three
    generated files stale), each time the gate's status was the filter's. The rule is in the close skill and the
    bootstrap; it does not act at the moment the command is typed. *Remedy:* the session hook that already guards
    `git commit` refuses a command where a gate's output is piped before `&& git commit`, unless `pipefail` is set;
    about half an hour with a planted test. *Collision:* the hook's other checks. *Again on 2026-10-07:* the unit tests piped into `tail` before
    `&&` in a chained commit; they passed, so nothing landed red. See `i-5ed7e8-bd65a0`, which removes the typed chain.
  - **`i-5ed7e8-bd65a0` · A home command that runs the gate and commits the named files.** Two frictions recur in the
    typed chain `tests && check && git add && git commit`: a gate piped through a filter (`i-5ed7e8-89ec30`, four
    occurrences in the archived hand-offs) and an edit chained into the same command as `git`, which the privacy hook
    refuses whole so the edit never lands (twice, the last two sessions). *Remedy:* `release.py commit -m MSG FILE...`
    runs the tests and `check` on their own exit status, prints the failures, and commits only the named files; the
    root file's checks section names it as the one way to commit here. About an hour with tests. *Collision:*
    `i-5ed7e8-89ec30`, the privacy hook.
  - **`i-5ed7e8-1e9567` · Resolve the persistent privacy warnings.** The same warnings print on every
    run and none changes; a warning that is always there stops being read. Reword each line or, where the
    user explicitly decides it may stay, mark it with a reason. *Collides with:* nothing but the warned
    lines.

- **2026-11-26: phase 2's records lane** (`meta/plans/2026-11-26-next-phase-2.md`, task 7 and 8): four queued extensions admitted into their notes and the queue's three defects fixed; the eval instrument's four remaining defects fixed; `docs fingerprint` named in `prompt-sync.md`. The items, whole:
  - **`i-5ed7e8-fe15a8` · The fifty-four oldest candidates, read, and three defects the queue itself carries.**
    Reviewed on 2026-11-24 (`meta/reviews/2026-11-24-oldest-candidates.md`): every row whose *Since* is the
    twentieth or twenty-first patch, twelve or thirteen releases of waiting. The largest harvest so far rewrote
    four of the fifty-four and cleared none: everything it added is marked in the rows themselves as one owner's,
    so it adds occurrences, not sources. Seven are blocked by the owner-agreement item alone, fifteen want a
    second repository, eight want a measurement nobody has run, and six want only a release's decision. Six could
    be decided at the next intake, all extensions of active notes whose literature the note already carries, two
    of them with a recorded experiment that confirms a form the note does not yet hold. **The queue's own
    defects, which matter beyond those rows:** one row cites two slugs that exist nowhere — as a note, a row or a
    history entry — one of them described as folded at a release; two rows are the same claim written twice; and
    one row's *Lacks* asks for evidence its own *Evidence* column now carries. The slug check written the same
    day does not catch these, because it reads only rows claiming a note was admitted. *Estimate:* the six
    decisions belong to an intake, one turn each; the three defects are about twenty minutes. *Collides with:*
    the next intake, which rewrites the same rows.

  - **`i-5ed7e8-1e9c1c` · A prose reduction pass is checked cut by cut by a reader other than its writer.** Twice in
    0.0.31 a pass listed each cut as `removed: … (restated by …)` and still dropped a rule (the incoming tool's exception;
    five rules), found only by a later review. *Estimate:* a paragraph in `prompt-sync.md` and a proposal; or a script
    that lists each removed sentence's rule words (numbers, commands, ids) and greps the rest for them, about two
    hours. *Collides with:* the next reduction pass.
  - **`i-5ed7e8-e09738` · The eval instruments' findings deferred at the close of 2026-10-07.** *Half done on 2026-10-08:* `review.py` now records a failed session as an error and retries it on resume; a command is judged whole. Left: standard error not drained, canaries all errored, a stopped run's verdict, the harness hash on resume. An isolated review of
    the code merged that night (a mid-size model) found, besides the three fixed before the merge: `evals/review.py`
    scores a session that exited in error as a valid trial and never retries an errored one on resume (high, medium;
    checked against the data: no trial of `review-1` or `review-2` crashed or timed out, but three, all `R2`, reached
    the turn limit without naming the target; D2 was read with and without them, `evals/REPORT.md` §4.13); `trigger.py` judges a command cut to 200 characters, does not drain standard error,
    calls a run valid when every canary errored, and prints a verdict for a run stopped by errors (low); the
    harness's frozen hash is not checked when a run resumes (low). A possible gap, an overlay's new file missing from
    the reviewer's diff, was checked: no diff adds a file. *Remedy:* each under a test, before the next pilot run.

- **2026-11-25: fifteen *Next* items found done, obsolete or closed by the triage** (`meta/reviews/2026-11-25-next-triage.md`, phase 1 task 1), moved here whole:
  - **`i-5ed7e8-2ebcee` · A command that carries a push is refused whole, and the writes in it never land.** **Done 2026-11-25 in 0.0.35:** the close skill and `prompt-sync.md` spell the push as a step of its own.
    Second occurrence on 2026-11-24: a push chained after a check was refused by the host's permission
    classifier, and the same push alone went through. The root instruction file already carries the rule —
    never put an edit in the same command as something a permission rule may refuse — which means the rule is
    text, and text is the ladder's weakest rung. What would hold instead: the close and the release procedures
    spell the push as its own step, so no agent composes it; and where a repository has a command that runs the
    gate and commits (`i-5ed7e8-bd65a0`), that command never takes a push. *Estimate:* a line in each
    procedure, about twenty minutes. *Collides with:* `i-5ed7e8-bd65a0`, whose shape this constrains.

  - **`i-5ed7e8-9ef5d1` · A voluntary, anonymised path for usage evidence to enter a record.** The owner's ask of
    2026-11-24. The standing rule is that usage data stays on its machine and only a generalised figure the owner
    approves enters a record. That rule has no procedure behind it, so in practice nothing ever enters: on the day
    it was raised, four weeks of local usage data were read, produced a picture of how the work actually goes, and
    **not one figure of it reached any record**, while *a measurement nobody has run* is the blocking reason on
    eight of the fifty-four oldest candidates. The rule is not wrong; what is missing is the step that lets it be
    obeyed and still used.
    **The shape, to be designed with the owner one decision at a time, not written straight out:** the tool already
    holds the local store, a consent level, a retention and a `brief`. What it lacks is a step that takes a
    question — *how often does this happen, over what* — and returns an answer already generalised to a ratio or an
    order of magnitude, with the raw figure shown only to the owner, who then approves or refuses it entering a
    named record. Three things that decide whether it works: the generalisation must happen in the tool, not in an
    agent's prose, or the rule relies on the thing it is guarding against; the approval must name the record the
    figure enters, since a figure approved once is not approved for everywhere; and a refused figure must leave a
    trace saying a measurement exists and was withheld, so the candidate's *Lacks* stops claiming nobody has run
    one. Whether a second machine's figures may be combined is its own decision, and the answer is probably no
    while each machine is one person.
    *Estimate:* a design round with the owner, then about a session to build with tests. *Collides with:* the
    standing rule itself, which this makes executable; `usage`'s consent model; every candidate whose *Lacks* is a
    measurement; and the privacy check, which must still fail on a figure that identifies anything.

  - **`i-5ed7e8-a98470` · The decisions check counts what it means.** **Done 2026-11-24**: the count now reads twenty-nine, with the agent's own nine on their own line. Two faults, found by using it on
    2026-11-24 (`d-5ed7e8-2f51c2`). A row whose status is `superseded by` or `deprecated` still counts as
    unconfirmed, though its reason is history and no person will ever be asked for it: six of forty-four. A row
    decided by an agent can never clear, because its reason is an agent's by definition, while the status column
    already says `· agent`: nine more. So fifteen of the warnings name nothing anyone can act on, and a count
    that cannot reach zero stops being read — the same failure as a warning on standard error that nobody looks
    at. The fix: skip superseded and deprecated rows, and report the agent-decided ones as their own line rather
    than inside the same number. What is left is the rows a person accepted whose reason a person never gave,
    which is what the warning was for. *Estimate:* about half an hour with tests, including one that a
    superseded row stops counting and its successor starts. *Collides with:* `release.py check`'s own output,
    which several closes quote by its totals.

  - **`i-5ed7e8-ee9f86` · Count what of the carrier tool a carrier never runs.** `tools/bundle.py` is 276,091
    bytes, 27% of the release and its single largest file, and nobody has asked which of its commands a carrier
    invokes. The question is the owner's, put on 2026-11-24: content whose only reader is a session that already
    has a home open costs a carrier nothing to lose, which is not the same as reading it from the home over a
    network — a carrier has no route to one and must not need one. So the work is a count, not a change: for each
    command, which session's file names it, and whether any of them is reachable without a home. Only then is
    there a decision to put. **Counted the same day** (`meta/reviews/2026-11-24-carrier-tool-commands.md`), and
    the answer is no: of twenty-five subcommands, none is named only by a file that exists in a home. Every command
    with a mention in the home's own method also has one in a file a carrier reads by itself, and the single command
    no method file names at all is run by the home's pre-push hook, which does not ship. So there is no home-only
    content in the tool by name, and that share of the release is not a saving. What the count does not show:
    whether a carrier runs everything it names, and whether home-only code hides in shared helpers, which are
    attributed to no command. A second, independent count the same day confirmed the verdict and
    corrected the first one's line figures, which measure dispatch blocks and understate the size of a command
    several times over; both are recorded in the review. Neither pass asked who actually *runs* a command, as
    against who names it, and a count by that measure could still find a home-only class. *Left:* nothing to
    build; the item closes at the next cut. *Collides with:* nothing.
  - **`i-5ed7e8-57358a` · Remove the product-noun check and its list.** **Done 2026-11-24**, except the changelog line, which belongs to the next cut's section. Decided by the owner on 2026-11-24
    (`d-5ed7e8-aa5d67`, superseding `d-5ed7e8-e0a56e` and `d-5ed7e8-4f76c8`), who asked whether the ban was
    wanted at all. Delete `meta/product-nouns.txt`, the `product_nouns` and `_product_cues` helpers, the cue
    problem they raise, and the tests that cover them; say so in the changelog, since a carrier's audit may
    expect a build to fail on such a cue. What replaces it is nothing: generality is step 2 of admission, which a
    person applies, and a product name that would identify a carrier is the privacy check's. *Estimate:* about
    twenty minutes with the tests. *Collides with:* `_note_problems`' signature, which several callers pass
    `nouns` into, and the changelog line that announced the check. It also closes `i-5ed7e8-6155a1`, which asked for the
    same check to stop false-positiving on punctuated and short nouns: the item was removed from *Later* when the
    check went, and its text is in the history at the 0.0.33 cut, kept here so nobody proposes it again.

  - **`i-5ed7e8-26a753` · The worktree's environment rule gains the exception its own note supports.** Decided by
    the owner on 2026-11-24 (`d-5ed7e8-381ef9`, superseding `d-5ed7e8-05fcd3`). Today the rule forbids a fresh
    environment inside a worktree outright and has every such result reported unproven; the note admitted at
    0.0.33 holds, on hermeticity literature, that an environment built for the copy is the better answer wherever
    it can be afforded. The rule becomes: build it where that is cheap and reproducible, and the result is proven;
    otherwise use the main working copy's and say the result is unproven. The two places that carry the rule — the home's
    sync method and §*4. Verify*, which is what a carrier reads — are rewritten together, and the note gains the
    cross-reference. *Estimate:* a paragraph in each, about half an
    hour, plus a line in the note. *Collides with:* every carrier update that reports a gate's result, since the
    word *proven* now means different work in different repositories and the report must say which.

  - **`i-5ed7e8-25ecc8` · `usage` drops a `.gitignore` beside its state folder.** **Done 2026-11-24**, with a test that a file symlinked out of the tool's folder leaves no `.gitignore` behind it. Decided by the owner on
    2026-11-24 (`d-5ed7e8-011bc5`, superseding `d-5ed7e8-eb2c2f`): the first write creates a `.gitignore` holding
    `*` in the tool's state folder, so a home folder that is itself a working tree cannot commit the usage data.
    The write there stays allowed and the warning stays, since it is still worth saying; what changes is that
    ignoring it no longer leaks. *Estimate:* about half an hour with a test that the file is created once, is not
    rewritten over a hand edit, and that the data is ignored by a repository rooted at the home folder.
    *Collides with:* nothing in the release; the tool's own tests of the refusal path.

  - **`i-5ed7e8-8b542b` · `bundle.py ids` resolves a note slug cited in a tracking table.** **Done 2026-11-24, and not where this item said:** a carrier holds neither the tracking tables nor the note sources, so the check lives in the home's own `check`, not in the tool every carrier runs; and it reads only rows that claim a note was admitted, a naive pass having left seventy-eight slugs unresolved that are rightly not files. Today `ids` checks the
    format of record ids and catches a decision cited and defined nowhere, but a **note slug** written into a
    tracking table is read by nobody: it is prose to the tool. On 2026-11-24 two slugs were written into the
    history table as admitted at the release being cut, from memory, and neither existed; they were plausible in
    form and in subject, and were found by a later search rather than by any check. The table is what the next
    release reads to know what was admitted, so an invented slug there is carried forward as fact. Every slug in
    those tables is mechanically resolvable: it names a file under the notes folder, in one of the three states,
    or a row of the queue. The check is therefore cheap and exact, and it is the `lacks` of the proposal this
    session wrote (`p-75679cf56f`). *Estimate:* about an hour with tests, and a first run that will probably find
    older slugs the tables already carry. *Collides with:* the tables' own retired and refused rows, whose slugs
    name files that no longer exist under any state, so the check needs the retired folder and the refused history
    in its resolution set before it can be made to fail a commit.
  - **`i-5ed7e8-5e0415` · `changelog --since` answers for a version it no longer holds, silently.** **Done 2026-11-24.** Asked for a
    version older than the oldest section the file still carries, it returns what it has and exits zero, saying
    nothing about the gap. A carrier two or three versions behind would therefore receive an answer that looks
    complete and is not, and the agent reading it has no way to tell. Found on 2026-11-24 while weighing whether to
    archive the oldest changelog sections to stay under the export cap; the archiving was rejected for this reason
    and the cap was raised instead (`d-5ed7e8-929f2a`), so the defect is now the only thing standing between the
    bundle and that option. *Estimate:* about half an hour with tests: name the oldest version held, and exit
    non-zero when the requested one is older than it. *Collides with:* any carrier update session that reads
    `--since` to decide what changed, and the archiving option this defect currently blocks.

  - **`i-5ed7e8-045188` · A delegation's estimate is written down before the launch.** **Eight pairs counted on 2026-11-24**, the first set this repository holds: every estimate was too high, the bounded read-only ones by ten to fifteen times, the editing one by about six, the reviews by five to fifteen. The direction is consistent, which is what makes it correctable; the pairs are in that day's session-log entry and in the local usage store. Counted, not remembered: the
    symptom appears twice, once in an earlier hand-off ("a large plan's estimate") and once on 2026-10-15, when
    three research agents were announced at 120–200k tokens and 15–25 minutes each and cost 19k, 55k and 69k in
    about a minute — **2.5× to 4× out**, and the announcement itself exists nowhere written, so the pair that would
    have calibrated the next one does not exist. The fix is the cheap half of `i-5ed7e8-55e022`: the estimate goes
    in the message that launches the batch *and* in the plan's ledger, and the actual is written beside it when the
    agent returns. *Estimate:* a line in the method and a column in the ledger, under an hour. *Collides with:* the
    cost ledger and board candidates already queued, and `i-5ed7e8-023814`.
  - **`i-5ed7e8-2a2e86` · A partial gather waits for the remaining carriers before intake.** Four
    carriers were harvested and closed on 2026-10-15 and offer **44 proposals** between them (17, 17,
    6 and 4); the owner holds at least one more carrier whose harvest comes separately, so the intake
    is deliberately **not** run: the pending state is the proposals themselves, committed in each
    carrier and reported by `gather` as waiting, and `gather` is read-only and repeatable over the
    full set. Verified at the time: every one passes the gathering step's privacy check, none held
    back. Worth knowing before the intake: three of the method proposals restate instruction lines
    this roadmap already records under *Blocked outside* for another machine (ids with a name table,
    the interaction designed as a flow, a delegation priced on the cheapest model) — they arrive with
    reasoning and evidence rather than as news, and the release decides whether that is enough to
    make them notes. *Next session's first step:* re-run `gather` over every carrier the owner names,
    including the one still to be harvested, and only then give the one table its verdicts.
    *Estimate:* the gather is minutes; the verdicts are the work. *Collides with:* nothing, while the
    intake is not run; a release cut before it would simply not carry them.
  - **`i-5ed7e8-b8c4b2` · The privacy check's false positives on the home's own prose.** **Done 2026-11-25 in 0.0.35,** every recorded shape with a test that the leak beside it still fails; the five allowances already written stay. **Two more on 2026-11-24, so eight over three sessions:** a decision id beside the ordinary English word for a working copy, reworded, and one beside a figure in a record. Four in one session, each worked around by rewording: a domain noun used as a unit of length beside a record id failed twice; a later release number read as a dependency pin failed once; a commit hash of digits only, and a regular expression's repeat count, warned as exact counts. **Two more on 2026-10-15, in this release's own records** (`d-5ed7e8-5663c8` beside the English word *debt*; the host's public minimum version after *requires*), and by the owner's instruction they are allowed in place with `privacy-allow` and their reason rather than reworded again — **this item is the debt, and the owner has asked that the rules themselves be fixed in a later release**, not that each occurrence be dressed around. Two were also reworded the same day (a bundle version after *cuts*, a word read as a domain noun), so the count now stands at six failures over two sessions. *Estimate:* about two hours with tests: skip a domain noun used as a unit after a number, a version after `release`, `requires` or `cuts`, and a hex hash. **A second gap found the same day:** in a table row the documented placement (the marker on that line) cannot be written at the end of the line, because the column check then counts an extra column, and the marker is not read if any backtick follows it — so it has to go inside the last cell. Both belong in the fix. *Collides with:* the rules' tests, which must still fail on a real leak, and `bundle.py decisions`' column count. <!-- privacy-allow: this item's own id beside the English word debt, the very false positive it records; allowed by the owner on 2026-10-15 -->
  - **`i-5ed7e8-780330` · In an isolated worktree, version-control calls go in plain separate commands.** The host
    refuses a compound command, a `-C` or `cd`, a variable where an option may stand, or any text naming git in a form it
    cannot verify; a script written to a file runs. Say it once in the method's worktree rule. *Estimate:* a few lines.
    *Collides with:* `prompt-sync.md`, the `close` skill.
  - **`i-5ed7e8-cc0b86` · Queue the experiments the five other new 0.0.27 notes name.** Only two of the
    seven admitted notes had their experiment queued in `meta/tracking/experiments.md`. *Collision:* none.
  - **`i-5ed7e8-d3ee51` · Close the residual gaps the adversarial review of 0.0.22 left open.** **Closed 2026-11-25** (`d-5ed7e8-c11cbb`): `note-state` made to check before it moves, in 0.0.36; the seven other residuals moved to `i-5ed7e8-688897`. Two rounds
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

- **`i-5ed7e8-c0341d`, 2026-11-25: the usage state folder honours an `XDG_STATE_HOME` the user set on macOS too**,
  so the three tests that steer it pass on this machine; a new test pins both platforms.

- **0.0.34, 2026-11-25: cut and tagged `v0.0.34`, spliced with 0.0.33 into fifteen carriers and the template on
  their own branches, nothing pushed.** Its scope: the harvest of this machine's carriers (90 proposals, 72
  occurrences added, 15 queued), one note boundary narrowed, six tool fixes with tests seen to fail first, the
  two-kind pause, the product-noun check removed. Sixteen carriers aligned. Session `s-5ed7e8-c1ada9`.

- **0.0.32, 2026-10-15: cut, tagged `v0.0.32`, taken by this home and by one canary carrier** (unpushed). Its
  scope: five tool fixes with their tests (the researcher's hook failing closed, the proposal title, the
  record-id allowance and the bullet definition, the word-boundary count, the privacy parity over a proposal),
  seven method changes (the delegate's foreground split; the commit rule in the delegate brief; what a permission
  rule cannot see; the author and committer channel; why a question's three parts matter; the update reading a
  delta that changes itself and naming which tool verifies across a shape change; the harvest showing its
  candidates, reading its gaps and counting one owner as one source), a new optional carrier field
  (`harvested_gaps`), the skill-path rule, seventeen folded occurrences, one admitted note
  (`a-workaround-that-writes-the-subject-destroys-the-measurement`), one note out of review, and the intake of 78
  proposals. Records: twelve decisions (`d-5ed7e8-5663c8` to `d-5ed7e8-1ed81d`), four review documents, four
  experiments run. Two fresh-context reviews before the cut found nine defects, all fixed.

Only the last release is kept here; the ones before 0.0.22 are in the home's
`meta/archive/method-changelog.md`, and from 0.0.22 in `.agents/CHANGELOG.md`.

- **0.0.31, 2026-10-09: cut and tagged `v0.0.31` (`17aa53a`).** Its scope below, plus the pre-review (`49d7bcf`), the trigger eval and descriptions by kind (`ef62c32`), the Layout line (`27aad43`).
- **0.0.31 scope, 2026-10-09 (on `main` at `6f9e34b`).** Closed: `i-5ed7e8-d203b6` (`c308f62`);
  `i-5ed7e8-12fcfb` (`017081a`); `i-5ed7e8-2d3b47` (`4011671`); the final review's fixes (`54e8c40`); the reduction
  pass (`6255772`); the shipped tool without comments (`07eb096`); the carrier tool's cleanup (`3446ee1`); the meta
  package, lineage and usage data (`7a3ba7e` to `c061cd2`, `965c245`, `202dc36`); five small fixes (`4cebc0c`); the
  changelog section (`cf4376b`, `6f9e34b`). Described in `.agents/CHANGELOG.md`.
- **0.0.31 tool fixes, 2026-10-09 (not yet cut; branch chain from `fix/coloured-help` to `docs/method-text`, reviewed).**
  Closed: `i-5ed7e8-cce629` (`7063adb`); `i-5ed7e8-74d789` (`f16d7ff`, the intake of the three held proposals could not
  run: no carrier here holds them); `i-5ed7e8-e44264` (`fc67c5e`, `16e0970`: a non-repository path is not read, and a
  carrier with no id is named); `i-5ed7e8-460736` (`cb19add`); `i-5ed7e8-1dd18c` (`f4f5943`, `4491d29`, with the
  prune table approved before the replace, `6bc60fa`); `i-5ed7e8-c390fa` (`40d7a87`, `ed17b76`, `da5d931`, `4b8c539`,
  `f964d35`, `6bb89c5`, `6bc60fa`, `4a49f35`; nothing left of it); and `d-5ed7e8-a3e7e8` (`55285713c9`). Described in
  `.agents/CHANGELOG.md` at the cut.
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
