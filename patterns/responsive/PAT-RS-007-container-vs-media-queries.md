---
id: PAT-RS-007
title: Container queries vs media queries — component-level vs page-level responsiveness
type: pattern
scope: responsive
topics: [container-queries, media-queries, components, design-systems, user-preferences, prefers-reduced-motion, prefers-color-scheme]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-09, P-08, P-12, P-15]
dimensions: [D-10, D-05, D-08]
gates: [QG-010, QG-050, QG-083, QG-042]
related: [PAT-RS-002, PAT-RS-004, PAT-RS-006, PAT-RS-008, PAT-RS-009, PAT-DT-001, PAT-DT-007]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Container queries vs media queries — component-level vs page-level responsiveness

## Problem

A card, a form row, or a chart is placed in several contexts: a full-width main column, a 320 px sidebar, a two-pane detail view, a dashboard tile. With only viewport media queries, the component styles itself for the *window*, not for the space it actually has. At 1440 px it decides it is "wide" while sitting in a 300 px pane, and it overflows or truncates. Teams then add context-specific overrides (`.sidebar .card {…}`) until the design system is unmaintainable. The opposite error also occurs: teams use container queries for things that really are page-wide or user-level, such as navigation form, reduced motion, or color scheme.

## Recommendation

**Outcome:** components adapt to the space they are given, wherever they are placed. Page structure and user or device conditions are decided once, at the page level.

1. **Use media queries for page-level and environment conditions:**
   - Page structure tied to window class: navigation form, pane count, page margins ([PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md)).
   - User preferences: `prefers-reduced-motion`, `prefers-color-scheme` (and `prefers-reduced-data` only as an optional enhancement; MDN reports it is not supported by default in any browser).
   - Input capabilities: `pointer`, `hover`, `any-pointer`, `any-hover` ([PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md)).
   - Display/environment: `display-mode` for installed PWAs (PAT-PW-001), viewport segments where supported ([PAT-RS-011](PAT-RS-011-orientation-foldables-hybrids.md)).
2. **Use size container queries for component internals:** whether a card shows its image beside or above its text, whether form labels sit beside or above fields, how many columns a tile grid uses, whether a toolbar collapses into overflow.
3. **Establish containers deliberately.** Mark layout regions (main, sidebar, pane, tile) with `container-type: inline-size` and, where needed, a `container-name`. A component cannot query its own size. It queries its nearest eligible ancestor container, so the slot, not the component, is the container.
4. **Design components with named size variants** (e.g. narrow < 400, regular, wide ≥ 700 container px) and document them in the design system. Test each variant in isolation and in each real slot.
5. **Keep source order stable across container variants.** Switching side-by-side to stacked must not reorder focus.
6. **Combine where needed, without duplication.** A component may use a container query for layout *and* a media query for `any-pointer: coarse` padding. These answer different questions.
7. **Prefer intrinsic techniques first.** `flex-wrap`, `grid-template-columns: repeat(auto-fit, minmax(…))`, and `clamp()` often remove the need for any query.
8. **Respect user preferences globally.** Reduced motion should be applied at the token or animation layer, not reimplemented per component (QG-083).

## Evidence

- **E3** MDN, "CSS container queries". https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries — Size container queries style descendants according to an eligible ancestor container rather than the viewport; `container-type: inline-size` establishes one; names select a particular container.
- **E3** Google (web.dev), "Micro layouts". https://web.dev/learn/design/micro-layouts — Component-level layout responds to its own available space, distinct from page-level macro layout.
- **E4** Google (web.dev), "Macro layouts". https://web.dev/learn/design/macro-layouts — Page-level structure with Grid/Flexbox and media queries for larger structural changes.
- **E4** Google (web.dev), "Media queries". https://web.dev/learn/design/media-queries — Media queries respond to viewport dimensions and other conditions; choose breakpoints by content.
- **E1** W3C, "Media Queries Level 4". https://www.w3.org/TR/mediaqueries-4/ — Defines `pointer`, `hover`, `any-pointer`, `any-hover` (Candidate Recommendation Draft).
- **E3** MDN, "prefers-reduced-motion". https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion — User preference to minimize nonessential motion.
- **E3** Google (web.dev), "Theming". https://web.dev/learn/design/theming — `prefers-color-scheme` selects styles by user preference; `color-scheme` lets built-in controls adapt.
- **E3** MDN, "prefers-reduced-data". https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-data — States the feature is not supported by any user agent; compatibility data lists Chromium behind a flag (checked 2026-11-08 in the research notes).
- **E4** Google (web.dev), "Accessibility". https://web.dev/learn/design/accessibility — CSS reordering does not change reading order.
- **E1** W3C, "WCAG 2.2 — 1.4.10 Reflow". https://www.w3.org/TR/WCAG22/#reflow — Components must still reflow at the 320 CSS px test width.

*Interpretation (ours):* the division "media for page and environment, container for component internals" follows MDN's framing (F-WP-04 in the research notes). Current browser support for container queries was not verified in the findings, so check MDN compatibility data before relying on them without a fallback.

## Alternatives and tradeoffs

- **Media queries only.** Adequate for small apps where each component appears in one context. Costs override complexity as the design system grows.
- **JavaScript ResizeObserver.** Works where container queries are unavailable or logic (not just style) must change, e.g. a chart choosing a different data density. Costs script and potential layout shift.
- **Container queries for page structure.** Possible (query the app shell), but splits structural decisions across mechanisms. Keep navigation form and pane count on media queries unless the shell itself is embedded.

## Exceptions and failure modes

- Forgetting to set `container-type`, so queries silently fall back to no match.
- Setting `container-type: size` (both axes) on elements whose height depends on content, collapsing them.
- Using container width to infer touch or hover.
- Components that look right in Storybook at fixed widths but were never tested in their real slots.
- Per-component `prefers-reduced-motion` handling that misses some animations.

## Evaluation questions

- Does each reusable component render correctly in every slot it is used in (main, sidebar, pane, tile) at the same viewport width? [running app] [screenshot]
- Are page structure decisions made by media queries and component internals by container queries, without overrides keyed to parent selectors? [automated]
- Does any container or media width query change input behavior? [automated]
- Does focus order stay stable when a component switches variants? [running app]
- Are user preferences (reduced motion, color scheme) honored across all components? [running app]

## Related

- Principles: [P-09](../../principles/P-09-consistency-familiarity.md), [P-08](../../principles/P-08-visual-hierarchy-readability.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-15](../../principles/P-15-craft-delight.md)
- Dimensions: D-10, D-05, D-08; Gates: QG-010, QG-050, QG-083, QG-042
- Patterns: [PAT-RS-002](PAT-RS-002-layout-reflow-canonical-layouts.md), [PAT-RS-004](PAT-RS-004-adaptive-density.md), [PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md), [PAT-RS-008](PAT-RS-008-responsive-typography-spacing.md), [PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md), [PAT-RS-011](PAT-RS-011-orientation-foldables-hybrids.md), [PAT-DT-001](../desktop/PAT-DT-001-wide-layout-density.md), PAT-DT-007

## Change log

- 2026-11-08 — Initial version (ADR-001).
