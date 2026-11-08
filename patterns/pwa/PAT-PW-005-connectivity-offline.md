---
id: PAT-PW-005
title: Connectivity and offline — detecting, communicating, and degrading gracefully
type: pattern
scope: pwa
topics: [offline, connectivity, network-failure, navigator-online, offline-page, service-worker, status-messages, graceful-degradation]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-10, P-11, P-13, P-14]
dimensions: [D-07, D-09]
gates: [QG-071, QG-093, QG-072, QG-028]
related: [PAT-PW-006, PAT-PW-007, PAT-PW-010, PAT-SH-016, PAT-SH-009, PAT-SH-010]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Connectivity and offline — detecting, communicating, and degrading gracefully

## Problem

People use web apps on trains, in lifts, on congested Wi-Fi, and behind captive portals. Connectivity is often neither fully on nor fully off. Apps fail in three typical ways:

- **They show the browser's generic error page or a blank screen.**
- **They spin forever on a request that will never finish.**
- **They treat `navigator.onLine` as the truth.** This disables features while the network actually works, or claims to be online on a LAN with no internet access.

An installed icon also implies the app will open.

## Recommendation

**Outcome:** with poor or no connectivity, users can tell what still works, what doesn't, and what happened to their action. They never lose input and never see a raw error.

1. **Decide offline scope per view.** List the views that must open offline (QG-093: previously visited core views load) and the actions that need the network. A service worker shell plus cached data for those views is the baseline. Installation alone does not make an app work offline.
2. **Serve a custom offline response** for uncached navigations, not the browser error page. It should name the app, explain the state, offer a retry, and link to cached content.
3. **Treat request failure as the real signal.** Use `online`/`offline` events and `navigator.onLine` only as hints, for example to show a "You seem to be offline" banner. Don't disable features because of them. A failed or timed-out request is what triggers the error state (QG-071).
4. **Communicate state persistently and near the work.**
   - Use a non-modal banner or status bar for connectivity.
   - Show per-item states for content and actions ("Saved on this device · will sync", "Couldn't load — Retry").
   - Don't rely on a fading toast for failures (PAT-SH-009).
   - Expose status changes as WCAG 4.1.3 status messages (QG-028), and keep them short and infrequent so they don't chatter.
5. **Bound waiting.** Set timeouts for network requests. Show progress for anything past about 1 s (PAT-SH-010). After a timeout, switch to cached content with a label, or to a retry state. Never spin indefinitely.
6. **Preserve input on failure** (QG-072). Keep the form filled. Either queue the action and say so (PAT-PW-007), or offer Retry. Don't make users type it again.
7. **Disable network-only actions honestly.** Where an action can't work offline (payment, live search), keep the control visible with an explanation and a "try when online" path, instead of hiding it silently.
8. **Recover automatically and quietly.** When requests succeed again, clear the offline banner, sync pending work (PAT-PW-007), and refresh stale views (PAT-PW-006).

## Evidence

- **E3** MDN Web Docs, "Navigator: onLine property" (last modified 2025-02-15; verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/API/Navigator/onLine — `online`/`offline` events fire when the value changes. A LAN without internet access can count as online. MDN calls the property "inherently unreliable" and advises not to disable features based on it, only to "provide hints when the user may seem offline".
- **E3** MDN Web Docs, "Making PWAs installable". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable — A service worker is not required for installability, so installing does not establish offline function.
- **E4** Google web.dev, "Offline data". https://web.dev/learn/pwa/offline-data — Recommends offline experiences with locally useful content.
- **E4** MDN Web Docs, "Best practices for PWAs". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Best_practices — A custom offline experience instead of a generic browser error. Test offline behavior.
- **E3** Google web.dev, "Serving". https://web.dev/learn/pwa/serving — A worker can return network, cached, or generated responses. Fetch-handler bugs can stop the app document from loading at all.
- **E3** MDN Web Docs, "Offline and background operation". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation — Browsers stop workers between events and limit background work.
- **E2** Nielsen Norman Group, "Indicators, Validations, and Notifications". https://www.nngroup.com/articles/indicators-validations-notifications/ — A mobile participant missed a brief error message and waited for content that never loaded. Fading toasts are a poor way to show errors.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Status messages must be programmatically determinable without receiving focus.
- **E4** Nielsen Norman Group, "Response Times: The 3 Important Limits". https://www.nngroup.com/articles/response-times-3-important-limits/ — Show feedback beyond about 1 s, and progress plus a way out beyond about 10 s.

Interpretation (ours): treating request failure as the signal is our synthesis. No source specifies timeout values.

## Alternatives and tradeoffs

- **Offline-first vs online-with-fallback.** Offline-first, meaning local data is primary and syncs later, suits field work, notes, and lists. It costs sync and conflict design (PAT-PW-007). Online-with-fallback, where a cached read-only view plus an offline page is the baseline, is enough for most transactional apps.
- **Global banner vs per-item status.** A banner is clear but generic. Per-item states are precise but busy. Use both.
- **Auto-retry vs manual retry.** Automatic retry with backoff suits idempotent reads. Writes need explicit status, and must not be retried silently if they aren't idempotent.

## Exceptions and failure modes

- Real-time or regulated tasks (trading, live auctions, medical orders) may legitimately refuse to work offline. Say so clearly instead of pretending they degrade.
- Failure modes:
  - The offline page is cached but its CSS or fonts aren't.
  - A banner says "offline" while requests are succeeding.
  - Submit buttons are disabled when `onLine` is false behind a VPN.
  - A spinner never ends.
  - Pending work is lost on reload.
  - Status announced on every retry attempt.
  - An offline page with no way back to cached views.

## Evaluation questions

These need the running app with network throttling and offline simulation, and ideally an installed app on a device.

1. In airplane mode, does the installed app open, and which views load? [running app]
2. Opening an uncached route offline, does a custom offline response with a way forward appear? [running app]
3. Under "slow 3G" throttling, does any request spin without a timeout or a message? [running app]
4. Submit a form offline. Is the input preserved, and is the outcome (queued, failed, retry) stated? [running app]
5. On a network that has connectivity but no internet (captive portal), does the app give accurate status? [running app]
6. Are connectivity changes announced to screen readers once, without stealing focus? [running app] [automated]
7. Do users understand what works offline? [user study]

## Related

- Principles: P-10, P-11, P-13, P-14
- Dimensions: D-07, D-09
- Gates: QG-071, QG-093, QG-072, QG-028
- Patterns: PAT-SH-016 (failure recovery), PAT-SH-009 (feedback), PAT-SH-010 (loading), PAT-PW-006 (caching and freshness), PAT-PW-007 (sync and queued actions), PAT-PW-010 (platform differences)

## Change log

- 2026-11-08 — Initial version (ADR-001).
