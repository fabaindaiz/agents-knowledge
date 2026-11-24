---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-7b6ae101bc
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.33
digest: c6da08a56637
kind: knowledge
action: new
target: classify-shipped-code-by-who-runs-it
lacks: the running measure itself, each command traced to the session that invokes it; a second owner's bundle, since both counts are of one; and the literature on reachable-versus-used
seen: "2026-11-24"
---

# Proposal: classify-shipped-code-by-who-runs-it

A tool shipped to every consumer of a bundle carries the producer's own commands, and the usual way of asking
which is which gives the wrong answer. Classifying a command by **who names it** — which document mentions it —
says everything is the consumer's, because the producer's own procedures are themselves documented in files the
consumer receives and reads. The question that separates the two is **who runs it**: a command whose every real
invocation happens in a session that already has the producer's repository open is the producer's, however many
shipped files describe it. The practical consequence is that the producer's code should live in a file of its
own, outside what travels, rather than inside the one artefact every consumer must carry, check and keep in
step. That split also makes the remaining tool smaller to read and simpler to reason about, and it gives the
producer's half somewhere to grow without charging every consumer for it.

## Evidence

Counted twice, independently, in one owner's repositories on 2026-11-24, over a shipped tool of about five
thousand lines that is roughly a quarter of the whole shipped artefact. By the naming measure both passes agreed:
none of twenty-five subcommands is named only by a producer-side file, so the naming measure says there is
nothing to move. The second pass then observed that several commands are written for the producer's own
procedure, and bounded their exclusive code at roughly four to six per cent of the file, with wide uncertainty,
and separately found about five per cent of the file unattributable to any command by a call graph — neither
shared nor exclusive, simply unreached. So the naming measure returned a confident zero where the running measure
suggests a real figure, which is the finding: a classification that is cheap and mechanical can be confidently
wrong about the thing it is asked. No measurement of the running figure itself: what would settle it is each
command traced to the session that invokes it. Literature: none consulted; what to read is dead-code and
feature-usage analysis, which distinguishes reachable from used and has the same trap.
