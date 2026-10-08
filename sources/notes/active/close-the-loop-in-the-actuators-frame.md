---
slug: "close-the-loop-in-the-actuators-frame"
topic: "time-and-control"
claim: "Measure a feedback loop's error in a frame the actuator moves and the observer's own motion does not, take the target once per input change, and give every threshold inside the loop hysteresis, because a loop comes to rest at its threshold."
confidence: "measured"
phases: ["implement", "debug"]
check: "a probe holding the input at the threshold counts zero mode changes, and applying a correction twice gives the same result as once"
about:
  - {do: "Write a control loop, a follow or steer behaviour, or a threshold that switches a mode", wrong_when: "the error is measured in a frame the loop itself moves, a correction is added to one already applied, or one threshold makes the mode chatter"}
rests_on: "Schmitt 1938, hysteresis"
strength: "foundational"
our_evidence: "measured in two repositories"
cues: ["control loop", "hysteresis", "pid", "chatter", "follow camera", "steer", "threshold switch", "mode change", "deadband", "setpoint", "feedback", "target position", "error correction", "oscillate"]
---

# Close the loop in the actuator's frame

## Why it works

Anything that steers toward a target — an object toward a pointer, a scroll toward a cursor, a controller toward a set point — reduces an error. If the error is measured in a frame that moves with the thing being steered (screen coordinates while the view follows the steered object), acting does not reduce it: the gap stays constant however far it travels, and the loop never arrives. Measured in the frame the actuator changes and the observer does not (world or ground coordinates), each step shrinks the gap and the loop converges.

The target has the same trap in time: re-reading a screen-space target every frame, while the view moves, re-creates the gap each frame. Take it once, when the input changes.

The correction itself moves the frame. A residual measured downstream of a correction already applied is in the corrected frame, so a loop that adds its proposal to the applied correction counts that correction twice, and its proposals grow run after run. Estimate absolute targets and apply them, never increments on increments; state in which frame each residual is measured; and pin it with a test that applying twice gives the same result as applying once. A search window that is right in the raw frame is wrong in the corrected one.

And a loop that converges does not stop anywhere in particular — it stops where the forces balance. With one threshold switching between two behaviours (slow or fast, on or off), that resting point **is** the threshold, and noise flips the behaviour back and forth. Two thresholds — switch up at one, back down at a lower one — give the resting state room.

## When it does NOT apply

- **Open-loop actions** with no feedback: a fixed move, a timed animation.
- **Thresholds crossed once and not revisited** (a one-way state change).
- **When the observer frame is what the user controls** — a pointer-relative UI where the goal is to follow the screen, not the world.

## What it costs

A dead band: between the two thresholds the system keeps its previous behaviour, which can read as lag. Converging to the target also changes behaviour users may rely on — here holding at the edge used to mean travelling indefinitely and became travelling there and stopping, and travelling became a drag.

## Where it came from

One repository, a renderer whose view follows a user-steered object. Steering by a held pointer (2026-09-21): the gap was measured on screen, and because the view was welded to the object, moving it barely changed its screen position, so a gap measured there never closed. Measured in world coordinates, it shrank monotonically with the pointer held still. The target is taken once per pointer position, not per frame, because the moving view would otherwise put the gap straight back. A single threshold between two modes of motion made one object switch modes repeatedly within a couple of seconds; with hysteresis (switch up at one distance, back down at a clearly lower one) the count was **0**. Before the fix an object had also been dragged away from the pointer, a separate leak recorded in `derive-state-from-one-clock`.

## Literature

- **Schmitt, 1938, ["A thermionic trigger"](https://doi.org/10.1088/0950-7671/15/1/305)** (Journal of Scientific Instruments 15, 24–26). The comparator with two thresholds; hysteresis rejects noise on a slowly varying input. *Verified 2026-09-22 against the IOPscience listing and reference summaries.* **What we take:** the hysteresis half. **Where we go further:** the frame-of-reference half — none known as a written rule; it is ordinary control practice that interactive code keeps getting wrong.
- **Positional and incremental (velocity) forms of a controller.** *Named by a carrier, not checked against a source.* A controller can output the absolute actuation or the change to it; the double count above is an incremental correction applied as if it were absolute.
- **Sibling in this base:** `derive-state-from-one-clock` — the other half of time-dependent behaviour; and `a-decoder-that-degrades-to-plausible-output-needs-an-out-of-band-check`, where a residual in the wrong frame made an estimator wrong while it reported itself reliable.

## Evidence

**2026-10-02 — a second repository, the correction's own frame.** In a real-time signal-processing service with a measurement loop, a recalibration loop stored its reference after the delay line, and the controller added the applied delay again: its proposals grew run after run, seen on real hardware and explained later. The rewrite estimates absolute arrivals per channel, and in simulation holds under half a millisecond for an hour at two drift rates. The repository made it a design rule, suggest absolute targets and never corrections on corrections, enforced by a test that applying twice gives the same result. In the same repository a delay estimator's lag bound was right for the raw reference and wrong for the median-shifted one: the same frame error, counted in the decoder note.

**Measured in one repository, at first writing:** repeated mode changes within a couple of seconds with one threshold, none with two; a gap that closed monotonically once measured in world coordinates. **Not measured:** the width of dead band that users stop noticing. The experiment: sweep the lower threshold from the upper one downward in a probe and record mode changes and time-to-arrive at each setting.
