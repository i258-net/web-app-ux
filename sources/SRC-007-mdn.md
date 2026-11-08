---
id: SRC-007
title: MDN Web Docs and MDN browser-compat-data
type: source
publisher: MDN Web Docs contributors (Mozilla); MDN browser-compat-data contributors
evidence_classes: [E3, E4]
status: active
updated: 2026-11-08
---

# SRC-007 MDN Web Docs and browser-compat-data

## Publisher and scope

MDN Web Docs is the community-maintained reference for web technologies, stewarded by Mozilla. Research used:

- the MDN PWA guides: what a PWA is, making PWAs installable, installing and uninstalling, offline and background operation, caching, and best practices
- the Web App Manifest reference: `display`, `display_override`, `start_url`, `scope`, and `shortcuts`
- API references: History, Navigation, `beforeunload`, `scrollRestoration`, View Transitions, PushManager, VirtualKeyboard, `BeforeInstallPromptEvent`, and storage quotas
- CSS references: container queries, `env()`, viewport segments, `touch-action`, `overscroll-behavior`, scroll snap, `:focus-visible`, and the reduced-motion and reduced-data media features
- HTML references: `inputmode`, `enterkeyhint`, `autocomplete`, the viewport `<meta>` tag, and `<a>`

The MDN compatibility tables did not render in the fetched HTML. For five features, research therefore fetched the underlying **MDN browser-compat-data (BCD) JSON** from GitHub: `BeforeInstallPromptEvent`, Navigation, PushManager, VirtualKeyboard, and the CSS `@media` features.

MDN's strengths are precise API semantics, dated pages ("last modified"), and the most reliable public source for **current browser support**.

## How to classify their material

| Output | Class | Why |
|---|---|---|
| Reference pages that describe API, attribute, or property behavior | **E3** | Platform documentation. It is not normative: the specification (SRC-001) is the E1 source, and MDN explains it |
| Compatibility statements in MDN text or BCD JSON | **E3, dated snapshot** | Accurate only as of the access date (2026-11-08). Re-check before relying on one |
| "Best practices" guides | **E4** for design advice, **E3** for platform facts | The PWA best-practices guide mixes both |

If a finding is classed E1 because it co-cites a specification, the MDN page in that finding is recorded here as **E3**. This applies to F-WP-45 and F-WP-58.

A support entry for a top-level API does not establish support for every sub-feature, embedded WebView, enterprise configuration, or older browser.

## Licensing and access

MDN prose is licensed CC BY-SA 2.5 and code samples CC0. BCD data is CC0. Attribute MDN and paraphrase it. If you quote substantial text, the share-alike terms apply. Nothing here is paywalled.

## Known limitations and biases

- **Compatibility goes stale fast.** Every support claim in the knowledge base needs an "as of" date and a re-check during refresh (see governance).
- **MDN can contradict itself.** The `start_url` Description constrains the URL to the origin of the installing page, while Best practices refers to the manifest's origin. F-WP-45 follows the normative manifest algorithm instead (WP disagreements).
- **Reduced data.** MDN does not establish dependable default-on support for `prefers-reduced-data` (F-WP-24). The semantics are specified but not reliably implemented.
- **Volunteer authorship.** Coverage depth varies between pages. Some PWA guides blend opinion with facts.
- **Outdated paths.** Principle P-07 cites older MDN paths (`/Web/HTML/Attributes/autocomplete` and `/Web/HTML/Global_attributes/inputmode`). The findings cite the current `/Web/HTML/Reference/…` paths. Prefer the current ones.

## Cited pages

All rows were accessed 2026-11-08. MDN dates are the "last modified" dates shown on each page. BCD JSON files show no date.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| `<a>`: The Anchor element | <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a> | 2026-10-28 | 2026-11-08 | E3 | F-DX-41 |
| CSS container queries - CSS \| MDN | <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries> | 2026-07-08 | 2026-11-08 | E3 | F-WP-04 |
| prefers-reduced-motion CSS media feature - CSS \| MDN | <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion> | 2026-06-10 | 2026-11-08 | E3 | F-WP-22, F-WP-63; also cited in P-15 |
| prefers-reduced-data CSS media feature - CSS \| MDN | <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-data> | 2026-06-16 | 2026-11-08 | E3 | F-WP-24 |
| MDN browser-compat-data: css/at-rules/media.json | <https://raw.githubusercontent.com/mdn/browser-compat-data/main/css/at-rules/media.json> | not shown | 2026-11-08 | E3 | F-WP-24 |
| horizontal-viewport-segments CSS media feature - CSS \| MDN | <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/horizontal-viewport-segments> | 2026-04-20 | 2026-11-08 | E3 | F-WP-25 |
| env() CSS function - CSS \| MDN | <https://developer.mozilla.org/en-US/docs/Web/CSS/env> | 2026-10-08 | 2026-11-08 | E3 | F-WP-25, F-WP-70 |
| What is a progressive web app? - Progressive web apps \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/What_is_a_progressive_web_app> | 2025-12-04 | 2026-11-08 | E3 | F-WP-27 |
| Making PWAs installable - Progressive web apps \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable> | 2026-10-06 | 2026-11-08 | E3 | F-WP-28, F-WP-37, F-WP-38, F-WP-39 |
| Offline and background operation - Progressive web apps \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation> | 2026-09-13 | 2026-11-08 | E3 | F-WP-30 |
| Caching - Progressive web apps \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching> | 2025-06-12 | 2026-11-08 | E3 | F-WP-31, F-WP-32, F-WP-33 |
| Best practices for PWAs - Progressive web apps \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Best_practices> | 2025-06-30 | 2026-11-08 | E4/E3 | F-WP-35, F-WP-56 |
| Storage quotas and eviction criteria - Web APIs \| MDN | <https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria> | 2026-01-05 | 2026-11-08 | E3 | F-WP-36 |
| Installing and uninstalling web apps - Progressive web apps \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Installing> | 2026-09-17 | 2026-11-08 | E3 | F-WP-38, F-WP-39 |
| BeforeInstallPromptEvent - Web APIs \| MDN | <https://developer.mozilla.org/en-US/docs/Web/API/BeforeInstallPromptEvent> | 2023-10-25 | 2026-11-08 | E3 | F-WP-40 |
| MDN browser-compat-data: api/BeforeInstallPromptEvent.json | <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/BeforeInstallPromptEvent.json> | not shown | 2026-11-08 | E3 | F-WP-40 |
| display - Web app manifest \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display> | 2025-08-08 | 2026-11-08 | E3 | F-WP-42 |
| display_override - Web app manifest \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display_override> | 2025-11-13 | 2026-11-08 | E3 | F-WP-44 |
| start_url - Web app manifest \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/start_url> | 2026-08-31 | 2026-11-08 | E3 | F-WP-45 |
| scope - Web app manifest \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/scope> | 2025-06-23 | 2026-11-08 | E3 | F-WP-46 |
| shortcuts - Web app manifest \| MDN | <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/shortcuts> | 2025-11-30 | 2026-11-08 | E3 | F-WP-47 |
| PushManager - Web APIs \| MDN | <https://developer.mozilla.org/en-US/docs/Web/API/PushManager> | 2026-09-28 | 2026-11-08 | E3 | F-WP-57 |
| MDN browser-compat-data: api/PushManager.json | <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/PushManager.json> | not shown | 2026-11-08 | E3 | F-WP-57 |
| History API - Web APIs \| MDN | <https://developer.mozilla.org/en-US/docs/Web/API/History_API> | 2024-07-26 | 2026-11-08 | E3 | F-WP-58 |
| Navigation API - Web APIs \| MDN | <https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API> | 2026-01-14 | 2026-11-08 | E3 | F-WP-59 |
| MDN browser-compat-data: api/Navigation.json | <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/Navigation.json> | not shown | 2026-11-08 | E3 | F-WP-59 |
| Window: beforeunload event - Web APIs \| MDN | <https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event> | 2026-10-26 | 2026-11-08 | E3 | F-WP-61 |
| History: scrollRestoration property - Web APIs \| MDN | <https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration> | 2025-05-23 | 2026-11-08 | E3 | F-WP-62 |
| View Transition API - Web APIs \| MDN | <https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API> | 2026-09-28 | 2026-11-08 | E3 | F-WP-63 |
| :focus-visible CSS pseudo-class - CSS \| MDN | <https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible> | 2026-10-16 | 2026-11-08 | E3 | F-WP-64 |
| inputmode HTML global attribute - HTML \| MDN | <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode> | 2026-04-17 | 2026-11-08 | E3 | F-WP-65 |
| autocomplete HTML attribute - HTML \| MDN | <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete> | 2026-08-27 | 2026-11-08 | E3 | F-WP-66 |
| enterkeyhint HTML global attribute - HTML \| MDN | <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint> | 2026-04-17 | 2026-11-08 | E3 | F-WP-67 |
| `<meta name="viewport">` HTML attribute value - HTML \| MDN | <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport> | 2026-09-23 | 2026-11-08 | E3 | F-WP-68, F-WP-70 |
| VirtualKeyboard API - Web APIs \| MDN | <https://developer.mozilla.org/en-US/docs/Web/API/VirtualKeyboard_API> | 2025-11-06 | 2026-11-08 | E3 | F-WP-69 |
| MDN browser-compat-data: api/VirtualKeyboard.json | <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/VirtualKeyboard.json> | not shown | 2026-11-08 | E3 | F-WP-69 |
| touch-action CSS property - CSS \| MDN | <https://developer.mozilla.org/en-US/docs/Web/CSS/touch-action> | 2026-04-20 | 2026-11-08 | E3 | F-WP-72 |
| overscroll-behavior CSS property - CSS \| MDN | <https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior> | 2026-10-13 | 2026-11-08 | E3 | F-WP-73 |
| CSS scroll snap - CSS \| MDN | <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap> | 2026-08-21 | 2026-11-08 | E3 | F-WP-74 |

### Cited in principles only

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| MDN, `inputmode` global attribute (older path of the page cited in F-WP-65) | <https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode> | not recorded | not recorded | E3 | none (principle only: P-07) |
| MDN, `autocomplete` attribute (older path of the page cited in F-WP-66) | <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete> | not recorded | not recorded | E3 | none (principle only: P-07) |
| MDN, Notifications API: Using the Notifications API (request permission on user gesture) | <https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API> | not recorded | not recorded | E3 | none (principle only: P-14) |
