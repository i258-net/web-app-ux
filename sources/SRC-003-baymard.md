---
id: SRC-003
title: Baymard Institute
type: source
publisher: Baymard Institute
evidence_classes: [E2, E4]
status: active
updated: 2026-11-08
---

# SRC-003 Baymard Institute

## Publisher and scope

Baymard Institute is an independent research firm that studies e-commerce UX. It runs large-scale moderated usability testing and benchmarks the implementations of leading commerce sites against its own guidelines. Its methodology page (F-NB-43) describes this research programme.

The research used public research articles and blog syntheses on these topics:

- form fields, labels, inline validation, and adaptive error messages
- touch keyboards
- address lookup and address line 2
- Apply buttons
- filtering and applied filters
- truncation and autocomplete
- product lists, main navigation, and mobile homepages
- accounts and self-service

Its strengths are depth on forms, product finding, and checkout, repeated benchmarks over many years, and explicit mobile coverage. The register also includes one Smashing Magazine article (F-DX-33) because a Baymard researcher, Christian Holst, wrote it and it reports Baymard commerce testing.

## How to classify their material

| Output | Class | Why |
|---|---|---|
| Research articles that report usability-test observations, such as "during testing, users…" | **E2, e-commerce context** | Large-scale qualitative testing. Say "likely generalizes" when applying it outside commerce, never "proven" |
| Benchmark prevalence figures, such as "31% of sites don't" | Context only. Never use one as a threshold or an effect size | They measure sampled site implementations, not the share of users affected, and not conversion uplift |
| Blog syntheses and "best practices" overviews, such as *What Is an Ecommerce Filter? UI Best Practices* | **E4**, or E2 only where the page itself reports test observations | Summaries that link to Premium guidelines |
| Premium guidelines, paid reports, videos, and raw datasets | Not used | Paywalled. Not inspected |

The register follows `evidence-classes.md` §Resolving disagreements, item 3: Baymard's checkout findings often generalize to any high-stakes form, but patterns must name e-commerce as the tested context.

## Licensing and access

Article summaries and key takeaways are free to read. The full guidelines, benchmark databases, and reports require a **Baymard Premium** subscription. Research recorded only what the public pages state. No account, mirror, or paywall bypass was used. Do not reproduce Baymard's guideline text, screenshots, or benchmark tables. Paraphrase, and quote a phrase at most.

**Paywalled or failed during research:**

- `https://baymard.com/labs/touch-keyboard-types` (the touch-keyboard cheat sheet) **timed out**: the web fetch returned "(400) Timeout fetching". It supplies no finding. The public touch-keyboard research article (F-NB-54, F-NB-55) loaded and is cited instead.
- The mobile e-commerce overview (F-NB-44) and the research articles link to **Premium** guidelines. Only the public summaries were read.
- The underlying benchmark datasets and video content were not inspected.

## Known limitations and biases

- **E-commerce context.** Product finding, carts, and checkout differ from logged-in productivity apps. Transfer the mechanism, such as label placement or keyboard type, not the conversion framing.
- **Inconsistent figures.** The inline-validation page reports 31% in its title and key takeaways but 32% in the body. Category-navigation prevalence differs across the 2023 and 2026 articles. Do not combine figures from different years into an undated statistic.
- **Age.** The 2013 mobile form articles are retained with their dates. The 2013 native-select navigation article is too dated to support a current OS-geometry rule.
- **Commercial interest.** Baymard sells access to the full guidelines. Its public articles are summaries and are not peer-reviewed.
- **Conflicts with NN/g** cover positive validation, live versus Apply filtering, and marking both required and optional fields. See the NB disagreements section and record both positions.

## Cited pages

All rows were accessed 2026-11-08.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Readability: The Optimal Line Length | <https://baymard.com/research-articles/line-length-readability> | 2022-05-10 | 2026-11-08 | E2 | F-DX-01 |
| Infinite Scrolling, Pagination Or “Load More” Buttons? Usability Findings In eCommerce | <https://www.smashingmagazine.com/2016/03/pagination-infinite-scrolling-load-more-buttons/> | 2016-03-01 | 2026-11-08 | E2 | F-DX-33 |
| Baymard’s UX Research Methodology | <https://baymard.com/research/methodology> | not shown | 2026-11-08 | E2 | F-NB-43 |
| Mobile E-Commerce UX | <https://baymard.com/research/mcommerce-usability> | not shown | 2026-11-08 | E2 | F-NB-44; also cited in P-01, P-07, P-11 |
| Checkout Optimization: 5 Ways to Minimize Form Fields in Checkout | <https://baymard.com/research-articles/checkout-flow-average-form-fields> | 2024-06-26 | 2026-11-08 | E2 | F-NB-45 |
| Field Label UX: Place Labels Above the Field | <https://baymard.com/research-articles/mobile-form-usability-label-position> | 2013-03-19 | 2026-11-08 | E2 | F-NB-46 |
| Mobile Form Usability: Never Use Inline Labels | <https://baymard.com/research-articles/mobile-forms-avoid-inline-labels> | 2013-06-04 | 2026-11-08 | E2 | F-NB-47 |
| Mobile Form Usability: Avoid Splitting Single Input Entities | <https://baymard.com/research-articles/mobile-form-usability-single-input-fields> | 2013-02-12 | 2026-11-08 | E2 | F-NB-48 |
| E-Commerce Checkouts Need to Mark Both Required Fields and Optional Fields Explicitly (Only 14% Do So) | <https://baymard.com/research-articles/required-optional-form-fields> | 2018-10-02; body includes 2021 benchmark results (update date not shown) | 2026-11-08 | E2 | F-NB-49 |
| Usability Testing of Inline Form Validation: 31% Don’t Have It, 4% Get It Wrong | <https://baymard.com/research-articles/inline-form-validation> | 2024-01-09 | 2026-11-08 | E2 | F-NB-50, F-NB-51, F-NB-52 |
| Improve Validation Errors with Adaptive Messages (98% Don’t) | <https://baymard.com/research-articles/adaptive-validation-error-messages> | 2023-12-14 | 2026-11-08 | E2 | F-NB-53 |
| ‘Touch Keyboard’ Implementations Have Improved Just 9% Since 2013 (60% Still Get it Wrong) | <https://baymard.com/research-articles/mobile-touch-keyboards> | 2015-12-15 | 2026-11-08 | E2 | F-NB-54, F-NB-55 |
| Provide a “Fully Automatic Address Lookup” Feature (55% Don’t) | <https://baymard.com/research-articles/automatic-address-lookup> | 2023-03-24 | 2026-11-08 | E2 | F-NB-56, F-NB-57 |
| Form Usability: Getting ‘Address Line 2’ Right | <https://baymard.com/research-articles/address-line-2> | 2022-10-04 | 2026-11-08 | E2 | F-NB-58 |
| Checkout UX: Avoid “Apply” Buttons for Most Fields (22% of Sites Don’t) | <https://baymard.com/research-articles/checkout-usability-apply-buttons> | 2012-07-11; updated 2025-05-14 | 2026-11-08 | E2 | F-NB-59 |
| What Is an Ecommerce Filter? UI Best Practices | <https://baymard.com/blog/ecommerce-filter-ui> | 2026-04-17 | 2026-11-08 | E4 | F-NB-60, F-NB-62 |
| Display “Applied Filters” in an Overview (28% Don’t) | <https://baymard.com/research-articles/how-to-design-applied-filters> | 2020-10-06; updated 2026-05-13 | 2026-11-08 | E2 | F-NB-61 |
| 6 Guidelines for Truncation Design | <https://baymard.com/research-articles/truncation-design> | 2014-05-21 | 2026-11-08 | E2 | F-NB-63 |
| 9 UX Best Practice Design Patterns for Autocomplete Suggestions (Only 19% Get Everything Right) | <https://baymard.com/research-articles/autocomplete-design> | 2022-08-02 | 2026-11-08 | E2 | F-NB-64 |
| Product List UX 2025: 8 Common Pitfalls & Best Practices (80% Have Serious Issues) | <https://baymard.com/research-articles/current-state-product-list-and-filtering> | 2024-08-22; updated 2025-09-09 | 2026-11-08 | E2 | F-NB-65 |
| Make Product Categories the Top-Level Navigation Items on Mobile Sites (33% Don’t) | <https://baymard.com/research-articles/main-navigation-product-categories> | 2023-01-24 | 2026-11-08 | E2 | F-NB-66 |
| Have a “View All” Option in the Main Navigation at Each Level of the Mobile Product Catalog (Only 24% Get It Right) | <https://baymard.com/research-articles/mobile-main-nav-view-all> | 2022-11-16 | 2026-11-08 | E2 | F-NB-67 |
| 42% of Mobile Homepages Risk Setting Wrong Expectations for Their Users | <https://baymard.com/research-articles/mobile-homepage-usability> | 2016-02-17 | 2026-11-08 | E2 | F-NB-68 |
| Accounts & Self-Service UX Research Update and Expansion: 3 Key Takeaways | <https://baymard.com/research-articles/accounts-and-self-service-ux-research-2026> | 2026-09-09 | 2026-11-08 | E2 | F-NB-69 |
| Homepage and Category Navigation UX 2026: 10 Pitfalls and Best Practices (64% of Sites Have Mediocre-to-Poor Performance) | <https://baymard.com/research-articles/ecommerce-navigation-best-practice> | 2024-08-06; updated 2026-10-13 | 2026-11-08 | E2 | F-NB-70 |

### Fetched but not cited by a numbered finding

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| 8 Recommendations for Creating Effective Input Fields | <https://baymard.com/blog/input-fields> | 2021-12-06; updated 2025-01-17 | 2026-11-08 | E4/E2 | none (NB "Additional pages fetched") |
| The State of Mobile E-Commerce Search and Category Navigation | <https://baymard.com/research-articles/mobile-ecommerce-search-and-navigation> | 2015-11-17 | 2026-11-08 | E2 (historical context) | none (NB "Additional pages fetched") |
| Drop-Down Mobile UX: Never Use Native Drop-Downs for Navigation | <https://baymard.com/research-articles/mobile-dropdown-navigation> | 2013-04-23 | 2026-11-08 | E2 (dated) | none (NB "Additional pages fetched") |

### Failed fetches (not evidence)

| URL | Outcome | Replacement |
|---|---|---|
| <https://baymard.com/labs/touch-keyboard-types> | "(400) Timeout fetching" | Public touch-keyboard research article (F-NB-54, F-NB-55) |

The DX coverage section also mentions an incidental Baymard industry page that was fetched but supplies no finding. The findings file does not record its URL, so it is not listed here.

### Cited in principles only

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| Baymard Institute, homepage and category navigation research (public articles) | <https://baymard.com/blog> | not recorded | not recorded | E2; e-commerce context | none (principle only: P-03) |
