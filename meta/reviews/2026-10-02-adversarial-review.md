# Adversarial review: initialisation, the method, and how the bundle is organised

Date: 2026-10-02. Bundle version under review: 0.0.25, plus an unmerged branch of prompt changes.

**Summary.** About a dozen repositories that carry, or once carried, the bundle were read to learn how
each was initialised, whether the method survives a hostile reading, and how the release should be
reorganised. The maintainer's thesis, *research the context, but ask the objectives of the
initialisation*, holds with refinements: ask an empty repository first; read an existing one for at
most about five minutes, then propose an objective to confirm; ask what the initialisation must deliver,
how deep, and which questions the research must answer; write findings as they land. The method has
four critical defects, the first being a pre-flight that asks about the environment, never the purpose.
The largest avoidable cost was the maintainer's standing rules not travelling between repositories
(history rewrites in several, attribution trailers left in some), now addressed outside the bundle by a
user-level profile. The redesign ships the method as skills (a base plus a carrier-owned `LOCAL.md`)
with a generated router, bookkeeping commands and an interview-first bootstrap. Section 4 reviews the
process that produced this review, including a privacy slip it made.

## Method

**What was read, by kind.** Three read-only investigations, each written up before this synthesis:

- *Initialisations:* every repository on one machine that carries the bundle or an older copy of it,
  about a dozen, of the kinds in table 1.1. Sources: carrier records, changelogs, decisions, roadmaps,
  git history, and transcripts parsed for typed turns, mid-turn messages and question answers.
- *The method:* the released bundle, the home's roadmap, ledger and evals, the unmerged prompt branch,
  and one carrier's first harvest as field evidence; measured with `bundle.py report` and `privacy`.
- *The organisation:* the same, plus a census of every repository's skills and hooks, the user-level
  and per-project assistant memories, and a third-party skill plugin the carriers run their coding
  sessions on (read as installed; none of its text is reproduced).

The maintainer's conclusions on all three were then given to this review and are recorded as such.

**Limits.** One initialisation transcript is missing (it ran on another machine; its records stand
in); one initialisation was in progress; only one machine was read. Field evidence comes mostly from
one carrier; patterns inferred from skill sets alone are ASSUMPTION. Transcript counts are scripted,
approximate, and rounded also for privacy. Costs are the bundle's estimates (characters / 4); benefits
are mostly unmeasured. The model family that did the reading wrote much of what it reviews, and no
independent reader checked it.

---

## 1. Initialisation

### 1.1 What happened, across the initialisations

Rows in rough chronological order. *Asked* means the agent asked what the repository or this
initialisation was for before acting on a guess.

| Kind | Method in use | Objective asked? | Research done | Early corrections from the maintainer | Rework later traced to the init |
|---|---|---|---|---|---|
| Origin of the method (interactive app) | none yet; maintainer-driven | no; supplied turn by turn | web guidance on the platform and genre | document roles dictated | root file over budget; migrated twice to the new layout |
| New application | first portable prompt, no pre-flight | no | the code the same session had written | about five in the first hour: scope, a size budget, battery, tooling | a budget invalidated; optimisation phases added; document language flipped two days later; no carrier record |
| Library | same | no; the maintainer asked for the open questions in their own language | code and history | an objectives brief, after the evaluation report | — |
| Presentation (not code) | their own structured brief, then the pre-flight | stated by them; the pre-flight was code-centric | the venue's practice; brief versus machine | not code; documents in their language; content checked by human review, not a gate | a foreign adoption date copied in |
| The home (meta) | — | stated by them | literature on documentation | privacy and anonymisation, a day later | random carrier ids, the privacy tool, a history rewrite in a public sibling |
| Empty, research-first | the pre-flight, adapted | **yes, first, no default** | three parallel lines a minute after the answer | a plan as well as research; how others built it | a reduced init declined skills, hooks and audit until a go/no-go that was bypassed by amendment; the decline list went stale as code grew past a hundred files |
| Empty, product | a plugin's brainstorming skill instead of the pre-flight | product objective yes; *what does initialising include*, in round two | four parallel subagents: landscape, reuse and licences, platform versions, mechanics | product model, reuse scope, licensing parked, authorship, merge without review, sibling tooling | over a dozen commits rewritten for authorship; dozens of rules recorded nowhere for days; never registered with the home |
| Non-code inventory | the bundle | stated by them; a scope option offered | a read-only scan of the machine | privacy first, within the hour; classification; misattributions | a history rewrite prepared, then judged unnecessary; scope widened two days later |
| Dormant codebase | export from the home, then the pre-flight | **no**; they ignored the environment questions | all code; framework claims verified; sibling conventions | the real problem and the domain research came after approval | a second plan document; a merge against the recommendation |
| The template | — | yes: what it carries, how it stays current | the home's release | — | its README asks the human to volunteer the objective |
| Empty port of an existing website | the template | **yes, improvised**: what is the project; is the source yours | the live site, read-only | paused early | two commits with assistant attribution trailers |
| Dormant codebase (in progress) | the template and the pre-flight | no | all code and history, then seven research lines | rejected the proposed document language; doubled the research scope | — |

Time to a first artefact and to a committed init, rounded: research-first, 15 and 30 minutes; empty
product, 15 minutes, then two hours to a green gate; dormant code, 30 and 90 minutes; others, hours.

**Recurring patterns.**

1. The pre-flight asks about the environment, never the purpose. Where purpose was decisive it was
   asked by improvisation (three cases) or arrived as a correction (five).
2. Guessing the objective from names and files failed twice: a repository's name suggested the wrong
   domain; code was read as the product when the motive was a missing platform feature.
3. Research *direction* was assumed, and redirected or widened by the maintainer in six of the eight
   inits with transcripts. Depth was never the problem.
4. Standing working rules (authorship, merge policy, language split, what *pause* means, the close)
   did not travel. Inits read siblings for format, not for the maintainer.
5. The repository was assumed to be code, and the threat model (privacy, visibility) was assumed;
   both arrived as corrections, twice each.
6. The document-language default (the request's language) was wrong in two of three visible cases;
   the answer depends on who reads the repository.
7. The initialisation does not end (one ran for days through many compactions), and a reduced one has
   no enforced upgrade.
8. Bundle hygiene defects (a copied record, an unreadable roadmap id form, home registration) recurred
   until export and the template; *write nothing before Phase 3* made two inits record a deviation.

### 1.2 The thesis, tested

**For.** Every init that did not ask the objective received it later as a correction, often after work
had been done against a guess. The one init that asked first, with no default, was the fastest and
best matched, and the agent's own guess there was wrong. Research direction depends on the objective.
The maintainer's own early definition of initialisation is research-heavy (research domain, language
and practice; record it; evaluate the state), and they repeatedly asked for more research.

**Against, or qualifying.** They also want the agent to work out what history and files can tell; a
bare *what are your objectives?* in a repository with a README, roadmap and history would be lazy. The
objective is often in the first message, so re-asking wastes a turn. Generic questions are skipped
(twice); concrete ones with a proposed answer work. Several decisive corrections were standing rules,
which asking objectives would not have caught and reading a profile would.

**Verdict.** The thesis holds, refined: (a) empty repository, ask first; existing repository, read for
at most about five minutes (README, roadmap, recent commits, siblings the request names), then propose
an objective to confirm; (b) ask what *this initialisation* must deliver and how deep; (c) ask which
questions the research must answer before launching it; (d) write findings as they land.

### 1.3 The recommended initialisation procedure

**Ordered steps.**

1. Export the release (never copy); check `carrier.toml` is this repository's; resolve the interpreter.
2. Read the maintainer's profile (3.7), so its rules are neither asked nor broken.
3. Short read, about five minutes at most, of what exists and what the request names; skip if empty.
4. The objectives interview (below), one message, in the maintainer's language.
5. Launch the research lines in parallel on the answers; write each record to the repository as it
   lands, dated, sourced, with ASSUMPTION marks. Records are not instructions and need no approval.
6. The state report, open questions at the top, in the maintainer's language.
7. The topology proposal, sized to the depth profile; wait for approval.
8. Generate, gate, and register the carrier with the home in the same step.
9. The first real task (acceptance), then an explicit close: a changelog entry ends the init, and the
   next session starts from the roadmap.

**The objectives interview.** At most five questions, each with a default from the request and the
short read; those the request or the profile already answer are skipped, said in one line.

1. *Purpose:* what the repository is for and what it should let you do that you cannot today. No
   default when empty; otherwise "I read X and think it is Y; confirm or correct".
2. *This initialisation's deliverable and depth:* research to a go/no-go; revive and fix; scaffold to a
   first slice; adopt conventions; document something that is not code. Anything declined gets a
   revisit trigger.
3. *What the research must answer:* two to four proposed lines (domain references, similar products and
   why they fall short, reuse and licences, how others built it, platform traps, underlying theory).
4. *Audience, visibility and language:* public or private; who reads the documents (this sets their
   language, not the request's language); terms that must never be written.
5. *Where it runs unobserved, and what is off limits* (today's questions, merged).

**Depth by repository kind** (set by answer 2, said aloud, overridable; when in doubt, the heavier):

| Kind | Read | Research | Produce first | Defer, with a mechanical trigger |
|---|---|---|---|---|
| Empty, research or feasibility | the request | parallel lines on the decision question | research records, a go/no-go item, a short root file | skills, audit, hooks, until the go/no-go closes *or* the first non-probe source file lands |
| Empty, product | siblings named | landscape, reuse and licences, platform versions | objective and spec, decisions, then scaffold and gate | — |
| Dormant code | all code if small; history; why it stopped | the original idea's domain and similar tools, then the stack | evaluation with defects, objective statement, gate | refactors, until the objective is confirmed |
| Active code with conventions | the full state evaluation; adopt mode | framework traps | guarantees, an existing-file table | anything not approved |
| Not code (presentation, inventory, notes) | the material itself | the genre's practice | what *verified* means here; the privacy gate | code-centric artefacts |
| Meta (home, template) | the bundle and its carriers | literature on the method | purpose and distribution rules | — |

**Acceptance by a first real task.** The init is done when one real roadmap item has gone through the
new system (brief, plan, build, verify, close) and its changelog entry records what the system failed
to supply: a missing command, a guessed rule, a skill that did not fire. Each gap is fixed or recorded
as debt first.

**The initialisation record.** Five lines atop the root file and the roadmap's *Where we are*: the
repository's purpose, this init's purpose, its depth, what was deferred with its trigger, the next step.

**Verification checks.**

- Read-back: a fresh agent given only the root file states the purpose, the depth and the next step.
- The profile's rules appear in the repository and the first commits obey them (a check fails on an
  attribution trailer when the profile forbids one).
- `bundle.py ids` counts every roadmap heading; the carrier is registered with the home.
- Every `declined` entry has a roadmap item with a mechanical trigger; the audit fails when the trigger
  holds while the item is open.
- Metric: corrections in the first three sessions about purpose, scope, research or standing rules,
  from transcripts; target none about standing rules, at most one about purpose.

---

## 2. The method, adversarially

Twenty-two findings, ranked. Evidence is generalised; *one carrier* is the one read most closely.

### Critical

**F1. The initialisation never asks the objectives, has no greenfield mode, and its pre-flight
contradicts itself.**
- *Evidence.* The bootstrap says to ask before reading anything, and to ask fewer when the repository
  answers one, which needs reading; the shared rule says both *nothing happens until answered* and
  *detect first, then ask*. No question concerns goals or ways of working, though the method's own test
  for a question (unreadable, a wrong answer wastes the run, only the human knows) admits exactly
  those. An empty repository is routed to all nine phases. *Write nothing before Phase 3* forbids
  persisting research.
- *Failure.* Obedience builds for goals never heard; improvisation yields ad-hoc rounds and deviations.
- *Fix.* Section 1.3: bounded recon, the interview, then research; a greenfield mode with product
  research; research records exempt from the gate; answers in the root file so nothing is re-asked.

**F2. The method preaches the enforcement ladder and leaves its own session loop on rung 1.**
- *Evidence.* The brief, card lookup, card checks, capture line, friction counting and *Done*
  checklist are prose; a carrier's gate enforces only file integrity. In one carrier: card citations
  in every entry on day one, about one in seven after, none in the phase that most needed them; the
  capture line dropped; frictions counted from memory; repeated procedures never promoted; two
  commits on a red gate. Nothing checks the root file's method lines or the installed reviewer.
- *Failure.* Week one looks compliant; by week two the judgement steps stop, nothing turns red, and
  the harvest reads a changelog that no longer records what it needs.
- *Fix.* A wiring check; a changelog-field linter; a *touched trigger paths, cited no card* report;
  optional brief and close hooks; an event-driven state review.

**F3. Repository precedence does not cover host plugins, assistant memory or harness defaults.**
- *Evidence.* In one carrier a third-party plugin drove design, planning and execution; its plan
  template had no card slot, so the card step vanished, and two *first thing* rules competed. *Review
  on request only* rests on eight pilot trials, while that plugin's whole-branch review found a defect
  in each of about a dozen runs, some critical-class; the home's ledger still refuses review by default
  as *already in the method*, untrue for a release now. The harness's default attribution won wherever
  no repository rule existed; local memory held rules the repository did not.
- *Failure.* Method steps lose their slot without a trace; a thinly measured rule argues against a
  review that catches critical defects; a hand-off loses what lived in memory.
- *Fix.* Host tools become part of the host in the precedence principle, detected at recon; a
  step-to-host-slot table, checked by the wiring check; the review rule restated with its measured
  boundary and the refusal reopened; an attribution line shipped by default.

**F4. Cost is measured, benefit is not; the method itself was never evaluated, and the programme is
paused.**
- *Evidence.* Study 1: cost about ×2 to ×2.8 per task; benefit on three discriminating tasks of
  sixteen, smallest attainable p-value 0.25; tasks written by people who had read the notes; one model
  family; no plugins; single sessions. Never measured: the pre-flight, brief, loop, close, harvest,
  update, adoption, multi-session work, host plugins. Study 2 has no data; efficacy work is paused.
- *Failure.* Carriers pay double for a benefit shown on three synthetic tasks; a worse release goes
  undetected.
- *Fix.* The planned transcript profile of real sessions (aggregates only); per-carrier adherence and
  correction counts; a field metric per release; the method labelled unvalidated until then.

### Important

**F5. Learning-to-availability latency is long and gated on one person and one machine.** Carriers are
reached only when open on the home's machine; one sits several releases behind; signed tags wait for a
second publisher; admitted items wait for a release; about two dozen versions in a week, mostly moving
the carrying machinery. *Fix:* freeze the carrier layout and adopt a cadence; a fast lane for method
defects with a reproduction; carriers fetch a tagged release themselves; a procedure another person
can run.

**F6. Ceremony is high and keeps growing.** One carrier in four days: about a hundred lines per
changelog entry, dozens of decision rows (some naming *code review* as enforcer, a smell by the
method's own list), a root file at its ceiling, about fifty proposals in one harvest; a twenty-box
checklist; a literature check per proposal; an update that nests a harvest. The unmerged branch adds
three fields, two boxes and a hazard. *Fix:* price ceremony like any friction; cap entry length;
machine-fill fields; shrink the checklist to the steps evidence shows are skipped, each tool-checked;
move the literature check to the home.

**F7. The admission bar is inconsistent and the queue's generated view contradicts itself.** Written
bar: one occurrence; practised bar: a second repository; method changes have no written bar. The queue
only grows. Two candidates appear as both *waiting* and *answered*, because an *offered again* history
row is read as an answer. A stale refusal blocks re-offering. *Fix:* one bar per kind (knowledge: one
measured occurrence plus literature, scoped; a second repository raises it to cross-domain; method
defects: a reproduction); a test that no slug sits in two sections; refusals with an expiry condition.

**F8. The index lookup is usable but expensive and domain-skewed.** Pilots spent most of the bundle's
extra input reading the whole index to reach one or two cards; `lookup` is planned, not built; rows
skew to backend and data work; few notes declare when they apply. Client and device projects read it
for nothing or over-apply a near-miss card, the one harm the pilots saw. *Fix:* build `lookup`;
`applies_if` on every note; per-carrier hit rates; prune notes no carrier opens.

**F9. The privacy checker cannot see what principle 20 names as the threat.** The principle says the
leak is a combination and forbids a carrier id beside a description; the checker matches a noun list
line by line. One carrier's proposals carried the carrier field in their header and a domain kind in
their body; the home's roadmap and a drafted changelog wrote a carrier id beside a description of
findings; all passed. Dozens of permanent quote warnings drown the channel; carriers get no hook.
*Fix:* fail on any carrier id outside the carriers file; strip the carrier field when proposals are
packed; permanent warnings become failures with an allowlist; ship the pre-commit hook to carriers.

**F10. The *hearing the request* fixes will not reach coding sessions.** The unmerged branch writes the
most frequent corrections (a skipped part of the request, a light remark read as a purge order,
*pause* read as *close*, the middle ground, free text over options) into a principle the working
invocation does not load; the coding budget sits at about 99 % there, anchored to a past size, not to
value. *Fix:* the five behaviours as a list in the loaded step and the root-file template, paid for by
dropping the engineering standards from the coding reading list; budgets from measured session cost.

**F11. The harvest contradicts itself on who applies the generality test, and missed the human's
input.** One passage has the carrier apply it strictly, another says only a release can, the
small-model guidance says not at all. The harvest read records, while most corrections lived in
mid-turn messages, question answers and memory. *Fix:* carriers apply the noun test only; the release
applies the cross-carrier test; transcript reading becomes a privacy-filtering tool.

**F12. Absolute rules hurt their owner.** *Never fold another session's change into yours* kept their
own change out of a commit; *write nothing before approval* blocks research records; *offer each
commit* fights owners who batch. *Fix:* each absolute gets its owner exception, once.

### Minor

- **F13.** `CONTRIBUTING.md` names a carrier-owned folder removed a release ago.
- **F14.** The home's records give three different carrier counts; generate it.
- **F15.** A *six-line* brief is shown as an eight-row block; show the add-on separately.
- **F16.** Which root file is the source (`CLAUDE.md` or `AGENTS.md`) is taught both ways; decide.
- **F17.** The model-tier table gives verify-and-look, the steps most skipped, to a small model; add
  "with a tool that proves the step ran".
- **F18.** The update's reading list loads unused subsections; minting is stated twice.
- **F19.** Emptying `incoming/` by keeping its README deleted nothing (every file there is a README);
  a command, `bundle.py incoming --clear`, instead of wording.
- **F20.** Numbers in shipped examples travel as facts; placeholders where an example names hardware.
- **F21.** The assistants question defaults to several assistants from one source; default to what
  recon detects.
- **F22.** Residue: the home's pre-commit hook skips the build check; a stale release folder was
  committed; `verify` skips the duplicate-carrier check; the roadmap template's id form is not what the
  checker reads.

### What to keep

- The enforcement ladder and *a check must be seen to fail*: planted failures caught real gaps on a
  carrier's first day.
- Integrity tooling that refuses: `verify` caught files a subagent wrote into the release; the carrier
  check caught a copied record; proposals are immutable and sealed.
- Cards as claim, *Not when*, check; the repository wins over a note; the trigger gate kept trivial
  tasks at no extra cost in the pilots.
- Honesty mechanics (ASSUMPTION, *what went wrong*, *not verified*, no-change proofs); questions
  together with a recommendation first (taken in about two thirds of a hundred answers in one carrier);
  working safely in a dirty tree; the evals' pre-registration; privacy as a tool-checked rule.

---

## 3. Organisation redesign

The spine stays: releases, checksums, carrier records, proposals, privacy, the knowledge funnel. What
changes is delivery. In the carrier read most closely the working invocation was never pasted; the loop
lived transcribed into the root file and the repository's own skills. Across the machine `state-review`
was written six times, `verify` six and `commit` three, each drifting. The method's prose is about 54 k
tokens; the coding session's load is at about 96 % of its budget (about 99 % on the unmerged branch).

### 3.1 The method as skills, installed as base plus `LOCAL.md`

- *What.* About a dozen skills generated by the home. Core: `session-brief`, `consult-knowledge`,
  `verify`, `commit`, `close`, `state-review`. Method jobs: `harvest`, `update-guides`,
  `evaluate-instructions`, `bootstrap`. By kind, on request: `research-log`, `copy-review`,
  `device-run`, `fresh-review`, `write-skill`. Shipped under `.agents/method/skills/<name>/`, **never
  `.agents/skills/`**, which another assistant auto-loads, bypassing the override. `bundle.py
  install-skills` writes `.claude/skills/<name>/SKILL.md` as the base merged with the carrier's
  `LOCAL.md`, whose `##` sections replace the same heading or append; local trigger phrases live
  there. `carrier.toml` lists installed skills; an uninstalled core skill is a `declined` line. The
  prompt library becomes the skills' `references/`, split by its headings, numbers unchanged.
- *Problem.* The invocation is not pasted; carriers rebuild the same skills; the loop's prose cannot
  grow; the procedures asked for most (*close*, *continue*) exist only as prose.
- *Cost, risks, measure.* Twelve skill files of 300 to 500 words; `install-skills` about 250 lines
  with tests; about an hour of migration per carrier (each old rule sorted into base, local or a
  `skill` proposal, with a preservation check); about +700 to +1,000 always-loaded tokens over today's
  practice, recovered only if the root file shrinks. Collisions with the plugin's skills; skills that
  do not fire or over-fire; an override shadowing later base fixes (reported). Measured by held-out
  trigger rate (fire at least 0.8, misfire at most 0.1), field adherence, duplicates at zero.

### 3.2 The router

- *What.* A generated block of about 25 lines between markers in the root file: one row per situation
  (first request, about to build, a change touching state or contracts, about to claim done, a piece
  passes the gate, close but not pause, back after a while, a pending release, a harvest, a procedure
  done by hand twice, kind-specific rows), the precedence line and the privacy line. Rows for skills
  not installed are not generated.
- *Problem.* Hand-written root-file lines drift; nothing always-loaded says when the brief, close or
  harvest happen, so the maintainer names them.
- *Cost, risks, measure.* About 400 always-loaded tokens, minus what it replaces; about 60 lines of
  tool code with a planted stale-block test. A generated block inside an owned file (markers, banner,
  an edit check); growth into another index (cap of 14 rows). Measured by root-file lines before and
  after, and the brief and close firing on their situations.

### 3.3 Bookkeeping as `bundle.py` commands

- *What.* `new entry|decision|item|research` writes a template skeleton with a minted id; `count
  "<symptom>"` counts a friction by search; `memory-diff` asks where each local memory belongs;
  `brief` prints facts (branch, dirty files and their authors, last entries' *Left undone*, pending
  release and proposals); `check-trailers` counts attribution trailers; `incoming --clear`.
- *Problem.* Changelog fields invented and dropped; wrong counts from memory; memory taken as a
  hand-off; the ladder's *a rule broken while loaded becomes a tool-written template*, unapplied.
- *Cost, risks, measure.* A few hundred lines plus templates. Templates that grow without a price (F6);
  commands that print opinions instead of facts. Measured by entries carrying every field over ten
  sessions, and friction counts equal to a search.

### 3.4 The bootstrap redesign

- *What.* The `bootstrap` skill in five stages: the interview (1.3), skipping what the profile answers;
  the kind, said aloud, scaling artefacts and skills; research scoped by the answers, siblings read when
  named, delegated agents given scratch space outside the repository; artefacts, every *must never
  happen* answer placed on the ladder (permission, hook, check, or prose with its reason); acceptance by
  one real task.
- *Problem.* Preferences learned late, per repository; full product-app artefact sets offered to a
  slide deck; success measured by files written, not by the first session working.
- *Cost, risks, measure.* One round of maintainer minutes; a kind table of about 40 lines. A
  questionnaire nobody answers (capped, defaults accepted); misclassification (overridable, ratchet
  upwards). Measured by *you should have known* corrections in the first sessions, artefacts unused
  within a month, and the acceptance task's gap count.

### 3.5 Cards actually consulted

- *What.* `bundle.py lookup <words>` returns one to three cards in a few hundred characters; a plan
  carries a `Cards:` header line (or *none apply, because…*), added through the winning template's
  local override, never by editing a plugin; `verify` runs the named cards' checks; the close reports
  *touched declared trigger paths, cited no card* as a finding, not a failure. No skill per note.
- *Problem.* Citation decayed to near zero; the host's plan template had no slot; the index is read
  whole to reach one card.
- *Cost, risks, measure.* `lookup` about 80 lines, generated from the notes; `cards-check` about 60. A
  ritual *none apply*; trigger paths as a proxy. Measured by the citation rate on trigger-touching
  entries (target at least 0.8) and the bundle's share of input in consulting sessions.

### 3.6 Checks as code, and optional hooks

- *What.* `bundle.py audit`, an opt-in library enabled in `carrier.toml [checks]`; each check reports
  how many subjects it examined, fails on zero, ships with a planted failure, and `--self-test` plants
  violations in a temporary copy: `doc-paths`, `index-complete`, `enforcers-resolve`, `root-budget`,
  `skills-current`, `entry-fields`, `forbidden-phrases`, `forbidden-dependencies`, `record-ids`,
  `every-check-planted`. Domain checks stay the carrier's. Optional hooks via `install-hooks`, merged
  and recorded: `privacy-gate`, `no-attribution` (also a git hook), `brief-facts`, `generated-guard`,
  `close-reminder`. Only deterministic checks block; the brief and close only print.
- *Problem.* Each carrier wrote its own path checks; a research index listed a third of its files;
  decision rows named enforcers that did not exist; a check that skipped missing files could never
  fail; the brief and close are the steps agents skip.
- *Cost, risks, measure.* About 500 lines for the library, 200 for hooks. A wrong library check is
  wrong everywhere (the self-test runs in each carrier); hooks are friction (never installed where
  declined); generalising a check can leak nouns (parameterised, `privacy` run on the tool). Measured by
  first-run violation counts per carrier and attribution trailers in new history.

### 3.7 The personal profile, kept out of the bundle

- *What.* Three layers: repository rules (travel with the repository); the personal profile (true of
  this person everywhere: authorship, approvals, question style, close and pause semantics, languages,
  research habits, merge style), whose source lives in a private place outside the home and is rendered
  into the user-level instruction file on each machine; and local memory, drained at close, never a
  hand-off. A repository's own rule wins over the profile, and the rendered block says so first.
- *Problem.* The sole-authorship rule lived in five project memories; no user-level instruction file
  existed; about nine harvest proposals were preferences waiting forever for a second repository.
- *Cost, risks, measure.* A small command set (`profile add|render|check|import-memory`); a block
  capped at about 60 lines. Privacy (never in `.agents/`, a proposal, a carrier or the home; the tool
  refuses to write it inside a repository); over-generalising a domain preference (scope by kind);
  staleness (dated entries). Measured by duplicate memories at zero and *I already said* corrections.

### 3.8 The faster home loop

- *What.* Intake without a release; data-only releases a carrier takes on a checksum proof that no
  method file changed; an active second-occurrence search (one read-only agent per carrier per batch,
  output generalised before writing); preferences routed to the profile first; a `skill` proposal kind
  merged across carriers into the base. No provisional card state.
- *Problem.* About three quarters of one carrier's proposals lack only a second occurrence; the method
  changes most needed wait on a release that does not fit its budget; no proposal kind carries a skill.
- *Cost, risks, measure.* Flags on existing commands, about 80 lines for data-only updates, agent runs
  per intake. More home sessions (short, tool-driven); reading private carriers (generalised first); a
  merged base losing sharper wording (preservation check). Measured by median proposal age to a verdict.

### 3.9 Skill evals

- *What.* Per shipped skill: twenty trigger queries (half near-misses, including the plugin's
  neighbouring skills and casual phrasings that mean something else), in English and each carrier
  language that uses it, three runs each, held-out split; two or three pressure scenarios on a fixture,
  run without and with the skill; a field query over transcripts, aggregates only. A skill whose
  scenarios do not fail without it does not ship.
- *Cost, risks, measure.* About sixty short runs per skill per iteration; ASSUMPTION: minutes and a
  small share of a day's usage limits. Overfitting (held-out), small samples (counts, not only
  percentages), model drift (record and re-run). Measured by the eval, and whether field adherence
  tracks it.

### 3.10 Design answers, settled

1. **Skill names:** plain (`close`, `verify`, `commit`, `state-review`); carriers' existing skills are
   migrated in place to base plus `LOCAL.md`.
2. **Router delivery:** a generated block in the root file; a session-start hook may print facts only.
3. **The profile's source:** a private place outside the home, rendered on each machine.
4. **Skill evals:** allowed as a capped exception while the efficacy studies are paused.
5. **The third-party skill plugin:** named only as *if installed* seams, its version recorded in
   `carrier.toml`; every skill works without it; its text is never copied.

### 3.11 Phased migration, smallest valuable step first

| Phase | Ships | Exit criterion (measured) |
|---|---|---|
| 0 (no release) | The personal profile, drafted from the harvest's owner pass and the duplicated memories, reviewed, rendered at user level; superseded memories deleted | duplicate preference memories at zero; no reminder of a profiled rule in the next five sessions |
| 1 | `install-skills` (merge, banner, `--check` in `verify`); `new entry`, `count`, `memory-diff`; the changelog template; the `close` skill with its eval | next entries in two carriers carry every field; friction counts equal a search; `close` fires on every close request |
| 2 | `verify`, `commit`, `state-review` bases; the `skill` proposal kind; audit library v1 (`doc-paths`, `index-complete`, `enforcers-resolve`, `root-budget`, `skills-current`, `entry-fields`, `every-check-planted`) with `--self-test` | duplicate skills at zero everywhere; each enabled check seen red on its plant in each carrier |
| 3 | the router; `session-brief` with `brief`; `consult-knowledge` with `lookup`; the `Cards:` line; `cards-check`; per-skill budgets set by a pilot (released wiring against router plus lookup) | cost at most ×1.5 of the minimal arm on non-trivial tasks with every discriminating task passing; card citation at least 0.8 over ten sessions |
| 4 | the method jobs as skills (`harvest` with a transcript pass, `update-guides`, `evaluate-instructions`); the reference split (a move commit, then an edit commit) | every reading list resolves; a harvest and an update run from the skills alone end green with no step invented |
| 5 | the `bootstrap` interview, kind table and acceptance task; optional skills by kind; the hooks pack | one new repository bootstrapped end to end, gap list empty or recorded; no attribution trailers in new history |
| In parallel, from phase 2 | intake-only sessions, data-only releases, second-occurrence search; skill evals as a release gate from phase 3 | median proposal age to a verdict halves |

Rollback: each phase is a release; a declined skill's `LOCAL.md` keeps working as a carrier skill.

### 3.12 Do not do

- Make skill use mandatory by fiat (default consultation cost over double in the pilots), or copy,
  vendor or paraphrase a third-party plugin's skills.
- Ship skills under `.agents/skills/`, or add carrier-owned files inside `.agents/` beyond
  `carrier.toml`, `proposals/` and `incoming/`.
- Let a carrier edit an installed `SKILL.md` or the router block; the override is `LOCAL.md`.
- Generate a skill per note or topic; drop `knowledge/INDEX.md` (stop reading it whole instead).
- Move and rewrite the prompts in one commit, or renumber anything while splitting.
- Put the profile, or anything describing the maintainer, in `.agents/`, a proposal, a carrier or the
  home.
- Let a hook decide anything that needs judgement, install a hook a carrier declined, or run the
  harvest, update or a release from a hook or schedule.
- Translate the shipped skills, let the router grow into an index, or ship a provisional card state
  or a skill whose scenarios do not fail without it.

---

## 4. The process that produced this review, adversarially

**The harvest's blind spot.** A carrier's first harvest wrote about fifty proposals and missed the
pre-flight gap entirely, as did the home's prompt branch built from it. The gap is invisible from one
repository; it appears only when a dozen initialisations sit side by side. A harvest is a
per-repository instrument and cannot see cross-repository patterns by construction. *Fix:* the
second-occurrence search (3.8) doubles as a cross-repository pass, and a periodic review of
initialisations across carriers becomes a home job.

**The false recorded lesson.** A carrier's changelog recorded that one of its tools hid failures. It
did not; this was caught only because the code was read before it was changed. Had the harvest
promoted it, a false lesson would have travelled with a record's authority, and much of this review
also rests on records. *Fix:* a recorded lesson is a claim to verify against code before it is
proposed.

**Ceremony added without a price.** The harvest's proposals and the branch built from them add
changelog fields, checklist boxes and a hazard, none with a cost estimate; the method's friction
principle, applied to itself, would have priced them (F6). This review proposes commands, hooks,
skills and evals; each carries a cost line, and the phases measure the cheapest step before the next.

**Skills duplicated per repository instead of shared.** Six repositories solved the delivery problem
independently by writing the same skills. Each harvest saw a local improvement, not a shared need, and
the home had no proposal kind to receive a skill, so the method's main structural problem sat in plain
sight. *Fix:* the `skill` proposal kind and the base-plus-`LOCAL.md` install.

**Preferences offered as knowledge.** About nine proposals were the maintainer's working preferences
phrased as general method. As knowledge they wait for a second repository; as preferences they were
already true in every repository they open. Routing them to the profile answers them at once and keeps
the knowledge base about building software.

**The standing rules that did not travel.** The largest avoidable cost was the maintainer's
cross-repository rules, above all sole authorship: history rewrites in several repositories, and
attribution trailers still in some, including one started from the template after the rule was
written down elsewhere. The fix landed outside the bundle, as the user-level profile; the bundle could
not carry it without describing a person, which is why 3.7 keeps them apart.

**A privacy slip in this same work.** Text written into a public repository placed a description of
findings next to a carrier's identifier. The adversarial method review caught it; the privacy check did
not, because it matches nouns line by line and cannot see combinations. History was rewritten. It is
principle 20's own threat, missed by its own tool, by an agent that had the rule loaded. *Fix:* F9 (fail
on any carrier id outside the carriers file) and a check of combinations, not nouns; meanwhile no
identifier appears in a file that leaves its repository, which this document follows.

---

## 5. Open questions, and what remains unmeasured

**Unmeasured.**

- Whether any session step of the method (pre-flight, brief, loop, close, harvest, update) improves
  outcomes; only knowledge-note transfer was measured, on synthetic single-session tasks.
- Whether the objectives interview reduces corrections; the metric's baseline is one carrier.
- Whether skills fire in the field, and whether router plus skills costs less than it saves (the
  pilot is designed, not run); the profile's effect on corrections.
- ASSUMPTION, not verified here: that the user-level instruction file is always loaded on the installed
  assistant; that a plugin's installed version and seam names can be read reliably (it has moved
  between generations); that project-scoped plugin enablement and pinning exist, which would reopen
  packaging the bundle as a plugin; the cost of skill evals.

**Open questions.**

1. How a reduced initialisation is upgraded when its trigger is bypassed by amendment rather than
   closed; the proposed audit check covers file-count triggers only.
2. Whether carrier ids should appear in any committed home record beyond the carriers file, given that
   the check cannot see combinations.
3. Who besides the maintainer can cut a release, and whether carriers should fetch tagged releases.
4. Whether a lasting seam dependency on a fast-moving third-party plugin is acceptable.
5. What the knowledge admission bar becomes when carriers rarely share a domain.
6. Whether *write nothing before approval* survives once research records are exempt, or only the
   generated instruction files stay gated.
