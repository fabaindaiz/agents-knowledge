# The roadmap's Next, triaged, and the two first-minor criteria priced

Date: 2026-11-25. Home repository, after the 0.0.36 cut, on one machine. Read-only apart from this file: three
delegated agents read the code, the records and git, and ran nothing but `evals/harness.py check` and
`release.py report`. Inputs to the plan of `d-5ed7e8-f6858b` (every *Next* item before 0.0.36 is carried).

## 1. Every item, checked against the code

Size is agent minutes · tokens · review rounds; "—" means nothing to build. A state is the triage's reading, checked
against a commit or a file, not the item's own text.

| id | title | state | size | owner? | carrier-facing | depends | kind | phase |
|---|---|---|---|---|---|---|---|---|
| 516d7a | 0.0.36 plan's nine tasks | partly: cut done; task 5's pilot left | 10·100k·1 + pilot | yes: which feature pilots the spec | yes | — | tool | 1 |
| b9628b | harvest/update guessed steps | open | 40·400k·2 with the re-run | no | yes | — | method text | 1 |
| 468621 | a fix's red never seen | partly: the habit in §18; no check | 6·60k·1 | yes: build the check | no | — | tool | 2 |
| 4cf7df | zsh unquoted-variable guard | open | 10·100k·1 | yes: approve it | no | — | tool | 2 |
| a3a0a1 | private channels research | open | 4·100k·0, background | yes: approve, then a channel | no | — | research | 5 |
| 151456 | 0.0.34 carrier branches | partly: four wait | the owner's hands | yes | yes | — | records-only | owner |
| cfd663 | phase-2 edits in carriers | open | the owner's hands | yes | yes | — | records-only | owner |
| 2ebcee | push as its own step | done | — | no | yes | — | — | 1, to *Done* |
| 9ef5d1 | anonymised usage path | done: `usage measure` | — | no | no | — | — | 1, to *Done* |
| a6b77f | split home commands from the tool | open | trace 20·250k; split 30·300k·2 | yes: a breaking split | yes | ee9f86 | tool | 4 |
| 74cbcd | gate cost, a retirement rung | open | 25·250k·1, background | no | yes | — | research | 3 |
| fe15a8 | oldest candidates, queue defects | open | 5·40k·1 + six intake turns | yes: six verdicts | no | — | records-only | 2 |
| a98470 | decisions check counts | done | — | no | no | — | — | 1, to *Done* |
| ee9f86 | count carrier-unused commands | done | — | no | no | — | — | 1, to *Done* |
| 23e94e | re-examine the export cap | open, unblocked | 10·80k·1 | yes: archive or keep the cap | yes | 5e0415 | records-only | 4 |
| 57358a | remove the product-noun check | done | — | no | yes | — | — | 1, to *Done* |
| 26a753 | worktree environment exception | done | — | no | yes | — | — | 1, to *Done* |
| 25ecc8 | usage `.gitignore` | done | — | no | no | — | — | 1, to *Done* |
| 8b542b | `ids` resolves slugs | done | — | no | no | — | — | 1, to *Done* |
| 5e0415 | `changelog --since` gap | done | — | no | yes | — | — | 1, to *Done* |
| dfae87 | 0.1.0 stable release | open, its target stale | 12·100k·1 | yes: a new target | yes | 3e6760 | method text | 5 |
| d6ecfe | persistent delegates | open | 15·150k·2 | yes: a design round | yes | 55e022 | method text | 3 |
| 045188 | a delegation's estimate first | done in 0.0.36 | — | no | yes | — | — | 1, to *Done* |
| 655151 | candidate-to-history command | open | 20·150k·2 | no | no | — | tool | 2 |
| 023814 | the session proposes the split | open | 10·100k·1 | yes: a design round | yes | 55e022 | method text | 3 |
| 55e022 | cost as a principle | open | 20·200k·2 | yes: design; the coding budget is nearly spent | yes | — | method text | 3 |
| 7e0dd7 | traditional development alongside | open | 20·200k·2 | yes: a design round | yes | — | tool | 3 |
| 2a2e86 | a partial gather waits | obsolete | — | no | no | — | — | 1, to *Done* |
| f0680a | parallelisation measured on cost | open | 30·300k, background | no | no | 1ac328 | experiment | 5 |
| be0f54 | a plan measures before executing | partly: needs, risks, spike, fresh read shipped | 8·80k·1 | no | yes | — | method text | 3 |
| b8c4b2 | privacy false positives | done | — | no | yes | — | — | 1, to *Done* |
| 36d9b1 | `user-walk` trigger gate | open | 15·150k + an eval | yes: a pilot carrier | yes | — | experiment | 5 |
| 1e9c1c | a reduction pass read by another | partly: `docs fingerprint` exists, unnamed in prompt-sync | 5·30k·1 | no | no | — | method text | 2 |
| 780330 | worktree git calls apart | open | 3·20k·1 | no | yes | — | method text | 1 |
| 6cf312 | `new entry` traceback | partly: `--write` to a missing log raises | 5·40k·1 | no | yes | — | tool | 1 |
| 11e17f | `memory-diff` in a worktree | open | 8·50k·1 | no | yes | — | tool | 1 |
| 307d02 | carrier audits stop re-checking | open | 10·80k·1 + per carrier | yes: drop the checks or ship `--json` | yes | — | tool | 1 |
| 7d64ee | guide and `next`, other languages | partly | 15·150k, background | no | no | — | experiment | 5 |
| fca056 | Cursor and Copilot support | partly: levels 1–2 shipped | 20·150k; level 3 the owner's | yes: CLIs, keys, terms | yes | — | experiment | 5 |
| 578c22 | trigger evals for the new skills | partly: `edit-docs` never evaluated | 15·150k, background | no | no | 36d9b1 | experiment | 5 |
| 54cb3f | the 2026-10-05 research leftovers | partly | 10·80k·1 | yes: a re-weigh | no | — | records-only | 5 |
| 89ec30 | refuse a filtered gate | open | 5·40k·1 | no | no | — | tool | 2, into bd65a0 |
| e09738 | eval instrument defects | partly: three left | 8·80k·1 | no | no | — | tool | 2 |
| bd65a0 | `release.py commit` | open | 15·120k·2 | no | no | 89ec30 | tool | 2 |
| 94f262 | review one carrier's method changes | open, overdue | 15·150k·1 | no | yes | — | method text | 3 |
| cc0b86 | queue the 0.0.27 notes' experiments | done in effect | — | no | no | — | — | 1, to *Done* |
| 3a8f87 | redesign 2: bases, audit library | open | 40·400k·2 | yes: keep in *Next* | yes | — | tool | 4 |
| 46b707 | redesign 3: router, brief | partly: `lookup` shipped | 30·300k·2 + pilot | yes: keep in *Next* | yes | 1ac328 | tool | 4 |
| 4a5e6d | redesign 4: jobs as skills | open | 40·400k·2 | yes: keep in *Next* | yes | 0ae753, 705aa8 | tool | 4 |
| f542de | redesign 5: bootstrap interview | open | 30·300k·2 | yes: keep in *Next* | yes | — | tool | 4 |
| 211d11 | a faster intake lane | open | 8·80k·1 | yes: the lane rule | no | 3e6760 | method text | 3 |
| 408166 | privacy: an id beside a description | partly: per line only | 12·100k·2 | no | yes | — | tool | 1 |
| 5df552 | a topic slug for proposals | open | 15·150k·2 | yes: a proposal format change | yes | — | tool | 1 |
| a4c2b2 | pre-commit runs `build --check` | open | 5·40k·1 | no | no | — | tool | 2 |
| 3e6760 | the first minor's criteria | open: 2 and 3 fail, 1 unproven | 10·80k·1 per cut | no | no | b9628b, 1ac328 | records-only | 5 |
| 1ac328 | consulting cost under ×2 | partly: `lookup` shipped | 60 wall, background·500k + API spend | yes: the spend | yes | — | experiment | 5 |
| ef066e | review hand-written boundaries | open | the owner's read, 5·50k | yes | yes | — | records-only | 3 |
| 543516 | publish release pages | open | 10·60k | yes: publish outward | no | — | records-only | owner |
| d3ee51 | 0.0.22 residual gaps | done: into 688897 | — | no | yes | — | — | 1, to *Done* |
| 688897 | residuals that lose no record | open | 15·100k·1 | no | yes | — | tool | 1 |
| 0ae753 | trim the update and bootstrap reads | open | 10·80k·1 | no | yes | — | method text | 1 |
| d65a4c | `applies_if` per note | partly: 6 of 53 | 20·200k·1 | no | yes | — | method text | 3 |
| 8236cb | `AGENTS.md` as the root artifact | partly | 8·80k·1 | no | yes | — | method text | 3 |
| d4f710 | verdicts on overlapping notes | open | 15·150k·1 | yes: merge or supersede | yes | — | method text | 3 |
| 08c9f7 | layout survey update | partly | 8·60k·1 | no | no | — | research | 3 |
| 1e9567 | persistent privacy warnings | partly: 350 over `--tracked` | 10·80k·1 | yes: the policy | no | — | tool | 2 |
| 3fa5c5 | a release cadence | open | 5·40k·1 | yes | no | — | method text | 3 |
| 973bd7 | the cheapest queued experiments | open: 64 queued | 40·400k, background | no | no | — | experiment | 5 |
| 705aa8 | duplicated prose | partly | 15·150k·1 | no | yes | 16b90a | method text | 3 |
| 13a8be | the private-terms list complete | ongoing | 2·10k | yes: the names | no | — | records-only | 2 |

## 2. The phases

1. **Carrying safely:** b9628b, 688897, 6cf312, 11e17f, 0ae753, 780330, 5df552, 307d02, 408166, 516d7a's rest; and the
   fifteen done or obsolete items moved to *Done*. About 130 min, 1.3M tokens, plus a cut.
2. **The home's enforcement and records tools:** bd65a0 (with 89ec30), a4c2b2, 4cf7df, 468621, 655151, fe15a8, 1e9567,
   e09738, 1e9c1c, 13a8be. About 90 min, 750k.
3. **Method decisions**, design rounds first, bounded by the coding budget: 55e022, then 023814, d6ecfe, be0f54;
   7e0dd7, 211d11, 3fa5c5, 94f262, d4f710, ef066e, 8236cb, 08c9f7, d65a4c, 705aa8, 74cbcd. About 200 min, 2M.
4. **Structure, breaking for carriers:** a6b77f's trace then split, 23e94e, then 3a8f87, 46b707, 4a5e6d, f542de. About
   230 min, 2.3M; may span two releases.
5. **Measurements and research, in the background, one at a time:** a3a0a1, 1ac328's pilot, f0680a, the 36d9b1, 578c22
   and 7d64ee trigger evals, fca056's canaries, 973bd7, 54cb3f; then 3e6760 and dfae87 at the cut. About 230 min wall,
   2.2M plus API spend.
6. **The owner's hands:** 151456, cfd663, 543516, and 516d7a's pilot choice.

Total: about fifteen hours of agent time and 8.5M tokens over four or five releases. Twenty-two decisions are the
owner's, more than one walk holds, so each phase's are walked before that phase.

## 3. Criterion 2: the gaps the copy runs found, with the fix drafted

1. H:214-217 vs H:294-296: step 3 delegated agent vs never leave a refusal unwritten -> refusals wait too, named in the report; H:294 "written once step 3's list is shown; a delegated agent reports it instead". +45
2. H:266: outbox detection -> `bundle.py verify` names an outbox; run it before Phase 1, convert first. +25
3. H:130-133: later-harvest branch, carrier side -> `git show BRANCH:.agents/carrier.toml` per branch ahead; optional: check-local prints other branches' harvested_through. +50
4. H:251: "last date read" -> last date whose records were read; unread transcripts to harvested_gaps as `span: transcripts`. +30
5. H step 8: harvest's own log entry via `new entry "harvest" --write` unless repo rules say none. +40
6. U:5-7: no home -> run the tool of the tree that holds the release. +50
7. U:209-216: live vs incoming -> follow live; incoming only diffed; switch only on approval at step 5. +35
8. U:79-83 + Reads: step 4 needs prompt-harvest Phase 1 -> +1,900..2,200 tokens (OWNER: keep in Reads, or point to a separate session).
9. U:106-117: `--migrate` prints, then `--migrate --write`; it names tables it leaves (open section) -> map by hand. +25
10. U:273: Phase 4 wiring lines -> root map carries them; read bootstrap §Phase 4 only when a delta names a wiring line. +40
11. U:119-121: one entry from `new entry "<title>" --write` (id from title; `id s "<title>"` same); optional: new entry prints its id. +30
12. U:272-273: other host -> its own agent folder, or none: say so, skip, record in adapted. +30
Shared unattended rule, pasted in both "Before you start" (H:73, U:140): "**Unattended run (no one to answer).** Say so first, take every proposed default, and write each one taken as `unattended: <question> -> <default>` at the head of the report and in the log entry. Never take a choice that needs the human's yes: a privacy warning or allowance, step 3's candidate list, a delete outside an approved table, a merge or push. Record it as pending and leave it unwritten. Stop rules still stop." +140 each.
Budget: harvest +370, cuts: drop bootstrap §8 from Reads (-1,077), anecdotes H:132-133, H:237-239 (-90): net ~-800 (26.3k -> 25.5k). Update +390 (+1,900..2,200 for item 8); cuts: U:40-54 to one sentence (-250), anecdotes U:208, U:214-216 (-70), drop §Version numbers (-147) and §Which document to run (-651) from Reads: net +1,170..+1,470 (8.5k -> 9.7..10.0k). No cap enforced on update/harvest (BUDGETS bundle.py:3425: coding, review, card).

## 4. Criterion 3: the cost pilot, priced

- Measured last: pilot-11 at 0.0.30, x2.74 [2.14, 3.57] vs minimal on 4 non-trivial tasks (evals/REPORT.md:593); a437c6 half measured (~1/60).
- Run: Study 1 cost smoke, pilot-9's six tasks, claude-sonnet-5, --config-dir default, 60 turns, 1800 s, 3 reps, --jobs 3; arms minimal, a 0.0.30/0.0.29 tag arm, a new v36 tag arm: 54 trials.
- Prep: add the v36 arm to evals/harness.py (CONDITIONS, TAG_BUNDLES, ROUTINGS with ROUTING_V30, REVIEWER/ALL_AGENTS arms) and a PREDICTIONS entry in cost_smoke.py; register prediction and rule in PROTOCOL.md before any trial; verify the frozen wiring against prompt-bootstrap Phase 4.
- Cost: a few units of currency at list price, about a tenth of one per trial as an earlier pilot measured; about an hour or more of wall time (ASSUMPTION).
- Expected: x2.7-2.9 (index +4.7%).
- Levers: (1) code lookup + triage line instead of the full index read (untested, predicted <=x1.5); (2) D2 index split (measured x0.97, weak); (3) output and report length (~3/10 of the extra).
- Caveat: 4 tasks give a wide interval; more tasks beat more reps.
- harness.py check: all tasks valid.
