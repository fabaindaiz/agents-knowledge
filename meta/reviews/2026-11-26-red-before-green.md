# Evidence that a fix's test was red first: what can be checked

2026-11-26, for `i-5ed7e8-468621` and the decision on `bundle.py red-check`. **A shallow search**: three web
searches, results read as snippets, no primary text read in full. Every claim below is that strength or is
marked an ASSUMPTION; verify before citing it as established.

## The question

§18 asks that a fix's test run in one command and the fix in the next, so its red is seen first. Three fixes in
one session broke it with the sentence loaded. What mechanism shows a test fails without its fix, cheaply, with
the standard library and git only?

## What was found

- **A commit line is self-asserted.** `git interpret-trailers` parses and adds `Key: value` lines and validates
  nothing about their content ([git docs](https://www.kernel.org/pub/software/scm/git/docs/git-interpret-trailers.html), snippet).
  No commit-lint tool was found that checks test evidence; they check format (ASSUMPTION, not read in full).
- **An editor hook that blocks implementation edits until a failing test exists** exists for Claude Code (TDD
  Guard, fed by a test reporter; its README, on its forge under the name `tdd-guard`). It
  trusts the reporter and checks edit order, not a tree (ASSUMPTION from the README's summary). A third-party
  dependency, which this repository does not take without the owner.
- **The parent re-run.** SWE-bench's FAIL_TO_PASS set is the tests that fail on the snapshot before the fix and
  pass after it, found by running the developer's test patch on the pre-fix snapshot
  ([dataset card](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified/raw/67358593635606946cea19233e3335b1b6ca69b9/README.md), snippet).
  Applied to a commit: lay the commit's tests over its parent's tree, require the new tests to fail; on the
  commit, to pass. It does not prove the agent *saw* the red, but it proves what seeing it was for — that the test
  catches the defect — and an agent cannot fake it without editing the check.
- Test-and-commit-or-revert enforces green commits, not a prior red; mutation testing measures tests in general,
  not one fix's (both ASSUMPTION, from memory).

| Mechanism | Proves the test catches the defect | Fakeable | Cost here |
|---|---|---|---|
| A `Red:` line alone | no | by typing it | 20–30 min |
| A ledger of runs in the working tree | if the ledger is trusted | by writing it | about an hour |
| An editor hook (TDD Guard) | edit order only | through the reporter | a dependency |
| **The parent re-run** | **yes** | only by editing the check | about an hour |

## Decided

The parent re-run, as `bundle.py red-check RANGE`, with `Red: none, <reason>` only for an exception such as a
regression guard that passed on arrival (`meta/decisions.md`, phase 2 review of 2026-11-26).
