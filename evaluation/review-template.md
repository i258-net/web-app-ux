---
id: EVAL-TEMPLATE
title: Standard review output format
type: reference
status: active
updated: 2026-11-08
---

# Standard review output format

Use this structure for every review. Sections may be brief; none may be silently omitted. Replace angle-bracket text.

```markdown
# UX review: <product / feature>

## 1. Scope and assumptions
- Product and primary users: <…>
- Primary tasks examined: <T1, T2, …>
- Device contexts in scope: mobile | tablet | desktop | responsive transitions | PWA (and which are N/A, with reason)
- Input modalities examined: touch | pointer | keyboard | assistive tech (named)
- Method(s): screenshots (viewports: …) | prototype | running app (device/browser/network) | automated (tools) | user study (n, protocol)
- What this review cannot verify: <explicit list from evaluation/methods.md>
- Assumptions: <…>

## 2. Blocking conditions
<None found | List each: finding ID, context, why it blocks (rubric/scoring.md §4)>

## 3. Results by device context
For each context evaluated:

### <Mobile | Desktop | Tablet | Responsive transitions | PWA>
| Dimension | Level (1–5 / N/A / insufficient evidence) | Confidence | Key evidence |
|---|---|---|---|
| D-01 … D-10 | | | |
Narrative: 2–5 sentences on the worst-affected primary task and the main strengths.

## 4. Overall cross-device task effectiveness
<pass | pass with major issues | fail | insufficient evidence> — <explanation referencing D-01 and D-10 across contexts; with insufficient evidence, give the scoped result for evaluated contexts and name the missing context or method>

## 5. Findings (ordered by severity, then dimension)
### F-01 <short title> — <Blocker | Major | Minor | Suggestion>
- Context: <mobile/desktop/…>; Dimension: <D-xx>; Gate: <QG-xxx or —>
- Label: <verified | likely concern | untested>
- **Observed:** <what was seen, where, with method and viewport/device>
- **Inferred:** <interpretation; keep separate from observed>
- Confidence: <high | medium | low>
- Supporting guidance: <PAT-xx-xxx title> (<evidence class of the key source>), <P-xx>
- **Recommendation:** <specific change>
- Alternatives / tradeoffs: <if relevant>

## 6. Quality gates checked
| Gate | Result (pass / fail / not verified) | Method | Note |
|---|---|---|---|

## 7. Strengths worth keeping
<bullets, each with context>

## 8. Confidence and limitations
<What was not tested; what would change the assessment; recommended next verification steps (e.g. AT test on iOS VoiceOver, field CWV)>

## 9. Sources applied
<List of pattern IDs and principle IDs used, with their primary source URLs>
```

## Writing rules

- Lead with blocking conditions and the worst context. Do not bury a mobile blocker under desktop praise.
- Observed and inferred are separate lines in every finding.
- Every recommendation cites at least one pattern or principle; patterns carry the evidence links.
- Do not universalize platform conventions: say "Apple HIG recommends 44 pt for iOS; the WCAG minimum is 24 px; we recommend 44–48 px for primary touch targets" rather than "must be 44 pt".
- Report "not verified" rather than guessing. A guess labeled as a guess is acceptable in *Inferred*.
