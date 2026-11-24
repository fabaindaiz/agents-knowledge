# Session log

**What each working session in this repository did, newest first.** One entry per session, in the
method's own format, started with `python3 .agents/tools/bundle.py new entry "<title>" --write`.
It is the record a friction count searches (`bundle.py count`), so a friction that is not written
here is a friction nobody can count later.

The hand-off each close replaces lives beside this file, in `roadmap-states.md`: that file holds the
states, this one holds what happened on the way. Sessions before 2026-11-24 are recorded only as
those states and in `meta/tracking/history.md`.

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
