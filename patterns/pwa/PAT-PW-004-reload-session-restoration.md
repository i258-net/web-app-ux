---
id: PAT-PW-004
title: Reload, back/forward cache, and restoring in-progress state
type: pattern
scope: pwa
topics: [reload, bfcache, scroll-restoration, session-restoration, state-persistence, interruption, pageshow, visibilitychange]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-11, P-04, P-13, P-01]
dimensions: [D-07, D-09, D-02]
gates: [QG-061, QG-062, QG-063, QG-072]
related: [PAT-PW-003, PAT-PW-006, PAT-PW-008, PAT-PW-012, PAT-SH-007, PAT-DT-010]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Reload, back/forward cache, and restoring in-progress state

## Problem

Web pages are reloaded, restored from the back/forward cache, discarded in the background by mobile operating systems, and reopened hours later. Users expect to come back to where they were: the same record, the same scroll position in a long list, and the half-written form still filled in. Apps that keep everything in memory lose it all on reload. Apps that set `scrollRestoration` to `manual` and forget to restore it send users to the top of a 300-item list. Apps restored from bfcache can briefly show stale or signed-out data as if it were current.

## Recommendation

**Outcome:** after reload, Back/Forward, a background discard, or a later return, users see the same place with their unfinished work intact. Anything that may have changed is refreshed or labeled.

1. **Put location in the URL.** Route, record, tab, and filters live in the URL, so reload and direct arrival restore the view (QG-061, PAT-PW-003).
2. **Save in-progress input continuously, not just at exit.** Persist drafts to IndexedDB, or to the server for valuable work, as users type or on `visibilitychange` to hidden. That event is more reliable than unload events, especially on mobile. Restore drafts on reload and say that you did ("Draft restored · Discard"). See PAT-PW-008.
3. **Restore list position on Back** (QG-063). Keep `history.scrollRestoration = "auto"` unless your router needs manual control. If you switch to `manual`, restore position yourself once the content has rendered. Paginated and infinite lists need the item anchor or the page as well (PAT-SH-007).
4. **Design for bfcache restoration.** Avoid `unload` handlers, which can keep a page out of bfcache. On `pageshow` with `event.persisted`, the page is a snapshot. Leave it usable right away, then re-check session and refresh time-sensitive data, labeling it if it can't be refreshed (PAT-PW-006).
5. **Rebuild from durable state.** Any ephemeral state you choose to restore, such as an open panel, a selected row, or a wizard step, comes from the URL or storage, not from objects in memory or the service worker.
6. **Fail safely when storage is gone.** Storage can be cleared, evicted, or full. Handle failed writes, rebuild without crashing, and never imply that a local draft is a permanent backup.
7. **Keep restored sessions accessible.** After restoring, place focus deliberately and announce restored drafts through a status message, without moving focus to it.

## Evidence

- **E3** Google web.dev, "Back/forward cache". https://web.dev/articles/bfcache — bfcache keeps a whole-page snapshot (DOM and JavaScript heap), separate from HTTP and service-worker caches, and is not guaranteed. `pageshow` with `persisted` signals restoration. Recommends avoiding `unload` handlers.
- **E3** MDN Web Docs, "History: scrollRestoration property". https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration — `auto` lets the browser restore scroll on traversal. `manual` disables that.
- **E3** MDN Web Docs, "Window: beforeunload event". https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event — Unload-time events may not fire, especially when a mobile app is killed. `visibilitychange` is the more reliable signal for saving state.
- **E3** Google web.dev, "Offline data". https://web.dev/learn/pwa/offline-data — IndexedDB suits structured data such as drafts. Web Storage is synchronous.
- **E3** MDN Web Docs, "Storage quotas and eviction criteria". https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria — Storage is best effort. Writes can fail on quota, and users can delete data. Safari can evict script-created data (rule details in PAT-PW-010).
- **E2** Nielsen Norman Group, "Mobile User Experience: Limitations and Strengths". https://www.nngroup.com/articles/mobile-ux/ — Mobile use is fragmented and interrupted, so save state and context and let users resume without redoing work. The research dates from 2015.
- **E2** Nielsen Norman Group, "Seamlessness in the Omnichannel User Experience". https://www.nngroup.com/articles/seamless-cross-channel/ — Handoff should minimize overhead when users switch context.
- **E3** Android Developers, "App orientation, aspect ratio, and resizability". https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability — Preserve state, including form input, across configuration and window changes. This is native guidance; we infer the principle carries over to web resizing and reload.
- **E3** MDN Web Docs, "History API". https://developer.mozilla.org/en-US/docs/Web/API/History_API — Restore app state from history entries on traversal.

## Alternatives and tradeoffs

- **Server-side drafts vs local drafts.** Server drafts survive device changes and eviction but need connectivity and raise privacy questions for sensitive fields. Local drafts are immediate but not durable. Valuable, long-form work merits both.
- **Restore silently vs ask.** Silent restoration is smooth when the user clearly left moments ago. For old drafts, or drafts that conflict with newer server data, offer "Restore draft / Discard" instead (PAT-PW-007).
- **Refreshing a bfcache-restored page.** Re-fetching everything on `pageshow` throws away the speed of bfcache. Re-fetching nothing risks showing stale data. Refresh only what is time-sensitive or tied to the session.

## Exceptions and failure modes

- Don't persist sensitive inputs (passwords, payment card numbers, one-time codes) to client storage. Restore the form without those fields and say so.
- On shared devices, restored drafts may expose data to the next user. Clear them on sign-out.
- Failure modes:
  - The draft is saved only in `beforeunload`.
  - A restored page shows a signed-out user's data after logout in another tab.
  - Scroll resets to the top on Back.
  - A "Draft restored" toast that disappears before a screen-reader user hears it.
  - Restoring a wizard to step 3 with step 2's answers missing.

## Evaluation questions

Most of these need the running app. Test reload, Back, and a forced background discard on real mobile devices.

1. Fill half a form, then reload. Is the input still there, and is that communicated? [running app]
2. Scroll deep into a list, open an item, then press Back. Is the position and the loaded content restored? [running app]
3. Switch to another app on a phone for a long time, then return. Is the task intact? [running app]
4. After Back from another site (bfcache), is session-dependent data re-checked? [running app]
5. Is `history.scrollRestoration` `manual`, and if so is scroll restored by the app? [automated] [running app]
6. With storage cleared or full, does the app recover without crashing or data-loss surprises? [running app]
7. Is restored-draft feedback announced to assistive technology? [running app] [automated]

## Related

- Principles: P-11, P-04, P-13, P-01
- Dimensions: D-07, D-09, D-02
- Gates: QG-061, QG-062, QG-063, QG-072
- Patterns: PAT-PW-003 (history), PAT-PW-008 (unsaved changes), PAT-PW-006 (freshness), PAT-PW-012 (updates and reload), PAT-SH-007 (list position), PAT-DT-010 (multi-window)

## Change log

- 2026-11-08 — Initial version (ADR-001).
