# The export's weight tree (2026-10-09)

What each shipped part weighs and who loads it, to decide what to shrink before the 0.0.31 cut, at the owner's request.
Generated from `.agents/` at `6255772`: bytes from the shipped files; *Loaded by* from the method's own `Reads:` lists
(`bundle.py` `sessions_of`). A section is listed when it is a level-2 heading, or a level-3 one of 2.5 KB or more.

**Reading it.** *Not in any session's read list* means one of three things: a tool reads it (`CHANGELOG.md` through
`bundle.py changelog --since`, `proposals/RECEIVED.md` through the prune), a host loads it when its trigger matches (the
skills), or a person pastes it (a prompt's paste box). *Never loaded: executed* is the tool: its bytes count toward the
export, never toward a session's context. In `tools/bundle.py`, comments are 27,274 bytes and docstrings 44,092.

**A dash in *Loaded by* does not mean unused.** The tree follows the `Reads:` lists only, not the pointers between
documents: *Workspaces* and *Using the set* in `prompt-context.md`, and the *Checklists* and *The working invocation* in
`prompt-bootstrap.md`, carry a dash and are reached by reference from the bootstrap, the harvest and the home's sync.
Reviewed with the owner the same day: the shipped tool loses its comments (−27 KB, the original keeps them); the old
changelog sections, `RECEIVED.md` and `OPEN.md`'s answered slugs stay, each saving under a kilobyte or needed by the one
carrier still on 0.0.25.

Export: 919269 bytes (897.7 KB). Cap: 913167 bytes.

| Part | Bytes | Share | Loaded by | How often |
|---|---:|---:|---|---|
| **method/** | 281401 | 30.6% | | |
| &nbsp;&nbsp;`method/prompt-context.md` | 133053 | 14.5% | coding, update, harvest, evaluate, bootstrap | every coding session; once per release, per carrier; once per repository |
| &nbsp;&nbsp;&nbsp;&nbsp;§ The set | 3012 | 0.3% | evaluate | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ Using the set (for the human) | 2774 | 0.3% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ The enforcement ladder | 3441 | 0.4% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 6. Measure before claiming, and record what the measurement killed | 4484 | 0.5% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 7. Name the class of bug this repo cannot see — then check it before i | 3496 | 0.4% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 15. Ask the few decisions that are the human's; decide the rest | 6447 | 0.7% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 17. The process is part of the system; improve it incrementally, and p | 3228 | 0.4% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 18. The test is written first, because an agent that writes it second  | 5967 | 0.6% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 19. Adopt into the repository that exists; the host's shapes win, the  | 3762 | 0.4% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 20. Nothing private travels, directly or by reconstruction | 4292 | 0.5% | coding, update, harvest, evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 1. Root `AGENTS.md` — under 200 lines | 3306 | 0.4% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 4. `.claude/settings.json` | 4029 | 0.4% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 5. The session log — `.claude/logs/agent-changelog.md` by default | 3244 | 0.4% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 6. `docs/decisions.md` — the index of everything settled | 3884 | 0.4% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 8. `docs/roadmap.md` | 4044 | 0.4% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ What each surface can actually do | 4296 | 0.5% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ The platform's own mechanics | 2667 | 0.3% | evaluate, bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ Which document to run | 2876 | 0.3% | update, evaluate | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ Workspaces: several repositories at once | 5175 | 0.6% | — | |
| &nbsp;&nbsp;`method/prompt-bootstrap.md` | 63487 | 6.9% | coding, harvest, bootstrap | every coding session; once per release, per carrier; once per repository |
| &nbsp;&nbsp;&nbsp;&nbsp;§ ▶ Paste this to start | 6267 | 0.7% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ Before you start — ask these | 3110 | 0.3% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Phase 1 — Evaluate the state (read-only). Report before proposing anyt | 2762 | 0.3% | bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Phase 2 — Research the outside (read-only but for its findings). Repor | 2589 | 0.3% | bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Phase 4 — Generate | 3898 | 0.4% | bootstrap | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 0. The opening brief — load the world before you touch the request | 3471 | 0.4% | coding | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 4. Verify — run the invariant test when you *claim* it, not when you t | 4601 | 0.5% | coding | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 7. Report honestly, and let the human decide what is theirs | 3224 | 0.4% | coding | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ 8. The closing review — return what the session learned | 4318 | 0.5% | coding, harvest | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Working safely in a tree you do not own | 3013 | 0.3% | coding | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Done — the bootstrap | 4034 | 0.4% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Done — every change after that | 2975 | 0.3% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ The working invocation | 4187 | 0.5% | — | |
| &nbsp;&nbsp;`method/prompt-evaluate.md` | 19535 | 2.1% | evaluate | once per repository |
| &nbsp;&nbsp;&nbsp;&nbsp;§ ▶ Paste this to start | 4081 | 0.4% | evaluate | |
| &nbsp;&nbsp;`method/prompt-update.md` | 18619 | 2.0% | update | once per release, per carrier |
| &nbsp;&nbsp;&nbsp;&nbsp;§ ▶ Paste this to start | 6747 | 0.7% | update | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ Replacing the bundle | 3606 | 0.4% | update | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ The prune | 2620 | 0.3% | update | |
| &nbsp;&nbsp;`method/prompt-harvest.md` | 14862 | 1.6% | harvest | once per release, per carrier |
| &nbsp;&nbsp;`method/skills/close/SKILL.md` | 8681 | 0.9% |  | not in any session's read list |
| &nbsp;&nbsp;`method/skills/README.md` | 6214 | 0.7% |  | not in any session's read list |
| &nbsp;&nbsp;`method/guide.md` | 5046 | 0.5% |  | not in any session's read list |
| &nbsp;&nbsp;`method/skills/decision-review/SKILL.md` | 4505 | 0.5% |  | not in any session's read list |
| &nbsp;&nbsp;`method/skills/user-walk/SKILL.md` | 4379 | 0.5% |  | not in any session's read list |
| &nbsp;&nbsp;`method/skills/next/SKILL.md` | 3020 | 0.3% |  | not in any session's read list |
| **tools/** | 272115 | 29.6% | | |
| &nbsp;&nbsp;`tools/bundle.py` | 272115 | 29.6% |  | never loaded: executed |
| **knowledge/notes/** (51 files) | 187684 | 20.4% | by lookup | on demand: a card when the index links it; a full note only when a card's boundary is unclear |
| **knowledge/** | 58874 | 6.4% | | |
| &nbsp;&nbsp;`knowledge/OPEN.md` | 28487 | 3.1% | harvest | once per release, per carrier |
| &nbsp;&nbsp;&nbsp;&nbsp;§ Experiments waiting to be run | 12640 | 1.4% | harvest | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ Candidates waiting for what they lack | 5421 | 0.6% | harvest | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ Answered: admitted, folded, refused or discarded, not to offer again | 9958 | 1.1% | harvest | |
| &nbsp;&nbsp;`knowledge/INDEX.md` | 24017 | 2.6% | consult, review, harvest | every question asked of the knowledge base; each review asked for; once per release, per carrier |
| &nbsp;&nbsp;&nbsp;&nbsp;§ By phase of work | 4165 | 0.5% | consult, review, harvest | |
| &nbsp;&nbsp;&nbsp;&nbsp;§ By what you are about to do | 14942 | 1.6% | consult, review, harvest | |
| &nbsp;&nbsp;`knowledge/README.md` | 6370 | 0.7% | harvest | once per release, per carrier |
| **knowledge/cards/** (51 files) | 46642 | 5.1% | by lookup | on demand: a card when the index links it; a full note only when a card's boundary is unclear |
| **(root)/** | 44689 | 4.9% | | |
| &nbsp;&nbsp;`CHANGELOG.md` | 34708 | 3.8% |  | not in any session's read list |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Added | 2972 | 0.3% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Changed | 7179 | 0.8% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Added | 2615 | 0.3% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Added | 2533 | 0.3% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Changed | 3018 | 0.3% | — | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Changed | 3930 | 0.4% | — | |
| &nbsp;&nbsp;`README.md` | 9981 | 1.1% | update, bootstrap | once per release, per carrier; once per repository |
| **proposals/** | 20042 | 2.2% | | |
| &nbsp;&nbsp;`proposals/RECEIVED.md` | 16047 | 1.7% |  | not in any session's read list |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;§ Received — the proposals the home repository took in | 15925 | 1.7% | — | |
| &nbsp;&nbsp;`proposals/README.md` | 3995 | 0.4% | harvest | once per release, per carrier |
| **agents/** | 4704 | 0.5% | | |
| &nbsp;&nbsp;`agents/knowledge-reviewer.md` | 2582 | 0.3% | review | each review asked for |
| &nbsp;&nbsp;`agents/researcher.md` | 2122 | 0.2% |  | not in any session's read list |
| **incoming/** | 3118 | 0.3% | | |
| &nbsp;&nbsp;`incoming/README.md` | 3118 | 0.3% |  | not in any session's read list |
