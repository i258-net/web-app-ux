---
id: PAT-SH-006
title: Selection and bulk actions
type: pattern
scope: shared
topics: [selection, multi-select, bulk-actions, select-all, checkboxes, batch-operations]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-01, P-10, P-11, P-12]
dimensions: [D-01, D-07, D-08]
gates: [QG-001, QG-008, QG-019, QG-028, QG-025]
related: [PAT-DT-005, PAT-DT-007, PAT-DT-011, PAT-SH-011, PAT-SH-008, PAT-MO-007, PAT-SH-016]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Selection and bulk actions

## Problem

Acting on many items at once saves effort, but selection is easy to get wrong:

- Users cannot tell which items are selected, or whether "select all" means this page or every match.
- Focus and selection are confused, so moving the keyboard silently changes what an action will hit.
- Selection is hidden behind gestures that touch, keyboard, or assistive-technology users cannot discover.
- A bulk action runs on a different set than the user believes it affects.
- The cost of a mistake grows with the number of items.

## Recommendation

**Outcome:** users can see exactly which items an action will affect, select and deselect by any input method, and recover from a bulk mistake.

1. **Use explicit selection controls.** Use a checkbox per item for multi-select, plus a header "select all" checkbox with checked, unchecked, and **indeterminate** (partial) states. Radios or a selected-row style suit single selection.
2. **Keep selected distinct from focused, hovered, and opened.** Each needs its own visual treatment and programmatic state (`aria-selected` or `aria-checked`). Selected state needs more than color, and its indicator needs at least 3:1 contrast against adjacent colors (QG-008).
3. **Define the scope of "select all".**
   - State it ("All 25 on this page selected").
   - When more items match, offer "Select all 1,240 matching items" explicitly.
   - Decide whether selection survives paging, filtering, and sorting, and say so. Selection silently persisting onto hidden items is a common source of bulk errors.
4. **Show a selection mode with a count and an exit.** When one or more items are selected:
   - reveal a bulk action bar that names the count ("3 selected") and offers the available actions and a clear "Cancel" or "Clear selection";
   - announce count changes as a status message (QG-028);
   - suspend per-row actions that would conflict with the batch.
5. **Make every selection method operable by keyboard and single pointer.** Space toggles a focused item. Shift-click or Shift+Arrow range selection is an accelerator, not the only route. Composite widgets follow a consistent model (PAT-DT-005).
6. **Keep targets usable.** Checkbox hit areas meet at least 24×24 CSS px or the spacing exception (QG-019). On touch, a row tap normally *opens* the item; selecting needs its own target or an explicit "Select" mode.
7. **Scale safeguards with scope.**
   - Prefer undo for reversible bulk changes.
   - For irreversible or large-scope actions, use a specific confirmation that names the count and the consequence (PAT-SH-011; data-modifying submissions: QG-025).
8. **Report partial outcomes.** After a bulk operation, say what succeeded and what failed ("18 archived, 2 couldn't be archived — Retry"). Keep the failed items selected for retry (PAT-SH-016).
9. **Restore focus sensibly** after items are removed: move to the next item, or to the list container if it is empty.

Expert accelerators (Shift-ranges, shortcuts, command-palette bulk actions) are in PAT-DT-011. Table-specific selection is in PAT-DT-007. On touch, enter a selection mode explicitly (a "Select" control or per-item checkboxes); long-press to select is a platform convention on Android and iOS lists (E3) that must be paired with a visible alternative because it is undiscoverable and conflicts with context menus in browsers. Swipe actions on rows (not selection) are in PAT-MO-007.

## Evidence

- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines — Row checkboxes for multi-select; a header checkbox with an indeterminate state; a batch action bar with cancel; per-row actions disabled during batch mode. Enterprise convention.
- **E3** W3C WAI, "APG listbox pattern". https://www.w3.org/WAI/ARIA/apg/patterns/listbox/ — Separates focus movement from selection. The recommended multi-select model toggles with Space without held modifiers; modifier-based alternatives are documented. (Classed E3 per `sources/evidence-classes.md`; listed E4 in the findings.)
- **E3** W3C WAI, "Developing a Keyboard Interface". https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/ — Roving tabindex for composites; deleting a focused item must not strand focus, and moving to the next item is one remedy.
- **E3** Google Material Design, "States". https://m3.material.io/foundations/interaction/states — Selection can combine with hover and focus; two visual indicators support accessibility. Material convention.
- **E1** W3C, "WCAG 2.2 — SC 1.4.11 Non-text Contrast". https://www.w3.org/TR/WCAG22/#non-text-contrast — Visual information identifying component states needs at least 3:1.
- **E1** W3C, "WCAG 2.2 — SC 2.5.8 Target Size (Minimum)". https://www.w3.org/TR/WCAG22/#target-size-minimum — 24×24 CSS px, or a spacing or other listed exception.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Selection counts and bulk results must be announced without focus.
- **E4** Nielsen Norman Group, "Confirmation Dialogs Can Prevent User Errors — If Not Overused". https://www.nngroup.com/articles/confirmation-dialog/ — Confirm only serious or irreversible actions, name the affected objects, and provide undo where feasible.
- **E3** React documentation, "useOptimistic". https://react.dev/reference/react/useOptimistic — Optimistic removal must restore items and show an error if the action fails.
- **E5** Mobbin, "Web Table UI". https://mobbin.com/explore/web/ui-elements/table — Shipped web tables combine checkbox selection with actions. Convention observed, usability unverified.

## Alternatives and tradeoffs

- **Always-visible checkboxes vs an explicit "Select" mode.** Persistent checkboxes are discoverable but add visual weight on every row. A Select mode keeps rows clean but adds a step. On dense pointer layouts, checkboxes that appear on hover must also appear on focus, and must be persistent when hover is unavailable (Carbon E3). Choose by how often users act in bulk.
- **Selection persisting across pages.** Persistence suits curated collections (e.g. adding files to a set). Clearing on filter change is safer for destructive operations. Either is acceptable if the scope is visible.
- **Undo vs confirm for bulk.** See PAT-SH-011. Bulk scope tilts toward confirmation when undo is impractical.

## Exceptions and failure modes

- Single-item apps, or lists where items are never acted on together, do not need bulk selection.
- Failure modes: "select all" silently including unseen items; selection shown only by a subtle tint; row click both opening and selecting; the bulk bar covering the focused item (QG-006); unannounced counts; focus left on `<body>` after bulk delete.

## Evaluation questions

1. Can the user always see how many items are selected and which ones? [screenshot] [running app]
2. Does "select all" state its scope, and does selection behave as stated across paging and filtering? [running app]
3. Can items be selected and deselected by keyboard alone and by single tap or click? [running app]
4. Is the selected state distinguishable without color and announced by a screen reader? [running app] [automated]
5. Does a bulk action report partial failures and allow retry? [running app]
6. After bulk removal, where does focus land? [running app]
7. Do users predict correctly which items a bulk action will affect? [user study]

## Related

- Principles: P-01, P-10, P-11, P-12
- Dimensions: D-01, D-07, D-08
- Gates: QG-001, QG-008, QG-019, QG-028, QG-025
- Patterns: PAT-DT-005 (selection models, focus), PAT-DT-007 (tables), PAT-DT-011 (expert bulk work), PAT-SH-011 (destructive actions), PAT-SH-008 (action menus), PAT-MO-007 (touch row actions and drag; not selection), PAT-SH-016 (partial failure)

## Change log

- 2026-11-08 — Initial version (ADR-001).
