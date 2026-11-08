---
id: PAT-MO-006
title: Gesture discoverability and redundancy with visible controls
type: pattern
scope: mobile
topics: [gestures, discoverability, hidden-interactions, accelerators, onboarding, coach-marks, motion]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, keyboard, assistive-tech]
principles: [P-02, P-12, P-06, P-09]
dimensions: [D-03, D-08]
gates: [QG-014, QG-017, QG-018, QG-001, QG-015]
related: [PAT-MO-007, PAT-SH-008, PAT-SH-013, PAT-SH-011, PAT-DT-008, PAT-DT-009, PAT-RS-009]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Gesture discoverability and redundancy with visible controls

## Problem

Gestures — swipe, long-press, pinch, double-tap, edge swipe, shake — have no visible signifier. Users who do not already know a gesture exists will not find the function behind it. Teams nonetheless hide core functions behind gestures to save space, then add a tutorial carousel to explain them. Gestures also exclude: many people using screen readers, switch access, voice control, a mouse, or a keyboard cannot perform them, and some motor impairments make path-based or multi-finger gestures impractical. On the web, custom gestures can also collide with gestures the browser or OS already owns.

The mechanics of swipe and drag (thresholds, scroll conflicts, browser gestures) are in PAT-MO-007; this pattern covers *whether and how users can find and avoid* a gesture.

## Recommendation

**Outcome:** every function is reachable through a visible, labelled control; gestures are optional accelerators that experienced users can adopt and everyone else can ignore.

1. **Visible control first.** Every gesture-triggered function also has a visible route: a button, a row action, or an item in an overflow menu (PAT-SH-008). Swipe-to-delete has a Delete in the row's menu; pinch-zoom on a map has + and − buttons; pull-to-refresh has a Refresh control or automatic refresh (PAT-MO-010).
2. **Use familiar gestures with familiar meanings.** Prefer standard platform gestures (scroll, tap, swipe a carousel, pinch on maps or images). Do not give a well-known gesture a surprising meaning, and keep a gesture's meaning consistent across the app.
3. **Single-pointer, non-path alternatives are required** for multipoint or path-based gestures (WCAG 2.5.1, QG-014), and **non-drag alternatives** for dragging (2.5.7, QG-018). Keyboard operability is separately required (2.1.1, QG-001).
4. **Never rely on device motion alone** (shake to undo, tilt to scroll); provide UI controls and let users disable motion actuation (2.5.4, QG-017).
5. **Teach in context, sparingly.** If a gesture is a real time-saver, reveal it where it applies: a brief hint after the user performs the slower route, a partial "peek" animation on first view of a swipeable row, or a tip that can be dismissed and does not reappear. Avoid up-front tutorial decks (PAT-SH-013).
6. **Give immediate feedback** as a gesture begins (the row moves, the action label appears) so users understand what will happen and can cancel before release (2.5.2, QG-015).
7. **Do not override browser or OS gestures** such as edge-swipe back, pull-to-refresh, pinch-zoom, or system bars, unless the replacement is clearly better and the original remains available (PAT-MO-007, PAT-MO-009).
8. **Make destructive gestures recoverable** with undo (PAT-SH-011).

Touch gestures also appear on tablets and touch laptops, where pointer and keyboard users share the same UI; detect capabilities rather than assume touch from width (PAT-RS-009, PAT-DT-008).

## Evidence

- **E1** W3C, "WCAG 2.2 — 2.5.1 Pointer Gestures, A". https://www.w3.org/TR/WCAG22/#pointer-gestures — Multipoint or path-based gestures need a single-pointer, non-path alternative unless essential.
- **E1** W3C, "WCAG 2.2 — 2.5.4 Motion Actuation, A". https://www.w3.org/TR/WCAG22/#motion-actuation — Motion-operated functions need UI alternatives and must be disableable.
- **E1** W3C, "WCAG 2.2 — 2.5.7 Dragging Movements, AA". https://www.w3.org/TR/WCAG22/#dragging-movements — Dragging needs a single-pointer non-drag alternative; keyboard support alone does not satisfy it.
- **E1** W3C, "WCAG 2.2 — 2.5.2 Pointer Cancellation, A". https://www.w3.org/TR/WCAG22/#pointer-cancellation — Activation on up-event with abort or undo.
- **E4** Nielsen Norman Group, "Using Swipe to Trigger Contextual Actions". https://www.nngroup.com/articles/contextual-swipe/ — Poor discoverability, unexpected actions, and inconsistent swipe meanings in mobile apps; familiarity with swipe-to-delete does not make unrelated swipe commands discoverable. Observations mainly from native apps.
- **E4** Nielsen Norman Group, "Flexibility and Efficiency of Use". https://www.nngroup.com/articles/flexibility-efficiency-heuristic/ — Accelerators such as gestures speed experts, but an interface relying only on them is harder to learn.
- **E2** Nielsen Norman Group, "Mobile Tutorials: Wasted Effort or Efficiency Boost?". https://www.nngroup.com/articles/mobile-tutorials/ — Between-subjects study, 70 users, 4 simple iPhone apps: deck-of-cards tutorials gave no significant task-success or time benefit and viewers rated tasks harder. Does not test contextual hints.
- **E3** Apple, "Human Interface Guidelines — Gestures". https://developer.apple.com/design/human-interface-guidelines/gestures.md — Prefer familiar standard gestures, give immediate feedback, provide alternatives (voice, keyboard, Switch Control), keep visible navigation alongside shortcut gestures, avoid conflicts with system gestures.
- **E3** Google, "Material Design 3 — Lists". https://m3.material.io/components/lists — Swipeable lists need an alternate route to hidden actions, such as a More control.
- **E4** Nielsen Norman Group, "Contextual Menus: Delivering Relevant Tools for Tasks". https://www.nngroup.com/articles/contextual-menus/ — Hidden triggers may go undiscovered; provide another route to the same commands.
- **E4** W3C, "Mobile Accessibility" (2015 draft). https://www.w3.org/TR/mobile-accessibility-mapping/ — Recommends simple gestures and touch/keyboard alternatives to device manipulation.
- **E5** Mobbin, "Mobile Pull To Refresh Screens". https://mobbin.com/explore/mobile/screens/pull-to-refresh — Gesture recurs in shipped apps; discoverability and alternatives not demonstrated.

## Alternatives and tradeoffs

- **Gesture-primary apps** (photo viewers, maps, drawing, games) legitimately centre on gestures because the gesture *is* the task; WCAG's "essential" exception may apply to genuinely path-based input (signatures, drawing), but zoom and pan still need button alternatives.
- **Hints vs no hints.** In-context hints aid discovery but add noise and can annoy repeat users; show once and remember dismissal.
- **Long-press menus** are a common accelerator on touch; treat them like right-click on desktop — never the only route (PAT-DT-008).

## Exceptions and failure modes

- Signature capture and freehand drawing are path-dependent by nature; still offer alternatives for everything around them (clear, undo, submit).
- Failures: delete or archive available only by swipe; carousel advanced only by swipe without visible arrows or pagination controls; shake-to-report with no menu equivalent; an edge-swipe drawer that hijacks browser back; a tutorial deck as the only explanation; swipe direction meaning different things on different screens.

## Evaluation questions

- List every gesture in the app: does each have a visible, labelled equivalent? [prototype] [running app]
- Are multipoint/path gestures, dragging, and motion each paired with the required alternative? [running app]
- Is each function operable with keyboard and with a screen reader on touch? [running app]
- Do custom gestures conflict with browser back, pull-to-refresh, or zoom? [running app]
- Without instruction, do participants complete tasks that have gesture shortcuts? Do they discover the shortcut later? [user study]

## Related

- Principles: [P-02](../../principles/P-02-discoverability-learnability.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-06](../../principles/P-06-interaction-ergonomics.md), [P-09](../../principles/P-09-consistency-familiarity.md); Dimensions: D-03, D-08; Gates: QG-014, QG-017, QG-018, QG-001, QG-015 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-MO-007, PAT-SH-008, PAT-SH-013, PAT-SH-011, PAT-DT-008, PAT-DT-009, PAT-RS-009

## Change log

- 2026-11-08 — Initial version (ADR-001).
