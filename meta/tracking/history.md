# History — where each candidate went when it left the queue

Newest first. One section per release or harvest; each row says where the candidate went, so it
is not offered again as a fresh idea. The queue itself is `candidates.md`. Name a candidate by its
slug in backticks, in the first cell of a table row: that is how `release.py intake` recognises one
answered here, and how the build lists it in the ledger, `INDEX.md`. Nothing is dropped by age; a
row here is a release's decision, with its reason.

## Refused by carriers' harvests, taken in at 0.0.27

| Candidate | Where it went |
|---|---|
| `ask-the-target-experience-before-correcting` | refused: requirements elicitation; the brainstorming skill already asks purpose first; kept as working-style evidence |
| `harness-time-limit-stops-a-background-service` | refused: harness-specific |
| `status-command-that-installs` | refused: tool-specific; at most an occurrence for steps-readable-by-a-permission-layer |
| `probe-a-privilege-with-the-exact-operation` | refused: one-line instance of testing the real dependency; close to test-double-fidelity |
| `background-job-ignores-interrupt` | refused: POSIX textbook behaviour |
| `interactive-tool-without-subcommand-hangs` | refused: tool trivia; the remedy is the answered never-block-the-session-on-a-long-wait |
| `measure-delay-with-broadband-not-tones` | refused: domain textbook (time-delay estimation) |
| `browser-test-waits-for-first-paint` | refused: known; standard test-synchronisation practice |
| `parallel-agents-pick-the-same-number` | refused: already answered by parallel-session-id-allocation and derived-over-chosen-identifiers |
| `formatter-run-by-a-parallel-agent` | refused: already in the method: format only the files in the change; parallel agents on disjoint files |
| `two-readers-of-one-source-correct-each-other` | refused: already known; close to the answered verify-an-api-against-the-compiled-artefact and the queued adversarial-review candidate |
| `render-explanations-from-the-test-simulator` | refused: one occurrence; no claim stronger than look at your outputs |
| `scripts-run-under-an-older-system-shell` | refused: platform trivia; the bundle's hook already finds a new enough interpreter |
| `kernel-log-shows-the-current-boot` | refused: tool trivia, true of one logging system only |
| `write-permission-rules-match-nothing` | refused: the bundle's method already states it |
| `one-place-defines-a-record-id` | refused: single source of truth is already the method's rule, and the bundle's id checker caught it |
| `a-prose-rule-loses-to-a-tool-default` | refused: already admitted as correction-lands-where-the-rule-is-enforced; an occurrence only |
| `a-warning-is-accepted-an-allowlist-is-justified` | refused: already embodied in the bundle's override marker, which requires a reason and is listed on every run |
| `a-check-by-location-sweeps-in-new-kinds` | refused: repository-local, and nothing beyond a-check-must-be-seen-to-fail |
| `summaries-of-reference-pages-invent-syntax` | refused: already admitted as check-a-relayed-claim-before-reporting-it; an occurrence only |
| `same-answer-or-refuse` | refused: already folded from this repository |
| `a-skip-reported-as-a-failure` | refused: platform-specific; its green-that-measured-nothing half is already a-check-must-be-seen-to-fail and report-coverage-before-findings |
| `pull-a-database-and-its-log-in-one-read` | refused: the embedded database's own backup guidance |
| `multi-line-messages-break-line-counts` | refused: textbook log framing |
| `retry-budget-for-a-probabilistic-step` | refused: textbook binomial arithmetic |
| `sweep-the-rendered-extremes` | refused: an occurrence from the repository that already extended this note; nothing new |
| `golden-image-reads-the-real-clock` | refused: textbook: inject the clock into rendering tests |
| `device-suite-uninstalls-the-app` | refused: platform-specific |
| `only-grows-shrinks-under-late-delivery` | refused: covered by monotonic-logic work on reordering (the CALM line; cited from memory, not checked) |
| `steps-readable-by-a-permission-layer` | refused: same repository again, which cannot be the queued form's second occurrence; the form is already in artifact 4 |
| `a-cache-key-names-its-invalidators` | refused: same repository as the candidate, no new boundary |
| `a-vendor-power-manager-freezes-a-foreground-process` | refused: platform-specific; reading the log first is textbook debugging |
| `line-breaking-strategy-pitfalls` | refused: specific to one UI toolkit |
| `assert-the-reason-not-only-the-outcome` | refused: already in the method: principle 18, assert the reason |
| `check-measured-decisions-against-the-domain-literature` | refused: covered by the method's section on the domain's own standards |
| `an-emulator-number-is-a-ceiling` | refused: covered by the answered `local-host-is-a-test-double-of-the-production-host` and the repository's own decision |
| `preview-the-build-on-real-records` | refused: covered by principle 14 and `validate-each-transformation-run`; an occurrence |
| `an-audit-walk-excludes-nested-checkouts` | refused: tool-specific; a single occurrence |
| `stale-roadmap-claims-cost-real-work` | refused: covered by principle 6 (a relayed claim is checked) and principle 16 |
| `redundant-comments-are-worse-than-lost-ones` | refused: covered by principle 5 (each fact lives once) |
| `weight-a-defect-count-by-usage` | refused: analytics textbook |
| `a-filtered-gate-cannot-block` | refused: already admitted; occurrence only |
| `prose-language-rule-held-only-by-the-ratchet` | refused: covered by principle 2 (rules are checked, not remembered); an occurrence count with no new boundary |
| `identical-needs-a-negative-control-in-end-to-end-tests` | refused: covered by `a-check-must-be-seen-to-fail` (identical needs a negative control) |
| `a-red-from-a-build-failure-is-not-the-red` | refused: already answered: principle 18, fail for the reason you expect |
| `an-override-flag-must-not-satisfy-what-it-excuses` | refused: textbook argument parsing; a single occurrence |
| `undo-a-planted-violation-by-editing-forward` | refused: covered by principle 18 (undo by editing forward) |
| `audit-importable-under-main-guard` | refused: ordinary engineering practice |
| `host-shell-traps` | refused: host friction of one machine, kept in the repository's root file |
| `ids-written-before-minted` | refused: already covered, ids come from the minting command and a format check cannot check provenance |
| `one-owners-deliverable-preferences` | refused: preferences of one owner for one deliverable; the general part is proposed separately |
| `word-counter-counts-markup` | refused: one heuristic in one repository; checking a metric against what a person sees is not new |
| `typesetting-engine-quirks` | refused: mechanics of one tool, kept in the repository's own area rules |
| `release-the-handle-before-deleting` | refused: platform-specific |
| `platform-affordance-first-triage` | refused: a standard first triage step, one occurrence |
| `routine-tools-leave-the-tree-as-found` | refused: same carrier as the first occurrence, not the second repository it lacks |
| `commit-split-rule-against-an-explicit-request` | refused: repository-local, recorded in its roadmap |
| `prove-a-content-change-is-in-the-history-before-reverting` | refused: specific to one repository's edit mode |
| `profile-before-optimising-per-frame-work` | refused: textbook; not a second occurrence of interleave-versions-in-one-window |
| `every-request-has-a-timeout` | refused: textbook |
| `one-entry-point-for-a-state-change` | refused: novelty (single entry point is textbook); overlaps kill-switch-reaches-every-path in shape |
| `hidden-is-not-deferred` | refused: one front-end library's trigger semantics; the general form is ordinary practice an agent already knows |
| `nested-partial-update-replaces` | refused: the lost update of a read-modify-write is textbook (P4); the mask half is the existing note, tested by this harvest's experiment |
| `shared-pool-pressure-reads-as-test-failure` | refused: environment-specific; the general part is answered by a-red-from-a-build-failure-is-not-the-red |
| `shared-mutable-default-carries-credentials` | refused: the mechanism is a textbook language pitfall that an agent already knows; the credential-crossing consequence alone does not pass the generality test without a second occurrence |
| `scripts-committed-without-exec-bit` | refused: trivial and repository-local |
| `cache-the-absence-of-a-lookup` | refused: negative caching is textbook |
| `derived-copy-goes-stale-silently` | refused: one occurrence, and it is already the note's case (a set difference against a stale stored copy) |
| `wait-for-the-response-not-network-idle` | refused: textbook; the browser-automation tool's documentation already discourages the idle wait for tests |
| `measure-a-ui-change-as-a-task` | refused: textbook usability practice (task-based measures, cognitive walkthrough); the working-style part belongs to the maintainer's profile |
| `error-message-names-the-right-remedy` | refused: textbook usability guidance on error recovery; the credential half is in the fail-closed-defaults extension |
| `paginate-by-timestamp-skips-ties` | refused: textbook (keyset pagination needs a unique tiebreaker); the store-precision corollary belongs to stored-timestamp-key-never-matches |
| `test-double-fidelity` | refused: the note's check already covers both directions, and a double that accepts less fails loudly, not silently |
| `a-non-portable-utility-option-garbles-a-comparison` | refused: tool-specific and textbook (portable shell options) |
| `a-binary-copied-over-a-run-binary-is-killed` | refused: platform-specific code-signing behaviour; it belongs in the repository's own troubleshooting notes, where it is |
| `one-concern-commits-from-hand-staged-blobs` | refused: textbook atomic-commit practice; a repository process item |
| `place-a-score-by-the-rankings-own-method` | refused: textbook (compare like with like; measure the noise floor before comparing) |
| `concurrent-build-tool-runs-corrupt-its-lock` | refused: tool-specific |
| `tool-specific-traps-of-one-toolchain` | refused: tool-specific |
| `patch-a-vendored-tool-at-build-from-its-pristine-source` | refused: established practice (patch series applied at build time) |
| `ids-typed-by-hand-before-minting` | refused: no harm shown: each was caught before commit, and a well-formed hand-typed id only risks a collision the duplicate check reports |
| `a-registry-filled-at-import-is-partial-during-import` | refused: too small and idiom-level |
| `attribution-and-unasked-pushes-and-partial-gate` | refused: occurrences of rules already in the user's instructions and of answered items (chain-the-commit-on-the-gate, a-filtered-gate-cannot-block) |

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
