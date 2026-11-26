# How to present the method, and how little is known about it

2026-11-26, at the owner's request, before the project is presented. A delegate researched primary sources
on the web; this home graded what came back. **The headline is a negative result about the research
itself**: there is no controlled evidence for how to present an engineering method. What exists is
documented practice by artefacts that succeeded, plus one old usability study about writing for the web.

Read the recommendations as design heuristics, not as a recipe with evidence behind it. Treating them as
more than that would be the error this repository's principle 6 names.

## What the delegate verified, and what it did not

It read in full: the Twelve-Factor page, the architecture-decision-record post, and the description of one
usability article. **It did not fetch** the version-scheme, changelog-format, commit-convention, diagram-model
or site-reliability sources; those entries rest on the delegate's memory and are marked ASSUMPTION below.
That is recorded because a recommendation resting on an unfetched memory is a weaker thing than one
resting on a page somebody opened, and the difference must not disappear into a tidy list.

## What is actually known

| Claim | Kind of evidence | How strong |
|---|---|---|
| Concise, scannable, objective prose measurably improves task performance on the web | a lab usability study, small samples, from the 1990s, measuring task performance rather than adoption | moderate, and old |
| A method page converts a sceptic better in one shape than another | **nothing found**: no trial, no documented rewrite with figures | none |
| Disclosing a null result helps or hurts adoption | **no direct study found** | none |
| A null result is rated lower in quality, more so when it contradicts expectations | an experiment with several hundred economists, read from a summary | moderate; the audience is academics, not engineers |
| Pre-registration raises perceived trust | the authors of a registered report say there is no empirical evidence for it | pre-registration is for rigour, not persuasion |
| Admitting a limit costs little in source credibility, while too much disclosure hurts | meta-analytic work on two-sided advertising messages, read from summaries; the relation is curvilinear | mixed, and from a different field |
| A documentation split by reader need works | adoption by several large projects, no independent effectiveness study | adoption only |
| Time to a first working result predicts tool adoption | practitioner writing only, no controlled study | opinion |

**The honest summary**: the one measured thing is that shorter, scannable, non-marketing prose is easier
to use. Everything else is practice worth copying because it belonged to things that worked, which is not
the same as knowing it caused them to work.

## What the artefacts that succeeded actually did

From the two pages the delegate read in full, and ASSUMPTION for the rest:

- **The problem comes first, then who should read it, then the rules.** None of them opens with a benchmark
  or a claim of benefit.
- **The authority is stated as experience, not as statistics.** The twelve-factor page says it comes from
  seeing hundreds of applications; it offers no numbers at all.
- **The core is small**, and the page is short.
- **The downside is part of the form.** A decision record's template has a *Consequences* section that lists
  every effect, good and bad; it is not an appendix.
- ASSUMPTION: the version, changelog and commit-convention pages each open with one line of purpose, keep
  the normative part short, and answer objections near the end.

## What this suggests for this project, in order

Each recommendation names what it would change about the page that exists today, which runs: hero, the
problem, the central idea, what you run, the evidence with its nulls, the cost, the obligations, where it
stands, who it is not for, how to adopt.

1. **Put the problem and the audience above the fold, and take the evidence figure out of the opening.**
   The page currently opens with a claim about what the bundle does. The artefacts that worked opened with
   the problem and with who should read. *Basis: the two pages read in full.*
2. **Move the cost and the "not for you" section up, beside the central idea.** A sceptic should meet the
   ×2 and the thin benefit early and by the author's choice, not discover them late. *Basis: the decision-record
   template's consequences; the two-sided-message meta-analysis, which is from another field.*
3. **Write the evidence section in the shape of a decision record**: the claim, the method, the result with
   its interval, what it cannot show, and the decision it supports. Replace every adjective with the number,
   the sample and the limit. *Basis: the decision-record post, read in full.*
4. **Cut it.** One screen per section, no superlatives, the cards on their own page. *Basis: the one measured
   finding in this whole review.*
5. **Split by what the reader came for**: a short adoption path, a reference for the cards, and a longer
   explanation of the method behind them. *Basis: adoption by large projects, no effectiveness study.*
6. **Open the adoption path with the smallest real trial**, its measured token cost, and how to remove the
   bundle again. *Basis: practitioner writing only.*

**What nobody should do with this review**: quote a conversion percentage. The delegate searched for one
and found only vendor blogs. There is no number here that predicts adoption, and inventing one would be
exactly the kind of claim this project exists to refuse.
