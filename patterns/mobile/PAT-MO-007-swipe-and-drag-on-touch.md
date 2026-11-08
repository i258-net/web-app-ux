---
id: PAT-MO-007
title: Swipe actions, swipe-to-dismiss, and drag reordering on touch
type: pattern
scope: mobile
topics: [swipe, drag, reorder, dismiss, touch-action, scroll-conflict, browser-gestures, overscroll]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, keyboard, assistive-tech]
principles: [P-06, P-11, P-12, P-10]
dimensions: [D-03, D-08, D-07]
gates: [QG-018, QG-014, QG-015, QG-001, QG-030, QG-081]
related: [PAT-MO-006, PAT-MO-010, PAT-MO-011, PAT-DT-009, PAT-SH-011, PAT-SH-006, PAT-RS-009]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Swipe actions, swipe-to-dismiss, and drag reordering on touch

## Problem

On a touch screen, the same finger movement can mean "scroll the page", "swipe this row", "drag this item", "dismiss this sheet", "go back" (browser edge swipe), or "zoom". When a web app adds its own swipe or drag, it competes with all of these. Typical results: vertical scrolling stutters because a list row captures every touch; a sheet dismisses when the user meant to scroll its content; a drag-to-reorder list cannot be scrolled; an edge swipe intended to open a drawer triggers browser back; developers set `touch-action: none` and silently disable pinch-zoom; and the whole interaction is unusable for screen-reader, switch, or keyboard users.

Whether to use a gesture at all, and how to make it discoverable, is PAT-MO-006. Desktop drag-and-drop with pointer feedback is PAT-DT-009.

## Recommendation

**Outcome:** gestures do what users intend, never break scrolling or zoom, can be cancelled before they commit, and every swipe or drag function also works with a single tap and with a keyboard.

**Every gesture has a non-gesture route**

1. **Swipe actions on rows** duplicate actions available in the row's menu or detail view; **drag reorder** has "Move up/down", "Move to…", or a reorder mode with buttons (WCAG 2.5.7 requires a single-pointer non-drag alternative; keyboard alone does not satisfy it).
2. **Swipe-to-dismiss** sheets and cards also have a visible Close/Done and respond to Escape and browser back where appropriate (PAT-MO-011).

**Resolve conflicts with scrolling and the browser**

3. **Constrain axes.** A horizontally swipeable row in a vertical list should claim only horizontal movement: `touch-action: pan-y` on the row lets the browser keep vertical scrolling and pinch-zoom. Commit to the gesture only after movement clearly favours one axis.
4. **Use a drag handle for reordering on touch.** Starting a drag from a dedicated handle (≥ 44 px, PAT-MO-001) or after a long-press leaves the rest of the row free to scroll. Auto-scroll the list when an item is dragged near its edge.
5. **Never use `touch-action: none` on large areas** or the whole page; it can block browser zoom (QG-030). Scope it to the handle or canvas that needs it.
6. **Keep away from screen edges** for custom swipes; edges are where browsers and OSs put back and app-switch gestures.
7. **Control scroll chaining** inside sheets, drawers, and scrollable panes with `overscroll-behavior: contain` so reaching the end of an inner list does not scroll the page behind or trigger pull-to-refresh (support is not universal; treat as enhancement).
8. **Sheets with scrollable content** should dismiss by drag only from the handle/header or when content is scrolled to the top.

**Make it forgiving**

9. **Show progress and the pending action** during the gesture (the row slides, the action label and colour appear, the item lifts) and **commit on release past a threshold**; releasing early cancels (2.5.2).
10. **Use undo, not confirmation,** for recoverable destructive swipes (PAT-SH-011), and avoid full-swipe-to-delete without undo.
11. **Keep gesture handling cheap** so responses stay within interaction-latency targets (QG-081). Animating transforms rather than layout properties is our implementation note, not a finding from the sources below.

Hybrid devices: touch laptops and tablets with trackpads use the same UI with mouse and touch; handle both input types in one implementation and test both (PAT-RS-009).

## Evidence

- **E1** W3C, "WCAG 2.2 — 2.5.7 Dragging Movements, AA". https://www.w3.org/TR/WCAG22/#dragging-movements — Single-pointer non-drag alternative required unless essential.
- **E1** W3C, "WCAG 2.2 — 2.5.1 Pointer Gestures, A". https://www.w3.org/TR/WCAG22/#pointer-gestures — Path-based gestures (including swipe where direction matters) need a non-path alternative.
- **E1** W3C, "WCAG 2.2 — 2.5.2 Pointer Cancellation, A". https://www.w3.org/TR/WCAG22/#pointer-cancellation — Complete on up-event with abort or undo.
- **E1** W3C, "WCAG 2.2 — 2.1.1 Keyboard, A". https://www.w3.org/TR/WCAG22/#keyboard — Keyboard operability unless the function depends on the movement path.
- **E3** MDN, "touch-action" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/CSS/touch-action — Values `auto`, `none`, `pan-x`, `pan-y`, directional pans, `pinch-zoom`, `manipulation`; values combine up to the nearest scrolling ancestor; `none` may block browser zoom, harming low-vision users. Baseline widely available.
- **E3** MDN, "overscroll-behavior" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior — `contain`/`none` prevent scroll chaining and pull-to-refresh-type behaviour; applies to scroll containers. Marked limited availability.
- **E4** Nielsen Norman Group, "Using Swipe to Trigger Contextual Actions". https://www.nngroup.com/articles/contextual-swipe/ — Swipe obscures item identity, triggers unexpected actions, and is inconsistent across apps; keep the affected item identifiable and offer visible alternatives.
- **E4** Nielsen Norman Group, "Drag–and–Drop: How to Design for Ease of Use". https://www.nngroup.com/articles/drag-drop/ — Signifiers, grabbed-object feedback, valid-drop previews; dragging can be imprecise or physically difficult.
- **E3** Apple, "Human Interface Guidelines — Gestures". https://developer.apple.com/design/human-interface-guidelines/gestures.md — Immediate feedback; custom gestures should not conflict with system gestures.
- **E3** Google, "Material Design 3 — Bottom sheets". https://m3.material.io/components/bottom-sheets — Optional drag handle with an accessible 48 dp hit target.
- **E3** Google, "Material Design 3 — Lists". https://m3.material.io/components/lists — Swipeable lists need an alternate route to hidden actions.

*Interpretation (ours):* the axis-locking, handle-start, and edge-avoidance techniques follow from the MDN behaviour and platform conflict guidance; no source here measures their effect.

## Alternatives and tradeoffs

- **Edit/reorder mode** with explicit up/down or drag handles that appear only in that mode avoids gesture conflicts entirely and is easier for AT; it costs a mode switch.
- **Long-press to drag** frees scrolling but is undiscoverable without a hint.
- **No swipe at all** — visible row actions or an overflow button — is often the best choice for low-frequency actions.

## Exceptions and failure modes

- Drawing, signature, and map panning are path-dependent and may be essential; scope `touch-action` to the canvas, not the page.
- Failures: page-wide `touch-action: none`; rows that capture vertical scroll; a sheet that dismisses while its content is being scrolled; a full swipe that deletes with no undo; drag-only reorder; edge-swipe drawers fighting browser back; gesture handlers heavy enough to make scrolling stutter.

## Evaluation questions

- Can every swipe and drag function be done with single taps and with a keyboard? [running app]
- Does vertical scrolling stay smooth over swipeable rows and in sheets? [running app]
- Does pinch-zoom still work everywhere except deliberate canvases? [running app] [automated]
- Can a gesture be abandoned mid-way without effect, and is a destructive swipe undoable? [prototype] [running app]
- Do custom swipes ever trigger browser back or pull-to-refresh by accident? [running app]
- Do participants trigger swipe actions unintentionally while scrolling? [user study]

## Related

- Principles: [P-06](../../principles/P-06-interaction-ergonomics.md), [P-11](../../principles/P-11-error-prevention-recovery.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-10](../../principles/P-10-feedback-predictability.md); Dimensions: D-03, D-08, D-07; Gates: QG-018, QG-014, QG-015, QG-001, QG-030, QG-081 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-MO-006, PAT-MO-010, PAT-MO-011, PAT-DT-009, PAT-SH-011, PAT-SH-006, PAT-RS-009

## Change log

- 2026-11-08 — Initial version (ADR-001).
