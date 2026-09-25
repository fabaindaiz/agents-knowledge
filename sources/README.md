# Sources — the full notes and what the release is built from

`notes/<state>/<slug>.md` is the one place a note is written, in full. `templates/` holds the index prose, with a marker where each generated table goes (`<!-- generated: cards TOPIC -->`, `<!-- generated: about -->`, `<!-- generated: founded -->`, and `{{notes:PHASE}}` in `INDEX.md`). `python3 meta/tools/release.py build` writes the short notes, every index table, `knowledge/OPEN.md` and `SHA256SUMS` into `.agents/`; nothing generated there is edited by hand, and `build --check` fails when it is not what these sources produce. [`references.md`](references.md) and [`layout.md`](layout.md) are the literature and the layout survey the bundle rests on.

## A full note

A frontmatter block in YAML (strings double-quoted; `meta/tools/check_yaml.py` proves PyYAML reads it as the tools do), a title, and six sections: *Why it works*, *When it does NOT apply*, *What it costs*, *Where it came from*, *Literature*, *Evidence*. A carrier receives the card fields and the first three sections; the last three stay here. Each paragraph is one line, and the claim is not repeated under the title.

| Field | Holds |
|---|---|
| `slug` | the file name without `.md` |
| `topic` | one topic, which must have a `cards` marker in one area template |
| `claim` | the heuristic in one sentence; its only wording, quoted by every table |
| `confidence` | `measured`, `reasoned` or `inherited`: **our** evidence, never the literature's |
| `phases` | where the phase guide lists it: any of `plan`, `dataset`, `implement`, `tests`, `review`, `verify`, `debug` |
| `check` | what shows it holds in the change at hand; the card's *Verify by* |
| `about` | the *about to do* rows: a list of `{do, wrong_when}` |
| `rests_on`, `strength` | what the claim rests on, and (optional) how well that is established |
| `our_evidence` | what we demonstrated, in a few words |
| `boundary` | the card's *Not when*, **only** when *When it does NOT apply* is prose; otherwise the build takes the bold lead-in of each of its bullets, and having both is refused |
| `retired_because`, `superseded_by` | on a retired note only: the evidence that removed it, and the note that replaced it |

A shipped note (in `active/` or `review/`) with no phase or no `about` row is refused by the build: a note no task leads to is never read.

## The lifecycle of a note

**Knowledge here is a set of claims under test, not a collection.** Every note is kept only while the evidence allows it, and the base is bounded so that keeping what was learned never turns into keeping everything.

**The folder is the state.** A note lives in exactly one of three folders under `notes/`, and nothing else records its state:

| Folder | State | Ships | An agent |
|---|---|---|---|
| `notes/active/` | admitted, and its evidence holds | yes, in every table it belongs to | uses it |
| `notes/review/` | contradicted, or its `confidence` or its admission disputed; a verdict is pending | yes, marked **⚠ review** | may use it, and must say in its report that the note is under review |
| `notes/retired/` | withdrawn or superseded | **never** — kept here only | does not act on it; recognised here when the idea comes back |

A note moves between folders only with `release.py note-state SLUG active|review|retired`, which moves the file, rewrites every link to it in `sources/` and `meta/`, and builds.

### 1. Admission — before a note is written

A candidate becomes a note only when all five hold. Until then it is a row of the queue, [`../meta/tracking/candidates.md`](../meta/tracking/candidates.md). An admitted note is written into `notes/active/`.

1. **It changes a decision.** An agent would get this wrong without it.
2. **It passes the generality test.** Stated without a single project noun, it still says something.
3. **The literature was consulted first.** Search for what is already established — peer-reviewed work, standards (RFCs, NIST), canonical practitioner sources — before writing. Three outcomes, all acceptable, each recorded under *Literature*: the claim is established (cite it, and say what we take and where we go further); it is contradicted (the candidate dies, or its boundary moves); nothing is found (say "none known" — never imply support you do not have). **Cite only what was checked against the source**; a citation from memory is marked as such until verified.
4. **It has an occurrence.** A measurement, an incident, or a design decision it changed — named in *Where it came from*. A note with no occurrence is an opinion, and opinions are obeyed anyway, which is worse than being argued with.
5. **It is not already here.** Check every note in the same topic and the neighbouring ones. A new occurrence, number or boundary of an existing claim **extends that note**; it does not become a second one.

**The queue is bounded by time.** `release.py intake` enters each new candidate with *Since*, the release it arrived at; a row offered again for a known slug lands in the queue's *Offered again, to merge* table, and the release adds it to its row or note as another occurrence; a row a harvest refused (`refused: <reason>` in *Lacks*) goes straight to the history. A candidate that waited three releases without gaining what it lacks is discarded by `release.py triage --apply-discards` into [`../meta/tracking/history.md`](../meta/tracking/history.md), which also records where every other candidate went, so an answered idea is not offered again as fresh.

### 2. Evidence — kept separate from the claim

`confidence` records **our** evidence and only ours. It moves in both directions: a note gains `measured` when a number produced in a repository is written into it, and loses it when that number is shown to be wrong. New evidence goes into *Evidence* with its date. Each note's *Evidence* ends with the experiment that would settle it; those experiments are queued in [`../meta/tracking/experiments.md`](../meta/tracking/experiments.md), which `knowledge/OPEN.md` shows every carrier, so that the cheap ones actually get run.

### 3. Review and falsification — evidence against a note is acted on

**A note contradicted by a measurement, a test or an incident is not worked around.**

**Entering review.** A note goes to `notes/review/` when evidence contradicts it, when its *Evidence* does not earn its `confidence`, or when it is found to fail an admission step. Its *Evidence* section then opens with one line — `⚠ **Under review since <date>:** <reason>` — that says why, and which verdict it awaits. The build marks it **⚠ review** in every table; it stays reachable, because a disputed note is still more than nothing.

**Leaving review** takes one of these verdicts, in order of preference, recorded with the release that reaches it:

- **The boundary moves.** Most contradictions show where the heuristic stops being true — *When it does NOT apply* gains a bullet, with the evidence. The note returns to `notes/active/`.
- **The claim or its `confidence` is revised** — reworded, or downgraded to what its evidence earns — with the evidence added to *Evidence* and dated. The note returns to `notes/active/`.
- **The missing piece is supplied** — the literature search, the experiment — and the note, having passed, returns to `notes/active/`.
- **The note is retired**: withdrawn, or superseded by a better-stated one.

In every case the review line is removed on the way out.

**Retirement.** The note moves to `notes/retired/`, and its frontmatter gains `retired_because:` (one sentence: the evidence that removed it) and, when another note replaced it, `superseded_by: <slug>`. [`../meta/tracking/retired.md`](../meta/tracking/retired.md) gains one line, pointing at the file. A retired note is **kept, not deleted**, so that it does not come back next year as somebody's fresh idea; it never ships, so no carrier pays for it.

### 4. Keeping it usable — a review with verdicts, not a cap

**Knowledge is not lost to make room.** A note that passed admission stays until evidence or a better-stated note removes it, and every removal is a recorded verdict. **There is no cap on the number of notes:** a fixed count checks nothing about the notes, and whoever meets it has to choose which true, measured learning to leave out for a reason unrelated to any of them. A learning dropped to stay under a number is relearned later at full price, and the second time it usually arrives as an incident.

What is bounded is **attention**, and each bound is one a check can see:

- **Every shipped note is reachable**: under its topic, in at least one phase, in at least one *about to do* row. The build refuses it otherwise.
- **Every index stays readable in one pass.** When one grows past that — a rough sign is a topic table longer than a screen — split it by area: a new template in `templates/areas/`, routed from `templates/INDEX.md`. Splitting is cheap and loses nothing; refusing a note is neither.
- **A topic is a decision, not a label.** Prefer fitting a note into an existing topic; create one only when a set of notes shares a mechanism the others do not.
- **A review closes every release**, and it ends in verdicts, not in a count. For every pair of notes whose claims overlap: *merge* (one claim, a sharper boundary), *supersede* (one replaces the other), or *keep both*, with the mechanism that separates them — and evidence counted in two notes is moved to one. For every note whose *Evidence* names an experiment never run: *queued*, or *downgraded*. For every note an occurrence contradicted: *boundary moved*, *revised*, *sent to review* or *retired*. For every note whose `confidence` its *Evidence* does not earn: *downgraded*, or *sent to review*. For every note in `notes/review/`: a verdict from §3, or *kept in review* with what it still awaits. The verdicts are recorded with the release, so the next one starts from them.
- **A review never prunes what its own release admitted.** A note that arrived in this release can only be *kept* or *queued* by the review that closes it; merging, superseding or retiring it waits for a later release with its own reasoning. The moment a learning arrives is the moment it is understood least, and the worst one to judge another redundant.

### 5. The index is the contract

Every table a carrier reads is generated from the notes' own fields, so an index cannot list a note that does not exist, miss one that ships, or disagree with its claim. **Checked, not remembered**: `release.py build --check` (in `release.py check`) fails on generated output that is not what these sources produce, and `bundle.py verify` fails on a dead link or an unreachable note in the shipped copy.
