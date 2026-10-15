# Cost as a principle — the mechanisms, and four rules a check could hold

**Research for `i-5ed7e8-55e022`, 2026-10-15.** Delegated to a cheaper model (about 69k tokens, under
two minutes) and reviewed here. Read before the design round; nothing here is method text yet.

## What the principle should be about

**Avoidable waste, not spending less.** Every rule below is of the form "do not pay twice for the same
thing" or "say what it costs before you spend it"; none of them says "do less work". That distinction is
what keeps a cost principle from becoming a reason to skip verification, which is the failure mode at
the end of this document.

## The mechanisms, ranked by the size of the effect

1. **A cache hit against a miss** is the largest lever by far: a read costs a small fraction of base
   input, while a write costs more than base. Once caching works, **output dominates the bill**, because
   output is priced several times input on every model, and thinking tokens bill as output.
2. **The model tier** is next: between the mid and top tiers the price per token differs by a factor of
   several, and a fast mode doubles it again.
3. **Context size**, because the whole history is re-sent on every request: a one-line question late in
   a long session still pays to re-read everything, at the cached rate if the cache is warm.
4. **Each agent launch**, because a delegate's first request cannot read the parent's cache — a
   different prefix — and its own cache lifetime is short. A team of agents multiplies a session's
   tokens several times over.
5. **Long tool outputs and re-reads**, where filtering at the source turns tens of thousands of tokens
   into hundreds.

## What breaks the cache, which is what a session must avoid mid-task

Switching model; changing the thinking or effort setting (on the current models an effort change keeps
the cache, which is the exception); turning on a fast mode; adding or removing tool definitions or
servers; compaction, by design; an upgrade of the host, applied at restart; and idle time past the cache
lifetime, which is minutes on an API key and an hour on a subscription. **Cache-safe:** editing files in
the repository, editing the root instruction file, changing permission or plan mode, and spawning a
delegate (the parent's prefix is untouched). The expensive case is **resuming cold and then
compacting**, which pays for the whole history twice.

## Model per task

The host's own guidance is advice with no measurement behind it: a mid tier for most coding, the top tier
for architecture or multi-step reasoning, the cheapest tier for simple delegates. The one piece of
peer-reviewed support found is a 2023 cascade result (a learned router matching the best single model at
a fraction of the cost on non-agentic benchmarks); it does **not** establish "a cheap model plus
verification" for coding work, and should not be cited as if it did.

## Budgets, and what makes them theatre

From the published error-budget practice: a budget works when it is the complement of a stated
objective, when a breach has a **named consequence** (work of a stated kind stops), when named causes
are exempt, when a single large incident forces a write-up, and when the framing is protecting the
subject rather than punishing the team. It is theatre when nothing follows a breach, when an estimate is
never compared with the actual, or when the number is the thing being optimised.

## The four rules, each with what a tool could measure

| Rule | What a tool measures | Cost to measure |
|---|---|---|
| **Prefix stability**: no model, effort or tool-set change mid-task unless recorded with a reason | the host reports cache misses and a likely cause; a miss count above a threshold with no recorded switch | near zero, the counts are local |
| **Tier and effort are named**: every delegation says its model, its effort and why the cheapest adequate one | the share of spend on the top tier against the plan's stated tier | low |
| **Bounded launches**: each launch states an expected-token estimate and a stop condition; compaction happens at task boundaries | per-agent tokens against the ledger's estimate | low, but the host's cache figures cover the main conversation only, not delegates |
| **A budget with a consequence**: below a stated fraction of the budget the plan switches to closing, and the consequence is written | the reported remaining budget against the plan's state | needs a reported figure; the host's own numbers are approximate and local |

## Where cost cutting degrades the work

The host's own documentation says effort and thinking trade thoroughness for tokens, and that planning
and early correction avoid expensive rework. No study was found quantifying a quality loss from
cheapening an agent's work; the cascade paper notes only that accuracy and cost need joint optimisation.
**So every cost rule is paired with a quality floor** — the gate passing, the verification run — and a
budget is never set below the cost of verifying the work.

## What this still lacks

Numbers for effort levels, which the reference does not give; a measurement of our own (the cost pilot,
`d-5ed7e8-5b183e`, still unrun); and a source for the claim that a number used as a target stops
measuring what it measured.
