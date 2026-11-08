---
id: GOV-INTAKE
title: Research intake and source verification
type: process
status: active
updated: 2026-11-08
---

# Research intake and source verification

## Flow

1. **Findings first.** New research is recorded in `research/findings/<assignment>.md` using `research/FINDINGS-FORMAT.md`. Findings are attributable, dated, and classified (E1–E5). They are not guidance.
2. **Synthesis.** A contributor (human or agent) proposes changes to `principles/`, `patterns/`, `rubric/`, or `sources/` that cite the findings. One PR per coherent topic.
3. **Verification.** A validator checks the PR against the checklist below. The validator should not be the author.
4. **Approval.** A maintainer merges significant changes. Minor and trivial changes follow `review-process.md`.
5. **Refresh.** After merge, refresh the OpenViking resource (`integration/openviking.md`).

## Source verification checklist

For each new or changed citation:

- [ ] The URL resolves and the page says what the finding claims (open it; do not trust a summary).
- [ ] The evidence class is correct. Only normative standard text is E1. Understanding/Techniques documents, W3C Notes (including WCAG2Mobile), tutorials, and design-system rationale are not E1.
- [ ] Numbers (thresholds, percentages, sample sizes) appear in the source verbatim. No rounding that changes meaning. No invented statistics.
- [ ] Context is recorded: platform (iOS/Android/web), domain (e-commerce, enterprise), device, study year where shown.
- [ ] Generalizability is stated when the source studied a narrow context.
- [ ] Paywalled content is cited only to the extent of its public summary.
- [ ] Access date recorded; publication/update date recorded when the page shows one.
- [ ] The publisher file in `sources/` is updated (new page added to its cited-pages table).
- [ ] Conflicts with existing guidance are noted in the pattern's *Alternatives and tradeoffs* or *Conflicts* section, not silently overwritten.

## Sources we accept

Formal standards bodies; platform owners' official documentation; research organizations that publish methodology (NN/g, Baymard); established design systems; peer-reviewed HCI research; reputable practitioner publications with clear reasoning. Mobbin and similar galleries are accepted as E5 only.

## Sources we treat with caution

Vendor marketing, undated blog posts without reasoning, AI-generated summaries, secondary summaries of research (cite the original), social media.

## Agent-proposed research

Agents may open PRs. The PR description must state the model, the pages fetched, and the findings file. Agent PRs are never auto-merged. A different model (or a human) performs verification.
