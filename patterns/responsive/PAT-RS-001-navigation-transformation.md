---
id: PAT-RS-001
title: Navigation transformation across window sizes — same destinations, different presentation
type: pattern
scope: responsive
topics: [navigation, responsive-navigation, tab-bar, navigation-rail, sidebar, drawer, destination-parity, wayfinding]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-04, P-03, P-02, P-09]
dimensions: [D-02, D-10, D-03]
gates: [QG-051, QG-004, QG-040, QG-019]
related: [PAT-MO-003, PAT-DT-002, PAT-SH-001, PAT-RS-002, PAT-RS-003, PAT-RS-006, PAT-RS-009, PAT-PW-001]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Navigation transformation across window sizes — same destinations, different presentation

## Problem

Primary navigation changes shape with the window: bottom bar, rail, sidebar or top bar. Teams design the two ends and let the middle happen by accident. Three failures recur:

1. **Parity loss.** A destination exists in the desktop sidebar but not in the compact bar or its overflow, or the reverse; users who switch devices or resize cannot find it.
2. **Mobile carried to desktop.** The hamburger and collapsed search stay at wide widths, hiding destinations for no reason.
3. **Width as modality.** "Mobile navigation" becomes touch-only, or the wide variant relies on hover flyouts.

This pattern governs the transformation. Compact choices are in [PAT-MO-003](../mobile/PAT-MO-003-bottom-vs-top-navigation.md); wide sidebars and hierarchy are in [PAT-DT-002](../desktop/PAT-DT-002-sidebar-hierarchical-navigation.md); structure and location cues are in [PAT-SH-001](../shared/PAT-SH-001-navigation-wayfinding.md).

## Recommendation

**Outcome:** at every window size, the same set of destinations is reachable, the current location is shown, and the most-used destinations are visible rather than hidden whenever space allows.

1. **Write a destination inventory and treat it as a contract.** List every top- and second-level destination with label, icon, and URL; every presentation renders from it. Parity is a release check: no destination exists in one window class only unless deliberately scoped and stated.
2. **Keep labels, order, icons, and URLs identical across presentations.**
3. **Use the space you have.** As width grows, *reveal* more: bar plus overflow, then rail, then labelled rail or sidebar with second-level items. No hamburger at expanded widths when destinations fit.
4. **A reasonable default sequence** (adapt to content; see [PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md)):
   - *compact (< 600):* 3–5 primary destinations in a bar, the rest in a labelled "More" or menu ([PAT-MO-003](../mobile/PAT-MO-003-bottom-vs-top-navigation.md)).
   - *medium (600–839):* rail at the leading edge, or keep the bar if a two-pane layout needs the width ([PAT-RS-002](PAT-RS-002-layout-reflow-canonical-layouts.md)).
   - *expanded and wider (≥ 840):* rail with labels or persistent sidebar; second-level items visible when the IA needs them ([PAT-DT-002](../desktop/PAT-DT-002-sidebar-hierarchical-navigation.md)).
5. **Transform without losing place.** On resize or rotation, keep the current destination selected, the current view open, and focus on an equivalent control. Do not reset to Home.
6. **Keep DOM and focus order meaningful** in every arrangement. Moving the bar from bottom to leading edge with CSS must not produce a confusing tab sequence (QG-004).
7. **Do not tie behavior to the presentation.** The compact bar still works with mouse and keyboard; the wide sidebar still works by touch. Flyouts open on click, tap, and Enter, not hover alone ([PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md)).
8. **Targets stay comfortable in every form.** Rails and collapsed sidebars are where icon targets shrink; keep them at 44–48 px on touch-capable devices (QG-040).

## Evidence

- **E2** Nielsen Norman Group, "Hamburger Menus and Hidden Navigation Hurt UX Metrics". https://www.nngroup.com/articles/hamburger-menus/ — In testing with 179 participants on 6 sites, hidden navigation was used less and later and performed worse on UX measures; the penalty was larger on desktop.
- **E2** Nielsen Norman Group, "Mobile First Is NOT Mobile Only". https://www.nngroup.com/articles/mobile-first-not-mobile-only/ — Attributes poor desktop navigation use to mobile patterns carried over (hidden navigation, collapsed search); each screen class's space should shape its design.
- **E4** Nielsen Norman Group, "Basic Patterns for Mobile Navigation: A Primer". https://www.nngroup.com/articles/mobile-navigation-patterns/ — Visible tabs are discoverable but space-consuming; menus fit more but reduce discoverability.
- **E3** Google, "Material Design 3 — Navigation bar". https://m3.material.io/components/navigation-bar — Bars carry 3–5 stable equal-priority destinations in compact/medium windows.
- **E3** Google, "Material Design 3 — Navigation rail". https://m3.material.io/components/navigation-rail — Rails carry 3–7 destinations in medium through extra-large windows at the leading edge.
- **E3** Google, "Material Design 3 — Navigation drawer". https://m3.material.io/components/navigation-drawer — Baseline guidance keeps standard drawers for expanded and wider and modal drawers for compact/medium; the May 2025 Expressive notice no longer recommends drawers and points to expanded rails. Pick one version coherently.
- **E3** Google, "Material Design 3 — Breakpoints". https://m3.material.io/foundations/layout/breakpoints — Window classes compact < 600dp, medium 600–839, expanded 840–1199, large 1200–1599, extra-large ≥ 1600; bars in compact, rails wider, with task-specific medium exceptions.
- **E3** Apple, "Human Interface Guidelines — Tab bars". https://developer.apple.com/design/human-interface-guidelines/tab-bars.md and "Sidebars". https://developer.apple.com/design/human-interface-guidelines/sidebars.md — iPadOS tab bar near the top can convert to a sidebar for broader destination sets; explain unavailable content rather than hiding tabs; sidebars usually expose up to two levels.
- **E3** Apple, "Human Interface Guidelines — Layout". https://developer.apple.com/design/human-interface-guidelines/layout.md — Functionality should remain the same as size classes change, although its visibility can change.
- **E1** W3C, "WCAG 2.2 — 2.4.3 Focus Order". https://www.w3.org/TR/WCAG22/#focus-order — Focus order must preserve meaning and operability after rearrangement.
*Interpretation (ours):* the "destination inventory as a contract" is a process recommendation derived from Apple's "functionality remains the same" guidance and the research notes' reading of Material navigation (F-SP-72); no source tests it directly.

## Alternatives and tradeoffs

- **Top navigation bar at every width.** Fine for content-led sites with few sections; at compact width it must become a visible-priorities-plus-overflow menu, not a lone hamburger.
- **Material rail vs Apple top-tab-to-sidebar.** Both are E3 conventions for their platforms. A web app can follow either; choose one per product and keep it consistent.
- **Medium window with bar vs rail.** Material allows keeping the bar or a modal rail when two panes need the width; this is legitimate when the list-detail task outweighs navigation visibility.

## Exceptions and failure modes

- Intentionally device-scoped destinations (e.g. a camera-scan flow only offered where a camera API exists) are acceptable when feature-detected and stated; they are not parity failures.
- Different labels for the same destination at different widths ("Inbox" vs "Messages").
- Breakpoints chosen per device rather than per content, causing nav to collide with logo or search at in-between widths.
- Hover-opened mega menus as the only route to second-level destinations.
- Navigation state (expanded groups, current item) lost on resize.

## Evaluation questions

- Does every destination in the inventory appear (visibly or in a labelled overflow) at compact, medium, and expanded widths? [screenshot] [running app]
- Is anything hidden behind a menu at expanded widths that would fit visibly? [screenshot]
- Are labels, order, and URLs identical across presentations? [screenshot] [automated]
- On resize across each transformation point, does the current destination and view persist? [running app]
- Is focus order sensible in each arrangement? [running app]
- Can users who learned the app on one size find a secondary destination on another? [user study]

## Related

- Principles: [P-04](../../principles/P-04-navigation-orientation.md), [P-03](../../principles/P-03-information-architecture.md), [P-02](../../principles/P-02-discoverability-learnability.md), [P-09](../../principles/P-09-consistency-familiarity.md)
- Dimensions: D-02, D-10, D-03; Gates: QG-051, QG-004, QG-040, QG-019
- Patterns: [PAT-MO-003](../mobile/PAT-MO-003-bottom-vs-top-navigation.md), [PAT-DT-002](../desktop/PAT-DT-002-sidebar-hierarchical-navigation.md), [PAT-SH-001](../shared/PAT-SH-001-navigation-wayfinding.md), [PAT-RS-002](PAT-RS-002-layout-reflow-canonical-layouts.md), [PAT-RS-003](PAT-RS-003-content-prioritization.md), [PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md), [PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md), PAT-PW-001

## Change log

- 2026-11-08 — Initial version (ADR-001).
