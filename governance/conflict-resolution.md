---
id: GOV-CONFLICT
title: Resolving conflicting evidence and contributor disagreement
type: process
status: active
updated: 2026-11-08
---

# Resolving conflicting evidence

## Between sources

Follow `sources/evidence-classes.md` §Resolving disagreements. In summary:

1. Name the conflict in the pattern.
2. Decide whether the sources answer the *same question* (minimum vs recommendation; iOS vs web; e-commerce vs general).
3. If the same question: prefer the stronger evidence class and the closer context.
4. If different questions: record both with their scope. That is not a conflict.
5. If genuinely split: document the tradeoff and make the rubric accept either when well executed.

Recorded conflicts live in the pattern's *Alternatives and tradeoffs* section and, when repository-wide, in `governance/decisions/`.

## Between contributors

- Disagreements are resolved on evidence, in the PR. The PR must link the sources.
- If unresolved, the maintainer decides and records an ADR with the reasoning and the dissent.
- A recommendation is not changed because one review found a counterexample; a counterexample becomes an *Exception* unless it is backed by evidence stronger than the original.

## Between the rubric and a pattern

The pattern is the detailed source; the rubric anchors summarize. If they diverge, fix the rubric anchor or the pattern explicitly in the same PR, and note it in `rubric-revision.md`'s log.
