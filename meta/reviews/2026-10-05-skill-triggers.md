# Will the method's skills fire on the owner's requests, and stay quiet otherwise?

**Date:** 2026-10-05. **For:** `i-5ed7e8-578c22`. **Status:** research; no live model was run.

## How a skill is selected (Claude Code docs, fetched 2026-10-05)

- **The model reads a listing** of names with `description` (plus `when_to_use`, appended), cut at 1,536 characters
  per skill; the body loads only on invocation. The docs describe no ranking engine; their advice is to put the key
  use case first, in the words users say. Skills tend to under-trigger and are skipped for one-step requests.
- **The listing has a budget** (a fraction of the context window, default one hundredth); over it, descriptions are
  shortened to fit (the settings reference). The research agent read the skills page as dropping the least-invoked
  skills' descriptions first, which would hit a newly installed skill first; a second reviewer could not confirm the
  order (ASSUMPTION until checked in the client's diagnostic view). Whether a given machine overflows
  is visible in the client's context and diagnostic views, and is not measured yet.
- **Precedence by name only decides which skill a slash command runs**; for automatic invocation every listed
  description competes in one prompt. A carrier cannot demote a plugin's skill from its own settings.
- **A general-purpose workflow plugin's start-of-session text** asks the model to invoke any skill that might apply
  and to run its own process skills first. In the owner's history its brainstorming skill took turns that
  `user-walk` now claims (batches of real-use observations, a usability pass), and its branch-finishing skill fired
  where `close` is meant to be offered.

## What `evals/skills/trigger.py` measures, and what it does not

It runs one fresh headless session per case in an empty repository and scores the first tool call. Limits: it hides
most tools from the model (a bare-name disallow removes them from context), scores only the first call, has none of
the carrier's own skills or root file, and no conversation history — so "offer close before a push that ends a plan"
cannot be tested. One run per case cannot clear a 0.8 threshold statistically (fourteen of fourteen gives a Wilson
lower bound near 0.78).

**A contradiction to settle:** 0.0.27's `close` description offers the close before a push that ends a plan, while
the roadmap lists a bare push as a near miss; a fresh session cannot see a plan ending. Resolved in 0.0.28 by
wording the offer as a question asked once, and keeping a bare push quiet.

## Draft held-out cases

About eighty scored cases (close, decision-review and user-walk, mostly in the owner's language, paraphrased) plus a
dozen ambiguous ones that need the owner's label, with tune and held splits. They are kept outside the repository:
they belong in the pilot carrier beside its `LOCAL.md`, and only the held half scores.

## Recommendations

1. **Lead each base description with its trigger, and name the neighbour that wins today** (applied in 0.0.28).
2. **A carrier adds the owner's phrases as `when_to_use` in `LOCAL.md`, rather than replacing `description`**, so later
   base fixes still reach it (`method/skills/README.md`, 0.0.28).
3. **Before trusting any eval, check that the three descriptions are in the listing.**
4. **`trigger.py`:** keep the tools visible by denying through a hook instead of hiding them; add a lenient metric
   (fires within the first three calls, before any write); run in a copy of the carrier's `.claude/` with a fixture;
   repeatable runs with Wilson intervals and a table of which competitor captured each case; an optional arm that
   resumes a real transcript.
5. **Protocol:** one pilot carrier with the plugin on; stage 1 one run per case, stage 2 three; pass at fire ≥ 0.8
   and misfire ≤ 0.1, the owner's-language cases alone ≥ 0.8, intervals reported; a prediction written before
   stage 2. Cost (ASSUMPTION): a couple of hours of runs and twenty minutes of the owner's labelling.

## References (opened 2026-10-05)

Claude Code docs: *Skills*, *Settings reference*, *Plugin evals*, *CLI reference*, *Permissions*, *Hooks*; Anthropic's
skill-authoring best practices; Anthropic's skill-creator guidance (ideas only). The bundle's own skill bases,
`merge_skill`, `evals/skills/trigger.py`, and the owner's extracted turns (used as aggregates and paraphrases only).
