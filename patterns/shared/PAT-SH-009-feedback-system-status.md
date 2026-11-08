---
id: PAT-SH-009
title: Feedback and system status — choosing toasts, inline messages, and banners
type: pattern
scope: shared
topics: [feedback, system-status, toasts, snackbars, banners, inline-status, success-messages, live-regions]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-10, P-12, P-14, P-11]
dimensions: [D-07, D-08, D-09]
gates: [QG-028, QG-029, QG-070, QG-006]
related: [PAT-SH-010, PAT-SH-003, PAT-SH-016, PAT-SH-011, PAT-SH-015, PAT-PW-005, PAT-PW-007]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Feedback and system status — choosing toasts, inline messages, and banners

## Problem

Users need to know that an action registered, what the system is doing, and whether it worked. Apps fail them in three ways:

- **Silence.** A save happens with no sign, or a background change alters the user's content unannounced.
- **The wrong channel.** A critical failure appears in a toast that fades in three seconds. A routine success interrupts with a modal.
- **Inaccessible status.** The message appears visually but is never announced, or is announced by stealing focus.

On compact screens, toasts and banners also compete with the keyboard, sticky bars, and the content itself.

## Recommendation

**Outcome:** every user-initiated action gets timely, proportionate feedback, in a place and for a duration that match its importance, and assistive technology announces it without losing the user's place.

1. **Acknowledge immediately; confirm truthfully.** Show the press state and a pending state on the control at once (e.g. a button label that changes to "Saving…" with an indicator). Distinguish *acknowledged* from *completed*: say "Saved" only when the save succeeded. Loading behavior is in PAT-SH-010.
2. **Pick the channel by importance and required action:**

   | Situation | Channel |
   |---|---|
   | Field- or item-level result | Inline, next to the item (status text, icon, changed state) |
   | Low-importance success that is safe to miss ("Archived") | Toast/snackbar, optionally with one action (Undo) |
   | Page- or app-level persistent condition (offline, read-only, quota exceeded) | Banner at the top of the affected region, persistent until resolved or dismissed |
   | Blocking decision with consequences | Dialog (PAT-SH-015) |
   | Failure that needs user action | Inline or banner, persistent, with a recovery action (PAT-SH-016) |

3. **Never let a transient message be the only record** of an error, or the only route to a recovery action. On the web, either repeat the toast's message inline or near the action, or keep an actionable toast visible until the user acts or dismisses it.
4. **Make toasts accessible.**
   - Announce them via a live region (`role="status"`, or `alert` for urgent messages) without moving focus (QG-028).
   - Show one at a time, with at most one action.
   - Pause the timeout on hover and focus. Any time-limited action must satisfy WCAG timing requirements (QG-029). Material's 4–10 seconds for non-action snackbars is a platform convention, not a compliance threshold.
   - Do not cover the focused element or primary actions (QG-006).
5. **Place status near its cause.** Feedback appears where the user's attention already is. On wide layouts, avoid corner toasts far from a mid-page action unless the action is also reflected inline.
6. **Use more than one cue.** Combine text with icon, color, or motion; never color alone. Haptics and sound are optional enhancements on platforms that support them.
7. **Confirm significant successes** (payment sent, invitation delivered) with specifics: what happened, to what, and what happens next. Skip success messages for trivial, self-evident changes.
8. **Report system-initiated changes** (sync updates, another user's edit, an expired session) in a way that does not destroy the user's in-progress work. Sync states are in PAT-PW-007; offline status is in PAT-PW-005.

## Evidence

- **E4** Nielsen Norman Group, "Visibility of System Status". https://www.nngroup.com/articles/visibility-system-status/ — Timely feedback tells users whether an action registered and what is happening. Silent changes undermine trust.
- **E2** Nielsen Norman Group, "Indicators, Validations, and Notifications". https://www.nngroup.com/articles/indicators-validations-notifications/ — Choose the communication type by urgency and required action. A mobile participant missed a brief error message and waited for content that never loaded. Fading toasts are poor for errors.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Status messages must be programmatically determinable without receiving focus.
- **E1** W3C, "WCAG 2.2 — SC 2.2.1 Timing Adjustable". https://www.w3.org/TR/WCAG22/#timing-adjustable — Content-set time limits must be adjustable or extendable unless an exception applies.
- **E3** Google Material Design, "Snackbar". https://m3.material.io/components/snackbar — One snackbar at a time, at most one action. Non-action snackbars auto-dismiss after 4–10 seconds depending on platform. *On web*, the message must also appear inline, or the snackbar must be actionable and persist; announce without moving focus. Material convention.
- **E3** Apple, "Feedback". https://developer.apple.com/design/human-interface-guidelines/feedback.md — Use multiple channels, place status near the items it describes, and reserve alerts for critical, actionable information. Apple platforms.
- **E3** Apple, "Buttons". https://developer.apple.com/design/human-interface-guidelines/buttons.md — Buttons can show an activity indicator and a changed label for a delayed action. Apple platforms.
- **E4** Nielsen Norman Group, "Modal & Nonmodal Dialogs". https://www.nngroup.com/articles/modal-nonmodal-dialog/ — Modals interrupt and cost context, so match modality to importance.
- **E2** Nielsen Norman Group, "Consistency in the Omnichannel Experience". https://www.nngroup.com/articles/omnichannel-consistency/ — Users expect changes to be reflected everywhere. Saved, pending, and stale states matter across devices.

## Alternatives and tradeoffs

- **Toast vs inline success.** Toasts are cheap and general, but easy to miss and far from the action on wide screens. Inline status is precise but needs layout space. We infer: inline for item-level changes, toast for list-level changes with Undo.
- **Auto-dismiss vs persistent.** Auto-dismiss reduces clutter. Persistence guarantees the message is seen and its action stays reachable. Persist anything with an action the user may need, or anything describing a failure.
- **Banners** are reliable for persistent conditions but consume compact vertical space; collapse to one line with "Details".

## Exceptions and failure modes

- Highly frequent, self-evident actions (toggling a checkbox) need only the state change itself as feedback.
- Failure modes: "Saved" before the server confirms; toasts stacked over bottom navigation; the only Undo in a 3 s toast; live-region spam on every keystroke; color-only status; focus moved to a toast; a banner covering the focused field.

## Evaluation questions

1. For each primary action, is there immediate acknowledgement and a truthful completion state? [running app] [prototype]
2. Is any error or recovery action delivered only through a transient message? [running app]
3. Are toasts and status messages announced by a screen reader without moving focus? [running app] [automated]
4. Can a user who needs more time still reach a toast's action (hover or focus pauses it, or it persists)? [running app]
5. Is feedback located near the action at both compact and large widths? [screenshot]
6. Do toasts or banners obscure focused elements or primary actions? [running app] [screenshot]
7. Can users say whether their last action succeeded? [user study]

## Related

- Principles: P-10, P-12, P-14, P-11
- Dimensions: D-07, D-08, D-09
- Gates: QG-028, QG-029, QG-070, QG-006
- Patterns: PAT-SH-010 (loading), PAT-SH-003 (field errors), PAT-SH-016 (failures), PAT-SH-011 (undo), PAT-SH-015 (dialogs), PAT-PW-005 (offline status), PAT-PW-007 (sync states)

## Change log

- 2026-11-08 — Initial version (ADR-001).
