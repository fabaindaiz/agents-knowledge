---
slug: "copied-instruction-claims-its-origin"
topic: "evolving-contracts"
claim: "A file copied from another repository, or metadata copied from the artefact another was cut from, keeps asserting facts about its origin — its stack, its commands, its layout, the run that made it — and it is read as if it described the copy."
confidence: "reasoned"
phases: ["plan", "review"]
check: "every command in a copied file is run once and every path resolved, and a derived artefact's metadata is copied by an explicit allowlist; what cannot be verified is removed, not softened"
about:
  - {do: "Copy an instruction, rule, config file or script from another repository, or derive an artefact from another", wrong_when: "the copy is made for its shape and read later for its content, and nothing marks which facts were about the origin"}
rests_on: "Aghajani et al. 2019; Lethbridge et al. 2003 — **drift research, a weaker claim**: none on copies"
our_evidence: "occurrences in four repositories, and three copies of one bundle; no rate"
boundary: "A bundle designed to travel, its repository-specific fields enumerated and its content free of local nouns · even then, those fields are never taken from upstream"
cues: ["copied from", "copy config", "template repo", "claude.md", "agents.md", "stale commands", "boilerplate", "metadata copy", "fork", "makefile copied", "readme paths", "cargo cult", "derived artefact", "allowlist fields"]
---

# A copied instruction claims its origin

## Why it works

Instruction files are copied precisely because writing one is expensive, and the copy is made at the moment somebody wants the *shape*, not the content. The shape is what transfers; the content is what is read later, by an agent that has no way to tell which sentences were about somewhere else.

It is worse than stale documentation in one specific way. Stale documentation was true here once, so its claims are at least the right *kind* of claim. A copied file may assert a build command that never existed here, a directory that does not exist, or a guardrail protecting an invariant this system does not have — and each of those reads exactly like a fact somebody established.

The failure is silent by construction:

- **It is confident.** Nothing in the prose marks which parts were inherited.
- **It is load-bearing.** Instruction files are consulted before acting, so a wrong one steers work before anyone checks it.
- **It survives review.** A reviewer who knows the repository skims a file that looks like the one they remember writing.

The defence is to treat a copy as *data until verified*: every command run once, every path resolved, every guardrail matched against something that actually exists here. The parts that cannot be verified are removed, not softened — a sentence nobody can check is a sentence that will be believed.

The same holds beyond instruction files. A script copied as a template carries its assumptions about where it lives, such as a root resolved to its own folder. An artefact derived from another by copying the parent's metadata wholesale declares facts about a run it never had, and a configuration object copied whole into an artefact carries build-only keys into it. There the defence is the boundary below made mechanical: copy metadata by an explicit allowlist, and keep what an artefact declares about itself apart from how it was built.

## When it does NOT apply

A bundle explicitly designed to travel, whose repository-specific fields are enumerated and whose content is written without local nouns — the whole point of separating what is portable from what is local. Even then, the fields that describe *this* repository are the ones a copy must never take from upstream.

## What it costs

Running every command and resolving every path in a file somebody already wrote, which feels like redoing finished work and is the reason it gets skipped. For derived artefacts, an allowlist to keep up as metadata fields are added.

## Where it came from

A hardware-bound service found, during a documentation audit, that one of its language-specific instruction files had been copied from another repository — it had been shipping instructions for a different project — and corrected it. A second repository in the same workspace had a set of rule files and a prompt file cloned from a sibling; the fields that described the sibling were only noticed when a distribution pass compared them.

## Literature

The closest established work is on documentation drift, which is a weaker claim: drift starts true and decays, while a copy starts false. No source was found on copied instruction files specifically.

- **[Aghajani et al., 2019, "Software Documentation Issues Unveiled"](https://doi.org/10.1109/ICSE.2019.00122)** (ICSE). "Up-to-dateness problems account for 39% of issues related to documentation content"; an outdated document is one "not in sync with other parts of a system" whose information "was correct and complete before a change was introduced." *Verified 2026-09-23 against the paper.* **What we take:** that content going false is the dominant documentation defect, not a corner case. **Where we go further:** their definition assumes the text was once correct here; a copy never was, so no change in this repository marks the moment it went wrong.
- **[Lethbridge, Singer & Forward, 2003, "How Software Engineers Use Documentation"](https://doi.org/10.1109/MS.2003.1241364)** (IEEE Software). Out-of-date documentation "has value, particularly if the high-level abstractions remain valid." *Verified 2026-09-23 against the paper.* **Where we differ:** that tolerance rests on the abstractions having been true of this system; a copied file's abstractions describe another one, which is why this note removes unverifiable sentences rather than keeping them as approximately right.

## Evidence

**2026-09-22 — the same failure in executable code, in a cloud service.** A new script followed an existing one that resolves its root to its own folder, where neither the source tree nor the environment file is. It was checked before use and corrected; the original still has the defect, left alone rather than fixed inside an unrelated change.

**2026-09-29 — the boundary's second half, broken three times.** Three repositories, over two consecutive releases, received a bundle designed to travel by a plain copy of its folder instead of its export command. Each copy carried the source's own record: its identity file (one with the empty upstream that means "this is the home") and between five and eight learnings written under the source's identity. The integrity check printed "verified" in all three; the copy was found only because the bootstrap asks the agent to read the identity file by hand first, and in one the agent's first plan was to keep the foreign identity and write its own records under it. So a travelling bundle is not exempt by design alone: the fields that describe a repository must be refused when copied, which is a check (an identity another repository in scope also holds), not a convention.

**2026-10-01 — an artefact's metadata, in a repository building data artefacts.** A smaller artefact cut from a larger one by size inherited a ledger describing an extraction it never performed, on the order of a hundred thousand drops it never made. Every test and the artefact verifier were green; it was found by deriving a sample and reading its metadata. In the same session, one key added to a per-artefact build declaration leaked into the metadata writer, which failed three layers away with a storage error that named no field. Both are the copy asserting its origin, and both are closed by copying metadata by an explicit allowlist.

**Reasoned: occurrences in four repositories, and three copies of one bundle; no rate.** What would measure it: for each instruction file in a set of repositories, run every command it names and resolve every path, and count the assertions that fail per file — separating "was never true here" from "stopped being true".
