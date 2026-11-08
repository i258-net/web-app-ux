---
id: ADR-001
title: Knowledge architecture, identifiers, and evidence scale
type: decision
status: accepted
updated: 2026-11-08
---

# ADR-001: Knowledge architecture, identifiers, and evidence scale

## Context

The knowledge base must serve human browsing and agent retrieval, remain Git-authoritative, and be ingested into OpenViking for progressive retrieval. Source material spans formal standards (WCAG), empirical research (NN/g, Baymard), platform conventions (Apple HIG, Material, web.dev, MDN), and shipped examples (Mobbin), which make different kinds of claims.

## Decisions

1. **Organize by problem, not publisher.** `principles/`, `patterns/{shared,mobile,desktop,responsive,pwa}/`, `rubric/`, with a `sources/` register for traceability. Publisher-centric summaries are not authoritative content.
2. **One pattern per scope directory, device applicability in metadata.** We keep the device directories because retrieval by "mobile" or "pwa" is a dominant access path, but every pattern also carries `platforms`, `viewports`, and `inputs` front matter so cross-cutting queries work. Shared problems with device adaptations live in `shared/` and link to the adaptation rather than duplicating.
3. **Five evidence classes E1–E5**, used identically everywhere, with E1 reserved for normative standard text.
4. **Stable identifiers** with scope in the ID; never reused.
5. **Viewport classes aligned to Material 3 window size classes** (compact < 600, medium 600–839, expanded 840–1199, large 1200–1599, extra-large ≥ 1600 CSS px) because they are the only widely published numeric scheme; input modality is always stated separately from viewport.
6. **Rubric separated into dimensions (judgment), scoring (procedure), and quality gates (objective)**, with per-device-context results and explicit blocking conditions.
7. **No database or custom retrieval service.** Markdown + front matter + `INDEX.md` + OpenViking's existing ingestion and semantic retrieval.
8. **Research findings kept in-repo under `research/`** for traceability, clearly labeled non-authoritative.

## Consequences

- Agents retrieve small files by problem and filter by metadata.
- Device-specific adaptation must be cross-linked carefully; the validator checks `related:` links resolve.
- Changing scope of a pattern requires a new ID.

## Alternatives considered

- Single flat `patterns/` directory with metadata only: cleaner hierarchy, but weaker browsability and weaker OpenViking directory-level abstracts for "mobile" or "pwa" queries.
- Publisher-based organization: rejected; it reproduces the sources rather than synthesizing them.
