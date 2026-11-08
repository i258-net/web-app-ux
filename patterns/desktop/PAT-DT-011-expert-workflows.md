---
id: PAT-DT-011
title: Expert workflows — bulk operations, command palettes, defaults, recents, and undo over confirm
type: pattern
scope: desktop
topics: [expert-users, power-users, bulk-actions, command-palette, defaults, recents, working-set, preferences, undo, confirmation]
platforms: [desktop, tablet]
viewports: [medium, expanded, large, extra-large]
inputs: [keyboard, pointer, touch, assistive-tech]
principles: [P-01, P-07, P-11, P-02, P-14]
dimensions: [D-01, D-04, D-07]
gates: [QG-001, QG-003, QG-025, QG-028]
related: [PAT-SH-004, PAT-SH-005, PAT-SH-006, PAT-SH-011, PAT-RS-011, PAT-DT-004, PAT-DT-005, PAT-DT-007, PAT-DT-010, PAT-RS-004, PAT-PW-007]
evidence_strength: limited
status: active
updated: 2026-11-08
---

# Expert workflows — bulk operations, command palettes, defaults, recents, and undo over confirm

## Problem

People who live in an app all day (support agents, operators, analysts, editors) repeat the same operations hundreds of times. Interfaces tuned for first use get in their way: one record at a time, menus three levels deep, settings that reset every session, "Are you sure?" on every action, and no way back to the five things they were just working on. Interfaces tuned only for experts lose newcomers. The goal is a learnable visible path with accelerators on top.

## Recommendation

**Outcome:** frequent work takes fewer steps for experienced users, without hiding the standard path from newcomers. Mistakes at scale stay recoverable.

1. **Bulk operations with clear scope.** Let people select many records (PAT-DT-005, PAT-DT-007) and act on them together from a selection bar that states the count and scope ("Archive 48 of 1,203 matching"). Give it a clear exit. While the selection mode is active, disable conflicting per-row actions. Report results, including partial failures ("45 archived, 3 failed — retry"), and announce them (QG-028). Universal guidance: PAT-SH-006.
2. **Undo for routine and recoverable actions; specific confirmation for serious ones.** Archive, move, status changes, and soft delete should run immediately and offer **Undo** in a persistent enough form: a snackbar plus an activity log or trash. Reserve confirmation for irreversible or high-impact actions. The confirmation names the objects and the consequence and uses an action-specific button ("Delete 48 invoices permanently"), not "OK". For legal, financial, or data-modifying submissions, WCAG 3.3.4 requires reversibility, checking, or confirmation (QG-025). Optimistic display is not reversibility. See PAT-SH-011.
3. **Command palette (optional, for command-heavy apps).** Use a single searchable entry point, bound to a documented shortcut, that lists commands, navigation targets, and recent objects. Show each command's shortcut and respect the current context (selection, view). It must be an accessible combobox or listbox dialog. Keep every command also reachable from visible UI. Pick a binding that doesn't collide with the browser or AT (PAT-DT-004). Search fundamentals: PAT-SH-004.
4. **Smart defaults.** Pre-fill from the most likely value, the last-used value, or the current context, such as the current project or today's date. Keep defaults visible and editable. Never silently pre-select costly options.
5. **Recents and working sets.** Provide recent items, pinned or favorite items, and a way to cycle through or return to recently viewed records. This complements browser tabs and does not replace them (PAT-DT-010).
6. **Remember preferences, with explicit scope and reset.** Column layout, density, sort, filters, and default views persist. Decide whether each setting belongs to the *person*, the *device*, or the *workspace*. Show overrides, and give each preference a "Reset to default". Some settings shouldn't sync, such as device-specific density or OS-specific shortcuts. If sync conflicts occur, surface them (PAT-PW-007).
7. **Teach the accelerators gradually.** Show shortcuts beside commands, include "Tip: press E to archive" in context after repeated pointer use, and keep a shortcut reference. Single-character shortcuts follow WCAG 2.1.4 (QG-003).
8. **Accelerators must not exclude.** Bulk actions, palettes, and recents must work by keyboard and screen reader (QG-001) and on touch-capable tablets (PAT-RS-011).

## Evidence

- **E4** Nielsen Norman Group, "Confirmation Dialogs Can Prevent User Errors — If Not Overused". https://www.nngroup.com/articles/confirmation-dialog/. Confirm only serious or irreversible actions. Name objects and consequences, use action-specific choices, and keep undo even with good dialogs. Generic repetition leads to automatic acceptance (F-DX-45, F-NB-30).
- **E4** Nielsen Norman Group, "Accelerators Maximize Efficiency in User Interfaces" and "Flexibility and Efficiency of Use". https://www.nngroup.com/articles/ui-accelerators/, https://www.nngroup.com/articles/flexibility-efficiency-heuristic/. Optional accelerators for recurring tasks, introduced in context. Relying only on shortcuts hurts learnability (F-DX-18, F-NB-07).
- **E4** Nielsen Norman Group, "Preventing User Errors: Avoiding Unconscious Slips". https://www.nngroup.com/articles/slips/. Sensible defaults and constraints reduce slips (F-NB-05).
- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines. A batch-action bar with cancel, and per-row actions disabled in batch mode (F-DX-32).
- **E3** Microsoft Visual Studio Code documentation, "User interface". https://code.visualstudio.com/docs/editing/getting-started/userinterface.md. The Command Palette as a common entry point that also surfaces shortcuts. Cycling through recently used editors and history navigation (F-DX-42, F-DX-43).
- **E3** Microsoft Visual Studio Code documentation, "User and workspace settings" and "Settings Sync". https://code.visualstudio.com/docs/configure/settings.md, https://code.visualstudio.com/docs/configure/settings-sync.md. User vs. workspace scope with per-setting Reset. Selectable sync categories, machine-scoped exclusions, and conflict resolution (F-DX-44, F-DX-51).
- **E3** React documentation, "useOptimistic". https://react.dev/reference/react/useOptimistic. Optimistic updates need rollback on failure (F-DX-28).
- **E1** W3C, WCAG 2.2 SC 3.3.4 Error Prevention (Legal, Financial, Data). https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data. Reversible, checked, or confirmable. A dialog for every action is not required (F-SP-29).

The evidence is **limited**. Command palettes, recents, and preference scoping are documented product conventions from an editor (VS Code, E3). No comparative usability studies of these patterns in web apps were found. The undo-over-confirm guidance is E4 and consistent across sources.

## Alternatives and tradeoffs

- **Palette vs. menu bar vs. toolbar.** A palette scales to hundreds of commands but requires recall of command names. Menus and toolbars support recognition. Command-heavy apps benefit from all three.
- **Undo vs. confirmation.** Undo needs reversible back-end operations (soft delete, a delay before commit). When those aren't feasible, a specific confirmation is the honest choice.
- **Auto-remembered vs. explicitly saved views.** Auto-persisting filters is convenient but can confuse people who don't realize a filter is still active. Show active filters (PAT-SH-005), or offer named saved views.

## Exceptions and failure modes

- Occasional-use apps rarely justify a palette or bulk tooling.
- Common failures: undo only in a toast that vanishes after a few seconds; "select all" that silently means only the visible page; bulk operations with no progress or partial-failure report; preferences with no reset; a palette as the only route to some commands.

## Evaluation questions

- Can a user act on many records at once, with the count and scope stated before acting? [screenshot] [running app]
- Are routine destructive actions undoable, and are irreversible ones confirmed with specific object names and a specific action label? [running app]
- Is there a recovery route beyond a transient toast, such as trash or an activity log? [running app]
- If a command palette exists, is every command in it also reachable from visible UI, and is the palette screen-reader operable? [running app]
- Are recent or pinned items available? [screenshot]
- Do preferences persist with a visible scope and a reset? [running app]
- Do experienced users complete their top repeated tasks in fewer steps than newcomers, without more errors? [user study]

## Related

- Patterns: PAT-SH-004, PAT-SH-005, PAT-SH-006, PAT-SH-011, [PAT-DT-004](PAT-DT-004-keyboard-navigation-shortcuts.md), [PAT-DT-005](PAT-DT-005-focus-selection-management.md), [PAT-DT-007](PAT-DT-007-data-tables-grids.md), [PAT-DT-010](PAT-DT-010-multi-window-resize.md), PAT-RS-004, PAT-RS-011, PAT-PW-007
- Principles: [P-01](../../principles/P-01-task-effectiveness.md), [P-07](../../principles/P-07-input-efficiency.md), [P-11](../../principles/P-11-error-prevention-recovery.md), [P-02](../../principles/P-02-discoverability-learnability.md), [P-14](../../principles/P-14-control-privacy-trust.md)
- Rubric: [D-01, D-04, D-07](../../rubric/dimensions.md); gates [QG-001, QG-003, QG-025, QG-028](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
