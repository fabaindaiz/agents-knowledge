# Timing in the gate: thresholds, hangs, and load from parallel agents

**Date:** 2026-10-05. **For:** `ratchet-in-a-pinned-environment` and principle 18. **Status:** research; the wording
below is proposed for the owner's approval at the next release.

## Findings

- **Timing is a leading cause of flaky tests:** asynchronous waits are the largest class of fixes (Luo et al., FSE
  2014; a fixed sleep lengthened is the commonest bad fix); timeouts caused most flaky failures in a large industrial
  suite, and a statistically set timeout cut them sharply (Berndt et al., ICSE-SEIP 2024); about half of flaky tests
  are resource-affected, CPU most of all (Silva et al., 2023).
- **Speed checks belong outside the correctness gate** (a database vendor's CI: Daly et al., ICPE 2020 — a static
  threshold gave false positives and missed small regressions; change-point detection over history replaced it).
  Instruction counts repeat to many digits where wall time barely repeats to one (SQLite's measurement page).
- **Valid timing needs A/A calibration and alternating test and control on one machine** (Laaber et al., EMSE 2019;
  the randomised multiple interleaved trials method of Abedi & Brecht, ICPE 2017).
- **A timeout detects a hang; it does not measure** (pytest-timeout's own documentation; size-class timeouts in
  Bazel, which also tell the local scheduler not to overload the machine).
- **Pilot on one laptop** (the home's `verify` as the gate, CPU burners standing in for other agents, conditions
  interleaved): wall time about ×2 with half the cores busy, ×2.6 with all busy, ×4 with twice as many busy processes
  as cores; every loaded run exceeded a 1.5× threshold set unloaded, and one unloaded run did too, because other
  sessions pushed the ambient load up; CPU time rose about ×1.6, so it is not a safe unit on heterogeneous cores
  either; the unloaded time drifted by a factor of two within minutes.

## Proposed wording (next release)

1. **The note's threshold paragraph:** the toolchain of a threshold is the whole machine and whatever else runs on
   it; a threshold in the gate is counted in a unit no machine changes, or made relative within one run (variants
   alternated in one window), or moved to a measurement job that repeats, reports an interval and is checked by an
   A/A run; a number kept per environment carries the environment's identity *and its load*.
2. **Its *When it does NOT apply*:** a dedicated pinned measurement machine; and a timeout is not a threshold.
3. **Principle 18, one paragraph (about 190 words):** a test in the gate asserts behaviour, never speed; a wait waits
   for its condition, never a fixed sleep; a timeout detects a hang, set about ten times above the normal time,
   enforced from outside the test, printing the stacks; a test found red on the untouched base gets the strict mark,
   not a sentence in the commit message.
4. **Optional, one line in the bootstrap's step 4:** when several sessions share a machine, the gate's workers are
   sized for its share, and a timing failure is reported with the load it ran under.

## Remedies, priced (minimum per carrier: R1, R2, R7, R9, R10 — about an afternoon)

R1 a per-test timeout as a hang detector (minutes); R2 a whole-gate supervisor timeout that prints load and CPU time
(under an hour); R3 a count instead of wall time (hours per test); R4 a relative assertion within one run (about an
hour per test); R5 speed checks moved to a measurement job with history (about a day); R6 a per-environment baseline
with its load recorded (about an hour); R7 wait for the condition, not a sleep (minutes); R8 load-aware sharing —
workers sized to the session's share and a machine-wide lock for heavy gates (about an hour); R9 record the load with
every gate run and rerun a timing failure once on a quiet machine, reported (minutes); R10 quarantine with a limit as
a strict expected failure (minutes); R11 shake a new timing-sensitive test under load before admitting it (minutes).

## Open

One machine and one CPU-bound gate; the carrier's hang is not diagnosed (starvation, a deadlock load exposed, or
memory); whether agent harnesses launch commands at a lower priority; minimum versus median under agent load.

## References (opened 2026-10-05 unless marked)

Luo et al., FSE 2014; Parry et al., TOSEM 2021; Eck et al., ESEC/FSE 2019 (via Parry); Silva et al. 2023 (arXiv
2310.12132); Berndt, Baltes & Bach, ICSE-SEIP 2024; Micco 2016 and Listfield 2017 (Google Testing Blog); Fowler 2011;
Laaber, Scheuner & Leitner, EMSE 2019; Abedi & Brecht, ICPE 2017 (abstract); Kalibera & Jones, ISMM 2013; Chen, Revels
& Edelman 2016 (arXiv 1608.04295); Mytkowicz et al., ASPLOS 2009 (abstract); Daly et al., ICPE 2020; SQLite's CPU
measurement page; pytest-timeout and pytest-xdist documentation; Bazel's test encyclopedia; GNU make's manual.
