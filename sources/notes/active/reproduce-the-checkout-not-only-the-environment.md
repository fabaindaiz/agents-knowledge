---
slug: "reproduce-the-checkout-not-only-the-environment"
topic: "verification"
claim: "A number from a check is a function of the commit, the environment and the checkout; reproducing it elsewhere means reproducing all three — pin the environment, and run from a clean export of the commit, because the working tree holds every untracked file the real runner will not have."
confidence: "measured"
phases: ["verify", "debug"]
check: "the number a gate is quoted for was taken from a clean export of the commit, in the declared environment, with the interpreter path and the collation recorded"
about:
  - {do: "Reproduce a gate, a CI run or any check that runs elsewhere, read a number from another environment, or explain why two runs disagree", wrong_when: "the replica was built in the working tree, so it holds credentials, caches and artefacts the real runner has never seen — or a stale environment or another locale produced the number"}
rests_on: "hermetic builds (Bazel); reproducible-builds.org on locales"
strength: "practice"
our_evidence: "measured in two repositories; the permissive direction met in three more"
cues: ["ci passes locally", "works on my machine", "clean checkout", "git archive", "untracked files", "docker image", "python version", "locale", "collation", "lockfile", "gitignored", "env differs", "flaky ci", "git stash", "reproduce failure"]
---

# Reproduce the checkout, not only the environment

## Why it works

A check that runs somewhere else has two inputs, and only one of them is ever discussed. The **environment** — interpreter, pinned dependencies, stubs, operating system — is declared, visible and the first thing blamed when two runs disagree, and reproducing it is real work that people do. The **checkout** is the other input, and it is invisible for the same reason a fish does not discuss water: you are standing in it.

The difference between the two is exactly the set of files nobody declared. Credentials, caches, local datasets, editor state, generated artefacts, a stale virtual environment, the output of the last experiment — every one of them is untracked or ignored, which is another way of saying that the remote runner will not have it. A check that reads one of them gives an answer locally for a reason that does not exist there, and the answer looks like every other answer.

It fails in both directions, and the permissive one is worse. A replica built in the tree has **more** than the real runner, so a check passes because something is present; the report says green, the remote gate says red, and the difference is a file nobody thought of as an input. The strict direction — a leftover file the runner will not have making a check fail — at least announces itself. And the commit can lack what the tree has, not only the reverse: a commit made with an explicit path list leaves out a new untracked file, and the gate run in the tree stays green because the file is on disk.

A fourth input sits beside the commit, the environment and the checkout: **a machine-local file that is never committed on purpose** — a list of private terms, a local allow-list — which changes on its own schedule and can be absent. A check that reads it holds only for the version it read: its verdict names that version (a count or a digest) wherever it is quoted, and a run on a machine where the file is absent reports itself as partial, never as green.

The fix is cheap enough that there is no reason to discuss it: export the commit into a scratch directory (`git archive HEAD | tar -x -C …` or an equivalent), and run the replica there. That is seconds, and it is the one operation that reproduces the checkout exactly, because it reproduces it by definition — what is in the commit, and nothing else.

The environment has its own quiet forms. Two environments on one machine — a stale one earlier on the path than the declared one — produce two different truths with the same commands, so when two measurements disagree, **identify which binary produced each before believing either**, and invoke tools through the project's own interpreter rather than whatever the name resolves to. And any number whose computation orders, formats or compares text is a number about the locale too: fix the collation (`LC_ALL=C`) in every recipe that publishes one.

## When it does NOT apply

- **A hermetic build system already does this**, by declaring every input and sandboxing every action (see *Literature*). Where the tool guarantees that the host and the tree cannot leak in, reproducing the checkout by hand is repeating work that is already done.
- **When the artefact under test is the working tree** — a formatter over uncommitted work, a check on staged changes, a pre-commit hook. The tree is the subject, not the contamination.
- **When the input is committed, or fetched by a pinned digest** — then it is part of the commit, and the export carries it.
- **When the untracked file is the point**: reproducing someone's local state to debug their failure. Then the export is the wrong direction, and what is worth writing down is which file made the difference.

## What it costs

An export and a second install: seconds to minutes, once per investigation. And a sentence in the report saying which inputs were reproduced — because "I reproduced CI" is three claims, and it is usually only one of them.

## Where it came from

One analytics repository, whose remote gate counts type errors against a baseline and runs a suite, measured on **2026-09-22** in two halves that arrived a week apart.

**The environment half.** With the remote logs unavailable, the gate's environment was rebuilt locally to reproduce a count: a replica built without the package installer reported **nearly three times as many errors** as the same replica built with it. Reproducing the environment was necessary, it was what the exercise was about, and it worked — the number that had to be explained moved by more than half on a difference nobody would have called an input.

**The checkout half, which is the one that names this note.** A clean export of `HEAD` **fails one test** that the same suite passes in the working tree, because that test builds a real store client from an ignored credential file which exists only there. The remote gate runs on a checkout and installs no credential. The last replica of that gate had been run **inside the tree**, and had reported the suite green: the environment had been reproduced with care, and the answer was still about a machine nobody else has.

**The same environment half, earlier, in the same repository** (moved 2026-09-24 from `ratchet-in-a-pinned-environment`, where it used to be counted). A stale environment first on the path explained three separately recorded "anomalies" at once: parallel tests "not working" (the plugin was absent there), a few more type errors with the same checker and library versions, and a directory of **dozens of tests that did not collect** because a declared dependency was missing.

**The locale, in a second repository.** A content digest computed over files ordered with the system `sort` depended on the locale: in `en_US` collation the hyphen is skipped, so the same unchanged content hashed to `fdc2ae7e7d36` there and to `2fa14bd0c1e5` in byte order.

**The permissive direction, in three more repositories.** A document repository whose source material is deliberately not versioned, 2026-09-21: the audit's own path checks read an ignored local folder, so the gate was green in the working tree and failed on its first run over a copy without it; the fix turned the absence into an advisory. A code-generator repository at adoption, 2026-10-05: a structural audit resolving the paths that documents name passed in the tree and failed on a copy without the build directory, because generated directories named on purpose exist only where they were built; the audit now lists those paths, each with its reason. In a third, 2026-10-01, a new function was committed without its new test file; the gate stayed green because the file was on disk, a status listing two commits later caught it, and the clean worktree of the commit that its own procedure asks for, skipped that time, would have shown a handful fewer tests. The first two were caught by deliberately running the check on a clean copy: the experiment below, run twice, one disagreement each.

**The machine-local input, in a repository of machine-configuration documents, 2026-09-29, three forms in a week.** The local term list grew a few terms shortly after a push, and a clean clone run as the final check found a handful of failures the local gate had passed a minute earlier, two of them already in published history. On a second machine the list did not exist; the check ran without it as a warning, and commits were pushed with only the generic patterns checked. And the gate went red on an unchanged main branch when the list gained a term that day, from a change made outside the repository; the fix was an allowance with a reason, decided by the owner. The tool already printed how many terms it read and said when the list was absent; nothing recorded that number where a verdict was quoted.

## Literature

- **Bazel, [*Hermeticity*](https://bazel.build/basics/hermeticity).** "When given the same input source code and product configuration, a hermetic build system always returns the same output by isolating the build from changes to the host system"; hermetic builds "are insensitive to libraries and other software installed on the local or remote host machine", tools are treated as source code, and among the named non-hermetic behaviours is "writing to the source tree during the build". *Verified 2026-09-22 against the page.* **What we take:** the framing that the inputs of a check include things nobody wrote down. **Where we go further:** the literature isolates the build from the **host**; this note is about isolating it from the **tree** — files that are there because of your own history, which no declaration mentions and which a hermetic system would never see in the first place. For a project without such a system, an export of the commit is the poor version of the same isolation, and it costs seconds.
- **reproducible-builds.org, ["Locales"](https://reproducible-builds.org/docs/locales/).** "The C locale will sort according to the byte values and is always available." *Verified 2026-09-22 against the page.* **What we take:** pin the collation like any other tool.

## Evidence

**Measured in two repositories.** In the first, three mechanisms: an error count nearly three times higher, produced by a missing installer in the replica's environment; a stale environment first on the path that produced three "anomalies"; and one failing test against none, produced by an ignored credential file in the replica's tree. In the second, one content digest with two values from the locale alone. All were found while trying to explain a number that two runs reported differently.

**2026-10 — occurrences in four more repositories:** the permissive direction three times (an ignored local folder, a build directory, an untracked file left out of the commit) and a machine-local input whose verdict held only for the version read. Occurrences, not a rate; two of them are the clean-copy experiment below run once, each finding one disagreement.

**Not measured:** how often it happens per gate. The experiments: record the interpreter path next to every number written into a document, and count how many disagreements turn out to be environmental; and for every check in a gate, run it once from a clean export of the commit and once in the working tree, and count the checks whose answers disagree. Each disagreement names a file that is an input and was never declared to be one.
