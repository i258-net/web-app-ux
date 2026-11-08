---
id: PAT-RS-003
title: Content prioritization across viewports — reorder and disclose, never remove function
type: pattern
scope: responsive
topics: [content-priority, progressive-disclosure, mobile-first, feature-parity, truncation, source-order, art-direction]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-05, P-01, P-03, P-02, P-08]
dimensions: [D-06, D-01, D-10, D-02]
gates: [QG-051, QG-004, QG-010]
related: [PAT-RS-001, PAT-RS-002, PAT-RS-005, PAT-RS-010, PAT-SH-014, PAT-MO-008, PAT-DT-001, PAT-DT-007]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Content prioritization across viewports — reorder and disclose, never remove function

## Problem

A compact screen shows only a fraction of what a wide one shows, so something has to come first and something has to wait. Two opposite errors follow:

- **Removal.** "Mobile-lite" views drop features, data columns, or settings at small widths ("use the desktop site for that"). Users on phones, people in narrow windows, and people at 200–400 % zoom then cannot finish real tasks.
- **No prioritization.** The desktop page is stacked into one column in source order, so the primary task sits below promotional blocks, metadata, and secondary panels.

Mobile-first is often read as "design the phone version and stop", which turns into mobile-only.

## Recommendation

**Outcome:** on every viewport the user's primary task and the information needed for it come first. Secondary content and functions are deferred, collapsed, or moved, but stay reachable. Nothing a user can do on a wide window is impossible on a narrow one unless it is intrinsically device-bound.

1. **Rank content by task, not by layout.** For each screen, list content and actions as *primary* (needed for the main task), *supporting* (needed sometimes), and *peripheral*. Base this on task analysis or analytics, not on what fits.
2. **Source order = priority order.** Put primary content first in the DOM. Wide layouts then *place* supporting content beside it. This also keeps reading and focus order sensible (QG-004).
3. **On compact, defer rather than delete.**
   - Collapse supporting sections behind clearly labelled disclosures ("Specifications", "Activity"), not ambiguous icons.
   - Truncate long value lists with an explicit "Show all N" control; keep selected items visible.
   - Move secondary actions into a labelled overflow menu (PAT-SH-008), keeping the primary action visible ([PAT-RS-005](PAT-RS-005-control-positioning.md)).
   - Hide lower-priority table columns only with a visible control to reveal them, and say that columns are hidden.
4. **On wide windows, reveal rather than stretch.** Use the extra space to show supporting content simultaneously (side panes, more columns, visible secondary navigation) instead of enlarging the compact design ([PAT-RS-002](PAT-RS-002-layout-reflow-canonical-layouts.md)).
5. **Keep meaning in images.** If an art-directed crop is used on compact, it must not remove information that the surrounding text refers to.
6. **Parity checklist.** For each feature, record where it lives at compact, medium, and expanded. A blank cell is a bug unless the feature is device-bound (camera, hardware API) and feature-detected.
7. **Verify with zoom.** 400 % zoom on a 1280 px desktop produces roughly a 320 CSS px layout. If something has been "removed on mobile", a desktop user loses it too.

## Evidence

- **E2** Nielsen Norman Group, "Mobile User Experience: Limitations and Strengths". https://www.nngroup.com/articles/mobile-ux/ — Repeated mobile studies describe small viewports, fragmented attention, and limited overview; recommends preserving state and context.
- **E2** Nielsen Norman Group, "Mobile First Is NOT Mobile Only". https://www.nngroup.com/articles/mobile-first-not-mobile-only/ — Mobile patterns carried to desktop harmed use; each screen's space and needs should shape its design while preserving capabilities.
- **E2** Baymard Institute, "Mobile E-Commerce UX". https://baymard.com/research/mcommerce-usability — Mobile research emphasizes loss of page overview; even better-performing mobile patterns remain compromises. E-commerce context; likely generalizes to content-heavy apps.
- **E2** Baymard Institute, "6 Guidelines for Truncation Design". https://baymard.com/research-articles/truncation-design — Truncating long value lists preserved overview better than showing all or nested scrolling, *if* users noticed the expansion control; otherwise they took the partial list as complete.
- **E4** Nielsen Norman Group, "Progressive Disclosure". https://www.nngroup.com/articles/progressive-disclosure/ — Defer advanced or rare options; the split must match real task importance and the route to more must be obvious and labelled.
- **E4** Nielsen Norman Group, "Aesthetic and Minimalist Design". https://www.nngroup.com/articles/aesthetic-minimalist-design/ — Minimalism removes noise, not useful elements; too few elements impair utility.
- **E4** Nielsen Norman Group, "Data Tables: Four Major User Tasks". https://www.nngroup.com/articles/data-tables/ — Indicate clearly when columns are hidden; provide discoverable hiding/reordering.
- **E3** Apple, "Human Interface Guidelines — Layout". https://developer.apple.com/design/human-interface-guidelines/layout.md — Functionality should remain the same as size classes change, although its visibility can change.
- **E4** Google (web.dev), "Introduction" (Learn Responsive Design). https://web.dev/learn/design/intro — Responsive design adapts to devices and user needs, including interaction mechanisms and preferences, not only phone layouts.
- **E3** Google (web.dev), "The picture element". https://web.dev/learn/design/picture-element — Art direction via `<picture>`; `img` remains the fallback carrying alternative text.
- **E1** W3C, "WCAG 2.2 — 1.4.10 Reflow". https://www.w3.org/TR/WCAG22/#reflow — Content and functionality must be retained at the 320 CSS px test width.

*Interpretation (ours):* the zoom equivalence (400 % at 1280 px ≈ 320 CSS px) is arithmetic consistent with the reflow criterion's intent. The "parity checklist" is a process recommendation.

## Alternatives and tradeoffs

- **Separate task-specific mobile flows** (e.g. a "quick capture" screen) are legitimate when users really do different things on the go, as long as the full flow is still reachable.
- **Tabs vs accordions vs stacked sections** on compact: tabs hide siblings, accordions suit selective reading, and long stacked pages suit reading everything. Choose by how much of the content users typically need (PAT-SH-014).
- **Feature-flagging by width** saves engineering effort but is a parity failure; scope by capability instead.

## Exceptions and failure modes

- Device-bound features (camera capture, NFC, file system access) may be absent where the capability is absent. Detect the capability; do not infer it from width.
- "Show more" styled as plain text, so users read the truncated list as complete.
- Promotional or decorative blocks first in source order, pushing the task below.
- Hiding the price, status, or error that the primary task depends on to save space.
- Settings available only on desktop.

## Evaluation questions

- For each key screen, what is the primary task, and is its content first at compact width? [screenshot]
- Is any feature or data field available at expanded width but unreachable at compact width or at 400 % zoom? [running app]
- Are collapsed and truncated regions labelled so that hidden content is obvious? [screenshot]
- Is DOM order the same as priority order? [automated] [running app]
- Do participants find a deferred function on compact without prompting? [user study]

## Related

- Principles: [P-05](../../principles/P-05-cognitive-clarity.md), [P-01](../../principles/P-01-task-effectiveness.md), [P-03](../../principles/P-03-information-architecture.md), [P-02](../../principles/P-02-discoverability-learnability.md), [P-08](../../principles/P-08-visual-hierarchy-readability.md)
- Dimensions: D-06, D-01, D-10, D-02; Gates: QG-051, QG-004, QG-010
- Patterns: [PAT-RS-001](PAT-RS-001-navigation-transformation.md), [PAT-RS-002](PAT-RS-002-layout-reflow-canonical-layouts.md), [PAT-RS-005](PAT-RS-005-control-positioning.md), [PAT-RS-010](PAT-RS-010-same-task-different-interaction.md), PAT-SH-014, PAT-MO-008, [PAT-DT-001](../desktop/PAT-DT-001-wide-layout-density.md), PAT-DT-007

## Change log

- 2026-11-08 — Initial version (ADR-001).
