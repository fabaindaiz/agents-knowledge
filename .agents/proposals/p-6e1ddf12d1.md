---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-6e1ddf12d1
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.37
digest: 8122e08cbd41
kind: knowledge
action: new
target: kernel-memory-defaults-are-trade-offs
lacks: an occurrence in a carrier; the sources read at abstract or summary level for some boundaries (meta/reviews/2026-11-26-optimisation-cards.md)
seen: "2026-11-26"
---

# Proposal: kernel-memory-defaults-are-trade-offs

Transparent huge pages and memory overcommit are trade-offs, not settings to switch on or off by reflex: huge pages with always-defrag stall the allocating thread in reclaim and compaction, and strict overcommit makes allocations fail where the default lets the out-of-memory killer act. It stops applying with huge pages limited to regions that ask for them, the default defrag setting. The check: the kernel's huge-page fault and fallback counters and its compaction stalls, before and after, per workload.

## Evidence

The kernel's memory-management documentation on transparent huge pages and overcommit accounting (summaries; it gives mechanisms, not magnitudes).
