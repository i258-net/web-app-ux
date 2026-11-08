---
id: P-02
title: Discoverability and learnability
type: principle
topics: [discoverability, learnability, affordances, onboarding]
dimensions: [D-03]
patterns: [PAT-SH-013, PAT-MO-006, PAT-DT-003, PAT-DT-004, PAT-SH-008]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-02 Discoverability and learnability

## Universal outcome

Users can find the functions they need and learn how to use them from the interface itself, without training or trial and error. Capabilities are signaled by visible affordances and signifiers; hidden interactions (gestures, hover reveals, keyboard shortcuts) are always redundant with something visible or taught at the moment of need.

## Why it matters

- Functions that cannot be found do not exist for the user. NN/g's research on hidden navigation found that hiding navigation behind a menu reduced its discoverability and use compared with visible navigation (E2; tested on both mobile and desktop).
- Gestures have no natural signifiers; NN/g and Apple both warn that gesture-only interactions must be discoverable or redundant (E4/E3).
- "Recognition rather than recall" (Nielsen heuristic 6) explains why visible options beat memorized commands for most users (E4).

## How to recognize it

- Interactive elements look interactive on the input in use (touch: visible controls; pointer: hover/cursor cues; keyboard: visible focus).
- Hidden accelerators (shortcuts, gestures, right-click) have visible equivalents and are taught in context (a tooltip showing the shortcut, a hint on first swipe).
- First-time users can complete the primary task without a tour; onboarding explains value and asks for permissions only when needed.
- Labels describe outcomes; icons that are not universally understood carry text.

## Contextual implementation notes

- **Compact touch:** keep primary destinations visible (tab bar) rather than behind a hamburger when destination count allows (PAT-MO-003); teach gestures or pair them with buttons (PAT-MO-006).
- **Pointer:** hover reveals are fine as a *second* path, never the only one (PAT-DT-003); shortcuts shown in menus and tooltips (PAT-DT-004).
- **All:** icon-only controls need accessible names and, usually, visible labels (PAT-SH-008).

## Evidence

- Pernice, K., Budiu, R. "Hamburger Menus and Hidden Navigation Hurt UX Metrics." NN/g, 2016. https://www.nngroup.com/articles/hamburger-menus/ — E2.
- Nielsen, J. "10 Usability Heuristics." https://www.nngroup.com/articles/ten-usability-heuristics/ — E4 (heuristics 6 and 7).
- Apple Human Interface Guidelines, Gestures. https://developer.apple.com/design/human-interface-guidelines/gestures — E3 (Apple platforms).

## Evaluation

Primary dimension D-03. Screenshots show affordances; discoverability of hidden paths needs a running app or a user study.
