# Context windows and compaction: what is lost, and what keeps it

2026-11-26, at the owner's request, to steer the next phase of the *Next* plan. Three searches in parallel: the
harnesses' own documentation, the published literature, and this home's own compactions. **Strength:** every
external page was read through a fetcher that summarises, and every paper at abstract level; no full text was read.
Figures below are second-hand from those summaries; anything marked ASSUMPTION is from memory. The local study is
one repository and one owner, judged by reading, not a controlled test.

## The question

What does a coding session lose when its context fills and is compacted, and what can the method make a session
do so that what matters survives?

## 1. What the harnesses do and say (primary docs, read 2026-11-26)

- **Claude Code** compacts by a model-written summary, automatically or on `/compact [focus]`
  ([context window](https://code.claude.com/docs/en/context-window), [how it works](https://code.claude.com/docs/en/how-claude-code-works),
  [hooks](https://code.claude.com/docs/en/hooks), [memory](https://code.claude.com/docs/en/memory)).
  - **Re-read from disk after a compaction:** the root instruction file and rules without a `paths:` scope, auto
    memory (its index's first lines), the plan of plan mode, the skill descriptions, and a handful of recently
    touched files (a large one comes back as a path only).
  - **An invoked skill's body comes back capped** (about 5k tokens each, about 25k in all), **keeping its top**:
    a skill's binding instructions belong at its head.
  - **Summarised away:** path-scoped rules, nested instruction files, and context earlier hooks injected. The
    docs say a rule that must persist drops its `paths:` or moves to the root file.
  - The summary keeps "your requests and key code snippets"; "detailed instructions from early in the conversation
    may be lost". The docs recommend persistent rules in the root file, a *Compact Instructions* section there, and
    `/compact focus on X`.
  - **Hooks:** `PreCompact` (manual or auto; its output becomes instructions to the summariser; it can block),
    `SessionStart` with matcher `compact` (its added context, kept short and phrased as facts, enters after the
    summary), `PostCompact` (cannot block).
  - Other controls: `/context`, `/clear` between tasks, `/rewind` and summarise from a point, a token threshold for
    auto-compaction; subagents keep large reads out of the main thread and return a summary; skills load on demand.
- **Anthropic's platform** ([context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing),
  [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction),
  [memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)): clearing old tool results
  is the lightest compaction (it costs a cache miss, hence a minimum per clear); a custom summarisation prompt where
  the default drops something; recent turns kept verbatim; a memory tool whose prompt says to assume interruption,
  recommended *with* compaction.
- **Anthropic's engineering posts** ([context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents),
  [long-running harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)):
  compaction should keep architectural decisions, unresolved bugs and implementation details and drop redundant tool
  output; over-eager compaction loses detail; compaction alone "does not always pass clear instructions on"; use a
  progress file, commits, a feature list in a structured format the model is less likely to overwrite, and a fixed
  start routine (where am I, the log, the progress file, the list, a smoke test); subagents return short summaries;
  retrieve just in time through references.
- **Others.** GitHub's Copilot documentation (its *context management* page) compacts at about four fifths of the
  window, keeps the original user instructions and says it loses exact wording, full command output and minor early
  decisions, irreversibly; it advises compacting between phases and a fresh session after many compactions. Cursor's
  blog (*dynamic context discovery*) calls summarisation lossy and keeps past chats as searchable files. Gemini CLI
  documents `/compress` and saved checkpoints, not what is lost. Aider has no summarise command in the pages read.
  OpenAI's API has server-side compaction to an opaque item; its CLI's compaction was found only in third-party
  sources (ASSUMPTION).

**The one recommendation every harness shares:** what must survive is written to a file the harness reads again
from disk; a summary is not a store.

## 2. What the literature measures (abstract level)

- **The effective window is much smaller than the advertised one.** Accuracy falls when the relevant item sits in
  the middle of a long input (Liu et al., *Lost in the Middle*, TACL 2024); about half of seventeen long-context
  models hold up at 32K (Hsieh et al., *RULER*, 2024); with literal matches removed, most of thirteen models fall
  below half their short-context score at 32K (Modarressi et al., *NoLiMa*, 2025); performance falls with length
  and with distractors across eighteen models, and a focused input of a few hundred tokens beats the full history
  of about a hundred thousand on a memory benchmark (Chroma, *Context Rot*, 2025, a technical report). Replicated.
- **Long multi-turn work is less reliable, and a wrong turn is not recovered.** Across six tasks and many simulated
  conversations, multi-turn performance averaged well below single-turn, mostly as unreliability (Laban et al.,
  *LLMs Get Lost in Multi-Turn Conversation*, arXiv 2505.06120, 2025). Single large study. That a consolidated
  restated prompt recovers much of it is an ASSUMPTION from memory.
- **Rewritten summaries lose detail.** *Brevity bias* (a summary drops domain detail) and *context collapse*
  (repeated rewriting erodes it); incremental structured updates to a playbook do better than whole rewrites (Zhang
  et al., *Agentic Context Engineering*, arXiv 2510.04618, 2025). Preprint.
- **Masking old tool output is as good as summarising it, and cheaper.** On a software-engineering agent benchmark,
  model summarisation did not beat hiding old observations while keeping actions and reasoning; a hybrid saved a
  little more (Lindenbauer et al., *The Complexity Trap*, arXiv 2508.21433, 2025). Optimised compression guidelines
  learned from failures cut peak tokens by a quarter to a half (*ACON*, arXiv 2510.00615, 2025). Preprints.
- **Not found:** a controlled test of keeping the user's instructions verbatim, of re-injecting constraints, or of
  subagent isolation on coding tasks; any per-kind loss rate under compaction.

## 3. What this home's own compactions lost (local transcripts)

Five automatic compactions in one long session, each at roughly four times the context the session kept afterwards;
the summary had nine fixed sections and kept a verbatim tail.

| Kind | Over five | What happened |
|---|---|---|
| Standing constraints (privacy, authorship, commits on the gate, no unasked push, the pause rule) | none lost | restated each time, and reloaded from the root file |
| Free-text answers | one distorted | kept as quotes, but a dozen answers lost the question each answered |
| Exact error text | four reduced | only the active blocker kept its text; the rest became one-line labels |
| Ids, hashes, paths | one partly lost | in-flight scratch paths and agent handles survive only while in use |
| State at the cut | two stale | a blocker recorded as current was already gone; a count was wrong and corrected to the owner next turn |
| Hand-backs arriving at the cut | five at risk | reports landed around every cut; the summary is written without seeing the kept tail |
| Decisions' reasons | five thin | outcomes kept; reasons only by pointer to a decision id or a review |
| Open questions | one kept | elsewhere folded into pending lists |

After each cut, most of the first file reads re-read files already read (they were needed to edit: the summary holds
pointers, not contents). No instruction had to be repeated by the owner.

## 3b. The same question, counted (2026-11-26, after the hooks were built)

Proposal 5 below asked for the hand reading of §3 to become a count. `bundle.py compaction` is that
probe: for each compaction it takes what the window before the cut named, and asks how much of it the
summary still names. It prints counts only — a transcript carries the account's identity and whatever
was pasted into the session, so nothing it reads is ever printed.

Over three compactions of this repository's own sessions, **before any hook was active**:

| What was in flight before the cut | What the summary still named |
|---|---:|
| Record ids | 66 % |
| File paths | 17 % |
| **The exact text of a failure** | **0 %, of twelve** |
| Files read after the cut that had been read before it | 13 % |

This is the baseline the hooks of T8 are judged against, and it agrees with the hand reading: ids
survive because they are short and repeated, and the exact text of a failure never survives — it is
reduced to a label, which is why `PreCompact` asks for it verbatim. Two cautions: three compactions of
one session is a sample of one session, and the probe counts a fact as *named* wherever it appears,
including inside a tool result, so the figures are an upper bound on what a reader would have seen.

## 4. What this means for the method (proposals, for the decision walk)

1. **The session's state lives in files at every step, not only at the close.** The decisions log already holds
   question, answer and reason by id; the gap is *when*: write each answer as it arrives (the answers-without-questions
   loss), each hand-back as it lands, and a short *where we are now* (current step, files in play and why, the last
   verified fact with the command that verified it). Evidence: every harness, Anthropic's harness post, the local
   study. Cost: a habit plus perhaps a `bundle.py` command; collides with the coding budget if it is a rule there.
2. **The compaction hooks.** `PreCompact` tells the summariser what this method needs kept (open questions with
   their question, the current step, exact error text of open failures, ids in flight); `SessionStart(compact)`
   re-injects a short fact block (the branch, the plan and its current task, what waits on the owner) beside the
   privacy rule it already prints. Evidence: the harness docs; nothing measured. Cost: hook code in the home first
   (a guard, so the owner approves its edit), then carried.
3. **Where binding text sits.** A skill's binding instructions at its head (bodies return capped from the top); no
   binding rule under a `paths:` scope or in a nested instruction file; the root file's critical lines at its start
   or end. Evidence: the harness docs, *Lost in the Middle*. Cost: an audit of the skills and the root files, cheap.
4. **Fresh contexts by design.** Delegate large reads and long loops (the subagent returns a short summary); prefer
   a fresh session with a written brief over a long one after a wrong turn or many compactions; tool output masked
   rather than summarised where the harness allows. Evidence: the literature (replicated for length, single studies
   for the rest). Cost: method text; overlaps `i-5ed7e8-55e022` (cost as a principle), `-d6ecfe` (persistent
   delegates) and `-1ac328` (the main thread's cost).
5. **Measure it.** A cheap probe: after a compaction, does the session still know the open questions, the current
   step and the last error, without re-reading? A transcript reader like the one this study used, kept as a tool,
   turns "nothing lost" from a reading into a count. Cost: a script and a few runs.

## Sources not reached

Codex CLI's official compaction docs, Cursor's current summarisation docs, Aider's history summarisation, a primary
source on the models' own context awareness, and the full texts of the papers above.
