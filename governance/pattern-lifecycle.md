---
id: GOV-LIFECYCLE
title: Pattern lifecycle and identifier rules
type: process
status: active
updated: 2026-11-08
---

# Pattern lifecycle and identifier rules

## When to create a pattern

Create a new pattern only when one of these holds:

- A recurring design problem has no home in an existing pattern.
- New empirical evidence changes guidance enough that an existing pattern would become incoherent.
- A platform introduces a meaningful new capability or constraint (e.g. a new viewport unit, a new permission model).
- An evaluation exposed a gap: the reviewer needed guidance that did not exist.
- An existing pattern has become too broad to apply (then **split**, keeping the original ID for the dominant half and recording the split).

Prefer **extending** an existing pattern over creating a neighbor that overlaps it.

## When to merge

Two patterns that are always retrieved together and share most evidence should merge. Keep the lower ID, deprecate the other with a pointer.

## Identifiers

- Format: `PAT-<SCOPE>-<nnn>` with scope `SH`, `MO`, `DT`, `RS`, `PW`; principles `P-nn`; dimensions `D-nn`; gates `QG-nnn`; sources `SRC-nnn`; examples `EX-nn`; decisions `ADR-nnn`.
- IDs are **never reused**. A deprecated ID stays in `INDEX.md` with status `deprecated` and a `superseded_by` field.
- The filename contains the ID and a slug: `PAT-SH-003-form-validation.md`. The slug may change; the ID may not.
- Moving a pattern between scopes requires a new ID and deprecation of the old (scope is part of the ID).

## Deprecation

1. Set `status: deprecated` and add `superseded_by:` (or `deprecated_reason:` if nothing replaces it).
2. Keep the file with a short notice at the top; do not delete it for at least one release cycle.
3. Update `INDEX.md` and any `related:` references.
4. Record the deprecation in the pattern's change log and, if it reflects a shift in evidence, in an ADR.

## Platform-specific guidance

Guidance tied to a platform version or browser capability must name the platform and record the access date. When platforms change (e.g. a browser gains installability, Safari changes storage eviction), update the pattern's *Exceptions and failure modes* and bump `updated:`. Never present platform guidance as universal.

## Change log

Each pattern ends with a `## Change log` section: date, change class, one line, link to PR or ADR. Trivial changes need no entry.
