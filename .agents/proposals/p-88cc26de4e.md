---
# bundle-proposal: a change this repository offers to the agent-guides bundle. Only the home repository integrates it; nothing here is guidance.
proposal: p-88cc26de4e
bundle: agent-guides
carrier: r-5ed7e8
base: 0.0.33
digest: 3e306398ace8
kind: method
action: extends
target: no-foreign-shell-constructs
lacks: "a check rather than another line of prose: a loop whose body depends on a directory change proves the change inside the body before the first write, and a counted run of whether such a check fires"
seen: "2026-11-24"
---

# Proposal: no-foreign-shell-constructs

A rule the agent itself has just written into the guidance, with the file loaded and read minutes before, is
still broken by that agent when the broken form is the host shell's default. The failing construct is the one
that takes a line of two fields and splits it into two variables: in a shell that does not split an unquoted
expansion, the second variable is empty, every directory change in the loop fails, and every iteration goes on
running in whatever directory the loop started in. Nothing in the loop says so, because each step's own exit
status is zero and the progress line it prints says the step is done. What makes this worse than an ordinary
portability trap is where the loop then writes: a loop meant to touch several repositories in turn touches one
repository several times, and the one it touches is the session's own. The narrow form of the rule is therefore
not "write portable shell" but: a loop whose body depends on a directory change verifies that change inside the
body, before the first command that writes, and a loop that writes in several repositories names each target as
an absolute path rather than carrying it in a variable the shell may split.

## Evidence

One occurrence in one owner's repositories on 2026-11-24, counted as one source, in a release session: the loop
edited and committed a file belonging to the repository it was running in, on its default branch. It was caught
by a push guard that refused the push, not by the loop, not by the agent reading its own output, and not by the
gate; the commit was undone before anything left the machine. The same release's harvest held eight earlier
occurrences of the same family across four carriers, five of them in one carrier **with the rule loaded in that
session**, including a script that executed nothing while reporting success and a checkout that discarded
uncommitted code. This occurrence adds the case the earlier ones did not have: the agent breaking the rule was
the one writing it, in the same session, into the same release. That is direct evidence for the ladder's own
claim that written text is its weakest rung, offered by the author of the ladder failing it. No measurement of
frequency; what is counted is occurrences, not attempts. Literature: the hierarchy-of-controls grounding
consulted for the enforcement ladder at this release, which predicts exactly this ordering — an administrative
control fails at the moment the person it governs is busiest.
