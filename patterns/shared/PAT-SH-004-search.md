---
id: PAT-SH-004
title: Search — entry, suggestions, results, and no-results recovery
type: pattern
scope: shared
topics: [search, autocomplete, suggestions, search-scope, no-results, recent-searches]
platforms: [mobile, tablet, desktop]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [touch, pointer, keyboard, assistive-tech]
principles: [P-04, P-07, P-02, P-14]
dimensions: [D-02, D-04, D-07]
gates: [QG-001, QG-028, QG-061, QG-020]
related: [PAT-SH-005, PAT-SH-012, PAT-SH-001, PAT-MO-004, PAT-RS-010, PAT-PW-003]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Search — entry, suggestions, results, and no-results recovery

## Problem

Search is the fallback when navigation fails, and many users go to it first. It breaks down when:

- the entry point is hidden behind an icon on a wide screen;
- users cannot tell whether they are searching the current section or the whole app;
- suggestion lists are long, unreadable with the keyboard open, or unreachable by keyboard;
- results lose the query on Back;
- a no-results page is a dead end.

## Recommendation

**Outcome:** users can find search, know what it covers, get useful suggestions without being overwhelmed, return to their results, and recover from zero results.

1. **Entry.**
   - If search matters to the app's tasks, give it a primary, visible position: a visible field at expanded widths and wider, not just an icon.
   - On compact widths an icon that expands to a field is acceptable when space is constrained. Make the icon a labeled button.
   - Aim for one clear global search, plus local search where sections are genuinely distinct.
2. **Scope.**
   - State what is being searched (placeholder hint plus a visible scope label or control, e.g. "Search in: Projects").
   - When a suggestion changes scope ("shoes *in Women's*"), style it distinctly from a query completion.
3. **Suggestions.**
   - Keep the list short: Baymard recommends no more than 10 on desktop and 4–8 on mobile (e-commerce research).
   - Show recent queries when the field is focused and empty, with a way to clear history.
   - Implement the suggestion list as a combobox: Down Arrow enters the list, Escape closes it, Enter accepts, and standard text-editing keys keep working.
   - Selecting a suggestion must not cause an unexpected change of context (QG-020). Selecting a destination suggestion may navigate if the suggestion is clearly a link to that destination.
4. **Results.**
   - Echo the query in an editable field.
   - Show the result count and announce it to assistive technology (QG-028).
   - Highlight the matched terms.
   - Put the query, scope, and filters in the URL so results survive reload, Back, and sharing (QG-061; PAT-PW-003).
   - Refinement is covered in PAT-SH-005.
5. **No results.** Say plainly that nothing matched *this query in this scope*. Offer recovery:
   - check spelling, or show a "did you mean";
   - broaden the scope;
   - remove active filters, listing them;
   - browse entry points or contact help.

   Never show a blank list. See PAT-SH-012.
6. **Tolerate input** (case, whitespace, common variants). This is our inference from slip-prevention guidance, not a search-specific finding.
7. **Structured search.** When the domain needs criteria (dates, location, quantities), use a dedicated form rather than overloading one text box.

Search keyboards: PAT-MO-004. Full-screen vs docked presentation: PAT-RS-010.

## Evidence

- **E2** Baymard Institute, "9 UX Best Practice Design Patterns for Autocomplete Suggestions". https://baymard.com/research-articles/autocomplete-design — Long suggestion lists slowed or overwhelmed users. Recommends ≤10 suggestions on desktop and 4–8 on mobile, distinct styling for scope suggestions, keyboard navigation on desktop, and enough space on mobile. *E-commerce*; the counts are research recommendations, not limits.
- **E2** Nielsen Norman Group, "Mobile First Is NOT Mobile Only". https://www.nngroup.com/articles/mobile-first-not-mobile-only/ — Collapsed search carried over from mobile contributed to poor desktop navigation use.
- **E3** Apple, "Searching". https://developer.apple.com/design/human-interface-guidelines/searching.md — Important search occupies a primary position; one clear place to search; show scope; use recent and predictive suggestions; let people clear history. Apple platforms.
- **E3** Google Material Design, "Search". https://m3.material.io/components/search — Focused search can show history, then update suggestions while typing. Compact uses full-screen; medium and expanded use docked. Back dismisses and restores the bar. Material convention.
- **E3** W3C WAI, "APG combobox pattern". https://www.w3.org/WAI/ARIA/apg/patterns/combobox/ — Keyboard contract for suggestion popups and preservation of text editing. (Classed E3 per `sources/evidence-classes.md`; the findings file lists APG as E4.)
- **E1** W3C, "WCAG 2.2 — SC 3.2.2 On Input". https://www.w3.org/TR/WCAG22/#on-input — Changing a setting must not change context without advance notice.
- **E1** W3C, "WCAG 2.2 — SC 4.1.3 Status Messages". https://www.w3.org/TR/WCAG22/#status-messages — Result counts and "no results" messages must reach AT without receiving focus.
- **E4** Nielsen Norman Group, "Designing Empty States in Complex Applications". https://www.nngroup.com/articles/empty-state-interface-design/ — Explain emptiness and offer a next step; never show "No records" while still loading.
- **E3** MDN Web Docs, "<a>: The Anchor element". https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a — Real URLs support new-tab, bookmarking, and sharing.
- **E5** Mobbin, "Mobile Searching & Finding User Flow". https://mobbin.com/explore/mobile/flows/searching-finding — Shipped flows include query-plus-suggestions and structured criteria (location, dates). Convention observed, usability unverified.

## Alternatives and tradeoffs

- **Suggest-as-you-type vs search-on-submit.** Material allows either. Suggestions reduce typing but add noise and cost requests. On slow backends, debounce the input and keep the user's typed text authoritative.
- **Full-screen vs inline search on compact.** Full-screen gives suggestions room above the keyboard (Baymard, Material). Inline keeps page context. Choose by suggestion richness.
- **Global vs scoped default.** Defaulting to the current section is more precise but surprises users who expect global search. Make the scope visible and changeable whichever default you choose.
- **Showing search history.** It reduces effort but exposes past queries on shared devices. Offer a clear control (Apple E3); consider privacy for sensitive domains (P-14).

## Exceptions and failure modes

- Apps with very small content sets may not need search. A filterable list (PAT-SH-005) may serve better.
- Failure modes:
  - an icon-only search on a 1440 px header;
  - suggestions that cannot be reached by arrow keys or are announced as plain text;
  - pressing Enter on a highlighted suggestion submits the raw text instead;
  - results not kept in the URL, so Back loses them;
  - "0 results" with no recovery;
  - spinner and "no results" shown at the same time.

## Evaluation questions

1. Is search visible, with its scope stated, at expanded widths and wider? [screenshot]
2. Can suggestions be navigated and accepted by keyboard and screen reader? [running app]
3. Are suggestions few enough to read with the virtual keyboard open? [running app] [screenshot]
4. Do results survive reload, Back, and copy-link with the query and scope intact? [running app]
5. Is the result count announced? [running app] [automated]
6. Does a zero-result search offer at least one concrete recovery action? [running app] [screenshot]
7. Do users understand whether they searched globally or locally? [user study]

## Related

- Principles: P-04, P-07, P-02, P-14
- Dimensions: D-02, D-04, D-07
- Gates: QG-001, QG-028, QG-061, QG-020
- Patterns: PAT-SH-005 (refining results), PAT-SH-012 (no-results state), PAT-SH-001 (navigation), PAT-MO-004 (search keyboards), PAT-RS-010 (modality variants), PAT-PW-003 (URL state)

## Change log

- 2026-11-08 — Initial version (ADR-001).
