---
id: PAT-PW-008
title: Unsaved changes — drafts and autosave first, beforeunload as a last resort
type: pattern
scope: pwa
topics: [unsaved-changes, beforeunload, autosave, drafts, navigation-guard, visibilitychange, data-loss, session-timeout]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-11, P-14, P-10, P-01]
dimensions: [D-07, D-09]
gates: [QG-062, QG-072, QG-029, QG-060]
related: [PAT-PW-004, PAT-PW-003, PAT-PW-007, PAT-PW-012, PAT-SH-002, PAT-SH-011, PAT-SH-015, PAT-DT-006]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Unsaved changes — drafts and autosave first, beforeunload as a last resort

## Problem

Users lose work when they tap a link mid-edit, swipe back, close a tab, when the OS kills a backgrounded browser, when an update reloads the app, or when a session times out. The usual defence is a `beforeunload` "Leave site?" dialog. It is weak:

- **The browser shows its own generic wording**, so you can't explain what will be lost.
- **It only appears after the user has interacted with the page.**
- **It may never fire, especially on mobile.** Apps that rely on it lose data silently.
- **Apps that register it permanently** nag users who have nothing unsaved.

## Recommendation

**Outcome:** a user's unfinished input survives navigation, reload, app switching, termination, updates, and timeouts. Warnings appear only when something would really be lost.

1. **Make drafts the primary protection.**
   - Autosave in-progress input locally (IndexedDB) as the user edits, debounced, and on `visibilitychange` to hidden.
   - For valuable content, also save server-side drafts.
   - Restore drafts on return, with a visible "Draft restored · Discard" (PAT-PW-004).
   - This satisfies QG-062 without relying on any prompt.
2. **Show save state.** For autosaving editors, show "Saving… / Saved / Couldn't save — Retry" near the content. Distinguish "saved on this device" from "saved to your account" (PAT-PW-007).
3. **Guard in-app navigation with your own UI.** When the app controls the transition (router links, in-app Back, closing a panel or dialog with edits), offer a specific choice: "Discard changes to *Invoice #1042*?", with Keep editing as the default, plus Save and Discard. Or, better, keep the draft and skip the question. You control the wording here, so be specific.
4. **Register `beforeunload` only while there is unsaved work that wasn't captured as a draft.** Add the handler when the form becomes dirty and remove it after saving or discarding. Never register it unconditionally. Don't write custom message text, because it won't be shown. Treat it as a secondary, desktop-leaning safety net.
5. **Don't let updates or timeouts destroy work.**
   - App updates wait for a safe point or save drafts first (PAT-PW-012).
   - Session timeouts warn and let users extend (QG-029, WCAG 2.2.1).
   - After re-authentication, return to the same view with the input intact.
6. **Preserve input on failed submit** (QG-072). An error never clears the form.
7. **Don't trap Back.** A guard may ask once. It must not loop, and it must not stop Back from closing an overlay that has no edits (QG-060).

## Evidence

- **E3** MDN Web Docs, "Window: beforeunload event" (modified 2026-10-26). https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event — The dialog requires sticky activation. It shows browser-controlled generic text, not the author's message. It may not fire reliably, especially when a mobile app is killed. MDN recommends registering the handler only while there are unsaved changes and removing it after saving, and names `visibilitychange` as the more reliable signal for saving state.
- **E3** Google web.dev, "Back/forward cache". https://web.dev/articles/bfcache — Avoid `unload` handlers, which affect lifecycle and bfcache eligibility.
- **E4** Nielsen Norman Group, "User Control and Freedom". https://www.nngroup.com/articles/user-control-and-freedom/ — Users need clear exits, and entered work should be kept when they return.
- **E2** Nielsen Norman Group, "Mobile User Experience: Limitations and Strengths". https://www.nngroup.com/articles/mobile-ux/ — Mobile use is interrupted, so save state so users can resume without redoing work.
- **E3** Atlassian, "Inline edit" (Forge UI Kit). https://developer.atlassian.com/platform/forge/ui-kit/components/inline-edit/ — Keep large text edits open on blur to avoid accidentally saving or discarding them.
- **E3** Android Developers, "App orientation, aspect ratio, and resizability". https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability — Preserve form input across configuration changes. Native guidance, applied here by analogy.
- **E3** MDN Web Docs, "Storage quotas and eviction criteria". https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria — Local drafts aren't guaranteed to persist. Handle failed writes.
- **E1** W3C, "WCAG 2.2 — SC 2.2.1 Timing Adjustable". https://www.w3.org/TR/WCAG22/#timing-adjustable — Time limits must be adjustable, or warned about with at least 20 seconds to extend, with listed exceptions.
- **E4** Nielsen Norman Group, "Confirmation Dialogs Can Prevent User Errors — If Not Overused". https://www.nngroup.com/articles/confirmation-dialog/ — Confirmations should name the affected object and consequence. Routine ones get dismissed on autopilot.

Interpretation (ours): drafts-first follows from MDN's reliability caveat and NN/g's interruption findings. No study compares drafts with leave-warnings.

## Alternatives and tradeoffs

- **Explicit Save with no autosave.** This is appropriate when partial changes would be harmful if applied, for example configuration or permissions. Even then, keep a *local draft* that isn't applied, and guard navigation in the app.
- **Autosave straight to the live record.** Smooth for documents and notes. It needs undo or version history, because every keystroke is committed (PAT-SH-011).
- **Discard-by-default for trivial input.** A search box or a one-field filter needs no draft or guard. Proportionality matters: guarding everything trains users to dismiss guards.

## Exceptions and failure modes

- Don't persist sensitive fields (passwords, card numbers, OTPs) as drafts. Warn instead.
- Kiosks and shared devices: clear drafts on sign-out or after an idle period.
- Failure modes:
  - `beforeunload` registered on every page.
  - Custom text in `returnValue`, with copy or tests that assume it will appear.
  - Drafts saved only in `beforeunload`, so they're lost when the mobile OS kills the tab.
  - A generic "Are you sure?" modal on in-app navigation.
  - A guard that fires after a successful save.
  - A timeout that redirects to login and drops the form.
  - An update reload in the middle of editing.

## Evaluation questions

These need the running app, on mobile devices and the installed app, including with the app killed from the task switcher.

1. Edit a form, then kill the browser or app from the OS switcher and reopen it. Is the input recoverable? [running app]
2. With no edits, does navigating away trigger any warning? It shouldn't. [running app] [automated]
3. With unsaved edits, does in-app navigation show a specific, non-generic choice, or keep a draft? [running app]
4. Is the `beforeunload` handler attached only while the form is dirty, and removed after save? [automated] [running app]
5. Does a session timeout warn and allow extension, and does re-login restore the input? [running app]
6. Is save state ("Saving / Saved / Failed") visible and announced? [screenshot] [running app]
7. Do users trust autosave enough not to copy their text elsewhere as a backup? [user study]

## Related

- Principles: P-11, P-14, P-10, P-01
- Dimensions: D-07, D-09
- Gates: QG-062, QG-072, QG-029, QG-060
- Patterns: PAT-PW-004 (restoration), PAT-PW-003 (history), PAT-PW-007 (sync state), PAT-PW-012 (updates), PAT-SH-002 (forms), PAT-SH-011 (undo), PAT-SH-015 (dialogs), PAT-DT-006 (inline editing)

## Change log

- 2026-11-08 — Initial version (ADR-001).
