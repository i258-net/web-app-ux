---
id: RUBRIC-DIMENSIONS
title: Evaluation dimensions and behavioral anchors
type: rubric
status: active
updated: 2026-11-08
---

# Evaluation dimensions

Ten dimensions, each with a five-level scale. Levels are **behavioral anchors**: descriptions of what an evaluator observes, not adjectives. Score what you observed; mark what you could not observe as *insufficient evidence* (see `scoring.md`).

Levels (shared across dimensions):

| Level | Name | Meaning |
|---|---|---|
| 1 | Failing | Users cannot complete core tasks, or a blocking defect exists for a supported device or input |
| 2 | Weak | Core tasks completable but with significant friction, errors, or exclusion of some users |
| 3 | Adequate | Tasks work; conventional patterns applied; noticeable rough edges remain |
| 4 | Strong | Tasks are efficient and comfortable on every evaluated device; good patterns consistently applied |
| 5 | Exemplary | Beyond strong: anticipates context, reduces effort measurably, handles edge cases gracefully |

Each dimension below lists: what it covers, the **device-contextual criteria** (how the same dimension is examined on compact touch, expanded pointer, transitions, and PWA), the anchors, the principles and patterns it draws on, and what each evaluation method can verify.

---

## D-01 Task effectiveness and efficiency

**Covers:** Can the primary tasks be completed? How many steps, decisions, and inputs does each take relative to the minimum? Are frequent tasks fast and infrequent ones guided?

**Device context:**
- *Compact touch:* steps per task given one-handed use; primary action reachable; no reliance on precision.
- *Expanded pointer/keyboard:* frequent tasks have accelerators (shortcuts, bulk actions, inline edit); density supports scanning without hunting.
- *Transitions:* a task started on one viewport can be finished after resizing or on another device without loss.
- *PWA:* tasks survive reload, back navigation, and short offline periods.

**Anchors:**
1. A primary task cannot be completed on a supported device, or requires workarounds (zooming, external tools).
2. Tasks completable but with redundant steps, repeated data entry, or unclear completion state.
3. Tasks completable with no more than a few steps beyond the minimum the task requires (count: fields, screens, confirmations); defaults sensible; some redundant confirmations or detours.
4. Step count matches the minimum for the task on every evaluated context; defaults correct for most users; frequent tasks have at least one accelerator (shortcut, bulk action, recents) on pointer/keyboard; mobile flows contain only the inputs the task needs.
5. As 4, and the system removes steps the user would otherwise repeat (prefill from known data, remembered choices), an interrupted task can be resumed where it was left, and the evaluator could not identify a removable step.

**Draws on:** P-01, P-07, P-14. Patterns: `PAT-SH-*` forms and selection, `PAT-DT-*` expert workflows, `PAT-PW-*` session restoration.

**Verifiable by:** running app and prototype (step counts, completion); user study (actual completion and time); screenshots only partially (step count inference).

---

## D-02 Information architecture and navigation

**Covers:** Content grouping matches users' mental model; labels are understandable; users always know where they are, where they can go, and how to get back.

**Device context:**
- *Compact:* navigation surfaces (tabs, drawer, hub-and-spoke) expose top-level destinations without hiding the primary ones; back behavior is predictable.
- *Expanded:* persistent navigation (sidebar, top nav) shows hierarchy and current location; breadcrumbs or equivalent for deep hierarchies.
- *Transitions:* the same destinations exist on all viewports; nothing is reachable only on one device unless intentionally scoped.
- *PWA/web:* URLs are shareable and deep-linkable; browser back behaves as expected; in standalone mode, in-app back exists.

**Anchors:**
1. Users get lost; destinations missing on a device; back navigation breaks or exits the app unexpectedly.
2. Confusing labels or grouping; current location unclear; primary destinations hidden behind a menu on compact viewports without cause.
3. Conventional structure; location indicated; some labels jargon-heavy or hierarchy too deep.
4. Clear, shallow hierarchy; persistent orientation cues on every viewport; deep links and back work everywhere.
5. Navigation adapts to context (recent, frequent, role) without breaking consistency; cross-device continuity of place.

**Draws on:** P-03, P-04. Patterns: `PAT-SH-00x` navigation and wayfinding, `PAT-MO-*` bottom/top navigation, `PAT-DT-*` sidebar, `PAT-RS-001` navigation transformation, `PAT-PW-*` history and deep links.

**Verifiable by:** screenshots (structure, labels, location cues); running app (back behavior, deep links); user study (findability, tree tests).

---

## D-03 Interaction ergonomics and discoverability

**Covers:** Controls are easy to hit, reach, and recognize; the input modality in use is served well; affordances are visible; gestures have discoverable alternatives.

**Device context:**
- *Touch:* target size and spacing; thumb reach for primary actions; no hover-only functionality; gestures discoverable or redundant with visible controls.
- *Pointer:* hover states and cursors signal interactivity; tooltips available without being required; right-click and drag have visible equivalents.
- *Keyboard:* everything reachable; focus visible; logical order; shortcuts where frequent.
- *Hybrid (touch laptop, tablet with keyboard):* both modalities work simultaneously; the app does not assume one from viewport width.

**Anchors:**
1. Critical controls cannot be activated with a supported input (hover-only on touch, mouse-only drag, tiny targets).
2. Targets small or crowded; primary actions out of comfortable reach; affordances ambiguous.
3. Targets meet minimums; affordances conventional; a few gesture-only or hover-only conveniences without fallback.
4. Comfortable targets and spacing; primary actions placed for the modality; every gesture and hover has a visible alternative.
5. Every function is operable and comfortable with each supported input simultaneously (touch, pointer, keyboard on the same device), whether by one inclusive control or by capability-aware adaptation; expert and novice paths both discoverable.

**Draws on:** P-02, P-06. Patterns: `PAT-MO-*` targets, reachability, gestures; `PAT-DT-*` hover, pointer, keyboard; `PAT-RS-*` touch vs pointer affordances. Gates: QG target size, hover/focus content, pointer gestures, dragging.

**Verifiable by:** screenshots (visual size, placement, affordances); running app (hit testing, hover/touch behavior, keyboard reach); automated (target-size heuristics, focusability).

---

## D-04 Input and data-entry efficiency

**Covers:** Forms and other data entry minimize effort and error: right input types and keyboards, autofill, sensible defaults, clear labels, inline validation timed well, no redundant entry.

**Device context:**
- *Compact touch:* correct virtual keyboard per field; labels visible when keyboard is up; field focus not obscured; single-column; minimal typing.
- *Pointer/keyboard:* tab order logical; Enter submits predictably; paste and autofill work; dense multi-column layouts only when fields are related.
- *Transitions:* the same form keeps progress when viewport changes.
- *Web platform:* autocomplete tokens; browser password managers and payment autofill not blocked; data preserved across reload/back.

**Anchors:**
1. Fields unusable with a supported input; data lost on error or navigation; validation blocks correct input.
2. Wrong keyboards, missing or placeholder-only labels on required fields, premature or late validation, redundant entry, unclear requirements.
3. Visible labels, correct types, and validation present; some friction (generic error wording, extra fields, labels that disappear while typing on some fields).
4. Minimal fields; autofill and correct `inputmode`; validation on blur/submit with specific messages; progress preserved.
5. Prefill from context, smart formatting, accessible authentication alternatives, resumable multi-step entry.

**Draws on:** P-07, P-11. Patterns: `PAT-SH-*` forms, validation, error messages; `PAT-MO-*` keyboards and mobile forms; `PAT-DT-*` inline editing. Gates: labels/instructions, error identification and suggestion, redundant entry, accessible authentication.

**Verifiable by:** running app (keyboard types, autofill, validation timing); source inspection (attributes); screenshots (labels, layout); automated (label association).

---

## D-05 Visual hierarchy, readability, and craft

**Covers:** The most important content and actions are visually dominant; text is legible at the viewing distance and size; spacing, alignment, and typography are consistent; motion and decoration serve comprehension.

**Device context:**
- *Compact:* one clear primary action per screen; comfortable base size for handheld reading; hierarchy survives narrow width.
- *Expanded:* line lengths bounded; density increases without flattening hierarchy; whitespace used, not wasted.
- *Transitions:* hierarchy preserved across breakpoints (the primary action stays primary).
- *All:* respects reduced-motion preference; dark mode, if offered, maintains contrast.

**Anchors:**
1. Illegible text or broken layout that prevents reading or acting at a supported viewport; the primary action cannot be found without searching the screen.
2. Flat hierarchy, cramped or overlong lines, inconsistent spacing, decorative motion that distracts.
3. Clear enough hierarchy; readable; some inconsistency or over-dense/over-sparse regions.
4. Deliberate hierarchy at every viewport; bounded measure; consistent type scale; purposeful motion.
5. As 4, and the evaluator finds no screen where hierarchy, spacing, or type deviates from the system, and no decorative element that competes with the primary action or delays a task. (Distinctiveness is a craft judgment reported separately in prose, not a level criterion.)

**Draws on:** P-08, P-15. Patterns: `PAT-RS-*` typography, adaptive density, visual hierarchy; `PAT-DT-*` wide layouts. Gates: contrast, text resize, text spacing, reflow.

**Verifiable by:** screenshots (most of this); running app (resize, zoom, motion preference); automated (contrast).

---

## D-06 Content clarity and cognitive load

**Covers:** Words are plain and task-oriented; the amount of information per step matches the decision; progressive disclosure hides complexity until needed; the interface does not require memory across screens.

**Device context:**
- *Compact:* chunked steps; essential info before the fold of the first screen; disclosure or scrolling chosen by task (disclosure for selective reading, exposed content for comparison and reading in sequence).
- *Expanded:* more can be shown at once, but not everything; grouping and scanning aids.
- *All:* consistent terminology; recognition over recall; help where needed.

**Anchors:**
1. Users cannot understand what to do; jargon or missing information blocks tasks.
2. Dense walls of text or options; unclear next step; terminology inconsistent.
3. Understandable; some overload or hidden-but-needed information.
4. Plain language; right amount at each step; disclosure used well; consistent terms.
5. Anticipates questions; explains consequences at the point of decision; adapts verbosity to expertise.

**Draws on:** P-05, P-03. Patterns: `PAT-SH-*` progressive disclosure, empty states, onboarding.

**Verifiable by:** screenshots and content review; user study (comprehension); not by automation.

---

## D-07 Feedback, errors, and recovery

**Covers:** Every action gets timely, proportional feedback; system status is visible; errors are prevented where possible, explained in plain language, and recoverable; destructive actions are reversible or confirmed proportionally.

**Device context:**
- *Compact:* feedback visible near the action and not hidden by keyboard; toasts not the only channel for important results.
- *Expanded:* feedback does not require hunting across a wide canvas; keyboard users get status announcements.
- *Web/PWA:* offline, failed save, and sync conflicts are communicated; undo favored over blocking confirmations.

**Anchors:**
1. Silent failures; data loss on error; destructive actions without protection; no loading indication for long waits.
2. Vague or technical errors; feedback delayed or misplaced; over-confirmation of trivial actions.
3. Errors identified and explained; loading indicated; confirmation present for destructive actions.
4. Specific, actionable messages at the point of error; undo or an equivalent recovery for most destructive actions; feedback for every action within the response-time limits, honest about whether a change is confirmed (optimistic or server-confirmed, as fits the stakes); status announced to AT.
5. Prevents errors through constraints and smart defaults; recovery paths preserve all user input; failure modes designed.

**Draws on:** P-10, P-11. Patterns: `PAT-SH-*` validation, error recovery, loading states, destructive actions, feedback; `PAT-PW-*` offline, unsaved changes. Gates: status messages, error identification, error prevention.

**Verifiable by:** running app (trigger errors, slow network); screenshots (presence of states, if captured); automated (live regions).

---

## D-08 Accessibility and adaptability

**Covers:** Works with keyboard, screen readers, switch access, voice control, magnification, and user preferences (text size, contrast, motion, orientation). Adapts to user settings rather than fighting them.

**Device context:**
- *Mobile:* orientation not locked; zoom not disabled; screen-reader gestures work; focus not obscured by keyboard or sticky bars.
- *Desktop:* full keyboard operability; visible focus; no traps; ARIA roles match behavior.
- *All:* contrast; reflow at 320 px; text spacing override; reduced motion honored.

**Anchors:**
1. Blocking failures: keyboard trap, unlabeled controls on critical paths, zoom disabled, contrast failures on primary content.
2. Multiple Level A/AA failures; partial screen-reader support; focus management absent after dynamic changes.
3. Mostly conformant; minor AA issues; some custom widgets with incomplete keyboard support.
4. Conforms to WCAG 2.2 AA where verified; focus managed; AT tested on at least one platform per device class.
5. Exceeds AA in meaningful ways (SC 2.5.5 target size enhanced, SC 2.4.13 focus appearance, SC 2.3.3 animation from interactions); AT tested on each supported platform; inclusive beyond conformance.

**Draws on:** P-12. Gates: the WCAG-derived QG set. Patterns: keyboard navigation, focus management, drag alternatives, text resize/reflow.

**Verifiable by:** automated (subset: contrast, names, roles, some structure); running app with AT (most); screenshots (very little: visible focus and contrast estimates only).

---

## D-09 Performance, resilience, and trust

**Covers:** Perceived and measured responsiveness; stability under slow or lost connectivity; honesty of UI (no dark patterns); privacy respected; permissions requested in context.

**Device context:**
- *Mobile:* mid-range device and throttled network baseline; loading states that preserve layout where the layout is known (skeleton or reserved space) and indicate progress otherwise; no layout shift under late-loading content.
- *Desktop:* heavy views (tables, dashboards) stay interactive; large uploads/downloads show progress.
- *PWA/web:* Core Web Vitals; offline fallback; permission prompts after user intent; install prompts not on first load.

**Anchors:**
1. Unusable on slow network or mid-range device; data loss on disconnect; deceptive patterns; permission prompts on arrival.
2. Long unexplained waits; layout shifts; connectivity failures surface as raw errors; unclear data use.
3. Acceptable speed; loading states present; offline handled with a message; permissions requested with minimal context.
4. Meets CWV "good" thresholds at p75 where measured; graceful degradation; contextual permission requests; transparent, reversible choices.
5. Resilient by design: work continues or queues safely through connectivity loss where the task allows, failures never lose user input, and defaults are honest and respectful.

**Draws on:** P-13, P-14. Patterns: `PAT-SH-*` loading states; `PAT-PW-*` offline, caching, notifications/permissions, performance. Gates: CWV thresholds (recommended), timing adjustable (standard).

**Verifiable by:** automated (CWV lab/field); running app with throttling; screenshots (no).

---

## D-10 Cross-device and platform appropriateness

**Covers:** Each device gets an experience designed for it, not a shrunk or stretched copy; platform conventions are respected without being universalized; the same task is achievable everywhere with modality-appropriate interactions; consistency where it matters, adaptation where it helps.

**Device context:**
- *Compact vs expanded:* layouts, navigation, and controls differ purposefully; nothing is desktop-only by accident.
- *Hybrid inputs:* touch laptops and tablets with keyboards are not broken by width-based assumptions.
- *PWA:* installed mode respects platform window behavior; browser mode does not duplicate browser chrome.
- *Continuity:* state and place carry across devices where the product supports multiple devices.

**Anchors:**
1. A supported device class is effectively unsupported (desktop is a phone layout stretched, or mobile is a desktop layout shrunk).
2. Works everywhere but one device class is clearly an afterthought; input assumptions tied to width.
3. Responsive and functional on all devices; adaptations generic; some convention mismatches.
4. Purposeful adaptation per device; hybrid inputs work without width-based assumptions; conventions respected per platform without forcing them elsewhere.
5. As 4, and the evaluator finds no task that is slower or less comfortable on one supported device than the device's constraints require; a task begun on one device can be continued on another without re-entering data (where multi-device use is supported).

**Draws on:** P-09, P-06, P-01. Patterns: all of `PAT-RS-*`; `PAT-PW-*` browser vs installed.

**Verifiable by:** running app at multiple viewports and with multiple inputs; screenshots at several viewports (partially); user study across devices.
