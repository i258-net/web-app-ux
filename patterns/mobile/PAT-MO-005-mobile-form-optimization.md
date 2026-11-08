---
id: PAT-MO-005
title: Mobile form optimization — layout, steps, autofill, and minimal typing
type: pattern
scope: mobile
topics: [forms, checkout, address, payment, autofill, single-column, steps, typing-effort, labels]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, keyboard, assistive-tech]
principles: [P-07, P-01, P-11, P-05]
dimensions: [D-04, D-01, D-07]
gates: [QG-023, QG-026, QG-027, QG-053, QG-062, QG-072]
related: [PAT-SH-002, PAT-SH-003, PAT-SH-014, PAT-MO-004, PAT-MO-010, PAT-MO-011, PAT-RS-010, PAT-PW-004, PAT-PW-008]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Mobile form optimization — layout, steps, autofill, and minimal typing

## Problem

Typing on glass is slow and error-prone, the keyboard hides much of the context, and mobile sessions are interrupted. Desktop-style forms — side-by-side fields, left labels, split phone boxes, an always-visible "Address line 2", intermediate "Apply" buttons — produce inputs too narrow to show what was typed, hidden errors, re-typing, and lost work.

**Scope.** Universal form guidance — field count, grouping, label placement, required/optional marking, help text — lives in **PAT-SH-002**; validation timing and error messages live in **PAT-SH-003**. Keyboard semantics live in **PAT-MO-004**. This pattern covers only the compact-touch adaptation.

## Recommendation

**Outcome:** people finish the form with as little typing and as few corrections as possible, can see and fix what they entered, and do not lose work to interruption.

1. **Single column, labels above fields,** so the full width shows the value. Short related pairs (expiry month/year) may share a row if both values stay visible.
2. **Reduce what users must consider before reducing screens.** Remove, infer, or defer fields first (PAT-SH-002); then split into a few coherent steps with visible progress only if it helps (PAT-SH-014).
3. **One perceived value, one field.** Do not split phone numbers, names, or card numbers; format within one field.
4. **Let the machine type.** `autocomplete` tokens for name, email, phone, address, payment (PAT-MO-004); address lookup where coverage is good; reuse data entered earlier in the process (QG-026); choices instead of typing for small fixed option sets (PAT-RS-010).
5. **Keep conventional fields visible alongside lookup and autofill** for review and manual fallback. Put genuinely optional fields ("Add apartment, suite, etc.") behind a clearly labelled link; keep any filled value visible.
6. **Let "Continue" commit the step.** No separate Apply/Save for ordinary fields; keep them for separate operations (promo codes, gift cards).
7. **Credentials:** allow paste and password managers (QG-027), offer "show password", state rules before entry.
8. **Payment:** `cc-*` tokens (e.g. `cc-number`) so saved cards fill; one numeric field for the card number.
9. **Keep the way forward visible.** Submit follows the last field; a sticky duplicate must not cover fields or errors with the keyboard open (QG-053, PAT-MO-010).
10. **Survive interruption.** Preserve input across reload, back, and failed submission (QG-062, QG-072; PAT-PW-004, PAT-PW-008).
11. **Errors:** after submit, take the user to the first error with its message beside the field (PAT-SH-003).

## Evidence

- **E2** Baymard Institute, "Field Label UX: Place Labels Above the Field". https://baymard.com/research-articles/mobile-form-usability-label-position — Mobile-commerce testing: left labels left fields too narrow to show entered values, impeding error detection; above labels permit wider inputs. 2013 devices.
- **E2** Baymard Institute, "Mobile Form Usability: Never Use Inline Labels". https://baymard.com/research-articles/mobile-forms-avoid-inline-labels — Users deleted values to reveal vanished in-field labels; links to PAT-SH-002 label guidance.
- **E2** Baymard Institute, "Mobile Form Usability: Avoid Splitting Single Input Entities". https://baymard.com/research-articles/mobile-form-usability-single-input-fields — Split phone/name fields caused struggles and interrupted typing on mobile; desktop evidence inconclusive for some cases.
- **E2** Baymard Institute, "Checkout Optimization: 5 Ways to Minimize Form Fields in Checkout". https://baymard.com/research-articles/checkout-flow-average-form-fields — Number of fields users must manage generally matters more than number of steps. Benchmark averages are descriptive, not targets.
- **E2** Baymard Institute, "Provide a 'Fully Automatic Address Lookup' Feature". https://baymard.com/research-articles/automatic-address-lookup — Live address suggestions performed well; conventional fields needed for fallback, review, and autofill.
- **E2** Baymard Institute, "Form Usability: Getting 'Address Line 2' Right". https://baymard.com/research-articles/address-line-2 — Exposed optional line 2 consumed attention and confused users; recommends a clearly described link.
- **E2** Baymard Institute, "Checkout UX: Avoid 'Apply' Buttons for Most Fields". https://baymard.com/research-articles/checkout-usability-apply-buttons — Intermediate Apply/Save controls were missed or confused with continuation; exceptions for promo codes and gift cards. E-commerce-specific.
- **E2** Baymard Institute, "Accounts & Self-Service UX Research Update and Expansion". https://baymard.com/research-articles/accounts-and-self-service-ux-research-2026 — Users struggled when password rules appeared only after submission and masking prevented verification.
- **E4** Nielsen Norman Group, "Website Forms Usability: Top 10 Recommendations". https://www.nngroup.com/articles/web-form-design/ — Short forms, label proximity, logical order, generally single column.
- **E2** Nielsen Norman Group, "Mobile User Experience: Limitations and Strengths". https://www.nngroup.com/articles/mobile-ux/ — Fragmented attention and interruption; save state so users can resume. 2015.
- **E1** W3C, "WCAG 2.2 — 3.3.7 Redundant Entry, A" and "1.3.5 Identify Input Purpose, AA". https://www.w3.org/TR/WCAG22/#redundant-entry — Previously entered information must be auto-populated or selectable within a process; field purpose must be programmatically determinable.
- **E1** W3C, "WCAG 2.2 — 3.3.8 Accessible Authentication (Minimum), AA". https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum — No cognitive function test without an alternative or assistance; supports paste and password managers.
- **E3** MDN, "autocomplete" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete — Token list including `name`, `tel`, `street-address`, `postal-code`, `cc-number`, `one-time-code`, and `shipping`/`billing` sections; `name` preferred over split name parts.
- **E3** Apple, "Human Interface Guidelines — Entering data". https://developer.apple.com/design/human-interface-guidelines/entering-data.md — Obtain available information, supply defaults, prefer choices, support paste.

Most E2 evidence here is e-commerce checkout; the mechanisms (visibility of entered values, fewer considered fields, fallback for automation) likely generalise to other high-effort forms, but that is our interpretation.

## Alternatives and tradeoffs

- **One long page vs steps.** A single page keeps overview and review; steps keep each screen short and let progress be saved. Choose by field count, branching, and whether review across sections matters.
- **Positive validation** for every field is recommended by Baymard and cautioned against by NN/g for trivial fields — see PAT-SH-003; neither is mandatory.
- **Native pickers vs custom controls** for dates and selects: native controls bring platform familiarity and AT support; custom controls may suit ranges and constrained choices (PAT-RS-010).

## Exceptions and failure modes

- Very short familiar forms (search, sign-in) may need none of this structure.
- Failures: input discarded on validation error; lookup with no manual fallback; country-specific assumptions (postcode formats, name order); masking with no reveal; autofill defeated by split fields or missing tokens.

## Evaluation questions

- Is the form single-column with labels above, and are entered values fully visible? [screenshot]
- Do autofill and address lookup fill correct fields on a real device, with manual fallback? [running app]
- Are any single values split across several inputs? [screenshot] [automated]
- Is earlier-entered data reused, not re-typed, within the process? [running app]
- Does data survive reload, back, and failed submission? [running app]
- How long do participants take, and how many corrections do they make, on a real phone? [user study]

## Related

- Principles: [P-07](../../principles/P-07-input-efficiency.md), [P-01](../../principles/P-01-task-effectiveness.md), [P-11](../../principles/P-11-error-prevention-recovery.md), [P-05](../../principles/P-05-cognitive-clarity.md); Dimensions: D-04, D-01, D-07; Gates: QG-023, QG-026, QG-027, QG-053, QG-062, QG-072 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-SH-002, PAT-SH-003, PAT-SH-014, PAT-MO-004, PAT-MO-010, PAT-MO-011, PAT-RS-010, PAT-PW-004, PAT-PW-008

## Change log

- 2026-11-08 — Initial version (ADR-001).
