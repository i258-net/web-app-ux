---
id: PAT-RS-008
title: Responsive typography and spacing — bounded fluid type, minimum sizes, and measure
type: pattern
scope: responsive
topics: [typography, fluid-type, clamp, rem, line-length, measure, zoom, text-resize, text-spacing, localization]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-08, P-12, P-15, P-05]
dimensions: [D-05, D-08, D-06]
gates: [QG-009, QG-011, QG-030, QG-010]
related: [PAT-RS-004, PAT-RS-006, PAT-RS-007, PAT-DT-001, PAT-MO-008, PAT-SH-002]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Responsive typography and spacing — bounded fluid type, minimum sizes, and measure

## Problem

Type that is comfortable on a phone looks small and sparse on a 27-inch monitor, and desktop headline sizes overflow a 360 px screen. Teams respond in three ways that each cause problems:

- **Pure viewport units** (`font-size: 4vw`), which become tiny on narrow screens, huge on wide ones, and can blunt browser zoom.
- **Many hard-coded px steps per breakpoint**, which jump abruptly and ignore user font-size settings.
- **Fixed-height containers** that clip text when users enlarge it, override spacing, or switch to a language with longer words.

Line length is usually left to the container, so prose runs 150 characters wide on large windows.

## Recommendation

**Outcome:** text is legible at every width, scales with user settings and zoom, and reads at a comfortable measure. Layouts grow to fit text rather than clipping it.

1. **Base sizes in `rem`.** Respect the user's browser default font size; do not set the root to a fixed px value.
2. **Fluid type must be bounded and keep a `rem` term.** Use `clamp(min, preferred, max)` where the preferred value mixes `rem` and viewport units, e.g. `clamp(1rem, 0.75rem + 1.5vw, 2rem)` for a heading. This is a starting expression, not an accessibility guarantee.
   - Apply fluid scaling mainly to display and heading sizes. Body text can stay at a fixed `rem` size or vary only slightly.
   - Test that 200 % text enlargement still enlarges text noticeably at every width (QG-009). A large `vw` share can damp zoom.
3. **Set a minimum.** Body text should not shrink at compact widths; the `clamp()` minimum should equal the body size.
4. **Constrain prose measure** with a font-relative max width (e.g. `max-inline-size: 65ch` as a starting point) and verify the rendered character count. Apply it to text blocks, not to the app shell or data tables ([PAT-DT-001](../desktop/PAT-DT-001-wide-layout-density.md)).
5. **Scale spacing with type.** Use `rem`/`em` spacing tokens, optionally fluid with `clamp()`, so vertical rhythm keeps pace with type size ([PAT-RS-004](PAT-RS-004-adaptive-density.md)).
6. **Never clip text.** Use `min-block-size` rather than fixed heights; allow wrapping and multi-line labels; switch horizontal label/value pairs to stacked when text grows (container queries, [PAT-RS-007](PAT-RS-007-container-vs-media-queries.md)).
7. **Survive WCAG text-spacing overrides** (line height 1.5, paragraph spacing 2×, letter 0.12em, word 0.16em) without loss (QG-011). These are override-tolerance tests, not required defaults.
8. **Never disable zoom.** No `user-scalable=no` or restrictive `maximum-scale` (QG-030).
9. **Plan for localization.** Long words, diacritics, and other scripts need room; avoid fixed-width buttons and string-length assumptions; use logical properties.

## Evidence

- **E4** Google (web.dev), "Typography". https://web.dev/learn/design/typography — Combines viewport-relative sizing with relative units and `clamp()` for minimum, preferred, and maximum values; pure viewport sizing yields unsuitable extremes; manage line length and line height; `ch` measures the "0" glyph width, not an exact character count.
- **E4** Google (web.dev), "Accessibility". https://web.dev/learn/design/accessibility — Respect users who need larger text or zoom; do not disable zoom to make a layout fit.
- **E2** Baymard Institute, "Readability: The Optimal Line Length". https://baymard.com/research-articles/line-length-readability — Recommends 50–75 characters per line for body text; overly long product descriptions discouraged reading in e-commerce testing. Wider application is our interpretation.
- **E1** W3C, "WCAG 2.2 — 1.4.4 Resize Text". https://www.w3.org/TR/WCAG22/#resize-text — Text resizable to 200 % without assistive technology and without loss of content or functionality.
- **E1** W3C, "WCAG 2.2 — 1.4.12 Text Spacing". https://www.w3.org/TR/WCAG22/#text-spacing — No loss of content under the specified spacing overrides.
- **E1** W3C, "WCAG 2.2 — 1.4.10 Reflow". https://www.w3.org/TR/WCAG22/#reflow — Content reflows at the 320 CSS px test width.
- **E4** W3C, "WCAG2Mobile" (Group Draft Note). https://www.w3.org/TR/wcag2mobile-22/ — Informative: resize discussion reproduces WCAG2ICT on 200 % enlargement; the 2015 predecessor advises keeping pinch zoom and avoiding restrictive viewport settings.
- **E3** Apple, "Human Interface Guidelines — Typography". https://developer.apple.com/design/human-interface-guidelines/typography.md — Dynamic Type: layouts should grow, switch horizontal arrangements to vertical, expand row height, and support multiple lines rather than crop text. Native setting; CSS relative units do not by themselves provide Dynamic Type support.
- **E4** Google (web.dev), "Internationalization". https://web.dev/learn/design/internationalization — Languages vary in word length and vertical space for marks; use logical properties; avoid fixed-height text containers.

*Interpretation (ours):* `65ch` and the example `clamp()` are starting points to be verified with real fonts and content. No source here sets a universal type scale or minimum body size for web apps.

## Alternatives and tradeoffs

- **Stepped type scale per window class.** Predictable and easy to spec; abrupt jumps at boundaries are acceptable if each step is tested at both edges.
- **Fluid everything (type and spacing).** Smooth, but harder to reason about in design files, and zoom behavior needs careful testing.
- **Container-relative units (`cqi`)** let component headings scale to their slot; same zoom caveats as `vw`.

## Exceptions and failure modes

- Root font size set in px, ignoring user preferences.
- `clamp()` with a max equal to the min at compact widths, making zoom ineffective.
- Prose measure applied to the whole page, cramping tables.
- Truncation (`text-overflow: ellipsis`) on labels that users need to read in full (PAT-MO-008).
- Images of text that cannot be resized or translated.

## Evaluation questions

- Are font sizes in `rem` with bounded fluid expressions, and is the root size left to the user? [automated]
- At 200 % browser text size and at 400 % zoom, does text enlarge and reflow without clipping? [running app]
- With WCAG text-spacing overrides applied, is any text clipped or overlapping? [automated] [running app]
- Is prose measure roughly 50–75 characters at large widths, while tables use the full width? [screenshot]
- Is pinch-zoom enabled in the viewport meta? [automated]
- With a long-word language (or pseudo-localized strings), do buttons and labels still fit? [running app]

## Related

- Principles: [P-08](../../principles/P-08-visual-hierarchy-readability.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-15](../../principles/P-15-craft-delight.md), [P-05](../../principles/P-05-cognitive-clarity.md)
- Dimensions: D-05, D-08, D-06; Gates: QG-009, QG-011, QG-030, QG-010
- Patterns: [PAT-RS-004](PAT-RS-004-adaptive-density.md), [PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md), [PAT-RS-007](PAT-RS-007-container-vs-media-queries.md), [PAT-DT-001](../desktop/PAT-DT-001-wide-layout-density.md), PAT-MO-008, [PAT-SH-002](../shared/PAT-SH-002-form-fundamentals.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
