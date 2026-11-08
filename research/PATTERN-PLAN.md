# Pattern plan (orchestrator working document)

Authoritative catalog, fixed by the orchestrator. Writers create exactly these files in their assigned directory and do not add, rename, or renumber patterns without recording a proposed change at the bottom of this file.

Filename: `patterns/<scope>/<ID>-<slug>.md`.

## shared/ (PAT-SH)
| ID | Slug | Problem |
|---|---|---|
| PAT-SH-001 | navigation-wayfinding | Global navigation structure, current-location cues, breadcrumbs, depth |
| PAT-SH-002 | form-fundamentals | Field count, grouping, labels (placement, placeholders), required/optional marking, help text |
| PAT-SH-003 | validation-error-messages | When to validate (blur/submit/live), error message content and placement, summary vs inline |
| PAT-SH-004 | search | Search entry, autocomplete/suggestions, results, no-results recovery, scope |
| PAT-SH-005 | filtering-sorting | Filter UI, apply vs live update, showing active filters, sort controls, result counts |
| PAT-SH-006 | selection-bulk-actions | Single/multi select, selection state visibility, bulk action bars |
| PAT-SH-007 | lists-pagination-infinite-scroll | Pagination vs load-more vs infinite scroll, footers, position memory |
| PAT-SH-008 | menus-action-overflow | Action menus, overflow ("…"), labeling, dangerous items, icon-only buttons |
| PAT-SH-009 | feedback-system-status | Status visibility, toasts vs inline vs banners, success confirmation, progress |
| PAT-SH-010 | loading-states | Response-time limits, spinners vs skeletons vs progress bars, optimistic UI, perceived speed |
| PAT-SH-011 | destructive-actions-undo | Confirmation vs undo, proportional friction, irreversible actions |
| PAT-SH-012 | empty-states | First-use, no-results, cleared, error-empty; guidance and primary action |
| PAT-SH-013 | onboarding-first-use | Tours vs contextual help vs empty states; permission and sign-up sequencing |
| PAT-SH-014 | progressive-disclosure | Accordions, show-more, steppers/wizards, advanced settings |
| PAT-SH-015 | dialogs-modality | When to use modal dialogs, sheets, inline expansion; focus, dismissal, stacking |
| PAT-SH-016 | failure-recovery | Server/network failures, retry, preserving input, error pages, partial failure |

## mobile/ (PAT-MO)
| ID | Slug | Problem |
|---|---|---|
| PAT-MO-001 | touch-target-size-spacing | Target sizes and spacing; WCAG min vs Apple/Material comfort |
| PAT-MO-002 | thumb-reach-primary-action | Reachability zones, primary-action placement, one-handed use |
| PAT-MO-003 | bottom-vs-top-navigation | Tab bars vs top bars vs hamburger drawer; destination count; labels |
| PAT-MO-004 | virtual-keyboards-input-types | inputmode/type/autocomplete/enterkeyhint, keyboard-aware layout, obscured fields |
| PAT-MO-005 | mobile-form-optimization | Single column, step splitting, autofill, minimizing typing, address/payment specifics |
| PAT-MO-006 | gesture-discoverability | Hidden gestures, redundancy with visible controls, teaching gestures |
| PAT-MO-007 | swipe-and-drag-on-touch | Swipe actions, swipe to dismiss, drag reordering on touch; conflicts with scroll and browser gestures |
| PAT-MO-008 | compact-density-truncation | Density, truncation, line clamping, horizontal carousels, "see all" |
| PAT-MO-009 | safe-areas-viewport | Safe-area insets, dynamic viewport units, browser chrome collapse, notches |
| PAT-MO-010 | scrolling-sticky-controls | Sticky headers/action bars, scroll performance, pull-to-refresh, scroll jank |
| PAT-MO-011 | bottom-sheets-mobile-modality | Bottom sheets, action sheets, full-screen dialogs on compact |

## desktop/ (PAT-DT)
| ID | Slug | Problem |
|---|---|---|
| PAT-DT-001 | wide-layout-density | Line length, max content width, multi-column, whitespace, density for experts |
| PAT-DT-002 | sidebar-hierarchical-navigation | Persistent sidebars, collapsing, mega menus, top vs left nav |
| PAT-DT-003 | hover-tooltips | Hover affordances, hover-revealed actions, tooltips, cursors |
| PAT-DT-004 | keyboard-navigation-shortcuts | Tab order, roving tabindex, skip links, shortcuts and their discoverability/conflicts |
| PAT-DT-005 | focus-selection-management | Focus after open/close/delete, selection models, keyboard selection |
| PAT-DT-006 | inline-editing | Edit-in-place, save/cancel semantics, autosave, optimistic update |
| PAT-DT-007 | data-tables-grids | Sorting, sticky headers, row selection, column management, responsive strategies for tables |
| PAT-DT-008 | contextual-actions-menus | Right-click menus, row hover actions, toolbars, redundancy for touch |
| PAT-DT-009 | drag-and-drop-accessible | Drag-and-drop with keyboard/button alternatives (WCAG 2.5.7) |
| PAT-DT-010 | multi-window-resize | Narrow desktop windows, side-by-side, multiple tabs, iPad multitasking |
| PAT-DT-011 | expert-workflows | Bulk operations, command palettes, defaults, recents, undo over confirm |

## responsive/ (PAT-RS)
| ID | Slug | Problem |
|---|---|---|
| PAT-RS-001 | navigation-transformation | How nav changes across viewports; parity of destinations |
| PAT-RS-002 | layout-reflow-canonical-layouts | List-detail, supporting pane, feed; reflow rules |
| PAT-RS-003 | content-prioritization | What goes first on compact; progressive enhancement of content, not removal of function |
| PAT-RS-004 | adaptive-density | Density tokens, spacing scales per window class, user density toggles |
| PAT-RS-005 | control-positioning | Where primary/secondary actions sit per viewport and input |
| PAT-RS-006 | breakpoints-window-classes | Breakpoint strategy, window size classes, content-driven breakpoints |
| PAT-RS-007 | container-vs-media-queries | When to use each; component-level responsiveness |
| PAT-RS-008 | responsive-typography-spacing | Fluid type, clamp, min sizes, line length control |
| PAT-RS-009 | input-detection-touch-vs-pointer | pointer/hover media features, runtime detection, hybrids |
| PAT-RS-010 | same-task-different-interaction | Date pickers, selects, filters, multi-select: modality-appropriate variants |
| PAT-RS-011 | orientation-foldables-hybrids | Orientation changes, foldables, touch laptops, tablets with keyboards |

## pwa/ (PAT-PW)
| ID | Slug | Problem |
|---|---|---|
| PAT-PW-001 | browser-vs-installed | Display modes, lost browser chrome, detection, parity |
| PAT-PW-002 | installation-prompts | Install criteria, custom prompts, timing, iOS add-to-home-screen |
| PAT-PW-003 | history-back-deep-links | History API/Navigation API, modal/back behavior, URL state, standalone back |
| PAT-PW-004 | reload-session-restoration | Reload, bfcache, scroll restoration, restoring in-progress state |
| PAT-PW-005 | connectivity-offline | Detecting and communicating offline, offline-capable views, graceful failure |
| PAT-PW-006 | caching-freshness | Caching strategies as UX: stale indicators, refresh affordances |
| PAT-PW-007 | sync-optimistic-conflicts | Queued actions, background sync, optimistic updates, conflicts |
| PAT-PW-008 | unsaved-changes | beforeunload constraints, drafts, autosave, in-app navigation guards |
| PAT-PW-009 | notifications-permissions | Permission timing, pre-prompts, badging, respecting denial |
| PAT-PW-010 | platform-capability-differences | Safari/iOS, Firefox, Chromium differences; feature detection; storage eviction |
| PAT-PW-011 | perceived-performance-vitals | CWV thresholds, skeletons, instant transitions, view transitions |
| PAT-PW-012 | app-updates | Service worker updates, notifying users, avoiding mid-task reload |

## Proposed changes (writers append here)

### From desktop writer (PAT-DT), 2026-11-08
- **Evidence-class reconciliation (no catalog change):** `research/findings/standards-platforms.md` tags WAI-ARIA APG findings F-SP-38…46 as E4, while `desktop-tablet-examples.md` (F-DX-21…24) and `sources/evidence-classes.md` treat APG as E3. PAT-DT-* cites APG as **E3**, except the Tooltip pattern (F-SP-45), which is cited as E4 because APG itself labels it work in progress. Proposal: the orchestrator settles on E3 for APG and updates F-SP-38…46.
- **Boundary note PAT-DT-005 ↔ PAT-SH-006:** PAT-DT-005 owns focus transitions and keyboard/pointer *selection models* (focus vs. selected vs. current, follow-focus vs. explicit activation). PAT-SH-006 owns selection UI and bulk-action bars. PAT-DT-005 is tagged for all viewports because focus loss is not desktop-specific. Consider moving it to `shared/` in a later revision.
- **Boundary note PAT-DT-007 ↔ responsive:** responsive table strategies (contained horizontal scroll, column priority, card stacking, list–detail) live in PAT-DT-007 as the brief instructed. PAT-RS-003 and PAT-MO-008 should link to it, not restate it.
- **Possible future pattern (not requested):** "multi-tab and multi-window data consistency", meaning the same record edited in two tabs or windows. It is touched on in PAT-DT-010 §6 and overlaps PAT-PW-007. Today it has no sourced evidence beyond F-DX-40/41, so it is not proposed for now.

### Orchestrator notes (2026-11-08)
- APG classification: `evidence-classes.md` governs. WAI-ARIA APG = **E3** (platform/standards-body authoring guidance, informative). standards-platforms.md F-SP-38…46 labeled it E4; the findings file is non-authoritative and is left as written, with this note as the resolution. Patterns use E3 for APG, E4 for APG patterns that APG itself marks work-in-progress.

### From mobile writer (PAT-MO), 2026-11-08
- **No catalog change.** All 11 PAT-MO files were written with the planned IDs and slugs.
- **New source not in findings: Hoober.** The brief and P-06 refer to Steven Hoober's grip observations, but no findings file cites them. I fetched and read both articles myself (verified 2026-11-08): https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php and https://www.uxmatters.com/mt/archives/2017/03/design-for-fingers-touch-and-people-part-1.php. PAT-MO-002 cites them as **E2 with limits**: non-random public observation, 2013 devices, no demographics, tablets excluded, and an editor's note saying the guidance was later revised. Proposal: add a `sources/` publisher entry for UXmatters/Hoober, and give the P-06 "Why it matters" bullet these URLs. That bullet currently names Hoober without a link. The 2017 article also states that users prefer to touch the centre of the screen, which qualifies the bottom-corner "thumb zone" shorthand in P-06.
- **web-platform.md arrived mid-task.** PAT-MO-004, 009, and 010 cite MDN pages that I fetched and marked "verified 2026-11-08". Their content matches F-WP-65…73. PAT-MO-009 also cites F-WP-71 (web.dev viewport units: virtual keyboards normally do not change viewport units).
- **Boundaries, for the PAT-SH and PAT-RS writers.** PAT-MO-005 defers field count, labels, and required marking to PAT-SH-002, and validation to PAT-SH-003. PAT-MO-011 defers modal focus and stacking rules to PAT-SH-015. PAT-MO-003 defers cross-viewport destination parity to PAT-RS-001. Placement on tablets and landscape is deferred to PAT-RS-005 and PAT-RS-011. Please keep those topics in your files so these links stay valid.
- **QG-053 vs WCAG 2.4.11.** The virtual keyboard is not author-created content, so 2.4.11 does not cover keyboard occlusion. QG-053 is correctly labelled a threshold, not a standard. Sticky bars covering focus are covered by QG-006.
- **Research gaps (E4-only sections).** The findings contain no evidence on these four topics: text line-clamping and ellipsis; horizontal carousels vs vertical lists; maximum sticky-chrome height or hide-on-scroll vs always-visible bars; and pull-to-refresh usability in web apps. Candidate future research tasks.

### From pwa/ writer (2026-11-08)

- **QG-090 wording conflicts with MDN.** QG-090 requires "a registered service worker", but MDN "Making PWAs installable" (https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable, F-WP-28/F-WP-37) states a service worker is not required for installability. Proposal: split it into QG-090a, "manifest meets the target browsers' install criteria (HTTPS; name/short_name; 192 and 512 px icons; start_url; display/display_override; prefer_related_applications false or absent)", and keep the service worker under QG-093 (offline). Alternatively, relabel QG-090 as this knowledge base's quality bar rather than the browser criterion. PAT-PW-002 records the conflict.
- **QG-095 source note.** The QG-095 row cites "NN/g permission requests (E4)", but no NN/g permission-request page appears in the findings. Pattern PAT-PW-009 instead cites MDN "Using the Notifications API" and web.dev `articles/push-notifications-permissions-ux` (both fetched and verified 2026-11-08). Proposal: update the source column, or add the NN/g page to the findings after fetching it.
- **Candidate gate (no new pattern):** "`beforeunload` handler is registered only while unsaved changes exist." This can be checked automatically and is supported by MDN (F-WP-61). It could fold into QG-062, which already says "(and only then)".
- **Research gaps to fill:** a Background Sync browser-compat snapshot, and a Badging API compat matrix (MDN says "limited availability" only). PAT-PW-007 and PAT-PW-010 avoid claiming either.

### From shared writer (PAT-SH), 2026-11-08
- **No catalog change.** All 16 PAT-SH files were written with the planned IDs and slugs. Every cited URL appears in `research/findings/`; no new sources were fetched.
- **Possible future shared pattern (not requested): "commit boundaries".** The choice between an explicit Save, autosave, an Apply step, and a step's Continue is spread across four patterns today: PAT-SH-002 §9, PAT-SH-005 (Apply vs live filtering), PAT-DT-006 (inline save/cancel), and PAT-PW-008 (drafts). Baymard F-NB-59 vs F-NB-60 shows that the right boundary depends on the task. A single shared pattern would stop the four from drifting apart. Hold until the evidence covers autosave directly; no finding tests autosave.
- **Boundary notes.** PAT-SH-016 owns general server and network failure, retry, partial failure, session expiry, and error pages; it points to PAT-PW-005 for offline detection and messaging and to PAT-PW-007 for conflicts. PAT-SH-012 owns the four empty causes. PAT-SH-004 and PAT-SH-005 link to it for no-results states rather than restating it. PAT-SH-015 holds modal focus and stacking rules, as PAT-MO-011 expects.
- **Research gaps (sections resting on E4/E5 or our inference).** These topics have no empirical evidence in the findings: empty-state design (PAT-SH-012 is E4 plus E5); spinner vs skeleton (PAT-SH-010); toast duration (only Material's 4–10 s convention); touch selection modes and long-press (PAT-SH-006); idempotent retry, backoff, and in-place re-authentication (PAT-SH-016); and floating labels (PAT-SH-002). Candidate future research tasks.

### From responsive writer (PAT-RS), 2026-11-08
- **No catalog change.** All 11 PAT-RS files were written with the planned IDs and slugs.
- **New sources fetched and read (marked "verified 2026-11-08" in the patterns):** MDN `<input type="date">` (https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date), MDN `<select>` (https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select), and MDN `PointerEvent.pointerType` (https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/pointerType). Proposal: add them to `sources/` publisher files and to `research/findings/web-platform.md` as new findings so other writers can cite them.
- **Proposed gate wording (QG-042):** clarify that `pointer`/`hover`/`any-*` report *capabilities*, not the input currently in use, and that event `pointerType` is the per-interaction signal. As written, "input modality detected at runtime" could be read as endorsing media features as current-input detectors. PAT-RS-009 carries the corrected reading.
- **Proposed gate (candidate QG-054, threshold):** "Changing window class, orientation, or posture mid-task preserves form input, selection, open panes, and scroll position." This is now a criterion in PAT-RS-002, PAT-RS-010, and PAT-RS-011 but has no gate. It is backed by Android resizability guidance (E3) and WCAG 1.3.4 only for orientation.
- **Boundary notes.** PAT-RS-009 is the single home of the "width ≠ input modality" thesis; other patterns link to it. PAT-RS-004 owns density *variation* (space axis vs input axis, user toggles); PAT-DT-001 owns expert wide-layout density and prose measure; PAT-RS-008 owns fluid type and links PAT-DT-001 for measure. PAT-RS-006 states that WCAG 1.4.10's 320/256 CSS px values are conformance test conditions, not breakpoints, and records the 1dp → 1 CSS px mapping as a repository convention.
- **Research gaps (thin evidence).** No empirical (E2) evidence covers: modality-specific control variants (PAT-RS-010: date pickers, comboboxes vs full-screen lists, reorder controls); density settings (PAT-RS-004); action placement on wide web layouts (PAT-RS-005); container vs media queries (PAT-RS-007, E3/E4 only, and container-query browser support was not verified in the findings); and foldable/hinge-aware web layouts (PAT-RS-011, where segment queries are experimental per MDN). Candidate research tasks: an MDN compat check for container queries; a fetch of the WCAG Understanding 1.4.10 page for the 1280 px / 400 % rationale; and native date-input accessibility evidence.
