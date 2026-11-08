---
id: PAT-DT-001
title: Wide layouts — readable measure, purposeful columns, and task-appropriate density
type: pattern
scope: desktop
topics: [layout, line-length, measure, max-width, multi-column, whitespace, density, expert-users]
platforms: [desktop, tablet]
viewports: [expanded, large, extra-large]
inputs: [pointer, keyboard, touch, assistive-tech]
principles: [P-08, P-05, P-01, P-12]
dimensions: [D-05, D-06, D-10]
gates: [QG-009, QG-010, QG-011, QG-019, QG-050]
related: [PAT-DT-002, PAT-DT-007, PAT-DT-010, PAT-DT-011, PAT-RS-002, PAT-RS-004, PAT-RS-008, PAT-RS-009, PAT-RS-011]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Wide layouts — readable measure, purposeful columns, and task-appropriate density

## Problem

A large window offers room that a phone does not, and teams usually waste it in one of two ways. Some stretch a single mobile column across 1,600 px. Lines of prose then run too long to read comfortably, and controls drift far from the content they act on. Others fill every pixel with panels and shrink the type until nothing has a clear hierarchy. Both mistakes treat width as the goal. What matters is what the person needs to see *at the same time*: read a document, compare records, or keep a list and a detail together.

## Recommendation

**Outcome:** on expanded and larger windows, people read prose at a comfortable measure. Related things they need together sit side by side, and density fits the task rather than the device.

1. **Constrain prose, not the page.** Give running text a maximum measure set in font-relative units, aiming at about 50–75 characters per line. Then check the measure you actually render, because `ch` is not an exact character count. This cap belongs to text blocks, not to the whole layout.
2. **Give comparison surfaces the width they need.** Tables, boards, timelines, and canvases should get the greatest width on the page instead of inheriting the prose cap (see PAT-DT-007).
3. **Add columns only for a relationship.** Use a second or third pane when the content is related: list–detail for parent–child items, or a supporting pane for secondary content tied to the primary task. Do not add panes just to fill empty space. Choose the layout from the task (PAT-RS-002), and keep the current selection highlighted so people know where the detail came from.
4. **Use whitespace to show grouping.** Put related controls and fields close together and separate groups with space, containers, or dividers. Do not spread a toolbar evenly across a wide bar. Keep actions near the object they affect.
5. **Treat density as a task setting.** Repetitive expert work, such as triage, monitoring, or data entry, can justify compact rows and smaller spacing. Occasional or reading-heavy work should not be compact. Where users differ, offer a remembered density preference with a clear scope (PAT-DT-011, PAT-RS-004). Compact mode must still meet target-size minimums (QG-019) and keep visible focus.
6. **Do not infer the user from the width.** A wide window can belong to a touch tablet or a touchscreen laptop. A desktop browser can be resized narrow. Density and target-size choices follow input capability (PAT-RS-009). Pane count follows available space (PAT-DT-010).
7. **Survive zoom and text overrides.** Wide multi-pane layouts must still reflow at 320 CSS px (QG-010). They must stay usable at 200% text size (QG-009) and with WCAG text-spacing overrides (QG-011), without clipping or overlap.

## Evidence

- **E2** Baymard Institute, "Readability: The Optimal Line Length". https://baymard.com/research-articles/line-length-readability. Recommends 50–75 characters per line for body text and reports that overly long product descriptions discouraged reading in e-commerce testing (F-DX-01). Applying this to non-commerce reading is our interpretation.
- **E2** Nielsen Norman Group, "Mobile First Is NOT Mobile Only". https://www.nngroup.com/articles/mobile-first-not-mobile-only/. Attributes poor desktop navigation use to patterns carried over from mobile, and argues that each platform's space should shape its design (F-NB-14).
- **E3** IBM Carbon Design System, "Data table — Guidelines". https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines. Gives tables ample main-content width to avoid cramped, truncated data (F-DX-02). Offers row sizes from dense to spacious (F-DX-05).
- **E3** Apple Human Interface Guidelines, "Layout". https://developer.apple.com/design/human-interface-guidelines/layout.md. Grouping through alignment, negative space, containers, or separators (F-DX-03). Layout follows available size, not device type (F-DX-37).
- **E3** Apple Human Interface Guidelines, "Designing for macOS". https://developer.apple.com/design/human-interface-guidelines/designing-for-macos.md. Use large displays to reduce nesting and modality without excessive density (F-SP-64).
- **E3** Google Material Design, "Canonical layouts". https://m3.material.io/foundations/layout/canonical-examples. Supporting-pane and list-detail layouts chosen from content relationships (F-SP-67, F-SP-68).
- **E4** Nielsen Norman Group, "Aesthetic and Minimalist Design". https://www.nngroup.com/articles/aesthetic-minimalist-design/. Minimalism means removing noise, not removing useful elements (F-NB-08).
- **E1** W3C, WCAG 2.2 SC 1.4.10 Reflow and 1.4.12 Text Spacing. https://www.w3.org/TR/WCAG22/#reflow, https://www.w3.org/TR/WCAG22/#text-spacing. The normative floor for zoomed and overridden layouts.
- **E5** Mobbin, "Explore web app designs". https://mobbin.com/explore/web. Multi-column layouts recur in communication and operational apps (F-DX-61). This is convention observed, not proof of usability.

No source sets a universal maximum page width, and no source sets a density optimum for web apps. The 50–75 character range applies to prose only.

## Alternatives and tradeoffs

- **Single centered column.** This is right for reading-first pages (articles, settings, simple forms), even on very wide screens. Empty margins are acceptable when nothing related needs to sit alongside.
- **Fluid full-width layout.** This suits canvases, maps, and spreadsheets. Prose inside it still needs its own measure cap.
- **Fixed density vs. user toggle.** A toggle serves mixed audiences but doubles visual QA. A single well-chosen default is cheaper and fine when the user base is homogeneous.
- **Breathing room vs. information per screen.** Apple and Carbon both allow dense layouts but warn against excess. The right balance comes from the task, not from a rule.

## Exceptions and failure modes

- Applying the prose `max-width` to the app shell, which cramps tables and leaves wide gutters.
- Adding a third pane that duplicates navigation or shows unrelated promotions.
- A compact density that drops targets below 24 px or removes focus outlines.
- Multi-pane layouts that break at 200% zoom, because zoom effectively turns a large window into an expanded or medium one (PAT-DT-010).
- CJK and other scripts: the character range comes from English-language guidance and does not transfer directly.

## Evaluation questions

- At 1440 and 1920 px, does body prose stay roughly within 50–75 characters per line? [screenshot]
- Do tables and comparison views get more width than prose, rather than sharing its cap? [screenshot]
- Does each extra column hold content related to the primary task? [screenshot]
- Are controls grouped near the objects they act on, not spread across the width? [screenshot]
- If a density setting exists, is it remembered, scoped clearly, and do compact targets still meet 24 px? [running app] [automated]
- At 200% zoom and with text-spacing overrides, does the layout reflow without clipping? [running app]
- Do expert users complete repetitive tasks faster in the dense mode without more errors? [user study]

## Related

- Patterns: [PAT-DT-002](PAT-DT-002-sidebar-hierarchical-navigation.md), [PAT-DT-007](PAT-DT-007-data-tables-grids.md), [PAT-DT-010](PAT-DT-010-multi-window-resize.md), [PAT-DT-011](PAT-DT-011-expert-workflows.md), PAT-RS-002, PAT-RS-004, PAT-RS-008, PAT-RS-009, PAT-RS-011
- Principles: [P-08](../../principles/P-08-visual-hierarchy-readability.md), [P-05](../../principles/P-05-cognitive-clarity.md), [P-01](../../principles/P-01-task-effectiveness.md), [P-12](../../principles/P-12-accessibility-inclusion.md)
- Rubric: [D-05, D-06, D-10](../../rubric/dimensions.md); gates [QG-009, QG-010, QG-011, QG-019, QG-050](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
