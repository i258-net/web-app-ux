---
id: EVAL-METHODS
title: Evaluation methods and what each can verify
type: reference
status: active
updated: 2026-11-08
---

# Evaluation methods and what each can verify

A review's claims are bounded by its method. State the method up front, and never claim more than it can show. The table lists each method's power for the dimensions and gate families.

| Can verify → | Static screenshots | Interactive prototype | Running application | Automated tests / tooling | Real-user study |
|---|---|---|---|---|---|
| Visual hierarchy, layout, labels, affordances (D-05, parts of D-02/D-03/D-06) | **Yes** (at captured viewports only) | Yes | Yes | Partial (contrast, overflow) | Indirect |
| Target size and spacing (QG-019, QG-040) | Estimate only (needs known scale) | Yes | Yes | Partial (DOM box sizes) | Indirect |
| Navigation structure and location cues (D-02) | Structure yes; behavior no | Yes (scripted paths) | Yes | No | **Yes** (findability) |
| Browser back, deep links, reload, restoration (QG-060…063) | **No** | Usually no | **Yes** | Partial (e2e scripts) | Indirect |
| Hover, focus, keyboard operability, focus order (QG-001…006) | **No** (focus indicator visible only if captured) | Partial | **Yes** | Partial (focusability, missing names) | Indirect |
| Screen-reader behavior, live regions, names/roles (QG-016, QG-028, D-08) | **No** | No | **Yes with AT** | Partial (axe-style checks find ~30–40% of issue types by common estimates; treat as a floor, not a conformance result) | Yes with AT users |
| Virtual keyboard behavior, `inputmode`, autofill (D-04, QG-053) | No | No | **Yes on device/emulator** | Partial (attribute inspection) | Yes |
| Validation timing, error messages, recovery (D-07) | Only if error states were captured | Partial | **Yes** | Partial (e2e) | Yes |
| Loading, offline, failure handling (QG-070…072, QG-093) | No | No | **Yes with throttling/offline** | Partial (e2e) | Indirect |
| Performance / Core Web Vitals (QG-080…082) | **No** | No | Lab only (indicative) | **Yes** (field data preferred; lab indicative) | Field data from real users |
| PWA install, display mode, update flow (QG-090…094) | No | No | **Yes (install it)** | Partial (manifest/SW checks) | Yes |
| Task completion, time on task, error rate (D-01) | Inference only | Partial (scripted) | Inference from walkthrough | No | **Yes** (the only method that measures it) |
| Comprehension and mental models (D-06, D-02) | Inference | Partial | Inference | No | **Yes** |
| Cross-device continuity (D-10) | No | No | Yes with multiple devices/viewports | Partial | Yes |

## Rules of claim

1. **Screenshot review** reports *observable visual and structural characteristics* and *likely concerns*. It never reports verified keyboard access, screen-reader behavior, performance, or task completion. Phrase accordingly: "Targets appear smaller than 44 px (estimate from 390 px-wide capture); verify in running app."
2. **Prototype review** adds scripted-path behavior but not platform behavior (history, keyboard, AT, performance). Say which paths were exercised.
3. **Running-application review** can verify most behaviors. It still cannot establish task success for real users or comprehension. Record device, browser, viewport, input used, network conditions, and whether AT was used.
4. **Automated tooling** establishes a subset of objective gates. A passing automated accessibility scan is a *floor*, not a conformance claim. A passing Lighthouse lab score is *indicative*, not field CWV.
5. **Real-user studies** provide evidence that heuristic review cannot replace. When a review disagrees with user data, the user data wins unless the study is flawed.
6. **Source-code inspection** is a supplementary method: it can reveal implementation facts (attributes, media features used, manifest, service worker strategies, `beforeunload` registration) that are invisible in screenshots. It verifies presence, not behavior.

## Minimum method for a claim of cross-device quality

To claim a product is good across devices, the review must have examined at least one compact touch context and one expanded pointer context with a running application or prototype, plus the transition between them. Otherwise report the gap.
