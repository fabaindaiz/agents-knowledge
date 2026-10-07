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

## Verified against the primary text, the same day

The host's skills documentation, downloaded whole, confirms the listing's budget: one percent of the model's
context window, descriptions dropped from the least invoked skills first, every name always kept, a warning in
the debug log when the listing overflows. A setting raises the fraction, and per-skill overrides set a skill to
show its name only, or to be hidden. A summarising fetch of the same page had answered that no automatic dropping
exists, which is wrong; the primary text was read instead. The consequence for the eval is that the budget follows
the pinned model. A smaller context window drops more descriptions, so the model is pinned to the one the owner
works with, and the debug warning is read to know whether the listing overflowed.

## Done before stage 1

- The cases, relabelled and partly rewritten as the owner decided (`d-5ed7e8-44de5f`), with one canary per skill.
  Expected and near-miss counts per skill, by the clear cases that decide: `close` nine and eight, `decision-review`
  six and five, `user-walk` six and six. `user-walk` has none of the owner's words left among its clear expected
  cases, so its owner gate does not apply and its fire rate rests on written cases.
- A fixture outside every repository: a spec with five open questions, a half-done plan and uncommitted source,
  plus the carrier's root files and release.

## Stage 1, a screen (one run per case)

The owner's default model, pinned; the carrier's skills from its release branch; the fixture; the router skill
looked past. No session errored, and every canary fired, so the setup measured something.

| Skill | Strict fire | Misfire | Owner's words | Screen |
|---|---:|---:|---:|---|
| `close` | 9 of 9 | 0 of 8 | 9 of 9 | pass; the ambiguous cases agreed with their labels, 6 of 6 |
| `decision-review` | 2 of 6 | 0 of 5 | 2 of 6 | fail |
| `user-walk` | 5 of 6 | 0 of 6 | none left | pass |

Every expected `decision-review` case that did not fire, and most near misses in every skill, began with a shell
call, which the hook refused and which ended the window. The eval did not record the command, so it is not known
whether the session was looking before choosing. *Fixed before stage 2:* a shell command that only reads runs and
is recorded, and does not end the window; anything else is refused as before. Stage 1 is a screen, so it decides
nothing: stage 2, with three runs, a written prediction and the trimmed-listing arm, does.

## Stage 2: the trimmed arm, set up and checked before any run

The host's skills documentation, fetched whole the same day, says per-skill overrides in a project's settings set
a skill to show its name only, and that **plugin skills are not affected by them**: a plugin is turned on or off
as a whole. The arm was built within that limit and probed with one-word sessions on the pinned model, reading
the debug log's listing warning:

| Setting in the copied `.claude/settings.json` | Skills listed | Listing against its budget |
|---|---:|---|
| none (the current listing, the carrier's skills included) | 117 | about 44k characters, over the 30k budget |
| the host's bundled skills set to name only | 117 | about 34k, still over |
| the bundled and the account-synced skills set to name only (54 overrides) | 117 | under the budget, no warning |

Overrides keyed by the synced skill's bare name and by its prefixed name both took effect (each hid its skill
when set to off). Turning the plugins off would also fit the budget, but it removes a router and the closest
competitors, so it measures a different machine; it was not used. No carrier skill, no method skill and no plugin
skill is overridden. Which descriptions the current listing drops is not logged; that the carrier's are among
them is an ASSUMPTION the trimmed arm tests.

## Stage 2: the registered prediction, written before any run

Both arms, three runs per case, the owner's default model pinned, the router looked past, the same fixture and
cases as stage 1. Each skill is judged by the eval's own gate; cases are also reported by per-case majority (two
runs of three).

| Skill | Current arm, strict fire | Misfire | Gate | Trimmed arm against current |
|---|---|---|---|---|
| `close` | 0.85 or more | 0.05 or less | pass | within 0.1 either way |
| `decision-review` | 0.3 to 0.6 (lenient 0.5 to 0.8) | 0.1 or less | fail on strict fire | 0 to 0.2 higher |
| `user-walk` | 0.7 to 0.9 | 0.05 or less | about even | within 0.1 either way |

The reasoning: `close` passed its screen with every case and its words are distinctive. `decision-review`'s
requests point at material, so a session now allowed to read before choosing will often read first, which the
strict metric scores as a miss. `user-walk` lost its one miss in the screen to a brainstorming competitor that no
override reaches. The trimmed arm should not lower any fire rate; it raises one only where the current listing
had dropped that skill's description.

**What it decides.** `d-5ed7e8-4c80c1` already advises trimming. If the trimmed arm lowers any skill's strict fire
by more than 0.1, or raises any misfire by more than 0.05, the advice is reopened. If the arms do not differ,
the advice stands on the listing's size alone, about a third smaller on every turn. If a skill fails its gate
in both arms, its description is rewritten before 0.0.30 ships it, and its cases are not.
