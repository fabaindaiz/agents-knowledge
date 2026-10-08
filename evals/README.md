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

**Amendment, 2026-09-25 (release 0.0.22).** The shipped notes are now short; the full note text the
`oracle` and `oracle_placebo` arms inject, and that `pick_placebo` measures, is read from `sources/notes/`,
so the placebo picks and the oracle text are unchanged (checked identical for all 26 auto tasks). The
bundle is identified by its version and the sha256 of `.agents/SHA256SUMS`: a plan keeps that hash under
`bundle_digest` and adds `bundle_version`. The `bundle` arm's content did change (short notes, cards, the
trigger wording in the invocation; retired notes and the home's records no longer ship), so a future run
measures 0.0.22, not the v0.0.21 the pilots carried. Study 2's frozen digest becomes a frozen version tag.

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
account's identity. Python 3.11 or newer, standard library only; Study 1's trials need `bwrap` and `socat`
for Claude Code's sandbox on Linux.

## Skill triggers

`skills/trigger.py` measures whether a skill fires on the requests it is for and stays quiet on the near
misses (its docstring says how). The protocol, set on 2026-10-05 (`meta/reviews/2026-10-05-skill-triggers.md`):

1. **One pilot carrier**, with its plugins on and its own `.claude/` copied in (`--claude-dir`); check first
   that the three method skills' descriptions are in the session's skill listing.
2. **Held-out cases in the carrier**, never here: requests that expect the skill, near misses, and the owner's
   own phrasings marked `"owner": true`; the owner labels the ambiguous ones (about twenty minutes).
3. **Stage 1**, one run per case, to find the cases that capture or misfire; **stage 2**, `--runs 3`, with a
   prediction written down before it runs.
4. **A pass**: strict fire at least 0.8, misfire at most 0.1, the owner's words alone at least 0.8, every rate
   reported with its interval and the capture table read for which competitor took each missed case.

The run itself waits on `i-5ed7e8-578c22`; cost (assumption) a couple of hours of headless sessions.

## Blind comparisons

Any comparison where a judge, a person or a model, picks between answers shown side by side follows these
rules, taken in at 0.0.31 from a pilot whose middle label was picked three times in four
(`meta/reviews/2026-10-08-pilot-and-carrier-intake.md`). Position effects are widely reported: people favour the
centre of a simultaneous array (Valenzuela & Raghubir 2009, [10.1016/j.jcps.2009.02.011](https://doi.org/10.1016/j.jcps.2009.02.011);
and test makers and takers the middle answer, Attali & Bar-Hillel 2003,
[10.1111/j.1745-3984.2003.tb01099.x](https://doi.org/10.1111/j.1745-3984.2003.tb01099.x); both read at their abstracts), and model judges
change verdicts when two answers swap places (Wang et al. 2023, [arXiv 2305.17926](https://arxiv.org/abs/2305.17926);
Zheng et al. 2023, [arXiv 2306.05685](https://arxiv.org/abs/2306.05685)). The direction varies by setting, so none is assumed.

1. **Shuffle the answer behind each label, and the position of each label.** A label kept in a fixed place
   keeps position and label confounded.
2. **Counterbalance positions**: every arm sits in every position equally often, by a Latin square of the
   arms' order, so the number of problems is a multiple of the number of arms.
3. **A model judge runs in both orders**, as both papers do; the home's stricter choice is that a win counts only
   when both orders agree, otherwise a tie.
4. **Report each position's rate beside the result**, and score by arm only after the balancing.
5. **An option list with a recommendation puts it in a random position**, or the rate it is taken cannot be
   told from a first-position or default effect.
6. **A judge has read no answer before the comparison.** Rules 5 and 6 come from the pilot's threats, not from a source.
