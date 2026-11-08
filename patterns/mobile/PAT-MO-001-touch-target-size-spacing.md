---
id: PAT-MO-001
title: Touch target size and spacing
type: pattern
scope: mobile
topics: [touch-targets, target-size, spacing, hit-area, ergonomics, accessibility]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, assistive-tech]
principles: [P-06, P-12, P-11]
dimensions: [D-03, D-08]
gates: [QG-019, QG-040]
related: [PAT-MO-002, PAT-MO-008, PAT-MO-010, PAT-RS-004, PAT-RS-009, PAT-SH-008, PAT-SH-011]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Touch target size and spacing

## Problem

A fingertip is imprecise and covers what it touches. On compact touch viewports, small or crowded controls produce mis-taps: the wrong row opens, a neighboring icon fires. Readable is not the same as tappable. Teams also confuse four different numbers (WCAG 24 px, WCAG 44 px, Apple 44 pt, Material 48 dp) and either treat the conformance floor as a design target or treat a platform convention as a legal requirement.

## Recommendation

**Outcome:** people hit the control they intended on the first attempt, with any finger and grip, and adjacent controls are not confused.

1. **Design primary touch targets at 44–48 CSS px in both dimensions, with at least 8 px between adjacent targets.** This is this repository's *recommended threshold* (QG-040), drawn from platform conventions and WCAG's enhanced criterion. Primary means frequent or task-critical: navigation items, primary and secondary buttons, list-row actions, form controls, close/back.
2. **Never go below the WCAG 2.5.8 standard gate (QG-019):** 24×24 CSS px, or one of its five exceptions applies (see Evidence). Dense secondary controls (e.g. inline chips in a compact toolbar) may sit between 24 and 44 px when space genuinely requires it, but must satisfy 2.5.8.
3. **Size the hit area, not the glyph.** A 24 px icon inside a 48 px padded button is the normal construction. Expand the hit area with padding or a pseudo-element; keep the visual compact if density matters.
4. **Separate destructive from frequent actions** — distance, not just size, prevents expensive slips (PAT-SH-011 for destructive actions, PAT-SH-008 for overflow placement).
5. **Make whole rows tappable** when a row has one primary action; avoid nesting small independent targets in a row.
6. **Do not shrink targets when chrome collapses** on scroll (PAT-MO-010).
7. **Test rendered geometry** on a real device, including the 24 px spacing circles for undersized targets.

Touch is not limited to phones. Touchscreen laptops and tablets with keyboards also need comfortable targets when a coarse pointer is present; use capability queries rather than width to adapt density (PAT-RS-009, PAT-RS-004).

## Evidence

The figures below are **different kinds of claims**. WCAG states testable conformance floors; Apple and Material state platform comfort conventions in their own units (pt, dp). They do not conflict, and the units are not interchangeable.

- **E1** W3C, "WCAG 2.2 — 2.5.8 Target Size (Minimum), AA". https://www.w3.org/TR/WCAG22/#target-size-minimum — Pointer targets at least 24×24 CSS px, with exactly five exceptions: **Spacing** (a 24 CSS px diameter circle centred on an undersized target's bounding box does not intersect another target or another undersized target's circle); **Equivalent** (another control on the same page performs the function and meets the criterion); **Inline** (in a sentence, or size constrained by the line-height of non-target text); **User Agent Control** (size set by the browser and not modified by the author); **Essential** (presentation essential or legally required). Backs QG-019.
- **E1** W3C, "WCAG 2.2 — 2.5.5 Target Size (Enhanced), AAA". https://www.w3.org/TR/WCAG22/#target-size-enhanced — 44×44 CSS px, with its own exceptions (equivalent, inline, user-agent, essential) and *no* spacing exception. One of the reference figures behind QG-040.
- **E3** Apple, "Human Interface Guidelines — Accessibility". https://developer.apple.com/design/human-interface-guidelines/accessibility.md — Current control-size table lists iOS/iPadOS **44×44 pt default** control size and **28×28 pt minimum**; recommends about 12 pt padding around bezelled controls and about 24 pt around visible edges of controls without a bezel. The page does not describe 44 pt as a minimum.
- **E3** Google, "Material Design 3 — Designing (accessibility)". https://m3.material.io/foundations/designing — Touch targets at least 48×48 dp (about 9 mm); 24 dp icon within a 48 dp target; 8 dp or more between targets in most cases; separately suggests 44×44 dp for pointer targets.
- **E3** Google, "Material Design 3 — Lists". https://m3.material.io/components/lists — Custom list content must keep targets at least 48×48 dp; single-action rows activate as a whole.
- **E2** Nielsen Norman Group, "Touch Targets on Touchscreens". https://www.nngroup.com/articles/touch-target-size/ — Citing a target-acquisition study, recommends physical targets of at least 1 cm × 1 cm and describes errors from small or crowded targets; readable elements can be too small to tap.
- **E4** W3C, "Mobile Accessibility: How WCAG 2.0 and Other W3C/WAI Guidelines Apply to Mobile" (2015 First Public Working Draft). https://www.w3.org/TR/mobile-accessibility-mapping/ — Older informative recommendation of at least 9 mm × 9 mm with inactive space around near-minimum targets. Not the current normative criterion.

*Interpretation (ours):* 44–48 CSS px is chosen because it sits at or above WCAG AAA and in the range both platform owners use as defaults, while 24 CSS px remains the only figure that is a web conformance requirement.

## Alternatives and tradeoffs

- **Spacing instead of size.** WCAG 2.5.8 lets a small target pass if its 24 px circle is clear of neighbours. This is legitimate for dense toolbars, but small-and-spaced is still harder to hit than large; use it for secondary controls only.
- **Density modes.** Expert apps may offer a compact density; keep the default comfortable and never drop below QG-019 (PAT-RS-004).
- **Equivalent route.** A tiny control can rely on the *Equivalent* exception if an easy-to-find full-size control does the same thing on the same page.

## Exceptions and failure modes

- **Inline text links** within sentences are excepted by both WCAG criteria; still avoid stacking several short links on adjacent lines.
- **Unmodified native controls** (e.g. a default checkbox) fall under the user-agent exception; restyling them removes the exception.
- Common failures: hit box equal to a small glyph; tiny "×" in sheet corners; adjacent Edit/Delete icons without spacing; padding on the visual but not the clickable element; nested tap targets inside a tappable card.
- Treating pt, dp, and CSS px as equal is a modelling error; the platform numbers are reference conventions only.

## Evaluation questions

- Do primary controls render at ≥ 44×44 CSS px hit area with ≥ 8 px separation? [screenshot] [running app]
- Does every pointer target meet 24×24 CSS px or a documented 2.5.8 exception? [automated] [running app]
- Are destructive actions physically separated from frequent ones? [screenshot] [prototype]
- Do targets keep their size when headers or bars compact on scroll? [running app]
- Do participants mis-tap adjacent controls in realistic one- and two-handed use? [user study]
- On a touchscreen laptop or tablet with coarse pointer, are the same controls comfortable? [running app]

## Related

- Principles: [P-06](../../principles/P-06-interaction-ergonomics.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-11](../../principles/P-11-error-prevention-recovery.md); Dimensions: D-03, D-08; Gates: QG-019, QG-040 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-MO-002, PAT-MO-008, PAT-MO-010, PAT-RS-004, PAT-RS-009, PAT-SH-008, PAT-SH-011

## Change log

- 2026-11-08 — Initial version (ADR-001).
