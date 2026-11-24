# Which subcommands of the bundle tool a carrier runs: a count (2026-11-24)

A count, not a proposal. It asks whether any content of `.agents/tools/bundle.py` has only a home session as its reader. It does not divide the file.

## Method

- The subcommands are the 25 registered in the argument parser (`add_parser`) and dispatched in `_run`. The parser and the dispatch list match one to one.
- *Lines* is the length of each command's `if args.command ==` block in `_run`. It is a proxy: the helpers a command calls (for example the privacy check, the verify checks, the proposal readers) are shared between commands and are not attributed here. The file has 5,351 lines in total.
- *Files that name it* is `grep -rnE "bundle\.py <command>"` over `.agents/`, `meta/` and `sources/`. `sources/bundle/` mirrors `.agents/`, so it is not listed separately. `CHANGELOG` files are listed only as history; they do not decide a class. A pattern miss was corrected by hand: the researcher agent calls `bundle.py" research-hook` with a quote before the command, which the pattern does not match. `.claude/`, `.githooks/` and the home's root `AGENTS.md` were searched too, for the two commands with no method prose.
- *Carrier-read* means a file under `.agents/` a carrier reads on its own: `method/`, the skills, the READMEs, `knowledge/`, `proposals/`, `incoming/`, and the shipped agent definitions. *Home* means files under `meta/`.
- Classes: **carrier solo** = named by at least one carrier-read file; **home only** = named only by `meta/` files or by steps that run in a meta-session; **nobody** = named by no method file.

## Table

| Command | Lines (approx.) | Files that name it (carrier-read; home) | Class |
|---|---:|---|---|
| verify | 12 | method: prompt-bootstrap, prompt-context, prompt-evaluate, prompt-harvest, prompt-update, skills/next, skills/README, README, proposals/README, incoming/README; home: meta/method/prompt-sync, roadmap, decisions, tracking (2), review | carrier solo (home also) |
| check-local | 16 | method: meta, prompt-harvest, prompt-update, README; home: prompt-sync, decisions, archive, review | carrier solo (home also) |
| carrier-id | 6 | method: meta, prompt-bootstrap, prompt-context, README; home: prompt-sync, release.py, tracking, archive | carrier solo (home also) |
| id | 3 | method: prompt-bootstrap, prompt-context, prompt-evaluate, prompt-update, README; home: prompt-sync, decisions, tests, tracking, reviews (2), archive | carrier solo (home also) |
| ids | 13 | method: prompt-bootstrap, prompt-context, README; home: decisions, roadmap, tracking, reviews (2), archive | carrier solo (home also) |
| decisions | 27 | method: prompt-bootstrap, prompt-context, prompt-update, skills/close; home: decisions, roadmap, tracking (3), reviews (2) | carrier solo (home also) |
| privacy | 21 | method: prompt-bootstrap, prompt-context, prompt-harvest, prompt-update, skills/close, README; home: prompt-sync, decisions, archive (2), reviews (3), tracking (3) | carrier solo (home also) |
| trailers | 29 | none in method; home: reviews (2); the home's `.githooks/pre-push` and root `AGENTS.md` (not shipped) | nobody (in method) |
| report | 10 | method: prompt-context; home: decisions, reviews (2) | carrier solo (home also) |
| changelog | 3 | method: meta, prompt-context, prompt-update, README; home: one review | carrier solo (home also) |
| home | 3 | method: meta, README; home: decisions, archive, reviews (2) | carrier solo (home also) |
| usage | 4 | method: prompt-bootstrap, prompt-context, prompt-harvest, skills/close; home: decisions, archive, reviews (3) | carrier solo (home also) |
| export | 3 | method: meta, prompt-bootstrap, prompt-update, README, incoming/README; home: prompt-sync (2), decisions, tracking (4) | carrier solo (home also) |
| propose | 17 | method: meta, prompt-harvest, proposals/README, README, knowledge/README, knowledge/INDEX; home: decisions, method/home, template index | carrier solo (home also) |
| proposals | 25 | method: meta, prompt-harvest, prompt-update, proposals/README, README; home: prompt-sync (3), release.py (5), tracking, review | carrier solo (home also) |
| install-skills | 19 | method: skills/README, prompt-update; home: decisions | carrier solo (home also) |
| surfaces | 25 | method: prompt-bootstrap, prompt-context, prompt-update, README; home: roadmap, decisions, archive, reviews (2), tests (5) | carrier solo (home also) |
| new | 20 | method: prompt-context, skills/close; home: roadmap, tracking (2), archive, reviews | carrier solo (home also) |
| research-hook | 2 | no method prose; named by the shipped researcher agent definition (PreToolUse hook) | carrier solo (wired, not prose) |
| lookup | 16 | method: guide, skills/next; home: decisions, roadmap, tests, release.py, reviews (3) | carrier solo (home also) |
| close | 11 | method: skills/close; home: decisions, archive, tests | carrier solo (home also) |
| docs-drift | 27 | method: prompt-context, skills/close; home: decisions, archive (2), tests, tracking | carrier solo (home also) |
| count | 11 | method: skills/close; home: archive (8), tracking (3), candidates | carrier solo (home also) |
| memory-diff | 15 | method: skills/close; home: review, tracking (2) | carrier solo (home also) |
| turns | 17 | method: prompt-harvest; home: reviews (3) | carrier solo (home also) |

## Totals

Total file: 5,351 lines.

| Class | Commands | Lines (approx.) | Share of the file |
|---|---:|---:|---:|
| carrier solo | 24 | 326 | about 6.1% |
| home only | 0 | 0 | 0% |
| nobody (in method) | 1 (`trailers`) | 29 | about 0.5% |
| total in the dispatch | 25 | 355 | about 6.6% |

Every command with a home mention also has a carrier-read mention. No command is named only by a `meta/` file.

## What the count shows and what it does not

It shows that, by naming, no subcommand is reserved for the home. Each command except `trailers` is named in a file a carrier reads, and most of the home's own references to them sit beside carrier-read ones. Under this test, moving the home-only subcommands out of a carrier copy would remove nothing.

It does not show that a carrier runs every command it is named by. Naming means the carrier's documents describe the command; it does not show that the carrier calls it. Nor does it show that the home-only code is absent: that code lives in helpers the dispatch lines do not count, which are shared between commands and were not attributed. Likewise, a command that no method file names can still be used by a person by hand, so "nobody" does not mean "not used". `trailers` is in fact run by the home's own git pre-push hook, which is outside the bundle.

Names in the shipped meta explanation (`method/meta.md`) and in the update procedure describe steps that happen at a home, so a carrier reading them is reading about the home, not running it. The count does not separate those steps from carrier steps.

## A second, independent count

The count above was repeated the same day by a different reader, who worked from the parser without
reading this document first and only compared afterwards.

**The verdict holds: zero of twenty-five subcommands are named only by a file that exists in a home.**
Two independent passes agree on the conclusion. They disagree on one label. This document puts the
trailer check in "nobody names it", because no method file writes its invocation literally; the second
count places it with the rest, because the close skill lists it among what one command runs, and a
carrier's own close calls it. The second reading is the better one: a carrier does run it. The verdict
is unchanged either way, since that command was never in the home-only class.

**The line figures in the table above understate badly, and should not be quoted.** They come from the
dispatch block of each command, which is about 357 lines in all — the work lives in the helpers those
blocks call. A call graph built over the same file reaches about 3,540 of its 4,142 function lines from
the dispatcher, and the exclusive code of single commands runs into the hundreds of lines each, not the
tens. Use the table for which files name a command, not for how large a command is.

**What a second method would have to answer.** Both counts classify by what *names* a command, and
naming is not running. Several commands are written for a meta-session even though a shipped file names
them — replacing an exported copy, comparing a carrier against its checksums, pruning received
proposals. A count by *who actually runs it* could produce a home-only class of roughly two to three
hundred lines, with wide uncertainty. Neither pass determined that, and neither should be read as having
ruled it out.
