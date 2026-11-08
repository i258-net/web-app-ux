---
id: PAT-SH-001
title: Navigation structure and wayfinding
type: pattern
scope: shared
topics: [navigation, wayfinding, breadcrumbs, information-architecture, current-location, deep-links]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-03, P-04, P-02, P-09]
dimensions: [D-02, D-10]
gates: [QG-051, QG-060, QG-061, QG-021, QG-004]
related: [PAT-MO-003, PAT-DT-002, PAT-RS-001, PAT-PW-003, PAT-SH-004, PAT-SH-008, PAT-SH-014]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Navigation structure and wayfinding

## Problem

People need to answer three questions on every screen: *where am I, what else is here, and how do I get back?* Web apps fail them by hiding destinations behind one menu control, using internal vocabulary, leaving the current location unmarked, landing deep links on pages with no visible parents, and fighting browser Back. Responsive apps add one more failure: phone navigation carried unchanged to a wide window.

## Recommendation

**Outcome:** at any viewport, users can reach the primary destinations, tell which one they are in, move up a meaningful hierarchy, and rely on browser Back.

1. **Derive the structure from users' groupings and words.** Label by user goals, not internal object names. Card sorting discovers groupings; a separate findability test (e.g. tree testing) validates the structure.
2. **Keep primary destinations visible where space allows**, with lower-priority ones in an overflow. Never hide all navigation behind one control on wide viewports. Adaptations: PAT-RS-001 (across widths), PAT-MO-003 (compact touch), PAT-DT-002 (sidebars, mega menus).
3. **Mark the current location** in the navigation itself (selected state with a non-color cue, exposed to assistive technology, e.g. `aria-current`), and in the page title and heading.
4. **Provide hierarchy cues for deep content.** Where the information model has meaningful ancestors, show a breadcrumb trail of *location* (not history). Keep trail items as usable targets on compact widths; truncate middle levels rather than wrapping into an unreadable block.
5. **Use real URLs.** Navigation items are `<a href>` links to addressable views, so new-tab, bookmark, and reload work (QG-061).
6. **Respect browser Back.** It returns to the previous meaningful state, closes page-like overlays, and never unexpectedly exits the app (QG-060; mechanics in PAT-PW-003).
7. **Keep destinations stable across widths** (QG-051): presentation changes, membership does not.
8. **Provide a bypass** for repeated navigation, and keep repeated help in a consistent relative order (QG-021).

## Evidence

- **E2** Nielsen Norman Group, "Hamburger Menus and Hidden Navigation Hurt UX Metrics". https://www.nngroup.com/articles/hamburger-menus/ — With 179 participants on 6 sites (2016), hidden navigation was used less and later and scored worse than visible or partly visible navigation, more so on desktop. A purely visible mobile condition was not fully tested.
- **E2** Nielsen Norman Group, "Mobile First Is NOT Mobile Only". https://www.nngroup.com/articles/mobile-first-not-mobile-only/ — Poor desktop navigation use was attributed to mobile patterns (hidden navigation, collapsed search) carried over to desktop.
- **E4** Nielsen Norman Group, "Basic Patterns for Mobile Navigation: A Primer". https://www.nngroup.com/articles/mobile-navigation-patterns/ — Visible navigation and tab bars are discoverable but cost space; menus fit more options but reduce discoverability.
- **E4** Nielsen Norman Group, "Breadcrumbs: 11 Design Guidelines for Desktop and Mobile". https://www.nngroup.com/articles/breadcrumbs/ — Breadcrumbs express hierarchy, help on direct entry to deep pages, supplement (not replace) global navigation; mobile trails need usable targets.
- **E4** Nielsen Norman Group, "User Control and Freedom". https://www.nngroup.com/articles/user-control-and-freedom/ — Back should return to the previous state; full-screen overlays that look like pages should close on Back.
- **E4** Nielsen Norman Group, "Card Sorting". https://www.nngroup.com/articles/card-sorting-definition/ — Card sorting reveals groupings; tree testing evaluates a structure. They are different methods.
- **E2** Baymard Institute, "Make Product Categories the Top-Level Navigation Items on Mobile Sites". https://baymard.com/research-articles/main-navigation-product-categories — Users abandoned when core categories were buried under a generic item. *E-commerce*; we infer the general lesson is to put the core task path at the first level.
- **E3** MDN Web Docs, "<a>: The Anchor element". https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a — Fake `href` values with click handlers break new-tab, copying, and bookmarking.
- **E1** W3C, "WCAG 2.2" (SC 2.4.1 Bypass Blocks). https://www.w3.org/TR/WCAG22/ — A mechanism to bypass repeated blocks is required.
- **E1** W3C, "WCAG 2.2 — SC 3.2.6 Consistent Help". https://www.w3.org/TR/WCAG22/#consistent-help — Repeated help mechanisms keep the same relative order.
- **E3** Apple, "Tab bars" / "Sidebars". https://developer.apple.com/design/human-interface-guidelines/tab-bars.md — Tab bars navigate sections, not commands, and can convert to a sidebar. Apple platforms only.
- **E3** Google Material Design, "Navigation bar / rail / drawer". https://m3.material.io/components/navigation-bar — Bars hold 3–5 destinations (compact/medium), rails 3–7 (medium and wider); Expressive no longer recommends drawers. Material products only.

## Alternatives and tradeoffs

- **Visible vs hidden navigation.** The E2 evidence favors visibility, but it comes from content websites in 2016. On compact screens, a menu can be justified when there are many destinations and visible chrome would crowd out content. We infer that the best default is a hybrid: the top priorities visible and the rest in a menu. Test it rather than assuming either extreme.
- **Top vs left navigation.** A small, stable set of destinations fits a top bar. Broad hierarchies favor a sidebar or grouped mega menu. NN/g reports test support for mega menus (E2) and recommends left navigation for broad hierarchies (E4). See PAT-DT-002.
- **Platform conventions disagree.** iPadOS favors a top tab bar that can convert to a sidebar. Material favors bottom bars on compact windows and rails on wider ones. Neither is a web rule. Pick one coherent strategy and keep destinations constant.
- **Breadcrumbs.** They are unnecessary in flat or linear apps, and in hierarchical apps they compete with local navigation for space. Omit them when there are no meaningful ancestors.

## Exceptions and failure modes

- Single-task flows (checkout, onboarding wizards) may legitimately suppress global navigation, but they still need a clear exit.
- Failure modes: breadcrumbs that echo history; in-app Back that differs from browser Back; color-only selected state; destinations that vanish at some breakpoints; `<div onclick>` navigation; a hamburger on a 1440 px window; team-only labels like "Hub".

## Evaluation questions

1. Are the primary destinations visible, or reachable in one action, at every supported viewport, and is the set identical across viewports? [screenshot] [running app]
2. Is the current location marked by more than color and exposed programmatically? [screenshot] [automated] [running app]
3. On a deep link to a nested page, can the user identify and reach its parent? [running app] [user study]
4. Does browser Back return to the previous meaningful state, including closing full-screen overlays, without leaving the app? [running app]
5. Can every destination be opened in a new tab, bookmarked, and reloaded to the same view? [running app] [automated]
6. Can a keyboard user skip repeated navigation? [running app] [automated]
7. Do representative users find target content using the labels as written? [user study]

## Related

- Principles: P-03, P-04, P-02, P-09
- Dimensions: D-02, D-10
- Gates: QG-051, QG-060, QG-061, QG-021, QG-004
- Patterns: PAT-MO-003 (compact navigation), PAT-DT-002 (sidebars, mega menus), PAT-RS-001 (navigation transformation), PAT-PW-003 (history and deep links), PAT-SH-004 (search as navigation), PAT-SH-008 (menus), PAT-SH-014 (disclosure)

## Change log

- 2026-11-08 — Initial version (ADR-001).
