# Decision records against the ADR literature, and records that never leave a carrier

**Date:** 2026-10-05. **Status:** design settled by the owner in a decision review, one decision per turn;
nothing in `sources/` changed. It feeds release 0.0.29 through five of this repository's proposals and the
intake (`i-5ed7e8-1bc188`). It closes `i-5ed7e8-ca6ce3`. The decisions are rows of
[`meta/decisions.md`](../decisions.md); this document holds the evidence and the reasons.

## The question

Does the method's decisions log (artifact 6, `docs/decisions.md`) lack what the architecture decision record
(ADR) literature asks for, and which of those gaps does *this* method need, judged by its own principles
rather than by conformance? A second question came with it: a carrier may want to keep confidential context
for its decisions (the ADR literature asks for the organisation's situation and priorities), and none of it
may reach the bundle.

## Evidence

**Public sources.**

- The ADR collection maintained by Henderson (Nygard's template, MADR, Tyree and Akerman, Y-statements and
  others): one record per decision with a status (`proposed`, `accepted`, `rejected`, `deprecated`,
  `superseded by`), timestamps on whatever can go stale, immutability by amendment or supersession, context,
  consequences both easier and harder, and fitness functions as an optional extra.
- MADR records the considered options with their pros and cons and splits positive from negative
  consequences. `sources/references.md` says an ADR does not record rejected options: true of Nygard's
  template, false of MADR.

**An external team's practice** (private; not cited). One record per decision with front matter; a status
that only a person moves from proposed to accepted, with the pipeline refusing to merge a proposed record;
the rationale marked confirmed or unknown, so a reason reconstructed from the code is not presented as the
decider's; a list of what looks deliberate and is not, which an agent may fix without asking; a structural
validator; a check named per decision; baselines that can only shrink; and sequential numbers whose next free
value depends on a branch not yet merged.

**This machine's carriers, read-only, as aggregates.** Most keep `docs/decisions.md`; logs range from about
fifteen rows to a few hundred. None keeps an ADR folder or one file per decision. Two invented, independently,
an "open, half-decided" section with states (unresolved, declared gap, accepted as advisory or visible debt)
and a column for who must close each one, always a role. One writes a date inside the Why cell in most rows;
others in a few. Supersession is written in prose, in several shapes, in the largest log. Negative
consequences appear in about a tenth of the largest log's rows and almost nowhere else. A reason marked as
unconfirmed appears twice in one log. Several logs carry business words (customers, vendors, prices), and the
harvest reads the log.

**This repository.** `propose` and `intake` run no privacy check of their own (`propose` prints a reminder);
0.0.26 rewrote a private carrier's verbatim evidence by hand before intake. The coding session loads about
98% of its token budget, and since 0.0.27 principle 2 says a rule acts only in the output the action
already reads, so a new rule reaches coding sessions through a check's output, not through prose.

## The standard against the method

| Element | ADR literature | Method before this | Decided |
|---|---|---|---|
| Unit | one file per decision | one row in one log; prose with the document that owns it | keep the row; no body file |
| Status | proposed, accepted, rejected, deprecated, superseded | none as a field | a Status cell |
| Date | timestamp what can go stale | none | in the Status cell |
| Who decided | deciders, owners, accountable team | none | an alias or an agent session; names private |
| Context | the organisation's situation, priorities, team | the Why column | public Why; confidential context private |
| Consequences | easier and harder; follow-ups; a review later | the cost of the alternative | an `accepting:` clause |
| Options | MADR lists them | principle 10's declined rows | unchanged: the owner of the long form holds them |
| Enforcement | an optional extra | the Enforced in column | unchanged; a check of the log itself added |
| Ids | sequential numbers | content-hash ids, frozen | unchanged: a number that depends on a branch collides |
| Known debt | absent in the collection | absent | a section of the log |

## The design

### The row

Five columns, as today plus one: `| Id | Status | Decision | Why | Enforced in |`. The id stays the first
cell, where `bundle.py ids` reads it; the check reads columns by position, so a log in another language keeps
its own headings.

**Status** is `<state> <date> · <decider>`, in fixed English keywords even in a log written in another language
(they are marks for a tool, like `d-` ids and `privacy-allow`):

- states: `proposed`, `accepted`, `declined` (principle 10; MADR's rejected), `deprecated` (no longer applies,
  nothing replaced it), `superseded by d-…` (principle 6: written in the old row, in place; the new row says
  `supersedes d-…` in its Why);
- the date is the decision's; a migrated row reads `accepted recorded <date>`, the date of the first commit
  that holds its id, because a bulk conversion would otherwise date many rows to one day;
- the decider is a stable alias of a person (`h1`), an agent's session (`agent s-…`), or `found` (read from the
  code, decided by nobody who can be asked). A proposed row adds who must decide: `· decides: h2`.

**Only a person accepts or declines.** An agent writes `accepted · agent s-…` only for what principle 15 leaves
to it, and reports it under *decided for you*; to change a decision a person took (or one with a blank decider),
it writes a `proposed` row that supersedes it.

**Who decided** matters (the owner: it is important to know who is taking the decisions), and a name must not
travel. So the row carries an alias, and `docs/private/people.md` maps each alias to a name and role.
An alias is never reassigned, like an id: a person who leaves keeps theirs, a new one gets the next. The public
home has only `h1`. A blank decider counts as a person for the check.

**Why** may begin with `unconfirmed:` when no person gave the reason (a bootstrap reading the code, an agent's
inference); only a person removes the mark, and the close offers each such row as a fact question
(principle 15's fact interview). A decision's own cost ends the cell as `accepting: <cost, with its number>`,
the tail of a Y-statement; it is asked for, not checked, since a decision with no cost of its own has nothing
to write.

**No body file.** The long form stays with the document that owns it; where none does, the changelog entry that
took the decision (`s-…`, which already holds the discarded alternatives and the numbers) owns it, and the row
cites it. A host that already keeps ADR files keeps them (below).

### Known debt

A section at the end of the log, *Looks deliberate, is not*: `| Id | What | Why it is not deliberate | Fix when |`,
with a `d-` id. It is principle 10 inverted: it tells an agent what it may fix without asking, and is deleted
row by row as the debt is fixed (the id is never reused).

### When to write a row

About eight lines in artifact 6, generalised: a row when a change adds or removes a runtime dependency, moves a
module boundary, changes persisted data, changes a public interface, is hard to revert, is a choice a reviewer
would question (not doing the common thing included), or fixes a cross-cutting convention; not for a fix, a
rename, a lint, or what an accepted row already covers. They stay out of the coding session (budget) and are
rung 1: no check can judge them.

### The check

`bundle.py decisions FILE`, run by the carrier's gate and by the `close` skill.

- FAIL: a state, date or decider that does not parse; `superseded by` with no target, or one not in the log;
  a superseding row whose `supersedes` is missing; `accepted · agent` superseding a row decided by a person or
  with a blank decider.
- WARN: every `proposed` row with its age and who must decide; every `unconfirmed:` reason; a backticked path in
  Enforced in that names no file (principle 2: a name cited enforces nothing).
- It never reads the private folder, so it cannot tell whether an alias exists.

### Migration

A command fills each existing row's Status as `accepted recorded <date>` from git, with a blank decider. The
update session maps supersessions and declined rows already written in prose; where unsure it leaves
`accepted`. The heading of each table gains the Status column. Several hundred rows across the carriers.

### Records that never leave a carrier

- **The folder.** `docs/private/` in each carrier (the host may name it otherwise and record that in `adapted`),
  for confidential context keyed by decision id (`docs/private/<d-id>.md`) and for `people.md`. No tool reads
  it; the harvest is told never to read it. In a public repository it is in `.gitignore`.
- **The sentinel.** Every file there starts with `confidential: never leaves this repository`. `bundle.py privacy`
  fails when that line, or the folder's path, appears in `.agents/` or in a commit range: it catches a pasted
  file even when nothing in it is on a terms list.
- **The public-repository guard.** When `carrier.toml` declares the carrier public, `verify` fails if the folder
  is tracked by git.
- **The home's re-check.** `release.py gather` and `intake` run the privacy check, sentinel included, over every
  proposal; one that fails is not taken in and is named in the report.
- **A warning is a question.** In a proposal, every privacy WARN (an exact figure, an N of M, a quote, or what the
  agent judges business or personal) becomes a question to the owner at the close or the harvest, defaulting to
  "generalise it". A yes writes `privacy-allow: <reason>`, the owner's explicit instruction the rule already
  requires; no answer means generalised. `intake` treats a WARN in a proposal with no allowance as a FAIL.

Per-machine terms lists do not carry this: a teammate's machine lacks this one's list, which is why names stay
in the private folder rather than in rows guarded by terms.

### Adopting a host that keeps ADRs

Principle 19: the host's ADR files stay. The method asks only for its guarantees: statuses mapped to its
vocabulary (`rejected` to `declined`, `pending` to `proposed`), an index row per ADR with Enforced in, and
supersession both ways; the mapping is recorded in `adapted`, and the check reads the host's index.

### References

`sources/references.md` corrects its line on rejected options (Nygard's template does not record them; MADR
does) and gains entries for the collection and for MADR in principle 8's shape. The external team's guide is
not cited.

## Firm, and under review

| Firm | Under review, re-judged at the 0.0.30 harvest |
|---|---|
| status with date; `proposed` and only a person accepts; known debt; the private folder and its layers; the check | the decider aliases and agent sessions; `unconfirmed:` and `found`; the `accepting:` clause; the when-to-write criteria |

The firm ones rest on two or more carriers or on leak risk; the others on one source or on principle alone.

## Not chosen

- **A body file per decision**: no carrier uses one, and it opens a second home for the why (principle 5).
- **An Accepting column**: little evidence of need, and a cell in every row of every carrier.
- **Paths per decision now**: only one log is large; `i-5ed7e8-bf017b` reopens it when a log outgrows one read.
- **Real names in rows**: the harvest reads the row, and the only guard would be a terms list that exists on
  one machine.
- **`propose` refusing on a privacy failure**: the owner chose the three later layers.
- **A reconstructed history for the home's log**: tens of rows, all `found` and `unconfirmed`, with no evidence
  they are needed.

## What changes in 0.0.29

`sources/bundle/method/prompt-context.md` (artifact 6, the adoption table, principle 20's private folder),
`prompt-harvest.md` (never read the private folder; warnings as questions), `prompt-bootstrap.md` and
`prompt-update.md` (the migration, the status grammar, the sentinel), the `close` skill (run the check; raise
proposed and unconfirmed rows), `sources/bundle/tools/bundle.py` (`decisions`, the migration, the sentinel and
the public guard), `meta/tools/release.py` (the re-check in `gather` and `intake`), `sources/references.md`, and
their tests.
