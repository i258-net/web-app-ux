---
id: PAT-SH-003
title: Validation timing and error messages
type: pattern
scope: shared
topics: [validation, inline-validation, error-messages, error-summary, positive-validation, forms]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-11, P-10, P-12, P-07]
dimensions: [D-07, D-04, D-08]
gates: [QG-022, QG-024, QG-028, QG-072, QG-006]
related: [PAT-SH-002, PAT-SH-009, PAT-SH-016, PAT-MO-005, PAT-DT-006]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Validation timing and error messages

## Problem

Validation fails in two directions. *Too early*: an error appears mid-typing, interrupting and accusing. *Too late or too vague*: it appears only after submit, says "Invalid input", sits far from the field, vanishes in a toast, or persists after the fix. The worst failures erase what the user typed.

## Recommendation

**Outcome:** users learn about a problem when they can act on it. They see what is wrong and how to fix it, at the field. Nothing they entered is lost, and the message disappears as soon as the problem is gone.

1. **Timing.**
   - Validate a field when the user leaves it (blur), or on submit.
   - For fixed-length or pattern inputs, you may validate once enough characters have been entered to judge.
   - Never mark an untouched or partly typed field invalid.
   - *Constructive* guidance while typing (e.g. a password rule checklist) is different from an error and is fine.
   - Once a field is in error, re-validate on every input so the error clears **immediately** when fixed. Re-validate dependent fields too (e.g. "confirm email").
2. **Placement.** Put the message adjacent to the field (Material places it below), associated programmatically (`aria-describedby`), and visible with the keyboard open. Do not put errors in tooltips.
3. **Content.**
   - Name the problem in the user's words and say how to fix it ("Enter a 5-digit ZIP code", not "Invalid").
   - Make messages *adaptive*: the text names the specific rule that failed (missing, too short, wrong format).
   - Give a known correction whenever doing so does not compromise security.
   - Do not imply a system failure when the problem is a correctable field.
4. **Never rely on color alone.** Use text plus an icon or another non-color cue; the error must be identified in text (QG-022).
5. **On submit with errors:**
   - Keep every value (QG-072).
   - Move focus to the first invalid field, or to an error summary at the top that links to each field. The summary is for *locating* errors; inline messages carry the explanation.
   - Announce the summary or the error count to assistive technology (QG-028).
6. **Show field-level server errors** (e.g. "email already registered") at the field, not in a generic banner.
7. **Disclose rules before entry**, not only on failure.
8. **No modal dialogs or transient toasts** for field errors.
9. **Disabled submit buttons** need a visible explanation of what is missing. Otherwise users cannot discover why they are stuck (see Alternatives).

Compact-touch specifics: PAT-MO-005. Inline-edit errors: PAT-DT-006.

## Evidence

- **E1** W3C, "WCAG 2.2 — SC 3.3.1 Error Identification". https://www.w3.org/TR/WCAG22/#error-identification — Detected errors must identify the item and describe the error in text.
- **E1** W3C, "WCAG 2.2 — SC 3.3.3 Error Suggestion". https://www.w3.org/TR/WCAG22/#error-suggestion — Known corrections must be offered unless they jeopardize security or purpose.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Status messages must be programmatically determinable without receiving focus.
- **E4** Nielsen Norman Group, "10 Design Guidelines for Reporting Errors in Forms". https://www.nngroup.com/articles/errors-forms-design-guidelines/ — Inline errors after the field is complete, near the input, with non-color cues; avoid premature, tooltip-only, and summary-only errors.
- **E2** Baymard Institute, "Usability Testing of Inline Form Validation". https://baymard.com/research-articles/inline-form-validation — Premature errors frustrated users and interrupted typing. Stale errors left after correction misled participants. Recommends validating on exit or once enough characters exist, and removing errors immediately. *E-commerce checkout*; likely generalizes.
- **E2** Baymard Institute, "Improve Validation Errors with Adaptive Messages". https://baymard.com/research-articles/adaptive-validation-error-messages — Generic error text left users stuck or abandoning. Messages specific to the failing sub-rule helped. *E-commerce*; likely generalizes.
- **E2** Nielsen Norman Group, "Indicators, Validations, and Notifications". https://www.nngroup.com/articles/indicators-validations-notifications/ — A participant missed a brief error message. Fading toasts are a poor way to show errors.
- **E2** Baymard Institute, "Accounts & Self-Service UX Research Update". https://baymard.com/research-articles/accounts-and-self-service-ux-research-2026 — Users struggled when password rules appeared only after submission. *Commerce accounts.*
- **E3** Google Material Design, "Text fields". https://m3.material.io/components/text-fields — Errors sit in supporting text below the field until fixed. Material convention.
- **E3** Apple, "Entering data". https://developer.apple.com/design/human-interface-guidelines/entering-data.md — Validate with timely feedback. Apple's example disables Next until required fields are complete. Apple platforms.

## Alternatives and tradeoffs

- **Positive validation: a direct disagreement.** Baymard (E2, checkout) recommends success indicators on *all* fields for reassurance. NN/g (E4) reserves them for fields with real uncertainty (username availability, password rules) and warns of noise on trivial fields. We do not force consensus. Positive validation on every field is acceptable in short, high-stakes consumer flows. Reserve it for meaningful checks in dense or repeated-entry professional forms. Either way, test assistive-technology announcement noise.
- **Blur vs submit-only.** Submit-only validation avoids premature errors, but it delays feedback in long forms. Blur validation is the better default in long forms. Either is acceptable in a two-field form.
- **Disabled submit vs enabled submit with errors.** Apple's example disables Next. Our inference for the web: keep submit enabled and report errors on press, *or* disable it only with visible text stating what is missing. A silently disabled button hides the problem.

## Exceptions and failure modes

- Authentication errors can deliberately stay vague ("email or password incorrect") for security. WCAG 3.3.3 permits this exception.
- Failure modes:
  - a red border with no text;
  - errors announced only visually;
  - a summary that does not link to the fields;
  - a submit that clears the password and every other field;
  - an error that stays after correction until the next submit;
  - errors hidden behind the virtual keyboard or a sticky footer (QG-006).

## Evaluation questions

1. Type part of a value and pause: does an error appear before the field is left? [running app] [prototype]
2. Fix an erroneous field: does the error clear immediately, including on dependent fields? [running app]
3. Does each error say what is wrong and how to fix it, in text, next to the field? [screenshot] [running app]
4. After a failed submit, are all values kept, is focus moved to the first error or the summary, and is the error announced? [running app] [automated]
5. Are rules and formats visible before entry? [screenshot]
6. Are any errors delivered only by toast, tooltip, or color? [running app] [screenshot]
7. Do users recover from each error without help? [user study]

## Related

- Principles: P-11, P-10, P-12, P-07
- Dimensions: D-07, D-04, D-08
- Gates: QG-022, QG-024, QG-028, QG-072, QG-006
- Patterns: PAT-SH-002 (labels and instructions), PAT-SH-009 (feedback channels), PAT-SH-016 (submission failures), PAT-MO-005 (mobile forms), PAT-DT-006 (inline editing)

## Change log

- 2026-11-08 — Initial version (ADR-001).
