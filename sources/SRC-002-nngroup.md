---
id: SRC-002
title: Nielsen Norman Group (NN/g)
type: source
publisher: Nielsen Norman Group
evidence_classes: [E2, E4]
status: active
updated: 2026-11-08
---

# SRC-002 Nielsen Norman Group

## Publisher and scope

NN/g is a UX research and consulting firm. Its free articles cover usability heuristics, mobile and desktop interaction, forms, navigation, information architecture, data tables, and cross-channel experience. Many articles summarize the firm's own usability studies, eye-tracking work, or diary studies. Others are expert syntheses with no study behind them.

The research used 50 distinct NN/g pages cited by findings F-NB-01 to F-NB-42, F-DX-06 to F-DX-50 (selected), and F-WP-79 (response times). The NB file also fetched the *10 Usability Heuristics* index, which established the heuristic framework. The firm's main strengths are long-running, dated research on general-purpose websites and applications, and clear, practical heuristics.

## How to classify their material

Classify each claim by what the page actually reports, not by the reputation of the NN/g brand.

| Output | Class | Why |
|---|---|---|
| Articles that describe NN/g's own testing and report observed behavior, such as hamburger menus, touch targets, mobile tutorials, placeholders, mega menus, omnichannel consistency, multi-tab "page parking", filter categories, and indicators | **E2** | The page describes a study or observations. State the study context and date |
| Heuristic explainers (the ten heuristics), design guidelines, and "how to" articles | **E4** | Expert synthesis. No study is described on the page |
| Restatements of older academic work, such as *Response Times: The 3 Important Limits* (Miller 1968; Card et al. 1991) and *The Aesthetic-Usability Effect* | **E4 restating E2** | The underlying studies were not fetched. Cite NN/g as the restatement only |
| Paid reports, training courses, and videos | Not used | Not fetched. The separate paid mobile report was not read |

If a finding marked E4 makes a claim the article supports with observations, the finding should say so. Do not change the class from memory of the brand.

## Licensing and access

The articles are free to read and are copyrighted by NN/g. Quote a phrase at most and paraphrase the rest. Research reports and courses are paid and were not accessed. No paywall bypass was used.

## Known limitations and biases

- **Age.** Many articles are from 2014 to 2019, and the response-time article dates from 1993 with a 2014 update. Interaction conventions change, so always cite the date. Several articles show a "last reviewed" date, which is recorded where it appeared.
- **Opaque methods.** Articles seldom give sample sizes, tasks, or statistics. Treat an E2 claim from NN/g as directional evidence about behavior, not as an effect size.
- **Web and e-commerce bias.** Many studies tested content and commerce websites, not complex logged-in applications.
- **Native apps.** The mobile tutorial experiment (F-NB-41) used native iPhone apps. Applying it to PWAs is an inference.
- **Units.** NN/g gives touch targets in physical centimetres. That figure is not interchangeable with WCAG CSS px, Apple pt, or Material dp.
- **Conflicts with Baymard** are recorded in the NB disagreements section, covering positive validation, live versus Apply filtering, and required/optional field marking. Keep both positions and do not average them.
- **The research had one access failure.** `https://www.nngroup.com/articles/table-sorting/` could not be fetched, so the sorting guidance uses Carbon (SRC-008).

## Cited pages

All rows were accessed 2026-11-08.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Left-Side Vertical Navigation on Desktop: Scalable, Responsive, and Easy to Scan | <https://www.nngroup.com/articles/vertical-nav/> | 2021-05-16 | 2026-11-08 | E4 | F-DX-06 |
| Mega Menus Work Well for Site Navigation | <https://www.nngroup.com/articles/mega-menus-work-well/> | 2017-03-26 | 2026-11-08 | E2 | F-DX-07 |
| Breadcrumbs: 11 Design Guidelines for Desktop and Mobile | <https://www.nngroup.com/articles/breadcrumbs/> | 2018-12-23; last reviewed 2026-09-01 | 2026-11-08 | E4 | F-DX-10, F-NB-38 |
| Timing Guidelines for Exposing Hidden Content | <https://www.nngroup.com/articles/timing-exposing-content/> | 2015-01-11 | 2026-11-08 | E4 | F-DX-11 |
| Tooltip Guidelines | <https://www.nngroup.com/articles/tooltip-guidelines/> | 2019-01-27 | 2026-11-08 | E4 | F-DX-13, F-NB-31 |
| Contextual Menus: Delivering Relevant Tools for Tasks | <https://www.nngroup.com/articles/contextual-menus/> | 2019-03-17 | 2026-11-08 | E4 | F-DX-15 |
| Drag–and–Drop: How to Design for Ease of Use | <https://www.nngroup.com/articles/drag-drop/> | 2020-02-23 | 2026-11-08 | E4 | F-DX-16 |
| Accelerators Maximize Efficiency in User Interfaces | <https://www.nngroup.com/articles/ui-accelerators/> | 2024-10-18 | 2026-11-08 | E4 | F-DX-18 |
| UI Copy: UX Guidelines for Command Names and Keyboard Shortcuts | <https://www.nngroup.com/articles/ui-copy/> | 2019-03-03 | 2026-11-08 | E4 | F-DX-19, F-NB-32 |
| Data Tables: Four Major User Tasks | <https://www.nngroup.com/articles/data-tables/> | 2022-04-03 | 2026-11-08 | E4 | F-DX-30, F-DX-36, F-NB-33 |
| Page Parking: Multi-Tab Mania | <https://www.nngroup.com/articles/multi-tab-page-parking/> | 2015-11-01 | 2026-11-08 | E2 | F-DX-40 |
| Confirmation Dialogs Can Prevent User Errors | <https://www.nngroup.com/articles/confirmation-dialog/> | 2018-02-18; last reviewed 2026-08-07 | 2026-11-08 | E4 | F-DX-45, F-NB-30; also cited in P-11 |
| Consistency in the Omnichannel Experience | <https://www.nngroup.com/articles/omnichannel-consistency/> | 2016-10-16 | 2026-11-08 | E2 | F-DX-48, F-DX-49 |
| Seamlessness in the Omnichannel User Experience | <https://www.nngroup.com/articles/seamless-cross-channel/> | 2017-03-19 | 2026-11-08 | E2 | F-DX-50 |
| Visibility of System Status (Usability Heuristic #1) | <https://www.nngroup.com/articles/visibility-system-status/> | 2018-06-03 | 2026-11-08 | E4 | F-NB-01 |
| Match Between the System and the Real World (Usability Heuristic #2) | <https://www.nngroup.com/articles/match-system-real-world/> | 2018-07-01 | 2026-11-08 | E4 | F-NB-02 |
| User Control and Freedom (Usability Heuristic #3) | <https://www.nngroup.com/articles/user-control-and-freedom/> | 2020-11-29 | 2026-11-08 | E4 | F-NB-03 |
| Maintain Consistency and Adhere to Standards (Usability Heuristic #4) | <https://www.nngroup.com/articles/consistency-and-standards/> | 2021-01-10 | 2026-11-08 | E4 | F-NB-04 |
| Preventing User Errors: Avoiding Unconscious Slips | <https://www.nngroup.com/articles/slips/> | 2015-08-23 | 2026-11-08 | E4 | F-NB-05 |
| Memory Recognition and Recall in User Interfaces | <https://www.nngroup.com/articles/recognition-and-recall/> | 2024-01-15 | 2026-11-08 | E4 | F-NB-06 |
| Flexibility and Efficiency of Use (Usability Heuristic #7) | <https://www.nngroup.com/articles/flexibility-efficiency-heuristic/> | 2020-11-22 | 2026-11-08 | E4 | F-NB-07 |
| Aesthetic and Minimalist Design (Usability Heuristic #8) | <https://www.nngroup.com/articles/aesthetic-minimalist-design/> | 2021-01-24 | 2026-11-08 | E4 | F-NB-08 |
| Error-Message Guidelines | <https://www.nngroup.com/articles/error-message-guidelines/> | 2023-05-14 | 2026-11-08 | E4 | F-NB-09; also cited in P-11 |
| Help and Documentation (Usability Heuristic #10) | <https://www.nngroup.com/articles/help-and-documentation/> | 2020-12-13 | 2026-11-08 | E4 | F-NB-10 |
| Mobile User Experience: Limitations and Strengths | <https://www.nngroup.com/articles/mobile-ux/> | 2015-04-19 | 2026-11-08 | E2 | F-NB-11 |
| Touch Targets on Touchscreens | <https://www.nngroup.com/articles/touch-target-size/> | 2019-05-05 | 2026-11-08 | E2 | F-NB-12 |
| Hamburger Menus and Hidden Navigation Hurt UX Metrics | <https://www.nngroup.com/articles/hamburger-menus/> | 2016-06-26 | 2026-11-08 | E2 | F-NB-13; also cited in P-02 |
| Mobile First Is NOT Mobile Only | <https://www.nngroup.com/articles/mobile-first-not-mobile-only/> | 2016-07-24 | 2026-11-08 | E2 | F-NB-14 |
| Basic Patterns for Mobile Navigation: A Primer | <https://www.nngroup.com/articles/mobile-navigation-patterns/> | 2015-11-15 | 2026-11-08 | E4 | F-NB-15 |
| Card Sorting: Uncover Users’ Mental Models for Better Information Architecture | <https://www.nngroup.com/articles/card-sorting-definition/> | 2024-02-02 | 2026-11-08 | E4 | F-NB-16; also cited in P-03 |
| Progressive Disclosure | <https://www.nngroup.com/articles/progressive-disclosure/> | 2006-12-03 | 2026-11-08 | E4 | F-NB-17; also cited in P-05 |
| Website Forms Usability: Top 10 Recommendations | <https://www.nngroup.com/articles/web-form-design/> | 2016-05-01 | 2026-11-08 | E4 | F-NB-18 |
| Placeholders in Form Fields Are Harmful | <https://www.nngroup.com/articles/form-design-placeholders/> | 2014-05-11; last reviewed 2018-09-10 | 2026-11-08 | E2 | F-NB-19 |
| Marking Required Fields in Forms | <https://www.nngroup.com/articles/required-fields/> | 2019-06-16 | 2026-11-08 | E4 | F-NB-20 |
| 10 Design Guidelines for Reporting Errors in Forms | <https://www.nngroup.com/articles/errors-forms-design-guidelines/> | 2019-02-03; last reviewed 2024-12-12 | 2026-11-08 | E4 | F-NB-21, F-NB-22 |
| Few Guesses, More Success: 4 Principles to Reduce Cognitive Load in Forms | <https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/> | 2025-07-18 | 2026-11-08 | E4 | F-NB-23 |
| Defining Helpful Filter Categories and Values for Better UX | <https://www.nngroup.com/articles/filter-categories-values/> | 2018-07-15 | 2026-11-08 | E2 | F-NB-24 |
| User Intent Affects Filter Design | <https://www.nngroup.com/articles/applying-filters/> | 2016-02-07 | 2026-11-08 | E4 | F-NB-25 |
| Mobile Faceted Search with a Tray: New and Improved Design Pattern | <https://www.nngroup.com/articles/mobile-faceted-search/> | 2015-07-26 | 2026-11-08 | E4 | F-NB-26 |
| Designing Empty States in Complex Applications: 3 Guidelines | <https://www.nngroup.com/articles/empty-state-interface-design/> | 2021-09-19 | 2026-11-08 | E4 | F-NB-27 |
| Response Times: The 3 Important Limits | <https://www.nngroup.com/articles/response-times-3-important-limits/> | 1993-01-01; web-application update added 2014 (day not shown) | 2026-11-08 | E4 | F-NB-28, F-WP-79; also cited in P-10, P-13 |
| Progress Indicators Make a Slow System Less Insufferable | <https://www.nngroup.com/articles/progress-indicators/> | 2014-10-26 | 2026-11-08 | E2 | F-NB-29 |
| Infinite Scrolling: When to Use It, When to Avoid It | <https://www.nngroup.com/articles/infinite-scrolling-tips/> | 2022-09-04 | 2026-11-08 | E4 | F-NB-34 |
| Sticky Headers: 5 Ways to Make Them Better | <https://www.nngroup.com/articles/sticky-headers/> | 2021-04-04 | 2026-11-08 | E4 | F-NB-35 |
| Using Swipe to Trigger Contextual Actions | <https://www.nngroup.com/articles/contextual-swipe/> | 2017-02-12 | 2026-11-08 | E4 | F-NB-36 |
| Accordions Are Not Always the Answer for Complex Content on Desktops | <https://www.nngroup.com/articles/accordions-complex-content/> | 2014-05-18 | 2026-11-08 | E4 | F-NB-37 |
| Modal & Nonmodal Dialogs: When (& When Not) to Use Them | <https://www.nngroup.com/articles/modal-nonmodal-dialog/> | 2017-04-23 | 2026-11-08 | E4 | F-NB-39 |
| Indicators, Validations, and Notifications: Pick the Correct Communication Option | <https://www.nngroup.com/articles/indicators-validations-notifications/> | 2024-01-17 | 2026-11-08 | E2 | F-NB-40 |
| Mobile Tutorials: Wasted Effort or Efficiency Boost? | <https://www.nngroup.com/articles/mobile-tutorials/> | 2020-03-08 | 2026-11-08 | E2 | F-NB-41 |
| Deceptive Patterns in UX: How to Recognize and Avoid Them | <https://www.nngroup.com/articles/deceptive-patterns/> | 2023-12-01 | 2026-11-08 | E4 | F-NB-42 |

### Fetched but not cited by a numbered finding

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| 10 Usability Heuristics for User Interface Design | <https://www.nngroup.com/articles/ten-usability-heuristics/> | 1994-04-24; last reviewed 2024-01-30 | 2026-11-08 | E4 | none (NB "Additional pages fetched"); also cited in P-01, P-02, P-05, P-09, P-10, P-11, P-14 |

### Failed fetches (not evidence)

| URL | Outcome | Replacement |
|---|---|---|
| <https://www.nngroup.com/articles/table-sorting/> | Fetch tool reported it inaccessible (DX coverage) | Carbon data-table guidance (SRC-008) |

### Cited in principles only

These URLs appear in principles but not in any findings fetch log. Before relying on one, fetch it and add a finding.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Nielsen, J. "Usability 101: Introduction to Usability." NN/g | <https://www.nngroup.com/articles/usability-101-introduction-to-usability/> | not recorded | not recorded | E4 (definitional) | none (principle only: P-01) |
| Whitenton, K. "Flat vs. Deep Website Hierarchies." NN/g | <https://www.nngroup.com/articles/flat-vs-deep-hierarchy/> | not recorded | not recorded | E4 | none (principle only: P-03) |
| Nielsen, J. "Breadcrumb Navigation Increasingly Useful." NN/g | <https://www.nngroup.com/articles/breadcrumb-navigation-useful/> | not recorded | not recorded | E4 | none (principle only: P-04) |
| Nielsen, J. "Top 10 Mistakes in Web Design." NN/g | <https://www.nngroup.com/articles/top-10-mistakes-web-design/> | not recorded | not recorded | E4 (back button) | none (principle only: P-04) |
| Whitenton, K. "Minimize Cognitive Load to Maximize Usability." NN/g | <https://www.nngroup.com/articles/minimize-cognitive-load/> | not recorded | not recorded | E4 | none (principle only: P-05) |
| Pernice, K. "F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant." NN/g, 2017 | <https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/> | not recorded | not recorded | E2 | none (principle only: P-08) |
| Nielsen, J. "Jakob's Law of Internet User Experience." NN/g | <https://www.nngroup.com/videos/jakobs-law-internet-ux/> | not recorded | not recorded | E4 | none (principle only: P-09) |
| Moran, K. "The Aesthetic-Usability Effect." NN/g | <https://www.nngroup.com/articles/aesthetic-usability-effect/> | not recorded | not recorded | E4 summarizing E2 | none (principle only: P-15) |
