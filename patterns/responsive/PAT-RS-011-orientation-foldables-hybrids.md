---
id: PAT-RS-011
title: Orientation changes, foldables, and hybrid devices — adapting mid-task without losing work
type: pattern
scope: responsive
topics: [orientation, rotation, foldables, viewport-segments, hinge, hybrid-devices, touch-laptop, tablet-keyboard, multitasking, state-preservation]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-01, P-11, P-12, P-06, P-10]
dimensions: [D-10, D-01, D-08, D-03]
gates: [QG-013, QG-010, QG-052, QG-042, QG-041, QG-062]
related: [PAT-RS-009, PAT-RS-002, PAT-RS-006, PAT-RS-010, PAT-DT-010, PAT-MO-009, PAT-PW-004]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Orientation changes, foldables, and hybrid devices — adapting mid-task without losing work

## Problem

Devices change shape and input while people are using them. A phone rotates in the middle of filling a form. A foldable opens from a compact to a near-square screen, or is used half-folded with a hinge across the display. An iPad gains a keyboard and trackpad and is put into Split View. A touchscreen laptop is used with the trackpad one moment and a finger the next. Common failures:

- Portrait-locked pages, or landscape layouts that hide the form behind a giant header.
- Re-rendering on resize that resets form input, scroll position, the selected item, or an open dialog.
- Controls or text placed across a fold or hinge.
- A device classified once at load ("tablet = touch") and never re-evaluated.

## Recommendation

**Outcome:** any change in orientation, window size, posture, or input keeps the user's work and place, and the new configuration is fully usable with whatever input is now in use.

1. **Support both orientations** unless a specific orientation is essential to the function (QG-013). Do not lock orientation via the manifest or with "please rotate" overlays.
2. **Design for short heights.** Landscape phones have little height: collapse sticky headers, avoid stacked fixed bars, and keep the focused field visible when the virtual keyboard opens.
3. **Preserve state through every change.** Form values, selection, scroll position, open panes and dialogs, and filters must survive rotation, resize, unfold, and window-class transitions. Keep state in the model or URL, not in layout-specific component instances that unmount on a breakpoint ([PAT-RS-002](PAT-RS-002-layout-reflow-canonical-layouts.md)).
4. **Re-evaluate continuously.** Listen for changes (media-query `change` events, resize observers) instead of classifying once at load. Pointer/hover capability media features can change when a pointing device is attached or removed; attaching a keyboard does not change them, so keyboard paths must simply always work ([PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md)).
5. **Foldables: continuous layout first, segments as enhancement.**
   - Without segment information, treat an unfolded device as a normal medium/expanded window.
   - Where `horizontal-viewport-segments` / `vertical-viewport-segments` and `env(viewport-segment-*)` are supported, place related panes on either side of the fold (list-detail fits naturally) and keep interactive controls and text off the hinge area.
   - One segment does not mean the device is not foldable; do not use segment count as a device detector.
6. **Hybrids: every input, any moment.**
   - Touch laptop: hover enhancements plus touch-sized targets where any coarse pointer exists; no hover-only functions (QG-041).
   - Tablet with keyboard/trackpad: full keyboard operation, shortcuts, visible focus, and pointer hover feedback, while touch still works in the same layout.
   - Multitasking windows: test Split View and Slide Over widths, which put a "tablet" into compact or medium classes.
7. **Respect safe areas in every orientation.** Insets move when the device rotates; fixed controls must follow `env(safe-area-inset-*)` (QG-052).

## Evidence

- **E1** W3C, "WCAG 2.2 — 1.3.4 Orientation". https://www.w3.org/TR/WCAG22/#orientation — View and operation must not be restricted to one orientation unless essential.
- **E4** W3C, "WCAG2Mobile" (Group Draft Note). https://www.w3.org/TR/wcag2mobile-22/ — Informative: says 1.3.4 applies and recommends supporting all available orientations, including reversed ones.
- **E3** Android Developers, "App orientation, aspect ratio, and resizability". https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability — Preserve app state, including form input, during orientation and window-size changes.
- **E3** Google, "Material Design 3 — Canonical layouts". https://m3.material.io/foundations/layout/canonical-examples — Items should reflow on rotation, unfolding, or multi-window changes.
- **E3** MDN, "horizontal-viewport-segments". https://developer.mozilla.org/en-US/docs/Web/CSS/@media/horizontal-viewport-segments — Queries the number of viewport segments; marked experimental with limited availability (checked 2026-11-08 in the research notes).
- **E3** MDN, "env()". https://developer.mozilla.org/en-US/docs/Web/CSS/env — Indexed `viewport-segment-*` variables describe segment geometry; `safe-area-inset-*` give safe distances.
- **E3** Google (web.dev), "Screen configurations". https://web.dev/learn/design/screen-configurations — Describes foldable and dual-screen configurations (older course; describes proposals that MDN now documents).
- **E3** Apple, "Human Interface Guidelines — Designing for iPadOS". https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados.md — iPad users combine touch, keyboard, pointer, Pencil, and voice; adapt to orientation, multitasking, and text size.
- **E3** Apple, "Human Interface Guidelines — Multitasking". https://developer.apple.com/design/human-interface-guidelines/multitasking.md — Apps should adapt to resizable multitasking contexts.
- **E3** Apple Support, "Use multitasking on your iPad". https://support.apple.com/en-us/102576 — Split View, Slide Over, and Stage Manager (on some models) produce intermediate and overlapping windows.
- **E3** Apple, "Human Interface Guidelines — Pointing devices". https://developer.apple.com/design/human-interface-guidelines/pointing-devices.md — Pointer supplements touch; keep the experience consistent as people switch inputs.
- **E1** W3C, "Media Queries Level 4". https://www.w3.org/TR/mediaqueries-4/ — `any-pointer` coarse and fine can match together; features describe capabilities, not the current input.
- **E4** Google (web.dev), "Window management". https://web.dev/learn/pwa/windows — Installed app windows remain resizable and can multiply; adapt to window dimensions.

*Interpretation (ours):* "continuous layout first, segments as enhancement" follows from MDN's experimental status. No source here measures usability of hinge-aware web layouts.

## Alternatives and tradeoffs

- **Dedicated landscape layout vs simple reflow.** Most screens only need reflow; media and capture screens benefit from a purpose-built landscape layout.
- **Orientation lock for essential cases.** Acceptable when the orientation is essential (WCAG's exception). Say so, and keep the rest of the app unlocked.
- **Treating a foldable as two windows.** Can suit list-detail; harms content that needs the full width (maps, video). Choose per screen.

## Exceptions and failure modes

- "Rotate your device" blockers for content that works in both orientations.
- Unmounting and remounting a form on breakpoint change, losing input.
- Dialogs that close or lose focus on rotation.
- Classifying input once at page load.
- A fixed bottom bar that lands under the home indicator after rotation.

## Evaluation questions

- Can every screen be used in both portrait and landscape? [running app] [automated]
- Rotate or resize mid-form, mid-selection, and with a dialog open: is everything preserved? [running app]
- In a landscape phone with the keyboard open, is the focused field visible? [running app]
- On a foldable (or emulator) with segments exposed, are controls and text kept off the hinge? [running app]
- On a tablet with keyboard and trackpad, and on a touch laptop, does every function work with each input in the same session? [running app] [user study]
- Does attaching or detaching a mouse or trackpad update capability-dependent styling without reload? [running app] Does every function remain keyboard-operable regardless of what is attached? [running app]

## Related

- Principles: [P-01](../../principles/P-01-task-effectiveness.md), [P-11](../../principles/P-11-error-prevention-recovery.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-06](../../principles/P-06-interaction-ergonomics.md), [P-10](../../principles/P-10-feedback-predictability.md)
- Dimensions: D-10, D-01, D-08, D-03; Gates: QG-013, QG-010, QG-052, QG-042, QG-041, QG-062
- Patterns: [PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md), [PAT-RS-002](PAT-RS-002-layout-reflow-canonical-layouts.md), [PAT-RS-006](PAT-RS-006-breakpoints-window-classes.md), [PAT-RS-010](PAT-RS-010-same-task-different-interaction.md), PAT-DT-010, PAT-MO-009, PAT-PW-004

## Change log

- 2026-11-08 — Initial version (ADR-001).
