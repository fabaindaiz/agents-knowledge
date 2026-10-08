---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-03af58edfc
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.30
digest: 1aa036d637af
kind: method
action: new
target: ask-the-design-decisions-before-designing
lacks: a second occurrence; whether it overlaps the pre-flight rule in prompt-context.md; whether recommended-first anchors the answer
seen: "2026-10-08"
---

For an open design question, an answer that first explains the few decisions that change the design, each in plain words with its options priced and the recommended one first, and then designs from the user's decisions, is preferred to a complete answer given at once, and it is the only form that contains the risks of the user's non-default choices.

## Evidence

The same design question was answered a fourth way: a fresh agent with the full knowledge base prepared eight decisions with priced options and decided sixteen smaller ones by default; the user answered, and the agent wrote the design from the answers. The user took the recommended option, always listed first, in three decisions in four. For the two deviations, the design added containment for each non-default choice that none of the three single-shot answers had: ambiguous cases removed at their source, an independent sampled check of automatic decisions, a per-unit switch back to the stricter mode, and, for retained inputs, a separate store with its own retention rules and an evaluation set sampled in advance. Asked afterwards, the user preferred this format to all three single-shot answers. Costs: eight answers from the user and a design about twice the length of the shortest answer.
