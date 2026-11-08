---
id: PAT-RS-005
title: Control positioning — where primary and secondary actions sit per viewport and input
type: pattern
scope: responsive
topics: [primary-action, secondary-actions, toolbar, fab, sticky-action-bar, overflow, reachability, safe-area, focus-obscured]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-06, P-01, P-08, P-09, P-02]
dimensions: [D-03, D-01, D-05, D-10]
gates: [QG-051, QG-006, QG-052, QG-053, QG-040, QG-004]
related: [PAT-MO-002, PAT-MO-010, PAT-MO-011, PAT-RS-003, PAT-RS-009, PAT-RS-002, PAT-SH-008, PAT-DT-008, PAT-DT-011]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Control positioning — where primary and secondary actions sit per viewport and input

## Problem

Actions belong in different places as space and input change. One-handed on a phone, a top-right Save is hard to reach. On a 1440 px window, a full-width sticky bar puts Save far from its form, and a floating action button hovers over a table. Teams pick one placement and stretch it, or move actions per breakpoint without preserving order and labels. The result is a primary action that changes name, position, and meaning across sizes, or disappears into an overflow menu on compact screens.

## Recommendation

**Outcome:** at every size the primary action is visible, labelled, reachable with the likely input, and close to what it acts on. Secondary actions are grouped consistently, and positioning never hides focused content.

1. **Rank actions per screen**: one primary action (the reason the screen exists), a few frequent secondary actions, and occasional actions. Rank by task, not by available space (as in [PAT-RS-003](PAT-RS-003-content-prioritization.md)).
2. **Compact (< 600), touch-capable:**
   - Put the primary action where a thumb reaches it ([PAT-MO-002](../mobile/PAT-MO-002-thumb-reach-primary-action.md)): a full-width button at the end of a short form, a sticky bottom action bar for long forms and checkout, or a floating action button for "create" on a collection screen.
   - Keep 1–2 frequent secondary actions visible; move the rest into a labelled overflow menu (PAT-SH-008).
   - Sticky bars must pad for safe-area insets and must not cover the focused field or the virtual keyboard's target (QG-052, QG-053, QG-006).
3. **Medium (600–839):** keep the primary action near the content it affects. In two-pane layouts, each pane owns its actions: list actions in the list header, item actions in the detail toolbar. A FAB may sit in or beside the navigation rail.
4. **Expanded and wider (≥ 840), any input:**
   - Place actions in a toolbar or header bound to the content region (pane, card, form section), not at the far window edge.
   - Put form submit buttons at the end of the form, aligned with the fields, not in a bar spanning the window.
   - Show more secondary actions inline as space grows, in the same order they had in the compact overflow.
   - Contextual row actions can appear on hover *and* must have a persistent or focus-revealed path ([PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md), PAT-DT-008).
5. **Same identity everywhere.** The primary action keeps its label, icon, and accessible name across positions. An icon-only FAB on compact still has an accessible name that matches its visible label on expanded.
6. **DOM order follows logical order.** A button visually pinned to the bottom with CSS should still come after the fields it submits in the tab sequence (QG-004).
7. **Do not position by width alone for reach.** Reachability matters when a hand-held touch device is used; a narrow desktop window does not need thumb placement, and a tablet in landscape held with two hands may need controls near the side edges. Combine window class with pointer capability, and test real grips.

## Evidence

- **E3** Google, "Material Design 3 — Floating action button". https://m3.material.io/components/floating-action-button — Use a FAB for the screen's most common or important action, persistent while content scrolls; a convention, not a requirement on every screen.
- **E3** Google, "Material Design 3 — Navigation rail". https://m3.material.io/components/navigation-rail — Rails in medium and wider windows can hold an optional FAB.
- **E3** Google, "Material Design 3 — Bottom sheets". https://m3.material.io/components/bottom-sheets — Bottom sheets hold secondary content in compact and medium windows, not the main app content.
- **E3** Apple, "Human Interface Guidelines — Toolbars". https://developer.apple.com/design/human-interface-guidelines/toolbars.md — Toolbars group current-view actions; move lower-priority items to overflow as width shrinks; customization can help iPad/Mac power users.
- **E3** Apple, "Human Interface Guidelines — Tab bars". https://developer.apple.com/design/human-interface-guidelines/tab-bars.md — Tab bars are for navigation, not commands; actions go elsewhere.
- **E3** Apple, "Human Interface Guidelines — Designing for iPadOS". https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados.md — Place controls within easy reach without obstructing content; account for orientation and multitasking.
- **E3** MDN, "env()". https://developer.mozilla.org/en-US/docs/Web/CSS/env — `env(safe-area-inset-*)` exposes safe distances when `viewport-fit=cover` fills the display.
- **E1** W3C, "WCAG 2.2 — 2.4.11 Focus Not Obscured (Minimum)". https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum — Author-created content (e.g. sticky bars) must not entirely hide the focused component.
- **E1** W3C, "WCAG 2.2 — 2.4.3 Focus Order". https://www.w3.org/TR/WCAG22/#focus-order — Focus order preserves meaning and operability.
- **E4** Nielsen Norman Group, "Sticky Headers: 5 Ways to Make Them Better". https://www.nngroup.com/articles/sticky-headers/ — Persistent bars should be small, clearly differentiated, and justified by real need.
- **E4** Nielsen Norman Group, "Mobile First Is NOT Mobile Only". https://www.nngroup.com/articles/mobile-first-not-mobile-only/ — Wide layouts should be optimized for their space rather than enlarged mobile layouts (applied here to action placement; our extension).

*Interpretation (ours):* the "actions bound to their content region on wide windows" rule is inference from Apple toolbar grouping and NN/g's mobile-first-not-only argument. No source here measures action placement on wide web layouts.

## Alternatives and tradeoffs

- **Top-right primary action on compact.** Matches some platform conventions (e.g. "Done" in a top navigation bar) and keeps the bottom free; costs reach on large phones. Acceptable for low-frequency confirmations.
- **Sticky bottom bar at all widths.** Simple and consistent, but on wide windows it separates action from content and costs height; prefer an end-of-form button plus a sticky bar only when the form is longer than the viewport.
- **FAB vs inline "New" button.** FAB suits creation-centric collections on touch; on wide pointer layouts an inline header button is usually closer and less obstructive.

## Exceptions and failure modes

- A FAB covering the last list item or table actions (no bottom padding).
- Primary action moved into overflow at compact width.
- Different labels for the same action at different widths ("Save" vs "Done" vs ✓).
- A sticky action bar that sits under the virtual keyboard or over the focused field.
- Hover-only row actions on a touch-capable expanded layout.

## Evaluation questions

- Is the primary action visible without opening a menu at every supported width? [screenshot] [running app]
- On a hand-held phone, is it reachable one-handed? [prototype] [user study]
- On expanded widths, is each action adjacent to the content it affects? [screenshot]
- Are label and accessible name identical across positions? [automated] [running app]
- With the virtual keyboard open, are the focused field and the submit control visible? [running app]
- Does the tab order reach the submit button after the fields? [running app]

## Related

- Principles: [P-06](../../principles/P-06-interaction-ergonomics.md), [P-01](../../principles/P-01-task-effectiveness.md), [P-08](../../principles/P-08-visual-hierarchy-readability.md), [P-09](../../principles/P-09-consistency-familiarity.md), [P-02](../../principles/P-02-discoverability-learnability.md)
- Dimensions: D-03, D-01, D-05, D-10; Gates: QG-051, QG-006, QG-052, QG-053, QG-040, QG-004
- Patterns: [PAT-MO-002](../mobile/PAT-MO-002-thumb-reach-primary-action.md), PAT-MO-010, PAT-MO-011, [PAT-RS-002](PAT-RS-002-layout-reflow-canonical-layouts.md), [PAT-RS-003](PAT-RS-003-content-prioritization.md), [PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md), PAT-SH-008, PAT-DT-008, PAT-DT-011

## Change log

- 2026-11-08 — Initial version (ADR-001).
