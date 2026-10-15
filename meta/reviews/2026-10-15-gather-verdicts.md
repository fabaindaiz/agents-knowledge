# Gather of 2026-10-15 — every proposal with its verdict

**Phase 1 of a meta-session, read-only. Nothing here has entered the ledger, the queue or the
notes; this file is the one table the owner approves before any of that is written** (`AGENTS.md`,
*The meta-session is this repository's normal session*, step 2).

Four carriers and one pack offered **90** proposals (17, 6, 4, 17 and 46). The gather held none back for
privacy, lost no line and reported no problem. **Twelve were already taken in at 0.0.31** and are listed
last: they are still in their carrier because it has not pruned, and they need no verdict. **Three more,
written on 2026-10-08, appear in no record at all** and are treated here as new. The intake is therefore
of **78** proposals.

A rule the harvest itself offers changes how this table counts (`p-a350eb7be0`): where several carriers of
one owner restate a line of that owner's global instruction file, they are **one** occurrence, not several.
The rows it affects say so.


## Fold into an existing active note, as another occurrence or a boundary (16)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-01b64707f7` | `refusal-must-not-read-like-an-answer` | K | Fold: a check piped into a filter inside an AND-chain loses its exit status, so a red check lets the commit through. Three occurrences, literature on the pipeline's status. Pairs with p-e6b84078cb. |
| `p-10252a897c` | `a-request-accepted-is-not-an-effect` | K | Fold: two occurrences (a mute accepted and read back while one output kept sounding; a level restored from a key shared by every stream of one program). |
| `p-1a2eedf51d` | `test-double-fidelity` | K | Fold: a double of a command-line tool that accepts an operand the real tool reads as an option; POSIX Guideline 10 checked at the source. |
| `p-a17f44c746` | `test-double-fidelity` | K | Fold as a prior question to the note's own: which double is this, and does more than one claim the name. One occurrence, no literature. |
| `p-5e0bb60fc9` | `reproduce-the-checkout-not-only-the-environment` | K | Fold: a toolchain pin found by walking up from the current directory applies only under it, so a build driven from a sibling uses the machine's default. Documented behaviour, checked. |
| `p-933d6dd2d0` | `ratchet-in-a-pinned-environment` | K | Fold as a boundary: where the counting environment cannot be pinned, the gate measures the baseline in the same environment instead of storing an absolute. |
| `p-789fae0a47` | `ratchet-in-a-pinned-environment` | K | Fold: pinning the tool does not pin what it counts; baseline the findings, not a total. Measured, and the same shape found three times in ten days. |
| `p-94b8414888` | `order-writes-by-failure-residue` | K | Fold, marked reasoned-not-executed: a core that adopts a configuration before the receiver accepts it keeps feeding the rejected one. |
| `p-9ce408ea7a` | `sweep-the-rendered-extremes` | K | Fold: the combinatorial axis (which notices appear at once); 288 combinations in one round found what four rounds of named cases had not. |
| `p-9d64b4aa5b` | `a-default-scope-is-the-widest-one` | K | Fold: an empty test selection, built by a shell feature the host lacked, read as run-everything. |
| `p-a794efaf45` | `coverage-measures-execution` | K | Fold: one mutant per design decision as a cheap substitute for a suite-wide score when a new suite passes on its first run. Two mutants, a quarter and two fifths of the new tests red. |
| `p-b67eebb06b` | `a-check-must-be-seen-to-fail` | K | Fold, with a new boundary worth the release's attention: a planted violation must be placed where the property it violates is visible. Literature on equivalent mutants. |
| `p-d9d4ea8c83` | `a-surviving-guard-mutation-means-a-missing-input` | K | Fold: a surviving mutation of a format-unchanged check, and a control that plants an allocation and must see it counted. |
| `p-ddd0740846` | `refuse-only-on-unassertable-evidence` | K | Fold: a third party asserting the refusing signal about the victim (token in the query string, no origin header, a few image tags lock the victim out). Reasoned, not run. |
| `p-d4e7c33d0e` | `validate-each-transformation-run` | K | Fold: the case before the note's own, the run touched files nobody named. A one-file command rewrote 140 files because the wrapper discards paths. |
| `p-10200ae07a` | `count-both-sides-and-use-a-control-window` | K | Fold: report the control's margin, not only the pass; a control that passes by about the race's own window has not exonerated anything. |

## Fold, and it bears on a pending review verdict (1)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-f37ce3e959` | `a-rewrite-cleans-only-what-refs-reach` | K | Fold AND it bears on this note's pending review verdict: never rewrite in a shallow clone (a fifth of the commits folded into a new root while every tree compared equal). Documented, checked. |

## An experiment's result, to record (2)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-a710d381ad` | `nested-partial-update-replaces` | K | Experiment confirms, against the store's own emulator. Record the result and fold its cheaper check: assert on the key an earlier delivery wrote, no access to the client's internals. |
| `p-3aa4282e09` | `timeout-is-not-an-outcome` | K | Experiment result: this harness reports the third state explicitly rather than collapsing it into failure. Supplies the occurrence the candidate lacked. |

## Proposed for admission as a note in 0.0.32 (2)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-32b9f2d027` | `a-workaround-that-writes-the-subject-destroys-the-measurement` | K | Admit as a note, with the literature search done at intake (observer effect): two independent carriers, a live device and a long-running service, with the causes only separated once the probes stopped writing. Pairs with p-d403dcf9a0. |
| `p-d403dcf9a0` | `a-workaround-that-writes-the-subject-destroys-the-measurement` | K | Second occurrence of the row above, from another carrier: the agent's own probes wrote the level under diagnosis, and one probe played into the very output being diagnosed. |

## Queue as a candidate (27)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-74aa2517d1` | `an-exemption-must-fail-when-its-reason-is-gone` | K | Queue (K), strong: the exemption is a second claim, and three lines make it self-expiring. Proved both ways by moving the exempted file. Lacks a second kind of allow-list. |
| `p-c3405d47c0` | `a-reservation-lock-and-an-atomicity-lock-are-not-the-same-wait` | K | Queue (K): only the reservation should make anyone wait; the atomic step gets one attempt and its contention maps to the domain's own conflict. Two measurements, one of them an accidentally correct status. |
| `p-fbc5e24561` | `a-lease-is-the-stranding-window-not-the-work-window` | K | Queue (K), strong: the lease measures how long work stays stranded, not how long it takes. Literature consulted (Gray and Cheriton, fencing tokens) and the gap named. |
| `p-7a55883d4d` | `an-injected-parameter-defeats-the-checker-and-its-usual-test` | K | Queue (K): a framework-injected parameter defeats the checker, and the usual «the caller calls it» test substitutes the callee, so it never proves the arity. |
| `p-cc533b4818` | `a-probe-catalogue-is-an-allow-list-not-a-shell` | K | Queue (K): a diagnostic tool against a live system is a catalogue of exact commands, not a verb with a free argument, or it is a remote shell with extra steps. |
| `p-3da35ed9c3` | `a-typed-callable-can-be-the-unbound-declaration` | K | Queue (K): the checker cannot tell the function implementing an operation from its declaration, so the guarantee a typed rewrite buys needs an effect assertion. |
| `p-4299e95d58` | `control-messages-do-not-share-a-lossy-queue-with-telemetry` | K | Queue (K), weak evidence: reasoned from a design review, no measurement, no literature consulted. |
| `p-c457db22cd` | `a-failure-before-the-limiter-counts-is-a-free-attempt` | K | Queue (K): a parse failure raised before the limiter counts makes the attempt free and unanswered. Reproduced and fixed; overlaps two existing notes. |
| `p-e6e2f44afe` | `releasing-a-global-lock-per-short-call-convoys` | K | Queue (K), measured and with the convoy-effect issue cited; its general half (measure a cost under the condition that produces it) may fold into an existing note. |
| `p-e8e7ae397b` | `a-perceptual-comparison-switches-without-a-gap-with-confounds-matched` | K | Queue (K): switch without a gap and match everything not under test. Lacks the literature verified against its source (marked INFERIDO). |
| `p-fefac267a4` | `a-relative-priority-is-relative-to-an-inherited-one` | K | Queue (K): a relative increment from a boosted thread leaves the child above normal. Not measured. |
| `p-61c0386538` | `a-convention-only-one-party-follows-degrades-to-a-suggestion` | M | Queue (M), strong: a check must tell work from inside the process from work from outside, and never rewrite what is merged. The cheapest way to green was editing someone else's record, and it passed. |
| `p-aaa9bac8d0` | `ready-is-stated-in-the-humans-terms` | M | Queue (M): where the human owns the publishing step, readiness is stated in the terms their command evaluates. Two occurrences in one session; the check is the read-only half of their command. |
| `p-6ff0438253` | `verification-load-competes-with-the-product` | M | Queue (M), measured with figures and kernel documentation: where the gate's machine also runs the product, the failure appears in the product. Lacks a second repository. |
| `p-ad30abad01` | `a-push-that-deploys-is-a-publish` | M | Queue (M): where the default branch deploys on push, «merge now, release later» does not exist. One occurrence, published before a cancel could land. |
| `p-ca617d2726` | `a-remaining-budget-reorders-the-plan-toward-closing` | M | Queue (M): a reported remaining budget re-orders the plan toward closing what is done. One occurrence; the owner's own instruction file is its source. |
| `p-db2fbd6bf8` | `a-guided-test-holds-the-blind-in-the-agent` | M | Queue (M): the agent draws the order, applies and verifies each option, asks only for the judgement, reveals afterwards. About twenty steps; two pairs found confounded. Useful to the experiments' protocol. |
| `p-5a407946ce` | `a-capped-key-list-and-a-ladder-by-form` | M | Queue (M): a capped key list plus a ladder by form, not by level. Designed with the owner one decision per turn and applied at once; overlaps the budgeted-root-file rows. Owner's file is its source. |
| `p-aede899fd0` | `a-board-of-what-is-active-while-agents-run` | M | Queue (M): a board of active tasks at the end of every message while delegates run. Owner's instruction, one carrier. |
| `p-9b961f278a` | `a-batch-states-why-it-is-split-and-which-model` | M | Queue (M): a batch states why it is split that way and why each model. Merge with the delegation rows below; same source. |
| `p-e31a0177df` | `a-plan-carries-a-cost-ledger` | M | Queue (M): per task the model, the estimate and the actual, with the totals. Merge with the delegation rows; same source. |
| `p-68b51667be` | `a-delegation-is-priced-before-it-starts` | M | Queue (M), one row with p-df414d871b: price before launching and take the cheapest model the task allows. |
| `p-df414d871b` | `a-delegation-is-priced-before-it-starts` | M | Same row: adds the batch shape (two or three agents on grouped tasks) and its integration step, with reported figures per run. |
| `p-eacfe1124f` | `a-passing-observation-is-not-an-order-to-purge` | M | Queue (M): fix what was named, report the rest, ask before widening. No occurrence in the session that wrote it, which the proposal says plainly. |
| `p-9b2fbaad7a` | `an-interaction-is-designed-one-decision-per-turn` | M | Queue (M): anything that changes how the human interacts is designed with them, one decision per turn. Its natural experiment is available here (which steps carriers adapted or declined). |
| `p-ad6874c637` | `cited-identifiers-carry-their-names` | M | Queue (M): a message citing hash-shaped ids carries a table naming each. One line per id; this home already owes it. |
| `p-ce0c867e01` | `a-finding-belongs-to-the-repository-that-can-fix-it` | M | Queue (M): record a finding where it can be fixed, leave a pointer where it was seen. One-line rule, owner's instruction. |

## Queue, and worth applying now (2)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-7d6c334723` | `kill-by-command-line-pattern-matches-own-shell` | M | Queue (M) and worth the ladder's next rung now: five occurrences in four sessions, the prose rule did not hold, the manual confirms the parent shell is not excluded. The bundle's standard permission rules can carry the typed form. |
| `p-96c1b445c5` | `a-completeness-marker-must-survive-truncation` | M | Queue (M) and apply to the home's runners: print the completeness marker at the end too, because agents read long output through a tail filter. One duplicated line replaces a rule asking the reader to behave. |

## Apply to the method or an agent in 0.0.32 (14)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-0907e14e60` | `questions-go-together-priced-and-before-the-writing` | M | Apply to prompt-context §15 (one row with p-26dc5c14cd): the method already asks for the shape and never says why the three parts matter, so both stops are read as a formality. |
| `p-26dc5c14cd` | `questions-go-together-priced-and-before-the-writing` | M | Same row: the disambiguation format (options with what each implies and costs, a middle option, «explain more»), noticed by the owner when an agent dropped it. |
| `p-c3aab40082` | `instructions-arrive-through-three-channels` | M | Apply to the closing and consulting procedures (one row with p-031ead1231): name the three channels, or «account for every part of what was asked» is read as covering the typed turns only. |
| `p-031ead1231` | `instructions-arrive-through-three-channels` | M | Same row, from another carrier: about one in six structured answers carried the instruction in its free text, and at least five instructions arrived mid-turn. |
| `p-a350eb7be0` | `an-owner-instruction-file-is-one-source` | M | Apply to the admission procedure itself, and it changes this very table: carriers of one owner that restate a line of that owner's global file are one occurrence, not several. Five of the rows above are so marked. |
| `p-4d00f226a1` | `isolated-review-by-default` | M | Answers the candidate reopened at 0.0.26 with the whole-branch figures it lacked: three reviews of batches already green found six, seven and three important findings, and re-running each delegate's claimed checks caught two false reports. |
| `p-f5033c1cc7` | `prompt-harvest` | M | Apply: the harvest shows its candidate list to the human before writing, because only they can tell their one-off instruction from their rule. Run as a question on eight candidates, the human took all eight. |
| `p-3d5f7e5d77` | `prompt-context` | M | Apply: an ask rule on a file is kept only by the host's edit tool, so a delegate brief says it, and a regenerating tool bypasses the rule as a shell write does. |
| `p-e6b84078cb` | `prompt-context` | M | Apply: the commit-on-exit-status rule must reach every place a commit is made, not only the closing skill. Two hidden reds in a day; both remedies held for two sessions. |
| `p-778e62a33b` | `prompt-context` | M | Apply, and extend this home's own check: author and committer identity is a second attribution channel the setting does not reach, and a trailer check cannot see it. A history was rewritten twice for it. |
| `p-c1f5e5068b` | `prompt-update` | M | Apply: a carrier follows a copy of the update that predates the delta it is applying, so a release that changes the update itself is invisible. Mark such deltas in the changelog, or read the incoming procedure as data. |
| `p-c653e9969c` | `prompt-update` | M | Apply: a release that changes the bundle's shape cannot be verified by the tool of the shape it replaces (fifty-one false problems). The update must name which tool verifies across a shape change. |
| `p-3a5177156d` | `researcher` | M | Apply in 0.0.32, highest priority of the method rows: the researcher's shell hook fails open where python3 is older than the tool needs (the version refusal exits 1, and the host treats any status but 2 as non-blocking, so every command is allowed). |
| `p-3d3316d1ee` | `state-review` | M | Apply: a skill's installed text must not name the carrier's own directories; the area-guide list belongs in the carrier's LOCAL.md. Same for the user-walk skill's repeated path line. |

## Needs one decision from the owner before it can be applied (5)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-9594c7ac75` | `prompt-harvest` | M | Needs one decision: a single high-water date cannot express a span read out of order. Record the spans read, or name where the out-of-order note goes so the next harvest looks there. |
| `p-360caf783c` | `prompt-context` | M | Needs one decision: for a delegate, a long check runs in the foreground split into pieces, not in the background — this reverses the current advice in §Long runs and delegates. Three stalled delegates and three killed background suites. |
| `p-fa58a0105d` | `proposals-readme` | M | Needs one decision, offered by two carriers independently and with its prediction held: a generated proposal has no title and fails a carrier's one-heading rule, and its identity is a hash so it cannot be fixed there. A title in the generator, or a named exemption in the README. |
| `p-b79c6549b7` | `proposals-readme` | M | Same decision, the first of the two occurrences: six freshly generated files went red in the step meant to confirm the close was finished. |
| `p-a2a7b66e7d` | `bundle-ids` | M | Needs one decision: an append-only record quoting an id-shaped placeholder is a permanent red, since entries are never rewritten. A skip marker the scanner honours, or a documented exemption. |

## A tool fix in 0.0.32 (3)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-5ed6279a27` | `bundle-count` | M | Fix the tool: match on word boundaries and name the unit where the count is printed. A three-letter symptom matched the middle of unrelated words, and the number is what gets quoted into a close. |
| `p-8a31b505c4` | `ids-reports-a-cited-id-defined-nowhere` | M | Fix the tool: report a cited id with this carrier's prefix that is defined nowhere. A probe over one repository found exactly one among well over a hundred, with no false positive; the current check passed a planted undefined id silently. |
| `p-df53430dec` | `bundle-privacy` | M | Fix: the check a carrier runs before offering its work must be the one the home applies when taking it in, or the difference is written where the carrier reads it. Four carriers closed the same day on that assumption. |

## A bookkeeping repair (1)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-d3aee52401` | `bundle-tool-export` | M | Already answered at 0.0.31 (`export --replace`), but this proposal was never recorded as received. Record it, with the history row pointing at the answer. |

## Refused, to the history (3)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-15e0f40f16` | `host-shell-traps` | K | Refuse, same reason as p-1420579d20: one machine's host friction, the same portability family. zsh does not split an unquoted expansion; it belongs in that carrier's root file. |
| `p-c5257b91f6` | `domain-listening-findings` | K | Refused by its own harvest (no claim survives without the domain's nouns). History row so the next harvest does not offer it again. |
| `p-fc9e89ae49` | `crossfade-law-follows-correlation` | K | Refused by its own harvest: one domain's fact, and its general half is ordinary two-sided boundary testing. |

## Merge into an existing candidate row (2)

| Proposal | Target | Kind | Verdict |
|---|---|---|---|
| `p-61ec6b0a14` | `a-worktree-check-needs-its-own-environment` | M | Merge: three further forms (no installed front-end dependencies in a new worktree, a per-worktree tool environment carrying older metadata, a stash shared by every worktree). The row's missing second occurrence arrives, from another carrier of the same owner. |
| `p-a1d190ad15` | `a-plan-keeps-a-status-table` | M | Merge: a plan as a living document amended in place, with a state section rewritten at each close. The row still lacks what it lacked, a carrier outside that team. |

## Already received at 0.0.31, no verdict needed (12)

`p-11a3b4d7c5`, `p-38a48d40f6`, `p-6fc1a0ee2d`, `p-b10b689423`, `p-b5ed4535bd`, `p-c5ccb46250`,
`p-c986101c49`, `p-cc620f4084`, `p-cd7569810c`, `p-f23391f5cc`, `p-f692458588`, `p-f94bec8bcc` —
their verdicts are in `received.md`; the carrier that offered them prunes them when it is next updated.

