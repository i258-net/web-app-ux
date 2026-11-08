---
id: SRC-005
title: Google Material Design 3 and Android adaptive guidance
type: source
publisher: Google (Material Design; Android Developers)
evidence_classes: [E3]
status: active
updated: 2026-11-08
---

# SRC-005 Material Design 3 and Android adaptive guidance

## Publisher and scope

Google's Material Design 3 (M3) is an open design system for Android, Flutter, and the web. Research used these M3 pages:

- breakpoints and window-size classes
- canonical layouts (list-detail, supporting pane, feed)
- interaction states
- accessible design: spacing, targets, and contrast
- navigation bar, navigation rail, and navigation drawer
- text fields, dialogs, snackbars, and bottom sheets
- floating action buttons (FAB), menus, lists, and search

Two Android Developers pages on adaptive apps supplied window-size-class and resizability guidance (F-DX-39, F-DX-46).

M3's strengths are explicit adaptive-layout guidance across five width classes (under 600dp, 600–839dp, 840–1199dp, 1200–1599dp, and 1600dp or wider), numeric target and spacing guidance, and component-level accessibility notes.

**How content was read.** The canonical m3.material.io pages load as a JavaScript shell. Research fetched the **published JSON content payloads** the site uses (version `2026-10-13_06-10-19`) and recorded both the canonical page and the payload URL in each finding. The payload version shows when the content was retrieved, not when the page was published. A runtime JavaScript asset was also fetched to identify the published routes.

## How to classify their material

| Output | Class | Why |
|---|---|---|
| M3 component, layout, and accessibility guidance | **E3** | A widely adopted design system's convention. Authoritative for Material-styled and Android-expected UI, **not** universal web rules |
| Android Developers adaptive-app guides | **E3** | Platform-owner implementation guidance for Android |
| Numeric values: 48×48dp touch targets with 8dp separation, 44×44dp pointer targets, and 4–10 s snackbar timing | **E3 recommended values** | May anchor a labelled recommended threshold. They are never WCAG equivalents |
| "Expressive" update notes | **E3, dated** | They change recommendations, for example from drawer to expanded rail. Cite the update month |

## Licensing and access

M3 documentation is free to read. Material code and components are open source under Apache 2.0. Treat the documentation text and imagery as Google content: paraphrase it, quote labels and numbers with units, and do not copy illustrations. The JSON payloads were fetched from the official domain only to read the published text, and nothing was redistributed.

## Known limitations and biases

- **Dates.** Most M3 pages show no publication date, so the table records "not shown". Some pages show an Expressive update month, which is recorded where it appeared.
- **Version overlap.** The baseline navigation drawer page is still published, but the May 2025 Expressive update recommends expanded rails instead. Breakpoint, rail, and drawer pages contain overlapping or broad sentences. Keep the version and context, and do not merge them into one unconditional rule (SP disagreement 5).
- **No data table.** The M3 route inventory has no data-table component page. Table guidance comes from the APG, WCAG, and Carbon instead.
- **The window-size-class page failed.** `https://m3.material.io/foundations/layout/applying-layout/window-size-classes` returned 404. The Android "Use window size classes" guide replaced it.
- **Units.** dp is not CSS px, and its breakpoints are window classes for Android, not required CSS breakpoints. WCAG reflow widths (320 CSS px) are conformance conditions, not design breakpoints.
- **Snackbar timing is not accessibility.** The 4–10 s range alone establishes neither WCAG timing conformance nor announcement by assistive technology. M3's own web guidance requires an accessible alternative.
- **Platform bias.** Following Material conventions in a web app may feel foreign to iOS users. Choose deliberately.

## Cited pages

All rows were accessed 2026-11-08. Each canonical page is followed by the published payload that was actually read.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| App orientation, aspect ratio, and resizability | <https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability> | 2026-10-28 | 2026-11-08 | E3 | F-DX-39 |
| Use window size classes | <https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes> | 2026-10-23 | 2026-11-08 | E3 | F-DX-46 |
| Material Design 3: foundations/layout/breakpoints | <https://m3.material.io/foundations/layout/breakpoints> | not shown / May 2025 Expressive update shown on navigation component pages; breakpoint publication date not shown | 2026-11-08 | E3 | F-SP-65, F-SP-72 |
| Published content payload for Material Design 3: foundations/layout/breakpoints | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/16281dc1-7630-4e78-abaf-c9bc8be69663.json> | not shown / May 2025 Expressive update shown on navigation component pages; breakpoint publication date not shown | 2026-11-08 | E3 | F-SP-65, F-SP-72 |
| Material Design 3: foundations/layout/canonical-examples | <https://m3.material.io/foundations/layout/canonical-examples> | not shown | 2026-11-08 | E3 | F-SP-66, F-SP-67, F-SP-68 |
| Published content payload for Material Design 3: foundations/layout/canonical-examples | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/23b84814-755b-469b-83a9-771fe027b0c0.json> | not shown | 2026-11-08 | E3 | F-SP-66, F-SP-67, F-SP-68 |
| Material Design 3: foundations/interaction/states | <https://m3.material.io/foundations/interaction/states> | not shown | 2026-11-08 | E3 | F-SP-69 |
| Published content payload for Material Design 3: foundations/interaction/states | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/b3339b30-4a6d-49b6-9a8b-8e581b2b1204.json> | not shown | 2026-11-08 | E3 | F-SP-69 |
| Material Design 3: foundations/designing | <https://m3.material.io/foundations/designing> | not shown | 2026-11-08 | E3 | F-SP-70, F-SP-71 |
| Published content payload for Material Design 3: foundations/designing | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/d352451b-8348-4816-abac-4d7983f72f88.json> | not shown | 2026-11-08 | E3 | F-SP-70, F-SP-71 |
| Material Design 3: components/navigation-bar | <https://m3.material.io/components/navigation-bar> | May 2025 Expressive update shown on navigation component pages; breakpoint publication date not shown | 2026-11-08 | E3 | F-SP-72 |
| Published content payload for Material Design 3: components/navigation-bar | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/9e4cdffa-f7fd-425f-9915-867aafbcc7d6.json> | May 2025 Expressive update shown on navigation component pages; breakpoint publication date not shown | 2026-11-08 | E3 | F-SP-72 |
| Material Design 3: components/navigation-rail | <https://m3.material.io/components/navigation-rail> | May 2025 Expressive update shown on navigation component pages; breakpoint publication date not shown | 2026-11-08 | E3 | F-SP-72 |
| Published content payload for Material Design 3: components/navigation-rail | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/98fe42bd-9bb1-4307-9e92-e61e57c3e9da.json> | May 2025 Expressive update shown on navigation component pages; breakpoint publication date not shown | 2026-11-08 | E3 | F-SP-72 |
| Material Design 3: components/navigation-drawer | <https://m3.material.io/components/navigation-drawer> | May 2025 Expressive update shown on navigation component pages; breakpoint publication date not shown | 2026-11-08 | E3 | F-SP-72 |
| Published content payload for Material Design 3: components/navigation-drawer | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/d2a1a290-0db4-4622-8a4b-bd11b6a4ec8d.json> | May 2025 Expressive update shown on navigation component pages; breakpoint publication date not shown | 2026-11-08 | E3 | F-SP-72 |
| Material Design 3: components/text-fields | <https://m3.material.io/components/text-fields> | not shown | 2026-11-08 | E3 | F-SP-73 |
| Published content payload for Material Design 3: components/text-fields | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/8741ef66-1a80-4b39-adb1-66bea5e6992f.json> | not shown | 2026-11-08 | E3 | F-SP-73 |
| Material Design 3: components/dialogs | <https://m3.material.io/components/dialogs> | not shown | 2026-11-08 | E3 | F-SP-74 |
| Published content payload for Material Design 3: components/dialogs | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/79c01ab5-d09a-4f6c-9aca-f76d310583bc.json> | not shown | 2026-11-08 | E3 | F-SP-74 |
| Material Design 3: components/snackbar | <https://m3.material.io/components/snackbar> | not shown | 2026-11-08 | E3 | F-SP-75 |
| Published content payload for Material Design 3: components/snackbar | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/26cf2750-80f7-43f8-a155-834aa01276df.json> | not shown | 2026-11-08 | E3 | F-SP-75 |
| Material Design 3: components/bottom-sheets | <https://m3.material.io/components/bottom-sheets> | not shown | 2026-11-08 | E3 | F-SP-76 |
| Published content payload for Material Design 3: components/bottom-sheets | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/aa6f9af2-d539-4b22-9af5-838e7cfc4a85.json> | not shown | 2026-11-08 | E3 | F-SP-76 |
| Material Design 3: components/floating-action-button | <https://m3.material.io/components/floating-action-button> | May 2025 Expressive update | 2026-11-08 | E3 | F-SP-77 |
| Published content payload for Material Design 3: components/floating-action-button | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/1e52f150-575c-45fa-8f5f-75868c5ab068.json> | May 2025 Expressive update | 2026-11-08 | E3 | F-SP-77 |
| Material Design 3: components/menus | <https://m3.material.io/components/menus> | November 2025 Expressive update | 2026-11-08 | E3 | F-SP-78 |
| Published content payload for Material Design 3: components/menus | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/24b60c3f-1ec7-48df-b175-0d8e011a8106.json> | November 2025 Expressive update | 2026-11-08 | E3 | F-SP-78 |
| Material Design 3: components/lists | <https://m3.material.io/components/lists> | December 2025 Expressive update | 2026-11-08 | E3 | F-SP-79 |
| Published content payload for Material Design 3: components/lists | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/6d4033c2-f92c-4c43-b585-b3bce8468d48.json> | December 2025 Expressive update | 2026-11-08 | E3 | F-SP-79 |
| Material Design 3: components/search | <https://m3.material.io/components/search> | February 2025 Expressive update | 2026-11-08 | E3 | F-SP-80 |
| Published content payload for Material Design 3: components/search | <https://m3.material.io/_dsm/content/m3/2026-10-13_06-10-19/22081e54-b56a-47b2-b137-9ba82953f05e.json> | February 2025 Expressive update | 2026-11-08 | E3 | F-SP-80 |

### Fetched but not cited by a numbered finding

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| M3 runtime asset (route inventory) | <https://m3.material.io/static/angular/main.de4ba8c67aed3c29.js> | not shown | 2026-11-08 | n/a (retrieval provenance) | none (SP coverage section) |

### Failed fetches (not evidence)

| URL | Outcome | Replacement |
|---|---|---|
| <https://m3.material.io/foundations/layout/applying-layout/window-size-classes> | HTTP 404 | Android "Use window size classes" (F-DX-46) |

### Cited in principles only

None of these appear in any findings fetch log. Fetch them and add a finding before relying on them.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Material Design 3, Accessibility (touch targets) | <https://m3.material.io/foundations/accessible-design/accessibility-basics> | not recorded | not recorded | E3 | none (principle only: P-06) |
| Material Design 3 (home) | <https://m3.material.io/> | not recorded | not recorded | E3 | none (principle only: P-09) |
| Material Design 3, Motion | <https://m3.material.io/styles/motion/overview> | not recorded | not recorded | E3 | none (principle only: P-15) |
