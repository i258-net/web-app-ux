---
id: SRC-004
title: Apple Human Interface Guidelines
type: source
publisher: Apple
evidence_classes: [E3]
status: active
updated: 2026-11-08
---

# SRC-004 Apple Human Interface Guidelines

## Publisher and scope

Apple's Human Interface Guidelines (HIG) document design conventions for iOS, iPadOS, macOS, watchOS, tvOS, and visionOS. Research used the following HIG pages:

- layout and safe areas
- accessibility, gestures, and buttons
- tab bars, sidebars, split views, and toolbars (which now include navigation bars)
- modality, sheets, and alerts
- typography and Dynamic Type
- inputs, feedback, loading, and onboarding
- entering data and virtual keyboards
- searching and menus
- designing for iPadOS, multitasking, and pointing devices
- designing for macOS and keyboards

It also used one Apple Support article on iPad multitasking (F-DX-38). The HIG's strengths are precise, current platform conventions with change logs, and explicit treatment of compact and regular size classes, pointers, and keyboards on iPad and Mac.

HTML pages on the HIG site load as a JavaScript shell. Apple's **official Markdown representations** (`…/<page>.md`) were fetched instead. Where the fetch tool rejected the Markdown MIME type, a direct HTTP request was used (DX coverage). The HTML and `.md` paths are the same document.

## How to classify their material

| Output | Class | Why |
|---|---|---|
| HIG guidance, size tables, and component conventions | **E3 (Apple platforms)** | Platform-owner convention. Authoritative for what Apple users expect. **Not** a web requirement |
| Apple Support articles | **E3** | Product documentation of OS behavior, which varies by OS release and device model |
| Native APIs, controls, and materials | Not transferable as such | A PWA does not get native semantics, pointer effects, or size classes |

Under `evidence-classes.md`, Apple figures never back a web quality gate on their own. They can anchor a clearly labelled *recommended* comfort threshold.

**Control sizes (F-SP-48).** The current Accessibility page (updated June 9, 2025) has a table with two columns: **Default control size** and **Minimum control size**. For **iOS and iPadOS** it lists **44×44 pt as the default** and **28×28 pt as the minimum**. For macOS it lists 28×28 pt default and 20×20 pt minimum, and for watchOS 44×44 pt default and 28×28 pt minimum. It recommends about 12 pt padding around bezelled controls and about 24 pt around the visible edges of controls without a bezel.

The common shorthand "Apple requires a 44 pt minimum" is **not** what the current page says. Patterns must not call 44 pt Apple's minimum. The Inputs page is a directory of input methods and gives no numerical hit-region rule.

## Licensing and access

The HIG is free to read and is copyrighted by Apple. Quote labels and numbers with their units. Paraphrase prose. Do not reproduce Apple artwork, SF Symbols, or screenshots. No authentication was needed.

**Two Apple paths returned HTTP 404 during research** (SP coverage):

- `https://developer.apple.com/design/human-interface-guidelines/navigation-bars.md`. Navigation-bar guidance was verified in **Toolbars**, whose change log records that it absorbed navigation bars.
- `https://developer.apple.com/design/human-interface-guidelines/touchscreens.md`. The Inputs directory has no standalone touchscreens entry. Numerical control sizes were verified in **Accessibility**.

The fetch tool also failed twice on Markdown content type, for the sidebar and multitasking pages. Direct HTTP fetches of both returned status 200.

## Known limitations and biases

- **Native only.** Apple conventions describe native apps. Copying iOS chrome into a web app can confuse Android and desktop users. The HIG does not establish equivalent support in a PWA.
- **Units.** Apple uses points (pt), which are not CSS px, Material dp, or millimetres. WCAG 2.5.8 (24×24 CSS px) answers a different question (SRC-001).
- **Contrast table.** The Accessibility page's contrast table includes a broad "all bold: 3:1" row and an Increase Contrast fallback that differ from WCAG wording. Do not use them to relax web contrast tests.
- **Version churn.** Many pages show 2025–2026 change-log dates, and iPad windowing behavior varies by OS release and model. Always cite the date.
- **No thresholds for responsive design.** The HIG gives no universal thumb-reach zone or CSS breakpoint.
- **Commercial interest.** Apple promotes its own platform idioms.

## Cited pages

All rows were accessed 2026-11-08. Dates are the change-log dates shown on each page.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Layout | <https://developer.apple.com/design/human-interface-guidelines/layout.md> | 2026-09-09 | 2026-11-08 | E3 | F-DX-03, F-DX-37, F-SP-47, F-SP-56 |
| Split views | <https://developer.apple.com/design/human-interface-guidelines/split-views.md> | 2025-06-09 | 2026-11-08 | E3 | F-DX-04 |
| Sidebars | <https://developer.apple.com/design/human-interface-guidelines/sidebars.md> | 2026-06-08 | 2026-11-08 | E3 | F-DX-08, F-DX-09, F-SP-52 |
| Use multitasking on your iPad | <https://support.apple.com/en-us/102576> | 2026-05-14 | 2026-11-08 | E3 | F-DX-38 |
| Pointing devices | <https://developer.apple.com/design/human-interface-guidelines/pointing-devices.md> | 2026-10-28 | 2026-11-08 | E3 | F-DX-52, F-SP-63, F-SP-64 |
| Apple HIG: inputs | <https://developer.apple.com/design/human-interface-guidelines/inputs.md> | not shown | 2026-11-08 | E3 | F-SP-48 |
| Apple HIG: accessibility | <https://developer.apple.com/design/human-interface-guidelines/accessibility.md> | 2025-06-09 | 2026-11-08 | E3 | F-SP-48, F-SP-49, F-SP-56 |
| Apple HIG: gestures | <https://developer.apple.com/design/human-interface-guidelines/gestures.md> | 2026-10-28 | 2026-11-08 | E3 | F-SP-50 |
| Apple HIG: buttons | <https://developer.apple.com/design/human-interface-guidelines/buttons.md> | 2025-12-16 | 2026-11-08 | E3 | F-SP-51 |
| Apple HIG: tab-bars | <https://developer.apple.com/design/human-interface-guidelines/tab-bars.md> | 2026-06-08 | 2026-11-08 | E3 | F-SP-52 |
| Apple HIG: toolbars | <https://developer.apple.com/design/human-interface-guidelines/toolbars.md> | 2025-12-16 | 2026-11-08 | E3 | F-SP-53 |
| Apple HIG: modality | <https://developer.apple.com/design/human-interface-guidelines/modality.md> | 2023-12-05 | 2026-11-08 | E3 | F-SP-54 |
| Apple HIG: sheets | <https://developer.apple.com/design/human-interface-guidelines/sheets.md> | 2026-03-24 | 2026-11-08 | E3 | F-SP-54 |
| Apple HIG: alerts | <https://developer.apple.com/design/human-interface-guidelines/alerts.md> | 2024-02-02 | 2026-11-08 | E3 | F-SP-55 |
| Apple HIG: typography | <https://developer.apple.com/design/human-interface-guidelines/typography.md> | 2025-12-16 | 2026-11-08 | E3 | F-SP-56 |
| Apple HIG: feedback | <https://developer.apple.com/design/human-interface-guidelines/feedback.md> | not shown | 2026-11-08 | E3 | F-SP-57 |
| Apple HIG: loading | <https://developer.apple.com/design/human-interface-guidelines/loading.md> | 2025-06-09 | 2026-11-08 | E3 | F-SP-58 |
| Apple HIG: onboarding | <https://developer.apple.com/design/human-interface-guidelines/onboarding.md> | 2024-06-10 | 2026-11-08 | E3 | F-SP-59 |
| Apple HIG: entering-data | <https://developer.apple.com/design/human-interface-guidelines/entering-data.md> | 2023-06-21 | 2026-11-08 | E3 | F-SP-60 |
| Apple HIG: virtual-keyboards | <https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards.md> | 2025-06-09 | 2026-11-08 | E3 | F-SP-60 |
| Apple HIG: searching | <https://developer.apple.com/design/human-interface-guidelines/searching.md> | 2026-06-08 | 2026-11-08 | E3 | F-SP-61 |
| Apple HIG: menus | <https://developer.apple.com/design/human-interface-guidelines/menus.md> | 2026-06-08 | 2026-11-08 | E3 | F-SP-62 |
| Apple HIG: designing-for-ipados | <https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados.md> | not shown | 2026-11-08 | E3 | F-SP-63 |
| Apple HIG: multitasking | <https://developer.apple.com/design/human-interface-guidelines/multitasking.md> | 2025-06-09 | 2026-11-08 | E3 | F-SP-63 |
| Apple HIG: designing-for-macos | <https://developer.apple.com/design/human-interface-guidelines/designing-for-macos.md> | 2026-10-28 | 2026-11-08 | E3 | F-SP-64 |
| Apple HIG: keyboards | <https://developer.apple.com/design/human-interface-guidelines/keyboards.md> | 2025-06-09 | 2026-11-08 | E3 | F-SP-64 |

### Failed fetches (not evidence)

| URL | Outcome | Replacement |
|---|---|---|
| <https://developer.apple.com/design/human-interface-guidelines/navigation-bars.md> | HTTP 404 | Toolbars (F-SP-53) |
| <https://developer.apple.com/design/human-interface-guidelines/touchscreens.md> | HTTP 404 | Accessibility (F-SP-48) |

### Cited in principles only

Principles cite some HTML paths whose Markdown versions appear in the findings, plus two pages that do not appear in any findings fetch log. Fetch and add a finding before relying on the Motion page or the HIG home page.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Apple HIG, Gestures (HTML path of the Markdown page cited in F-SP-50) | <https://developer.apple.com/design/human-interface-guidelines/gestures> | not recorded | not recorded | E3 (Apple platforms) | none (principle only: P-02) |
| Apple HIG, Accessibility (HTML path of the Markdown page cited in F-SP-48) | <https://developer.apple.com/design/human-interface-guidelines/accessibility> | not recorded | not recorded | E3 | none (principle only: P-06) |
| Apple HIG (home) | <https://developer.apple.com/design/human-interface-guidelines/> | not recorded | not recorded | E3 | none (principle only: P-09) |
| Apple HIG, Motion | <https://developer.apple.com/design/human-interface-guidelines/motion> | not recorded | not recorded | E3 | none (principle only: P-15) |
