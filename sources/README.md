# Sources — the full notes and what the release is built from

`notes/<state>/<slug>.md` is the one place a note is written, in full: its frontmatter carries every field the indexes show, and its body all six sections. `templates/` holds the index prose, with a marker where each generated table goes. `meta/tools/release.py build` writes the short notes, the tables and `SHA256SUMS` into `.agents/`; nothing there is edited by hand. `references.md` and `layout.md` are the literature and the layout survey the bundle rests on.

## The lifecycle of a note

**Knowledge here is a set of claims under test, not a collection.** Every note is kept only while the evidence allows it, and the base is bounded so that keeping what was learned never turns into keeping everything.

**The folder is the state.** A note lives in exactly one of three folders under `notes/`, and nothing else records its state:

| Folder | State | Indexed | An agent |
|---|---|---|---|
| `notes/active/` | admitted, and its evidence holds | yes, in every table it belongs to | uses it |
| `notes/review/` | contradicted, or its `confidence` or its admission disputed; a verdict is pending | yes, marked **⚠ review** | may use it, and must say in its report that the note is under review |
| `notes/retired/` | withdrawn or superseded | no — kept, never listed in the phase or *about to do* tables | does not act on it; recognises it when the idea comes back |

A note moves between folders with `bundle.py note-state SLUG active|review|retired`, which moves the file and rewrites every relative link to it inside the bundle. Moving it by hand leaves dead links, and the audit fails on them.

### 1. Admission — before a note is written

A candidate becomes a note only when all five hold. Until then it is a line in `../tracking/candidates.md`. An admitted note is written into `notes/active/`.

1. **It changes a decision.** An agent would get this wrong without it (the two questions above).
2. **It passes the generality test.** Stated without a single project noun, it still says something.
3. **The literature was consulted first.** Search for what is already established — peer-reviewed work, standards (RFCs, NIST), canonical practitioner sources — before writing. Three outcomes, all acceptable, each recorded under *Literature*: the claim is established (cite it, and say what we take and where we go further); it is contradicted (the candidate dies, or its boundary moves); nothing is found (say "none known" — never imply support you do not have). **Cite only what was checked against the source**; a citation from memory is marked as such until verified.
4. **It has an occurrence.** A measurement, an incident, or a design decision it changed — named in *Where it came from*. A note with no occurrence is an opinion, and opinions are obeyed anyway, which is worse than being argued with.
5. **It is not already here.** Check every note in the same topic and the neighbouring ones. A new occurrence, number or boundary of an existing claim **extends that note**; it does not become a second one.

### 2. Evidence — kept separate from the claim

`confidence` records **our** evidence and only ours (see the table above). It moves in both directions: a note gains `measured` when a number produced in a repository is written into it, and loses it when that number is shown to be wrong. New evidence goes into *Evidence* with its date. Each note's *Evidence* ends with the experiment that would settle it; those experiments are queued in `../tracking/experiments.md` so that the cheap ones actually get run.

### 3. Review and falsification — evidence against a note is acted on

**A note contradicted by a measurement, a test or an incident is not worked around.**

**Entering review.** A note goes to `notes/review/` when evidence contradicts it, when its *Evidence* does not earn its `confidence`, or when it is found to fail an admission step. Its *Evidence* section then opens with one line — `⚠ **Under review since <date>:** <reason>` — that says why, and which verdict it awaits. Its index rows gain the **⚠ review** mark; nothing else about it changes, and it stays reachable, because a disputed note is still more than nothing.

**Leaving review** takes one of these verdicts, in order of preference, recorded in the changelog entry of the pass that reaches it:

- **The boundary moves.** Most contradictions show where the heuristic stops being true — *When it does NOT apply* gains a bullet, with the evidence. The note returns to `notes/active/`.
- **The claim or its `confidence` is revised** — reworded, or downgraded to what its evidence earns — with the evidence added to *Evidence* and dated. The note returns to `notes/active/`.
- **The missing piece is supplied** — the literature search, the experiment — and the note, having passed, returns to `notes/active/`.
- **The note is retired**: withdrawn, or superseded by a better-stated one.

In every case the review line is removed on the way out.

**Retirement.** The note moves to `notes/retired/`, and its frontmatter gains `retired_because:` (one sentence: the evidence that removed it) and, when another note replaced it, `superseded_by: <slug>`. It leaves every table in `INDEX.md` and its area index, and `../tracking/retired.md` gains one line — the chronological log of retirements — pointing at the file in `notes/retired/`. A retired note is **kept, not deleted**, so that it does not come back next year as somebody's fresh idea. What leaves is its place in the index, which is where attention is spent.

### 4. Keeping it usable — a review with verdicts, not a cap

**Knowledge is not lost to make room.** A note that passed admission stays until evidence or a better-stated note removes it, and every removal is a recorded verdict. **There is no cap on the number of notes:** a fixed count checks nothing about the notes, and whoever meets it has to choose which true, measured learning to leave out for a reason unrelated to any of them. A learning dropped to stay under a number is relearned later at full price, and the second time it usually arrives as an incident.

What is bounded is **attention**, and each bound is one a check can see:

- **Every note is reachable.** Every note in `notes/active/` and `notes/review/` is under its topic, in at least one phase, and in at least one *about to do* row — a note no task leads to is never read, however true. Checked by the audit.
- **Every index stays readable in one pass.** When one grows past that — a rough sign is a topic table longer than a screen — split it by area: `INDEX.md` stays the one entry point and routes to the area indexes. Splitting is cheap and loses nothing; refusing a note is neither.
- **A topic is a decision, not a label.** Prefer fitting a note into an existing topic; create one only when a set of notes shares a mechanism the others do not.
- **A review closes every harvest**, and it ends in verdicts, not in a count. This list is the one the other documents point to. For every pair of notes whose claims overlap: *merge* (one claim, a sharper boundary), *supersede* (one replaces the other), or *keep both*, with the mechanism that separates them — and evidence counted in two notes is moved to one. For every note whose *Evidence* names an experiment never run: *queued* in `../tracking/experiments.md`, or *downgraded*. For every note an occurrence contradicted: *boundary moved*, *revised*, *sent to review* or *retired*. For every note whose `confidence` its *Evidence* does not earn: *downgraded*, or *sent to review*. For every note in `notes/review/`: a verdict from §3, or *kept in review* with what it still awaits. The verdicts go in the changelog entry of the harvest, so the next one starts from them.
- **A review never prunes what its own harvest admitted.** A note that arrived in this harvest can only be *kept* or *queued* by the review that closes it; merging, superseding or retiring it waits for a later pass with its own reasoning. The moment a learning arrives is the moment it is understood least, and the worst one to judge another redundant.

### 5. The index is the contract

Every note in `notes/active/` and `notes/review/` is in the index — `INDEX.md`, or an area index it routes to — under its topic, at least one phase and at least one *about to do* row, and a note in `notes/review/` is marked **⚠ review** wherever it is listed. No note in `notes/retired/` is in those tables. Every indexed note exists, every relative link resolves, and every note carries its required fields and sections. **Checked by the audit (`bundle.py digest --check`), not remembered.**
