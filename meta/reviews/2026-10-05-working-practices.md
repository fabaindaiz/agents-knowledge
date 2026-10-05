# Three working practices in the agent's flow — decision review, deciding by example, walking the user

**Date:** 2026-10-05. **Status:** research for release 0.0.27; the designs in §4 are what the owner
approved on that date, before wording. **Sources:** the owner's turns in every session transcript on one
machine (some seventy sessions over about six weeks, across ten repositories, about a thousand messages
and some six hundred questions asked through the question tool), read by one agent with no access to
any repository's content; a second agent's reading of the installed skills and of the literature; and
the harvest readings of eight carriers. Counts are given as ratios; what was said is paraphrased.

## 1. What the owner actually does

**Questions are the main decision channel, and two modes coexist.**

- A short batched **pre-flight**, as §15 and the pre-flight section describe: answered in one word when
  the defaults are right.
- A long **decision review** that the owner asks for explicitly, in most of the repositories: every
  decision of a spec or design, one per round or in themed rounds of up to four, each explained with an
  example. Reviews of fifteen to thirty questions ran without complaint, at roughly one to two minutes
  per question.
- A **fact interview**: facts only the owner holds, with the agent's reading stated for confirmation and
  no recommendation.
- **"Ask me everything now"** before leaving the agent alone, or before an expensive step: questions
  that would otherwise arrive mid-work are batched or parked.

About three questions in four carried a recommendation, always first; it was taken about seven times in
ten. Free text, about one answer in fifteen, overrode the options and carried most real corrections. In
one carrier the owner's rulings were walked *after* a plan had run, and most of them changed or grew,
costing an addendum of about a dozen tasks; the next round walked them *before* the plan, and no
addendum followed.

**Decisions go fastest when each option carries something concrete**: a draft with its length and the
time it saves, a rendered mockup or capture, a measured table, a working spike, a sample of real data
that misbehaves. Pricing an option did not change how often the recommendation was taken; it removed
the follow-up questions. The owner repeatedly asks for, or writes, a **middle option** composed of two
offered ones; in the largest review such composites won about a third of the answers.

**User-flow iteration is driven by the owner's own use.** The owner uses the build on the real device
and sends batches of observations; each is expected to be reproduced on an emulator that matches the
device, fixed with a test that fails first, swept for its whole class, and answered by name in the
report. Where agents walked flows themselves (two carriers), they found dead ends and cut one task to
less than half its steps, but walked mostly the ideal path; delays, interruptions and setbacks came
from the owner or from flaky tests.

**Corrections that recur:** a question buried in a long report; a term the owner did not know; a
question an emulator or probe could have answered; a choice the agent made silently (a whole language
added to the stack); a part of a batch of observations left unanswered; questions drifting out of the
owner's language after a context compaction.

## 2. Where this meets the bundle

| Rule today | Observed | Verdict |
|---|---|---|
| §15: ask before writing, together, cap at three | holds for an unsolicited batch; a review the owner asks for runs to thirty | refine: name the modes |
| §15 / pre-flight: a question mid-work has already been answered by the code | welcome when a measurement overturned a premise, or when the owner opened a channel | refine: batch before writing, before an expensive step and before autonomy; otherwise park |
| §15: decide what is reversible in ten minutes | what the user sees, the stack, and the owner's own content are wanted as questions even when reversible | refine: reversibility is not the only test |
| Pre-flight: say what you are not asking | rarely done; silent decisions were found later | enforce, at the end of every mode |
| Pre-flight: could I answer this by reading or by trying? | answers sent the agent to the emulator | state that a probe, an emulator or a spike counts as trying |

## 3. What the installed skills cover

No installed skill does any of the three. The general-purpose brainstorming skill asks one question at
a time only to understand intent, then approves a design section by section; it never inventories the
decisions of an existing spec, and some of its rounds carried no recommendation. The planning and
test-first skills consume a list of cases but never produce one. A branch-finishing skill asks about a
pull request after every phase, which the owner's standing rule already answers. Licences: the
general-purpose skill set is MIT; one plugin set is Apache-2.0 at its root; one document skill carries no
licence of its own. **Ideas only enter the bundle; no text is copied**, and the bundle recommends those
skills as optional seams, by the moment each fits.

## 4. The approved design

1. **§15 names four question modes** and says which one runs: the pre-flight (at most four questions,
   aim for three, each with a default, `defaults` offered, one line on what is not asked); the decision
   review (the skill below); the fact interview (the agent's reading, confirmed; no recommendation); and
   parked questions (during autonomy: decide what is reversible and not user-visible, write the rest to
   the roadmap with a recommendation, raise them at the next report). Every mode asks in the owner's
   language and plain words, never asks what a probe could answer, and never hides a question inside a
   report.
2. **The example rule (b), in §15:** every option shows one concrete case at the same fidelity, is priced
   in the repository's units, and says what it forecloses; two or three options; a middle ground only
   when it is real and priced like the others; the recommendation first, with a reason for every option;
   a mockup or a throwaway prototype only for a visual question.
3. **A `decision-review` skill (a):** read first; show the **inventory** of every decision at once, each
   tagged the human's or the agent's (the agent's already decided, one line each); then walk the
   human's decisions **one per turn** (or a theme of up to four, if asked), each by rule (b); recompute
   what each answer settles or reopens; after a long run of accepted recommendations, name the riskiest
   for a second look, and never change a recommendation for anything but a new fact; stop when the
   inventory is empty and the summary is confirmed; write every decision to the repository before any
   plan. The middle ground between "ask together" and "one at a time": **the inventory goes together; the
   decisions go one at a time.**
4. **A `user-walk` skill (c):** actors and goals; the ideal flows; then **every** delay, interruption,
   setback, failure and misuse case listed before any is handled, plus a premortem pass; merge and price;
   where each ends; each one kept becomes a Given/When/Then and a failing test; optionally a second,
   independent walk by a fresh agent; reported as hypotheses, naming the cheapest real check. When the
   owner reports from real use, each observation is reproduced, fixed red-first, swept for its class and
   answered by name.
5. **A table of which installed skill fits which moment**, in the method, with the overrides a carrier
   writes in its `LOCAL.md` (for example: no pull request where the owner's rule says so).

Both skills get a trigger eval in a pilot carrier before they are relied on (fire at least four times in
five on held-out phrasings in the owner's words; misfire at most one in ten), with near misses such as
"execute the plan" and "write tests for this function", and a check that brainstorming does not shadow
`decision-review` on a request to review an existing spec. Cost estimates (an ASSUMPTION until a pilot
measures them): each skill about 1.5k tokens when loaded; a review of six to twelve decisions about as
many turns and ten to twenty-five minutes of the owner's time; a user walk a few thousand tokens per flow.

## 5. What narrows each practice

- A recommendation listed first acts as a default, and defaults are strong; a reason for every option
  is the counterweight, plus a passivity check and a rule against yielding to mood (sycophancy).
- Choice overload is near zero on average and appears under uncertainty or hard tasks: keep two or three.
- A middle option wins partly by position: offer it only when it is real.
- Two evaluators using the same walkthrough method find largely different problems, and imagined users
  are more positive than real ones: a walk produces hypotheses and tests, not evidence about users.
- The premortem's evidence is that imagining a failure as already happened yields more reasons, not
  that it identifies them more accurately; cite the narrower claim.

## References

Each was checked against its source by the research agent; what it supports is in brackets.

- MacLean, Young, Bellotti, Moran (1991). Questions, Options, and Criteria: elements of design space analysis. *Human–Computer Interaction* 6. [(a) the unit of review]
- Gause, Weinberg (1989). *Exploring Requirements: Quality Before Design.* [(a) decide the limbs before the branches]
- Davis, Dieste, Hickey, Juristo, Moreno (2006). Effectiveness of requirements elicitation techniques. RE'06. [(a) structured interviews]
- Cowan (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences* 24. [few open items per turn]
- Johnson, Goldstein (2003). Do defaults save lives? *Science* 302. [narrows (a)]
- Jachimowicz, Duncan, Weber, Johnson (2019). When and why defaults influence decisions: a meta-analysis. *Behavioural Public Policy* 3. [narrows (a)]
- Desiraju, Dietvorst (2023). Reason defaults. *Psychological Science* 34. [(a)/(b) a reason per option]
- Parasuraman, Manzey (2010). Complacency and bias in human use of automation. *Human Factors* 52. [(a) the passivity check]
- Sharma et al. (2023). Towards understanding sycophancy in language models. arXiv 2310.13548. [(a)]
- Tohidi, Buxton, Baecker, Sellen (2006). Getting the right design and the design right. CHI. [(b) several alternatives]
- Dow et al. (2010). Parallel prototyping leads to better design results. *ACM TOCHI* 17. [(b)]
- Carroll (2000). *Making Use: Scenario-Based Design of Human–Computer Interactions.* MIT Press. [(b)/(c)]
- Adzic (2011). *Specification by Example.* Manning. [(b)/(c) examples become tests]
- Wynne (2015). Introducing Example Mapping. Cucumber blog. [(b)/(c) split signals]
- Scheibehenne, Greifeneder, Todd (2010). Can there ever be too many options? *Journal of Consumer Research* 37. [narrows (b)]
- Chernev, Böckenholt, Goodman (2015). Choice overload: a conceptual review and meta-analysis. *Journal of Consumer Psychology* 25. [(b) keep two or three]
- Simonson (1989). Choice based on reasons: attraction and compromise effects. *Journal of Consumer Research* 16. [narrows (b)]
- Cockburn (2000). *Writing Effective Use Cases.* Addison-Wesley. [(c) list every extension before handling any]
- Wharton, Rieman, Lewis, Polson (1994). The cognitive walkthrough method: a practitioner's guide. [(c) four questions per step]
- Kaner (2003). An introduction to scenario testing. [(c) disfavoured users]
- Sindre, Opdahl (2005). Eliciting security requirements with misuse cases. *Requirements Engineering* 10. [(c)]
- Klein (2007). Performing a project premortem. *Harvard Business Review* 85(9); Mitchell, Russo, Pennington (1989). Back to the future. *Journal of Behavioral Decision Making* 2. [(c), and its narrower claim]
- Hertzum, Jacobsen (2001). The evaluator effect. *International Journal of Human–Computer Interaction* 13. [narrows (c)]
- Rosala, Moran (2024). Synthetic users. Nielsen Norman Group. [narrows (c)]
- Nielsen (2012). Thinking aloud: the #1 usability tool. Nielsen Norman Group. [(c) the real-user check]
