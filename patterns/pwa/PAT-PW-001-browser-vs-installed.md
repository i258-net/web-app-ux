---
id: PAT-PW-001
title: Browser tab vs installed app — display modes and lost browser chrome
type: pattern
scope: pwa
topics: [pwa, display-mode, standalone, installed, browser-chrome, back-navigation, urls, sharing, manifest]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-04, P-09, P-10, P-14]
dimensions: [D-02, D-10]
gates: [QG-092, QG-060, QG-061, QG-052]
related: [PAT-PW-002, PAT-PW-003, PAT-PW-004, PAT-PW-010, PAT-SH-001, PAT-MO-009, PAT-DT-010]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Browser tab vs installed app — display modes and lost browser chrome

## Problem

The same web app can run in a browser tab or, once installed, in its own window or full screen. In a tab, users have the URL bar, Back, Reload, and Share. In `standalone` or `fullscreen` mode, most of those are gone. Teams design for one mode and ship to both. The installed app strands users on non-root screens with no way back, hides the URL that someone wanted to share, or launches into a view that assumes a navigation history it does not have. Browser mode, meanwhile, gets duplicate chrome.

## Recommendation

**Outcome:** every task works in every display mode. The installed app replaces the browser affordances it removes, and the URL stays real and shareable whatever the mode.

1. **Treat `display` as a request, not a guarantee.** Declare a baseline `display` and test what the browser actually does on launch. Browsers fall back along a defined chain, and `display_override` is an ordered preference list that may be ignored.
2. **Provide in-app Back for every non-root view in `standalone` and `fullscreen`** (QG-092). It must be visible, labeled, and reachable by keyboard and assistive technology. When the view was opened directly (launch URL, shortcut, notification) and there is no in-app history, Back goes to the logical parent, not to nothing.
3. **Keep URLs real in every mode.** Each meaningful view has an addressable URL that restores it on reload (QG-061). Installation must not turn the app into a single URL with hidden state.
4. **Replace lost affordances only where they matter.** In standalone: add a share or copy-link action on shareable content, a way to retry or refresh views that can go stale (see PAT-PW-006), and route titles that tell windows apart. In browser mode, don't duplicate the browser's own Back or Reload controls.
5. **Detect presentation, not installation.** Use the `display-mode` media feature (`matchMedia('(display-mode: standalone)')`) to adjust chrome. It reports the current presentation. It is not a reliable "is installed" flag, because `fullscreen` can match through the Fullscreen API in a plain tab.
6. **Plan the edges of `scope`.** Navigating out of scope (sign-in providers, help sites, payment pages) can bring back browser UI or open another context. Test each of these hand-offs.
7. **Respect window geometry.** Installed desktop windows can be resized and multiplied (PAT-DT-010). Edge-to-edge mobile layouts must keep controls inside the safe-area insets (QG-052, PAT-MO-009).
8. **Treat installed-only entry points as extras.** Manifest `shortcuts` and share targets are optional. The same actions must exist inside the app.

## Evidence

- **E1** W3C, "Web Application Manifest" (Working Draft, 2026-11-06). https://www.w3.org/TR/appmanifest/ — User agents must support `browser`. Unsupported display requests fall back through `fullscreen`, `standalone`, `minimal-ui`, `browser`. The `display-mode` media feature reflects the current presentation, and `fullscreen` can match via the Fullscreen API without installation. Normative text, but the document is a draft.
- **E3** MDN Web Docs, "display — Web app manifest". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display — `standalone` omits standard browser UI such as the URL bar. `minimal-ui` keeps a minimal, browser-dependent set of controls.
- **E3** Google web.dev, "App design". https://web.dev/learn/pwa/app-design — Warns that users lose familiar browser navigation in app windows.
- **E3** MDN Web Docs, "display_override". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display_override — The first supported mode in the list wins, before normal fallback. Marked experimental.
- **E3** Google web.dev, "Detection". https://web.dev/learn/pwa/detection — Uses `matchMedia` on `display-mode` to adapt presentation.
- **E3** MDN Web Docs, "scope — Web app manifest". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/scope — Out-of-scope navigation can expose browser UI. Scope is not a security boundary.
- **E3** MDN Web Docs, "shortcuts — Web app manifest". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/shortcuts — How many shortcuts appear, and how, depends on browser and OS.
- **E3** MDN Web Docs, "<a>: The Anchor element". https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a — Real `href` URLs are what make copying, new tabs, and bookmarking work.
- **E4** Google web.dev, "Window management". https://web.dev/learn/pwa/windows — Installed windows vary in size and number. Document titles distinguish them.
- **E4** Nielsen Norman Group, "User Control and Freedom". https://www.nngroup.com/articles/user-control-and-freedom/ — Back should return users to the previous state.

Interpretation (ours): the direct-launch Back fallback is inferred. No source specifies its design.

## Alternatives and tradeoffs

- **`minimal-ui` instead of `standalone`.** It keeps some browser navigation, which reduces how much you must rebuild, but those controls vary by browser and the mode may fall back. Test what actually appears.
- **Staying `browser`-only.** Not every product benefits from installing. A complete in-tab experience with no install promotion is legitimate (see PAT-PW-002).
- **`fullscreen`** suits immersive media, games, or kiosks, but only with an in-app exit and navigation.
- **Mode-specific chrome vs one chrome.** One header that always includes Back on non-root views is simpler and works in both modes. Hiding Back in browser mode removes duplication but adds a branch that must be tested.

## Exceptions and failure modes

- Root views need no Back. They still need primary navigation (PAT-SH-001).
- Failure modes:
  - In-app Back calls `history.back()` on a fresh launch and does nothing, or exits the app.
  - Share actions copy the start URL instead of the current view.
  - Using `display-mode: standalone` to infer "installed", then hiding the browser-mode install path or showing a broken prompt.
  - Layout built for `window-controls-overlay` without checking the mode actually applied.
  - Fixed bottom bars under the home indicator.
  - Login redirects that leave the app window.

## Evaluation questions

Most of these need the app actually installed on target devices. A responsive preview in a desktop browser cannot answer them.

1. In `standalone`/`fullscreen`, does every non-root view show a visible, labeled, keyboard-reachable Back? [running app]
2. Launched directly into a deep view (shortcut, link, notification), where does in-app Back go? [running app]
3. Can a user copy or share the URL of the current view in the installed app, and does that URL reopen the same view in a browser? [running app]
4. Which display mode does each target browser actually apply, and does the UI adapt? [running app] [automated]
5. Do out-of-scope flows (auth, payment, help) return the user to the app window? [running app]
6. Are fixed controls clear of safe-area insets in installed and browser modes? [screenshot] [running app]
7. Do users of the installed app find a way back and a way to share without being told? [user study]

## Related

- Principles: P-04, P-09, P-10, P-14
- Dimensions: D-02, D-10
- Gates: QG-092, QG-060, QG-061, QG-052
- Patterns: PAT-PW-003 (history and deep links), PAT-PW-002 (installation), PAT-PW-004 (reload and restoration), PAT-PW-010 (platform differences), PAT-SH-001 (navigation), PAT-MO-009 (safe areas), PAT-DT-010 (multi-window)

## Change log

- 2026-11-08 — Initial version (ADR-001).
