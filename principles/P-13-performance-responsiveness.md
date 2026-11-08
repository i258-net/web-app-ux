---
id: P-13
title: Performance and responsiveness
type: principle
topics: [performance, speed, core-web-vitals, perceived-performance, resilience]
dimensions: [D-09]
patterns: [PAT-SH-010, PAT-PW-011, PAT-PW-005, PAT-PW-006, PAT-MO-010]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-13 Performance and responsiveness

## Universal outcome

The product feels immediate. Content appears quickly and stably, interactions respond without perceptible lag, and the experience degrades gracefully on slow devices and poor networks rather than failing. Perceived speed (what users feel) matters as much as measured speed, and both are designed, not left to chance.

## Why it matters

- Core Web Vitals give widely adopted, measurable thresholds: Largest Contentful Paint ≤ 2.5 s, Interaction to Next Paint ≤ 200 ms, Cumulative Layout Shift ≤ 0.1, each judged at the 75th percentile of page loads (E3; Google's field-data program). They are recommended thresholds, not standards, but they are the best available objective targets.
- The response-time limits (0.1 s / 1 s / 10 s) describe how delay affects the sense of direct manipulation, flow, and attention (E2 origin; see P-10).
- Mobile users are disproportionately on mid-range devices and variable networks; performance budgets set for a developer's laptop systematically overestimate real experience (E3, web.dev).
- Layout shift causes mis-taps and lost reading position, which is both a performance and an ergonomics failure.

## How to recognize it

- Meaningful content paints quickly; nothing jumps as late content arrives (reserved space for images, ads, fonts).
- Interactions respond within ~100 ms with at least visual acknowledgment; longer work shows progress.
- Skeletons or placeholders preserve layout during loads; optimistic updates are reconciled honestly.
- Slow or lost connectivity produces a designed state, not a blank screen.

## Contextual implementation notes

- **Mobile:** test on throttled CPU and network; sticky controls and scroll must not jank (PAT-MO-010).
- **Desktop:** heavy views (tables, dashboards) stay interactive via virtualization and progressive loading.
- **Web/PWA:** caching and prefetching as UX decisions (PAT-PW-006); instant navigations and view transitions (PAT-PW-011); offline (PAT-PW-005).

## Evidence

- web.dev, "Web Vitals." https://web.dev/articles/vitals — E3 (thresholds and p75 rule).
- web.dev, "Interaction to Next Paint (INP)." https://web.dev/articles/inp — E3.
- Nielsen, J. "Response Times: The 3 Important Limits." https://www.nngroup.com/articles/response-times-3-important-limits/ — E4 restating E2.
- web.dev, Learn PWA: Caching. https://web.dev/learn/pwa/caching — E3.

## Evaluation

Primary dimension D-09; gates QG-070, QG-080 … QG-082. Field data is authoritative; lab measurements are indicative; screenshots cannot verify performance.
