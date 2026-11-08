---
id: P-01
title: Task effectiveness and efficiency
type: principle
topics: [tasks, efficiency, goals, steps]
dimensions: [D-01]
patterns: [PAT-SH-002, PAT-SH-006, PAT-SH-011, PAT-DT-011, PAT-PW-004]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# P-01 Task effectiveness and efficiency

## Universal outcome

Users accomplish what they came to do, completely and correctly, with the fewest steps, decisions, and inputs the task genuinely requires. Effectiveness (can it be done at all, without error) comes before efficiency (how fast). An interface that is fast but produces wrong results, or that only experts can finish, has failed this principle.

Effectiveness and efficiency are two of the three components of usability as defined in ISO 9241-11 (the third is satisfaction), and the first-listed quality attributes in Nielsen's definition of usability. They are the reason the rest of this knowledge base exists.

## Why it matters

- Every extra step, field, or decision is an opportunity to abandon or err. Baymard's checkout research repeatedly attributes abandonment to unnecessary form fields and steps (E2; e-commerce context, likely general for any high-stakes form).
- "Flexibility and efficiency of use" is one of Nielsen's ten heuristics: accelerators for experts should not slow novices (E4, widely adopted).

## How to recognize it

- The primary tasks are identifiable and each has a shortest path that does not require knowledge of the system's internals.
- Defaults are the most common choice; repeated entry is eliminated (see WCAG 3.3.7 Redundant Entry, E1).
- Interruptions (reload, disconnect, switching device) do not lose progress.
- Frequent users have faster paths (shortcuts, bulk actions, recents) that novices can ignore.

## Contextual implementation notes

- **Compact touch:** cut tasks to essentials; one primary action per screen; avoid precision work (see PAT-MO-002, PAT-MO-005).
- **Expanded pointer/keyboard:** add accelerators and density; inline editing and bulk operations (PAT-DT-006, PAT-DT-011).
- **Web/PWA:** preserve state across reload and back (PAT-PW-004, PAT-PW-008).

## Evidence

- Nielsen, J. "Usability 101: Introduction to Usability." NN/g. https://www.nngroup.com/articles/usability-101-introduction-to-usability/ — E4 (definitional).
- Nielsen, J. "10 Usability Heuristics for User Interface Design." NN/g. https://www.nngroup.com/articles/ten-usability-heuristics/ — E4; heuristic 7, flexibility and efficiency of use.
- ISO 9241-11:2018, Ergonomics of human-system interaction — Usability: Definitions and concepts. https://www.iso.org/standard/63500.html — E1 (definitional standard; paywalled, cited for definitions only).
- W3C WCAG 2.2 SC 3.3.7 Redundant Entry. https://www.w3.org/TR/WCAG22/#redundant-entry — E1.
- Baymard Institute, checkout usability research (public articles). https://baymard.com/research/mcommerce-usability — E2; e-commerce context.

## Evaluation

Primary dimension D-01. Only a user study measures completion and time; heuristic review infers from step counts and failure points (see `../evaluation/methods.md`).
