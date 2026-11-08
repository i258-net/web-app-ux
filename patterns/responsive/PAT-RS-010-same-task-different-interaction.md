---
id: PAT-RS-010
title: Same task, different interaction — modality-appropriate control variants
type: pattern
scope: responsive
topics: [input-modality, date-entry, select, combobox, filters, multi-select, reorder, drag-and-drop, numeric-entry, text-editing, keyboard]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-07, P-06, P-12, P-09, P-11]
dimensions: [D-04, D-03, D-08, D-10]
gates: [QG-001, QG-018, QG-014, QG-019, QG-040, QG-053, QG-023]
related: [PAT-RS-009, PAT-RS-003, PAT-RS-005, PAT-SH-002, PAT-SH-005, PAT-SH-006, PAT-MO-004, PAT-MO-007, PAT-DT-009, PAT-DT-004]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Same task, different interaction — modality-appropriate control variants

## Problem

Some controls suit a mouse on a wide screen and are awkward with a thumb, or the reverse: a calendar grid of small cells, a 200-item dropdown, drag-only reorder, a slider for an exact number. Teams either ship one control everywhere or fork "mobile" and "desktop" widgets keyed to width, which breaks hybrids (PAT-RS-009) and often drops keyboard support on one side.

## Recommendation

**Outcome:** the task and its result (data, validation, value format) are identical everywhere; the presentation adapts to space and pointer capability, and every variant has a keyboard path.

1. **Pick the variant by space and capability (`any-pointer`), never by width alone.** A compact presentation in a narrow desktop window still accepts mouse and keyboard.
2. **Keep one value model.** Switching presentation on resize preserves value, selection, and draft (PAT-RS-011).
3. **Typed entry is the universal fallback** wherever a value can be typed.
4. **Every drag, path, or multi-point gesture needs a single-pointer, non-drag alternative** (QG-014, QG-018). Keyboard support (QG-001) is required separately and does not satisfy the dragging criterion.

### Worked examples

| Task | Touch-compact variant | Pointer-expanded variant | Keyboard requirement (all variants) |
|---|---|---|---|
| **Date entry** | Native `<input type="date">`, whose picker the browser/OS supplies; or segmented typed fields for dates far from today. | Text field accepting forgiving formats, plus a calendar popover for nearby dates. | Typing the date must work without opening a calendar; any calendar grid supports arrow-key movement and Escape to close. |
| **Single select, many options** | Full-screen searchable list, or the native `<select>`. Targets ≥ 44 px. | Editable combobox: type to filter, suggestions in a popover. | Down Arrow opens the popup, Escape dismisses, Enter accepts; type-ahead in long lists. |
| **Multi-select filters** | Filter panel or tray of checkboxes with an explicit "Show N results" apply step when updates are slow or disruptive. | Persistent sidebar of checkboxes; live updates when fast and the layout stays stable. | Checkboxes in Tab order, or a listbox where Space toggles without modifiers; applied filters removable by keyboard. Avoid relying on `<select multiple>` modifier-clicks. |
| **Reorder** | Visible "Move up / Move down" or "Move to…" controls; optional long-press drag handle that does not fight page scroll. | Drag-and-drop with grab cues and drop previews, *plus* the same Move controls (e.g. in a row menu). | Move commands reachable by focus and Enter; focus follows the moved item; announce the new position. |
| **Numeric entry** | Text field with `inputmode="numeric"` or `"decimal"`; stepper buttons ≥ 44 px for small increments. Slider only when approximate values are acceptable, always with a visible value. | Text field with steppers; slider paired with a field for range-like values. | Field accepts typing; slider supports arrows, Home/End (and optionally Page Up/Down); validation is explicit because `inputmode` does not validate. |
| **Long-text editing** | Full-height editor sized to the visible viewport; formatting toolbar kept clear of the virtual keyboard; autosave. | Inline or pane editor with persistent toolbar and shortcut hints in tooltips/menus. | Every toolbar action has a keyboard path; Tab/Escape leave the editor (no trap); shortcuts do not override browser/AT commands. |

Variants may add accelerators but never remove the baseline path.

## Evidence

- **E3** MDN, "`<input type="date">`". https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date — (verified 2026-11-08) Picker appearance "varies based on the browser and operating system"; displayed date follows locale while `value` is always `yyyy-mm-dd`. MDN does not say when the control is unsuitable; our "far-from-today" advice is interpretation.
- **E3** MDN, "`<select>`". https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select — (verified 2026-11-08) `multiple` uses Ctrl/Command or Shift with click; keyboard multi-selection "not standardized"; tell users more than one option can be selected.
- **E4** W3C WAI, "APG combobox". https://www.w3.org/WAI/ARIA/apg/patterns/combobox/ — Down Arrow enters the popup, Escape dismisses, Enter accepts; editable comboboxes keep platform text editing.
- **E4** W3C WAI, "APG listbox". https://www.w3.org/WAI/ARIA/apg/patterns/listbox/ — Type-ahead recommended in longer lists; recommended multi-select model lets Space toggle without modifiers.
- **E4** W3C WAI, "APG grid". https://www.w3.org/WAI/ARIA/apg/patterns/grid/ — Managed Tab entry and arrow-key navigation for grid composites (e.g. calendars).
- **E4** W3C WAI, "APG slider". https://www.w3.org/WAI/ARIA/apg/patterns/slider/ — Arrow/Home/End keys; some touch AT may not synthesize the key events.
- **E3** MDN, "inputmode". https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode — Hints a virtual keyboard; `numeric` and `decimal` differ; no validity constraint.
- **E1** W3C, "WCAG 2.2 — 2.5.7 Dragging Movements". https://www.w3.org/TR/WCAG22/#dragging-movements and "2.1.1 Keyboard". https://www.w3.org/TR/WCAG22/#keyboard — Non-drag single-pointer alternative; all functionality by keyboard.
- **E4** Nielsen Norman Group, "Drag–and–Drop: How to Design for Ease of Use". https://www.nngroup.com/articles/drag-drop/ — Grab cues, drop previews; dragging can be imprecise or physically hard.
- **E4** Nielsen Norman Group, "User Intent Affects Filter Design". https://www.nngroup.com/articles/applying-filters/ — Batch vs live filtering depends on intent and latency.
- **E4** Baymard Institute, "What Is an Ecommerce Filter? UI Best Practices". https://baymard.com/blog/ecommerce-filter-ui — Deliberate "Show X Results" on mobile; real-time updates generally on desktop.
- **E4** Nielsen Norman Group, "Preventing User Errors: Avoiding Unconscious Slips". https://www.nngroup.com/articles/slips/ — Constraints, defaults, and forgiving formats reduce slips.

*Interpretation (ours):* the variant pairings in the table are synthesis; no source here compares them in a controlled study.

## Alternatives and tradeoffs

- **One control everywhere.** Reasonable when a native control already fits (`<select>` for short lists, `type="date"` for near-term dates); weaker for approximate dates or very long lists.
- **Live vs batch filtering.** Baymard leans batch-on-mobile, live-on-desktop; NN/g conditions it on intent and latency. Decide by measured latency, not width.
- **Custom widgets** buy styling at the cost of owning all keyboard and AT behavior.

## Exceptions and failure modes

- Widget swap at a breakpoint that loses the entered value.
- Drag-only reorder "because there is a mouse".
- Sliders for exact values with no field.
- Unhinted `<select multiple>` as the only multi-select.
- Full-screen pickers that trap focus or break Back (PAT-SH-015).

## Evaluation questions

- For each complex control, can the task be completed by touch, mouse, and keyboard alone in both compact and expanded layouts? [running app]
- Does resizing across the variant boundary preserve the current value? [running app]
- Does every drag operation have a visible non-drag alternative? [screenshot] [running app]
- Can a date or number be typed directly in every variant? [prototype] [running app]
- Do keyboard interactions follow APG contracts for the widget role? [running app] [automated]
- Do participants choose the expected value faster or with fewer errors in the adapted variant? [user study]

## Related

- Principles: [P-07](../../principles/P-07-input-efficiency.md), [P-06](../../principles/P-06-interaction-ergonomics.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-09](../../principles/P-09-consistency-familiarity.md), [P-11](../../principles/P-11-error-prevention-recovery.md)
- Dimensions: D-04, D-03, D-08, D-10; Gates: QG-001, QG-018, QG-014, QG-019, QG-040, QG-053, QG-023
- Patterns: [PAT-RS-009](PAT-RS-009-input-detection-touch-vs-pointer.md) (capability detection), [PAT-RS-003](PAT-RS-003-content-prioritization.md), PAT-SH-002, PAT-SH-005, PAT-SH-006, PAT-MO-004, PAT-MO-007, PAT-DT-009, PAT-DT-004

## Change log

- 2026-11-08 — Initial version (ADR-001).
