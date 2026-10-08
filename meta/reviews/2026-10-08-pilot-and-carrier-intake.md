# Two intakes for 0.0.31: a pilot's four candidates and one carrier's first update (2026-10-08)

One `release.py intake --version 0.0.31` over one gather, run from the home on the owner's request. No release
was cut. It took in two sources:
- **A pilot**: four candidate learnings from a four-arm experiment run in a repository with no carrier id. They
  entered as the home's own proposals (`d-5ed7e8-67a443`), with the literature each one named as missing.
- **A carrier**: the 15 proposals of one carrier's first formal update to 0.0.30 and its harvest. The update's
  process log and harvest report were read as evidence and stay in that carrier.

Neither source is named here. The pilot's domain is left out, and the carrier is "one carrier".

| | |
|---|---|
| Received | 18 proposals: the home's 6 (the pilot's 4 and two left from the 0.0.30 close) and 12 of the carrier's 15 |
| Held | 3 of the carrier's, on unanswered `quote` warnings (see *The carrier*) |
| Queued as new candidates | 4, of which 3 left the queue the same day by verdict (`meta/tracking/history.md`) |
| Experiment runs logged | 2, both *confirms* |
| Roadmap items added | `i-5ed7e8-1dd18c`, `i-5ed7e8-74d789`, `i-5ed7e8-e44264`, `i-5ed7e8-460736` |

## The pilot

**What was tested.** One open system-design question spanning several components and an effect that cannot be
undone, asked in chat and answered four ways by the same model:

| Arm | Condition | Read |
|---|---|---|
| A | fresh agent, no tools, no knowledge base | nothing |
| B | fresh agent told to follow the knowledge base's read-me, then its index | the read-me, the index, about twenty cards, a few notes |
| C | the session holding the conversation, picking cards by title from a directory listing | 7 cards |
| D | fresh agent with B's access, interactive: explained eight decisions with priced options, recommended first, decided sixteen by default, then designed from the answers | about twenty cards, a few notes |

One person judged A, B and C blind, problem by problem, over eight problems. C was preferred most, A next and B
least. In D the user took the recommended option three times in four, and afterwards preferred D's format to all
three. Known threats: one question and one judge; the judge had read C before; C had the conversation's context;
labels were shuffled per problem but kept fixed positions, and the middle one was picked three times in four; D's
recommendation always came first. The repository had no root instruction file yet, so nothing told C to route
through the index. The export gave B and D's reads as about twenty cards each, and a message gave one figure one
card higher; the export's is used.

### The literature, and how far each source was read

Four delegated researchers searched one area each; a fifth checked every citation against its own page. Their
shell fetches were mostly refused (`i-5ed7e8-460736`), so most sources were read through a summarising fetch.
**Level** says what was actually seen: *body* (the claim in the full text), *abstract*, or *bibliography only*.

| Source | Level | What it says, paraphrased | Bears on |
|---|---|---|---|
| Liu et al., "Lost in the Middle", TACL 2024, [arXiv 2307.03172](https://arxiv.org/abs/2307.03172) | abstract | answers are best when the relevant passage sits at the start or end of a long context | 1: reading more cards is not free |
| Cuconasu et al., "The Power of Noise", [arXiv 2401.14887](https://arxiv.org/abs/2401.14887) | body (§5.1, Table 1, by a delegated reader); venue not confirmed | passages that rank high but lack the answer lower accuracy; a few retrieved passages did best | 1: extra cards help only if they bear on the question |
| Sarthi et al., "RAPTOR", [arXiv 2401.18059](https://arxiv.org/abs/2401.18059) | abstract; venue not confirmed | retrieval over a tree of recursive summaries beats flat retrieval on several tasks | 1: structure helps, in one benchmark |
| Asai et al., "Self-RAG", [arXiv 2310.11511](https://arxiv.org/abs/2310.11511) | abstract | retrieving a fixed number of passages regardless of need can hurt; retrieving on demand does better | 1 |
| Hansen & Wänke 2010, [10.1177/0146167210386238](https://doi.org/10.1177/0146167210386238) | abstract; journal pages from a search result | the same statement worded concretely is judged more probably true | 2: indirect, credibility not preference |
| Kaminski, Sloutsky & Heckler 2008, Science, [10.1126/science.1154659](https://doi.org/10.1126/science.1154659) | bibliography only | (unverified) abstract instruction transferred better to a new problem | 2: the boundary, unverified |
| Singhal et al., "A Long Way to Go", COLM 2024, [arXiv 2310.03716](https://arxiv.org/abs/2310.03716) | abstract | a reward built on length alone reproduces most preference-training gains | 2: length biases preference |
| Zheng et al., "Judging LLM-as-a-Judge", NeurIPS 2023, [arXiv 2306.05685](https://arxiv.org/abs/2306.05685) | body (§3.3–3.4, by a delegated reader) | model judges show position and verbosity bias; remedy: judge in both orders | 2, 4 |
| Wang et al., "Large Language Models are not Fair Evaluators", [arXiv 2305.17926](https://arxiv.org/abs/2305.17926) | body (§2.2, §3.2, by a delegated reader); venue not confirmed | swapping two answers' order changes the verdict often; balanced position calibration | 4 |
| Kuhn, Gal & Farquhar, "CLAM", [arXiv 2212.07769](https://arxiv.org/abs/2212.07769) | abstract | detect ambiguity, ask, then answer: more accurate on mixed questions | 3 |
| Li, Tamkin, Goodman & Andreas, "Eliciting Human Preferences with Language Models", [arXiv 2310.11589](https://arxiv.org/abs/2310.11589) | abstract | model-led elicitation more informative than user-written prompts; users report less effort and new considerations | 3: closest, no comparison with a complete answer |
| Vijayvargiya et al., "Ambig-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering", [arXiv 2502.13069](https://arxiv.org/abs/2502.13069) | abstract | interaction on underspecified coding tasks gives large gains; models struggle to tell when to ask | 3 |
| Horvitz, "Principles of Mixed-Initiative User Interfaces", CHI 1999, [author's copy](https://erichorvitz.com/chi99horvitz.pdf) | body (by a delegated reader); pages not seen | ask when the goal is uncertain and a wrong action costs more than the interruption | 3; now in `sources/references.md` behind principle 15 |
| Johnson & Goldstein, "Do Defaults Save Lives?", Science 2003 | not opened | (unverified) defaults raise uptake far above opt-in | 3: not relied on |
| Valenzuela & Raghubir 2009, [10.1016/j.jcps.2009.02.011](https://doi.org/10.1016/j.jcps.2009.02.011) | abstract | options in the centre of an array are chosen more, believed most popular | 4 |
| Attali & Bar-Hillel 2003, [10.1111/j.1745-3984.2003.tb01099.x](https://doi.org/10.1111/j.1745-3984.2003.tb01099.x) | abstract | test makers and takers favour middle positions | 4 |
| Krosnick & Alwin 1987, [10.1086/269029](https://doi.org/10.1086/269029) | bibliography only | (unverified in part) primacy in survey responses | 4: not relied on |
| Williams 1949, [10.1071/CH9490149](https://doi.org/10.1071/CH9490149) | abstract | designs balanced for the preceding treatment: one square for an even order, two for an odd one | 4: the counterbalancing design |

**The position figure.** With three positions and eight problems, the middle chosen at least three times in four
has a probability of about 0.02 under chance if the middle was named in advance, and about 0.06 if any position
could have been the favoured one. Enough to justify the rule, not to claim a measured effect.

### Verdicts

| Proposal | Candidate | Verdict | Why |
|---|---|---|---|
| `p-6a1060aa5b` | `consult-knowledge-through-the-index` | **merged** into `index-unread-where-rules-absorbed-it`, as its second repository | The rule exists: the bootstrap wires the index into the root file's map (`prompt-bootstrap.md`), and *nothing in `.agents/` loads by itself*. With no root file before a bootstrap, the rule reached no session. The queued candidate is another repository where the index went unread during design. Whether both show one claim, and whether reaching more cards gives a better answer, wait on the experiment, since the routed answer was the least preferred. |
| `p-d9a96d5862` | `a-card-enters-an-answer-as-a-mechanism` | **queued** | Passes the noun test, but rests on one judge with three confounds. The literature bears only indirectly and the length bias cuts across it. |
| `p-03af58edfc` | `ask-the-design-decisions-before-designing` | **folded** into `prompt-context.md` §15, text unchanged | Not the pre-flight, which asks facts that cannot be read. §15's decision-review mode covers more decisions than one message holds, and §15 already says a recommendation listed first acts as a default, which is why the three-in-four uptake cannot be read as agreement. "The only form that contains the risks" is an argument: a complete answer could state each alternative's risks. |
| `p-ec397a675e` | `counterbalance-positions-in-a-blind-comparison` | **refused** as a learning | An established result. Taken as a procedure for the home's own comparisons: `evals/README.md` §*Blind comparisons*. |
| `p-7954a4c123` | the id-name table (extends `prompt-context`) | **queued**, offered again to merge | One carrier's evidence; the owner chose to wait for a second. |
| `p-b90ef8c317` | a heading lookup as a derived copy | **merged** into the note `derived-copy-goes-stale-silently`, *Evidence* | Another form of the stale copy: a lookup key in code, repeated in a test fixture. |

### The follow-up experiment, queued

Rows for `index-unread-where-rules-absorbed-it` and `a-card-enters-an-answer-as-a-mechanism` in
`meta/tracking/experiments.md`, which `OPEN.md` shows. The design:

- **Questions:** six open design questions, written without the pilot's domain, before anyone reads the answers.
- **Single-shot arms:** four, each run twice per question. No knowledge base; routed through the read-me and the
  index; cards picked by title by a fresh agent, so none has the conversation's context; and a volume control
  that picks by title but reads as many cards as the routed arm. The control separates routing from reading volume.
- **Interactive arm:** the decision walk, its recommended option in a random position. It is compared with a
  complete answer that carries the same options and risks.
- **Judges:** two people who have read no answer before, and a model judge of another family run in both orders.
- **Positions:** each question is judged over eight problems, as in the pilot, and the four single-shot arms
  sit in a Latin square of order four over them, each arm in each position twice; each position's rate is reported.
- **Measures:** preference per problem; a rubric of failure handling, scored blind; the relevant cards each arm read;
  each answer's length.
- **Cost:** about 50 answers, of the order of millions of tokens on a subscription (hours). About 12 hours of
  judging and 2 of answering the interactive arm's decisions.

## The carrier

**The proposals.** All 15 matched the harvest report's mapping, by id, kind and target. Twelve entered: ten name
a slug already known and wait under *Offered again, to merge* for the 0.0.31 release's verdicts, and two are
experiment runs, logged as *confirms*.
Three were held: their `quote` warnings quote the bundle's procedure and its tool's messages, which the owner judged
false positives in the carrier's log, but intake accepts only `privacy-allow:` on the line. They stay in the carrier,
unedited, and enter at the next gather once `i-5ed7e8-74d789` lands.

**The process log's findings**, against what the proposals cover:

| # | Finding | Covered by | Otherwise |
|---|---|---|---|
| 1 | the live tool cannot verify a release that changed the bundle's shape | `p-5fd7b61d19` (held) | — |
| 2 | the live update procedure is one version behind the deltas it applies | `p-d2fa16b1fd` (held) | — |
| 3 | a worktree lacks the gitignored inputs a gate needs | `p-b5ed4535bd` | — |
| 4 | the update's pre-flight and the harvest's nest | `p-38a48d40f6` | — |
| 5 | a branch cut from the previous release's remote branch tracks it | `p-cc620f4084` | — |
| 6 | `export` refuses a non-empty folder | `p-de14564c12` (held) | `i-5ed7e8-1dd18c`, with 7 |
| 7 | edit denies leave a shell copy as the only way to replace the bundle | the log only | `i-5ed7e8-1dd18c` |
| 8 | `privacy` warns on quotes of the bundle's own text | the log only | `i-5ed7e8-74d789` |
| 9 | a harvest sees only the transcripts on its own machine | the log only | none: an occurrence of the `close` skill's rule that what lives on one machine is written down |
| 10 | `align` stops at a listed carrier with no bundle on disk (found here) | — | `i-5ed7e8-e44264` |

**Estimates for the tool changes.**
- **Finding 1, about 1–2 hours.** The fix that helps is in the procedure: verify with the incoming copy's own tool,
  run isolated, as a named exception to "nothing in `incoming/` is loaded", since the checksum against the tag
  already proves the copy's origin. A verifier tolerant of the previous shape costs about half a day and helps only
  from the next shape change on. By finding 2, any procedure change reaches a carrier one release late.
- **Findings 6 and 7, about 3 hours.** `export --replace`.
- **Finding 8, about 3 hours.**

**The OPEN experiments this carrier could answer in minutes.** Worth running there: `absent-constraint-widens`
(it has a fake store client and scoped queries) and `documented-defaults-drift-from-code` (against the documented
settings only). Not worth it: `nested-partial-update-replaces`, since the fake may not model nested updates and an
emulator is not minutes; and the ratchet under load, since that ratchet is hand-copied from a sibling and would not
be an independent occurrence. Both are already queued; nothing was added.

**Register and align.** `release.py register` on the carrier's worktree set its row to 0.0.30 and kept the main
checkout's path in the machine's manifest, as the 0.0.30 fix for worktrees intends. `align` given the worktree
reports it aligned. `align` over the manifest stops at the main checkout, which holds no bundle while the pull
request is unmerged, and checks no other carrier. Neither answer is right: the release is on a branch, not on the
carrier's integration branch. The roadmap records it under *Blocked outside*, and `i-5ed7e8-e44264` makes `align`
say so.

**Templates.** Two template repositories exist now, and the roadmap's standing facts record both and when each was
refreshed, without naming the second. `AGENTS.md` step 7 and `prompt-sync.md` Phase 3 step 6 now say "each template
repository". The step's copy of the agents named only the reviewer, which 0.0.30's researcher made stale; it now
copies every agent.

## What went wrong in this session

- **My delegations named a scratch folder the researcher's hook refuses.** The host's guidance for background jobs
  names its own temporary folder; the researcher's definition and hook accept only the system temporary folder. My
  prompt won, the agents' fetches were refused, and most citations stayed at their abstracts. The hook's refusal
  named neither the folder nor the shape it accepts, so three agents gave up on the shell (`i-5ed7e8-460736`).
- **`align` at the session's start printed one line and checked nothing**, and it read as a report until the code
  was read (`i-5ed7e8-e44264`).
- **The worktree's isolation refused compound shell commands** reaching another repository's files; they were split.
- **A fresh-context review of this diff found two counts the records did not support and a pilot description
  close enough to its domain to be recognised.** The counts were corrected, and three of the pilot's proposals were
  written again, generalised, before any commit; their ids changed with their text.
