---
id: PAT-SH-007
title: Long lists — pagination, Load more, and infinite scroll
type: pattern
scope: shared
topics: [lists, pagination, load-more, infinite-scroll, scroll-restoration, footer, feeds]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-04, P-01, P-13, P-12]
dimensions: [D-01, D-02, D-09]
gates: [QG-063, QG-061, QG-028, QG-004]
related: [PAT-DT-007, PAT-PW-004, PAT-PW-003, PAT-SH-010, PAT-MO-010, PAT-MO-008, PAT-SH-005]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Long lists — pagination, Load more, and infinite scroll

## Problem

Long collections must be split somehow, and each method has costs:

- Pagination adds clicks and fragments scanning.
- Infinite scroll makes the footer unreachable, breaks keyboard paths, grows page weight, and makes items hard to refind.
- Load more needs a deliberate action for each batch.

The most damaging failure is shared by all three: returning from a detail view resets the list to the top, so users lose their place and their loaded results.

## Recommendation

**Outcome:** users can browse or retrieve items efficiently, keep their place when they leave and return, and reach everything on the page, including the footer.

1. **Choose by task:**
   - **Pagination** for deliberate retrieval and comparison, stable references ("it was on page 3"), operational tables, and bounded result sets where users jump to a position.
   - **Load more** (a button, optionally with lazy-loaded images) for browsing result lists where continuity matters but the footer and orientation must stay reachable.
   - **Infinite scroll** for continuous, homogeneous feeds that users consume rather than search, with no important content after the list.
2. **Preserve position and loaded state.**
   - Returning via Back restores the scroll position, every loaded batch, and the active filters (QG-063).
   - Put the page or cursor in the URL so reload and sharing restore the view (QG-061; mechanics in PAT-PW-004 and PAT-PW-003).
3. **Give orientation landmarks.**
   - Show the total count when it is known ("Showing 1–40 of 312").
   - Keep page numbers or batch boundaries meaningful.
   - In infinite feeds, offer a way back to the top, and keep the footer reachable or duplicate its essential links elsewhere.
4. **Keyboard and assistive technology.**
   - After Load more, keep focus on the button or move it to the first new item. Never reset it to the top (QG-004).
   - Announce "20 more items loaded" as a status message (QG-028).
   - For infinite scroll, provide a keyboard-operable way to load more, or make loading happen as focus advances. Never require a scroll gesture.
5. **Show loading and end states.** Show an inline loading indicator at the point of loading, an explicit "End of results", and an inline error with Retry if a batch fails (PAT-SH-016). Reserve space for incoming items to avoid layout shift (PAT-SH-010).
6. **Keep list items scannable.** Order items logically, format them consistently, and put the identifying information first. Each item has one primary target, plus secondary actions with their own targets.
7. **Manage memory for very long lists.** Virtualize or window long lists for performance. Make sure find-in-page, focus order, and screen-reader item counts still behave sensibly, or offer pagination as an alternative.

Compact density and truncation are in PAT-MO-008. Sticky list headers and pull-to-refresh are in PAT-MO-010. Table pagination and density are in PAT-DT-007.

## Evidence

- **E4** Nielsen Norman Group, "Infinite Scrolling: When to Use It, When to Avoid It". https://www.nngroup.com/articles/infinite-scrolling-tips/ — Infinite scroll suits continuous browsing. It causes problems for refinding, footer access, keyboard navigation, and page weight. Load more and pagination are alternatives, and no approach is best everywhere.
- **E2** Smashing Magazine (Christian Holst, Baymard Institute), "Infinite Scrolling, Pagination Or 'Load More' Buttons? Usability Findings In eCommerce". https://www.smashingmagazine.com/2016/03/pagination-infinite-scrolling-load-more-buttons/ — Commerce testing favored Load more with lazy loading over pagination and unlimited scrolling. Infinite scroll encouraged broad scanning but reduced attention and could obstruct the footer. *E-commerce product lists, 2016*; weak grounds for operational grids.
- **E2** Nielsen Norman Group, "Mobile User Experience: Limitations and Strengths". https://www.nngroup.com/articles/mobile-ux/ — Mobile users are frequently interrupted. Save state and context so they can resume without redoing work. (2015.)
- **E4** Nielsen Norman Group, "User Control and Freedom". https://www.nngroup.com/articles/user-control-and-freedom/ — Back should return users to the previous state.
- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines — Documents pagination for operational tables (as noted in the DX findings' discussion of F-DX-33).
- **E3** Google Material Design, "Lists". https://m3.material.io/components/lists — Order items logically and keep them scannable and consistently formatted. Material convention.
- **E1** W3C, "WCAG 2.2 — SC 2.4.3 Focus Order". https://www.w3.org/TR/WCAG22/#focus-order — Focus order must preserve meaning and operability, including after content is appended.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — "More loaded" and "end of list" messages must be announced without focus.

## Alternatives and tradeoffs

- **Pagination vs Load more vs infinite scroll: a recorded disagreement in context.** Baymard's commerce testing (E2) favors Load more for product discovery. NN/g (E4) refuses a universal ranking. Carbon (E3) uses pagination for operational tables. These do not conflict once context is attached: **discovery browsing → Load more; continuous feeds → infinite scroll with safeguards; retrieval, comparison, and record management → pagination.** The rubric accepts any of them if position memory, footer access, and keyboard operation work.
- **Hybrid.** Auto-load the first few batches, then switch to a Load more button. This keeps the footer reachable while reducing clicks.
- **Page size.** Larger pages reduce paging but increase load time. No finding sets an optimum.

## Exceptions and failure modes

- Short lists (one or two screens) need no splitting.
- Failure modes:
  - Back from a detail page lands at the top with only the first batch loaded;
  - infinite scroll above a footer that holds legal, help, or contact links;
  - Load more that moves focus to the top;
  - pagination controls with tiny targets;
  - no total count, so users cannot judge the size of the set;
  - a silent failure when the next batch errors.

## Evaluation questions

1. Does the chosen method fit the task (browse, feed, or retrieve and compare)? [screenshot] [user study]
2. Open an item deep in the list, then press Back: are scroll position, loaded batches, and filters restored? [running app]
3. Can a keyboard-only user load more items and reach the footer? [running app]
4. Are new batches and the end of the list announced to a screen reader? [running app] [automated]
5. Does the URL represent the current page or position so reload restores it? [running app]
6. Is there an inline Retry when loading a batch fails (test with network throttling)? [running app]
7. Can users find again an item they saw earlier? [user study]

## Related

- Principles: P-04, P-01, P-13, P-12
- Dimensions: D-01, D-02, D-09
- Gates: QG-063, QG-061, QG-028, QG-004
- Patterns: PAT-DT-007 (tables), PAT-PW-004 (restoration), PAT-PW-003 (URL state), PAT-SH-010 (loading), PAT-MO-010 (sticky and refresh), PAT-MO-008 (compact density), PAT-SH-005 (filters)

## Change log

- 2026-11-08 — Initial version (ADR-001).
