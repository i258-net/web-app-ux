# Validation disposition

Independent validation was performed by GPT-6.1 Sol (high reasoning) in two passes on 2026-11-08, read-only, each producing one report. The orchestrator (Claude Fable 5.1) evaluated each finding and recorded the disposition here. "Fixed" means the change is in the same PR as this file; "accepted as limitation" means recorded in `governance/limitations.md`; "rejected" includes the reason.

## Coherence validation (`coherence-validation.md`)

| ID | Severity | Disposition | Where |
|---|---|---|---|
| F01 | material | Fixed: `touch-action: pan-y pinch-zoom`, ancestor note, verify zoom | PAT-MO-007 |
| F02 | material | Fixed: QG-062 now scopes to valuable, safe-to-store input; sensitive fields via warning + disclosure; trivial inputs exempt | quality-gates |
| F03 | material | Fixed: QG-093 splits universal failure communication from offline-view loading, which applies only to products claiming offline support; honest online-only refusal is not a failure | quality-gates |
| F04 | material | Fixed: QG-003 non-printable-key condition; QG-014 non-path single-pointer alternative + essential exception | quality-gates |
| F05 | material | Fixed: split into QG-020a (On Focus) and QG-020b (On Input); references updated | quality-gates, 7 files |
| F06 | material | Fixed: QG-029 lists 10× / 20 s warning with ≥10 extensions / off, and the three exceptions | quality-gates |
| F07 | material | Fixed: QG-001…030 rewritten as summaries that include each SC's exceptions and scope; table preamble requires reading the full SC before a fail; QG-015 lists all four branches; QG-021 and QG-025 scoped to the SC's covered kinds | quality-gates |
| F08 | material | Fixed: overall judgment adds `insufficient evidence` with scoped per-context result | scoring, review-template |
| F09 | material | Fixed: D-01, D-03, D-07, D-09, D-10 higher anchors re-expressed as outcomes (operable with each input; honest timely feedback; no removable step) rather than techniques | dimensions |
| F10 | material | Fixed: EX-01 expects a Major D-04 finding for paste-blocking at password creation and a QG-027 check on sign-in | scenarios |
| F11 | material | Fixed: INP no longer cited for continuous scroll/drag; device observation and traces required | PAT-MO-007, PAT-MO-010 |
| F12 | minor | Fixed: field/error visibility and submit reachability asked separately | PAT-MO-004 |
| F13 | material | Fixed: limitations now points to `research/validation/` with scope, model, findings, and this disposition | limitations |
| F14 | minor | Fixed: stale QG-090 conflict removed; manifest list marked illustrative with MDN checklist pointer | PAT-PW-002 |
| F15 | minor | Fixed: D-01, D-05, D-10 Level 5 rewritten with observable boundaries; distinctiveness reported in prose, not scored | dimensions |
| F16 | minor | Fixed: Consistent Help removed from D-08 Level 5 examples; AAA criteria listed instead | dimensions |
| F17 | minor | Fixed: APG normalized to E3 in PAT-RS-010 (orchestrator ruling recorded in PATTERN-PLAN) | PAT-RS-010 |
| F18 | minor | Fixed: QG-030 and QG-083 reclassified as `policy` (new gate kind) with the normative outcome tests kept separate | quality-gates |
| F19 | minor | Fixed: QG-050 excludes contained scroll regions and essential 2-D workspaces; 1920 added | quality-gates |
| F20 | minor | Fixed: QG-011 includes functionality, font-relative units, exceptions | quality-gates |
| F21 | minor | Fixed: new `policy` kind for E4-backed or approximate gates; QG-070 reclassified | quality-gates |
| F22 | minor | Fixed: keyboard attachment no longer expected to change pointer features | PAT-RS-011 |
| F23 | minor | Fixed: disclosure vs scrolling made task-dependent in P-05 and D-06 | P-05, dimensions |
| F24 | minor | Fixed: PAT-DT-004 metadata broadened to all platforms/viewports with a baseline note | PAT-DT-004 |
| F25 | minor | Fixed: real source paths and links | quality-gates, scoring, retrieval-guide |
| F26 | minor | Fixed: touch selection-mode guidance added to PAT-SH-006; referral reworded | PAT-SH-006 |
| F27 | minor | Fixed: QG-094 requires communication only when disruptive or action-requiring | quality-gates |
| F28 | minor | Fixed: skill uses the five canonical window classes | SKILL.md |
| F29 | minor | Fixed: source inspection verifies declared hints only | P-07 |
| F30 | note | Fixed: EX-09 cross-device handoff scenario added; tablet evidence gap remains in limitations | scenarios |

## Evidence validation (`evidence-validation.md`)

| ID | Severity | Disposition | Where |
|---|---|---|---|
| M01 | material | Fixed: denial-rate and Chromium-research claims removed; MDN gesture requirement and web.dev E4 advice cited separately | P-14 |
| M02 | material | Fixed: numeric ~300 ms generalization removed; Apple (no number) and Material (350–750 ms spatial) stated | P-15 |
| M03 | material | Fixed: claim narrowed to what the article-level Baymard citations in PAT-SH-001/PAT-MO-003 support; synthesis labeled | P-03 |
| M04 | material | Fixed (with coherence F21): QG-070 reclassified as `policy`, source linked | quality-gates |
| M05 | material | Fixed (with coherence F18): QG-030 reclassified as `policy`; normative outcome tests are QG-009/010 | quality-gates |
| M06 | material | Fixed (with coherence F07): QG-007/008 carry scope and exemptions | quality-gates |
| m07 | minor | Fixed: Tractinsky attribution and "replicated since" removed | P-15 |
| m08 | minor | Fixed: "most used" removed | P-04 |
| m09 | minor | Fixed: Nielsen's five components stated accurately; effectiveness attributed to ISO | P-01 |
| m10 | minor | Fixed: cites web.dev Serving | PAT-PW-006 |
| m11 | minor | Fixed: ranges attributed (Baymard 50–75 E2; Bringhurst via web.dev 45–75 E4; Butterick 45–90 E4); speed claim removed | P-08 |
| m12 | minor | Fixed: mobile hidden-vs-combo condition and participant count stated | P-02 |
| m13 | minor | Fixed: SC 2.4.13 added to Evidence | PAT-DT-004 |
| m14 | minor | Fixed: "minority" replaced with "subset"; no percentage | P-12 |
| m15 | minor | Fixed: page URLs added to QG-040, QG-070, QG-080…082 | quality-gates |
| m16 | minor | Fixed: `ch` definition cited to MDN | PAT-RS-008 |
| N17 | note | Fixed: QG-050 widths labeled a repository test matrix | quality-gates |
| N18 | note | Fixed: SRC-010 and SRC-005 rows reconciled with current citations | sources |
| N19 | note | Accepted as limitation: ISO 9241-11 definition cited from the public abstract only | limitations |
