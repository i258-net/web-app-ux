---
id: PAT-PW-012
title: App updates — service worker versions, notifying users, and never reloading mid-task
type: pattern
scope: pwa
topics: [updates, service-worker, skipwaiting, reload, versioning, update-banner, multi-window, data-loss]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-10, P-11, P-14]
dimensions: [D-07, D-09]
gates: [QG-094, QG-062, QG-028]
related: [PAT-PW-008, PAT-PW-004, PAT-PW-006, PAT-PW-007, PAT-SH-009, PAT-DT-010]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# App updates — service worker versions, notifying users, and never reloading mid-task

## Problem

A web app with a service worker keeps running the old version after you deploy. The new worker installs and waits while old pages are open, and installed apps can stay open for days. Teams respond in one of two ways, and both cause trouble:

- **Do nothing.** Users stay on stale code that may no longer match the API.
- **Force it.** Call `skipWaiting()` and reload automatically, which wipes a half-written form, or mixes old pages with new assets and breaks them.

With several windows or tabs open, the problem multiplies.

## Recommendation

**Outcome:** users get new versions promptly. They're told when a reload is needed, choose when it happens (or it happens at a safe moment), and lose nothing.

1. **Detect updates without blocking.** Listen for `updatefound` and the new worker reaching `installed` while a controller exists. Check for updates on launch and on return to the foreground. Never hold up first paint for an update check.
2. **Tell the user, without interrupting.** Show a persistent, non-modal message such as "A new version is available · Reload", near the app's status area. It should stay until the user acts or dismisses it, not fade away (PAT-SH-009), and be announced as a status message (QG-028).
3. **Apply the update at a safe point.** When the user chooses Reload, message the waiting worker to activate (`skipWaiting` on request), then reload on `controllerchange`. If the user doesn't act, apply it on the next natural navigation or cold launch. Never reload silently in the middle of a task (QG-094).
4. **Save work before any reload.** Flush drafts and pending queue entries (PAT-PW-008, PAT-PW-007) before triggering it, and restore the route, scroll, and draft afterwards (PAT-PW-004). If unsaved state can't be saved, ask first.
5. **Keep versions coherent.** Version assets with content hashes, and keep the previous version's assets available long enough for pages still running it. Avoid automatic `skipWaiting()` unless old pages can't break against the new worker.
6. **Coordinate windows.** One worker controls every open window of the app. Show the prompt in every window, reload all windows together after each has saved its state, or tell the others that they will update.
7. **Reserve forced updates for real emergencies.** For security fixes or a breaking backend change, block further *writes* with an explanation and a one-tap reload, but keep the current content readable and copyable. Explain why.
8. **Say what changed when it matters.** A short "What's new" link is optional. Users should never have to read release notes to keep working.

## Evidence

- **E3** Google web.dev, "Update". https://web.dev/learn/pwa/update — An updated worker installs, then normally waits while the previous worker controls clients. `skipWaiting()` speeds up activation but risks pages loaded under one version running against a worker from another.
- **E4** Google web.dev, "Update" (same page, recommendation portion). https://web.dev/learn/pwa/update — Watch `updatefound` and worker state, tell users when a new version is ready, and offer an update action. Update checks need not block the initial interface.
- **E3** Google web.dev, "Service workers". https://web.dev/learn/pwa/service-workers — Installation and activation stages. The first page isn't controlled until a later navigation unless the worker claims it.
- **E4** Google web.dev, "Window management". https://web.dev/learn/pwa/windows — Installed apps can have several windows. Our inference: each can hold different unsaved state when an update affects all of them.
- **E3** MDN Web Docs, "Window: beforeunload event". https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event — Unload-time warnings are unreliable, so drafts must be saved before a reload rather than protected by a prompt during it.
- **E2** Nielsen Norman Group, "Indicators, Validations, and Notifications". https://www.nngroup.com/articles/indicators-validations-notifications/ — Brief transient messages get missed. Notifications that need action should persist.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — The update notice must be programmatically determinable without focus.
- **E1** W3C, "WCAG 2.2 — SC 3.2.2 On Input". https://www.w3.org/TR/WCAG22/#on-input — Changing a setting must not trigger an unannounced change of context. A silent reload is a broader instance of the same predictability problem (our interpretation; the SC itself is narrower).
- **E3** Google web.dev, "Tools and debug". https://web.dev/learn/pwa/tools-and-debug — Devtools for inspecting worker lifecycle. Test update and reload explicitly.

Interpretation (ours): applying updates on the next cold launch, and the emergency read-only mode, are synthesis. No source tests update-prompt designs with users.

## Alternatives and tradeoffs

- **Update silently on next launch only.** Least intrusive and fine for apps with short sessions. Long-lived installed windows may then stay stale for days.
- **Automatic `skipWaiting` with clients claimed.** Delivers fixes fastest. It's safe only when old pages can't break against the new worker and there is no unsaved state, for example a static content site.
- **Version handshake with the server.** The API returns the minimum client version it supports, and the client prompts when it falls below. This catches mismatches the worker lifecycle alone misses.

## Exceptions and failure modes

- Apps without a service worker still have long-lived single-page app sessions. A version check against the server serves the same purpose.
- Failure modes:
  - `location.reload()` on `controllerchange` triggered by a background update.
  - An update toast that disappears in 4 s.
  - A modal "Update now" with no "Later".
  - Old asset files deleted at deploy, so old pages fail to load chunks.
  - One window reloads while another keeps writing against the old schema.
  - A draft lost on the update reload.
  - An update check that delays startup.

## Evaluation questions

These need the running app, installed, with two windows open across a real deploy or a worker-update simulation in devtools.

1. After a deploy, does an open session learn about the new version without reloading? [running app]
2. Is the update notice persistent, non-modal, and announced? [running app] [automated]
3. With a half-filled form, does choosing Reload preserve the input and the route? [running app]
4. Does anything reload automatically while the user is mid-task? [running app]
5. With two windows open, do both end up on the same version without losing state? [running app]
6. Do pages still running the old version load their assets after a deploy? [running app] [automated]
7. Do users understand the notice and pick a convenient moment? [user study]

## Related

- Principles: P-10, P-11, P-14
- Dimensions: D-07, D-09
- Gates: QG-094, QG-062, QG-028
- Patterns: PAT-PW-008 (unsaved changes), PAT-PW-004 (restoration after reload), PAT-PW-006 (cached shell), PAT-PW-007 (pending queue), PAT-SH-009 (feedback), PAT-DT-010 (multi-window)

## Change log

- 2026-11-08 — Initial version (ADR-001).
