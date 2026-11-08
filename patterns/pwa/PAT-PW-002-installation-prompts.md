---
id: PAT-PW-002
title: Installation prompts — criteria, timing, and platform-specific install paths
type: pattern
scope: pwa
topics: [pwa, install, beforeinstallprompt, add-to-home-screen, ios, manifest, onboarding, promotion]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-14, P-02, P-01, P-09]
dimensions: [D-09, D-10]
gates: [QG-090, QG-091]
related: [PAT-PW-001, PAT-PW-009, PAT-PW-010, PAT-PW-005, PAT-SH-013]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Installation prompts — criteria, timing, and platform-specific install paths

## Problem

Teams want people to install the app, so they show an "Install app" banner the moment the page loads. It interrupts the first task, often on a browser that can't act on it. iOS has no programmatic install prompt, and desktop Firefox doesn't install from a manifest. A button that calls `prompt()` either does nothing or throws. Other teams make the opposite mistake and treat "installable" as meaning "works offline", or never explain what installing gets the user.

## Recommendation

**Outcome:** users who would benefit learn they can install at a moment that makes sense to them, through a path that works in their current browser. Nobody is blocked or nagged.

1. **Meet the browser criteria, but don't treat them as the goal.** Serve over HTTPS and provide a complete manifest. Chromium promotion needs `name` or `short_name`, 192 px and 512 px icons, `start_url`, `display` and/or `display_override`, and `prefer_related_applications` false or absent (QG-090). Installability does not mean offline readiness: test offline behavior separately (PAT-PW-005).
2. **Never prompt on first load** (QG-091). Invite installation after the user has seen value: a completed task, a return visit, or turning on a feature that needs installation (for example push on iOS, see PAT-PW-009). Keep the invitation outside the primary task flow. A dismissible banner, a menu item, or a settings entry is fine; a modal over the task is not.
3. **Gate the custom button on the event.** Show an actionable "Install" control only after `beforeinstallprompt` has fired and you have kept the event. Call `prompt()` from a user action. The event can be used **once**, so clear it and hide the control afterwards.
4. **Give platform-specific instructions where there is no event.** On iOS, explain the Share-menu "Add to Home Screen" path in context. Don't show a button that implies one tap will install. On desktop Safari, the equivalent is Add to Dock. Where manifest installation isn't supported (desktop Firefox), don't promote it at all.
5. **Say what installing gets them**, in their terms: launch from the home screen or dock, a separate window, notifications where that's true. Don't promise offline use unless it has been built and tested.
6. **Remember dismissal for a long time** and don't re-prompt on every visit. Keep a permanent, low-key entry point (a menu or settings item) for users who change their mind.
7. **Keep the browser experience complete.** Installing is an enhancement. No task should require it, except platform-gated capabilities, and those must be explained.

## Evidence

- **E3** MDN Web Docs, "Making PWAs installable". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable — Lists HTTPS or localhost and the Chromium manifest criteria. States that a service worker is **not** required for installability. As of 2026-11-08: iOS 16.4+ supports installation from Safari, Chrome, Edge, Firefox, and Orion via the Share menu; `beforeinstallprompt` is not supported on iOS; desktop Firefox does not support manifest installation; Safari 17+ on macOS Sonoma supports Add to Dock.
- **E3** MDN Web Docs, "Installing and uninstalling web apps". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Installing — Install and uninstall UI differs across browser/OS combinations.
- **E3** MDN Web Docs, "BeforeInstallPromptEvent". https://developer.mozilla.org/en-US/docs/Web/API/BeforeInstallPromptEvent — Nonstandard. The event can be kept after `preventDefault()` and used to call `prompt()` once.
- **E3** MDN browser-compat-data, "api/BeforeInstallPromptEvent.json". https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/BeforeInstallPromptEvent.json — As of 2026-11-08: Chrome supported; Firefox and Safari not supported.
- **E3** Google web.dev, "Installation prompt". https://web.dev/learn/pwa/installation-prompt — The deferred-prompt lifecycle. Its iOS compatibility statements are older than MDN's and are not used here.
- **E4** Google web.dev, "Patterns for promoting PWA installation". https://web.dev/articles/promote-install — Promotions should be dismissible and non-disruptive, wait for signs of interest, remember dismissal, and stay out of primary task flows. Prompting on page load can overwhelm users or be missed. No conversion study is described.
- **E3** Apple, "Onboarding" (HIG). https://developer.apple.com/design/human-interface-guidelines/onboarding.md — Postpone nonessential setup and ask when it's relevant to the feature. Native Apple guidance; we apply it to install invitations by analogy.

## Alternatives and tradeoffs

- **No custom promotion.** Leave installation to the browser's own UI. This is the least intrusive option and right for occasional-use sites. Users who would benefit may never find it.
- **Contextual promotion vs a settings entry.** A contextual invitation after a success converts better in principle, but no fetched source measures this (E4 reasoning). A settings entry is always available but rarely seen. Use both.
- **Promoting install to unlock a capability.** On iOS, web push requires a Home Screen app, so an install invitation can legitimately sit inside the "turn on notifications" flow (PAT-PW-009). Explain both steps.
- **Installability versus offline.** QG-090 follows MDN: a service worker is not required for installability; offline behavior is gated separately (QG-093) and only for products that claim it. QG-090's manifest list is illustrative; the authoritative checklist is each target browser's criteria (MDN, Making PWAs installable), including Chromium's `prefer_related_applications` and icon-size conditions and permitted development origins.

## Exceptions and failure modes

- Kiosk, enterprise-managed, or store-distributed deployments may install through other channels. Promotion is then unnecessary.
- Failure modes:
  - An install button visible on browsers that never fire the event.
  - A button that stays enabled after the event has been used.
  - A banner that covers the primary action on compact viewports.
  - Re-prompting on every session.
  - Calling the app "offline-ready" without testing it offline.
  - Hiding the prompt by testing `display-mode` and assuming that tells you whether the app is installed (PAT-PW-001).
  - iOS instructions that name the wrong browser path.

## Evaluation questions

1. Does any install promotion appear on first load, before the user has done anything? [running app] [screenshot]
2. On a Chromium browser, does the custom install control appear only after `beforeinstallprompt`, and disappear after use? [running app] [automated]
3. On iOS Safari and desktop Firefox, is the user shown an action that can't work? [running app]
4. Can the promotion be dismissed, and is the dismissal remembered across sessions? [running app]
5. Does the invitation say what installing gives the user, accurately? [screenshot]
6. Does the manifest meet the criteria for each target browser? [automated]
7. After installing, does the app do what the invitation promised (offline, notifications)? [running app]
8. Do users who see the invitation understand it and not feel interrupted? [user study]

## Related

- Principles: P-14, P-02, P-01, P-09
- Dimensions: D-09, D-10
- Gates: QG-090, QG-091
- Patterns: PAT-PW-001 (display modes), PAT-PW-009 (notifications), PAT-PW-010 (platform differences), PAT-PW-005 (offline), PAT-SH-013 (onboarding)

## Change log

- 2026-11-08 — Initial version (ADR-001).
