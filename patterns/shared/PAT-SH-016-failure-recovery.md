---
id: PAT-SH-016
title: Failure recovery — server and network errors, retry, and preserving input
type: pattern
scope: shared
topics: [errors, failure, retry, network-errors, server-errors, error-pages, partial-failure, input-preservation, session-expiry]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-11, P-10, P-13, P-14]
dimensions: [D-07, D-09]
gates: [QG-071, QG-072, QG-029, QG-028, QG-062, QG-093]
related: [PAT-PW-005, PAT-PW-007, PAT-PW-008, PAT-PW-004, PAT-SH-003, PAT-SH-009, PAT-SH-012, PAT-SH-010]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Failure recovery — server and network errors, retry, and preserving input

## Problem

Networks drop, servers time out, sessions expire, and some items in a batch fail. Apps respond with:

- blank screens and spinners that never end;
- raw codes ("Error 500", stack traces);
- a toast that disappears before it is read;
- a form that empties itself after a failed submit;
- a session timeout that throws away a long draft.

Users lose work, retry blindly (sometimes duplicating orders), or abandon.

## Recommendation

**Outcome:** when something fails, users learn what happened in plain language, keep everything they entered, and have a clear way forward: retry, wait, save elsewhere, or get help.

1. **Never lose input.** A failed submission keeps every field value (QG-072). Long-form input is saved as a draft locally or on the server, so reloads and crashes do not erase it (QG-062; PAT-PW-008).
2. **Explain in human terms, at the place of failure.**
   - Say what failed and what to do: "Couldn't save your changes. Check your connection and try again."
   - Keep technical details (status code, request ID) secondary: collapsed or copyable for support.
   - Do not blame the user, and do not imply a system failure when the cause is a correctable field (PAT-SH-003).
3. **Make failures persistent and actionable.** Use an inline message or banner with **Retry**. A failure is never shown only in a transient toast (PAT-SH-009), and the message is announced (QG-028). Show region-level failures in the region; keep the rest of the page usable.
4. **Retry safely.**
   - Make submissions idempotent, or detect duplicates, so retrying cannot double-charge or double-send.
   - Auto-retry transient read failures with backoff and show "Retrying…".
   - Do not auto-retry non-idempotent writes without the user knowing.
5. **Distinguish failure types:**
   - **Offline / network:** say so; keep cached content usable; queue or disable network-only actions (PAT-PW-005, PAT-PW-007; QG-093).
   - **Server error:** apologize briefly and offer Retry, status page, or support.
   - **Not found / no permission:** say which, without leaking sensitive information. Offer a way back to a known place (home, parent, search).
   - **Conflict** (someone else changed it): show both versions or the changed fields and let the user choose (PAT-PW-007).
6. **Report partial failures precisely.** For batches: "18 of 20 uploaded. 2 failed: [names] — Retry failed". Keep failed items selected or listed (PAT-SH-006).
7. **Handle session expiry gracefully.**
   - Warn before a time limit with an option to extend (QG-029).
   - If the session has ended, re-authenticate *in place* (dialog or new tab), then resume the action with the data preserved.
8. **Design error pages as navigation.** 404 and 500 pages keep the app frame, explain the problem, and offer search, home, and the parent location. The URL stays unchanged so reload can succeed later.
9. **Roll back optimistic changes visibly** with an explanation, and restore focus sensibly (PAT-SH-010).

## Evidence

- **E4** Nielsen Norman Group, "Error-Message Guidelines". https://www.nngroup.com/articles/error-message-guidelines/ — Messages are visible, plain-language, and constructive; offer remedies; preserve users' work rather than making them start over.
- **E2** Nielsen Norman Group, "Indicators, Validations, and Notifications". https://www.nngroup.com/articles/indicators-validations-notifications/ — A mobile participant missed a brief error and waited for content that would not load. Fading toasts are poor for errors.
- **E2** Nielsen Norman Group, "Mobile User Experience: Limitations and Strengths". https://www.nngroup.com/articles/mobile-ux/ — Variable connectivity and fragmented attention: save state so users can resume without redoing work. (2015; offline persistence is our implementation inference.)
- **E4** Nielsen Norman Group, "Designing Empty States in Complex Applications". https://www.nngroup.com/articles/empty-state-interface-design/ — Users cannot tell failure from "found nothing" when empty containers are unexplained.
- **E2** Baymard Institute, "Improve Validation Errors with Adaptive Messages". https://baymard.com/research-articles/adaptive-validation-error-messages — Generic messages left users stuck. Avoid implying a system or payment-provider failure when the issue is correctable. *E-commerce.*
- **E3** React documentation, "useOptimistic". https://react.dev/reference/react/useOptimistic — Optimistic deletes restore the item and display an error on failure.
- **E2** Nielsen Norman Group, "Consistency in the Omnichannel Experience". https://www.nngroup.com/articles/omnichannel-consistency/ — Users were frustrated when changes did not appear elsewhere. Pending, failed, and stale states must be understandable.
- **E3** Google, Android Developers, "App orientation, aspect ratio, and resizability". https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability — Preserve app state, including form input, across configuration changes. Android guidance; the principle transfers.
- **E1** W3C, "WCAG 2.2 — SC 2.2.1 Timing Adjustable". https://www.w3.org/TR/WCAG22/#timing-adjustable — Time limits need an off, adjust, or warn-and-extend option (at least 20 seconds to extend), unless an exception applies.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Failure and retry status must reach AT without receiving focus.

**Evidence note:** idempotent retry, backoff, in-place re-authentication, and error-page design are our engineering inferences from the mechanisms above. No finding tests them directly.

## Alternatives and tradeoffs

- **Auto-retry vs manual Retry.** Auto-retry hides transient blips but can mask persistent failures and drain batteries. Use bounded auto-retry for reads, show the state, and fall back to manual Retry.
- **Local drafts vs server drafts.** Local drafts survive offline use but stay on one device and raise privacy questions on shared machines. Server drafts sync but need connectivity. Many apps use both (P-14).
- **Detail vs simplicity in messages.** Request IDs help support but intimidate users. Collapse them by default.

## Exceptions and failure modes

- Security-sensitive failures (authentication, permissions) may deliberately withhold specifics.
- Failure modes: a blank screen on an unhandled exception; a spinner forever after a timeout; "Something went wrong" with no action; a form cleared after a 500; Retry that double-submits; session expiry that drops the draft; a 404 without the app's navigation.

## Evaluation questions

1. With the network throttled or cut mid-action, does the UI show an in-place message with Retry, rather than a blank screen or an endless spinner? [running app]
2. After a failed submit, are all entered values intact? [running app]
3. Are failure messages persistent, plain-language, and announced? [running app] [automated]
4. Can retrying a payment or send ever produce a duplicate? [running app]
5. Do partial batch failures identify the failed items and offer a targeted retry? [running app]
6. When a session expires mid-edit, is the work preserved through re-authentication? [running app]
7. Do 404 and 500 pages keep navigation and offer a way forward? [screenshot] [running app]

## Related

- Principles: P-11, P-10, P-13, P-14
- Dimensions: D-07, D-09
- Gates: QG-071, QG-072, QG-029, QG-028, QG-062, QG-093
- Patterns: PAT-PW-005 (offline), PAT-PW-007 (sync, conflicts), PAT-PW-008 (unsaved changes), PAT-PW-004 (restoration), PAT-SH-003 (field errors), PAT-SH-009 (feedback channels), PAT-SH-012 (error-empty), PAT-SH-010 (loading and optimistic UI)

## Change log

- 2026-11-08 — Initial version (ADR-001).
