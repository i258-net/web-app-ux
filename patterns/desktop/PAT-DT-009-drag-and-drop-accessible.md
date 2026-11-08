---
id: PAT-DT-009
title: Accessible drag-and-drop — single-pointer and keyboard alternatives (WCAG 2.5.7)
type: pattern
scope: desktop
topics: [drag-and-drop, reorder, move, resize, kanban, wcag-2.5.7, single-pointer, keyboard-alternative, cursor, drop-target]
platforms: [desktop, tablet, mobile]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [pointer, touch, keyboard, assistive-tech]
principles: [P-06, P-12, P-10, P-02]
dimensions: [D-03, D-08, D-07]
gates: [QG-018, QG-001, QG-014, QG-015, QG-028, QG-019]
related: [PAT-DT-003, PAT-DT-004, PAT-DT-005, PAT-DT-008, PAT-MO-007, PAT-SH-011, PAT-RS-009, PAT-RS-010]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Accessible drag-and-drop — single-pointer and keyboard alternatives (WCAG 2.5.7)

## Problem

Dragging is the natural gesture for reordering a list, moving a card between Kanban columns, resizing a pane, or filing an item into a folder. It is also physically demanding. It needs sustained press, precise movement, and release on a small target, often while the page auto-scrolls. People with tremor, limited dexterity, a head pointer, eye-gaze, or voice control may be unable to drag. So may anyone on a trackpad or touchscreen moving a long distance. Many implementations offer *only* dragging. Some add a keyboard mode and assume that is enough. It is not.

## Recommendation

**Outcome:** everything that can be done by dragging can also be done with simple single-pointer clicks or taps, and with the keyboard. Dragging stays available as the fast path.

### Know exactly what WCAG requires

- **SC 2.5.7 Dragging Movements (AA):** every function that uses a dragging movement must also be achievable **with a single pointer without dragging**, unless dragging is essential or the user agent determines the function and the author has not modified it. "Single pointer" means click, tap, or a stylus press: one point of contact, activated without a path.
- **A keyboard-only alternative does *not* satisfy 2.5.7.** A user with a head pointer or touch-only access can't use Space-to-lift and arrows. Pointer users need a tap or click route.
- **SC 2.1.1 Keyboard (A)** *separately* requires keyboard operability. A conforming design needs **both** alternatives, and one button-based UI often provides both, because buttons are keyboard-operable as well.

### Provide the alternatives

1. **Click/tap alternatives (satisfy 2.5.7).** Choose per task.
   - *Reorder:* "Move up" / "Move down" buttons, or a "Move to position…" menu.
   - *Move between containers:* a "Move to…" menu or dialog listing destinations, such as Kanban columns or folders.
   - *Select then place:* tap an item to pick it up, then tap a destination. Show the picked-up state and a Cancel.
   - *Resize:* a numeric input, preset sizes, or increment/decrement buttons. A splitter can have collapse and expand buttons.
   - *Sliders:* clicking a point on the track is a single-pointer alternative.
   Put these in the item's overflow menu (PAT-DT-008) so they are discoverable without clutter.
2. **Keyboard operation (satisfy 2.1.1).** The same buttons and menus work by keyboard. Optionally add a keyboard drag mode: Space or Enter on the handle lifts, arrows move, Space or Enter drops, and Escape cancels and restores the original position. Use APG slider keys for splitters. Announce lift, position ("3 of 8, in Done"), and drop with a live region (QG-028).
3. **Design the drag itself well.**
   - *Before:* a visible handle or grab affordance, with move or grab cursors where meaningful.
   - *During:* the grabbed item is clearly lifted and follows the pointer. Valid drop zones are highlighted and invalid ones refused visibly. A placeholder shows where the item will land. Auto-scroll works near edges.
   - *After:* the item settles into place with clear feedback, and focus stays on the moved item (PAT-DT-005).
   - Allow cancelling by dropping back at the origin or pressing Escape, consistent with pointer-cancellation intent (QG-015).
4. **Make consequential drops recoverable.** Offer undo for moves that change state, such as status, assignee, or folder (PAT-SH-011).
5. **Avoid touch conflicts.** On touch, drags compete with scrolling and browser gestures. Require a handle or a short press-and-hold, and keep tap alternatives prominent (PAT-MO-007).

## Evidence

- **E1** W3C, WCAG 2.2 SC 2.5.7 Dragging Movements. https://www.w3.org/TR/WCAG22/#dragging-movements. A single-pointer non-dragging alternative is required, with the essential and user-agent exceptions. The research summary's interpretation states that keyboard support alone does not satisfy it (F-SP-21, F-DX-17).
- **E1** W3C, WCAG 2.2 SC 2.1.1 Keyboard. https://www.w3.org/TR/WCAG22/#keyboard. All functionality through the keyboard. The exception covers path-dependent input only, not endpoint-based moves (F-SP-08).
- **E1** W3C, WCAG 2.2 SC 2.5.1 Pointer Gestures and 2.5.2 Pointer Cancellation. https://www.w3.org/TR/WCAG22/#pointer-gestures, https://www.w3.org/TR/WCAG22/#pointer-cancellation. Path-based gestures need a single-pointer alternative, and activation must be abortable (F-SP-17).
- **E4** Nielsen Norman Group, "Drag–and–Drop: How to Design for Ease of Use". https://www.nngroup.com/articles/drag-drop/. Recognizable drag cues, standard cursors, grabbed-object feedback, and previews of valid destinations. Dragging can be imprecise or physically hard (F-DX-16).
- **E3** W3C WAI APG, "Slider Pattern". https://www.w3.org/WAI/ARIA/apg/patterns/slider/. Arrow, Home/End, and Page keys for range controls. Some touch AT may not send the needed key events, so offer a numeric alternative (F-SP-46).
- **E1** W3C, WCAG 2.2 SC 4.1.3 Status Messages. https://www.w3.org/TR/WCAG22/#status-messages. Announce move results (F-SP-32).

The keyboard drag-mode key mapping (Space to lift, arrows, Escape) is a common convention and our recommendation. No APG pattern for drag-and-drop was in the research set.

## Alternatives and tradeoffs

- **Buttons only, no dragging.** Fully accessible and simple, but slow for frequent reordering. Acceptable for low-frequency tasks.
- **Move menu vs. up/down buttons.** Up/down is fine for short lists but tedious for long moves. A "Move to position" or destination menu scales better.
- **Pick-up-and-place mode.** Efficient on touch and with switch access, but it adds a mode, which must be visible and cancellable.

## Exceptions and failure modes

- **Essential dragging:** freehand drawing or signature capture, where the path *is* the input. Even then, consider an alternative such as a typed signature, where the task allows one.
- **User-agent dragging:** native text selection or native file drag from the OS. Offering an `<input type="file">` alongside the drop zone is still expected (our interpretation).
- Common failures: keyboard-only alternatives claimed as 2.5.7 conformance; alternatives only in a separate "accessibility mode"; drop zones too small (QG-019); and no announcement of the new position.

## Evaluation questions

- For every drag interaction, can the same outcome be reached by clicks or taps alone, with no dragging? [running app]
- Can the same outcome be reached by keyboard alone? [running app]
- Are the alternatives discoverable from the item itself, for example in its overflow menu? [screenshot]
- During a drag, are valid targets and the landing position shown, and can the drag be cancelled? [running app] [prototype]
- Are lift, move, and drop announced to screen readers? [running app]
- Can a consequential move be undone? [running app]
- On a touchscreen, does dragging conflict with page scroll? [running app]
- Do users with motor impairments complete reorder and move tasks? [user study]

## Related

- Patterns: [PAT-DT-003](PAT-DT-003-hover-tooltips.md), [PAT-DT-004](PAT-DT-004-keyboard-navigation-shortcuts.md), [PAT-DT-005](PAT-DT-005-focus-selection-management.md), [PAT-DT-008](PAT-DT-008-contextual-actions-menus.md), PAT-MO-007, PAT-SH-011, PAT-RS-009, PAT-RS-010
- Principles: [P-06](../../principles/P-06-interaction-ergonomics.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-10](../../principles/P-10-feedback-predictability.md), [P-02](../../principles/P-02-discoverability-learnability.md)
- Rubric: [D-03, D-08, D-07](../../rubric/dimensions.md); gates [QG-018, QG-001, QG-014, QG-015, QG-019, QG-028](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
