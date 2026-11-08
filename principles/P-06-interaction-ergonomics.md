---
id: P-06
title: Interaction ergonomics
type: principle
topics: [ergonomics, touch, pointer, reach, targets, fatigue]
dimensions: [D-03, D-10]
patterns: [PAT-MO-001, PAT-MO-002, PAT-MO-007, PAT-DT-003, PAT-RS-009, PAT-DT-009]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-06 Interaction ergonomics

## Universal outcome

Controls are comfortable to operate with the body and the input device actually in use. Targets are large enough and far enough apart to hit reliably; frequent actions are where the hand already is; no interaction demands precision, speed, or dexterity that excludes people or produces accidental activation.

## Why it matters

- Fingers are imprecise and occlude what they touch. WCAG 2.2 sets a normative minimum of 24×24 CSS px for pointer targets (SC 2.5.8, AA) and an enhanced 44×44 (SC 2.5.5, AAA); Apple's current HIG table lists 44×44 pt as the *default* control size for iOS/iPadOS and 28×28 pt as the *minimum*; Material recommends 48×48 dp targets with 8 dp spacing (E1/E3). The WCAG figure is a conformance floor; the platform figures are comfort conventions for their platforms. This repository recommends 44–48 CSS px for primary touch targets (QG-040) and treats 24 px as the standard gate (QG-019).
- One-handed phone use is common and the thumb's comfortable range does not cover the whole screen; large phones push top corners out of reach (E4, widely reported; Hoober's observational studies are the usual citation and are themselves E2 but with limitations in sampling).
- Precision requirements (tiny close buttons, drag-only interactions, hover-only reveals) exclude people with motor impairments and anyone on a bumpy train. WCAG 2.5.7 requires a non-dragging alternative (E1).

## How to recognize it

- Primary touch targets ≥ 44 px with spacing; no adjacent targets that are easy to confuse.
- On compact viewports, the most frequent actions are in the lower half of the screen or in a persistent bar; rarely used or dangerous actions are out of the way.
- Nothing requires hover, right-click, multi-touch, or drag without a simple alternative.
- Accidental activation is hard; destructive actions are not adjacent to frequent ones.

## Contextual implementation notes

- **Compact touch:** targets and spacing (PAT-MO-001); thumb reach and primary action placement (PAT-MO-002); swipe conflicts with scroll (PAT-MO-007).
- **Pointer:** hover as enhancement, with cursor cues; precision is available but not required (PAT-DT-003).
- **Hybrid:** detect pointer coarseness at runtime, not from width (PAT-RS-009).
- **All:** drag-and-drop with keyboard and button alternatives (PAT-DT-009).

## Evidence

- W3C WCAG 2.2 SC 2.5.8 Target Size (Minimum). https://www.w3.org/TR/WCAG22/#target-size-minimum — E1. SC 2.5.5 Target Size (Enhanced). https://www.w3.org/TR/WCAG22/#target-size-enhanced — E1 (AAA). SC 2.5.7 Dragging Movements. https://www.w3.org/TR/WCAG22/#dragging-movements — E1.
- Apple HIG, Accessibility (control-size table: 44×44 pt default, 28×28 pt minimum for iOS/iPadOS). https://developer.apple.com/design/human-interface-guidelines/accessibility — E3.
- Material Design 3, Foundations: Designing (48×48 dp touch targets, 8 dp spacing). https://m3.material.io/foundations/designing — E3.
- Hoober, S. "How Do Users Really Hold Mobile Devices?" UXmatters, 2013. https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php — E2 (observational; sampling limits).

## Evaluation

Primary dimension D-03; gates QG-019, QG-040, QG-018, QG-041. Target size is estimable from screenshots with known scale; reachability and accidental activation need a device.
