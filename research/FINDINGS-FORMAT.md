# Research findings format

Research agents write findings here. This directory is **working material**, not authoritative guidance.
Authoritative guidance lives in `principles/`, `patterns/`, `rubric/`, and `sources/`, and is synthesized by the orchestrator from these findings.

## Rules

1. One file per research assignment: `research/findings/<assignment>.md`.
2. Every finding must carry a **source URL that you actually fetched**. If you could not fetch a page, say so and do not cite it.
3. Separate **Finding** (what the source says) from **Interpretation** (what we think it implies). Never blend them.
4. Classify evidence using the shared scale below. Do not invent study results, sample sizes, or percentages that are not in the source.
5. Mark generalizability: does this finding apply broadly, or only to the context the source studied (e.g. e-commerce checkout, iOS native apps)?
6. Quote sparingly (a phrase, not paragraphs). Paraphrase. Respect paywalls: if content is behind a paywall, record only what the public abstract or summary states.
7. Record the access date (today) and the publication/update date if the page shows one.

## Evidence classes (shared across the whole knowledge base)

| Class | Name | Meaning | Examples |
|---|---|---|---|
| E1 | Formal standard | Normative, testable requirements from a standards body | WCAG 2.2 success criteria, HTML/CSS specifications |
| E2 | Empirical research | Findings from usability testing, controlled studies, large-scale observation | Baymard usability studies, NN/g research articles reporting test findings |
| E3 | Platform convention | Documented guidance from a platform owner or widely adopted design system | Apple HIG, Material Design, web.dev platform guidance, MDN compatibility data |
| E4 | Practitioner recommendation | Expert opinion or synthesized best practice without a described study | NN/g opinion articles, web.dev tutorials, practitioner blogs |
| E5 | Shipped example | Observation of what real products do | Mobbin screenshots, product teardowns |

E5 shows what is common, **not** what is usable. E3 is authoritative for its platform, **not** universal.

## Finding entry template

```markdown
### F-<assignment>-<nn>: <short claim>

- **Source:** <title> — <URL>
- **Publisher:** <publisher>
- **Published/updated:** <date or "not shown">
- **Accessed:** 2026-11-08
- **Evidence class:** E1 | E2 | E3 | E4 | E5
- **Finding:** <what the source actually states, paraphrased>
- **Interpretation:** <what this implies for web-app UX guidance; may be empty>
- **Applies to:** <platforms: mobile / tablet / desktop / all; input: touch / pointer / keyboard / AT; context: general / e-commerce / native-only / ...>
- **Generalizability:** high | medium | low — <why>
- **Conflicts/tensions:** <other findings or sources that disagree, if any>
- **Candidate knowledge targets:** <principle or pattern topic(s) this should feed>
```

## Deliverable per assignment

1. The findings file (20–60 findings is a typical useful range; quality over count).
2. A short "Coverage and gaps" section at the end: what you could not verify, pages that failed to load, and topics the sources do not address.
3. A short "Disagreements" section listing any cross-source tensions you noticed.
