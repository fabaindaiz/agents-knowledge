---
name: brief
description: "Use when work is about to be handed to a delegated agent, or a lane of a plan is about to start: it composes that agent's brief from this session's live state — the plan, the files in play, the last fact actually verified — and leaves a visible gap wherever only the session knows the answer. Not for deciding whether to delegate, and not for splitting work into lanes, which is `lanes`."
release_description: "Use when work is about to be handed to a delegated agent or a lane is about to start: composes the brief from the session's live state and leaves a visible gap where only the session knows. Not for deciding whether to delegate."
allowed-tools: Bash, Read, Grep, Glob
---

# Brief

A delegate knows only what its brief says. The brief is usually retyped from memory at the end of a long
session, which is when memory is worst, and what goes missing is never the goal — it is the scratch
directory, the price, and the files another lane is writing. This skill composes the brief from what the
session has already written down about itself, and marks what it cannot know.

## 1. Compose it, do not retype it

```bash
python3 .agents/tools/bundle.py brief --task "ONE LINE"
```

It reads this session's live state (`bundle.py now`) and fills the plan, the branch, the files in play and
the last fact actually verified with the command that verified it. Those four are where a retyped brief
goes wrong: a delegate sent to re-derive something already settled spends its budget twice.

**If the live state is empty, write it first** (`bundle.py now --write`). The brief is only as good as it,
and a session with no live state is the one whose delegates go out least equipped.

## 2. Fill every gap, or say why it is empty

What the tool cannot know it prints as `<< ... >>`:

| Gap | Why it is the session's and not the tool's |
|---|---|
| the task | What comes back, not how to get it. A brief that prescribes the method gets the method back |
| what is already settled | The delegate cannot know what this session ruled out, and will rule it out again |
| what not to change | The files another lane holds. Nothing stops a delegate from writing them |
| the scratch directory | **Outside the repository**, always, for any delegate that writes or downloads |
| the price | Model, tokens and wall time, stated before launching, compared when it returns |
| what comes back | A report, a branch, a file. Unsaid, it comes back as prose that has to be re-read |

**Nothing here is checked.** The command never refuses an incomplete brief, by design: the gap in the
printed text is the whole guard. A gap deleted rather than filled is a decision taken in silence, so
delete one only by writing in its place why it is empty.

## 3. The cheapest model the task allows

Price before launching, not after. A read-only delegate — search, verification, a review — is cheaper and
needs no branch; one that writes gets a branch and a scratch directory of its own.

## 4. Then hand it over, and keep its row

Paste the brief into the call that launches the delegate. While it runs, this session carries its row:
task, model, start, expected duration, what waits on it — and `bundle.py now --write --delegates` keeps
that row where a compaction cannot lose it.

Splitting work into lanes in the first place is `lanes`; this skill starts where that one ends.
