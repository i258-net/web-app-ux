---
id: PAT-DT-002
title: Sidebars and hierarchical navigation on wide windows
type: pattern
scope: desktop
topics: [navigation, sidebar, left-nav, top-nav, mega-menu, collapsible, hierarchy, breadcrumbs, skip-link]
platforms: [desktop, tablet]
viewports: [expanded, large, extra-large]
inputs: [pointer, keyboard, touch, assistive-tech]
principles: [P-03, P-04, P-02, P-12]
dimensions: [D-02, D-03, D-08]
gates: [QG-001, QG-004, QG-005, QG-051, QG-061]
related: [PAT-SH-001, PAT-RS-001, PAT-DT-001, PAT-DT-003, PAT-DT-004, PAT-DT-010, PAT-MO-003]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Sidebars and hierarchical navigation on wide windows

## Problem

Web apps with many destinations, such as workspaces, projects, settings, and reports, need navigation that people can scan and that stays usable as the product grows. On wide windows, teams often carry over a phone-era hamburger menu and hide everything. Others jam vague one-word labels into a horizontal bar, or render a whole tree five levels deep in the sidebar. Keyboard users then tab through dozens of links on every page. This pattern covers the wide-window form of navigation. Universal wayfinding (location cues, labeling, breadcrumbs) lives in PAT-SH-001, and the cross-viewport transformation lives in PAT-RS-001.

## Recommendation

**Outcome:** on expanded and larger windows, primary destinations are visible without opening anything. The current location is obvious. The hierarchy shows the relevant branch, not the whole tree. People can collapse the navigation and restore it.

1. **Show navigation when space allows.** Do not hide primary destinations behind a menu button on expanded or wider windows.
2. **Pick top or left from the structure.** Use a **left vertical sidebar** when the set of destinations is broad, growing, or has longer labels. Use a **top bar** for a small, stable set of short, clear labels. In content-heavy sites with broad hierarchies, a **grouped mega menu** can show lower levels together (see PAT-DT-003 for hover activation).
3. **Limit depth in the sidebar.** Show about two levels and use disclosure for longer sections. Move deeper levels into the content area: a list pane, a page, or a breadcrumb trail. Use real disclosure buttons with `aria-expanded`, not clickable headings.
4. **Mark the current location persistently.** Highlight the current destination and the selected item that led to a detail view, and expose it with `aria-current`. Keep that state through reload and deep links (QG-061).
5. **Make collapse reversible and labeled.** Users can hide the sidebar, and a persistent, labeled control brings it back. Do not hide the sidebar by default. Collapsing to an icon rail is acceptable only if each icon has a visible label on focus or hover *and* an accessible name. Unlabeled icons alone are not acceptable. Remember the user's choice.
6. **Collapse automatically on narrow windows.** When a desktop window shrinks, collapse to a rail or drawer instead of crushing content. Restore when space returns, and keep every destination reachable (QG-051, PAT-DT-010).
7. **Keep keyboard costs low.** Provide a skip link or landmark structure so people can bypass repeated navigation (WCAG 2.4.1). Sidebar links are ordinary links in the Tab order. Do not turn them into an ARIA `menu`, which brings in a different keyboard contract (PAT-DT-004). Focus order follows visual order (QG-004).
8. **Use real links.** Every destination is an `<a href>` so it can be opened in a new tab, bookmarked, and copied (PAT-DT-010).

## Evidence

- **E2** Nielsen Norman Group, "Hamburger Menus and Hidden Navigation Hurt UX Metrics". https://www.nngroup.com/articles/hamburger-menus/. Hidden navigation was used less and later and performed worse than visible navigation, with a larger penalty on desktop (F-NB-13).
- **E2** Nielsen Norman Group, "Mega Menus Work Well for Site Navigation". https://www.nngroup.com/articles/mega-menus-work-well/. User-testing support for grouped panels that show many choices together (F-DX-07). This was tested on site navigation, not app sidebars.
- **E4** Nielsen Norman Group, "Left-Side Vertical Navigation on Desktop". https://www.nngroup.com/articles/vertical-nav/. Recommends left navigation for broad or growing hierarchies and warns against vague labels squeezed into a top bar (F-DX-06).
- **E3** Apple Human Interface Guidelines, "Sidebars". https://developer.apple.com/design/human-interface-guidelines/sidebars.md. Let people hide and reveal the sidebar, avoid hiding it by default, collapse it in narrow windows, and generally show no more than two levels (F-DX-08, F-DX-09, F-SP-52).
- **E3** Google Material Design, navigation rail and drawer. https://m3.material.io/components/navigation-rail. Rails support 3–7 destinations in medium and larger windows. M3 Expressive replaces drawers with expanded rails (F-SP-72). This is a Material-version convention.
- **E4** Nielsen Norman Group, "Breadcrumbs: 11 Design Guidelines". https://www.nngroup.com/articles/breadcrumbs/. Breadcrumbs supplement global and local navigation for deep pages (F-DX-10).
- **E1** W3C, WCAG 2.2 SC 2.4.1 Bypass Blocks. https://www.w3.org/TR/WCAG22/. Requires a way to bypass repeated blocks (F-DX-25).
- **E3** MDN, "<a>: The Anchor element". https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a. Fake links break new-tab, copy, and bookmark (F-DX-41).
- **E5** Mobbin, "Web Side Navigation UI". https://mobbin.com/explore/web/ui-elements/side-navigation. Side navigation recurs in shipped web apps (F-DX-60). This is convention observed, not proof of usability.

## Alternatives and tradeoffs

- **Top bar vs. sidebar.** A top bar saves width for content and suits five to seven stable destinations. A sidebar scales and is easier to scan, but it permanently takes width away from content. Apple's two-level limit and NN/g's mega-menu support describe different structures. Neither is a universal rule.
- **Icon rail by default.** A rail saves space for experts who know the icons. It hurts discoverability for newcomers, so use it as a collapsed state, not the default.
- **Mega menu vs. sidebar.** A mega menu suits browsing a large site. A sidebar suits switching repeatedly between app areas.
- **Platform version.** Material's drawer guidance changed with M3 Expressive. Pick one documented version and apply it consistently.

## Exceptions and failure modes

- Focused, single-task flows (checkout, onboarding, editors in focus mode) may hide global navigation on purpose. They still need a clear exit.
- A sidebar that scrolls the content along with it, or has no focus-visible styles.
- Collapse controls that are icon-only with no accessible name.
- Rendering the full tree, which makes keyboard traversal and scanning expensive.
- Navigation that differs in *destinations*, not just in presentation, between wide and narrow windows. This breaks parity (PAT-RS-001).

## Evaluation questions

- At 1280 px and wider, are primary destinations visible without opening a menu? [screenshot]
- Is the current destination marked visually and with `aria-current`? [screenshot] [automated]
- Does the sidebar show at most about two levels, with deeper content in the main area? [screenshot]
- Can the sidebar be collapsed and restored with a labeled control, and is the choice remembered? [running app]
- When the window is narrowed to about 900 px, does navigation collapse with every destination still reachable? [running app]
- Does a skip link or landmark structure let keyboard users bypass the sidebar? [running app] [automated]
- Can each destination be opened in a new tab? [running app]
- Do first-time users find a second-level destination without help? [user study]

## Related

- Patterns: PAT-SH-001, PAT-RS-001, PAT-MO-003, [PAT-DT-001](PAT-DT-001-wide-layout-density.md), [PAT-DT-003](PAT-DT-003-hover-tooltips.md), [PAT-DT-004](PAT-DT-004-keyboard-navigation-shortcuts.md), [PAT-DT-010](PAT-DT-010-multi-window-resize.md)
- Principles: [P-03](../../principles/P-03-information-architecture.md), [P-04](../../principles/P-04-navigation-orientation.md), [P-02](../../principles/P-02-discoverability-learnability.md), [P-12](../../principles/P-12-accessibility-inclusion.md)
- Rubric: [D-02, D-03, D-08](../../rubric/dimensions.md); gates [QG-001, QG-004, QG-005, QG-051, QG-061](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
