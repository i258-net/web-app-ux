---
id: P-10
title: System feedback and predictable behavior
type: principle
topics: [feedback, status, response-time, predictability, animation]
dimensions: [D-07]
patterns: [PAT-SH-009, PAT-SH-010, PAT-PW-005, PAT-PW-007, PAT-PW-012]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-10 System feedback and predictable behavior

## Universal outcome

Every user action produces an immediate, proportionate, and understandable response, and the system's state is always visible. Users can predict what a control will do before they use it and can confirm what it did afterward. Nothing changes without a cause the user can see, and long operations show progress.

## Why it matters

- "Visibility of system status" is Nielsen's first heuristic (E4). The classic response-time thresholds—about 0.1 s to feel instantaneous, about 1 s to keep flow, about 10 s as the limit of attention—derive from Miller (1968) and Card et al. (1991) and are restated by NN/g (E2 origin, E4 restatement).
- Unexpected context changes (on focus, on input) are WCAG failures (3.2.1, 3.2.2) and a frequent source of disorientation for keyboard and screen-reader users (E1).
- Status messages must reach assistive technology without stealing focus (WCAG 4.1.3, E1).

## How to recognize it

- Pressed, loading, success, and failure states exist and are distinguishable for every action.
- Waits over ~1 s are indicated; waits over ~10 s show determinate progress or allow the user to leave and return.
- Feedback appears near the action and, for important outcomes, persists until acknowledged (not toast-only).
- Changes in connectivity, sync state, or app version are communicated, never silent.

## Contextual implementation notes

- **Compact:** feedback must not be hidden by the virtual keyboard or sticky bars; prefer inline state over toasts for critical results (PAT-SH-009).
- **Expanded:** feedback placed within the user's focal area on a wide canvas; status announced via live regions for keyboard users.
- **Web/PWA:** offline, failed sync, and update states surfaced explicitly (PAT-PW-005, PAT-PW-007, PAT-PW-012).

## Evidence

- Nielsen, J. "10 Usability Heuristics." https://www.nngroup.com/articles/ten-usability-heuristics/ — E4 (heuristic 1).
- Nielsen, J. "Response Times: The 3 Important Limits." NN/g. https://www.nngroup.com/articles/response-times-3-important-limits/ — E4 summarizing E2 (Miller 1968; Card, Robertson & Mackinlay 1991).
- W3C WCAG 2.2 SC 3.2.1 On Focus, 3.2.2 On Input, 4.1.3 Status Messages. https://www.w3.org/TR/WCAG22/#on-focus — E1.

## Evaluation

Primary dimension D-07; gates QG-020a, QG-020b, QG-028, QG-070. Only a running app shows timing and state behavior.
