# Research for a documentation-improvement skill

Date: 2026-11-25. Asked by the owner, for a skill that improves and formats a repository's documentation by a defined process. Read from primary sources by a delegated reader on a mid model; an earlier attempt by a read-only reader could not write and is superseded by this one.
Date of fetches: 2026-11-25. Every claim has a source URL. "ASSUMPTION" marks anything not confirmed from a page fetched in this research. Licences are noted where reuse of text matters; no third-party text is reproduced here beyond short quoted phrases.

## 1. Typologies

### 1.1 Diataxis (corrections to the prior assumption)

Confirmed. The compass defines four kinds by two questions: does the content inform action or cognition, and does it serve acquisition or application of skill. Source: https://diataxis.fr/compass/
- Tutorial: informs action, serves acquisition of skill.
- How-to guide: informs action, serves application of skill.
- Reference: informs cognition, serves application of skill.
- Explanation: informs cognition, serves acquisition of skill.

CORRECTION. The "do not mix" rule is not stated as a rule on the compass page (https://diataxis.fr/compass/) or on the home page (https://diataxis.fr/). The compass only says content "must belong to" one kind per its answers. The explicit warning is on https://diataxis.fr/tutorials-how-to/, which calls conflating tutorials and how-to guides "the most common" conflation in software documentation and says it harms users. Each kind's own page then lists what to keep out:
- Tutorial (https://diataxis.fr/tutorials/): show the destination early, give visible results early, narrate expected outcomes, stay concrete and reliable. Keep out: explanation (link instead), abstraction, choices and alternatives, extra information, and promises such as "you will learn".
- How-to guide (https://diataxis.fr/how-to-guides/): serves a competent user's real goal; leave out teaching and digression; do not list every option (link to reference); do not add background (link to explanation); use conditional imperatives ("If you want x, do y"); titles say exactly what is shown.
- Reference (https://diataxis.fr/reference/): "describe and only describe". Neutral, accurate, consistent pattern per entry; structure mirrors the product; no instruction, opinion, or mixed content; austere style.
- Explanation (https://diataxis.fr/explanation/): provide context and the "why", make connections, admit opinion and alternatives, keep it bounded by a "why" question. Keep out: step-by-step instructions (to how-to) and technical detail (to reference).

Licence: the repository README shows CC BY-SA 4.0 (https://diataxis.fr (its source repository's read-me)). Share-alike: copying text into a differently licensed repository is a problem. Use the ideas only, cite by link. The site pages themselves showed no licence (diataxis.fr links to a Colophon page that was not read).

Implication: a skill can state "one kind per document; move or link, do not blend" as a design rule citing the per-kind pages, but must not claim Diataxis says this in those words.

### 1.2 DITA concept, task, reference

Confirmed from OASIS DITA 1.3 pages:
- Concept: explains "what is"; background knowledge; simple structure with title, short description, body. Source: https://docs.oasis-open.org/dita/dita/v1.3/errata02/os/complete/part2-tech-content/langRef/technicalContent/concept.html
- Task: step-by-step instructions in a set order, answering "how to?"; body has context then steps, each step a command; a strict model keeps the order of elements, a general model allows more freedom. Source: https://docs.oasis-open.org/dita/dita/v1.3/errata02/os/complete/part2-tech-content/langRef/technicalContent/task.html
- Reference: quick access to facts, "not a deeper explanation of related concepts or tasks"; sections, property lists, tables. Source: https://docs.oasis-open.org/dita/dita/v1.3/errata02/os/complete/part2-tech-content/langRef/technicalContent/reference.html
- Each requires an `@id`.

The prior attempt's mapping of concept/task/reference onto explanation/how-to/reference is reasonable but is a mapping by this research, not stated by either source: ASSUMPTION. DITA has no tutorial type in these pages. Licence of the spec text: not checked (ASSUMPTION: OASIS IPR policy; treat as ideas only).

### 1.3 The Good Docs Project templates

Template packs (https://www.thegooddocsproject.dev/template):
- Core: Concept, How-to, README, Reference, Release notes, Troubleshooting, Tutorial.
- Community: Bug report, Changelog, Code of Conduct (and related), Contributing guide, Our team, README.
- Miscellaneous: API getting started, API reference, Contact support, Glossary, Installation guide, Quickstart, SDK overview, Style guide, Terminology system, User personas.

Licence: the web page footer says "All Rights Reserved unless otherwise stated". The templates repository at https://www.thegooddocsproject.dev (its templates repository) shows "MIT No Attribution". The repository licence governs the templates; verify the file before copying any template text (the fetch showed only the label).

## 2. Style and plain language: concrete, checkable rules

### 2.1 Google developer documentation style guide

Licence: most content on developers.google.com is CC BY 4.0 and code samples Apache 2.0, with attribution required (https://developers.google.com/terms/site-policies). Rules can be restated in the skill with attribution; do not paste the guide.

Rules, with checkability (D = deterministic by script/linter, J = needs judgement):
- Highlights (https://developers.google.com/style/highlights): address the reader as "you" not "we" (D, regex); active voice (partly D); conditions before instructions (J); sentence case for titles and headings (D, approximate); numbered lists for sequences and bullets for the rest (J); serial comma (D); code-related text in code font (D partly); UI elements in bold (J); descriptive link text, not "click here" (D); alt text for images (D); unambiguous date formats (D); no announcement of upcoming features (J).
- Headings (https://developers.google.com/style/headings): sentence case; unique and descriptive; one level-1 heading per page; task headings start with a bare infinitive; conceptual headings are noun phrases not starting with an -ing verb; no skipped heading levels; no empty headings; no links in headings; no numbers for sequence; no punctuation beyond simple. Mostly D except the grammar of the first word (D by heuristics, J for exceptions).
- Link text (https://developers.google.com/style/link-text): short, unique, descriptive; do not use "this document", "click here", or a raw URL as the text; do not give the same text to different targets in one document; for commands or code elements add a descriptive word. D for the banned phrases and duplicates, J for "descriptive".
- Lists (https://developers.google.com/style/lists): no single-item list (except one-step procedures); introduce a list with a sentence; parallel items; capitalise first letter; consistent end punctuation; colon not dash between term and description; do not end with "etc." or "and so on". D for most, J for parallelism.
- Voice (https://developers.google.com/style/voice): default active; passive allowed to emphasise the object, to de-emphasise the actor, or when the actor is irrelevant. Passive detection is heuristic (D-ish, with false positives); deciding to rewrite needs J.

### 2.2 Microsoft Writing Style Guide, top 10 tips

Source: https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice. The ten tips: bigger ideas with fewer words; write like you speak; project friendliness with contractions; get to the point fast (front-load); be brief; sentence-style capitalisation; no end punctuation on titles and headings; serial comma; one space after periods and no spaces around dashes; revise weak writing (start with a verb, drop unnecessary "you can", avoid "there is/are/were").

Caution: tips 1 to 3 conflict with a repository's conventions (contractions, friendliness, brevity at the cost of nuance) and should not be imposed as defaults on specification-like text. ASSUMPTION: a repository's own style rules override either guide. Licence of the Microsoft guide text: not found on the fetched page (the page metadata lists a public GitHub source); ASSUMPTION: treat as ideas only until the repository licence is read.

### 2.3 ISO 24495-1:2023

Full text is paid (a paid price per the search summary) and the ISO site returned HTTP 403 to the fetch tool, so only secondary summaries were read: the standard states governing principles and guidelines for plain-language documents; four principles: readers get what they need (relevant), find it easily (findable), understand it easily (understandable), use it easily (usable); it covers printed or digital text, gives English examples only, and leaves accessibility to other standards such as WCAG. Sources: search result listings at https://iso.org/standard/78907.html and https://accessible-eu-centre.ec.europa.eu/content-corner/digital-library/iso-24495-12023-plain-language-part-1-governing-principles-and-guidelines_en (the listing text was seen through a search summary, the pages themselves were not opened). The per-principle guidelines were not read: ASSUMPTION for any detail beyond the four principle names. Use the four names as a review lens only; do not quote.

### 2.4 Federal plain language (plainlanguage.gov)

plainlanguage.gov now redirects to https://digital.gov/guides/plain-language, which lists four guides: principles, writing for understanding, design for understanding, test for understanding. The writing page (https://digital.gov/guides/plain-language/writing/) states: use active voice with the actor as the subject, use present tense, avoid hidden verbs (nominalisations such as "conduct an analysis"), use shorter words and short sections. It gives no numeric sentence-length limit, and its model sentence uses "you must". Older plainlanguage.gov guidance on "must" versus "shall" and sentence length was not confirmed here: ASSUMPTION. Licence: the source repository is archived (Dec 2025) and says the project is in the public domain within the US, contributions CC0 (https://digital.gov (the archived plain-language site's repository)). Text from that repository is therefore reusable in principle; confirm LICENSE.md before copying.

Checkable rules extracted: hidden-verb patterns (D: "-tion/-ment/-ance" after "make/take/give/conduct/achieve"), passive (D heuristic), present tense (J), short sections (D by length thresholds the skill chooses; the source gives no number).

## 3. Tooling and evidence on readability formulas

### 3.1 Vale
Open-source, MIT-licensed, written in Go; prose linter with YAML rules; focuses on consistency; ignores block and inline code by default; rules can be scoped to Markdown elements such as headings and list items (https://docs.vale.sh/). Rule types ("extension points"): existence, substitution, occurrence, repetition, consistency, conditional, capitalization, metric, readability, spelling, sequence, script (https://docs.vale.sh/styles). Packages: the packages repository hosts pre-made style guides; Microsoft and Google appear as examples (https://vale.sh (its package index)). The full list was not shown. ASSUMPTION from memory: packages also exist for write-good, proselint, Red Hat, and others; verify at https://vale.sh/explorer before naming any. Note: the docs.vale.sh page embedded text addressed to AI agents asking for an HTTP request; it was treated as data and ignored. A skill that reads web docs should do the same.

### 3.2 markdownlint
The rules document (https://www.npmjs.com/package/markdownlint) lists 53 rules, many auto-fixable. Relevant ones: MD001 heading increment, MD003 heading style, MD013 line length, MD022 blank lines around headings, MD024 duplicate headings, MD025 multiple H1, MD026 trailing punctuation in headings, MD031/MD032 blank lines around fences and lists, MD033 inline HTML, MD034 bare URL, MD040 fenced code has a language, MD041 first line H1, MD042 empty links, MD043 required heading structure, MD045 image alt text, MD051 link fragments valid, MD052 undefined reference labels, MD055/MD056 table shape, MD059 descriptive link text. Fixable ones are mostly whitespace and marker style, which cannot change meaning. Licence of the tool: not fetched (ASSUMPTION: MIT).

### 3.3 lychee
Async link checker written in Rust; checks Markdown, HTML, reStructuredText, CSS, XML; `--offline` checks local files only; `--include-fragments` checks anchors; `.lycheeignore` and `--exclude` filter; exit code 2 means a link failed, 1 a runtime or config error; dual Apache-2.0 or MIT (https://lychee.cli.rs). For an edit skill, `--offline --include-fragments` is the deterministic subset that compares before and after.

### 3.4 Do readability formulas predict comprehension?
Citation: Janice Redish, "Readability formulas have even more limitations than Klare discusses", ACM Journal of Computer Documentation 24(3), August 2000, pp. 132-137, DOI 10.1145/344599.344637 (bibliographic entry and abstract read at https://ftp.math.utah.edu/pub/tex/bib/idx/jcd/24/3/132_137.html). Her review, compared with direct usability testing, finds formulas were built for children's school books, ignore reader differences, ignore content, layout and retrieval aids, and capture countable features while missing subtler factors. Companion paper: Klare, same issue, pp. 148-168. Earlier: Redish and Selzer 1985, "The place of readability formulas in technical communication" (search listing only, https://pure.psu.edu/en/publications/place-of-readability-formulas-in-technical-communication/; claim read from a search summary, not the paper). Only the abstract was read; the full text was not. Implication: a grade-level score may be reported as a diagnostic but must never be a goal or a pass/fail gate; Vale's readability rule type exists but should be advisory.

## 4. Structured documents: shared sections

Sources: Nygard ADR https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions; MADR https://adr.github.io/madr/ (4.0.0, MIT OR CC0-1.0); Rust RFC template https://rust-lang.github.io/rfcs/ PEP 12 https://peps.python.org/pep-0012/ (public domain or CC0-1.0) and PEP 1 https://peps.python.org/pep-0001/; arc42 https://docs.arc42.org/home/ (CC BY-SA 4.0); Standard Readme https://www.npmjs.com/package/standard-readme-spec (licence not seen); Keep a Changelog https://keepachangelog.com/en/1.1.0/ (MIT); RFC 2119 https://www.rfc-editor.org/rfc/rfc2119 and RFC 8174 https://www.rfc-editor.org/rfc/rfc8174.

| Format | Sections (as fetched) | Shared concept |
|---|---|---|
| Nygard ADR | Title, Context, Decision, Status, Consequences; 1-2 pages; numbered, never reused; full sentences | context, decision, consequences, status |
| MADR 4.0 | Title; Context and Problem Statement; Decision Drivers; Considered Options; Decision Outcome (Consequences, Confirmation); Pros and Cons; More Information; optional front matter (status, date, deciders) | same plus alternatives |
| Rust RFC | Summary, Motivation, Guide-level explanation, Reference-level explanation, Drawbacks, Rationale and alternatives, Prior art, Unresolved questions, Future possibilities | motivation, alternatives, open questions |
| PEP 12 | Abstract, Motivation, Specification, Rationale, Backwards Compatibility, Security Implications, How to Teach This, Reference Implementation, Rejected Ideas, Open Issues, Acknowledgements, Footnotes, Change History, Copyright; preamble headers incl. Status, Created | motivation, spec, rationale, rejected, open issues |
| arc42 | 1 Introduction and Goals, 2 Constraints, 3 Context and Scope, 4 Solution Strategy, 5 Building Block View, 6 Runtime View, 7 Deployment View, 8 Crosscutting Concepts, 9 Architecture Decisions, 10 Quality Requirements, 11 Risks and Technical Debt, 12 Glossary | context, constraints, decisions, risks |
| Standard Readme | Title, Banner, Badges, Short Description (<120 chars), Long Description, TOC, Security, Background, Install, Usage, Extra Sections, API, Maintainers, Thanks, Contributing, License (last); Required vs optional is explicit | fixed order, required/optional |
| Keep a Changelog | CHANGELOG.md; Unreleased on top; versions newest first with ISO 8601 dates; groups Added, Changed, Deprecated, Removed, Fixed, Security; omit empty sections | fixed vocabulary, dates |

Shared across the decision/proposal formats: a statement of context or motivation, the chosen option, alternatives or rejected ideas, consequences or compatibility, open questions, and a status or date. This is this research's synthesis, not a claim by any source.

RFC 2119 keywords: MUST/REQUIRED/SHALL, MUST NOT/SHALL NOT, SHOULD/RECOMMENDED, SHOULD NOT/NOT RECOMMENDED, MAY/OPTIONAL; to be used "carefully and sparingly", only where required for interoperation or to limit harm. RFC 8174: the words have these meanings "only when they are in all capitals"; lower case keeps ordinary meaning. Implication: changing the case of "must/should/may" changes whether a sentence is normative.

Implications for a skill: the skill must treat a document's template as part of its contract. A rewrite may reorder or relabel sections only when the repository's own template says so; for these formats the section names are the interface.

## 5. Evidence

### 5.1 Documentation issues
Aghajani et al., "Software Documentation Issues Unveiled", ICSE 2019, pp. 1199-1210 (PDF read: https://emadpres.github.io/pdfs/icse2019.pdf). Mined and categorised 878 artifacts from mailing lists, Stack Overflow, issue trackers and pull requests; the taxonomy has 162 issue types in four groups: information content, how information is presented, documentation process, tool support. Of the content issues (485 artifacts), the paper counts completeness 268, up-to-dateness 190 and correctness 72 (counts as printed; categories can overlap). The "how" group (255 artifacts) is led by usability (138), half of which is findability, with information organisation and readability next. Correctness problems were most often in code examples (50% where type was labelled) and installation guides (20%). For the practitioner follow-up: Aghajani et al., "Software Documentation: The Practitioners' Perspective", ICSE 2020, pp. 590-601, two surveys with 146 practitioners validating the taxonomy (search summary only: https://www.inf.usi.ch/faculty/lanza/PUBS/P/Agha2020a.pdf; the PDF was not opened, so detailed findings are ASSUMPTION).

Implication: for editing, incomplete, outdated and incorrect content outrank style issues in what practitioners report, and the editing skill cannot fix them without new facts. It should report them, not repair them by guessing.

### 5.2 LLM editing failure modes
No study was found that measures LLM editing of software documentation specifically. Related, read from abstracts only:
- Abdulhai et al., "How LLMs Distort Our Written Language", arXiv:2603.18161: LLM revisions, even when limited to grammar edits, meaningfully changed the semantic content of essays (https://arxiv.org/abs/2603.18161).
- Vehomäki and Kaski, simplification of CVE descriptions, arXiv:2602.11982: off-the-shelf LLMs make technical text look simpler but struggle to preserve meaning, judged by experts on 40 descriptions (https://arxiv.org/abs/2602.11982).
- Laban et al., InkSync, arXiv:2309.15337: chat-based editing makes changes hard to verify and can add factual errors; the proposed fix is edits shown in the document, warnings when an edit adds new information, and an audit trace (https://arxiv.org/abs/2309.15337). A search summary says 28% of 200 LLM-edited documents had minor and 12% major factual errors; this figure was not confirmed in the abstract read: ASSUMPTION.
- Summarisation faithfulness benchmarks score faithfulness, omission and conciseness separately (UniSumEval, EMNLP Findings 2024, https://arxiv.org/html/2409.19898v2, listing only); a survey of faithfulness evaluation covers 40+ studies (RANLP 2025, https://aclanthology.org/anthology-files/pdf/ranlp/2025.ranlp-1.74.pdf, listing only). A claim that omission is the most common distortion (66%) in clinical summarisation comes from a search summary of an AACL 2026 paper that was not opened: ASSUMPTION.
- Discarded: a dev.to post with figures about legal clauses could not be traced to a study.

Taxonomy usable as a checklist (this research's synthesis, supported by the sources above): meaning drift (stance, strength or scope changes), omission (dropped constraints, caveats, numbers), fabrication (new facts), and escalation or softening of modality (a "should" becoming a "must").

## 6. Process

### 6.1 Editing levels
Editors Canada, Professional Editorial Standards (2024; https://editors.ca/professional-editorial-standards; definitions page https://editors.ca/hire/skills):
- Structural editing: "assessing and shaping draft material to improve its organization and content" (reorganise, cut, expand, adapt).
- Stylistic editing: clarify meaning, coherence and flow, refine language, removing jargon, fitting the audience, keeping the author's voice.
- Copy editing: correctness, accuracy, consistency, completeness: grammar, spelling, punctuation, usage, consistency of facts and names, style sheet.
- Proofreading: final check after layout; a proofreader should "flag or correct egregious errors", not do structural, stylistic, or copy work (quote via a search summary of the 2024 edition; the official PDF was not read).
Editors Canada licence: not found; ideas only. The Chicago Manual of Style (developmental, substantive, copyedit levels) was not fetched: ASSUMPTION about its terminology. The prior attempt's names "developmental/substantive" are therefore not confirmed here.

### 6.2 Review and audit checklists
Write the Docs "docs as code" (https://www.writethedocs.org/guide/docs-as-code/) says docs use the same tools as code (version control, issue tracker, plain-text markup, code review, automated tests) and that merges can be blocked until docs are included. The page has no audit checklist and the benefits are asserted without data. No Write the Docs audit checklist was found in this research; a documentation-audit checklist from a primary source remains an open gap. Practical consequence: use the Aghajani taxonomy and the lists below as the checklist.

## 7. Implications for a skill

### 7.1 Step sequence
Ordered from the top editing level to the bottom, matching Editors Canada, with one commit-sized change per level so each can be reviewed and reverted.

0. Scope and inventory. List files; read the repository's own style rules, templates and glossary first (they override any external guide); record the baseline (see 7.4). Classify each document by kind (Diataxis compass: action or cognition, acquisition or application), or by template where it is a structured format (ADR, RFC, changelog).
1. Audit (read-only). Report issues using the Aghajani groups: incorrect, incomplete, outdated, hard to find, mixed kinds. Do not fix content issues that need facts; list them as questions for a human.
2. Structural edit. Fix heading hierarchy and order; split or move content that mixes kinds (link instead of duplicating); add missing required sections of a known template as empty "TODO: owner must supply" markers, not invented content.
3. Stylistic edit. Active voice, hidden verbs, front-loaded points, descriptive link text, parallel lists, terminology consistency. Preserve the author's voice and any quoted standard.
4. Copy edit. Spelling, punctuation, capitalisation, dates (ISO 8601), code font, consistent names.
5. Mechanical formatting. markdownlint with auto-fix limited to whitespace and marker rules; link check.
6. Verification (7.4) and the proofread: read the diff, not the file.
7. Report: changes by level, items refused, open questions.

### 7.2 Deterministic versus judgement

Deterministic (script, linter):
- Heading levels, one H1, no skipped levels, no empty headings, no trailing punctuation, sentence-case heuristics (markdownlint MD001, MD025, MD026, MD041).
- Lists and tables well-formed, fences have a language, images have alt text, no bare URLs, link fragments valid, undefined references (MD032, MD040, MD045, MD034, MD051, MD052, MD056).
- Link text blocklist ("click here", "this document", raw URL) and duplicate link text for different targets.
- Banned phrases and patterns via Vale existence/substitution: "we" for the reader, hidden-verb phrases, "there is/are", "etc.", "and so on".
- Link and anchor integrity (lychee `--offline --include-fragments`).
- Template conformance: required headings present and in order (MD043, or a short script).
- Normative keyword, number, code block, link and id counts before and after (7.4).
- Date format, trailing newline, whitespace.

Needs judgement (model or human):
- Which kind a document is, and whether content belongs in another kind.
- Whether a passive is acceptable, whether link text is descriptive, whether list items are parallel.
- Whether a rewrite preserves meaning, tone and strength of obligation.
- Whether a statement is outdated or wrong (needs source, code or owner).
- Whether the audience needs the content ("relevant" in ISO 24495-1).
Readability scores: advisory only (Redish 2000).

### 7.3 Checklist (for the skill's output)
1. The repository's own rules and templates were read and applied before any external guide.
2. Each document has one kind or template; mixed content is moved or linked, not blended.
3. Every heading is unique, hierarchical and descriptive; one H1; no skipped levels.
4. Instructions are numbered in order; conditions precede actions; one action per step.
5. Link text is descriptive and unique; links and anchors resolve.
6. Terms are used consistently; acronyms defined on first use; names unchanged.
7. Every code block, command, path, number, version, identifier and quoted passage is byte-identical unless the change was requested.
8. Every normative keyword (all caps per RFC 8174) present before is present after, in the same sentence.
9. No new factual claim; each added sentence is traceable to the old text, the repository, or a named source.
10. Open issues (outdated, missing, unverifiable) are listed, not patched.
11. Style findings that were not applied are listed with a reason.

### 7.4 Verifying that an edit preserved meaning
Compute a fingerprint before and after, per file, and diff the fingerprints. A change is allowed only if the diff is empty, or each difference is listed and approved.
- Counts of RFC 2119 words in all capitals (MUST, MUST NOT, SHALL, SHOULD, MAY, REQUIRED, RECOMMENDED, OPTIONAL, NOT RECOMMENDED), plus a list of the sentences containing them; also lower-case "must/should/may/shall" counts, since a loss of capitals or a promotion changes meaning (RFC 8174).
- Sets of numbers with units, versions, dates, percentages, and their surrounding words.
- Fenced and inline code, byte-for-byte (hash each block).
- Link targets (set equality) and anchors; heading list (ids and titles; renames require a redirect or anchor-preservation note).
- Record ids and cross-references (patterns the repository defines); proper nouns and defined terms from the glossary.
- Negations and quantifiers: counts of "not", "never", "only", "all", "any", "except", "unless", "at least", "at most", "before", "after". A drop or addition is flagged for review (ASSUMPTION: a useful heuristic, not validated in the literature).
- Length change: a large shrink is a signal for omission, which the summarisation literature identifies as a main failure.
- Second reader: a separate context, given the old and new text and a short rubric (list each constraint, number and condition in the old; mark preserved, weakened, strengthened, dropped, added in the new). InkSync's approach is the analogue: surface additions of new information rather than trusting the editor (https://arxiv.org/abs/2309.15337). Give the second reader the diff, not the first reader's conclusion.
- Human sampling for high-risk files (specifications, security, safety, legal text).

### 7.5 What the skill must refuse
- Change meaning: no edit that alters scope, conditions, strength of obligation, or order of steps; if clarity needs a change that could alter meaning, ask.
- Drop a normative sentence or any constraint, caveat, warning, exception, number, or example, even if redundant; merging duplicates requires listing both sources.
- Invent facts: no new versions, flags, commands, behaviours, rationale, dates, authors, or links; missing content is marked as a gap for the owner.
- Rewrite a quoted standard, licence text, legal text, generated file, verbatim output, or a block marked as generated or frozen; changes there are findings only.
- Alter code, command lines, paths, identifiers, or ids (record ids are never renumbered).
- Change the case of requirement keywords, or add RFC 2119 words where the document does not define them.
- Edit history records (changelog entries already released, decision records marked accepted); ADR practice is to supersede, not rewrite (https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions says reversed decisions stay recorded and marked superseded).
- Impose an external guide where it conflicts with the repository's rules.
- Copy text from share-alike or unlicensed sources into the repository (Diataxis CC BY-SA 4.0, arc42 CC BY-SA 4.0).
- Use a readability score as a pass/fail target.

### 7.6 Open items and unverified points
- ISO 24495-1 guideline-level text was not read (paywalled, 403).
- Vale package list, markdownlint licence, Microsoft guide licence, Chicago levels, Standard Readme licence: not confirmed.
- Practitioner-survey (ICSE 2020) findings: only the abstract-level facts from search listings.
- No empirical study on LLM-edited software documentation was found; the failure-mode list is inferred from adjacent work (summarisation, simplification, essay revision).
- No primary-source documentation audit checklist was found (Write the Docs page has none).
