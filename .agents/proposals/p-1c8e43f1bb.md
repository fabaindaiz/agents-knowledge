---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-1c8e43f1bb
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.28
digest: 104372939f6a
kind: method
action: new
target: private-records-and-privacy-layers
lacks: the sentinel rule, the public guard, the home re-check and their tests; the harvest and close wording
seen: "2026-10-05"
---

Each carrier may keep confidential records in a private folder, `docs/private/` by default (the host may name it otherwise, recorded in `adapted`): context keyed by decision id, and `people.md`, which maps the decider aliases to names and roles; an alias is never reassigned. No tool reads the folder and the harvest is told never to read it; in a public repository it is in `.gitignore`. Three layers guard it: every file in it starts with a sentinel line, and `bundle.py privacy` fails when that line or the folder's path appears in `.agents/` or in a commit range; `verify` fails when `carrier.toml` declares the carrier public and the folder is tracked by git; `release.py gather` and `intake` run the privacy check over every proposal and do not take in one that fails. A privacy warning in a proposal becomes a question to the owner at the close or the harvest, defaulting to generalise; a yes writes `privacy-allow: <reason>`, and `intake` treats a warning with no allowance as a failure.

## Evidence

The decision literature asks for the organisation's situation and priorities in a decision's context, the detail principle 20 keeps out of the bundle, and the harvest reads the decisions log. Several carriers' logs carry business words. `propose` and `intake` run no privacy check of their own today, and one release rewrote a private carrier's verbatim evidence by hand before its intake. A terms list exists on one machine only, so a name in a row would be unguarded wherever another machine harvests.
