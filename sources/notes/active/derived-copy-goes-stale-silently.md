---
slug: "derived-copy-goes-stale-silently"
topic: "failure-behaviour"
claim: "When a derived artefact can be served or read in place of its source, delete it on every write to the source or make the source win by rule, and never decide freshness on modification time alone."
confidence: "measured"
phases: ["implement", "debug"]
check: "edit the source with an older timestamp, and again keeping its size and time: every derived copy is rebuilt or refused, whichever path consumes it"
about:
  - {do: "Add a cache, a precompressed file, a baked artefact or a build step keyed on timestamps", wrong_when: "the copy can be served in place of the source, and nothing removes it when the source changes"}
rests_on: "Pennarun 2018 on mtime"
strength: "practitioner"
our_evidence: "measured in four repositories; occurrences in three more"
---

# A derived copy goes stale silently

## Why it works

Caches, compressed twins, compiled forms, baked previews and class indexes all exist to be used *instead of* their source. That is their whole value and their whole risk: once a consumer prefers the derived copy, a write to the source changes nothing the consumer sees, and no error is raised — the old answer is a perfectly valid answer. The defect shows up far from its cause, as "my change did nothing".

Two rules close it. **Invalidate on write**: whatever rewrites a source removes its derived twins in the same step, so the consumer falls back to the source until the copy is rebuilt. **The source wins**: where both may exist, a rule says the source is read and the copy ignored, so a stale copy costs time, never correctness.

Modification time is the usual freshness test and a weak one: a move or a preserving copy keeps the old time, a clock or a filesystem's precision can order two writes wrongly, and a tool that sees "nothing newer" does nothing, successfully. Which edit it misses depends on the comparison. A *newer-than* comparison misses an edited source dated before its copy. An *equality* key over size and modification time notices that edit and misses one that keeps both, widened to the precision at which the time is stored: a key normalised to milliseconds misses a sub-millisecond difference, and an interpreter's bytecode cache keyed on whole seconds and size serves a stale compiled module when a source is changed and restored within the same second at the same size, which is what a mutation probe does. After such a probe, use hash-checked caches, turn cache writing off, or delete the cache.

**The freshness check sits on the path every consumer takes**, not in the build script alone. A rebuild guarded by a stamp is bypassed by any consumer that reuses an existing artefact without passing the step that checks the stamp, and a test suite that imports the generated copy of a tool tests the previous build, not the source being edited. Call the build every time (it is cheap when the stamp matches), and test the original, letting the build check the copy.

## When it does NOT apply

- **Content-addressed copies** — keyed by a hash of their source, they cannot be stale, only absent.
- **Copies that are never read in place of the source** (a log, a report).
- **When rebuilding on every write is too expensive** — then keep the copy, but key freshness on content (hash, size, inode) rather than on time alone, and make staleness visible in a readout.

## What it costs

Rebuild time after every write, or a few bytes served uncompressed until the copy is regenerated; a hash or a richer comparison where a timestamp used to do.

## Where it came from

One repository, a client application deployed as a web build to a runtime its developers cannot observe. Its local server prefers a precompressed twin of any file when one exists; on 2026-09-17 the step that stamps a new cache version rewrote the page and the service worker after compression had already run, so the target received **the previous service worker** — a stale build served by the very step whose job is to prevent stale builds. The stamping step now deletes the twins of every file it rewrites; without a twin the server falls back to the file, which costs a few kilobytes on two small files and cannot be wrong.

Twice more the copy won silently. Restoring a deliberately broken table with a move kept its old modification time, the importer saw nothing new, and the gate kept failing on the broken import until the file was touched. After a long absence the gate was green while the validator failed to load, because a stale class index left several classes unresolved. That incident has two halves: its cause, a stale cache read in place of its source, belongs here; why the gate stayed green through it — a failure that did not change the exit code — is `a-check-must-be-seen-to-fail`.

The source-wins form is the repository's design elsewhere: when a content description and a baked copy of it both exist, the description wins, because the other order would let the copy silently override the data it was made from, and edits would do nothing until someone regenerated it. Its content packages are regenerated by every tool that runs the product, and a source folder newer than its package stands in for it and fails the gate — a check that, like the regeneration of its interface layouts, still compares modification times.

## Literature

- **Pennarun, 2018, ["mtime comparison considered harmful"](https://apenwarr.ca/log/20181113).** "Rebuilding a target because its mtime is older than the mtimes of its dependencies, like make does, is very error prone"; track inode, size, owner and mode as well. *Verified 2026-09-22 against the post.* **What we take:** the mtime caveat. **Where we go further:** the served-in-place case, where the stale copy is not merely unrebuilt but preferred.
- **PEP 552, "Deterministic pycs".** *Cited from a carrier's proposal; its text was not fetched.* The carrier read the interpreter's own loader source: a cached module records its source's modification time in whole seconds and its size, and is rejected only when either differs; a hash-checked mode exists. **What we take:** the equality-key blind spot, in a runtime rather than a build.

## Evidence

**From three incidents:** one stale service worker shipped by the anti-staleness step itself; one reimport that did nothing after an mtime-preserving move; one green gate over unresolved classes.

**Measured, 2026-09-22, in two repositories.** The queued experiment — give every mtime-keyed step an edited source dated *before* its derived copy, and record which ones notice — was run in both. In the client application, **none of its three noticed**: the scaffold-if-needed check, with its interface builders back-dated against the layouts they write, asked for no rebuild; the precompressed twin was kept without re-encoding; and the stale twin was served in place of the newer source, which is the one of the three that reaches the target. In an analytics repository with exactly one such step — a columnar cache served beside its source when it is newer — the second read returned **the first file's rows, with no warning**, while the source on disk held the new content. All four mtime-keyed steps in two repositories are blind to an edited source that is not newer, and not one of them reports anything. The step whose own comment declared this as its limit was right, and the declaration is now an observation.

**2026-10-03 — a second form, in an app repository with an on-device test suite.** A test runner writes its results to a fixed path, so a run that fails before writing leaves the previous run's file to be read as this one's; one session's sweep was first written against such a stale file, and the repository now deletes the results before every run. The reverse holds too: the build tool clears its capture folder on every run, so the evidence of the last run is lost unless it is copied out at once. Related, still queued: `gate-reads-untracked-derived-state`.

**2026-09-24 — the content-addressed exemption observed, in a repository building data artefacts.** One content-keyed step, a checksum check over a built bundle run by the repository's audit, was given a source edited and stamped with an old date, and still refused it. One step only; the second was not run, because staging it meant editing a published catalogue.

**2026-09-28 — the copy a test suite imports, in the bundle's home.** Tools generated into a release folder were tested through the release copy, so edits to the original stayed untested until a rebuild, and a rebuild was not allowed while an experiment was reading that folder.

**2026-10-03 — a runtime's own cache, in an app repository.** A mutation probe in a checker script was reverted within one second; the mutant's bytecode stayed in use, and the gate went red on an untouched file until the cache was deleted. The carrier verified the mechanism in the interpreter's loader source.

**2026-10-04 — the experiment on an equality key, in a web service.** A scan cache skips re-downloading a remote file whose path, size and modification time equal the previous scan's entry, with a periodic full scan that trusts no entry. Its planning function was run with a changed file under four timestamps: an older-dated edit was noticed, a newer-dated one was noticed, one with identical size and time was missed, and one differing by less than a millisecond was missed, because the key is normalised to the store's millisecond precision so that it survives a round trip; full mode noticed all. Verdict: moves the boundary, as now written under *Why it works*. The module's own documentation named a restore that keeps old timestamps as invisible to the cache, which the run shows is wider than the real blind spot. The scheduled full scan is this note's bounded-staleness remedy.

**2026-10-05 — a stamp bypassed by its consumers, in a code-generator repository.** A host build of a vendored tool was patched and stamped so that older builds would rebuild; two consumer scripts reused any existing binary and so ran the unpatched one. A fresh-context review of the fix found it; every consumer now calls the build script every time.

**Still unmeasured:** whether a step keyed on content (hash, size, inode) is reached in practice before the stale copy is served. Answered for one content-keyed step (it refused) and one equality-keyed step (it missed only an edit that kept size and time). Each carrier's mtime-keyed steps are its own, so the experiment stays queued for the ones that have not run it.

**2026-09-24, offered at 0.0.29 — a restated procedure is a derived copy too.** A carrier skill that restated how the method is changed (edit its documents directly, raise the version) went on being followed as written after the method made releases the only writer: in two carriers' state-review skills, read in place of the method they copied.
