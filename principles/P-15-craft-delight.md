---
id: P-15
title: Visual craft and appropriate delight
type: principle
topics: [craft, polish, motion, delight, brand, animation]
dimensions: [D-05]
patterns: [PAT-RS-008, PAT-RS-004, PAT-SH-010, PAT-SH-012]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# P-15 Visual craft and appropriate delight

## Universal outcome

The product feels considered. Details are consistent, alignment is precise, motion explains rather than decorates, and moments of personality appear where they cost the user nothing. Delight is appropriate when it is subordinate to clarity and performance: it never slows a task, hides information, distracts from errors, or ignores a user's reduced-motion preference.

## Why it matters

- Perceived quality affects perceived usability: the aesthetic–usability effect, first documented by Kurosu and Kashimura (1995) and replicated since, shows users rate attractive interfaces as easier to use (E2). This cuts both ways: polish can mask real problems during evaluation, which is why craft is scored separately and weighted lightly in the rubric.
- Motion that conveys spatial relationships (where a sheet came from, where an item went) aids orientation; motion that merely decorates adds delay. Material and Apple both frame animation as communication (E3).
- Vestibular disorders make some motion physically harmful; WCAG 2.3.3 (AAA) and the `prefers-reduced-motion` media feature exist for this reason (E1/E3).

## How to recognize it

- Consistent spacing, alignment, iconography, and type across every screen and state, including empty, loading, and error states.
- Transitions are short (typically under ~300 ms), purposeful, and interruptible; none block input.
- Personality lives in copy, illustration, and empty states, not in obstacles.
- `prefers-reduced-motion` disables non-essential animation; nothing flashes.

## Contextual implementation notes

- **Compact:** restraint; motion on scroll-heavy screens must not jank.
- **Expanded:** more room for brand expression in layout and imagery without lengthening lines (PAT-RS-008, PAT-RS-004).
- **All:** loading and empty states are the places where craft is most visible (PAT-SH-010, PAT-SH-012).

## Evidence

- Moran, K. "The Aesthetic-Usability Effect." NN/g. https://www.nngroup.com/articles/aesthetic-usability-effect/ — E4 summarizing E2 (Kurosu & Kashimura 1995; Tractinsky et al.).
- Material Design 3, Motion. https://m3.material.io/styles/motion/overview — E3.
- Apple HIG, Motion. https://developer.apple.com/design/human-interface-guidelines/motion — E3.
- W3C WCAG 2.2 SC 2.3.3 Animation from Interactions (AAA). https://www.w3.org/TR/WCAG22/#animation-from-interactions — E1. MDN, `prefers-reduced-motion`. https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion — E3.

## Evaluation

Primary dimension D-05; gate QG-083. Screenshots show static craft; motion needs a running app.
