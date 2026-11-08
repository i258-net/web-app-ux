---
id: PAT-SH-013
title: Onboarding and first use — tours, contextual help, and sequencing sign-up and permissions
type: pattern
scope: shared
topics: [onboarding, first-use, tutorials, product-tours, contextual-help, sign-up, permissions, setup]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-02, P-01, P-14, P-05]
dimensions: [D-01, D-03, D-09]
gates: [QG-027, QG-091, QG-095]
related: [PAT-SH-012, PAT-SH-014, PAT-PW-002, PAT-PW-009, PAT-MO-006, PAT-SH-002]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Onboarding and first use — tours, contextual help, and sequencing sign-up and permissions

## Problem

First use decides whether people continue. Common approaches work against that:

- Front-loaded tutorial carousels that users swipe past.
- Coach-mark tours that point at controls before the user has a reason to care.
- Mandatory account creation and preference setup before any value is shown.
- Permission prompts (notifications, location) and install prompts on first load, with no context.

Each delays the first useful outcome, and users forget the instructions before they need them.

## Recommendation

**Outcome:** a new user reaches a meaningful result quickly, learns features at the moment they become relevant, and grants accounts, permissions, and data only when they understand why.

1. **Make the interface teach itself first.** Clear labels, visible primary actions, sensible defaults, and well-designed empty states (PAT-SH-012) are the baseline. Onboarding cannot fix an unusable interface.
2. **Prefer contextual help to up-front tutorials.**
   - Show short tips next to the relevant control when the user first reaches it.
   - Use inline hints in empty states.
   - Offer "Learn more" links.
   - Make every pushed tip dismissible, and make the help retrievable later.
3. **If you use a tour or intro, keep it short, skippable, and revisitable.** Reserve it for genuinely novel or specialized workflows, not for conventional interfaces. Any tour must be keyboard-operable, and focus must return to where the user was.
4. **Defer sign-up until it adds value**, where the product allows it. Let users explore, try, or build something first, then ask for an account to save or share it. Keep work done before sign-up.
5. **Postpone nonessential setup.** Ask only what is required to start. Use defaults for everything else, and let users personalize later from settings.
6. **Request permissions in context.**
   - Ask when the user invokes a feature that needs the permission, with a sentence explaining the benefit.
   - Never ask on first load (QG-095).
   - Respect a denial: keep the app working, and explain how to enable the permission later. Details are in PAT-PW-009.
   - Install prompts follow the same rule: show them after demonstrated engagement, not on first load (QG-091; PAT-PW-002).
7. **Make authentication accessible.** Allow password managers and paste. Do not require a cognitive test without an alternative (QG-027).
8. **Be honest.** No pre-checked marketing consent, no "skip" link styled to be missed, no dark-pattern friction on declining (P-14).
9. **Show the scope early.** The first view should convey what the product can do, not only one promoted feature.

Teaching hidden gestures is covered in PAT-MO-006.

## Evidence

- **E2** Nielsen Norman Group, "Mobile Tutorials: Wasted Effort or Efficiency Boost?". https://www.nngroup.com/articles/mobile-tutorials/ — A between-subjects study with 70 users and 4 relatively simple iPhone apps found no significant task-success or time benefit from deck-of-cards tutorials, and tutorial viewers rated tasks as harder. *Limits:* native iOS apps, simple tasks, iOS-experienced participants, one tutorial format. The study does not rule out setup, interactive practice, or specialist training.
- **E4** Nielsen Norman Group, "Help and Documentation". https://www.nngroup.com/articles/help-and-documentation/ — Contextual help is less likely to be ignored than pushed instructions. Pushed help should be dismissible and retrievable.
- **E3** Apple, "Onboarding". https://developer.apple.com/design/human-interface-guidelines/onboarding.md — Prefer learning by safe interaction and contextual tips. Keep prerequisite onboarding brief and tutorials optional. Postpone nonessential setup, and request permissions when they are relevant to a feature. Apple platforms.
- **E4** Nielsen Norman Group, "Flexibility and Efficiency of Use". https://www.nngroup.com/articles/flexibility-efficiency-heuristic/ — Keep an obvious, learnable standard path; accelerators are optional additions.
- **E1** W3C, "WCAG 2.2 — SC 3.3.8 Accessible Authentication (Minimum)". https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum — No cognitive function test without an alternative or assistance.
- **E4** Nielsen Norman Group, "Deceptive Patterns in UX". https://www.nngroup.com/articles/deceptive-patterns/ — Deception, misdirection, and obstruction steer users against their interests; conversion gains alone do not show good UX.
- **E2** Baymard Institute, "42% of Mobile Homepages Risk Setting Wrong Expectations". https://baymard.com/research-articles/mobile-homepage-usability — Unrepresentative first views caused false assumptions about scope. *E-commerce*; we infer the same risk for app first-run screens.
- **E5** Mobbin, "Mobile App Onboarding Screen User Flow Design". https://mobbin.com/explore/mobile/flows/onboarding — Shipped onboarding often combines account creation, verification, and preference setup. Convention observed, usability unverified. It does not show that mandatory setup helps.

## Alternatives and tradeoffs

- **Up-front tutorial vs contextual learning.** The only E2 evidence (NN/g, native simple apps) found no benefit from tutorial cards. Complex or regulated tools (clinical, financial, professional software) may still warrant guided setup or training. Test these rather than assuming either way.
- **Early vs deferred sign-up.** Deferring lowers the barrier but adds complexity (anonymous state, merging on sign-up). Products whose value requires identity (banking, messaging) must authenticate first. That is acceptable when explained.
- **Personalization at start vs later.** Asking preferences up front can tailor the first view (common in shipped apps, E5) but delays value. Prefer inferring preferences from use, or ask one high-value question.

## Exceptions and failure modes

- Security- or compliance-driven flows (identity verification) cannot be deferred. Keep them efficient and explain why they are needed.
- Failure modes:
  - a 5-screen carousel before the app;
  - coach marks that block the UI and cannot be dismissed by keyboard;
  - a notification prompt on first load;
  - an install banner before any interaction;
  - losing a guest's work at sign-up;
  - an onboarding flow that cannot be revisited;
  - tips that reappear after dismissal.

## Evaluation questions

1. How many steps and screens separate first launch from the first meaningful result? [running app] [prototype]
2. Is any permission or install prompt shown before a related user action? [running app]
3. Are tours or tips skippable, dismissible by keyboard, and retrievable later? [running app]
4. Is work done before sign-up preserved after sign-up? [running app]
5. Can a password manager fill credentials, and does paste work? [running app]
6. Are consent choices unbiased (no pre-checked boxes, equal-weight decline)? [screenshot]
7. After first use, can new users complete a core task without the tutorial? [user study]

## Related

- Principles: P-02, P-01, P-14, P-05
- Dimensions: D-01, D-03, D-09
- Gates: QG-027, QG-091, QG-095
- Patterns: PAT-SH-012 (empty states), PAT-SH-014 (disclosure), PAT-PW-002 (install prompts), PAT-PW-009 (notification permissions), PAT-MO-006 (teaching gestures), PAT-SH-002 (sign-up forms)

## Change log

- 2026-11-08 — Initial version (ADR-001).
