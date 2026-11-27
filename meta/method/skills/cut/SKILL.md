---
name: cut
description: "Use in this repository when a release of the bundle is to be cut, tagged or carried to the carriers, or when asked what the next version would contain. Walks the cut: the scope against the commits, the owner's word, build, check, release, tag. Not for shipping a carrier's own work, which is `ship`, and not for closing a session, which is `close`."
allowed-tools: Bash, Read, Edit, Write, Grep
---

# Cut

Cutting a release of the bundle is **this repository's own procedure**. No carrier runs it, and it
never leaves here: the full order is `meta/method/prompt-sync.md`, and this skill is the short path
through the part that cuts, for a session already in the home with the work merged.

**The cut is never a side effect.** A change to `sources/` is a change to the next release. If the
session was doing something else, say so and stop here.

## 1. Check you are in the home, and that there is a release to cut

```sh
test -f meta/tools/release.py && test -f .agents/carrier.toml
```

No `meta/tools/release.py` and this is a carrier, not the home: stop, and use `ship`.
Then: **no empty releases.** If nothing a carrier reads changed since the last tag, cut none and
say so.

## 2. Walk the scope before asking for the word

Read the release's roadmap item against the commits and against `sources/`, part by part, in one
table: the item, what landed (its commit), what did not, and why. Every record id in it carries
its name. A cut made over a passing check with scoped items not done has been reverted before;
the table is what prevents it.

## 3. The owner's word closes the version

**A passing gate is not that word, and neither is a chosen option.** Show the table of step 2,
name the version proposed, and ask. Wait. Nothing below runs before the answer.

## 4. Intake and the originals

1. `python3 meta/tools/release.py intake DIR --version X.Y.Z`, where `DIR` is the gather's output.
2. Edit **the originals in `sources/`** only; never a file under `.agents/`.
3. A reduction is a build rule, not a deletion: the block keeps its full text and gains its short
   form between `<!-- release: short NAME -->`, `<!-- release: as -->` and `<!-- /release -->`,
   and every normative word, number, inline code span, link target or record id the short form
   drops has a row in `meta/tracking/cut-ledger.md`, or the build fails.
4. Move a note between states with `release.py note-state`, never by hand.
5. Account for every line `gather` reported lost, and check the ledger `meta/tracking/INDEX.md`.

## 5. The changelog

A `## [X.Y.Z] - YYYY-MM-DD` section in `sources/bundle/CHANGELOG.md`, Keep a Changelog, saying
what a reader does differently — not what was edited. A layout change a carrier's audit reads gets
its `Layout:` line under *Changed*.

## 6. Build, check, test

```sh
python3 meta/tools/release.py build
python3 -m unittest discover -s meta/tests -t .
python3 meta/tools/release.py check
python3 meta/tools/release.py report
```

`check` passes, and every privacy allowance it lists was given by the user explicitly. `report`
shows the export under its cap — shrink it before the cut, since `check` only warns between
releases. The release's three layers run here (`MANIFEST.md`): the gate above, the cost pilot
against the previous release's tag, and the trigger eval for every skill whose description changed.

## 7. Cut and tag

```sh
python3 meta/tools/release.py release X.Y.Z
```

It refuses a version not newer than every tag, or one the changelog does not describe. Then commit
through the gate — `python3 meta/tools/release.py commit -m "build: release X.Y.Z" FILE...` — and
run the tag command it printed. The push is a step of its own, never chained to a check or a
commit, and only when the owner asks.

## 8. Then it is a meta-session, not a cut

Carrying the release into the carriers is Phase 2 and Phase 3 of `meta/method/prompt-sync.md`:
`splice`, each carrier's own gate and changelog entry, `register`, and `align` reporting every
reached carrier aligned. Say that it is next, with its cost; this skill ends at the tag.
