---
id: PAT-DT-010
title: Narrow desktop windows, side-by-side use, multiple tabs, and iPad multitasking
type: pattern
scope: desktop
topics: [window-resize, narrow-window, split-view, side-by-side, multitasking, stage-manager, multiple-tabs, deep-links, state-preservation, zoom]
platforms: [desktop, tablet]
viewports: [compact, medium, expanded, large, extra-large]
inputs: [pointer, keyboard, touch, assistive-tech]
principles: [P-04, P-09, P-11, P-12, P-13]
dimensions: [D-10, D-02, D-08]
gates: [QG-009, QG-010, QG-013, QG-050, QG-051, QG-060, QG-061, QG-062]
related: [PAT-DT-001, PAT-DT-002, PAT-DT-011, PAT-RS-001, PAT-RS-002, PAT-RS-006, PAT-RS-007, PAT-RS-009, PAT-RS-011, PAT-PW-003, PAT-PW-004]
evidence_strength: moderate
status: active
updated: 2026-11-08
---

# Narrow desktop windows, side-by-side use, multiple tabs, and iPad multitasking

## Problem

"Desktop" describes a device and an input setup, not a window width. People snap a browser to half of a laptop screen next to a document or video call. They zoom to 200%, which halves the CSS viewport. They run a PWA in a small floating window, or use Split View, Slide Over, or Stage Manager on iPad. And they open five records in five tabs to compare them. Apps designed only for "phone" and "full-screen desktop" fail all of these. A half-width laptop window gets a cramped wide layout, or a stretched phone layout with a hamburger menu and bottom bar. Resizing mid-task resets the selection or wipes a draft. Records open in a transient panel with no URL, so they can't be opened in a tab.

## Recommendation

**Outcome:** the app works at whatever size and shape the window actually is. Resizing never loses work. People can spread their work across tabs and windows.

1. **Lay out from available space, not device type.** Use window-size breakpoints, and container queries for components (PAT-RS-006, PAT-RS-007). A 700 px-wide window on a 27-inch monitor gets the medium layout. Do not infer touch from narrowness, or pointer from width (PAT-RS-009).
2. **Design the medium and expanded layouts on purpose.** They are not a stretched phone or a squeezed desktop. Typical moves: the sidebar collapses to a labeled rail; list–detail goes from two panes to one, with selection preserved (PAT-RS-002); supporting panes move below or into a toggleable panel. Consider height too. Short, wide windows can make two panes and sticky headers impractical.
3. **Keep the input model regardless of width.** A narrow desktop window still has hover, right-click, and shortcuts. Don't swap in touch-only patterns (swipe-only actions, bottom sheets with no keyboard support) because the viewport got small.
4. **Preserve state across resize.** Keep the selected record, scroll position, unsaved input, open panels, filters, and focus when a breakpoint is crossed. Do not unmount and remount a form in a way that drops its values. Do not reset routes.
5. **Treat zoom as resizing.** At 200% browser zoom on a 1280 px screen, the layout behaves like a 640 px window and must reflow without loss (QG-009, QG-010, QG-050).
6. **Support multiple tabs and windows.** Every record and meaningful view has its own URL using `<a href>` (QG-061), so middle-click, Cmd/Ctrl-click, and "Open in new tab" work. Give each tab a distinct `document.title` naming the object ("INV-1042 · Acme — Billing"). Let tabs work independently. Sync shared data across tabs where needed (for example via `BroadcastChannel` or storage events), and warn rather than silently overwrite when two tabs edit the same record.
7. **Keep browser history meaningful.** Back returns to the previous meaningful state, and opening a detail pane should be reflected in the URL when it is a real destination (QG-060, PAT-PW-003). Reload restores the view (PAT-PW-004).
8. **Test the in-between sizes.** Check about 500, 700, 900, and 1100 px widths and short heights, as well as iPad Split View fractions and Stage Manager windows where you support them. Verify current OS behavior rather than assuming it.

## Evidence

- **E3** Apple Human Interface Guidelines, "Layout". https://developer.apple.com/design/human-interface-guidelines/layout.md. Base layout on available size classes, not device type or orientation, and keep functionality as size changes (F-DX-37).
- **E3** Apple Support, "Use multitasking on your iPad". https://support.apple.com/en-us/102576. Split View, Slide Over, and Stage Manager on some models (F-DX-38).
- **E3** Apple Human Interface Guidelines, "Multitasking" and "Designing for iPadOS". https://developer.apple.com/design/human-interface-guidelines/multitasking.md, https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados.md. iPad users combine inputs, and apps adapt to multitasking and resizable windows (F-SP-63).
- **E3** Google, Android Developers, "App orientation, aspect ratio, and resizability". https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability. Preserve state, including form input, across window-size changes (F-DX-39).
- **E3** Google, Android Developers, "Use window size classes". https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes. Medium (600–839 dp) and expanded (840–1199 dp) classes are based on window space, and height can rule out two panes (F-DX-46).
- **E2** Nielsen Norman Group, "Page Parking: Multi-Tab Mania". https://www.nngroup.com/articles/multi-tab-page-parking/. Users open several candidates in tabs as memory aids, plus parallel browsing (F-DX-40). The observations come from historical young-adult studies.
- **E3** MDN, "<a>: The Anchor element". https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a. Fake links break new-tab, copy, and bookmarking (F-DX-41).
- **E1** W3C, Media Queries Level 4. https://www.w3.org/TR/mediaqueries-4/. Width and pointer/hover capability are independent (F-DX-47). The spec is a Candidate Recommendation Draft.
- **E1** W3C, WCAG 2.2 SC 1.4.10 Reflow. https://www.w3.org/TR/WCAG22/#reflow. Reflow at a 320 CSS px equivalent (F-SP-04).

Cross-tab sync APIs are implementation suggestions and are not sourced here. The test widths are ours.

## Alternatives and tradeoffs

- **In-app tabs or a working set vs. browser tabs.** In-app tabs keep context in one window but duplicate browser features. Provide them only alongside real URLs (PAT-DT-011).
- **Single-window PWA vs. multiple windows.** Installed PWAs may open links in the same window. Decide deliberately whether "open in new window" is supported.
- **Same pane count with smaller panes vs. fewer panes.** In the medium class, Material recommends one pane for dense content or deep focus, and allows two for fast browsing (F-SP-67).

## Exceptions and failure modes

- Single-purpose tools (kiosk, presentation mode) may lock to one layout, but not one orientation (QG-013).
- Dropping primary navigation or actions at intermediate widths (QG-051).
- `resize` handlers that re-fetch data or reset routes.
- Modals that open in new tabs as blank pages.
- Showing touch-sized bottom navigation in a narrow window on a pointer device.

## Evaluation questions

- At about 700 px width on a desktop browser, is the layout intentional, with all primary destinations and actions available? [screenshot] [running app]
- Does resizing through every breakpoint mid-edit keep the draft, selection, scroll, and focus? [running app]
- At 200% zoom on 1280 px, does content reflow without loss or horizontal page scroll? [running app]
- Does a narrow pointer window still support hover, right-click, and shortcuts? [running app]
- Can records be opened in new tabs, and do tab titles identify them? [running app] [automated]
- With the same record open in two tabs, are conflicting edits detected? [running app]
- In iPad Split View at half and one-third widths, are tasks completable? [running app]
- Do people working beside another app complete tasks without excessive scrolling? [user study]

## Related

- Patterns: [PAT-DT-001](PAT-DT-001-wide-layout-density.md), [PAT-DT-002](PAT-DT-002-sidebar-hierarchical-navigation.md), [PAT-DT-011](PAT-DT-011-expert-workflows.md), PAT-RS-001, PAT-RS-002, PAT-RS-006, PAT-RS-007, PAT-RS-009, PAT-RS-011, PAT-PW-003, PAT-PW-004
- Principles: [P-04](../../principles/P-04-navigation-orientation.md), [P-09](../../principles/P-09-consistency-familiarity.md), [P-11](../../principles/P-11-error-prevention-recovery.md), [P-12](../../principles/P-12-accessibility-inclusion.md), [P-13](../../principles/P-13-performance-responsiveness.md)
- Rubric: [D-10, D-02, D-08](../../rubric/dimensions.md); gates [QG-009, QG-010, QG-013, QG-050, QG-051, QG-060, QG-061, QG-062](../../rubric/quality-gates.md)

## Change log

- 2026-11-08 — Initial version (ADR-001).
