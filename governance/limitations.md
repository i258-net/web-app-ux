---
id: GOV-LIMITATIONS
title: Known limitations and research gaps
type: reference
status: active
updated: 2026-11-08
---

# Known limitations and research gaps

Honest accounting of what this knowledge base is and is not. Update when gaps close or new ones appear.

## Methodological limitations

1. **No calibration.** The five-level anchors and the provisional weights in `rubric/scoring.md` have not been tested for inter-rater reliability or correlated with real-user outcomes. Scores are structured judgments, not measurements.
2. **Synthesis by language models.** Research extraction and pattern drafting were performed by AI agents reading original sources, with a different model performing independent verification (see `research/VALIDATION-LOG.md`). Human review has not yet occurred. Misreadings are possible; every claim carries a URL so it can be checked.
3. **Secondary restatement of some classic research.** Response-time limits (Miller 1968; Card et al. 1991), the aesthetic–usability effect (Kurosu & Kashimura 1995), and reading-pattern findings are cited via NN/g restatements, because the originals are behind publisher paywalls. They are marked E4 restating E2.
4. **Paywalled sources.** Baymard's full reports and ISO 9241-11 were not read; only public summaries and definitions are used.
5. **Access dates matter.** Platform guidance (Apple HIG, Material 3, browser compatibility) changes. All platform claims are dated 2026-11-08 and must be re-verified before being relied on later.

## Coverage gaps (candidates for future patterns or research)

- **Tablet-specific empirical research** is thin everywhere; tablet guidance here rests mainly on Apple and Material conventions (E3) and inference.
- **Foldables and multi-screen** devices: platform documentation exists (viewport segments) but little usability evidence.
- **Voice and conversational input**, **gaming controllers**, **TV browsers**, and **automotive** web are out of scope.
- **Internationalization**: text expansion, right-to-left layouts, locale-specific input formats are mentioned only in passing.
- **Data visualization** usability (charts on small screens) is not covered.
- **Authentication flows** beyond WCAG 3.3.8 (passkeys, magic links, MFA UX) deserve a pattern.
- **Notifications content design** (what to say, frequency) is covered only as permission timing.
- **Cross-device continuity** (handoff, sync conflicts) rests mostly on design-system and platform documentation, with limited empirical evidence.
- **Quantitative thresholds** for density, line length, and animation duration are conventions, not experimental results; the knowledge base says so where it uses them.
- **Deceptive patterns** are covered as a principle (P-14) without a dedicated pattern catalog.

## Evidence-quality caveats recorded in findings

- Baymard findings are e-commerce; generalization to other domains is an inference (`research/findings/nngroup-baymard.md`, F-NB-43/44).
- WCAG2Mobile is an unfinished draft Note; some thumb-reach and keyboard advice traces to its 2015 predecessor (`research/findings/standards-platforms.md`, Disagreement 8).
- Apple's current control-size table reads 44 pt *default* / 28 pt *minimum*, not the commonly repeated "44 pt minimum" (F-SP-48).
- Some web.dev course pages contain compatibility statements that are out of date relative to MDN data (`research/findings/web-platform.md`, Disagreements).
- Mobbin shows prevalence only (E5); no usability inference is drawn from it.

## Integration limitations

See `integration/openviking.md` §Verification log for what was and was not exercised against the OpenViking server, including whether in-place refresh of an existing resource URI works on the installed client/server versions.
