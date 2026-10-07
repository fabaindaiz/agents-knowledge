# Cost levers for the bundle: what the primary sources say

**Date:** 2026-10-07. **Status:** research by a delegated agent, read-only; bears on release 0.0.30's focus
(`d-5ed7e8-7cac23`). Sources are ideas only, paraphrased; ASSUMPTION marks a claim not checked against its source.
Read with `meta/reviews/2026-10-07-reviewer-cost-decomposition.md` and `meta/reviews/2026-10-07-cost-inventory.md`.

## Findings

**Progressive disclosure.**
- In the host, skill descriptions are always in context, capped at about one and a half thousand characters; a
  skill's body and supporting files load only when used.
- Imports in the root file load at launch and save nothing. Rules scoped to paths load on demand.
- A recent preprint found lazy loading saved a quarter to four fifths of tokens with small open models, at one
  extra call and some latency, with mixed retrieval quality. A vendor's deferred tool search saves most tokens only
  for tool definitions above about ten thousand tokens.
- The pilots fit the pattern: lazy loading pays in proportion to what it removes from a context re-sent every turn.

**Subagents.**
- Multi-agent systems use roughly fifteen times a chat's tokens and single agents about four times; coding is
  less parallelisable than research. Agent teams use about seven times.
- A subagent starts with its own system prompt plus the whole root-file hierarchy, unless its definition omits
  it, and a separate cache with a five-minute lifetime; a fork shares the parent's cache.
- Delegating saves tokens only when the material kept out of the main session, times that session's remaining
  turns, outweighs the subagent's prefix times its own turns. This rarely holds for a reviewer of a dozen calls.
- **The reviewer pilot measures a stand-in**: it runs the reviewer as a headless main session (the host's system
  prompt, the one-hour cache). The real subagent path differs in prompt, root files and cache.

**Routing by complexity.**
- Effort can be set per subagent or skill, and so can the model. Lower effort means fewer tokens and less checking
  of edge cases. A vendor reports matching a larger model's best benchmark score at medium effort with far fewer
  output tokens.
- Model cascades cut cost sharply on non-agentic tasks. Routing from the task description alone has an error
  floor (ASSUMPTION, an abstract). Picking runs that overthink less improved results with less compute.
- A skill that names a model switches it for the turn and misses the whole cache.

**Caching.**
- A five-minute cache write costs 1.25 times base input, a one-hour write twice, a read a tenth or less. A
  five-minute entry is refreshed on each hit.
- The host gives the main conversation one hour only on a subscription and five minutes elsewhere. The lifetime
  can be chosen by setting or environment variable, separately for the main session and for subagents, and per
  subagent in its frontmatter (recent host versions).
- Static content goes first; skills and plan mode are appended and keep the cache; changing tools, model or
  (mostly) effort breaks it. A preprint measured caching cutting agent cost by two fifths to four fifths.

**Shortening instructions.**
- A recent study found context files gave no gain in success, raised cost by about a fifth and added steps, and
  advises minimal requirements only. Another associated a root file with shorter runtime and fewer output tokens
  at comparable completion.
- Compressing skills by a third to a half kept quality, and file size had no detectable effect on adherence (both
  already in `sources/references.md`).
- Shortening is low-risk where content is redundant. Only the oracle tasks can show whether content that changes
  decisions survives a cut.

**Fewer turns.** A vendor recommends one system-prompt sentence asking for independent tool calls in parallel.
Hooks can filter output before the model sees it, and scripts a skill runs do not enter context. No primary study
measures telling an agent when to stop verifying (ASSUMPTION).

## The ranked levers

1. **A five-minute cache for automated runs and subagents.** About a seventh of the reviewer's cost, no change in
   content. Interactive sessions idle past five minutes pay a re-write, so document it rather than force it.
   *Measure:* a harness arm with the lifetime set, reading the five-minute and one-hour write fields.
2. **A cheaper check phase for the reviewer.** One run per card's check, the first reads batched, a check that
   cannot run returned as a test to write, and a stated point to stop. Up to a quarter of its cost; the checks are
   evidence, so recall is the guard.
3. **The reviewer's definition.** Lower effort, an optional cheaper model, and a test of omitting the root files,
   which may hurt honouring repository overrides. *First:* run the reviewer pilot through the real subagent path.
4. **Effort on the author by complexity**, never globally, guarded by the discriminating tasks at low effort.
5. **The index toward a lookup table.** D2 saved 7 to 9 percent, with a ceiling near a fifth; routing could move
   into skill descriptions.
6. **Batched tool calls on the author**, one root-file sentence, measured in calls per trial.
7. **Card checks as scripts or hooks that print only failures**, cutting turns and output.
8. **A cache-safety rule for releases**: nothing dynamic in always-loaded files, no model named in a skill.
9. **Not recommended:** forks for the reviewer (they defeat its independence), or more subagents.
