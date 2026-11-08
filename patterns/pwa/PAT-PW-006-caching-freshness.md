---
id: PAT-PW-006
title: Caching strategies as UX — freshness, stale indicators, and refresh
type: pattern
scope: pwa
topics: [caching, service-worker, cache-first, network-first, stale-while-revalidate, freshness, stale-data, refresh, last-updated]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-10, P-13, P-14, P-05]
dimensions: [D-09, D-07]
gates: [QG-093, QG-071, QG-028]
related: [PAT-PW-005, PAT-PW-007, PAT-PW-004, PAT-PW-012, PAT-PW-011, PAT-SH-009, PAT-MO-010]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Caching strategies as UX — freshness, stale indicators, and refresh

## Problem

Service-worker caching decides what users see before the network answers. Teams usually choose a strategy as a performance setting, but the choice has UX consequences:

- **Cache-first** feels instant but can show yesterday's balance as if it were current.
- **Network-first** stays fresh but leaves users waiting on a slow connection while a perfectly good cached copy sits unused.
- **Stale-while-revalidate** refreshes the cache, but the screen the user is looking at doesn't change until a later visit, so people see old data and don't know it.

## Recommendation

**Outcome:** users get useful content quickly and can always tell how current it is. When freshness matters, they can get the latest version.

1. **Choose the strategy per resource from how much staleness it can tolerate:**

| Resource | Strategy | UX obligation |
|---|---|---|
| Versioned shell assets (JS/CSS with hashed names, icons, fonts) | Cache-first, precached | Replace them through the update flow (PAT-PW-012) |
| Content where slightly old is fine (articles, catalogs, avatars) | Stale-while-revalidate | Decide whether the visible view updates when fresh data arrives |
| Content where freshness matters but an old copy helps offline (inbox, dashboards, order status) | Network-first with timeout, then cache | Label the fallback as stale, with its age and a refresh |
| Must-be-current data (prices at checkout, balances before a transfer, permissions) | Network-only | Show a clear failure state offline (PAT-PW-005) |

2. **Label stale content.** When a view shows cached data that may be out of date, show its age ("Updated 2 h ago") and a Refresh action next to it, not hidden in a menu. Use relative time with an absolute timestamp available.
3. **Make background refreshes visible without disrupting the user.** When stale-while-revalidate or a background fetch brings newer data, either apply it to parts of the view not being interacted with, or show a non-modal "New items · Show" affordance. Don't reorder a list under the user's finger or cursor. Announce significant updates as status messages (QG-028).
4. **Provide a manual refresh.** In standalone mode there is no browser reload button, so give an in-app Refresh on views that can go stale. Pull-to-refresh is an optional addition on touch (PAT-MO-010).
5. **Never present a cached success as a new one.** A cached response to a write or transaction is not a confirmation. Writes go to the network or to an explicit queue (PAT-PW-007).
6. **Bound cache size and age.** Use expiration rules so cached data doesn't grow without limit or survive past its useful life. Remove cached personal data on sign-out.
7. **Treat a library's defaults as decisions you still have to make.** Workbox implements strategies; it doesn't choose them for your content.

## Evidence

- **E3** MDN Web Docs, "Caching — Progressive web apps". https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching — Defines cache-first, network-first, and stale-while-revalidate with example uses. Versioning makes cached static assets safe to reuse.
- **E3** Google web.dev, Learn PWA: "Serving". https://web.dev/learn/pwa/serving — Defines the same strategies. Network-first falls back to cache when the network fails. Stale-while-revalidate's refreshed copy normally helps a later request, not the current one.
- **E3** Google web.dev, "Workbox". https://web.dev/learn/pwa/workbox — Workbox provides precaching, routing, runtime strategies, and expiration modules.
- **E3** Google web.dev, "Back/forward cache". https://web.dev/articles/bfcache — bfcache snapshots are a separate cache. A restored page can show state that was current when the user left.
- **E4** Nielsen Norman Group, "Visibility of System Status". https://www.nngroup.com/articles/visibility-system-status/ — Users need to know the system's current state. Silent changes undermine predictability and trust.
- **E2** Nielsen Norman Group, "Consistency in the Omnichannel Experience". https://www.nngroup.com/articles/omnichannel-consistency/ — A participant was frustrated when an account change made by phone didn't appear online. Customers expect current data.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Updates must be programmatically determinable without focus.

Interpretation (ours): the mapping from resource to strategy in the table is our synthesis of MDN and web.dev's descriptions. The sources describe how each strategy behaves and give examples, but they don't classify domain data. No source gives a staleness threshold; it depends on the domain.

## Alternatives and tradeoffs

- **Speed vs correctness.** Cache-first and stale-while-revalidate cut waiting but risk stale data. Network-first cuts staleness but adds waiting on slow networks. A timeout on network-first (fall back to cache after N seconds) is a middle path, and N is a product decision.
- **Auto-apply updates vs prompt.** Auto-applying keeps data current but can move content while users are reading or tapping. A "Show new" affordance keeps things stable at the cost of one tap. Prefer auto-apply for passive views and the prompt for lists people are acting on.
- **Showing timestamps everywhere** adds noise. Show them where decisions depend on freshness, or when the data comes from cache.

## Exceptions and failure modes

- Fully real-time views over sockets don't use these caches for live data. They still need a "reconnecting" state (PAT-PW-005).
- Failure modes:
  - Precaching the whole site, so first visits are slow and storage fills.
  - Cache-first for API responses with no expiry.
  - Stale data with no label after an offline launch.
  - "New items" auto-inserted above the scroll position, moving content.
  - A refresh control only in a hidden overflow.
  - Cached data surviving sign-out on a shared device.
  - An old shell cached forever because asset names aren't versioned.

## Evaluation questions

These need the running app, with the service worker active, throttling, and offline toggling.

1. Which strategy does each resource class use, and does it match how stale that resource may be? [running app] [automated]
2. Offline or on timeout, is cached content labeled with its age and a refresh path? [running app]
3. When fresh data arrives in the background, does the view update without moving the user's target? [running app]
4. Is there an in-app refresh in standalone mode for views that can go stale? [running app]
5. After sign-out, are personal responses removed from Cache Storage? [running app] [automated]
6. Are background-update announcements exposed to assistive technology without focus moves? [running app]
7. Do users trust the data, and do they notice when it is stale? [user study]

## Related

- Principles: P-10, P-13, P-14, P-05
- Dimensions: D-09, D-07
- Gates: QG-093, QG-071, QG-028
- Patterns: PAT-PW-005 (offline), PAT-PW-007 (writes and sync), PAT-PW-004 (bfcache), PAT-PW-012 (shell updates), PAT-PW-011 (perceived performance), PAT-SH-009 (feedback), PAT-MO-010 (pull-to-refresh)

## Change log

- 2026-11-08 — Initial version (ADR-001).
