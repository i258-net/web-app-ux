---
id: PAT-MO-010
title: Scrolling, sticky headers and action bars, and pull-to-refresh
type: pattern
scope: mobile
topics: [scrolling, sticky-header, sticky-footer, action-bar, hide-on-scroll, pull-to-refresh, scroll-jank, overscroll, scroll-restoration]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, keyboard, assistive-tech]
principles: [P-13, P-06, P-04, P-10]
dimensions: [D-09, D-03, D-02]
gates: [QG-006, QG-053, QG-063, QG-081, QG-082, QG-083, QG-040]
related: [PAT-MO-001, PAT-MO-002, PAT-MO-003, PAT-MO-004, PAT-MO-007, PAT-MO-009, PAT-MO-011, PAT-SH-007, PAT-PW-004, PAT-PW-006, PAT-DT-007, PAT-RS-005]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Scrolling, sticky headers and action bars, and pull-to-refresh

## Problem

On a compact screen, every pixel of persistent chrome is a pixel of content lost. A sticky header plus a sticky filter bar plus a cookie banner plus a bottom navigation bar plus a sticky "Add to cart" can leave a sliver of content, especially in landscape or with the keyboard open. Sticky elements also cover focused fields and anchored headings, jump in and out distractingly, or shrink their buttons below comfortable size. Scrolling itself breaks: custom scroll containers stutter, inner panes chain into the page, a custom pull-to-refresh fights the browser's own, and returning from a detail view loses the user's place in a long list.

## Recommendation

**Outcome:** persistent controls are there when needed, cost little space, never hide what the user is working on, and scrolling stays smooth and position-preserving.

**Sticky chrome**

1. **Make something sticky only if users need it continuously** — global navigation (PAT-MO-003), a primary action in a long task (checkout total + Continue), table headers during comparison (PAT-DT-007), the current section title in long content. Otherwise let it scroll away.
2. **Budget the total.** Assess header + sub-bars + bottom bars + banners together, in portrait *and* landscape, and with the keyboard open. Collapse or merge bars before adding another.
3. **Keep sticky bars small but not their targets.** Compact the visual, not the hit areas (QG-040, PAT-MO-001).
4. **Partially persistent headers** (hide on scroll down, reveal on scroll up) recover space while keeping access; use modest, quick motion and respect reduced-motion preferences (QG-083).
5. **Never cover focus.** Sticky headers and footers must not entirely hide a focused element (QG-006) — set `scroll-padding-top`/`bottom` to the bar heights so focus and anchor jumps land below them — and must not obscure the focused field or submit control when the virtual keyboard is open (QG-053, PAT-MO-004).
6. **Pad for safe areas and leave room at the end.** Bottom bars respect `env(safe-area-inset-bottom)` (PAT-MO-009) and the content gets enough bottom padding that the last item is reachable above them.
7. **Implement sticky with `position: sticky`** where possible (it needs an inset such as `top`, and sticks within its nearest scrolling ancestor) rather than script that repositions elements on scroll.

**Scrolling behaviour**

8. **Use the document as the main scroller** where feasible; nested full-height scroll containers break browser chrome collapse, scroll restoration, and some AT behaviour.
9. **Contain inner scrollers** (sheets, drawers, side panes) with `overscroll-behavior: contain` so they do not chain into the page (PAT-MO-007, PAT-MO-011).
10. **Restore scroll position** when users return to a list (QG-063, PAT-SH-007, PAT-PW-004).
11. **Keep scrolling smooth**: avoid layout work on scroll; watch layout shift from bars appearing (QG-082). Scroll smoothness is continuous interaction, which INP (QG-081) does not measure; verify on a device and with frame/main-thread traces.

**Pull-to-refresh**

12. **Rely on the browser's refresh where it exists** (MDN notes mobile browsers may reload the page on overscroll at the top); in an installed PWA or a custom scroller, a custom pull-to-refresh is acceptable as an accelerator, but **also provide a visible Refresh control or automatic refresh** and show freshness (PAT-PW-006). Disable browser pull-to-refresh only on surfaces where it conflicts with the task, using `overscroll-behavior`.

Sticky bars on tablets and touch laptops follow the same budget; on wide windows, persistent chrome is cheaper and side placement often replaces bottom bars (PAT-RS-005).

## Evidence

- **E4** Nielsen Norman Group, "Sticky Headers: 5 Ways to Make Them Better". https://www.nngroup.com/articles/sticky-headers/ — Small, readable, clearly differentiated sticky headers with minimal motion; consider whether persistence is needed; partially persistent headers restore access on upward scroll.
- **E1** W3C, "WCAG 2.2 — 2.4.11 Focus Not Obscured (Minimum), AA". https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum — Author-created content must not entirely hide a focused component; explicitly relevant to sticky bars.
- **E3** MDN, "position" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/CSS/position — `sticky` offsets relative to the nearest scrolling ancestor, needs a non-`auto` inset on the sticky axis, and stays stuck until the opposite edge of its containing block; notes that fixed or sticky content repainted during scroll can cause jank. Baseline widely available.
- **E3** MDN, "overscroll-behavior" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior — Prevents scroll chaining and pull-to-refresh-type behaviour on scroll containers; limited availability.
- **E3** MDN, "env()" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/CSS/env — Example pads a sticky footer with `env(safe-area-inset-bottom)`.
- **E4** Nielsen Norman Group, "Infinite Scrolling: When to Use It, When to Avoid It". https://www.nngroup.com/articles/infinite-scrolling-tips/ — Refinding and footer access problems; preserve list position when returning from details.
- **E3** Google, "Material Design 3 — Floating action button". https://m3.material.io/components/floating-action-button — Key action persists while content scrolls.
- **E5** Mobbin, "Mobile Pull To Refresh Screens". https://mobbin.com/explore/mobile/screens/pull-to-refresh — Pull-to-refresh recurs in shipped apps; discoverability and alternatives not demonstrated.

**Evidence gaps.** No source here measures a maximum acceptable sticky-chrome height, compares hide-on-scroll with always-visible bars, or tests pull-to-refresh usability in web apps. Points 2, 8, and 12 are our reasoning (E4 level). `scroll-padding` is named as an implementation candidate and was not separately verified for this pattern.

## Alternatives and tradeoffs

- **Always-visible vs hide-on-scroll.** Always-visible is predictable and better for frequent actions; hide-on-scroll saves space for reading but makes controls intermittently absent and adds motion.
- **Inline actions at the end of content** instead of sticky ones work for short pages; long tasks benefit from a sticky primary action.

## Exceptions and failure modes

- Reading-focused views (articles, documents) often need no sticky chrome beyond a slim, scrolling-away header.
- Failures: stacked sticky bars consuming a large share of landscape height; a cookie banner over the submit button; sticky footer riding over the keyboard; anchor links landing under the header; bars that shrink buttons; scroll-linked script animations that stutter; a custom pull-to-refresh in a browser tab that also triggers the browser's; list position lost after Back.

## Evaluation questions

- With all sticky elements visible, how much content remains in portrait, landscape, and with the keyboard open? [screenshot] [running app]
- Does any sticky element hide a focused control or an anchored heading? [running app]
- Do sticky bars keep targets ≥ 44 px and respect safe areas? [screenshot] [running app]
- Is scroll position restored on Back in long lists? [running app]
- Is scrolling smooth on a mid-range device (frame drops observed, not inferred from INP)? [running app] Is it free of layout shift as bars appear? [running app] [automated]
- Is there a non-gesture way to refresh? [running app]
- Do participants find hide-on-scroll navigation when they need it? [user study]

## Related

- Principles: [P-13](../../principles/P-13-performance-responsiveness.md), [P-06](../../principles/P-06-interaction-ergonomics.md), [P-04](../../principles/P-04-navigation-orientation.md), [P-10](../../principles/P-10-feedback-predictability.md); Dimensions: D-09, D-03, D-02; Gates: QG-006, QG-053, QG-063, QG-081, QG-082, QG-083, QG-040 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-MO-001, PAT-MO-002, PAT-MO-003, PAT-MO-004, PAT-MO-007, PAT-MO-009, PAT-MO-011, PAT-SH-007, PAT-PW-004, PAT-PW-006, PAT-DT-007, PAT-RS-005

## Change log

- 2026-11-08 — Initial version (ADR-001).
