---
slug: "an-isolated-copy-is-not-the-working-checkout"
topic: "verification"
claim: "An isolated working copy — a worktree, a container, a fresh clone — holds only what version control tracks, so a hand-off to one states which ignored files it carries, which revision it starts from, and which paths its checks must not walk; otherwise the gate fails there for reasons that have nothing to do with the change."
confidence: "measured"
phases: ["verify", "implement"]
check: "run the repository's own gate in a fresh clone or worktree with nothing copied in; every failure it reports that the working checkout does not is an undeclared input, and is either removed, declared in the hand-off, or excluded from the check by path"
about:
  - {do: "Hand work to an agent, a container or a CI job in a copy of the repository", wrong_when: "the gate, a linter or a path audit depends on something git ignores, or the copy starts from the default branch instead of the branch being worked on"}
rests_on: "hermetic builds"
strength: "practice"
our_evidence: "measured in one owner's repositories; four of them, counted as one source"
boundary: "A hermetic build, which has already paid this cost by declaring its inputs · a repository with no ignored inputs at all · a copy made by copying the whole directory rather than by checking out, which carries the ignored files and loses the isolation instead"
cues: ["worktree", "fresh clone", "container build", "gitignore", "local config", "sdk path", "gate fails in CI", "works on my machine", "delegate", "sandbox", "path audit", "isolated review", "ci only failure"]
---

# An isolated copy is not the working checkout

## Why it works

A working checkout is two things at once: the tracked tree, and everything that has accumulated beside it — local toolchain configuration, credentials, caches, generated directories, scratch folders. Only the first travels. An isolated copy is therefore a different machine wearing the same name, and three failures follow from that one fact:

- **The gate depends on something nobody declared.** A build or check that reads an ignored file passes for whoever has that file and fails for everyone else. The failure arrives as a message about the change, which is the expensive part: the agent reading it has no reason to suspect its own environment.
- **The copy starts from the wrong revision.** A worktree or container created from the default branch does not contain the branch being worked on, so a delegate sent to read "the plan" or "the brief" finds an older one, or none, and reports on what it could see.
- **The checks walk paths that exist only there.** An audit of document paths, a formatter or a test collector run inside the copy sweeps in the copy's own scaffolding — nested worktrees, build output, the agent's working folders — and reports them as the repository's.

The remedy is not to make the copy more like the checkout. It is to say, once, in the procedure that creates it: these ignored files are carried and why, this is the revision it starts from, these paths are not part of the repository. Each of the three is cheap to write and none of them is discoverable from inside the copy.

## When it does NOT apply

- A hermetic build, where inputs are declared and the build is insensitive to the host, this problem has already been paid for in a better way. The hermetic answer to an undeclared input is to remove it, not to carry it — so where that is affordable, do that instead and this note is only the fallback.
- A copy made by copying the directory rather than by checking out: it carries the ignored files, and loses the isolation that made it worth making.
- A repository with nothing ignored that any check reads. Rare, and worth knowing you are in.

## What it costs

A list that must be maintained: ignored files carried into a copy are an undeclared dependency written down rather than removed, and the next person to add one will not update the list. The path exclusions are a second place where "what is the repository" is defined, and it can drift from the first.

## Where it came from

Four repositories of one owner, which count as one source.

In the first, at least six incidents over three days: two delegated agents broke on a document-path audit, four on local toolchain configuration that version control ignores. The audit was narrowed twice, with successively tighter exceptions, rather than redesigned — which is its own lesson, since the second failure of one check for one cause is the point to change the check's design and not to add another exception.

In a second, the same gate failure appeared three times in three days before it was fixed on the main branch. In a third, delegate worktrees created inside the agent's own folder were read by the repository's audit as if they were the repository, producing on the order of a hundred failures, and those delegates started from the main branch rather than the working one, so what they had been told to read was not there. In a fourth, a reviewer could not read its brief at all: the brief had been written to an unversioned folder of the main checkout.

The same owner's sandbox adds a fourth shape, recorded as a boundary rather than a claim: where writes to a versioned folder are refused, switching between branches that differ there fails halfway and leaves the copy with most of a hundred files removed, so a fast-forward is done without switching branches.

## Literature

The mechanism is the well-established problem of non-hermetic builds. Bazel's documentation holds that a build should be insensitive to the host and should be verified in a container holding only the checked-out source plus an explicit list of host tools, precisely so that implicit dependencies surface as failures; it also names writes into the source tree as a source of non-hermeticity. Twelve-factor warns that configuration and credentials kept outside version control are easy to lose track of. Work cited in a 2024 study of local buildability reports that a large share of open-source projects fail to build outside their authors' environments, though it does not isolate ignored files as the cause. **What we take:** the explanation, and the clean-environment run as the check. **What we add:** the procedural rule for handing work to an isolated copy — the ignored files carried, the revision, the paths checks must not walk. We found no source stating it, and no source at all addressing the third. **Where we differ:** the hermetic tradition would remove the dependency rather than carry it, so this note is explicitly the fallback for repositories that are not hermetic. The claim that a fresh worktree contains only tracked files is documented behaviour we did not re-verify.

## Evidence

**Measured in one owner's repositories, four of them, which count as one source.** At least six incidents over three days in the first; three occurrences in three days in the second; about a hundred audit failures in the third, plus delegates starting from the wrong branch; one unreadable brief in the fourth. No rate: these are counted incidents, not a share of runs.

What would settle it: across repositories that hand work to isolated copies, the share of gate failures in the copy that the working checkout does not reproduce, and how many of those trace to an ignored input rather than to the change. A cheaper first step, available to any carrier: run the gate once in a fresh clone with nothing copied in, and count what it reports.
