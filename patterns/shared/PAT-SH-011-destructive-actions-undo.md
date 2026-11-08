---
id: PAT-SH-011
title: Destructive actions — undo, confirmation, and proportional friction
type: pattern
scope: shared
topics: [destructive-actions, undo, confirmation-dialogs, delete, irreversible, friction, recovery]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-11, P-14, P-10]
dimensions: [D-07, D-09]
gates: [QG-025, QG-015, QG-028, QG-029]
related: [PAT-DT-011, PAT-DT-005, PAT-MO-007, PAT-SH-015, PAT-SH-009, PAT-SH-006, PAT-PW-007]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Destructive actions — undo, confirmation, and proportional friction

## Problem

Deleting, sending, and overwriting can cost real work or money. Apps make two opposite mistakes:

- **No protection.** A swipe or a mis-tap permanently deletes.
- **Too much.** Every action asks "Are you sure?" until users click through without reading, so the one dialog that mattered is ignored as well.

A third is false reassurance: an "undo" that cannot restore what the server already deleted.

## Recommendation

**Outcome:** recoverable actions are fast and undoable. Irreversible or high-consequence actions require a deliberate, informed choice. Users never lose data they did not mean to lose.

1. **Classify each action by reversibility and consequence:**

   | Class | Treatment |
   |---|---|
   | Reversible, low consequence (archive, move, remove from list) | Act immediately; offer **Undo** |
   | Reversible with effort (delete to trash) | Act immediately; Undo now; restore from Trash later |
   | Irreversible or high consequence (permanent delete, payment, account closure, send to many) | **Specific confirmation** before acting |
   | Legal, financial, or user-data modifications | At least one of: reversible, checked with a chance to correct, or review-and-confirm (QG-025) |

2. **Design Undo properly.**
   - Undo must truly restore the item: defer the destructive commit or keep a soft-delete.
   - Offer it near the action or in a toast, with enough time to use it. A time-limited Undo must meet WCAG timing requirements (QG-029), or remain available elsewhere (Trash, history, Ctrl/Cmd+Z).
   - Announce "Deleted — Undo available" as a status message (QG-028).
3. **Write confirmations that inform.**
   - Name the object and the consequence: "Delete 'Q3 report'? This also deletes 12 comments and can't be undone."
   - Label the buttons with the action ("Delete report" / "Cancel"), not "OK" / "Cancel" or "Yes" / "No".
   - Never make the destructive button the default.
   - Put initial focus on the least destructive option (PAT-SH-015).
4. **Make friction proportional.** For catastrophic, rare actions (deleting an organization), add typing the object's name or re-authentication. Do not use this for routine deletes.
5. **Separate dangerous from routine controls.** Keep destructive items distinct in style (text and icon, not color alone), spaced from frequent actions, and last in menus (PAT-SH-008).
6. **Allow aborting a press.** Pointer activation completes on release, so sliding off cancels (QG-015). Swipe-to-delete needs a visible alternative and Undo (PAT-MO-007).
7. **Scale with scope.** Bulk destructive actions show the count, and they confirm when Undo is impractical (PAT-SH-006).
8. **Manage focus after removal.** Move focus to the next item, the previous item, or the empty-state control. Never strand it on `<body>`. On Undo, return focus to the restored item.
9. **Optimism is not reversibility.** An optimistic removal must roll back visibly on server failure (PAT-SH-010); that is error handling, not undo.

## Evidence

- **E4** Nielsen Norman Group, "Confirmation Dialogs Can Prevent User Errors — If Not Overused". https://www.nngroup.com/articles/confirmation-dialog/ — Confirm serious or irreversible actions, not routine ones. Name affected objects and consequences and use action-specific labels. Generic, repetitive confirmations lead to automatic acceptance. Undo is preferable where feasible. (Last reviewed 2026-08-07.)
- **E1** W3C, "WCAG 2.2 — SC 3.3.4 Error Prevention (Legal, Financial, Data)". https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data — For these submissions, at least one of: reversible, checked with a chance to correct, or review and confirm. It does *not* require a confirmation dialog for every action.
- **E1** W3C, "WCAG 2.2 — SC 2.5.2 Pointer Cancellation". https://www.w3.org/TR/WCAG22/#pointer-cancellation — Single-pointer functions must be abortable or undoable (no down-event completion unless essential).
- **E1** W3C, "WCAG 2.2 — SC 2.2.1 Timing Adjustable". https://www.w3.org/TR/WCAG22/#timing-adjustable — Applies to time limits, such as a disappearing Undo window, unless an exception applies.
- **E3** Apple, "Alerts". https://developer.apple.com/design/human-interface-guidelines/alerts.md — Do not alert for common, undoable destructive actions. Use an alert for an uncommon, irreversible one when it can prevent an accident. Apple platforms.
- **E3** Apple, "Buttons". https://developer.apple.com/design/human-interface-guidelines/buttons.md — Avoid a destructive action as the primary or default button. Apple platforms.
- **E3** W3C WAI, "APG modal dialog pattern". https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ — Initial focus can go to the least destructive choice; return focus on close. (E3 per `sources/evidence-classes.md`.)
- **E3** W3C WAI, "Developing a Keyboard Interface". https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/ — Deleting the focused element loses focus unless it is moved, for example to the next item.
- **E3** Google Material Design, "Snackbar". https://m3.material.io/components/snackbar — On the web, an actionable snackbar (e.g. Undo) persists until acted on or dismissed, or its content is also available inline.
- **E4** Nielsen Norman Group, "Using Swipe to Trigger Contextual Actions". https://www.nngroup.com/articles/contextual-swipe/ — Swipe actions can be triggered unexpectedly and need visible alternatives and undo or confirmation.

## Alternatives and tradeoffs

- **Confirmation vs undo: the core disagreement.** Undo is the preferred default (NN/g E4, Apple E3). Confirmation remains justified where reversal is impossible or costly. The tension is real when undo is *technically* possible but expensive (e.g. emails already sent to recipients). We resolve it by consequence: if the effect leaves the system (sent, published, paid), treat it as irreversible and confirm, or delay the send with an Undo window. The rubric accepts either approach if it is executed well.
- **Delayed commit vs soft delete.** A delayed server call is simple but fails if the tab closes; soft delete with Trash survives reloads. Prefer soft delete for user content.
- **Type-to-confirm** is strong but costly and a barrier for some users; reserve it for rare, catastrophic actions and allow paste.

## Exceptions and failure modes

- Trivially redoable actions (clearing a search field) need neither.
- Failure modes: "Are you sure?" with OK/Cancel and no object named; confirming every archive; a 3 s Undo toast with no other recovery; "Undo" that cannot restore; Delete beside Save in identical style; a destructive default button; focus lost after delete.

## Evaluation questions

1. For each destructive action, is it undoable, confirmed, or both, and does that match its reversibility? [running app] [prototype]
2. Do confirmations name the object and consequence and use action-labeled buttons? [screenshot]
3. Does Undo actually restore the item (including after a short delay or reload, where promised)? [running app]
4. Can a keyboard or screen-reader user reach Undo before it disappears? [running app]
5. After deletion and after Undo, where does focus go? [running app]
6. Are destructive controls visually and spatially separated from frequent ones? [screenshot]
7. Do users read confirmations or click through by habit? [user study]

## Related

- Principles: P-11, P-14, P-10
- Dimensions: D-07, D-09
- Gates: QG-025, QG-015, QG-028, QG-029
- Patterns: PAT-DT-011 (undo over confirm for experts), PAT-DT-005 (focus after delete), PAT-MO-007 (swipe-to-delete), PAT-SH-015 (dialogs), PAT-SH-009 (toasts), PAT-SH-006 (bulk), PAT-PW-007 (sync conflicts)

## Change log

- 2026-11-08 — Initial version (ADR-001).
