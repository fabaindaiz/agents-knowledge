# Session log

**What each working session in this repository did, newest first.** One entry per session, in the
method's own format, started with `python3 .agents/tools/bundle.py new entry "<title>" --write`.
It is the record a friction count searches (`bundle.py count`), so a friction that is not written
here is a friction nobody can count later.

The hand-off each close replaces lives beside this file, in `roadmap-states.md`: that file holds the
states, this one holds what happened on the way. Sessions before 2026-11-24 are recorded only as
those states and in `meta/tracking/history.md`.

## 2026-11-25 · s-5ed7e8-d5fb84 — 0.0.35 cut, the owner's nine decisions, and the splice paused mid-way

**What.** `release/0.0.35` went to `main` once the host's guard could read its own script again (the folder's access had been withdrawn by the operating system). Two items the owner approved were built: the push as a step of its own in the close and the release procedure, and the two table parsers merged into one (compared on every table row in the home: no difference). The eight recorded privacy false positives were fixed test-first. A delegated study read one carrier's planning, review and decision practices against the bundle, and a second researched documentation practice; both are dated documents. The owner walked nine decisions one at a time (`d-5ed7e8-cbb288` to `d-5ed7e8-5dc49a`). 0.0.35 was cut and tagged here and in the template; the 0.0.36 plan and a private-channel pilot entered the roadmap. Three delegates spliced 0.0.35 into sixteen carriers until the owner paused; three carriers are committed, thirteen are spliced and uncommitted, and their worktrees were moved out of the temporary folder.

**Areas.** `sources/bundle/tools/bundle.py`, `sources/bundle/method/skills/close/SKILL.md`, `sources/bundle/CHANGELOG.md`, `meta/method/prompt-sync.md`, `meta/tests/test_bundle.py`, `meta/decisions.md`, `meta/reviews/` (three documents, one merged from its branch), `meta/roadmap.md`, `meta/archive/`, `.agents/` (generated), one home proposal.

**Why.** The owner's requests in order: push the branch; say what is left and prepare a release with the pending changes; apply everything and consider their own proposals (spec-driven development, work across machines, standard development steps, usage evidence, and anything forgotten); study one carrier's process learnings deeply; research a documentation skill; then pause the waiting work; then close.

**Architecture.** ✅ Complies. The release was generated from `sources/`; carriers were written only in worktrees outside them; nothing was pushed into a carrier.

**Cards relied on, and the checks that ran.** none consulted by card; `release.py check` passed before every commit, the tool suite passed (402 tests), `privacy --tracked` reports no failure, `docs-drift` warns that the root file did not change with the tool (it describes nothing the change made false: docs-unchanged: the privacy allowance's documented placement still holds).

**Review.** An isolated review of the release's tool changes, by a delegate in a fresh context given the diff, at the close: two HIGH (any domain noun after a number was skipped; a release word excused a real dependency pin), three MEDIUM (a formatted count in a code span read as a hash; *tech* excused every noun; `checkout` dropped from the domain list), one LOW (a relative `XDG_STATE_HOME` honoured), and three tests that pinned nothing. All fixed test-first with its inputs as tests, and **0.0.35 was cut again** at the owner's word: the first tag had reached no remote, so no published release carries the wider exceptions. Clean: the allowance terminator and the merged parser (fuzzed, no difference on rows a caller passes).

**What went wrong on the way.** The researcher agent was briefed to write a file it cannot write, and returned a short report from memory (home proposal `p-920709a5b4`). The previous session's worktrees had been kept in the session's temporary folder and were gone, with one carrier's uncommitted splice; this session's were moved out at the pause. An unquoted list variable in zsh was passed as one argument again, the third incident, in the same session the ladder gained a line about it. A decision row was refused by the privacy check for a minor version after *at*, reworded. Two of the new tests asserted a behaviour the old parser never had and were corrected against it. The first fix of the false positives was wider than each case it answered, and the suite could not see it: every exception's test asserted only the false positive passing, never the leak beside it failing; the review found it.

**What was left undone.** Thirteen carriers spliced and uncommitted, their register and align not run (the hand-off); two carriers' 0.0.34 harvest branches only local; the 0.0.36 plan (`i-5ed7e8-516d7a`); the spec pilot's carrier, the owner's to name.

**Deviation from the plan.** none.

**Not verified.** The three committed carriers' gates were run by their delegates, not re-run here; the thirteen uncommitted ones did not finish theirs.

**Measured.** Delegations, estimate then actual: a carrier study 40–60 min and 150k tokens, about 10 min and 276k; a documentation research 30–45 min and 120k, about 4 min and 112k; a failed researcher, about half a minute and 16k; the splice delegates, 20–45 min, still running at about 45 min when stopped. Time again too high by four to twelve times; tokens near or above.

**Learned.** *General:* a delegate's tool limits beat its brief (a read-only agent asked to write a file); work a session must be able to resume does not belong in a folder the system clears; a rule written as text for an agent's own shell habit did not hold within the hour it was written. *Local:* the researcher's output, routed to the home proposal; the worktree location and the zsh habit, to the roadmap's process items. Captured: 3 learnings, 4 frictions (the guard's lost file access, the researcher's write, the temporary worktrees, the zsh list). Nothing needs you beyond the items named.

## 2026-11-25 · s-5ed7e8-c1ada9 — The harvest of this machine, the cut of 0.0.34 and its splice

**What.** The transcripts only this machine holds were harvested in sixteen carriers, one owner counted as one source, on branches based on the other machine's unmerged harvest branches. The home took in 90 proposals and a delegated agent added the 71 occurrences among them to their rows and notes, narrowing one note's boundary. Six tool fixes landed test-first (credential redaction and shell escapes in `turns`, suffixed legacy decision ids, labelled harvest gaps with a frontier rule, a later harvest named by `gather`, no quote for `overlaps`), the close skill gained the owner's two-kind pause, and the changelog announces the product-noun check's removal first. 0.0.34 was cut and tagged; three delegated agents spliced it, with 0.0.33, into fifteen carriers; sixteen align. The template was refreshed and tagged. A research document on spec formats was written on its own branch and published as a private page.

**Areas.** `sources/bundle/tools/bundle.py`, `meta/tools/release.py`, `meta/tests/`, `sources/bundle/method/`, `sources/bundle/CHANGELOG.md`, `sources/bundle/README.md`, eleven active notes, `meta/tracking/`, `meta/roadmap.md`, `meta/archive/`, `meta/reviews/` (on its own branch), `.agents/` (generated), two home proposals.

**Why.** The owner's brief: push what only this machine held, harvest it, cut 0.0.34 only on their word, and splice 0.0.33 and 0.0.34 together into the carriers reachable here.

**Architecture.** ✅ Complies. Every carrier was written only in a worktree of its own repository, never in a checkout with someone's work.

**Cards relied on, and the checks that ran.** `release.py check` passed before each commit and the cut; `bundle.py verify` reports 0.0.34; `align` reports sixteen aligned; the tool suite passes but for three usage tests that fail on a clean `HEAD` on macOS (`i-5ed7e8-c0341d`).

**Review.** none in fresh context; the phase-2 agents read each carrier's own definitions beside the release and fixed five conflicts in execution or broken references, listed in `i-5ed7e8-cfd663`.

**What went wrong on the way.** An unquoted list variable in zsh passed sixteen paths as one argument, twice; the second time the write tool reported fifteen carriers missing, and the zsh-native fix was refused by the host's guard (home proposal `p-069d110c27`). One carrier was missed by the first harvest pass and found only by listing every carrier's frontier; `turns` then printed a shell escape's output, a remote included, as a human turn, fixed the same hour. A merge agent's report and a test run read as green while three tests failed on this platform before any change.

**What was left undone.** One carrier's update is uncommitted on a red gate it did not cause (`i-5ed7e8-88cd88`); nothing is pushed or merged (`i-5ed7e8-151456`); the `lineage` field (`i-5ed7e8-25fd85`); the design of `i-5ed7e8-9ef5d1` and the spec-program idea wait on the owner.

**Not verified.** Gates reported unproven in five carriers, where a worktree could not build its own environment; one carrier's typecheck and lint were not reproduced at all.

**Measured.** Three phase-2 delegations were announced at 300 to 500 thousand tokens each and used about 180 thousand each: too high by two to three times, the same direction as `i-5ed7e8-045188`'s pairs. The merge delegation used about 190 thousand.

**Learned.** *General:* a check made to read more finds debt that was always there (a decision row skipped in silence now read with an empty status); a harvest needs every carrier's frontier listed before it is called complete. *Local:* the zsh construct, routed to the home proposal; the two pauses, into the close skill. Captured: 3 learnings, 2 frictions (the zsh list, the missed carrier). Nothing needs you beyond the items named.

## 2026-11-24 · s-5ed7e8-2afb2c — The close that followed the 0.0.33 cut

**What.** 0.0.33 was cut, tagged and pushed; then eight further commits landed on `main` after the tag. The
owner walked the five unconfirmed reasons that still bind and decided all five, which queued eight items; six
were built the same day and two were answered by counting instead. The tools gained: a `.gitignore` written
beside the usage store and never outside the tool's own folder, a non-zero exit when `changelog --since` is
asked for a version older than the oldest section kept, a decisions count that excludes what no person can ever
confirm, and a check that resolves note slugs cited in the tracking tables. The product-noun check over a note's
cues and its hand-seeded list were removed. The worktree rule now builds a hermetic environment where that is
cheap. The home's own proposals were written and the eight it had already received were pruned. This file was
created: the home had never named its session log.

**Areas.** `sources/bundle/tools/bundle.py`, `meta/tools/release.py`, `meta/tests/`, `sources/bundle/method/`,
`meta/method/prompt-sync.md`, one active note, `meta/roadmap.md`, `meta/decisions.md`, `meta/reviews/`,
`meta/archive/`, `.agents/` (generated) and `.agents/carrier.toml`.

**Why.** The owner asked to finish everything that depends on this machine so the next release can be cut from
the other one, and, during the walk, that the questions behind two of the decisions be answered rather than the
rows merely confirmed. Two of their own proposals were dictated in the same session.

**Architecture.** ✅ Complies. One departure worth naming: the slug check was specified in the roadmap as living
in the tool every carrier runs, and it was built in the home's own check instead, because a carrier holds neither
the tracking tables nor the note sources. The item was rewritten to say so.

**Cards relied on, and the checks that ran.** `release.py check` (passed), `release.py build`, 391 tests (one
skipped, none failing), `bundle.py privacy --commits` and `--tracked` (0 FAIL), `bundle.py trailers` (clean),
`bundle.py ids` (0 errors), `bundle.py decisions`, `bundle.py docs-drift` (3 warnings, see below),
`bundle.py close --base` (every check passed).

**Review.** Four reviews in fresh context, plus one final review of the whole branch, all by delegates that had
not written the code. They found, in order of severity: a `.gitignore` holding `*` that a resolved symlink could
place inside an unrelated repository, silencing every new file in it; a claim pattern that would have failed the
build on the ordinary phrase *not admitted as a note*; a `continue` that silently stopped checking broken paths
on one class of row; records that stated the opposite of the code; and a delegate that deleted a roadmap item
instead of closing it. All were fixed before the push. Deferred: a changelog line that still describes the
removed check, which belongs to the next cut's section.

**What went wrong on the way.** A loop whose directory change failed silently edited and committed this
repository's own carrier file on the default branch; a push guard caught it, nothing left the machine, and the
rule it broke was being written into the same release. Two note slugs were written into a tracking table from
memory and did not exist. The privacy check failed twice more on its own prose, once on a repository name that
should never have been written and once as a false positive on an ordinary English word. `new entry --write`
crashed with a traceback rather than refusing in one line, because this repository had never named a log. Two
estimates of delegated work were wrong by a factor of ten to fifteen, in the direction of caution.

**What was left undone.** The splice of 0.0.33 into any carrier, by the owner's decision, to go with 0.0.34. The
twenty-nine reasons an agent wrote under decisions a person accepted. Six candidates a review says could be
admitted at the next intake, and three defects the queue itself carries. One orphan slug that the new check warns
about on every run. Three documents `docs-drift` flags as unchanged while the tools moved: the root instruction
file, the bundle's README and the manifest — none of their claims was found false, but none was re-read in full.

**Not verified.** That the harvest did not read this repository's own sessions between 2026-10-05 and 2026-11-23.
The frontier was advanced and that span declared a gap on that reading; the evidence lives outside the
repository, and the final review confirmed the repository can neither support nor contradict it. The gap was
declared wide on purpose: being wrong costs a re-read, not a loss.

**Measured.** Four delegations were announced with an estimate and compared on return: two bounded read-and-delete
tasks finished in about one and a half minutes against estimates of twenty, a factor of ten to fifteen; the one
editing task took eight minutes against forty-five to sixty, a factor of about six the same way; one review took
two minutes against fifteen. Every estimate was too high, and the bounded read-only ones by the most. The
decisions warning fell from forty-four rows to twenty-nine once the fifteen that can never clear were separated.
Two independent counts of the shipped tool agreed that no subcommand is named only by a home-side file, and
disagreed on the size of what that implies by several times.

**Learned.** *General:* a rule the author has just written is still broken by that author when the broken form is
the host's default; the identifier is the form most likely to be asserted from memory, because it reads as a
citation; a gate only ever grows, since a rung exists for adding a control and none for retiring one; and a
classification by who *names* a thing cannot separate a producer's code from a consumer's, because the producer's
procedures are documented in what the consumer receives. All four went out as proposals, `p-88cc26de4e`,
`p-75679cf56f`, `p-19e2887fcf` and `p-7b6ae101bc`. *Local:* the estimate-and-actual pairs went to
`i-5ed7e8-045188`; the privacy false positive to `i-5ed7e8-b8c4b2`; the missing session log is closed by this
file; the usage-evidence process to `i-5ed7e8-9ef5d1` and `d-5ed7e8-355404`, which waits on the owner's design.
Captured: 4 learnings, 6 frictions (shell word-splitting; assertion from memory; two privacy false positives; a
tool crashing where it should refuse; estimates high by an order of magnitude; a delegate deleting a record
instead of closing it). The usage-evidence design needs you.
