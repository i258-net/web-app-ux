---
id: PAT-SH-010
title: Loading states, progress, and perceived speed
type: pattern
scope: shared
topics: [loading, spinners, skeletons, progress-bars, optimistic-ui, response-times, perceived-performance]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-13, P-10, P-11]
dimensions: [D-09, D-07]
gates: [QG-070, QG-028, QG-081, QG-082, QG-083]
related: [PAT-PW-011, PAT-SH-009, PAT-SH-012, PAT-SH-016, PAT-PW-007, PAT-DT-006, PAT-SH-007]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Loading states, progress, and perceived speed

## Problem

Waiting is unavoidable on real networks. Unexplained waiting is what users cannot tolerate. Common failures:

- a blank screen;
- a spinner with no end and no recovery;
- "No records found" flashing before the data arrives;
- placeholders that jump the layout when content lands;
- double submissions because nothing showed that a click registered;
- optimistic updates that pretend success and never reconcile a failure.

## Recommendation

**Outcome:** users always know whether something is happening, roughly how long it will take, and what they can do meanwhile. The interface never claims an outcome it has not achieved.

1. **Use response-time heuristics as design targets, not SLAs.**
   - Around **0.1 s**, the result feels instantaneous; no indicator is needed.
   - Around **1 s**, flow of thought holds; show an indicator if work may exceed this.
   - Around **10 s**, attention starts to break; show determinate progress or let users leave and come back (QG-070).

   These are approximate heuristics from older research. Do not add artificial delays to "match" them.
2. **Acknowledge input at once.** Show a pressed or pending state on the control and prevent duplicate submission (disable *that* control or make the action idempotent). Keep the rest of the UI usable where possible.
3. **Choose the indicator by what you know:**
   - **Determinate progress bar** when remaining work can be estimated (uploads, multi-step jobs). Show what is happening ("Uploading 3 of 8").
   - **Indeterminate indicator** (spinner or bar) for short or unestimable waits, placed at the loading region, not as a global overlay.
   - **Skeleton or placeholder layout** when the content's structure is known. It shows early structure and reserves space, which reduces layout shift (QG-082).
4. **Show content as soon as possible.** Render what is available and replace placeholders progressively. Let users keep working while background work continues.
5. **Keep loading, empty, and error separate.** Never show an empty-state message until loading has finished with zero results (PAT-SH-012). Never leave an indefinite spinner as the only response to a failed request: time out into an error with Retry (PAT-SH-016).
6. **Use optimistic UI only for likely-success, reversible actions.** Show the expected result immediately, mark it as pending where the distinction matters, reconcile with the server, and on failure roll back visibly with an error and a retry. Do not use optimistic UI for payments, irreversible deletes, or anything users would act on before confirmation.
7. **Announce long-running state changes** to assistive technology: "Loading results", "Upload complete" (QG-028). Do not announce every progress tick.
8. **Respect reduced-motion preferences** in shimmer and spinner animations (QG-083).
9. **Measure.** Interaction responsiveness and layout stability have recommended thresholds (QG-081, QG-082). Field data and the PWA perceived-performance pattern (PAT-PW-011) cover them.

## Evidence

- **E4** Nielsen Norman Group, "Response Times: The 3 Important Limits". https://www.nngroup.com/articles/response-times-3-important-limits/ — Approximate limits of 0.1 s, 1 s, and 10 s; longer or variable waits need progress information. A historical synthesis (1993, with a 2014 web update); these are heuristics, not a standard.
- **E2** Nielsen Norman Group, "Progress Indicators Make a Slow System Less Insufferable". https://www.nngroup.com/articles/progress-indicators/ — Reports research in which a dynamic progress indicator improved tolerance of waiting. Lack of feedback provokes repeated clicks. Use determinate progress when work can be estimated.
- **E3** Apple, "Loading". https://developer.apple.com/design/human-interface-guidelines/loading.md — Show content or placeholders as soon as possible, let people work during background loading, use determinate progress when the duration is known and indeterminate when not. Apple platforms.
- **E3** Apple, "Buttons". https://developer.apple.com/design/human-interface-guidelines/buttons.md — Buttons can show an activity indicator and a changed label during a delayed action. Apple platforms.
- **E4** Nielsen Norman Group, "Designing Empty States in Complex Applications". https://www.nngroup.com/articles/empty-state-interface-design/ — Criticizes showing "No records" while data is still loading.
- **E3** React documentation, "useOptimistic". https://react.dev/reference/react/useOptimistic — Documents optimistic values while an action is pending; the delete example restores the item and shows an error on failure. Implementation guidance, not evidence that optimism suits high-risk actions.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Loading-complete and progress status messages must reach AT without focus.

## Alternatives and tradeoffs

- **Spinner vs skeleton.** None of the findings establishes a general winner (coverage gap noted in research). We infer that skeletons suit structured content with known layout and waits longer than about 1 s, because they reserve space and show structure. Spinners suit short waits, unknown layouts, and actions on a single control. A skeleton that does not match the final layout is worse than a spinner, because it causes the shift it was meant to prevent.
- **Optimistic vs confirmed updates.** Optimistic updates feel instant but can lie. Confirmed updates are truthful but slower. Choose by failure probability and consequence. Offline queues are in PAT-PW-007.
- **Blocking vs background.** Blocking overlays prevent conflicting edits but stop all work. Prefer region-level indicators, and block only the parts that are genuinely unsafe to use.
- **Delay before the indicator.** Showing a spinner only after a short delay avoids flicker on fast responses. No finding specifies the delay; keep it well below 1 s.

## Exceptions and failure modes

- Truly instantaneous local actions need no loading state.
- Failure modes:
  - a full-page spinner for a single widget's data;
  - the progress bar stuck at 99 %;
  - an indeterminate spinner that runs forever after a network error;
  - an "Empty" message during loading;
  - the submit button still enabled, producing duplicate orders;
  - an optimistic item that silently disappears on failure;
  - skeleton shimmer with no reduced-motion fallback.

## Evaluation questions

1. Under network throttling, does every view show a loading state within about 1 s, with no blank screen? [running app]
2. Do operations longer than about 10 s show determinate progress or allow leaving? [running app]
3. Is "no results" ever shown before loading completes? [running app] [screenshot]
4. Does content shift when placeholders are replaced (CLS)? [automated] [running app]
5. Is a double click or tap on submit prevented from creating duplicates? [running app]
6. When an optimistic action fails, is the rollback visible and explained? [running app]
7. Are loading and completion announced to a screen reader without excessive chatter? [running app]

## Related

- Principles: P-13, P-10, P-11
- Dimensions: D-09, D-07
- Gates: QG-070, QG-028, QG-081, QG-082, QG-083
- Patterns: PAT-PW-011 (perceived performance, Core Web Vitals), PAT-SH-009 (feedback channels), PAT-SH-012 (empty vs loading), PAT-SH-016 (failure), PAT-PW-007 (optimistic sync), PAT-DT-006 (inline save), PAT-SH-007 (list loading)

## Change log

- 2026-11-08 — Initial version (ADR-001).
