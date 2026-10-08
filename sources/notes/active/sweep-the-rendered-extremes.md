---
slug: "sweep-the-rendered-extremes"
topic: "verification"
claim: "Check a visual or layout invariant on the rendered output across the whole configuration matrix — every screen, language, user size, accessibility setting, aspect ratio, moment and sequence of updates — because the extremes break it, and a number derived from the source or measured once goes stale."
confidence: "measured"
phases: ["tests", "review", "verify"]
check: "a gate renders the whole matrix; an over-long string planted in one language fails it and names the control"
about:
  - {do: "Change layout, text, fonts, sizes or anything drawn on screen", wrong_when: "it is checked at the default size, language and aspect, and the extremes are where it breaks"}
rests_on: "pseudolocalization — **practice**; boundary-value analysis — **textbook**"
our_evidence: "measured in one repository; occurrences in others"
cues: ["layout", "font size", "overflow", "long string", "translation", "i18n", "locale", "aspect ratio", "screenshot test", "css", "text truncation", "accessibility", "dark mode", "responsive", "viewport"]
---

# Sweep the rendered extremes

## Why it works

Whether text fits, whether a control stays still, whether a figure is visible — these are functions of content length, the user's chosen size, the viewport and the instant, and they fail at the corners of that space: the longest string in the wordiest language at the largest size on the narrowest screen. A developer looks at the typical case. A number written in a document ("clears it by a few pixels") was true for the configuration it was measured in, and stays in the document after the layout moves.

Rendering every configuration headlessly and asserting geometry on the result — no label shows a raw key, nothing reaches past an edge, the tabs do not move between pages, a line is drawn whole or not at all, a subject is covered less than a budget — makes the invariant a check instead of an impression, and finds the corner before a user does.

The matrix is not only static configuration. **Accessibility settings are an axis**: a setting that zeroes durations (reduced motion) turns a looping animation of zero-length steps into an endless loop, and makes a timed screen that subtracts an authored fade leave early. **So is the state reached by a sequence of updates**: a partial page update applied onto a page that already holds the swapped element can break an invariant no seeded page shows. That axis is seen by listening for the platform's own violation events over exercised flows, not by scanning the templates.

## When it does NOT apply

- **Layout guaranteed by construction** (fixed cells, text that is never user-sized).
- **A matrix too large to enumerate**: sample the extremes on each axis and their combinations rather than every point.
- **Deliberate overflow** — a scrolled list runs off the screen by design; it needs an exemption written in the check, not a silent skip — and the check then reports what it exempted beside what it found (`report-coverage-before-findings`).

## What it costs

A headless renderer in the gate and the time to open every screen in every configuration; an exemption list that must be maintained; covered-fraction measurements that must be re-run whenever what they measure moves.

## Where it came from

A client application drawn on a fixed small canvas, used on a device its developers cannot observe. Sweeping a whole piece at the three user text sizes found a scrolling text column reaching **past both the top and the bottom** of the screen at the largest size; after the fix (a line is drawn whole or not at all) every size fits inside it with a margin. The same sweep showed that a document's claim about how far the column cleared a strip was old: the column overlapped it.

Its interface check opens every screen in each language and fails if a label shows a raw key or passes any edge. Proved by breaking it: an emptied translation cell failed two checks, **one over-long caption failed about ten controls**, and a long hint pushed several controls off the screen. A settings page that quietly grew shifted the tabs and the back button with nothing watching; the check added for it fails with the reserved height and names the page. At the device's real width, **nearly all** text lines fit in two rows at the largest size, which is why the size table was left alone.

The same practice applies to occlusion. Planting decoration across the path of small moving figures left them **covered nearly all the time**; uniform rows gave about 90 %, measured clearings where they stand still about 50 %, against about 30 % with the rows in the figures' own lane removed altogether (what still covers them then is mostly other decoration elsewhere in their band) — at one instant, fully covered became about a third. A pointer drawn inside the figures' own depth band kept a few pixels visible over one figure and none over another.

## Literature

- **Microsoft, ["Pseudolocalization"](https://learn.microsoft.com/en-us/globalization/methodology/pseudolocalization)** (Globalization documentation). Expand strings about 40% — real translations reach "200% or even 400%" — and wrap them in delimiters so truncation is visible, to find layout faults before translating. *Verified 2026-09-22 against the Microsoft Learn page.* **What we take:** test layout with the long case, not the source language. **Where we go further:** assert the geometry on the rendered output, and sweep user sizes, aspect ratios and moments as well as languages.
- **Myers, Badgett & Sandler, [*The Art of Software Testing*](https://doi.org/10.1002/9781119202486), 3rd ed., ch. 4 "Test-Case Design", boundary-value analysis:** "Boundary conditions are those situations directly on, above, and beneath the edges of input equivalence classes and output equivalence classes." *Verified 2026-09-23 against the book.* **What we take:** test on the edges, not in the middle — the rendered extremes are the output-side edges.

## Evidence

**2026-10-03 — a second repository, an app with an on-device test suite and a display whose usable width varies with position.** Sweeps found misfits in 7 sessions over 4 days: about twenty texts past the display edge in the first copy, about ten with uneven rows, a couple of dozen under a stricter one-row rule, several lines from a randomised pool on two rows. Two forms the rule already implies, now stated: **a display assertion is not a fit check** — the framework's "is displayed" passed while a text sat tens of pixels outside the display shape, so fit is the layout box against the real shape; and **count every misfit** — a sweep that stopped at its first misfit hid the size of the problem. Two more wait for a second repository: **done includes the sweep** where the renderer runs only on a device outside the gate (once skipped, and a screen test failed later), and **measure before approval** (lines approved unmeasured were shortened afterwards, and the friction stopped once drafts were swept before they were shown).

**2026-09-28 and 2026-10-04 — two axes beyond static configuration, in two repositories.** In an interactive client, with reduced motion on, a start-screen pulse became an endless loop of zero-length steps (a debug build stops it with an error; whether a release build hangs was not reproduced), and a timed end screen left about an eighth of its time early. The interface validator never opens either screen, so the gate could not see them; a code-review agent found both, and the fix skips the pulse and subtracts the fade that actually ran. In a server-rendered administration panel with a strict content policy (no inline script or style), a second round of a usability walk-through run as real task flows found a policy violation when a job-finished event refreshed a section that already held a form: a front-end library's shipped default copies a style attribute from the old element to the new while settling a swap. The visual sweep over seeded pages never refreshes a page that way, and the template tests read HTML, not what the library does to it. The fix removed the attribute from the library's settle list, with a unit test that parses that configuration, and the sweep now listens for violation events on every page of the exercised flows. The violation event is defined by the W3C Content Security Policy specification, cited from the proposal and *not checked against the source*.

**Measured in one repository:** a text column overflowing both edges before the fix and fitting after; about ten controls failed by one long caption; a small layout shift caught; nearly all lines fitting at the real width; occlusion from nearly 100 % through about 90 % and 50 % to 30 %; a pointer visible over one figure and invisible over another. **Not measured:** how many of these a typical-case review would have caught. The experiment: hand a reviewer the default-configuration screenshots of each defect above and count how many they flag.
