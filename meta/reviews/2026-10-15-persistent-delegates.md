# Persistent delegates — what the harness actually offers, and what the method should say

**Research for `i-5ed7e8-d6ecfe`, 2026-10-15.** Delegated to a cheaper model (about 55k tokens, one
minute) and reviewed here. Read before the design round; nothing here is method text yet.

## The finding that changes the question

**A delegate does not stay open.** A subagent's run ends; a later message **resumes** it under the same
id, with its transcript. So the design question is not "an agent kept open" but **warm resume against
fresh spawn**, and the method should be written in those words — otherwise it promises a process that
does not exist.

What the host's own reference states (verified at the source): a finished delegate stays addressable by
id or name; a resume starts a new run with its tool set, model and effort; its transcript lives in its
own file, untouched by the main session's compaction, and survives a restart of the same session;
transcripts are deleted after the configured retention. A delegate stopped by hand is **not** resumable,
and a message to it is refused. A name that now points at a newer agent is refused rather than delivered
to the wrong one. A delegate **auto-compacts** when it fills its own context, which is lossy, and a turn
cap ends a run with partial output that can be resumed.

## The economics, which decide the rule

The cache is an exact-prefix match, and **a subagent's requests get a short cache lifetime by default
(minutes), while the main conversation gets an hour on a subscription**. A resume inside that window pays
the accumulated history at the read rate, a small fraction of base input. A resume **after** it
reprocesses the whole accumulated history uncached, and then writes it again — which can cost more than
a fresh delegate with a short brief. The history grows with every task, so a long-lived delegate becomes
steadily more expensive per task. Our own agent definitions already set a cache lifetime explicitly,
which is the lever this rule would use.

## When warm wins, when fresh wins

Warm wins where the delegate's accumulated reading is the asset and the next task arrives within the
cache window: iterative review of one module, a verifier re-run after each fix, a research thread
queried repeatedly. Fresh wins for unrelated tasks, after a long gap, once the history is large or has
been compacted, when the instruction has materially changed, and whenever a clean second opinion is the
point of the delegation.

## What a multi-task brief needs that a one-task brief does not

Inferred, not documented: the delegate's own name as its handle; the rule that each message supersedes
earlier ones, and that a superseded instruction must be acknowledged in the next report; a re-read rule,
because its context is a snapshot while the files move; the scratch path where it leaves state **so a
fresh replacement can take over** — the disk, not the transcript, is the durable hand-off; a report
shape per task with an end marker; a budget, a turn cap and a close condition the caller states, rather
than simply stopping; and the key rules restated in each task message, because auto-compaction may have
dropped the brief.

## Failure modes

Documented: the lossy auto-compaction, the refusal on a reused name, and a roster of siblings that is a
snapshot taken at start, so later agents are missing from it. Reported by practitioners but **not** in
the reference: a stall watchdog that cuts a waiting delegate, with figures that disagree between reports
(about ten minutes in some, a shorter stream-idle limit in others) and reports of kills during active
generation. The consequence for the method is the same whichever figure is right: **a delegate that
waits should end its run and be resumed, never block.** Unverified: whether tool state (a background
job, a server connection) survives a resume — assume it does not until tested; and whether a resumed
delegate receives the host's file-change notices.

## What a check could verify

Every message to a delegate resumed an agent not stopped by hand; each delegate has a recorded close;
each multi-task brief names its scratch directory, its handle and its close condition; the gap before
each resume is recorded against the cache window; and each superseded instruction has an acknowledgement
in a later report.

## What this still lacks

A measurement of our own: two delegations of the same task shape, one warm and one fresh, with their
token counts. The canonical literature on long-lived workers (supervision trees, blackboard systems, the
actor model) was **not** read; it is named only so the design round can decide whether it is worth the
hour. Nothing above rests on it.
