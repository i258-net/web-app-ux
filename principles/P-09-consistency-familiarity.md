---
id: P-09
title: Consistency and platform familiarity
type: principle
topics: [consistency, conventions, platform, standards, familiarity]
dimensions: [D-10, D-02]
patterns: [PAT-RS-001, PAT-PW-001, PAT-MO-003, PAT-DT-004, PAT-RS-010]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# P-09 Consistency and platform familiarity

## Universal outcome

The same things look and behave the same way throughout the product (internal consistency), and the product behaves the way users expect from the platform and the wider web (external consistency). Where devices differ, the product adapts to each platform's conventions instead of forcing one platform's idioms on another. Deviations from convention are deliberate and earn their cost.

## Why it matters

- Nielsen's heuristic 4 ("consistency and standards") and Jakob's Law ("users spend most of their time on other sites") explain why convention is itself a usability mechanism: it lets users apply what they already know (E4).
- Apple and Material each document conventions that users of their platforms expect (tab bar placement, back behavior, sheet gestures). These are authoritative for their platforms (E3) and are evidence of *expectation*, not universal rules for the web.
- Web users expect web behaviors: working back button, shareable URLs, text selection, zoom, right-click. Breaking them in pursuit of an "app-like" feel is a common PWA failure (E3/E4).

## How to recognize it

- Components with the same function look and behave identically everywhere in the product.
- Navigation, help, and key controls are in consistent locations (WCAG 3.2.3, 3.2.4, 3.2.6, E1).
- Mobile uses touch idioms, desktop uses pointer and keyboard idioms, and neither is a scaled copy of the other.
- Platform-specific affordances (iOS back-swipe, Android back button, browser back) are respected rather than fought.

## Contextual implementation notes

- **Responsive:** transform navigation and controls per viewport while keeping destinations and vocabulary identical (PAT-RS-001, PAT-RS-010).
- **PWA:** respect display-mode differences; do not duplicate browser chrome in browser mode (PAT-PW-001).
- **Desktop:** honor OS and browser shortcut conventions; avoid hijacking standard keys (PAT-DT-004).

## Evidence

- Nielsen, J. "10 Usability Heuristics." https://www.nngroup.com/articles/ten-usability-heuristics/ — E4 (heuristic 4).
- Nielsen, J. "Jakob's Law of Internet User Experience." NN/g. https://www.nngroup.com/videos/jakobs-law-internet-ux/ — E4.
- W3C WCAG 2.2 SC 3.2.3 Consistent Navigation, 3.2.4 Consistent Identification, 3.2.6 Consistent Help. https://www.w3.org/TR/WCAG22/#consistent-navigation — E1.
- Apple HIG (platform conventions). https://developer.apple.com/design/human-interface-guidelines/ — E3. Material Design 3 (platform conventions). https://m3.material.io/ — E3.

## Evaluation

Primary dimension D-10 (with D-02). Internal consistency is visible in screenshots; platform behavior needs a running app on the platform.
