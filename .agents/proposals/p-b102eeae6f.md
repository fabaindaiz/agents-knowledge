---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-b102eeae6f
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.29
digest: 61942017fec6
kind: method
action: extends
target: prompt-context
lacks: the wording in §15, decision-review and the planning step; a measure of misreadings caught, in the trigger eval or a pilot
seen: "2026-10-07"
---

Building a plan and walking decisions are where the method learns most from the human, and the human is their final reviewer: the one who holds the knowledge to decide, but not the agent's context, and who must read and understand everything asked. So a review turn has a fixed shape. It holds three to five short blocks of about three lines each: what is being decided, why it matters, the options each with its concrete case, the recommendation, and the question; anything longer is offered behind *explain this more* instead of written up front. Every question, in a decision walk or batched, carries one extra answer, *review more*, which opens a second level instead of explaining everything up front: *I do not understand it* (another example, in smaller pieces), *I think something is wrong* (the assumptions listed, for the human to mark the one that fails), *options are missing* (others, or a middle ground) and *I need context* (where the decision comes from and what depends on it); each mode returns to the original question. One option rather than several leaves three of the question tool's four for real options. After a decision that is costly or irreversible, or a long explanation, a one-click comprehension check comes before it is recorded: which of these describes what will happen, one answer right and the others plausible, and a wrong pick is explained again rather than recorded. Before a plan is written, the skills relevant to it (from the catalogue of `p-480f968069`) are offered as a short table, each with what it is for here, how it would be used and its cost, followed by a multi-select question on which to use. This lands in `prompt-context.md` §15, the `decision-review` skill and the planning step.

## Evidence

Asked by the owner on 2026-10-07, each part decided by them in a walk run in the proposed format (`meta/decisions.md`, d-5ed7e8-88e016 to d-5ed7e8-0fec6e; the first form, two fixed answers, d-5ed7e8-d34899, was superseded the same day). Health-literacy practice (chunk and check, teach-back) holds that information given in a block is often forgotten or misremembered, and that checking each small chunk catches it; plain-language guidance holds that readers scan; human-agent planning studies find people trust plausible plans without checking them. Sources and their limits in `meta/reviews/2026-10-07-review-turn-format.md`.
