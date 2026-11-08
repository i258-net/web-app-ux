---
id: PAT-DT-005
title: Focus management and selection models
type: pattern
scope: desktop
topics: [focus-management, focus-restoration, selection, multi-select, keyboard-selection, dialogs, deletion, aria-selected]
platforms: [desktop, tablet, mobile]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [keyboard, pointer, touch, assistive-tech]
principles: [P-12, P-10, P-04, P-05]
dimensions: [D-08, D-07, D-03]
gates: [QG-001, QG-002, QG-004, QG-005, QG-006, QG-020a, QG-020b, QG-028]
related: [PAT-DT-004, PAT-DT-006, PAT-DT-007, PAT-DT-011, PAT-SH-006, PAT-SH-011, PAT-SH-015]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Focus management and selection models

## Problem

In dynamic apps, the element that has focus keeps disappearing. A dialog closes, a row is deleted, a panel collapses, a list re-renders after a filter. When the focused element leaves the DOM, browsers typically drop focus back to `<body>`. A keyboard or screen-reader user then starts again at the top of the page. A second, related confusion is between **focus** (where the keyboard is), **selection** (which items an action will apply to), and **current/active** (which item the detail pane shows). When these are merged or poorly signaled, people act on the wrong records. These problems are most severe in wide, multi-pane, keyboard-heavy layouts, but they apply at every width.

## Recommendation

**Outcome:** after any change, focus lands somewhere meaningful and nearby. People can always tell which items are focused, which are selected, and which is open.

### Focus transitions

1. **Opening a modal moves focus inside.** Put focus on the first sensible control. For long content, focus a static heading. For destructive confirmations, focus the least destructive option. Tab cycles within the modal while it is open, and Escape closes it. Generic dialog behavior lives in PAT-SH-015.
2. **Closing returns focus to the invoker**, unless the invoker no longer exists or the workflow makes another target more logical, such as the newly created item after "Create".
3. **Deleting the focused item moves focus to a defined neighbor.** Choose the next item, else the previous item, else the list's empty-state action or heading. Define this before building the delete. The same applies to removing a row with an optimistic update and then rolling it back (PAT-DT-006).
4. **Re-rendering preserves focus** on the same logical item when it still exists, after filtering, sorting, pagination, or a live update. Do not let a background refresh steal focus.
5. **Do not move focus just to announce status.** Use live regions for "Saved" or "3 items deleted" (QG-028). Move focus only when the user's next task is at the new location.
6. **Focus must not trigger a context change** (QG-020a). Arrowing through a list may update a preview pane only if that is fast and doesn't navigate the page.

### Selection models

7. **Pick one model per collection and apply it consistently.**
   - *Single-select, selection follows focus.* Arrowing changes the selection. This suits list–detail views with fast, cheap previews.
   - *Single-select, explicit activation.* Arrow keys move focus, and Enter or Space opens the item. Use this when opening is slow or costly.
   - *Multi-select.* Each row has a checkbox (pointer and touch). With the keyboard, Space toggles the focused row without modifiers. Shift+Arrow and Shift+click can extend a range, and Ctrl/⌘+A selects all within the collection's focus. A header checkbox has checked, unchecked, and indeterminate states.
8. **Signal focus, selection, and current differently**, both visually and semantically. For example, a focus ring, a filled checkbox and tint, and an accent bar with `aria-current`. Use `aria-selected` or `aria-checked` as the role requires. Do not rely on color alone.
9. **Make selection scope explicit.** Show the count ("12 selected"). Say whether "select all" means this page or all matching results, and offer to extend it. Clear the selection deliberately: on Escape or a Clear button, never silently on scroll (bulk actions: PAT-SH-006, PAT-DT-011).

## Evidence

- **E3** W3C WAI APG, "Dialog (Modal) Pattern". https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/. Move focus in on open, contain Tab, choose initial focus by content and risk, and return to the invoker unless it is gone or the workflow says otherwise (F-DX-22, F-SP-40).
- **E3** W3C WAI APG, "Developing a Keyboard Interface". https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/. Deleting or closing can lose focus, and moving focus to the next list item is a remedy (F-DX-23). Roving tabindex (F-DX-24).
- **E3** W3C WAI APG, "Listbox Pattern". https://www.w3.org/WAI/ARIA/apg/patterns/listbox/. Single selection may follow focus. The recommended multi-select model lets Space toggle without modifiers, with modifier alternatives documented (F-SP-42).
- **E3** W3C WAI APG, "Tabs Pattern". https://www.w3.org/WAI/ARIA/apg/patterns/tabs/. Activation on focus is recommended only when panels show without noticeable latency (F-SP-39). We extend this to preview panes as an interpretation.
- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines. Row checkboxes with a header checkbox that has an indeterminate state (F-DX-31).
- **E3** Apple Human Interface Guidelines, "Split views". https://developer.apple.com/design/human-interface-guidelines/split-views.md. Keep the selection that leads to the detail view highlighted (F-DX-04).
- **E3** React documentation, "useOptimistic". https://react.dev/reference/react/useOptimistic. The optimistic-delete example restores the item on failure, which implies a focus policy for both removal and restoration (F-DX-28).
- **E1** W3C, WCAG 2.2 SC 2.4.3, 3.2.1, 4.1.3. https://www.w3.org/TR/WCAG22/#focus-order, https://www.w3.org/TR/WCAG22/#on-focus, https://www.w3.org/TR/WCAG22/#status-messages. Focus order, no context change on focus, and status messages announced without moving focus (F-SP-12, F-SP-23, F-SP-32).

WCAG does not specify *where* focus goes after deletion. That guidance is E3 convention.

## Alternatives and tradeoffs

- **Selection follows focus vs. explicit activation.** Follow-focus is fast for skimming mail or files. It is costly if each preview loads slowly or marks items as read. Explicit activation is safer.
- **Checkbox column vs. modifier-click only.** Checkboxes are discoverable and work on touch. Modifier-click alone is invisible to novices and unavailable on touch, so offer it as an accelerator.
- **Focus to heading vs. first control after navigation.** Focusing a heading orients screen-reader users. Focusing the first field speeds up form entry. Choose per view.

## Exceptions and failure modes

- Non-modal panels and drawers should not trap focus. Opening one may move focus into it, but Tab must be able to leave.
- `autofocus` on page load in content pages can disorient screen-reader users.
- Selection lost on pagination with no warning.
- Highlighting the "current" row the same way as "selected" rows.
- Restoring focus to an element hidden under a sticky header (QG-006).

## Evaluation questions

- After closing each dialog, is focus back on the invoker, or on a logically better target? [running app]
- After deleting the focused item, does focus land on a neighbor or the empty state, not on `<body>`? [running app] [automated]
- Do filter, sort, and live refresh keep focus on the same item? [running app]
- Are focus, selection, and current visually distinct without relying on color alone? [screenshot]
- Is selection state exposed (`aria-selected` / `aria-checked`) and announced? [automated] [running app]
- Is the scope of "select all" stated, and is the selection count visible? [screenshot]
- Do screen-reader users keep their place through delete and close actions? [user study]

## Related

- Patterns: [PAT-DT-004](PAT-DT-004-keyboard-navigation-shortcuts.md), [PAT-DT-006](PAT-DT-006-inline-editing.md), [PAT-DT-007](PAT-DT-007-data-tables-grids.md), [PAT-DT-011](PAT-DT-011-expert-workflows.md), PAT-SH-006, PAT-SH-011, PAT-SH-015
- Principles: [P-12](../../principles/P-12-accessibility-inclusion.md), [P-10](../../principles/P-10-feedback-predictability.md), [P-04](../../principles/P-04-navigation-orientation.md), [P-05](../../principles/P-05-cognitive-clarity.md)
- Rubric: [D-08, D-07, D-03](../../rubric/dimensions.md); gates [QG-001, QG-002, QG-004, QG-005, QG-006, QG-020a, QG-028](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
