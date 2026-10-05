---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-8de6fcd6f2
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.27
digest: 6e4d974b1cce
kind: method
action: new
target: long-gates-run-where-a-watchdog-cannot-stop-them
lacks: a second occurrence
seen: "2026-10-05"
---

A delegated agent that runs a long gate in the background and waits on it can be killed by the harness's stall watchdog, leaving its commit undone and its state described only in its scratch files. Long gates the commit depends on run in the foreground with progress, or in the coordinator; a brief asks for the report in the final message, since a harness may refuse report files written by subagents.

## Evidence

In one meta-session a delegate waiting on a five-minute gate was stopped after ten minutes without progress; the coordinator re-ran the gate chained on the pending commit from the delegate's saved message. Three delegates in the same session had report files refused by the harness and returned their reports as text.
