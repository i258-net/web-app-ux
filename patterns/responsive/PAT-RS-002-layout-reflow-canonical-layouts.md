---
id: PAT-RS-002
title: Layout reflow and canonical layouts — list-detail, supporting pane, feed
type: pattern
scope: responsive
topics: [layout, reflow, list-detail, split-view, supporting-pane, feed, multi-pane, canonical-layouts, source-order]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-03, P-04, P-01, P-08]
dimensions: [D-10, D-02, D-01, D-08]
gates: [QG-010, QG-050, QG-004, QG-061]
related: [PAT-RS-001, PAT-RS-003, PAT-RS-006, PAT-RS-007, PAT-RS-011, PAT-DT-001, PAT-DT-007, PAT-DT-010, PAT-PW-003]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Layout reflow and canonical layouts — list-detail, supporting pane, feed

## Problem

Most app screens are one of a few shapes: browse a collection and open an item, work on a primary object with secondary context, or scan a stream of cards. Designed only as a phone column and a desktop canvas, the wide layout becomes a stretched phone screen and the narrow one a squeezed desktop. Reflow between them often loses the selected item, scroll position, or URL.

## Recommendation

**Outcome:** each screen uses a layout shape that matches the task's relationships. Panes appear side by side when space allows and become a logical sequence when it does not. Reflow never loses the user's place.

1. **Classify the screen by task relationship, not by device.**
   - **List-detail**: parent collection plus one selected child (mail, files, tickets).
   - **Supporting pane**: one primary work area plus secondary content that relates to it (document plus comments, map plus results).
   - **Feed**: many peer items for browsing (cards, media).
2. **List-detail reflow.**
   - *compact:* one pane at a time. List → detail is a navigation with its own URL; Back returns to the list at the same scroll position with the item still identifiable.
   - *medium:* one pane for dense content or deep focus, two panes for fast browsing; choose per task.
   - *expanded and wider:* two panes; keep the selection persistently highlighted in the list.
   - On resize from two panes to one, show the *detail* that was selected (not the list top) and keep Back meaningful.
3. **Supporting-pane reflow.**
   - *compact and medium:* place supporting content below the primary content, or in a non-modal bottom sheet, with a visible control to reach it.
   - *expanded and wider:* a side pane of fixed, modest width beside a primary area of roughly two-thirds. Supporting content must not become the only route to a primary action.
4. **Feed reflow.** Single column of full-width items on compact; add columns as width grows. Keep reading order equal to DOM order so keyboard and screen-reader order matches the visual scan ([PAT-RS-007](PAT-RS-007-container-vs-media-queries.md) for card internals).
5. **Prefer intrinsic layout** (Grid/Flexbox with `minmax()`, wrapping) for column counts. Reserve breakpoint-level changes for structural switches like one pane to two.
6. **Consider height.** Two panes in a short, wide window (landscape phone, laptop with docked browser tools) may be unusable; decide pane count from both dimensions.
7. **State belongs to the URL and the model, not to the layout.** Selected item, open pane, and filters survive resize, rotation, reload, and deep links (QG-061; [PAT-RS-011](PAT-RS-011-orientation-foldables-hybrids.md)).
8. **Reflow must pass WCAG 1.4.10** at the 320 CSS px test width: no two-dimensional scrolling except for content that needs a 2-D layout, such as data tables (QG-010; [PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md)).

## Evidence

- **E3** Google, "Material Design 3 — Canonical layouts". https://m3.material.io/foundations/layout/canonical-examples — List-detail: compact shows list *or* detail; medium one pane for dense content/deep focus, two for fast browsing; expanded and larger two panes. Supporting pane: primary area about two-thirds; compact/medium place supporting content below or in a bottom sheet; expanded uses a fixed 360dp pane. Feed: compact stacks full-width items, wider layouts add columns; items reflow on rotation, unfolding, or multi-window changes.
- **E3** Apple, "Human Interface Guidelines — Split views". https://developer.apple.com/design/human-interface-guidelines/split-views.md — Split views show adjacent hierarchy levels; keep the selections leading to the detail persistently highlighted.
- **E3** Apple, "Human Interface Guidelines — Sidebars". https://developer.apple.com/design/human-interface-guidelines/sidebars.md — A permanent sidebar uses a navigation split view; sidebars generally expose no more than two hierarchy levels.
- **E3** Apple, "Human Interface Guidelines — Layout". https://developer.apple.com/design/human-interface-guidelines/layout.md — Decide layout from available size classes, not device type or orientation; functionality remains as size classes change.
- **E3** Android Developers, "Use window size classes". https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes — Medium 600–839dp and expanded 840–1199dp classes are based on available window space; height can make two panes impractical.
- **E3** Android Developers, "App orientation, aspect ratio, and resizability". https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability — Preserve app state, including form input, during orientation and window-size changes.
- **E4** Google (web.dev), "Macro layouts". https://web.dev/learn/design/macro-layouts — Grid and Flexbox distribute space intrinsically; media queries for larger structural changes; start from a simple source order.
- **E4** Google (web.dev), "Accessibility". https://web.dev/learn/design/accessibility — Visual CSS reordering does not change reading order; keep source order understandable.
- **E1** W3C, "WCAG 2.2 — 1.4.10 Reflow". https://www.w3.org/TR/WCAG22/#reflow — No two-dimensional scrolling at 320 CSS px width (vertical content) or 256 CSS px height (horizontal content), except where 2-D layout is essential.
- **E4** Adrian Roselli, "A Responsive Accessible Table". https://adrianroselli.com/2017/11/a-responsive-accessible-table.html — Stacking table rows into cards can remove table semantics; a focusable scrolling wrapper is an alternative.
- **E5** Mobbin, "Explore web app designs". https://mobbin.com/explore/web — Multi-column layouts recur in communication and operational web apps; convention observed, usability unverified.

*Interpretation (ours):* translating dp thresholds to CSS px is a mapping decision ([PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md)); "show the selected detail on collapse" is our inference from Material's selected-context and Android's state-preservation guidance.

## Alternatives and tradeoffs

- **Overlay detail (modal or sheet over the list)** at medium widths keeps list context but blocks list interaction; acceptable for quick previews, poor for repeated triage.
- **Three panes** (navigation, list, detail) at large and extra-large widths suit expert tools; compress navigation to a rail first ([PAT-RS-001](PAT-RS-001-navigation-transformation.md)).
- **Tables vs cards.** Converting rows to cards suits record-by-record reading and harms comparison; a scrolling table region is a legitimate 2-D exception (PAT-DT-007).

## Exceptions and failure modes

- Two panes squeezed into medium width where neither is usable.
- Detail pane with no URL, so deep links, reload, and Back fail.
- Collapsing to one pane and resetting to the list top, losing the selected item.
- Supporting pane holding the only Save/Submit control, which disappears below the fold on compact.
- Visual reordering (`order`, grid placement) that makes the tab order jump between panes.

## Evaluation questions

- Which canonical shape is each key screen, and does its compact and expanded form match that shape's reflow rules? [screenshot] [prototype]
- Resize from two panes to one with an item selected: is that item's detail shown and Back meaningful? [running app]
- Do selected item and pane state survive reload and deep link? [running app]
- At 320 CSS px width, is there any two-dimensional scroll outside essential 2-D regions? [automated] [running app]
- Does tab order follow the visual pane order? [running app]
- In a short, wide window, are both panes usable? [running app]

## Related

- Principles: [P-03](../../principles/P-03-information-architecture.md), [P-04](../../principles/P-04-navigation-orientation.md), [P-01](../../principles/P-01-task-effectiveness.md), [P-08](../../principles/P-08-visual-hierarchy-readability.md)
- Dimensions: D-10, D-02, D-01, D-08; Gates: QG-010, QG-050, QG-004, QG-061
- Patterns: [PAT-RS-001](PAT-RS-001-navigation-transformation.md), [PAT-RS-003](PAT-RS-003-content-prioritization.md), [PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md), [PAT-RS-007](PAT-RS-007-container-vs-media-queries.md), [PAT-RS-011](PAT-RS-011-orientation-foldables-hybrids.md), [PAT-DT-001](../desktop/PAT-DT-001-wide-layout-density.md), PAT-DT-007, PAT-DT-010, PAT-PW-003

## Change log

- 2026-11-08 — Initial version (ADR-001).
