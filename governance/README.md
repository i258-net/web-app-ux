---
id: GOV-INDEX
title: Governance and maintenance
type: index
status: active
updated: 2026-11-08
---

# Governance and maintenance

Lightweight processes that keep the knowledge base trustworthy as evidence, standards, and platforms change. The guiding rule: **Git-tracked Markdown is the single source of truth; nothing else (OpenViking, agent memory, chat transcripts) is authoritative.**

| File | Process |
|---|---|
| [`research-intake.md`](research-intake.md) | How new research enters: findings file → synthesis → PR. Source verification checklist. |
| [`pattern-lifecycle.md`](pattern-lifecycle.md) | When to create, extend, split, merge, or deprecate a pattern; identifier rules |
| [`conflict-resolution.md`](conflict-resolution.md) | Resolving disagreements between sources and between contributors |
| [`rubric-revision.md`](rubric-revision.md) | How dimensions, anchors, weights, and gates may change |
| [`review-process.md`](review-process.md) | What needs review, what does not; agent-proposed PRs |
| [`limitations.md`](limitations.md) | Known limitations and open research gaps |
| [`decisions/`](decisions/) | Architecture decision records (ADR-xxx) |

## Roles

- **Maintainer**: a human who approves significant changes. There is no automatic acceptance of research changes.
- **Contributor**: human or agent who proposes changes via pull request.
- **Validator**: human or agent who independently checks a PR against the source-verification checklist. May be a different model than the author.

## Change classes

| Class | Examples | Required |
|---|---|---|
| Trivial | Typos, broken-link fixes, formatting, metadata date bumps | Validation script passes. No review needed. |
| Minor | New evidence link added to an existing pattern; clarified wording with no change in recommendation | Validation + one reviewer skim |
| Significant | New pattern; changed recommendation; new or changed gate; new principle; rubric anchor or weight change; deprecation | Validation + source verification + maintainer approval; ADR for architectural changes |

## Dates and traceability

Every authoritative file has `updated:` in its front matter. Every cited page records access date and, where shown, publication/update date in the `sources/` register. When a recommendation changes, the old text is kept in Git history and the pattern's **Change log** section records what changed and why with a link to the new evidence.
