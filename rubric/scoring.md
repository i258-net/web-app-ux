---
id: RUBRIC-SCORING
title: Scoring procedure, confidence, severity, weights, and blocking conditions
type: rubric
status: active
updated: 2026-11-08
---

# Scoring procedure

This document turns dimension levels into results an engineering or design team can act on. It is deliberately conservative: **it is better to report "not verified" than to invent a score.**

## 1. Units of evaluation

A review scores each applicable dimension (D-01 … D-10) **separately for each evaluated device context**:

| Context | What it is | When applicable |
|---|---|---|
| **Mobile** | Compact (and medium, if supported) viewports **and** touch as the primary input. The context is named by the combination; with screenshots only, label it by viewport class and state that input was assumed | Whenever the product supports phones |
| **Desktop** | Expanded or wider viewports with pointer and keyboard | Whenever the product supports laptops/desktops |
| **Tablet / intermediate** | Medium–expanded viewports, touch primary, keyboard/pointer possible | When the product explicitly supports tablets, or when evidence shows meaningful tablet usage |
| **Responsive transitions** | Behavior while resizing, rotating, or switching input mid-task | Always, for any multi-device product |
| **PWA behavior** | Installability, display mode, offline, history, restoration | Only if the product is installable or markets offline/installed use. Otherwise N/A, but the web-platform behaviors (history, reload, unsaved changes) are still evaluated under D-02 and D-07 |

Results are reported **per context**. There is no single "average score" that merges mobile and desktop.

## 2. Assigning a level

For each dimension × context:

1. Collect the **observed evidence** (what you saw, with location and method).
2. Match it to the **behavioral anchors** in `dimensions.md`. Choose the level whose description best matches the *worst-affected primary task*, not the average screen.
3. Record **confidence**: `high` (verified by interaction or measurement), `medium` (strong inference from static evidence or source code), `low` (plausible concern not directly observed).
4. If the dimension cannot be observed with the available method, record **`insufficient evidence`** instead of a level. Do not guess.
5. If the dimension does not apply to this product or context, record **`N/A`** with a one-line reason.

A dimension with low confidence can still be scored, but the report must say the score is provisional and name the method that would confirm it.

## 3. Findings and severity

Each finding is a discrete observation tied to a dimension, a context, and, where possible, a pattern or gate. Severity is assigned on impact, frequency, and persistence (adapted from the widely used NN/g severity rating logic; see `../sources/nngroup.md`):

| Severity | Definition |
|---|---|
| **Blocker** | Prevents completion of a primary task for a user group, or violates a Level A/AA requirement on a critical path, on a supported device |
| **Major** | Significant friction, data loss risk, or exclusion; task completable with difficulty or workaround |
| **Minor** | Noticeable friction or inconsistency; users recover easily |
| **Cosmetic / suggestion** | Polish or opportunity; no task impact |

Each finding records: *what was observed*, *where*, *method*, *confidence*, *which dimension and context*, *supporting pattern/evidence links*, and *recommendation*. Observation and inference are separate fields.

## 4. Blocking conditions (prevent an overall passing result)

A review cannot report an overall pass if any of these hold, regardless of other scores:

- Any **Blocker** finding on a supported device context.
- Any **quality gate marked as a standard** (`QG-*` with `kind: standard`) fails on a critical path, where verified.
- Any dimension at **Level 1** in any evaluated context.
- The **Mobile** or **Desktop** context has not been evaluated at all for a product that supports it, *and* the report claims cross-device quality. (Report the gap instead.)

Blocking conditions are reported at the top of the review. A strong desktop result does not soften a mobile blocker, and vice versa.

## 5. Overall cross-device task-effectiveness judgment

After per-context results, the review states one qualitative judgment on whether the product's primary tasks are achievable and efficient **across all supported devices**: `pass`, `pass with major issues`, or `fail`. It is derived from D-01 and D-10 across contexts plus the blocking conditions, and it is explained in prose. It is not a number.

## 6. Provisional weights

If a team wants a weighted per-context summary, use the following provisional weights. They encode a judgment that task completion, accessibility, and feedback matter more than craft, and they are **uncalibrated**: no inter-rater reliability or outcome validation has been performed. Treat any weighted number as a communication aid, never as a measurement.

| Dimension | Weight | Rationale |
|---|---|---|
| D-01 Task effectiveness | 15 | The purpose of the product |
| D-08 Accessibility | 15 | Exclusion is a failure of the product, and much of it is objectively verifiable |
| D-07 Feedback, errors, recovery | 12 | Primary driver of data loss and abandonment |
| D-02 IA and navigation | 10 | Findability precedes everything |
| D-03 Ergonomics and discoverability | 10 | Mobile-first emphasis; input-modality fit |
| D-04 Input efficiency | 10 | Forms are where most tasks succeed or fail |
| D-09 Performance, resilience, trust | 10 | Speed and honesty strongly affect outcomes |
| D-10 Cross-device appropriateness | 8 | The distinctive goal of this knowledge base |
| D-06 Content clarity | 5 | Important, but partially captured by D-01/D-02 |
| D-05 Visual hierarchy and craft | 5 | Matters; rarely blocks tasks by itself |

Weights sum to 100. Recalibrate when evidence from real reviews is available (see `../governance/rubric-revision.md`).

## 7. Conflicting findings

When two observations point to different levels (e.g. excellent forms, broken navigation) within one dimension and context, score to the **worst-affected primary task** and list the strengths explicitly. When two evaluators or two methods disagree, report both with their confidence and prefer the method with greater verification power (`../evaluation/methods.md`). Never average away a verified failure with an inferred strength.

## 8. What a score is not

- Not a measurement of user satisfaction or conversion.
- Not a conformance claim. "D-08 Level 4" is not "WCAG 2.2 AA conformant"; conformance requires a full audit.
- Not comparable across products reviewed with different methods. A screenshot review and an interactive review of the same product are different evidence.
