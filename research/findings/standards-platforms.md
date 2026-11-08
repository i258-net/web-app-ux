# Standards and platform conventions

Research working material for assignment **SP**, accessed **2026-11-08**. This file separates normative WCAG requirements from informative W3C guidance and Apple/Material platform conventions. It is not a claim of legal compliance: WCAG becomes a legal or contractual obligation only through the applicable law, policy, or agreement.

**80 findings:** 32 E1 entries covering the 32 requested WCAG success criteria plus SC 1.3.5 in the redundant-entry entry; 14 E4 entries (5 mobile guidance, 9 APG patterns); 34 E3 entries (18 Apple, 16 Material). Finding text is paraphrased except short labels and exact numerical/unit strings. Interpretation is synthesis, not an additional source requirement.

WCAG source version: W3C Recommendation **12 December 2024**. The fetched WCAG2Mobile publication is a **6 May 2025 Group Draft Note**, not a completed Recommendation. APG keyboard patterns are informative guidance. Apple content was read through its official Markdown representations. Material content was read from the published JSON payloads used by the fetched site, version `2026-10-13_06-10-19`; payload version is retrieval provenance, not the publication date of each claim.

## Normative WCAG 2.2 requirements

### F-SP-01: 1.3.4 Orientation — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#orientation
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** View and operation must not be restricted to one display orientation, such as portrait or landscape, unless that orientation is essential.
- **Interpretation:** Keep tasks usable after rotation and window changes.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Adaptive layout; orientation

### F-SP-02: 1.4.3 Contrast (Minimum) — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#contrast-minimum
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Text and images of text require at least 4.5:1 contrast; large-scale text requires at least 3:1. There is no contrast requirement for inactive-component text, purely decorative text, text invisible to everyone, text within a picture containing significant other visual content, or text in logos or brand names. The normative large-scale definition is at least 18 point, or 14 point bold, or an equivalent size for CJK fonts.
- **Interpretation:** Test actual foreground/background combinations in every supported appearance.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** Apple’s current contrast table uses different size/weight wording; see Disagreements.
- **Candidate knowledge targets:** Text contrast; themes

### F-SP-03: 1.4.4 Resize Text — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#resize-text
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Except for captions and images of text, text must support resizing without assistive technology up to 200 percent with no loss of content or functionality.
- **Interpretation:** Allow enlargement and let containers grow.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Zoom; typography

### F-SP-04: 1.4.10 Reflow — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#reflow
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Content must retain information and functionality without two-dimensional scrolling at a width equivalent to 320 CSS pixels for vertically scrolling content, or a height equivalent to 256 CSS pixels for horizontally scrolling content. Parts requiring a two-dimensional layout for meaning or use are excepted.
- **Interpretation:** Treat 320 CSS px as a reflow test condition, not a prescribed responsive breakpoint.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** Material’s dp breakpoints serve a different purpose.
- **Candidate knowledge targets:** Reflow; narrow viewports

### F-SP-05: 1.4.11 Non-text Contrast — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#non-text-contrast
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Visual information needed to identify UI components and their states requires at least 3:1 contrast against adjacent colors. Inactive components and unmodified user-agent appearances are excepted. Graphic parts needed for understanding also require at least 3:1 unless the particular presentation is essential.
- **Interpretation:** Check controls, state indicators, and meaningful graphics separately from text.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** Material distinguishes standalone and clustered containers; WCAG tests the visual information required for identification.
- **Candidate knowledge targets:** Control contrast; states

### F-SP-06: 1.4.12 Text Spacing — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#text-spacing
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** For markup supporting these properties, applying all of the following without changing other style properties must cause no loss of content or functionality: line height at least 1.5 times font size; paragraph spacing at least 2 times font size; letter spacing at least 0.12 times font size; word spacing at least 0.16 times font size. Languages/scripts without a listed property need satisfy only their applicable properties.
- **Interpretation:** These are override-tolerance test values, not a requirement that every design use those defaults.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Typography; resilient containers

### F-SP-07: 1.4.13 Content on Hover or Focus — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Additional content shown on hover or focus must be dismissible without moving pointer or focus, hoverable when hover triggers it, and persistent until the trigger is removed, the user dismisses it, or the information becomes invalid. Dismissibility is excepted when it communicates an input error or does not obscure/replace content. Unmodified user-agent-controlled additional content is excepted from the criterion.
- **Interpretation:** Implement tooltips and hover panels for keyboard users as well as pointer users.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Tooltips; popovers

### F-SP-08: 2.1.1 Keyboard — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#keyboard
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** All functionality must work through a keyboard interface without timing requirements on individual keystrokes. The exception concerns underlying functions whose input depends on the movement path rather than only endpoints.
- **Interpretation:** A touch-first interaction still needs a keyboard-operable route when the function is not inherently path-dependent.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Keyboard access; input independence

### F-SP-09: 2.1.2 No Keyboard Trap — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#no-keyboard-trap
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** When a keyboard interface can move focus into a component, a keyboard interface must also move it away. If exiting requires more than unmodified arrow/Tab keys or another standard exit method, users must be told the exit method.
- **Interpretation:** A modal can contain Tab navigation while open if users have a keyboard way to close it.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Focus management; dialogs

### F-SP-10: 2.1.4 Character Key Shortcuts — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#character-key-shortcuts
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** A shortcut consisting only of letters, punctuation, numbers, or symbols must either be switchable off, remappable to include at least one non-printable key, or active only while its UI component has focus.
- **Interpretation:** Scope or configure single-letter application shortcuts.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Keyboard shortcuts; voice input

### F-SP-11: 2.2.1 Timing Adjustable — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#timing-adjustable
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** For each content-set time limit, provide one of: turn it off beforehand; adjust it beforehand across a range at least ten times the default; or warn and allow at least 20 seconds for a simple extension action, with at least ten extensions. Exceptions cover unavoidable real-time-event limits, essential limits whose extension invalidates the activity, and limits longer than 20 hours.
- **Interpretation:** Audit sessions and timed actions for an applicable option or a documented exception.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** A Material snackbar duration is not a blanket WCAG timing exception.
- **Candidate knowledge targets:** Timeouts; session recovery

### F-SP-12: 2.4.3 Focus Order — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#focus-order
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Where sequential navigation is possible and navigation sequences affect meaning or operation, focusable components must receive focus in an order that preserves meaning and operability.
- **Interpretation:** Check focus order after responsive rearrangement, not only visual order.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Focus order; responsive composition

### F-SP-13: 2.4.7 Focus Visible — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#focus-visible
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Every keyboard-operable interface must have a mode of operation in which the keyboard focus indicator is visible.
- **Interpretation:** Keep a clear visible indicator on custom interactive components.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** The numerical area/contrast requirement of 2.4.13 is AAA, not part of this AA criterion.
- **Candidate knowledge targets:** Focus indicators

### F-SP-14: 2.4.11 Focus Not Obscured (Minimum) — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** When a UI component receives keyboard focus, author-created content must not hide it entirely.
- **Interpretation:** Check sticky bars, overlays, and responsive sheets against focused controls.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** This minimum does not require that every part remain visible.
- **Candidate knowledge targets:** Focus visibility; sticky UI

### F-SP-15: 2.4.13 Focus Appearance — AAA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#focus-appearance
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** When keyboard focus is visible, an indicator area must be at least the area of a 2 CSS pixel thick perimeter of the unfocused component/subcomponent, with at least 3:1 contrast between the same pixels in focused and unfocused states. Exceptions: the user agent determines an indicator the author cannot adjust; or neither the indicator nor its background color is author-modified.
- **Interpretation:** Specify indicator area and state-change contrast together; a literal 2 CSS px outline is one possible implementation.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** AAA enhanced requirement; do not label it an AA minimum.
- **Candidate knowledge targets:** Focus indicators; enhanced accessibility

### F-SP-16: 2.5.1 Pointer Gestures — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#pointer-gestures
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Functions using multipoint or path-based gestures must also work with a single pointer without a path-based gesture, unless the multipoint/path gesture is essential.
- **Interpretation:** Provide simple controls for functions otherwise exposed through pinch or drawn gestures.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Gesture alternatives

### F-SP-17: 2.5.2 Pointer Cancellation — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#pointer-cancellation
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** For single-pointer functions, satisfy at least one: do not execute any part on the down-event; complete on the up-event with a way to abort beforehand or undo afterward; reverse the down-event outcome on the up-event; or show that down-event completion is essential.
- **Interpretation:** Design activation so users can recover from an unintended press.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Pointer activation; cancellation

### F-SP-18: 2.5.3 Label in Name — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#label-in-name
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** For a UI component with a visible text or image-of-text label, its accessible name must contain that visible text.
- **Interpretation:** Use matching visible and programmatic names so speech commands correspond to what people see.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Accessible naming; voice control

### F-SP-19: 2.5.4 Motion Actuation — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#motion-actuation
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Device-motion or user-motion functions must also work through UI components, and motion responses must be disableable to prevent accidental activation. Exceptions cover accessibility-supported motion interfaces and motion essential to the function where alternatives would invalidate the activity.
- **Interpretation:** Do not make shake or tilt the sole path to an ordinary command.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Motion alternatives

### F-SP-20: 2.5.5 Target Size (Enhanced) — AAA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#target-size-enhanced
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Pointer targets must be at least 44 by 44 CSS pixels. Exceptions: an equivalent link/control on the same page is at least 44 by 44 CSS pixels; the target is within a sentence or block of text; unmodified user-agent sizing; or a presentation essential to conveying the information.
- **Interpretation:** 44×44 CSS px is an enhanced web target requirement, with its own exceptions.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** Same number as Apple’s 44 pt default, but different units and authority; no spacing exception in this AAA criterion.
- **Candidate knowledge targets:** Target size; enhanced accessibility

### F-SP-21: 2.5.7 Dragging Movements — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#dragging-movements
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Every function operated by dragging must also be achievable with a single pointer without dragging, unless dragging is essential or the user agent determines the function and the author does not modify it.
- **Interpretation:** Add tap/click alternatives for reorder, movement, and drag-only controls. Keyboard support alone does not satisfy the single-pointer alternative.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Drag alternatives; reorder

### F-SP-22: 2.5.8 Target Size (Minimum) — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#target-size-minimum
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Pointer targets must be at least 24 by 24 CSS pixels, subject to exactly five exceptions. Spacing: for each undersized target, a 24 CSS pixel diameter circle centered on its bounding box must not intersect another target or the corresponding circle of another undersized target. Equivalent: the same function is available through another control on the same page that satisfies this criterion. Inline: the target occurs in a sentence or its size is constrained by the line-height of non-target text. User Agent Control: sizing is determined by the user agent and not author-modified. Essential: the presentation is essential or legally required for the conveyed information.
- **Interpretation:** Test target geometry rather than just icon size; spacing is a geometric alternative, not a universal 24 px gap.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** 24×24 CSS px AA is a conformance floor with exceptions; Material 48dp and Apple control guidance are platform recommendations.
- **Candidate knowledge targets:** Target size; target spacing

### F-SP-23: 3.2.1 On Focus — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#on-focus
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Receiving focus must not itself initiate a change of context.
- **Interpretation:** Do not navigate or submit just because a control receives keyboard focus.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Predictability; focus

### F-SP-24: 3.2.2 On Input — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#on-input
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Changing a component setting must not automatically change context unless the user was advised of that behavior before using the component.
- **Interpretation:** Make consequential automatic navigation predictable before selection.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Forms; predictable interaction

### F-SP-25: 3.2.6 Consistent Help — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#consistent-help
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** If repeated across pages in a set, human contact details, human contact mechanisms, self-help options, and fully automated contact mechanisms must occur in the same relative order to other page content unless the user initiates a change.
- **Interpretation:** Keep repeated help placement/order consistent within corresponding responsive presentations; this does not require adding a help mechanism.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Help; navigation consistency

### F-SP-26: 3.3.1 Error Identification — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#error-identification
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** When an input error is automatically detected, identify the erroneous item and describe the error to the user in text.
- **Interpretation:** Do more than change a border color.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Form errors

### F-SP-27: 3.3.2 Labels or Instructions — A

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#labels-or-instructions
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Provide labels or instructions when content requires user input.
- **Interpretation:** Make field purpose and required input understandable before submission.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Form labels; instructions

### F-SP-28: 3.3.3 Error Suggestion — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#error-suggestion
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** For automatically detected input errors, provide known correction suggestions unless doing so would jeopardize security or the purpose of the content.
- **Interpretation:** Give actionable recovery guidance where a correction is known.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Error recovery

### F-SP-29: 3.3.4 Error Prevention (Legal, Financial, Data) — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** For pages causing legal commitments or financial transactions, modifying/deleting user-controllable stored data, or submitting user test responses, satisfy at least one: reversible submissions; input checked for errors with an opportunity to correct; or a way to review, confirm, and correct before final submission.
- **Interpretation:** Match safeguards to the consequence; this criterion does not require a confirmation dialog for every action.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** Apple’s restraint on alerts is compatible with reversible or checked submissions.
- **Candidate knowledge targets:** Destructive actions; consequential submissions

### F-SP-30: 3.3.7 Redundant Entry — A; 1.3.5 Identify Input Purpose — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#redundant-entry; WCAG 2.2, 1.3.5 — https://www.w3.org/TR/WCAG22/#identify-input-purpose
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** 3.3.7 (A): information already entered by or provided to the user that must be entered again in the same process must be auto-populated or available for selection. Exceptions: essential re-entry, security needs, or information no longer valid. Separately, 1.3.5 (AA): the purpose of each field collecting user information must be programmatically determinable when its purpose is in the specified Input Purposes list and the technology supports identifying the expected meaning of form input data.
- **Interpretation:** Reuse existing information and provide field semantics for supported personal-data purposes. Autofill is an implementation choice; these two criteria have different scopes.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Autofill; data minimization; input semantics

### F-SP-31: 3.3.8 Accessible Authentication (Minimum) — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** No authentication step may require a cognitive function test, such as password recall or puzzle solving, unless that step offers a non-cognitive alternative, assistance for completing the test, object recognition, or recognition of non-text content previously supplied by the user to the site.
- **Interpretation:** Permit mechanisms such as password-manager use and paste to reduce memory/transcription burden.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** The object-recognition and personal-content exceptions belong to the minimum criterion; do not generalize this as a prohibition of every CAPTCHA.
- **Candidate knowledge targets:** Authentication; password managers

### F-SP-32: 4.1.3 Status Messages — AA

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/#status-messages
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** In markup-language content, status messages must be programmatically determinable through roles or properties so assistive technologies can present them without receiving focus.
- **Interpretation:** Announce asynchronous results and errors without moving focus just to expose a message.
- **Applies to:** All responsive web apps and PWAs; touch / pointer / keyboard / AT as relevant to the criterion; general web content.
- **Generalizability:** high — normative web requirements independent of device type.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Live regions; asynchronous feedback

## Informative W3C mobile application guidance

### F-SP-33: WCAG2Mobile is informative draft application guidance

- **Source:** WCAG2Mobile — https://www.w3.org/TR/wcag2mobile-22/
- **Publisher:** W3C
- **Published/updated:** 2025-05-06 (Group Draft Note)
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** The publication covers WCAG 2.2 A/AA application to native, mobile web, and hybrid apps on phones/tablets. It does not create requirements, change WCAG, cover AAA, supply implementation techniques, or provide guidance for wearables/laptops. It maps web pages to screens and sets of pages to sets of screens. Its status is Group Draft Note, with many unfinished sections.
- **Interpretation:** Use normative WCAG directly for web conformance; use the mobile mapping as explanatory material. It is not an alternative mobile-only accessibility standard.
- **Applies to:** Mobile phones/tablets; touch / keyboard / pointer / AT; native, hybrid, and mobile web contexts as stated.
- **Generalizability:** medium — informative draft guidance; version and platform limits matter.
- **Conflicts/tensions:** The assignment’s shorthand “Group Note” needs the draft qualification shown by the fetched publication.
- **Candidate knowledge targets:** Evidence hierarchy; mobile scope

### F-SP-34: Mobile touch/gesture guidance has both current mappings and older recommendations

- **Source:** WCAG2Mobile — https://www.w3.org/TR/wcag2mobile-22/; Mobile Accessibility mapping — https://www.w3.org/TR/mobile-accessibility-mapping/
- **Publisher:** W3C
- **Published/updated:** 2025-05-06; 2015-02-26 (First Public Working Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** The 2025 background identifies 2.5.1, 2.5.4, 2.5.7, and 2.5.8 as relevant mobile additions; its 2.5.8 section repeats WCAG/WCAG2ICT text and ends in a work-in-progress placeholder. The 2015 predecessor recommends targets at least 9 mm high by 9 mm wide with inactive space around near-minimum targets, simple gestures, activation on release, and touch/keyboard alternatives to device manipulation.
- **Interpretation:** The older 9 mm recommendation must not be mislabeled as the current normative 24 CSS px criterion or a new requirement in the 2025 draft.
- **Applies to:** Mobile phones/tablets; touch / keyboard / pointer / AT; native, hybrid, and mobile web contexts as stated.
- **Generalizability:** medium — informative draft guidance; version and platform limits matter.
- **Conflicts/tensions:** 9 mm is an older physical-size recommendation; CSS px, pt, and dp are distinct units.
- **Candidate knowledge targets:** Touch targets; gesture alternatives

### F-SP-35: Mobile orientation and zoom remain accessibility concerns

- **Source:** WCAG2Mobile — https://www.w3.org/TR/wcag2mobile-22/; Mobile Accessibility mapping — https://www.w3.org/TR/mobile-accessibility-mapping/
- **Publisher:** W3C
- **Published/updated:** 2025-05-06; 2015-02-26
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** The 2025 orientation section says WCAG 1.3.4 applies and recommends all available orientations, including reversed portrait/landscape. Its resize section reproduces WCAG2ICT discussion of 200% enlargement and has an unfinished mobile-specific placeholder. The 2015 predecessor advises keeping pinch zoom available, avoiding restrictive user-scalable/maximum-scale viewport settings, and preferring text resizing with reflow to horizontal panning.
- **Interpretation:** Support both orientation changes and usable zoom; do not treat older viewport advice as a new normative rule in the 2025 Note.
- **Applies to:** Mobile phones/tablets; touch / keyboard / pointer / AT; native, hybrid, and mobile web contexts as stated.
- **Generalizability:** medium — informative draft guidance; version and platform limits matter.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Orientation; zoom; reflow

### F-SP-36: Reachability should accommodate varied grips and handedness

- **Source:** Mobile Accessibility mapping, section 3.5 — https://www.w3.org/TR/mobile-accessibility-mapping/
- **Publisher:** W3C
- **Published/updated:** 2015-02-26 (First Public Working Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** The predecessor recommends placing interactive elements within easy reach while the device is held in different positions. It cautions that one-handed optimization can benefit some people and disadvantage others because handedness and thumb movement differ; flexibility is the goal. It also states that mobile and desktop have no absolute divide: touch desktops, external keyboards/mice, and responsive windows overlap.
- **Interpretation:** Use reachable frequent controls while testing multiple grips; do not turn a single thumb-zone diagram into a universal requirement. This discussion was verified in the older document, not the unfinished 2025 mapping.
- **Applies to:** Mobile phones/tablets; touch / keyboard / pointer / AT; native, hybrid, and mobile web contexts as stated.
- **Generalizability:** medium — informative draft guidance; version and platform limits matter.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Reachability; multimodal design

### F-SP-37: Mobile entry guidance recommends matching keyboards and reducing typing

- **Source:** Mobile Accessibility mapping, sections 5.1–5.3 — https://www.w3.org/TR/mobile-accessibility-mapping/; WCAG2Mobile — https://www.w3.org/TR/wcag2mobile-22/
- **Publisher:** W3C
- **Published/updated:** 2015-02-26; 2025-05-06
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** The 2015 text recommends virtual keyboards appropriate to data type, including HTML5 field controls; it warns keyboard changes may confuse screen-reader users. It recommends choices and automatic entry of known date/time/location to reduce typing, and respecting platform zoom/font/caption features. The 2025 1.3.5 mapping discusses input-purpose semantics through WCAG2ICT but leaves mobile-specific guidance as a placeholder; neither fetched mobile document gives a specific HTML autocomplete-token recipe.
- **Interpretation:** Use suitable web input types/input modes and supported autofill semantics as implementation candidates; the specific autocomplete implementation is interpretation, not a quoted mobile-Note requirement. Keep external-keyboard and speech entry usable.
- **Applies to:** Mobile phones/tablets; touch / keyboard / pointer / AT; native, hybrid, and mobile web contexts as stated.
- **Generalizability:** medium — informative draft guidance; version and platform limits matter.
- **Conflicts/tensions:** Do not attribute detailed autofill advice or keyboard-occlusion rules to a draft section that does not supply them.
- **Candidate knowledge targets:** Forms; virtual keyboards; autofill

## Informative WAI-ARIA Authoring Practices patterns

### F-SP-38: APG menu/menubar keyboard model

- **Source:** WAI-ARIA Authoring Practices Guide: APG menu/menubar keyboard model — https://www.w3.org/WAI/ARIA/apg/patterns/menubar/
- **Publisher:** W3C WAI
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Tab/Shift+Tab enter or leave a menubar rather than traverse its items; opening a menu moves focus inside. Arrows navigate items/submenus, Enter opens or activates, and Escape closes and returns focus to the invoking context. Home/End are expected when arrow wrapping is absent; character type-ahead and some Space behaviors are optional. Disabled items can receive focus but cannot activate.
- **Interpretation:** Apply this composite-widget contract when building a menu/menubar; it is not automatically the contract for ordinary site-navigation links.
- **Applies to:** All web apps using the named custom ARIA widget; keyboard / AT, with touch support needing separate validation.
- **Generalizability:** high — widely applicable widget interaction guidance, informative rather than normative WCAG text.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Menus; composite keyboard navigation

### F-SP-39: APG tabs distinguish focus from activation

- **Source:** WAI-ARIA Authoring Practices Guide: APG tabs distinguish focus from activation — https://www.w3.org/WAI/ARIA/apg/patterns/tabs/
- **Publisher:** W3C WAI
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Tab enters the active tab and then exits the tablist. Horizontal Left/Right arrows move between tabs with wrapping; vertical lists use Up/Down. Space/Enter activates in manual mode; Home/End are optional. Automatic activation is recommended only when panels display without noticeable latency.
- **Interpretation:** Preload panels before choosing activation-on-focus, or use explicit activation.
- **Applies to:** All web apps using the named custom ARIA widget; keyboard / AT, with touch support needing separate validation.
- **Generalizability:** high — widely applicable widget interaction guidance, informative rather than normative WCAG text.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Tabs; focus versus selection

### F-SP-40: APG modal dialog contains focus and restores it

- **Source:** WAI-ARIA Authoring Practices Guide: APG modal dialog contains focus and restores it — https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- **Publisher:** W3C WAI
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Opening moves focus into the dialog; Tab and Shift+Tab cycle within it; Escape closes it. Initial focus depends on content and risk, including a static heading for long structured content or the least destructive choice. On close, return focus to the invoker unless it no longer exists or workflow makes another destination more logical. A visible close/cancel control is strongly recommended.
- **Interpretation:** Make background content inert and preserve a meaningful return location.
- **Applies to:** All web apps using the named custom ARIA widget; keyboard / AT, with touch support needing separate validation.
- **Generalizability:** high — widely applicable widget interaction guidance, informative rather than normative WCAG text.
- **Conflicts/tensions:** Containing Tab while a dismissible modal is open is compatible with WCAG No Keyboard Trap.
- **Candidate knowledge targets:** Modal dialogs; focus restoration

### F-SP-41: APG combobox preserves platform text editing

- **Source:** WAI-ARIA Authoring Practices Guide: APG combobox preserves platform text editing — https://www.w3.org/WAI/ARIA/apg/patterns/combobox/
- **Publisher:** W3C WAI
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Down Arrow enters an available popup; Escape dismisses it; Enter accepts the selected suggestion. Editable comboboxes support printable input and platform single-line editing keys. Up Arrow and Alt+Arrow options vary. In a listbox popup, arrows move the selected suggestion while DOM focus stays on the combobox via aria-activedescendant; popup options are excluded from the page Tab sequence.
- **Interpretation:** Avoid intercepting browser editing shortcuts; implement the contract for the actual popup type.
- **Applies to:** All web apps using the named custom ARIA widget; keyboard / AT, with touch support needing separate validation.
- **Generalizability:** high — widely applicable widget interaction guidance, informative rather than normative WCAG text.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Combobox; autocomplete

### F-SP-42: APG listbox separates navigation and selection

- **Source:** WAI-ARIA Authoring Practices Guide: APG listbox separates navigation and selection — https://www.w3.org/WAI/ARIA/apg/patterns/listbox/
- **Publisher:** W3C WAI
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Up/Down move option focus; selected or first options determine entry focus. Home/End are optional but strongly recommended beyond five options; type-ahead is recommended, especially beyond seven. Single-selection may follow focus. The recommended multiple-selection model lets Space toggle an option without holding modifiers; modifier-based alternatives are documented.
- **Interpretation:** Choose and consistently implement a selection model. A listbox is a selection widget, not a generic list of links and buttons.
- **Applies to:** All web apps using the named custom ARIA widget; keyboard / AT, with touch support needing separate validation.
- **Generalizability:** high — widely applicable widget interaction guidance, informative rather than normative WCAG text.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Listbox; selection

### F-SP-43: APG grid/data grid requires managed directional navigation

- **Source:** WAI-ARIA Authoring Practices Guide: APG grid/data grid requires managed directional navigation — https://www.w3.org/WAI/ARIA/apg/patterns/grid/
- **Publisher:** W3C WAI
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** An interactive grid is a composite with a managed Tab entry point and arrow-key cell navigation. For data grids, Home/End navigate within a row and Control+Home/End reach grid ends; Page Up/Down are optional. Layout grids allow additional wrapping options. Enter/F2 can enter cell interaction/editing, with Escape/F2 restoring navigation as appropriate; embedded arrow-key widgets need a deliberate mode switch.
- **Interpretation:** Use a semantic table for static data rather than taking on a grid’s keyboard contract unnecessarily.
- **Applies to:** All web apps using the named custom ARIA widget; keyboard / AT, with touch support needing separate validation.
- **Generalizability:** high — widely applicable widget interaction guidance, informative rather than normative WCAG text.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Data grid; editable tables

### F-SP-44: APG disclosure uses button activation

- **Source:** WAI-ARIA Authoring Practices Guide: APG disclosure uses button activation — https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/
- **Publisher:** W3C WAI
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Enter and Space toggle the disclosure content when the controlling element has focus. The pattern uses a button and aria-expanded, with aria-controls optionally relating it to content.
- **Interpretation:** Use a real button for an expandable region and keep state synchronized.
- **Applies to:** All web apps using the named custom ARIA widget; keyboard / AT, with touch support needing separate validation.
- **Generalizability:** high — widely applicable widget interaction guidance, informative rather than normative WCAG text.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Disclosure; expandable navigation

### F-SP-45: APG tooltip retains trigger focus

- **Source:** WAI-ARIA Authoring Practices Guide: APG tooltip retains trigger focus — https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- **Publisher:** W3C WAI
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Escape dismisses the tooltip; focus remains on its trigger. A focus-triggered tooltip disappears after blur; a pointer-triggered tooltip stays open while the pointer is over either trigger or tooltip. The pattern is explicitly work in progress and lacks task-force consensus.
- **Interpretation:** Do not put essential interactive content inside a tooltip; validate against WCAG 1.4.13 separately.
- **Applies to:** All web apps using the named custom ARIA widget; keyboard / AT, with touch support needing separate validation.
- **Generalizability:** high — widely applicable widget interaction guidance, informative rather than normative WCAG text.
- **Conflicts/tensions:** Informative draft pattern; WCAG 1.4.13 remains the normative obligation.
- **Candidate knowledge targets:** Tooltips

### F-SP-46: APG slider defines range keys

- **Source:** WAI-ARIA Authoring Practices Guide: APG slider defines range keys — https://www.w3.org/WAI/ARIA/apg/patterns/slider/
- **Publisher:** W3C WAI
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Right/Up increase by one step; Left/Down decrease. Home/End set the first/last allowed values. Page Up/Down optionally make a larger change. Focus is on the slider thumb; direction can be reversed when context makes that more intuitive. The pattern warns that some touch assistive technologies may not synthesize required key events.
- **Interpretation:** Test touch screen readers and offer an alternative numeric control when needed.
- **Applies to:** All web apps using the named custom ARIA widget; keyboard / AT, with touch support needing separate validation.
- **Generalizability:** high — widely applicable widget interaction guidance, informative rather than normative WCAG text.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Sliders; range input

## Apple Human Interface Guidelines — Apple-platform conventions

### F-SP-47: Apple layout follows available space and safe areas

- **Source:** Apple HIG: layout — https://developer.apple.com/design/human-interface-guidelines/layout.md
- **Publisher:** Apple
- **Published/updated:** layout: September 9, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** HIG recommends adapting to rotation, window resizing, displays, localization, and text size; using system safe areas, margins, and guides; and making decisions from compact/regular horizontal and vertical size classes rather than device type or orientation. Functionality should remain the same as size classes change, although its visibility can change. Safe areas exclude edge hardware and overlapping system/app views. No universal numerical compact/regular breakpoint is given here.
- **Interpretation:** For web apps, derive layouts from available viewport/container space and account for safe-area insets. Do not transplant a native size class or a television-specific safe-area measurement as a universal CSS breakpoint.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** Material supplies numerical dp classes; Apple’s fetched page uses system-provided categories.
- **Candidate knowledge targets:** Adaptive layout; safe areas; localization

### F-SP-48: Apple’s current control-size table distinguishes default and minimum

- **Source:** Apple HIG: inputs — https://developer.apple.com/design/human-interface-guidelines/inputs.md; Apple HIG: accessibility — https://developer.apple.com/design/human-interface-guidelines/accessibility.md
- **Publisher:** Apple
- **Published/updated:** inputs: not shown; accessibility: June 9, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** The Inputs page is a directory of input methods and gives no numerical hit-region rule. The current Accessibility page lists iOS/iPadOS default control size 44x44 pt and minimum control size 28x28 pt; macOS 28x28 pt default and 20x20 pt minimum; watchOS 44x44 pt default and 28x28 pt minimum. It recommends about 12 points padding around bezel controls and about 24 points around visible edges of controls without a bezel.
- **Interpretation:** Record 44×44 pt as the current iOS/iPadOS default, and 28×28 pt as that table’s minimum. The fetched pages do not justify calling 44 pt a universal minimum hit region. Favor comfortable targets and verify web conformance independently.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** Differs from common older “44 pt minimum” shorthand, WCAG’s CSS px requirements, and Material’s 48dp touch recommendation.
- **Candidate knowledge targets:** Touch targets; control density; spacing

### F-SP-49: Apple accessibility recommends contrast and redundant cues

- **Source:** Apple HIG: accessibility — https://developer.apple.com/design/human-interface-guidelines/accessibility.md
- **Publisher:** Apple
- **Published/updated:** accessibility: June 9, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** HIG recommends scalable text, VoiceOver descriptions, simple interactions, gesture alternatives, keyboard access, and information beyond color alone. Its Accessibility Inspector guidance table lists “Up to 17 pts / All / 4.5:1”, “18 pts / All / 3:1”, and “All / Bold / 3:1”. It says to check light/dark appearances and, if the default scheme lacks these minima, at least provide a higher-contrast scheme under Increase Contrast.
- **Interpretation:** Use native accessibility features as design inputs, but use WCAG’s exact size thresholds and contrast obligations for web conformance.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** The current table’s unrestricted Bold row and Increase Contrast fallback should not be substituted for WCAG 1.4.3; see Disagreements.
- **Candidate knowledge targets:** Accessibility; contrast; redundant feedback

### F-SP-50: Apple gestures should be familiar, responsive, and optional

- **Source:** Apple HIG: gestures — https://developer.apple.com/design/human-interface-guidelines/gestures.md
- **Publisher:** Apple
- **Published/updated:** gestures: October 28, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** HIG recommends familiar standard gestures, immediate predictive feedback, alternate inputs such as voice/keyboard/Switch Control, and custom gestures only when needed. Shortcut gestures supplement visible standard navigation, such as keeping Back while also supporting an edge swipe. Custom gestures should not conflict with system UI gestures.
- **Interpretation:** Treat gestures as accelerators with a discoverable accessible route to the same task.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Gesture alternatives; discoverability

### F-SP-51: Apple buttons communicate intent and protect against destructive defaults

- **Source:** Apple HIG: buttons — https://developer.apple.com/design/human-interface-guidelines/buttons.md
- **Publisher:** Apple
- **Published/updated:** buttons: December 16, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** HIG recommends a clear purpose through familiar icons or concise action labels; limiting prominent buttons to one or two per view; distinguishing preferred choices with style rather than size; and avoiding a destructive action as the primary/default button. In iOS/iPadOS, buttons can show an activity indicator and a changed label for a delayed action.
- **Interpretation:** Use explicit action names, restrained primary emphasis, and local pending feedback in a web button.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Buttons; primary actions; pending states

### F-SP-52: Apple top-level navigation adapts between tab bar and sidebar

- **Source:** Apple HIG: tab-bars — https://developer.apple.com/design/human-interface-guidelines/tab-bars.md; Apple HIG: sidebars — https://developer.apple.com/design/human-interface-guidelines/sidebars.md
- **Publisher:** Apple
- **Published/updated:** tab-bars: June 8, 2026; sidebars: June 8, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Tab bars navigate top-level sections rather than execute commands; labels aid navigation, overflow should be avoided, and unavailable content should be explained without hiding/disabling its tab. Current iPadOS HIG prefers a tab bar near the top and allows conversion to a sidebar for a wider set of destinations. For user-customizable tabs, aim for five or fewer default items. A permanent sidebar without conversion uses navigation split view. Sidebars generally expose no more than two hierarchy levels.
- **Interpretation:** Keep destinations stable and choose navigation from hierarchy and available space. Current iPad guidance is not a rule that every tablet must always use a sidebar.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** Material typically uses a leading navigation rail for larger widths; iPad’s tab-to-sidebar convention is platform-specific.
- **Candidate knowledge targets:** Primary navigation; adaptive sidebar

### F-SP-53: Apple toolbars include navigation-bar guidance

- **Source:** Apple HIG: toolbars — https://developer.apple.com/design/human-interface-guidelines/toolbars.md
- **Publisher:** Apple
- **Published/updated:** toolbars: December 16, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Toolbars group current-view actions, titles, and navigation controls. HIG recommends deliberate selection, logical grouping, and moving lower-priority items to overflow as width shrinks; customization can help iPad/Mac power users. A navigation toolbar at the top helps traverse hierarchy; in iOS this is sometimes called a navigation bar. Use standard Back and Close appearance/behavior consistently. The page’s change log says navigation-bar guidance was incorporated on June 9, 2025.
- **Interpretation:** Keep view actions separate from top-level destinations and preserve a recognizable back path.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** The separate navigation-bars Markdown URL returned 404; current guidance was verified in Toolbars.
- **Candidate knowledge targets:** Toolbars; navigation hierarchy

### F-SP-54: Apple modality needs a clear task and an exit

- **Source:** Apple HIG: modality — https://developer.apple.com/design/human-interface-guidelines/modality.md; Apple HIG: sheets — https://developer.apple.com/design/human-interface-guidelines/sheets.md
- **Publisher:** Apple
- **Published/updated:** modality: December 5, 2023; sheets: March 24, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Use modal presentation only for a clear benefit, keep the task short and focused, title it, provide an obvious dismiss route, and guard against losing user-generated content. Avoid simultaneous stacked modal flows. Sheets recommend a nonmodal alternative for supplementary content needed alongside the main task; pair Done with Cancel or a Back path. Resizable sheets use a grabber; iPhone medium detents support progressive disclosure, while iPad generally prefers page/form sheet styles.
- **Interpretation:** Provide explicit exits and data-loss handling; native sheet detents are a platform behavior to adapt thoughtfully on the web.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Modals; sheets; dismissal

### F-SP-55: Apple alerts are for important actionable interruptions

- **Source:** Apple HIG: alerts — https://developer.apple.com/design/human-interface-guidelines/alerts.md
- **Publisher:** Apple
- **Published/updated:** alerts: February 2, 2024
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Use alerts sparingly; do not alert just to convey passive information, on every startup, or for common destructive actions that are undoable. Use an alert for an uncommon irreversible destructive action when it can prevent an accident. Titles should explain the situation, with concise, neutral language and useful actions.
- **Interpretation:** Prefer inline feedback or undo for routine work, and reserve interruption for decisions with consequences.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** Compatible with WCAG 3.3.4, which permits reversibility or checking instead of mandatory confirmation dialogs.
- **Candidate knowledge targets:** Alerts; undo; destructive actions

### F-SP-56: Apple Dynamic Type requires layout adaptation

- **Source:** Apple HIG: typography — https://developer.apple.com/design/human-interface-guidelines/typography.md; Apple HIG: layout — https://developer.apple.com/design/human-interface-guidelines/layout.md; Apple HIG: accessibility — https://developer.apple.com/design/human-interface-guidelines/accessibility.md
- **Publisher:** Apple
- **Published/updated:** typography: December 16, 2025; layout: September 9, 2026; accessibility: June 9, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Use system text styles and implement equivalent scaling/accessibility behavior in custom fonts. Dynamic Type is a system setting on supported Apple platforms. HIG recommends layouts that grow, switch horizontal arrangements to vertical, expand row height, and support multiple lines rather than crop or overlap text. Accessibility guidance separately recommends enlargement of at least 200 percent, or 140 percent for watchOS.
- **Interpretation:** Use flexible web text/layout sizing and test browser text enlargement; native Dynamic Type support is not established merely by using CSS relative units.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Typography; scaling; resilient layout

### F-SP-57: Apple feedback should stay contextual and accessible

- **Source:** Apple HIG: feedback — https://developer.apple.com/design/human-interface-guidelines/feedback.md
- **Publisher:** Apple
- **Published/updated:** feedback: not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Provide feedback through multiple appropriate channels such as text, color, sound, and haptics; place status near the items it describes; reserve alerts for critical ideally actionable information. Warn about unexpected irreversible data loss. Confirm significant successes when useful and explain why commands cannot be carried out.
- **Interpretation:** Keep async state close to the affected action and expose it programmatically.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Feedback; status messages

### F-SP-58: Apple loading guidance favors early content and continued work

- **Source:** Apple HIG: loading — https://developer.apple.com/design/human-interface-guidelines/loading.md
- **Publisher:** Apple
- **Published/updated:** loading: June 9, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Show content or placeholders as soon as possible, replace placeholders as data arrives, and let people do other work while loading in the background. Communicate ongoing loading and expected duration. Use determinate progress when duration is known and indeterminate progress when it is not.
- **Interpretation:** Design usable partial/loading states rather than an empty blocked screen.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Loading; progress; skeletons

### F-SP-59: Apple onboarding teaches in context and postpones setup

- **Source:** Apple HIG: onboarding — https://developer.apple.com/design/human-interface-guidelines/onboarding.md
- **Publisher:** Apple
- **Published/updated:** onboarding: June 10, 2024
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Prefer learning by safe interaction and contextual tips near the relevant UI. Keep prerequisite onboarding brief; make separate tutorials optional when appropriate and available later. Postpone nonessential customization, provide sensible defaults, avoid making downloads block first use, and request permissions when relevant to the feature unless essential for initial operation.
- **Interpretation:** Give users a useful first task and progressively teach features.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Onboarding; permissions; progressive disclosure

### F-SP-60: Apple data entry minimizes typing and matches input semantics

- **Source:** Apple HIG: entering-data — https://developer.apple.com/design/human-interface-guidelines/entering-data.md; Apple HIG: virtual-keyboards — https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards.md
- **Publisher:** Apple
- **Published/updated:** entering-data: June 21, 2023; virtual-keyboards: June 9, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Obtain already available information from the system with appropriate permission; explain fields and supply reasonable defaults; prefer choices when useful; support paste and drag/drop; and validate entered values with timely feedback. Virtual-keyboard guidance recommends a keyboard matching data type and semantic content, and a Return label that describes an action such as Search. Entering data says not to prepopulate a password field and instead use entry, biometric, or keychain authentication.
- **Interpretation:** For web forms, use appropriate semantics and supported autofill while avoiding unnecessary typing. Do not interpret Apple’s password-field sentence as permission to block password managers or paste.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** Apple’s required-field example disables Next until completion; web UX must still make missing requirements discoverable. WCAG 3.3.8 remains applicable.
- **Candidate knowledge targets:** Forms; input types; autofill; validation

### F-SP-61: Apple search has a discoverable entry and clear scope

- **Source:** Apple HIG: searching — https://developer.apple.com/design/human-interface-guidelines/searching.md
- **Publisher:** Apple
- **Published/updated:** searching: June 8, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** If important, search should occupy a primary position; aim for one clear place to search app content, with local search when sections are distinct. Show current search scope through descriptive text, scope controls, or titles; use recent/predictive suggestions to reduce typing; consider privacy before exposing history and let people clear it.
- **Interpretation:** Make global versus local search and stored history understandable.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Search; scope; privacy

### F-SP-62: Apple menus prioritize meaningful labels and grouping

- **Source:** Apple HIG: menus — https://developer.apple.com/design/human-interface-guidelines/menus.md
- **Publisher:** Apple
- **Published/updated:** menus: June 8, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Use concise action labels, familiar symbols, important/frequent items early, and logical groups with separators. Keep related commands together even when frequency differs. Show unavailable commands as unavailable; a menu with all items unavailable should still open to reveal its commands. Add an ellipsis when completion needs more input or choices.
- **Interpretation:** Offer predictable, scannable commands without hiding the existence of temporarily unavailable functions.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Menus; action organization

### F-SP-63: Apple iPadOS combines inputs and resizable multitasking

- **Source:** Apple HIG: designing-for-ipados — https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados.md; Apple HIG: multitasking — https://developer.apple.com/design/human-interface-guidelines/multitasking.md; Apple HIG: pointing-devices — https://developer.apple.com/design/human-interface-guidelines/pointing-devices.md
- **Publisher:** Apple
- **Published/updated:** designing-for-ipados: not shown; multitasking: June 9, 2025; pointing-devices: October 28, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** iPad users may combine touch, virtual/physical keyboard, pointer, Pencil, and voice; viewing distance and input mode affect comfortable density. HIG recommends taking advantage of the large display, minimizing needless modal/full-screen transitions, placing controls within easy reach without obstructing content, and adapting to orientation, multitasking, and text-size changes. Pointer guidance supports predictable hover feedback and using the pointer to reveal minimized controls.
- **Interpretation:** Do not equate tablet with touch-only or fixed full-screen dimensions. No universal numerical thumb-reach boundary was verified in these pages.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Tablet UX; reachability; multitasking; mixed input

### F-SP-64: Apple desktop design supports efficient keyboard and pointer workflows

- **Source:** Apple HIG: designing-for-macos — https://developer.apple.com/design/human-interface-guidelines/designing-for-macos.md; Apple HIG: keyboards — https://developer.apple.com/design/human-interface-guidelines/keyboards.md; Apple HIG: pointing-devices — https://developer.apple.com/design/human-interface-guidelines/pointing-devices.md
- **Publisher:** Apple
- **Published/updated:** designing-for-macos: October 28, 2026; keyboards: June 9, 2025; pointing-devices: October 28, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Mac guidance recommends resizable/movable windows, high-precision pointer interaction, keyboard shortcuts and keyboard-only work, customizable toolbars, and using large displays to reduce nesting and modality without excessive density. The current October 28, 2026 update also describes touch as secondary to keyboard/pointer and recommends keeping layout/density stable while supporting larger hit targets or controls that expand on touch.
- **Interpretation:** Build efficient keyboard/pointer workflows across responsive widths rather than merely enlarging a phone layout. Validate current platform guidance instead of assuming device category determines input.
- **Applies to:** Apple-platform conventions; native iOS / iPadOS / macOS as specified; touch / pointer / keyboard / AT.
- **Generalizability:** medium — authoritative for Apple experiences, transferable to web only with context and validation.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Desktop UX; keyboard efficiency; pointer precision

## Material Design 3 — design-system conventions

### F-SP-65: Material defines five width breakpoints in dp

- **Source:** Material Design 3: foundations/layout/breakpoints — https://m3.material.io/foundations/layout/breakpoints (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/16281dc1-7630-4e78-abaf-c9bc8be69663.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** The current page calls window size classes “breakpoints” and gives: Compact — Under 600dp; Medium — 600–839dp; Expanded — 840–1199dp; Large — 1200–1599dp; Extra-large — 1600dp+. These apply to Android and web. Layout changes consider available window space, ergonomics, and platform conventions. Compact margins are 16dp; medium/expanded leading/trailing margins and pane spacers are 24dp.
- **Interpretation:** Preserve the exact source units. Define an explicit web token/CSS mapping rather than silently relabeling every dp figure as CSS px.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** WCAG’s 320 CSS px is a conformance reflow width, not a competing layout breakpoint; Apple compact/regular classes have no numeric thresholds in the fetched HIG page.
- **Candidate knowledge targets:** Breakpoints; adaptive layout; spacing

### F-SP-66: Material feed layouts change column count with space

- **Source:** Material Design 3: foundations/layout/canonical-examples — https://m3.material.io/foundations/layout/canonical-examples (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/23b84814-755b-469b-83a9-771fe027b0c0.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** A feed supports browsing large amounts of content through a configurable grid of cards/lists, including variable proportions and sizes. Compact feeds stack full-width items vertically. Medium and wider layouts can add columns; expanded layouts usually increase their count. Size and position can convey relationships, and items should reflow on rotation, unfolding, or multi-window changes.
- **Interpretation:** Adapt content density and reading order alongside grid columns.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Feeds; responsive grids

### F-SP-67: Material list-detail keeps one or two visible panes

- **Source:** Material Design 3: foundations/layout/canonical-examples — https://m3.material.io/foundations/layout/canonical-examples (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/23b84814-755b-469b-83a9-771fe027b0c0.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Use list-detail for browsing items and their details, such as conversations, files, or albums. Compact shows either list or detail in one pane. Medium recommends one pane for dense content/deep focus but permits two for fast browsing. Expanded and larger use two panes. A medium two-pane layout can use bottom navigation or a modal rail to save horizontal space.
- **Interpretation:** Preserve selected-item context while switching between sequential and simultaneous presentations.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** List-detail; adaptive panes

### F-SP-68: Material supporting pane distinguishes primary and secondary content

- **Source:** Material Design 3: foundations/layout/canonical-examples — https://m3.material.io/foundations/layout/canonical-examples (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/23b84814-755b-469b-83a9-771fe027b0c0.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Supporting-pane layouts divide content into a primary area, typically about two-thirds of the window, and a secondary area meaningful in relation to it. For parent-child content use list-detail instead. Compact and medium place supporting content below the focus pane; a bottom sheet is a compact option. Expanded places a supporting pane of fixed 360 dp width at the leading or trailing side.
- **Interpretation:** Choose multi-pane composition from task relationships rather than filling empty width indiscriminately.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Supporting pane; progressive disclosure

### F-SP-69: Material states communicate interaction and can combine

- **Source:** Material Design 3: foundations/interaction/states — https://m3.material.io/foundations/interaction/states (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/b3339b30-4a6d-49b6-9a8b-8e581b2b1204.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** The page describes enabled, disabled, hover, focused, pressed, and dragged states, consistent state application, and combinations such as selection plus hover. State layers are semitransparent overlays; only one state layer applies at a time even when multiple logical states coexist. It calls for two visual indicators to support accessibility.
- **Interpretation:** Specify focus, hover, selected, pending/error, and disabled behavior explicitly in component design; do not rely solely on a subtle color overlay. Pending/error are additional implementation states, not claims that this six-state list defines them.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Interaction states; focus visibility

### F-SP-70: Material recommends 48dp touch targets and 8dp spacing

- **Source:** Material Design 3: foundations/designing — https://m3.material.io/foundations/designing (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/d352451b-8348-4816-abac-4d7983f72f88.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** For most platforms, consider touch targets at least 48 x 48dp, approximately 9mm; the page calls 7–10mm a recommended physical range. A 24 x 24dp icon can sit within a 48 x 48dp target. In most cases, 8dp or more between targets balances density/usability. It separately suggests pointer targets at least 44 x 44dp. Its cross-reference to iOS says 44 x 44dp, which is the Material page’s wording.
- **Interpretation:** Differentiate visible glyph, hit area, and spacing. Use Apple’s own pt figures when discussing Apple conventions instead of adopting Material’s iOS unit label.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** WCAG AA 24×24 CSS px and AAA 44×44 CSS px differ in unit, purpose, and exceptions; current Apple HIG distinguishes default/minimum control sizes.
- **Candidate knowledge targets:** Touch targets; spacing; input modes

### F-SP-71: Material accessibility contrast guidance follows WCAG-like ratios

- **Source:** Material Design 3: foundations/designing — https://m3.material.io/foundations/designing (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/d352451b-8348-4816-abac-4d7983f72f88.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** The page recommends at least 4.5:1 for small text and at least 3:1 for large text, defined there as 14 pt bold/18 pt regular and up, and graphics. Disabled states are exempt in this guidance. It differentiates clustered button containers, which should have 3:1 against the background, from standalone prominent components such as FAB containers, which it says do not benefit from that container/background contrast.
- **Interpretation:** Test readable labels/icons and the visual cues needed to recognize a control. A visually prominent FAB does not exempt its text or identifying graphics from WCAG requirements.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** Material’s container-specific treatment must be assessed against WCAG 1.4.11’s required identifying information rather than copied as a blanket FAB exemption.
- **Candidate knowledge targets:** Contrast; component boundaries

### F-SP-72: Material navigation changes with window size and Expressive version

- **Source:** Material Design 3: components/navigation-bar — https://m3.material.io/components/navigation-bar (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/9e4cdffa-f7fd-425f-9915-867aafbcc7d6.json); Material Design 3: components/navigation-rail — https://m3.material.io/components/navigation-rail (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/98fe42bd-9bb1-4307-9e92-e61e57c3e9da.json); Material Design 3: components/navigation-drawer — https://m3.material.io/components/navigation-drawer (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/d2a1a290-0db4-4622-8a4b-bd11b6a4ec8d.json); Material Design 3: foundations/layout/breakpoints — https://m3.material.io/foundations/layout/breakpoints (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/16281dc1-7630-4e78-abaf-c9bc8be69663.json)
- **Publisher:** Google Material Design
- **Published/updated:** May 2025 Expressive update shown on navigation component pages; breakpoint publication date not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Navigation bars support 3–5 stable equal-priority destinations in compact/medium windows. Rails support 3–7 destinations plus an optional FAB in medium through extra-large windows; collapsed rails sit at the leading edge. Current breakpoints favor bottom navigation in compact, rails in medium/expanded/larger, with task-specific medium two-pane exceptions. The drawer page retains baseline guidance: standard drawers for expanded/large/extra-large, primarily modal drawers for compact/medium. Its May 2025 notice says drawers are no longer recommended in M3 Expressive: use expanded navigation rails.
- **Interpretation:** Select one coherent primary navigation strategy for the adopted Material version; preserve destinations across responsive swaps. Medium is conditional, not a rigid bar-for-phone/rail-for-tablet taxonomy.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** The source retains baseline and Expressive guidance together, and some rail wording is internally overbroad. Expressive expanded rail replaces the older always-visible desktop drawer recommendation.
- **Candidate knowledge targets:** Adaptive navigation; rails; drawers

### F-SP-73: Material fields retain labels and explain errors near input

- **Source:** Material Design 3: components/text-fields — https://m3.material.io/components/text-fields (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/8741ef66-1a80-4b39-adb1-66bea5e6992f.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Text fields have filled/outlined variants and visible states. Label text identifies expected information, moves with field state, or can be supplied through a separate adjacent leading-aligned label. Supporting text provides guidance and error correction; errors remain below the field until fixed. Required fields use an asterisk next to the label with an explanation either in supporting text or at the start of the form. Keep labels/errors concise and actionable.
- **Interpretation:** Keep field identity available after entry, associate helper/error text programmatically, and reserve space for variable-length feedback.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Text fields; labels; validation

### F-SP-74: Material dialogs are interruptive single-task decisions

- **Source:** Material Design 3: components/dialogs — https://m3.material.io/components/dialogs (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/79c01ab5-d09a-4f6c-9aca-f76d310583bc.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Use dialogs sparingly for information or decisions that block normal operation, including high-risk confirmations; keep one task per dialog. Variants are basic and full-screen. Low/medium-priority information should use a less disruptive presentation such as a snackbar. Basic dialog container width is Min 280dp; Max 560dp.
- **Interpretation:** Choose a modal for a decision that warrants blocking, and make keyboard focus/dismissal comply with the web dialog pattern. The width range is a component specification, not a page breakpoint.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Dialogs; consequential decisions

### F-SP-75: Material web snackbars need persistent alternatives or actions

- **Source:** Material Design 3: components/snackbar — https://m3.material.io/components/snackbar (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/26cf2750-80f7-43f8-a155-834aa01276df.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Snackbars are minimally interruptive and displayed one at a time, with at most one action plus an optional close affordance. Non-action snackbars can auto-dismiss after 4–10 seconds depending on platform. On web, the same message must also appear through an accessible inline/near-action method, or the snackbar should be actionable and persist until acted on/dismissed. When it appears, announce its message without moving focus.
- **Interpretation:** Do not put the only recovery action or essential status inside a rapidly disappearing toast. Apply WCAG timing/status requirements to the actual implementation.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** The 4–10 seconds guidance is not a universal accessibility-safe timeout and does not override WCAG 2.2.1 or 4.1.3.
- **Candidate knowledge targets:** Snackbars; status messages; undo

### F-SP-76: Material bottom sheets supplement compact and medium content

- **Source:** Material Design 3: components/bottom-sheets — https://m3.material.io/components/bottom-sheets (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/aa6f9af2-d539-4b22-9af5-838e7cfc4a85.json)
- **Publisher:** Google Material Design
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Bottom sheets are for secondary/additional content in compact and medium breakpoints, not the main app content. Standard and modal variants differ by whether a scrim blocks underlying interaction; both are dismissible. The page specifies a maximum width of 640dp and an optional drag handle with an accessible 48dp hit target.
- **Interpretation:** Distinguish modal blocking from a panel that leaves the main task usable; add non-drag and keyboard ways to perform actions required for web accessibility.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Bottom sheets; modal versus nonmodal

### F-SP-77: Material FAB emphasizes the screen’s key action

- **Source:** Material Design 3: components/floating-action-button — https://m3.material.io/components/floating-action-button (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/1e52f150-575c-45fa-8f5f-75868c5ab068.json)
- **Publisher:** Google Material Design
- **Published/updated:** May 2025 Expressive update
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Use a FAB for the most common or important screen action, with a clear understandable icon and persistence while content scrolls. Current variants are FAB, medium FAB, and large FAB. The May 2025 Expressive update introduces medium sizing and no longer recommends the small FAB.
- **Interpretation:** Use a persistent key-action control only when the task hierarchy warrants it and ensure it does not obscure content or keyboard focus.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** A Material FAB is a design-system convention, not a universal requirement to put a floating action on every mobile screen.
- **Candidate knowledge targets:** Primary actions; FAB

### F-SP-78: Material menus temporarily expose contextual actions

- **Source:** Material Design 3: components/menus — https://m3.material.io/components/menus (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/24b60c3f-1ec7-48df-b175-0d8e011a8106.json)
- **Publisher:** Google Material Design
- **Published/updated:** November 2025 Expressive update
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Menus present a temporary set of actions; use a toolbar when the actions need to remain visible. Menus can originate from icon/split buttons and text fields; context menus apply to a particular element and often open through secondary click. The November 2025 update adds expressive vertical menus with grouping gaps, dividers, and refined submenus.
- **Interpretation:** Keep common high-priority actions discoverable and provide keyboard/touch routes to context actions.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Menus; contextual actions

### F-SP-79: Material lists optimize scanning and accessible actions

- **Source:** Material Design 3: components/lists — https://m3.material.io/components/lists (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/6d4033c2-f92c-4c43-b585-b3bce8468d48.json)
- **Publisher:** Google Material Design
- **Published/updated:** December 2025 Expressive update
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Order items logically, keep them short/scannable, and format icons, text, and actions consistently. The current page offers standard/segmented styles and flexible slots but warns that custom content must preserve accessibility, including targets at least 48x48dp. Single-action items activate with Space/Enter after keyboard focus. Swipable lists need an alternate route to hidden actions, such as a More control.
- **Interpretation:** Avoid densely nesting independently interactive controls inside a row; preserve access when reducing information at compact widths.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Lists; row actions; swipe alternatives

### F-SP-80: Material search changes presentation while preserving the query task

- **Source:** Material Design 3: components/search — https://m3.material.io/components/search (published content fetched: https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/22081e54-b56a-47b2-b137-9ba82953f05e.json)
- **Publisher:** Google Material Design
- **Published/updated:** February 2025 Expressive update
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Search supports queries, suggestions or results, and an optional emphasized global entry through a search app bar. Focused search can show history before typing, update suggestions/results during typing, or wait for submission. Compact defaults to full-screen results/suggestions; medium/expanded best use a docked presentation. Back releases focus, dismisses suggestions/results, and restores the original search-bar state.
- **Interpretation:** Preserve query and understandable scope across responsive presentation changes, and make suggestion navigation keyboard-accessible.
- **Applies to:** Material-based Android and responsive web experiences; phone / tablet / desktop; touch / pointer / keyboard / AT as relevant.
- **Generalizability:** medium — documented design-system guidance, not a universal web standard.
- **Conflicts/tensions:** None identified.
- **Candidate knowledge targets:** Search; suggestions; adaptive overlays

## Coverage and gaps

- **Successful document coverage: 56 distinct pages/documents.** W3C: 3 technical reports (WCAG 2.2, WCAG2Mobile, 2015 predecessor) plus 11 APG pages (home, patterns index, and nine requested patterns). Apple: 25 documents including the HIG index and Inputs directory. Material: 17 canonical pages including its home and the 16 content pages used here. Additionally fetched: 16 published Material JSON payloads and one runtime JavaScript asset used to identify published payloads and routes. Repeated fetches and HTML/Markdown representations of the same document are not counted as additional pages.
- **Two document paths failed with HTTP 404:** `https://developer.apple.com/design/human-interface-guidelines/navigation-bars.md` and `https://developer.apple.com/design/human-interface-guidelines/touchscreens.md`. These failed paths are not evidence citations. Navigation-bar material was verified in Toolbars, whose change log explicitly records that incorporation. The Inputs directory has no standalone touchscreens entry or numerical target rule; numerical control sizes were verified in Accessibility.
- **Retrieval limitations resolved:** Apple's HTML pages expose a JavaScript shell; its linked official Markdown was fetched successfully by direct HTTP after the web extraction service rejected the Markdown MIME type. Material HTML also exposes a JavaScript shell; all 16 relevant published payloads were successfully fetched from the official domain. Each Material Source field includes both the canonical page fetched and the content URL actually read. No browser interaction, rendered-page inspection, empirical usability test, or device validation was performed.
- **Normative scope:** every requested SC has a numbered finding with its level and requirement. F-SP-30 additionally records SC 1.3.5. Notes/techniques/Understanding material have not been promoted into E1 requirements. This is a selected UX-oriented extraction, not an exhaustive WCAG audit: media, flashing, semantics, bypass mechanisms, language, and other unlisted criteria still matter.
- **Mobile draft gaps:** much of the 2025 publication reproduces WCAG/WCAG2ICT and retains work-in-progress placeholders. Orientation has a concrete mobile recommendation. Detailed reachability, virtual-keyboard, and reduced-entry advice was verified separately in the older **26 February 2015 First Public Working Draft**, not attributed to the 2025 draft. Neither fetched mobile publication supplies a detailed HTML autocomplete-token recipe. No independently specified virtual-keyboard occlusion/viewport algorithm was verified there. This guidance is not a substitute for WCAG, platform accessibility APIs, or current browser testing.
- **APG:** all nine requested patterns were fetched and summarized. Optional key assignments and selection/activation variants remain optional. Tooltip is explicitly unfinished and lacks task-force consensus. The [patterns index](https://www.w3.org/WAI/ARIA/apg/patterns/) and [APG home](https://www.w3.org/WAI/ARIA/apg/) were both fetched.
- **Apple:** covered Layout/safe areas, Accessibility, Gestures, Buttons, Tab bars/Sidebars, Toolbars including Navigation bars, Modality/Sheets/Alerts, Typography/Dynamic Type, Inputs, Feedback, Loading, Onboarding, Entering data/Virtual keyboards, Searching, Menus, iPadOS/Multitasking/Pointing devices, and macOS/Keyboards. No universal numerical thumb-reach zone or CSS breakpoint was verified. The current control-size table distinguishes default and minimum; a generic “44 pt minimum hit region” was not verified in the current Inputs/Accessibility pages. Native conventions and APIs do not establish equivalent support in a PWA.
- **Material:** covered five breakpoints, adaptive layout, all three canonical layouts, states, accessibility/spacing/contrast, all three navigation components with Expressive caveats, fields, dialogs, snackbars, bottom sheets, FAB, menus, lists, and search. No data-table component appears in the published route inventory used by this version of M3; no M3 data-table page was available to extract. The verified route inventory is in the fetched official [runtime asset](https://m3.material.io/static/angular/main.de4ba8c67aed3c29.js). Static table/grid guidance here comes from APG and WCAG, not an invented M3 table specification.
- **Dates and evidence:** source-visible change-log dates or component-update dates are recorded where available; otherwise “not shown.” Copyright years, payload timestamps, and retrieval dates are not substituted for publication dates. No empirical effect sizes, studies, sample sizes, or conversion improvements are asserted.

## Disagreements

1. **Target size describes different kinds of claims, not interchangeable measurements.** WCAG 2.5.8 AA specifies **24 by 24 CSS pixels** with five exact exceptions; WCAG 2.5.5 AAA specifies **44 by 44 CSS pixels** with different exceptions and no spacing exception. Material generally recommends **48 x 48dp** touch targets and **8dp** separation, plus **44 x 44dp** pointer targets. The current Apple table calls **44x44 pt** the iOS/iPadOS default and **28x28 pt** the minimum. Treat WCAG as a conformance threshold (and a legal minimum only where applicable rules adopt it), and platform figures as their owners' size/comfort conventions. Keep units attached; do not assume that CSS px, native pt, dp, or millimeters are globally equivalent.
2. **Apple's current wording differs from common 44 pt minimum shorthand.** The fetched Accessibility table expressly labels its columns “Default control size” and “Minimum control size.” This research preserves that distinction rather than rewriting the source to match the assignment's expected example. Its padding recommendations do not mean every target needs a universal 12 pt or 24 pt edge-to-edge gap.
3. **Contrast ratios align more closely than their qualifications.** WCAG uses **4.5:1** ordinary text, **3:1** large-scale text (at least **18 point**, or **14 point bold**) and required non-text identification information. Material's large-text thresholds closely track that wording. Apple's fetched Inspector table says up to **17 pts: 4.5:1**, **18 pts: 3:1**, and **all bold: 3:1**, plus an Increase Contrast fallback when defaults lack contrast. The broad bold row/fallback is not the normative WCAG wording and should not relax web tests. Material's standalone-FAB-container discussion is likewise not a blanket exemption for labels or required identifying graphics.
4. **Reflow widths are not design breakpoints.** WCAG's **320 CSS pixels** width / **256 CSS pixels** height are conformance conditions, not recommended widths for switching navigation. Material's width classes are **Under 600dp**, **600–839dp**, **840–1199dp**, **1200–1599dp**, and **1600dp+**. Apple provides compact/regular size-class behavior without universal numerical CSS cutoffs in the fetched page. Build and test layouts against content, window space, zoom, and the selected platform conventions.
5. **Navigation conventions differ by platform and source version.** Current iPad HIG favors a top tab bar with optional sidebar conversion for more complex navigation; macOS favors window/sidebar conventions. Material uses compact bottom bars and wider-window rails, with conditional medium layouts. Its baseline drawer page remains published but the Expressive update recommends expanded rails instead. Even within Material, breakpoint, rail, and baseline drawer pages retain overlapping or overly broad sentences; preserve their version/context rather than synthesizing an unconditional rail/drawer rule.
6. **Short-lived feedback is conditional.** Material's **4–10 seconds** applies to non-action snackbar timing with platform qualifications; its web guidance requires another accessible inline message or an actionable persistent snackbar. That number alone establishes neither compliance with WCAG Timing Adjustable nor reliable AT announcement. Apple also reserves disruptive alerts for consequential, actionable situations. Pair timely feedback with recoverable actions and accessible status semantics.
7. **Conformance floors and interaction guidance solve different problems.** A visible focus indicator under AA 2.4.7 is not the same claim as AAA 2.4.13's **2 CSS pixel** perimeter-equivalent area and **3:1** state contrast. APG gives widget keyboard contracts; native HIG/Material appearance does not supply those semantics automatically. A dismissible modal's focus containment is compatible with No Keyboard Trap; a trap with no keyboard exit is not.
8. **Document maturity and mobile/desktop scope matter.** The 2025 mobile draft is unfinished, and the specific thumb-reach, virtual-keyboard, and physical-target advice comes from its 2015 predecessor. That predecessor rejects an absolute mobile/desktop divide. Apple and Material likewise support mixed input and resized windows. Mobile-first supports an adaptive starting point, not removal of desktop/keyboard capabilities.
