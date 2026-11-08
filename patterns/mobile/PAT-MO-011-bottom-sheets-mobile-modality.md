---
id: PAT-MO-011
title: Bottom sheets, action sheets, and full-screen dialogs on compact screens
type: pattern
scope: mobile
topics: [bottom-sheet, action-sheet, full-screen-dialog, modality, detents, scrim, dismissal, back-button, focus]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, keyboard, assistive-tech]
principles: [P-10, P-04, P-12, P-06, P-11]
dimensions: [D-03, D-07, D-08, D-02]
gates: [QG-002, QG-004, QG-006, QG-018, QG-060, QG-053]
related: [PAT-SH-015, PAT-SH-011, PAT-SH-005, PAT-SH-008, PAT-PW-003, PAT-PW-008, PAT-MO-001, PAT-MO-002, PAT-MO-004, PAT-MO-007, PAT-MO-009, PAT-RS-010]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Bottom sheets, action sheets, and full-screen dialogs on compact screens

## Problem

Centred desktop-style dialogs work poorly on a phone: small, far from the thumb, cramped when the keyboard opens. Compact layouts use **bottom sheets** (partial-height panels from the bottom edge), **action sheets** (a few choices for one object), and **full-screen dialogs** (a temporary full-screen task such as composing). Typical web failures: drag-only closing; browser Back leaving the page instead of closing the sheet; focus left behind; inner scrolling that scrolls the page or dismisses the sheet; the keyboard hiding the sheet's input; stacked sheets; unsaved input lost by one tap on "×".

When to interrupt with a modal at all, focus containment, and stacking rules are universal and live in **PAT-SH-015**. This pattern covers the compact-touch containers.

## Recommendation

**Outcome:** the right container for the task, opened near the hand, always closable in several obvious ways, with focus and Back behaving predictably and no lost work.

**Choose the container**

1. **Modal bottom sheet** (with scrim) for short secondary tasks tied to the current screen — filters (PAT-SH-005), sort, share.
2. **Standard (non-modal) sheet** for supplementary content that coexists with a still-usable main view (map place details, mini-player).
3. **Action sheet** for a few choices about one object; destructive choice last and distinct; include Cancel (PAT-SH-008, PAT-SH-011).
4. **Full-screen dialog** for multi-field tasks (compose, edit) too cramped for a sheet with the keyboard open; title it, with explicit Save/Done and Cancel.
5. **Never use a sheet for main content** or primary navigation.
6. **On wider windows** these become side sheets, popovers, or centred dialogs (PAT-RS-010); task and dismissal routes stay the same.

**Make it closable and predictable**

7. **Multiple dismissal routes:** a visible Close/Cancel/Done button (≥ 44 px, PAT-MO-001), tapping the scrim for modal sheets with nothing to lose, Escape with a keyboard, and dragging down via a handle. **Drag is never the only way** (WCAG 2.5.7, QG-018).
8. **Browser Back closes the overlay** when it looks like a new layer, rather than leaving the underlying page (QG-060, PAT-PW-003). Push a history entry when opening and handle its removal on close.
9. **Guard user content.** If the sheet or dialog holds edits, closing by scrim, drag, or Back asks to keep or discard, or saves a draft (PAT-PW-008).
10. **Manage focus.** Move focus in on open; contain Tab while modal without trapping (QG-002); return focus to the invoker on close; keep logical order (QG-004); make the background inert.
11. **One at a time.** Replace content within a sheet or move to a full-screen step rather than stacking.

**Fit the compact viewport**

12. **Respect bottom safe areas** (PAT-MO-009) and keep inputs visible with the keyboard open (QG-053, PAT-MO-004).
13. **Separate scroll from dismiss.** Drag-to-dismiss from the handle/header or only when content is at the top; contain scroll chaining with `overscroll-behavior: contain` (PAT-MO-007).
14. **Expandable heights** ("detents") are a native convention; on the web, offer an expand button as well as a drag.

## Evidence

- **E3** Google, "Material Design 3 — Bottom sheets". https://m3.material.io/components/bottom-sheets — For secondary content in compact and medium windows, not main app content; standard vs modal variants differ by whether a scrim blocks interaction; both dismissible; max width 640 dp; optional drag handle with an accessible 48 dp hit target.
- **E3** Google, "Material Design 3 — Dialogs". https://m3.material.io/components/dialogs — Use sparingly for decisions that block normal operation; one task per dialog; basic and full-screen variants; lower-priority information belongs in less disruptive components.
- **E3** Apple, "Human Interface Guidelines — Modality" and "Sheets". https://developer.apple.com/design/human-interface-guidelines/sheets.md — Modal tasks short and focused, titled, with an obvious dismiss route and protection against losing user-generated content; avoid stacked modal flows; nonmodal alternative for supplementary content; pair Done with Cancel; resizable sheets use a grabber; iPhone medium detents support progressive disclosure.
- **E3** Apple, "Human Interface Guidelines — Alerts". https://developer.apple.com/design/human-interface-guidelines/alerts.md — Reserve alerts for important, actionable interruptions; not for undoable common destructive actions.
- **E3** W3C WAI, "ARIA Authoring Practices — Dialog (Modal)". https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ — Move focus into the dialog, cycle Tab within it, Escape closes, return focus to the invoker; visible close control strongly recommended.
- **E1** W3C, "WCAG 2.2 — 2.1.2 No Keyboard Trap, A". https://www.w3.org/TR/WCAG22/#no-keyboard-trap — Containing focus in a dismissible modal is compatible; a trap with no keyboard exit is not.
- **E1** W3C, "WCAG 2.2 — 2.5.7 Dragging Movements, AA". https://www.w3.org/TR/WCAG22/#dragging-movements — Drag-to-dismiss or drag-to-resize needs a single-pointer alternative.
- **E4** Nielsen Norman Group, "User Control and Freedom". https://www.nngroup.com/articles/user-control-and-freedom/ — When a full-screen overlay looks like a new page, Back should close it rather than leave the page.
- **E4** Nielsen Norman Group, "Modal & Nonmodal Dialogs: When (& When Not) to Use Them". https://www.nngroup.com/articles/modal-nonmodal-dialog/ — Modals interrupt and cause context loss; match modality to importance.
- **E3** MDN, "overscroll-behavior" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior — Prevents scroll chaining from an overlay into the page behind.

*Interpretation (ours):* Material and Apple sheet behaviours are platform conventions; web apps borrow them because many users know them from native apps, not because they are web requirements. The history-entry technique for Back is an implementation suggestion; detailed history handling is in PAT-PW-003.

## Alternatives and tradeoffs

- **A new page** instead of a full-screen dialog gives a real URL and natural Back; better for deep-linkable tasks.
- **Scrim-tap dismissal** is fast but risky when the sheet holds input; disable or confirm then.

## Exceptions and failure modes

- Irreversible confirmations may warrant a centred alert-style dialog instead of a sheet.
- Failures: tiny corner "×"; Back exits the app; focus not moved or not returned; background still scrollable or exposed to screen readers; nested sheets; sheets as main navigation.

## Evaluation questions

- Is each overlay the right type for its task (sheet, action sheet, full-screen, page)? [screenshot] [prototype]
- Can it be dismissed by button, Escape, Back, and (where offered) drag — and is drag never required? [running app]
- Does Back close the overlay and not leave the page? [running app]
- Does focus move in on open, stay contained while modal, and return on close? Is the background inert? [running app] [automated]
- With the keyboard open, are the sheet's inputs and actions visible? [running app]
- Is unsaved input protected on dismissal? [running app]
- Do participants find how to close sheets unprompted? [user study]

## Related

- Principles: [P-10](../../principles/P-10-feedback-predictability.md), [P-04](../../principles/P-04-navigation-orientation.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-06](../../principles/P-06-interaction-ergonomics.md), [P-11](../../principles/P-11-error-prevention-recovery.md); Dimensions: D-03, D-07, D-08, D-02; Gates: QG-002, QG-004, QG-006, QG-018, QG-060, QG-053 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-SH-015, PAT-SH-011, PAT-SH-005, PAT-SH-008, PAT-PW-003, PAT-PW-008, PAT-MO-001, PAT-MO-002, PAT-MO-004, PAT-MO-007, PAT-MO-009, PAT-RS-010

## Change log

- 2026-11-08 — Initial version (ADR-001).
