---
id: EX-RETRIEVAL
title: Retrieval tests
type: reference
status: active
updated: 2026-11-08
---

# Retrieval tests

Run after each OpenViking refresh and whenever patterns are added or renamed. A test passes if at least one of the expected documents (or its parent directory sidecar) appears in the top 8 results. Record outcomes in the table at the bottom.

| # | Query (plain-language problem) | Expected documents (any) |
|---|---|---|
| R1 | virtual keyboard covers the submit button on a phone form | PAT-MO-004, PAT-MO-005, PAT-MO-009 |
| R2 | should I show errors while the user types or after they leave the field | PAT-SH-003 |
| R3 | hamburger menu versus bottom tab bar on mobile | PAT-MO-003, PAT-RS-001 |
| R4 | desktop table: sort, select many rows, run a bulk action | PAT-DT-007, PAT-SH-006 |
| R5 | actions only appear on hover and touch users cannot find them | PAT-DT-003, PAT-RS-009 |
| R6 | reorder a list by dragging with a keyboard alternative | PAT-DT-009, PAT-MO-007 |
| R7 | browser back button exits the installed PWA instead of closing the modal | PAT-PW-003, PAT-PW-001 |
| R8 | what to show when a search returns nothing | PAT-SH-012, PAT-SH-004 |
| R9 | confirm dialog or undo for deleting an item | PAT-SH-011 |
| R10 | lines of text are too long on a wide monitor | PAT-DT-001, PAT-RS-008 |
| R11 | detect touch versus mouse instead of using screen width | PAT-RS-009 |
| R12 | show that the app is offline and let the user retry | PAT-PW-005, PAT-SH-016 |
| R13 | when to ask for notification permission | PAT-PW-009 |
| R14 | minimum touch target size for accessibility versus comfortable size | PAT-MO-001, QG-019/QG-040 rows in rubric/quality-gates.md |
| R15 | how do I score a mobile app separately from desktop | rubric/scoring.md |
| R16 | what can a screenshot review verify | evaluation/methods.md |

## Results log

| Date | Source (OpenViking / local) | Passed | Failed (IDs) | Notes |
|---|---|---|---|---|
| 2026-11-08 | OpenViking (temporary local-folder snapshot, since removed) | 1/16 | R1–R15 | Run before semantic processing of `patterns/` had completed (directory abstracts "not ready"); INDEX.md chunks dominated results. Not a valid measure of ranking; rerun against the Git-watched resource `viking://resources/repos/i258-net/web-app-ux` after its first completed run. |
