<img src="assets/icon.svg" width="64" height="64" alt="">

# web-app-ux

A research-grounded, mobile-first knowledge base defining what excellent user experience means in responsive web applications and Progressive Web Apps (PWAs). It is written for two readers at once: humans designing or reviewing interfaces, and AI agents that retrieve small, relevant pieces of guidance on demand.

**Mobile-first, not mobile-only.** Mobile receives deep treatment because its constraints are the hardest (small screens, touch, thumbs, virtual keyboards). Desktop and tablet are equally legitimate product experiences and get deliberate guidance of their own. The goal is a great experience on every supported device, not one layout that technically fits everywhere.

## How the knowledge is organized

Knowledge is organized around **problems, behaviors, and patterns**, not around publishers. Every substantive document has a stable identifier, YAML front matter with platform and input applicability, and explicit evidence links.

| Directory | What it holds | Identifier prefix |
|---|---|---|
| [`principles/`](principles/README.md) | Fifteen cross-platform UX principles: the outcomes we want, independent of any component or layout | `P-xx` |
| [`patterns/`](patterns/README.md) | The pattern library, grouped by scope: `shared/`, `mobile/`, `desktop/`, `responsive/`, `pwa/` | `PAT-SH-xxx`, `PAT-MO-xxx`, `PAT-DT-xxx`, `PAT-RS-xxx`, `PAT-PW-xxx` |
| [`rubric/`](rubric/README.md) | Evaluation dimensions, behaviorally anchored scoring, device-specific results, and objective quality gates | `D-xx`, `QG-xxx` |
| [`evaluation/`](evaluation/README.md) | How to run a review: methods and what each can verify, the standard review output format, checklists | — |
| [`sources/`](sources/README.md) | Source register: one file per publisher with evidence classification, cited pages, access dates, and known limitations | `SRC-xxx` |
| [`examples/`](examples/README.md) | Representative evaluation scenarios and worked sample reviews | `EX-xx` |
| [`governance/`](governance/README.md) | Research intake, source verification, pattern lifecycle, conflict resolution, deprecation, decision records | `ADR-xxx` |
| [`integration/`](integration/openviking.md) | OpenViking ingestion, refresh, and retrieval validation | — |
| [`research/`](research/FINDINGS-FORMAT.md) | Working research findings that fed the synthesis. Attributable but **not authoritative** | `F-xx-nn` |
| `scripts/` | Validation tooling (structure, links, identifiers, front matter) | — |

Start with [`INDEX.md`](INDEX.md), a machine-readable and human-readable catalog of every identifier, title, and path.

## Evidence standard

Every recommendation is classified by the kind of evidence behind it. The scale is used identically in research findings, patterns, principles, rubric criteria, and quality gates.

| Class | Name | Treat as |
|---|---|---|
| **E1** | Formal standard | Verifiable requirement (e.g. WCAG 2.2 success criteria). Can back a quality gate. |
| **E2** | Empirical research | Strong guidance with stated context. Check generalizability (e.g. e-commerce vs general). |
| **E3** | Platform convention | Authoritative for that platform or design system. Not a universal rule for the web. |
| **E4** | Practitioner recommendation | Reasoned advice. Useful; weigh against E1–E3 when they disagree. |
| **E5** | Shipped example | Shows what is common. Says nothing by itself about usability. |

Details, including how conflicts between sources are resolved, are in [`sources/evidence-classes.md`](sources/evidence-classes.md).

## Using this with an agent

The companion skill **`web-app-ux-review`** (installed separately, outside this repository) is the procedural interface: it identifies the product and device scope, retrieves only the relevant principles, patterns, rubric criteria, and quality gates, inspects the artifact or application, and produces a source-grounded review. It reads this repository either through OpenViking (preferred, progressive disclosure) or directly from the Git checkout. See [`integration/openviking.md`](integration/openviking.md) and [`evaluation/retrieval-guide.md`](evaluation/retrieval-guide.md).

Retrieval is designed to be progressive: identify the design problem → read one pattern or principle → follow its evidence links → check its exceptions and related patterns. An agent should never need to load the whole repository.

## Status and honesty

This is a curated synthesis, not a replacement for user research. The rubric's five-level anchors and provisional weights have **not** been calibrated against human raters or real-user outcomes; see [`rubric/scoring.md`](rubric/scoring.md) and [`governance/limitations.md`](governance/limitations.md). Baymard findings mostly come from e-commerce studies and are marked as such. Apple and Material guidance are platform conventions, not web requirements.

## Contributing

See [`governance/README.md`](governance/README.md) for research intake, source verification, pattern lifecycle, and the review process for significant changes. Agent-proposed updates are welcome as pull requests and are never auto-merged.

## Validation

```bash
python3 scripts/validate.py
```

Checks directory structure, front matter, identifier uniqueness, cross-references, and internal links.
