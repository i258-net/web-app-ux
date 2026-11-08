---
id: P-11
title: Error prevention and recovery
type: principle
topics: [errors, prevention, recovery, undo, confirmation, validation]
dimensions: [D-07, D-04]
patterns: [PAT-SH-003, PAT-SH-011, PAT-SH-016, PAT-PW-008, PAT-DT-011]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-11 Error prevention and recovery

## Universal outcome

The design makes mistakes hard to make and easy to undo. Constraints, defaults, and clear affordances prevent slips; when errors happen, they are explained in plain language at the point of the problem with a specific way forward, and nothing the user entered is lost. Reversibility is preferred to interrogation: undo beats "Are you sure?".

## Why it matters

- Nielsen's heuristics 5 ("error prevention") and 9 ("help users recognize, diagnose, and recover from errors") are among the most frequently violated (E4). NN/g's error-message guidelines are grounded in decades of usability testing (E4/E2).
- Confirmation dialogs lose their protective value when they appear for routine actions; users habituate and click through. NN/g recommends undo for most reversible actions and confirmations only for consequential, irreversible ones (E4).
- WCAG 2.2 makes several of these normative: errors identified in text (3.3.1), suggestions where known (3.3.3), reversible or confirmable legal/financial/data submissions (3.3.4) (E1).
- Losing entered data on an error is the most costly failure in forms; Baymard documents it as a top abandonment cause in checkout (E2; e-commerce).

## How to recognize it

- Inputs are constrained to valid values where possible (pickers, masks that still allow typing, sensible defaults).
- Validation timing fits the field: on blur or submit for most fields, live only where it helps (password strength, availability).
- Error text says what is wrong and how to fix it, next to the field, and the field is identifiable to assistive technology.
- Destructive actions are undoable for a window, or separated and confirmed with specific language; dangerous and routine actions are not adjacent.
- Failed submissions preserve all input; drafts survive reload and navigation.

## Contextual implementation notes

- **Compact touch:** error text visible above the keyboard; undo via snackbar/toast with adequate duration and an accessible alternative (PAT-SH-003, PAT-SH-011).
- **Expanded:** undo via shortcut and menu; bulk operations are reversible (PAT-DT-011).
- **Web/PWA:** unsaved-changes protection and draft preservation (PAT-PW-008); failure states with retry (PAT-SH-016).

## Evidence

- Nielsen, J. "10 Usability Heuristics." https://www.nngroup.com/articles/ten-usability-heuristics/ — E4 (heuristics 5, 9).
- Nielsen, J. "Error Message Guidelines." NN/g. https://www.nngroup.com/articles/error-message-guidelines/ — E4.
- Laubheimer, P. "Confirmation Dialogs Can Prevent User Errors — If Not Overused." NN/g. https://www.nngroup.com/articles/confirmation-dialog/ — E4.
- W3C WCAG 2.2 SC 3.3.1, 3.3.3, 3.3.4. https://www.w3.org/TR/WCAG22/#error-identification — E1.
- Baymard Institute, checkout form validation research (public articles). https://baymard.com/research/mcommerce-usability — E2; e-commerce.

## Evaluation

Primary dimension D-07; gates QG-022, QG-024, QG-025, QG-072. Trigger real errors in a running app; screenshots show only captured states.
