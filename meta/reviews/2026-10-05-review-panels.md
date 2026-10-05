# One reviewer or several, and what the bundle should say meanwhile

**Date:** 2026-10-05. **For:** the queued candidate `adversarial-review-per-attack-surface-before-a-tag`, and 0.0.27's
whole-branch review offered at the end of a multi-task plan. **Status:** research; nothing changed.

## Findings

- **Human inspection:** one reviewer finds less than two; four find no more than two (Porter et al. 1997, a
  randomised field experiment); practice settled on two active reviewers (Rigby & Bird 2013); collection meetings add
  nothing net — independent reviewers whose findings are merged do as well (Porter, Votta & Basili 1995).
- **Splitting by perspective or area is unsettled:** scenario- and perspective-based reading beat ad hoc reading in
  some experiments (Porter et al. 1995; Basili et al. 1996; Biffl & Halling 2003), found nothing in a replication
  (Regnell et al. 2000), and an aggregation found no clear effect and signs of researcher bias (Ciolkowski 2009).
  The comparison that matters is k specialists against k generalists, not against one.
- **LLM review:** merging repeated runs of the same reviewer alone roughly doubled recall on a benchmark of real pull
  requests (SWR-Bench, 2025); the union of different agents beat the best single one by about a third (c-CRAB, 2026);
  errors are correlated across models (Kim et al. 2025); deliberating teams fall short of their best member (Pappu et
  al. 2026); a verifier agent is not a gate (TeamBench, 2026). A fresh context is well supported: models miss their
  own errors and catch the same ones attributed to others (Tsui 2025; Huang et al. 2023; Kamoi et al. 2024).
- **The 0.0.27 evidence claim should be narrowed:** the five repositories' reviews had no control and recorded no
  precision, and on large changes almost any capable review finds something (a vendor reports findings on most changes
  over a thousand lines; vendor figures, not peer reviewed).

## What the bundle should state meanwhile (proposed for the next release)

1. Keep the offered whole-branch review; narrow its evidence sentence (uncontrolled; a second run of the same reviewer
   was never compared).
2. Ask every review for a proof per finding (the command, test or line); one without is reported unconfirmed.
3. Each review records confirmed and rejected findings, tokens and minutes in the entry's *Review*: free data.
4. Rewrite the candidate's gap: it lacks a comparison with k independent generalists at equal cost; what holds either
   way is independence, merged findings with proofs, no debate, and that a verifier's approval is not a gate.
5. Do not offer an area split yet.

## The experiment

On the home's own history (states before reviews whose fixes are known; a sealed planted-defect set as a secondary
unit), isolated from later history: arms G1 (one generalist), G1c (one with a five-area checklist), G3 (three
independent generalists, merged), S3 (three area reviewers, merged), equal tokens per reviewer, two runs each, a blind
adjudicator. Pre-registered: the split wins if S3 beats G3 by at least fifteen points of recall on blocking or silent
defects with comparable precision; it loses within five points; more reviewers are worth it if they find a blocking
defect one reviewer missed on half the units; stop early if one reviewer finds nine in ten. Cost (estimate): a pilot
of about 5×10^6 tokens, a minimal version about a third of that.

## References (opened 2026-10-05; full text where the research agent marked it)

Porter, Siy, Toman & Votta, IEEE TSE 1997; Porter, Votta & Basili, IEEE TSE 1995; Basili et al., Empirical Software
Engineering 1996; Regnell, Runeson & Thelin, ESE 2000; Ciolkowski, ESEM 2009; Biffl & Halling, IEEE TSE 2003; Rigby &
Bird, ESEC/FSE 2013; Bacchelli & Bird, ICSE 2013; McIntosh et al., MSR 2014; Kemerer & Paulk, IEEE TSE 2009; Briand et
al., IEEE TSE 2000; SWR-Bench (arXiv 2509.01494); c-CRAB (arXiv 2603.23448); Kim et al., correlated errors (arXiv
2506.07962); Kim et al., scaling agent systems (arXiv 2512.08296); Pappu et al. (arXiv 2602.01011); TeamBench (arXiv
2605.07073); Cemri et al. (arXiv 2503.13657); Huang et al. (arXiv 2310.01798); Kamoi et al. (arXiv 2406.01297); Tsui
(arXiv 2507.02778); Panickssery et al. (arXiv 2404.13076); Xiang et al. (arXiv 2607.21656); Du et al. (arXiv
2510.05381); McAleese et al. (arXiv 2407.00215); Cihan et al. (arXiv 2412.18531).
