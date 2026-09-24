---
# bundle-header — provenance for this document. Identical across the bundle.
bundle:    agent-guides
lineage:   g-8b5800/main
ancestry:  [g-c7344c, g-099a8a, g-8b5800]
version:   15
component: roadmap
released:  2026-09-24
---

# Roadmap — how this bundle itself improves

**What is planned for the method and the knowledge base, and what each item will collide
with.** Not a promise: a ledger of accepted work on the bundle, in the same five states the
method uses for a repository's roadmap. Work on a *repository* goes in that repository's
roadmap; this file is only about `.agents/` itself.

Newest first within each state. Each item names its **collision** — what it will touch that
something else depends on — because that is what decides its order.

| State | Means |
|---|---|
| **Next** | accepted, and nothing blocks it |
| **Later** | accepted, waiting on something named |
| **Blocked outside** | depends on a decision or a party outside the bundle |
| **Closed by measurement** | was proposed, and a number said no — kept so it is not proposed again |
| **Done** | shipped in a named version; kept one release, then removed |

## Next

- **`i-5ed7e8-0d9b6a` · Measure whether the bundle changes what an agent does, and whether its
  content is the cause.** Controlled studies of repository context files found no reliable gain in
  task success and a cost increase of about a fifth; the bundle has never been measured against that.
  The pre-registered experiment is in the home repository's `evals/` (it does not travel): judgment,
  boundary and neutral tasks graded by hidden tests; the bundle against the same bundle with the
  relevant notes removed, against no bundle, and against the note certainly in context or an
  irrelevant note of matched length. State: five exploratory pilots run (the home repository's
  `evals/REPORT.md`); the cost overhead is established, a content effect is seen on few tasks and
  is not significant, and the confirmatory run waits on new tasks by another author, ablation by
  principle rather than by note, and boundary tasks at distance. *Collides with:*
  every packaging change to the method, since a null that comes from routing rather than from content
  changes what the packaging should be; and the notes' `confidence`.
- **`i-5ed7e8-8236cb` · Make `AGENTS.md` the root artifact of the method.** The artifact list in
  `method/prompt-context.md` names a root `CLAUDE.md` as the source, puts the per-change log under
  `.claude/logs/` and skills under `.claude/skills/`, while `layout.md`, *Three agents, one source*,
  and this repository treat `AGENTS.md` as the source and the logs as assistant-neutral documents.
  Found by the external audit of 2026-09-24. *Collides with:* artifacts 1, 3 and 5, the bootstrap's
  checklists, and every carrier's `Reads:` lists that name those headings.
- **`i-5ed7e8-c5f622` · Check what arrives through `incoming/` for invisible text and executable
  configuration.** The bundle is spread by agent-run merges, and the privacy check looks only at what
  leaves. Invisible and direction-changing Unicode in instruction files is a published attack on coding
  agents, and a copied settings or hook file would run in the receiving repository. A check in
  `bundle.py` (`digest --check` and `gather`) that refuses both. *Collides with:* `prompt-update.md`,
  `prompt-merge.md` and `prompt-sync.md`, which would call it.
- **`i-5ed7e8-08c9f7` · Update `layout.md` for the shared `.agents/` namespace and the assistants it
  omits.** At least one assistant now scans `.agents/skills/` in every directory, and a dependency
  tool uses `.agents/` with a manifest and a lockfile; `layout.md` compares three drafts and misses
  both. The capability table covers three assistants of the six or more that read `AGENTS.md`, and
  spec-driven workflows, MCP-served knowledge and plugin packaging are neither adopted nor declined in
  writing. *Collides with:* `layout.md` (a release) and `prompt-context.md`, *Three agents, one source*.
- **`i-5ed7e8-d4f710` · Review overlapping notes as principles.** The efficacy pilots found that
  removing one note did not remove its principle: agents used `merge-by-shared-fact-not-shared-shape`
  in place of `derived-over-chosen-identifiers`, and `order-writes-by-failure-residue` in place of
  `retry-over-irreversible-effect`. The knowledge base's own review rule asks for a verdict on every
  overlapping pair (merge, supersede, or keep both with the mechanism that separates them). *Collides
  with:* the index and area tables, and the experiment's ablation, which should remove a principle,
  not a file.
- **`i-5ed7e8-3fa5c5` · A release cadence, and a candidate queue that drains.** The method moved through
  about two dozen versions in one week, each needing a meta-session, and one carrier already trails;
  the candidate queue holds about seventy-five rows and the last release admitted none. Batch
  releases on a cadence, and apply the three-harvest discard rule. *Collides with:* `prompt-sync.md`
  §*The cycle*.
- **`i-5ed7e8-1e9567` · Resolve the persistent privacy warnings.** Seventeen warnings print on every
  run and none changes; a warning that is always there stops being read. Reword each line or, where
  the user explicitly decides it may stay, mark it with a reason. *Collides with:* nothing but the
  warned lines.
- **`i-5ed7e8-973bd7` · Run the cheapest queued experiments** in `tracking/experiments.md`, one
  per note that has none. *Collides with:* the notes' `confidence`, which moves in both directions.
- **`i-5ed7e8-705aa8` · Clean up the duplicated prose that remains in the method.** The worked
  examples are still long, and a few rules are still restated in more than one prompt. *Collides
  with:* the `Reads:` lists, which name exact headings.
- **`i-5ed7e8-13a8be` · Keep the private-terms list of each machine complete.** `bundle.py
  privacy` checks the names in `~/.config/agent-guides/private-terms.txt`, which never travels; a
  private name missing from it is caught only by the generic rules. Each machine's owner adds the
  names of private repositories, organisations, products and people. *Collides with:* nothing in
  the bundle; it is the one list that must never enter it.

## Later

- **`i-5ed7e8-8623a8` · Package the method's invocations as Agent Skills.** The session loop and the
  six procedures are paste-in blocks; the open skill format is read by most assistants, from their
  descriptions, without a paste. The efficacy pilots found routing weaker for a smaller model (the
  index opened in about two thirds of trials, the note in about two fifths). *Waits on:* the
  confirmatory run of `i-5ed7e8-0d9b6a`, which says whether routing or content is the limit.
  *Collides with:* `i-5ed7e8-08c9f7` (where skills live) and every `Reads:` list.
- **`i-5ed7e8-a89859` · A short summary per note, with the full note on demand.** Carrying the bundle cost
  about 2.1 to 2.3 times as much per task for the frontier model in every pilot, and in one
  discriminating trial the one-line claim in an area index was enough. A summary (claim, boundary, check)
  in the always-consulted path and the evidence on demand might keep the benefit at a fraction of the
  cost. *Waits on:* `i-5ed7e8-0d9b6a`, to measure the summary against the note. *Collides with:* the
  note shape in `knowledge/README.md` and the digest recipe.
- **`i-5ed7e8-f71f36` · Simplify versioning toward tags and a lockfile.** Three lineages, each with an
  ancestry, a fork point and a digest, carry what version tags and one hashed lockfile per carrier
  would, while `adapted` and `declined` carry what nothing else does. *Waits on:* `i-5ed7e8-3fa5c5`
  and every carrier aligned. *Collides with:* `bundle.py` (stamp, gather, align), every header, and
  *Keeping the set versioned* in `prompt-context.md`.
- **`i-5ed7e8-aca224` · A host-side record-id and renumbering check in every carrier's audit.**
  `bundle.py ids` checks record ids for format, prefix and duplicates; each carrier's audit should
  call it over its own records, and check that principles, artifacts and phases are never
  renumbered. *Waits on:* one carrier adopting it first.

## Blocked outside

- **`i-5ed7e8-b83f16` · Offer the current release to the carriers not reached.** They are listed
  in `tracking/carriers.md` without ids, plus `r-a2f271`, registered at v20. Each receives it
  through its `incoming/` or the next meta-session that has it open, mints its own random id if it
  has none, and keeps its repository fields. *Blocked on:* a session with those repositories open.

## Closed by measurement

None yet.

## Done

Only the last release is kept here; every earlier one is a row of `method/changelog.md`.

- **Bundle v21 (method v24, knowledge v11), 2026-09-24: the `g-c7344c` carriers are reached.**
  Four carriers that had stayed on that line since it merged into this one were brought onto this
  line in one meta-session. Their bodies had nothing this line lacked — the merge and the privacy
  scrub had already taken it — so the release changes `tracking/` only: their harvests of
  2026-09-22 became candidate rows, generalised first (eleven candidates and eight extensions
  offered to existing notes), two experiment runs, and two refusals in `tracking/history.md`.
  `gate-sequence-stops-at-the-first-red-step` arrived with one occurrence in each of the four.
  Nothing was admitted: admission waits for a release that runs it. The four carriers minted
  random ids and are registered; their audits now read the three note states and call
  `bundle.py privacy` and `ids`. Method and knowledge are unchanged, so their digests are too.
