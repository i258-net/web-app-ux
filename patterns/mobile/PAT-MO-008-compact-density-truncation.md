---
id: PAT-MO-008
title: Compact density, truncation, line clamping, and horizontal carousels
type: pattern
scope: mobile
topics: [density, truncation, line-clamp, ellipsis, carousel, see-all, show-more, reflow, text-size, visual-hierarchy, comparison]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, keyboard, assistive-tech]
principles: [P-08, P-05, P-02, P-12]
dimensions: [D-05, D-06, D-08]
gates: [QG-009, QG-010, QG-011, QG-019, QG-040, QG-050]
related: [PAT-RS-003, PAT-RS-004, PAT-RS-008, PAT-RS-009, PAT-SH-014, PAT-SH-007, PAT-DT-007, PAT-MO-001, PAT-MO-006]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Compact density, truncation, line clamping, and horizontal carousels

## Problem

A compact viewport shows a fraction of a desktop. Teams either cram desktop density in — small text, tight rows, many controls per row — or remove information to look clean: one-line titles that make items indistinguishable, statuses dropped from rows, filter values cut off without "Show more", content pushed into horizontal carousels. With enlarged text, fixed-height rows clip.

What content goes first and what is deferred across viewports is PAT-RS-003; density tokens across window classes are PAT-RS-004; type scale is PAT-RS-008.

## Recommendation

**Outcome:** on a compact screen people can still identify, compare, and act on items; anything shortened is visibly shortened and can be expanded; layouts survive text enlargement and reflow.

**Density**

1. **Keep the information needed to choose** in each list row — the distinguishing title, the key attribute (price, status, date, owner) — and defer the rest to detail views. Decide by task, not by visual quietness.
2. **Do not shrink touch targets to gain density.** Rows and controls keep the 44–48 px recommended threshold for primary actions (QG-040), never below 24 px (QG-019). One primary action per row; others in an overflow (PAT-MO-001).
3. **Let rows grow.** Use intrinsic heights so rows expand with longer text and enlarged type (QG-009, QG-011). No fixed-height cards for variable content.

**Truncation and clamping**

4. **Truncate lists, not meaning.** For long option lists (filters, facets, tags), show the first few and a clearly labelled "Show all 24 brands" control; keep selected options visible even when collapsed.
5. **Clamp text only where the full text is one tap away** (a detail view or an expand control) and where the clamped portion still distinguishes items. Prefer clamping descriptions over titles; prefer two or three lines over one for titles that share prefixes.
6. **Truncate at the right end.** Where the unique part of a string is at the end (file names, account numbers), use middle truncation or show the tail.
7. **Make the full text available to assistive technology** — clamping is visual; the accessible name should not be truncated.
8. **Label disclosure precisely** ("Show 6 more", "Read full description") and keep its target at threshold size.

**Horizontal carousels and "see all"**

9. **Use horizontal scrollers for browsing samples, not for content people must see.** Show a partial next item so scrollability is visible; offer a "See all" link that opens the full list in a vertical layout.
10. **Do not nest horizontal scrollers inside one another** or put essential actions only at the end of a horizontal strip.
11. **Provide non-swipe controls** where the carousel is a primary way to navigate (previous/next buttons, a list view), and keep carousels keyboard-reachable (PAT-MO-006).
12. **Pass reflow:** at 320 CSS px, nothing outside a deliberate 2-D component requires horizontal scrolling (QG-010, QG-050).

Touch-capable tablets and laptops may use medium density with coarse-pointer targets; adapt by capability (PAT-RS-004, PAT-RS-009).

## Evidence

- **E1** W3C, "WCAG 2.2 — 1.4.10 Reflow, AA". https://www.w3.org/TR/WCAG22/#reflow — No two-dimensional scrolling at 320 CSS px width for vertically scrolling content, except where 2-D layout is essential.
- **E1** W3C, "WCAG 2.2 — 1.4.4 Resize Text, AA" and "1.4.12 Text Spacing, AA". https://www.w3.org/TR/WCAG22/#resize-text — Text resizable to 200% and spacing overrides without loss of content; fixed-height containers fail.
- **E2** Baymard Institute, "6 Guidelines for Truncation Design". https://baymard.com/research-articles/truncation-design — Truncating long filter-value lists preserved overview better than showing everything or nested scrolling, *if* users noticed the expansion control; otherwise they mistook a partial list for the full set. Applies to list truncation, not to text ellipsis.
- **E2** Baymard Institute, "Have a 'View All' Option in the Main Navigation at Each Level of the Mobile Product Catalog". https://baymard.com/research-articles/mobile-main-nav-view-all — Explicit "View All" wording made broad scope discoverable in mobile navigation. E-commerce.
- **E2** Baymard Institute, "Product List UX 2025". https://baymard.com/research-articles/current-state-product-list-and-filtering — Showing variants as separate items cluttered mobile lists; group true variants. E-commerce-specific.
- **E4** Nielsen Norman Group, "Aesthetic and Minimalist Design". https://www.nngroup.com/articles/aesthetic-minimalist-design/ — Remove noise, not utility; too few elements impair use.
- **E4** Nielsen Norman Group, "Progressive Disclosure". https://www.nngroup.com/articles/progressive-disclosure/ — Defer secondary options with an obvious, well-labelled route to them.
- **E3** Apple, "Human Interface Guidelines — Typography" and "Layout". https://developer.apple.com/design/human-interface-guidelines/typography.md — Layouts should grow, switch to vertical arrangements, and support multiple lines rather than crop text as type size increases.
- **E3** Google, "Material Design 3 — Canonical layouts (feed)". https://m3.material.io/foundations/layout/canonical-examples — Compact feeds stack full-width items; columns increase with space.
- **E4** Adrian Roselli, "A Responsive Accessible Table". https://adrianroselli.com/2017/11/a-responsive-accessible-table.html — Stacking table rows into cards can remove semantics and impede comparison (PAT-DT-007).

**Evidence gaps.** No source in this repository's findings tests text line-clamping or ellipsis, or compares horizontal carousels with vertical lists; points 5–6 and 9–11 are E4-level reasoning (ours), built from the list-truncation evidence and WCAG reflow.

## Alternatives and tradeoffs

- **Expand-in-place vs navigate to detail.** In-place expansion keeps context; navigation suits long content and gives a shareable URL.
- **User density toggle** (comfortable/compact) for expert users on touch, defaulting to comfortable (PAT-RS-004).
- **Grid of thumbnails** instead of a carousel for visual browsing — more items visible, no hidden horizontal scroll.
- **Data tables on compact:** keep comparison columns with a horizontally scrollable, keyboard-reachable table (the 2-D exception) rather than forcing cards when comparison is the task.

## Exceptions and failure modes

- Maps, media timelines, and data tables are legitimately 2-D (reflow exception), but the surrounding page must still reflow.
- Failures: one-line titles that make items identical; "…" with no way to expand; a "Show more" styled as body text; fixed-height cards that clip at 200% text; carousels holding required content; nested horizontal scroll; tiny pagination dots as the only carousel control (target-size failure).

## Evaluation questions

- Can a user tell list items apart and choose without opening each? [screenshot] [user study]
- Is every truncated element visibly truncated and expandable, with full text in the accessible name? [screenshot] [running app]
- At 200% text size and with text-spacing overrides, does anything clip or overlap? [running app] [automated]
- At 320 CSS px, is there horizontal page scroll outside deliberate 2-D components? [automated]
- Do carousels show a partial next item, offer "See all", and work without swipe? [screenshot] [running app]
- Do participants notice "Show more" on truncated lists? [user study]

## Related

- Principles: [P-08](../../principles/P-08-visual-hierarchy-readability.md), [P-05](../../principles/P-05-cognitive-clarity.md), [P-02](../../principles/P-02-discoverability-learnability.md), [P-12](../../principles/P-12-accessibility-inclusion.md); Dimensions: D-05, D-06, D-08; Gates: QG-009, QG-010, QG-011, QG-019, QG-040, QG-050 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-RS-003, PAT-RS-004, PAT-RS-008, PAT-RS-009, PAT-SH-014, PAT-SH-007, PAT-DT-007, PAT-MO-001, PAT-MO-006

## Change log

- 2026-11-08 — Initial version (ADR-001).
