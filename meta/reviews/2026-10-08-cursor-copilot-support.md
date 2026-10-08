# What supporting Cursor and Copilot takes (2026-10-08)

Roadmap item `i-5ed7e8-fca056`; scope decided by the owner (`d-5ed7e8-0ff9eb`, then `d-5ed7e8-1e7a9a`: levels 1
and 2 joined 0.0.30 as experimental support, and level 2's items 1 to 3 and 5 were built that day, as
`bundle.py surfaces`). **Level 1:** the method says what to
write for each assistant. **Level 2:** the bundle generates and checks each assistant's surfaces from one source.
**Level 3:** the bundle's efficacy is measured with each assistant's own CLI. Levels 1 and 2 are built and level 3
is designed in 0.0.30's successor; 0.0.30 closes with this document, the item and the method's table corrected.

## Method

- Three mid-size-model agents ran read-only.
  - Two answered from the vendors' primary documentation, fetched whole as Markdown into a scratch folder outside
    the repository: Cursor's documentation pages and GitHub's documentation sources, plus the VS Code docs.
  - One surveyed the assistant surfaces of the six work carriers open on this machine, read-only.
- The main session verified each load-bearing claim by searching the fetched pages. Those claims are: the Claude
  locations each vendor reads, the CLI flags, and the isolation variables.
- What no fetched page states is marked **ASSUMPTION**, with the test that would settle it.
- Carriers are counted, never named.
- Sources are paraphrased and listed in `sources/references.md`, *Writing for an agent*.

## Findings

### 1. Both assistants now read most of what the bundle writes for Claude Code

| Bundle piece | Cursor | Copilot |
|---|---|---|
| Root `AGENTS.md` | read, root and nested, the more specific winning | read; the nearest wins. Coding agent, code review, CLI and JetBrains read it; VS Code reads it with nested files off by default; Visual Studio and GitHub.com chat are not documented (**ASSUMPTION**: not read) |
| Root `CLAUDE.md` importing `@AGENTS.md` | the CLI reads both at the root; the IDE is not documented | the CLI, the coding agent and code review read it, with `@` imports, and the CLI drops identical copies; VS Code only behind a setting |
| Skills in `.claude/skills/` | loaded for compatibility, beside `.cursor/skills/` and `.agents/skills/`; `name` must equal the folder (the bundle's three do) | loaded beside `.github/skills/` and `.agents/skills/`, on the coding agent, code review, CLI, VS Code and JetBrains |
| The reviewer in `.claude/agents/` | loaded for compatibility as a subagent with its own context; a same-named `.cursor/agents/` file wins; tools restricted only by `readonly: true`, no per-tool list | loaded as a custom agent; the CLI runs it as a subagent with its own context; its `tools` list uses Copilot's aliases (`read`, `search`, `execute`…) |
| Hooks in `.claude/settings.json` | loaded and mapped (`Bash` becomes `Shell`, exit code 2 denies); the IDE runs them; the cloud agent runs command hooks only; on the Linux CLI they are reported to fail silently (**ASSUMPTION** until a canary runs) | the CLI reads them; VS Code only behind a setting, and it ignores matchers; the coding agent reads `.github/hooks/*.json` |
| `permissions.deny` | only the CLI's own (`.cursor/cli.json`); `.cursorignore` is not a boundary for the terminal or MCP | none; content exclusion is set in the organisation's settings, and VS Code's agent mode does not honour it |
| Per-area rules (`.claude/rules/` with `paths:`) | `.cursor/rules/*.mdc` with `globs`, or a skill's `paths` | `.github/instructions/*.instructions.md` with `applyTo` |
| A review on a pull request | the review bot reads `.cursor/BUGBOT.md`, not the `.mdc` rules | code review reads `AGENTS.md` and the repository's instructions |

**What follows:** the one-source design already reaches both assistants on most surfaces, through `AGENTS.md` and
through the Claude locations both vendors now read for compatibility. The gaps are narrower than the table of
2026-09-24 implied:
- the reviewer's tool restriction;
- hooks on two surfaces;
- the deny list;
- per-area rules written three times by hand.

### 2. The carriers write those surfaces by hand, and nothing checks them

Six of six:
- **Root files:** an `AGENTS.md` source, with a `CLAUDE.md` that imports it.
- **Cursor:** eight to thirteen numbered `.mdc` rules, mostly attached by glob, written by hand.
- **Copilot:** a short `copilot-instructions.md`, a hand-written pointer to `AGENTS.md`.
- **Generation:** none of these surfaces is generated, and no script, hook or CI step writes or compares them.

Four of six:
- A per-language Copilot instructions file.
- A `.claude/rules/` folder that repeats the `.mdc` area rules by hand. The one pair compared differed only in its
  frontmatter.

Dates:
- **Copilot:** in four, the Copilot file is the oldest surface, months behind `AGENTS.md`.
- **Cursor:** many `.mdc` rules have not moved since the bootstrap.

Five of six carry an audit that fails a dead pointer in any always-on surface. That checks links, not content.

The bundle's pieces reach both assistants only through `AGENTS.md`: the knowledge line, the privacy reminder, the
reviewer's name and the skills. That works wherever `AGENTS.md` is read (finding 1). In all six, the session log
lives under the Cursor folder, not the bundle's default, which the `log` field now names.

### 3. Measuring with their CLIs is possible, with one missing number

| | Cursor CLI (`agent`) | Copilot CLI (`copilot`) |
|---|---|---|
| Install | an install script into the user's bin folder | an npm package, or an install script |
| Auth | an API key in the environment | a fine-grained token with the Copilot-requests permission |
| Headless | `-p`, edits applied only with `--force` | `-p` with `--no-ask-user` and the allow flags |
| Output | JSON, or a stream with tool-call events | JSON lines; a transcript file with `--share`; tool calls and tokens in the JSON are not documented (**ASSUMPTION**) |
| Tokens or cost per run | **not in any documented schema** | not documented; a soft cap per response exists |
| Same model as Study 1 | Claude models offered | Claude models offered; Sonnet 5.5 by default |
| Isolation | config folder by environment variable; no flag excludes user rules or the compatibility imports (**ASSUMPTION**: a fresh home is needed) | a home-folder variable replaces the user's config; a flag turns off repository instructions, which gives the `minimal` arm |
| Billing | usage at API price inside a plan | usage-based credits per token and model |

**What follows:** both CLIs can run the harness's tasks with the same model as Claude Code. That separates the
assistant's harness from the model, which no run so far could.
- **Cursor:** gives no cost per run, so its cost line would need its dashboard or token counts read elsewhere.
- **Copilot:** reports cost only as an undocumented text summary.

Adherence counts work where tool calls are logged: Cursor's stream, and Copilot's transcript file.

## The gaps, by level

**Level 1, the method.** For 0.0.30:
- The table *What each surface can actually do* is corrected with finding 1. It now names the Claude locations
  both vendors read, the hooks in VS Code, `CLAUDE.md` in the CLIs, the review bot's own file and the change in
  billing.
- *Three agents, one source* gains the conclusion: write once in `AGENTS.md` and the Claude locations; generate
  only what has no common location.

For 0.0.31: the bootstrap's title and the prompts that say "Claude Code" where they mean any assistant.

**Level 2, the tools**, for 0.0.31, in order of what each closes:

| # | Gap | Work | Size |
|---|---|---|---|
| 1 | Per-area rules hand-written two or three times, drifting | `bundle.py surfaces`: generate `.cursor/rules/*.mdc` (`globs`) and `.github/instructions/*.instructions.md` (`applyTo`) from `.claude/rules/*.md` (`paths:`), each marked generated; `verify` fails a stale or hand-edited copy | the largest: a converter, a freshness check, tests, and a migration a carrier runs once (its hand-written rules compared with their sources first) |
| 2 | The reviewer's tool restriction holds only in Claude Code | the update writes `.cursor/agents/knowledge-reviewer.md` with `readonly: true` and `.github/agents/knowledge-reviewer.agent.md` with Copilot's tool aliases, both generated from the one template; the researcher likewise | small |
| 3 | Copilot pointer files go stale | a generated `copilot-instructions.md` holding only the pointer to `AGENTS.md` and the privacy line, or none at all where every surface in use reads `AGENTS.md` | small |
| 4 | The privacy and commit hooks reach Cursor's IDE and Copilot's CLI by compatibility, not the rest | keep the guarantee in git hooks and CI (rung 3), as principle 2 already says; generate `.github/hooks/` and `.cursor/hooks.json` only where an assistant's own surface lacks the import | small, after the canaries |
| 5 | `install-skills` writes only `.claude/skills/` | nothing, since both vendors read it; verify the frontmatter each ignores (`allowed-tools`) is harmless | none, a test |
| 6 | `memory-diff` and `turns` read only Claude's local memory and transcripts | their stores, located and read where documented | research first |
| 7 | The review bots on pull requests | a generated `.cursor/BUGBOT.md` pointing at the knowledge index, if the owner uses that bot | small, optional |

**Level 3, measurement**, designed in 0.0.31:
- **Harness:** an adapter per CLI in `evals/harness.py`. Its invocation and its trace parsing live in one place each.
- **Isolation:** a fresh home per trial.
- **Model:** the same Claude model as Study 1.
- **First run:** a pilot of pilot-12's three discriminating tasks with `minimal` and the current release in each
  assistant. Registered before any trial, like every run.
- **Its outcomes:** passes, and adherence from the logged tool calls.
- **Cost:** Copilot's from its usage, if its JSON carries it; Cursor's only once a source for it is found.
- **Blocked on the owner:** installing both CLIs, an API key for one and a token for the other, and each account's
  terms for automated runs (already on the owner's list).

## Open questions, each with its test

| Question | Test |
|---|---|
| Does the Cursor IDE read `CLAUDE.md`? | a canary line in a scratch repository's `CLAUDE.md`, asked for in the IDE |
| Do Claude-format hooks run in the Cursor CLI on Linux? | a canary hook that writes a file, in a headless run |
| Does Copilot's JSON output carry tool calls and tokens? | one headless run, its output read |
| Does a Cursor subagent with `readonly: true` refuse an edit? | a scratch run asking the reviewer to edit |
| Does Copilot honour the reviewer's Claude-format `tools` field, or ignore it? | the same, in the Copilot CLI |
| Does reading both `AGENTS.md` and a `CLAUDE.md` that imports it load the root file twice? | token counts with and without `CLAUDE.md`, once the cost source is known |
