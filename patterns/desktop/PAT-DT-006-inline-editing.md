---
id: PAT-DT-006
title: Inline editing — edit-in-place, save and cancel semantics, autosave, optimistic updates
type: pattern
scope: desktop
topics: [inline-edit, edit-in-place, autosave, save-cancel, blur, optimistic-ui, rollback, layout-shift]
platforms: [desktop, tablet, mobile]
viewports: [medium, expanded, large, extra-large]
inputs: [pointer, keyboard, touch, assistive-tech]
principles: [P-07, P-01, P-10, P-11]
dimensions: [D-04, D-07, D-01]
gates: [QG-001, QG-002, QG-022, QG-023, QG-025, QG-028, QG-072, QG-082]
related: [PAT-DT-005, PAT-DT-007, PAT-SH-002, PAT-SH-003, PAT-SH-009, PAT-PW-007, PAT-PW-008, PAT-MO-011, PAT-RS-010]
evidence_strength: limited
status: active
updated: 2026-11-08
---

# Inline editing — edit-in-place, save and cancel semantics, autosave, optimistic updates

## Problem

Editing a value where it is displayed, such as a title, a status, or a table cell, avoids a round trip to a form. It removes friction for people who make many small changes. The cost is ambiguity. Is this text editable? Am I in edit mode now? Did leaving the field save my change, discard it, or do nothing? Is the green check a confirmed server save or just local optimism? Inline editors also shift the layout when the edit view is a different size from the read view. Long text edits are easily lost to an accidental click elsewhere.

## Recommendation

**Outcome:** people can see what is editable. Entering and leaving edit mode is predictable for every input. Nobody loses or saves work without knowing.

1. **Signal editability.** Use a visible affordance: a hover or focus outline, a pencil icon, or a persistent "Edit" button. Do not rely on a hover-only cue (PAT-DT-003). The read view should be a focusable control whose accessible name includes the field label and its value. A plain `div` with a click handler does not qualify.
2. **Make the edit view the same size and position as the read view.** Same font, baseline, and width, so entering edit mode doesn't push content around. Unexpected layout shift also counts against CLS (QG-082).
3. **Specify the full commit contract and keep it consistent across the app.**

   | Trigger | Short single-line field | Long or multi-line text, rich content |
   |---|---|---|
   | Enter | Save | New line (Ctrl/⌘+Enter saves) |
   | Escape | Cancel, revert to the last saved value | Cancel, with confirmation if there is substantial change |
   | Blur (click or Tab away) | Save, or keep open if invalid | **Keep open**, do not save or discard silently |
   | Explicit ✓ / ✕ buttons | Provide them when space allows | Always provide them |

   Return focus to the read view after save or cancel (PAT-DT-005).
4. **Validate before committing.** Show errors inline next to the field and keep the edit open with the input preserved (QG-022, QG-072). Field-level validation rules are in PAT-SH-003.
5. **Separate pending from confirmed.** If the UI updates optimistically, show a subtle pending state, then "Saved" once the server confirms. Announce it in a live region (QG-028). If the save fails, **revert or keep the user's value visibly marked as unsaved**, explain the problem, and offer retry. Restore focus sensibly. Never show a success state that the server later contradicts without telling the user.
6. **Autosave only with visible status.** For documents and long forms, autosave can replace explicit Save. It needs a persistent status ("Saving…", "Saved 2 min ago", "Offline — changes queued"), and conflicts must surface. Drafts, `beforeunload`, and sync are covered in PAT-PW-007 and PAT-PW-008.
7. **Offer a form when inline editing gets heavy.** If editing one record touches many related fields, or needs a review before commit, open a detail panel or form instead of chaining inline editors.
8. **Use the grid contract for table cells.** In an interactive grid, Enter or F2 starts editing a cell, and Escape or F2 returns to navigation (PAT-DT-007).

## Evidence

- **E3** Atlassian Forge UI Kit, "Inline edit". https://developer.atlassian.com/platform/forge/ui-kit/components/inline-edit/. Read and edit views on the same page, aligned to avoid a jarring transition (F-DX-26). Confirm and cancel controls kept when unobstructed. Large text edits stay open on blur to avoid accidental save or discard (F-DX-27).
- **E3** React documentation, "useOptimistic". https://react.dev/reference/react/useOptimistic. Show an optimistic value while an action is pending. The delete example restores the item and shows an error on failure (F-DX-28).
- **E3** W3C WAI APG, "Grid Pattern". https://www.w3.org/WAI/ARIA/apg/patterns/grid/. Enter or F2 enters cell editing, and Escape or F2 restores navigation (F-SP-43).
- **E2** Baymard Institute, "Checkout UX: Avoid 'Apply' Buttons for Most Fields". https://baymard.com/research-articles/checkout-usability-apply-buttons. In checkout tests, shoppers missed intermediate Apply/Save buttons, which left data unsaved (F-NB-59). This is e-commerce evidence. Applying it to inline editors means "do not depend on a separate per-field save button people may miss", and that application is our interpretation.
- **E4** Nielsen Norman Group, "Visibility of System Status". https://www.nngroup.com/articles/visibility-system-status/. Silent changes to user-owned content undermine trust (F-NB-01).
- **E1** W3C, WCAG 2.2 SC 4.1.3 Status Messages. https://www.w3.org/TR/WCAG22/#status-messages. Save results are announced without moving focus (F-SP-32).

The evidence is **limited**. Component documentation (E3) is consistent, but no comparative study of inline editing against forms, or of blur-save against blur-keep, was found. The blur-behavior table is a synthesis of the Atlassian policy and is not tested guidance.

## Alternatives and tradeoffs

- **Explicit edit mode for the whole record** (one Edit button, then Save/Cancel for all fields). Slower for single changes, but clearer about scope. It is better for related fields that must change together or need review (WCAG 3.3.4 contexts: QG-025).
- **Always-editable fields** (like a spreadsheet or settings that apply at once). Fastest, but there is no read state and accidental edits are more likely. Pair with undo.
- **Save on blur vs. keep open on blur.** Blur-save matches spreadsheet expectations for short values. Keep-open protects long input. Mixing them unpredictably is the real failure.
- **Optimistic vs. pessimistic updates.** Optimistic feels instant on reliable networks. For irreversible, financial, or high-conflict data, wait for confirmation.

## Exceptions and failure modes

- On touch-only compact screens, a full-screen editor or bottom sheet often works better than a tiny inline field (PAT-MO-011, PAT-RS-010).
- Common failures: editable text with no hover or focus cue; Escape that saves; edit mode that can't be left by keyboard (QG-002); "Saved" shown before the request completes; validation errors only in a toast (PAT-SH-009).

## Evaluation questions

- Can a first-time user tell which values are editable, without hovering? [screenshot] [user study]
- Does entering edit mode cause visible layout shift? [running app] [automated]
- Do Enter, Escape, blur, and ✓/✕ behave per the documented contract, the same way in every editor? [running app]
- Does a long text edit survive an accidental click outside? [running app]
- With the network throttled or failing, does the UI show pending, then error, and keep or revert the value with a retry? [running app]
- Is "Saved" announced to screen readers? [running app] [automated]
- Is focus returned to the read view after commit? [running app]

## Related

- Patterns: [PAT-DT-005](PAT-DT-005-focus-selection-management.md), [PAT-DT-007](PAT-DT-007-data-tables-grids.md), PAT-SH-002, PAT-SH-003, PAT-SH-009, PAT-PW-007, PAT-PW-008, PAT-MO-011, PAT-RS-010
- Principles: [P-07](../../principles/P-07-input-efficiency.md), [P-01](../../principles/P-01-task-effectiveness.md), [P-10](../../principles/P-10-feedback-predictability.md), [P-11](../../principles/P-11-error-prevention-recovery.md)
- Rubric: [D-04, D-07, D-01](../../rubric/dimensions.md); gates [QG-001, QG-002, QG-022, QG-023, QG-025, QG-028, QG-072, QG-082](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
