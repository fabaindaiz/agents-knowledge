# Release and carry the bundle in one meta-session

## ▶ Paste this to start

**List the carriers first**, in the local manifest `~/.config/agent-guides/carriers.toml`
(`carriers = ["/path/to/repo", ...]`) — this machine's paths, never written into the bundle.
Then paste the block below, in the home repository.

**╔══════════ COPY EVERYTHING INSIDE THE BOX BELOW ══════════╗**

~~~text
You are running a meta-session over every carrier of the agent guides, from
the home repository. Follow `meta/method/prompt-sync.md`, with
`.agents/method/prompt-context.md` beside it for the reasoning, and run its
mechanical steps with `meta/tools/release.py` and each carrier's
`.agents/tools/bundle.py` — never by a script written for the occasion.

**FIRST, before reading anything else: run the pre-flight.** Open that document
§*Before you start*, ask me those questions in one message, and wait. Then
read only this:

Reads:
- meta/method/prompt-sync.md
- meta/method/prompt-merge.md §Phase 2 — Classify every item (read-only). Report before writing. §Reconciling two divergent knowledge notes
- .agents/method/prompt-context.md §Workspaces: several repositories at once §Keeping the set versioned, so other copies can catch up §20. Nothing private travels, directly or by reconstruction
- .agents/README.md §The fields that are this repository's
- sources/README.md
- .agents/knowledge/README.md
- meta/tracking/INDEX.md
- meta/tracking/experiments.md

Then work the three phases. **Phase 1 is read-only, and you write nothing
until I approve the reconciliation table.** Phase 2 happens in each carrier by
itself, under that carrier's own conventions. Phase 3 does not end until
`release.py align` reports every carrier aligned, or names the ones that are
not and why.

Non-negotiable while you work: every item gets a verdict; nothing a carrier
added is lost without being named; each carrier keeps its own
`.agents/carrier.toml`; each carrier's gate runs in that carrier; uncommitted
work in a carrier belongs to whoever left it.

Privacy (principle 20): nothing that enters the release or `meta/tracking/`
may identify, directly or by reconstruction, a private carrier, its people or
its users; generalise first, and `release.py check` must pass before the
release is cut.
~~~

**╚══════════ COPY EVERYTHING INSIDE THE BOX ABOVE ══════════╝**

---

## Before you start — ask these

**Ask all of them in one message, then stop.**

~~~text
Before I cut a release and bring every carrier onto it, four things — reply
`defaults` to take them as proposed.

1. The carriers. I will use the manifest's list and compare it with
   `meta/tracking/carriers.md`. A carrier registered there with no path here
   stays out and is named as not reached. Say if any path is missing or should
   be left out. For each carrier, I will read from its own rules which branch an
   update starts from (its integration branch, not the bundle branch a last
   meta-session left) and how it lands (a ticket branch and a pull request, or a
   direct commit); say where I read it wrong.

2. Uncommitted work. Where a carrier's `.agents/` has uncommitted changes, I
   will stop on that carrier and ask, unless you tell me now that they are
   yours and belong in this release.

3. The version. I will propose the next patch version, `0.0.z`. Moving to
   `0.1.0` or `1.0.0` is yours to decide; say so if this is that release.

4. Commits. By default I commit and tag the release here, and offer one commit
   per carrier, following that repository's own commit rules and branch. Say if
   I should commit there too, or leave every carrier uncommitted.
~~~

---

## Why one meta-session

A carrier writes only what it owns: `.agents/carrier.toml` and its proposals, one file each in `.agents/proposals/`. Everything else in its `.agents/` is the release it holds, checked by `SHA256SUMS`. So a meta-session is not a merge: it **gathers** what each carrier learned, **releases** once in the home, and **carries** that release into each carrier by itself, **closed by a check** (`align`) rather than by a sentence in a changelog. Carrying releases pairwise by hand was observed to lose things: one carrier's own fields copied into all of them, same-day tracking rows dropped by the copy that overwrote them, a copy distributed with its own checks never run, and no record of who the carriers were.

## The cycle: two meta-sessions around one round of harvests

| | What runs | Why it is where it is |
|---|---|---|
| **1. Align first** | when every carrier is already on the current release, only `release.py align` and `bundle.py check-local`; otherwise this document in full | every harvest then reads the *same* knowledge and writes its candidates against it; a carrier a release behind proposes what the others already have |
| **2. Harvest, per carrier** | `.agents/method/prompt-harvest.md` — phase 0 closes what that repository has in flight, phase 1 writes its proposals | the learning is inside each repository, and only a session with it open can read its record, run its gate and have its owner review the commit |
| **3. Release** | this document, in full | every carrier's candidates on one table is the only place the generality test is honest: a claim offered by two of them is a second occurrence, by one a candidate |

**Step 1 is cheap when nothing diverged, and it is not skipped for that reason**: "nothing diverged" is a claim, and those two commands turn it into a fact. **Between steps 2 and 3, a carrier writes nothing into `.agents/` but its proposals and its `carrier.toml`**; that is what makes step 3 a gathering rather than a merge.

## The tool

`meta/tools/release.py` is the home's half (Python 3.11+, standard library only); it loads the carrier tool, `.agents/tools/bundle.py`, so every rule both need exists once. Its tests: `python3 -m unittest discover -s meta/tests -t .`. **A command that writes is given the repositories; it never works them out** (`prompt-context.md` §*Workspaces: several repositories at once*). A read-only command may fall back to the manifest, and says so.

| Step | Command | Writes |
|---|---|---|
| verify one copy | `bundle.py verify [TREE]`, in the carrier | nothing |
| what a carrier changed | `bundle.py check-local [REPO...]` — by checksums, only what it owns may differ | nothing |
| a carrier's id | `bundle.py carrier-id [REPO]`; `--mint` writes a random one, once | `--mint`: its `carrier.toml` |
| a record id in a carrier | `bundle.py id d\|i\|s TEXT... [--repo REPO]` — minted once, frozen | nothing |
| the privacy check | `bundle.py privacy [TREE] [--paths FILE...]` | nothing |
| the home's CI | `release.py check` — verify, `build --check`, privacy and links of `meta/` and `sources/`, the home sessions' reads, budgets | nothing |
| phase 1 | `release.py gather [REPO...] --out DIR [--packs FILE...]` | only `DIR` |
| the proposals into the records | `release.py intake DIR [--version X.Y.Z]` | `meta/tracking/candidates.md`, `meta/tracking/experiments.md`, `meta/tracking/received.md`, `DIR/intake.json` |
| the loss check | `release.py lost BASE SNAPSHOT...` — run by `gather` for a carrier on the layout before 0.0.22 | nothing |
| move a note | `release.py note-state SLUG active\|review\|retired` | `sources/`, its links in `meta/`, then a build |
| the generated knowledge | `release.py build [--check]` | `.agents/knowledge/` (generated files), `.agents/proposals/RECEIVED.md`, `SHA256SUMS` and the ledger `meta/tracking/INDEX.md` |
| sizes and the funnel | `release.py report [--check]` | nothing |
| cut the release | `release.py release X.Y.Z` — prints the tag command | the version and date in `sources/bundle/README.md`, then a build |
| phase 2 | `release.py splice [REPO...]`, then `--write --backup BACKUP` | each carrier, after a backup |
| a carrier's proposals | `bundle.py proposals [--prune \| --pack FILE \| --from-outbox]`, in the carrier | `--prune` and `--from-outbox`: its `proposals/`; `--pack`: `FILE` |
| the carriers table | `release.py register [REPO...]` | `meta/tracking/carriers.md` |
| phase 3 | `release.py align [REPO...]` | nothing |
| the template's release | `bundle.py export DEST`, from the tagged home | only `DEST`, which must be empty |

## Phase 1 — Gather (read-only)

0. **Every carrier should have closed its open session and run its harvest** (`prompt-harvest.md`, phases 0 and 1) since the last release: that is what there is to gather. Run `bundle.py check-local` in each carrier on the current layout. A carrier that changed a file only a release writes has forked it locally — a finding, triaged as a divergence of its own, never folded in silently.
1. **List the carriers**: this session's workspace — **every repository open here and only those** — each with its carrier id, set against `meta/tracking/carriers.md` and the manifest. **Search, never trust the manifest alone**: look for bundle folders on disk, and read every branch, local and remote, of every repository there, because a bundle kept on a branch that is not checked out leaves no folder (`release.py carriers` lists the branches that hold one, and at which version); a carrier found that the manifest lacks is added to it. **Compare each carrier's branch with its remote** (`git fetch`, then the two heads): `gather` reads the working tree, so a checkout left behind by a history rewrite, or never pulled, offers an old bundle as current. Where they differ, the remote is the record unless the user says otherwise; the session works on a new branch cut from the remote, never by resetting the old one, and moving the old branch is the owner's step afterwards. A carrier with no stored id mints one with `bundle.py carrier-id --mint` once it has a `carrier.toml`; an id is never derived from anything about the repository. A carrier registered, or known to this machine, that the workspace does not hold is **not reached**: nothing is written into it.
2. **Verify every copy**: `bundle.py verify` in each. A copy whose checksums fail is not believed; let content decide from there.
3. **Run `release.py gather [REPO...] --out DIR`.** It snapshots every carrier, reads the version it holds (a pre-0.0.22 integer `version: N` reads as `0.0.N`), and extracts that version's tag, `vX.Y.Z`, as its **base**. For each carrier `DIR/gather.md` lists the proposals it offers and what it changed that only a release writes. An outbox of 0.0.22 or 0.0.23 still in its `tracking/` is read as proposals too, one per row, each with the id the carrier's conversion will give it, so nothing is taken in twice. A carrier this session cannot open may send its proposals as one file (`bundle.py proposals --pack FILE`, run there); `--packs FILE...` reads them as they are, never extracting anything. A carrier on the layout before 0.0.22 is compared line by line instead: its offered proposals are the tracking rows it added over its release, and every line it added that the home holds nowhere (`.agents/`, `meta/`, `sources/`) is printed — that is `lost`, built in. The rows of its candidate and run tables are not among them: they travel as proposals, recorded by id when taken in, and a splice refuses a carrier with any other added line in `tracking/` the home does not hold. A carrier whose version has no tag has no base: say so and compare by hand.
4. **Give every item a verdict**, with the rules of `prompt-merge.md` §*Phase 2 — Classify every item* — *same*, *only in*, *divergent*, *undecidable* — across all carriers at once: each proposal, each forked file, each lost line. Two notes that disagree are reconciled by `prompt-merge.md` §*Reconciling two divergent knowledge notes*, never by date.
5. **Report one reconciliation table and wait for approval.** One table and one approval for every carrier.

## Build the release, once

In the home, never in a carrier.

1. **`release.py intake DIR --version X.Y.Z`**, with the version this release will carry. New candidates enter `meta/tracking/candidates.md` with that version as *Since*; runs enter `meta/tracking/experiments.md` under *Run*. A proposal whose slug the queue, the history or a note already holds is printed as `already known`: add it to that row or note as another occurrence, which is what admission counts. Every proposal taken in gets a row in `meta/tracking/received.md` — its id, this version and where it went, never its carrier — and one already there is skipped. A proposal written against a release after which its note changed is printed as `written against an older release`: read the note again before merging it. A proposal that does not read whole is printed as `not taken in` and stays in its carrier, which fixes it.
2. **Apply the approved verdicts.** **Candidates become the bundle here, and only here**, generalised first (principle 20). Knowledge runs admission (`sources/README.md`, *The lifecycle of a note*); the method, the generality test. **Extend before adding.** A note is written only in full, in `sources/notes/<state>/<slug>.md`, and its frontmatter places it in every table; a state changes only by `release.py note-state`, and a retirement adds a row to `meta/tracking/retired.md`. Experiments a note names go to `meta/tracking/experiments.md` *Queued*. What does not pass stays in the queue with what it lacks; a candidate that leaves it another way gets its row in `meta/tracking/history.md`. The closing review of `sources/README.md` §4 runs here, and a note admitted in this release may only be *kept* or *queued* by it.
3. **Account for every lost line.** Each line gather printed is taken into the file it belongs to or is an approved removal, named in the changelog; a removal for privacy is named generically ("carrier-specific detail removed for privacy"), never restated. Rerun `release.py lost DIR/base/<version>/.agents DIR/carriers/<name>/.agents` until it prints only approved removals.
4. **Check the ledger, `meta/tracking/INDEX.md`, before admitting a note or keeping a candidate**: every note under review or retired, every queued candidate and every answered one is listed there by slug. An idea already listed is extended, merged or left answered, never created again under a new name. Nothing leaves the queue by age: dropping a candidate is a decision of this release, written in `meta/tracking/history.md` with its reason.
5. **Rows taken in between releases wait outside the build's inputs.** A row a carrier added over its release that is neither a candidate nor a run (a queued experiment, say) is held in `meta/roadmap.md` until the release, never in a tracking file that generates a shipped page: taking it into `experiments.md` between releases makes `knowledge/OPEN.md` stale against its sources. At the release, move each such row to where it belongs.
6. **No empty releases**: if nothing a carrier reads changed, cut none and say so; a version history of empty releases teaches the next reader that versions mean nothing. Otherwise **write the changelog**: a `## [X.Y.Z] - YYYY-MM-DD` section in `sources/bundle/CHANGELOG.md` (Keep a Changelog), saying what a reader does differently, not what was edited. While the version is `0.0.z`, any release may break.
7. **`release.py build`, then `release.py check`**, which passes (and the tests, when a tool changed); every privacy allowance it lists was given by the user, explicitly.
7a. **Test the release in its three layers before cutting it** (`MANIFEST.md`, `d-5ed7e8-7cac23`): the gate above; a cost pilot on the pilot tasks with three arms in one run, `minimal`, the previous release taken from its tag (`evals/harness.py` `TAG_BUNDLES`) and the candidate, registered in `evals/PROTOCOL.md` before its first trial, which fails the release if the candidate costs more than ×1.10 of the previous release or a discriminating task passes fewer times (`d-5ed7e8-86df04`); its ratio against `minimal` is reported toward the manifest's aim; and `evals/skills/trigger.py` for every skill whose description changed, with `--gate lenient` where `meta/decisions.md` says so. About an hour, more when skills changed. The external benchmark is run once, not here (`d-5ed7e8-d47ee1`). One release a month carries what accumulated; a privacy or data-loss fix is a patch at any time.
8. **The cut waits for the owner's word that the version is closed.** A passing rule or a chosen option to ship is not that word. Before asking for it, walk the release's roadmap item against the commits and the sources, part by part, in a table that gives each record id its name, and show what did not land (2026-10-08: a cut made after a passing pilot, with three scoped items not done, was reverted). Then **`release.py release X.Y.Z`.** It refuses a version not newer than every tag, or one the changelog does not describe, then writes the version and date and builds. **Commit** (Conventional Commits; `!` when it breaks), then run the tag command it printed: `git tag -a vX.Y.Z -m "agent-guides X.Y.Z"`. Splice refuses anything but the tagged release.

## Phase 2 — Apply, in each carrier by itself

**First, when the release changes wording an agent follows or a path a carrier references, review each carrier in execution**: one read-only agent per carrier reads that carrier's own definitions of work (its task tracker, plans, review, commits, logs, gate, audit) beside what the release makes an agent do there, and classifies every meeting point as a conflict in execution, a broken reference, an unstated precedence, or wording only. The tool tests and each carrier's `verify` prove the files; only this reading proves the carrier still works as it defines itself. A conflict found is fixed in the bundle before the release is carried, or named for that carrier's own commit. (The queued `dry-run-a-procedure-by-an-agent-before-release` is the same reading applied to the procedure itself.)

**Then run each carrier's own audit over the new release in a scratch copy**: a carrier's audit that reads a file the release generates by its layout breaks when the layout changes while `bundle.py verify` stays green, and only running it finds that.

For each carrier, and **with that carrier as today's repository** (`prompt-context.md` §*Workspaces*):

1. **Dry run first**: `release.py splice REPO`. It counts what would be written and names every path it would remove.
2. **Write**: `release.py splice REPO --write --backup BACKUP`. It refuses a carrier whose shipped files carry uncommitted changes — they belong to whoever left them — backs up its whole `.agents/`, writes every shipped file and `SHA256SUMS`, removes what the release no longer ships, and keeps what the carrier owns (`carrier.toml`, its proposals, `incoming/`, evaluation reports). **It never removes a proposal.** An outbox of 0.0.22 or 0.0.23 is turned into one proposal per row before its tables go, whether or not it was gathered. A carrier on the layout before 0.0.22 has its own fields moved from its old headers into `carrier.toml` (refused when two headers disagree), the files that moved to the home removed, and the tracking rows it added over its release turned into proposals (refused when that release has no tag here). Uncommitted shipped files the carrier's owner says are theirs and belong in the release are overwritten only with `--allow-dirty`.
3. **Triage what this carrier refuses.** It records a delta it does not take in its own `declined`, with its reason written for a stranger; it never edits a shipped file.
4. **Follow the carrier's own links to the files the splice removed** (its dry run lists them): a decision row or a doc that pointed at a moved file is repointed or reworded in the carrier's own style; append-only history (a changelog, a session log) keeps what it said. **Adapt the host**, if the release asks for it: a gate that must call `bundle.py verify`, a linter that must leave `.agents/` alone, the reviewer copied into the assistant's agent folder and the root file's knowledge line rewritten as the bootstrap's Phase 4 words it (the carrier's live update procedure may predate that step). That is the carrier's own code, in its own style.
5. **Run `bundle.py proposals --prune` there**, which is the carrier's own tool removing what the release lists as received, and report what it printed. **Then run `bundle.py verify` and that carrier's gate there**, and report exactly which selection ran. There is no workspace-level green.
6. **One changelog entry** in that carrier's format and language, with an `s-` id minted there (`bundle.py id s`), and **one commit** on its branch under its own rules — offered, or made if the pre-flight said so.

## Phase 3 — Align, and close

1. **`release.py register REPO...`** writes each reached carrier's row, by its stored id, at the release.
2. **`release.py align REPO...`.** It fails on a carrier that does not verify, whose `SHA256SUMS` is not the tagged release's, or that is missing from `meta/tracking/carriers.md` or registered at another version. **The meta-session is not closed while it reports anything.**
3. **Empty every `incoming/`** this session triaged.
4. **Name what was not reached**: every registered carrier with no path here goes into `meta/roadmap.md`, *Blocked outside*, by its id alone.
5. **Close**: the home's own learnings as its proposals (`prompt-harvest.md`), the release under *Done* in `meta/roadmap.md`, *Where we are* rewritten there for the next session, and one commit in the home (Conventional Commits), pushed with the tag. The closing report gives, per carrier, its branch, its commit, the gate selection that ran and what it declined; the verdict counts; every *divergent* item and how it was reconciled; every *undecidable* one, which is the agenda for the next meta-session; and where the backups are.
6. **Refresh each template repository**, one a new project is started from, when its clone is open on this machine. It is not a carrier: it holds no `carrier.toml`, so every repository started from it mints its own id, and it is never registered or aligned. From the tagged home, `bundle.py export DIR/.agents` into an empty folder, then replace the template's `.agents/` with it (`rsync -a --delete DIR/.agents/ TEMPLATE/.agents/`) and copy every agent in `.agents/agents/` over the template's `.claude/agents/` copies (from 0.0.30, the reviewer and the researcher). In the template, `bundle.py verify --release` passes and `git status` shows changes under those two folders only; its other files (its read-me, its gate workflow, its commit hook) are its own and change only by hand. One commit, `chore: agent-guides X.Y.Z`, and the tag `vX.Y.Z` on it, pushed under the template's own rules. A template not open here is not refreshed: the closing report says so.

## What a meta-session must never do

- **Never write before the one table is approved**, and never build the release in a carrier.
- **Never gather, splice or compare by a script written for the occasion.** The tool is the one recipe.
- **Never carry an untagged release**, and never carry one carrier's `carrier.toml` into another.
- **Never write over uncommitted bundle files** without their owner's word.
- **Never close on "the checksums match"** — close on `align`, which also verifies and checks the registry.
- **Never guess a carrier.** One that is not reached is named, not assumed aligned.
- **Never leave a long meta-session to a machine that may sleep, or to gates run in parallel**: a sleeping
  machine fires every wall-clock timer at wake, and parallel gates compete for it
  (`prompt-context.md` §*Long runs and delegates*).
- **Never let two parallel agents share a scratch directory.** Each gets its own, named for its task, and a destructive step there (planting a violation, deleting a folder) first checks that its target resolves inside it.
- **Never let a private carrier become recognisable** in the release, in `meta/tracking/` or in a changelog, and never write a description beside a carrier id.
- **Never write into a repository this session does not have open**, even when its path is in the manifest. `release.py splice` refuses it; that refusal is the rule, not an obstacle to work around.
