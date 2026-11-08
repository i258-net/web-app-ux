---
id: P-03
title: Information architecture
type: principle
topics: [information-architecture, grouping, labeling, hierarchy, mental-models]
dimensions: [D-02, D-06]
patterns: [PAT-SH-001, PAT-SH-004, PAT-SH-005, PAT-RS-003, PAT-DT-002]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# P-03 Information architecture

## Universal outcome

Content and functions are grouped and labeled the way users think about them, not the way the organization or the database is structured. The hierarchy is as shallow as the content allows, labels are understandable without context, and the same information architecture underlies every device, even when its presentation differs.

## Why it matters

- Findability precedes usability: users who cannot locate a function cannot use it. NN/g's IA guidance recommends validating categories with card sorting and tree testing because designers' groupings routinely differ from users' (E4, methodology-backed).
- Baymard's category-navigation research found that unclear or overlapping category names cause users to pick the wrong path and conclude a product does not exist (E2; e-commerce, but the mechanism generalizes).
- Deep hierarchies multiply the chance of a wrong turn at each level; breadth vs depth is a tradeoff, not a rule.

## How to recognize it

- Top-level categories are mutually exclusive and collectively cover the content; items are not reachable only through an unexpected parent.
- Labels use users' words (validated by research or search logs), not internal jargon.
- The same destinations exist on compact and expanded viewports; mobile does not silently drop sections.
- Search and filters reflect the same vocabulary as navigation.

## Contextual implementation notes

- **Compact:** expose top-level structure in a tab bar or a well-organized drawer; use hub pages for sections (PAT-MO-003, PAT-RS-003).
- **Expanded:** show more of the hierarchy at once (sidebar with sections, mega menus with grouping) (PAT-DT-002).
- **All:** consistent terminology across navigation, search, headings, and page titles (PAT-SH-001, PAT-SH-004).

## Evidence

- Nielsen Norman Group, "Information Architecture" topic and card-sorting guidance. https://www.nngroup.com/articles/card-sorting-definition/ — E4 (method guidance).
- Whitenton, K. "Flat vs. Deep Website Hierarchies." NN/g. https://www.nngroup.com/articles/flat-vs-deep-hierarchy/ — E4.
- Baymard Institute, homepage and category navigation research (public articles). https://baymard.com/blog — E2; e-commerce context.
- Rosenfeld, Morville, Arango. *Information Architecture: For the Web and Beyond* (4th ed.). — E4 (foundational text; not freely available).

## Evaluation

Primary dimension D-02; D-06 for labeling clarity. Tree testing and card sorting (user studies) are the only methods that verify the mental-model match.
