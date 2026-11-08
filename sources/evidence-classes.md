---
id: SRC-000
title: Evidence classes and how to weigh them
type: reference
topics: [evidence, methodology, citations]
status: active
updated: 2026-11-08
---

# Evidence classes and how to weigh them

Every claim in this knowledge base carries an evidence class. The class describes **what kind of claim the source makes**, not how much we like the source.

## The scale

| Class | Name | What it is | Typical sources | Can it back a quality gate? |
|---|---|---|---|---|
| **E1** | Formal standard | Normative, testable requirements from a standards body or specification | WCAG 2.2 success criteria; HTML, CSS, and Web App Manifest specifications | Yes |
| **E2** | Empirical research | Findings from moderated or unmoderated usability testing, controlled experiments, eye-tracking, or large-scale behavioral observation | Baymard Institute studies; NN/g articles that report test findings | Yes, if the measurement is objective and the context matches (otherwise it anchors a rubric level) |
| **E3** | Platform convention | Documented guidance from a platform owner or a widely adopted design system | Apple HIG; Material Design 3; web.dev and MDN platform documentation; WAI-ARIA Authoring Practices | Only for the platform in question, or when the threshold is a recommended quality threshold rather than a standard |
| **E4** | Practitioner recommendation | Expert reasoning or synthesized best practice with no described study | NN/g opinion pieces; web.dev tutorials; design-system rationale text; practitioner articles | No (it anchors rubric levels) |
| **E5** | Shipped example | Observation of what real products do | Mobbin; product teardowns | No |

## How the classes are used

- **Principles** cite the strongest available evidence and say when a principle rests on E4 reasoning alone.
- **Patterns** list every supporting source with its class. A pattern whose only support is E5 is labeled *convention observed, usability unverified*.
- **Rubric dimensions** anchor their behavioral levels in E1–E4; an evaluator must still observe the behavior.
- **Quality gates** require E1 (a standard) or a clearly labeled **recommended threshold** drawn from E2/E3 (e.g. Core Web Vitals "good" thresholds, 44–48 px comfortable touch targets). The two are never conflated.

## Resolving disagreements

When sources disagree, we do not average them. We:

1. **Name the disagreement** explicitly in the pattern's *Alternatives and tradeoffs* or *Conflicts* section.
2. **Check whether the claims are the same kind.** WCAG 2.5.8 (24×24 CSS px, E1) is a legal-style minimum; Apple's 44×44 pt and Material's 48×48 dp (E3) are comfort recommendations. These do not conflict; they answer different questions.
3. **Check context.** Baymard's checkout findings are about e-commerce purchase funnels. They often generalize to any high-stakes form, but we say "likely generalizes" rather than "proven".
4. **Prefer the stronger class only when the question is the same.** E1 beats E3 for *requirements*. E2 beats E4 for *what users actually do*. E3 beats E2 for *what users of that platform expect*, because convention is itself the mechanism.
5. **Record the tradeoff** rather than forcing consensus. Where evidence is genuinely split, the pattern says so and the rubric treats either choice as acceptable if executed well.

## What we refuse to do

- Fabricate study results, percentages, or sample sizes.
- Cite a page that was not fetched and read.
- Treat Apple or Material conventions as web-wide requirements.
- Treat the popularity of a design on Mobbin as evidence that it works.
- Upgrade an informative W3C note (such as WCAG2Mobile or Understanding documents) to E1. Only success criteria text is normative.

## Recording a source

Each publisher has a file in `sources/` with: publisher, scope, evidence class(es) it typically provides, access and publication dates per cited page, licensing or paywall notes, and known limitations. Individual pattern files cite pages by URL and link to the publisher file.
