# The method, for the home repository

Sections of the method that only the home repository uses: why the method exists, how it forks and how often it moves, and a worked example. Cut from `.agents/method/prompt-context.md` at 0.0.22; a carrier's sessions never read them.

## Why this exists

An agent is fast, tireless, and arrives with no memory of yesterday. That
combination has six failure modes, and everything below is aimed at them:

1. **It re-derives.** Every session re-discovers the same constraints, and
   re-opens the same settled questions, because nothing wrote them down in a
   form that survives a new context window.
2. **It breaks what it cannot see.** A rule that exists only in prose gets
   broken silently. The agent is not careless; it simply had no way to check.
3. **It parallelises into collision.** Sessions are cheap to run side by side.
   Two of them working the same feature will not see each other, and the merge
   is discovered at compile time — or worse, at review time.
4. **It stops at green.** A passing gate says the code did what it was told. It
   does not say that what it was told was right, and an agent that never looks
   at what it produced will ship something that satisfies every assertion and is
   obviously wrong to the first human who sees it.
5. **It mis-sorts the decisions.** Either it guesses on the two choices that
   were genuinely the human's and builds the wrong thing confidently, or it
   escalates everything and hands the work back. Both look like diligence.
6. **It accepts friction as given.** It will run the same nine-step manual
   ritual forty times without once proposing to automate it, because each
   instance is individually cheap and no single session is the one where the
   cost is obvious. Tirelessness, which is a strength everywhere else, is
   exactly what hides this.

The first three are solved by the artifacts. The last three are solved by how a
session is *run* — see **The session loop** in `prompt-bootstrap.md`, which is
the half of the method that applies forever after the bootstrap is over.

The system below is not documentation for humans that an agent happens to read.
It is a **control surface**: the set of files that decide what the agent treats
as settled, what it must verify, and what it must refuse to do.

---

## How to fork, and how versions move

**A fork is a git fork of the home repository.** Its releases and versions are its own, never
compared with the home's; anything general either side learns travels the other way as a
candidate, through a harvest, never by overwriting a file.

- **Versions are cut by a release in the home, never by a carrier.** One Semantic Versioning
  version for the whole bundle, set by `release.py release X.Y.Z` in the frontmatter of
  `.agents/README.md`, a dated section in `.agents/CHANGELOG.md` saying what a reader *does
  differently* now, not what was edited, and a tag `vX.Y.Z`. While it is `0.0.z`, any release may
  break; moving to `0.1.0` or `1.0.0` is the user's decision.
- **Never renumber the principles.** Append. A repository referring to
  "principle 14" must still be right after the next revision, exactly as an enum
  written to disk is appended to and never inserted into. If a principle dies,
  mark it withdrawn and leave the number spent.
- Same for the artifacts, the phases and the steps of the loop. A repository's own records are
  not numbered at all (*Workspaces*, record ids).

## The two directions

**Down — distributing an improvement.** Put the newer bundle in the target's
`.agents/incoming/` — never over the live one — and run the **update
invocation**; for every carrier open at once, `prompt-sync.md` carries the
tagged release into each with `release.py splice`. The update reads the version the repo had, lists only the deltas
since, and — the part that matters — decides which of them apply *there*,
because a repo with no rendered output does not need the rule about looking at
the artifact.

**Up — harvesting from a repository.** Rarer and more valuable.
`prompt-harvest.md` asks the repository *what have you learned that the method
does not know?* and writes the answers as candidates in its outbox, `.agents/tracking/`.
The next release gathers them (`release.py gather`, `release.py intake`), applies the generality test, brutally, and takes the two that survive
rather than the nine that were offered. The failure mode here is a method that
accretes one repo's idiosyncrasies until it is portable to nowhere.

## A cadence that works

Tie the reviews to events rather than to the calendar, because a monthly ritual
gets skipped and an event-driven one does not:

| When | Do |
|---|---|
| Every session close | step 8 — harvest to level 1 and 2 |
| When a friction is hit a second time | promote it to the roadmap's process area |
| When the local review skill runs (Phase 9) | ask which level-2 rules pass the generality test |
| When you notice yourself explaining the same thing to a second repository | record it as a candidate for level 3 in the outbox, `.agents/tracking/candidates.md`; the next release decides |
| At every release | `release.py triage`: a candidate that waited three releases without gaining what it lacks is discarded |
| Before a round of harvests | align every carrier first (`prompt-sync.md` §*The cycle*): two commands when nothing diverged, and what makes every harvest read the same base |
| Before a meta-session, in every carrier | run the local step, `prompt-harvest.md`: it is what the meta-session gathers |
| When a repo gets significant new work after a gap | run the update invocation before starting, not after |

**The last row is the one people get wrong.** Updating the method *after* the
work means the work was done under the old method, and the first thing the new
method says is usually something the work should have done.

---

## Worked example: how this landed in one repository

An interactive time-synced renderer, scripted, **deployed where its developers
cannot observe it**: every test on the real target goes through somebody outside
the development side. That single constraint shaped everything, and it is why
the example transfers: most repositories have some version of *a place where the
software runs and you cannot look.*

**The invariant.** One clock is the master; every visual is a pure function of
that clock's current time. Never accumulate frame delta.

**The enforcement chain for that one invariant**, rung by rung:

| Rung | Mechanism |
|---|---|
| 1 | Two paragraphs at the top of `CLAUDE.md`, each rule carrying the measurement that produced it |
| 2 | A decisions table, a run of consecutive rows, each naming the class or constant that enforces it |
| 3 | A validator that fails the gate on the constructs that cannot be seeked — anything that simulates forward from the previous frame, or reads a clock other than the master — plus a renderer that reaches each moment **from both directions and compares the pixels** |
| 4 | The data format itself: an element names a *layer*, never a number, so the layering rule cannot be violated in the data |

**What the numbers did, and the bug that justified the system**, are the
examples already told in principles 2, 5, 6 and 7: the audit failing every one
of its rules on its first run, the root file shrinking to about a quarter of its
size, the batching measurement that kept the layering rule, and the list the
build emptied. One more: a refactor of the rendering system was accepted only
because every reference frame rendered byte-identical before and after.
Its sessions supply the examples of principles 14 and 15 and of the session
loop's steps 0 and 1 — one roadmap item taken through the whole loop, with the
screen rendered and looked at, three questions asked and no more, and one
structural decision handed back rather than taken mid-feature. None of it is
specific to that kind of software.

**The transfer.** Nothing above depends on that platform or that domain.
Substitute your own nouns:

| Here | A backend service | A Python package | A data platform |
|---|---|---|---|
| the master clock | the transaction boundary | the public API | the partition window |
| seek from both directions and compare pixels | replay the request twice and compare state | install the wheel in a clean venv and smoke-test | rerun the window and diff the table |
| the runtime nobody here can observe | production under concurrency | the user's machine | the full-size dataset |
| the data format that cannot express a bad layering | a config type with no optional timeout | a `Money` type with no float constructor | a contract that rejects an unknown column |

---

## Method changelog

From 0.0.22, each release is a section of `.agents/CHANGELOG.md`. The table of what each earlier
method version changed is frozen in [`method-changelog.md`](../archive/method-changelog.md).
