---
id: PAT-INDEX
title: Pattern library — how patterns are organized and written
type: index
status: active
updated: 2026-11-08
---

# Pattern library

Patterns are the smallest useful unit of design knowledge: one recurring design problem, the recommended behavior, the evidence, the alternatives, and the questions an evaluator should ask. They are organized by **scope** and tagged with **platform, viewport, and input applicability** so that a pattern can be found by problem and filtered by context.

| Directory | Prefix | Scope |
|---|---|---|
| `shared/` | `PAT-SH-` | Problems every web app has regardless of device: navigation, forms, search, feedback, errors, loading, empty states, destructive actions, onboarding, disclosure |
| `mobile/` | `PAT-MO-` | Small touch viewports: ergonomics, targets, keyboards, gestures, safe areas, sticky controls |
| `desktop/` | `PAT-DT-` | Wide pointer-and-keyboard contexts: density, sidebars, hover, shortcuts, tables, inline editing, multi-window |
| `responsive/` | `PAT-RS-` | How the *same task* changes across space and input: navigation transformation, reflow, prioritization, density, breakpoints, container queries, input detection |
| `pwa/` | `PAT-PW-` | Web-platform behaviors: browser vs installed, install prompts, history and deep links, reload and restoration, offline, sync, unsaved changes, notifications, platform limits |

A pattern lives in exactly one directory. Where a shared problem has a strong device-specific adaptation (e.g. forms on mobile), the shared pattern holds the universal guidance and links to the device pattern for the adaptation. Do not duplicate guidance across the two.

## Front matter schema

```yaml
---
id: PAT-SH-001                 # stable; never reused after deprecation
title: Short problem-oriented title
type: pattern
scope: shared | mobile | desktop | responsive | pwa
topics: [navigation, wayfinding]           # free-form, lowercase, used for retrieval
platforms: [mobile, tablet, desktop]       # where the guidance applies
viewports: [compact, medium, expanded]     # see rubric/dimensions.md for definitions
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-03, P-04]                   # principles this pattern serves
dimensions: [D-02]                         # rubric dimensions it informs
gates: [QG-010]                            # quality gates it relates to, if any
related: [PAT-MO-003, PAT-RS-001]
evidence_strength: strong | moderate | limited   # strongest class present and consistency across sources
status: active | draft | deprecated
updated: 2026-11-08
---
```

Viewport classes used throughout the repository (aligned to Material 3 window size classes because they are the only widely published, numerically defined scheme; the names are ours):

| Class | Width (CSS px / dp) | Typical devices |
|---|---|---|
| compact | < 600 | Phones in portrait |
| medium | 600 – 839 | Phones in landscape, small tablets, foldables unfolded in portrait |
| expanded | 840 – 1199 | Tablets, small laptops, resized desktop windows |
| large | 1200 – 1599 | Laptops, desktops |
| extra-large | ≥ 1600 | Large desktops, ultrawide |

Width **never** implies input modality. Patterns that depend on input must say "touch" or "pointer", not "mobile" or "desktop".

## Body sections (in this order)

1. **Problem** — what users are trying to do and what goes wrong.
2. **Recommendation** — the behavior to deliver. Outcome first; concrete implementation guidance second.
3. **Evidence** — bullet list of sources, each with class tag and URL, and what each source supports. Say when a claim is our interpretation.
4. **Alternatives and tradeoffs** — legitimate other approaches and when they are better.
5. **Exceptions and failure modes** — when the recommendation does not apply; common ways teams get it wrong.
6. **Evaluation questions** — observable questions an evaluator asks, each tagged with the method that can answer it (screenshot / prototype / running app / automated / user study).
7. **Related** — links to related patterns, principles, dimensions, gates.

Keep a pattern to roughly one screen of reading (400–1200 words). If it grows past that, it is probably two problems.
