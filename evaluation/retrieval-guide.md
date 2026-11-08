---
id: EVAL-RETRIEVAL
title: Retrieval guide — finding the right knowledge without loading everything
type: reference
status: active
updated: 2026-11-08
---

# Retrieval guide

The repository is designed for **progressive discovery**. Whether you are a person or an agent, follow the same path.

## 1. Name the design problem

Translate what you are looking at into a problem, not a component. "Hamburger menu" → *navigation on compact viewports*; "red text under field" → *validation and error messages*; "spinner" → *loading states*.

## 2. Pick the entry point

| You want | Go to |
|---|---|
| The outcome that matters and why | `principles/P-xx-*.md` (15 files, ~1 screen each) |
| Concrete guidance for a problem | `patterns/<scope>/PAT-*.md` — use `INDEX.md` or `index.json` to find by title/topics; filter by `platforms`, `inputs`, `viewports` |
| How to judge it | `rubric/dimensions.md` → the one `## D-xx` section you need |
| Whether it is a hard requirement | `rubric/quality-gates.md` → the relevant `QG-xxx` rows |
| Whether the method can prove it | `evaluation/methods.md` |
| How strong the evidence is | the pattern's *Evidence* section → `sources/SRC-0xx-<publisher>.md` (index in `sources/README.md`) |

## 3. Follow references, don't browse

Each pattern's `related:` list and *Related* section point to the adjacent patterns (e.g. shared form guidance → mobile keyboard pattern → responsive same-task variants). Follow those rather than reading a whole directory.

## 4. Stop when the questions are answered

A typical review of one screen needs 3–6 patterns, 1–3 dimension sections, and the gates table rows that match, **in addition to** the standing documents every review reads once (methods, review template, scoring). If you are loading more than ~10 patterns for one screen, you are browsing, not retrieving.

## With OpenViking

The repository is ingested as a Git-watched resource (see `integration/openviking.md`). Use semantic `find` scoped to the resource URI to locate candidate documents by problem description, read the **abstract** (Level 0) or **overview** (Level 1) to confirm relevance, then read the full document (Level 2) only for the 3–6 that matter. OpenViking renames files by title and may split them into section chunks; resolve IDs with `grep "id: PAT-…"` rather than by filename. Example queries that work well: "mobile form virtual keyboard obscures submit button", "desktop data table keyboard selection", "PWA back button standalone mode".

## Without OpenViking

Use `INDEX.md` (or `index.json` for programmatic access) to match titles and topics, then open the files. `grep -ril "<term>" patterns/` is a fine fallback. The structure is the retrieval system; no database is needed.

## Staleness check

Compare the `updated:` field in the retrieved file with the current Git checkout, or check the Git watch's last successful run (`ov task watch ls`) against the last commit time. If the watch is behind, the OpenViking copy may be stale; prefer the Git copy and trigger the watch (`ov task watch trigger <id>`).
