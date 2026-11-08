---
id: GOV-RUBRIC
title: Revising the rubric and quality gates
type: process
status: active
updated: 2026-11-08
---

# Revising the rubric and quality gates

## Dimensions and anchors

- Adding, removing, or renaming a dimension is a significant change requiring an ADR.
- Anchor wording may be clarified as a minor change if the observable behavior it describes does not change.
- Anchors must remain *behavioral*: an anchor that cannot be observed by at least one method in `evaluation/methods.md` is rejected.

## Weights

Weights are provisional until calibrated. Calibration means at least one of:

- Inter-rater agreement measured across several reviewers on the same products.
- Correlation of per-dimension levels with real-user outcomes (task success, errors, satisfaction).

Until then, weight changes are allowed only with a written rationale and remain labeled *provisional*. Never present a weighted score as validated.

## Quality gates

- A gate of `kind: standard` changes only when the underlying standard changes (new WCAG version, errata). Record the standard's version.
- A gate of `kind: threshold` changes when the cited platform guidance changes (e.g. Core Web Vitals thresholds) or when E2 evidence justifies it. Record the source and date.
- Proposals to add a gate must show: how it is verified, what method, and why it is a requirement rather than a preference.

## Revision log

| Date | Change | Class | Reference |
|---|---|---|---|
| 2026-11-08 | Initial rubric: 10 dimensions, 5 levels, provisional weights, gate set QG-001…095 | Initial | ADR-001 |
