---
id: SRC-006
title: web.dev and Chrome for Developers
type: source
publisher: Google (web.dev; Chrome for Developers)
evidence_classes: [E3, E4]
status: active
updated: 2026-11-08
---

# SRC-006 web.dev and Chrome for Developers

## Publisher and scope

web.dev is Google's web-platform guidance site. Research read the **Learn Responsive Design** course in full (the index plus 16 modules) and the **Learn PWA** course in full (the index plus 22 modules). It also read articles on the back/forward cache, viewport units, install promotion, reduced motion, and the Core Web Vitals (LCP, INP, CLS, and the Web Vitals overview). Two Chrome for Developers pages were fetched as supplements after web.dev paths returned 404.

The site's strengths are practical, implementation-level guidance on responsive layout, PWA architecture (service workers, caching, installation, updates), and the **Core Web Vitals definitions and "good" thresholds, assessed at the 75th percentile**. These thresholds are the main source for the performance recommended thresholds.

## How to classify their material

| Output | Class | Why |
|---|---|---|
| Core Web Vitals metric definitions, thresholds, and the p75 rule (F-WP-75 to F-WP-78) | **E3, recommended threshold** | Google's documented platform metric. It may back a quality gate labelled as a *recommended threshold*, never as a standard |
| Course modules that document platform behavior, such as service-worker lifecycle, caching strategies, `picture`, and theming | **E3** | Platform-owner documentation of how the web platform works |
| Course modules and articles giving design advice, such as UI patterns, icons, install-promotion patterns, and window management | **E4** | Tutorial or opinion. No study is described |
| Browser-compatibility statements in web.dev courses | **Not used as compatibility evidence** | Many are dated snapshots from 2021–2022. Use MDN and browser-compat-data instead (SRC-007) |

Some pages were cited as E3 by one finding and E4 by another (for example, *Interaction*, *Offline data*, *App design*, and *Update*). The table records both. The class follows the specific claim.

## Licensing and access

web.dev content is free. Unless a page says otherwise, text is CC BY 4.0 and code samples are Apache 2.0. Attribute and paraphrase. Nothing here is paywalled.

## Known limitations and biases

- **Outdated compatibility claims** (WP disagreements section):
  - The **Installation prompt** module (`/learn/pwa/installation-prompt`, 2022-03-09) still says Chrome and Edge on iOS do not support installation. Current MDN documents installation from the Share menu in Safari, Chrome, Edge, Firefox, and Orion from **iOS 16.4** (F-WP-38).
  - The **Update** module (`/learn/pwa/update`, 2022-03-10) groups background APIs, including push, under a "Chromium-only" claim. MDN browser-compat-data documents **conditional Safari push support**: iOS 16.4 or later for Home Screen web apps, and desktop Safari 16 or later on macOS Ventura or later (F-WP-57).
  - Desktop Safari installation (Add to Dock, Safari 17 and later on macOS Sonoma) was likewise assessed from current MDN, not from the course (F-WP-39).

  These passages are **not** used as current compatibility evidence.
- **Course age.** Most modules date from 2021–2022. Some have later updates, such as App design (2024-09-20), Media queries (2025-08-23), and The picture element (2026-07-16).
- **Chromium perspective.** Google ships Chrome, and the guidance favors Chromium capabilities (install prompts, `beforeinstallprompt`, window controls). Treat capability guidance as conditional and feature-detect.
- **No user research.** Performance thresholds come from Google's field-data analysis, which the fetched pages do not describe as usability studies. web.dev discusses skeletons and previews, but no fetched study compares skeletons with spinners.
- **Four web.dev paths returned 404** (listed below). They are failures, not citations.

## Cited pages

All rows were accessed 2026-11-08.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Introduction \| web.dev | <https://web.dev/learn/design/intro> | 2021-11-03 | 2026-11-08 | E4 | F-WP-01 |
| Welcome to Learn Responsive Design! \| web.dev | <https://web.dev/learn/design/welcome> | 2021-10-14 | 2026-11-08 | E4 | F-WP-01 |
| Media queries \| web.dev | <https://web.dev/learn/design/media-queries> | 2025-08-23 | 2026-11-08 | E4 | F-WP-02 |
| Macro layouts \| web.dev | <https://web.dev/learn/design/macro-layouts> | 2021-11-03 | 2026-11-08 | E4 | F-WP-03 |
| Micro layouts \| web.dev | <https://web.dev/learn/design/micro-layouts> | 2021-11-03 | 2026-11-08 | E3 | F-WP-04 |
| Internationalization \| web.dev | <https://web.dev/learn/design/internationalization> | 2021-11-03 | 2026-11-08 | E4 | F-WP-05, F-WP-06 |
| Typography \| web.dev | <https://web.dev/learn/design/typography> | 2021-12-09 | 2026-11-08 | E4 | F-WP-07, F-WP-08; also cited in P-08 |
| Accessibility \| web.dev | <https://web.dev/learn/design/accessibility> | 2021-12-23 | 2026-11-08 | E4 | F-WP-08, F-WP-15 |
| Responsive images \| web.dev | <https://web.dev/learn/design/responsive-images> | 2021-12-09 | 2026-11-08 | E3 | F-WP-09, F-WP-10, F-WP-12 |
| The picture element \| web.dev | <https://web.dev/learn/design/picture-element> | 2026-07-16 | 2026-11-08 | E3 | F-WP-11 |
| Icons \| web.dev | <https://web.dev/learn/design/icons> | 2021-12-09 | 2026-11-08 | E4 | F-WP-13 |
| Theming \| web.dev | <https://web.dev/learn/design/theming> | 2021-12-09 | 2026-11-08 | E3 | F-WP-14 |
| Interaction \| web.dev | <https://web.dev/learn/design/interaction> | 2021-12-23 | 2026-11-08 | E3/E4 | F-WP-16, F-WP-21 |
| Screen configurations \| web.dev | <https://web.dev/learn/design/screen-configurations> | 2021-12-23 | 2026-11-08 | E3 | F-WP-25 |
| User interface patterns \| web.dev | <https://web.dev/learn/design/ui-patterns> | 2021-12-23 | 2026-11-08 | E4 | F-WP-26 |
| Foundations \| web.dev | <https://web.dev/learn/pwa/foundations> | 2021-11-03 | 2026-11-08 | E3 | F-WP-27 |
| Getting started \| web.dev | <https://web.dev/learn/pwa/getting-started> | 2021-11-03 | 2026-11-08 | E3 | F-WP-27 |
| Assets and data \| web.dev | <https://web.dev/learn/pwa/assets-and-data> | 2021-11-18 | 2026-11-08 | E3 | F-WP-29 |
| Offline data \| web.dev | <https://web.dev/learn/pwa/offline-data> | 2022-01-10 | 2026-11-08 | E3/E4 | F-WP-29, F-WP-35 |
| Service workers \| web.dev | <https://web.dev/learn/pwa/service-workers> | 2021-12-03 | 2026-11-08 | E3 | F-WP-30 |
| Caching \| web.dev | <https://web.dev/learn/pwa/caching> | 2021-12-03 | 2026-11-08 | E3 | F-WP-31, F-WP-32, F-WP-33; also cited in P-13 |
| Workbox \| web.dev | <https://web.dev/learn/pwa/workbox> | 2022-01-10 | 2026-11-08 | E3 | F-WP-34 |
| App design \| web.dev | <https://web.dev/learn/pwa/app-design> | 2024-09-20 | 2026-11-08 | E4/E3 | F-WP-35, F-WP-42; also cited in P-04 |
| Installation prompt \| web.dev | <https://web.dev/learn/pwa/installation-prompt> | 2022-03-09 | 2026-11-08 | E3 | F-WP-40; also cited in P-14 |
| Patterns for promoting PWA installation \| Articles \| web.dev | <https://web.dev/articles/promote-install> | 2019-06-04 | 2026-11-08 | E4 | F-WP-41 |
| Update \| web.dev | <https://web.dev/learn/pwa/update> | 2022-03-10 | 2026-11-08 | E3/E4 | F-WP-48, F-WP-49, F-WP-50 |
| Enhancements \| web.dev | <https://web.dev/learn/pwa/enhancements> | 2024-09-20 | 2026-11-08 | E3 | F-WP-50 |
| OS Integration \| web.dev | <https://web.dev/learn/pwa/os-integration> | 2022-04-15 | 2026-11-08 | E3 | F-WP-51, F-WP-53 |
| Detection \| web.dev | <https://web.dev/learn/pwa/detection> | 2024-09-18 | 2026-11-08 | E3 | F-WP-52 |
| Capabilities \| web.dev | <https://web.dev/learn/pwa/capabilities> | 2022-04-20 | 2026-11-08 | E3 | F-WP-53 |
| Window management \| web.dev | <https://web.dev/learn/pwa/windows> | 2022-04-15 | 2026-11-08 | E4 | F-WP-54 |
| Experimental features \| web.dev | <https://web.dev/learn/pwa/experimental> | 2022-04-15 | 2026-11-08 | E3 | F-WP-55 |
| Tools and debug \| web.dev | <https://web.dev/learn/pwa/tools-and-debug> | 2022-05-15 | 2026-11-08 | E3 | F-WP-56 |
| Serving \| web.dev | <https://web.dev/learn/pwa/serving> | 2022-01-10 | 2026-11-08 | E3 | F-WP-56 |
| Back/forward cache \| Articles \| web.dev | <https://web.dev/articles/bfcache> | 2026-10-16 | 2026-11-08 | E3 | F-WP-60 |
| The large, small, and dynamic viewport units \| Blog \| web.dev | <https://web.dev/blog/viewport-units> | 2022-11-29 | 2026-11-08 | E3 | F-WP-71 |
| Largest Contentful Paint (LCP) \| Articles \| web.dev | <https://web.dev/articles/lcp> | 2025-09-04 | 2026-11-08 | E3 | F-WP-75 |
| Interaction to Next Paint (INP) \| web.dev | <https://web.dev/articles/inp> | 2025-09-02 | 2026-11-08 | E3 | F-WP-76; also cited in P-13 |
| Cumulative Layout Shift (CLS) \| Articles \| web.dev | <https://web.dev/articles/cls> | 2023-04-12 | 2026-11-08 | E3 | F-WP-77 |
| Web Vitals \| Articles \| web.dev | <https://web.dev/articles/vitals> | 2024-10-31 | 2026-11-08 | E3 | F-WP-78; also cited in P-13 |
| prefers-reduced-motion: Sometimes less movement is more \| Articles \| web.dev | <https://web.dev/articles/prefers-reduced-motion> | 2019-03-11 | 2026-11-08 | E4 | F-WP-80 |

### Fetched but not cited by a numbered finding

These Chrome for Developers pages were fetched to supplement failed web.dev paths (WP coverage). No finding cites them directly.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Viewport resize behavior (Chrome for Developers blog) | <https://developer.chrome.com/blog/viewport-resize-behavior> | not shown | 2026-11-08 | E3 | none (WP coverage section) |
| VirtualKeyboard API (Chrome for Developers) | <https://developer.chrome.com/docs/web-platform/virtual-keyboard> | not shown | 2026-11-08 | E3 | none (WP coverage section) |

### Failed fetches (not evidence)

| URL | Outcome | Replacement |
|---|---|---|
| <https://web.dev/articles/viewport-units> | HTTP 404 | <https://web.dev/blog/viewport-units> (F-WP-71) |
| <https://web.dev/articles/patterns-for-promoting-pwa-installation> | HTTP 404 | <https://web.dev/articles/promote-install> (F-WP-41) |
| <https://web.dev/articles/viewport-resize-behavior> | HTTP 404 | Chrome blog page above, plus the MDN viewport reference |
| <https://web.dev/articles/virtual-keyboard> | HTTP 404 | MDN VirtualKeyboard API (F-WP-69), plus the Chrome docs page above |
