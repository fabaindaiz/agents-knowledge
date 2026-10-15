# Traditional development beside the method — who can bypass what, and four designs

**Research for `i-5ed7e8-7e0dd7`, 2026-10-15.** Delegated to a cheaper model (about 19k tokens, one
minute) and reviewed here. **The thinnest of the three reports:** four sources read at the source, much
of the rest marked as unverified by the agent itself, and no peer-reviewed material reached. Read before
the design round; nothing here is method text yet.

## The finding that decides the shape

**No local enforcement point binds a person.** Local hooks are not copied by a clone, are opt-in per
clone, and are bypassed by one flag; a hook runner's own stage setting can demote any check to advisory.
Only a receiving-side check binds — and even a protected branch does not apply to administrators or to
roles holding a bypass permission unless that is explicitly closed. Two details matter for us: a
required check **passes when it skips itself**, so a check that excuses itself is indistinguishable from
one that ran; and whoever can edit the workflow in the same change can weaken it, unless that path is
owned.

So the only arrangement that holds is: **the receiving side decides, the local side advises, and the
check reads a marker in the change rather than guessing who made it.**

## Identifying which population a change comes from

| How | Holds? |
|---|---|
| Author identity | **No.** The author field is free text; a person can also commit through the agent's account |
| Path | Robust and cheap, but the records both populations touch — the log, the decisions file — are exactly the shared paths |
| Branch | Weak: a merge mixes the two populations |
| A marker in the record or the commit message | Explicit and checkable on the receiving side; it fails when forgotten, so **absence must default to a defined state, not to a pass** |

## The pattern for a record both populations write

Check that existing lines are **unchanged** (the diff shows only additions) and treat an entry with no
minted id as *foreign, unverified* rather than as an error; mint the id when the change is merged, not
when the line is written. Established records practice replaces an edit with a superseding entry rather
than a rewrite. Our own candidate says the same from the other side: a convention only one party follows
degrades to a suggestion for the others, and the cheapest way to green — editing the other person's
record to satisfy your tool — passes the check, which is why it must be impossible rather than
discouraged.

## Detecting drift between a human edit and a generated artefact

Regenerate on the receiving side and fail on a difference, or compare a checksum manifest — which is
what this bundle already does for its own release. What the established tools add is the report: the
first differing path and the command that regenerates it.

## Four candidate designs

1. **The receiving side blocks, the local side advises.** The required check is the only blocker; local
   hooks warn. A reconciling job mints ids and appends a catch-up entry as its own labelled commit.
   *Costs the human:* nothing until merge, then one extra commit. *Costs the agent:* little. *Measure:*
   the share of merges needing reconciliation. **Constraint: the job may only add, never edit**, or it
   becomes the named failure mode.
2. **Marker-scoped enforcement.** A marker in the change declares that the method was followed; strict
   checks apply to marked changes, and unmarked ones get an advisory report plus a ledger line. *Measure:*
   the unmarked share over time, and how many ledger lines are later closed.
3. **Path partition.** Method-owned paths are written only through the tool and are owned on the
   receiving side; human-owned paths are never checked for method fields. *Measure:* how often the other
   population touches a method path, and whether a second copy of a record appears outside it.
4. **Baseline and ratchet.** Record today's violations, block only new ones, report stale baseline
   entries. *Measure:* the baseline falling month by month. **The baseline must itself be owned**, or it
   is edited to go green.

Every design needs a seeded fault — a deliberate bad change that is **seen to fail** on the receiving
side, not only locally.

## Reported failure modes

Checks disabled by the bypass flag or by a skip variable; red builds nobody reads any more; a record
rewritten to satisfy a tool; a second source of truth appearing beside the owned one; and a baseline
that grows instead of falling.

## What this still lacks

Everything about adoption in mixed teams is unverified here: no peer-reviewed evidence on partial
adoption, no data on records practice, no documentation-drift study. The agent did not search for them.
Before the design round, one of the four designs should be tried against **this** repository's own
history: how many of its commits would a receiving-side check have refused, and how many of its records
carry an id minted after the fact.
