---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-cc00fe80fe
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.37
digest: 8122e08cbd41
kind: knowledge
action: new
target: a-benchmark-measures-what-it-ran
lacks: an occurrence in a carrier; the sources read at abstract or summary level for some boundaries (meta/reviews/2026-11-26-optimisation-cards.md)
seen: "2026-11-26"
---

# Proposal: a-benchmark-measures-what-it-ran

A performance figure measures the configuration and the load that produced it, and two usual setups measure something else: a debuggable, unoptimised or emulated build (and, on a mobile platform, one without its ahead-of-time startup profile), and a closed-loop load generator that waits for each response, which drops the slow samples and reports a tail latency far better than users see. It stops applying to algorithmic comparisons within one configuration, and to clients that really wait. The check: benchmark the shipped configuration with its compilation modes compared, and drive latency tests at a fixed arrival rate from the scheduled send time, against an injected stall, reporting percentiles, never averages. Borders a-check-must-be-seen-to-fail.

## Evidence

A mobile platform's benchmarking and startup-profile documentation (its own figures for the profile); Tene, *How NOT to Measure Latency* (talk, 2013 onward), snippets only.
