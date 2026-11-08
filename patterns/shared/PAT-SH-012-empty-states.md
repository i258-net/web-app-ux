---
id: PAT-SH-012
title: Empty states — first use, no results, cleared, and error-empty
type: pattern
scope: shared
topics: [empty-states, no-results, first-use, zero-data, cleared-state, error-state]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-10, P-02, P-05, P-11]
dimensions: [D-07, D-06, D-01]
gates: [QG-028, QG-071]
related: [PAT-SH-004, PAT-SH-005, PAT-SH-013, PAT-SH-010, PAT-SH-016, PAT-PW-005]
evidence_strength: limited
status: active
updated: 2026-11-08
---

# Empty states — first use, no results, cleared, and error-empty

## Problem

An empty container is ambiguous. Users cannot tell whether data is still loading, the request failed, nothing matches, or nothing exists yet. Apps often render the same blank panel or "No items" text for all four, sometimes while data is still loading. Empty views are also missed opportunities: the first visit to an empty dashboard is exactly when users need to know what the area is for and how to start.

## Recommendation

**Outcome:** whenever a region is empty, users know *why* and *what they can do next*.

1. **Model four empty causes separately**, plus loading, and design each one:

   | Cause | Message focus | Primary next step |
   |---|---|---|
   | **First use** (nothing created yet) | What this area is for and what will appear here | Create or import the first item; link to brief help |
   | **No results** (search or filters exclude everything) | That nothing matched *this query or these filters* | Show the active filters with one-tap removal; edit the query; broaden the scope (PAT-SH-004, PAT-SH-005) |
   | **Cleared / done** (user emptied it: inbox zero, all tasks complete) | Confirmation that this is a success state | Optional: what to do next, or nothing |
   | **Error-empty** (data could not load) | That loading failed, in plain language, not "no data" | Retry; offline explanation; preserved context (PAT-SH-016, PAT-PW-005) |

2. **Never show an empty message before loading completes.** Show the loading state until the request resolves (PAT-SH-010).
3. **Keep the page frame.** Keep headings, navigation, and the toolbar in place so users stay oriented. Disable controls that cannot apply, and explain why where needed.
4. **Lead with one primary action** that fits the cause. Avoid a wall of options. Link to help for more.
5. **Write specific copy.** Use the object's name ("No invoices yet" rather than "No data"). Keep it short. Illustration is optional and must not push the action below the fold on compact viewports.
6. **Consider sample or template content** for complex first-use states, clearly labeled as samples and easy to remove.
7. **Announce dynamic transitions to empty** ("No results") as a status message without moving focus (QG-028).
8. **Respect permissions.** If the area is empty because the user lacks access, say so and say who can grant it. Do not imply that nothing exists.

Onboarding sequencing (when an empty state is enough instead of a tour) is in PAT-SH-013.

## Evidence

- **E4** Nielsen Norman Group, "Designing Empty States in Complex Applications: 3 Guidelines". https://www.nngroup.com/articles/empty-state-interface-design/ — Unexplained empty containers leave users unsure whether processing finished, failed, or found nothing. NN/g criticizes "No records" shown during loading and recommends learning cues and direct paths into key tasks.
- **E2** Baymard Institute, "Display 'Applied Filters' in an Overview". https://baymard.com/research-articles/how-to-design-applied-filters — Visible applied filters give context and fast removal. We infer they are the most useful recovery in a filter-caused empty state. *E-commerce.*
- **E2** Nielsen Norman Group, "Indicators, Validations, and Notifications". https://www.nngroup.com/articles/indicators-validations-notifications/ — A participant missed a brief error and waited for content that never loaded. We infer that error-empty states need a persistent in-place explanation.
- **E4** Nielsen Norman Group, "Help and Documentation". https://www.nngroup.com/articles/help-and-documentation/ — Contextual help tied to current work is less likely to be ignored than pushed instructions.
- **E3** Apple, "Onboarding". https://developer.apple.com/design/human-interface-guidelines/onboarding.md — Teach in context and provide sensible defaults. Apple platforms.
- **E2** Baymard Institute, "42% of Mobile Homepages Risk Setting Wrong Expectations". https://baymard.com/research-articles/mobile-homepage-usability — First views that were narrow or unrepresentative led users to wrong assumptions about scope. *E-commerce*; we infer that first-use states should show what the area will contain.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — "No results" after a dynamic update is a status message.
- **E5** Mobbin, "Empty State UI". https://mobbin.com/explore/mobile/screens/empty-state — Empty states recur in shipped collection and search screens, often with illustrations. Convention observed, usability unverified.

**Evidence note:** the direct design guidance here rests mainly on E4 (NN/g) plus E5 examples. The E2 sources support adjacent mechanisms (applied-filter visibility, missed transient errors, first-view expectations) that we apply by inference. We found no empirical comparison of empty-state designs.

## Alternatives and tradeoffs

- **Illustration vs text-only.** Illustration adds warmth (P-15) but costs space and adds nothing to comprehension. No finding shows it improves outcomes. It is acceptable when it does not displace the action.
- **Sample data vs a truly empty view.** Samples show what the area will look like but can be mistaken for real data or clutter the account. Label them clearly and remove them with one action.
- **Suggesting related content on no results.** This can rescue the task, but it can also mislead users into thinking the results matched. Label suggestions as "Related" or "Popular", separate from results.

## Exceptions and failure modes

- Transient regions (a notification popover) may need only a single line ("You're all caught up").
- Failure modes:
  - "No data" flashing before content loads;
  - the same message for error and no-results;
  - an empty dashboard with no way to add the first widget;
  - a large illustration that pushes the button off a compact screen;
  - no-results with filters active but not shown;
  - an empty state caused by permissions that implies nothing exists.

## Evaluation questions

1. For each collection view, are first-use, no-results, cleared, and error-empty states designed and distinguishable? [screenshot] [prototype]
2. Under throttling, does an empty message ever appear before loading finishes? [running app]
3. Does each empty state offer a relevant primary action visible without scrolling at compact width? [screenshot]
4. In a filter-caused empty state, can the user see and remove the filters responsible? [running app]
5. Does an error-empty state offer Retry and avoid saying "no items"? [running app]
6. Is the transition to empty announced to assistive technology? [running app]
7. On first use, can users say what the area is for and how to start? [user study]

## Related

- Principles: P-10, P-02, P-05, P-11
- Dimensions: D-07, D-06, D-01
- Gates: QG-028, QG-071
- Patterns: PAT-SH-004 (search no-results), PAT-SH-005 (filters), PAT-SH-013 (onboarding), PAT-SH-010 (loading), PAT-SH-016 (failure), PAT-PW-005 (offline)

## Change log

- 2026-11-08 — Initial version (ADR-001).
