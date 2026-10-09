# 0.0.31: the skill trigger eval and the carriers' audits (2026-10-09)

Plan step 7a without its cost pilot (moved to a later release, `d-5ed7e8-5b183e`) and step 7b. Results reported as
they fell, figures from the runs' own output; the runs and the cases stay outside every repository (the cases are the
owner's own words).

## The trigger eval

**Setup.** `evals/skills/trigger.py`, one run per case, sonnet, in a fresh headless session per case holding the
pilot carrier's `.claude/` and the machine's own plugins (the competition the skills meet), the 0.0.31 descriptions.
Cases: 18 to 21 per skill, written from the owner's typed turns in this machine's transcripts (`bundle.py turns`),
nine ambiguous ones labelled by the owner (all nine: fire). **Gate, by decision** (`d-5ed7e8-7a95b5`): the lenient fire
at least 0.8, the owner's own words at least 0.8, a misfire of at most 0.25 (a skill that fires slightly too often is
preferred to one that misses; the long skills now open with a pre-review, `d-5ed7e8-d7c0b7`).

| Skill | Fire (95% Wilson) | Owner's words | Misfire | Gate | Description |
|---|---:|---:|---:|---|---|
| `next` | 0.92 [0.65, 0.99] | 0.89 | 0.13 | **pass** | unchanged |
| `close` | passes | — | — | **pass** | unchanged; one readiness question taken by `next` |
| `decision-review`, first run | 0.82 [0.52, 0.95] | 0.71 | 0.00 | fail | 0.0.30's |
| `decision-review`, second run | 0.91 [0.62, 0.98] | 0.86 | 0.00 | **pass** | adds going over proposals or decisions again, reconsidering one |
| `user-walk`, first run | 0.42 [0.19, 0.68] | 0.00 | 0.00 | fail | 0.0.30's |
| `user-walk`, second run | 0.58 [0.32, 0.81] | 0.29 | 0.00 | fail | broadened to anything a person does or meets in the app |
| `user-walk`, third run | 0.58 [0.32, 0.81] | 0.29 | 0.00 | fail | 90 more characters, past the old cap: **no gain, not kept** |

**What took `user-walk`'s cases.** A debugging skill and a brainstorming skill from a plugin installed at the user
level, both of which ask to run before any response, and in two cases a plain search of the code; the owner's own
reports of what went wrong while using an app, and requests to improve an interaction, went there. No near miss fired
`user-walk` in any run. The competition is this machine's, so a carrier without that plugin may fare better; that is
a hypothesis, not measured. **Known gap shipped in 0.0.31**; the next step is a routing line in a carrier's root file,
measured, in a later release.

**Caps.** The descriptions' cap is now by kind (`d-5ed7e8-cf8021`, superseding the raise `d-5ed7e8-96b54e`): a long
process 750, a light skill 250, an agent run on request 250, a delegated agent 200, 2,776 in total; the knowledge
reviewer's description lost its topic list. Measured total: about 2,570.

**Cost.** Four skills, then two, then one: about 25 minutes of runs in all, on the owner's account.

## The carriers' audits

Eleven of thirteen listed carriers hold a bundle on this machine; each one's committed tree was copied to a scratch
folder, its `.agents/` replaced by the candidate (its own files kept), and its own audit and `bundle.py verify` run.

| Outcome | Carriers |
|---|---:|
| audit passes | 1 |
| only `verify` could run (the audit needs tools not installed, or the sandbox refused it) | 2 |
| fails only on stale copies of skills or of the reviewer under `.claude/` (the update's `install-skills` rewrites them) | 4, this home included |
| fails on one file of the carrier's own (a pointer to a missing rule file) | 1 |
| **fails on the release's layout** (51 to 162 failures each) | **3** |

**The layout break is older than 0.0.31.** The three carriers hold 0.0.25. Their audits parse the index's *By phase
of work* rows as links to cards, which 0.0.27 changed to backticked slugs, and read `knowledge/areas/`, which 0.0.30
removed; neither change was stated as a **Layout:** line. 0.0.31's changelog now carries that line for a carrier coming
from 0.0.26 or earlier, naming both changes and what to point an audit at (`i-5ed7e8-307d02` proposes that carriers
drop such checks and rely on `verify`).
