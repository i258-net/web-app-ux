---
id: PAT-PW-010
title: Platform capability differences — Safari/iOS, Firefox, Chromium, and feature detection
type: pattern
scope: pwa
topics: [compatibility, feature-detection, progressive-enhancement, ios, safari, firefox, chromium, storage-eviction, experimental-features]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-09, P-14, P-11, P-12]
dimensions: [D-10, D-09]
gates: [QG-090, QG-093, QG-042]
related: [PAT-PW-001, PAT-PW-002, PAT-PW-003, PAT-PW-005, PAT-PW-007, PAT-PW-009, PAT-MO-004]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Platform capability differences — Safari/iOS, Firefox, Chromium, and feature detection

## Problem

"PWA" isn't one platform. Installation, install prompts, push, badging, the Navigation API, keyboard geometry, and storage durability all differ between browser engines and operating systems, and the differences change from one release to the next. Teams build on Chromium desktop, then ship:

- Install buttons that do nothing on iOS.
- Push toggles that can't work in Safari tabs.
- Offline drafts that Safari evicts after a week of inactivity.
- Features that only work behind a browser flag.

Or they avoid a capability everywhere because of an outdated claim.

## Recommendation

**Outcome:** the core task works in every supported browser. Enhanced capabilities appear only where they actually work, and users are never shown an affordance their platform can't honor.

1. **Define a complete baseline**: ordinary links, forms, file inputs, and in-tab use. Then layer capabilities on top. Installing must never be the only route to a core task.
2. **Detect features, not browsers.** Gate each capability on its own API (`'BeforeInstallPromptEvent' in window` combined with the event actually firing, `'PushManager' in window`, `'navigation' in window`, `'setAppBadge' in navigator`) and on permission state. A user-agent string isn't evidence of a capability, and one API being present doesn't mean related ones are.
3. **Show platform-appropriate instructions** where a capability exists but has no API (iOS Add to Home Screen, macOS Safari Add to Dock), and say nothing where it doesn't exist.
4. **Assume local data can disappear.** Request persistent storage where it's useful, handle quota errors, sync valuable work to the server, and offer export. Don't promise that installation protects local data.
5. **Never require experimental features or flags for core tasks.** Origin trials expire and flags differ by user. Keep a fallback.
6. **Keep a dated compatibility register.** Record each capability your product depends on with its source and "as of" date, and **re-verify it before each major release**. The snapshot below is dated and will go stale.

### Compatibility snapshot (as of 2026-11-08; re-verify before relying on it)

All entries are from MDN pages and MDN browser-compat-data, as recorded in the research findings.

| Capability | Status as recorded |
|---|---|
| Manifest installation | Chromium on supported desktop OSes. **Desktop Firefox does not support manifest installation.** Safari 17+ on macOS Sonoma: Add to Dock, with or without a manifest. iOS 16.4+: Share menu in Safari, Chrome, Edge, Firefox, Orion. iOS ≤16.3: Safari only |
| `beforeinstallprompt` | Chrome supported. Firefox and Safari not supported. Not supported on iOS. Nonstandard |
| Push (`PushManager`) | iOS Safari 16.4+, **only in Home Screen web apps**. Desktop Safari 16+ on macOS Ventura+ |
| Badging API | Limited availability, not Baseline |
| Navigation API | Baseline 2026: Chrome 102, Firefox 147, Safari 26.2. Sub-features vary |
| VirtualKeyboard API | Chrome 94. No Firefox or Safari support. Experimental |
| `display_override` | Experimental |
| `prefers-reduced-data` | MDN says no user agent supports it. Chromium behind a flag |
| Storage | Best effort everywhere. Safari proactively evicts script-created data after seven days of browser use without user interaction when tracking prevention is on (server-set cookies exempt). No blanket exemption for installed iOS apps is established |

## Evidence

- **E3** MDN Web Docs, "Making PWAs installable". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable — Installation criteria and the per-platform install support above.
- **E3** MDN Web Docs, "Installing and uninstalling web apps". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Installing — Install and uninstall UI varies by browser and OS. Firefox extensions are a separate route.
- **E3** MDN browser-compat-data, "api/BeforeInstallPromptEvent.json". https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/BeforeInstallPromptEvent.json — Install-prompt support row.
- **E3** MDN browser-compat-data, "api/PushManager.json". https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/PushManager.json — iOS Home Screen restriction.
- **E3** MDN browser-compat-data, "api/Navigation.json". https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/Navigation.json — Navigation API versions.
- **E3** MDN browser-compat-data, "api/VirtualKeyboard.json". https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/VirtualKeyboard.json — VirtualKeyboard support.
- **E3** MDN Web Docs, "Badging API" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/API/Badging_API — "Limited availability."
- **E3** MDN Web Docs, "display_override". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display_override — Marked experimental.
- **E3** MDN Web Docs, "prefers-reduced-data". https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-data — Not supported by any user agent.
- **E3** MDN Web Docs, "Storage quotas and eviction criteria". https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria — Best-effort storage, quota failures, and Safari's proactive eviction rule.
- **E3** Google web.dev, "Experimental features". https://web.dev/learn/pwa/experimental — Flags and origin trials can change or disappear. Use progressive enhancement.
- **E3** Google web.dev, "Capabilities". https://web.dev/learn/pwa/capabilities — APIs can require feature detection, a secure context, permission, user activation, or installation, and are not interchangeable.
- **E3** Google web.dev, "Tools and debug". https://web.dev/learn/pwa/tools-and-debug — Tooling for manifests, workers, caches, and offline simulation. Tools don't replace testing on real devices.

Source disagreement: older web.dev course passages say Chrome and Edge on iOS can't install, and group push as Chromium-only. Current MDN contradicts both, and the snapshot follows MDN.

## Alternatives and tradeoffs

- **Supporting a narrower browser set** (for example, an enterprise app on managed Chromium) is legitimate if it's stated. Still keep the baseline usable elsewhere if links are shared outside.
- **Native wrapper or store app** for capabilities the web doesn't offer on a key platform. That trades web reach and URL-based behavior for capability.

## Exceptions and failure modes

- Embedded WebViews and in-app browsers often lack PWA features even on capable OSes, and none of the data above covers them. Test them separately.
- Failure modes:
  - User-agent sniffing.
  - Treating "Chromium-only" claims as permanent.
  - Showing every capability on every platform.
  - Assuming installed iOS apps are exempt from eviction.
  - A core flow that depends on an origin trial.
  - A compatibility table with no date.

## Evaluation questions

These need the running app on each target browser and OS: installed and in a tab, on real devices, with no offline simulator substituting.

1. Can the core task be completed in a tab on each supported browser, without installing? [running app]
2. Is any affordance shown that the current browser can't honor (install button, push toggle, badge setting)? [running app]
3. Is each capability gated by feature detection rather than the user-agent string? [automated] [running app]
4. With site data cleared, or after Safari's inactivity eviction, does the app recover and say what was lost? [running app]
5. Does the team keep a dated compatibility register, re-verified for this release? [automated]
6. Do any core paths depend on experimental or flagged features? [automated]

## Related

- Principles: P-09, P-14, P-11, P-12
- Dimensions: D-10, D-09
- Gates: QG-090, QG-093, QG-042
- Patterns: PAT-PW-002 (install paths), PAT-PW-009 (push), PAT-PW-003 (Navigation API), PAT-PW-001 (display modes), PAT-PW-005 (offline), PAT-PW-007 (background sync), PAT-MO-004 (virtual keyboards)

## Change log

- 2026-11-08 — Initial version (ADR-001).
