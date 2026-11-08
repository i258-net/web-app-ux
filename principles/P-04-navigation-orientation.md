---
id: P-04
title: Navigation and orientation
type: principle
topics: [navigation, wayfinding, orientation, back, location]
dimensions: [D-02]
patterns: [PAT-SH-001, PAT-MO-003, PAT-DT-002, PAT-RS-001, PAT-PW-003]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-04 Navigation and orientation

## Universal outcome

At every moment users know where they are, how they got there, where they can go next, and how to get back. Moving between places is predictable: the same action always goes to the same kind of place, and "back" undoes the last navigation rather than doing something surprising.

## Why it matters

- Wayfinding is a basic cognitive need; disorientation produces anxiety and abandonment. NN/g's wayfinding guidance treats "where am I" and "where can I go" as the minimum any page must answer (E4).
- On the web, the browser's back button is the most used navigation control; breaking it (modals that trap, SPAs that do not push history) is a long-documented top usability failure (E4, NN/g).
- In installed PWAs the browser back button and URL bar may be absent, so the app must provide its own orientation and back controls (E3, web.dev).

## How to recognize it

- Current location is marked in navigation and in the page title; deep pages show a path (breadcrumbs or equivalent) on expanded viewports.
- Browser back returns to the previous meaningful state; modals and drawers close on back where that matches user expectation; no view is a dead end.
- Every primary view has a URL that reproduces it; links are shareable.
- Navigation is in the same place and order on every page of the same type (consistency; WCAG 3.2.3, E1).

## Contextual implementation notes

- **Compact touch:** tab bar or top bar with consistent back affordance; avoid hiding primary destinations (PAT-MO-003).
- **Expanded pointer:** persistent sidebar or top navigation with visible current state; breadcrumbs for depth (PAT-DT-002).
- **Transitions:** the navigation model must transform without losing destinations (PAT-RS-001).
- **Web/PWA:** manage history explicitly; provide in-app back in standalone display mode (PAT-PW-003).

## Evidence

- Nielsen, J. "Breadcrumb Navigation Increasingly Useful." NN/g. https://www.nngroup.com/articles/breadcrumb-navigation-useful/ — E4.
- Nielsen, J. "Top 10 Mistakes in Web Design." NN/g. https://www.nngroup.com/articles/top-10-mistakes-web-design/ — E4 (back button).
- W3C WCAG 2.2 SC 3.2.3 Consistent Navigation (AA). https://www.w3.org/TR/WCAG22/#consistent-navigation — E1.
- web.dev, Learn PWA: App design (display modes). https://web.dev/learn/pwa/app-design — E3.

## Evaluation

Primary dimension D-02. Back behavior and deep links are only verifiable in a running application (QG-060, QG-061).
