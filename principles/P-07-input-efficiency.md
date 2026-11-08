---
id: P-07
title: Input efficiency
type: principle
topics: [forms, input, keyboards, autofill, data-entry]
dimensions: [D-04]
patterns: [PAT-SH-002, PAT-SH-003, PAT-MO-004, PAT-MO-005, PAT-DT-006, PAT-RS-010]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-07 Input efficiency

## Universal outcome

Users provide information with the least effort and the fewest errors: the system asks only for what it needs, accepts input in the formats people naturally use, offers the right input method for each field and device, fills in what it already knows, and never makes someone type the same thing twice.

## Why it matters

- Typing is slow and error-prone on touch keyboards; every avoided keystroke matters. Baymard's mobile form research recommends matching the virtual keyboard to the field (numeric for card numbers, email keyboard for addresses) and reports that mismatched keyboards slow users and cause errors (E2; e-commerce checkout, generalizes to any mobile form).
- Browser autofill and password managers are the most efficient input method available; blocking paste or autofill harms efficiency and violates WCAG 3.3.8 Accessible Authentication where it affects login (E1).
- Redundant entry is both an efficiency loss and, within a process, a WCAG 2.2 failure (SC 3.3.7, E1).

## How to recognize it

- Field count is the minimum for the task; optional fields are justified or removed.
- Fields use the correct `type`, `inputmode`, and `autocomplete` tokens; paste works everywhere.
- Formatting is forgiving (spaces in card numbers, any phone format) and the system normalizes.
- Known information is prefilled or offered as a choice; multi-step forms carry data forward.
- On pointer/keyboard, tab order and Enter behave predictably; inline editing avoids round trips.

## Contextual implementation notes

- **Compact touch:** keyboards and keyboard-aware layout (PAT-MO-004); single-column, step-split forms (PAT-MO-005).
- **Expanded pointer/keyboard:** denser forms where fields are related; inline editing (PAT-DT-006).
- **Responsive:** choose modality-appropriate controls for the same data (date pickers, selects) (PAT-RS-010).
- **All:** validation that helps rather than blocks (PAT-SH-003).

## Evidence

- Baymard Institute, mobile form and checkout usability (public articles). https://baymard.com/research/mcommerce-usability — E2; e-commerce context.
- MDN, `inputmode` global attribute. https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode — E3. MDN, `autocomplete` attribute. https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete — E3.
- W3C WCAG 2.2 SC 3.3.7 Redundant Entry; SC 3.3.8 Accessible Authentication (Minimum). https://www.w3.org/TR/WCAG22/#redundant-entry ; https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum — E1.
- Wroblewski, L. *Web Form Design: Filling in the Blanks* (2008). — E4/E2 (book; includes eye-tracking studies on label placement).

## Evaluation

Primary dimension D-04; gates QG-023, QG-026, QG-027. Source inspection verifies that `type`, `inputmode`, and `autocomplete` hints are declared; only a running device verifies the keyboard and autofill behavior the browser actually delivers. Neither is visible in screenshots.
