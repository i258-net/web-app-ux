---
id: PAT-RS-006
title: Breakpoint strategy — window size classes plus content-driven breakpoints
type: pattern
scope: responsive
topics: [breakpoints, window-size-classes, media-queries, content-driven-breakpoints, reflow, testing-widths, design-tokens]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-09, P-08, P-12, P-01]
dimensions: [D-10, D-08, D-05]
gates: [QG-010, QG-050, QG-009, QG-042]
related: [PAT-RS-001, PAT-RS-002, PAT-RS-004, PAT-RS-007, PAT-RS-008, PAT-RS-009, PAT-RS-011, PAT-DT-010]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Breakpoint strategy — window size classes plus content-driven breakpoints

## Problem

Breakpoints are often copied from a framework or from device lists ("iPhone 375, iPad 768, laptop 1024") and then treated as device detectors. Three problems follow. Layouts break at in-between widths nobody tested: a 700 px split-screen window, a 900 px foldable, a 1100 px laptop with a sidebar open. Device breakpoints get conflated with input ("768 and below = touch"). And teams sometimes mistake accessibility test widths, such as WCAG's 320 CSS px, for design breakpoints.

## Recommendation

**Outcome:** a small, shared set of named window classes gives the product a consistent structural vocabulary. Between and inside those classes, layouts adapt to their content without breaking. Breakpoints never stand in for device type or input.

1. **Adopt a small set of named window classes for structural decisions** (navigation form, pane count, margins). This repository uses Material 3's classes:

   | Class | Material width | Repository mapping |
   |---|---|---|
   | compact | < 600dp | < 600 CSS px |
   | medium | 600–839dp | 600–839 CSS px |
   | expanded | 840–1199dp | 840–1199 CSS px |
   | large | 1200–1599dp | 1200–1599 CSS px |
   | extra-large | ≥ 1600dp | ≥ 1600 CSS px |

   The 1dp → 1 CSS px mapping is *our* convention for shared vocabulary. Material does not state it, and teams may choose another as long as they write it down.
2. **Add content-driven breakpoints where content needs them.** Resize slowly through the whole range; wherever text wraps badly, navigation collides, or a control becomes unusable, add a local adjustment. These are often component-level and belong in container queries ([PAT-RS-007](PAT-RS-007-container-vs-media-queries.md)).
3. **Prefer intrinsic layout first.** Grid/Flexbox with `minmax()`, `clamp()`, and wrapping reduce the number of breakpoints needed ([PAT-RS-008](PAT-RS-008-responsive-typography-spacing.md)).
4. **Write breakpoints mobile-first (`min-width`).** Consider relative units (`em`) in media queries so layout responds when users enlarge text. *(The relative-unit choice is a web.dev demonstration; effects on zoom must be tested in target browsers.)*
5. **Consider height.** Short windows (landscape phones, laptops with docked tools) may need single-pane layouts or non-sticky chrome even at expanded width.
6. **Never use width as an input signal.** Width selects layout; `pointer`/`hover`/`any-*` select input refinements (QG-042; [PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md)).
7. **Separate test widths from breakpoints.**
   - **WCAG 1.4.10 Reflow** sets *conformance test conditions*: content must work without two-dimensional scrolling at a width equivalent to **320 CSS px** (vertically scrolling content) or a height equivalent to **256 CSS px** (horizontally scrolling content). These are **not design breakpoints**. They model a 1280 px window at 400 % zoom and narrow viewports. Your compact layout must simply survive them (QG-010).
   - QG-050's widths (320, 375, 768, 1024, 1440) are a regression sample, not a breakpoint set. Also test just either side of each class boundary (e.g. 599/600, 839/840).
8. **Tokenize classes once** (CSS custom media or a shared constants file) so CSS, JS, and design files agree.

## Evidence

- **E3** Google, "Material Design 3 — Breakpoints". https://m3.material.io/foundations/layout/breakpoints — Window size classes ("breakpoints"): Compact under 600dp; Medium 600–839dp; Expanded 840–1199dp; Large 1200–1599dp; Extra-large 1600dp+. Apply to Android and web; layout changes consider window space, ergonomics, and conventions.
- **E3** Android Developers, "Use window size classes". https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes — Classes reflect available window space, not device; height can make two panes impractical.
- **E3** Apple, "Human Interface Guidelines — Layout". https://developer.apple.com/design/human-interface-guidelines/layout.md — Decide from compact/regular size classes rather than device type or orientation; the fetched page gives no numeric thresholds.
- **E4** Google (web.dev), "Media queries". https://web.dev/learn/design/media-queries — Let content determine breakpoints rather than named device sizes; demonstrates relative units and `min-width` queries.
- **E4** Google (web.dev), "Macro layouts". https://web.dev/learn/design/macro-layouts — Intrinsic Grid/Flexbox layouts plus media queries for structural changes.
- **E1** W3C, "WCAG 2.2 — 1.4.10 Reflow". https://www.w3.org/TR/WCAG22/#reflow — 320 CSS px width / 256 CSS px height conditions, with an exception for content requiring 2-D layout.
- **E1** W3C, "WCAG 2.2 — 1.4.4 Resize Text". https://www.w3.org/TR/WCAG22/#resize-text — Text resizable to 200 % without loss of content or functionality.
- **E3** Google (web.dev), "Interaction". https://web.dev/learn/design/interaction — Screen size does not determine input mechanism.
- **E3** Apple Support, "Use multitasking on your iPad". https://support.apple.com/en-us/102576 — Split View, Slide Over, and Stage Manager produce intermediate window widths on tablets.

*Interpretation (ours):* that WCAG's reflow widths correspond to 1280 px at 400 % zoom is a common reading of the criterion's intent; the normative text only states the CSS px conditions. The research notes record Material's dp classes and WCAG's reflow widths as answering different questions (standards-platforms Disagreement 4).

## Alternatives and tradeoffs

- **Framework breakpoints (e.g. 576/768/992/1200).** Fine if documented and content-tested; they conflict only in name with Material's classes. Pick one vocabulary per product.
- **Fully intrinsic, no named classes.** Works for content sites; app shells usually still need a few structural switches (navigation form, pane count).
- **Apple size classes.** Useful conceptually (compact/regular per axis) but without published numeric thresholds for the web.

## Exceptions and failure modes

- Breakpoints named after devices ("tablet") and used to switch input behavior.
- Testing only at breakpoint values, missing breakage at 601 or 1150 px.
- Designing a dedicated "320 px layout" to satisfy WCAG instead of making compact reflow robust.
- Media queries in px that ignore text enlargement, so 200 % text overflows a layout that never reflows.
- Breakpoints duplicated with different values in CSS and JS.

## Evaluation questions

- Are window classes defined once and documented, including the unit mapping? [automated]
- Does a slow resize from 320 to 1920 px reveal any width where layout breaks? [running app] [automated]
- At 320 CSS px width (and 256 px height for horizontal content), is there two-dimensional scrolling outside essential 2-D regions? [automated] [running app]
- Does any breakpoint change input behavior (hover, gestures, shortcuts)? [running app]
- At 200 % text size, does the layout reflow rather than clip? [running app]
- In a short landscape window, are panes and sticky chrome still usable? [running app]

## Related

- Principles: [P-09](../../principles/P-09-consistency-familiarity.md), [P-08](../../principles/P-08-visual-hierarchy-readability.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-01](../../principles/P-01-task-effectiveness.md)
- Dimensions: D-10, D-08, D-05; Gates: QG-010, QG-050, QG-009, QG-042
- Patterns: [PAT-RS-001](PAT-RS-001-navigation-transformation.md), [PAT-RS-002](PAT-RS-002-layout-reflow-canonical-layouts.md), [PAT-RS-004](PAT-RS-004-adaptive-density.md), [PAT-RS-007](PAT-RS-007-container-vs-media-queries.md), [PAT-RS-008](PAT-RS-008-responsive-typography-spacing.md), [PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md), [PAT-RS-011](PAT-RS-011-orientation-foldables-hybrids.md), PAT-DT-010

## Change log

- 2026-11-08 — Initial version (ADR-001).
