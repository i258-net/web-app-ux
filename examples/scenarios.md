---
id: EX-SCENARIOS
title: Representative evaluation scenarios
type: reference
status: active
updated: 2026-11-08
---

# Representative evaluation scenarios

Each scenario states the material available (which determines the method), the device contexts, the primary task, and the knowledge an evaluator should retrieve. They exercise the skill end to end and double as regression tests for retrieval.

## EX-01 Mobile sign-up form (screenshots)

- **Material:** three screenshots at 390×844 CSS px: form at rest, form with keyboard open on the email field, form after submit with errors.
- **Context:** mobile, touch. Method: screenshot review.
- **Task:** create an account with email, password, phone, and date of birth.
- **Observed design:** placeholder-only labels; a numeric date field split into three inputs; error summary at the top of the page only; "Continue" button below the fold when the keyboard is open; password field blocks paste.
- **Expected retrieval:** PAT-SH-002, PAT-SH-003, PAT-MO-004, PAT-MO-005, PAT-MO-001; P-07, P-11; D-04, D-07; QG-023, QG-022, QG-027, QG-053.
- **Expected outcome:** Major D-04 finding on paste-blocking during password *creation* (QG-027 applies to authentication steps, not sign-up; flag the sign-in form for a QG-027 check) and on the keyboard obscuring submit (QG-053: screenshot 2 suggests it; whether the control is reachable by scrolling needs a device); Major on placeholder labels; split date-of-birth field reported with the documented tradeoff (PAT-SH-002 vs PAT-RS-010 on dates far from today); method limits stated (keyboard type, autofill, validation timing unverified).

## EX-02 Desktop settings form (running application)

- **Material:** running app at 1440×900, mouse and keyboard, Chrome; no assistive technology available.
- **Context:** desktop, pointer + keyboard. Method: running app.
- **Task:** change notification preferences and save.
- **Observed design:** two-column form with unrelated fields side by side; Save button at bottom of a long page with no sticky bar; changes apply on toggle without Save for some controls and require Save for others; Tab order jumps between columns; focus indicator removed by CSS.
- **Expected retrieval:** PAT-SH-002, PAT-DT-004, PAT-DT-005, PAT-DT-006, PAT-SH-009, PAT-SH-011; P-10, P-12; D-04, D-07, D-08; QG-004, QG-005, QG-020a.
- **Expected outcome:** Blocker on missing focus indicator (QG-005 fail, verified); Major on inconsistent save model and focus order; recommendation of a consistent commit model with feedback.

## EX-03 Navigation adapting between mobile and desktop (prototype)

- **Material:** clickable prototype at 375 and 1280 CSS px.
- **Context:** responsive transitions, mobile and desktop. Method: prototype.
- **Task:** reach "Reports" and return to "Home".
- **Observed design:** desktop has a seven-item sidebar; mobile hamburger drawer lists five of the seven; current section is highlighted on desktop only; browser back not modeled.
- **Expected retrieval:** PAT-RS-001, PAT-MO-003, PAT-DT-002, PAT-SH-001; P-04, P-09; D-02, D-10; QG-051.
- **Expected outcome:** Major on destination parity and missing current-location cue on mobile; back behavior reported as untested (prototype limit).

## EX-04 Touch vs keyboard interaction on a task board (running application)

- **Material:** running app on a touchscreen laptop (1366×768) and a phone (412×915).
- **Context:** hybrid input; mobile. Method: running app with touch, trackpad, keyboard.
- **Task:** move a card to another column and open its details.
- **Observed design:** card actions appear only on hover; card can be moved only by dragging; on the touchscreen laptop touch shows no actions; keyboard cannot reach cards.
- **Expected retrieval:** PAT-RS-009, PAT-DT-003, PAT-DT-009, PAT-DT-004, PAT-MO-007; P-06, P-12; D-03, D-08; QG-001, QG-018, QG-041, QG-042.
- **Expected outcome:** Blockers on keyboard reach (QG-001) and drag-only (QG-018); explicit statement that width-based input assumptions broke the hybrid device.

## EX-05 Drag-and-drop reordering with accessible alternatives (source + running app)

- **Material:** running app and source code for a sortable list component.
- **Context:** desktop and mobile. Method: running app plus source inspection.
- **Task:** reorder items in a playlist.
- **Observed design:** drag handle present; "Move up/Move down" items in an overflow menu; keyboard reorder via arrow keys while handle focused; live region announces position.
- **Expected retrieval:** PAT-DT-009, PAT-MO-007, PAT-DT-005, PAT-SH-009; P-06, P-12; D-03, D-08; QG-018, QG-028, QG-001.
- **Expected outcome:** Gates pass where verified; Strong level on D-03/D-08 for this component; note any remaining concerns (touch drag conflict with scroll) and what AT testing would add.

## EX-06 Empty, loading, and error states in a dashboard (screenshots + running app)

- **Material:** screenshots of first-use and no-results states at 390 px; running app at 1280 px with network throttling.
- **Context:** mobile and desktop. Method: mixed.
- **Task:** view this week's metrics; recover from a failed load.
- **Observed design:** first-use state is a blank area; no-results state says "No data"; loading shows a spinner for ~6 s with layout shift when charts arrive; failure shows a raw error string with no retry.
- **Expected retrieval:** PAT-SH-012, PAT-SH-010, PAT-SH-016, PAT-SH-009, PAT-PW-005; P-10, P-11, P-13; D-07, D-09; QG-070, QG-071, QG-082.
- **Expected outcome:** Major on empty states without guidance, failure without retry; CLS concern noted as lab-indicative only.

## EX-07 PWA and browser behavior (installed app)

- **Material:** app installed from Chrome on Android and from Safari on iOS; running in standalone display mode; airplane mode available.
- **Context:** PWA. Method: running app (installed), offline.
- **Task:** open a saved item from a notification; go back; continue editing offline.
- **Observed design:** standalone mode; no in-app back on detail views; install prompt shown on first load; offline shows browser dinosaur page; notification permission requested at launch; draft lost on reload.
- **Expected retrieval:** PAT-PW-001, PAT-PW-002, PAT-PW-003, PAT-PW-005, PAT-PW-008, PAT-PW-009, PAT-PW-010; P-04, P-14, P-13; D-02, D-09; QG-091, QG-092, QG-093, QG-095, QG-062.
- **Expected outcome:** Multiple gate failures; iOS-specific limits (no `beforeinstallprompt`, push requires Home Screen install) stated as platform facts, not product defects.

## EX-08 Responsive visual hierarchy of a pricing page (screenshots)

- **Material:** screenshots at 360, 768, 1024, 1920 CSS px.
- **Context:** responsive. Method: screenshot review.
- **Task:** compare plans and choose one.
- **Observed design:** at 1920 px, body text lines exceed ~140 characters and three plan cards sit in a narrow center column with large empty margins; at 360 px, the recommended plan's CTA is visually identical to the others and the comparison table scrolls horizontally without indication; headings scale down to body size at 768 px.
- **Expected retrieval:** PAT-RS-008, PAT-DT-001, PAT-RS-003, PAT-RS-004, PAT-DT-007, PAT-MO-008; P-08, P-15; D-05, D-10; QG-010, QG-050, QG-007.
- **Expected outcome:** Major on line length and flattened hierarchy; Minor on undiscoverable horizontal scroll; contrast "not verified" without measurement.

## EX-09 Cross-device handoff of an in-progress task (running application, two devices)

- **Material:** running app on a phone (390×844) and a laptop (1440×900), same account; network available.
- **Context:** cross-device continuity; PWA/web. Method: running app on both devices.
- **Task:** start a multi-step expense report on the phone (upload a receipt, fill two fields), then open the app on the laptop and finish it.
- **Observed design:** the laptop shows the report list without the draft; the draft exists only in the phone's local storage; after creating a second draft on the laptop, returning to the phone shows both with no indication which is newer; editing the same field on both and saving produces a silent last-write-wins.
- **Expected retrieval:** PAT-PW-004, PAT-PW-007, PAT-PW-008, PAT-DT-010, PAT-RS-011; P-01, P-10, P-14; D-01, D-07, D-10; QG-062, QG-072.
- **Expected outcome:** Major on local-only drafts for a multi-device product and on silent conflict overwrite; the review distinguishes saved-versus-local state, arrival at the right item and step on the second device, and conflict recovery; D-10 scored on continuity, not only on layout adaptation.
