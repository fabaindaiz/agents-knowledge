# Long commands in delegated agents: sleep, the stall watchdog, and the hand-off

**Date:** 2026-10-05. **Status:** research on one meta-session's incidents; the wording below is proposed, not
released.

## What stopped the delegates: the machine slept

Every incident lines up, to the second, with the operating system's power log: an idle sleep a couple of minutes
after a delegate ended its turn on a background gate, and a lid-closed sleep on battery right after two gates
started. **Wall-clock timers kept counting while processes were frozen, and fired at the next wake**: a command's
timeout, the background time limit, the harness's stall watchdog. The gate that seemed to "hang under load" spent
its whole limit with the machine asleep; the load (about one and a half to two times the core count) was real but
secondary. The client keeps the machine awake only against idle sleep, and only while it is active.

## What counts as progress for the watchdog

Documented: a delegate whose model request streams nothing for about ten minutes is aborted and reported failed;
the timer resets on each stream event, and a stalled delegate can be resumed by message. Reported in the client's
issue tracker, consistent with what was observed: the timer is deferred while a tool runs, so the exposed window is
the model's *next answer*, not the wait. Printing progress or a sleep loop changes nothing.

## How a delegate should run a long command

- Under the foreground ceiling (ten minutes by default): foreground, with a timeout above its usual time.
- Longer: background with an explicit timeout of about three times its usual time, and the delegate ends its turn
  until notified; never a sleep loop.
- Several delegates with gates: serialise the gates behind one lock per machine (`lockf` on macOS, `flock` on Linux),
  or each delegate stops at *staged, message saved* and the coordinator runs the gates one at a time.
- Some recent versions of the client apply the background time limit (thirty minutes by default, two hours at most)
  to interactive sessions too; later ones apply it only to unattended sessions (the client's changelog says which).
- A subagent's prompt cache lives five minutes, so every longer wait re-reads its whole context uncached; a one-hour
  subagent cache setting pays from the first such wait (a user-settings choice, not a bundle rule).

## Parallel agents and reports

The documented caps are about twenty concurrent subagents per session and teams of three to five recommended; the
gates, not the agents, compete for the machine. Judgement, not sourced: five to eight delegates, one gate at a time
per machine. A harness may refuse a report file written by a delegate (four times in this session; undocumented);
the documented channel is the delegate's final message, which a hook can persist.

## Proposed wording (for the next release, priced in the home's chars/4 estimate)

1. `prompt-bootstrap.md`, a subsection after *Research does not end at Phase 2*, about 470 tokens: a delegate ends in
   a report; three things stop one that does nothing wrong (a machine that sleeps, the stall watchdog, a lost
   hand-off); how to run a gate under and over the foreground ceiling; serialise gates.
2. `meta/method/prompt-sync.md`, one line in *What a meta-session must never do*, about 90 tokens: never leave a long
   meta-session to a machine that may sleep or to gates run in parallel.
3. Three lines in every delegate brief (scratch and done-state; how to run the gate and the lock; the report as the
   final message), about 100 tokens per brief.

## Coordinator's checklist

Before: the machine stays awake (mains power, lid open, a keep-awake held for the session) or the run is attended;
the client's version is known; one scratch directory per delegate; each brief names its done-state, how to run the
gate, the lock and "report in the final message"; gates serialised; five to eight delegates, none of which dispatch
background delegates and then end their turn. While running: a stalled delegate is not a failed task — read its
scratch directory and `git status`, then resume it by message; a delegate silent far past its gate's usual time is
checked first-hand. Closing: every report checked first-hand; each stall, kill and resume logged with its cause.

## Open

The watchdog's exact reset rule (from an issue's code reading); whether stalls happen without sleep at this scale;
the keep-awake renewal rule; what triggers the report-file refusal; whether the stop hook fires on an abort.

## References (fetched 2026-10-05)

Claude Code docs: sub-agents, tools reference, environment variables, interactive mode, hooks, settings reference,
workflows, agent teams, errors, changelog; the Agent SDK's handling of stalled responses; the API's prompt-caching
pricing; Anthropic's write-up of its multi-agent research system; issues in the client's public tracker on the stall
watchdog and background agents; the macOS `caffeinate(8)` and `lockf(1)` manual pages; this session's own
transcripts and the machine's power log (durations and counts only).
