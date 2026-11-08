---
id: PAT-RS-009
title: Input detection — touch vs pointer capabilities, runtime signals, and hybrid devices
type: pattern
scope: responsive
topics: [input-modality, pointer, hover, any-pointer, any-hover, media-queries, hybrid-devices, touch, progressive-enhancement]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-06, P-12, P-02, P-09]
dimensions: [D-03, D-08, D-10]
gates: [QG-042, QG-041, QG-040, QG-019, QG-001, QG-012]
related: [PAT-RS-010, PAT-RS-011, PAT-RS-004, PAT-RS-005, PAT-MO-001, PAT-DT-003, PAT-DT-004, PAT-DT-008]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Input detection — touch vs pointer capabilities, runtime signals, and hybrid devices

This is the repository's home for the thesis that **viewport width does not determine input modality**. Other patterns link here rather than restating it.

## Problem

Teams commonly treat `@media (max-width: 768px)` as "phone, so touch" and everything wider as "desktop, so mouse and hover". Both inferences fail on touchscreen laptops, tablets with keyboards and trackpads, phones with Bluetooth keyboards, and desktop windows snapped narrow. The results: hover-only row actions unreachable on a touch laptop, 24 px targets on a hand-held wide tablet, shortcuts missing from a narrow desktop window.

The opposite error is treating `pointer` and `hover` media features as a reliable "is the user touching right now?" switch. They are not.

## Recommendation

**Outcome:** every core function works with touch, a fine pointer, and the keyboard on any viewport; capability signals only *enhance* that baseline.

1. **Use width for space, capability queries for input.** Width (media or container queries) decides layout; `pointer`, `hover`, `any-pointer`, and `any-hover` decide target padding, hover enhancements, and similar refinements. Never derive one from the other (QG-042).
2. **Know what each feature reports.**
   - `pointer: coarse | fine | none` and `hover: hover | none` describe the **primary** pointing device chosen by the user agent.
   - `any-pointer` and `any-hover` describe the **union of all available** pointing devices. `any-pointer: coarse` and `any-pointer: fine` can both match on the same device.
   - None of them reports the device **currently in use**, and none detects a **keyboard**.
3. **Default to the inclusive case.** Build controls usable with coarse input and the keyboard, then refine for fine pointers (e.g. tighter lists under `(pointer: fine)`).
4. **Treat hover strictly as an enhancement.** Anything revealed on hover must also be reachable by tap/click and focus (QG-041, QG-012). Even `any-hover: hover` does not justify hover-only functions: a touch laptop matches it while the user touches the screen.
5. **Keep coarse affordances when any coarse pointer exists.** Enlarge targets under `@media (any-pointer: coarse)` so a mouse-primary device with a touchscreen still gets touchable targets.
6. **If you need the current modality, observe events, not media.** Each pointer event carries `pointerType` (`"mouse"`, `"pen"`, `"touch"`, or an empty string when the browser cannot detect the device type). Use it for momentary adaptation of the interaction in progress (e.g. a touch-friendly menu after a touch long-press) and handle the empty and unknown cases. Do not persist a "this user is touch" flag that removes pointer or keyboard paths; keyboard use produces no pointer event at all.
7. **Do not hide keyboard affordances by pointer type.** Shortcuts, focus styles, and roving focus apply regardless of `pointer` values; `:focus-visible` follows browser heuristics, not a keyboard-only test, so keep visible focus everywhere.
8. **Test hybrids explicitly**: touch laptop, tablet with keyboard and trackpad, narrow desktop window, phone with external keyboard.

## Evidence

- **E1** W3C, "Media Queries Level 4". https://www.w3.org/TR/mediaqueries-4/ — `pointer` (none/coarse/fine) and `hover` describe the UA-selected primary pointing device; `any-pointer`/`any-hover` aggregate all available devices, so coarse and fine can both match; `any-hover: none` means *no* device can hover. The UA may report a less capable value; keyboards and the current device are not detected. Candidate Recommendation Draft (2026-02-19).
- **E3** Google (web.dev), "Interaction". https://web.dev/learn/design/interaction — Wide displays can accept touch and narrow windows can be used with a mouse; recommends adequate targets and hover alternatives.
- **E3** Apple, "Human Interface Guidelines — Pointing devices". https://developer.apple.com/design/human-interface-guidelines/pointing-devices.md — iPad pointer support supplements touch; experience should stay consistent as people switch among pointer, keyboard, and gestures.
- **E3** Apple, "Human Interface Guidelines — Designing for macOS". https://developer.apple.com/design/human-interface-guidelines/designing-for-macos.md — Current guidance treats touch as secondary on Mac and recommends stable layout and density with larger hit targets or controls that expand on touch.
- **E3** MDN, "PointerEvent: pointerType property". https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/pointerType — (verified 2026-11-08; page last modified 2025-09-18) Indicates the device type that caused a given pointer event: `"mouse"`, `"pen"`, `"touch"`, or `""` if undetectable; other types should be vendor-prefixed. Marked Baseline widely available.
- **E3** MDN, ":focus-visible". https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible — Matches when the browser judges a focus indicator appropriate; not a keyboard-vs-mouse switch.
- **E3** Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines — Optional hover-revealed row actions also reveal on focus and stay persistent when hover is unsupported.
- **E1** W3C, "WCAG 2.2 — 1.4.13 Content on Hover or Focus". https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus — Hover/focus content must be dismissible, hoverable, persistent.
- **E1** W3C, "WCAG 2.2 — 2.1.1 Keyboard". https://www.w3.org/TR/WCAG22/#keyboard — All functionality operable by keyboard, independent of pointer type.
- **E4** Nielsen Norman Group, "Tooltip Guidelines". https://www.nngroup.com/articles/tooltip-guidelines/ — Essential instructions do not belong in hover tooltips; touch needs a deliberate popup path.

*Interpretation (ours):* "default to inclusive, refine for fine pointers" is our synthesis of the E1 semantics and E3 guidance; no source here tests it against the reverse ordering.

## Alternatives and tradeoffs

- **Separate builds or user-agent sniffing.** Brittle and wrong for hybrids; for platform-gated capabilities, feature-detect instead.
- **User "touch mode" or density toggle.** A legitimate complement for expert tools (PAT-RS-004); it changes spacing, never removes functions.
- **`pointer` vs `any-pointer` for sizing.** `pointer` keeps mouse-primary hybrids denser; `any-pointer` protects occasional touch. Prefer `any-pointer` for primary actions.

## Exceptions and failure modes

- `@media (hover: hover)` wrapping the *only* way to reveal actions — fails on touch laptops when the user touches.
- `@media (max-width: …)` used to swap in a touch-only gesture UI or to hide keyboard shortcuts.
- Treating `hover: none` as a guarantee that `:hover` styles never apply; sticky hover states after taps are possible.
- Persisting a modality guess from the first interaction and removing other paths.
- Path-based or drag gestures introduced "because it is touch" without single-pointer alternatives (QG-014, QG-018; PAT-RS-010).

## Evaluation questions

- Does any CSS or script infer touch, hover, or keyboard from viewport width or user agent? [automated] [running app]
- With a mouse in a narrow (< 600 px) window, are fine-pointer affordances and shortcuts still available? [running app]
- On a touchscreen laptop, can every hover-revealed action be reached by touch and by keyboard focus? [running app]
- Are primary touch targets ≥ 44 px wherever any coarse pointer is available? [automated] [running app]
- On a tablet with keyboard and trackpad, does switching input mid-task lose state or functions? [running app] [user study]
- Is visible focus present regardless of pointer type? [screenshot] [running app]

## Related

- Principles: [P-06](../../principles/P-06-interaction-ergonomics.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-02](../../principles/P-02-discoverability-learnability.md), [P-09](../../principles/P-09-consistency-familiarity.md)
- Dimensions: D-03, D-08, D-10; Gates: QG-042, QG-041, QG-040, QG-019, QG-001, QG-012 ([rubric/quality-gates.md](../../rubric/quality-gates.md))
- Patterns: [PAT-RS-010](PAT-RS-010-same-task-different-interaction.md) (modality variants), [PAT-RS-011](PAT-RS-011-orientation-foldables-hybrids.md) (hybrid devices), [PAT-RS-004](PAT-RS-004-adaptive-density.md), [PAT-RS-005](PAT-RS-005-control-positioning.md), PAT-MO-001, PAT-DT-003, PAT-DT-004, PAT-DT-008

## Change log

- 2026-11-08 — Initial version (ADR-001).
