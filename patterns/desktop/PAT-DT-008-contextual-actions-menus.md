---
id: PAT-DT-008
title: Contextual actions — right-click menus, row hover actions, and toolbars with touch and keyboard parity
type: pattern
scope: desktop
topics: [context-menu, right-click, row-actions, toolbar, overflow-menu, long-press, menu-button, input-parity]
platforms: [desktop, tablet, mobile]
viewports: [medium, expanded, large, extra-large]
inputs: [pointer, keyboard, touch, assistive-tech]
principles: [P-02, P-06, P-07, P-09, P-12]
dimensions: [D-03, D-01, D-08]
gates: [QG-001, QG-012, QG-015, QG-016, QG-019, QG-041]
related: [PAT-SH-008, PAT-SH-011, PAT-DT-003, PAT-DT-004, PAT-DT-007, PAT-DT-011, PAT-MO-006, PAT-MO-007, PAT-RS-009]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Contextual actions — right-click menus, row hover actions, and toolbars with touch and keyboard parity

## Problem

Desktop users expect to act on objects directly: right-click a file, hover a row to reveal Archive, use a toolbar that changes with the selection. These accelerators are efficient, but they are often the *only* route to the command. Right-click is invisible to newcomers and has no reliable touch equivalent. Long-press conflicts with text selection and the browser's own menu. Keyboard users need the Menu key or Shift+F10, which many custom menus ignore. Hover-revealed actions vanish on tablets. Universal guidance on labeling, ordering, and dangerous items in action menus lives in PAT-SH-008. This pattern covers the desktop-specific triggers and how to keep parity across inputs.

## Recommendation

**Outcome:** the commands that apply to an object can be found through a visible control, and invoked by pointer, touch, and keyboard. Right-click, hover, and shortcuts make experts faster without being required.

1. **Every contextual command has a visible home.** That can be a per-object overflow button ("…" with an accessible name such as "Actions for Invoice 1042"), a selection toolbar, or a detail-view action bar. A custom right-click menu should show the *same* commands in the same order as that visible menu, so learning carries over.
2. **Show frequent actions in toolbars; use menus for the rest.** A toolbar keeps high-priority actions visible. A menu temporarily exposes a longer or less frequent set. Order menu items by frequency and logic, group them with separators, put destructive items last and set apart, and follow the destructive-action guidance in PAT-SH-011. Show unavailable commands as disabled rather than removing them, so people learn they exist. Add an ellipsis to labels that need more input.
3. **Implement custom context menus fully, or not at all.**
   - Open on `contextmenu`, which also fires for the keyboard Menu key and Shift+F10 in common browsers. Verify this in your supported browsers.
   - Use `role="menu"` / `menuitem` with the APG menu contract: focus moves into the menu, arrows move between items, Enter activates, and Escape closes and returns focus to the target.
   - Position the menu within the viewport and dismiss it on outside click or Escape.
   - Don't hijack right-click on text, links, images, or inputs where the browser menu (copy, open in new tab, spell-check) is more useful. Scope custom menus to app objects.
4. **Row hover actions follow PAT-DT-003.** Reveal on hover *and* focus-within, show persistently when `any-hover: none`, and keep at least the overflow button always visible.
5. **Touch gets a visible route first.** Long-press can be an optional accelerator, but it is not discoverable and competes with native selection. Always pair it with a visible overflow control or a selection mode. Swipe actions are covered in PAT-MO-007.
6. **Use toolbar semantics deliberately.** A grouped set of controls can use `role="toolbar"` with a single Tab stop and arrow keys between controls (PAT-DT-004). Icon-only buttons need accessible names that match their tooltips (QG-016) and targets of at least 24 px (QG-019).
7. **Show shortcut hints in menus** next to items (PAT-DT-004).

## Evidence

- **E4** Nielsen Norman Group, "Contextual Menus: Delivering Relevant Tools for Tasks". https://www.nngroup.com/articles/contextual-menus/. Contextual actions relevant to the target, visible menu signifiers, and a second route because hidden triggers go undiscovered (F-DX-15).
- **E3** Google Material Design, "Menus". https://m3.material.io/components/menus. Menus temporarily expose actions. Use a toolbar when actions need to stay visible. Context menus apply to an element and often open by secondary click (F-SP-78).
- **E3** Apple Human Interface Guidelines, "Menus". https://developer.apple.com/design/human-interface-guidelines/menus.md. Concise labels, frequent items early, logical groups, unavailable items shown as unavailable, and an ellipsis when more input is needed (F-SP-62).
- **E3** W3C WAI APG, "Menu and Menubar Pattern". https://www.w3.org/WAI/ARIA/apg/patterns/menubar/. Arrow navigation, Enter activation, Escape closes and returns focus. Disabled items can receive focus (F-SP-38). APG is non-normative.
- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines. Persistent row overflow by default, and hover mode with focus and no-hover fallbacks (F-DX-12).
- **E3** Google Material Design, "Lists". https://m3.material.io/components/lists. Swipeable lists need an alternate route to hidden actions, such as a More control (F-SP-79).
- **E1** W3C, WCAG 2.2 SC 2.1.1 Keyboard and 2.5.2 Pointer Cancellation. https://www.w3.org/TR/WCAG22/#keyboard, https://www.w3.org/TR/WCAG22/#pointer-cancellation. Commands must be keyboard operable. Activation should not complete on the down-event unless that is essential (F-SP-08, F-SP-17).

That the `contextmenu` event fires for the Menu key and Shift+F10 is an implementation observation that should be checked per browser. It is not sourced here.

## Alternatives and tradeoffs

- **Hover-reveal vs. always-visible row actions.** See PAT-DT-003. Persistent overflow is the safe default, and hover-reveal is a density optimization.
- **Contextual toolbar vs. context menu.** A toolbar that appears with a selection is discoverable and works with multi-select. A context menu is faster for single objects with a mouse. Many apps offer both.
- **No custom context menu.** It is often the best choice for document-like content, where the browser's menu is what people want.

## Exceptions and failure modes

- Canvas, drawing, and map apps may legitimately take over right-click and long-press. They must still expose the same commands through a menu bar or toolbar.
- Context menus that contain commands found nowhere else.
- Menus that open on `mousedown` and act on release, so an accidental press can't be abandoned (QG-015).
- Long-press with no visible signifier on touch.
- Context menus clipped off-screen in narrow windows.

## Evaluation questions

- Is every command in the context menu also available from a visible control? [running app]
- On a touch-only device, can every contextual command be reached without long-press? [running app]
- Do the Menu key and Shift+F10 open the custom menu, and do arrows, Enter, and Escape behave per APG with focus returning to the target? [running app]
- Is the browser's menu preserved on text, links, and inputs? [running app]
- Are destructive items separated, and are unavailable items shown as disabled? [screenshot]
- Do icon-only toolbar buttons have accessible names that match their tooltips? [automated]
- Do new users find row-level actions without being told? [user study]

## Related

- Patterns: PAT-SH-008, PAT-SH-011, [PAT-DT-003](PAT-DT-003-hover-tooltips.md), [PAT-DT-004](PAT-DT-004-keyboard-navigation-shortcuts.md), [PAT-DT-007](PAT-DT-007-data-tables-grids.md), [PAT-DT-011](PAT-DT-011-expert-workflows.md), PAT-MO-006, PAT-MO-007, PAT-RS-009
- Principles: [P-02](../../principles/P-02-discoverability-learnability.md), [P-06](../../principles/P-06-interaction-ergonomics.md), [P-07](../../principles/P-07-input-efficiency.md), [P-09](../../principles/P-09-consistency-familiarity.md), [P-12](../../principles/P-12-accessibility-inclusion.md)
- Rubric: [D-03, D-01, D-08](../../rubric/dimensions.md); gates [QG-001, QG-012, QG-015, QG-016, QG-019, QG-041](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
