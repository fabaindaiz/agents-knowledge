# Rules restated in more than one prompt (i-5ed7e8-705aa8, 2026-10-08)

Scope, by `d-5ed7e8-9f3502`: only rules restated in more than one prompt; long worked examples wait for
`i-5ed7e8-16b90a`. A mid-size model read the six method prompts and the skills whole, read-only, and listed 15
candidate duplicates, the paste-block copies and 8 places where copies disagree. Each was checked against the files
before any edit. Line numbers are those of 2026-10-08 and will drift.

## The test applied

A copy is removed only where the document holding it already loads the owner through its `Reads:` list. A copy in a
document that runs alone (a skill, the session loop, a job prompt run without `prompt-context.md`, a paste block) is
there so that document works alone. Removing it would make that document depend on reading another one, which costs
more context than the copy. Copies within one file are outside the scope.

## Verdicts on the candidates

| Id | Rule | Verdict |
|---|---|---|
| D1 | The root file's knowledge row | **Kept.** It is the wiring the cost pilots measured (`evals/REPORT.md` §4.14 to §4.16); rewording it needs a pilot |
| D2 | A method procedure never overrides the repository's own | **Kept**, for the same reason: it is a row of the root file's map |
| D3 | Documents true again | **Kept.** `close` and the session loop each run alone, and their lists carry commands the other lacks |
| D4 | Count frictions by searching | **Kept**, as D3 |
| D5 | The question's shape, in `decision-review` | **Kept.** The skill runs without loading §15; pointing at it would load more than it saves |
| D6 | A privacy warning on a proposal | **Kept.** `close` runs alone |
| D7 | One source and three agents, in evaluate's first question | **Removed**: evaluate loads `prompt-context.md` §*Three agents, one source* |
| D8 | What the bundle's state means next, in evaluate | **Removed**: evaluate loads §*Which document to run* |
| D9 | The ladder's rungs, re-tabulated in evaluate | **Removed**: evaluate loads §*The enforcement ladder* |
| D10 | Several carriers onto one release is the home's job | **Kept.** The update prompt runs without the shared reference |
| D11 to D13, D15 | Restatements within one file | Outside the scope |
| D14 | Run evaluate first | Kept; the copies disagree (N4, below) |

## Copies that disagree

| Id | Where | Verdict |
|---|---|---|
| N1 | The harvest's *when* table took a second hit in one repository as the admission evidence; its own rule counts across carriers | **Fixed**: a second hit is a reason to propose now; admission still counts across carriers |
| N2 | Principle 16 writes `docs-map.toml`; the bootstrap's step 6 and checklist never named it | **Fixed**: both name it for what a script can check |
| N3 | Reports follow the reader; evaluate writes its report in the repository's language | Not a contradiction: one is a conversation, the other a file in the repository |
| N4 | Evaluate first: always (context and evaluate), unless the repository is known empty (bootstrap), only when unsure (update) | **The owner's** |
| N5 | The bootstrap stated the whole-branch review's evidence without principle 19's caveat | **Fixed**: the caveat and its pointer added |
| N6 | Principle 19: one artifact per session in adopt mode; the first pass generates every artifact in one session, adopt mode included | **The owner's** |
| N7 | The harvest closes an in-flight session by default, and never closes somebody else's without being told | **The owner's**: which wins when the tree holds work the harvester did not do |
| N8 | `decision-review` said "reversible in minutes"; §15 says ten | **Fixed** |

## What it saved

About 150 words of evaluate, against the roughly 1,100 the first list estimated: most of what looked duplicated is
there on purpose, so that a document runs alone.
