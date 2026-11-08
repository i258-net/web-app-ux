---
id: PAT-DT-007
title: Data tables and grids — sorting, sticky headers, selection, columns, and responsive strategies
type: pattern
scope: desktop
topics: [data-table, grid, sorting, sticky-header, frozen-column, row-selection, column-management, responsive-table, horizontal-scroll, card-stacking, pagination]
platforms: [desktop, tablet, mobile]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [pointer, keyboard, touch, assistive-tech]
principles: [P-01, P-05, P-08, P-12]
dimensions: [D-01, D-05, D-06, D-08, D-10]
gates: [QG-001, QG-004, QG-006, QG-010, QG-019, QG-050]
related: [PAT-DT-001, PAT-DT-003, PAT-DT-005, PAT-DT-006, PAT-DT-008, PAT-DT-011, PAT-SH-005, PAT-SH-006, PAT-SH-007, PAT-RS-003, PAT-RS-004, PAT-MO-008]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Data tables and grids — sorting, sticky headers, selection, columns, and responsive strategies

## Problem

Tables are where operational work happens: finding records, comparing values across rows, editing one record, and acting on many. On wide screens, the failures are headers that scroll away, unclear sort state, ambiguous selection, and too many equally weighted columns. On narrow windows, teams let the whole page scroll sideways, or turn every row into a card. Cards end comparison across rows and can strip table semantics. This pattern is the single home for table guidance, and responsive patterns link here.

## Recommendation

**Outcome:** people can find, compare, edit, and act on records at any width without losing row or column context.

1. **Use a semantic `<table>`** with `<th scope>` and an accessible name. Adopt the ARIA **grid** pattern only when cell-to-cell navigation and editing are needed. A grid commits you to its full contract: arrows between cells, Home/End, Ctrl+Home/End, and Enter/F2 to edit (PAT-DT-004).
2. **Order columns by task.** Put a human-readable identifier first, keep related columns together, and right-align numbers.
3. **Sort from the column header.** Use a `<button>` inside `<th>`, with `aria-sort` and a persistent direction indicator. Sortability must be visible without hover (PAT-DT-003).
4. **Freeze the header row and identifier column** when the table exceeds the viewport. Add row tracking on hover *and* focus. Sticky regions must not cover focused cells (QG-006).
5. **Use explicit selection.** Row checkboxes and a header checkbox with an indeterminate state, plus a visible count and a stated select-all scope. Show a bulk-action bar with an exit (PAT-DT-005, PAT-SH-006, PAT-DT-011).
6. **Keep row actions reachable.** Keep a persistent "…" button, or reveal actions on hover and focus with a no-hover fallback (PAT-DT-008).
7. **Make column management discoverable.** Let people show, hide, and reorder columns, indicate hidden columns, offer density options (PAT-DT-001), and remember choices (PAT-DT-011).
8. **Choose loading from the task.** Operational grids that need stable ranges and totals usually suit pagination, and browsing lists may suit Load More (PAT-SH-007). With virtualization, keep `aria-rowcount` / `aria-rowindex` accurate.

### Responsive strategies (choose by task, not by default)

| Strategy | Keeps cross-row comparison | Semantics | Best for | Costs |
|---|---|---|---|---|
| **A. Horizontal scroll in a contained region** | Yes | Kept | Comparison at any width | Columns off-screen. Needs keyboard scroll access |
| **B. Column priority** | Yes, for visible columns | Kept | Clear must-have columns | Priority research. Hidden data must stay reachable |
| **C. Stacked cards** | **No** | Can be lost | One-record reading, few columns, simple headers | Ends comparison. Longer page |
| **D. List–detail** | Partial | Kept | Many fields per record | Extra step |

- **A.** Wrap the table in `role="region"` with an accessible name and `tabindex="0"`, so keyboard users can focus it and scroll with the arrow keys. Show an overflow cue and freeze the identifier column. Only the table scrolls, not the page (QG-050). WCAG 1.4.10 exempts content that needs a two-dimensional layout for meaning or use. We read that as covering a real comparison table, but not the page around it (QG-010).
- **B.** Rank columns by what users compare. Hidden columns stay reachable via a "Columns" control, an expandable row, or the detail view. Never discard them silently at a breakpoint.
- **C.** Use stacking only when record-by-record reading fits the task. Label every value with its header. Changing `display` on table elements can remove table semantics, so restore roles or render a list on purpose, and test with real AT. Do not use it for spanning headers or editable grids.

## Evidence

- **E4** Nielsen Norman Group, "Data Tables: Four Major User Tasks". https://www.nngroup.com/articles/data-tables/. The four tasks (find, compare, view/edit, act). Identifier first, related columns adjacent, frozen headers and identifier columns, tracking aids, discoverable hiding and reordering, and an indication of hidden columns (F-DX-30, F-DX-36, F-NB-33).
- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines. Ample width, row sizes, header sort states, checkbox selection with an indeterminate header, a batch bar with cancel, and persistent overflow (F-DX-02, F-DX-05, F-DX-12, F-DX-29, F-DX-31, F-DX-32).
- **E4** Adrian Roselli, "A Responsive Accessible Table". https://adrianroselli.com/2017/11/a-responsive-accessible-table.html. A named, focusable scroll wrapper. Labeled stacking, and a warning that display changes can remove table semantics (F-DX-34, F-DX-35).
- **E3** W3C WAI APG, "Grid Pattern". https://www.w3.org/WAI/ARIA/apg/patterns/grid/. The grid keyboard contract. Use a semantic table for static data (F-SP-43).
- **E4** Nielsen Norman Group, "Sticky Headers: 5 Ways to Make Them Better". https://www.nngroup.com/articles/sticky-headers/. Persistent regions must earn their space (F-NB-35).
- **E2** Smashing Magazine / Baymard, "Infinite Scrolling, Pagination Or 'Load More' Buttons?". https://www.smashingmagazine.com/2016/03/pagination-infinite-scrolling-load-more-buttons/. Commerce testing favored Load More, for product browsing rather than operational grids (F-DX-33). NN/g likewise finds no approach best everywhere: https://www.nngroup.com/articles/infinite-scrolling-tips/ (E4, F-NB-34).
- **E1** W3C, WCAG 2.2 SC 1.4.10 Reflow. https://www.w3.org/TR/WCAG22/#reflow. The two-dimensional-layout exception (F-SP-04).

No comparative study of responsive table strategies was found. The strategy table is our synthesis.

## Alternatives and tradeoffs

- **Grid vs. table.** A grid gives spreadsheet-like efficiency, but it is costly to build and unfamiliar to screen-reader users when it isn't needed.
- **Scroll vs. cards.** Scrolling keeps comparison but hides columns. Cards read well one at a time but end comparison. NN/g and Roselli both say to decide from the task.

## Exceptions and failure modes

- Spreadsheet editors and pivot tables need grid semantics and dedicated testing beyond this pattern.
- Common failures: a focusable scroll region with no name or overflow cue; sorting through a click handler on a plain `<th>`; columns dropped at a breakpoint; stacked sticky header, toolbar, and filter bar covering most of a short window.

## Evaluation questions

- Does the identifier column stay visible during horizontal scroll? [screenshot] [running app]
- Is sort state visible without hover and exposed via `aria-sort`? [screenshot] [automated]
- Are the selection count and the scope of select-all stated? [screenshot]
- At 375 px, does only the table scroll sideways, and can a keyboard user focus and scroll it? [running app] [automated]
- At narrow widths, can every hidden field still be reached? [running app]
- If rows stack, do screen readers still announce the header for each value? [running app]
- At 200% zoom, do sticky headers leave room for data? [running app]
- Can users compare two records across columns on a tablet? [user study]

## Related

- Patterns: [PAT-DT-001](PAT-DT-001-wide-layout-density.md), [PAT-DT-003](PAT-DT-003-hover-tooltips.md), [PAT-DT-004](PAT-DT-004-keyboard-navigation-shortcuts.md), [PAT-DT-005](PAT-DT-005-focus-selection-management.md), [PAT-DT-006](PAT-DT-006-inline-editing.md), [PAT-DT-008](PAT-DT-008-contextual-actions-menus.md), [PAT-DT-011](PAT-DT-011-expert-workflows.md), PAT-SH-005, PAT-SH-006, PAT-SH-007, PAT-RS-003, PAT-RS-004, PAT-MO-008
- Principles: [P-01](../../principles/P-01-task-effectiveness.md), [P-05](../../principles/P-05-cognitive-clarity.md), [P-08](../../principles/P-08-visual-hierarchy-readability.md), [P-12](../../principles/P-12-accessibility-inclusion.md)
- Rubric: [D-01, D-05, D-06, D-08, D-10](../../rubric/dimensions.md); gates [QG-001, QG-004, QG-006, QG-010, QG-019, QG-050](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
