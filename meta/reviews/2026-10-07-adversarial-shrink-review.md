# What to cut: an adversarial review of the export and the home

**Date:** 2026-10-07. **Status:** review by a delegated agent on the main model (adversarial judgement,
`d-5ed7e8-cdf1f3`), read-only, asked by the owner to be pessimistic; release 0.0.29. Its figures are its own;
the main session re-measured the file sizes, the tag dates and the carrier count, which match. Tokens here are
measured ones, about bytes over 2.8 (`meta/reviews/2026-10-07-cost-inventory.md`). It feeds `MANIFEST.md`.

**Baseline.** The shipped export is about 900 KB in 123 files (`release.py report`). The pilots used the knowledge
index (read in nearly every non-trivial trial) and about one and a half cards per trial; area indexes, method
prompts, skill bodies and the reviewer were never read, a full note once. About nine tenths of the export has no
measured use.

## Cuts to the export, ranked

1. **The coding invocation's reads** (about 40 KB, about 14k tokens per coding session): the session loop of
   `prompt-bootstrap.md`, the engineering standards and principle 20 of `prompt-context.md`. Move the loop into a
   skill of about 8 KB, drop its fresh-context review step (measured at several times a session's cost, no task
   passed by it), keep principle 20's forbidden list only. About 10k tokens per session. *Risk:* putting documents
   back to true and the honest report get skipped; untested either way.
2. **The index as a lookup** (24 KB): keep the action-to-card rows as action and slug; drop the by-phase route and
   the authors' prose, or replace with `bundle.py lookup` (`d-5ed7e8-90786d`). About 6k tokens per non-trivial
   task. *Risk:* the phase route, never seen in use.
3. **Drop the area indexes** (about 58 KB): never read, routed to by no procedure, and each row repeats the card.
   *Risk:* none measured; browsing by topic becomes a search.
4. **Shrink `knowledge/OPEN.md`** (47 KB, read whole by every harvest): its waiting candidates are the home's
   backlog. Ship slugs and states, about 5 KB. *Risk:* a candidate offered twice, which intake de-duplicates.
5. **Cut `prompt-context.md`** (126 KB): five sections no `Reads:` line routes to (about 20 KB); the principles as
   essays (45 KB); overlaps between principles 1–2 and the enforcement ladder, 5, 10 and 16, 9 and 11 with the
   artifacts, 15 with the pre-flight, the session loop and `decision-review`. One paragraph per principle, claim
   and enforcer, the essays to `sources/`. About 50 KB. *Risk:* no eval ever ran a method prompt.
6. **One-time prompts out of the export**: `prompt-evaluate.md` (21 KB) and the bootstrap phases (about 25 KB),
   fetched from the tag when a repository adopts the bundle. Disk and review surface, no context cost today.
7. **`proposals/RECEIVED.md`** (30 KB, two thirds from one release): the last two releases, or ids only.
8. **The changelog** (36 KB): only the sections since the oldest registered carrier's version.
9. **`tools/bundle.py`** (212 KB, 18 subcommands): home-only modes (`turns`, `memory-diff`, `count`, `report`)
   and legacy paths (a deprecated alias, the outbox layout, the decisions migration), about 400 lines.
10. **Skill and agent descriptions**, loaded on every turn in every carrier (about 450 to 750 characters each):
    about 250 each, about 600 tokens per turn; split `user-walk`, which does two jobs.
11. **Minor** (about 10 KB): the bundle README's writing section, most of the knowledge README (author rules), the
    skills README, short notes' frontmatter repeating each card.

Cuts 1 to 9 take the export from about 900 KB to about 550 KB; a coding session from about 25k bundle tokens to
about 9k; a harvest by about 14k.

## The home's overhead, ranked

1. **Release churn:** ten tags in twelve days; the carriers sit on four versions, and each release costs every
   carrier a splice, a prune, a gate, a changelog entry and a commit. *Cut:* release on a measured gain, or monthly.
2. **Research outruns decisions:** twenty reviews, nineteen in three days; the hand-off alone is about 4k tokens.
   *Cut:* a hand-off of about 300 words; a review only when a decision waits on it.
3. **A clogged funnel:** 96 candidates, 41 waiting nine releases; 62 experiments queued against 26 run. *Cut:*
   retire a candidate with no second occurrence after a set number of releases.
4. **The records' weight:** `meta/` is about 61k words; 51 decisions in two weeks with their own validator; the
   received ledger mirrored in the export.
5. **Dead procedures:** `meta/method/prompt-merge.md`, untouched for over a week and referenced from the archive
   and two tools; `meta/method/home.md`, which restates AGENTS.md.
6. **The meta-session's chain** (gather, intake, build, release, splice, prune, register, align, template): keep
   the tests, merge `register`, `align` and `carriers`.

## The harshest critiques

1. **The data says shrink, and the export grows.** The bundle costs about twice the base model per task and does
   not help where the answer is in front of the agent; its benefit rests on three of sixteen tasks
   (`evals/REPORT.md`). What was measured useful, index and cards, is under a tenth of the export.
2. **The process outweighs the product:** commits to `meta/` and `evals/` outnumber those to `.agents/` and
   `sources/`.
3. **The last adversarial review's shrinking advice was deferred and its additive advice shipped**
   (`meta/reviews/2026-10-02-adversarial-review.md` §3.11).
4. **One owner's preferences ship as a general method:** the close's counted frictions, the review turn's format
   and the trailer rules mirror the owner's own instructions; every carrier pays for them, nothing measures them.
5. **The largest surfaces are untested:** no pilot ran a method prompt, an area index, a skill body or an
   unprompted reviewer, about 250 KB; Study 2 is a long draft with no data.

## Keep untouched

The cards; `bundle.py privacy` and its hooks; `SHA256SUMS`, `verify` and the `incoming/` quarantine; proposals as
content-hashed files each carrier prunes; the generated-file marks and `build --check`; the tests; the candour of
`evals/REPORT.md`.
