---
id: PAT-MO-009
title: Safe-area insets, dynamic viewport units, and collapsing browser chrome
type: pattern
scope: mobile
topics: [safe-area, notch, home-indicator, viewport-units, dvh, svh, lvh, viewport-fit, browser-chrome, zoom, orientation]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, keyboard, assistive-tech]
principles: [P-06, P-12, P-08, P-13]
dimensions: [D-10, D-08, D-05]
gates: [QG-052, QG-030, QG-013, QG-010, QG-006, QG-082]
related: [PAT-MO-003, PAT-MO-004, PAT-MO-007, PAT-MO-010, PAT-MO-011, PAT-PW-001, PAT-RS-011, PAT-RS-006]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Safe-area insets, dynamic viewport units, and collapsing browser chrome

## Problem

A phone screen is not a clean rectangle and its usable height is not constant. Notches, camera cut-outs, rounded corners, and home indicators intrude at the edges; mobile browsers expand and retract their address and tool bars as the user scrolls; the virtual keyboard takes height away; installed PWAs lose browser chrome entirely. Layouts built on a fixed `100vh` and edge-to-edge fixed bars break in predictable ways: a "full-height" hero whose call-to-action sits under the browser toolbar, a bottom navigation bar under the home indicator, side buttons clipped by a landscape notch, content that jumps as the toolbar retracts. Some teams "fix" layout instability by disabling zoom, which harms low-vision users.

## Recommendation

**Outcome:** interactive content is never under hardware cut-outs or system indicators, full-height layouts fit the space actually visible, layout does not jump while scrolling, and users can still zoom and rotate.

**Safe areas**

1. **Only opt into edge-to-edge when you need it.** `viewport-fit=cover` in the viewport meta extends the page under cut-outs; when you use it, you must pad with safe-area insets (QG-052).
2. **Pad fixed and edge-aligned UI with `env(safe-area-inset-*)`**, with a fallback: e.g. a fixed bottom bar uses `padding-bottom: max(8px, env(safe-area-inset-bottom))`. Apply left/right insets too — in landscape, notches sit at the sides.
3. **Backgrounds may bleed; controls may not.** Let colour fill under the inset; keep text and tap targets inside it.

**Viewport height**

4. **Size full-height layouts with small or dynamic viewport units, deliberately.** `svh` fits the viewport with browser UI expanded — content is never hidden, but a gap can appear when UI retracts; `lvh` (and plain `vh`, which currently equals `lvh`) fits the retracted state, so content can be hidden behind expanded UI; `dvh` tracks the change but can make content resize while scrolling. Use `svh` (or `min-height` with `dvh`) for screens whose bottom must be visible; avoid `dvh` on large layout blocks if the resizing causes jank or layout shift (QG-082).
5. **Prefer `min-height` to `height`** so content can grow and scroll, and so the keyboard and text enlargement do not clip it.
6. **Handle the keyboard separately.** Virtual keyboards normally do not change viewport units, so `dvh` does not solve keyboard occlusion; `interactive-widget` and the VirtualKeyboard API are the relevant controls (PAT-MO-004).

**Never trade accessibility for stability**

7. **Do not disable zoom** (`user-scalable=no`, restrictive `maximum-scale`) — QG-030. Use `width=device-width`.
8. **Support both orientations** (QG-013) and test with notch on either side; reflow at 320 CSS px (QG-010).
9. **Check installed mode** (`display: standalone`) separately: there is no browser chrome, so top and bottom edges meet system UI directly (PAT-PW-001).

Tablets, foldables, and desktop windows have different insets and window segments; container- and capability-based layout is covered in PAT-RS-006 and PAT-RS-011.

## Evidence

- **E3** MDN, "env()" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/CSS/env — `safe-area-inset-top/right/bottom/left` give safe distances from viewport edges for non-rectangular displays (0 on a plain rectangle); `safe-area-max-inset-*` are maximum values; example pads a sticky footer with `env(safe-area-inset-bottom)`; `keyboard-inset-*` are defined by the VirtualKeyboard API. Baseline widely available, with some parts varying.
- **E3** MDN, "&lt;meta name="viewport"&gt;" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport — `viewport-fit` (`auto`, `contain`, `cover`); with `cover`, safe-area insets are strongly recommended; `interactive-widget` (`resizes-visual` default, `resizes-content`, `overlays-content`) and its effect on viewport units; warning that `user-scalable=no` prevents low-vision users from reading, noting WCAG requires at least 2× scaling.
- **E3** MDN, "&lt;length&gt; — viewport-percentage units" (verified 2026-11-08). https://developer.mozilla.org/en-US/docs/Web/CSS/length — Small (`sv*`), large (`lv*`), dynamic (`dv*`), and default units; small fits with UI expanded and is "safer"; large can hide content when UI returns; dynamic can resize content while scrolling, degrading UI and performance; default `vh` etc. currently equal large units.
- **E3** Google web.dev, "The large, small, and dynamic viewport units". https://web.dev/blog/viewport-units — `svh`/`lvh`/`dvh` semantics; dynamic updates may be throttled; virtual keyboards normally do not affect these units.
- **E3** Apple, "Human Interface Guidelines — Layout". https://developer.apple.com/design/human-interface-guidelines/layout.md — Use system safe areas, which exclude edge hardware and overlapping system views; adapt to rotation and window size; decide from available space, not device.
- **E1** W3C, "WCAG 2.2 — 1.3.4 Orientation, AA". https://www.w3.org/TR/WCAG22/#orientation — Do not restrict orientation unless essential.
- **E1** W3C, "WCAG 2.2 — 1.4.4 Resize Text, AA" and "1.4.10 Reflow, AA". https://www.w3.org/TR/WCAG22/#reflow — Basis for QG-030 (zoom) and QG-010 (reflow).
- **E1** W3C, "WCAG 2.2 — 2.4.11 Focus Not Obscured (Minimum), AA". https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum — Fixed bars must not entirely hide focused items.
- **E4** W3C, "Mobile Accessibility" (2015 draft). https://www.w3.org/TR/mobile-accessibility-mapping/ — Keep pinch zoom; avoid restrictive `user-scalable`/`maximum-scale`; prefer resize with reflow over panning.

*Interpretation (ours):* the `svh`-first choice and the `max()` fallback are implementation recommendations derived from MDN's descriptions; no empirical usability study is cited. Browser behaviour for chrome collapse differs across engines and versions — verify on target devices.

## Alternatives and tradeoffs

- **No `viewport-fit=cover`.** The browser letterboxes content inside the safe area; simpler and safe, at the cost of edge-to-edge visuals.
- **`dvh` for app-shell layouts** gives an exact fit at all times; accept that the shell resizes as chrome moves, and keep heavy content outside that resizing box.
- **Script-based measurement** of the visible viewport gives precise control but adds complexity and resize handling; use only when CSS units cannot express the need (not covered by the sources cited here).

## Exceptions and failure modes

- Full-screen media and games may legitimately draw under cut-outs, but controls still respect insets.
- Failures: bottom nav under the home indicator; landscape notch clipping a back button; `height: 100vh` hero with its CTA hidden behind the toolbar; `dvh` on a long page causing visible jumping; `user-scalable=no` added to stop double-tap zoom (MDN's `touch-action: manipulation` removes double-tap zoom while keeping pinch zoom, PAT-MO-007); insets applied in the browser but not in installed mode, or vice versa.

## Evaluation questions

- If `viewport-fit=cover` is set, do all fixed and edge controls use `env(safe-area-inset-*)`? [automated] [running app]
- On a notched phone in both orientations, is any control under a cut-out or the home indicator? [running app]
- Does the first screen's primary action stay visible with browser chrome expanded? [running app]
- Does layout jump as the toolbar retracts during scroll? [running app] [automated]
- Is zoom enabled and the viewport meta free of `user-scalable=no`/restrictive `maximum-scale`? [automated]
- Is the installed PWA's top area clear of the status bar? [running app]

## Related

- Principles: [P-06](../../principles/P-06-interaction-ergonomics.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-08](../../principles/P-08-visual-hierarchy-readability.md), [P-13](../../principles/P-13-performance-responsiveness.md); Dimensions: D-10, D-08, D-05; Gates: QG-052, QG-030, QG-013, QG-010, QG-006, QG-082 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-MO-003, PAT-MO-004, PAT-MO-007, PAT-MO-010, PAT-MO-011, PAT-PW-001, PAT-RS-011, PAT-RS-006

## Change log

- 2026-11-08 — Initial version (ADR-001).
