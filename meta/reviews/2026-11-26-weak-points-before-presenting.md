# The weak points, before the project is presented

2026-11-26, at the owner's request: everything that would not survive a sceptical reading, in one list, to
be worked **one at a time**. Each row says what is wrong, what would fix it, what the fix costs, and
whether it blocks a presentation. Nothing here is a defect of the code; these are defects of the
**evidence and the claims**, which is what a presentation stands on.

The ordering is by what a sceptic reaches first, not by what is cheapest.

## A. The evidence

| # | Weak point | What would fix it | Price | Blocks? |
|---|---|---|---|---|
| A1 | **The cost is above the bound the project set itself.** The last registered measurement is about ×2.7 against a two-line instruction file, where the criterion asks for at most ×2 on non-trivial tasks. | Optimise, measure, then update the figure — the owner's ruling of 2026-11-26. The read has already fallen about a third this release; whether that moves the ratio is unmeasured. | A pilot run: a subscription token or an API key, the owner's quota, about an hour of wall time | **yes** |
| A2 | **The pre-registered primary contrast was null**, and the report says so itself: neighbouring notes carry the same principle, so deleting the target note does not remove it. The headline test was the wrong test. | Register a new primary contrast that fits the bundle — carrying it against a two-line file, on the tasks that discriminate — before any further trial. | Writing: under an hour. The run is A1's. | **yes** |
| A3 | **Nothing is statistically significant, and nothing can be.** The contrast is an exact sign-flip test over paired per-task differences, so with *k* tasks all moving one way the smallest two-sided p-value is 2/2^k. With the three discriminating tasks that exist, that is 0.25 — a ceiling of the design, not a measure of the effect. **Six tasks is the first count that can reach p < 0.05 (0.031), and the project's own pre-registered analysis plan refuses to test a contrast over fewer than eight.** It is testing with three against its own rule of eight. | Write five more discriminating tasks, to reach eight. Writing them needs no credentials; only the run does. | About an hour each to write and grade: five tasks is under a working day | **yes** |
| A4 | **The tasks were written by the maintainers after reading the notes.** The most common objection to any in-house benchmark, and it is correct. | Derive tasks from defects that real repositories actually shipped, taken from their histories, with the hidden tests being the real fix's tests. The proposal exists and is unrun. | A day to build the harness; then it needs a carrier owner's approval task by task | no, if disclosed |
| A5 | **Harm is almost unmeasured.** One over-application observed, and no boundary tasks at distance — the exact shape where a note would misfire. | Write boundary tasks at the two distances the design already uses. | About half of A3's work, and it shares its run | no, if disclosed |
| A6 | **The general-performance study has no data.** The only evidence is on tasks derived from the notes themselves. | Run it, or stop citing a second study until it exists. | Large; or free, if the claim is withdrawn | no, if disclosed |
| A7 | **Real sessions cannot show benefit.** Two measurements now give the real cost share, but nobody ran the same task twice, so neither says the bundle helps. | Nothing fixes this; it is a limit of observational data and must be stated wherever the figures appear. | Free | no |

## B. The claims and the records

| # | Weak point | What would fix it | Price |
|---|---|---|---|
| B1 | The frame declares a cost figure older than the last measurement. | Optimise, measure, update — the owner's ruling. Follows A1. | Minutes, after A1 |
| B2 | The frame promises one release a month; the real cadence is roughly two a week. | Either change the promise to what is done, or say why the burst is temporary. A promise nobody keeps is rung 0. | Minutes, plus a decision row |
| B3 | The experiment's own README and the head of its report say "five exploratory pilots"; it runs to twelve and the reviewer runs. | Rewrite both headers from the body. | Half an hour |
| B4 | Criterion 2, *the procedure is followed without guessing*, is unmet: a review of 2026-11-26 found a dozen gaps in the harvest and update texts. | Close those gaps, then re-run the criterion's own test: an agent follows the written method on a copy with nothing invented. | A day, plus a run |
| B5 | Criterion 1, *the loop has turned for real*, is unproven: no two carriers have gone through the whole cycle over two consecutive releases. | The pilot cohort chosen on 2026-11-26 is the path; it needs two releases carried into at least two of them, with nothing lost or taken in twice. | Two release cycles |
| B6 | Twenty-eight decision rows give a reason no person confirmed, and twenty of those are an agent's own, which no one else can confirm, and five name an enforcing file that no longer exists. | Walk the rows; the five stale enforcers are minutes. | The five: minutes. The twenty-eight: a decision walk |
| B7 | Two slugs in the experiment table name no note, candidate or answered idea. | Resolve or remove them; the check warns on every run. | Minutes |

## C. How it is presented

Being researched separately on 2026-11-26. The page that exists today is honest and dense; whether that
converts a sceptical reader, or only satisfies one who already agreed, is not known and is the question
the research was asked.


## What 2026-11-27 changed in this table

**A3's diagnosis is done, and it moved A2 and A5 with it.**
`meta/reviews/2026-11-27-why-three-of-sixteen-discriminated.md` found that **the variable the design varied
was not the one that mattered**: distance from the edited file does not decide whether a task discriminates.
What decides it is whether anything the agent reads already names or offers the safe action — a parameter in
a signature, a sibling that does it, a fixture, a phrase in the request. Seventeen of seventeen failures in
the arms without a note fall in the three variants that have no such pointer; every trial of the other thirteen
passed. Counted twice, by two agents, over the same file.

What it does to each row:

- **A3** — the count of discriminating tasks is **two independent traps, not three**: two of the three are
  one trap at two distances, and seven of the eight pairs are concordant. The ceiling is therefore worse
  than the row said. But the tasks can now be *designed* rather than fished for, which is the difference
  between about fifty attempts and about twelve. **The rule is not approved and nothing is built on it.**
- **A2** — the new primary contrast can now be stated in terms of the pointer rather than of distance,
  which is the first time the registered contrast has had a mechanism behind it.
- **A5** — boundary tasks at distance were the planned shape for measuring harm. Distance being the wrong
  axis, the boundary tasks should vary the pointer too, or they will measure as little as the thirteen did.
- **A1, A4, A6, A7** — unchanged. A1 still needs a run.

**B2, B3, B6 and B7 are done** (2026-11-27, lane R of the next session's plan), and two of them were not what
this table said: B6's five rows were a *superseded* decision naming the list its own successor deleted, and
B7's two slugs were experiments on rules of the method rather than on notes. Both were fixed in the checks,
not in the data. **A row of this register is a lead, not a diagnosis**, and the next lane should expect the
same.

**B1 is done differently than this table proposed.** The frame now carries the measured ×2.74 with its
interval, the release it was measured on, and the count of releases shipped unmeasured since, rather than
waiting for a new measurement to replace a stale band (`d-5ed7e8-6a5524`).

## What this list is not

It is not a plan. Nothing here is scheduled, and the owner takes them one at a time. A row leaves this
table only when its fix has landed and the claim it weakened is true, or when the claim is withdrawn.
