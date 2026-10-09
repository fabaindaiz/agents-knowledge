# Consented local usage data: research (2026-10-09)

**Question.** The owner asked that a carrier may learn its machine user's usage patterns and preferences, and that the
bundle may measure whether its processes help (including agent-run cost estimates against actuals), only with the
user's prior, informed consent: what is stored, how, why and what will be done with it. Nothing may leave the machine
or enter git. This document records what primary sources say, before any design. Delegated to a read-only researcher
(sonnet); claims marked UNVERIFIED were not read in a primary source; ASSUMPTION marks the home's own inference.

**Answer first.** Every coding agent surveyed keeps learned memory per user, outside the repository; only one is off
by default. The safest place for this data is a per-user directory outside the working tree (no ignore rule needed),
with a default-off, affirmative opt-in, a one-command show/delete/disable, an explicit retention limit, and a
with/without comparison to measure it. Consent is arguably not legally required for data that never leaves its own
user's machine, but the consent elements below are good practice and cheap.

## 1. How agents store learned memory

| Agent | Where | Default | What the user sees and controls | Retention |
|---|---|---|---|---|
| Claude Code ([memory docs](https://code.claude.com/docs/en/memory.md)) | `~/.claude/projects/<project>/memory/`: an index plus topic files (user, feedback, project, reference); `CLAUDE.local.md` at the repository root, gitignored by the user | auto memory on in local sessions; a setting, `/memory`, or an environment variable turns it off | "saved/recalled N memories" messages; plain Markdown, editable and deletable | until edited or deleted; the index's first 200 lines or 25 KB load at every start |
| Codex CLI ([memories docs](https://developers.openai.com/codex/memories.md)) | `~/.codex/memories/` (summaries, entries, recent inputs, evidence; secrets redacted) | **off**; enabled in settings or config | per-chat use and contribution; one "delete memories" reset; hand edits discouraged, required rules belong in `AGENTS.md` | not stated |
| Copilot Memory ([docs](https://docs.github.com/en/copilot/concepts/agents/copilot-memory), read through a summary) | the vendor's servers: repository facts with code citations validated against the branch, and user preferences | on for individuals; administrator opt-in for organisations | view and delete; no editing mentioned | **unused entries deleted after 28 days** |
| Windsurf ([docs](https://docs.devin.ai/desktop/cascade/memories), read through a summary) | `~/.codeium/windsurf/memories/`, per workspace, never committed | automatic, or on request | view and edit; deletion not documented | not stated |
| Cursor | UNVERIFIED: the docs could not be read; forum posts say its memories were a beta stored on the vendor's servers | UNVERIFIED | UNVERIFIED | UNVERIFIED |

Staleness is answered by design in two of them: expiry plus validation against current code (Copilot), a modified
timestamp and an audit of outdated or conflicting files (Claude Code).

## 2. Keeping files out of git ([gitignore](https://git-scm.com/docs/gitignore), read through a summary)

- A `.gitignore` in any directory is **versioned and travels with every clone**: right for a public pattern such as
  `.agents/local/`, wrong for a private one.
- `.git/info/exclude` is per clone, never shared, and seen by every worktree of that clone.
- `core.excludesFile` (default `$XDG_CONFIG_HOME/git/ignore`) is per user, for every repository.
- Ignore rules do not affect a file already tracked (it needs `git rm --cached`); `git add -f` bypasses them
  (UNVERIFIED here); backup and sync tools ignore them (UNVERIFIED).
- Data kept **outside the working tree** needs no ignore rule at all, and cannot be committed by mistake.

## 3. Where per-user data lives

- [XDG Base Directory 0.8](https://specifications.freedesktop.org/basedir-spec/latest/): config in `XDG_CONFIG_HOME`
  (`~/.config`), data in `XDG_DATA_HOME` (`~/.local/share`), **state in `XDG_STATE_HOME` (`~/.local/state`)**: data that
  persists across restarts but is "not important or portable enough" for data, including action history and logs. A
  consent flag is config; learned patterns and cost logs are state.
- [macOS](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html)
  (read through a summary): `~/Library/Application Support/<app>/`.
- [Windows](https://learn.microsoft.com/en-us/windows/apps/design/app-settings/store-and-retrieve-app-data): local app
  data for data that should not roam. Mapping it to `%LOCALAPPDATA%` (not the roaming `%APPDATA%`) is ASSUMPTION.
- The bundle already keeps per-machine files in `~/.config/agent-guides/` (the carriers manifest, the private-terms
  list); a state directory beside it is the consistent choice (ASSUMPTION).

## 4. What consent must say

- GDPR ([Art. 4](https://gdpr-info.eu/art-4-gdpr/), [5](https://gdpr-info.eu/art-5-gdpr/),
  [7](https://gdpr-info.eu/art-7-gdpr/), [2](https://gdpr-info.eu/art-2-gdpr/)): consent is freely given, specific,
  informed and unambiguous, by a clear affirmative act (4(11)); purposes specified and explicit (5(1)(b)); data limited
  to what is necessary (5(1)(c)); kept no longer than needed (5(1)(e)); the request distinguishable from other matters
  (7(2)); withdrawal as easy as giving it (7(3)); bundling purposes counts against validity (7(4)).
- Art. 2(2)(c) excludes purely personal or household processing: data a person's own tool keeps on their own machine
  and sends nowhere is arguably outside the regulation, and the bundle's publisher is not its controller (ASSUMPTION;
  not legal advice). Art. 13 (what to inform) was not read: UNVERIFIED.
- Other national laws modelled on it state the same elements (free, specific, unequivocal, informed, affirmative; no
  pre-ticked boxes, no bundled purposes), from secondary sources only: UNVERIFIED.
- [Mozilla's data principles](https://wiki.mozilla.org/Data_Collection) (search snippets only, UNVERIFIED in full): no
  surprises, user control, limited data; categories beyond the essential are off by default and opt-in, documented so a
  user understands them without reading code.

**A consent prompt, synthesised** (no single source): what is recorded, by category and with an example; why; the exact
path; that nothing leaves the machine or enters git; how long it is kept; how to view, export, delete and turn it off,
with the command; that declining changes nothing else; each purpose its own choice, none pre-selected.

## 5. Measuring whether it helps

- The memory benchmarks ([LongMemEval](https://arxiv.org/abs/2410.10813), [LoCoMo](https://arxiv.org/abs/2402.17753),
  [MemoryAgentBench](https://arxiv.org/abs/2507.05257)) measure conversational recall, not whether memory helps a real
  user's work.
- A with/without ablation of repository context files for coding agents
  ([arXiv 2602.11988](https://arxiv.org/abs/2602.11988), read through a search summary: UNVERIFIED in detail) reports no
  gain or lower success at over 20% more inference cost: **stored context can hurt, so success and cost are measured
  together.**
- No published metric definitions were found for coding agents. Candidates, the home's own: repeated-instruction rate
  (the user restates a preference already stored), correction rate, recall-and-use rate, token overhead per session,
  and estimate error (actual cost over estimate).
- Design candidate: memory on and off alternated per session on the user's own machine, the metrics registered before
  the first comparison, as `evals/PROTOCOL.md` already does for the bundle; the on/off switch doubles as the consent
  control.

## What the bundle already has

`.private/` (confidential records; no tool or harvest reads it; a sentinel line), `bundle.py memory-diff` (the local
memories the repository does not hold), `bundle.py turns` (what the human said in local transcripts, read-only). None
asks for consent, states a purpose or retention, or measures usefulness.

## First data point for the estimate-and-compare loop

| Run | Model | Estimate | Actual | Ratio |
|---|---|---|---|---|
| a task review of a refactor diff | sonnet | none made | 105 s, 52k tokens, 11 tool calls | — |
| this research, five questions | sonnet | 15–20 min, 200–300k tokens | 132 s, 59k tokens, 31 tool calls | time ×0.1, tokens ×0.2–0.3 |
