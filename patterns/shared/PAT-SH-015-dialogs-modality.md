---
id: PAT-SH-015
title: Dialogs and modality — modal, nonmodal, sheets, and inline expansion
type: pattern
scope: shared
topics: [dialogs, modals, modality, sheets, popovers, focus-management, dismissal, stacking]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-10, P-12, P-14, P-04]
dimensions: [D-03, D-07, D-08]
gates: [QG-002, QG-004, QG-005, QG-006, QG-060, QG-012]
related: [PAT-MO-011, PAT-PW-003, PAT-DT-005, PAT-SH-011, PAT-SH-014, PAT-PW-008, PAT-SH-009]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Dialogs and modality — modal, nonmodal, sheets, and inline expansion

## Problem

Modal dialogs block everything behind them. That is right for a decision that must happen now, and costly for everything else. Apps overuse them for routine status, forms that need reference to the underlying page, and marketing. Implementation failures are equally common:

- focus stays behind the dialog or escapes into the page;
- Escape does nothing;
- browser Back closes the whole page instead of the dialog;
- a second dialog stacks on the first;
- closing discards what the user typed;
- focus is lost to `<body>` on close.

## Recommendation

**Outcome:** users are interrupted only when an immediate decision or focused subtask justifies it. Every overlay has an obvious exit, keeps focus where keyboard and screen-reader users expect it, and never loses input.

1. **Choose the lightest presentation that works:**

   | Need | Presentation |
   |---|---|
   | Supplementary information or quick edit related to visible content | Inline expansion or a nonmodal panel/popover (PAT-SH-014) |
   | Status or low-priority information | Inline or toast (PAT-SH-009) — never a modal |
   | Short, focused subtask or decision that must complete before continuing | Modal dialog |
   | Consequential, irreversible decision | Modal confirmation (PAT-SH-011) |
   | Long or complex subtask | Full page or full-screen dialog with its own URL |
   | Content needed alongside the main task | Nonmodal side panel or standard (nonmodal) sheet |

2. **Keep one task per dialog.** Give it a clear title, action-labeled buttons, and no nested dialogs. If a dialog needs another dialog, convert the flow to a page or a step.
3. **Manage focus.**
   - On open, move focus into the dialog. Target the first field, a static heading for long content, or the least destructive button for confirmations.
   - Contain Tab and Shift+Tab within the dialog, and make background content inert.
   - On close, return focus to the invoking control. If the invoker no longer exists, move focus to the next logical place (PAT-DT-005).
4. **Provide every exit.** Offer a visible Close or Cancel, and Escape. Clicking or tapping the scrim may close nonconsequential dialogs. For overlays that look like pages (full-screen dialogs, sheets on compact), browser Back closes the overlay, not the underlying view (QG-060; PAT-PW-003).
5. **Protect input.** If closing would discard entered data, ask, or keep a draft (PAT-PW-008).
6. **Containment is not a keyboard trap.** Focus containment is fine while a keyboard exit (Escape, Close) exists (QG-002).
7. **Use semantics.** Prefer the native `<dialog>` element shown modally, or the equivalent ARIA pattern with an accessible name and description. We infer the native element reduces focus and inert bugs; verify behavior in the browsers you support.
8. **Keep content visible.** Dialogs scroll internally, never exceed the viewport, and keep their actions reachable at 200 % zoom and with the virtual keyboard open. Sticky dialog footers must not hide the focused field (QG-006).
9. **Hover and focus popovers** (non-dialog) must be dismissible, hoverable, and persistent (QG-012).

Compact presentation (bottom sheets, action sheets, full-screen dialogs) is in PAT-MO-011.

## Evidence

- **E4** Nielsen Norman Group, "Modal & Nonmodal Dialogs: When (& When Not) to Use Them". https://www.nngroup.com/articles/modal-nonmodal-dialog/ — Modals interrupt, force context switching, and can make users forget their task. Match modality to importance.
- **E3** W3C WAI, "APG modal dialog pattern". https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ — Move focus in on open; Tab cycles within; Escape closes. Initial focus depends on content and risk. Return focus to the invoker unless it is gone. A visible close control is strongly recommended. (E3 per `sources/evidence-classes.md`.)
- **E1** W3C, "WCAG 2.2 — SC 2.1.2 No Keyboard Trap". https://www.w3.org/TR/WCAG22/#no-keyboard-trap — Focus must be movable away by keyboard. Containment within a dismissible modal is compatible with this.
- **E1** W3C, "WCAG 2.2 — SC 2.4.3 Focus Order". https://www.w3.org/TR/WCAG22/#focus-order — Focus order must preserve meaning and operability.
- **E1** W3C, "WCAG 2.2 — SC 2.4.11 Focus Not Obscured (Minimum)". https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum — Author content must not entirely hide the focused component.
- **E4** Nielsen Norman Group, "User Control and Freedom". https://www.nngroup.com/articles/user-control-and-freedom/ — A full-screen overlay that looks like a page should close on Back.
- **E3** Apple, "Modality" and "Sheets". https://developer.apple.com/design/human-interface-guidelines/modality.md — Use modality only for a clear benefit; keep the task short and titled; provide an obvious dismissal; guard against losing content; avoid stacked modals. Prefer nonmodal presentation for supplementary content needed alongside the main task. Apple platforms.
- **E3** Google Material Design, "Dialogs". https://m3.material.io/components/dialogs — Use sparingly, for blocking decisions; one task per dialog; low- and medium-priority information goes to less disruptive components. Material convention.
- **E3** Google Material Design, "Bottom sheets". https://m3.material.io/components/bottom-sheets — Modal and standard sheets differ in whether a scrim blocks the underlying UI, and both are dismissible. Material convention.

## Alternatives and tradeoffs

- **Modal vs nonmodal for editing.** A modal focuses attention but hides context the user may need ("what was the order number?"). A nonmodal panel keeps context but allows conflicting edits. Choose by whether users need to reference the background.
- **Dialog vs page.** Pages have URLs, survive reload, and avoid focus complexity. Dialogs keep context. Long or shareable subtasks belong on pages.
- **Scrim-tap dismissal** is convenient but risks losing input; disable it once data is entered, or ask before discarding.

## Exceptions and failure modes

- Legally or security-required interruptions (session expiry with an extend option, QG-029) are justified modals.
- Failure modes: modal newsletter prompts on first load; no Close button and Escape ignored; focus left behind the scrim; confirm nested inside a dialog; Back exiting the page while a sheet is open; dialogs taller than the viewport hiding submit; silent discard of form input on close.

## Evaluation questions

1. Is each modal justified by an immediate decision or focused subtask, or could it be inline or nonmodal? [screenshot] [prototype]
2. On open, does focus move into the dialog, and does Tab stay inside? [running app]
3. Do Escape and a visible Close both work, and does focus return to the invoker? [running app]
4. Does browser Back close full-screen overlays without leaving the view? [running app]
5. Are dialogs ever stacked? [running app]
6. Is entered data protected on dismissal? [running app]
7. At 200 % zoom and with the virtual keyboard open, are dialog actions reachable? [running app]

## Related

- Principles: P-10, P-12, P-14, P-04
- Dimensions: D-03, D-07, D-08
- Gates: QG-002, QG-004, QG-005, QG-006, QG-060, QG-012
- Patterns: PAT-MO-011 (compact sheets), PAT-PW-003 (Back and history), PAT-DT-005 (focus management), PAT-SH-011 (confirmations), PAT-SH-014 (inline expansion), PAT-PW-008 (unsaved changes), PAT-SH-009 (nonmodal feedback)

## Change log

- 2026-11-08 — Initial version (ADR-001).
