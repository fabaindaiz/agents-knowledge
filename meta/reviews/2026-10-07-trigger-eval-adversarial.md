# The skill trigger eval, reviewed adversarially before its first run

**Date:** 2026-10-07. **Status:** review by a delegated agent, read-only, before stage 1 (`d-5ed7e8-07da79`); its
two critical findings and part of the third were fixed the same day in `evals/skills/trigger.py`, test first.
The cases are the owner's words and live outside every repository; they are cited here by count only.

## The cases that decide

`close` has ten expected cases and eight near misses, all ten expected in the owner's words. `decision-review`
has seven and six, all seven the owner's. `user-walk` has eight and six, two of the eight the owner's. For the
first two, the owner-words gate is the fire gate again.

## Findings, most severe first

1. **Critical: a session that crashed scored as a correct near miss.** Standard error was discarded, and a
   session with no tool call (a usage limit, an authentication failure) was read as quiet. A limit hit mid-run
   would have passed every remaining near miss and failed every expected case. *Fixed:* a session without an
   init event, or ending in an error result before any tool call, is an error, left out of every rate. A few
   errors in a row stop the run. A watchdog ends a session that hangs.
2. **Critical, safety: the refusing hook listed eight built-in tools.** A connector's tools passed, including
   tools that launch processes, write files or write to a tracker. A near miss asking to push or commit could have
   acted through one. *Fixed:* the hook allows by name (read, search, the skill tool, tool search, the to-do
   list) and refuses everything else.
3. **High: "the skill tool as the first call" undercounts.** A host may load a skill by reading its file. A
   router skill that asks to run before any response, or a to-do call, may come first. The lenient window was
   three calls. *Fixed:* reading the skill's file counts as invoking it. A routed metric looks past router skills
   named with `--router` and past the preamble calls. The window is five calls. *Open:* letting read-only git
   commands run in the fixture.
4. **High: the requests have nothing to refer to.** Most expected decision-review cases point at "those points"
   or "all this", and one names a spec that does not exist. Close requests land in an empty repository with
   nothing to commit. The carrier's root file is not copied, while the owner's global instructions, which hold
   their own closing procedure, are. *To do before stage 1:* a fixture with a spec with open decisions, a plan
   and an uncommitted change, plus the carrier's root file, all kept outside the repository.
5. **High: power.** In stage 1 one misfire fails the gate, and zero of eight near misses still has an upper
   bound near a third. A skill with a true fire rate of 0.9 and a misfire rate of 0.05 passes stage 1 about half
   the time, and all three together about a fifth: a stage-1 fail is the expected outcome. Three runs raise this
   to between two thirds and nine tenths, and runs of one request are correlated. *So:* stage 1 is a screen,
   never a verdict. Stage 2 also reports cases passed by per-case majority and a bootstrap over cases. All three
   skills are present in every session, so one pass over the pooled requests can score all three.
6. **Medium: leakage and homogeneity.** Raw shared words with the descriptions are few. The agent-written
   user-walk cases carry about twice the description's concepts of the owner's, reading as translations of it.
   Two near misses mirror the description's own exclusions. All ten close cases share one verb, and six of seven
   decision-review cases hinge on one adverb: one phrasing, not seven cases.
7. **Medium: near misses too easy, and labels to check.** Four near misses no skill would fire on. Two expected
   user-walk cases may belong to a brainstorming skill, which the user-walk description itself excludes. One
   close case is a question. One decision-review case asks for the review after the plan, so a correct model
   would not call the skill first.
8. **Medium: the listing, the model, headless mode.** The listing's budget follows the model's context window,
   and over a hundred skills compete, so the model must be pinned (*fixed:* `--model`). The version and what the
   session loaded are recorded (*fixed*). A canary case naming each skill outright tells a broken setup from a
   weak description (*fixed:* a canary that does not fire makes the run invalid). Headless sessions have no
   history, so close, which comes at the end of a long session, is measured at its easiest.
9. **Low.** A plugin skill sharing a name would count as ours; none exists today.

## Public guidance (paraphrased)

A skill-authoring tool's own trigger eval uses about twenty queries, half near misses sharing keywords, a train
and test split, three runs per query, and a per-query threshold of one half. It counts a skill call or a read of
the skill's file, judged on the first tool call. The assistant's plugin-eval documentation compares sessions
with and without the plugin, three runs per case. It starts from an empty workspace with read-only tools, and
warns that usage-limit errors score zero without notice.

## The delegated agent's prediction for stage 2 (not the registered one)

`close`: strict fire 0.6 to 0.85, misfire 0.05 to 0.15, a pass about even. `decision-review`: strict 0.4 to 0.7,
likely fail. `user-walk`: agent-written cases at least 0.8, the owner's captured by a brainstorming skill,
likely failing the owner gate. The registered prediction is written before stage 2, after the fixture.
