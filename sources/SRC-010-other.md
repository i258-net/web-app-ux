---
id: SRC-010
title: Other cited sources (ISO 9241-11, Hoober, Butterick, Norman, Deceptive Design, Microsoft Inclusive Design, Miller and Card)
type: source
publisher: Various
evidence_classes: [E1, E2, E4]
status: active
updated: 2026-11-08
---

# SRC-010 Other cited sources

## Publisher and scope

This file registers sources that the **principles** cite but that fit no other publisher file. **None of them appears in any research findings file or fetch log.** The research assignments did not fetch or read them. They entered the principles during synthesis.

`evidence-classes.md` says we never cite a page that was not fetched and read. Each row below is therefore marked **unverified** until a research intake fetches the page and records a finding (see `governance/`).

| Source | Used in | Claimed class | What it is used for |
|---|---|---|---|
| ISO 9241-11:2018, *Usability: Definitions and concepts* | P-01 | E1 (definitional) | The definition of usability as effectiveness, efficiency, and satisfaction in a specified context of use |
| Don Norman, *Signifiers, not affordances* (jnd.org) | P-02 | E4 | The distinction between signifiers and affordances |
| Steven Hoober, *How Do Users Really Hold Mobile Devices?* (UXmatters, 2013) | P-06 | E2 (observational, with sampling limits) | How people hold phones and reach with the thumb |
| Matthew Butterick, *Practical Typography*, "Line length" | P-08 | E4 | Typographic measure |
| Microsoft Inclusive Design toolkit | P-12 | E4 | Inclusive-design framing (permanent, temporary, and situational disability) |
| Harry Brignull, Deceptive Design (deceptive.design) | P-14 | E4 | A catalog of deceptive patterns |
| Miller (1968); Card, Robertson & Mackinlay (1991) | P-10 | E2 origin (not fetched) | The 0.1 s, 1 s, and 10 s response-time limits, cited only **through** NN/g's restatement (SRC-002, F-WP-79 and F-NB-28). No URL is recorded |

## How to classify their material

- **ISO 9241-11.** Only the normative definitions count as E1, and they are definitions, not testable UI requirements. Never use ISO 9241-11 to back a quality gate.
- **Hoober (2013).** E2 observational field data: people were observed in public, with no controlled sample. It is directional evidence that grips vary and change, **not** a thumb-zone map with exact boundaries. It predates today's larger phones.
- **Norman, Butterick, Microsoft Inclusive Design, and Deceptive Design.** E4 expert reasoning or catalogs. Use them to anchor rubric levels and vocabulary, not gates. Deceptive Design is a catalog of examples, so its examples are E5 for "this exists" and E4 for "this is harmful".
- **Miller and Card.** The original papers were not read. Cite the NN/g restatement as E4 restating E2 and do not attribute specific numbers to the original papers.

## Licensing and access

- **ISO 9241-11 is paywalled.** The public catalog page shows only the abstract. Cite the definition by name and do not reproduce the standard's text.
- UXmatters, jnd.org, Practical Typography, Microsoft Inclusive Design, and deceptive.design are free to read and copyrighted by their authors or publishers. Practical Typography asks readers to pay if they find it useful.
- Paraphrase all of these, quote a phrase at most, and do not copy the Inclusive Design toolkit's illustrations.

## Known limitations and biases

- **Not fetched.** This is the main limitation. Until each page is fetched and a finding recorded, principles should treat these citations as provisional. Patterns, rubric anchors, and gates must not depend on them.
- **Age.** Hoober (2013) and the response-time papers (1968, 1991) are old, and device form factors have changed since.
- **Advocacy.** Deceptive Design and Microsoft Inclusive Design advocate for particular practices. Microsoft's toolkit also reflects that company's product framing.
- **Typography is domain-specific.** Butterick's measure guidance concerns prose. It does not set limits for data-dense layouts (see the DX disagreements on prose width versus data width).

## Cited pages

_No page from this publisher is cited by a numbered finding._

### Cited in principles only (unverified; not in any findings fetch log)

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| ISO 9241-11:2018, Ergonomics of human-system interaction — Usability: Definitions and concepts | <https://www.iso.org/standard/63500.html> | not recorded | not recorded | E1 (definitional; paywalled) | none (principle only: P-01) |
| Norman, D. "Signifiers, not affordances." | <https://jnd.org/signifiers_not_affordances/> | not recorded | not recorded | E4 | none (principle only: P-02) |
| Hoober, S. "How Do Users Really Hold Mobile Devices?" UXmatters, 2013 | <https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php> | not recorded | not recorded | E2 (observational; sampling limits) | none (principle only: P-06) |
| Butterick, M. *Practical Typography*, "Line length." | <https://practicaltypography.com/line-length.html> | not recorded | not recorded | E4 | none (principle only: P-08) |
| Microsoft, Inclusive Design toolkit | <https://inclusive.microsoft.design/> | not recorded | not recorded | E4 | none (principle only: P-12) |
| Brignull, H. Deceptive Design (formerly Dark Patterns) catalog | <https://www.deceptive.design/> | not recorded | not recorded | E4 | none (principle only: P-14) |
