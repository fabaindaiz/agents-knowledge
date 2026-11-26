---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-5acdb1b0b0
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.37
digest: 8122e08cbd41
kind: knowledge
action: new
target: a-blocked-ui-thread-is-not-only-slow-code
lacks: an occurrence in a carrier; the sources read at abstract or summary level for some boundaries (meta/reviews/2026-11-26-optimisation-cards.md)
seen: "2026-11-26"
---

# Proposal: a-blocked-ui-thread-is-not-only-slow-code

An unresponsive interface is as often a UI thread waiting as one computing: a synchronous call to a slow peer process, a lock held by another thread, a deadlock. Moving the computation off the UI thread, the usual answer, misses those. It stops applying where all the UI thread's work is local. The check: the platform's strict-mode detector and traces of the UI thread's blocked state, not only its CPU time.

## Evidence

A mobile platform's documentation on unresponsive applications (its timeouts and causes).
