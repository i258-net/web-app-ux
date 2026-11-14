---
id: PAT-SH-014
title: Progressive disclosure — accordions, show more, steppers, and advanced settings
type: pattern
scope: shared
topics: [progressive-disclosure, accordions, show-more, truncation, steppers, wizards, advanced-settings]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-05, P-02, P-03, P-08]
dimensions: [D-06, D-02, D-03]
gates: [QG-001, QG-004, QG-020b]
related: [PAT-MO-008, PAT-RS-003, PAT-SH-002, PAT-SH-015, PAT-DT-002, PAT-SH-005]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Progressive disclosure — accordions, show more, steppers, and advanced settings

## Problem

Showing everything at once overwhelms users. Hiding too much makes needed information and options undiscoverable. Teams reach for accordions, "show more", multi-step wizards, and "Advanced" sections to manage complexity, often splitting by what *fits the layout* rather than by what users need. The result: frequent options buried a level down, content users must expand one section at a time, a "show more" nobody notices, and wizards that hide the review users need before committing.

## Recommendation

**Outcome:** the primary task shows what most users need. Secondary material is one obvious, well-labeled step away. Nothing required for the main task is hidden.

1. **Split by task importance, not layout.** Base the split on usage data or research. Primary and frequent options stay visible; advanced or rare options go to the second level. Validate that the hidden level is genuinely rare.
2. **Make the route to hidden content obvious and specific.** "Show all 24 brands", "Add apartment, suite, etc.", and "Advanced filters (3)" beat "More" or a bare chevron. Show the count of hidden items or active settings in the label.
3. **Accordions are for selective reading.**
   - Use them when users need *different* subsets of the sections.
   - Prefer showing content openly, or with an in-page overview and anchor links, when users need most sections or must compare across them.
   - Allow several sections open at once unless there is a strong reason not to.
   - Headings must be descriptive.
4. **Use correct disclosure semantics.** The trigger is a real button with an expanded state (`aria-expanded`); Enter and Space toggle it. The revealed content follows the trigger in focus order (QG-004). Expanding never moves focus or navigates (QG-020b).
5. **Use "show more" for lists only with a discoverable expansion.** Keep selected values visible even when the list is collapsed. Avoid nested scroll areas.
6. **Use steppers and wizards to reduce what users consider at once**, not to inflate step counts.
   - Show progress ("Step 2 of 4", with step names).
   - Allow Back without data loss.
   - Ask only questions relevant to earlier answers (branching).
   - End with a review screen where every value can be edited before final commit.
   - Fewer total fields matter more than fewer steps.
7. **Keep disclosed state.** Remember expanded sections and "Advanced" toggles across Back and reload when users return to the same task (PAT-PW-004).
8. **Disclose, do not delete, at compact widths.** Content prioritization moves secondary content behind disclosure. It does not remove functionality (PAT-RS-003). Truncation and line clamping are in PAT-MO-008.
9. **Do not hide errors.** If a collapsed section contains a validation error, expand it or flag the section heading.

## Evidence

- **E4** Nielsen Norman Group, "Progressive Disclosure". https://www.nngroup.com/articles/progressive-disclosure/ — Show primary functions first and move advanced or rare options to a secondary level. The split must match real task importance, and the route must be obvious and well labeled.
- **E4** Nielsen Norman Group, "Accordions Are Not Always the Answer for Complex Content on Desktops". https://www.nngroup.com/articles/accordions-complex-content/ — Expanding sections increases interaction cost and hides information. When users need most sections, exposed content is easier. *Desktop focus.*
- **E2** Baymard Institute, "6 Guidelines for Truncation Design". https://baymard.com/research-articles/truncation-design — Truncated lists preserved overview only if users noticed the expansion control; otherwise they took the partial list as complete.
- **E2** Baymard Institute, "Form Usability: Getting 'Address Line 2' Right". https://baymard.com/research-articles/address-line-2 — An exposed optional field confused users who did not need it. A clearly described link to reveal it worked better. *E-commerce checkout.*
- **E2** Baymard Institute, "Checkout Optimization: 5 Ways to Minimize Form Fields". https://baymard.com/research-articles/checkout-flow-average-form-fields — The number of fields generally matters more than the number of steps. *Checkout.*
- **E4** Nielsen Norman Group, "Few Guesses, More Success: 4 Principles to Reduce Cognitive Load in Forms". https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/ — Predictable progression and relevant branching reduce cognitive load.
- **E2** Nielsen Norman Group, "Hamburger Menus and Hidden Navigation Hurt UX Metrics". https://www.nngroup.com/articles/hamburger-menus/ — Hidden navigation is used less, which is the cost side of disclosure.
- **E3** W3C WAI, "APG disclosure pattern". https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/ — Use a button with `aria-expanded`; Enter and Space toggle. (E3 per `sources/evidence-classes.md`.)
- **E3** Apple, "Sidebars". https://developer.apple.com/design/human-interface-guidelines/sidebars.md — Generally no more than two sidebar levels, with disclosure for extensive content. Apple platforms.
- **E3** Google Material Design, "Canonical layouts". https://m3.material.io/foundations/layout/canonical-examples — The supporting pane moves below the primary content on compact and medium windows, and a bottom sheet is an option. Material convention.

## Alternatives and tradeoffs

- **Disclosure vs overview: a real tension.** Disclosure reduces load only when the hidden material is genuinely secondary (NN/g E4). Hiding destinations or commonly needed sections raises cost (NN/g E2/E4, Baymard E2). Decide by what users must inspect *together*. Neither "minimal" nor "show everything" is correct by default.
- **Accordion vs tabs vs anchored long page.** Tabs suit parallel, mutually exclusive views. Accordions suit selective reading on narrow screens. An anchored long page suits reading and comparison on wide screens. Responsive designs may switch between them (PAT-RS-003).
- **Wizard vs single page.** A wizard helps with branching and long, high-stakes flows. A single page helps with review and editing. A single page with section headings and a sticky progress summary is a legitimate middle ground.

## Exceptions and failure modes

- Legally required disclosures must not be hidden behind optional expansion.
- Failure modes:
  - collapsing every FAQ answer so users must open each one;
  - an "Advanced" section holding a setting most users need;
  - a chevron-only trigger with no accessible name;
  - expanded content inserted far from the trigger in DOM order;
  - wizard Back that clears answers;
  - no final review;
  - a collapsed section hiding an error.

## Evaluation questions

1. Is anything required for the primary task hidden behind disclosure? [screenshot] [prototype]
2. Are disclosure labels specific, and do they show counts where useful? [screenshot]
3. Do disclosure triggers expose expanded state and work by keyboard? [running app] [automated]
4. In wizards, are progress, Back without loss, and a final editable review present? [running app]
5. Do users notice and use "show more" when the item they need is hidden? [user study]
6. Are expanded states and wizard answers retained after Back or reload? [running app]

## Related

- Principles: P-05, P-02, P-03, P-08
- Dimensions: D-06, D-02, D-03
- Gates: QG-001, QG-004, QG-020b
- Patterns: PAT-MO-008 (truncation), PAT-RS-003 (content prioritization), PAT-SH-002 (forms), PAT-SH-015 (dialogs vs inline expansion), PAT-DT-002 (hierarchical navigation), PAT-SH-005 (filter value lists)

## Change log

- 2026-11-08 — Initial version (ADR-001).
