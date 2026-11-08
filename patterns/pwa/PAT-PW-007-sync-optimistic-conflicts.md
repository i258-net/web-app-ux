---
id: PAT-PW-007
title: Queued actions, background sync, optimistic updates, and conflicts
type: pattern
scope: pwa
topics: [sync, background-sync, offline-queue, optimistic-ui, conflicts, pending-state, multi-device, rollback]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-10, P-11, P-14, P-13]
dimensions: [D-07, D-09, D-10]
gates: [QG-072, QG-028, QG-025]
related: [PAT-PW-005, PAT-PW-006, PAT-PW-008, PAT-PW-010, PAT-SH-011, PAT-SH-016, PAT-DT-006]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Queued actions, background sync, optimistic updates, and conflicts

## Problem

To feel fast and to work offline, apps show changes before the server confirms them, and queue writes made offline. Done carelessly, this misleads users:

- **A green tick appears for a save that later fails silently.**
- **A message shows as "sent" but sits in an IndexedDB queue that the browser never flushes.**
- **Two devices edit the same record and the second overwrites the first without a word.**

Background sync is managed by the browser and isn't available everywhere, so "it will sync in the background" is a promise the app can't always keep.

## Recommendation

**Outcome:** users always know whether a change is confirmed, pending, or failed. Pending work survives reload and connectivity loss. Failures and conflicts are recoverable without retyping.

1. **Distinguish three states visibly, per item:**
   - **Pending.** "Sending…", "Saved on this device", a subdued style, or a clock icon with text.
   - **Confirmed.** The normal appearance, or a brief confirmation where it matters.
   - **Failed.** A persistent inline error with Retry and Edit, plus Discard where appropriate.

   Never style pending items the same as confirmed ones (PAT-SH-009).
2. **Use optimistic updates for reversible, low-risk actions** such as toggling, starring, reordering, or adding a comment. Apply the change at once. On failure, roll it back visibly, explain why, and offer a retry. Restore focus sensibly if an item reappears.
3. **Don't be optimistic about high-stakes or irreversible actions** (payments, sending to external parties, legal submissions). Wait for confirmation and show progress (QG-025).
4. **Persist the queue durably.** Store pending writes in IndexedDB, not in memory or in the service worker's globals. Each write gets an idempotency key so retries don't duplicate it.
5. **Flush the queue opportunistically.** Use Background Sync where it is available and feature-detected. Always also retry in the foreground: when the app opens, regains focus, or a request succeeds. Show a pending count and a manual "Sync now".
6. **Detect and surface conflicts.** Send a version or ETag with each write. When the server rejects a stale write:
   - Auto-merge only when the fields don't overlap.
   - Otherwise show both versions side by side ("Your change / Latest version") with Keep mine, Keep theirs, and, for text, a merge or copy option.
   - Never discard the user's version silently.
7. **Warn before leaving with unsynced work.** Signing out or clearing data with a non-empty queue needs an explicit warning, because storage is cleared and evicted (PAT-PW-010).
8. **Make sync state visible across windows and devices.** Other open tabs reflect pending and confirmed state, and a change made on one device appears on another, or is marked as pending there.
9. **Announce outcomes accessibly.** Failures and conflicts are status messages (QG-028). Failures persist until resolved. Don't rely on toasts alone.

## Evidence

- **E3** MDN Web Docs, "Offline and background operation". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation — Browsers stop workers between events. Background sync execution and retries are managed and limited by the browser.
- **E3** Google web.dev, "Service workers". https://web.dev/learn/pwa/service-workers — Service workers are event-driven and have a lifecycle, so state must not live only in worker memory.
- **E4** Google web.dev, "Offline data". https://web.dev/learn/pwa/offline-data — Handle offline changes appropriately. IndexedDB holds structured data used by pages and workers.
- **E3** React, "useOptimistic". https://react.dev/reference/react/useOptimistic — Show an optimistic value while an action is pending. The example restores a deleted item and shows an error if the deletion fails.
- **E2** Nielsen Norman Group, "Consistency in the Omnichannel Experience". https://www.nngroup.com/articles/omnichannel-consistency/ — Users expect changes to appear across channels and were frustrated when they didn't.
- **E3** Microsoft, "Settings Sync" (VS Code docs). https://code.visualstudio.com/docs/configure/settings-sync.md — Explicit local/remote conflict resolution, and exclusion of device-specific settings.
- **E4** Nielsen Norman Group, "Visibility of System Status". https://www.nngroup.com/articles/visibility-system-status/ — Distinguish acknowledgement from completion. Make background changes visible.
- **E3** MDN Web Docs, "Storage quotas and eviction criteria". https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria — Local storage is best effort and writes can fail.
- **E1** W3C, "WCAG 2.2 — SC 3.3.4 Error Prevention (Legal, Financial, Data)". https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data — Such submissions must be reversible, checked, or confirmed.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Results must be programmatically determinable without focus.

Interpretation (ours): idempotency keys, ETags, and side-by-side conflict UI are our inference. No fetched source tests conflict UIs with users.

## Alternatives and tradeoffs

- **Last-write-wins.** Simple, and acceptable for low-value single-field preferences. It silently loses data in collaborative or long-form content.
- **Field-level merge or CRDTs.** These reduce visible conflicts for collaborative text, but at significant engineering cost. Users still need to see when merged results differ from what they wrote.
- **Pessimistic UI.** Wait for the server on every action. Slower, but honest. Right for high-stakes actions and acceptable when latency is consistently low (PAT-SH-010).
- **Disabling writes offline** avoids conflicts entirely but blocks work.

## Exceptions and failure modes

- Actions that depend on the server's real-time state (seat booking, inventory reservation) can't be queued meaningfully. Explain that they need a connection.
- Failure modes:
  - "Saved" shown on local write only.
  - A queue held in memory and lost on reload.
  - Retries that create duplicates.
  - Rollbacks with no explanation, so the item just vanishes.
  - Conflict dialogs offering only "Overwrite".
  - Background Sync assumed to exist without feature detection, which strands the queue wherever it is missing. The findings don't establish a cross-browser support matrix, so check current data (PAT-PW-010).
  - A pending badge in one tab while another tab shows the item as confirmed.

## Evaluation questions

These need the running app, offline toggling, and a second device or tab.

1. Make a change offline. Is it marked as pending in words, and still pending after reload? [running app]
2. Reconnect. Does the queue flush in the foreground without Background Sync, and is it confirmed exactly once? [running app]
3. Force a server failure. Is the optimistic change rolled back with an explanation and a retry? [running app]
4. Edit the same record on two devices. Is the conflict surfaced with both versions? [running app]
5. Sign out with pending changes. Is the user warned? [running app]
6. Are failures and conflicts announced and persistent for screen-reader users? [running app] [automated]
7. Do users correctly interpret pending vs confirmed states? [user study]

## Related

- Principles: P-10, P-11, P-14, P-13
- Dimensions: D-07, D-09, D-10
- Gates: QG-072, QG-028, QG-025
- Patterns: PAT-PW-005 (offline), PAT-PW-006 (caching), PAT-PW-008 (drafts), PAT-PW-010 (capability differences), PAT-SH-011 (destructive actions and undo), PAT-SH-016 (failure recovery), PAT-DT-006 (inline editing)

## Change log

- 2026-11-08 — Initial version (ADR-001).
