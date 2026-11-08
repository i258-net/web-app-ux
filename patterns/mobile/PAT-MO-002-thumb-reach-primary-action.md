---
id: PAT-MO-002
title: Thumb reach and primary-action placement on compact touch screens
type: pattern
scope: mobile
topics: [reachability, thumb-zone, one-handed, primary-action, fab, ergonomics, grips, handedness]
platforms: [mobile, tablet]
viewports: [compact, medium]
inputs: [touch, assistive-tech]
principles: [P-06, P-01, P-12]
dimensions: [D-03, D-01, D-10]
gates: [QG-040, QG-051, QG-006]
related: [PAT-MO-001, PAT-MO-003, PAT-MO-010, PAT-MO-011, PAT-RS-005, PAT-RS-009, PAT-RS-011, PAT-SH-011]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Thumb reach and primary-action placement on compact touch screens

## Problem

People often hold a phone in one hand and tap with the thumb, but not always, and not the same way all the time. When the most frequent action sits in the top corner of a tall phone, many users must shift grip, use a second hand, or stretch — slower, and a cause of dropped phones and mis-taps. The opposite error is also common: teams adopt a single "thumb-zone" heat map as fact, cram every control into the bottom-right for a right-handed thumb, and disadvantage left-handed users, people who cradle the phone, and people using assistive technology, a stylus, or a tablet.

## Recommendation

**Outcome:** the actions people perform most can be reached comfortably in the grips they actually use, without disadvantaging other grips, and without hiding content under controls.

1. **Rank actions by frequency and consequence.** One primary action per view (compose, add, checkout, send) is the candidate for the most comfortable position; destructive or rare actions are not.
2. **Place frequent, non-destructive actions in the lower part of the screen or in a persistent bar** on compact touch layouts — a bottom tab bar (PAT-MO-003), a sticky action bar (PAT-MO-010), a bottom sheet (PAT-MO-011), or a floating primary button. Treat this as a **heuristic that tends to help one-handed use**, not as a universal rule.
3. **Keep content central.** Primary content occupies the middle of the screen; controls frame it at top and bottom edges rather than covering it.
4. **Do not optimize for one hand.** Centre a single floating button, or mirror placements, rather than assuming a right thumb; avoid placing critical controls only in one corner. Never require a reach gesture to the top corner for a frequent action unless an alternative exists (e.g. a bottom-positioned equivalent, or swipe-back plus a visible back button).
5. **Put risk out of easy reach.** Destructive actions should not sit where a resting thumb lands; pair with undo or confirmation (PAT-SH-011).
6. **Keep primary actions at 44–48 px** (QG-040) and present at every viewport (QG-051); a floating or sticky control must not obscure the focused element (QG-006).
7. **Re-evaluate for other contexts.** On tablets, landscape phones and foldables, reach changes completely: hands hold the sides, and the bottom-centre can be the hardest area. Use available space and input capability, not width alone, to reposition actions (PAT-RS-005, PAT-RS-011, PAT-RS-009). Touch laptops are typically used at arm's length, where reach zones do not apply.

## Evidence

Reach zones are *not* a standard. The sources are an informative W3C draft (E4) and observational field work (E2, with substantial limits).

- **E4** W3C, "Mobile Accessibility: How WCAG 2.0 and Other W3C/WAI Guidelines Apply to Mobile" (2015 First Public Working Draft), section 3.5. https://www.w3.org/TR/mobile-accessibility-mapping/ — Recommends placing interactive elements within easy reach while the device is held in different positions; cautions that one-handed optimisation can benefit some and disadvantage others because handedness and thumb movement differ, so flexibility is the goal; states that mobile and desktop have no absolute divide. Predecessor to the current WCAG2Mobile draft; informative, not normative.
- **E4** W3C, "WCAG2Mobile" (2025 Group Draft Note). https://www.w3.org/TR/wcag2mobile-22/ — Current draft does not carry forward a specific reachability requirement; it creates no requirements.
- **E2** Steven Hoober, UXmatters, "How Do Users Really Hold Mobile Devices?" (18 Feb 2013; verified 2026-11-08). https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php — Public field observation of 1,333 phone users (780 touching the screen) over two months. Among those touching the screen: "one handed—49%", "cradled—36%", "two handed—15%"; of one-handed users, "right thumb on the screen—67%", "left thumb on the screen—33%". Grip is "not a static state" and changed "very often—sometimes every few seconds". Limits stated by the author: no denominator of passers-by, no demographics, tablets excluded, largest device a Galaxy Note 2, reach charts approximate, grip switching not captured. An editor's note says the author has since updated these guidelines.
- **E2** Steven Hoober, UXmatters, "Design for Fingers, Touch, and People, Part 1" (6 Mar 2017; verified 2026-11-08). https://www.uxmatters.com/mt/archives/2017/03/design-for-fingers-touch-and-people-part-1.php — Adds 651 observations in schools, offices and homes and a literature review; states users "prefer to view and touch the center of the screen", rejects the familiar thumb-sweep chart, notes Back is often heavily used "even when it's in the upper-right corner", and that people shift their hold a lot without realising it.
- **E3** Apple, "Human Interface Guidelines — Designing for iPadOS". https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados.md — Place controls within easy reach without obstructing content; no numerical reach boundary is given.
- **E3** Google, "Material Design 3 — Floating action button". https://m3.material.io/components/floating-action-button — A FAB represents the screen's most common or important action and persists while content scrolls; a convention, not a requirement for every screen.

*Interpretation (ours):* the evidence supports "frequent actions low and central, content in the middle, flexibility across grips". It does not support precise zone boundaries, a right-hand bias, or claims about all users. The Hoober percentages describe one non-random 2013 sample and should not be quoted as population figures.

## Alternatives and tradeoffs

- **Top-placed primary actions** match conventions where expected (Save in a top app bar); acceptable for infrequent actions.
- **Floating button vs bottom bar.** A FAB costs no height but covers content; a bottom bar reserves space but stacks with browser chrome (PAT-MO-003, PAT-MO-009).

## Exceptions and failure modes

- Forms: the submit button belongs after the last field in reading order; a sticky duplicate may help on long forms, but must not hide fields when the keyboard opens (PAT-MO-004, QG-053).
- Failures: right-corner-only FABs that cover row actions; destructive "Delete" in the thumb's resting zone; bottom bars that cover the last item; reach-optimised layouts carried unchanged into landscape or tablet; focus order that no longer matches visual order after moving actions (QG-004).

## Evaluation questions

- What is each view's primary action, and is it in the lower part or a persistent bar on compact touch? [screenshot]
- Is placement neutral to handedness (centred or mirrored), or biased to one thumb? [screenshot]
- Are destructive actions away from the resting thumb position and recoverable? [prototype]
- Does any floating or sticky action cover content or the focused element? [running app]
- Can participants complete the core task one-handed with either hand, and cradled? [user study]
- Does placement adapt sensibly in landscape and on a tablet? [running app]

## Related

- Principles: [P-06](../../principles/P-06-interaction-ergonomics.md), [P-01](../../principles/P-01-task-effectiveness.md), [P-12](../../principles/P-12-accessibility-inclusion.md); Dimensions: D-03, D-01, D-10; Gates: QG-040, QG-051, QG-006 ([quality gates](../../rubric/quality-gates.md))
- Patterns: PAT-MO-001, PAT-MO-003, PAT-MO-010, PAT-MO-011, PAT-RS-005, PAT-RS-009, PAT-RS-011, PAT-SH-011

## Change log

- 2026-11-08 — Initial version (ADR-001).
