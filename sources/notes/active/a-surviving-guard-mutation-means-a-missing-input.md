---
slug: "a-surviving-guard-mutation-means-a-missing-input"
topic: "verification"
claim: "A surviving mutant that removes a guard is not evidence that the guard is dead: no test produces its input, no assertion observes what it prevents, it is not worth a test, or the mutant is equivalent; show equivalence, never infer it from survival, before the guard is deleted."
confidence: "reasoned"
phases: ["tests"]
check: "before a guard is removed: its reaching input searched for in the fixtures and in the real data, an assertion on what it prevents, or a written argument that the mutant is equivalent"
about:
  - {do: "Delete a guard because removing it broke no test", wrong_when: "no test produces its input or asserts its effect"}
rests_on: "equivalent-mutant undecidability (Budd & Angluin 1982); RIPR, Li & Offutt 2017"
strength: "well established"
our_evidence: "occurrences in two repositories; no rate"
cues: ["mutation test", "surviving mutant", "remove guard", "dead code", "unused branch", "if guard", "mutmut", "no test fails", "unreachable", "delete check", "simplify condition", "edge case input", "equivalent mutant"]
---

# A surviving guard mutation means a missing input, until shown otherwise

## Why it works

A mutant that deletes a guard and survives tells you that nothing in the suite distinguished the code with the guard from the code without it. It does not say why, and there are four explanations:

- **No test produces the input** the guard exists for: the reaching input is missing.
- **The input is produced, but no assertion observes what the guard prevents**: the wrong value propagates and nobody looks at it.
- **The guard is not worth a test**: a log line, a capacity hint, behaviour outside the specification.
- **The mutant is equivalent**: no input can make the two versions differ.

Only the last makes the guard dead, and it is the one that cannot be inferred from survival: equivalence is undecidable in general, and in studies of hand-classified mutants close to half of the survivors were *not* equivalent. Reading survival as "dead code" bets a deletion on a coin flip, and the loss is asymmetric: a deleted guard is a defect waiting for its input, while a kept one costs a test.

So the search comes before the deletion. Look for the reaching input in the fixtures and in the real data the code will meet: an input absent from the fixtures is often present in production, and running the surviving mutant over the real corpus is the cheapest way to find it. Look for an assertion that would see the guard's effect. A cheap signal on the way: a mutant that changes what runs (coverage, branches taken) is more likely to be killable than one that does not. And a guard whose input occurs nowhere today stays as declared specification, pinned by a synthetic test that says so.

## When it does NOT apply

- **The mutant is shown equivalent**: its compiled form is identical to the original's, or no input can reach the mutated point or change the state there.
- **The guarded code is arid**: logging, a hint, behaviour that is not part of the specification. Not every surviving guard is untested; some are unproductive to test.

## What it costs

A search for the reaching input, in the fixtures and in the real data, before every deletion a mutation tool suggests; a run of the mutant over a production corpus where one exists; and synthetic tests for guards whose input does not occur yet, which look like tests of nothing until the input arrives.

## Where it came from

An app repository with an on-device test suite: a guard meant to allow one action per input event was removed as untestable after its mutation survived. A fresh-context review found the path (a small drift within the input's tolerance before a longer gesture), a test then reproduced two actions from one input, and the guard came back with that test biting.

A second repository, building data artefacts from two real sources, met it several times in about a week. A branch whose removal changed nothing in the suite was, over the real sources, the only rescue for tens of records, so it earned a test instead of a deletion. A prefix-instead-of-exact mutation survived until the real data showed words that share the prefix, and a handful of real keys would have been destroyed. A guard whose trigger occurs nowhere in today's source was kept as specification for the next one. Two tests could not reach their branch (a declaration cycle in which nothing is absorbed, and a fixture whose key made the precedence unobservable), and two fixtures never contained the case (a cut that happened to land on a boundary, and no punctuation at the cut). Each of those is the missing-input or missing-assertion explanation, not a dead guard.

## Literature

- **Budd & Angluin, 1982, "Two notions of correctness and their relation to testing"** (Acta Informatica 18). *Bibliographic record checked 2026-10-05; the full text was not opened.* Cited, as the survey below cites it, for the undecidability of mutant equivalence.
- **Papadakis, Kintis, Zhang, Jia, Le Traon & Harman, 2019, "Mutation Testing Advances: An Analysis and Survey"** (Advances in Computers 112). *Checked 2026-10-05 against the authors' copy.* Detecting equivalent mutants is undecidable and handled only by heuristics (identical compiled code; mutants shown unable to reach or infect). **What we take:** equivalence is shown by a specific argument, never inferred from survival.
- **Li & Offutt, 2017, "Test Oracle Strategies for Model-Based Testing"** (IEEE Transactions on Software Engineering 43(4)). *Checked 2026-10-05 against the authors' copy.* Extends reachability, infection and propagation to RIPR: a fault that propagates is still missed if the oracle does not check the part of the state holding the wrong value. **What we take:** the second explanation; a surviving guard mutant may have its input and lack the assertion.
- **Schuler & Zeller, 2013, "Covering and Uncovering Equivalent Mutants"** (Software Testing, Verification and Reliability 23(5)). *Abstract checked 2026-10-05.* In manually classified mutations over seven programs, about 45 % of undetected mutants were equivalent, each classification took about a quarter of an hour, and a mutant that changes coverage is more likely non-equivalent. **What we take:** survival is close to a coin flip, so the note rests on the cost of a wrong deletion, not on frequency; and the coverage signal.
- **Petrović, Ivanković, Fraser & Just, 2021, "Practical Mutation Testing at Scale"** (arXiv preprint). *Checked 2026-10-05.* Developers judged many reported mutants unproductive, trivially equivalent or not worth a test, and mutants in arid code are suppressed before they are generated. **What we take:** the third explanation and the boundary.

**Where we go further:** the literature gives the explanations; what it does not give is the order of the search for an agent about to delete a guard, the real-data corpus as the place the missing input usually is, and keeping a guard with no input today as declared specification.

## Evidence

**Reasoned, from occurrences in two repositories:** one guard deleted and restored with the test that bites; several surviving mutants in a week, each explained by a missing input or a missing assertion, one of them the only rescue for tens of real records. No rate. The experiment: for every surviving guard mutant over a period, record which of the four explanations held once it was investigated, and how many were found only by running the mutant over real data.
