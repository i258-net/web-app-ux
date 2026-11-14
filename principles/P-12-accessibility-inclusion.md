---
id: P-12
title: Accessibility and inclusive design
type: principle
topics: [accessibility, wcag, inclusive-design, assistive-technology, keyboard, screen-reader]
dimensions: [D-08]
patterns: [PAT-DT-004, PAT-DT-005, PAT-DT-009, PAT-MO-001, PAT-RS-008, PAT-SH-015]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-12 Accessibility and inclusive design

## Universal outcome

Everyone can perceive, operate, and understand the product, whatever their abilities, assistive technologies, or settings. Accessibility is not a feature or a compliance exercise; it is the condition under which the other fourteen principles hold for all users. WCAG 2.2 Level AA is the verifiable floor; inclusive design goes further by treating situational and temporary limitations (bright sun, one hand, noisy room, slow network) as ordinary conditions.

## Why it matters

- WCAG 2.2 is the formal, testable standard referenced by law and procurement in many jurisdictions; its success criteria are normative and verifiable (E1). It is the backbone of this repository's quality gates.
- The W3C's WCAG2Mobile note explains how the criteria apply to mobile contexts (touch targets, orientation, zoom, keyboards) and is informative, not normative (E4/E3).
- Accessible design benefits everyone: captions in noisy places, keyboard operability for power users, large targets for anyone moving. The "curb-cut effect" is widely observed though rarely quantified (E4).
- Automated checks establish only a subset of accessibility requirements; the rest require manual and assistive-technology testing (see `../evaluation/methods.md`). No coverage percentage is claimed here.

## How to recognize it

- Full keyboard operability with visible focus and logical order; no traps.
- Every control has an accessible name matching its visible label; roles and states are exposed.
- Content reflows at 320 CSS px, text resizes to 200%, spacing overrides do not break layout, orientation is not locked, zoom is not disabled.
- Status changes are announced; focus is managed on dynamic changes; motion respects user preference.
- Targets meet at least 24 px (and ideally 44–48 px); gestures and dragging have simple alternatives.

## Contextual implementation notes

- **Mobile:** screen-reader gestures (VoiceOver, TalkBack) work; focus not hidden by keyboard or sticky bars (QG-006); zoom allowed (QG-030) (PAT-MO-001).
- **Desktop:** complete keyboard model per WAI-ARIA Authoring Practices; focus management (PAT-DT-004, PAT-DT-005); drag alternatives (PAT-DT-009).
- **All:** dialogs and sheets trap and restore focus correctly (PAT-SH-015); fluid type honors user font settings (PAT-RS-008).

## Evidence

- W3C, Web Content Accessibility Guidelines (WCAG) 2.2. https://www.w3.org/TR/WCAG22/ — E1.
- W3C, Guidance on Applying WCAG 2.2 to Mobile (WCAG2Mobile), Group Note. https://www.w3.org/TR/wcag2mobile-22/ — E4/E3 (informative).
- W3C, WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/ — E3.
- Microsoft, Inclusive Design toolkit. https://inclusive.microsoft.design/ — E4.

## Evaluation

Primary dimension D-08; gates QG-001 … QG-030. Most require manual or assistive-technology testing; a passing automated scan is a floor, never a conformance claim.
