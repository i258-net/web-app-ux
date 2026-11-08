---
id: EX-08-REVIEW
title: "Sample review — EX-08 Responsive visual hierarchy of a pricing page (screenshots)"
type: example-review
scenario: EX-08
method: screenshot review (static captures at 360, 768, 1024, 1920 CSS px)
knowledge_source: local-checkout
model: claude-opus-5-5
status: active
updated: 2026-11-08
---

# UX review: Pricing page, responsive visual hierarchy (EX-08, synthetic scenario)

## 1. Scope and assumptions
- Product and primary users: the public pricing page of a web product, used by prospective customers deciding which plan to buy. The product is synthetic. The "Observed design" bullets in `examples/scenarios.md` EX-08 are treated as what the screenshots show.
- Primary tasks examined: T1 compare the plans (price and features); T2 identify the recommended plan; T3 choose a plan by activating its call-to-action (CTA).
- Device contexts in scope, assigned by **width class only** (input is unknown and was not inferred from width):
  - **Mobile / compact:** 360 px.
  - **Tablet / medium:** 768 px.
  - **Desktop / expanded and large:** 1024 px and 1920 px.
  - **Responsive transitions:** compared across the four discrete captures only; no resize was observed.
  - **PWA:** N/A, no evidence the page is part of an installable app.
- Input modalities examined: none directly. Touch, pointer, keyboard, and assistive technology were all not examined. The 768 px and 1024 px captures could be a tablet with touch or a narrow desktop window; this review does not assume either.
- Method(s): screenshots at 360, 768, 1024, and 1920 CSS px. No prototype, running app, source, automated tooling, or user research.
- Knowledge source: **local Git checkout** `~/.t3/projects/web-app-ux` at commit `06233c5`. OpenViking was treated as **unavailable** for this test; no staleness comparison was made.
- What this review cannot verify (from `evaluation/methods.md`):
  - behavior while resizing, rotating, or zooming. Only discrete widths were captured, and **none at 320 px**, so reflow (QG-010) cannot be checked;
  - whether horizontal scrolling belongs to the page or to a contained table region (QG-050), and whether that region is keyboard-focusable;
  - hover, focus, keyboard operability, and focus order (QG-001…006);
  - screen-reader behavior and table semantics (D-08);
  - contrast (QG-007, QG-008): this needs measurement; visual estimates are not reported;
  - text resize to 200 % and text-spacing overrides (QG-009, QG-011);
  - target size and spacing: estimate only, and no scale is given;
  - performance, layout shift, and loading states (QG-080…082);
  - task completion and comprehension (D-01, D-06): inference only;
  - what happens after a CTA is pressed.
- Assumptions:
  - A1. At 1920 px the ">140 characters per line" text is running prose (intro, plan descriptions, or FAQ) in a region separate from the narrow card column. The scenario reports both "lines exceed ~140 characters" and "cards sit in a narrow center column", which is only consistent if they are different regions.
  - A2. At widths other than 360 px, the recommended plan's CTA is visually distinguished. The scenario reports the CTAs as identical only at 360 px.
  - A3. At 360 px, "scrolls horizontally" is inferred from the table being clipped at the right edge with no cue. A static capture cannot show scrolling.
  - A4. No issues were described at 1024 px. This is treated as **no observation**, not as a pass.

## 2. Blocking conditions
**None found.** No finding prevents T1–T3, and no **standard** gate was verified as failing. The standard gates in scope (QG-007, QG-010) are *not verified*. No dimension is at Level 1.

The D-05 anchor for Level 1 ("primary actions visually indistinguishable at a supported viewport") was considered for the 360 px CTAs and rejected. Each plan's CTA is presumably still the visually primary action *within its card*. What is lost is the emphasis on the recommended plan, which matches Level 2 ("flat hierarchy"). If a running review finds the CTAs indistinguishable from other page content, re-score D-05 mobile to Level 1, and a §4 blocking condition then applies.

## 3. Results by device context

### Mobile (360 CSS px; input not examined)
| Dimension | Level (1–5 / N/A / insufficient evidence) | Confidence | Key evidence |
|---|---|---|---|
| D-01 Task effectiveness | 3 (provisional) | low | Inference: plans can be compared and chosen. The comparison needs undiscoverable sideways scrolling (F-05), and the recommendation is not signalled (F-03) |
| D-02 IA and navigation | insufficient evidence | — | Site navigation not described |
| D-03 Ergonomics and discoverability | 3 (provisional) | low | Horizontal table scroll with no cue is a swipe convenience with no visible fallback (anchor 3). Target sizes not given |
| D-04 Input efficiency | N/A | — | No data entry in the examined tasks |
| D-05 Visual hierarchy and craft | 2 | medium | Recommended plan's CTA visually identical to the others (F-03) |
| D-06 Content clarity | 3 (provisional) | low | Comparison columns clipped off-screen with no indication that more exist (F-05) |
| D-07 Feedback, errors, recovery | insufficient evidence | — | No states captured |
| D-08 Accessibility | insufficient evidence | — | Contrast not measured; reflow at 320 px not captured; table semantics not observable |
| D-09 Performance, resilience, trust | insufficient evidence | — | Not observable |
| D-10 Cross-device appropriateness | 3 (provisional) | low | The table is kept at compact width (a strength), but the adaptation is generic: clipped table, no column priority, and the recommendation emphasis is dropped |

Narrative: The worst-affected task is T1/T2 at 360 px. A user sees cards whose CTAs carry equal weight, so nothing guides them toward the recommended plan. Below that, the comparison table is cut off at the right edge with no cue that more plans or columns sit off-screen. Users may compare only the visible columns and take them as complete (the failure mode PAT-RS-003 and PAT-MO-008 describe). A strength: the comparison table is kept rather than removed at compact width.

### Tablet / medium (768 CSS px; input not examined)
| Dimension | Level (1–5 / N/A / insufficient evidence) | Confidence | Key evidence |
|---|---|---|---|
| D-01 Task effectiveness | insufficient evidence | — | Only the heading observation was given for this width |
| D-02 IA and navigation | insufficient evidence | — | — |
| D-03 Ergonomics and discoverability | insufficient evidence | — | — |
| D-04 Input efficiency | N/A | — | No data entry |
| D-05 Visual hierarchy and craft | 2 | medium | Headings render at body-text size (F-04): sections and plan names lose their hierarchy |
| D-06 Content clarity | insufficient evidence | — | Scanning is likely harder (F-04), but no layout description was given |
| D-07 Feedback, errors, recovery | insufficient evidence | — | — |
| D-08 Accessibility | insufficient evidence | — | Contrast and resize not measured |
| D-09 Performance, resilience, trust | insufficient evidence | — | — |
| D-10 Cross-device appropriateness | insufficient evidence | — | Single observation |

Narrative: Only one observation is available at 768 px: the type scale collapses so headings match body text. This flattens the page structure that T1 depends on (finding plan names and section boundaries while scanning). Nothing else can be scored at this width.

### Desktop (1024 and 1920 CSS px; input not examined)
| Dimension | Level (1–5 / N/A / insufficient evidence) | Confidence | Key evidence |
|---|---|---|---|
| D-01 Task effectiveness | 3 (provisional) | low | Inference: three cards side by side permit comparison at 1920. Reading the prose costs extra effort (F-01) |
| D-02 IA and navigation | insufficient evidence | — | — |
| D-03 Ergonomics and discoverability | insufficient evidence | — | Hover and pointer behavior not observable |
| D-04 Input efficiency | N/A | — | No data entry |
| D-05 Visual hierarchy and craft | 2 | medium | 1920: prose lines exceed ~140 characters (F-01), far above the KB's 50–75 character recommendation. Plan cards are confined to a narrow centre column with large empty margins (F-02). Anchor 2: "cramped or overlong lines". 1024: no observation |
| D-06 Content clarity | insufficient evidence | — | — |
| D-07 Feedback, errors, recovery | insufficient evidence | — | — |
| D-08 Accessibility | insufficient evidence | — | — |
| D-09 Performance, resilience, trust | insufficient evidence | — | — |
| D-10 Cross-device appropriateness | 3 (provisional) | low | The large width is used generically: prose is stretched while the comparison surface stays narrow, the inverse of PAT-DT-001 rec. 1–2 |

Narrative: The worst-affected task at 1920 px is reading plan details. Long prose lines slow reading. Meanwhile the cards, the actual comparison surface, sit in a narrow column, so the layout gives width to the wrong element. No problems were reported at 1024 px; that is an absence of observations, not a pass.

### Responsive transitions (comparison of discrete captures)
| Dimension | Level (1–5 / N/A / insufficient evidence) | Confidence | Key evidence |
|---|---|---|---|
| D-01 Task effectiveness | insufficient evidence | — | No mid-task resize observed |
| D-02 IA and navigation | insufficient evidence | — | — |
| D-03 Ergonomics and discoverability | insufficient evidence | — | — |
| D-04 Input efficiency | N/A | — | — |
| D-05 Visual hierarchy and craft | 2 | medium | Hierarchy is not preserved across breakpoints: the recommended emphasis is lost at 360 (F-03), headings collapse at 768 (F-04), and measure is unbounded at 1920 (F-01). D-05 transitions criterion: "the primary action stays primary" |
| D-06 Content clarity | insufficient evidence | — | — |
| D-07 Feedback, errors, recovery | insufficient evidence | — | — |
| D-08 Accessibility | insufficient evidence | — | Zoom and reflow not exercised |
| D-09 Performance, resilience, trust | insufficient evidence | — | Layout shift not observable |
| D-10 Cross-device appropriateness | 3 (provisional) | low | Each width is functional, but the typographic and emphasis system does not adapt deliberately |

Narrative: Across the four widths, the pricing page's hierarchy is inconsistent rather than deliberately adapted. Each breakpoint loses a different signal: emphasis at 360 px, heading scale at 768 px, measure at 1920 px. Behavior *between* the captured widths is untested.

### PWA
N/A: no evidence that the page belongs to an installable app.

## 4. Overall cross-device task effectiveness
**pass with major issues (provisional; screenshot evidence only)**. D-01 is provisionally Level 3 on mobile and desktop by inference. D-10 is provisionally Level 3 in every scored context. No blocking condition was found. Under `methods.md`, a claim of cross-device *quality* needs a running app or prototype in a compact touch and an expanded pointer context, plus the transition between them. This review has none of those, so it makes **no cross-device quality claim**; it reports visual and structural characteristics only.

## 5. Findings (ordered by severity, then dimension)

### F-01 Prose line length exceeds ~140 characters at 1920 px — Major
- Context: desktop (large, 1920 CSS px); Dimension: D-05 (also D-06); Gate: — (no gate covers measure; QG-009/QG-011 not verified)
- Label: **Likely concern** (visually observed; reading impact inferred).
- **Observed:** In the 1920 px screenshot, body text lines run beyond about 140 characters (scenario estimate; not counted by this reviewer).
- **Inferred:** The prose block has no maximum measure and fills its container. At roughly twice the upper end of the knowledge base's recommended range, plan descriptions and FAQ text will be skimmed or skipped, and finding the start of the next line gets harder. Assumption A1 applies.
- Confidence: medium.
- Supporting guidance:
  - PAT-DT-001 *Wide layouts* rec. 1 "Constrain prose, not the page … about 50–75 characters per line". Key source: Baymard "Readability: The Optimal Line Length", **E2**, e-commerce testing; "applying this to non-commerce reading is our interpretation".
  - PAT-RS-008 *Responsive typography and spacing* rec. 4, `max-inline-size: 65ch` as a starting point. Same Baymard source, E2.
  - P-08 *Visual hierarchy and readability*, which gives "roughly 45–75 characters" with E4 plus partial E2 support.
- **Recommendation:** Cap running text blocks with a font-relative maximum (e.g. `max-inline-size: 65ch` as a starting point), then count the rendered characters with the real font, since `ch` is not an exact character count. Apply the cap to text blocks only, not to the page shell or the comparison surfaces (see F-02).
- Alternatives / tradeoffs: The knowledge base sets no universal maximum page width; the 50–75 range applies to prose only, and to English-language text (PAT-DT-001, failure modes).

### F-02 Plan cards confined to a narrow centre column with large empty margins at 1920 px — Minor
- Context: desktop (large, 1920 CSS px); Dimension: D-05 (also D-10); Gate: —
- Label: **Likely concern**.
- **Observed:** In the 1920 px screenshot, the three plan cards sit in a narrow column at the centre of the page, with large empty margins on both sides.
- **Inferred:** The comparison surface appears to inherit a page-shell or prose-width cap. This matches the failure PAT-DT-001 describes ("Applying the prose `max-width` to the app shell, which cramps tables and leaves wide gutters"). Combined with F-01, the page constrains the wrong element and leaves the right one unconstrained. Cramped cards may truncate or wrap feature lists; that cannot be confirmed without a closer capture.
- Confidence: medium on the observation; low on impact.
- Supporting guidance: PAT-DT-001 rec. 2 "Give comparison surfaces the width they need" and rec. 4 (whitespace to show grouping). Key sources: IBM Carbon data-table guidelines, **E3**; Apple HIG Layout, **E3**. PAT-RS-003 rec. 4 "On wide windows, reveal rather than stretch" (NN/g "Mobile First Is NOT Mobile Only", **E2**).
- **Recommendation:** Let the card group and the comparison table use a wider container than the prose (for example, give the cards enough width that feature lists do not wrap awkwardly), while keeping the prose cap from F-01. Consider using the 1920 px width to show the comparison table beside or directly under the cards, without a scroll gap.
- Alternatives / tradeoffs: PAT-DT-001 explicitly allows "Single centered column … Empty margins are acceptable when nothing related needs to sit alongside". Centred cards are therefore not wrong in themselves. That is why this is Minor rather than Major: the concern is narrowness that cramps the cards, not the margins.

### F-03 Recommended plan's CTA visually identical to the others at 360 px — Major
- Context: mobile (compact, 360 CSS px), and responsive transitions; Dimension: D-05 (also D-06, D-10); Gate: —
- Label: **Likely concern**.
- **Observed:** In the 360 px screenshot, the recommended plan's CTA has the same visual treatment as the other plans' CTAs.
- **Inferred:** Under assumption A2, the emphasis present at wider widths is dropped at compact width, so the one place where users scan cards one at a time loses its main decision cue. Users who rely on the recommendation must read and compare every card in full. Whether a non-CTA cue such as a "Recommended" badge remains is not stated.
- Confidence: medium.
- Supporting guidance:
  - P-08 "one primary action per screen is visually dominant", with NN/g eye-tracking on scanning, **E2**.
  - `dimensions.md` D-05 compact criterion "one clear primary action per screen" and transitions criterion "the primary action stays primary".
  - PAT-RS-003 *Content prioritization*, rec. 1–2: rank content by task; primary content first. Key sources are NN/g/Baymard mobile research, **E2**.
  - Evidence gap: no pattern in the knowledge base specifically addresses emphasising a recommended option among equivalent CTAs. The guidance here is principle-level.
- **Recommendation:** Keep the recommended plan's distinguishing treatment at every width: a filled vs outlined CTA, a visible text badge (not color alone), and, at compact width, place the recommended plan first or open by default if that matches the business intent. Verify its contrast with measurement (QG-007, QG-008).
- Alternatives / tradeoffs: Featuring one plan is a business choice. If there is deliberately no recommended plan, identical CTAs are correct, and then the recommendation should be absent at every width, not only at 360 px.

### F-04 Headings scale down to body-text size at 768 px — Major
- Context: tablet/medium (768 CSS px), and responsive transitions; Dimension: D-05 (also D-06); Gate: —
- Label: **Likely concern**.
- **Observed:** In the 768 px screenshot, headings render at the same size as body text.
- **Inferred:** The fluid or stepped type scale probably has a minimum that reaches body size at medium widths, for example a `clamp()` whose minimum equals the body size or a breakpoint step set too low. Section and plan-name boundaries lose their visual weight, so users scanning to compare plans have no structure to scan by. Weight or color may still differ; the scenario mentions only size.
- Confidence: medium.
- Supporting guidance:
  - PAT-RS-008 *Responsive typography and spacing* rec. 2–3: bounded fluid type applied mainly to headings, with a sensible minimum. Key source: web.dev "Typography", labelled **E4** in this pattern; P-08 labels the same page E3 (see Test notes).
  - P-08 "consistent type scale".
  - D-05 transitions criterion "hierarchy preserved across breakpoints".
- **Recommendation:** Give each heading level a `clamp()` minimum above the body size (e.g. a heading expression with a `rem` term whose minimum stays distinctly larger than body text), or use a stepped scale per window class tested at both edges of each class. Check 600, 768, and 839 px specifically, the medium class boundaries in the skill.
- Alternatives / tradeoffs: PAT-RS-008 documents stepped vs fluid scales. A stepped scale is predictable, and its abrupt jumps are acceptable if each step is tested at both edges. Fluid scaling is smooth but needs zoom testing (QG-009).

### F-05 Comparison table at 360 px is clipped with no overflow indication — Minor
- Context: mobile (compact, 360 CSS px); Dimension: D-03 (also D-06, D-08); Gate: QG-050, QG-010 (not verified)
- Label: **Likely concern**; scroll behavior **untested**.
- **Observed:** In the 360 px screenshot, the plan comparison table extends past the right edge of the viewport. No visual cue shows that more content lies to the side: no partial column, fade, arrow, or "scroll for more" text. (Assumption A3: "scrolls horizontally" is inferred.)
- **Inferred:** Users may compare only the visible plans or columns and take them as complete. Whether only the table scrolls (acceptable under the KB's reading of the WCAG 1.4.10 two-dimensional exception) or the whole page scrolls sideways (a QG-050 failure) cannot be told from the capture. Keyboard reach of the scroll region is also unknown.
- Confidence: medium on the missing cue; low on scroll mechanics.
- Supporting guidance:
  - PAT-DT-007 *Data tables* responsive strategy A: horizontal scroll in a contained region with an overflow cue, a frozen identifier column, `role="region"`, an accessible name, and `tabindex="0"`. Key sources: Adrian Roselli "A Responsive Accessible Table", **E4**; WCAG 2.2 SC 1.4.10, **E1**, for the 2-D exception; the strategy table is "our synthesis".
  - PAT-MO-008 rec. 9: show a partial next item so scrollability is visible. E4-level, by the pattern's own evidence-gap note.
  - PAT-RS-003 rec. 3: say when columns are hidden (NN/g data tables, **E4**; Baymard truncation, **E2**, users took partial lists as complete).
- **Recommendation:** Keep the table, which preserves comparison (a strength), and make the overflow visible:
  1. Let the next column peek in partially.
  2. Freeze the feature-name column.
  3. Wrap the table in a named, focusable scroll region so only the table scrolls.
  4. Verify at 320 and 375 px that the page itself does not scroll sideways (QG-010, QG-050).
- Alternatives / tradeoffs: PAT-DT-007 documents the alternatives:
  - **B, column priority:** e.g. a plan selector showing two plans at a time. Hidden plans must stay reachable.
  - **C, stacked cards:** ends cross-plan comparison, which is the primary task, so it is weaker here.

  NN/g and Roselli both say to choose by task.

## 6. Quality gates checked
| Gate | Result (pass / fail / not verified) | Method | Note |
|---|---|---|---|
| QG-007 Text contrast ≥ 4.5:1 (3:1 large) | not verified | screenshot | Needs measurement. Not estimated from images |
| QG-008 Non-text contrast ≥ 3:1 | not verified | screenshot | Relevant to any outlined vs filled CTA treatment (F-03) |
| QG-010 Reflow at 320 CSS px | not verified | screenshot | No 320 px capture. The table may qualify for the 2-D exception (PAT-DT-007 interpretation); the surrounding page must still reflow |
| QG-050 No horizontal page scroll at 320/375/768/1024/1440 | not verified | screenshot | Captured widths (360/768/1024/1920) only partly overlap the gate's widths. At 360, whether page or table scrolls is unknown (F-05) |
| QG-009 Text resizable to 200 % | not verified | — | Needs running app |
| QG-011 Text-spacing overrides | not verified | — | Needs running app |
| QG-030 Pinch-zoom not disabled | not verified | — | Needs source/automated check of viewport meta |
| QG-051 Primary action present and operable at every viewport | not verified | screenshot | CTAs are *visually present* at all four captured widths. Operability needs interaction |
| QG-019 / QG-040 Target size | not verified | screenshot | No scale or dimensions available |
| QG-001 / QG-004 / QG-005 Keyboard, focus order, focus visible | not verified | — | Includes keyboard access to the table scroll region |

## 7. Strengths worth keeping
- Mobile (360 px): the comparison table is kept rather than removed at compact width, which preserves feature parity. PAT-RS-003 says "defer rather than delete", and PAT-DT-007 strategy A keeps cross-row comparison.
- Desktop (1920 px): all three plan cards are visible side by side, which supports direct comparison (T1).
- All captured widths: every plan has a visible CTA (visual presence only; QG-051 not verified).

## 8. Confidence and limitations
- Overall confidence: **medium** for the four visual observations; **low** for every scroll, interaction, and accessibility consequence.
- Not tested: resize behavior between the captured widths, 320 px reflow, zoom and text-spacing, contrast, keyboard and screen-reader access to the table, hover and focus states on CTAs, and what happens on CTA activation. The 1024 px capture yielded no reported observations; it was not examined for issues independently of the scenario text.
- What would change the assessment:
  - Measured contrast failures on CTA labels or prices would add a standard-gate failure on the critical path, which is a blocking condition.
  - Page-level horizontal scroll at 320/375 px would turn F-05 into a QG-050 / QG-010 failure.
  - If the 360 px CTAs prove indistinguishable from surrounding content, D-05 mobile moves to Level 1 (blocking).
- Recommended next verification steps:
  1. Load the page in a browser and resize continuously from 320 to 1920 px, watching heading sizes, the card container, and the table.
  2. Run an automated contrast check, then manually check CTA states.
  3. At 1280 px, zoom to 400 % (about 320 CSS px) and confirm reflow.
  4. Keyboard-tab through the cards and table, and scroll the table with the arrow keys.
  5. Run a screen-reader pass on the table.
  6. If plan choice drives revenue, run a short comparison task with real users on a phone; real-user evidence outranks this review.

## 9. Sources applied
- PAT-DT-001 Wide layouts. https://baymard.com/research-articles/line-length-readability (E2); https://www.nngroup.com/articles/mobile-first-not-mobile-only/ (E2); https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines (E3); https://developer.apple.com/design/human-interface-guidelines/layout.md (E3)
- PAT-RS-008 Responsive typography and spacing. https://baymard.com/research-articles/line-length-readability (E2); https://web.dev/learn/design/typography (E4 as labelled in this pattern); https://www.w3.org/TR/WCAG22/#resize-text (E1)
- PAT-RS-003 Content prioritization. https://www.nngroup.com/articles/mobile-ux/ (E2); https://baymard.com/research-articles/truncation-design (E2); https://www.nngroup.com/articles/data-tables/ (E4); https://www.w3.org/TR/WCAG22/#reflow (E1)
- PAT-DT-007 Data tables and grids. https://adrianroselli.com/2017/11/a-responsive-accessible-table.html (E4); https://www.nngroup.com/articles/data-tables/ (E4); https://www.w3.org/TR/WCAG22/#reflow (E1)
- PAT-MO-008 Compact density, truncation, carousels. https://www.w3.org/TR/WCAG22/#reflow (E1); https://baymard.com/research-articles/truncation-design (E2)
- P-08 Visual hierarchy and readability. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ (E2); https://www.w3.org/TR/WCAG22/#contrast-minimum (E1)
- Rubric: `rubric/dimensions.md` D-01…D-10; `rubric/scoring.md` §1–§5; `rubric/quality-gates.md`; `evaluation/methods.md`; `sources/evidence-classes.md` (SRC-000).

## Test notes

**Files retrieved: 18 distinct files for this review (12 shared with EX-01, 6 EX-08-specific).** The shared set was retrieved once (see the EX-01 review's test notes for its full log):
- skill files: `SKILL.md`, `references/retrieval.md`, `references/scenarios.md`;
- KB reference: `examples/scenarios.md`, `evaluation/review-template.md`, `evaluation/methods.md`, `examples/README.md`, `INDEX.md`, `sources/evidence-classes.md`;
- rubric: `rubric/scoring.md`, `rubric/quality-gates.md`, `rubric/dimensions.md` (all ten sections; D-05 and D-10 were the ones this review needed most).

EX-08-specific:

| # | File | Why |
|---|---|---|
| 1 | `patterns/responsive/PAT-RS-008-responsive-typography-spacing.md` | Headings collapsing at 768; measure |
| 2 | `patterns/desktop/PAT-DT-001-wide-layout-density.md` | 1920 px line length; narrow centre column |
| 3 | `patterns/responsive/PAT-RS-003-content-prioritization.md` | Recommended-plan emphasis and hidden columns at 360 |
| 4 | `patterns/desktop/PAT-DT-007-data-tables-grids.md` | Responsive comparison table strategies; QG-050 / QG-010 exception |
| 5 | `patterns/mobile/PAT-MO-008-compact-density-truncation.md` | Horizontal-scroll cue. Read from the title line onward; front matter skipped, Related section read |
| 6 | `principles/P-08-visual-hierarchy-readability.md` | Principle for D-05 |

**Expected retrieval IDs (`examples/scenarios.md` EX-08):** PAT-RS-008 ✓, PAT-DT-001 ✓, PAT-RS-003 ✓, PAT-DT-007 ✓, PAT-MO-008 ✓; P-08 ✓; D-05 ✓, D-10 ✓; QG-010 ✓, QG-050 ✓, QG-007 ✓. **Not opened: PAT-RS-004 (adaptive density) and P-15 (craft and delight).** I left them out deliberately to stay near the skill's ~10-document budget, judging that the observations were about measure, type scale, and emphasis rather than spacing tokens or delight. That is a retrieval miss against the expected list. As in EX-01, retrieval was not blind: the expected list was read first. A post-hoc `index.json` topic check shows:
- `line-length`, `measure`, and `typography` return PAT-DT-001, PAT-RS-008, and P-08;
- `horizontal-scroll` and `responsive-table` return PAT-DT-007;
- **`visual-hierarchy`, `pricing`, and `comparison` return nothing**, and `hierarchy` returns only PAT-DT-002, P-03, and P-08.

So a blind topic query would not surface PAT-RS-003 or PAT-MO-008 for this scenario. Only title browsing in INDEX.md or `related:` links get there.

**Drift between skill and knowledge base:** the skill's `references/scenarios.md` row lists PAT-RS-008, PAT-DT-001, PAT-RS-003, PAT-DT-007; QG-010, QG-050. It omits PAT-RS-004, PAT-MO-008, QG-007, and the principles and dimensions in the KB's list.

**Missing, ambiguous, or contradictory guidance:**
1. **No pattern for emphasising a recommended option** among equivalent CTAs (pricing tiers, plan choosers). F-03 rests on P-08 and D-05 principle-level wording only. Pricing and comparison pages are common enough to warrant a pattern, or at least `pricing` / `comparison` topics.
2. **D-05 Level 1 anchor is too literal for this case.** "Primary actions visually indistinguishable at a supported viewport" would make the 360 px CTA observation a Level 1, and therefore a §4 blocking condition, while the scenario expects Major. I scored Level 2 and explained why. The anchor needs to say "indistinguishable from non-primary content", not "from each other".
3. **Evidence-class inconsistency.** web.dev "Learn Design: Typography" is labelled **E4** in PAT-RS-008 and **E3** in P-08. Separately, SRC-000 lists "web.dev and MDN platform documentation" under E3 and "web.dev tutorials" under E4, so the same page can be classed either way.
4. **Line-length range inconsistency.** PAT-DT-001 and PAT-RS-008 say 50–75 characters (Baymard E2). P-08 says "roughly 45–75" (E4 with partial E2). This is minor, but a reviewer quoting "the KB's number" has two to choose from.
5. **The scenario's observations are internally tense.** "Lines exceed ~140 characters" and "cards in a narrow centre column with large empty margins" at the same width only make sense for different regions (assumption A1).
6. **Capture widths vs gate widths.** QG-050 tests 320/375/768/1024/1440 and QG-010 tests 320, while the scenario captures 360/768/1024/1920. A screenshot reviewer can never close these gates with this material. The skill's viewport classes (compact < 600, …) do not tell the reviewer which widths to request.
7. **"Scrolls horizontally" is behavior.** A static capture can only show clipping (assumption A3).
8. **The rubric's device contexts bundle width with input** ("Mobile = compact with touch as the primary input"), but the skill forbids inferring input from width. For a screenshot-only responsive review there is no input evidence, so the context labels are by width class only. The KB does not say how to label contexts in that case.
9. **No observation was given for 1024 px.** The template forces a context table, so most of the 1024 cells are effectively silent. I merged 1024 into "Desktop" and said so.

**SKILL.md: unclear or tempting to over-claim:**
- The scenario's expected outcome ("Major on line length and flattened hierarchy; Minor on undiscoverable horizontal scroll; contrast 'not verified'") closely matches what I produced. Agreeing with an answer key I had already read is weak evidence that the skill works.
- "Screenshots verify most of [D-05]" (`dimensions.md`) tempts confident D-05 scores. I kept D-05 at medium confidence because the observations are second-hand scenario text, not my own measurements: no character counts and no type-size values.
- The ~10-document budget conflicts with the expected-retrieval lists, which name 6 patterns + 2 principles + rubric + gates per scenario, before the mandatory template, methods, and scoring files. Following the budget literally produced the RS-004 / P-15 miss.
- Step 8 lists viewport classes but says nothing for screenshot-only reviews beyond "record these as untested". Fine, but the template's "Responsive transitions" table then becomes a near-empty grid of "insufficient evidence".

**Retrieval effort:** 6 EX-08-specific file reads, plus the 12 shared files (about 14 shared read operations, since `dimensions.md` took 3 calls). About 20 read operations attributable to this review; 30 for both reviews combined, plus one post-hoc `index.json` query.
