---
id: P-INDEX
title: Foundational UX principles
type: index
status: active
updated: 2026-11-08
---

# Foundational UX principles

Principles describe the **outcome** an excellent web application achieves. They never mandate a specific component or layout. Each is cross-platform; the contextual advice for realizing it on touch, pointer, or keyboard lives in the pattern library.

| ID | Principle | Primary rubric dimension |
|---|---|---|
| [P-01](P-01-task-effectiveness.md) | Task effectiveness and efficiency | D-01 |
| [P-02](P-02-discoverability-learnability.md) | Discoverability and learnability | D-03 |
| [P-03](P-03-information-architecture.md) | Information architecture | D-02 |
| [P-04](P-04-navigation-orientation.md) | Navigation and orientation | D-02 |
| [P-05](P-05-cognitive-clarity.md) | Cognitive clarity and mental models | D-06 |
| [P-06](P-06-interaction-ergonomics.md) | Interaction ergonomics | D-03 |
| [P-07](P-07-input-efficiency.md) | Input efficiency | D-04 |
| [P-08](P-08-visual-hierarchy-readability.md) | Visual hierarchy and readability | D-05 |
| [P-09](P-09-consistency-familiarity.md) | Consistency and platform familiarity | D-10 |
| [P-10](P-10-feedback-predictability.md) | System feedback and predictable behavior | D-07 |
| [P-11](P-11-error-prevention-recovery.md) | Error prevention and recovery | D-07 |
| [P-12](P-12-accessibility-inclusion.md) | Accessibility and inclusive design | D-08 |
| [P-13](P-13-performance-responsiveness.md) | Performance and responsiveness | D-09 |
| [P-14](P-14-control-privacy-trust.md) | User control, privacy, and trust | D-09 |
| [P-15](P-15-craft-delight.md) | Visual craft and appropriate delight | D-05 |

## Universal vs contextual

Each principle file has two parts: **the universal outcome** (true on every device) and **contextual implementation notes** (how the outcome is typically achieved on touch, pointer, keyboard, and assistive technology). Only the first part is a principle; the second is a pointer into patterns.

## Front matter schema

```yaml
---
id: P-01
title: Task effectiveness and efficiency
type: principle
topics: [tasks, efficiency]
dimensions: [D-01]
patterns: [PAT-SH-001, ...]
evidence_strength: strong | moderate | limited
status: active
updated: 2026-11-08
---
```
