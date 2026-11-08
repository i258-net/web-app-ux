---
id: GOV-REVIEW
title: Review process for changes
type: process
status: active
updated: 2026-11-08
---

# Review process for changes

## Pull requests

All changes except direct trivial fixes by a maintainer arrive as pull requests. The PR template (`.github/PULL_REQUEST_TEMPLATE.md`) asks for: change class, affected IDs, findings file (if research), sources fetched, and validation output.

## What requires what

| Class | Checks | Reviewer |
|---|---|---|
| Trivial | `scripts/validate.py` passes | None (maintainer may push directly) |
| Minor | Validation; evidence link opened by the reviewer | One reviewer |
| Significant | Validation; full source verification checklist; ADR if architectural; OpenViking refresh after merge | Maintainer approval |

## Agent-proposed changes

- Agents open PRs like anyone else and must disclose themselves and the model used.
- Agent PRs are never auto-merged, and the verifying reviewer should be a human or a *different* model.
- Agents must not rewrite authoritative guidance silently; a change in a recommendation is always a significant change.

## After merge

Refresh the OpenViking resource per `integration/openviking.md` and confirm with a retrieval spot check.
