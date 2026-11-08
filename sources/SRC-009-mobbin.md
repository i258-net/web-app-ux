---
id: SRC-009
title: Mobbin
type: source
publisher: Mobbin
evidence_classes: [E5]
status: active
updated: 2026-11-08
---

# SRC-009 Mobbin

## Publisher and scope

Mobbin is a commercial library of curated screenshots and recorded flows from shipped mobile and web apps. It is indexed by screen type, UI element, and flow. Research used ten public collection and index pages, covering:

- mobile: onboarding, empty states, filtering and sorting, searching, tab bars, settings and preferences, pull-to-refresh
- web: side navigation, the web explore index, tables

These are findings F-DX-53 to F-DX-62. Mobbin's strength is quick, broad visibility of **what shipped products commonly do**, with named examples.

## How to classify their material

| Output | Class | Why |
|---|---|---|
| Any Mobbin observation | **E5 only** | A shipped example. It shows what is common in a curated sample. It says **nothing** about whether a pattern is usable |

Rules, following `evidence-classes.md`:

- A pattern supported **only** by Mobbin must be labelled *convention observed, usability unverified*.
- Never treat Mobbin popularity or recurrence as evidence that a design works.
- "Common" means recurring in the publicly visible curated sample. It is not a measured share of all shipped apps.
- Name no more than three products per pattern.

## Licensing and access

Mobbin is a subscription product. Its public collection pages show a limited set of examples and then the prompt "Log in or join for free to continue browsing". **No login was performed and no access restriction was bypassed.** The observations use only the rendered public index tags, product names, and written flow summaries. Screenshots belong to Mobbin and the original app owners. **Do not reproduce Mobbin screenshots or flow recordings** in this repository. Describe observations in words and link to the collection.

## Known limitations and biases

- **Partial access.** Only public tags, named examples, and some written flow descriptions were visible. Current product behavior, keyboard support, responsive transitions, animation timing, and usability outcomes were **not** verified.
- **Undated.** The metadata research inspected did not show capture dates or app versions, so every row records "not shown".
- **Curation bias.** The library favors visually polished, popular consumer apps. It cannot support population-prevalence claims.
- **Thin observations.** Pull-to-refresh observations concern how screens are indexed, not a tested gesture. The Tab Bar index does not by itself verify bottom placement.
- **Native bias.** Most mobile examples are native apps. Applying them to a PWA is an inference.
- **A failed route.** `https://mobbin.com/explore/mobile/screens/settings` returned "Page not found". The working public route is `settings-preferences` (F-DX-58).

## Cited pages

All rows were accessed 2026-11-08.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Mobile App Onboarding Screen User Flow Design | <https://mobbin.com/explore/mobile/flows/onboarding> | not shown | 2026-11-08 | E5 | F-DX-53 |
| Empty State UI | <https://mobbin.com/explore/mobile/screens/empty-state> | not shown | 2026-11-08 | E5 | F-DX-54 |
| Mobile Filter UX Flows | <https://mobbin.com/explore/mobile/flows/filtering-sorting> | not shown | 2026-11-08 | E5 | F-DX-55 |
| Mobile Searching & Finding User Flow | <https://mobbin.com/explore/mobile/flows/searching-finding> | not shown | 2026-11-08 | E5 | F-DX-56 |
| Mobile Tab Bar UI | <https://mobbin.com/explore/mobile/ui-elements/tab-bar> | not shown | 2026-11-08 | E5 | F-DX-57 |
| Mobile Settings Screen | <https://mobbin.com/explore/mobile/screens/settings-preferences> | not shown | 2026-11-08 | E5 | F-DX-58 |
| Mobile Pull To Refresh Screens | <https://mobbin.com/explore/mobile/screens/pull-to-refresh> | not shown | 2026-11-08 | E5 | F-DX-59 |
| Web Side Navigation UI | <https://mobbin.com/explore/web/ui-elements/side-navigation> | not shown | 2026-11-08 | E5 | F-DX-60 |
| Explore web app designs | <https://mobbin.com/explore/web> | not shown | 2026-11-08 | E5 | F-DX-61 |
| Web Table UI | <https://mobbin.com/explore/web/ui-elements/table> | not shown | 2026-11-08 | E5 | F-DX-62 |

### Fetched but not cited by a numbered finding

The DX coverage section also reports fetching the Mobbin homepage and the mobile explore index as navigation pages. It does not record their URLs, so they are not listed here.

### Failed fetches (not evidence)

| URL | Outcome | Replacement |
|---|---|---|
| <https://mobbin.com/explore/mobile/screens/settings> | Rendered "Page not found" | <https://mobbin.com/explore/mobile/screens/settings-preferences> (F-DX-58) |
