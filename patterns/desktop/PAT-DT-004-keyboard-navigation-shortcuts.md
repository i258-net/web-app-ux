---
id: PAT-DT-004
title: Keyboard navigation, tab order, roving tabindex, skip links, and shortcuts
type: pattern
scope: desktop
topics: [keyboard, tab-order, roving-tabindex, skip-link, shortcuts, accelerators, discoverability, conflicts, wcag-2.1.4]
platforms: [desktop, tablet]
viewports: [medium, expanded, large, extra-large]
inputs: [keyboard, pointer, assistive-tech]
principles: [P-12, P-07, P-02, P-09]
dimensions: [D-08, D-03, D-01]
gates: [QG-001, QG-002, QG-003, QG-004, QG-005, QG-006]
related: [PAT-DT-005, PAT-DT-007, PAT-DT-008, PAT-DT-011, PAT-DT-002, PAT-SH-015, PAT-RS-011]
evidence_strength: strong
status: active
updated: 2026-11-08
---

# Keyboard navigation, tab order, roving tabindex, skip links, and shortcuts

## Problem

Keyboard operation is two things at once. It is a baseline accessibility requirement for people who cannot use a pointer, and it is the main speed tool for expert desktop users, including iPad users with a hardware keyboard. Products fail at both ends. Custom widgets can't be reached or escaped, every row in a 200-row table is its own Tab stop, focus is invisible, and the sidebar repeats on every page. At the other end, single-letter shortcuts fire while someone is dictating into a comment field, shortcuts take over browser or screen-reader keys, or shortcuts exist that nobody can find.

## Recommendation

**Outcome:** everything works from the keyboard in a predictable order with visible focus. Frequent actions have discoverable, conflict-free shortcuts that people can turn off or that are scoped to focus.

### Baseline navigation

1. **Everything is reachable and operable by keyboard** (QG-001), with no traps (QG-002). Prefer native elements (`button`, `a href`, `input`, `select`, `dialog`), because they come with keyboard behavior built in.
2. **Tab order follows meaning and visual order** (QG-004). Re-check after responsive rearrangement. CSS `order` and grid placement can separate visual order from DOM order. Avoid positive `tabindex`.
3. **Focus is always visible** (QG-005) and never entirely hidden by sticky headers, toolbars, or cookie banners (QG-006). Use `:focus-visible` with a high-contrast indicator. The 2 px / 3:1 metric is AAA (SC 2.4.13) and serves as a good target, not an AA requirement.
4. **Bypass repeated blocks.** Provide a working "Skip to main content" link that becomes visible on focus, plus landmarks (`header`, `nav`, `main`).
5. **One Tab stop per composite widget.** Toolbars, tablists, listboxes, trees, menus, and interactive grids take a single Tab stop, and arrow keys move within them. Implement this with **roving tabindex** (the active child has `tabindex="0"`, the others `-1`) or `aria-activedescendant`. Follow the role's APG contract exactly. For example, tabs use arrows plus Enter/Space in manual activation, and menus use arrows, Enter, and Escape returning to the invoker. Do **not** apply composite behavior to ordinary navigation links or static tables, where Tab between links is expected.

### Shortcuts

6. **Assign shortcuts from observed frequency**, not to every command. Keep platform conventions (Ctrl/⌘ + C/V/Z/F, and so on) and show the correct modifier per OS.
7. **Make them discoverable where the action is.** Show the key combination beside menu items and in tooltips on toolbar buttons, and provide a searchable shortcut reference, often bound to `?` and also reachable from a Help menu. A command palette can list them (PAT-DT-011).
8. **WCAG 2.1.4 for character-only keys.** A shortcut made only of a letter, number, punctuation, or symbol (`j`, `k`, `e`, `/`, `?`) must meet at least one condition. It can be **turned off**, it can be **remapped** to include a non-printable key such as Ctrl, Alt, or ⌘, or it is **active only while the relevant component has focus**. Speech-input users are one group affected: when dictated words become keystrokes, they can trigger letter shortcuts by accident. Never fire character shortcuts while focus is in a text field, `contenteditable`, or combobox.
9. **Audit conflicts** with browser shortcuts (Ctrl/⌘ + L, T, W, N, F, R, digit keys), OS shortcuts, and assistive-technology commands. Test with the screen readers you support, because their command sets differ. Never override text-editing keys inside inputs. Where a desired combination collides, choose another. If one cannot be avoided, document it and offer the visible route.
10. **Shortcuts are accelerators.** Every shortcut action is also available through visible UI.

## Evidence

- **E1** W3C, WCAG 2.2 SC 2.1.1, 2.1.2, 2.1.4, 2.4.1, 2.4.3, 2.4.7, 2.4.11. https://www.w3.org/TR/WCAG22/#keyboard, https://www.w3.org/TR/WCAG22/#character-key-shortcuts, https://www.w3.org/TR/WCAG22/#focus-order, https://www.w3.org/TR/WCAG22/#focus-visible, https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum. Normative keyboard, focus, bypass, and character-shortcut requirements (F-SP-08/09/10/12/13/14, F-DX-20, F-DX-25).
- **E3** W3C WAI APG, "Developing a Keyboard Interface". https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/. Roving tabindex and one Tab stop per composite (F-DX-24). Shortcut conflicts with OS, browser, and AT can block essential functions and should be avoided or mitigated (F-DX-21).
- **E3** W3C WAI APG, Menubar and Tabs patterns. https://www.w3.org/WAI/ARIA/apg/patterns/menubar/, https://www.w3.org/WAI/ARIA/apg/patterns/tabs/. Role-specific keyboard contracts (F-SP-38, F-SP-39). APG is non-normative.
- **E4** Nielsen Norman Group, "UI Copy: UX Guidelines for Command Names and Keyboard Shortcuts". https://www.nngroup.com/articles/ui-copy/. Pick shortcuts from frequent tasks, show them beside commands, give Mac and Windows equivalents, and avoid reassigning familiar or AT shortcuts (F-DX-19, F-NB-32).
- **E4** Nielsen Norman Group, "Accelerators Maximize Efficiency in User Interfaces". https://www.nngroup.com/articles/ui-accelerators/. Optional accelerators introduced in context (F-DX-18).
- **E4** Nielsen Norman Group, "Flexibility and Efficiency of Use". https://www.nngroup.com/articles/flexibility-efficiency-heuristic/. Accelerators sit alongside learnable paths (F-NB-07).
- **E3** Apple Human Interface Guidelines, "Keyboards". https://developer.apple.com/design/human-interface-guidelines/keyboards.md. Mac and iPad support keyboard-only work and shortcuts (F-SP-64).

## Alternatives and tradeoffs

- **Global letter shortcuts with a settings toggle vs. modifier-only shortcuts.** Letter keys (Gmail/GitHub style) are fast for experts and satisfy 2.1.4 if they can be turned off. Modifier combinations avoid the problem but collide more often with browser keys.
- **Roving tabindex vs. `aria-activedescendant`.** Roving moves real DOM focus and works well for scroll-into-view. `activedescendant` keeps focus on a container or input, which suits comboboxes. Both are valid.
- **Sequences (`g` then `i`)** reduce collisions but are harder to discover.

## Exceptions and failure modes

- Interactive grids, editors, and canvases may intercept arrow keys and some letters while they have focus. That is acceptable under 2.1.4's focus-scoped option, provided Tab or Escape still exits.
- `outline: none` with no replacement indicator.
- Shortcut help that only exists in documentation.
- Assuming tablet means no keyboard. iPad and Android tablets with keyboards need the same model (PAT-RS-011).
- A focus trap in a non-modal panel.

## Evaluation questions

- Can every task be completed with the keyboard alone, with no traps? [running app]
- Does Tab order match visual order at each breakpoint? [running app]
- Is focus always visible and never fully covered by sticky elements? [running app] [screenshot]
- Is there a working skip link? [running app] [automated]
- Do toolbars, tabs, and grids use a single Tab stop with arrow navigation per APG? [running app]
- Are character-only shortcuts switchable, remappable, or focus-scoped, and do they stay silent in text fields? [running app]
- Do any shortcuts override browser, OS, or screen-reader keys? [running app]
- Are shortcuts shown beside commands and in a reference? [screenshot]
- Do screen-reader users complete core tasks without shortcut collisions? [user study]

## Related

- Patterns: [PAT-DT-002](PAT-DT-002-sidebar-hierarchical-navigation.md), [PAT-DT-005](PAT-DT-005-focus-selection-management.md), [PAT-DT-007](PAT-DT-007-data-tables-grids.md), [PAT-DT-008](PAT-DT-008-contextual-actions-menus.md), [PAT-DT-011](PAT-DT-011-expert-workflows.md), PAT-SH-015, PAT-RS-011
- Principles: [P-12](../../principles/P-12-accessibility-inclusion.md), [P-07](../../principles/P-07-input-efficiency.md), [P-02](../../principles/P-02-discoverability-learnability.md), [P-09](../../principles/P-09-consistency-familiarity.md)
- Rubric: [D-08, D-03, D-01](../../rubric/dimensions.md); gates [QG-001–QG-006](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
