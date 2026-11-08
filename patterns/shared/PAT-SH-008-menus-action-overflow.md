---
id: PAT-SH-008
title: Action menus, overflow, and icon-only buttons
type: pattern
scope: shared
topics: [menus, overflow, kebab-menu, icon-buttons, action-labels, destructive-items, toolbars]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-02, P-05, P-09, P-12]
dimensions: [D-03, D-06, D-08]
gates: [QG-001, QG-016, QG-019, QG-012, QG-041]
related: [PAT-DT-008, PAT-DT-003, PAT-MO-011, PAT-SH-011, PAT-SH-006, PAT-MO-001, PAT-SH-001]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Action menus, overflow, and icon-only buttons

## Problem

Apps run out of room for actions, so they push them into "…" menus, icon-only buttons, right-click menus, and hover-revealed toolbars. Hidden actions are found less often. Unlabeled icons are ambiguous. Menus mix routine and destructive commands, and custom menus often break keyboard and screen-reader use. When responsive layouts move actions into overflow, users who learned one width cannot find the action at another.

## Recommendation

**Outcome:** frequent actions are visible; less frequent ones are one predictable step away; every action has a clear name that assistive technology announces; dangerous actions are hard to trigger by accident.

1. **Prioritize by frequency and importance.**
   - Keep the one or two most frequent or important actions as visible, labeled buttons.
   - Put the rest in an overflow menu.
   - When width shrinks, move the lowest-priority items into overflow first, and keep the *order* of the remaining items stable (PAT-RS-005).
2. **Label actions with verbs** ("Archive", "Duplicate"). Add an ellipsis when the command needs further input ("Rename…").
   - Icon-only buttons are acceptable only for widely recognized icons (search, close, more). Each needs an accessible name. A tooltip on hover *and* focus can help sighted users (PAT-DT-003), but the name must not depend on it.
   - Where a visible label exists, the accessible name contains it (QG-016).
3. **Name and position the overflow trigger.** Use a recognizable icon (⋯ or ⋮), consistently placed. Give it an accessible name that includes its context ("More actions for Invoice 42"), not just "More". The target meets at least 24×24 CSS px or the spacing exception (QG-019); comfort sizes for touch are in PAT-MO-001.
4. **Group and order menu items.**
   - Put frequent items first.
   - Group related commands with separators.
   - Put destructive items last, separated, and styled distinctly (text, not color alone).
   - Never make a destructive item the default or the first focused item.
5. **Show unavailable commands as disabled, rather than removing them**, so users learn the command exists. Explain why when that is not obvious. A menu whose items are all unavailable still opens.
6. **Use correct semantics.**
   - For action menus, use a real button that opens a menu and exposes its expanded state.
   - Follow the APG menu contract: Enter opens or activates, arrows move between items, Escape closes and returns focus to the trigger.
   - Do **not** apply ARIA `menu` roles to ordinary site-navigation link lists (PAT-SH-001).
7. **No hover-only or right-click-only routes.** Context menus and hover toolbars are accelerators. The same commands must be reachable through a visible control for touch and keyboard users (QG-041). Row hover actions also appear on focus, and they are persistent where hover is unavailable (PAT-DT-008).
8. **Keep menus temporary.** If users need actions continuously, use a toolbar instead of a menu.

## Evidence

- **E3** Apple, "Menus". https://developer.apple.com/design/human-interface-guidelines/menus.md — Concise labels, frequent items early, logical groups with separators, show unavailable items as unavailable, add an ellipsis when more input is needed. Apple platforms.
- **E3** Google Material Design, "Menus". https://m3.material.io/components/menus — Menus are temporary; use a toolbar when actions must stay visible; context menus often open by secondary click. Material convention.
- **E3** Apple, "Toolbars". https://developer.apple.com/design/human-interface-guidelines/toolbars.md — Group actions logically and move lower-priority items to overflow as width shrinks. Apple platforms.
- **E3** Apple, "Buttons". https://developer.apple.com/design/human-interface-guidelines/buttons.md — Clear purpose through familiar icons or concise labels; never make a destructive action the default. Apple platforms.
- **E3** W3C WAI, "APG menu/menubar pattern". https://www.w3.org/WAI/ARIA/apg/patterns/menubar/ — Keyboard contract for menus. It is not the contract for ordinary site-navigation links. (E3 per `sources/evidence-classes.md`.)
- **E4** Nielsen Norman Group, "Contextual Menus: Delivering Relevant Tools for Tasks". https://www.nngroup.com/articles/contextual-menus/ — Show visible menu signifiers and provide another route, because hidden triggers go undiscovered.
- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines — Persistent row overflow by default. The optional hover mode also reveals on focus and stays persistent without hover.
- **E2** Nielsen Norman Group, "Hamburger Menus and Hidden Navigation Hurt UX Metrics". https://www.nngroup.com/articles/hamburger-menus/ — Hidden navigation was used less and later. We infer the same discoverability cost applies to hidden *actions*; the study tested navigation, not action menus.
- **E4** Nielsen Norman Group, "Tooltip Guidelines". https://www.nngroup.com/articles/tooltip-guidelines/ — Tooltips are supplemental and need keyboard-focus access; essential information does not belong in them.
- **E1** W3C, "WCAG 2.2 — SC 2.5.3 Label in Name". https://www.w3.org/TR/WCAG22/#label-in-name — The accessible name contains the visible label.
- **E1** W3C, "WCAG 2.2 — SC 1.4.13 Content on Hover or Focus". https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus — Hover and focus content must be dismissible, hoverable, and persistent.

## Alternatives and tradeoffs

- **Visible actions vs overflow.** Visible actions are discoverable but crowd compact layouts. Overflow is compact but hides actions. Use usage data to decide what stays visible.
- **Icon-only vs labeled.** Labels are unambiguous; icons save space. A hybrid is common: labeled at expanded widths, icon plus accessible name at compact widths. Keep the icon identical across widths.
- **Bottom action sheet vs dropdown on compact.** Sheets offer larger targets near the thumb; dropdowns keep spatial context. See PAT-MO-011.
- **Hover-revealed row actions.** They reduce clutter in dense pointer layouts (Carbon E3), at a discoverability cost (NN/g E4). They are acceptable only with focus reveal and touch persistence.

## Exceptions and failure modes

- Single-action items do not need a menu.
- Failure modes:
  - "Delete" placed next to "Edit" with identical styling;
  - a "⋯" announced as "button";
  - a menu that opens on hover and closes as the pointer moves toward it;
  - right-click as the only route to "Rename";
  - actions that silently disappear at narrow widths;
  - `role="menu"` on a navigation link list, which forces arrow-key navigation and hides the links from the Tab order.

## Evaluation questions

1. Are the most frequent actions visible without opening a menu at each viewport? [screenshot] [running app]
2. Does every icon-only control have an accessible name that includes its context? [automated] [running app]
3. Can every menu be opened, navigated, and closed by keyboard, with focus returning to the trigger? [running app]
4. Are destructive items separated, distinctly labeled, and never focused first? [screenshot] [running app]
5. Is every context-menu or hover action also reachable by touch and keyboard? [running app]
6. Do users find a secondary action without hints? [user study]

## Related

- Principles: P-02, P-05, P-09, P-12
- Dimensions: D-03, D-06, D-08
- Gates: QG-001, QG-016, QG-019, QG-012, QG-041
- Patterns: PAT-DT-008 (context menus, row actions), PAT-DT-003 (hover, tooltips), PAT-MO-011 (action sheets), PAT-SH-011 (destructive actions), PAT-SH-006 (bulk actions), PAT-MO-001 (touch targets), PAT-SH-001 (navigation)

## Change log

- 2026-11-08 — Initial version (ADR-001).
