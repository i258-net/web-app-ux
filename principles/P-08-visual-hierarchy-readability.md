---
id: P-08
title: Visual hierarchy and readability
type: principle
topics: [hierarchy, typography, readability, contrast, layout]
dimensions: [D-05]
patterns: [PAT-RS-008, PAT-DT-001, PAT-MO-008, PAT-RS-004]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-08 Visual hierarchy and readability

## Universal outcome

The eye lands first on what matters most and reads comfortably from there. Importance is encoded consistently through size, weight, contrast, position, and space, so users can scan a screen and understand its structure before reading a word. Text is legible at the device's typical viewing distance for people with ordinary and reduced vision.

## Why it matters

- Users scan rather than read; NN/g's eye-tracking work (F-pattern and later studies) shows that strong headings and front-loaded content guide attention while flat pages are skimmed inefficiently (E2).
- Contrast and size are normative accessibility requirements: WCAG 1.4.3 (4.5:1 for text), 1.4.11 (3:1 for UI components), 1.4.4 (resize to 200%), 1.4.12 (text spacing) (E1).
- Overlong lines slow reading; typographic guidance converges on roughly 45–75 characters per line, though empirical results vary by task and medium (E4 with partial E2 support).

## How to recognize it

- One primary action per screen is visually dominant; secondary and tertiary actions step down clearly.
- A consistent type scale (a handful of sizes), consistent spacing rhythm, and alignment that creates visible groups.
- Body text comfortably readable without zooming on each device; line length bounded on wide screens.
- Contrast meets or exceeds minimums in all states and themes; hierarchy survives dark mode and zoom.

## Contextual implementation notes

- **Compact:** fewer levels of hierarchy visible at once; truncation and density handled deliberately (PAT-MO-008).
- **Expanded:** bound line length; use the width for structure (columns, panes), not for longer lines (PAT-DT-001); adapt density by window class (PAT-RS-004).
- **Responsive:** fluid type with sensible minimums and maximums (PAT-RS-008).

## Evidence

- Pernice, K. "F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant." NN/g, 2017. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ — E2.
- W3C WCAG 2.2 SC 1.4.3, 1.4.4, 1.4.11, 1.4.12. https://www.w3.org/TR/WCAG22/#contrast-minimum — E1.
- Butterick, M. *Practical Typography*, "Line length." https://practicaltypography.com/line-length.html — E4.
- web.dev, Learn Responsive Design: Typography. https://web.dev/learn/design/typography — E3.

## Evaluation

Primary dimension D-05; gates QG-007, QG-008, QG-009, QG-011. Screenshots verify most of this; zoom, spacing override, and theme behavior need a running app.
