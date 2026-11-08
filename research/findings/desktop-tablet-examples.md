# Desktop and tablet interaction patterns, continuity, and shipped examples

Research assignment: DX. Access date: 2026-11-08. This is working research material, not authoritative guidance.

Part A contains 52 findings. Part B contains 10 E5 observations from public Mobbin pages. There are 62 findings in total: E1 5, E2 7, E3 27, E4 13, E5 10.

Evidence is classified by the claim supported, not by publisher reputation. NN/g recommendations without reported supporting test observations are E4 here. Apple, Carbon, Atlassian, Android/Material, React, MDN, Microsoft, and nonnormative ARIA APG guidance are E3 conventions or implementation guidance, not universal usability results. The Media Queries source is explicitly a Candidate Recommendation Draft. WCAG success criteria are E1. No sample sizes or outcome percentages have been inferred.

## Part A — Desktop, tablet, and continuity

### F-DX-01: Constrain prose measure even on a wide monitor

- **Source:** Readability: The Optimal Line Length — https://baymard.com/research-articles/line-length-readability
- **Publisher:** Baymard Institute
- **Published/updated:** 2022-05-10
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard recommends 50–75 characters per line for body text and reports that overly long product descriptions discouraged reading during e-commerce testing.
- **Interpretation:** Set a font-relative maximum prose width; verify the actual rendered measure rather than treating a CSS ch value as an exact character count.
- **Applies to:** all; touch / pointer / keyboard / AT; reading, with empirical examples from e-commerce
- **Generalizability:** medium — readability transfers plausibly, but the reported tests concern commerce and do not establish an optimum for every language or task.
- **Conflicts/tensions:** F-DX-02: prose measure is not a maximum width for every component.
- **Candidate knowledge targets:** typography; readable measure; wide-screen content

### F-DX-02: Give tables room instead of applying the prose width cap everywhere

- **Source:** Data table — Guidelines — https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines
- **Publisher:** IBM Carbon Design System
- **Published/updated:** 2026-09-30
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Carbon recommends giving data tables ample main-content space and considering the greatest width on the page to avoid cramped, truncated data.
- **Interpretation:** Use separate width constraints for prose and comparison surfaces.
- **Applies to:** desktop / tablet; pointer / keyboard / AT; enterprise tables
- **Generalizability:** medium — an enterprise design-system convention, not a universal page-width experiment.
- **Conflicts/tensions:** F-DX-01: wider tables and narrower prose serve different tasks.
- **Candidate knowledge targets:** content width; comparison layouts

### F-DX-03: Whitespace should express relationships

- **Source:** Layout — https://developer.apple.com/design/human-interface-guidelines/layout.md
- **Publisher:** Apple Human Interface Guidelines
- **Published/updated:** 2026-09-09
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Apple recommends alignment, indentation, and grouping through negative space, containers, or separators to communicate relationships and hierarchy.
- **Interpretation:** On wide screens, organize related controls into meaningful groups instead of distributing them evenly across unused space.
- **Applies to:** desktop / tablet / mobile; all input; Apple native layout guidance
- **Generalizability:** medium — grouping principles transfer to web; Apple materials and native layout APIs remain platform-specific.
- **Conflicts/tensions:** F-DX-05: visual breathing room must coexist with useful density.
- **Candidate knowledge targets:** whitespace; visual hierarchy; grouping

### F-DX-04: Use multiple panes to keep hierarchy and details together

- **Source:** Split views — https://developer.apple.com/design/human-interface-guidelines/split-views.md
- **Publisher:** Apple Human Interface Guidelines
- **Published/updated:** 2025-06-09
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Apple describes split views for adjacent hierarchy levels and recommends persistently highlighting the selections that lead to the detail view.
- **Interpretation:** A wide list–detail layout can preserve context and reduce repeated navigation; collapse it into a logical sequence when narrow.
- **Applies to:** desktop / tablet; touch / pointer / keyboard / AT; native split views
- **Generalizability:** medium — suitable for hierarchical tasks, not all content pages.
- **Conflicts/tensions:** F-DX-35: simultaneous comparison can be lost when panes or tables become isolated cards.
- **Candidate knowledge targets:** list–detail; multi-column layout; selection context

### F-DX-05: Density is a task choice, not a device label

- **Source:** Data table — Guidelines — https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines
- **Publisher:** IBM Carbon Design System
- **Published/updated:** 2026-09-30
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Carbon supplies multiple row sizes, ranging from highly dense layouts to spacious rows supporting easier interaction and multiline content.
- **Interpretation:** Offer a suitable default and consider a remembered density preference for repetitive expert work.
- **Applies to:** desktop / tablet; pointer / touch / keyboard; enterprise tables
- **Generalizability:** medium — the variants are documented conventions; their pixel sizes are not proven web-wide optima.
- **Conflicts/tensions:** F-DX-03: density must retain grouping; F-DX-47: width does not identify input precision.
- **Candidate knowledge targets:** density; expert workflows; display settings

### F-DX-06: Choose left navigation when the information architecture needs room

- **Source:** Left-Side Vertical Navigation on Desktop: Scalable, Responsive, and Easy to Scan — https://www.nngroup.com/articles/vertical-nav/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2021-05-16
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends visible, left-aligned vertical navigation for broad or growing hierarchies, avoiding short, vague labels forced into a horizontal bar.
- **Interpretation:** Choose navigation placement from category breadth and label clarity; a small stable set can still fit top navigation.
- **Applies to:** desktop; pointer / keyboard / AT; broad website and web-app navigation
- **Generalizability:** medium — a research-informed recommendation, not a controlled comparison for every application.
- **Conflicts/tensions:** F-DX-08: sidebars consume width and may need to collapse.
- **Candidate knowledge targets:** sidebar navigation; top versus left navigation

### F-DX-07: Grouped mega menus can expose lower levels effectively

- **Source:** Mega Menus Work Well for Site Navigation — https://www.nngroup.com/articles/mega-menus-work-well/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2017-03-26
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** NN/g explicitly reports user-testing support for mega menus that group many choices and let people see options together rather than remembering scrolled-away alternatives.
- **Interpretation:** Consider a grouped panel for a broad site hierarchy; do not equate it with displaying the entire information architecture.
- **Applies to:** desktop / tablet; pointer / touch / keyboard; large-site navigation
- **Generalizability:** medium — results concern navigation menus; implementation and available space matter.
- **Conflicts/tensions:** F-DX-09: a sidebar has different hierarchy limits; F-DX-11: hover needs intentional activation.
- **Candidate knowledge targets:** mega menus; navigation hierarchy

### F-DX-08: A sidebar needs both discoverability and an escape hatch

- **Source:** Sidebars — https://developer.apple.com/design/human-interface-guidelines/sidebars.md
- **Publisher:** Apple Human Interface Guidelines
- **Published/updated:** 2026-06-08
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Apple recommends allowing people to hide and reveal sidebars, avoiding default hiding, and considering automatic collapse as a Mac window becomes narrow.
- **Interpretation:** Expose navigation when space permits and provide a persistent, labeled way to restore a collapsed sidebar.
- **Applies to:** desktop / tablet; touch / pointer / keyboard; macOS and iPadOS sidebars
- **Generalizability:** medium — native convention; web controls must implement their own accessible state and behavior.
- **Conflicts/tensions:** F-DX-06: visibility improves access but competes with content space.
- **Candidate knowledge targets:** collapsible sidebars; narrow windows

### F-DX-09: A sidebar need not display the full tree

- **Source:** Sidebars — https://developer.apple.com/design/human-interface-guidelines/sidebars.md
- **Publisher:** Apple Human Interface Guidelines
- **Published/updated:** 2026-06-08
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Apple generally recommends no more than two sidebar hierarchy levels, using disclosure controls for extensive content and a content list for deeper hierarchies.
- **Interpretation:** Show the useful current branch and context; use another pane or destination for deeper levels.
- **Applies to:** desktop / tablet; pointer / touch / keyboard / AT; hierarchical native apps
- **Generalizability:** medium — the two-level recommendation is an Apple convention, not a universal limit on web trees.
- **Conflicts/tensions:** F-DX-07: mega menus can reveal multiple levels in a different navigation structure.
- **Candidate knowledge targets:** hierarchical navigation; progressive disclosure

### F-DX-10: Breadcrumbs express location, not browsing history

- **Source:** Breadcrumbs: 11 Design Guidelines for Desktop and Mobile — https://www.nngroup.com/articles/breadcrumbs/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2018-12-23; last reviewed 2026-09-01
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends hierarchical breadcrumbs as a supplement to global and local navigation, especially for direct arrivals on deep pages; flat or linear sites may not need them.
- **Interpretation:** Expose ancestor context for deep links without replacing sibling navigation or the browser Back action.
- **Applies to:** desktop / tablet / mobile; all input; hierarchical sites
- **Generalizability:** high — the distinction between location and history transfers broadly; exact breadcrumb presentation depends on width.
- **Conflicts/tensions:** F-DX-09: neither breadcrumbs nor sidebars require exposing every branch.
- **Candidate knowledge targets:** breadcrumbs; deep-link orientation

### F-DX-11: Immediate hover feedback differs from delayed disclosure

- **Source:** Timing Guidelines for Exposing Hidden Content — https://www.nngroup.com/articles/timing-exposing-content/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2015-01-11
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g distinguishes immediate feedback that a target is interactive from delayed disclosure of potentially disruptive hover content; merely crossing a target does not establish intent.
- **Interpretation:** Highlight controls promptly, but test dwell and pointer-path behavior for menus that cover content.
- **Applies to:** desktop / tablet; pointer; hover-triggered interfaces
- **Generalizability:** medium — practitioner timing guidance, not a universal measured delay for every control.
- **Conflicts/tensions:** F-DX-07: NN/g's mega-menu article gives a specific dwell example; generalize the intent principle cautiously.
- **Candidate knowledge targets:** hover affordances; menu activation

### F-DX-12: Hover-revealed row actions need focus and touch behavior

- **Source:** Data table — Guidelines — https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines
- **Publisher:** IBM Carbon Design System
- **Published/updated:** 2026-09-30
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Carbon defaults to persistent row overflow controls; its optional hover mode also reveals on focus and keeps controls persistent when hover is unsupported.
- **Interpretation:** Keep essential actions discoverable and verify touch and keyboard access independently.
- **Applies to:** desktop / tablet / mobile; pointer / touch / keyboard; tables
- **Generalizability:** medium — component behavior is a useful model, not evidence that hiding actions improves all tables.
- **Conflicts/tensions:** F-DX-13 and F-DX-47: hover availability cannot be assumed from width.
- **Candidate knowledge targets:** row actions; progressive disclosure; input parity

### F-DX-13: Tooltips supplement visible information

- **Source:** Tooltip Guidelines — https://www.nngroup.com/articles/tooltip-guidelines/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2019-01-27
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends brief, useful tooltips, excludes information essential to completing the task, and calls for both mouse-hover and keyboard-focus access.
- **Interpretation:** Keep requirements and primary instructions visible; provide a touch-appropriate disclosure for supplemental help.
- **Applies to:** desktop / tablet / mobile; pointer / keyboard / touch / AT; contextual help
- **Generalizability:** high — the access and memory problems apply broadly, although the article primarily addresses desktop tooltips.
- **Conflicts/tensions:** F-DX-12: hiding primary actions or meaning increases discovery cost.
- **Candidate knowledge targets:** tooltips; inline help; touch alternatives

### F-DX-14: Hover content has testable accessibility requirements

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** WCAG 2.2 SC 1.4.13 requires qualifying hover/focus content to be dismissible, hoverable, and persistent, subject to its stated exceptions.
- **Interpretation:** Test custom tooltips and submenus for pointer transfer, dismissal without losing focus, and continued visibility.
- **Applies to:** all; pointer / keyboard / AT; web content
- **Generalizability:** high — normative Level AA requirement within the criterion's scope.
- **Conflicts/tensions:** F-DX-11: dwell timing alone does not satisfy these requirements.
- **Candidate knowledge targets:** hover content; tooltip accessibility

### F-DX-15: Right-click menus are accelerators, not the only route

- **Source:** Contextual Menus: Delivering Relevant Tools for Tasks — https://www.nngroup.com/articles/contextual-menus/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2019-03-17
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends contextual actions relevant to the current target, visible menu signifiers, and another route to the same commands because hidden triggers may go undiscovered.
- **Interpretation:** Support right-click for efficiency alongside an accessible button or menu available to touch and keyboard users.
- **Applies to:** desktop / tablet / mobile; pointer / touch / keyboard / AT; object actions
- **Generalizability:** high — hidden-trigger discoverability applies broadly; exact gestures are platform-specific.
- **Conflicts/tensions:** F-DX-18: accelerators supplement the learnable interface.
- **Candidate knowledge targets:** context menus; overflow actions

### F-DX-16: Drag-and-drop needs signifiers and feedback through the whole action

- **Source:** Drag–and–Drop: How to Design for Ease of Use — https://www.nngroup.com/articles/drag-drop/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2020-02-23
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends recognizable drag cues, standard move/resize cursors, grabbed-object feedback, and previews of valid drop destinations; dragging can be imprecise or physically difficult.
- **Interpretation:** Design the before, during, and after states, including invalid destinations and clear completion feedback.
- **Applies to:** desktop / tablet; pointer / touch; moving, reordering, resizing
- **Generalizability:** high — the feedback model transfers broadly; cursor guidance applies only with pointers.
- **Conflicts/tensions:** F-DX-17: good dragging still needs a non-drag pointer alternative.
- **Candidate knowledge targets:** drag and drop; cursor affordances; feedback

### F-DX-17: A keyboard alternative alone does not satisfy the dragging criterion

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** WCAG 2.2 SC 2.5.7 requires dragging functionality to work with a single pointer without dragging, unless essential or an unmodified user-agent behavior.
- **Interpretation:** Provide click/tap operations such as Move to, Move up/down, or destination selection, alongside keyboard support.
- **Applies to:** all; pointer / touch; author-defined dragging
- **Generalizability:** high — normative Level AA requirement with explicit exceptions.
- **Conflicts/tensions:** F-DX-16: precise visual feedback is complementary, not a substitute.
- **Candidate knowledge targets:** non-drag alternatives; accessible reordering

### F-DX-18: Make shortcuts discoverable at the relevant action

- **Source:** Accelerators Maximize Efficiency in User Interfaces — https://www.nngroup.com/articles/ui-accelerators/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2024-10-18
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends optional accelerators for recurring tasks, including shortcut hints beside menu commands and contextual introductions rather than overwhelming newcomers.
- **Interpretation:** Let people learn shortcuts while using the visible workflow; keep a searchable reference for experts.
- **Applies to:** desktop / tablet; keyboard / pointer; repeated web-app tasks
- **Generalizability:** high — broad efficiency guidance, without a quantified speedup in this article.
- **Conflicts/tensions:** F-DX-20 and F-DX-21: discoverable shortcuts must also be safely scoped and conflict-aware.
- **Candidate knowledge targets:** keyboard shortcuts; progressive learning

### F-DX-19: Prioritize frequent tasks and preserve shortcut conventions

- **Source:** UI Copy: UX Guidelines for Command Names and Keyboard Shortcuts — https://www.nngroup.com/articles/ui-copy/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2019-03-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends observing frequent tasks before assigning shortcuts and avoiding reassignment of familiar commands or interference with accessibility shortcuts.
- **Interpretation:** Keep shortcut labels, meanings, and platform modifiers consistent; validate the actual browser and assistive-technology combinations.
- **Applies to:** desktop / tablet; keyboard / AT; command-heavy applications
- **Generalizability:** high — broad convention guidance, with platform-specific key choices.
- **Conflicts/tensions:** F-DX-21: browser, OS, and AT conflicts need explicit review.
- **Candidate knowledge targets:** shortcut design; command names

### F-DX-20: Single-character shortcuts require an escape from accidental activation

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** WCAG 2.2 SC 2.1.4 requires character-only shortcuts to be switchable off, remappable to include a non-printable key, or active only when the component has focus.
- **Interpretation:** Do not add global letter shortcuts without an appropriate user control or focus scope.
- **Applies to:** all; keyboard / speech input / AT; web shortcuts
- **Generalizability:** high — normative Level A requirement, retained from WCAG 2.1.
- **Conflicts/tensions:** F-DX-18: convenience does not override accidental-activation protection.
- **Candidate knowledge targets:** character shortcuts; keyboard accessibility

### F-DX-21: Audit shortcut conflicts across browser, operating system, and AT

- **Source:** Developing a Keyboard Interface — https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/
- **Publisher:** W3C WAI, ARIA Authoring Practices Guide
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** The APG explains that shortcut conflicts can block essential functions and recommends avoiding or mitigating collisions with OS, browser, and assistive-technology commands.
- **Interpretation:** Test a supported platform matrix and expose alternatives when a shortcut cannot be used.
- **Applies to:** desktop / tablet; keyboard / AT; custom web widgets
- **Generalizability:** high — established web keyboard conventions; APG is nonnormative, not itself WCAG.
- **Conflicts/tensions:** F-DX-19: familiar app shortcuts may still collide in a browser.
- **Candidate knowledge targets:** shortcut conflicts; platform conventions

### F-DX-22: Opening and closing a dialog is a focus transition

- **Source:** Dialog (Modal) Pattern — https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- **Publisher:** W3C WAI, ARIA Authoring Practices Guide
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** The APG modal-dialog pattern moves focus inside on opening, keeps Tab navigation within the dialog, and normally returns focus to the invoker on closing, with logical workflow exceptions.
- **Interpretation:** Choose initial focus deliberately; if the invoker disappears, move to the next meaningful task location.
- **Applies to:** all; keyboard / AT; web modal dialogs
- **Generalizability:** high — a widely adopted nonnormative interaction pattern; native dialogs may supply some mechanics.
- **Conflicts/tensions:** F-DX-23: destructive actions can invalidate the original focus target.
- **Candidate knowledge targets:** modal dialogs; initial focus; focus restoration

### F-DX-23: Deleting a focused item must not strand focus on the page body

- **Source:** Developing a Keyboard Interface — https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/
- **Publisher:** W3C WAI, ARIA Authoring Practices Guide
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** The APG identifies deletion and dialog closure as cases where removing the active element can lose focus, and gives moving focus to the following list item as a remedy.
- **Interpretation:** Define a next-item, previous-item, or empty-list control destination before implementing deletion.
- **Applies to:** desktop / tablet / mobile; keyboard / AT; mutable lists
- **Generalizability:** high — a general DOM focus failure; exact destination depends on task and remaining items.
- **Conflicts/tensions:** F-DX-28: optimistic removal and rollback also need a focus policy.
- **Candidate knowledge targets:** list deletion; focus recovery

### F-DX-24: Use composite-widget keyboard conventions deliberately

- **Source:** Developing a Keyboard Interface — https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/
- **Publisher:** W3C WAI, ARIA Authoring Practices Guide
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** The APG describes one tab stop per composite and roving tabindex: one child at 0, others at -1, with focus moved by navigation keys.
- **Interpretation:** Use this for appropriate grids, trees, toolbars, and tablists; do not impose it on ordinary document links or static tables.
- **Applies to:** all; keyboard / AT; composite web widgets
- **Generalizability:** high — documented web conventions; role-specific behavior must still be implemented.
- **Conflicts/tensions:** F-DX-31: selection and keyboard focus are distinct states.
- **Candidate knowledge targets:** roving tabindex; grids; keyboard navigation

### F-DX-25: Repeated desktop chrome needs a bypass route

- **Source:** Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/
- **Publisher:** W3C
- **Published/updated:** 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** WCAG 2.2 SC 2.4.1 requires a mechanism to bypass blocks repeated across pages.
- **Interpretation:** Provide a working skip-to-main link or another sufficient bypass mechanism so keyboard users need not traverse every sidebar on each page.
- **Applies to:** all; keyboard / AT; repeated web navigation
- **Generalizability:** high — normative Level A requirement; a skip link is one implementation, not the sole mandated technique.
- **Conflicts/tensions:** F-DX-06: persistent navigation should not become repeated keyboard overhead.
- **Candidate knowledge targets:** skip links; page landmarks; navigation efficiency

### F-DX-26: Inline editing needs a recognizable transition between reading and editing

- **Source:** Inline edit — https://developer.atlassian.com/platform/forge/ui-kit/components/inline-edit/
- **Publisher:** Atlassian Forge UI Kit
- **Published/updated:** 2025-07-18
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Atlassian's Inline edit switches a custom input between read and edit views on the same page and advises aligning the two views to avoid a jarring transition.
- **Interpretation:** Make the edit affordance and active edit state visible without shifting unrelated content.
- **Applies to:** desktop / tablet / mobile; pointer / touch / keyboard; Forge UI Kit inline editing
- **Generalizability:** medium — component guidance; not a comparison of inline editing against full-page forms.
- **Conflicts/tensions:** F-DX-27: compact appearance does not settle save semantics.
- **Candidate knowledge targets:** inline editing; edit mode; layout stability

### F-DX-27: Save and cancel semantics must survive blur

- **Source:** Inline edit — https://developer.atlassian.com/platform/forge/ui-kit/components/inline-edit/
- **Publisher:** Atlassian Forge UI Kit
- **Published/updated:** 2025-07-18
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Atlassian supplies confirm/cancel controls, recommends retaining them when unobstructed, and recommends keeping large text edits open on blur to avoid accidental saving or discarding.
- **Interpretation:** Specify Enter, Escape, blur, validation, and explicit save/cancel behavior; preserve unfinished long edits.
- **Applies to:** desktop / tablet / mobile; pointer / touch / keyboard / AT; inline fields
- **Generalizability:** medium — a documented component policy, not a universal mandate to save every field on blur.
- **Conflicts/tensions:** F-DX-28: local feedback must not imply an unconfirmed server save.
- **Candidate knowledge targets:** inline editing; save and cancel; draft preservation

### F-DX-28: Optimistic UI requires failure recovery

- **Source:** useOptimistic — https://react.dev/reference/react/useOptimistic
- **Publisher:** React documentation
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** React documents showing an optimistic value while an Action is pending; its optimistic-delete example restores a removed item and displays an error if deletion fails.
- **Interpretation:** For inline saves or bulk actions, distinguish pending from confirmed results and design rollback, retry, and focus recovery.
- **Applies to:** all; all input; asynchronous React interactions
- **Generalizability:** medium — implementation guidance, not empirical proof that optimistic updates suit irreversible or high-risk actions.
- **Conflicts/tensions:** F-DX-23: removing or restoring a focused item needs deliberate focus handling.
- **Candidate knowledge targets:** optimistic UI; asynchronous saves; error recovery

### F-DX-29: Sorting needs a persistent indication of the current order

- **Source:** Data table — Guidelines — https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines
- **Publisher:** IBM Carbon Design System
- **Published/updated:** 2026-09-30
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Carbon places sorting in column headers and distinguishes unsorted, ascending, and descending states, retaining an indicator on the sorted column.
- **Interpretation:** Expose sort state to assistive technology and keep keyboard activation available.
- **Applies to:** desktop / tablet; pointer / keyboard / AT; sortable tables
- **Generalizability:** medium — design-system convention; its hover-only unsorted cues need separate discoverability checks.
- **Conflicts/tensions:** F-DX-12: hover cues alone can obscure which columns are sortable.
- **Candidate knowledge targets:** table sorting; state visibility

### F-DX-30: Keep headers available during large-table comparisons

- **Source:** Data Tables: Four Major User Tasks — https://www.nngroup.com/articles/data-tables/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2022-04-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends frozen header rows and identifier columns when a table exceeds the screen, plus visual tracking cues to keep cell context clear.
- **Interpretation:** Test sticky regions at zoom and narrow widths so they preserve context without consuming the usable viewport.
- **Applies to:** desktop / tablet; pointer / keyboard / AT; large workplace tables
- **Generalizability:** medium — a research-informed recommendation, not a universal sticky-header experiment.
- **Conflicts/tensions:** F-DX-34: horizontal scrolling benefits from retained row identity.
- **Candidate knowledge targets:** sticky headers; frozen columns; comparison

### F-DX-31: Selection needs explicit controls and a partial-selection state

- **Source:** Data table — Guidelines — https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines
- **Publisher:** IBM Carbon Design System
- **Published/updated:** 2026-09-30
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Carbon uses row checkboxes for multiselection and a header checkbox with checked, unchecked, and indeterminate states.
- **Interpretation:** Keep selected, focused, expanded, and navigated rows visually and semantically distinct.
- **Applies to:** desktop / tablet; pointer / touch / keyboard / AT; selectable tables
- **Generalizability:** medium — established component convention; scope across pages needs an additional product rule.
- **Conflicts/tensions:** F-DX-24: focus movement alone must not silently imply selection.
- **Candidate knowledge targets:** row selection; select all; mixed states

### F-DX-32: Bulk actions deserve a clear selection mode

- **Source:** Data table — Guidelines — https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines
- **Publisher:** IBM Carbon Design System
- **Published/updated:** 2026-09-30
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Carbon reveals a batch-action bar for selected rows, offers cancellation, and disables per-row actions during batch mode.
- **Interpretation:** Show which records the action affects and provide a clear exit.
- **Applies to:** desktop / tablet; pointer / touch / keyboard / AT; repetitive table operations
- **Generalizability:** medium — enterprise component convention; not evidence for a universal batch-mode design.
- **Conflicts/tensions:** F-DX-45: recovery or specific confirmation becomes more important as operation scope grows.
- **Candidate knowledge targets:** bulk actions; selection mode; expert efficiency

### F-DX-33: Choose pagination strategy from the task, not a universal ranking

- **Source:** Infinite Scrolling, Pagination Or “Load More” Buttons? Usability Findings In eCommerce — https://www.smashingmagazine.com/2016/03/pagination-infinite-scrolling-load-more-buttons/
- **Publisher:** Smashing Magazine; Christian Holst, Baymard Institute
- **Published/updated:** 2016-03-01
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard's commerce testing favored Load more with lazy loading over pagination and unlimited scrolling; infinite scrolling encouraged broad scanning but reduced attention and could obstruct the footer.
- **Interpretation:** Treat this as product-discovery evidence. Operational grids needing stable ranges or direct page access may reasonably use pagination.
- **Applies to:** desktop / mobile / tablet; all input; e-commerce product lists
- **Generalizability:** medium — strong contextual evidence, weak grounds for a universal rule covering enterprise grids.
- **Conflicts/tensions:** Carbon F-DX-32's source separately documents table pagination; commerce browsing and record management have different needs.
- **Candidate knowledge targets:** Carbon documents pagination for operational tables, while this research concerns commerce browsing; the tasks need not share the same loading strategy.

### F-DX-34: A horizontally scrolling table must remain keyboard reachable

- **Source:** A Responsive Accessible Table — https://adrianroselli.com/2017/11/a-responsive-accessible-table.html
- **Publisher:** Adrian Roselli
- **Published/updated:** 2017-11-02; updated 2026-10-06
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Roselli presents a named, focusable scrolling wrapper as a responsive-table fallback, allowing keyboard users to reach and scroll content that exceeds the viewport.
- **Interpretation:** Keep the surrounding page responsive and make overflow apparent; test current browser and AT behavior.
- **Applies to:** desktop / tablet / mobile; pointer / touch / keyboard / AT; wide HTML tables
- **Generalizability:** medium — a worked accessibility implementation with browser-dependent behavior, not a comparative usability study.
- **Conflicts/tensions:** F-DX-35: scrolling preserves a grid, while stacked layouts alter comparison behavior.
- **Candidate knowledge targets:** responsive tables; horizontal overflow; keyboard scrolling

### F-DX-35: Stacking table rows into cards can change both meaning and comparison

- **Source:** A Responsive Accessible Table — https://adrianroselli.com/2017/11/a-responsive-accessible-table.html
- **Publisher:** Adrian Roselli
- **Published/updated:** 2017-11-02; updated 2026-10-06
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Roselli demonstrates a narrow stacked-table presentation with cell labels and warns that changing table display properties can remove table semantics in accessibility APIs.
- **Interpretation:** Use stacking only when record-by-record reading fits the task; retain labels and verify semantics with supported AT.
- **Applies to:** tablet / mobile / narrow desktop; all input; responsive data presentation
- **Generalizability:** medium — the example is a simple table, not a solution for complex spanning headers or spreadsheet editing.
- **Conflicts/tensions:** F-DX-30 and F-DX-36: card-like records can make cross-row comparison harder.
- **Candidate knowledge targets:** card collapse; table semantics; responsive transformation

### F-DX-36: Column priority should follow what people compare

- **Source:** Data Tables: Four Major User Tasks — https://www.nngroup.com/articles/data-tables/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2022-04-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends a human-readable identifier first, important and related columns nearby, discoverable hiding/reordering controls, and a clear indication when columns are hidden.
- **Interpretation:** Prioritize columns from tasks, provide access to omitted fields, and avoid silently discarding lower-priority data at breakpoints.
- **Applies to:** desktop / tablet / mobile; pointer / keyboard / AT; workplace tables
- **Generalizability:** medium — task-centered guidance; exact priorities must come from the product's users.
- **Conflicts/tensions:** F-DX-35: collapsing a comparison table into isolated records may undermine its primary task.
- **Candidate knowledge targets:** column priority; table personalization; comparison

### F-DX-37: A desktop-sized device can contain a narrow application window

- **Source:** Layout — https://developer.apple.com/design/human-interface-guidelines/layout.md
- **Publisher:** Apple Human Interface Guidelines
- **Published/updated:** 2026-09-09
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Apple says to determine layout from available size classes rather than device type or orientation, preserving functionality as windows and size classes change.
- **Interpretation:** Test narrow desktop windows, short wide windows, zoom, and side-by-side use; change presentation while retaining task access.
- **Applies to:** desktop / tablet; all input; Apple adaptive layouts
- **Generalizability:** high — available-space reasoning transfers to responsive web; native size-class APIs do not.
- **Conflicts/tensions:** F-DX-46: medium windows deserve deliberate layouts, not a stretched phone view.
- **Candidate knowledge targets:** window responsiveness; capability parity; resize behavior

### F-DX-38: iPad multitasking includes adjacent and overlapping contexts

- **Source:** Use multitasking on your iPad — https://support.apple.com/en-us/102576
- **Publisher:** Apple Support
- **Published/updated:** 2026-05-14
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Apple Support describes resizable side-by-side Split View, floating Slide Over, keyboard-assisted Spotlight multitasking, and Stage Manager availability on some models.
- **Interpretation:** Include intermediate window widths and simultaneous reference-app use in tablet scenarios; verify OS and device support separately.
- **Applies to:** tablet; touch / pointer / keyboard; iPadOS features documented by Apple
- **Generalizability:** medium — shipped platform behavior, with model and OS differences; not a mandate to reproduce native window controls on the web.
- **Conflicts/tensions:** F-DX-37: a tablet label does not imply full-screen width; current HIG also describes freely resizable iPad windows.
- **Candidate knowledge targets:** tablet multitasking; Split View; Stage Manager

### F-DX-39: Resizing should preserve work and context

- **Source:** App orientation, aspect ratio, and resizability — https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability
- **Publisher:** Google, Android Developers
- **Published/updated:** 2026-10-28
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Android guidance explicitly calls for preserving app state, including form input, during orientation and window-size changes so users retain context.
- **Interpretation:** Keep the selected record, draft, filters, and meaningful position when a web layout changes; test resizing mid-task.
- **Applies to:** desktop / tablet / mobile; all input; Android adaptive app guidance
- **Generalizability:** high — preservation of work transfers broadly; Android activity recreation is a native implementation detail.
- **Conflicts/tensions:** F-DX-37: responsive rearrangement is not permission to restart a workflow.
- **Candidate knowledge targets:** state preservation; responsive transitions; drafts

### F-DX-40: Multiple tabs are a legitimate research and comparison workflow

- **Source:** Page Parking: Multi-Tab Mania — https://www.nngroup.com/articles/multi-tab-page-parking/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2015-11-01
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** NN/g observed page parking in young-adult studies: users open several candidates before evaluating them, using tabs as memory aids; parallel browsing serves separate simultaneous tasks.
- **Interpretation:** Support user-controlled tab opening, useful document titles, and independent item views rather than forcing every task through one transient panel.
- **Applies to:** desktop / tablet; pointer / keyboard; shopping, research, and parallel browsing
- **Generalizability:** medium — observed behavior is broader than one site, but the reported age pattern is historical and should not be projected onto all users.
- **Conflicts/tensions:** F-DX-41: stable URLs enable this workflow; opening tabs automatically is not implied.
- **Candidate knowledge targets:** multi-tab workflows; page titles; comparison

### F-DX-41: Real destination URLs support tabs, bookmarks, and deep links

- **Source:** <a>: The Anchor element — https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a
- **Publisher:** MDN Web Docs
- **Published/updated:** 2026-10-28
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** MDN warns that fake href values with click handlers break copying, new-tab opening, and bookmarking, and recommends hyperlinks for navigation to real URLs.
- **Interpretation:** Give records and meaningful destinations addressable URLs; make reload and direct arrival restore an intelligible view.
- **Applies to:** desktop / tablet / mobile; pointer / keyboard / AT; web navigation
- **Generalizability:** high — built-in browser behavior is broadly applicable; restoring application state requires additional design.
- **Conflicts/tensions:** F-DX-10: direct arrivals need location context; F-DX-40: links preserve user choice.
- **Candidate knowledge targets:** deep linking; native links; browser interoperability

### F-DX-42: A command palette can consolidate expert access

- **Source:** User interface — https://code.visualstudio.com/docs/editing/getting-started/userinterface.md
- **Publisher:** Microsoft Visual Studio Code documentation
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Microsoft documents the Command Palette as a common entry point for running commands, opening files, finding symbols, and discovering available operations and shortcuts.
- **Interpretation:** For command-heavy web apps, consider searchable actions with contextual availability while retaining visible routes to core work.
- **Applies to:** desktop / tablet; keyboard / pointer; editor-style applications
- **Generalizability:** medium — documented product/platform convention, not evidence that every app needs a palette.
- **Conflicts/tensions:** F-DX-18: discovery and novice workflows still matter; F-DX-21: the web cannot copy every native shortcut safely.
- **Candidate knowledge targets:** command palette; command search; expert workflows

### F-DX-43: Recent items reduce the need to reconstruct a working set

- **Source:** User interface — https://code.visualstudio.com/docs/editing/getting-started/userinterface.md
- **Publisher:** Microsoft Visual Studio Code documentation
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** VS Code documents commands to cycle recently used editors and history-based navigation, alongside a list of open editors when tabs are insufficient.
- **Interpretation:** Provide recent items or a resumable working set for repeated document and record workflows.
- **Applies to:** desktop / tablet; keyboard / pointer; multirecord work
- **Generalizability:** medium — a documented editor convention, not a measured benefit for every consumer app.
- **Conflicts/tensions:** F-DX-40: built-in recent items should complement browser tabs rather than obstruct them.
- **Candidate knowledge targets:** recent items; task resumption; working sets

### F-DX-44: Remember settings with an explicit scope and reset path

- **Source:** User and workspace settings — https://code.visualstudio.com/docs/configure/settings.md
- **Publisher:** Microsoft Visual Studio Code documentation
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** VS Code distinguishes global user settings from overriding workspace settings, stores chosen values, and provides an individual Reset Setting action.
- **Interpretation:** For expert web apps, define whether density, columns, and defaults belong to a person, device, or workspace; make overrides visible and reversible.
- **Applies to:** desktop / tablet; keyboard / pointer / AT; configurable applications
- **Generalizability:** medium — a mature product convention; which preferences to persist remains task-specific.
- **Conflicts/tensions:** F-DX-51: persistence and synchronization have different scopes.
- **Candidate knowledge targets:** defaults; preference memory; settings scope

### F-DX-45: Use undo for recoverable work and confirmation for serious consequences

- **Source:** Confirmation Dialogs Can Prevent User Errors — If Not Overused — https://www.nngroup.com/articles/confirmation-dialog/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2018-02-18; last reviewed 2026-08-07
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g discourages routine confirmations, recommends specific confirmations for serious or irreversible consequences, and urges providing undo even with good dialogs.
- **Interpretation:** Prefer recoverable routine actions; name affected objects and consequences when a confirmation is justified.
- **Applies to:** all; all input; destructive or consequential actions
- **Generalizability:** high — general error-prevention guidance; actual reversibility and risk determine the design.
- **Conflicts/tensions:** F-DX-32: bulk scope can increase consequences; F-DX-28: optimistic display does not make an action reversible.
- **Candidate knowledge targets:** undo; confirmation dialogs; destructive actions

### F-DX-46: Medium and expanded windows are separate design opportunities

- **Source:** Use window size classes — https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes
- **Publisher:** Google, Android Developers / Material 3 Adaptive
- **Published/updated:** 2026-10-23
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Google's Material 3 Adaptive guidance defines medium width as 600dp ≤ width < 840dp and expanded as 840dp ≤ width < 1200dp, based on available window space; height can make two panes impractical.
- **Interpretation:** Design and test an intermediate layout, considering both dimensions; do not copy native dp thresholds into CSS without checking content.
- **Applies to:** tablet / desktop / mobile; all input; Android adaptive layouts
- **Generalizability:** medium — official platform breakpoints are opinionated, not universal web-device categories.
- **Conflicts/tensions:** F-DX-37: the same physical device can move among classes.
- **Candidate knowledge targets:** tablet layouts; window classes; adaptive breakpoints

### F-DX-47: Window width does not identify the active input method

- **Source:** Media Queries Level 4, §§7.1–7.3 — https://www.w3.org/TR/mediaqueries-4/
- **Publisher:** W3C CSS Working Group
- **Published/updated:** 2026-02-19 (Candidate Recommendation Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E1
- **Finding:** Media Queries Level 4 defines pointer/hover around the primary pointing device and any-pointer/any-hover around available devices; fine and coarse pointers may coexist. The fetched specification is a Candidate Recommendation Draft.
- **Interpretation:** Use width for space decisions and capability queries for enhancements, preserving fully usable touch and keyboard paths.
- **Applies to:** all; pointer / touch / keyboard; CSS interaction capabilities
- **Generalizability:** high — standards-defined query semantics; draft status is explicit and capabilities do not reveal user intent.
- **Conflicts/tensions:** F-DX-12: a hover-capable laptop may also be used by touch.
- **Candidate knowledge targets:** hybrid inputs; pointer detection; hover queries

### F-DX-48: Cross-device consistency starts with core tasks and meaning

- **Source:** Consistency in the Omnichannel Experience — https://www.nngroup.com/articles/omnichannel-consistency/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2016-10-16
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** NN/g's omnichannel research recommends consistent core functionality and workflows, while acknowledging contextual optimization; a desktop/tablet insurance example exposed different access to policy information.
- **Interpretation:** Keep task outcomes, terminology, and information availability aligned while adapting control placement and interaction to input and space.
- **Applies to:** all; all input; cross-channel services
- **Generalizability:** medium — research includes commerce and services, not every class of PWA.
- **Conflicts/tensions:** F-DX-37 and F-DX-52: consistent capability does not require identical layouts or gestures.
- **Candidate knowledge targets:** cross-device consistency; feature parity; information parity

### F-DX-49: Synced data is part of perceived consistency

- **Source:** Consistency in the Omnichannel Experience — https://www.nngroup.com/articles/omnichannel-consistency/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2016-10-16
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** NN/g reports a participant's frustration when a telephone account change was not visible online, explaining that customers expect valid, current data across channels.
- **Interpretation:** Make saved, pending, stale, and conflicted states understandable across device transitions instead of assuming one successful screen completes the experience.
- **Applies to:** all; all input; cross-channel account data
- **Generalizability:** medium — concrete service-research evidence, without a universal acceptable synchronization delay.
- **Conflicts/tensions:** F-DX-51: offline changes can legitimately require conflict handling.
- **Candidate knowledge targets:** state synchronization; save status; cross-channel trust

### F-DX-50: Handoff should avoid redoing work

- **Source:** Seamlessness in the Omnichannel User Experience — https://www.nngroup.com/articles/seamless-cross-channel/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2017-03-19
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** NN/g defines seamless handoff as changing channels with minimal overhead and describes users switching because of interruptions, task fit, or required journey steps.
- **Interpretation:** Test starting on desktop, continuing on tablet or phone, and returning; verify the relevant draft, selection, or task step survives.
- **Applies to:** all; all input; interrupted and cross-channel journeys
- **Generalizability:** medium — the research spans service journeys; exact state and privacy rules are product-specific.
- **Conflicts/tensions:** F-DX-48: visual consistency alone cannot make a transition seamless.
- **Candidate knowledge targets:** cross-device handoff; task continuity; resume state

### F-DX-51: Synchronizing preferences needs exclusions and conflict recovery

- **Source:** Settings Sync — https://code.visualstudio.com/docs/configure/settings-sync.md
- **Publisher:** Microsoft Visual Studio Code documentation
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** VS Code documents selectable sync categories, excludes machine-scoped settings, separates shortcuts by OS by default, and offers explicit local/remote conflict resolution.
- **Interpretation:** Distinguish portable preferences from device-specific settings and give users a comprehensible recovery path for offline divergence.
- **Applies to:** desktop / tablet; keyboard / pointer / AT; configurable cross-device apps
- **Generalizability:** medium — official product behavior; it does not prescribe the correct sync policy for every web app.
- **Conflicts/tensions:** F-DX-44: a setting's persistence scope is not automatically its synchronization scope.
- **Candidate knowledge targets:** settings sync; conflict resolution; device-specific preferences

### F-DX-52: Tablet pointer support complements touch and keyboard

- **Source:** Pointing devices — https://developer.apple.com/design/human-interface-guidelines/pointing-devices.md
- **Publisher:** Apple Human Interface Guidelines
- **Published/updated:** 2026-10-28
- **Accessed:** 2026-11-08
- **Evidence class:** E3
- **Finding:** Apple says iPad pointer interaction supplements touch and recommends a consistent experience as people switch among a pointing device, keyboard, and gestures.
- **Interpretation:** Test an iPad with external keyboard and trackpad, as well as a touchscreen laptop; keep all input routes viable within the same layout.
- **Applies to:** tablet / desktop; pointer / touch / keyboard; Apple input guidance
- **Generalizability:** high — mixed-input reasoning transfers to web; Apple pointer effects and gestures are native conventions.
- **Conflicts/tensions:** F-DX-47: available space and available inputs are independent dimensions.
- **Candidate knowledge targets:** tablet input; touch and keyboard hybrids; pointer support

## Part B — Mobbin: E5 only

Popularity is not evidence of usability. “Common” below means recurring in the publicly visible curated sample, not a measured share of all shipped apps. Observations use rendered public index tags and flow summaries; they do not claim that every screenshot or recorded interaction was inspected. These collections expose examples and then display “Log in or join for free to continue browsing.” No login was performed and no access restriction was bypassed. Each pattern names no more than three products. Product capture dates and versions were not shown in the inspected metadata.

### F-DX-53: Onboarding repeatedly combines account creation with setup

- **Source:** Mobile App Onboarding Screen User Flow Design — https://mobbin.com/explore/mobile/flows/onboarding
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** Public Mobbin flow summaries show account creation plus verification in Revolut and preference selection in Spotify. Both appear in the onboarding collection.
- **Interpretation:** Treat these as recurring shipped-flow examples, not proof that mandatory setup or personalization improves onboarding.
- **Applies to:** mobile; input behavior untested; public flow descriptions
- **Generalizability:** low — curated, login-limited sample; neither completion rates nor overall prevalence are measured.
- **Conflicts/tensions:** Popularity is not evidence of usability; setup can also delay first value.
- **Candidate knowledge targets:** onboarding examples; account setup

### F-DX-54: Empty states occur in collections and search

- **Source:** Empty State UI — https://mobbin.com/explore/mobile/screens/empty-state
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** Mobbin publicly tags Pinterest collection screens and Todoist search screens as Empty State; illustration tags occur in some collection examples.
- **Interpretation:** Include empty content and no-result states in design inventories; the public tags do not establish effective copy or recovery actions.
- **Applies to:** mobile; input behavior untested; public screen metadata
- **Generalizability:** low — categorized examples, without task observation or verification of current product versions.
- **Conflicts/tensions:** Popularity is not evidence of usability; illustration alone does not explain a useful next step.
- **Candidate knowledge targets:** empty states; no results; collection examples

### F-DX-55: Filtering is commonly applied to a visible results set

- **Source:** Mobile Filter UX Flows — https://mobbin.com/explore/mobile/flows/filtering-sorting
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** Mobbin's public summaries describe Turo filtering cars by type/year and Walmart filtering product results by price and other attributes, then displaying the refined results.
- **Interpretation:** Use these as references for refinement flows; evaluate active-filter visibility and removal independently.
- **Applies to:** mobile; input behavior untested; public filter-flow descriptions
- **Generalizability:** low — two examples in a curated collection cannot establish comparative performance or market prevalence.
- **Conflicts/tensions:** Popularity is not evidence of usability; the collection does not show that one filter presentation is best.
- **Candidate knowledge targets:** filter examples; refinement flows

### F-DX-56: Search flows recur across retail and travel

- **Source:** Mobile Searching & Finding User Flow — https://mobbin.com/explore/mobile/flows/searching-finding
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** Mobbin describes Walmart query entry, suggestions, and results, and Turo entering location, dates, and driver age before seeing matching cars.
- **Interpretation:** Search can require domain-specific criteria; reuse the task structure only after checking the product's information needs.
- **Applies to:** mobile; input behavior untested; public search-flow descriptions
- **Generalizability:** low — descriptive shipped examples, without evidence about suggestion quality or search success.
- **Conflicts/tensions:** Popularity is not evidence of usability; one search box is not a universal model for structured queries.
- **Candidate knowledge targets:** search examples; structured search

### F-DX-57: Tab-bar navigation recurs in shipped mobile screens

- **Source:** Mobile Tab Bar UI — https://mobbin.com/explore/mobile/ui-elements/tab-bar
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** The public Tab Bar collection repeatedly tags home screens, including Nextdoor and Walmart, with Tab Bar; these examples also carry Top Navigation Bar tags.
- **Interpretation:** Tab navigation is a common reference pattern in this sample. Bottom placement, label quality, and selection behavior were not verified from metadata.
- **Applies to:** mobile; touch / keyboard behavior untested; public UI-element tags
- **Generalizability:** low — classification shows recurrence, not correct destination count or navigational usability.
- **Conflicts/tensions:** Popularity is not evidence of usability; these mobile examples do not dictate desktop navigation.
- **Candidate knowledge targets:** tab bars; bottom-navigation research candidates

### F-DX-58: Settings combine preferences and account operations

- **Source:** Mobile Settings Screen — https://mobbin.com/explore/mobile/screens/settings-preferences
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** Mobbin tags Nextdoor settings with turning options on/off, dark mode, and logout; KakaoBank examples include Switch and dark-mode tags.
- **Interpretation:** Settings are a recurring home for controls and account operations; test grouping and separation of consequential actions.
- **Applies to:** mobile; input behavior untested; public settings metadata
- **Generalizability:** low — metadata does not establish information architecture quality or persistence semantics.
- **Conflicts/tensions:** Popularity is not evidence of usability; a switch tag does not prove accessible state or immediate saving.
- **Candidate knowledge targets:** settings examples; preference controls

### F-DX-59: Pull-to-refresh appears across several product categories

- **Source:** Mobile Pull To Refresh Screens — https://mobbin.com/explore/mobile/screens/pull-to-refresh
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** The public Pull to Refresh collection includes Wise with Loading Indicator, Deliveroo with Skeleton, and Gmail with Pull to Refresh tags.
- **Interpretation:** The gesture recurs in shipped apps; its discoverability, thresholds, and keyboard or desktop alternatives were not demonstrated by the public index.
- **Applies to:** mobile; gesture behavior untested; public screen metadata
- **Generalizability:** low — categorized screen examples cannot verify a temporal interaction or recommend it for PWAs.
- **Conflicts/tensions:** Popularity is not evidence of usability; provide another refresh route when the task needs one.
- **Candidate knowledge targets:** refresh examples; gesture alternatives

### F-DX-60: Side navigation remains common in shipped web-app examples

- **Source:** Web Side Navigation UI — https://mobbin.com/explore/web/ui-elements/side-navigation
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** Mobbin's public web collection tags Notion, Front, and Canva examples with Side Navigation, across home, communication, and content-browsing contexts.
- **Interpretation:** Persistent desktop navigation deserves explicit exploration when the information architecture and available space justify it.
- **Applies to:** desktop web; input behavior untested; public screen metadata
- **Generalizability:** low — curated collection demonstrates recurrence, not sidebars outperforming top navigation.
- **Conflicts/tensions:** Popularity is not evidence of usability; F-DX-06 supplies separate design reasoning.
- **Candidate knowledge targets:** sidebar examples; desktop navigation

### F-DX-61: Multiple columns recur in communication and operational web apps

- **Source:** Explore web app designs — https://mobbin.com/explore/web
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** The public web-app index tags Front, Better Stack, and Lemni screens with Multi-Column Layout, alongside navigation or toolbar elements.
- **Interpretation:** These are shipped references for using wide-screen space to keep related work visible; responsive behavior was not inspected.
- **Applies to:** desktop web; input behavior untested; public screen metadata
- **Generalizability:** low — static categories do not reveal narrow-window transitions or whether simultaneous panes help a particular task.
- **Conflicts/tensions:** Popularity is not evidence of usability; F-DX-04 supplies platform guidance for related panes.
- **Candidate knowledge targets:** multi-column examples; desktop workspaces

### F-DX-62: Web tables coexist with task controls

- **Source:** Web Table UI — https://mobbin.com/explore/web/ui-elements/table
- **Publisher:** Mobbin
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E5
- **Finding:** Mobbin publicly lists Shopify tables with filtering/sorting tags, Notion tables with breadcrumbs, and ClickUp tables with checkbox/selection tags.
- **Interpretation:** Treat tables as task surfaces with navigation and actions; selection semantics, sorting behavior, and responsiveness still need verification.
- **Applies to:** desktop web; input behavior untested; public table metadata
- **Generalizability:** low — three shipped examples do not validate accessibility or the usability of any interaction.
- **Conflicts/tensions:** Popularity is not evidence of usability; E3 table conventions and E2/E4 research remain separate evidence.
- **Candidate knowledge targets:** data-table examples; selection; comparison

## Coverage and gaps

All ten Part A topic groups have at least one substantively fetched source. Coverage includes prose measure versus table width; whitespace and pane layouts; navigation hierarchy; hover, tooltips, context menus, cursors, and drag alternatives; shortcut discovery and conflicts; focus recovery and composite navigation; inline save/cancel and optimistic recovery; sortable/selectable tables, bulk actions, sticky headers, column priority, and responsive transformations; window resizing, multitasking, tabs, and URLs; command palettes, recents, and preference scope; intermediate layouts and hybrid input; and cross-device consistency, synchronization, and handoff.

Fetch accounting counts distinct content pages, treating equivalent HTML/Markdown representations, redirects, repeated reads, and fragments as one page. Search-result snippets are discovery aids and are not counted as fetched sources.

| Fetch outcome | Count | Scope |
|---|---:|---|
| Readable pages cited by findings | 45 | 35 Part A sources and 10 Mobbin collection/index pages |
| Other readable navigation or incidental pages | 3 | Mobbin homepage, Mobbin mobile explore index, and an incidental Baymard industry page; none supplies a finding |
| Additional unusable candidate routes | 4 | Listed below; none supplies a finding |
| Fetch-tool errors subsequently recovered | 2 | Apple sidebar and multitasking Markdown requests; recovered through direct HTTP |

Thus, 48 substantive pages were fetched successfully, of which 45 are cited. Two Apple HTML entry pages returned JavaScript shells before their corresponding Markdown content was fetched; those shells are not substantive sources.

Unusable candidate routes, recorded as failures rather than cited evidence:

- `https://m3.material.io/foundations/layout/applying-layout/window-size-classes` returned 404. The fetched official Android Material 3 Adaptive window-class guidance supplies the medium/expanded coverage instead.
- `https://atlassian.design/components/inline-edit/` yielded no readable article content in the fetch tool. The fetched official Forge UI Kit Inline edit documentation supplies the inline-edit findings.
- `https://www.nngroup.com/articles/table-sorting/` was reported inaccessible by the fetch tool. Sorting findings use the fetched Carbon guidance.
- `https://mobbin.com/explore/mobile/screens/settings` rendered Page not found. The working public Settings & Preferences route is the source for F-DX-58.

The web fetch tool rejected Apple's sidebar and multitasking Markdown responses as unsupported content-type. Direct HTTP fetched both with status 200; the cited Markdown URLs are the recovered content. Layout, split-view, and pointing-device Markdown pages were also fetched directly.

Limits requiring further research:

- Mobbin access was partial: public category tags, named examples, and some written flow descriptions were available, followed by a login prompt. No current-product behavior, keyboard support, responsive transitions, animation timing, or usability outcomes were verified. Pull-to-refresh observations concern indexing, not a tested gesture. The Tab Bar index does not alone verify bottom placement. The public sample is curated and cannot support population-prevalence claims.
- Apple's current HIG describes resizable/windowed iPad apps; the separate Support page discusses Split View and mentions Stage Manager. Exact availability and behavior vary by OS release and model. Native window controls, pointer effects, and Apple size classes should not be copied literally into a PWA.
- The optimal prose measure is supported by commerce observations and typographic guidance, not a controlled universal optimum across languages, fonts, reading ability, and expert applications. No universal maximum page width was established.
- Density, remembered defaults, recents, and command palettes are supported mainly by design-system or official product documentation. Comparative usability studies for these choices in responsive PWAs were not found in this pass.
- Responsive table stacking is a simple-table technique. Complex headers, virtualization, spreadsheet editing, sticky regions at high zoom, and current browser/AT combinations need implementation-specific testing. Column priority should be researched with the actual comparison tasks.
- Synchronization sources establish expectations and illustrate conflict handling; they do not establish acceptable latency, offline conflict policy, security boundaries, or whether drafts and all preferences should sync automatically.
- Focus management and WCAG requirements are documented here; no implementation or conformance audit was performed. PWA installation, service workers, and offline architecture are outside this assignment's evidence coverage.

## Disagreements

- **Prose width versus data width:** F-DX-01 limits reading measure; F-DX-02 favors ample space for tables. These are task-dependent constraints, not grounds for one global maximum width.
- **Visibility versus reduced chrome:** F-DX-06–09 favor understandable, discoverable navigation while permitting collapsed sidebars and progressive hierarchy. Apple generally limits sidebar depth; NN/g supports grouped mega menus for broad sites. The patterns serve different information structures.
- **Visible actions versus hover disclosure:** Carbon permits row controls revealed on hover/focus with touch fallback (F-DX-12); NN/g cautions that hidden contextual actions and tooltips have discovery and access costs (F-DX-13, F-DX-15). Optional acceleration should not conceal the only route to a task.
- **Density versus ease of interaction:** F-DX-05 documents density options; F-DX-47 and F-DX-52 reject inferring input from width. Dense expert layouts still need usable targets and keyboard paths on hybrid devices.
- **Load more versus pagination:** Commerce tests in F-DX-33 favor load more with lazy loading for discovery. Carbon also documents table pagination. The evidence does not justify replacing operational-grid pagination everywhere, or infinite scrolling everywhere.
- **Grid comparison versus stacked records:** F-DX-30 and F-DX-36 preserve headers, identity, and adjacent comparison; F-DX-35's stacked option can fit narrow record reading but can undermine comparison and table semantics. Choose from the task and test the transformation.
- **Undo versus confirmation:** F-DX-45 argues against routine interruptions while retaining specific confirmations for consequential or irreversible work. Optimistic UI (F-DX-28) is a latency behavior, not an alternative to actual recovery.
- **Consistency versus adaptation:** F-DX-48–50 support consistent tasks, data, and continuity, while F-DX-37, F-DX-46, and F-DX-52 support different arrangements and input methods. Equivalent outcomes do not require pixel-identical interfaces.

