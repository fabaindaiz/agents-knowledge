# Measures for two owner candidates: the gate's cost and redundancy, and who runs the shipped tool's commands

Date: 2026-11-25. Home repository, working tree of the 0.0.35 line, on one macOS machine. Read-only apart from this file;
every scratch artefact (timing runner, mutation copies, tag worktrees) lived outside the repository and the worktrees
were removed.

Two queued candidates each name a measure they lack. This document runs what this machine allows, says what it could
not, and returns a verdict per row. Counts only; no transcript text, no repository or folder names.

## 1. `a-gate-is-pruned-as-well-as-grown`

The row's Lacks: *a counted run over one suite: for each check, when it was last red, and how many of its failures
another check already catches first.*

### 1.1 Method

- **Suite.** `python3 -m unittest discover -s meta/tests -t .` under a small timing runner (a `TextTestResult`
  subclass that records each test's wall time). Three `Usage` tests fail before any change on this platform (a known
  defect); they are counted but excluded from every "red" statement below. One test of a copy of the tree under a
  scratch folder also differed, so the baseline was re-taken inside the copy used for the fault runs (one failure there).
- **Check.** `python3 meta/tools/release.py check` was timed as a whole (wall) and step by step, by calling the
  functions `check()` chains, in process, one after the other.
- **When red.** Three cheap sources: (a) re-running each suite at two earlier release tags in throwaway worktrees;
  (b) the test history: for every test method now present, the commit that first added it (parsed from the diffs of
  `meta/tests/`), by commit type; (c) the session log and roadmap-state archive, searched for a test or check named as
  having caught something.
- **Redundancy.** Fault injection, a small sample: eight single-line faults planted one at a time in a scratch copy of
  the shipped tool's original, the whole suite run for each, the failing tests listed.

### 1.2 Cost

| Quantity | Value |
|---|---|
| Tests (this tree) | 397 (7 files) |
| Suite wall time, one quiet run | 57.3 s (an earlier tag's 277 tests: 37.0 s; a later tag's 387: 84 s on a busier machine) |
| Median test | 43 ms |
| Tests under 10 ms / under 100 ms | 165 (42%) / 255 (64%) |
| Slowest tenth (39 tests) | 56% of the total time |
| Slowest 5 / slowest 10 | 19% / 29% |
| Slowest test alone | 4.7 s (8%): a review-pilot test building six notes' diff sets |
| Fastest half (198 tests) | 2.7% of the total |
| By file | `test_bundle` 221 tests, 27.2 s; `test_release` 62, 17.2 s; `test_review_pilot` 7, 6.0 s; `test_skills` 63, 3.1 s; `test_evals` 5, 2.5 s; `test_surfaces` 16, 1.2 s; `test_formats` 23, 0.1 s |

Of the 39 slowest, the top ones are subprocess-heavy round trips (git hooks, export-and-verify, gather/intake/splice
round trip, review pilot), not unit tests. The tail is cheap: half the tests together cost under 3% of the time.

`release.py check`, 7.3 s wall (6.0 s in process, step by step):

| Step | Seconds | Share of the steps |
|---|---|---|
| privacy over the home's own files | 4.08 | 68% |
| privacy over the bundle | 1.20 | 20% |
| verify (checksums, links, routing) | 0.26 | 4% |
| invisible characters | 0.24 | 4% |
| build `--check` | 0.15 | 3% |
| everything else (links, sessions, budgets, funnel, queue, manifest, slugs, decisions, export cap) | 0.28 | 5% |

The whole home gate is the suite plus `check`: about 65 s on this machine, 88% of it the suite.

### 1.3 When each check or test was last red

| Evidence | Result |
|---|---|
| Suite at the tag two releases before the previous one (277 tests) | 0 red |
| Suite at the tag two before the latest (387 tests) | 2 red, both `Usage` platform tests (the known defect) |
| Current tree | 3 red, the same `Usage` tests; nothing else |
| Tests whose first appearance is in a `fix` commit | 111, 28% of the suite; they carry 18.9 s of the 57.3 s (33%) |
| Tests first added by `feat` / `build` / `test` / `docs` / `chore` | 254 / 15 / 12 / 3 / 2 |
| Commits that touched `meta/tests/`, of 299 in all | 109; by type 54 fix, 36 feat, 6 test, 5 build, 3 feat!, 3 docs, 1 refactor, 1 chore |
| Test names removed or renamed over the history | 10 occurrences (the only retirements found; no commit is a retirement as such) |
| Session log and roadmap archive naming a test or check that caught something | 3 passing mentions in about 72 KB; none names a check that has since stayed green |

Reading: a tag-time rerun measures whether a release was shipped red, and it was not; it cannot say when a check was
last red during development, because a red run between commits leaves no record (no CI logs on this machine, and the
gate's output is not kept). The only durable trace of a red is the regression test written after it, and by that proxy
28% of the suite exists because something broke once. The other 72% was written with the feature, so its first red, if
any, is unrecorded.

### 1.4 Redundancy (eight planted faults)

Each fault was a one-line change to the shipped tool's original. In every run one further test always fails
(`test_release.ShippedTool`, "the shipped tool parses to the same tree as its original"), because the release copy no
longer matches the edited original; that is an artefact of the method and is excluded below, but it is itself a
check that fails first on any edit of the tool, so it is redundant with every other check for the purpose of
detecting a change, and not for what the change breaks.

| Fault planted | Tests that failed (besides the artefact) | Reading |
|---|---|---|
| record id hash width 6 to 5 | 1 (the id-form test) | one test, no overlap |
| checksum function changed to another hash | 51, in 14 classes | broad, not redundant in kind: each class exercises the checksum on its own path |
| invisible-character category test dropped | 1 (bidirectional controls found) | one test |
| attribution-line matcher returns nothing | 6: five trailer tests and the close-command test | five tests of one function, each a distinct scenario (default range, no upstream, published commits, trailer forms); the close test is a broader chain |
| frontmatter split off by one | 1 (write-then-read round trip) | one test |
| duplicate decision row no longer reported | 1 | one test |
| quote no longer escaped when writing frontmatter | 1 (the same round trip) | the same test as the split fault: one round-trip test covers two distinct faults |
| table cell unescape of a pipe broken | 0 | **no test catches it**; only the artefact test failed |

So: of seven faults that were caught at all, six were caught by exactly one test or by a family of scenario tests of
one function, and one by a broad shared function (51 tests). Overlap between a unit test and a broader round trip
was seen once (the close command over the trailers). One fault was caught by none. Across the eight runs, 60 distinct
tests failed under at least one fault; 3 of them under two or more.

### 1.5 What this moves, and what it does not

Moves the boundary of *Lacks*:

- The cost half is now counted, for one suite: 57 s, the slowest tenth is 56% of it, the fastest half under 3%, and
  the gate's cheap-to-run `check` is 7 s, two thirds of it one privacy scan.
- The redundancy half has a first, small figure: in a sample of eight faults, strict redundancy (a second test failing on
  the same fault with nothing of its own to add) is rare; the suite is mostly one-test-per-fault with scenario families,
  and in this sample the dominant hazard is a **missing** test (one fault caught by none), not an excess.

Does not move:

- *When last red per check* is not obtainable here: no record of red runs exists, tag reruns only show a green release,
  and the one proxy (a regression test exists) shows what failed once, not when it last did. The row's measure needs
  the gate's results kept for a window; this machine has none. A check that has never been red in a window cannot be
  identified from the repository.
- Eight faults in one file of one tool is a sample, not a census; the faults were chosen by the author, so they are
  biased toward code that has a test. The sample cannot say that an uncovered check does not exist elsewhere.
- Suite order and the first-failing check: unittest runs all tests, and `check` collects all problems, so "fails
  first" was read as "also fails", not as an ordering. The row's stop-at-first-red premise was not exercised.
- Whether removal is safe: no coverage data was taken, and the literature the row names was not consulted.

### 1.6 Verdict: **moves the boundary** (inconclusive on the claim's core)

The claim is a process claim (additions need an incident, removals need nobody) and this does not test it. What it
establishes is that the suite's cost is concentrated (a tenth of the tests pay for most of the seconds, so a pruning
or tiering decision has an obvious place to look), that unit-level redundancy is low in a sample, and that the
history cannot answer the row's "last red" question without a new record. The counted run the row asks for is
therefore still short of one column, and what it lacks is a log, not an analysis.

## 2. `classify-shipped-code-by-who-runs-it`

The row's Lacks: *the running measure itself, each command traced to the session that invokes it.*

### 2.1 Method

- Subcommands listed from `bundle.py --help`: 25 (the row's number).
- Transcripts: this machine's assistant session files, one folder per project, top level only. For each tool-use
  record of the shell tool, the command text was matched for `bundle.py <subcommand>` (allowing options before the
  subcommand) and `release.py <subcommand>`; one count per distinct subcommand per command.
- Split: by the record's working directory (the home versus any other repository), cross-checked against the project
  folder's name; the two splits differed by under 2% of invocations, and the table uses the working directory.
- Sidechain records (a subagent's) were skipped when flagged; none were flagged in the files read, and the subagent
  transcript files that sit one folder deeper were not read, so subagent-run commands are not counted.
- Counts are aggregated over all other repositories ("carriers"); no name is kept.

Scope, stated plainly: 32 transcript files on this machine, spanning 2026-10-26 to 2026-11-25; **1 session in the home
and 18 in carriers** contain any of these commands (2 files are the home's, 30 are carriers'). The home's own history
on this machine is therefore thin and the other machine's is not here. Commands run by a hook (the privacy check at
commit, the research hook) are not tool-use records and are not counted; commands the human types are not either.

### 2.2 Result: `bundle.py`

| Subcommand | Home (invocations) | Carriers (invocations) | Carrier sessions using it |
|---|---|---|---|
| id | 2 | 662 | 17 |
| usage | 2 | 275 | 16 |
| decisions | 2 | 252 | 15 |
| close | 0 | 189 | 15 |
| count | 2 | 138 | 16 |
| new | 2 | 115 | 15 |
| memory-diff | 0 | 98 | 14 |
| verify | 7 | 91 | 11 |
| propose | 7 | 46 | 7 |
| docs-drift | 0 | 41 | 8 |
| privacy | 11 | 36 | 8 |
| trailers | 1 | 30 | 8 |
| export | 1 | 26 | 8 |
| ids | 1 | 23 | 5 |
| check-local | 3 | 21 | 9 |
| install-skills | 3 | 19 | 7 |
| changelog | 2 | 12 | 7 |
| proposals | 2 | 11 | 6 |
| surfaces | 0 | 7 | 1 |
| turns | 6 | 4 | 2 |
| carrier-id | 0 | 4 | 2 |
| research-hook | 0 | 3 | 1 |
| home | 0 | 3 | 2 |
| lookup | 0 | 1 | 1 |
| report | 0 | 1 | 1 |
| **Total** | **54** | **of the order of two thousand** | |

Every one of the 25 subcommands was invoked at least once from a carrier session; **none is home-only by running**.
Eleven were also run in the home, and fourteen never in the one home session read. The weakest carrier use is a single
invocation (`lookup`, `report`) and a single session (`surfaces`, `research-hook`).

### 2.3 Result: `release.py` (the home's own tool, for comparison)

| Subcommand | Home | Carriers |
|---|---|---|
| check | 16 | 0 |
| build | 7 | 0 |
| gather | 6 | 0 |
| intake | 4 | 0 |
| splice | 3 | 0 |
| register | 3 | 0 |
| align | 3 | 0 |
| carriers | 1 | 0 |
| release | 1 | 0 |

Every `release.py` command ran in the home and none in a carrier: the split the row wants for `bundle.py` exists
cleanly for the tool that is not shipped, which is a check that the method can tell producer from consumer.

### 2.4 Against the naming measure

A rough naming pass over this repository's tracked files: for each subcommand, the shipped files (everything under the
release folder except the tool itself, the changelog and checksums) that name `bundle.py <subcommand>`, against files
that do not ship.

- Subcommands named by at least one shipped file: 23, of the 25. Named **only** by a non-shipped file: `trailers` and
  `research-hook`. The row's two earlier passes found none; the difference is a matter of what counts as a shipped
  mention (this pass did not count the changelog, the tool's own docstrings, or hook and settings files), and should
  be read as the naming measure being sensitive to its definition, not as a correction.
- By the running measure, those two are run in carriers (30 and 3 invocations in 8 and 1 sessions). So where naming
  says "producer's", running says "carrier's": the naming error runs in both directions.
- No subcommand is run only in the home, so by this running measure there is no command whose exclusive code could
  move out of the shipped tool. That contradicts nothing in the row (which found a bounded 4 to 6 percent from reading
  the code) but it does not support it either.

### 2.5 What this moves, and what it does not

Moves: the running figure now exists as a count, for one machine, and for the shipped tool's own subcommands the count
is lopsided, not split: about 97.5% of invocations are from carrier sessions and the home accounts for 2.5%.
Every command has a carrier user.

Does not move:

- **The home's use is under-sampled** (one session). The home runs the producer's procedure (gather, intake, splice)
  through `release.py`, not `bundle.py`, so the producer-side commands in `bundle.py` may be exactly the ones the
  home's sessions use rarely, and a thin home sample cannot show them.
- **A carrier session is not always the carrier's own work.** A meta-session run from the home may `cd` into a carrier
  and call `check-local`, `export`, `proposals --prune`, `changelog` there; the working directory then reads "carrier"
  while the procedure is the producer's. This measure cannot tell the two apart without reading the sessions, which
  was not done. The commands this affects most are the ones with few carrier sessions (`check-local`, `export`,
  `changelog`, `proposals`, `home`, `turns`, `surfaces`, `lookup`, `report`, `carrier-id`).
- It counts commands, not code paths: it says nothing about the share of the file reachable only from a command, nor
  the 5% the row found unreached.
- One owner, one machine, one month: the row's "second owner's bundle" is untouched, and the reachable-versus-used
  literature was not consulted.

### 2.6 Verdict: **moves the boundary, partly confirms**

It confirms the row's central point as far as it goes: the naming measure and the running measure disagree, in two
commands even by my cruder pass, and in the direction the row did not name (commands named as the producer's that
carriers run). It does not confirm that there is code to move: on a count alone, no command is the producer's by
running. The decisive refinement is whether the carrier-side calls of the producer-flavoured commands come from
procedures run on the carrier's own behalf, and that needs the sessions read, or a record of who invoked the command
(a field the tool could write), neither of which this measure had.

## 3. Limits common to both

- One machine, one macOS platform, one tree state (the working tree changed under the run, by edits that were not
  mine; the suite's size moved between 397 and 398 tests).
- Timings vary with load: runs in parallel (the fault runs) took three to four times as long and were not used for
  the cost figures.
- Both rows still lack the literature the rows name; neither was consulted.
