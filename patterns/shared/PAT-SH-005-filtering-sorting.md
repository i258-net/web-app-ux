---
id: PAT-SH-005
title: Filtering and sorting collections
type: pattern
scope: shared
topics: [filtering, faceted-search, sorting, applied-filters, result-count, live-update, apply-button]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-05, P-10, P-06, P-03]
dimensions: [D-02, D-06, D-07]
gates: [QG-028, QG-020b, QG-061, QG-063]
related: [PAT-SH-004, PAT-SH-007, PAT-SH-012, PAT-RS-010, PAT-MO-011, PAT-DT-007, PAT-PW-003]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Filtering and sorting collections

## Problem

Filters fail when criteria are not the ones users decide by, each tap reloads and breaks a multi-select episode, active filters vanish once the panel closes, long value lists are cut off without an obvious "show more", or users cannot tell sorting (reorders) from filtering (narrows). On compact screens the panel usually covers the results, hiding each choice's effect.

## Recommendation

**Outcome:** users narrow and order a collection by criteria they understand. They always see what is applied and how many results remain, and they can remove any constraint in one step.

1. **Derive facets from real decision criteria** for this content type, in user vocabulary. Prioritize the most-used facets; hide irrelevant ones per category.
2. **Make selection semantics explicit.**
   - Allow multiple values within a group where users weigh alternatives. The typical logic is OR within a group and AND across groups; confirm that this fits the domain.
   - Use checkboxes for multi-select and radios or segmented controls for exclusive choices.
3. **Choose a commit model deliberately** (see Alternatives):
   - **Live update** when results return fast, the panel does not cover the results, and position and focus are preserved.
   - **Batch with Apply** when the panel covers the results (typical full-screen compact panels), when users usually select several values, or when updates are slow.
   - With Apply, label the button with the outcome ("Show 42 results") and keep the panel open while the user assembles a combination.
4. **Show applied filters next to the results.** Use a summary, removable chips, or both. Each chip removes one filter. Provide "Clear all" when two or more are active. This includes filters inherited from a link.
5. **Show the result count** and update it as filters change. Announce changes via a status message, not by moving focus (QG-028).
6. **Truncate long value lists only with a discoverable expansion** ("Show all 24 brands"). Keep selected values visible even when collapsed. Avoid nested scrolling areas.
7. **Keep sort separate from filter.**
   - Show the current sort order persistently ("Sorted by: Newest").
   - Use a single control with named options; "Price: low to high" is clearer than an arrow alone.
   - In tables, show sort state in the column header and expose it with `aria-sort` (PAT-DT-007).
8. **Persist filter and sort state in the URL** so reload, Back from a detail view, and sharing restore them (QG-061, QG-063; PAT-PW-003).
9. **Prevent dead ends.** Where cheap, show counts per value or disable zero-result values with an explanation. When a combination yields nothing, list the active filters with one-tap removal (PAT-SH-012).
10. **No unexpected context change** (QG-020b): choosing a value never navigates away or moves focus.

Compact presentations (sheet vs full-screen panel vs tray) are in PAT-MO-011 and PAT-RS-010.

## Evidence

- **E2** Nielsen Norman Group, "Defining Helpful Filter Categories and Values for Better UX". https://www.nngroup.com/articles/filter-categories-values/ — Users struggled when key criteria were missing or unfamiliar. Facets should be relevant, predictable, and free of jargon. Examples are mainly shopping and travel.
- **E4** Nielsen Norman Group, "User Intent Affects Filter Design". https://www.nngroup.com/articles/applying-filters/ — Refreshing after every choice interrupts multi-select intent, especially on slow sites. Avoid disruptive position changes.
- **E4** Nielsen Norman Group, "Mobile Faceted Search with a Tray". https://www.nngroup.com/articles/mobile-faceted-search/ — A partial overlay keeps some results visible and favors fast feedback.
- **E4** Baymard Institute, "What Is an Ecommerce Filter? UI Best Practices". https://baymard.com/blog/ecommerce-filter-ui — Recommends a deliberate "Show X Results" on mobile and real-time updates on desktop. Also covers OR within a group and AND across groups, and filter vs sort. *E-commerce practitioner synthesis.*
- **E2** Baymard Institute, "Display 'Applied Filters' in an Overview". https://baymard.com/research-articles/how-to-design-applied-filters — Users were disoriented when active filters were not visible near results. An overview gives confirmation and fast removal. *E-commerce*; likely generalizes to filtered collections.
- **E2** Baymard Institute, "6 Guidelines for Truncation Design". https://baymard.com/research-articles/truncation-design — Truncated value lists preserved overview only when users noticed the expansion control.
- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines — Sort state (unsorted, ascending, descending) stays indicated on the sorted column. Enterprise convention.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Count updates must be announced without receiving focus.
- **E5** Mobbin, "Mobile Filter UX Flows". https://mobbin.com/explore/mobile/flows/filtering-sorting — Shipped apps filter a visible result set. Convention observed, usability unverified.

## Alternatives and tradeoffs

- **Live vs Apply: a real disagreement.** NN/g's tray article favors immediate feedback so users see each filter's effect. Baymard's public synthesis recommends Apply on mobile and live updates on desktop. NN/g's intent article conditions the choice on multi-select intent and latency rather than device. All three are E4, and none establishes one rule for every web app. We therefore decide by **visibility of results, latency, and selection intent**, not by viewport label. A fast live update in a side panel on a tablet can be right; a full-screen panel on a large phone usually needs Apply. Either is acceptable if it is executed with counts and stable position.
- **Hybrid.** Live counts inside the panel ("42 results") plus an Apply button combine feedback with a single commit.
- **Faceted filters vs categories.** Baymard (E2, e-commerce) found overlapping attributes work better as combinable filters (https://baymard.com/research-articles/ecommerce-navigation-best-practice). Keep categories for stable, exclusive concepts.

## Exceptions and failure modes

- Very small collections (fewer than about a screenful) may need only search or sort. A heavy filter UI adds cost.
- Failure modes: each checkbox reloads and scrolls to top; chips not individually removable; "Clear all" with no undo; missing or stale counts; sort shown as an unlabeled arrow; filters lost on Back; Apply hidden below a long panel (sticky actions: PAT-MO-010).

## Evaluation questions

1. Do facet names and values match how users describe their decision? [user study] [screenshot]
2. While selecting several values, does the page keep its position and focus? [running app]
3. Are active filters visible next to the results and removable one at a time? [screenshot] [running app]
4. Is the result count shown, updated, and announced? [running app] [automated]
5. Is the current sort visible and distinguishable from filters? [screenshot]
6. After opening a result and pressing Back, are filters, sort, and scroll position restored? [running app]
7. When a combination yields zero results, can the user see and undo the cause? [running app]

## Related

- Principles: P-05, P-10, P-06, P-03
- Dimensions: D-02, D-06, D-07
- Gates: QG-028, QG-020b, QG-061, QG-063
- Patterns: PAT-SH-004 (search), PAT-SH-007 (lists), PAT-SH-012 (no results), PAT-RS-010 (modality variants), PAT-MO-011 (sheets), PAT-DT-007 (table sorting), PAT-PW-003 (URL state)

## Change log

- 2026-11-08 — Initial version (ADR-001).
