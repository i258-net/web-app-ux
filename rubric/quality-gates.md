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
| **policy** | A verifiable repository decision with a stated rationale, where the evidence is E4 or the figure is an approximation (e.g. response-time heuristics, zoom meta policy). Failing is a quality risk; the rationale is given in the row. | E4 / repository rationale |

Each gate lists the verification methods. `A` = automatable (tools can detect many failures, but passing an automated check does not prove the gate passes), `M` = manual verification required, `AT` = requires testing with assistive technology.

Exact WCAG wording is in the specification; links go to each success criterion. Only the success-criterion text is normative. See [`../sources/SRC-001-w3c.md`](../sources/SRC-001-w3c.md).

---

## Accessibility (WCAG 2.2, Level A and AA unless noted)

Each row is an operational summary **including the SC's exceptions**. Before reporting a *fail* on a standard gate, read the linked success criterion in full and confirm no exception applies; a verified standard failure blocks a passing review (`scoring.md` §4).

| ID | Gate (summary with exceptions) | Kind | Criterion | Verify |
|---|---|---|---|---|
| QG-001 | All functionality operable through a keyboard interface without requiring specific timings for individual keystrokes. Exception: functions whose underlying input depends on the path of the user's movement (e.g. freehand drawing), not just endpoints | standard | [SC 2.1.1 Keyboard (A)](https://www.w3.org/TR/WCAG22/#keyboard) | M, A (partial) |
| QG-002 | Focus can be moved away from any component using the keyboard; if non-standard keys are required, the user is told how | standard | [SC 2.1.2 (A)](https://www.w3.org/TR/WCAG22/#no-keyboard-trap) | M |
| QG-003 | Single-character (letter, punctuation, number, symbol) shortcuts can be turned off, **remapped to include a non-printable key** (Ctrl, Alt, etc.), or are active only when the relevant component has focus | standard | [SC 2.1.4 (A)](https://www.w3.org/TR/WCAG22/#character-key-shortcuts) | M |
| QG-004 | Where navigation sequence affects meaning or operation, focus order preserves meaning and operability | standard | [SC 2.4.3 (A)](https://www.w3.org/TR/WCAG22/#focus-order) | M |
| QG-005 | A mode of operation exists in which the keyboard focus indicator is visible | standard | [SC 2.4.7 (AA)](https://www.w3.org/TR/WCAG22/#focus-visible) | M, A (partial) |
| QG-006 | When a component receives keyboard focus, it is not entirely hidden by **author-created** content (sticky bars, cookie banners, non-modal overlays). Native virtual keyboards are not author content (see QG-053) | standard | [SC 2.4.11 Focus Not Obscured (Minimum) (AA)](https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum) | M |
| QG-007 | Text and images of text have contrast ≥ 4.5:1, or ≥ 3:1 for large text (≥ 18 pt, or ≥ 14 pt bold). Exceptions: inactive components, pure decoration, text not visible, incidental text in images, logotypes | standard | [SC 1.4.3 (AA)](https://www.w3.org/TR/WCAG22/#contrast-minimum) | A, M (states, images of text) |
| QG-008 | Visual information required to identify UI components and their states, and parts of graphics required to understand content, have ≥ 3:1 contrast against adjacent colors. Exceptions: inactive components, user-agent-determined appearance, essential presentation | standard | [SC 1.4.11 (AA)](https://www.w3.org/TR/WCAG22/#non-text-contrast) | A (partial), M |
| QG-009 | Text (except captions and images of text) can be resized up to 200% without assistive technology and without loss of content or functionality | standard | [SC 1.4.4 (AA)](https://www.w3.org/TR/WCAG22/#resize-text) | M |
| QG-010 | Content presents without loss of information or functionality and without two-dimensional scrolling at 320 CSS px width (vertical scrolling content) or 256 CSS px height (horizontal scrolling content). Exception: parts whose usage or meaning requires two-dimensional layout (maps, data tables, diagrams, toolbars) | standard | [SC 1.4.10 Reflow (AA)](https://www.w3.org/TR/WCAG22/#reflow) | M, A (partial) |
| QG-011 | No loss of content **or functionality** when the user overrides line height to ≥ 1.5× font size, paragraph spacing to ≥ 2×, letter spacing to ≥ 0.12 em, word spacing to ≥ 0.16 em. Exceptions: languages and scripts where a property is not used; content that is not markup text (e.g. canvas, images) | standard | [SC 1.4.12 (AA)](https://www.w3.org/TR/WCAG22/#text-spacing) | M (bookmarklet/automated assist) |
| QG-012 | Additional content shown on hover or focus is dismissible (without moving pointer/focus, unless it does not obscure other content or replaces nothing meaningful), hoverable (pointer can move over it), and persistent until hover/focus removed, dismissed, or no longer valid. Exception: presentation controlled by the user agent (native tooltips) | standard | [SC 1.4.13 (AA)](https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus) | M |
| QG-013 | Content does not restrict view and operation to a single display orientation unless a specific orientation is essential | standard | [SC 1.3.4 (AA)](https://www.w3.org/TR/WCAG22/#orientation) | M, A (meta/CSS check) |
| QG-014 | Functionality using multipoint or path-based gestures is also operable with a **single pointer without a path-based gesture** (e.g. taps/clicks on buttons). Exception: the gesture is essential | standard | [SC 2.5.1 (A)](https://www.w3.org/TR/WCAG22/#pointer-gestures) | M |
| QG-015 | For single-pointer activation, at least one holds: no down-event completion; completion on up-event with abort/undo available; the up-event reverses the down-event outcome; or down-event completion is essential | standard | [SC 2.5.2 (A)](https://www.w3.org/TR/WCAG22/#pointer-cancellation) | M |
| QG-016 | For components with visible text labels, the accessible name contains the visible text | standard | [SC 2.5.3 (A)](https://www.w3.org/TR/WCAG22/#label-in-name) | A (partial), AT |
| QG-017 | Functionality operated by device or user motion is also operable by UI components, and motion response can be disabled. Exceptions: motion used through an accessibility-supported interface; motion is essential | standard | [SC 2.5.4 (A)](https://www.w3.org/TR/WCAG22/#motion-actuation) | M |
| QG-018 | Functionality that uses dragging is also achievable with a single pointer without dragging. Exception: dragging is essential or determined by the user agent and not modified by the author | standard | [SC 2.5.7 Dragging Movements (AA)](https://www.w3.org/TR/WCAG22/#dragging-movements) | M |
| QG-019 | Pointer targets ≥ 24×24 CSS px, or one of: spacing (24 px circle centered on target does not intersect other targets' circles), an equivalent target elsewhere on the page meets it, the target is inline in text, size is user-agent-determined, or the size is essential | standard | [SC 2.5.8 Target Size (Minimum) (AA)](https://www.w3.org/TR/WCAG22/#target-size-minimum) | A (partial), M |
| QG-020a | Receiving focus does not initiate a change of context (no navigation, form submission, or focus move on focus alone; advance notice is **not** an allowance here) | standard | [SC 3.2.1 On Focus (A)](https://www.w3.org/TR/WCAG22/#on-focus) | M |
| QG-020b | Changing a setting of a UI component does not automatically cause a change of context unless the user has been advised beforehand | standard | [SC 3.2.2 On Input (A)](https://www.w3.org/TR/WCAG22/#on-input) | M |
| QG-021 | Help mechanisms of the covered kinds (human contact details, human contact mechanism, self-help option, automated contact mechanism) that are repeated across a set of pages occur in the same relative order unless the user initiates a change | standard | [SC 3.2.6 Consistent Help (A)](https://www.w3.org/TR/WCAG22/#consistent-help) | M |
| QG-022 | Automatically detected input errors are identified and described to the user in text | standard | [SC 3.3.1 (A)](https://www.w3.org/TR/WCAG22/#error-identification) | M, AT |
| QG-023 | Labels or instructions are provided when content requires user input | standard | [SC 3.3.2 (A)](https://www.w3.org/TR/WCAG22/#labels-or-instructions) | A (partial), M |
| QG-024 | When an input error is detected and suggestions are known, they are provided, unless doing so would jeopardize security or purpose | standard | [SC 3.3.3 (AA)](https://www.w3.org/TR/WCAG22/#error-suggestion) | M |
| QG-025 | For pages that cause legal commitments or financial transactions, modify or delete user-controllable data in data storage systems, or submit test responses, at least one of: submissions are reversible; data is checked for errors with an opportunity to correct; a review/confirm/correct step precedes finalization | standard | [SC 3.3.4 (AA)](https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data) | M |
| QG-026 | Information previously entered by or provided to the user in the same process is auto-populated or available to select. Exceptions: re-entering is essential; required for security (e.g. password re-entry); the previous information is no longer valid | standard | [SC 3.3.7 Redundant Entry (A)](https://www.w3.org/TR/WCAG22/#redundant-entry) | M |
| QG-027 | No step of an **authentication process** requires a cognitive function test (remembering a password, solving a puzzle, transcribing) unless at least one holds: an alternative method without such a test; a mechanism assists (e.g. paste and password managers are not blocked); the test is object recognition; or the test uses personal content the user provided. Password *creation* at sign-up is not authentication under the SC; blocking paste there is reported as a Major D-04 finding | standard | [SC 3.3.8 Accessible Authentication (Minimum) (AA)](https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum) | M |
| QG-028 | Status messages can be programmatically determined through role or properties so AT can present them without receiving focus (live regions are one implementation) | standard | [SC 4.1.3 (AA)](https://www.w3.org/TR/WCAG22/#status-messages) | AT, A (partial) |
| QG-029 | For each time limit, at least one holds: the user can turn it off; adjust it to ≥ 10× the default; or is warned before expiry, given ≥ 20 s to extend with a simple action, and can extend ≥ 10 times. Exceptions: real-time events; the limit is essential; the limit is longer than 20 hours | standard | [SC 2.2.1 (A)](https://www.w3.org/TR/WCAG22/#timing-adjustable) | M |
| QG-030 | Pinch-zoom and user scaling are not disabled (`user-scalable=no`, `maximum-scale<2` absent). This is a repository implementation policy that commonly causes QG-009/QG-010 failures on mobile; the normative tests are the resize and reflow outcomes themselves | policy | Supports [SC 1.4.4](https://www.w3.org/TR/WCAG22/#resize-text) and [SC 1.4.10](https://www.w3.org/TR/WCAG22/#reflow); see [`../sources/SRC-001-w3c.md`](../sources/SRC-001-w3c.md) for the WCAG2Mobile note | A, then M (zoom and reflow on device) |

## Touch and pointer comfort (recommended thresholds)

| ID | Gate | Kind | Threshold | Source | Verify |
|---|---|---|---|---|---|
| QG-040 | Primary touch targets ≥ 44×44 CSS px with ≥ 8 px spacing between adjacent targets. Reference figures: Apple HIG 44×44 pt default control size (28×28 pt minimum); Material 48×48 dp with 8 dp spacing; WCAG 2.5.5 (AAA) 44×44 CSS px | threshold | 44–48 px | Apple HIG (E3), Material 3 (E3), WCAG 2.5.5 AAA (E1) | A (partial), M |
| QG-041 | No functionality is hover-only on any device where touch is a supported input | threshold | — | WCAG 1.4.13 context; NN/g hover guidance (E4); web.dev interaction (E3) | M |
| QG-042 | Input handling is not inferred from viewport width: hover- and pointer-dependent behavior is gated on capability media features (`pointer`, `hover`, `any-pointer`, `any-hover`) or on the active event's `pointerType`, never on breakpoints. Media features report capabilities, not the input in use | threshold | — | web.dev Learn Design (E3); MDN PointerEvent.pointerType (E3) | source inspection, M |

## Responsive layout integrity

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-050 | No horizontal *page* scroll or clipped content at 320, 375, 768, 1024, 1440, 1920 CSS px widths. Contained scrolling regions and essential two-dimensional workspaces (maps, canvases, wide data tables with keyboard-reachable scroll) are not failures | threshold (at 320 px the standard is QG-010, with its essential-layout exception) | — | A, M |
| QG-051 | Primary navigation and primary action present and operable at every supported viewport | threshold | — | M |
| QG-052 | Layout honors `env(safe-area-inset-*)` when `viewport-fit=cover` is used; fixed controls not under notches or home indicators | threshold | — | M (device), source inspection |
| QG-053 | With the virtual keyboard open, the focused field and its error text are visible, and the submit control is reachable by scrolling without dismissing the keyboard (it need not be visible simultaneously) | threshold | — | M (device) |
| QG-054 | Changing window class, orientation, or device posture mid-task preserves form input, selection, open panes, and scroll position | threshold | — | M (running app) |

## Browser navigation and state

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-060 | Browser back returns to the previous meaningful state (closes modal/drawer or returns to previous view) and never exits the app unexpectedly | threshold | — | M |
| QG-061 | Every primary view has a shareable URL that restores it on reload (deep linking) | threshold | — | M |
| QG-062 | For work users would not want to redo, reload or accidental navigation preserves in-progress input (draft/autosave) **except** sensitive fields (passwords, card numbers, one-time codes), which are instead protected by a loss warning and disclosed as not restored; trivial inputs (search box, filters) need no draft. Any `beforeunload` warning is registered only while unsaved changes exist and is never the sole protection (browsers show generic text; mobile browsers may discard pages without firing it) | threshold | MDN beforeunload (E3); PAT-PW-004, PAT-PW-008 | M, A (partial: handler registration) |
| QG-063 | Scroll position restored on back navigation in lists | threshold | — | M |

## Loading and failure handling

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-070 | Any operation exceeding ~1 s shows a progress indication; operations over ~10 s show determinate progress or allow leaving. Approximate limits adopted as repository policy from the NN/g restatement (E4) of Miller 1968 and Card et al. 1991; not measured boundaries | policy | NN/g response-time limits (E4 restating E2) | M |
| QG-071 | Network failure and offline states produce an in-UI message with a retry path; no raw errors or blank screens | threshold | — | M (throttling) |
| QG-072 | Failed submissions preserve user input | threshold | — | M |

## Performance (Core Web Vitals, recommended thresholds)

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-080 | Largest Contentful Paint ≤ 2.5 s at the 75th percentile of page loads | threshold | web.dev Vitals (E3) | A (field preferred; lab indicative) |
| QG-081 | Interaction to Next Paint ≤ 200 ms at p75 | threshold | web.dev Vitals (E3) | A (field) |
| QG-082 | Cumulative Layout Shift ≤ 0.1 at p75 | threshold | web.dev Vitals (E3) | A |
| QG-083 | When `prefers-reduced-motion: reduce` is set, non-essential motion animation (movement, parallax, scaling, auto-playing motion) is disabled or replaced (a brief opacity fade is acceptable). Broader than SC 2.3.3 (AAA), which covers interaction-triggered motion only | policy (SC 2.3.3 AAA is the related standard) | MDN prefers-reduced-motion (E3); WCAG 2.3.3 (E1, AAA) | M, A (partial) |

## PWA (applicable only if the product is installable or claims offline support)

| ID | Gate | Kind | Threshold | Verify |
|---|---|---|---|---|
| QG-090 | Web app manifest meets the target browsers' installability criteria (served over HTTPS; manifest with name or short_name, icons, `start_url`, `display` or `display_override`). A service worker is **not** required for installability per MDN; offline capability is gated separately by QG-093 | threshold (installability criteria are browser-defined and differ) | MDN, Making PWAs installable (E3); web.dev Learn PWA (E3) | A |
| QG-091 | Install prompt is not shown on first load before user intent | threshold | web.dev installation prompt guidance (E3/E4) | M |
| QG-092 | In `standalone`/`fullscreen` display modes, in-app back navigation exists for every non-root view | threshold | web.dev PWA app design (E3) | M (installed) |
| QG-093 | Network loss is communicated in-UI with a retry path and no uncaught errors (applies to every web app, see QG-071). **If the product claims offline support**, previously visited core views load offline and queued or refused actions are explained; an installable but online-only product may honestly refuse offline operation (e.g. real-time or regulated tasks) and is not failed for that | threshold | web.dev / MDN offline guidance (E3); PAT-PW-005 | M (offline) |
| QG-094 | A new version is applied without data loss or mid-task reload. The user is told about the update when it requires action, interrupts work, changes behavior, or is incompatible with queued data; silent application on next launch is acceptable for safe, non-disruptive updates | threshold | web.dev update guidance (E3); PAT-PW-012 | M |
| QG-095 | Notification permission requested only after a user action that implies intent, with an explanation; denial respected (no repeated prompting) | threshold | MDN, Using the Notifications API (E3); web.dev, push notification permissions UX (E4) | M |

---

## What is deliberately not a gate

Subjective preferences are not gates: hamburger vs tab bar, labels above vs beside fields, pagination vs infinite scroll, use of a FAB, dark mode availability, animation style. These are evaluated in the rubric with evidence-based reasoning, not pass/fail.

## Reporting

Report each checked gate as `pass`, `fail`, or `not verified` with the method used. For Core Web Vitals (QG-080…082) report mobile and desktop segments separately and say whether the data is field (real users) or lab. Never report `pass` on the strength of an automated check alone for gates marked `M` or `AT`; report `not verified (automated check passed)`.
