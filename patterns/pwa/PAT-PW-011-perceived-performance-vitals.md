---
id: PAT-PW-011
title: Perceived performance — Core Web Vitals, placeholders, and view transitions
type: pattern
scope: pwa
topics: [performance, core-web-vitals, lcp, inp, cls, skeletons, view-transitions, reduced-motion, perceived-speed, response-time]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-13, P-10, P-12, P-15]
dimensions: [D-09, D-07]
gates: [QG-080, QG-081, QG-082, QG-083, QG-070]
related: [PAT-SH-010, PAT-SH-009, PAT-PW-006, PAT-PW-003, PAT-PW-005]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Perceived performance — Core Web Vitals, placeholders, and view transitions

## Problem

Users judge speed by when the main content appears, whether a tap responds at once, and whether the page jumps under their finger. Teams optimize the wrong thing:

- **A fast shell with a spinner** counts as "loaded" when nothing useful is on screen yet.
- **Lab scores on a developer laptop** stand in for mid-range phones on real networks.
- **Late-loading banners** shift the button the user is about to tap.

Native-feeling animations can hide poor focus handling and cause motion discomfort.

## Recommendation

**Outcome:** main content appears quickly, interactions respond at once, nothing moves unexpectedly, and long waits are explained. This holds for real users on both mobile and desktop.

1. **Measure the three Core Web Vitals in the field at the 75th percentile, separately for mobile and desktop.** Google's recommended "good" thresholds (E3, recommended thresholds, not standards):
   - **LCP ≤ 2.5 s** (QG-080). Needs improvement is above 2.5 s and up to 4.0 s; poor is above 4.0 s.
   - **INP ≤ 200 ms** (QG-081). Needs improvement is above 200 ms and up to 500 ms; poor is above 500 ms.
   - **CLS ≤ 0.1** (QG-082). Needs improvement is above 0.1 and up to 0.25; poor is above 0.25.

   Lab tools help with diagnosis. A non-interactive Lighthouse load can't measure INP; Total Blocking Time (TBT) is the lab proxy.
2. **Get the main content on screen first.** Make the likely LCP image discoverable and prioritized (`fetchpriority="high"`, used sparingly). Don't lazy-load it. Lazy-load what is off screen.
3. **Acknowledge every interaction on the next frame.** Show pressed and pending states at once, and move heavy work off the main thread. INP measures the next paint, not completion, so long operations still need feedback.
4. **Reserve space.** Give images and embeds `width`/`height` or an aspect ratio, and reserve slots for asynchronous content. Insert late UI (banners, "new items") where it won't push targets the user may be about to hit.
5. **Match placeholders to the wait** (QG-070; details in PAT-SH-010).
   - Under about 1 s: no indicator.
   - Over about 1 s: an indicator that names what is loading.
   - Predictable structure: a stable skeleton.
   - Over about 10 s: determinate progress, or the ability to leave and come back.
6. **Use view transitions as an enhancement.** The View Transition API can animate same-document and cross-document changes. Routing, focus placement, history, and announcements must work without it. Feature-detect each part you use.
7. **Honor reduced motion** (QG-083). Under `prefers-reduced-motion: reduce`, replace large slides, zooms, parallax, and shimmer with a fade or an instant change. Keep the status information.
8. **Let cached content show early** in installed apps (PAT-PW-006). A cached shell plus labeled cached data often beats waiting on the network.

## Evidence

- **E3** Google web.dev, "Largest Contentful Paint (LCP)". https://web.dev/articles/lcp — Definition. Good ≤ 2.5 s, needs improvement ≤ 4.0 s, poor > 4.0 s.
- **E3** Google web.dev, "Interaction to Next Paint (INP)". https://web.dev/articles/inp — Covers click, tap, and keyboard interactions, and measures the next paint. Good ≤ 200 ms, needs improvement ≤ 500 ms, poor > 500 ms.
- **E3** Google web.dev, "Cumulative Layout Shift (CLS)". https://web.dev/articles/cls — Unitless. Good ≤ 0.1, needs improvement ≤ 0.25, poor > 0.25.
- **E3** Google web.dev, "Web Vitals". https://web.dev/articles/vitals — Each metric is assessed at the 75th percentile of page loads, segmented by mobile and desktop. Field data is preferred. Lighthouse can't measure INP; TBT is the lab proxy.
- **E3** Google web.dev, "Responsive images". https://web.dev/learn/design/responsive-images — Intrinsic dimensions reserve space. Don't lazy-load the hero image. Use `fetchpriority` sparingly.
- **E4** Nielsen Norman Group, "Response Times: The 3 Important Limits". https://www.nngroup.com/articles/response-times-3-important-limits/ — About 0.1 s feels instantaneous, about 1 s keeps flow, about 10 s holds attention. Historical expert synthesis.
- **E2** Nielsen Norman Group, "Progress Indicators Make a Slow System Less Insufferable". https://www.nngroup.com/articles/progress-indicators/ — Dynamic progress indicators improved tolerance of waiting in the research it reports. Missing feedback provokes repeated clicks.
- **E4** Google web.dev, "prefers-reduced-motion: Sometimes less movement is more". https://web.dev/articles/prefers-reduced-motion — Skeletons and previews convey what is coming. Excessive animation can distract or cause motion sickness. **No controlled comparison of skeletons and spinners is reported.**
- **E3** MDN Web Docs, "View Transition API". https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API — Same-document and cross-document transitions. Support differs by part of the API.
- **E3** MDN Web Docs, "prefers-reduced-motion". https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion — The user's request to minimize nonessential motion.
- **E3** Apple, "Loading" (HIG). https://developer.apple.com/design/human-interface-guidelines/loading.md — Show content or placeholders early and let people keep working. Native guidance.

## Alternatives and tradeoffs

- **Skeleton vs spinner vs progress bar.** No fetched source shows that one is universally better (see PAT-SH-010). Skeletons suit predictable layouts. Spinners suit short, unpredictable waits. Determinate bars suit measurable work.
- **Optimistic UI** feels instant but must handle failure (PAT-PW-007).
- **Transitions.** They can aid orientation when moving between list and detail, but they add time. Keep them short and skippable, and drop them under reduced motion.
- **Passing vs good.** All three metrics can be "good" while a task is still slow end to end, for example a slow search API. Measure task time too.

## Exceptions and failure modes

- Internal or authenticated apps may lack public field data. Use real-user monitoring.
- Failure modes:
  - Reporting a lab Lighthouse score as "Core Web Vitals pass".
  - Combining mobile and desktop into one number.
  - A shimmer that ignores reduced motion.
  - An artificial delay added so a skeleton "shows".
  - A view transition that leaves focus on the old element.
  - Average instead of p75.
  - A cookie banner that causes CLS.

## Evaluation questions

1. What are the field p75 LCP, INP, and CLS, separately for mobile and desktop? [automated]
2. On a mid-range phone with throttling, when does the main content (not the shell) appear? [running app]
3. Does each tap or keypress produce visible feedback on the next frame? [running app]
4. Do late-loading elements move targets the user is about to hit? [running app] [screenshot]
5. Are waits over about 1 s indicated, and over about 10 s given progress or a way to leave? [running app]
6. With reduced motion enabled, are large transitions and shimmers removed? [running app] [automated]
7. Do users describe the app as fast for their key tasks? [user study]

## Related

- Principles: P-13, P-10, P-12, P-15
- Dimensions: D-09, D-07
- Gates: QG-080, QG-081, QG-082, QG-083, QG-070
- Patterns: PAT-SH-010 (loading states), PAT-SH-009 (feedback), PAT-PW-006 (caching), PAT-PW-003 (navigation and transitions), PAT-PW-005 (offline)

## Change log

- 2026-11-08 — Initial version (ADR-001).
