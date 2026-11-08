---
id: SRC-001
title: W3C and WHATWG (WCAG 2.2, WCAG2Mobile, WAI-ARIA APG, web specifications)
type: source
publisher: World Wide Web Consortium (W3C); WHATWG
evidence_classes: [E1, E3, E4]
status: active
updated: 2026-11-08
---

# SRC-001 W3C and WHATWG

## Publisher and scope

The W3C publishes the Web Content Accessibility Guidelines (WCAG), the Web Accessibility Initiative's informative notes and the WAI-ARIA Authoring Practices Guide (APG), and the CSS and Web Application Manifest specifications. The WHATWG maintains the HTML Living Standard. Research used:

- **WCAG 2.2**, the W3C Recommendation of 12 December 2024. Findings F-SP-01 to F-SP-32 cover 32 success criteria plus SC 1.3.5, and F-DX-14/17/20/25 cite the whole document.
- **WCAG2Mobile** (`wcag2mobile-22`), a **6 May 2025 Group Draft Note**, and its predecessor, the **26 February 2015 First Public Working Draft** *Mobile Accessibility: How WCAG 2.0 and Other W3C/WAI Guidelines Apply to Mobile* (`mobile-accessibility-mapping`).
- **WAI-ARIA APG**: the home page, the patterns index, nine widget patterns, and the keyboard-interface practice page.
- **Specifications**: Media Queries Level 4 (Candidate Recommendation Draft, 2026-02-19), Media Queries Level 5 (Working Draft, 2026-02-19), Web Application Manifest (Working Draft, 2026-11-06), and the HTML Standard section on navigation and session history.

Strengths: normative, testable, vendor-neutral, and versioned. This is the only publisher in the register whose text can back a quality gate unconditionally.

## How to classify their material

| Output | Class | Why |
|---|---|---|
| WCAG 2.2 success criterion text, including its level, defined terms, and listed exceptions | **E1** | Normative conformance requirement |
| WCAG notes, Understanding documents, Techniques, and the informative intro | **E4** | Informative. The research did not promote any of them to E1 |
| WCAG2Mobile (2025) and the Mobile Accessibility mapping (2015) | **E4** | Informative draft notes. `evidence-classes.md` forbids upgrading them to E1 |
| APG patterns and practices | **E3** when used as the keyboard and semantics contract for a widget (as in the DX findings); **E4** when read as advisory guidance (as in F-SP-38 to F-SP-46) | Informative, and the APG says so itself. The tooltip pattern is explicitly unfinished and lacks task-force consensus |
| Normative text in a CSS, Manifest, or HTML specification | **E1**, with its maturity stated | Normative in the cited version. It does **not** establish that any browser implements it |

The two research files classified APG differently. Patterns keep whichever class the citing finding recorded. The table below shows both where both were used (for example, the modal dialog pattern is listed as `E3/E4`).

## Licensing and access

W3C documents are free to read and are published under the W3C Document License. WHATWG standards are published under CC BY 4.0. Quote short labels and exact thresholds (for example "24 by 24 CSS pixels") with attribution. Paraphrase everything else. Nothing here was behind a paywall.

## Known limitations and biases

- **Conformance is not good UX.** WCAG sets a floor for access. A page can pass every criterion and still be hard to use.
- **Legal status varies.** WCAG becomes an obligation only through a law, policy, or contract that adopts it. The research makes no legal-compliance claim.
- **The mobile notes are drafts.** Much of the 2025 note repeats WCAG or WCAG2ICT and still contains placeholders. The detailed reachability, virtual-keyboard, and reduced-entry advice comes from the 2015 draft, so it is old and was never finalized.
- **Spec status is not browser support.** Media Queries 5 and the Manifest are Working Drafts. Use MDN compatibility data (SRC-007) for support claims.
- **The research covered a selection of WCAG.** It extracted UX-relevant success criteria only. Criteria it did not list, such as those on media, flashing, bypass blocks, and language, still apply.
- **Scope.** WCAG measures in CSS pixels. Do not convert its thresholds into Apple pt or Material dp.

## Cited pages

All rows were accessed 2026-11-08 and are taken from the `Source` lines of the findings. WCAG anchors are listed separately because each anchor points to a different success criterion in the same fetched document.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/> | 2024-12-12 | 2026-11-08 | E1 | F-DX-14, F-DX-17, F-DX-20, F-DX-25; also cited in P-12 |
| Developing a Keyboard Interface | <https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/> | not shown | 2026-11-08 | E3 | F-DX-21, F-DX-23, F-DX-24 |
| Dialog (Modal) Pattern | <https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/> | not shown | 2026-11-08 | E3/E4 | F-DX-22, F-SP-40 |
| Media Queries Level 4, §§7.1–7.3 | <https://www.w3.org/TR/mediaqueries-4/> | 2026-02-19 (Candidate Recommendation Draft) | 2026-11-08 | E1 | F-DX-47, F-WP-17, F-WP-18, F-WP-19, F-WP-20 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#orientation> | 2024-12-12 | 2026-11-08 | E1 | F-SP-01 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#contrast-minimum> | 2024-12-12 | 2026-11-08 | E1 | F-SP-02; also cited in P-08 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#resize-text> | 2024-12-12 | 2026-11-08 | E1 | F-SP-03 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#reflow> | 2024-12-12 | 2026-11-08 | E1 | F-SP-04 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#non-text-contrast> | 2024-12-12 | 2026-11-08 | E1 | F-SP-05 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#text-spacing> | 2024-12-12 | 2026-11-08 | E1 | F-SP-06 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus> | 2024-12-12 | 2026-11-08 | E1 | F-SP-07 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#keyboard> | 2024-12-12 | 2026-11-08 | E1 | F-SP-08 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#no-keyboard-trap> | 2024-12-12 | 2026-11-08 | E1 | F-SP-09 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#character-key-shortcuts> | 2024-12-12 | 2026-11-08 | E1 | F-SP-10 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#timing-adjustable> | 2024-12-12 | 2026-11-08 | E1 | F-SP-11 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#focus-order> | 2024-12-12 | 2026-11-08 | E1 | F-SP-12 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#focus-visible> | 2024-12-12 | 2026-11-08 | E1 | F-SP-13 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum> | 2024-12-12 | 2026-11-08 | E1 | F-SP-14 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#focus-appearance> | 2024-12-12 | 2026-11-08 | E1 | F-SP-15 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#pointer-gestures> | 2024-12-12 | 2026-11-08 | E1 | F-SP-16 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#pointer-cancellation> | 2024-12-12 | 2026-11-08 | E1 | F-SP-17 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#label-in-name> | 2024-12-12 | 2026-11-08 | E1 | F-SP-18 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#motion-actuation> | 2024-12-12 | 2026-11-08 | E1 | F-SP-19 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#target-size-enhanced> | 2024-12-12 | 2026-11-08 | E1 | F-SP-20; also cited in P-06 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#dragging-movements> | 2024-12-12 | 2026-11-08 | E1 | F-SP-21; also cited in P-06 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#target-size-minimum> | 2024-12-12 | 2026-11-08 | E1 | F-SP-22; also cited in P-06 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#on-focus> | 2024-12-12 | 2026-11-08 | E1 | F-SP-23; also cited in P-10 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#on-input> | 2024-12-12 | 2026-11-08 | E1 | F-SP-24 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#consistent-help> | 2024-12-12 | 2026-11-08 | E1 | F-SP-25 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#error-identification> | 2024-12-12 | 2026-11-08 | E1 | F-SP-26; also cited in P-11 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#labels-or-instructions> | 2024-12-12 | 2026-11-08 | E1 | F-SP-27 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#error-suggestion> | 2024-12-12 | 2026-11-08 | E1 | F-SP-28 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data> | 2024-12-12 | 2026-11-08 | E1 | F-SP-29 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#redundant-entry> | 2024-12-12 | 2026-11-08 | E1 | F-SP-30; also cited in P-01, P-05, P-07 |
| WCAG 2.2, 1.3.5 | <https://www.w3.org/TR/WCAG22/#identify-input-purpose> | 2024-12-12 | 2026-11-08 | E1 | F-SP-30 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum> | 2024-12-12 | 2026-11-08 | E1 | F-SP-31; also cited in P-07 |
| Web Content Accessibility Guidelines (WCAG) 2.2 | <https://www.w3.org/TR/WCAG22/#status-messages> | 2024-12-12 | 2026-11-08 | E1 | F-SP-32 |
| WCAG2Mobile | <https://www.w3.org/TR/wcag2mobile-22/> | 2025-05-06 (Group Draft Note) | 2026-11-08 | E4 | F-SP-33, F-SP-34, F-SP-35, F-SP-37; also cited in P-12 |
| Mobile Accessibility mapping | <https://www.w3.org/TR/mobile-accessibility-mapping/> | 2015-02-26 (First Public Working Draft) | 2026-11-08 | E4 | F-SP-34, F-SP-35, F-SP-36, F-SP-37 |
| WAI-ARIA APG: Menu and Menubar Pattern | <https://www.w3.org/WAI/ARIA/apg/patterns/menubar/> | not shown | 2026-11-08 | E4 | F-SP-38 |
| WAI-ARIA APG: Tabs Pattern | <https://www.w3.org/WAI/ARIA/apg/patterns/tabs/> | not shown | 2026-11-08 | E4 | F-SP-39 |
| WAI-ARIA APG: Combobox Pattern | <https://www.w3.org/WAI/ARIA/apg/patterns/combobox/> | not shown | 2026-11-08 | E4 | F-SP-41 |
| WAI-ARIA APG: Listbox Pattern | <https://www.w3.org/WAI/ARIA/apg/patterns/listbox/> | not shown | 2026-11-08 | E4 | F-SP-42 |
| WAI-ARIA APG: Grid (Data Grid) Pattern | <https://www.w3.org/WAI/ARIA/apg/patterns/grid/> | not shown | 2026-11-08 | E4 | F-SP-43 |
| WAI-ARIA APG: Disclosure Pattern | <https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/> | not shown | 2026-11-08 | E4 | F-SP-44 |
| WAI-ARIA APG: Tooltip Pattern | <https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/> | not shown | 2026-11-08 | E4 | F-SP-45 |
| WAI-ARIA APG: Slider Pattern | <https://www.w3.org/WAI/ARIA/apg/patterns/slider/> | not shown | 2026-11-08 | E4 | F-SP-46 |
| Media Queries Level 5 | <https://www.w3.org/TR/mediaqueries-5/> | 2026-02-19 (Working Draft) | 2026-11-08 | E1 | F-WP-23 |
| Web Application Manifest | <https://www.w3.org/TR/appmanifest/> | 2026-11-06 (Working Draft) | 2026-11-08 | E1 | F-WP-43, F-WP-45, F-WP-46, F-WP-52 |
| HTML Standard | <https://html.spec.whatwg.org/multipage/nav-history-apis.html> | 2026-11-06 (Living Standard) | 2026-11-08 | E1 | F-WP-58 |

### Fetched but not cited by a numbered finding

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| WAI-ARIA Authoring Practices Guide (home) | <https://www.w3.org/WAI/ARIA/apg/> | not shown | 2026-11-08 | E3/E4 | none (SP coverage section); also cited in P-12 |
| WAI-ARIA APG: Patterns index | <https://www.w3.org/WAI/ARIA/apg/patterns/> | not shown | 2026-11-08 | E3/E4 | none (SP coverage section) |

### Cited in principles only

These are anchors inside the fetched WCAG 2.2 document, but no finding extracted these particular success criteria. Verify the SC text before using either one in a gate.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| W3C WCAG 2.2 SC 3.2.3 Consistent Navigation (AA) | <https://www.w3.org/TR/WCAG22/#consistent-navigation> | not recorded | not recorded | E1 | none (principle only: P-04, P-09) |
| W3C WCAG 2.2 SC 2.3.3 Animation from Interactions (AAA) | <https://www.w3.org/TR/WCAG22/#animation-from-interactions> | not recorded | not recorded | E1 | none (principle only: P-15) |
