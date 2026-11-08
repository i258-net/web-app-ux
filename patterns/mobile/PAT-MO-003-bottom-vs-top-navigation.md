---
id: PAT-MO-003
title: Bottom tab bar vs top bar vs navigation drawer on compact screens
type: pattern
scope: mobile
topics: [navigation, tab-bar, bottom-navigation, hamburger, drawer, top-app-bar, labels]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, keyboard, assistive-tech]
principles: [P-04, P-02, P-03, P-09]
dimensions: [D-02, D-03, D-10]
gates: [QG-051, QG-019, QG-040]
related: [PAT-SH-001, PAT-RS-001, PAT-MO-002, PAT-MO-009, PAT-MO-010, PAT-PW-001, PAT-PW-003]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Bottom tab bar vs top bar vs navigation drawer on compact screens

## Problem

A compact viewport cannot show a desktop navigation bar. Teams choose a bottom tab bar, a top bar with tabs or links, or a hamburger drawer — often by copying another product. Each trades discoverability against space: an all-hidden hamburger hides destinations; seven icon-only tabs are cryptic and tiny; a bottom bar in a browser tab can collide with the browser toolbar and home indicator.

This pattern covers the compact-touch choice. Global structure, current-location cues, and depth belong to PAT-SH-001; how the same destinations transform at wider widths belongs to PAT-RS-001.

## Recommendation

**Outcome:** people can see, or reach in one obvious step, the few destinations they use most, can tell where they are, and the navigation costs as little content space as the task allows.

1. **Count and rank destinations first.** Identify top-level sections by frequency of use and task importance (see PAT-SH-001 for IA research).
2. **3–5 stable, equal-rank, frequently switched destinations → persistent tab bar.** Use text labels with icons; icon-only tabs are acceptable only for universally recognised symbols and still need accessible names. Tabs navigate between sections; they do not run commands (put "New", "Share", etc. in the view's toolbar or a primary action, PAT-MO-002).
3. **More destinations, or rarely switched sections → visible priorities plus overflow.** Keep the 2–4 most important destinations visible (tabs or top links) and put the rest in a clearly labelled "More" or menu. Do not hide *everything* behind a hamburger when a few destinations dominate use.
4. **Deep hierarchies → top bar with back/up and title, plus search** where search is a primary finding route. The top bar shows location and hierarchy; it is not a substitute for top-level destinations.
5. **Position.** Bottom placement is nearer the thumb for many grips (PAT-MO-002) and matches Material compact and iPhone conventions. Top placement is legitimate where users expect it (content sites, current iPadOS) or where a bottom bar would collide with browser chrome. Neither is shown to be universally superior in these sources; test.
6. **Show the current destination** beyond colour and via `aria-current="page"`.
7. **Respect the edge.** Pad a fixed bottom bar with `env(safe-area-inset-bottom)` (PAT-MO-009); in installed PWAs verify back affordances (PAT-PW-001, PAT-PW-003).
8. **Keep tab targets at 44–48 px** (QG-040).
9. **Preserve tab state** (scroll, sub-view) on return.

Touch also occurs on tablets and touch laptops; a medium or expanded window typically moves to a rail or sidebar (PAT-RS-001), and input should be detected, not inferred from width (PAT-RS-009).

## Evidence

- **E2** Nielsen Norman Group, "Hamburger Menus and Hidden Navigation Hurt UX Metrics". https://www.nngroup.com/articles/hamburger-menus/ — In testing with 179 participants on 6 sites (2016), hidden navigation was used less and later and performed worse than visible or partly visible navigation; the penalty was larger on desktop, and a purely visible mobile condition was not fully tested. Supports "visible priorities plus overflow" over all-hidden.
- **E4** Nielsen Norman Group, "Basic Patterns for Mobile Navigation: A Primer". https://www.nngroup.com/articles/mobile-navigation-patterns/ — Tab bars are discoverable but consume space and do not scale to many destinations; hamburger menus fit more but reduce discoverability. Its tab-position examples reflect 2015 native conventions.
- **E3** Google, "Material Design 3 — Navigation bar". https://m3.material.io/components/navigation-bar — Navigation bars carry 3–5 stable, equal-priority destinations in compact/medium windows; rails take over at wider widths. The May 2025 Expressive update no longer recommends drawers, favouring expanded rails.
- **E3** Apple, "Human Interface Guidelines — Tab bars". https://developer.apple.com/design/human-interface-guidelines/tab-bars.md — Tab bars navigate top-level sections rather than execute commands; labels aid navigation; avoid overflow; explain unavailable content rather than hiding or disabling tabs; aim for five or fewer default items where tabs are customisable; current iPadOS places the tab bar near the top with optional sidebar conversion.
- **E3** Apple, "Human Interface Guidelines — Toolbars". https://developer.apple.com/design/human-interface-guidelines/toolbars.md — The top navigation toolbar traverses hierarchy with consistent Back/Close; view actions are separate from top-level destinations.
- **E2** Baymard Institute, "Make Product Categories the Top-Level Navigation Items on Mobile Sites". https://baymard.com/research-articles/main-navigation-product-categories — In e-commerce testing, users abandoned when core categories were buried under a generic first-level item. Likely generalises as "put core-task entry points at the first menu level"; retail taxonomy itself does not.
- **E5** Mobbin, "Mobile Tab Bar UI". https://mobbin.com/explore/mobile/ui-elements/tab-bar — Tab bars recur in shipped apps; convention observed, usability unverified.

*Interpretation (ours):* the 3–5 threshold is a platform convention, not an empirical optimum. No source here compares bottom and top tab placement in a controlled test for web apps.

## Alternatives and tradeoffs

- **Hamburger/drawer only.** Acceptable for apps with many equal-weight sections that users rarely switch between, or content sites where search and in-page links carry most navigation. Costs discoverability (E2 above).
- **Scrollable top tabs.** Works for peer categories within one section (e.g. feed filters); items beyond the edge are less discoverable — show a partial item to signal more (PAT-MO-008).
- **Bottom bar in a browser tab** stacks with bottom browser toolbars; consider top navigation for browser-first sites, bottom tabs for app-like or installed experiences, and test.
- **Hide-on-scroll bars** recover space but make navigation intermittently unavailable (PAT-MO-010).

## Exceptions and failure modes

- A "+" tab that opens a composer breaks the tab model; if used, make it distinct and expose it as a button.
- Failures: ambiguous icon-only tabs; a sixth tab squeezed below 44 px; different destinations at compact and wide widths (PAT-RS-001); a fixed bar covering the focused field (PAT-MO-004) or the last list item.

## Evaluation questions

- How many top-level destinations exist, and does the chosen pattern match that count and their usage frequency? [screenshot] [prototype]
- Are tabs labelled, ≥ 44 px, and is the current tab indicated beyond colour and via `aria-current`? [screenshot] [automated]
- Is any tab actually a command? [screenshot]
- Does a fixed bottom bar respect safe-area insets and avoid browser chrome and the keyboard? [running app]
- Is tab state (scroll, sub-view) restored on return? [running app]
- Can participants find a secondary destination hidden in overflow without prompting? [user study]

## Related

- Principles: [P-04](../../principles/P-04-navigation-orientation.md), [P-02](../../principles/P-02-discoverability-learnability.md), [P-03](../../principles/P-03-information-architecture.md), [P-09](../../principles/P-09-consistency-familiarity.md); Dimensions: D-02, D-03, D-10; Gates: QG-051, QG-019, QG-040 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-SH-001, PAT-RS-001, PAT-MO-002, PAT-MO-009, PAT-MO-010, PAT-PW-001, PAT-PW-003

## Change log

- 2026-11-08 — Initial version (ADR-001).
