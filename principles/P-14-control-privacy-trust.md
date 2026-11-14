---
id: P-14
title: User control, privacy, and trust
type: principle
topics: [control, freedom, privacy, permissions, trust, dark-patterns, transparency]
dimensions: [D-09, D-07]
patterns: [PAT-PW-009, PAT-PW-002, PAT-SH-013, PAT-SH-011, PAT-SH-015]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# P-14 User control, privacy, and trust

## Universal outcome

Users stay in charge. They can leave, cancel, undo, and change their minds; the product asks for data, permissions, and attention only when the user can see why and can decline without penalty; it never deceives, pressures, or traps. Trust is earned by honesty about what the product does with the user's data and attention.

## Why it matters

- "User control and freedom" is Nielsen's heuristic 3: clearly marked exits, undo and redo (E4).
- Permission prompts shown without context (on first load, before the user has done anything) are easy to deny and, once denied, are hard to re-request on many platforms; MDN requires requesting notification permission from a user gesture and web.dev recommends explaining the value first (E3/E4). No denial-rate study is cited here; treat the harm as reasoned, not measured.
- Deceptive patterns ("dark patterns") produce short-term metrics and long-term distrust; they are increasingly regulated (EU DSA, FTC guidance). NN/g and the deceptive.design catalog document common forms (E4).
- Interruptive install prompts, modal sign-up walls, and notification nags are the PWA-specific versions of this failure.

## How to recognize it

- Every flow can be cancelled or exited without side effects; modals close by all conventional means.
- Permission requests (notifications, location, camera) come after an action that implies intent, with a pre-prompt explanation, and denial is respected (no repeated nagging).
- Pricing, consequences, and data use are stated plainly before commitment; defaults favor the user; opting out is as easy as opting in.
- No countdown pressure, confirmshaming, pre-ticked consent, or hidden costs.

## Contextual implementation notes

- **PWA:** install prompts gated on engagement, never on first paint (PAT-PW-002); notification permission flow (PAT-PW-009).
- **Onboarding:** value before sign-up; permissions deferred (PAT-SH-013).
- **All:** undo over confirmation (PAT-SH-011); dismissible, non-trapping modality (PAT-SH-015).

## Evidence

- Nielsen, J. "10 Usability Heuristics." https://www.nngroup.com/articles/ten-usability-heuristics/ — E4 (heuristic 3).
- web.dev, Learn PWA: Installation prompt (install promotion timing). https://web.dev/learn/pwa/installation-prompt — E3.
- web.dev, push notification permissions UX. https://web.dev/articles/push-notifications-permissions-ux — E4.
- MDN, Notifications API: Using the Notifications API (request permission on user gesture). https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API — E3.
- Brignull, H. Deceptive Design (formerly Dark Patterns) catalog. https://www.deceptive.design/ — E4.

## Evaluation

Primary dimension D-09 (trust) with D-07 (control). Permission timing and exits are verifiable in a running app; deceptive patterns are visible in screenshots.
