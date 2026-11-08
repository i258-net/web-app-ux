---
id: SRC-INDEX
title: Source register
type: index
status: active
updated: 2026-11-08
---

# Source register

This directory has one file per publisher. Each file records how that publisher's material is classified on the evidence scale, how it may be quoted, its known limitations, and every page the research findings cited, with publication and access dates and the finding IDs that used it.

The register is built from `research/findings/*.md` and from the URLs cited in `principles/`. It adds no page that those files did not cite. Pages that failed to load are listed separately as failures, never as evidence.

## Publishers

"Pages" counts the distinct URLs in each file's main **Cited pages** table. A Material page and its published JSON payload count separately.

| ID | Publisher | Typical evidence class(es) | Scope and strengths | Key limitations | Pages | File |
|---|---|---|---|---|---:|---|
| SRC-001 | W3C and WHATWG | **E1** (WCAG success-criterion text and spec normative text); E4 (WCAG2Mobile, Understanding docs); E3/E4 (APG) | WCAG 2.2 conformance, mobile accessibility notes, APG keyboard models, Media Queries 4/5, Web App Manifest, HTML history | Conformance is a floor, not good UX. The mobile notes are drafts. Spec status is not browser support | 50 | [SRC-001-w3c.md](SRC-001-w3c.md) |
| SRC-002 | Nielsen Norman Group | **E2** (articles that report tests); **E4** (heuristics and guidelines) | Heuristics, mobile and desktop navigation, forms, tables, omnichannel, response times | Methods are seldom detailed, many articles are dated, web-content bias | 50 | [SRC-002-nngroup.md](SRC-002-nngroup.md) |
| SRC-003 | Baymard Institute | **E2, e-commerce context**; E4 (blog syntheses) | Large-scale testing of forms, keyboards, addresses, filtering, navigation, product lists | E-commerce scope, Premium paywall, prevalence figures are not effect sizes | 25 | [SRC-003-baymard.md](SRC-003-baymard.md) |
| SRC-004 | Apple Human Interface Guidelines | **E3 (Apple platforms)** | iOS, iPadOS, and macOS conventions: layout, controls, modality, keyboards, pointer, multitasking | Native-only. Uses pt units. 44×44 pt is the *default* and 28×28 pt the *minimum* on iOS/iPadOS. Two paths returned 404 | 26 | [SRC-004-apple-hig.md](SRC-004-apple-hig.md) |
| SRC-005 | Material Design 3 and Android Developers | **E3 (Material/Android)** | Window-size classes, canonical layouts, navigation components, fields, dialogs, snackbars | Uses dp units. Mostly undated. Expressive-version overlap. No M3 data-table page | 32 | [SRC-005-material.md](SRC-005-material.md) |
| SRC-006 | web.dev and Chrome for Developers | **E3** (platform behavior, Core Web Vitals thresholds); **E4** (tutorial advice) | Responsive and PWA courses, bfcache, viewport units, Core Web Vitals "good" thresholds at p75 | Chromium perspective, 2021–2022 course age, outdated iOS and push compatibility claims | 41 | [SRC-006-webdev.md](SRC-006-webdev.md) |
| SRC-007 | MDN Web Docs and browser-compat-data | **E3** (reference and dated compatibility); E4 (best-practice advice) | API, CSS, and HTML semantics. PWA guides and manifest members. Current browser support | Compatibility data goes stale. Some internal inconsistencies, such as `start_url` | 39 | [SRC-007-mdn.md](SRC-007-mdn.md) |
| SRC-008 | Design systems and product docs (Carbon, Atlassian, React, VS Code, Adrian Roselli) | **E3** (system conventions); E4 (rationale, practitioner) | Data tables, inline edit, optimistic UI, accessible responsive tables, command palette, settings scope | Each serves its own products' users. No comparative studies. Polaris and Fluent are not cited | 7 | [SRC-008-design-systems.md](SRC-008-design-systems.md) |
| SRC-009 | Mobbin | **E5 only** | What shipped apps commonly do, with named examples | Popularity is not usability. Partial public access. Undated. Curated sample | 10 | [SRC-009-mobbin.md](SRC-009-mobbin.md) |
| SRC-010 | Other (ISO 9241-11, Hoober, Butterick, Norman, Deceptive Design, Microsoft Inclusive Design, Miller and Card) | E1 (ISO definitions); E2 (Hoober); E4 (others) | Usability definition, thumb reach, line length, signifiers, deceptive patterns, inclusive design | **Cited only in principles. Not fetched during research.** Unverified until intake | 0 (6 principle-only) | [SRC-010-other.md](SRC-010-other.md) |
| SRC-011 | OpenViking documentation | Docs (E3-like); not UX evidence | Ingestion, refresh, retrieval, skills, MCP, for [`integration/openviking.md`](../integration/openviking.md) | Rolling docs not pinned to the installed version. No mutation tests | 17 | [SRC-011-openviking.md](SRC-011-openviking.md) |

## How to cite

1. **Classify the claim, not the publisher.** Use the scale and the disagreement rules in [`evidence-classes.md`](evidence-classes.md). A single publisher can supply several classes. For example, WCAG success-criterion text is E1 but the WCAG2Mobile note is E4, and an NN/g test report is E2 but an NN/g heuristic article is E4.
2. **Cite the page by URL** in the pattern, principle, or rubric file, followed by its class, for example `— E2 (e-commerce)`. Link to the publisher file here for its context and limitations.
3. **Only cite pages listed in a register table with a finding ID.** Rows marked "principle only" or "not recorded" have not been fetched and verified. Fetch the page and record a finding before relying on it (see [`governance/`](../governance/README.md)).
4. **Keep units and context attached.** Write CSS px, pt, dp, or cm with every number, and write "e-commerce" for Baymard results. Never use Apple or Material values, or Mobbin prevalence, as web-wide requirements.
5. **Respect licensing.** Paraphrase, and quote a phrase or an exact threshold at most. Never reproduce paywalled (Baymard Premium, ISO) or proprietary content (Mobbin screenshots).
6. **Re-check compatibility claims** (SRC-006 and SRC-007) during every refresh. They are dated snapshots, last checked 2026-11-08.
