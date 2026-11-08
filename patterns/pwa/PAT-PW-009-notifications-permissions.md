---
id: PAT-PW-009
title: Notifications and permissions — timing, pre-prompts, badging, and respecting denial
type: pattern
scope: pwa
topics: [notifications, push, permissions, pre-prompt, badging, ios, user-activation, consent]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-14, P-10, P-02]
dimensions: [D-09, D-07]
gates: [QG-095, QG-091]
related: [PAT-PW-002, PAT-PW-010, PAT-PW-001, PAT-SH-013, PAT-SH-009, PAT-SH-015]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Notifications and permissions — timing, pre-prompts, badging, and respecting denial

## Problem

Permission prompts that appear on arrival ask for something before the user knows what it's for. Many people block them, and a blocked site can't ask again. Teams then lose a channel they actually needed, for order updates or replies. Other failures:

- Promising push on iOS in a browser tab, where it isn't available.
- Making the app icon badge the only place an important event appears.
- Pestering users who said no.

## Recommendation

**Outcome:** users are asked for permission at a moment when the benefit is obvious and in response to their own action. Saying no costs them nothing essential, and the app respects the choice.

1. **Ask after a user action that implies intent** (QG-095). Examples: "Notify me when my order ships" after checkout, a bell toggle on a conversation, or a settings switch. Call `Notification.requestPermission()` from that gesture. Never ask on page load or first visit, the same rule as install prompts (QG-091).
2. **Use an in-page pre-prompt for broad permissions.** Explain the concrete value and frequency in your own UI ("We'll notify you about replies and delivery updates — no marketing"), with "Turn on" and "Not now". Show the browser prompt only after "Turn on". If the user picks "Not now", respect it and don't show the browser prompt, so the site isn't blocked permanently.
3. **Branch on permission state.**
   - `default`: offer the opt-in in context.
   - `granted`: show notification controls and an easy way to turn them off.
   - `denied`: don't ask again. Show the setting as off, with a short explanation of how to re-enable it in browser or OS settings if the user wants to.
4. **Make notifications controllable in the app.** Offer per-category toggles, frequency, and an off switch. Users who can't find "off" in the app block at the browser level.
5. **Handle platform gating honestly.** On iOS, web push works only for a web app added to the Home Screen. In a Safari tab, explain that step instead of showing a toggle that can't work, and connect it to the install path (PAT-PW-002). Feature-detect `PushManager` and `Notification`. On mobile, show notifications through the service worker registration, not the `Notification()` constructor.
6. **Treat badges as supplementary.** The Badging API (`setAppBadge`, `clearAppBadge`) can mark unread or pending activity on an installed app's icon. It is best effort: a platform may show a dot instead of a number. Clear stale badges when content is read. Every badged event must also be visible inside the app.
7. **Keep in-app status as the source of truth.** Notifications and badges are reminders. The app's own inbox, activity list, and status UI must show everything important, persistently (PAT-SH-009).
8. **Apply the same rules to other permissions** (location, camera, files). Request at the moment of use, explain why, and offer a non-permission fallback such as typing an address or using a file picker.

## Evidence

- **E3** MDN Web Docs, "Using the Notifications API" (modified 2026-09-02; verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API — Request permission only in response to a user gesture, and browsers are moving to disallow anything else (Firefox from version 72, and Safari). Chrome and Firefox require a secure context. Documents the `default`/`granted`/`denied` states. The `Notification()` constructor throws on most mobile browsers, so use `ServiceWorkerRegistration.showNotification()`.
- **E4** Google web.dev, page at `/articles/push-notifications-permissions-ux` (title not captured; author Matt Gaunt; verified 2026-11-08). https://web.dev/articles/push-notifications-permissions-ux — Ask when the benefit is obvious. Asking on arrival is "the worst thing you can do". Describes the double-permission (pre-prompt) pattern, and says that "if the user blocks the permission request, your web app can't ask for permission again." Recommends explaining how to turn push off. Gives no quantitative data.
- **E3** MDN browser-compat-data, "api/PushManager.json". https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/PushManager.json — As of 2026-11-08: Safari on iOS supports push from 16.4, with notifications only in web apps saved to the Home Screen. Desktop Safari from 16 on macOS Ventura or later.
- **E3** MDN Web Docs, "Badging API" (modified 2024-07-25; verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/API/Badging_API — `setAppBadge()` is for installed apps. Secure context. User agents may show a marker instead of a number. As of 2026-11-08 it is "Limited availability … not Baseline".
- **E3** Google web.dev, "Enhancements". https://web.dev/learn/pwa/enhancements — Badges indicate unread or pending activity, subject to platform integration. The "Update" module (https://web.dev/learn/pwa/update) calls badging best effort.
- **E3** Google web.dev, "Capabilities". https://web.dev/learn/pwa/capabilities — Capabilities may need permissions or user activation. A passed feature check doesn't mean permission has been granted.
- **E3** Apple, "Onboarding" (HIG). https://developer.apple.com/design/human-interface-guidelines/onboarding.md — Ask for permissions when relevant to the feature (native).
- **E2** Nielsen Norman Group, "Indicators, Validations, and Notifications". https://www.nngroup.com/articles/indicators-validations-notifications/ — Choose the communication method by urgency. Transient messages get missed.

## Alternatives and tradeoffs

- **Passive opt-in only** (a settings or footer toggle). Least intrusive; suits content sites. Fewer opt-ins.
- **Pre-prompt vs direct prompt.** A pre-prompt adds a step but protects against reflexive blocks. A direct prompt from a clearly labeled "Enable notifications" button is acceptable.
- **Email or SMS fallbacks** reach users without push, with separate consent.

## Exceptions and failure modes

- Messaging and calling apps may ask early, since notifications are core, but still after the user understands the product.
- Failure modes:
  - A prompt on load.
  - A pre-prompt whose "Not now" triggers the browser prompt anyway.
  - Repeated pre-prompts every session.
  - A push toggle in iOS Safari that does nothing.
  - Badge counts that never clear.
  - Events available only as push.
  - Marketing sent on a permission granted for transactional updates.

## Evaluation questions

Test in the running app on each target platform, including iOS in a tab and installed.

1. Does any permission prompt appear before the user acts? [running app] [screenshot]
2. Is the browser prompt triggered from a user gesture after an explanation of value? [running app]
3. After "Not now" or a browser denial, does the app stop asking, and does it show how to re-enable? [running app]
4. In iOS Safari (not installed), what does the app offer for notifications? [running app]
5. Are notification categories and an off switch available in the app? [screenshot] [running app]
6. Is every badged or pushed event also visible in the app, and do badges clear when read? [running app]
7. Do users understand what they agreed to receive? [user study]

## Related

- Principles: P-14, P-10, P-02
- Dimensions: D-09, D-07
- Gates: QG-095, QG-091
- Patterns: PAT-PW-002 (install), PAT-PW-010 (platform differences), PAT-PW-001 (installed mode), PAT-SH-013 (onboarding and permission sequencing), PAT-SH-009 (feedback), PAT-SH-015 (dialogs)

## Change log

- 2026-11-08 — Initial version (ADR-001).
