# A host's ticket cycle against the method

**Date:** 2026-10-07. **Status:** review, read-only; feeds the next release through five of this repository's
proposals. The carriers' side (each skill's `LOCAL.md`) is done in the carriers themselves.

## What was read

Several carriers of one team keep a shared set of procedures for working a tracker ticket from creation to
closing: creating a ticket, writing a plan, implementing it, reviewing the pull request, and closing the
ticket, plus a README for a plans folder. They are copies of one origin: on the integration branches, three
carriers hold the creation, planning and implementation documents byte-identical, three more hold them on a
ticket branch not yet merged, and the review checklist exists in about five different versions. Several
copies point at documents their own repository does not have.

## The cycle, in the host's words, generalised

1. **Create the ticket**: search for a duplicate first; one ticket, one outcome; a problem in a sentence or
   two, expected results, and acceptance criteria that are each a checkable fact; the whole ticket fits on a
   screen; an open decision is its own ticket.
2. **Plan**: research before planning, written apart from the plan (what is true today, with references and
   measurements); stop when the research contradicts the ticket. The plan has a goal, a baseline, non-goals,
   and a task table where each task names what it changes, is committable alone, says how it is verified,
   and is marked when it needs a person. **Every acceptance criterion maps to a task, and every task to a
   criterion.** A person approves the plan.
3. **Implement**: one branch per ticket, one commit per task, a **status table** in the plan kept current
   with each commit's hash ("a status table reconstructed at the end is fiction"), decisions recorded while
   fresh, a task that turns out wrong marked with its reason, work beyond the ticket becoming a new ticket.
   The gates are blocking; the pull request body says what changed, how each criterion was verified and what
   was left out; a summary for the ticket's author goes on the ticket, readable without the code.
4. **Review**: a checklist ranked blocker, warning, nit, each finding with its location and a concrete fix,
   and a verdict; a single open blocker means changes requested.
5. **Close**: **a person decides**; the agent prepares the evidence and stops. After approval: merge, remove
   the worktree, delete the branch, mark the ticket done.

**The plan is a working artifact, not a record.** The plans folder is excluded from git; a plan lives in the
worktree where it was written and disappears with it, so a second, drifting explanation of the change never
ships. Before it disappears, each kind of content moves to the record that survives: the why of the change to
the change log, what was delivered against the criteria to the ticket, what changed and how it was verified
to the pull request, and anything deferred to a new ticket.

## Against the method

| Practice | In the method today | Verdict |
|---|---|---|
| Comments describe the code, no ticket ids or change narration | yes, *Documentation, in the code* | confirms |
| A person merges and closes; the agent stops at ready | partly: `close` pushes or merges only when asked, but has no "ready for review" stop | proposal |
| The plan as a local working artifact, with a table of where each kind of content survives | no; `close` copies rulings from "the plan's ledger" and assumes it persists | proposal; conflicts today |
| Acceptance criteria and tasks map both ways | no | proposal |
| A plan's status table with commit hashes, kept current | no | proposal |
| An external tracker as the source of pending work; the roadmap cites its keys | no in the method; decided in two bootstraps on 2026-10-05 | proposal |
| Review findings by severity, each located and fixable, with a verdict | partly: 0.0.29 asks a proof per finding | folded into the review proposal of 0.0.29; no new one |
| Procedures copied across repositories drift | the problem the bundle solves (principle 5, one source) | confirms; the copies themselves are the host's to unify |

## What the carriers did

In each of six carriers holding the release, the skills `close` and `decision-review` gained a `LOCAL.md`
section that maps them onto this cycle: the agent stops at "ready for review" and a person merges and closes;
a plan is local and its content moves to the records before cleanup; the repository's own closing procedure,
where it has one, wins over the skill. The four carriers updated on 2026-10-05 installed the skills with this change; the two bootstrapped that day had them already.

## What this review did not do

It read one carrier's copy closely and compared the others by content hash only; it did not read the
tracker; it measured nothing about how often the cycle is followed.
