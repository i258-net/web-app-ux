---
id: PAT-DT-003
title: Hover affordances, hover-revealed actions, tooltips, and cursors
type: pattern
scope: desktop
topics: [hover, tooltips, cursor, affordance, hover-reveal, popover, mega-menu, wcag-1.4.13]
platforms: [desktop, tablet]
viewports: [medium, expanded, large, extra-large]
inputs: [pointer, keyboard, touch, assistive-tech]
principles: [P-02, P-06, P-10, P-12]
dimensions: [D-03, D-06, D-08]
gates: [QG-012, QG-041, QG-042, QG-005, QG-006, QG-016, QG-020a]
related: [PAT-DT-002, PAT-DT-007, PAT-DT-008, PAT-RS-009, PAT-RS-011, PAT-SH-008, PAT-SH-014]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Hover affordances, hover-revealed actions, tooltips, and cursors

## Problem

With a mouse or trackpad, hover is a cheap channel. It can confirm that something is interactive, preview a label, or reveal row actions without clutter. The same channel fails keyboard users, touch users (including on wide tablets and touchscreen laptops), screen-magnifier users who can't keep the pointer still, and anyone who doesn't know to look. Common failures: essential instructions only in a tooltip, row actions that never appear on touch, flyout menus that vanish when the pointer crosses a gap, and tooltips that cover the content you are trying to read and can't be dismissed.

## Recommendation

**Outcome:** hover makes pointer use faster and more confident, and nobody needs it to complete a task.

1. **Immediate feedback, delayed disclosure.** Show hover and pressed states on interactive elements promptly, and use the conventional cursor (pointer for links, text for editable text, move or resize handles where relevant). Delay content that pops out and covers other content (flyouts, mega menus, previews) until the pointer dwells. Crossing a target does not signal intent. Tune the delay in testing. No universal millisecond value is sourced here.
2. **Never put essential content only in a tooltip.** Labels, requirements, errors, and prices stay visible. Tooltips hold brief supplementary help or the name of an icon-only control. For touch, provide a deliberate tap-to-reveal help control instead of a hover tooltip.
3. **Every hover trigger is also a focus trigger.** Content that appears on hover also appears when the trigger receives keyboard focus. Escape dismisses it, and focus stays on the trigger.
4. **Meet WCAG 1.4.13 for author-built hover and focus content.** It must be **dismissible** without moving pointer or focus (Escape). It must be **hoverable**, so the pointer can move onto it without it closing, which means no gap that closes the panel. It must be **persistent** until the trigger is removed, the user dismisses it, or it is no longer valid. Do not auto-hide on a timer.
5. **Hover-revealed actions need focus and no-hover fallbacks.** If row actions appear on hover, they also appear when the row or any control in it has focus. They show permanently when hover is unavailable. Detect that with `@media (hover: none)` / `(any-hover: none)` or pointer events, never from viewport width (QG-042, PAT-RS-009). The most important action, or an overflow "…" button, should be visible at all times (PAT-DT-008).
6. **Icon-only controls get an accessible name and a visible label on hover/focus.** The tooltip text should match the accessible name (QG-016).
7. **Do not change context on hover or focus.** Hovering or focusing must not navigate, submit, or open a modal (QG-020a).

## Evidence

- **E1** W3C, WCAG 2.2 SC 1.4.13 Content on Hover or Focus. https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus. Dismissible, hoverable, persistent, with stated exceptions (F-SP-07, F-DX-14).
- **E1** W3C, Media Queries Level 4 §§7.1–7.3. https://www.w3.org/TR/mediaqueries-4/. `hover` / `any-hover` and `pointer` / `any-pointer` describe input capability, and fine and coarse pointers can coexist (F-DX-47). This is a Candidate Recommendation Draft.
- **E4** Nielsen Norman Group, "Tooltip Guidelines". https://www.nngroup.com/articles/tooltip-guidelines/. Tooltips are brief and supplementary, never essential, and reachable by mouse hover and keyboard focus. Touch needs a click/tap popup tip (F-DX-13, F-NB-31).
- **E4** Nielsen Norman Group, "Timing Guidelines for Exposing Hidden Content". https://www.nngroup.com/articles/timing-exposing-content/. Distinguishes immediate hover feedback from delayed disclosure and says crossing a target is not intent (F-DX-11).
- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines. Row overflow menus are persistent by default. The optional hover mode also reveals on focus and stays persistent without hover (F-DX-12).
- **E4** W3C WAI APG, "Tooltip Pattern". https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/. Escape dismisses and focus stays on the trigger. The pattern is labeled work in progress (F-SP-45).
- **E3** Apple Human Interface Guidelines, "Pointing devices". https://developer.apple.com/design/human-interface-guidelines/pointing-devices.md. Pointer interaction supplements touch on iPad, and hover feedback should be predictable (F-DX-52, F-SP-63).

The overall strength is "strong" because the core rule rests on E1, and E3 and E4 sources agree with it. Timing values are not established.

## Alternatives and tradeoffs

- **Always-visible actions vs. hover-reveal.** Visible actions are discoverable and work for every input, but they add visual noise to dense tables. Hover-reveal reduces noise for pointer users but costs discovery. A middle ground is to show one primary action and a "…" button permanently and reveal the rest on hover or focus.
- **Tooltips vs. inline help vs. toggletips.** Inline help is best when most users need the information. A click-to-open toggletip works for all inputs and avoids the hover timing problem. Hover tooltips are fine for naming icons.
- **Hover-opened vs. click-opened menus.** Click-to-open is more predictable, works on touch, and avoids accidental opening. Hover-opening a mega menu can be faster but needs dwell delay, a hoverable path, and a click alternative.

## Exceptions and failure modes

- Browser-native `title` tooltips are user-agent controlled and outside 1.4.13. They are not keyboard- or touch-accessible, so do not rely on them.
- Error messages that appear on hover may be exempt from the dismissible requirement, but they should still be visible without hover.
- Hiding controls with `display:none` until hover, which removes them from the keyboard Tab order.
- Tooltips that cover the focused control or nearby content needed to continue (relates to QG-006).
- Treating `@media (min-width: 1024px)` as meaning "has hover".

## Evaluation questions

- With hover disabled (touch device or `any-hover: none` emulation), is every action and piece of essential information still reachable? [running app]
- Does each hover-triggered panel also open on keyboard focus? [running app]
- Can each panel be dismissed with Escape without moving focus? Can the pointer move onto it? Does it stay open without a timer? [running app]
- Do any tooltips hold required instructions, constraints, or errors? [screenshot] [prototype]
- Are hover and pointer behaviors gated by capability queries rather than width breakpoints? [automated]
- Do cursors match the affordance (pointer, text, move, resize)? [running app]
- Do new users find hover-revealed row actions without being told? [user study]

## Related

- Patterns: [PAT-DT-002](PAT-DT-002-sidebar-hierarchical-navigation.md), [PAT-DT-007](PAT-DT-007-data-tables-grids.md), [PAT-DT-008](PAT-DT-008-contextual-actions-menus.md), PAT-RS-009, PAT-RS-011, PAT-SH-008, PAT-SH-014
- Principles: [P-02](../../principles/P-02-discoverability-learnability.md), [P-06](../../principles/P-06-interaction-ergonomics.md), [P-10](../../principles/P-10-feedback-predictability.md), [P-12](../../principles/P-12-accessibility-inclusion.md)
- Rubric: [D-03, D-06, D-08](../../rubric/dimensions.md); gates [QG-005, QG-006, QG-012, QG-016, QG-020a, QG-041, QG-042](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
