---
id: PAT-PW-003
title: History, Back, and deep links in client-routed apps
type: pattern
scope: pwa
topics: [history, back-button, deep-links, urls, routing, navigation-api, overlays, modals, standalone]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-04, P-09, P-11]
dimensions: [D-02, D-10]
gates: [QG-060, QG-061, QG-092, QG-063]
related: [PAT-PW-001, PAT-PW-004, PAT-PW-008, PAT-SH-001, PAT-SH-015, PAT-MO-011, PAT-DT-010]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# History, Back, and deep links in client-routed apps

## Problem

Browser Back is the most used navigation control on the web, and client-side routing breaks it easily. Typical failures:

- Screens change without a history entry, so Back leaves the app.
- Every keystroke in a filter adds an entry, so Back takes twenty presses.
- A full-screen sheet on a phone looks like a page, but Back closes the page underneath it.
- Links are `<div>` click handlers that can't open in a new tab.
- A shared or reloaded URL lands on the home screen.

Installed apps make this worse. They have no visible Back or URL bar, and often launch straight into a deep view.

## Recommendation

**Outcome:** Back and Forward move between the states users think of as places. Every such place has a URL that restores it. Direct arrival, by link, reload, shortcut, or notification, produces an understandable view with a way up.

1. **Decide what counts as a history entry.** Push an entry (`pushState`, or a Navigation API navigation) for each destination users would call "a page": a list, a record, a step, a page-like overlay. Replace the entry (`replaceState`) for refinements users don't think of as places, such as typing in search, adjusting a slider, or switching sort. Filters and sort still go in the URL so the view can be shared and reloaded.
2. **Make page-like overlays closable with Back.** On compact viewports, a full-screen dialog or sheet that replaces the view should push an entry, and Back should close it (QG-060). A small anchored popover doesn't need an entry; Escape and an explicit Close dismiss it.
3. **Use real links and real URLs** for navigation (`<a href>`) so new tab, copy link, bookmark, and middle-click work (QG-061). Users park work in tabs to compare and remember, so support that.
4. **Restore on traversal.** On `popstate`, or the Navigation API `navigate` event, restore the route and its state: selection, filters, open panel, and scroll (QG-063, PAT-PW-004). Put focus somewhere sensible and update the document title.
5. **Make every deep link stand alone.** A view opened directly shows its context (title, parent link, breadcrumb where meaningful) and doesn't depend on in-memory state from a previous screen. Logged-out arrivals return the user to the requested URL after sign-in.
6. **Give installed apps an in-app Back** for every non-root view (QG-092). If there is no in-app history (fresh launch), it goes to the logical parent (PAT-PW-001).
7. **Adopt the Navigation API as an enhancement.** It centralizes interception, focus, and scroll handling. Feature-detect it. Intercept only when `canIntercept` allows, and leave downloads, external links, and hash navigation alone.

## Evidence

- **E1** WHATWG, "HTML Standard — Session history APIs". https://html.spec.whatwg.org/multipage/nav-history-apis.html — `pushState()` creates a session-history entry and `replaceState()` updates the current one. State is serialized. URL rewrites are same-origin. `pushState()` does not fire `popstate`.
- **E3** MDN Web Docs, "History API". https://developer.mozilla.org/en-US/docs/Web/API/History_API — Explains using history entries and `popstate` to restore app state on traversal.
- **E3** MDN Web Docs, "Navigation API". https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API — Exposes same-origin history entries and a `navigate` event with interception, focus, and scroll handling. The initial load is not a `navigate` event, and history cannot be reordered arbitrarily.
- **E3** MDN browser-compat-data, "api/Navigation.json". https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/Navigation.json — As of 2026-11-08: Baseline 2026, with Chrome 102, Firefox 147, Safari 26.2. Sub-features need separate checks, and older browsers still need a fallback.
- **E4** Nielsen Norman Group, "User Control and Freedom". https://www.nngroup.com/articles/user-control-and-freedom/ — Back should return to the previous state. A full-screen overlay that looks like a new page should close on Back.
- **E3** MDN Web Docs, "<a>: The Anchor element". https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a — Fake `href`s with click handlers break copying, new tab, and bookmarking.
- **E2** Nielsen Norman Group, "Page Parking: Multi-Tab Mania". https://www.nngroup.com/articles/multi-tab-page-parking/ — In studies of young adults, people opened several tabs as memory aids for comparison. The age pattern is historical.
- **E3** Google web.dev, "App design". https://web.dev/learn/pwa/app-design — App windows lose familiar browser navigation.
- **E3** MDN Web Docs, "shortcuts — Web app manifest". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/shortcuts — Shortcuts open in-scope URLs directly. We infer that those routes must work without a prior navigation stack.

Interpretation (ours): no source prescribes which UI states deserve entries. The split in step 1 is ours.

## Alternatives and tradeoffs

- **Multi-page architecture.** Document navigation gets history and reload right for free, and a PWA needn't be a single-page app.
- **Overlay entries on wide viewports.** On expanded and wider viewports, a dialog over a visible page is clearly not a page, and some teams don't give it an entry. Either choice is acceptable if consistent. The rule that matters is that Back must never close the underlying page while the overlay is open.
- **Filter state in URL vs in storage.** Storage keeps URLs clean but breaks sharing and reload. Use the URL for anything that defines what the view shows.

## Exceptions and failure modes

- Transient states such as an open menu, a hover card, or validation errors don't belong in history.
- Multi-step transactions that can't be resubmitted (payment confirmation) should replace their entry after submission, so Back doesn't repeat them.
- Failure modes:
  - Router guards that block Back with no explanation.
  - In-app Back that disagrees with browser Back.
  - Scroll reset to the top on Back.
  - Deep links that depend on a list loaded on a previous screen.
  - Focus left on `<body>` after a route change.
  - The same `document.title` on every route.

## Evaluation questions

1. Open a record, open a full-screen sheet, then press Back twice. Does each press undo exactly one step without leaving the app? [running app]
2. Does typing in search or changing sort add history entries? [running app]
3. Can every destination be opened in a new tab, copied, and reloaded to the same view, including filters? [running app] [automated]
4. Opened cold from a URL, shortcut, or notification, does a deep view show its context and a way up? [running app]
5. In the installed app, is there in-app Back on every non-root view? [running app]
6. After Back, are focus, title, and scroll position sensible? [running app]
7. Do users predict correctly what Back will do in overlays? [user study]

## Related

- Principles: P-04, P-09, P-11
- Dimensions: D-02, D-10
- Gates: QG-060, QG-061, QG-092, QG-063
- Patterns: PAT-PW-001 (display modes), PAT-PW-004 (reload and restoration), PAT-PW-008 (unsaved-change guards), PAT-SH-001 (wayfinding), PAT-SH-015 (dialogs), PAT-MO-011 (bottom sheets), PAT-DT-010 (multi-window and tabs)

## Change log

- 2026-11-08 — Initial version (ADR-001).
