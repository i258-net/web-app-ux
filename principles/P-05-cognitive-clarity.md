---
id: P-05
title: Cognitive clarity and mental models
type: principle
topics: [cognitive-load, mental-models, clarity, plain-language, chunking]
dimensions: [D-06]
patterns: [PAT-SH-014, PAT-SH-012, PAT-SH-013, PAT-SH-009]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# P-05 Cognitive clarity and mental models

## Universal outcome

The interface matches how users already think about the task and asks them to hold as little as possible in their heads. Each step presents what is needed for that decision, in plain language, and no more. Users are never required to remember information from a previous screen, translate system terms, or infer what will happen next.

## Why it matters

- Working memory is small and interruptions are constant, especially on mobile. Nielsen's heuristics "match between system and the real world" and "recognition rather than recall" address this directly (E4).
- NN/g's work on cognitive load distinguishes intrinsic load (the task itself) from extraneous load (the interface); design should remove the extraneous (E4).
- Progressive disclosure, which defers secondary options, is supported by NN/g as a way to improve learnability and reduce errors without removing power (E4).

## How to recognize it

- Terminology is the users', consistent across the product.
- Each screen has one evident purpose and one primary action; secondary options are available but not competing.
- Consequences of actions are explained at the point of decision (what "Archive" does; whether it can be undone).
- Users do not have to remember values across steps; the system carries them forward (also WCAG 3.3.7, E1).

## Contextual implementation notes

- **Compact:** chunk into steps; disclose rather than scroll past; essential context above the fold (PAT-SH-014).
- **Expanded:** more can be shown, but still grouped and prioritized; avoid filling the width with equally weighted options.
- **All:** empty states and onboarding explain, briefly, what the space is for (PAT-SH-012, PAT-SH-013).

## Evidence

- Nielsen, J. "10 Usability Heuristics." https://www.nngroup.com/articles/ten-usability-heuristics/ — E4 (heuristics 2 and 6).
- Whitenton, K. "Minimize Cognitive Load to Maximize Usability." NN/g. https://www.nngroup.com/articles/minimize-cognitive-load/ — E4.
- Nielsen, J. "Progressive Disclosure." NN/g. https://www.nngroup.com/articles/progressive-disclosure/ — E4.
- W3C WCAG 2.2 SC 3.3.7 Redundant Entry. https://www.w3.org/TR/WCAG22/#redundant-entry — E1.

## Evaluation

Primary dimension D-06. Comprehension is verified only by user research; heuristic review identifies likely load problems.
