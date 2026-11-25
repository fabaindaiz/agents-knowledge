# One carrier's process practices against the bundle: planning, implementation, review, reporting, decisions

Date: 2026-11-25. Read-only study of one carrier on this machine, by a delegated reader on a mid model, asked by the
owner; its local evidence (file paths) stayed in a scratch file. Figures are rounded where they could identify the
carrier.

Scope: one carrier, a multi-module app, 284 commits on the checked-out branch and about 340 more on later
lane branches (the newest work is not on the checked-out branch; it was read from the lane branches). Sources: its
session log (about 110 KB, 14 entries), roadmap, decisions (161 rows), 30+ plans and specs, its delegate rules,
its out-of-repo execution workspace, its proposals. Dates 2026-11-11 to 2026-11-25. Verdict words: ABSENT, PARTIAL,
PRESENT (file:line in the home's `sources/bundle/method/`), QUEUED (row in `meta/tracking/candidates.md`).

## 0. The headline the owner should know first

The belief "many improvements not yet absorbed" is only partly true, and the reason matters.

- The carrier already sent 37 proposals, all received at 0.0.33 and 0.0.34 (`harvested_through = 2026-11-24`).
  Most of what its log calls "Learned. General" is therefore already a note, a merged occurrence or a queued row.
- What was NOT harvested is the carrier's way of working that is not a "learning": plan shapes, the execution
  workspace of its delegated lanes, the review-round practice and its numbers, how it prices and re-prices plans,
  how it parks and records owner answers inside plans. These are the findings below.
- Roughly 60% of what looks new maps to a queued candidate or to existing text (principle 21 and the bootstrap's
  step 4 already carry estimate-beside-actual, whole-branch review, merge chained to the gate, batch of unrun
  device work). The carrier follows the bundle's log format, brief format and decision-row format almost to the
  letter, so reporting is largely PRESENT.
- Two findings contradict or strain existing bundle text and deserve a decision, not just an addition: R2 (the
  "at most two re-reviews" cap against measured rounds) and P1 (the plan's unit of estimate).
- Theme 5 (Artifacts) has NO evidence in this carrier. It used throwaway in-app mock screens, not published pages.

## 1. Planning

### P1. Plans and roadmap items are priced per task in "work hours"; the first plan's actual was measured once, later ones never
- Practice: every plan has a price per task (a range) and a total; a scope change re-prices with the delta named
  ("+1 h, because ..."); the total is labelled "an estimate, not a measurement" or "uncalibrated for this
  surface"; roadmap items carry "about N h"; a queue is priced in work hours and then converted to clock hours
  for the lanes that will run it.
- Evidence: at least 12 plans/specs; totals of 35, 41.75, 42.75, 38-46 and 80.5 h. Actual versus estimate was
  written once (first plan: 1 h 20 min wall for tasks priced at several hours each, "estimate stands untested").
  From commit timestamps, a lane's first eight tasks priced 21-25 h landed in about 36 minutes of commits, and the
  next four priced 13-16 h in about 37 minutes; the elapsed time after that was spent in four review rounds (about
  2.5 h). So the price is in a unit (human-equivalent work hours) that the measured work never uses, and the
  measured cost is dominated by review and fix rounds, not building. Nobody recorded the ratio.
- Verdict: PARTIAL. Estimate beside actual is PRESENT (`prompt-context.md:1032`, `prompt-bootstrap.md:526`,
  `skills/close/SKILL.md:73`); the token/cost ledger is QUEUED (`a-plan-carries-a-cost-ledger`,
  `record-the-estimate-and-actual-of-a-delegation`). Missing: say in which unit a plan is priced, and that the
  first plan of a kind writes its conversion (priced unit to measured wall time and review rounds).
- Smallest change: one sentence in `prompt-context.md` section 21.1 and `prompt-bootstrap.md:526`: "price a plan in
  the unit you will measure it in (wall minutes of agent work, review rounds); if you price in human work hours,
  record the conversion after the first plan, and show estimates with the conversion". Fold the carrier's pairs
  into the existing `record-the-estimate...` row as its second occurrence.

### P2. A plan section "Starts after (dependencies)" with a stop rule
- Practice: a table of what the plan consumes (types, functions, schema versions, branches), where each lives
  today, and the sentence "if a row is missing, stop and report; do not build a stand-in". It also says which tasks
  do not depend on the missing row and may run before it, and which task must wait (for example a migration whose
  number depends on another branch landing).
- Evidence: 4 plans (including three written after a lane built a stand-in or merged a dependency itself, and a
  "duplicated merge across lanes" friction). The rule fired once in practice: a lane stopped with a clean tree and
  asked, instead of building around a missing dependency.
- Verdict: PARTIAL. Collisions with live branches are PRESENT (`prompt-context.md:1027`) and QUEUED
  (`a-wide-change-maps-its-live-collisions`, `an-inventory-of-live-branches-with-its-merge-order`). The
  upstream-dependency table and its stop rule are ABSENT.
- Smallest change: one sentence in the plan paragraph of `prompt-bootstrap.md:~521` and in 21.1: "a plan also lists
  what it needs from unmerged work, where it lives, and which tasks wait; a missing row means stop and report".

### P3. A plan section "Review Focus": the failure scenarios a reviewer must probe, each bound to a named test
- Practice: three to five numbered risks (a boundary in time, a setting change while offline, an empty period, a newer
  format version, an upgrade with something already delivered), each naming the task and the test that pins it.
  The plan ends with a self-review that checks spec coverage, that each Review Focus line has its test, that the
  types used across tasks agree, and that the plan is proportionate to the spec.
- Evidence: at least 3 plans plus the specs they came from; the same lanes still logged "a new output without a
  shared case, twice" and "7 fix rounds in 11 tasks", so the section is not proof of effect. Effect NOT measured.
- Verdict: ABSENT (no "review focus" anywhere). Criteria mapped to tasks both ways is PRESENT
  (`prompt-bootstrap.md:~521`).
- Smallest change: add to that same paragraph: "name the risks a reviewer must probe, each with its test; the
  review's brief is those lines". Cheap, and it gives the reviewer brief a source.

### P4. "Builder's calls" and numbered vetoable calls, with a cost-if-wrong clause
- Practice: where a plan resolves a spec conflict or fills a gap, it lists "calls made here (reversible; the owner
  may veto)". The spec numbers its own (V1..V12). When the owner accepts the plan, the acceptance names which
  were taken as written and which vetoed. In the execution ledger a ruling reads "Ruling: X, cost if wrong: Y".
- Evidence: 29 rulings in the first plan, 20 numbered calls in one plan, rulings in 6 ledgers; one veto recorded.
  A friction line in the log: "superseded rulings" (rulings made during execution that a later answer replaced).
- Verdict: PARTIAL. "Rulings taken there go in its ledger, never asked" is PRESENT (`skills/README.md:57`);
  decide-alone-if-reversible is PRESENT (`decision-review/SKILL.md:36`). ABSENT: the cost-if-wrong clause, and
  numbering the calls so acceptance can veto one by number.
- Smallest change: one line in `skills/README.md:57` and `prompt-context.md` section 15: "a ruling names its cost if
  wrong; the plan's acceptance lists the rulings, numbered, for veto".

### P5. The plan carries the owner's answers as a binding section that overrides the body
- Practice: a plan header states "approved by the owner, date; paused mid wave" and a section "The owner's answers
  on this plan" that is explicitly binding "wherever it differs from the body"; open questions stay in the plan
  until answered and the price is amended with the delta.
- Evidence: 5 specs/plans. Cheap and it prevents a builder from reading the stale body.
- Verdict: ABSENT as a precedence rule (answers are recorded by `decision-review`, `unconfirmed:` marker is
  PRESENT, `an-answer-to-a-misdescribed-option-is-superseded` QUEUED).
- Smallest change: one sentence in `skills/decision-review/SKILL.md` where answers are recorded: "in a spec or plan,
  the answers section outranks the body and says so in its first line".

### P6. Task 0 is a set of spikes on a throwaway branch; only a dated note is committed
- Practice: before tasks that depend on unknown platform behaviour, the plan opens with spikes (priced, 5 h),
  run on a branch that is never merged; the spike code is not kept, the note is committed with the exact
  environment and build identity, and ends with "what this changes for tasks N to M". The answers amended two
  later tasks' interfaces and a constant.
- Evidence: 2 occurrences (the first-day build-wiring spike and the later platform spike); in both the spike
  changed the plan.
- Verdict: PARTIAL. A throwaway probe is PRESENT (`prompt-context.md:632`, `:825`; `decision-review/SKILL.md:26`).
  The plan-level gate (spike first, answers mapped to the tasks they can move, price effect "plus or minus 3 h")
  is ABSENT.
- Smallest change: one row in the plan paragraph: "a plan with an unknown the answer to which changes tasks starts
  with a priced spike task; the note maps answers to tasks".

### P7. Splitting by lanes and waves
- Practice: waves with a "files it owns" column (disjoint), lanes capped by the machine (two heavy builds at once
  on a small host), a shared ordered queue from which a freed lane takes the next item, work priced in work hours
  then halved for two lanes plus a close every 8 h. The owner picked "parallel in waves, short tasks only".
- Verdict: QUEUED (`a-granted-parallelism-is-kept-filled`, `propose-the-split-before-being-asked`,
  `a-batch-states-why-it-is-split-and-which-model`, `one-device-plan-at-a-time-on-a-small-host`,
  `parallel-sessions-partition-by-write-surface`). Nothing new except the "files it owns" column and the shared
  ordered queue in the roadmap; add them as occurrences.

### P8. Execution record in the plan; roadmap state lines with dated owner statements
- Practice: a table (task, commit, note) appended as tasks land; "paused" state names where each agent's work
  sits, including uncommitted code saved in an ignored scratch folder; roadmap items read "Planned (owner, date),
  about N h" then "Amended (owner, date)" then "Built, device runs owed (date)", and a friction item states its
  incident count and fix price.
- Verdict: PRESENT/QUEUED. `a-plan-keeps-a-status-table`, `a-paused-plan-is-resumed-from-its-commit-subject`,
  `a-handoff-carries-what-no-artefact-holds` are queued; artifact 8 (friction items with a price) is PRESENT
  (`prompt-context.md:1653`); the pause rule is PRESENT (`skills/close/SKILL.md` section 0).

## 2. Implementation

### I1. Standing delegate rules file, handed with every brief
- Practice: one file of rules "read once, they bind you" (test-first with red output kept, no dispatching other
  agents, scratch outside the repository, the gate read by exit code, never stash, never kill by a pattern that
  matches your own shell, shell word-splitting traps, ask-list files edited with the edit tool); the brief only
  adds branch, scratch and what to report.
- Verdict: PRESENT (`prompt-context.md:2213`, `:1411`). One datum: the rule "never wait with a pattern that
  matches your own command line" was in that file and the wait loop that matched itself still happened twice
  afterwards (see Frictions F2).

### I2. An execution workspace outside the repository: one ledger, one file set per task
- Practice: a git-ignored folder per plan holds a ledger (one line per event: dispatch, rebase, review verdict,
  ruling with cost-if-wrong, deferred minors with their file) and, per task, brief, implementer report, review
  diff, review, fix diff, re-review, gate output. The ledger is the hand-off on a pause.
- Evidence: 3 plans; one workspace had 50 files for 6 tasks. A real value: when a session limit stopped lanes, the
  ledger let them resume with work intact.
- Verdict: PARTIAL. Ledger mentioned (`skills/README.md:57`); QUEUED `a-delegates-result-is-an-artefact`,
  `a-plan-may-be-a-working-artifact`. The per-task artefact set and the "deferred minors are ledger lines with a
  pointer" convention are ABSENT.
- Smallest change: a bullet in "Long runs and delegates" (`prompt-context.md:2189`): the per-task file set.

### I3. Landing discipline and the merge that commits before the gate
- Practice: one lane lands at a time by fast-forward after a rebase onto the integration head, with the gate run
  on the rebased head; integration branch separate from main; a device build made from a build-only branch rather
  than by merging two unreviewed lanes.
- Evidence of the gap: "a merge commit made before its gate ran" happened at least 4 times (a roadmap item
  proposed the fix of `merge --no-commit` and it still recurred twice afterwards).
- Verdict: PARTIAL. The rule is PRESENT (`prompt-context.md:1060`); the enforcement is ABSENT. This is the
  ladder's own lesson: a rule on rung 1 recurred four times.
- Smallest change: ship a `pre-merge-commit` hook stub beside the pre-commit stub in the bundle's hook guidance and
  name it in the "merge is chained to the gate" sentence.

### I4. Test-first evidence is classified, not just asserted
- Practice: every report and every review says, per test, which red it saw: a failing assertion; only a compile
  failure (weak); not possible (device-only, compiled); passed on arrival and named a "guard"; or a mutation
  check standing in. Reviews carry a column for it and mark such a task as spec-OK but evidence-weak.
- Evidence: at least 8 reviews/entries; tests that "passed on first run, so their red was not seen" are listed
  openly; three guards named as guards.
- Verdict: ABSENT. Principle 18 asks for red first; nothing classifies the red, and a compile failure counts
  as red in the wild.
- Smallest change: a bullet in `prompt-context.md` section 18 and in the delegate report line: "state per test which
  of five reds you saw; a compile failure alone is not a red; a test passing on arrival is a guard and is named".

### I5. Device work that cannot run is written, compiled, listed as owed, and run in one batch
- Verdict: PRESENT (`prompt-context.md:1062`). Evidence strengthens it: devices tests written without a device
  failed on their first run 20 times in one day (11 and 9 failures), for the same handful of reasons. The carrier's
  fix proposal (end the lane with a run, or name the classes owed in the report's first line) is PRESENT in
  substance. No change needed except citing the count as another occurrence.

### I6. A runner tool in front of a physical device that the human also uses
- Practice: a script that reads the device id at run time, refuses a locked screen, saves device settings that
  automation changes as a side effect, restores them on every exit and reads them back, installs in place only,
  runs one test class per invocation, treats zero tests as failure, refuses classes that change user settings or
  data unless agreed, and is itself tested against a scripted fake of the device tool. The human's use of the
  device wins: the agent does not touch the screen while they use it.
- Evidence: two incidents in four days of the automation changing a device setting the human had turned off, and a
  tap that landed in the human's own app; both led to the tool and a key rule.
- Verdict: PARTIAL. Zero tests is a failure is PRESENT (note `a-check-must-be-seen-to-fail`); cleanup by the
  supervisor, tools leave the tree as found, and an install is a migration on one device (note
  `no-simultaneous-deploy`, 2026-11-24 occurrence) are PRESENT/QUEUED. ABSENT: automation on a device the human is
  also using changes its settings and must restore and yield.
- Smallest change: a candidate row `automation-on-the-humans-own-device-restores-and-yields` (2 incidents, one
  owner, one carrier), and a line in the device paragraph of the guide.

### I7. Coordinator and lane roles
- Practice: a "coordinating session" (controller) assigns tasks to lanes, dispatches the isolated reviews,
  integrates onto an integration branch and keeps the build the human tests; a lane owns a branch, a worktree and
  a file set, and never merges another lane's dependency by itself (a duplicated merge across lanes produced the
  same conflicts solved twice); lanes report a base commit and a range.
- Evidence: 12+ lane entries; one friction.
- Verdict: ABSENT as vocabulary (controller appears only in the gate-serialising sentence at
  `prompt-context.md:2211`); the partitioning is QUEUED (`parallel-sessions-partition-by-write-surface`).
- Smallest change: a short subsection in "Long runs and delegates" naming the two roles and who merges.

### I8. Worktree and workspace hygiene
- Evidence: a worktree per lane under the repository's own tool folder; 38 live worktrees plus 2 prunable and
  three old workspaces at the end of the period; the log says "deleting the workspaces and old worktrees after
  asking" in "left undone" in at least 3 entries; one removal was denied by the permission layer; four incidents of
  a fresh worktree lacking an ignored environment file in one day; three of a gate failing on an ignored path.
- Verdict: PARTIAL. Worktree environment is PRESENT/QUEUED (`prompt-bootstrap.md:596`, `:653`,
  `a-worktree-check-needs-its-own-environment`, `read-the-state-before-deleting-a-branch`). ABSENT: a plan's close
  includes removing its merged worktrees and workspaces, with the human's yes, and the permission layer is told
  so in advance.
- Smallest change: one step in the close skill: "list merged worktrees and plan workspaces; offer to remove".

### I9. Model tiering of reviewers by blast radius
- Practice: the strongest model for correctness-critical tasks and whole-branch reviews, a mid model otherwise, a
  mid model for scoped re-reviews. Recorded in the ledger per review.
- Evidence: weak (no head-to-head); the whole-branch reviews on the top model both said "not ready" and found
  cross-task breakage the per-task reviews had not.
- Verdict: PARTIAL (`prompt-context.md:2239` table has stages, not review tiers; queued
  `a-batch-states-why-it-is-split-and-which-model`). Smallest change: one row in the table.

## 3. Review

### R1. The review report has a fixed shape
- Practice: Part 1 per item of the brief: spec compliance with a mark (ok / partial / fail) and the test-first
  evidence note; Part 2 quality by severity (Critical, Important, Minor; later HIGH, MEDIUM, LOW, NIT) with file
  and line; a header stating what it was given ("from the diff file; the suite was not re-run"); minor findings
  ledger-listed as deferred with a pointer.
- Verdict: PARTIAL. The reviewer agent and "say which context it was given" are PRESENT
  (`prompt-context.md:1071-1075`); no findings/severity vocabulary is fixed, and two vocabularies coexisted in
  the carrier. Smallest change: fix one severity scale and the two-part header in the reviewer agent's text.

### R2. The re-review cap against measured rounds (a CONFLICT, needs the owner's decision)
- Evidence: the first-plan final review; four lanes with 2 to 5 review rounds: one lane needed five rounds and still
  had a regression at the fifth; another had four reviews and findings of MEDIUM severity at rounds 2 and 3
  (a scheduled event firing twice; a refresh that froze every interaction; a corrected event firing again); the fixes of the
  last round were not reviewed again, three times. A fix to a review finding was itself wrong in two lanes.
- The bundle says "at most two re-reviews: what is still open goes to the user" (`prompt-bootstrap.md:631`).
  The measured pattern is that rounds 3 to 5 still found MEDIUM or worse in three lanes of four, so a flat cap of two
  would have shipped them. Queued: `a-re-review-cap-restarts-when-the-rule-moves`,
  `a-review-fix-is-a-new-change-and-gets-its-own-pass`, `clean-context-review-closes-a-batch`.
- Verdict: PARTIAL, contradicting. Smallest change: replace the flat cap by "continue while a round finds MEDIUM or
  worse, stop when a round finds only LOW or NIT, hard stop at five and ask; a fix of MEDIUM or worse gets its own
  scoped pass" in `prompt-bootstrap.md:631` and 21.4.

### R3. Whole-branch review after per-task reviews
- Verdict: PRESENT (`prompt-context.md:1071`), offered in the bootstrap (`:620`) but practiced by the carrier as part
  of the plan (the owner chose "per-task agents with review" at acceptance). Both its whole-branch reviews said
  "not ready" and found breakage across tasks. Supports the queued `clean-context-review-closes-a-batch`.

### R4. Plans and specs are not reviewed in a fresh context
- Evidence: the log records "the two plans had no isolated review; the owner answered their questions"; defects
  that the plan caused reached code: a new output without a shared case (twice, because the plan's test was
  language-only), a brief that named an item no longer at head (twice), "7 fix rounds in 11 tasks". One spec got a
  "builder check" and its two owner questions were answered.
- Verdict: ABSENT (the only review rules are for code, cards and a whole branch).
- Smallest change: a row in `skills/README.md`'s table: "a plan or spec is written -> a fresh-context read of the
  plan against the code at head: stale claims, missing cases, the review-focus lines, dependency rows".

### R5. Reviewer recomputes by hand; decide which side is wrong from a trace
- Verdict: QUEUED (`decide-which-side-is-wrong-from-a-trace`, `a-claim-built-by-hand-proves-only-what-follows-it`).
  Evidence: a number copied from a failing run is not a derivation (review caught it, 2 times).

### R6. Verification before claiming done
- Verdict: PRESENT: gate by exit code, never through a filter (`prompt-context.md:2216`); zero tests; counts read;
  "Not verified" field. Every log entry states "the gate ran by exit code before each commit".

## 4. Reporting

- R-1. Session log entry: PRESENT; the carrier copied the bundle's format and uses every field; its additions are
  a dated "Needs the owner:" line and a "Captured: N learnings, M frictions" count taken from the ledger.
- R-2. The opening brief of six one-liners with "nada" for an empty one: PRESENT (`prompt-bootstrap.md:438-500`).
- R-3. A lane report states first what is owed and unverified, then the range and gate: PRESENT in substance.
- R-4. Copy the agent wrote is marked PROPOSED/NEW until the human has seen it, kept out of the shipped strings
  or committed flagged, and listed for them on one page they mark. ABSENT. Evidence: 4 specs and 3 tasks carried
  "NEW" strings; a task stopped (needs-context) on two owner questions about wording instead of choosing.
  Smallest change: one bullet in `prompt-context.md` section 15 (or the `user-walk` skill): visible text the agent
  authored is PROPOSED until seen rendered; list it on one page; the builder may commit it flagged.
- R-5. Questions: recommendation first, each option by what the human would see, price in hours added to a base,
  "decide from mockups": PRESENT (section 15, `decision-review/SKILL.md:61`).
- R-6. Counting frictions by search: PRESENT (`bundle.py count`); the carrier records counts (wireless connection
  rediscovered 5 times, shell word splitting 3, etc.).
- R-7. Owner's one-day restrictions ("this time only, not a standing rule", "no device in this wave") are written
  with their date and scope in the plan and quoted in the log's Not-verified. Smallest: ABSENT as a stated rule;
  add a sentence to section 15 or the close skill.

## 5. Working with Artifacts (published pages)

No evidence at all in this carrier: no published page, no Artifact, no HTML. What it did instead:
- A single commit of throwaway mock screens for three visual directions, inside the app's debug-only source set
  with static data and the bundled font and its licence, so the human chooses "by looking" on their own device;
  then a restyle table "derived from the mocks the owner approved by sight". Priced 1 h in the queue; it cost
  one commit of over a thousand lines.
- Specs that ask the human to decide "from mockups", options shown by what they would see; copy reviewed in a
  text page the human marks up; screenshots captured on the emulator for the store listing.
Verdict: a mock for a "how it looks" question is PRESENT (`prompt-context.md:675`, `decision-review/SKILL.md:61`);
anything about published pages is ABSENT from both the carrier and the bundle. Nothing to absorb from this
carrier for theme 5. If the owner has seen Artifact use in design sessions, it did not happen in this repository.
The one transferable detail (a mock lives in the product's own runtime so density and fonts are real) is a single
occurrence: leave it as an observation.

## 6. Incremental decisions

- D1. One decision per turn in `decision-review`, recorded as rows with an id and a decider: `h1` is the owner,
  `agent s-...` a session; agent rows can start `unconfirmed:`; the summary the owner approves names the agent's own
  calls. 161 rows, 20 by an agent, 4 unconfirmed. PRESENT (principle 21.2 and the decisions tool).
- D2. Validation against constraints: each log entry has an "Architecture" field (complies / deviation) judged
  against a named invariant; the root file lists non-negotiable constraints, "do not propose alternatives unless
  asked", each with an enforcer; each row has an "Enforced in" column naming the test; a row can be amended in place
  ("Amended date: amended by row X"; 19 amendments) or superseded (4). PRESENT; the in-row amendment chain is a
  convention the decisions tool tolerates but the bundle text does not describe: PARTIAL (smallest change: one
  sentence in the decision-row artifact).
- D3. A batch of answers to a lettered question set is recorded as one row per answer with its id, and the open
  items are parked in the roadmap with a recommendation: PRESENT/QUEUED (`two-contradicting-answers-need-a-third-question`,
  `an-answer-to-a-misdescribed-option-is-superseded`).
- D4. A row records only the owner's words as its Why, an agent's reading is marked; a row whose rationale an agent
  invented was removed in review: QUEUED (`a-decision-row-never-speaks-for-the-owner`).
- D5. Rulings made during execution (29 in the first plan) wait in the plan until "the final review is where they
  are promoted or reversed". ABSENT as a step. Evidence: a log friction "superseded rulings". Smallest change: a step
  in the close skill: "rulings in a plan's ledger become decision rows or are reversed, before the plan's close".

## 7. Frictions the log records that the method caused or failed to prevent

1. A merge commit made before its gate ran: 4 or more occurrences after the rule was written. The rule was PRESENT
   but on rung 1 (see I3). Cost: low per occurrence, but it is the known failure.
2. A wait loop whose pattern matches its own command line: twice after the rule was in the delegate rules.
   Same lesson: a written rule was not enough; the cheap enforcement is a permission or hook refusing the pattern.
3. A fresh worktree lacking ignored files: 7 incidents over 3 sessions (an audit path 3 times, an SDK path 4 times)
   before the audit was changed. The bundle's isolated-copy text arrived after.
4. Reviews: the cap (R2), fixes not reviewed (3 times), a plan's own gap (R4).
5. Estimates in a unit nobody measures (P1).
6. Scripted document edits that slice between two markers and multiply on an empty slice: 2 occurrences, one grew a
   file to 600 thousand lines. Queued as a-scripted-edit-is-validated-by-the-set-it-selected. The rule that
   `git diff --stat` follows any scripted edit was in the log, not in a rung above prose.
7. A stand-in decision made by a builder in front of a contradiction (a visual choice that was the owner's): QUEUED
   (`a-contradiction-stops-the-constructor`); it recurred as a task stopping with "needs context" at the next
   chance, which worked.
8. Session limit ended a lane mid-task, 3 times; recovery depended on the workspace ledger and a clean tree (I2).
9. Device tests written without a device failing on first run (20 failures in a day): present in the bundle, but the
   carrier took a day and an item to arrive at "name the owed classes in the report's first line".
10. Leftovers: worktrees and workspaces never removed (I8).

## 8. Ranked top 10 to adopt

1. R2 (re-review rule by severity, hard stop five, fix gets its own pass). It changes a rule the data contradicts;
   the effect is shipping fewer MEDIUM defects. One paragraph.
2. I4 (classify the red). The cheapest honest signal on whether tests mean anything; 8+ occurrences; zero text today.
3. I3 (a hook for merge-before-gate). Four recurrences of a written rule; the clearest ladder evidence.
4. R4 (fresh-context review of a plan before it runs). Plan gaps reached code in several lanes; one row in a table.
5. P1 (unit of an estimate and its conversion). Real data: 20x to 40x gap between priced hours and wall time.
6. P3 (Review Focus in the plan, mapped to tests, source of the review brief). Cheap; 3 plans.
7. P2 (dependency table and stop rule). Prevents stand-ins and duplicated merges.
8. D5 (promote or reverse rulings at close). Stops a rulings graveyard in plans.
9. I7 (coordinator and lane roles, who merges). Gives the queued parallelism rows a shared vocabulary.
10. R-4 (PROPOSED marker on agent-authored visible copy, one review page). Recurring in 3 specs.
Close behind: P4 cost-if-wrong on rulings, I8 worktree removal step, I2 per-task file set, I6 device runner candidate.

## 9. What not to adopt (already there or too thin)

- Estimate beside actual in principle: present. Whole-branch review: present. Merge chained: present. Device
  batch: present. Log format, brief, decision rows, friction pricing: present.
- Model tiering for reviewers: thin evidence. Mock-in-product-runtime: one occurrence.
- Theme 5: nothing in this carrier.
