# History — where each candidate went when it left the queue

Newest first. One section per release or harvest; each row says where the candidate went, so it
is not offered again as a fresh idea. The queue itself is `candidates.md`. Name a candidate by its
slug in backticks, in the first cell of a table row: that is how `release.py intake` recognises one
answered here, and how the build lists it in the ledger, `INDEX.md`. Nothing is dropped by age; a
row here is a release's decision, with its reason.

## Taken out of the queue by the release 0.0.29

The decision-record review settled by the owner (`meta/reviews/2026-10-05-decision-records.md`, rows in
`meta/decisions.md`), one carrier's proposals that had waited since 0.0.25, and the home's own. Four of that
carrier's proposals quoted text and were rewritten generalised by the carrier before intake, at the owner's word.

| Candidate | Where it went |
|---|---|
| `decision-log-status-decider-and-why` | **admitted into the method**, artifact 6: the Status cell, proposed rows only a person accepts, `unconfirmed:` and `accepting:`; the decider aliases, `unconfirmed:`/`found`, `accepting:` and the criteria under review until the 0.0.30 harvest |
| `decision-log-known-debt-and-criteria` | **admitted into the method**, artifact 6: *Looks deliberate, is not* and the criteria for a row |
| `decisions-check-and-migration` | **admitted into the tools**: `bundle.py decisions` and `--migrate`, tried read-only against every reachable carrier's log before release |
| `private-records-and-privacy-layers` | **admitted into the method and the tools**: the private folder, the sentinel rule, the public guard and the home's re-check; `propose` refusing was declined (`d-5ed7e8-e9cdd9`) |
| `adopting-a-host-that-keeps-adrs` | **admitted into the method**: the adoption table's row |
| `prune-cannot-lift-into-a-body-it-may-not-edit` | **answered**: already resolved; the prune's *Covered, worse* verdict offers the better wording as a proposal |
| `ids-misses-the-roadmap-heading` | **answered**: resolved in 0.0.27, where the roadmap template moved the id after the middle dot |
| `own-fields-have-two-homes` | **answered**: resolved; the method files carry no header fields, and `carrier.toml` is the one home the README states |
| `long-gates-run-where-a-watchdog-cannot-stop-them` | **applied to the method** with its correction: §*Long runs and delegates* in `prompt-context.md`, a line in the meta-session procedure and three lines per brief; the cause was a sleeping machine whose timers fired at wake, not load (`meta/reviews/2026-10-05-long-runs-and-delegates.md`) |
| `a-rewrite-cleans-only-what-refs-reach` | **admitted under review**, from the research of 2026-10-05 and the home's own rewrite; it awaits a carrier's rewrite or a decision to leave one, at the 0.0.30 harvest |
| `a-local-copy-of-the-release-procedure-goes-stale` | **folded** into `derived-copy-goes-stale-silently` as a form of it: a carrier skill restating the method's change procedure, read in place of its source |

| Proposal | Where it went |
|---|---|
| `p-0ddd2bc888`, an occurrence offered for the method's admitted `a-filtered-gate-cannot-block` | **recorded**: the home's own, on 2026-10-05; the enforcer is `i-5ed7e8-89ec30` |
| `p-3cd68c8c75`, an occurrence offered for the queued experiment `remote-mutation-names-target-effect-reversal` | **recorded**; the experiment stays queued |
| `p-5da3b658f6`, extends `split-a-checked-file-and-the-check-goes-blind` (folded into `a-check-must-be-seen-to-fail`) | **merged** into that note's evidence: an index check that globbed a folder a release had moved |
| `p-d8c7a59ff1`, extends `a-check-must-be-seen-to-fail` | **merged** into that note's evidence: two more checks over zero subjects, found by a triage |

## Taken out of the queue by the release 0.0.27

Method changes resting on one carrier's evidence were published marked so, and are reviewed at the next release. Proposals that extend a method file share its name as a slug, so each is recorded below by its id; occurrences offered for a note that stands are in the next section, also by id. Every figure a carrier gave is a ratio or an order of magnitude here.

| Candidate | Where it went |
|---|---|
| `refusal-must-not-read-like-an-answer` | **admitted** as a note, four repositories: the queued data-analysis occurrence and three offered at this release (a channel with no signal that returned the batch's cleanest timing, outvoting the median; tool glue that sent errors to standard output or swallowed the exit status; a lookup by name that answered a well-formed default for a name it did not know). The literature step ran before admission. Its experiment is queued in `experiments.md` |
| `readout-per-silent-outcome` | **admitted** as a note, two repositories: the second supplied the answer from the target runtime the row lacked (readouts read on the real device, the build identity read back as the only proof of which build ran), and a boundary: where a deliberate policy removes a known share, the per-reason count ships as a readout, not a check. Kept apart from the *fail visible* boundary of `fail-closed-defaults`. Its experiment is queued in `experiments.md` |
| `documented-defaults-drift-from-code` | **admitted** as a note, four repositories, with the remedy the row lacked: rewrite the reference from its reader, then hold every documented key table to the keys the reader reads, both directions and optional keys included, as a gate check seen to fail. A check scoped to required settings let about a third of the settings the code reads drop out of a template while it stayed green, which bounds the remedy. Boundary: readers whose keys are computed |
| `a-decoder-that-degrades-to-plausible-output-needs-an-out-of-band-check` | **admitted** as a note, with the second domain and repository it lacked: estimators whose self-consistency passed on correlated errors while their real error was orders of magnitude larger. A component that degrades to well-formed wrong output is checked only out of band (a parameter hash, a known truth, independent measurements) |
| `a-request-accepted-is-not-an-effect` | **admitted** as a note, two repositories: a session manager's policy that silently overrode accepted requests, and a deploy whose command succeeded while the old container kept serving (folded from an occurrence offered for `derived-copy-goes-stale-silently`). Read the resulting state back, not the exit status. Kept apart from `detect-by-observation-not-build-flag` and the exit-code clause of `a-check-must-be-seen-to-fail` |
| `a-version-bump-spends-the-forward-compatibility-it-was-protecting` | **admitted** as a note, with the second repository it waited for: one version shared by every record kind made an older build refuse every kind, and a writer that read unreadable as absent duplicated a once-only record. Remedy: a version per kind, and ask whether one is held at all before creating. The unreadable-as-absent half also extends `absence-is-a-third-value` |
| `a-surviving-guard-mutation-means-a-missing-input` | **admitted, narrowed** by the literature step to four explanations of a surviving guard mutant (no test produces its input, no assertion observes what it prevents, it is not worth a test, or the mutant is equivalent; equivalence is shown, never inferred from survival). The second repository brought several occurrences in a week and a boundary: run the surviving mutant over the production data before deleting the guard; a guard no real data reaches stays as declared specification, pinned by a synthetic test |
| `one-field-one-decision` | **folded** into `merge-by-shared-fact-not-shared-shape` as its dual, one sentence: the literature step found the core textbook (orthogonality, control coupling). Its second repository and domain, a notice's success tone that also triggered its auto-close, went into that note's *Evidence* |
| `an-error-response-is-a-retry-instruction` | **folded** into `retry-over-irreversible-effect` as a boundary, two repositories: an error reported after the effect is a retry instruction, so catch only the error that proves the effect did not happen |
| `empty-success-retried-write` | **folded** into `retry-over-irreversible-effect`, its second repository: a bodyless success decoded as an error, under a retry over any exception, would repeat power or delete writes. Its double that answered one body for every call is an occurrence in `test-double-fidelity` |
| `copied-code-carries-logic-not-the-values-it-compares` | **folded** into `fail-closed-defaults` as a boundary, two repositories: where the refusing condition is a value another system owns, failing closed locks everyone out; read the owner's current documented value before depending on it, and prefer conditions the operator controls |
| `tolerant-of-absent-is-not-tolerant-of-malformed` | **folded** into `absence-is-a-third-value`, three repositories: the claim keeps absent distinct from false, from empty and from unreadable; a value present but malformed refuses at boot, naming the key and never the value; parsers are tested with every lexical class the format retypes. Literature checked (a serialisation format's older integer forms, removed in its next version) |
| `recursive-scan-skips-nested-checkouts` | **folded** into `absent-constraint-widens`: an existence or uniqueness scan with no scope clause is satisfied by a superset (a nested checkout, a fixture, generated output). Two repositories, with the audit-walk occurrence the home took from a refused harvest (below). Its method half went to the bootstrap's step 0 brief: *In the tree* lists every worktree and its uncommitted state. one carrier's evidence; reviewed at the next release |
| `a-derived-artefact-copies-metadata-by-allowlist` | **extended** `copied-instruction-claims-its-origin`, applied with the queued 0.0.21 row on executable code: the claim widens from instruction files to metadata copied from the artefact another was cut from; copy it by an explicit allowlist |
| `a-judgement-check-warns-a-mistake-check-fails` | **extended** `ratchet-in-a-pinned-environment` as a boundary: a rule with no correct, portable zero (a judgement call, or a threshold that belongs to the machine that set it) stays out of the blocking gate, paired with a report someone reads. One repository for each form |
| `extend-reproduce-the-checkout-not-only` | **extended** `reproduce-the-checkout-not-only-the-environment`: an audit whose path checks read an ignored local folder, green in the working tree and red on every fresh clone (the permissive direction) |
| `reproducibility-runs-straddle-the-clock` | **folded** into `a-check-must-be-seen-to-fail`: two runs that share an uncontrolled variable cannot disagree on it, so the check could not fail; separate them by more than the timestamp's resolution, or vary the clock |
| `stored-timestamp-key-never-matches` | **folded** into `same-answer-or-refuse`: a cache key built from a fresh listing and from the stored copy is that note's round trip, and its failure is a cache that always misses. The in-memory double that kept the original object is one sentence in `test-double-fidelity` |
| `match-rendered-units-to-source-by-content` | **folded** into the queued `batch-get-is-unordered`, its second repository: two sequences paired by position when their orders differ. That row stands, lacking novelty |
| `mint-registers-the-carrier` | **folded** into the queued `verify-enforces-the-carrier-record`, same tool area: minting should register the carrier in the machine's manifest or print the line to add. Its never-receives-a-release half was answered at 0.0.26 (`find-carriers-by-searching-not-by-the-manifest`) |
| `a-field-run-names-its-readout-first` | **folded** into the principle 6 sentence of `a-measurement-states-what-would-invalidate-it-before-it-is-read`, its second repository: decide what will be read, from where, and what invalidates it, before the run |
| `a-choice-in-a-composition-is-measured-in-it` | **folded** into the principle 6 sentence of `a-cost-justified-by-an-unmeasured-constraint`, as its qualifier: measured on the composed result, not on the part |
| `a-number-is-only-a-measurement-after-the-last-edit` | **applied to the method**, three repositories, settling its placement question: principle 6, a number carries its date, its environment and the state it was taken at; an edit to what it measures turns it back into a claim |
| `a-cost-justified-by-an-unmeasured-constraint` | **applied to the method**, three repositories: principle 6, a cost or constraint that justifies a decision is measured before deciding, and the correcting measurement is checked like any other. When an estimate is good enough stays open |
| `a-measurement-states-what-would-invalidate-it-before-it-is-read` | **applied to the method**, two repositories: principle 6, write what would invalidate a measurement before reading the number. Its literature (preregistration) is not checked against the source |
| `identity-preserving-copy-is-a-no-op-mutation` | **applied to the method** with `a-mutation-that-did-not-apply-reads-as-a-result`, two repositories: principle 18's mutation paragraph asserts that the replacement happened exactly once and that the mutant builds before the test is read |
| `a-mutation-that-did-not-apply-reads-as-a-result` | **applied to the method**, see the row above |
| `the-call-site-is-untested-when-the-function-is` | **applied to the method**: principle 18, break the call site too (the argument replaced by a null, the call deleted, the assignment made a no-op); where that survives, extract the transport into a pure function. one carrier's evidence; reviewed at the next release. Its first form is the second repository of the queued `unconsulted-parameter-is-still-a-contract` |
| `expected-failure-names-its-exception` | **applied to the method** with `known-defects-as-must-fail-checks`, two carriers: principle 18, an expected-failure mark is strict and names the exception it expects |
| `known-defects-as-must-fail-checks` | **applied to the method**: principle 18, defects found at adoption are recorded as checks that must fail, and the gate fails when one passes until its mark and its roadmap entry move together. one carrier's evidence; reviewed at the next release |
| `isolated-review-by-default` | **applied to the method**, answering its 0.0.26 reopening with five repositories, one of them not code, and the cost figures it lacked (minutes, and on the order of 1e5 tokens or a few dozen tool calls, per review; nearly every whole-branch review after a green suite found an important defect): a whole-branch review in a fresh context is offered, with its cost, in one question at the end of every multi-task plan, neither run by default nor left to a request; task reviews do not replace it, and its fix wave is re-reviewed. The session loop's intro and step 4, principle 19 and the skills README's moment table are reconciled. The card-driven reviewer stays on request. Still unmeasured: a card-driven run on the same branches |
| `review-the-merged-change-after-the-task-reviews` | **applied to the method** with `isolated-review-by-default`, see the row above |
| `a-precondition-check-lives-where-the-action-already-looks` | **applied to the method**, four repositories: one paragraph in §The enforcement ladder, a rule acts only in the output the action already reads at the moment it applies |
| `a-session-ended-by-a-push-skips-the-close` | **applied to the method**: `close` is offered in one question before a push or deploy that ends a plan when it has not run (the close skill's description and §0, and the moment table). Its general half is the paragraph above; the specific: one carrier's evidence; reviewed at the next release |
| `a-local-memory-is-not-a-handoff` | **extended in the method**, four carriers with `harness-attribution-needs-a-root-rule` and two refused harvests' occurrences (below): a rule that lives only in one machine's memory or user-level file is reverted on the others and loses to a harness default (close step 5, bootstrap step 8's row); each carrier sets the host's attribution setting empty in its committed project settings, and a check fails on an attribution trailer. Its memory-diff false positive is **fixed** in 0.0.27 |
| `harness-attribution-needs-a-root-rule` | **folded** into the attribution change of `a-local-memory-is-not-a-handoff`, see the row above |
| `count-a-friction-by-searching-the-log` | **extended in the method**, two carriers: `bundle.py count` counts entries, not incidents, folds an event copied into several entries, and its help says so; the close skill's step 4 reads each hit and searches several spellings of the symptom |
| `a-deny-rule-stops-at-the-agents-prompt` | **applied to the method**, artifact 4, two carriers with `a-path-deny-covers-one-tool`: a deny stops the agent's typed spelling, not the same effect inside a script or a process that already holds the file; where the effect must not happen, enforce it in the tools or a sandbox. What is assumed of the host's permission behaviour is marked so |
| `a-path-deny-covers-one-tool` | **applied to the method**, see the row above |
| `edit-deny-also-blocks-shell-writes` | **applied to the method**, artifact 4, two carriers with `a-deny-for-secrets-catches-their-template`: a deny reaches more than meant, so test each against what the workflow must write; user-level denies merge with the project's, so read them together. `bundle.py verify` now warns when a user-level deny covers a committed file |
| `a-deny-for-secrets-catches-their-template` | **applied to the method**, see the row above |
| `document-language-is-its-readers` | **applied to the method**, three repositories: a document follows its readers' language, and the headings and keywords a tool parses follow the tool's (the bootstrap's technical-names rule and the language question of the bootstrap and evaluate pre-flights) |
| `dry-run-a-procedure-by-an-agent-before-release` | **applied to the method**, three repositories: bootstrap step 4 covers the worked examples a reader copies, and a guide a person runs with no disposable copy carries a tested undo section and is run once for real with approval, its expected outputs replaced by the observed ones |
| `citation-checked-for-existence-is-not-checked-for-relevance` | **applied to the method**, two repositories: bootstrap Phase 2, a reference that resolves is not thereby the right one; research becomes a decision's reason only after the cited text is read, and the tool run where the claim is behavioural |
| `a-fetched-specification-is-a-summary` | **applied to the method**, two carriers with `summaries-of-reference-pages-invent-syntax` (below): bootstrap Phase 2, a fetch tool that answers through a model returns a summary even at the primary address; download a machine-readable source whole and read it with a parser |
| `an-append-only-log-cannot-be-grandfathered-by-line` | **applied to the method**, two repositories (that the first occurrence is another carrier is an ASSUMPTION): principle 2, grandfathering exemptions are keyed on content, never on line numbers |
| `check-every-anchor-before-the-first-write` | **applied to the method**, two repositories: *Working safely in a tree you do not own*, a scripted edit across files asserts that every anchor matches exactly once, in every file, before it writes any |
| `a-rule-cannot-name-its-subject-as-its-enforcer` | **applied to the method**: principle 1, an enforcer is a check that runs and fails, not a name cited. one carrier's evidence; reviewed at the next release |
| `reread-the-source-case-before-recording-an-answer` | **applied to the method**, from two proposals of one repository: §15's fact interview asks one fact per question and never records a reason the human did not give. one carrier's evidence; reviewed at the next release |
| `commit-granularity-by-context` | **applied to the method**, two carriers with the refused `commit-split-rule-against-an-explicit-request` (below): bootstrap step 7 groups commits by context, and an explicit request from the human about grouping wins over the split rule |
| `a-delegated-change-to-a-check-is-a-finding` | **applied to the method**: the moment table's "the plan runs" row and the close skill's step 9, a delegate's change to a check (a filter on its output, a skipped red run, an added exemption) is a finding the controller reviews. one carrier's evidence; reviewed at the next release |
| `walk-the-rulings-before-the-plan-runs` | **answered by the method** of this release: §15's decision-review mode and the `decision-review` skill, whose opening cites this occurrence. One carrier for the before-the-plan claim; open: the reversal rate of rulings taken during execution |
| `measure-a-ui-change-as-a-task` | refused as knowledge by its own harvest, rightly; **the home disagrees in part**: it is **fixed** in 0.0.27 as evidence behind the `user-walk` skill (measure the walked task in actions, page changes and dead ends) |
| `a-prose-rule-loses-to-a-tool-default` | refused by its own harvest as an occurrence of an admitted note; **the home disagrees** with the target: **folded** into the attribution change of `a-local-memory-is-not-a-handoff`, to which it gave the remedy, the host's setting in the committed project settings |
| `summaries-of-reference-pages-invent-syntax` | refused by its own harvest as an occurrence of principle 6; **the home disagrees** in part: its automatic-summary half is **folded** into `a-fetched-specification-is-a-summary`, its second carrier; the delegated-report half stays an occurrence of principle 6 |
| `template-id-format-matches-the-checker` | **fixed** in 0.0.27: the roadmap template puts an item's id after the middle dot, where the id checker reads it. Further carriers met it at this release, one with a check green while blind on these ids (`experiments.md`) |
| `roadmap-heading-id-position` | **fixed** in 0.0.27, see the row above |
| `own-log-format-hides-new-method-fields` | **fixed** in 0.0.27: `bundle.py new entry` appends the method's fields a log's own format lacks, and names them |
| `bundle-tool-refuses-an-old-interpreter-in-one-line` | **fixed** in 0.0.27: the tools refuse an interpreter older than 3.11 in one line, before any import that needs it |
| `fix-stale-note-path-in-bootstrap` | refused: the path was corrected in 0.0.22, after the release the proposal was written against. Its second half, that the link check skips paths in code spans, is still true and is left to the roadmap |
| `a-principle-can-have-no-subject-in-a-carrier` | **reopened as a queued candidate**: the 0.0.23 answer (re-triage a not-applicable delta the day its subject appears) existed and did not act; apply-later reasons filed as declined were never re-triaged, and the deny they postponed would have stopped a destroyed working tree. It lacks a second carrier and a design. Its general half joined `a-precondition-check-lives-where-the-action-already-looks` |
| `steps-readable-by-a-permission-layer` | the compound-command form met its second and third repositories (one from a harvest that refused its own repetition, below); that sentence of artifact 4 no longer rests on one carrier, and no text changed. Classifier false positives from the candidate's first carrier were merged into its row, dated. The row stands, lacking a second repository for its other forms |
| `a-cache-key-names-its-invalidators` | offered again with a third repository (a privacy check scoped to changed files, whose terms list is an input missing from its key); its open question moved with two equality-key runs (see `derived-copy-goes-stale-silently`). The row stands, lacking the literature and that decision |
| `batch-get-is-unordered` | offered again with its second repository, the fold above; the row stands, lacking novelty |
| `gate-sequence-stops-at-the-first-red-step` | offered again: a gate red for a known, unrelated reason masks every new failure, the same masking in a one-step gate. The row stands, lacking its own-note-or-boundary decision |
| `committed-secret-is-not-a-gitignore-fix` | offered again with a second repository, if private data and secrets are one claim (read so here; the claim now says both): a check over each commit about to be pushed, and rewriting published history weighed by sensitivity and audience. The home's `bundle.py privacy --commits` and its pre-push hook apply the scan. The row stands, lacking the decision whether it extends `secrets-survive-rotation` |
| `adversarial-review-per-attack-surface-before-a-tag` | offered again with the second repository it lacked, widening the moment to a periodic review by area and concern; queued, not applied: its cost, and whether per-surface reviewers beat one, are unmeasured |
| `unconsulted-parameter-is-still-a-contract` | offered again with its second repository (a build option parsed and wired to nothing); the row stands, lacking the literature and its boundary |
| `verify-enforces-the-carrier-record` | offered again with the folded `mint-registers-the-carrier`; the row stands |
| `a-check-must-be-seen-to-fail` | **extended**: the executed census ran in two repositories (about two in three checks never observed to fail in one; every check seen red in the other, one of them green while blind for a session) and closes the queued executed run. Boundaries: count by implementation, not by subject; compare the count a check examined with the subjects known to exist, since partial blindness is not zero; inside one test only the first failing assertion is seen red; a probe of persistent state is bracketed with the state just before. The plant is the defect the check exists for, applied to the real artefact. Folded: `reproducibility-runs-straddle-the-clock` |
| `report-coverage-before-findings` | **extended**: a removal rule judged against a hand-written known-good list passes everything the list omits, so its coverage is the removed items read one by one; and a two-repository boundary: when the defect removes the subject from the found population, take the expected set from a source independent of the code under test and compare both ways. A third repository's hand-kept-list occurrence is folded in |
| `absence-is-a-third-value` | **extended**, occurrences from three carriers: a per-reason counter that writes only the buckets that fired (declare every reason, write zeros); several readers of one flag each collapsing "missing" their own way (one predicate that only an explicit value passes); unreadable read as absent; and the folded `tolerant-of-absent-is-not-tolerant-of-malformed`, above |
| `absent-constraint-widens` | **extended** with the folded `recursive-scan-skips-nested-checkouts`, above |
| `close-the-loop-in-the-actuators-frame` | **extended**, a second repository and mechanism: a residual measured downstream of the applied correction is already in the corrected frame, so adding it again counts it twice; estimate absolute targets and pin it with a test that applying twice gives the same result. Positional against incremental controller literature not checked |
| `copied-instruction-claims-its-origin` | **extended**: the claim widens to metadata copied from the artefact another was cut from, applying the queued 0.0.21 row; see `a-derived-artefact-copies-metadata-by-allowlist`, above |
| `derive-state-from-one-clock` | **extended**: the 0.0.26 boundary rewritten (an offset monotone in one direction holds only where the other is harmless; where both gain, bound placement on both sides from the monotonic anchor and clamp the instant state is evaluated at); a pooled platform resource's first report carries the previous user's position (bounded by the wall time since start; not measured on the target runtime); an accumulation hidden in a setup hook that re-runs on every view change |
| `derived-copy-goes-stale-silently` | **extended**, its boundary moved by two repositories: an equality key on modification time and size notices an older-dated edit, and its blind spot is an edit that keeps both, widened to the precision the time is stored at (whole seconds in an interpreter's bytecode cache, milliseconds in a scan cache). The freshness check sits on the path every consumer takes, applying the queued 0.0.24 row; a content-keyed step confirmed its exemption once. An occurrence offered here went to `a-request-accepted-is-not-an-effect` |
| `derived-over-chosen-identifiers` | **extended**, `confidence` reasoned → measured for the collision claim: over a handful of real packages, the self-declared name and version resolved under half exactly, a digest of the bytes all of them |
| `detect-by-observation-not-build-flag` | **extended**: a flag read, not stated, and found false on an emulator (a device-class property naming the target's class on an image about a fifth narrower). The queued row stays for a reading on the target device |
| `fail-closed-defaults` | **extended**, two boundaries from two repositories each: a boot check tests a value's shape, not its presence (applying the queued 0.0.24 placeholder row); and the folded `copied-code-carries-logic-not-the-values-it-compares`, above. A readiness probe does not cover upstream credentials unless it makes one cheap authenticated read |
| `merge-by-shared-fact-not-shared-shape` | **extended**: a second repository (per-surface content rules replaced by one predicate with a test that the two consumers' answers are complementary; a width split copied to a table that only looked alike, reverted), and the folded `one-field-one-decision` as its dual |
| `metric-against-trivial-predictor` | **extended**, *Evidence* only: beyond models, the trivial arm is doing nothing and the cheapest existing tool; the claim widens only when the comparison returns. The listening-test standard is not checked against the source |
| `nested-partial-update-replaces` | **extended**: a third client measured, whose semantics are per call, not per client (the same mapper call replaces with a nested value and touches a leaf with a dotted key); layered configuration is a partial update of the effective configuration (an override's table replaces the inherited one unless the tool names a merge). The queued row stays per client |
| `persist-inputs-derive-verdicts` | **extended**: results users have already seen version the rule by an effective date, compared with the input's real time; persist at the grain the user acted; a chosen-flag holds only if written in the same step as its value |
| `ratchet-in-a-pinned-environment` | **extended** with the folded `a-judgement-check-warns-a-mistake-check-fails` and a machine-dependent threshold: performance thresholds are set per environment, made relative, or kept out of the gate, since a red accepted as "red on main too" blocks nothing |
| `reproduce-the-checkout-not-only-the-environment` | **extended**: three more repositories for the permissive direction (audits that read an ignored folder or generated directories, green in the tree and red on a clean copy; a commit with an explicit path list that left out a new file); and a fourth input, a deliberately uncommitted local file, whose version the verdict names, a run without it reporting itself partial. `bundle.py privacy` now prints how many terms and which list it read, and says partial when there is none. The clean-export row stays queued |
| `retry-over-irreversible-effect` | **extended** with the two folds above (`an-error-response-is-a-retry-instruction`, `empty-success-retried-write`) |
| `same-answer-or-refuse` | **extended**, two repositories: a measurement or a check that reimplements the rule is a second path, so measure and verify through the product's own function; one comparison test was not built, and *Evidence* says so. Folded: `stored-timestamp-key-never-matches` |
| `secrets-survive-rotation` | **extended** with its first rotation incident, reproduced in two browser engines in a second repository: storage names derived from the key renamed everything on rotation, and the leftover sweep deleted the newly written file; name stored things from what survives the rotation |
| `sweep-the-rendered-extremes` | **extended**, two repositories: the matrix holds accessibility settings (reduced motion turned a pulse into an endless loop) and sequences of partial updates (a library's default copied a style attribute across a swap and broke a strict content policy). The release-build hang was not reproduced |
| `test-double-fidelity` | **extended**: the harness clock is checked against the host before a run whose readers filter by time; an interface method with a neutral default lets every double answer nothing (one repository); the rendered surface as a double met its second repository; an editor runtime is a double of each export target |
| `unrunnable-system-moves-the-gate` | **extended**: the composition-only boot rig, run once in a third repository, caught two composition failures no check saw, one of which a type checker also missed. It closes the queued boot row with a caveat (latent failures present now, not past startup failures it would have caught); `confidence` stays reasoned |
| `validate-each-transformation-run` | **extended**: an agent condensing a document is a transformation run, which moves the free-rewrite boundary (list the kinds of content that must survive and check each); and a guard that keeps each tracked file's line endings as in the last commit, seen red on a planted conversion |

**Proposals to a method file, or to an experiment, by id** (not slugs: the ledger lists none of them).

| Proposal | Where it went |
|---|---|
| `p-349520fae9`, extends `prompt-bootstrap`: one event copied into a later entry counts twice | **applied to the method** with `count-a-friction-by-searching-the-log`, above |
| `p-bf2579d9d9`, extends `prompt-context`: gendered references a delegated writer gave the maintainer | **applied to the method**: §20's table makes gendered references to a person whose pronouns were not given neutral, and a delegated draft is read for them before commit. one carrier's evidence; reviewed at the next release |
| `p-272e889ea9`, extends `prompt-bootstrap`: an offered commit with no enforcer at the moment it applies | **folded** into `a-precondition-check-lives-where-the-action-already-looks`, above; its specific enforcer (an end-of-turn notice of gated, uncommitted files) lacks a design |
| `p-843caad988`, an occurrence offered for the method's admitted `a-filtered-gate-cannot-block` | **folded** into the queued `a-cache-key-names-its-invalidators` as its third repository, above: a check scoped to changed files leaves its rule set out of its key. Not the commit-filter form already admitted |
| `p-75253ad330`, a data point offered for the queued experiment `remote-mutation-names-target-effect-reversal` | **recorded** in `experiments.md` *Run*, with the boundary that a probe which sends input is a write; the experiment stays queued |

## Refused by carriers' harvests, taken in at 0.0.27

Each proposal by its id; one offered for a note or an answered item is named by its id, so the ledger does not list that slug as refused. Two rows record where **the home disagrees** with the harvest's refusal.

| Candidate | Where it went |
|---|---|
| `ask-the-target-experience-before-correcting` | refused (`p-1b8559b29c`): requirements elicitation, not knowledge; its substance is answered by §15 in 0.0.27 (what the user sees stays theirs even when reversible) |
| `harness-time-limit-stops-a-background-service` | refused (`p-486cadec03`): harness-specific |
| `status-command-that-installs` | refused (`p-5243221d44`): tool-specific; not a form of the queued `steps-readable-by-a-permission-layer` either (a side effect, not a classifier misreading) |
| `probe-a-privilege-with-the-exact-operation` | refused (`p-7653b5934e`): a stand-in narrower than the real operation, covered by `test-double-fidelity`; the failure was a loud false red |
| `background-job-ignores-interrupt` | refused (`p-940bf2c979`): shell textbook behaviour |
| `interactive-tool-without-subcommand-hangs` | refused (`p-9f1754a08c`): tool trivia; the remedy is the maintainer-profile item `never-block-the-session-on-a-long-wait`. It counts toward the queued `a-batch-child-gets-no-terminal` |
| `measure-delay-with-broadband-not-tones` | refused (`p-a83f2dfa38`): domain textbook (time-delay estimation) |
| `browser-test-waits-for-first-paint` | refused (`p-b1d0825adf`): standard test synchronisation; a second repository met it at this release, and novelty fails either way |
| `parallel-agents-pick-the-same-number` | refused (`p-b42d2322a0`): answered by `parallel-session-id-allocation` and `derived-over-chosen-identifiers` |
| `formatter-run-by-a-parallel-agent` | refused (`p-d281eed90b`): answered by `parallel-agents-on-disjoint-files`, folded at 0.0.26 (format only the change) |
| `two-readers-of-one-source-correct-each-other` | refused (`p-e534c841e6`): its documentation-against-code half is the same event this carrier already gave `documented-defaults-drift-from-code`; not counted again |
| `render-explanations-from-the-test-simulator` | refused (`p-e9ae388290`): one occurrence; nothing beyond principle 14 |
| `p-10f85b5cb7`, an occurrence offered for the note `same-answer-or-refuse`, which stands | refused: already folded from this repository |
| `a-skip-reported-as-a-failure` | refused (`p-25adfe5ab5`): platform-specific; its general half is `a-check-must-be-seen-to-fail` and `report-coverage-before-findings` |
| `pull-a-database-and-its-log-in-one-read` | refused (`p-2e724dea78`): the embedded database's own backup guidance |
| `multi-line-messages-break-line-counts` | refused (`p-8b9b70ed39`): textbook log framing |
| `retry-budget-for-a-probabilistic-step` | refused (`p-96bc2c9474`): textbook binomial arithmetic |
| `p-9b3e664daf`, an occurrence offered for the note `sweep-the-rendered-extremes`, which stands | refused: from the repository that already extended the note; nothing new |
| `golden-image-reads-the-real-clock` | refused (`p-9e9ad8fdf2`): textbook: inject the clock into rendering tests |
| `device-suite-uninstalls-the-app` | refused (`p-bbd015e401`): platform-specific |
| `only-grows-shrinks-under-late-delivery` | refused (`p-c9c6fa4459`): one occurrence, recorded by its repository as its limit. The monotonic-logic literature its harvest cited is from memory (ASSUMPTION, not checked) and is not the reason |
| `p-f1d4188f8a`, an occurrence offered for the queued `steps-readable-by-a-permission-layer` | **the home disagrees** with its harvest's refusal: the carrier is right that its own repetition is not a second repository, but another carrier's edit, lost in a compound command a rule refused, is. Recorded as an occurrence, counted once with this carrier's 0.0.26 form; that sentence of artifact 4 now rests on three repositories, and the queued row stands |
| `p-0f36ede788`, an occurrence offered for the queued `a-cache-key-names-its-invalidators`, whose row stands | refused: same repository as the candidate's first occurrence, no new boundary; its open question moved through two equality-key runs instead |
| `a-vendor-power-manager-freezes-a-foreground-process` | refused (`p-29be475822`): platform-specific; reading the log first is textbook debugging |
| `line-breaking-strategy-pitfalls` | refused (`p-36e0bf31bd`): specific to one UI toolkit |
| `p-3d21b013e1`, an occurrence offered for the method's answered `assert-the-reason-not-only-the-outcome` | refused: already in principle 18 (assert the reason) |
| `check-measured-decisions-against-the-domain-literature` | refused (`p-43622a75fe`): covered by the method's section on the domain's own standards |
| `an-emulator-number-is-a-ceiling` | refused (`p-558d9bb6f6`): covered by `test-double-fidelity` (the local host as a double, folded) and the repository's own decision |
| `preview-the-build-on-real-records` | refused (`p-6f21be4805`): covered by principle 14 and `validate-each-transformation-run`; an occurrence |
| `an-audit-walk-excludes-nested-checkouts` | **the home disagrees** with its harvest's refusal as a single occurrence (`p-7361d45428`): another carrier offered the same mechanism, a recursive scan that counts a worktree nested in the repository; with it, **folded** into `absent-constraint-widens` with `recursive-scan-skips-nested-checkouts`, two repositories |
| `stale-roadmap-claims-cost-real-work` | refused (`p-77479dde43`): covered by principle 6 (a relayed claim is checked) and principle 16 |
| `redundant-comments-are-worse-than-lost-ones` | refused (`p-9ce95c6cd8`): covered by principle 5 (each fact lives once) |
| `weight-a-defect-count-by-usage` | refused (`p-b4a2a380c8`): analytics textbook |
| `p-bb38157dbc`, an occurrence offered for the method's admitted `a-filtered-gate-cannot-block` | refused: already admitted; an occurrence only. Its name-filtered test run with none of the new tests run is the zero-tests clause of `a-check-must-be-seen-to-fail` |
| `prose-language-rule-held-only-by-the-ratchet` | refused (`p-c8a0d1ee0b`): covered by principle 2 (rules are checked, not remembered); a count with no new boundary |
| `identical-needs-a-negative-control-in-end-to-end-tests` | refused (`p-eb559fe989`): covered by `a-check-must-be-seen-to-fail` (identical needs a negative control) |
| `a-red-from-a-build-failure-is-not-the-red` | refused again (`p-f43f143cdd`): refused at 0.0.26 under the same slug (principle 18, fail for the reason you expect) |
| `an-override-flag-must-not-satisfy-what-it-excuses` | refused (`p-f557e6fa1f`): textbook argument parsing; one occurrence |
| `undo-a-planted-violation-by-editing-forward` | refused (`p-f6cb6c9d22`): covered by principle 18 (undo by editing forward) |
| `audit-importable-under-main-guard` | refused (`p-0ebd0b0dbf`): ordinary engineering practice |
| `host-shell-traps` | refused (`p-1420579d20`): one machine's host friction, kept in the repository's root file; the same portability family as two other carriers' refusals |
| `ids-written-before-minted` | refused (`p-888bb155cc`): ids come from the minting command, and a format check cannot check provenance; the duplicate check is the backstop |
| `one-owners-deliverable-preferences` | refused (`p-aa28d761f6`): preferences of one owner for one deliverable; the general part was proposed separately |
| `word-counter-counts-markup` | refused (`p-c2c01db7f1`): one heuristic in one repository; checking a metric against what a person sees is principle 14 |
| `typesetting-engine-quirks` | refused (`p-f63866a6a4`): mechanics of one tool, kept in the repository's own area rules |
| `release-the-handle-before-deleting` | refused (`p-0d91291209`): platform-specific |
| `platform-affordance-first-triage` | refused (`p-271241e4dc`): a standard first triage step, one occurrence |
| `p-5fd3ec7890`, an occurrence offered for the queued `routine-tools-leave-the-tree-as-found`, whose row stands | refused: same carrier as the first occurrence, not the second repository the row lacks |
| `commit-split-rule-against-an-explicit-request` | refused (`p-7e93ae63c6`): repository-local as a candidate; its occurrence still counts as the second carrier of the commit-grouping change in `commit-granularity-by-context` |
| `prove-a-content-change-is-in-the-history-before-reverting` | refused (`p-8d242646f4`): specific to one repository's edit mode |
| `profile-before-optimising-per-frame-work` | refused (`p-c8a732b813`): textbook; not a second occurrence of `interleave-versions-in-one-window` |
| `every-request-has-a-timeout` | refused (`p-e4de9e38bc`): textbook |
| `one-entry-point-for-a-state-change` | refused (`p-f069b1157f`): a single entry point is textbook; the same shape as `kill-switch-reaches-every-path`, not an occurrence of it (no switch) |
| `hidden-is-not-deferred` | refused (`p-0dbcddd68d`): one front-end library's trigger semantics; ordinary practice |
| `p-161bdcd683`, an occurrence offered for the note `nested-partial-update-replaces`, which stands | refused: the lost update of a read-modify-write is textbook; the mask half is the note, measured by this carrier's run at this release |
| `shared-pool-pressure-reads-as-test-failure` | refused (`p-2355909d87`): environment-specific; principle 18 (fail for the expected reason) |
| `shared-mutable-default-carries-credentials` | refused (`p-2d8db87a40`): a textbook language pitfall; the credential-crossing consequence alone has one occurrence |
| `scripts-committed-without-exec-bit` | refused (`p-42cd3ebe8d`): trivial and repository-local |
| `cache-the-absence-of-a-lookup` | refused (`p-4553abdc95`): negative caching is textbook |
| `p-51cd17c789`, an occurrence offered for the note `derived-copy-goes-stale-silently`, which stands | refused: one occurrence, already the note's case (a set difference against a stale stored copy) |
| `wait-for-the-response-not-network-idle` | refused (`p-9974240ff8`): textbook; the automation tool's documentation discourages the idle wait. With another carrier's first-paint occurrence, two repositories; novelty fails either way |
| `error-message-names-the-right-remedy` | refused (`p-cd94f30172`): usability textbook; its credential half is in the `fail-closed-defaults` extension |
| `paginate-by-timestamp-skips-ties` | refused (`p-d939b1aadc`): keyset pagination needs a unique tiebreaker (textbook); the precision corollary went with `stored-timestamp-key-never-matches` |
| `p-e72a5d1152`, an occurrence offered for the note `test-double-fidelity`, which stands | refused: the note's check covers both directions, and a double that accepts less fails loudly |
| `scripts-run-under-an-older-system-shell` | refused (`p-0724a44a03`): platform trivia; its interpreter half is the one-line refusal of an old interpreter, fixed in 0.0.27 |
| `kernel-log-shows-the-current-boot` | refused (`p-370ca7c158`): one logging system's default |
| `write-permission-rules-match-nothing` | refused (`p-3ad6ecc680`): artifact 4 already says path rules for writes are accepted, never consulted, and warned about; an occurrence that confirms it |
| `one-place-defines-a-record-id` | refused (`p-4fdfbfa55b`): the method's single-source rule, and the id checker caught it |
| `a-warning-is-accepted-an-allowlist-is-justified` | refused (`p-a3b4441308`): already embodied in the bundle's override marker, which needs a reason and is listed on every run |
| `a-check-by-location-sweeps-in-new-kinds` | refused (`p-c5401dbd7f`): repository-local, and the failure was loud; a weak occurrence noted under the queued `a-new-case-must-reach-every-classifier`, not its second repository |
| `a-non-portable-utility-option-garbles-a-comparison` | refused (`p-11b5e09dda`): portable shell options are textbook |
| `a-binary-copied-over-a-run-binary-is-killed` | refused (`p-39841077c7`): platform code-signing behaviour, kept in the repository's own notes |
| `one-concern-commits-from-hand-staged-blobs` | refused (`p-428932cd54`): textbook atomic-commit practice |
| `place-a-score-by-the-rankings-own-method` | refused (`p-72d567bcea`): textbook (compare like with like; measure the noise floor first) |
| `concurrent-build-tool-runs-corrupt-its-lock` | refused (`p-85d5314336`): tool-specific |
| `tool-specific-traps-of-one-toolchain` | refused (`p-8f681c5178`): tool-specific |
| `patch-a-vendored-tool-at-build-from-its-pristine-source` | refused (`p-988df660e1`): established practice (a patch series applied at build time) |
| `ids-typed-by-hand-before-minting` | refused (`p-db9415fe19`): no harm shown; each was caught before commit, and the duplicate check is the backstop |
| `a-registry-filled-at-import-is-partial-during-import` | refused (`p-dcf54666cf`): idiom-level |
| `attribution-and-unasked-pushes-and-partial-gate` | refused (`p-f62a14e734`): occurrences of the maintainer's standing preferences and of `chain-the-commit-on-the-gate`; its attribution half counts toward the attribution change in `a-local-memory-is-not-a-handoff` |

## Taken out of the queue by the release 0.0.26

Method changes resting on one carrier's evidence were published, marked so, and are reviewed at the exit of the redesign's phase 1. Proposals that extend a method file share its name as a slug, so each is recorded below by its id.

| Candidate | Where it went |
|---|---|
| `splice-dry-run-lists-what-it-removes` | **fixed** in 0.0.26: the splice's report names every path it removes, dry run included, with a test |
| `review-each-carrier-in-execution-before-propagating` | **applied to the home's procedure**: `prompt-sync.md` Phase 2 opens with one read-only agent per carrier when a release changes wording an agent follows or a path a carrier references. The same reading applied to a procedure is the queued `dry-run-a-procedure-by-an-agent-before-release` |
| `taken-in-rows-wait-outside-build-inputs` | **applied to the home's procedure**: `prompt-sync.md`, building the release, step 5. At this release the five experiment rows parked in the roadmap went to `experiments.md` *Queued* |
| `find-carriers-by-searching-not-by-the-manifest` | **applied to the home's procedure**, from two proposals (the search of the disk, and of every branch): `prompt-sync.md` Phase 1 step 1, and `release.py carriers` lists every branch that holds a bundle, with a test |
| `gather-reads-the-remote-not-a-stale-checkout` | **applied to the home's procedure**, from two proposals: `prompt-sync.md` Phase 1 step 1 compares each carrier with its remote, takes the remote as the record, and works on a branch cut from it, never by a reset |
| `parallel-agents-get-disjoint-scratch` | **admitted into the method** with `a-delegated-agent-writes-into-the-callers-tree`, two repositories: the bootstrap's *Research does not end at Phase 2* gives a delegated agent that writes its own scratch directory outside the repository, and a destructive step there checks its target resolves inside it. The home's own rule is in `prompt-sync.md` |
| `a-delegated-agent-writes-into-the-callers-tree` | **admitted into the method**, see the row above |
| `parallel-agents-on-disjoint-files` | **folded** into the scratch-directory rule above, as a third repository's occurrence (an interactive client) |
| `a-filtered-gate-cannot-block` | **admitted into the method** with `chain-the-commit-on-the-gate`, two repositories: the close skill's step 9 runs the commit on the gate's own exit status, never through a filter or only under `pipefail`; the commit base follows in the redesign's phase 2 (`i-5ed7e8-3a8f87`). Kept apart from the queued `gate-sequence-stops-at-the-first-red-step` (*keep both*: a step never run, against a status ignored). The home's own enforcer is `i-5ed7e8-a4c2b2` |
| `chain-the-commit-on-the-gate` | **admitted into the method**, see the row above |
| `carrier-audits-delegate-bundle-shape-to-verify` | **admitted into the method**, evidence from several carriers: one sentence in artifact 9. Related: the redesign's audit library (`i-5ed7e8-3a8f87`) and the queued `a-shared-rule-has-one-enforcer-per-copy` |
| `check-a-relayed-claim-before-reporting-it` | **admitted into the method**, two repositories (the home's two relayed claims; a carrier's recorded lesson found false): principle 6, *a relayed claim is checked before it is repeated*. The close skill's step 3 says it of lessons |
| `tick-every-part-of-the-request` | **admitted into the method**: principle 15, the session loop's step 7, the *Done* checklist, the close skill's step 1. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `an-answers-free-text-overrides-its-options` | **admitted into the method**: one clause in principle 15, and the close skill's step 1. one carrier's evidence; reviewed at the exit of the redesign's phase 1. Undecidable for novelty (it may be default behaviour); the question goes to the skill evals of the redesign's phase 3 |
| `a-local-memory-is-not-a-handoff` | **admitted into the method**: a step 8 row, the closing question, the close skill's step 5 and `bundle.py memory-diff`. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `count-a-friction-by-searching-the-log` | **admitted into the method**: step 8, the *Done* checklist, the close skill's step 4 and `bundle.py count`; its last clause feeds principle 6. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `pause-means-pause` | **resolved by the maintainer's profile**, a standing preference, not a method rule; taken out of principle 15. The close skill's step 0 keeps its own boundary between pause and close |
| `art-goes-to-approval-as-drawn-proposals` | **resolved by the maintainer's profile**; taken out of principle 15. Its copy half is in `sweep-the-rendered-extremes` (measure before approval, waiting for a second repository) |
| `a-quick-deploy-stays-quick` | **resolved by the maintainer's profile**; taken out of principle 15 |
| `research-before-a-sensitive-choice-and-offer-the-middle` | **resolved by the maintainer's profile**; taken out of principle 15 |
| `never-block-the-session-on-a-long-wait` | **resolved by the maintainer's profile**; taken out of principle 15 |
| `a-light-observation-is-not-a-purge-order` | **resolved by the maintainer's profile**; taken out of principle 15 |
| `split-a-checked-file-and-the-check-goes-blind` | **folded** into `a-check-must-be-seen-to-fail`: the home's audits that went green on zero subjects after a layout moved were its second repository |
| `one-rule-two-readers-agree-on-the-verdict-not-the-refusal` | **folded** into `same-answer-or-refuse`, whose first remedy it is: a host tool that re-implemented an app's validation and diverged both ways was its second repository |
| `suspect-the-harness-first` | **folded** into `test-double-fidelity` as a boundary: the harness is a double, and "it passes alone" does not convict it, since pollution and real races pass alone too. Its second repository arrived with about ten infrastructure incidents. Luo et al. 2014 and Gyori et al. 2015 cited, not checked against the source |
| `a-check-must-be-seen-to-fail` | **extended**: zero subjects after a layout moved, zero tests run, a threshold's cut between a measured good and bad (its boundary sentence waits for a second repository), the idiomatic spelling of a plant; and the census run once, statically (*confirms*), into its *Evidence* |
| `absence-is-a-third-value` | **extended**: a template's empty default is absence, not a decision, into its *Evidence* |
| `a-default-scope-is-the-widest-one` | **extended**: a device task with no serial, the second tool the note lacked, into its *Evidence*. `bumping-a-monotone-counter-is-not-idempotent`, held for the same gap, was revisited: its queued row stands, lacking only its own second tool |
| `sweep-the-rendered-extremes` | **extended**, a second repository: a display assertion is not a fit check, and count every misfit; *done includes the sweep* and *measure before approval* into its *Evidence*, each waiting for a second repository |
| `test-double-fidelity` | **extended**: the surface a render draws on is a double (two occurrences), and the harness boundary folded above |
| `derived-copy-goes-stale-silently` | **extended**: a results file at a fixed path survives a failed run, and its reverse, into its *Evidence*. Related, still queued: `gate-reads-untracked-derived-state` |
| `derive-state-from-one-clock` | **extended**, a second repository and a new mechanism: under a user-settable clock, a counter that must not outrun real time needs an offset that only decreases; a rate limit only slows the leak. Literature: none consulted |
| `same-answer-or-refuse` | **extended**: the folded row above, into its *Evidence* |
| `a-cache-key-names-its-invalidators` | offered again with **the second repository it waited for** (a build stamp whose key left out the working tree's diff); the literature step was not run in this release, so its queued row stands, lacking the literature and a decision on whether it is the boundary of `derived-copy-goes-stale-silently` |
| `steps-readable-by-a-permission-layer` | two new forms merged into its queued row (a global option before the subcommand passes a prefix deny; a compound command with one denied part is refused whole); both are written into artifact 4. The row stands, lacking a second occurrence of one form |
| `isolated-review-by-default` | **reopened as a queued candidate**: the recorded answer rests on a card-driven review of one diff, and whole-branch reviews after a multi-task plan found a defect the suite passed in each of about a dozen runs. It lacks cost figures and a card-driven run on the same branches. The boundary of the measurement is stated in principle 19 |

**Proposals to a method file, by id** (not slugs: the ledger lists none of them).

| Proposal | Where it went |
|---|---|
| `p-10e696d3ae`, extends `prompt-bootstrap`: a detector for a procedure done twice | **admitted into the method**: step 8's row and the close skill's step 4 (`bundle.py count`). one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-1bf4aedf89`, extends `prompt-bootstrap`: a scratch directory for a delegated agent | **admitted into the method** with `parallel-agents-get-disjoint-scratch`, above |
| `p-207be9eaf6`, extends `prompt-bootstrap`: count frictions by searching | **admitted into the method**: step 8, the *Done* checklist, the close skill's step 4. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-53b1e16730`, extends `prompt-bootstrap`: an index-completeness row and check | **admitted into the method**: step 6's table and artifact 9; the redesign's phase 2 audit library is to enforce it. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-5a33d7a5d9`, extends `prompt-bootstrap`: open device questions at close | **admitted into the close skill's step 6 only**; kept out of the session loop for its budget. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-b333c94ddc`, extends `prompt-bootstrap`: a route for what lives only in local memory | **admitted into the method**: step 8's row, the closing question, the close skill's step 5. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-f0576912a0`, extends `prompt-bootstrap`: the boundary of the review-on-request measurement | **admitted into principle 19 only**; kept out of the session loop for its budget. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-532edbd1fc`, extends `prompt-context`: *Review* and *Learned* in the changelog entry | **admitted into the method**: artifact 5, and the close skill's step 3 (`bundle.py new entry`). one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-94fc43c6d1`, extends `prompt-context`: see the red after the code exists | **admitted into the method**: principle 18. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-c8cc171d0c`, extends `prompt-context`: *Cards relied on*, and the card step mapped into a winning host template | **admitted into the method**: artifact 5, principle 19, the bootstrap's Phase 4. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-eaf9e35bde`, extends `prompt-context`: deny per destructive subcommand | **admitted into artifact 4 only**; kept out of the session loop's *Working safely* for its budget. Also an occurrence for `steps-readable-by-a-permission-layer`. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-a5a8909619`, extends `prompt-harvest`: read every form of the human's input | **admitted into the method**: the harvest's Phase 1 step 1 and its pre-flight, its privacy sentence kept. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |
| `p-ed4b1f83fc`, extends `prompt-update`: keep only the top-level `incoming/README.md` | **admitted into the method** as a defect fix: the update's step 4. one carrier's evidence; reviewed at the exit of the redesign's phase 1 |

**The closing review** (`sources/README.md` §4), over the notes this release touched. No note was admitted, so none is protected. *Keep both*: the method's gate rule and the queued `gate-sequence-stops-at-the-first-red-step` (a status ignored, against a step never run). *Folds*: three queued rows into `a-check-must-be-seen-to-fail`, `same-answer-or-refuse` and `test-double-fidelity`, each counted once, in that note. Every touched note's *Evidence* still names an experiment never run, and each stays *queued* in `experiments.md`; the census of `a-check-must-be-seen-to-fail` ran statically, and its executed run stays queued. No `confidence` changed.

## Refused by carriers' harvests, taken in at 0.0.26

| Candidate | Where it went |
|---|---|
| `a-red-from-a-build-failure-is-not-the-red` | refused: already in the method (principle 18, fail for the reason you expect) |
| `fetched-content-carries-instructions` | refused: prompt injection, platform-level and already known |
| `p-32fee93dc6`, an occurrence offered for the note `derive-state-from-one-clock`, which stands | refused: one occurrence, specific to one platform's aggregate API; at most a footnote |
| `pixel-identical-capture-proves-no-change` | refused: already a method rule (a change meant to change nothing); an occurrence with no new boundary |
| `p-9cb706ce2e`, an occurrence offered for the note `copied-instruction-claims-its-origin`, which stands | refused: the pre-flight caught it as designed, and the candidate is already answered |
| `p-cacafbf6a4`, an occurrence offered for the note `unrunnable-system-moves-the-gate`, which stands | refused: narrow and platform-specific; already implied by the note |
| `p-cb1ba3bc96`, extends `prompt-bootstrap` | refused: repository-specific; the method's own example names no device, the foreign name was added in this repository's skill |
| `expected-value-copied-from-a-wrong-comment` | refused: the test-oracle problem is textbook; a single occurrence |
| `verify-an-api-against-the-compiled-artefact` | refused: already the primary-sources rule; nothing new |
| `apply-mutations-one-at-a-time` | refused: textbook mutation-testing practice |

## Taken out of the queue by the release 0.0.24

| Candidate | Where it went |
|---|---|
| `splicing-an-old-layout-carrier-keeps-what-gather-found` | **fixed** in 0.0.24: the splice turns the rows a carrier added over its release into proposals before the tables go, and refuses when that release has no tag. Seen again at 0.0.24: two carriers on an untagged release were converted by hand, their added rows accounted for by `lost` first |
| `occurrence-of-documented-default-values-drift` | **merged** into `documented-defaults-drift-from-code` as a second occurrence, from a second repository |
| `validate-each-transformation-run` | **extended**: an up-to-date check that compared text rather than bytes, into its *Evidence* |
| `absence-is-a-third-value` | **extended**: a default of an empty list that turned "not reached" into "nothing found", into its *Where it came from* |
| `copied-instruction-claims-its-origin` | **extended**: a bundle folder copied whole with its source's identity and records, into its *Evidence* |
| `absent-constraint-widens` | **extended**: an equivalence suite whose world held no case that tells two designs apart, into its *Evidence* |
| `an-update-is-driven-by-the-new-side` | offered again with nothing new; its queued row stands |
| `a-repair-request-runs-once-per-load` | offered again with nothing new; its queued row stands |
| `local-host-is-a-test-double-of-the-production-host` | offered again with nothing new; already folded into `test-double-fidelity` |

## Refused by carriers' harvests, taken in at 0.0.24

| Candidate | Where it went |
|---|---|
| `isolated-review-by-default` | refused: already in the method |

## Taken out of the queue by the release 0.0.23

| Candidate | Where it went |
|---|---|
| `test-double-fidelity` | **extended**: two occurrences offered by two repositories (a fixture that lacked what the real input carries; a local host that differs from production) went into its *Evidence* |
| `local-host-is-a-test-double-of-the-production-host` | **folded** into `test-double-fidelity` as an occurrence |
| `same-answer-or-refuse` | **extended**: the subset reader that refuses what the full parser types differently, measured, into its *Evidence* |
| `validate-each-transformation-run` | **extended**: the byte-for-byte proof of a table migration, into its *Evidence* |
| `follow-the-procedure-literally-to-review-it` | **admitted into the method**, with `execute-the-procedure-to-review-it`: two repositories; the session loop's verify step says to run a changed procedure literally |
| `execute-the-procedure-to-review-it` | **admitted into the method**, see the row above |
| `privileged-call-inside-the-host-gesture` | offered again by the same kind of repository with nothing new; its queued row stands, still lacking a measurement on the target runtime |

## Refused by four carriers' harvests of 2026-09-22, recorded by the release of 2026-09-24

Offered by those carriers' records and not written as candidates, with the reason, so the next
harvest does not offer them again with the same gap.

- **A rename applied at a definition and not at its use sites is a broken state that reaches
  production.** Refused independently by two carriers: the default tooling already catches it —
  a type checker named it in one line. What failed was that the gate never ran that checker,
  which is `gate-sequence-stops-at-the-first-red-step`, and this is one of its occurrences
  rather than a claim of its own.
- **A suppression comment placed on the closing line of a multi-line call silences nothing and
  reports itself unused.** Language-specific, and the type checker already reports it. Worth a
  repository rule, not a note.

## Taken out of the queue by the release of 2026-09-24

| Candidate | Where it went |
|---|---|
| `parallel-session-id-allocation` | **answered by the method**: records written by parallel sessions (decisions, roadmap items, session entries) take `<kind>-<repo6>-<content6>` ids minted by `bundle.py id`, so no session needs to see another's numbers. Its evidence — a parallel session's rows already held nine ids — is the occurrence the change cites |

## Taken out of the queue by the release of 2026-09-23

Nine candidates left this table in that release, and two were merged into one row of `candidates.md`.

| Candidate | Where it went |
|---|---|
| `correction-lands-where-the-rule-is-enforced` | **admitted into the method**, principle 6: a retraction reaches the copy that is loaded and a superseded decision's own row. The second repository was the one it waited for, and it extended the claim from guardrails to decision records |
| `a-safe-degrade-must-know-whether-its-target-should-exist`, `a-check-whose-subject-is-prose-is-one-translation-from-vacuous`, `a-completion-check-states-its-negative` | **folded** into `a-check-must-be-seen-to-fail` as a named form, *a check over zero subjects*, with all three measured occurrences. A new occurrence of an existing claim extends its note |
| `incoming-cannot-be-checked-empty-while-the-bundle-ships-a-file-into-it` | **fixed**: the rule is now *empty except its own `README.md`*, in `incoming/README.md` and `prompt-update.md` |
| `the-set-declares-a-version-the-changelog-does-not-reach` | **fixed**: Method changelog rows 17–21 written from the bundle roadmap's *Done* entries; row 17 says it is a number nobody holds |
| `a-principle-can-have-no-subject-in-a-carrier` | **already in the method**: the triage verdict *Does not apply* is exactly this. What was missing was one sentence — it is not `declined`, and it is re-triaged the day the subject appears — now in `prompt-update.md` §*The triage* |
| `skills-have-two-declared-homes-in-one-bundle` | **fixed** in `layout.md`: a repository served by one assistant keeps one skills folder, the one that assistant loads; `.agents/skills/` is the source only when several assistants read it |

## Taken out of the queue by the release of 2026-09-22

Six candidates left this table in that release. Where each one went, so that a later harvest
offering it again can see it was answered rather than lost.

| Candidate | Where it went |
|---|---|
| `a-replica-inherits-the-tree-it-is-built-in` + `rebuild-ci-to-reproduce-ci` | **admitted, as one note**: `reproduce-the-checkout-not-only-the-environment`. The first was the second occurrence the second had been waiting for, and both are measured |
| `default-scope-is-the-widest-one` | **admitted**: `a-default-scope-is-the-widest-one`. Two measured occurrences in one tool, two different mechanisms; the boundary says so |
| `a-constraint-needs-a-second-subject-to-be-visible` | **folded** into `absent-constraint-widens` as a boundary: a new boundary of a claim extends its note |
| `a-cap-that-hands-off-is-not-a-cap-that-exempts` | **folded** into `abuser-controlled-exemption` as a boundary. It keeps its open half — what the human queue behind the hand-off is worth — which is `detect-only-control-is-its-queue`, still a candidate |
| `assert-the-reason-not-only-the-outcome` | **folded into the method**, principle 18: a mutation test asserts the *reason* a check reported, not only which item it named |
| `fingerprint-fixes-its-collation` | **discarded**: already in `ratchet-in-a-pinned-environment`, with both of its values. Two carriers reached that verdict independently in the same harvest |

## Refused by the harvest of 2026-09-22, second pass

Offered by the record of that period and not written as candidates, with the reason, so the
next harvest does not offer them again with the same gap.

- **A fingerprint whose file order depends on the locale is not a fingerprint.** Already the
  third repository's evidence in `ratchet-in-a-pinned-environment`, with both of its values.
  Nothing here adds to it.
- **A version number stamped by a run that then failed is spent, and is never reissued.**
  Arrived with the release that records it; the run happened in the carrier the release was
  authored in, not here. Counting it here would be the same occurrence twice. It stays with
  that carrier's harvest, and it is close enough to `parallel-session-id-allocation` that the
  two may be one claim about monotone ids.
- **A digest over an empty input returns a well-formed value indistinguishable from an
  answer.** Same reason: it is in the release's own record, not in this repository's. Worth
  offering by the carrier that met it, where it would extend `report-coverage-before-findings`.
