# evals — does the bundle change what an agent does?

This folder is not part of the bundle and never travels to a carrier. It holds two studies, which ask
different questions and must not be read as one.

| Study | Question | Pre-registration | State |
|---|---|---|---|
| **1: instruction transfer** (roadmap `i-5ed7e8-0d9b6a`) | On a task where a note applies, does its content change the decision, rather than the extra context or the routing? | [`PROTOCOL.md`](PROTOCOL.md) | five exploratory pilots, reported in [`REPORT.md`](REPORT.md); confirmatory run not started |
| **2: general performance** (roadmap `i-5ed7e8-bf5663`) | On work nobody chose to suit the bundle, does carrying it change success, and at what cost? | [`PROTOCOL-general.md`](PROTOCOL-general.md) | draft 2, reviewed adversarially and checked against its data sources; not frozen, no data |

**Why two.** Study 1's tasks were written from the notes, each hidden test checks its note's claim,
and one arm receives the note itself. So Study 1 can show that a note's content reaches a decision, but
not whether the agent does better work in general. Study 2 uses tasks from external benchmarks (real
issues, competitive programming, code reasoning, optimisation, design by consequence), graded
automatically, with no task, grader or rule derived from the notes. Study 1 keeps its role; Study 2 does
not replace it.

| File | Does |
|---|---|
| `PROTOCOL.md` | Study 1's pre-registration: six arms, judgment, boundary and neutral tasks, the analysis plan and its deviations |
| `REPORT.md` | Study 1's pilots, written as they happened, with the instrument defects found and corrected |
| `PROTOCOL-general.md` | Study 2's protocol: competing explanations, falsifiable hypotheses with their severity, five task blocks, routed controls, gates G0–G4, forecasts, the decision map, threats, what must be built, and what changed from draft 1 |
| `harness.py` | validates the tasks, freezes a plan, runs trials in isolation, grades them (Study 1; Study 2's arms and adapters are listed in `PROTOCOL-general.md` §16) |
| `analyze.py` | Study 1's pre-registered analysis of a run |
| `power.py` | Monte Carlo power for a paired superiority test, to size a run before it happens |
| `power_tost.py` | Study 2's severity check: on realised effects, the chance of detecting a harm and of declaring equivalence or non-inferiority, at a family's alpha, across per-task effect spreads |
| `tasks/<id>/` | Study 1's tasks: `task.json`, `prompt.md`, `AGENTS.minimal.md`, `repo/` (the start), `hidden/` (the grader), `naive/` and `reference/` (overlays that prove the grader discriminates) |

## Running Study 1

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

## Study 2: where it stands

Nothing of Study 2 runs yet. Its next steps, in order, are in `PROTOCOL-general.md`:

1. The decisions that belong to the user: a budget cap before the pilot (§17), the forecasts (§13), and
   pushing the freeze tag before the first confirmatory trial (§10, G2).
2. Building what §16 lists, until gate G0 passes: task adapters, graders, the container for block E,
   the placebo, the scrub, the new arms and the Study 2 analysis with its simulation mode.
3. The blinded pilot (G1), then the freeze (G2), the run (G3) and the analysis (G4).

Its severity figures can be reproduced now:

```bash
python3 evals/power_tost.py --tasks 120 --reps 3                 # block E, two-sided at 0.05
python3 evals/power_tost.py --tasks 120 --reps 3 --alpha 0.025   # block A: non-inferiority and the Holm harm label
python3 evals/power_tost.py --tasks 40 --reps 3 --margin 0.20 --hetero 0.15   # the routed controls
```

`evals/runs/` holds transcripts and diffs and is not committed: transcripts carry the logged-in
account's identity. Python 3.9 or newer, standard library only; Study 1's trials need `bwrap` and `socat`
for Claude Code's sandbox on Linux.
