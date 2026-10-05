# How the knowledge index should scale

**Date:** 2026-10-05. **Status:** research; feeds `i-5ed7e8-1ac328` (consulting cost) and the reviewer's budget.
Figures are estimated tokens as the home's `report` counts them (characters / 4), measured on release 0.0.27.

## Where the tokens are

| Part of `INDEX.md` (50 notes, 58 lookup rows) | Est. tokens | Share |
|---|---:|---:|
| *By what you are about to do* (the lookup) | ~3,650 | 61% |
| *By phase of work* (slugs only since 0.0.27) | ~1,000 | 17% |
| Prose: preamble, how to use, areas, how well founded, keeping usable, not here | ~1,300 | 22% |
| **Whole file** | **~5,950** | |
| Reviewer before any card (its prompt plus the index) | ~6,570 | budget 6,900 |

- In the lookup, the card link `[slug](cards/slug.md)` writes the slug twice: about 30% of the table.
- Rows are already short (median about 200 characters); **growth is in the number of rows**, so a row cap is a
  drift guard, not a way to scale.
- Each new note costs every reader of the index about 90 tokens; the reviewer has room for about three more.
- A subagent also loads the carrier's root instruction chain unless its definition opts out, so the
  reviewer's budget is a floor, not its whole load.

## What the literature and vendors say

- **Progressive disclosure** is the vendors' answer to this shape: names and descriptions always loaded,
  bodies on trigger, references one level deep from the entry file (Anthropic's Agent Skills docs and
  best-practice page). Deferring tool definitions pays above roughly ten thousand tokens of them, and
  raised selection accuracy there (Anthropic, tool search, 2025-11-24).
- **Lazy loading fails at the decision to load.** In one vendor's evals a skill the agent had to decide to
  invoke was not invoked in about half the cases, while a compressed passive index in the instruction file
  scored best (a vendor blog on one framework, 2026-01-27; not peer reviewed).
- **Retrieval or two-stage routing pays at hundreds or thousands of items** (RAG-MCP, 2025; MCP-Zero, 2025;
  Repantis et al., 2026); off-the-shelf retrieval is weak at tool retrieval (Shi et al., ACL 2025), so a
  similarity search would inherit that weakness.
- **Length and accuracy at this size:** degradation is measured at tens of thousands of tokens (NoLiMa,
  ICML 2025; Chroma's context-rot study, 2025); a factorial study of configuration-file size found no
  effect on adherence (McMillan, 2026). **So reshaping the index is about cost and headroom, not accuracy**,
  and a reshaping that adds a decision point can lose accuracy.
- **Cost mechanics:** a cached write costs about 1.25× base input and a read about 0.1×, so a file read once
  and carried for ten more calls costs about thirteen times its size in base input; input, not output,
  drives agent cost (Bai et al., 2026).

## Designs, priced

| Design | Hot read | Reviewer now | Notes of headroom |
|---|---:|---:|---:|
| D0 today | ~5,950 | ~6,570 | ~3 |
| D1 slug-only cells in the lookup too | ~5,330 | ~5,950 | ~11 |
| **D2 `INDEX.md` is the lookup; phases and prose move to a generated `knowledge/PHASES.md`** | ~3,100 | **~3,730** | ~50 |
| D3 topic slices behind a router | router ~475 + slices | ~1,425–4,460 | — |
| D4 slices by action class | ~1,100–2,000 | | — |
| D5 `bundle.py lookup` by code | ~100 + ~60 per card | flat | — |

What each breaks: D1 the carrier-side reachability rule (it must accept slug cells, with a planted test),
`render_index` and the reviewer's step 2. D2 adds the template split and two generated files, keeps the path
`knowledge/INDEX.md` as the entry point (no root-file line, `Reads:` list, skill or harness changes), and
should lower the reviewer budget to measured plus a tenth in the same release, with a lookup budget and a row
cap as drift guards. D3/D4 add a second routing decision (actions matched to subjects), two-hop reachability
and per-slice budgets. D5 adds a command an agent must decide to run.

## Recommendation

1. **Adopt D2 next, measured through pilot-9, not as a side effect.** It halves every hot read, gives the
   reviewer about fifty notes of headroom, changes no path, and adds no decision point.
2. **Do not slice by topic now.** Revisit when the lookup passes about six thousand tokens (about a hundred
   notes), measuring action-class slices against D2.
3. **Keep `bundle.py lookup` only as a filter on a closed vocabulary**, with the D2 lookup as its fallback;
   never a similarity search.
4. **Record the reviewer's unmeasured load** (the carrier's instruction chain) as a gap of the review budget.

## The experiment that would decide it

- **Pilot-9 (already registered):** add an arm with D2's index. Predicted: non-trivial tasks at most ×2.0 of
  the unaided cost (refuted above ×2.2), every discriminating task passing as often as before, trivial tasks
  within ×1.2.
- **Pilot-R (new, reviewer only):** about twenty fixed diffs (each target note's naive and reference diff,
  the boundary tasks, the neutral ones); arms R0 (today), R2 (D2), R4 (action-class slices, never shipped);
  outcomes: target card opened, raised on the naive diff, raised as blocking on the reference diff, cards
  opened on neutral diffs, tokens before the first card. Predicted: R2 at most 0.6× R0's tokens with equal
  recall; R4's recall is the open question. The cheapest arm with R0's recall and no more over-application
  decides.

## Open

Whether the phase table is used at all (no transcript count exists); whether the *wrong when* column earns its
~1,400 tokens; a tokenizer count to calibrate the chars/4 budgets; how the reviewer's recall falls as diffs grow.

## References (each opened on 2026-10-05 by the research agent)

Anthropic: *Equipping agents for the real world with Agent Skills* (2025-10-16); Agent Skills overview and
best-practice pages; Claude Code docs, *Skills* and *Subagents*; *Introducing advanced tool use* (2025-11-24);
*Effective context engineering for AI agents* (2025-09-29); prompt-caching docs. OpenAI Codex docs on
`AGENTS.md` (a 32 KiB default cap). Vercel blog, *AGENTS.md outperforms skills in our agent evals* (2026-01-27).
Li et al., *Retrieval Augmented Generation or Long-Context LLMs?*, EMNLP 2024 (arXiv 2407.16833). Yin & Feng,
2026 (arXiv 2607.13034). Gan & Sun, *RAG-MCP*, 2025 (arXiv 2505.03275). Fei et al., *MCP-Zero*, 2025 (arXiv
2506.01056). Repantis et al., 2026 (arXiv 2605.24660). Shi et al., *ToolRet*, ACL 2025 (arXiv 2503.01763).
Hong et al., *Context Rot*, Chroma, 2025. Modarressi et al., *NoLiMa*, ICML 2025 (arXiv 2502.05167). McMillan,
2026 (arXiv 2605.10039). Bai et al., 2026 (arXiv 2604.22750). ASSUMPTION: the per-note growth rate stays at
today's, and the share of the consulting overhead due to the index scales linearly with its size.
