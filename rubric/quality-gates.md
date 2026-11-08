---
id: RUBRIC-GATES
title: Objective quality gates
type: rubric
status: active
updated: 2026-11-08
---

# Objective quality gates

Quality gates are requirements or thresholds that can be **meaningfully verified** and reported as *pass*, *fail*, or *not verified*. They are kept separate from rubric judgment. A product can score well on the rubric and still fail a gate, and the gate failure is reported as such.

Two kinds, never conflated:

| `kind` | Meaning | Source class |
|---|---|---|
| **standard** | Normative requirement from a formal standard. Failing is a conformance failure. | E1 |
| **threshold** | Recommended target drawn from platform guidance or empirical research. Failing is a quality risk, not a conformance failure. | E2 / E3 |

Each gate lists the verification methods. `A` = automatable (tools can detect many failures, but passing an automated check does not prove the gate passes), `M` = manual verification required, `AT` = requires testing with assistive technology.

Exact WCAG wording is in the specification; links go to each success criterion. Only the success-criterion text is normative. See `../sources/w3c.md`.

---

## Accessibility (WCAG 2.2, Level A and AA unless noted)

| ID | Gate | Kind | Criterion | Verify |
|---|---|---|---|---|
| QG-001 | All functionality operable via keyboard without specific timings | standard | [SC 2.1.1 Keyboard (A)](https://www.w3.org/TR/WCAG22/#keyboard) | M, A (partial) |
| QG-002 | No keyboard trap | standard | [SC 2.1.2 (A)](https://www.w3.org/TR/WCAG22/#no-keyboard-trap) | M |
| QG-003 | Single-character shortcuts can be turned off, remapped, or are active only on focus | standard | [SC 2.1.4 (A)](https://www.w3.org/TR/WCAG22/#character-key-shortcuts) | M |
| QG-004 | Focus order preserves meaning and operability | standard | [SC 2.4.3 (A)](https://www.w3.org/TR/WCAG22/#focus-order) | M |
| QG-005 | Keyboard focus indicator visible | standard | [SC 2.4.7 (AA)](https://www.w3.org/TR/WCAG22/#focus-visible) | M, A (partial) |
| QG-006 | Focused component not entirely hidden by author-created content (sticky bars, cookie banners, keyboards toolbars) | standard | [SC 2.4.11 Focus Not Obscured (Minimum) (AA)](https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum) | M |
| QG-007 | Text contrast ≥ 4.5:1 (≥ 3:1 for large text) | standard | [SC 1.4.3 (AA)](https://www.w3.org/TR/WCAG22/#contrast-minimum) | A, M (states, images of text) |
| QG-008 | UI component and graphical-object contrast ≥ 3:1 | standard | [SC 1.4.11 (AA)](https://www.w3.org/TR/WCAG22/#non-text-contrast) | A (partial), M |
| QG-009 | Text resizable to 200% without loss of content or functionality | standard | [SC 1.4.4 (AA)](https://www.w3.org/TR/WCAG22/#resize-text) | M |
| QG-010 | Content reflows at 320 CSS px width (or 256 px height for horizontal scroll content) without two-dimensional scrolling, except where 2-D layout is essential | standard | [SC 1.4.10 Reflow (AA)](https://www.w3.org/TR/WCAG22/#reflow) | M, A (partial) |
| QG-011 | No loss of content when text spacing is overridden (line-height 1.5, paragraph 2×, letter 0.12em, word 0.16em) | standard | [SC 1.4.12 (AA)](https://www.w3.org/TR/WCAG22/#text-spacing) | M (bookmarklet/automated assist) |
| QG-012 | Content on hover or focus is dismissible, hoverable, and persistent | standard | [SC 1.4.13 (AA)](https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus) | M |
| QG-013 | Orientation not restricted to portrait or landscape unless essential | standard | [SC 1.3.4 (AA)](https://www.w3.org/TR/WCAG22/#orientation) | M, A (meta/CSS check) |
| QG-014 | Multipoint or path-based gestures have a single-pointer alternative | standard | [SC 2.5.1 (A)](https://www.w3.org/TR/WCAG22/#pointer-gestures) | M |
| QG-015 | Pointer actions can be aborted or undone (no down-event completion, or essential) | standard | [SC 2.5.2 (A)](https://www.w3.org/TR/WCAG22/#pointer-cancellation) | M |
| QG-016 | Accessible name contains the visible label text | standard | [SC 2.5.3 (A)](https://www.w3.org/TR/WCAG22/#label-in-name) | A (partial), AT |
| QG-017 | Motion-actuated functions have UI alternatives and can be disabled | standard | [SC 2.5.4 (A)](https://www.w3.org/TR/WCAG22/#motion-actuation) | M |
| QG-018 | Dragging functionality has a single-pointer non-dragging alternative | standard | [SC 2.5.7 Dragging Movements (AA)](https://www.w3.org/TR/WCAG22/#dragging-movements) | M |
| QG-019 | Pointer targets ≥ 24×24 CSS px, or spacing/equivalent/inline/user-agent/essential exception applies | standard | [SC 2.5.8 Target Size (Minimum) (AA)](https://www.w3.org/TR/WCAG22/#target-size-minimum) | A (partial), M |
| QG-020 | Receiving focus or changing a setting does not trigger an unexpected context change | standard | [SC 3.2.1](https://www.w3.org/TR/WCAG22/#on-focus), [3.2.2 (A)](https://www.w3.org/TR/WCAG22/#on-input) | M |
| QG-021 | Help mechanisms appear in a consistent relative order across pages | standard | [SC 3.2.6 Consistent Help (A)](https://www.w3.org/TR/WCAG22/#consistent-help) | M |
| QG-022 | Input errors are identified and described in text | standard | [SC 3.3.1 (A)](https://www.w3.org/TR/WCAG22/#error-identification) | M, AT |
| QG-023 | Labels or instructions provided for user input | standard | [SC 3.3.2 (A)](https://www.w3.org/TR/WCAG22/#labels-or-instructions) | A (partial), M |
| QG-024 | Error suggestions provided when known | standard | [SC 3.3.3 (AA)](https://www.w3.org/TR/WCAG22/#error-suggestion) | M |
| QG-025 | Legal, financial, or data-modifying submissions are reversible, checked, or confirmable | standard | [SC 3.3.4 (AA)](https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data) | M |
| QG-026 | Previously entered information is auto-populated or selectable, not re-typed, within a process | standard | [SC 3.3.7 Redundant Entry (A)](https://www.w3.org/TR/WCAG22/#redundant-entry) | M |
| QG-027 | Authentication does not require a cognitive function test without alternative or assistance (paste and password managers not blocked) | standard | [SC 3.3.8 Accessible Authentication (Minimum) (AA)](https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum) | M |
| QG-028 | Status messages are programmatically determinable (live regions) without receiving focus | standard | [SC 4.1.3 (AA)](https://www.w3.org/TR/WCAG22/#status-messages) | AT, A (partial) |
| QG-029 | Time limits adjustable, extendable, or off unless essential | standard | [SC 2.2.1 (A)](https://www.w3.org/TR/WCAG22/#timing-adjustable) | M |
| QG-030 | Pinch-zoom and user scaling not disabled (`user-scalable=no`, `maximum-scale<2` absent) | standard (via SC 1.4.4 and 1.4.10) | [SC 1.4.4](https://www.w3.org/TR/WCAG22/#resize-text); see `../sources/w3c.md` for the WCAG2Mobile note | A |

## Touch and pointer comfort (recommended thresholds)

| ID | Gate | Kind | Threshold | Source | Verify |
|---|---|---|---|---|---|
| QG-040 | Primary touch targets ≥ 44×44 CSS px with ≥ 8 px spacing between adjacent targets. Reference figures: Apple HIG 44×44 pt default control size (28×28 pt minimum); Material 48×48 dp with 8 dp spacing; WCAG 2.5.5 (AAA) 44×44 CSS px | threshold | 44–48 px | Apple HIG (E3), Material 3 (E3), WCAG 2.5.5 AAA (E1) | A (partial), M |
| QG-041 | No functionality is hover-only on any device where touch is a supported input | threshold | — | WCAG 1.4.13 context; NN/g hover guidance (E4); web.dev interaction (E3) | M |
| QG-042 | Input handling is not inferred from viewport width: hover- and pointer-dependent behavior is gated on capability media features (`pointer`, `hover`, `any-pointer`, `any-hover`) or on the active event's `pointerType`, never on breakpoints. Media features report capabilities, not the input in use | threshold | — | web.dev Learn Design (E3); MDN PointerEvent.pointerType (E3) | source inspection, M |

## Responsive layout integrity

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-050 | No horizontal page scroll or clipped content at 320, 375, 768, 1024, 1440 CSS px widths | threshold (320 is standard via QG-010) | — | A, M |
| QG-051 | Primary navigation and primary action present and operable at every supported viewport | threshold | — | M |
| QG-052 | Layout honors `env(safe-area-inset-*)` when `viewport-fit=cover` is used; fixed controls not under notches or home indicators | threshold | — | M (device), source inspection |
| QG-053 | Virtual keyboard does not obscure the focused field or the submit control | threshold | — | M (device) |
| QG-054 | Changing window class, orientation, or device posture mid-task preserves form input, selection, open panes, and scroll position | threshold | — | M (running app) |

## Browser navigation and state

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-060 | Browser back returns to the previous meaningful state (closes modal/drawer or returns to previous view) and never exits the app unexpectedly | threshold | — | M |
| QG-061 | Every primary view has a shareable URL that restores it on reload (deep linking) | threshold | — | M |
| QG-062 | Reload preserves in-progress form data (draft/autosave), and any `beforeunload` warning is registered only while unsaved changes exist. The warning alone is insufficient: browsers show generic text and mobile browsers may discard pages without firing it | threshold | MDN beforeunload (E3) | M, A (partial: handler registration) |
| QG-063 | Scroll position restored on back navigation in lists | threshold | — | M |

## Loading and failure handling

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-070 | Any operation exceeding ~1 s shows a progress indication; operations over ~10 s show determinate progress or allow leaving | threshold | 1 s / 10 s response-time limits (NN/g, E4; original Miller/Card research) | M |
| QG-071 | Network failure and offline states produce an in-UI message with a retry path; no raw errors or blank screens | threshold | — | M (throttling) |
| QG-072 | Failed submissions preserve user input | threshold | — | M |

## Performance (Core Web Vitals, recommended thresholds)

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-080 | Largest Contentful Paint ≤ 2.5 s at the 75th percentile of page loads | threshold | web.dev Vitals (E3) | A (field preferred; lab indicative) |
| QG-081 | Interaction to Next Paint ≤ 200 ms at p75 | threshold | web.dev Vitals (E3) | A (field) |
| QG-082 | Cumulative Layout Shift ≤ 0.1 at p75 | threshold | web.dev Vitals (E3) | A |
| QG-083 | Reduced-motion preference disables non-essential animation | threshold (standard at AAA 2.3.3) | — | M, A (partial) |

## PWA (applicable only if the product is installable or claims offline support)

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-090 | Web app manifest meets the target browsers' installability criteria (served over HTTPS; manifest with name or short_name, icons, `start_url`, `display` or `display_override`). A service worker is **not** required for installability per MDN; offline capability is gated separately by QG-093 | threshold (installability criteria are browser-defined and differ) | MDN, Making PWAs installable (E3); web.dev Learn PWA (E3) | A |
| QG-091 | Install prompt is not shown on first load before user intent | threshold | web.dev installation prompt guidance (E3/E4) | M |
| QG-092 | In `standalone`/`fullscreen` display modes, in-app back navigation exists for every non-root view | threshold | web.dev PWA app design (E3) | M (installed) |
| QG-093 | Offline: previously visited core views load; actions requiring network fail gracefully with explanation; no uncaught errors | threshold | web.dev / MDN offline guidance (E3) | M (offline) |
| QG-094 | A new version is communicated and applied without data loss (no silent reload mid-task) | threshold | web.dev update guidance (E3) | M |
| QG-095 | Notification permission requested only after a user action that implies intent, with an explanation; denial respected (no repeated prompting) | threshold | MDN, Using the Notifications API (E3); web.dev, push notification permissions UX (E4) | M |

---

## What is deliberately not a gate

Subjective preferences are not gates: hamburger vs tab bar, labels above vs beside fields, pagination vs infinite scroll, use of a FAB, dark mode availability, animation style. These are evaluated in the rubric with evidence-based reasoning, not pass/fail.

## Reporting

Report each checked gate as `pass`, `fail`, or `not verified` with the method used. Never report `pass` on the strength of an automated check alone for gates marked `M` or `AT`; report `not verified (automated check passed)`.
