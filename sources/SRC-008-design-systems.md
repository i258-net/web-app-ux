---
id: SRC-008
title: Design systems and product documentation (Carbon, Atlassian, React, VS Code, Adrian Roselli)
type: source
publisher: IBM Carbon; Atlassian; Meta (React); Microsoft (Visual Studio Code); Adrian Roselli
evidence_classes: [E3, E4]
status: active
updated: 2026-11-08
---

# SRC-008 Design systems and product documentation

## Publisher and scope

This file groups the design-system, framework, and product documentation, plus one accessibility practitioner, that the findings cite. All of it comes from the desktop and tablet assignment (DX).

| Publisher | What was used | Findings |
|---|---|---|
| **IBM Carbon Design System** | Data table guidelines: width, row density, row actions on hover or focus, sorting, selection and bulk actions, pagination | F-DX-02, 05, 12, 29, 31, 32 |
| **Atlassian (Forge UI Kit)** | Inline edit component: read and edit views, save and cancel | F-DX-26, 27 |
| **React (Meta)** | `useOptimistic` reference: optimistic UI and reverting on failure | F-DX-28 |
| **Adrian Roselli** | *A Responsive Accessible Table*: keeping table semantics when layouts reflow | F-DX-34, 35 |
| **Microsoft Visual Studio Code docs** | User interface (command palette and shortcut discovery), user versus workspace settings, Settings Sync | F-DX-42, 43, 44, 51 |

**Not cited.** The findings do **not** cite Shopify Polaris, Microsoft Fluent, or other design systems. Do not cite them from this register until a finding fetches them. The Atlassian Design System's inline-edit page (`atlassian.design`) returned no readable content, so the Forge UI Kit documentation was used instead.

These sources are strongest on desktop and data-dense behavior: tables, inline editing, command discovery, and preference scope. The general UX literature covers these areas thinly.

## How to classify their material

| Output | Class | Why |
|---|---|---|
| Design-system component guidance (Carbon, Atlassian) | **E3** for that design system | A widely adopted system's documented convention. It is not evidence that the pattern is usable for everyone |
| Design-system rationale text ("we recommend X because…") | **E4** | Reasoning without a described study |
| Framework API documentation (React) | **E3** | Platform and implementation documentation. It shows how optimistic UI works, not when users benefit from it |
| Product documentation (VS Code) | **E3** as a documented convention of a widely used expert tool | Describes what one shipped product does and documents. Treat it as close to E5 when generalizing |
| Practitioner article (Adrian Roselli) | **E4** | Expert accessibility practice with tested code, but no described user study |

## Licensing and access

Everything was free to read. The Carbon documentation is open source (Apache 2.0 for the code; check its site for documentation terms). Atlassian, React, and VS Code documentation is published by the vendors, and react.dev content is CC BY 4.0. Adrian Roselli's article is the author's copyright. Paraphrase all of it, quote a phrase at most, and do not copy component screenshots.

## Known limitations and biases

- **Each system serves its own products.** Carbon targets IBM enterprise software, and Atlassian targets Jira and Confluence. Their defaults (density, hover-revealed row actions) reflect expert, desktop-heavy users.
- **No comparative usability evidence.** Density options, remembered defaults, command palettes, and settings sync are supported mainly by documentation, not by comparative studies (DX coverage).
- **Hover-revealed actions conflict with NN/g.** Carbon allows row controls that appear on hover or focus, with a touch fallback. NN/g warns that hidden actions are costly to discover (DX disagreements). Optional acceleration should never be the only route to a task.
- **Stacked tables.** Roselli's article and Carbon pagination address simple tables. Complex headers, virtualization, and spreadsheet editing need implementation-specific testing.
- **Implementation dependence.** React's `useOptimistic` is a framework detail. The UX principle behind it, visible pending state plus real recovery, does not depend on React.

## Cited pages

All rows were accessed 2026-11-08.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Data table | <https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines> | 2026-09-30 | 2026-11-08 | E3 | F-DX-02, F-DX-05, F-DX-12, F-DX-29, F-DX-31, F-DX-32 |
| Inline edit | <https://developer.atlassian.com/platform/forge/ui-kit/components/inline-edit/> | 2025-07-18 | 2026-11-08 | E3 | F-DX-26, F-DX-27 |
| useOptimistic | <https://react.dev/reference/react/useOptimistic> | not shown | 2026-11-08 | E3 | F-DX-28 |
| A Responsive Accessible Table | <https://adrianroselli.com/2017/11/a-responsive-accessible-table.html> | 2017-11-02; updated 2026-10-06 | 2026-11-08 | E4 | F-DX-34, F-DX-35 |
| User interface | <https://code.visualstudio.com/docs/editing/getting-started/userinterface.md> | not shown | 2026-11-08 | E3 | F-DX-42, F-DX-43 |
| User and workspace settings | <https://code.visualstudio.com/docs/configure/settings.md> | not shown | 2026-11-08 | E3 | F-DX-44 |
| Settings Sync | <https://code.visualstudio.com/docs/configure/settings-sync.md> | not shown | 2026-11-08 | E3 | F-DX-51 |

### Failed fetches (not evidence)

| URL | Outcome | Replacement |
|---|---|---|
| <https://atlassian.design/components/inline-edit/> | No readable article content | Forge UI Kit Inline edit (F-DX-26, F-DX-27) |
