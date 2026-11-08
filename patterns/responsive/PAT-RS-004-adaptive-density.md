---
id: PAT-RS-004
title: Adaptive density — spacing tokens per window class and input, and user density settings
type: pattern
scope: responsive
topics: [density, spacing, design-tokens, margins, target-size, density-toggle, any-pointer, user-preferences]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-08, P-06, P-12, P-14, P-15]
dimensions: [D-05, D-03, D-08, D-10]
gates: [QG-019, QG-040, QG-011, QG-009, QG-005]
related: [PAT-RS-009, PAT-RS-006, PAT-RS-008, PAT-DT-001, PAT-DT-007, PAT-DT-011, PAT-MO-001, PAT-MO-008]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Adaptive density — spacing tokens per window class and input, and user density settings

## Problem

Density is how much content and how many controls fit in a given area. It is set by spacing, row height, padding, and target size. Teams usually tie it to a single variable: "mobile = roomy, desktop = compact". That fails in two directions. A touchscreen laptop or a tablet in landscape gets cramped mouse-sized rows. A narrow desktop window gets oversized touch spacing and shows half the rows it could. Some teams also ship one density for everyone, which frustrates both the occasional user (too dense) and the expert who triages hundreds of items a day (too sparse).

Wide-layout density for expert work is covered in [PAT-DT-001](../desktop/PAT-DT-001-wide-layout-density.md); this pattern covers how density *varies* across space, input, and preference.

## Recommendation

**Outcome:** spacing fits the available space, target size fits the available input, and users who need a different density can choose one without losing function or accessibility.

1. **Treat density as two independent axes.**
   - **Space axis (window or container class):** page margins, gutters, pane spacers, and the number of columns. These vary by window class (compact, medium, expanded and wider).
   - **Input axis (pointer capability):** hit-area size, minimum spacing between targets, and row height of interactive lists. These vary by `any-pointer` / `pointer`, never by width ([PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md)).
2. **Express both as tokens.** Define a spacing scale (e.g. 4-based steps) and map semantic tokens (`--space-page-margin`, `--space-pane-gap`, `--size-target`, `--row-height-list`) per class. Components consume semantic tokens only, so a change of class or input re-themes them consistently.
3. **Starting values for the space axis.** Material uses 16dp margins on compact and 24dp leading/trailing margins and pane spacers on medium and expanded. That is a reasonable starting point once mapped to CSS px ([PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md)).
4. **Starting values for the input axis.**
   - Where any coarse pointer is available: primary targets ≥ 44–48 px with ≥ 8 px separation (QG-040).
   - Fine-pointer-only: tighter rows are acceptable, but every target must still meet WCAG 2.5.8 (24×24 CSS px or the spacing exception) (QG-019).
   - Keep the *visual* glyph small if needed and enlarge the *hit area* with padding.
5. **Offer a user density setting for repetitive or data-heavy work.** Typically "Comfortable / Compact" (sometimes "Spacious").
   - Scope it clearly (this table, this app, this device) and remember it.
   - Compact mode may reduce padding and row height; it must never drop below QG-019, remove focus indicators, or hide labels.
   - On coarse-pointer devices either keep the comfortable target floor in compact mode, or warn that compact is pointer-oriented.
6. **Let text enlargement override density.** Rows and containers grow with text size and text-spacing overrides (QG-009, QG-011). Fixed row heights that clip enlarged text are a failure.
7. **Density follows grouping.** Reducing space must keep related items visibly grouped and unrelated items separated; compress evenly within groups before removing the gaps between them.

## Evidence

- **E3** Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines — Offers multiple row sizes, from highly dense to spacious rows that ease interaction and multiline content.
- **E3** Google, "Material Design 3 — Breakpoints". https://m3.material.io/foundations/layout/breakpoints — Compact margins 16dp; medium/expanded margins and pane spacers 24dp; layout changes consider window space, ergonomics, and conventions.
- **E3** Google, "Material Design 3 — Designing". https://m3.material.io/foundations/designing — Touch targets at least 48×48dp (≈ 9 mm), 8dp or more between targets; pointer targets at least 44×44dp; a 24dp icon can sit inside a 48dp target.
- **E3** Apple, "Human Interface Guidelines — Designing for iPadOS". https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados.md — Viewing distance and input mode affect comfortable density on iPad.
- **E3** Apple, "Human Interface Guidelines — Designing for macOS". https://developer.apple.com/design/human-interface-guidelines/designing-for-macos.md — Keep layout and density stable while supporting larger hit targets or controls that expand on touch.
- **E3** Apple, "Human Interface Guidelines — Accessibility". https://developer.apple.com/design/human-interface-guidelines/accessibility.md — Distinguishes default (iOS/iPadOS 44×44 pt) and minimum (28×28 pt) control sizes; macOS 28×28 pt default, 20×20 pt minimum.
- **E3** Apple, "Human Interface Guidelines — Layout". https://developer.apple.com/design/human-interface-guidelines/layout.md — Group with negative space, containers, and separators to communicate relationships.
- **E1** W3C, "WCAG 2.2 — 2.5.8 Target Size (Minimum)". https://www.w3.org/TR/WCAG22/#target-size-minimum — 24×24 CSS px or the spacing/equivalent/inline/user-agent/essential exceptions.
- **E1** W3C, "WCAG 2.2 — 1.4.12 Text Spacing". https://www.w3.org/TR/WCAG22/#text-spacing — No loss of content when line height, paragraph, letter, and word spacing are overridden.
- **E1** W3C, "Media Queries Level 4". https://www.w3.org/TR/mediaqueries-4/ — `pointer`/`any-pointer` describe pointer accuracy, not viewport size.

*Interpretation (ours):* the two-axis model is a synthesis. Neither Material nor Apple defines a web density token scheme, and no source here sets an optimal density for web apps. Material dp values are not CSS px without an explicit mapping.

## Alternatives and tradeoffs

- **Single fixed density.** Cheapest to design and test; adequate for homogeneous audiences and low-volume tasks.
- **Automatic density only (no toggle).** Avoids settings UI but cannot serve experts and occasional users on the same device.
- **Density by `pointer` vs `any-pointer`.** `pointer` keeps mouse-primary hybrid devices dense; `any-pointer` protects occasional touch. Prefer `any-pointer` for primary actions and lists users act on; `pointer` is acceptable for read-only dense views.
- **Container-driven density.** A card in a narrow sidebar can tighten its own spacing via container queries ([PAT-RS-007](PAT-RS-007-container-vs-media-queries.md)), which is often better than a page-wide switch.

## Exceptions and failure modes

- Compact mode shrinking targets below 24 px or removing the focus ring.
- Row heights in px that clip text at 200 % enlargement.
- Density switched by `max-width`, making touch laptops cramped and narrow desktop windows sparse.
- Density setting stored per page with no indication, so it seems to change at random.
- Spacing reduced uniformly so groups merge and hierarchy flattens.

## Evaluation questions

- Are spacing and target sizes defined as tokens that change by window class and pointer capability independently? [automated] [running app]
- On a touch laptop at expanded width, are list and toolbar targets ≥ 44 px? [running app]
- In a narrow desktop window with a mouse, is density appropriate rather than touch-sized? [running app]
- If a density setting exists, is it scoped, remembered, and do compact targets still meet 24 px with visible focus? [running app] [automated]
- At 200 % text size and with WCAG text-spacing overrides, does any row clip or overlap? [running app] [automated]
- Do expert users complete repetitive tasks faster in compact mode without more errors? [user study]

## Related

- Principles: [P-08](../../principles/P-08-visual-hierarchy-readability.md), [P-06](../../principles/P-06-interaction-ergonomics.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-14](../../principles/P-14-control-privacy-trust.md), [P-15](../../principles/P-15-craft-delight.md)
- Dimensions: D-05, D-03, D-08, D-10; Gates: QG-019, QG-040, QG-011, QG-009, QG-005
- Patterns: [PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md), [PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md), [PAT-RS-007](PAT-RS-007-container-vs-media-queries.md), [PAT-RS-008](PAT-RS-008-responsive-typography-spacing.md), [PAT-DT-001](../desktop/PAT-DT-001-wide-layout-density.md), PAT-DT-007, PAT-DT-011, [PAT-MO-001](../mobile/PAT-MO-001-touch-target-size-spacing.md), PAT-MO-008

## Change log

- 2026-11-08 — Initial version (ADR-001).
