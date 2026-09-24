# evals — does the bundle change what an agent does?

The experiment behind roadmap item `i-5ed7e8-0d9b6a`. [`PROTOCOL.md`](PROTOCOL.md) is the
pre-registration: the question, the arms, the task rules, the analysis and what each result would mean.
This folder is not part of the bundle and never travels to a carrier.

| File | Does |
|---|---|
| `harness.py` | validates the tasks, freezes a plan, runs trials in isolation, grades them |
| `analyze.py` | the pre-registered analysis of a run |
| `power.py` | Monte Carlo power, to size the run before it happens |
| `tasks/<id>/` | `task.json`, `prompt.md`, `AGENTS.minimal.md`, `repo/` (the start), `hidden/` (the grader), `naive/` and `reference/` (overlays that prove the grader discriminates) |

## Running it

Once per machine, a clean Claude configuration directory that holds credentials and nothing else:

```bash
mkdir -p ~/.config/agent-guides/eval-claude && chmod 700 ~/.config/agent-guides/eval-claude
CLAUDE_CONFIG_DIR=~/.config/agent-guides/eval-claude claude   # log in, then exit
```

No API key is needed: the login is the Claude subscription. For a headless machine, `claude setup-token`
prints a long-lived subscription token; export it as `CLAUDE_CODE_OAUTH_TOKEN` and the harness passes it
through (so does `ANTHROPIC_API_KEY`, if you have one). For an exploratory run, `--config-dir default`
reuses the logged-in `~/.claude` with user settings excluded; run `probe` to confirm what each arm loads.
Then:

```bash
python3 evals/harness.py check                                  # every task's grader is seen to fail and pass
python3 evals/harness.py plan evals/runs/pilot --model MODEL --reps 2
python3 evals/harness.py probe evals/runs/pilot                 # which instructions each arm loads
python3 evals/harness.py run evals/runs/pilot --limit 5         # resumable; drop --limit to finish
python3 evals/analyze.py evals/runs/pilot --exploratory
```

`evals/runs/` holds transcripts and diffs and is not committed. Python 3.9 or newer, standard library only;
the trials need `bwrap` and `socat` for Claude Code's sandbox on Linux.
