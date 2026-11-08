---
id: PAT-MO-004
title: Virtual keyboards, input types, and keyboard-aware layout
type: pattern
scope: mobile
topics: [virtual-keyboard, inputmode, enterkeyhint, autocomplete, input-type, autocorrect, keyboard-occlusion, forms]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, keyboard, assistive-tech]
principles: [P-07, P-11, P-12, P-06]
dimensions: [D-04, D-08, D-07]
gates: [QG-053, QG-006, QG-023, QG-026, QG-027]
related: [PAT-MO-005, PAT-MO-009, PAT-MO-010, PAT-MO-011, PAT-SH-002, PAT-SH-003, PAT-SH-004, PAT-RS-009, PAT-RS-010]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Virtual keyboards, input types, and keyboard-aware layout

## Problem

On a touch device the on-screen keyboard is part of the interface and takes a large share of the screen, especially in landscape. Two failures follow. The **wrong keyboard**: a phone field opens the alphabetic layout, Return says "return" instead of "Search", autocorrect turns a surname into a dictionary word. The **keyboard covers the task**: the focused field, its error, a sticky Submit, or suggestions disappear behind it.

## Recommendation

**Outcome:** every field opens a keyboard suited to its data, Return does what its label says, the browser and password manager can fill known data, and the focused field, its feedback, and the way forward stay visible while typing.

**Choose semantics per field**

1. **Use the correct `type`** when the value must be that kind of data (`email`, `tel`, `url`, `search`); it brings validation and a suitable keyboard.
2. **Use `inputmode`** to hint the keyboard where `type` would be wrong — e.g. `inputmode="numeric"` on a `type="text"` field for card numbers, one-time codes, or postal codes, which are identifiers rather than quantities. `inputmode` changes only the keyboard; it does not validate. Values: `none`, `text`, `decimal`, `numeric`, `tel`, `search`, `email`, `url`.
3. **Label the Return key with `enterkeyhint`** (`enter`, `done`, `go`, `next`, `previous`, `search`, `send`) to match what pressing it does, and make the behaviour match the label.
4. **Add `autocomplete` tokens** for personal data (`name`, `email`, `tel`, `street-address`, `postal-code`, `cc-number`, `one-time-code`, with `shipping`/`billing` sections). This serves WCAG 1.3.5 and enables autofill. Do not set `autocomplete="off"` broadly; never block paste or password managers (QG-027).
5. **Turn off autocorrection and auto-capitalisation where dictionaries are wrong** — names, addresses, usernames, codes, email — and keep them for prose. (Attribute support for these hints varies by browser; verify on target devices.)
6. **Keep valid characters valid.** A numeric keyboard must not prevent legitimate input (international postal codes with letters, phone numbers with "+").

**Keep the task visible with the keyboard open**

7. **Ensure the focused field and its label, hint, and error remain visible** (QG-053, QG-006). Let the browser scroll focused fields into view; do not fight it with fixed-height (`100vh`) containers that cannot scroll.
8. **Sticky footers and bottom bars must not cover the focused field or the submit control** when the keyboard is open. Either let them scroll with content, hide them while a text field is focused, or position them above the keyboard using platform features below.
9. **Size keyboard-aware layouts deliberately.** The viewport meta `interactive-widget` key (`resizes-visual` default, `resizes-content`, `overlays-content`) and the experimental VirtualKeyboard API (`overlaysContent`, `geometrychange`, `env(keyboard-inset-*)`) give control in supporting browsers; treat them as progressive enhancements, with the default browser behaviour as the baseline (PAT-MO-009).
10. **Leave room for suggestions.** Autocomplete lists must be legible above the keyboard (PAT-SH-004 for suggestion design).
11. **Test on real devices in portrait and landscape** — landscape leaves very little height above the keyboard.

Field count, labels, and validation messages are universal form concerns: see PAT-SH-002 and PAT-SH-003. Mobile form flow is PAT-MO-005.

## Evidence

- **E1** W3C, "WCAG 2.2 — 1.3.5 Identify Input Purpose, AA". https://www.w3.org/TR/WCAG22/#identify-input-purpose — Field purpose must be programmatically determinable for listed input purposes. Autofill tokens are our implementation choice.
- **E1** W3C, "WCAG 2.2 — 2.4.11 Focus Not Obscured (Minimum), AA". https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum — Author-created content must not entirely hide a focused component; applies to sticky bars. The keyboard itself is not author content, so keyboard occlusion is covered by our threshold QG-053.
- **E1** W3C, "WCAG 2.2 — 3.3.8 Accessible Authentication (Minimum), AA". https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum — Supports allowing password managers and paste.
- **E3** MDN, "inputmode" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode — Lists values; hint only, no validation; prefer the matching `type` where data must be of that type. Baseline widely available.
- **E3** MDN, "enterkeyhint" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint — Lists values; labels vary by browser and language. Baseline widely available.
- **E3** MDN, "autocomplete" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete — Token syntax and examples; links tokens to WCAG 1.3.5; warns against broad `off`; notes `off` does not stop most password managers.
- **E3** MDN, "VirtualKeyboard API" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/API/VirtualKeyboard_API — Default browser behaviour resizes the viewport and scrolls the focused field into view; `overlaysContent`, `geometrychange`, keyboard-inset env variables. Experimental, not Baseline; MDN compatibility data lists Chrome 94 and no Firefox or Safari support.
- **E3** MDN, "&lt;meta name="viewport"&gt;" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport — `interactive-widget` values and their effect on the viewport and viewport units.
- **E2** Baymard Institute, "'Touch Keyboard' Implementations Have Improved Just 9% Since 2013". https://baymard.com/research-articles/mobile-touch-keyboards — Mobile testing found better performance with purpose-built keyboards, especially numeric, more typos with the standard keyboard for numeric fields, and autocorrect silently changing names and addresses. E-commerce, 2015; mechanisms likely generalise.
- **E3** Apple, "Human Interface Guidelines — Virtual keyboards". https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards.md — Keyboard should match data type; Return label should describe the action.
- **E4** W3C, "Mobile Accessibility" (2015 draft), sections 5.1–5.3. https://www.w3.org/TR/mobile-accessibility-mapping/ — Recommends data-appropriate virtual keyboards; warns keyboard changes may confuse some screen-reader users.

## Alternatives and tradeoffs

- **Custom on-page keypads** (`inputmode="none"`) suit PIN pads or calculators but remove familiar keyboard features, dictation, and some AT support. Use rarely.
- **Hide vs reposition sticky bars on focus.** Hiding is robust and simple; repositioning above the keyboard keeps the action reachable but depends on browser support.
- **`resizes-content`** makes layouts reflow to the smaller viewport; it can cause large jumps. Test both.

## Exceptions and failure modes

- `type="number"` on identifiers (card numbers, codes, postal codes). These are strings, not quantities; our interpretation is to use `type="text"` with `inputmode="numeric"` and validate the string.
- Inconsistent keyboards across one flow; `enterkeyhint="next"` that submits; `100vh` containers that clip fields; footers riding up over the field.
- Assuming the keyboard is present: tablets with hardware keyboards and touch laptops show no virtual keyboard — layouts must work both ways (PAT-RS-009).

## Evaluation questions

- Does each field declare an appropriate `type`/`inputmode`, `enterkeyhint`, and `autocomplete` token? [automated] [running app]
- Does the keyboard shown on a real device match the data for every field? [running app]
- With the keyboard open, are the focused field, its error, and the submit control visible in portrait and landscape? [running app]
- Is paste and password-manager fill permitted in credential fields? [running app]
- Are names and addresses left uncorrupted by autocorrect? [running app] [user study]
- Do sticky bars obscure focused fields? [running app]

## Related

- Principles: [P-07](../../principles/P-07-input-efficiency.md), [P-11](../../principles/P-11-error-prevention-recovery.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-06](../../principles/P-06-interaction-ergonomics.md); Dimensions: D-04, D-08, D-07; Gates: QG-053, QG-006, QG-023, QG-026, QG-027 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-MO-005, PAT-MO-009, PAT-MO-010, PAT-MO-011, PAT-SH-002, PAT-SH-003, PAT-SH-004, PAT-RS-009, PAT-RS-010

## Change log

- 2026-11-08 — Initial version (ADR-001).
