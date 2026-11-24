# Spec-driven development: what the tools store, and which formats serve three goals

Research, 2026-11-24, asked by the owner. Read-only: nothing here changes the bundle. The question was how to
define a spec that (G1) stores what a tool needs, (G2) keeps everything relevant from the process that should
not be lost, and (G3) explains the project to another person simply. Two delegated surveys were run, then their
central claims were checked against the primary pages, listed at the end. A claim not checked that way is marked
**ASSUMPTION**.

## The answer in one paragraph

No single established format covers all three goals. Requirement notations (EARS, Given-When-Then) serve G1 and
say nothing of why; decision records (Nygard ADRs, MADR) and proposal documents (Python PEPs, Rust RFCs) serve G2,
and are the only formats with a named place for rejected alternatives and open questions; documentation frameworks
(Diátaxis, README-first) serve G3. The agent-era tools (Spec Kit, Kiro, OpenSpec) all converge on the same chain:
*requirements → design or plan → tasks*, plus a durable context layer, and **none of them has a dedicated place
for rejected alternatives** — the part G2 needs most. The one published practitioner test found the specs verbose,
tedious to review and not always followed. So the design question is less "which format" than "which small set of
typed parts, and which mechanism keeps them true".

## 1. The three levels of spec-driven development

Birgitta Böckeler (Thoughtworks), on martinfowler.com, 2025-10-15, separates three levels:

- **spec-first**: "A well thought-out spec is written first, and then used in the AI-assisted development workflow
  for the task at hand." The spec may be discarded afterwards.
- **spec-anchored**: "The spec is kept even after the task is complete, to continue using it for evolution and
  maintenance of the respective feature."
- **spec-as-source**: "the spec is the main source file over time, and only the spec is edited by the human".

The level decides most of the cost. G2 and G3 both require at least *spec-anchored*: a spec that is thrown away
keeps nothing and explains nothing a month later.

## 2. What the tools store

| Tool | Artefacts | Level | Where the reasons live | Verified |
|---|---|---|---|---|
| GitHub Spec Kit | `memory/constitution.md` (principles); per feature `specs/<branch>/`: `spec.md`, `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`, `tasks.md`; ambiguities marked `[NEEDS CLARIFICATION: question]`, and the checklist requires none to remain | aims at spec-anchored ("maintaining software means evolving specifications"), with code as "continuously regenerated output"; whether a feature's folder is kept after it ships is not stated | `plan.md` and `research.md` | `spec-driven.md` read |
| AWS Kiro | per spec `requirements.md` (EARS), `design.md`, `tasks.md`; steering files (`product.md`, `tech.md`, `structure.md`) | mostly spec-first (Böckeler) | `design.md`, steering; no field for discarded options | ASSUMPTION (docs summarised, not read whole) |
| OpenSpec | `openspec/specs/` = current behaviour; `openspec/changes/<name>/` = `proposal.md`, delta `specs/` (`## ADDED Requirements`), `design.md`, `tasks.md`; requirements as `### Requirement:` with `#### Scenario:` WHEN/THEN; an archive step moves a change to `changes/archive/<date>-<name>/` and updates `specs/` | spec-anchored, the only tool whose own step keeps the truth current | `proposal.md` and `design.md`, kept in the dated archive | README read; MODIFIED/REMOVED deltas not on the page |
| Tessl | `.spec.md` per file, `@generate` / `@describe`; a registry of library usage specs | exploring spec-as-source | not found | ASSUMPTION |
| BMAD-METHOD | role agents (product, architecture, UX, dev, test) | — | — | README only; artefact list ASSUMPTION |

Cross-cutting: plain Markdown in git; a human approval between steps; a durable context file beside the
per-change specs (constitution, steering, `AGENTS.md`). **Onboarding a person is a stated goal of none of them**;
it arrives, if at all, as a side effect of specs that were kept.

## 3. The established formats, by goal

| Format | Serves | Its parts (from the source) |
|---|---|---|
| **EARS** (Mavin et al., Rolls-Royce, published 2009) | G1 | five patterns: ubiquitous "The <system> shall <response>"; state "While <precondition>, …"; event "When <trigger>, …"; optional "Where <feature is included>, …"; unwanted "If <trigger>, then …"; and combinations |
| **Given-When-Then** (Gherkin) | G1, executable | Feature, Scenario, Given/When/Then — ASSUMPTION, not re-read |
| **Nygard ADR** (2011) | G2 | Title, Context, Decision, Status, Consequences; "If a decision is reversed, we will keep the old one around, but mark it as superseded"; numbers "will not be reused" |
| **MADR**, major version 4 (released 2024-09-17) | G2 | Context and Problem Statement (required); Decision Drivers; Considered Options; Decision Outcome, with Consequences and Confirmation; Pros and Cons of the Options; More Information |
| **PEP 1** | G2 + G3 | its list of parts includes Rationale (item 5), Rejected Ideas (item 10) and Open Issues (item 11) |
| **Rust RFC template** | G1 + G2 + G3 | Summary; Motivation; Guide-level explanation; Reference-level explanation; Drawbacks; Rationale and alternatives; Prior art; Unresolved questions; Future possibilities |
| **Diátaxis** | G3 | tutorials, how-to guides, reference, explanation, separated by two questions: "action or cognition? acquisition or application?" |
| **README-driven development** (Preston-Werner, 2010) | G3 | "Write your Readme first." |
| **llms.txt** (v2) | G3 for agents | an H1 with the name ("the only required section"), a blockquote summary, free sections, then H2 lists of links; an `Optional` H2 for what an agent may skip |

The Rust RFC template is the closest existing single document to all three goals: *Guide-level explanation* is
G3 written for a newcomer, *Reference-level explanation* is G1, and *Rationale and alternatives* plus *Unresolved
questions* are G2. Its known cost is that an RFC is written once and rarely updated (ASSUMPTION, practitioner
consensus, not measured).

## 4. The evidence against, and its size

- **Böckeler's test of Spec Kit and Kiro**: the files "were repetitive, both with each other, and with the code
  that already existed"; a small bug became "4 'user stories' with a total of 16 acceptance criteria"; "I'd rather
  review code than all these markdown files"; "I frequently saw the agent ultimately not follow all the
  instructions"; and spec-as-source may combine "the downsides of both MDD and LLMs: Inflexibility and
  non-determinism".
- **Thoughtworks Technology Radar**, Spec Kit, *Assess*, 2026-04-15: "overly verbose markdown outputs that
  increased cognitive load", instruction bloat and context rot as instructions grow.
- **Measured effect: thin.** An arXiv overview (2602.00180) cites "up to 50%" fewer errors from refined specs, and
  calls the underlying studies nascent (ASSUMPTION: read through a summary). A 2026 ESEM paper titled
  *Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects* was seen by title only; its
  PDF returned 404 on the check, so its sample and effect are **unknown** and it must not be cited for a number.
- No study was found on whether kept specs help a new contributor understand a project (G3), nor on review burden.

## 5. Three shapes for the owner's spec, priced

| Shape | Example | Gains | Costs |
|---|---|---|---|
| **A. One file, RFC-shaped** | `spec.md`: Summary · How to understand it (guide-level) · Requirements (EARS, with ids) · Decisions, with the options rejected · Open questions · Evidence | one place to read, for a person and an agent; G3 first | grows; G2 history is lost to edits unless decisions are append-only |
| **B. Thin spec plus a decision log** (middle) | `spec.md` holds the summary, the guide and the EARS requirements with ids; `decisions.md` is append-only (Status, supersession, Considered Options); each requirement links the decision that set it | G2 never rewritten; G1 stays short; matches OpenSpec's truth/changes split | two files can disagree; needs a check that every requirement links a decision and every link resolves |
| **C. A folder of typed parts** | `spec/requirements/`, `spec/decisions/` (MADR), `spec/explain/` (Diátaxis explanation and a context diagram), an index | each goal updated on its own; scales to a large project | most files, most links, and the most verbose — the failure the practitioner test reports |

**Recommendation: B.** It is the only shape where what is lost in the other two — rejected options and the reason
a requirement exists — has a place that is never edited, and it keeps the part a newcomer reads short. It is
also what this bundle already half does: carriers keep an append-only decisions log with a Status column and
supersession, and `bundle.py decisions` checks it. What B adds is the requirement ids in EARS form, a
guide-level section written for someone new, and the link from each requirement to its decision.

Whatever the shape, the sources agree on two mechanisms more than on any format: **an explicit marker for what is
not yet known** (Spec Kit's `[NEEDS CLARIFICATION]`, PEP *Open Issues*, RFC *Unresolved questions*) that a check
refuses to ship with; and **a step that moves a change into the kept truth** (OpenSpec's archive), without which a
spec drifts.

## Open questions

1. What the ESEM 2026 paper measured, from a URL that resolves.
2. Kiro's, Tessl's and BMAD's artefacts, read whole.
3. Whether any study measures a kept spec's effect on a newcomer's understanding (G3).
4. For this bundle: whether shape B becomes a method artefact (a template and a check) — a design decision for the
   owner, not taken here.

## Sources checked

- https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- GitHub Spec Kit repository, file `spec-driven.md` on its main branch
- OpenSpec repository (Fission-AI), its README on the main branch
- https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit
- https://alistairmavin.com/ears/
- https://adr.github.io/madr/
- https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- https://peps.python.org/pep-0001/
- Rust RFCs repository, file `0000-template.md`
- https://diataxis.fr/ and https://diataxis.fr/compass/
- https://tom.preston-werner.com/2010/08/23/readme-driven-development.html
- https://llmstxt.org/

Not checked (summary or search only): https://kiro.dev/docs/specs/, https://tessl.io/blog/tessl-launches-spec-driven-framework-and-registry/,
the BMAD-METHOD repository README, https://arxiv.org/html/2602.00180v1, the ESEM 2026 PDF (404).
