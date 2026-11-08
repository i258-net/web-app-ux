---
id: PAT-SH-002
title: Form fundamentals — fields, grouping, labels, and required status
type: pattern
scope: shared
topics: [forms, labels, placeholders, required-fields, optional-fields, help-text, field-reduction]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-07, P-05, P-11, P-12]
dimensions: [D-04, D-06, D-08]
gates: [QG-023, QG-016, QG-026, QG-004]
related: [PAT-SH-003, PAT-MO-004, PAT-MO-005, PAT-SH-014, PAT-PW-008, PAT-DT-006]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Form fundamentals — fields, grouping, labels, and required status

## Problem

Users abandon forms or make errors when they meet fields that need not exist, labels that vanish on typing, required and optional fields that look alike, instructions hidden in tooltips, and a visual order that differs from the keyboard order. Each makes users interpret, remember, or guess, and each makes review after autofill or an interruption harder.

## Recommendation

**Outcome:** users understand what each field wants and whether they must fill it. They can see what they entered at any time, and they meet no field the task does not need.

1. **Remove, infer, or defer fields first.** Ask only what this task needs now. Reuse information already given in the process (QG-026) and expose input purposes programmatically (`autocomplete`; see PAT-MO-004).
2. **Use a single column with a logical order** as the default. Exceptions are short related fields that are perceived as one row (e.g. city and postal code). Visual order must match focus order (QG-004).
3. **Group related fields** under a visible heading or `fieldset`/`legend`.
4. **Give every field a persistent visible label** outside the input. Above-field labels are the safe default at every width. Side labels are acceptable on wide viewports for long, repetitive forms. The accessible name must contain the visible label text (QG-016).
5. **Do not use placeholder text as the label.** A placeholder may show an example format only when the label and any essential hint remain visible after typing and after autofill.
6. **Mark required status at each field**, in text or with an explained symbol, exposed to assistive technology. In long or mixed forms, also mark optional fields explicitly ("optional"). Do not rely on one instruction at the top of the form.
7. **Put essential instructions in persistent text beside the field**, shown *before* entry. Tooltips hold supplementary explanation only (PAT-DT-003).
8. **Use one field per perceived value** (split-field evidence is in PAT-MO-005), and accept common formatting variants.
9. **Make the commit boundary obvious.** A step's primary action saves ordinary entry. Avoid intermediate Apply/Save buttons except where a separate operation exists (e.g. a promo code).

Compact-touch adaptations: PAT-MO-004, PAT-MO-005. Validation: PAT-SH-003. Drafts: PAT-PW-008.

## Evidence

- **E1** W3C, "WCAG 2.2 — SC 3.3.2 Labels or Instructions". https://www.w3.org/TR/WCAG22/#labels-or-instructions — Labels or instructions are required when content requires input.
- **E1** W3C, "WCAG 2.2 — SC 3.3.7 Redundant Entry; SC 1.3.5 Identify Input Purpose". https://www.w3.org/TR/WCAG22/#redundant-entry — Reuse already-entered information; personal-data field purposes must be programmatically determinable.
- **E2** Nielsen Norman Group, "Placeholders in Form Fields Are Harmful". https://www.nngroup.com/articles/form-design-placeholders/ — Placeholder-as-label caused lost context, harder review of autofill and errors, and fields that looked filled.
- **E2** Baymard Institute, "Mobile Form Usability: Never Use Inline Labels". https://baymard.com/research-articles/mobile-forms-avoid-inline-labels — Shoppers deleted entries to reveal vanished labels. Narrow one- or two-field exceptions allowed. *E-commerce, 2013*; likely generalizes.
- **E2** Baymard Institute, "Field Label UX: Place Labels Above the Field". https://baymard.com/research-articles/mobile-form-usability-label-position — On mobile, left labels left fields too narrow to show entered values. *E-commerce, 2013 devices.*
- **E4** Nielsen Norman Group, "Website Forms Usability: Top 10 Recommendations". https://www.nngroup.com/articles/web-form-design/ — Short forms, label proximity, logical order, and generally a single column. Side labels can suit very long desktop forms.
- **E2** Baymard Institute, "Checkout Optimization: 5 Ways to Minimize Form Fields". https://baymard.com/research-articles/checkout-flow-average-form-fields — The number of fields to manage generally matters more than the number of steps. *E-commerce checkout*; the benchmark averages are descriptive, not targets.
- **E4** Nielsen Norman Group, "Few Guesses, More Success: 4 Principles to Reduce Cognitive Load in Forms". https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/ — Grouping, explicit requirements, predictable progression, and relevant branching.
- **E4** Nielsen Norman Group, "Marking Required Fields in Forms". https://www.nngroup.com/articles/required-fields/ — Mark each required field; top-of-form instructions get missed. Optional marking is described as beneficial.
- **E2** Baymard Institute, "E-Commerce Checkouts Need to Mark Both Required Fields and Optional Fields Explicitly". https://baymard.com/research-articles/required-optional-form-fields — Implicit status caused confusion, errors, and abandonment in checkout and long account forms. Short forms were less affected.
- **E2** Baymard Institute, "Checkout UX: Avoid 'Apply' Buttons for Most Fields". https://baymard.com/research-articles/checkout-usability-apply-buttons — Intermediate Apply/Save buttons were missed or confused with continuing. *Checkout-specific.*
- **E3** Google Material Design, "Text fields". https://m3.material.io/components/text-fields — In Material, labels stay visible across states. Required fields use an asterisk explained in supporting text or at the start of the form.

## Alternatives and tradeoffs

- **Required vs optional marking (sources differ in strength).** NN/g requires marking required fields and calls optional marking beneficial. Baymard strongly recommends marking both in long checkout and account forms, and limits the claim for short familiar forms. We adopt: always mark required fields; also mark optional fields in long or mixed forms. A two-field sign-in form needs neither.
- **Floating labels.** Material's label moves but stays visible, unlike a placeholder. No finding validates floating labels empirically; evaluate legibility, truncation, and autofill.
- **Side labels.** Acceptable on expanded and wider viewports for long, repetitive data entry (E4). Avoid them on compact viewports, where they narrow the input (E2).
- **One page vs steps.** Splitting into steps can reduce what users must consider at once. It is not a goal in itself; see PAT-SH-014.

## Exceptions and failure modes

- A search box or a single-purpose two-field form may use a placeholder hint, provided the purpose remains clear (for search, a visible button or icon with an accessible name).
- Failure modes: labels associated only by proximity; asterisks with no legend; format rules revealed only after a failed submit; focus order jumping between columns; collecting data "for later"; help available only in a hover tooltip.

## Evaluation questions

1. Does every field have a visible label that stays after typing and autofill, and is it programmatically associated? [screenshot] [running app] [automated]
2. Is required (and, in long forms, optional) status shown at each field? [screenshot]
3. Can any field be removed, inferred, or deferred without harming the task? [prototype] [user study]
4. Does Tab order follow the visual reading order at each viewport? [running app]
5. Are format constraints visible before entry, not only after an error? [screenshot] [running app]
6. Is previously entered information reused within the same process? [running app]
7. Do users hesitate over what a field means or whether it is required? [user study]

## Related

- Principles: P-07, P-05, P-11, P-12
- Dimensions: D-04, D-06, D-08
- Gates: QG-023, QG-016, QG-026, QG-004
- Patterns: PAT-SH-003 (validation), PAT-MO-004 (keyboards, input types), PAT-MO-005 (mobile form optimization), PAT-SH-014 (steppers), PAT-PW-008 (unsaved changes), PAT-DT-006 (inline editing)

## Change log

- 2026-11-08 — Initial version (ADR-001).
