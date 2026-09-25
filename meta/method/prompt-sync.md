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
   be left out.

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

A carrier writes only what it owns: `.agents/carrier.toml` and its harvest outbox, `.agents/tracking/`. Everything else in its `.agents/` is the release it holds, checked by `SHA256SUMS`. So a meta-session is not a merge: it **gathers** what each carrier learned, **releases** once in the home, and **carries** that release into each carrier by itself, **closed by a check** (`align`) rather than by a sentence in a changelog. Carrying releases pairwise by hand was observed to lose things: one carrier's own fields copied into all of them, same-day tracking rows dropped by the copy that overwrote them, a copy distributed with its own checks never run, and no record of who the carriers were.

## The cycle: two meta-sessions around one round of harvests

| | What runs | Why it is where it is |
|---|---|---|
| **1. Align first** | when every carrier is already on the current release, only `release.py align` and `bundle.py check-local`; otherwise this document in full | every harvest then reads the *same* knowledge and writes its candidates against it; a carrier a release behind proposes what the others already have |
| **2. Harvest, per carrier** | `.agents/method/prompt-harvest.md` — phase 0 closes what that repository has in flight, phase 1 writes its outbox | the learning is inside each repository, and only a session with it open can read its record, run its gate and have its owner review the commit |
| **3. Release** | this document, in full | every carrier's candidates on one table is the only place the generality test is honest: a claim offered by two of them is a second occurrence, by one a candidate |

**Step 1 is cheap when nothing diverged, and it is not skipped for that reason**: "nothing diverged" is a claim, and those two commands turn it into a fact. **Between steps 2 and 3, a carrier writes nothing into `.agents/` but its outbox and its `carrier.toml`**; that is what makes step 3 a gathering rather than a merge.

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
| phase 1 | `release.py gather [REPO...] --out DIR` | only `DIR` |
| the offered rows into the records | `release.py intake DIR [--version X.Y.Z]` | `meta/tracking/candidates.md`, `meta/tracking/experiments.md`, `DIR/intake.json` |
| the loss check | `release.py lost BASE SNAPSHOT...` — run by `gather` for a carrier on the layout before 0.0.22 | nothing |
| move a note | `release.py note-state SLUG active\|review\|retired` | `sources/`, its links in `meta/`, then a build |
| the generated knowledge | `release.py build [--check]` | `.agents/knowledge/` (generated files), `SHA256SUMS` and the ledger `meta/tracking/INDEX.md` |
| sizes and the funnel | `release.py report [--check]` | nothing |
| cut the release | `release.py release X.Y.Z` — prints the tag command | `.agents/README.md` version and date, then a build |
| phase 2 | `release.py splice [REPO...]`, then `--write --backup BACKUP --taken DIR` (`DIR`: the gather's) | each carrier, after a backup |
| the carriers table | `release.py register [REPO...]` | `meta/tracking/carriers.md` |
| phase 3 | `release.py align [REPO...]` | nothing |

## Phase 1 — Gather (read-only)

0. **Every carrier should have closed its open session and run its harvest** (`prompt-harvest.md`, phases 0 and 1) since the last release: that is what there is to gather. Run `bundle.py check-local` in each carrier on the current layout. A carrier that changed a file only a release writes has forked it locally — a finding, triaged as a divergence of its own, never folded in silently.
1. **List the carriers**: this session's workspace — **every repository open here and only those** — each with its carrier id, set against `meta/tracking/carriers.md` and the manifest. A carrier with no stored id mints one with `bundle.py carrier-id --mint` once it has a `carrier.toml`; an id is never derived from anything about the repository. A carrier registered, or known to this machine, that the workspace does not hold is **not reached**: nothing is written into it.
2. **Verify every copy**: `bundle.py verify` in each. A copy whose checksums fail is not believed; let content decide from there.
3. **Run `release.py gather [REPO...] --out DIR`.** It snapshots every carrier, reads the version it holds (a pre-0.0.22 integer `version: N` reads as `0.0.N`), and extracts that version's tag, `vX.Y.Z`, as its **base**. For each carrier `DIR/gather.md` lists the rows its outbox offers and what it changed that only a release writes. A carrier on the layout before 0.0.22 is compared line by line instead: its offered rows are the tracking rows it added over its release, and every line it added that the home holds nowhere (`.agents/`, `meta/`, `sources/`) is printed — that is `lost`, built in. A carrier whose version has no tag has no base: say so and compare by hand.
4. **Give every item a verdict**, with the rules of `prompt-merge.md` §*Phase 2 — Classify every item* — *same*, *only in*, *divergent*, *undecidable* — across all carriers at once: each offered row, each forked file, each lost line. Two notes that disagree are reconciled by `prompt-merge.md` §*Reconciling two divergent knowledge notes*, never by date.
5. **Report one reconciliation table and wait for approval.** One table and one approval for every carrier.

## Build the release, once

In the home, never in a carrier.

1. **`release.py intake DIR --version X.Y.Z`**, with the version this release will carry. New candidates enter `meta/tracking/candidates.md` with that version as *Since*; runs enter `meta/tracking/experiments.md` under *Run*. A row whose slug the queue, the history or a note already holds is printed as `already known`: add it to that row or note as another occurrence, which is what admission counts.
2. **Apply the approved verdicts.** **Candidates become the bundle here, and only here**, generalised first (principle 20). Knowledge runs admission (`sources/README.md`, *The lifecycle of a note*); the method, the generality test. **Extend before adding.** A note is written only in full, in `sources/notes/<state>/<slug>.md`, and its frontmatter places it in every table; a state changes only by `release.py note-state`, and a retirement adds a row to `meta/tracking/retired.md`. Experiments a note names go to `meta/tracking/experiments.md` *Queued*. What does not pass stays in the queue with what it lacks; a candidate that leaves it another way gets its row in `meta/tracking/history.md`. The closing review of `sources/README.md` §4 runs here, and a note admitted in this release may only be *kept* or *queued* by it.
3. **Account for every lost line.** Each line gather printed is taken into the file it belongs to or is an approved removal, named in the changelog; a removal for privacy is named generically ("carrier-specific detail removed for privacy"), never restated. Rerun `release.py lost DIR/base/<version>/.agents DIR/carriers/<name>/.agents` until it prints only approved removals.
4. **Check the ledger, `meta/tracking/INDEX.md`, before admitting a note or keeping a candidate**: every note under review or retired, every queued candidate and every answered one is listed there by slug. An idea already listed is extended, merged or left answered, never created again under a new name. Nothing leaves the queue by age: dropping a candidate is a decision of this release, written in `meta/tracking/history.md` with its reason.
5. **No empty releases**: if nothing a carrier reads changed, cut none and say so; a version history of empty releases teaches the next reader that versions mean nothing. Otherwise **write the changelog**: a `## [X.Y.Z] - YYYY-MM-DD` section in `.agents/CHANGELOG.md` (Keep a Changelog), saying what a reader does differently, not what was edited. While the version is `0.0.z`, any release may break.
6. **`release.py build`, then `release.py check`**, which passes (and the tests, when a tool changed); every privacy allowance it lists was given by the user, explicitly.
7. **`release.py release X.Y.Z`.** It refuses a version not newer than every tag, or one the changelog does not describe, then writes the version and date and builds. **Commit** (Conventional Commits; `!` when it breaks), then run the tag command it printed: `git tag -a vX.Y.Z -m "agent-guides X.Y.Z"`. Splice refuses anything but the tagged release.

## Phase 2 — Apply, in each carrier by itself

For each carrier, and **with that carrier as today's repository** (`prompt-context.md` §*Workspaces*):

1. **Dry run first**: `release.py splice REPO`. It lists what would be written and removed.
2. **Write**: `release.py splice REPO --write --backup BACKUP --taken DIR`, with the gather's `DIR`. It refuses a carrier whose shipped files carry uncommitted changes — they belong to whoever left them — backs up its whole `.agents/`, writes every shipped file and `SHA256SUMS`, removes what the release no longer ships, keeps what the carrier owns (`carrier.toml`, the outbox, `incoming/`, evaluation reports), and removes from the outbox the rows intake took. A carrier on the layout before 0.0.22 has its own fields moved from its old headers into `carrier.toml` (refused when two headers disagree), the files that moved to the home removed, and its outbox reset. Uncommitted shipped files the carrier's owner says are theirs and belong in the release are overwritten only with `--allow-dirty`.
3. **Triage what this carrier refuses.** It records a delta it does not take in its own `declined`, with its reason written for a stranger; it never edits a shipped file.
4. **Follow the carrier's own links to the files the splice removed** (its dry run lists them): a decision row or a doc that pointed at a moved file is repointed or reworded in the carrier's own style. **Adapt the host**, if the release asks for it: a gate that must call `bundle.py verify`, a linter that must leave `.agents/` alone. That is the carrier's own code, in its own style.
5. **Run `bundle.py verify` and that carrier's gate there**, and report exactly which selection ran. There is no workspace-level green.
6. **One changelog entry** in that carrier's format and language, with an `s-` id minted there (`bundle.py id s`), and **one commit** on its branch under its own rules — offered, or made if the pre-flight said so.

## Phase 3 — Align, and close

1. **`release.py register REPO...`** writes each reached carrier's row, by its stored id, at the release.
2. **`release.py align REPO...`.** It fails on a carrier that does not verify, whose `SHA256SUMS` is not the home's, or that is missing from `meta/tracking/carriers.md` or registered at another version. **The meta-session is not closed while it reports anything.**
3. **Empty every `incoming/`** this session triaged.
4. **Name what was not reached**: every registered carrier with no path here goes into `meta/roadmap.md`, *Blocked outside*, by its id alone.
5. **Close**: the release under *Done* in `meta/roadmap.md`, and one commit in the home (Conventional Commits). The closing report gives, per carrier, its branch, its commit, the gate selection that ran and what it declined; the verdict counts; every *divergent* item and how it was reconciled; every *undecidable* one, which is the agenda for the next meta-session; and where the backups are.

## What a meta-session must never do

- **Never write before the one table is approved**, and never build the release in a carrier.
- **Never gather, splice or compare by a script written for the occasion.** The tool is the one recipe.
- **Never carry an untagged release**, and never carry one carrier's `carrier.toml` into another.
- **Never write over uncommitted bundle files** without their owner's word.
- **Never close on "the checksums match"** — close on `align`, which also verifies and checks the registry.
- **Never guess a carrier.** One that is not reached is named, not assumed aligned.
- **Never let a private carrier become recognisable** in the release, in `meta/tracking/` or in a changelog, and never write a description beside a carrier id.
- **Never write into a repository this session does not have open**, even when its path is in the manifest. `release.py splice` refuses it; that refusal is the rule, not an obstacle to work around.
