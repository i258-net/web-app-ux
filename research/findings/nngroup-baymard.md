# NN/g and Baymard: empirical and heuristic UX findings

Working research material for assignment **NB**, accessed **2026-11-08**. This file contains **70 findings**: 42 from Nielsen Norman Group and 28 from Baymard Institute.

**Scope and evidence:** mobile-first responsive web applications and PWAs, with desktop needs retained. NN/g heuristics and design syntheses are classified E4 unless the particular claim reports empirical observations or an experiment. E2 does not imply a randomized experiment: source descriptions identify observational, benchmark, or experimental evidence where available. No finding here is a formal E1 accessibility or performance requirement.

**Baymard scope:** its research is primarily e-commerce. Each Baymard entry explicitly distinguishes e-commerce-specific conclusions from mechanisms likely to generalize. Benchmark percentages describe sampled sites and implementations, not the proportion of all users who experience a problem, and do not establish a causal conversion improvement. Only public page text was used; linked Premium guidelines, paid reports, video contents, and underlying raw datasets were not inspected.

### F-NB-01: Show the outcome and current state of user actions

- **Source:** Visibility of System Status (Usability Heuristic #1) — https://www.nngroup.com/articles/visibility-system-status/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2018-06-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends timely feedback so users can tell whether an interaction registered, what the system is doing, and what to do next. Silent changes to user-owned content undermine predictability and trust.
- **Interpretation:** Give saves, submissions, selections, and background changes a visible state; distinguish acknowledgement from successful completion.
- **Applies to:** all; touch / pointer / keyboard / AT; general
- **Generalizability:** high — a broad interaction heuristic; particular feedback implementations still need testing.
- **Conflicts/tensions:** Balance with F-NB-08 and F-NB-40: feedback should be relevant and proportionate.
- **Candidate knowledge targets:** system status; action feedback; trust

### F-NB-02: Use users’ vocabulary and natural task order

- **Source:** Match Between the System and the Real World (Usability Heuristic #2) — https://www.nngroup.com/articles/match-system-real-world/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2018-07-01
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** The system should use familiar words and concepts rather than internal terminology, and arrange information in an order consistent with users’ expectations. Familiarity depends on the intended audience.
- **Interpretation:** Research domain vocabulary and label destinations and actions by user goals; do not assume internal object names make sense externally.
- **Applies to:** all; touch / pointer / keyboard / AT; general
- **Generalizability:** high — broadly applicable, but the vocabulary and metaphors are audience-specific.
- **Conflicts/tensions:** Consistency (F-NB-04) does not justify unfamiliar terminology.
- **Candidate knowledge targets:** plain language; mental models; information architecture

### F-NB-03: Back, Cancel, Close, and Undo express different forms of control

- **Source:** User Control and Freedom (Usability Heuristic #3) — https://www.nngroup.com/articles/user-control-and-freedom/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2020-11-29
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends discoverable exits and undo. Browser Back should return users to the previous state; when a full-screen overlay looks like a new page, Back should close it rather than unexpectedly leaving the underlying page.
- **Interpretation:** Define navigation and mutation recovery separately; retain entered work and restore the state users expect when returning.
- **Applies to:** all; touch / pointer / keyboard / AT; general web navigation and editing
- **Generalizability:** high — transferable to responsive apps, with browser-history behavior requiring implementation-specific verification.
- **Conflicts/tensions:** F-NB-38: hierarchical breadcrumbs are not a replacement for history-based Back.
- **Candidate knowledge targets:** navigation history; cancellation; undo; overlays

### F-NB-04: Maintain internal consistency and respect external conventions

- **Source:** Maintain Consistency and Adhere to Standards (Usability Heuristic #4) — https://www.nngroup.com/articles/consistency-and-standards/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2021-01-10
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Consistent wording, interaction behavior, and layout reduce learning effort. NN/g distinguishes consistency inside a product from conventions learned across other products, platforms, and industries.
- **Interpretation:** Use a shared component vocabulary while adapting behavior to the platform and task; familiarity need not force identical layouts at every width.
- **Applies to:** all; touch / pointer / keyboard / AT; general
- **Generalizability:** high — a general heuristic with platform- and domain-dependent details.
- **Conflicts/tensions:** F-NB-14: identical mobile and desktop layouts can violate rather than improve practical consistency.
- **Candidate knowledge targets:** consistency; conventions; design systems

### F-NB-05: Prevent slips with constraints, defaults, and forgiving formatting

- **Source:** Preventing User Errors: Avoiding Unconscious Slips — https://www.nngroup.com/articles/slips/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2015-08-23
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g distinguishes unintended slips from mistaken goals. Helpful constraints, contextual suggestions, sensible defaults, and acceptance of familiar input formatting reduce opportunities for slips.
- **Interpretation:** Constrain genuinely impossible choices, normalize benign formatting differences, and show users what a default means before committing consequential changes.
- **Applies to:** all; touch / pointer / keyboard; general data entry
- **Generalizability:** high — broad prevention mechanisms; constraints must match actual domain rules.
- **Conflicts/tensions:** F-NB-42: defaults must not manipulate users into unwanted choices.
- **Candidate knowledge targets:** error prevention; defaults; input normalization

### F-NB-06: Keep relevant options and context available for recognition

- **Source:** Memory Recognition and Recall in User Interfaces — https://www.nngroup.com/articles/recognition-and-recall/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2024-01-15
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Recognition is easier than recalling information without cues. NN/g explains how visible context supports memory and recommends interfaces that reduce the need to remember commands or information from elsewhere.
- **Interpretation:** Keep labels, selected filters, recent context, and meaningful options available at the point of use.
- **Applies to:** all; touch / pointer / keyboard / AT; general
- **Generalizability:** high — broad cognitive principle, with the useful cues depending on the task.
- **Conflicts/tensions:** F-NB-17: disclosure should defer secondary detail without hiding essential context.
- **Candidate knowledge targets:** recognition over recall; working memory; persistent context

### F-NB-07: Provide accelerators alongside learnable interaction paths

- **Source:** Flexibility and Efficiency of Use (Usability Heuristic #7) — https://www.nngroup.com/articles/flexibility-efficiency-heuristic/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2020-11-22
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** The efficiency heuristic supports different methods for novice and expert users. Shortcuts and gestures can speed repeated actions, but an interface relying only on such methods is harder to learn; excessive duplication can also confuse.
- **Interpretation:** Keep an obvious standard path and add discoverable shortcuts for frequent work, without forcing first-time users to learn hidden commands.
- **Applies to:** all; touch / pointer / keyboard; general, especially repeated tasks
- **Generalizability:** high — the novice/expert distinction transfers across app types.
- **Conflicts/tensions:** F-NB-36 and F-NB-41: gestures and tutorials do not replace a usable baseline.
- **Candidate knowledge targets:** accelerators; expert efficiency; learnability

### F-NB-08: Minimize irrelevant information while retaining necessary controls

- **Source:** Aesthetic and Minimalist Design (Usability Heuristic #8) — https://www.nngroup.com/articles/aesthetic-minimalist-design/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2021-01-24
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g defines minimalist design as maximizing useful information and removing noise. It explicitly warns that too few elements can impair utility and that the heuristic is not an instruction to adopt a fashionable sparse or flat style.
- **Interpretation:** Evaluate each element against task value; do not remove labels, navigation, or feedback merely to reduce visible UI.
- **Applies to:** all; touch / pointer / keyboard / AT; general
- **Generalizability:** high — a general heuristic rather than a fixed density target.
- **Conflicts/tensions:** F-NB-13 and F-NB-19 show costs of hiding navigation or labels for visual simplicity.
- **Candidate knowledge targets:** information hierarchy; visual clarity; content density

### F-NB-09: Explain errors precisely and protect users’ effort

- **Source:** Error-Message Guidelines — https://www.nngroup.com/articles/error-message-guidelines/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2023-05-14
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Error messages should be visible, readable, constructive, and nonjudgmental. NN/g recommends naming the problem in familiar language, offering remedies, and preserving users’ work rather than making them start over.
- **Interpretation:** Design recovery with the message: retain valid input, explain the next action, and keep technical diagnostics secondary.
- **Applies to:** all; touch / pointer / keyboard / AT; general
- **Generalizability:** high — broad recovery guidance; sensitive failures may require careful disclosure.
- **Conflicts/tensions:** F-NB-53: specific validation messages are stronger than generic ‘invalid’ text; avoid exposing unnecessary technical detail.
- **Candidate knowledge targets:** error messages; recovery; input preservation

### F-NB-10: Prefer concise help in the context of the task

- **Source:** Help and Documentation (Usability Heuristic #10) — https://www.nngroup.com/articles/help-and-documentation/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2020-12-13
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g distinguishes proactive and reactive help. Contextual help related to current work is less likely to be ignored than pushed instructions; pushed help should be dismissible, and users should be able to retrieve help later.
- **Interpretation:** Offer focused assistance beside unfamiliar tasks and maintain searchable instructions; make any introductory walkthrough skippable and revisitable.
- **Applies to:** all; touch / pointer / keyboard / AT; general
- **Generalizability:** high — broad guidance, with more extensive training appropriate for complex domains.
- **Conflicts/tensions:** F-NB-41 does not establish that all onboarding or specialist training is ineffective.
- **Candidate knowledge targets:** contextual help; onboarding; documentation

### F-NB-11: Design for interrupted work and limited mobile overview

- **Source:** Mobile User Experience: Limitations and Strengths — https://www.nngroup.com/articles/mobile-ux/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2015-04-19
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Drawing on repeated mobile studies, NN/g describes small viewports, fragmented attention, variable connectivity, and constrained multitasking. It recommends saving state and context so users can resume without redoing work.
- **Interpretation:** Preserve drafts, navigation position, and task context; keep tasks self-contained and make resumption understandable. Offline persistence is an implementation implication, not a tested PWA result here.
- **Applies to:** mobile; touch / keyboard; mobile websites and apps
- **Generalizability:** medium — research spans mobile websites and apps but dates to 2015; device capabilities have evolved.
- **Conflicts/tensions:** F-NB-14: mobile constraints should not become restrictions imposed on desktop users.
- **Candidate knowledge targets:** interruption recovery; responsive design; state preservation

### F-NB-12: Size and space touch targets for accurate selection

- **Source:** Touch Targets on Touchscreens — https://www.nngroup.com/articles/touch-target-size/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2019-05-05
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Citing a target-acquisition study, NN/g recommends physical targets of at least 1 cm × 1 cm and describes observed errors from small or crowded targets. Readable elements can still be too small to tap reliably.
- **Interpretation:** Evaluate actual hit areas and adjacent-action spacing on real devices; enlarge targets without requiring the visible icon itself to fill the hit area.
- **Applies to:** mobile / tablet / touch-enabled desktop; touch; general
- **Generalizability:** medium — physical acquisition principles transfer; the article is not a normative CSS-pixel accessibility standard.
- **Conflicts/tensions:** Do not equate its centimetres with Apple points or a WCAG threshold; see Disagreements.
- **Candidate knowledge targets:** touch targets; input ergonomics; error prevention

### F-NB-13: Hidden navigation reduces discoverability on both screen classes

- **Source:** Hamburger Menus and Hidden Navigation Hurt UX Metrics — https://www.nngroup.com/articles/hamburger-menus/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2016-06-26
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** In testing with 179 participants on 6 sites, hidden navigation was used less and later and performed worse on UX measures than visible or partly visible navigation. The penalty was greater on desktop. The study did not fully test a purely visible mobile condition.
- **Interpretation:** Expose important destinations where space permits and test a combination of visible priorities and an overflow menu on phones.
- **Applies to:** mobile / desktop; touch / pointer; website content finding
- **Generalizability:** medium — measured across several sites in 2016, not proof that every hamburger implementation fails.
- **Conflicts/tensions:** F-NB-15: limited space and many destinations can justify mobile menus; the study is not a direct bottom-tabs comparison.
- **Candidate knowledge targets:** navigation visibility; hamburger menus; responsive navigation

### F-NB-14: Optimize desktop navigation instead of enlarging a mobile layout

- **Source:** Mobile First Is NOT Mobile Only — https://www.nngroup.com/articles/mobile-first-not-mobile-only/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2016-07-24
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** The companion navigation-study analysis attributes poor desktop navigation use to patterns carried over from mobile, including hidden navigation and collapsed search. NN/g argues that each platform’s space and needs should shape its design.
- **Interpretation:** Use larger viewports to expose useful destinations, search, and comparison context while preserving the same underlying capabilities.
- **Applies to:** mobile / tablet / desktop; touch / pointer / keyboard; responsive websites
- **Generalizability:** medium — the findings directly cover desktop and smartphones; tablet extension is an interpretation.
- **Conflicts/tensions:** F-NB-04: consistent meaning does not require identical presentation.
- **Candidate knowledge targets:** mobile-first not mobile-only; responsive layouts

### F-NB-15: Choose mobile tabs and menus according to destination count and chrome cost

- **Source:** Basic Patterns for Mobile Navigation: A Primer — https://www.nngroup.com/articles/mobile-navigation-patterns/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2015-11-15
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g describes visible navigation and persistent tab bars as discoverable but space-consuming, especially when there are many destinations. Hamburger menus fit more options but make individual destinations less discoverable. Its tab-position examples reflect contemporary native platform conventions.
- **Interpretation:** Use a small stable set of frequent destinations for visible tabs where appropriate; evaluate content space, labels, and target size together rather than prescribing bottom tabs for every PWA.
- **Applies to:** mobile; touch; mobile sites and native-app examples
- **Generalizability:** medium — tradeoffs transfer, but 2015 iOS/Android tab placement is historical platform context.
- **Conflicts/tensions:** F-NB-13 favors visibility; neither source establishes a universally optimal bottom-navigation layout.
- **Candidate knowledge targets:** mobile navigation; tabs; menus; content-to-chrome ratio

### F-NB-16: Use card sorting to discover grouping expectations, then evaluate the IA

- **Source:** Card Sorting: Uncover Users’ Mental Models for Better Information Architecture — https://www.nngroup.com/articles/card-sorting-definition/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2024-02-02
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Card sorting asks participants to organize labeled items into meaningful groups, revealing mental models useful for information architecture. NN/g distinguishes this from tree testing, which evaluates an existing structure, and notes that card sorting lacks the full interface context.
- **Interpretation:** Research category names and grouping with representative users, then test realistic findability rather than treating a card-sort cluster as a finished navigation system.
- **Applies to:** all; touch / pointer / keyboard / AT; research method for information architecture
- **Generalizability:** high — broadly useful method guidance, not evidence that a particular taxonomy works.
- **Conflicts/tensions:** Grouping based on repeated keywords can differ from conceptual grouping; page context and task behavior need separate validation.
- **Candidate knowledge targets:** information architecture; card sorting; tree testing

### F-NB-17: Defer secondary complexity while keeping frequent tasks visible

- **Source:** Progressive Disclosure — https://www.nngroup.com/articles/progressive-disclosure/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2006-12-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Progressive disclosure initially exposes primary functions and moves advanced or rarely used options to a secondary level. NN/g says the split must match actual task importance and the route to additional options must be obvious and well labeled.
- **Interpretation:** Hide optional complexity, not the action or information required for the main task; validate both common and advanced tasks.
- **Applies to:** all; touch / pointer / keyboard / AT; general applications and information-rich sites
- **Generalizability:** high — broadly useful principle whose specific split requires task research.
- **Conflicts/tensions:** F-NB-13, F-NB-37, and F-NB-63: hiding has costs when users need broad overview or most content.
- **Candidate knowledge targets:** progressive disclosure; cognitive load; complexity management

### F-NB-18: Reduce unnecessary fields and provide a clear reading sequence

- **Source:** Website Forms Usability: Top 10 Recommendations — https://www.nngroup.com/articles/web-form-design/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2016-05-01
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends short forms, proximity between labels and fields, logical field order, and generally a single column. It allows limited exceptions for short related fields and notes that very long desktop forms can warrant side labels.
- **Interpretation:** Start with a single clear entry path and remove fields that can be omitted, inferred, or deferred; test keyboard order as well as visual order.
- **Applies to:** all; touch / pointer / keyboard / AT; general website forms
- **Generalizability:** high — broad form-design guidance, with layout dependent on content and context.
- **Conflicts/tensions:** F-NB-45: shorter perceived effort does not necessarily mean fewer screens; F-NB-46 includes mobile orientation exceptions.
- **Candidate knowledge targets:** form layout; field reduction; keyboard sequence

### F-NB-19: Do not replace persistent labels with disappearing placeholders

- **Source:** Placeholders in Form Fields Are Harmful — https://www.nngroup.com/articles/form-design-placeholders/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2014-05-11; last reviewed 2018-09-10
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** NN/g reports usability and eyetracking problems when placeholders stand in for labels: people lose field context, cannot readily review autofill or correct errors, and may overlook fields that look filled. Important instructions also become harder to use when they disappear.
- **Interpretation:** Keep an external visible label and persistent essential hints, including after typing, autofill, errors, and interruption.
- **Applies to:** all; touch / pointer / keyboard / AT; general forms
- **Generalizability:** high — multiple mechanisms affect both mobile and desktop; findings are not a ban on every supplementary placeholder.
- **Conflicts/tensions:** F-NB-47 notes narrow exceptions in Baymard’s older article; floating labels require a separate assessment.
- **Candidate knowledge targets:** persistent labels; placeholders; form accessibility

### F-NB-20: Identify required fields individually rather than relying on a global instruction

- **Source:** Marking Required Fields in Forms — https://www.nngroup.com/articles/required-fields/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2019-06-16
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends marking each required field with an asterisk or ‘required’; instructions at the top can be missed or forgotten. It says marking optional fields too reduces cognitive load, but describes this as beneficial rather than obligatory.
- **Interpretation:** Make the status understandable at each field and expose its meaning to assistive technology.
- **Applies to:** all; touch / pointer / keyboard / AT; general forms
- **Generalizability:** high — broad guidance; familiar minimal login forms are a contextual exception discussed by the source.
- **Conflicts/tensions:** F-NB-49 is stronger about marking both types; older NN/g form guidance is less explicit. See Disagreements.
- **Candidate knowledge targets:** required fields; optional fields; form expectations

### F-NB-21: Validate completed input and keep error instructions beside the field

- **Source:** 10 Design Guidelines for Reporting Errors in Forms — https://www.nngroup.com/articles/errors-forms-design-guidelines/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2019-02-03; last reviewed 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends inline errors after users finish a field, actionable messages near the affected input, and non-color cues. It warns against premature errors, tooltip-only errors, and relying on a summary as the only error indication.
- **Interpretation:** Show the issue where it can be fixed, preserve inputs, and use any summary as a way to locate errors rather than as the sole explanation.
- **Applies to:** all; touch / pointer / keyboard / AT; forms
- **Generalizability:** high — broadly applicable recommendation, not a normative timing requirement.
- **Conflicts/tensions:** F-NB-50 agrees on completion-sensitive timing; guidance while constructing a complex password is distinct from declaring an incomplete first entry invalid.
- **Candidate knowledge targets:** inline validation; error placement; recovery

### F-NB-22: Use positive validation when it adds useful information

- **Source:** 10 Design Guidelines for Reporting Errors in Forms — https://www.nngroup.com/articles/errors-forms-design-guidelines/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2019-02-03; last reviewed 2024-12-12
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends success feedback for complex inputs such as available usernames or password requirements, but cautions that a success message for a field whose only requirement is nonemptiness can distract without adding useful context.
- **Interpretation:** Reserve extra success treatment for meaningful uncertainty; evaluate whether routine checkmarks improve confidence or add noise.
- **Applies to:** all; touch / pointer / keyboard / AT; forms
- **Generalizability:** medium — expert recommendation; optimal reassurance depends on task risk and audience.
- **Conflicts/tensions:** Direct tension with F-NB-52, which reports benefits from positive validation for all checkout fields.
- **Candidate knowledge targets:** positive validation; feedback density

### F-NB-23: Reduce the thinking required to understand and complete forms

- **Source:** Few Guesses, More Success: 4 Principles to Reduce Cognitive Load in Forms — https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2025-07-18
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g organizes cognitive-load guidance around structure, transparency, clarity, and support. Logical grouping, explicit requirements, predictable progression, and relevant branching reduce interpreting, remembering, and deciding during entry.
- **Interpretation:** Measure comprehension and hesitation alongside typing effort; show upcoming expectations and ask only relevant follow-up questions.
- **Applies to:** all; touch / pointer / keyboard / AT; general forms
- **Generalizability:** high — broad synthesis rather than a controlled evaluation of the complete framework.
- **Conflicts/tensions:** F-NB-45 supports reducing considered fields; disclosure must still preserve orientation and review.
- **Candidate knowledge targets:** cognitive load; form structure; branching; progress

### F-NB-24: Match filtering criteria and labels to the current content and users

- **Source:** Defining Helpful Filter Categories and Values for Better UX — https://www.nngroup.com/articles/filter-categories-values/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2018-07-15
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** NN/g’s research examples show users struggling when key criteria are missing or unfamiliar. It recommends filter categories and values that are relevant, predictable, free of jargon, and prioritized for the user’s needs.
- **Interpretation:** Derive facets from real decision criteria and adapt them to the content category; provide clear active-filter context.
- **Applies to:** all; touch / pointer / keyboard; search and large content collections
- **Generalizability:** medium — examples are heavily shopping and travel oriented, though the article discusses broader collections.
- **Conflicts/tensions:** F-NB-62: filtering narrows a set whereas sorting changes order; the controls must communicate different effects.
- **Candidate knowledge targets:** faceted search; filter labels; domain vocabulary

### F-NB-25: Choose batch or live filtering by intent, latency, and UI stability

- **Source:** User Intent Affects Filter Design — https://www.nngroup.com/articles/applying-filters/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2016-02-07
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g says refreshing after each choice can interrupt people who intend to select several filters, especially on slow sites. It recommends considering user intent and response speed and avoiding page-position changes that disrupt continued selection.
- **Interpretation:** Support a coherent selection episode; preserve position and focus, and use explicit Apply where repeated updates would interrupt it.
- **Applies to:** all; touch / pointer / keyboard; filtering
- **Generalizability:** high — the decision framework transfers better than a fixed rule about Apply buttons.
- **Conflicts/tensions:** Qualifies the live-update preference in F-NB-26 and the platform-based advice in F-NB-60.
- **Candidate knowledge targets:** filter application; latency; focus and scroll stability

### F-NB-26: A mobile filter tray can preserve the relationship between choices and results

- **Source:** Mobile Faceted Search with a Tray: New and Improved Design Pattern — https://www.nngroup.com/articles/mobile-faceted-search/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2015-07-26
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g presents an overlay tray as a way to retain some simultaneous visibility of facets and results on small screens. It favors fast feedback because that visibility helps people understand what a filter does.
- **Interpretation:** Consider partial overlays when the remaining results area is useful; compare them with full-screen batch filtering for complex selections.
- **Applies to:** mobile; touch; search and faceted results
- **Generalizability:** medium — 2015 design analysis with examples; no universal controlled result for all mobile filter designs.
- **Conflicts/tensions:** F-NB-60 recommends deliberate Apply on mobile; F-NB-25 makes latency and multi-selection intent explicit.
- **Candidate knowledge targets:** mobile filters; overlay trays; immediate feedback

### F-NB-27: Distinguish empty results from loading and failure, then offer a useful next step

- **Source:** Designing Empty States in Complex Applications: 3 Guidelines — https://www.nngroup.com/articles/empty-state-interface-design/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2021-09-19
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g says unexplained empty containers leave users uncertain whether processing finished, failed, or found nothing. It specifically criticizes showing ‘No records’ while data is still loading and recommends contextual learning cues and paths into key tasks.
- **Interpretation:** Model loading, empty, error, and initial setup separately; explain the cause of emptiness and offer a relevant action such as adjusting filters or creating an item.
- **Applies to:** all; touch / pointer / keyboard / AT; complex applications
- **Generalizability:** high — directly relevant to general web-app states; specific text and actions depend on the cause.
- **Conflicts/tensions:** F-NB-40: a disappearing error toast cannot replace a persistent failed-state explanation.
- **Candidate knowledge targets:** empty states; loading states; no-results recovery; onboarding

### F-NB-28: Use response-time thresholds as human-experience heuristics

- **Source:** Response Times: The 3 Important Limits — https://www.nngroup.com/articles/response-times-3-important-limits/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 1993-01-01; web-application update added 2014 (day not shown)
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g’s historical synthesis gives approximate limits of 0.1 seconds for instantaneous response, 1 second for uninterrupted thought, and 10 seconds for sustained attention. Longer or variable waits need progress information; its web update applies the same reasoning to web applications.
- **Interpretation:** Acknowledge input quickly and provide increasingly informative feedback for longer work. These figures are design heuristics, not a performance SLA or a standard.
- **Applies to:** all; touch / pointer / keyboard / AT; interactive applications
- **Generalizability:** medium — foundational synthesis based on older research; perceived delay varies by task and expectations.
- **Conflicts/tensions:** F-NB-29 adds progress treatment; do not delay a completed operation merely to meet a threshold.
- **Candidate knowledge targets:** response times; perceived performance; feedback timing

### F-NB-29: Communicate ongoing progress rather than leaving users uncertain

- **Source:** Progress Indicators Make a Slow System Less Insufferable — https://www.nngroup.com/articles/progress-indicators/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2014-10-26
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** NN/g reports research in which a dynamic progress indicator improved tolerance of waiting and explains that lack of feedback can provoke repeated clicks. Determinate progress is useful when remaining work can be estimated; other ongoing feedback is needed when it cannot.
- **Interpretation:** Represent actual work and completion honestly, identify what is loading, and avoid leaving an indefinite indicator as the only recovery path for failed work.
- **Applies to:** all; touch / pointer / keyboard / AT; loading and long-running tasks
- **Generalizability:** medium — article summarizes external studies and design advice; it does not establish one ideal spinner or skeleton for every task.
- **Conflicts/tensions:** F-NB-27: an empty-state message must not masquerade as progress; F-NB-28 provides approximate timing context.
- **Candidate knowledge targets:** progress indicators; duplicate-action prevention; long-running work

### F-NB-30: Reserve specific confirmations for serious consequences and support undo

- **Source:** Confirmation Dialogs Can Prevent User Errors — If Not Overused — https://www.nngroup.com/articles/confirmation-dialog/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2018-02-18; last reviewed 2026-08-07
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends confirmations for serious or irreversible actions, not routine actions. Dialogs should identify affected objects and consequences and use action-specific choices; repetitive generic confirmations encourage automatic acceptance. Undo is preferable where feasible.
- **Interpretation:** Offer recoverable actions with clear undo, and require a meaningful confirmation when harm cannot reasonably be reversed.
- **Applies to:** all; touch / pointer / keyboard / AT; destructive or costly actions
- **Generalizability:** high — broadly transferable risk-sensitive guidance, with thresholds dependent on the domain.
- **Conflicts/tensions:** F-NB-03 supports recovery; F-NB-39 explains the interruption cost of modals.
- **Candidate knowledge targets:** destructive actions; confirmation dialogs; undo

### F-NB-31: Keep essential information available without hover

- **Source:** Tooltip Guidelines — https://www.nngroup.com/articles/tooltip-guidelines/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2019-01-27
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g describes tooltips as brief, user-triggered supplemental information available through pointer or keyboard hover. It says essential task instructions do not belong in tooltips and distinguishes touch/click popup tips from hover tooltips.
- **Interpretation:** Keep required labels and instructions visible; support focus access for tooltips and provide a deliberate touch path for optional explanations.
- **Applies to:** all; touch / pointer / keyboard / AT; contextual help
- **Generalizability:** high — input-capability distinction transfers across responsive devices, including hybrid laptops.
- **Conflicts/tensions:** F-NB-19 and F-NB-21: labels and errors need persistence rather than hover dependence.
- **Candidate knowledge targets:** hover; tooltips; input capabilities; contextual help

### F-NB-32: Make keyboard shortcuts learnable and avoid overriding established commands

- **Source:** UI Copy: UX Guidelines for Command Names and Keyboard Shortcuts — https://www.nngroup.com/articles/ui-copy/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2019-03-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends shortcuts for frequent tasks, discoverable references beside commands, equivalents for Mac and Windows, and avoiding conflicts with established or assistive-technology shortcuts. New combinations should be memorable and not demand excessive modifiers.
- **Interpretation:** Add shortcuts as optional accelerators and test interactions with browsers, text fields, operating systems, and assistive technologies.
- **Applies to:** all with hardware keyboard; keyboard / AT; general applications
- **Generalizability:** high — relevant beyond desktop-only layouts; actual key availability varies.
- **Conflicts/tensions:** F-NB-07: visible controls remain necessary for novices and other input modes.
- **Candidate knowledge targets:** keyboard shortcuts; accelerators; conventions

### F-NB-33: Choose table behavior around finding, comparing, editing, and acting

- **Source:** Data Tables: Four Major User Tasks — https://www.nngroup.com/articles/data-tables/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2022-04-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g identifies four core workplace-table tasks: find records, compare data, view/edit/add one record, and take actions. Tables support comparison by showing adjacent data; relevant column order, recognizable identifiers, and clear filtered state matter.
- **Interpretation:** On narrow screens, preserve the comparisons and actions the task needs instead of automatically converting every row to an isolated card.
- **Applies to:** desktop / mobile / tablet; pointer / keyboard / touch; workplace data tables
- **Generalizability:** medium — source focuses primarily on large workplace tables on desktop; the responsive consequence is interpretation.
- **Conflicts/tensions:** F-NB-14: more space can support simultaneous comparison; this source does not validate a particular mobile table layout.
- **Candidate knowledge targets:** data tables; comparison; bulk actions; responsive data

### F-NB-34: Choose scrolling and pagination according to task and refinding needs

- **Source:** Infinite Scrolling: When to Use It, When to Avoid It — https://www.nngroup.com/articles/infinite-scrolling-tips/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2022-09-04
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g describes infinite scrolling as useful for continuous browsing but problematic for refinding, reaching the footer, keyboard navigation, and page weight. It discusses Load More and integrated pagination and says no approach is best for every site.
- **Interpretation:** Favor bounded landmarks for deliberate retrieval and comparison; preserve list position and loaded context when returning from details.
- **Applies to:** all; touch / pointer / keyboard / AT; long lists and feeds
- **Generalizability:** high — broad task-based tradeoffs; the article does not rank every pattern in every domain.
- **Conflicts/tensions:** F-NB-03 and F-NB-61: Back should retain useful list and filter state.
- **Candidate knowledge targets:** infinite scroll; pagination; Load More; position restoration

### F-NB-35: Persistent headers earn their space only when they support real needs

- **Source:** Sticky Headers: 5 Ways to Make Them Better — https://www.nngroup.com/articles/sticky-headers/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2021-04-04
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends small, readable, clearly differentiated sticky headers with minimal motion and consideration of whether persistence is needed at all. Partially persistent headers can restore access when users scroll upward.
- **Interpretation:** Keep frequent navigation or actions available without obscuring content; test the combined cost of headers, bottom bars, keyboards, and overlays.
- **Applies to:** all; touch / pointer / keyboard; scrolling pages
- **Generalizability:** high — general tradeoff, with the usable size dependent on content and device.
- **Conflicts/tensions:** F-NB-12: shrinking chrome must not shrink usable touch targets; F-NB-15 considers total chrome rather than one bar alone.
- **Candidate knowledge targets:** sticky headers; persistent actions; content occlusion

### F-NB-36: Treat contextual swipe as an enhancement with consistent meanings

- **Source:** Using Swipe to Trigger Contextual Actions — https://www.nngroup.com/articles/contextual-swipe/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2017-02-12
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g describes poor discoverability, obscured item identity, unexpected actions, and inconsistent swipe meanings in mobile apps. Familiarity with swipe-to-delete does not ensure users will discover unrelated commands hidden behind the same gesture.
- **Interpretation:** Provide visible alternative actions, keep the affected item identifiable, and avoid changing gesture meaning unpredictably across contexts.
- **Applies to:** mobile / tablet; touch; native-app examples
- **Generalizability:** medium — the observations are mainly native apps; transfer to PWA gestures requires browser and accessibility testing.
- **Conflicts/tensions:** F-NB-07 supports optional accelerators; F-NB-30 supports undo or confirmation for destructive effects.
- **Candidate knowledge targets:** gestures; swipe actions; discoverability; undo

### F-NB-37: Use accordions for selective reading, not simply to shorten desktop pages

- **Source:** Accordions Are Not Always the Answer for Complex Content on Desktops — https://www.nngroup.com/articles/accordions-complex-content/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2014-05-18
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g warns that opening headings increases interaction and decision effort and hides information. When users need most sections, exposing content can be easier than repeatedly expanding it; clear headings and accessible behavior are necessary.
- **Interpretation:** Use accordions where people need different subsets, and prefer visible content or an overview when tasks require cross-section reading and comparison.
- **Applies to:** desktop; pointer / keyboard / AT; complex website content
- **Generalizability:** medium — article specifically addresses desktop content; mobile costs and space constraints need separate evaluation.
- **Conflicts/tensions:** F-NB-17: progressive disclosure helps only when the hidden material is genuinely secondary for the task.
- **Candidate knowledge targets:** accordions; disclosure; scanning; long-form content

### F-NB-38: Use breadcrumbs to express hierarchy, not browsing history

- **Source:** Breadcrumbs: 11 Design Guidelines for Desktop and Mobile — https://www.nngroup.com/articles/breadcrumbs/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2018-12-23; last reviewed 2026-09-01
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g recommends breadcrumbs for wayfinding and access to ancestors, particularly on direct entry to deep pages. They supplement global and local navigation. Mobile breadcrumbs should avoid tiny targets and wrapping that makes the trail difficult to use.
- **Interpretation:** Show a meaningful hierarchy and preserve accessible parent navigation on narrow screens; keep browser Back as a separate history function.
- **Applies to:** all; touch / pointer / keyboard / AT; hierarchical sites
- **Generalizability:** high — useful when the information model has meaningful ancestors; less applicable to flat workflows.
- **Conflicts/tensions:** F-NB-03 distinguishes history from hierarchy; collapsing a trail trades overview for space.
- **Candidate knowledge targets:** breadcrumbs; wayfinding; deep links; hierarchy

### F-NB-39: Interrupt with a modal only when immediate attention is justified

- **Source:** Modal & Nonmodal Dialogs: When (& When Not) to Use Them — https://www.nngroup.com/articles/modal-nonmodal-dialog/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2017-04-23
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g defines modals as disabling background interaction until addressed and explains their costs: interruption, context switching, and forgetting the original task. It recommends matching modality to importance rather than using it indiscriminately.
- **Interpretation:** Use nonmodal or in-context communication for ordinary status and short corrections; make consequential blocking decisions clear and easy to exit.
- **Applies to:** all; touch / pointer / keyboard / AT; dialogs
- **Generalizability:** high — broad interaction principle; a complete accessible modal implementation needs additional normative sources.
- **Conflicts/tensions:** F-NB-30 justifies confirmations for serious harm; F-NB-21 cautions against modal form errors.
- **Candidate knowledge targets:** modals; interruption cost; nonmodal dialogs

### F-NB-40: Transient toasts are unsuitable as the sole error message

- **Source:** Indicators, Validations, and Notifications: Pick the Correct Communication Option — https://www.nngroup.com/articles/indicators-validations-notifications/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2024-01-17
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** NN/g distinguishes communication by urgency and required action. It reports a mobile participant missing a brief error message and waiting for content that would not load, and says fading toasts are a poor way to present errors.
- **Interpretation:** Keep blocking failures and recovery actions persistent and discoverable; use low-intrusion transient feedback for outcomes that can safely be missed.
- **Applies to:** all; touch / pointer / keyboard / AT; status and notifications
- **Generalizability:** medium — specific observation plus broader design guidance, not a universal toast-duration experiment.
- **Conflicts/tensions:** F-NB-01 requires feedback; F-NB-39 limits interruption, so persistence need not mean modality.
- **Candidate knowledge targets:** toasts; notifications; persistent errors; feedback priority

### F-NB-41: Do not assume introductory tutorial cards improve simple-task performance

- **Source:** Mobile Tutorials: Wasted Effort or Efficiency Boost? — https://www.nngroup.com/articles/mobile-tutorials/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2020-03-08
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** A between-subject study with 70 users and 4 relatively simple iPhone apps found no significant task-success or completion-time benefit from viewing deck-of-cards tutorials; tutorial viewers rated tasks harder. Participants already knew iOS, and the study did not test every onboarding technique.
- **Interpretation:** Prefer usable defaults and contextual assistance for ordinary interactions; test instructional onboarding when a novel or specialized workflow genuinely requires it.
- **Applies to:** mobile; touch; first use of relatively simple native iPhone apps
- **Generalizability:** medium — direct experimental evidence with important app, task, platform, and tutorial-format limits.
- **Conflicts/tensions:** F-NB-10 supports contextual help; this finding does not rule out setup, permissions explanation, interactive practice, or enterprise training.
- **Candidate knowledge targets:** onboarding; tutorials; contextual learning

### F-NB-42: Judge success by informed user outcomes as well as conversions

- **Source:** Deceptive Patterns in UX: How to Recognize and Avoid Them — https://www.nngroup.com/articles/deceptive-patterns/
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 2023-12-01
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** NN/g describes deceptive patterns as steering users toward business-benefiting choices through deception, misdirection, shame, or obstruction. It warns that conversion-focused experiments and copying competitors can normalize harmful designs.
- **Interpretation:** Review consent, cancellation, pricing, defaults, and exit paths for informed choice; conversion increases alone do not demonstrate improved UX.
- **Applies to:** all; touch / pointer / keyboard / AT; trust and choice architecture
- **Generalizability:** high — broad ethical design guidance; the article is not a jurisdiction-specific legal standard.
- **Conflicts/tensions:** F-NB-05: defaults and friction reduction must serve the user, not conceal consequential choices.
- **Candidate knowledge targets:** trust; deceptive patterns; consent; meaningful metrics

### F-NB-43: Interpret Baymard as primarily e-commerce usability evidence

- **Source:** Baymard’s UX Research Methodology — https://baymard.com/research/methodology
- **Publisher:** Baymard Institute
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard describes moderated think-aloud usability testing, manual site benchmarking, eye tracking, and quantitative studies. The methodology page reports 4,400+ participant/site sessions across 25 qualitative rounds and explicitly says the aim is not precise statistical prediction of issue incidence on an individual site.
- **Interpretation:** Use observations to identify mechanisms and candidate solutions; distinguish benchmark implementation prevalence from the percentage of users who will fail or any promised conversion lift.
- **Applies to:** all; touch / pointer / keyboard; primarily e-commerce finding, evaluation, purchase, and account tasks
- **Generalizability:** low — e-commerce-specific research population and tasks, mainly US/European contexts; study mechanisms may transfer but prevalence estimates do not.
- **Conflicts/tensions:** Counts of sessions, participants, sites, guidelines, and research hours are different denominators and should not be substituted for one another.
- **Candidate knowledge targets:** evidence quality; research interpretation; generalizability

### F-NB-44: Mobile commerce patterns involve genuine constraints and compromises

- **Source:** Mobile E-Commerce UX — https://baymard.com/research/mcommerce-usability
- **Publisher:** Baymard Institute
- **Published/updated:** not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard’s public mobile overview describes research into touch input, limited screen space, and mobile shopping behavior. It emphasizes loss of page overview and says even better-performing mobile patterns remain compromises under these constraints. Detailed guidelines are offered through Premium.
- **Interpretation:** Evaluate mobile flows as complete tasks, including orientation and recovery; a compact rendering of desktop content is insufficient evidence of usability.
- **Applies to:** mobile; touch; e-commerce websites
- **Generalizability:** low — e-commerce-specific public overview; findings do not establish outcomes for all responsive apps or PWAs.
- **Conflicts/tensions:** F-NB-14 supports adaptation across screen sizes; do not infer mobile conversion differences are caused solely by UX.
- **Candidate knowledge targets:** mobile overview; responsive tradeoffs; evidence scope

### F-NB-45: Reduce fields users must consider before optimizing checkout step count

- **Source:** Checkout Optimization: 5 Ways to Minimize Form Fields in Checkout — https://baymard.com/research-articles/checkout-flow-average-form-fields
- **Publisher:** Baymard Institute
- **Published/updated:** 2024-06-26
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard reports that the number of fields users must manage generally matters more to checkout usability than the number of steps. Its 2024 benchmark averages are 5.1 steps and 11.3 fields; these are descriptive values, not targets for every checkout.
- **Interpretation:** Remove unnecessary decisions and visible inputs first; assess total effort, error recovery, and review instead of optimizing a screen-count metric.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; checkout
- **Generalizability:** medium — e-commerce-specific evidence; reducing unnecessary consideration is likely general, but field counts and checkout thresholds are not.
- **Conflicts/tensions:** F-NB-18 and F-NB-23: a clear staged flow can be easier than cramming everything onto one screen.
- **Candidate knowledge targets:** form effort; checkout; progressive disclosure; workflow metrics

### F-NB-46: Above-field mobile labels leave space to see and correct input

- **Source:** Field Label UX: Place Labels Above the Field — https://baymard.com/research-articles/mobile-form-usability-label-position
- **Publisher:** Baymard Institute
- **Published/updated:** 2013-03-19
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** In mobile-commerce testing, left-positioned labels often left fields too narrow to display entered values, making error detection and correction difficult. Above-field labels permit wider inputs. The article discusses very short forms and landscape orientation as exceptions to a blanket positioning rule.
- **Interpretation:** Default to persistent labels above mobile inputs, and verify the form with the keyboard open in portrait and landscape rather than relying on a full-page mockup.
- **Applies to:** mobile; touch; checkout and account forms
- **Generalizability:** medium — likely general for narrow forms; e-commerce evidence uses 2013 devices, so the exact landscape layout needs current validation.
- **Conflicts/tensions:** F-NB-18 allows context-specific desktop side labels; more vertical scrolling can be preferable to hidden input.
- **Candidate knowledge targets:** field labels; keyboard occlusion; form layout

### F-NB-47: Disappearing in-field labels remove the context needed for error recovery

- **Source:** Mobile Form Usability: Never Use Inline Labels — https://baymard.com/research-articles/mobile-forms-avoid-inline-labels
- **Publisher:** Baymard Institute
- **Published/updated:** 2013-06-04
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed mobile shoppers deleting entered values to reveal vanished labels, struggling with validation, and sometimes abandoning. Its ‘inline labels’ mean labels inside the input that disappear, not inline validation. The article allows limited familiar one- or two-field exceptions.
- **Interpretation:** Keep field identity and essential format guidance visible through typing, review, errors, and resumption; do not treat a search-box exception as a general form pattern.
- **Applies to:** mobile / desktop; touch / keyboard / pointer; commerce forms
- **Generalizability:** high — likely general memory and review mechanisms, though evidence is primarily e-commerce.
- **Conflicts/tensions:** F-NB-19 aligns strongly; this older source’s narrow exceptions qualify its categorical title and do not validate all floating-label designs.
- **Candidate knowledge targets:** persistent labels; error context; form review

### F-NB-48: Avoid splitting one perceived input into several mobile fields

- **Source:** Mobile Form Usability: Avoid Splitting Single Input Entities — https://baymard.com/research-articles/mobile-form-usability-single-input-fields
- **Publisher:** Baymard Institute
- **Published/updated:** 2013-02-12
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed users struggling with phone numbers split across fields, ambiguous required/optional subparts, and names split contrary to users’ expectations. Extra field transitions interrupted typing. The article explicitly says its desktop checkout evidence was inconclusive for some split-field cases.
- **Interpretation:** Use one coherent field when users perceive one value, and format it without forcing extra focus changes; account for real international naming and address requirements.
- **Applies to:** mobile; touch / keyboard; commerce data entry
- **Generalizability:** medium — likely general for mobile entry of coherent values; not evidence that all compound information must use one field.
- **Conflicts/tensions:** F-NB-05 supports forgiving formatting; desktop conclusions and specialized structured inputs require separate assessment.
- **Candidate knowledge targets:** single input entities; focus transitions; names; phone fields

### F-NB-49: Mark both required and optional fields in long commerce forms

- **Source:** E-Commerce Checkouts Need to Mark Both Required Fields and Optional Fields Explicitly (Only 14% Do So) — https://baymard.com/research-articles/required-optional-form-fields
- **Publisher:** Baymard Institute
- **Published/updated:** 2018-10-02; body includes 2021 benchmark results (update date not shown)
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard’s repeated checkout studies found confusion, validation errors, slower progress, and abandonment when fields’ status was implicit. It recommends explicit marking of both types. The source limits its strongest claim to checkout and long account forms, saying short sign-up/contact forms are less affected.
- **Interpretation:** Make each field’s completion obligation clear without requiring a scan back to the top or inference from other fields.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; checkout and long account forms
- **Generalizability:** medium — e-commerce-specific evidence; likely general to long mixed-requirement forms, weaker for very short familiar forms.
- **Conflicts/tensions:** F-NB-20 requires marking required fields but calls optional marking beneficial rather than obligatory. See Disagreements.
- **Candidate knowledge targets:** required and optional fields; local instructions; error prevention

### F-NB-50: Avoid premature inline errors on untouched or unfinished fields

- **Source:** Usability Testing of Inline Form Validation: 31% Don’t Have It, 4% Get It Wrong — https://baymard.com/research-articles/inline-form-validation
- **Publisher:** Baymard Institute
- **Published/updated:** 2024-01-09
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed frustration and interrupted typing when fields were declared invalid before users had a chance to finish. It recommends checking on field exit or, for suitable inputs, after enough characters have been entered to judge completeness.
- **Interpretation:** Separate untouched, in-progress, invalid, and valid states; distinguish helpful construction guidance from an error that claims the user has finished incorrectly.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; checkout forms
- **Generalizability:** high — likely general entry and attention mechanisms; evidence originates in e-commerce.
- **Conflicts/tensions:** F-NB-21 aligns; fixed-length checking must respect variable national formats and valid input lengths.
- **Candidate knowledge targets:** inline validation; validation timing; form states

### F-NB-51: Remove stale errors as soon as the underlying issue is fixed

- **Source:** Usability Testing of Inline Form Validation: 31% Don’t Have It, 4% Get It Wrong — https://baymard.com/research-articles/inline-form-validation
- **Publisher:** Baymard Institute
- **Published/updated:** 2024-01-09
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed participants being misled when an error remained after correction, including mismatched repeated values where fixing the first field did not update the second field’s message. It recommends removing errors immediately once resolved.
- **Interpretation:** Revalidate related dependencies and synchronize error messages with the current values; do not force a second submit or focus change just to clear a resolved error.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; checkout forms
- **Generalizability:** high — likely general for interdependent inputs and truthful feedback; commerce supplies the direct observations.
- **Conflicts/tensions:** F-NB-50 concerns initial validation timing; correction feedback can be immediate without prematurely judging first input.
- **Candidate knowledge targets:** error recovery; dependent validation; truthful feedback

### F-NB-52: Baymard reports reassurance from positive validation for all fields

- **Source:** Usability Testing of Inline Form Validation: 31% Don’t Have It, 4% Get It Wrong — https://baymard.com/research-articles/inline-form-validation
- **Publisher:** Baymard Institute
- **Published/updated:** 2024-01-09
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard recommends positive inline validation for all fields, including ordinary inputs, to confirm acceptance and reduce uncertainty about whether entry was valid. This is separate from removing an existing error.
- **Interpretation:** Treat universal success cues as a testable commerce recommendation; compare confidence benefits against visual and assistive-technology noise in the target application.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; checkout forms
- **Generalizability:** medium — e-commerce-specific recommendation; transfer to dense professional or repeated-entry forms is uncertain.
- **Conflicts/tensions:** Direct disagreement with F-NB-22: NN/g advises success indicators only where the additional context is useful.
- **Candidate knowledge targets:** positive validation; confidence; feedback density

### F-NB-53: Explain the particular validation rule that failed

- **Source:** Improve Validation Errors with Adaptive Messages (98% Don’t) — https://baymard.com/research-articles/adaptive-validation-error-messages
- **Publisher:** Baymard Institute
- **Published/updated:** 2023-12-14
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed users becoming stuck or abandoning because generic error text did not reveal the actual cause. Adaptive messages change with the failing subrule, helping users distinguish such cases as missing input, too few digits, or a formatting problem.
- **Interpretation:** Map known validation failures to precise recovery instructions and retain the entered value; avoid implying a system or payment-provider failure when the issue is a correctable field.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; checkout and account entry
- **Generalizability:** high — likely general error-recovery mechanism; studied primarily in e-commerce.
- **Conflicts/tensions:** F-NB-09 aligns; field-specific explanations should not unnecessarily disclose sensitive authentication or system information.
- **Candidate knowledge targets:** adaptive errors; validation copy; recovery

### F-NB-54: Invoke a keyboard suited to the particular mobile input

- **Source:** ‘Touch Keyboard’ Implementations Have Improved Just 9% Since 2013 (60% Still Get it Wrong) — https://baymard.com/research-articles/mobile-touch-keyboards
- **Publisher:** Baymard Institute
- **Published/updated:** 2015-12-15
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard’s mobile testing found better performance with purpose-built touch keyboards, especially numeric input, and more typos when numeric fields used a standard keyboard. It emphasizes consistent configuration across a flow rather than optimizing only selected fields.
- **Interpretation:** Choose input semantics and keyboard hints per field, and test actual devices. Numeric-looking identifiers and international postal codes must still permit their valid characters.
- **Applies to:** mobile / tablet; touch; commerce checkout and sign-up forms
- **Generalizability:** high — likely general for touch entry; article examples and benchmark figures date to 2015.
- **Conflicts/tensions:** The separate keyboard cheat sheet failed to fetch; no current implementation recipe is inferred from it.
- **Candidate knowledge targets:** input types; input modes; touch keyboards

### F-NB-55: Disable harmful autocorrection and choose capitalization per field

- **Source:** ‘Touch Keyboard’ Implementations Have Improved Just 9% Since 2013 (60% Still Get it Wrong) — https://baymard.com/research-articles/mobile-touch-keyboards
- **Publisher:** Baymard Institute
- **Published/updated:** 2015-12-15
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed valid names, addresses, and other non-dictionary strings being autocorrected into wrong values, sometimes unnoticed before submission. It recommends configuring correction and capitalization according to the data being collected.
- **Interpretation:** Prevent text assistance from silently changing identifiers or addresses, while keeping useful typing assistance for ordinary prose and appropriate names.
- **Applies to:** mobile; touch; commerce forms
- **Generalizability:** high — likely general for data that dictionaries cannot reliably predict; exact browser attribute support needs current technical sources.
- **Conflicts/tensions:** F-NB-05: forgiving formatting helps, but silently changing meaningful content can introduce errors.
- **Candidate knowledge targets:** autocorrect; autocapitalization; data integrity

### F-NB-56: Address lookup can reduce effort and entry mistakes

- **Source:** Provide a “Fully Automatic Address Lookup” Feature (55% Don’t) — https://baymard.com/research-articles/automatic-address-lookup
- **Publisher:** Baymard Institute
- **Published/updated:** 2023-03-24
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard reports repeated friction during manual address entry and says live full-address suggestions performed well in testing. One round found typos or misspellings in 9% of manually entered shipping addresses; this is a study-specific observation, not a universal error rate.
- **Interpretation:** Offer address suggestions when coverage is good and users can inspect and edit the result; assess geographic coverage and actual delivery-address formats.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; shipping-address forms
- **Generalizability:** medium — e-commerce-specific evidence; likely general to address capture, but delivery and locality assumptions matter.
- **Conflicts/tensions:** F-NB-57 requires manual fallback; lookup is not proof that an address is deliverable or appropriate.
- **Candidate knowledge targets:** address autocomplete; error prevention; data-entry effort

### F-NB-57: Keep conventional address fields available alongside lookup and autofill

- **Source:** Provide a “Fully Automatic Address Lookup” Feature (55% Don’t) — https://baymard.com/research-articles/automatic-address-lookup
- **Publisher:** Baymard Institute
- **Published/updated:** 2023-03-24
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** When lookup did not provide the desired address, users needed conventional fields to continue manually. Baymard recommends displaying those fields by default for review, revision, and fallback, and notes that doing so also supports browser autofill.
- **Interpretation:** Treat lookup and browser autofill as aids to editable fields; make manual entry and correction straightforward when suggestions fail or the saved address is inappropriate.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; address forms
- **Generalizability:** high — likely general principle of automation with fallback; direct evidence is e-commerce address entry.
- **Conflicts/tensions:** F-NB-58 hides a secondary optional line; it does not justify hiding the core fields required for fallback.
- **Candidate knowledge targets:** browser autofill; address fallback; automation transparency

### F-NB-58: Reveal optional secondary address input when needed

- **Source:** Form Usability: Getting ‘Address Line 2’ Right — https://baymard.com/research-articles/address-line-2
- **Publisher:** Baymard Institute
- **Published/updated:** 2022-10-04
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard’s checkout and eyetracking observations found that an exposed ‘Address Line 2’ consumed attention and confused people who did not need it. It recommends placing the secondary field behind a clearly described link rather than showing an empty optional box by default.
- **Interpretation:** Use a discoverable ‘Add apartment, suite, etc.’ disclosure where this information is genuinely optional for the user population; preserve any populated secondary address.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; shipping and billing addresses
- **Generalizability:** medium — e-commerce-specific evidence; applicability varies with local address structures and how often secondary information is needed.
- **Conflicts/tensions:** F-NB-57 keeps core address fields visible; F-NB-17 requires sensible disclosure labels and task-based prioritization.
- **Candidate knowledge targets:** optional inputs; address forms; progressive disclosure

### F-NB-59: Avoid redundant Apply or Save buttons inside ordinary checkout entry

- **Source:** Checkout UX: Avoid “Apply” Buttons for Most Fields (22% of Sites Don’t) — https://baymard.com/research-articles/checkout-usability-apply-buttons
- **Publisher:** Baymard Institute
- **Published/updated:** 2012-07-11; updated 2025-05-14
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed shoppers missing intermediate Apply/Save controls or confusing them with the main continuation action, causing unsaved data and errors. Its updated public article recommends avoiding these for most checkout fields, with exceptions for promo codes and gift cards, and distinguishes editing account data.
- **Interpretation:** Have the primary continuation action commit ordinary step input predictably; use explicit save boundaries where users are deliberately editing persistent records or where the task requires a separate operation.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; checkout
- **Generalizability:** low — e-commerce-specific workflow convention; not a general instruction to autosave every web-app edit.
- **Conflicts/tensions:** F-NB-60 recommends Apply for mobile filters; different user goals justify different commit boundaries.
- **Candidate knowledge targets:** checkout progression; commit boundaries; Apply buttons

### F-NB-60: Baymard recommends explicit mobile filter application with a result count

- **Source:** What Is an Ecommerce Filter? UI Best Practices — https://baymard.com/blog/ecommerce-filter-ui
- **Publisher:** Baymard Institute
- **Published/updated:** 2026-04-17
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** The public filter-UI synthesis recommends deliberate ‘Show X Results’ application on mobile so multiple selections are not disrupted by refreshes, while generally preferring real-time updates on desktop. It also recommends clear result counts and visible filter state.
- **Interpretation:** Use platform differences as a starting hypothesis, then test selection episodes, latency, and continuity. Keep a mobile filter panel open while users assemble the intended combination.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; commerce filtering
- **Generalizability:** medium — e-commerce-specific practitioner synthesis referencing Baymard research; likely general where full-screen panels and multi-selection are used.
- **Conflicts/tensions:** F-NB-26 favors simultaneous results and controls; F-NB-25 conditions the choice on intent and speed rather than device alone.
- **Candidate knowledge targets:** mobile filters; Apply vs live updates; result counts

### F-NB-61: Show and allow removal of applied filters in the results context

- **Source:** Display “Applied Filters” in an Overview (28% Don’t) — https://baymard.com/research-articles/how-to-design-applied-filters
- **Publisher:** Baymard Institute
- **Published/updated:** 2020-10-06; updated 2026-05-13
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed disorientation and extra work when users could not see active filters without inspecting the sidebar or reopening the mobile panel. An applied-filter overview provides confirmation, context, and a faster removal path, including for filters inherited from an earlier link.
- **Interpretation:** Surface active constraints near the results, support individual removal and an appropriate reset, and preserve context when returning from details.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; product lists and search results
- **Generalizability:** high — likely general to filtered collections; evidence is primarily e-commerce.
- **Conflicts/tensions:** F-NB-06 supports recognition; counts in different dated Baymard benchmarks must not be treated as one current prevalence estimate.
- **Candidate knowledge targets:** applied filter chips; filtered-state clarity; filter removal

### F-NB-62: Make multi-select filtering and sorting effects explicit

- **Source:** What Is an Ecommerce Filter? UI Best Practices — https://baymard.com/blog/ecommerce-filter-ui
- **Publisher:** Baymard Institute
- **Published/updated:** 2026-04-17
- **Accessed:** 2026-11-08
- **Evidence class:** E4
- **Finding:** Baymard distinguishes filtering, which narrows a result set, from sorting, which reorders it. Its public synthesis recommends allowing multiple values within a filter group, typically OR within a group and AND across groups, so users can consider several acceptable alternatives.
- **Interpretation:** Use control types and labels that match selection semantics; retain the active sort and filters visibly, and test combinations that reflect actual decision criteria.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; commerce product lists
- **Generalizability:** medium — likely general for independent categorical facets; e-commerce supplies the framing, and other domains may need different Boolean semantics.
- **Conflicts/tensions:** F-NB-24 requires meaningful domain criteria; mutually exclusive states or specialized query builders may require different logic.
- **Candidate knowledge targets:** filter logic; sorting; multi-select controls

### F-NB-63: Truncate long filter-value lists only with discoverable expansion

- **Source:** 6 Guidelines for Truncation Design — https://baymard.com/research-articles/truncation-design
- **Publisher:** Baymard Institute
- **Published/updated:** 2014-05-21
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard found truncating long value lists could preserve overview better than displaying every value or using nested scrolling. The benefit depended on users noticing the expansion control; otherwise they mistook a partial list for the full set.
- **Interpretation:** Use clear ‘Show more’ wording and link styling, preserve selected options, and verify that users can discover a value initially hidden by truncation.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; commerce filters and option lists
- **Generalizability:** medium — likely general overview tradeoff; specific counts and layouts depend on the category and viewport.
- **Conflicts/tensions:** F-NB-17 supports secondary disclosure; F-NB-37 cautions against hiding information users commonly need. This is list truncation, not evidence about ellipsizing text.
- **Candidate knowledge targets:** filter-value truncation; Show more; nested scrolling

### F-NB-64: Keep search suggestions manageable and distinguish query from scope

- **Source:** 9 UX Best Practice Design Patterns for Autocomplete Suggestions (Only 19% Get Everything Right) — https://baymard.com/research-articles/autocomplete-design
- **Publisher:** Baymard Institute
- **Published/updated:** 2022-08-02
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard found long suggestion lists could slow or overwhelm users. It recommends no more than 10 suggestions on desktop and a target of 4–8 on mobile, distinct styling for category scope, keyboard navigation and active highlighting on desktop, and enough space with reduced competing content on mobile.
- **Interpretation:** Use a small useful suggestion set that remains legible with the keyboard open; let users understand whether selecting an option changes the query, its scope, or both.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; commerce search autocomplete
- **Generalizability:** medium — likely general suggestion-design mechanisms; counts are research recommendations, not universal limits or standards.
- **Conflicts/tensions:** F-NB-12 requires adequate hit areas; F-NB-31 rules out essential hover-only explanations.
- **Candidate knowledge targets:** search autocomplete; keyboard interaction; search scope

### F-NB-65: Combine product variants so mobile lists communicate real catalog breadth

- **Source:** Product List UX 2025: 8 Common Pitfalls & Best Practices (80% Have Serious Issues) — https://baymard.com/research-articles/current-state-product-list-and-filtering
- **Publisher:** Baymard Institute
- **Published/updated:** 2024-08-22; updated 2025-09-09
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard’s product-list research found that showing variants as separate items cluttered the list and made both the range of distinct products and particular variants harder to find. It recommends combining variants within one list item with clear variant access.
- **Interpretation:** Group variants when they are meaningfully one product, while keeping availability and selection understandable; do not force needless detail-page visits to discover alternatives.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; product listings
- **Generalizability:** low — e-commerce-specific product/variant semantics; grouping unrelated records in other apps could hide meaningful differences.
- **Conflicts/tensions:** F-NB-33: a commerce card-list recommendation does not override workplace-table comparison requirements.
- **Candidate knowledge targets:** product lists; variants; list density; comparison

### F-NB-66: Expose main product categories directly in a mobile commerce menu

- **Source:** Make Product Categories the Top-Level Navigation Items on Mobile Sites (33% Don’t) — https://baymard.com/research-articles/main-navigation-product-categories
- **Publisher:** Baymard Institute
- **Published/updated:** 2023-01-24
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed participants abandoning category navigation when core categories were hidden under a generic ‘Shop’, ‘Products’, or ‘Departments’ item among other options. It recommends making the categories the menu’s first level and styling secondary utility paths distinctly.
- **Interpretation:** On a shopping site, make the path into the catalog evident as soon as the menu opens; for other apps, prioritize their actual core tasks rather than copying retail categories.
- **Applies to:** mobile; touch; commerce main navigation
- **Generalizability:** low — e-commerce-specific catalog-finding tasks; a mixed-purpose SaaS or corporate site may have a different primary hierarchy.
- **Conflicts/tensions:** F-NB-15: a small set of tabs and a broad retail taxonomy solve different navigation problems.
- **Candidate knowledge targets:** mobile navigation; category hierarchy; utility separation

### F-NB-67: Provide explicit access to the broad category at each mobile menu level

- **Source:** Have a “View All” Option in the Main Navigation at Each Level of the Mobile Product Catalog (Only 24% Get It Right) — https://baymard.com/research-articles/mobile-main-nav-view-all
- **Publisher:** Baymard Institute
- **Published/updated:** 2022-11-16
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard found users often missed broad product lists when access depended on tapping a category header that looked informational or on distinguishing subtle hit areas. Explicit ‘View All’ wording made the broader scope more discoverable in mobile category navigation.
- **Interpretation:** Distinguish expanding a hierarchy from opening the full set at that level, with clear labels and separate usable controls where needed.
- **Applies to:** mobile; touch; hierarchical commerce menus
- **Generalizability:** medium — e-commerce-specific evidence; likely general to hierarchical browsers that need both drill-down and broad views.
- **Conflicts/tensions:** F-NB-31: the mobile solution cannot depend on the desktop hover cue that exposes an extra action.
- **Candidate knowledge targets:** View All; category drill-down; broad-scope navigation

### F-NB-68: Show representative breadth rather than a narrow promotion-only homepage

- **Source:** 42% of Mobile Homepages Risk Setting Wrong Expectations for Their Users — https://baymard.com/research-articles/mobile-homepage-usability
- **Publisher:** Baymard Institute
- **Published/updated:** 2016-02-17
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard observed new or moderately familiar mobile visitors inferring the catalog’s scope from homepage content. Narrow or unrepresentative content caused false assumptions about what the store carried, later finding problems, and some abandonments.
- **Interpretation:** Use representative category entry points alongside promotions. In noncommerce apps, test whether the first view communicates the actual range of supported tasks.
- **Applies to:** mobile; touch; e-commerce homepages
- **Generalizability:** medium — e-commerce-specific evidence; orientation through representative content is likely general, while merchandising choices are not.
- **Conflicts/tensions:** F-NB-08: visual simplicity should not erase information needed to understand the product’s scope.
- **Candidate knowledge targets:** homepage; category navigation; first-use orientation; trust

### F-NB-69: Keep password requirements and entered-value verification available

- **Source:** Accounts & Self-Service UX Research Update and Expansion: 3 Key Takeaways — https://baymard.com/research-articles/accounts-and-self-service-ux-research-2026
- **Publisher:** Baymard Institute
- **Published/updated:** 2026-09-09
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard’s public 2026 account-research summary describes users struggling when password rules appeared only after submission and password masking prevented verification, including during password reset. Its observations concern commerce account management and sign-in.
- **Interpretation:** Disclose necessary requirements before entry and offer a deliberate way to inspect the value; evaluate credential entry with password managers and the product’s actual security requirements.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; commerce authentication and account updates
- **Generalizability:** medium — likely general entry/recovery mechanisms; this public summary does not establish a secure universal password policy.
- **Conflicts/tensions:** F-NB-59 explicitly distinguishes persistent account edits from checkout entry; no claim here endorses weakening authentication.
- **Candidate knowledge targets:** password fields; show password; requirements; account recovery

### F-NB-70: Use filters for combinable attributes instead of mutually exclusive category branches

- **Source:** Homepage and Category Navigation UX 2026: 10 Pitfalls and Best Practices (64% of Sites Have Mediocre-to-Poor Performance) — https://baymard.com/research-articles/ecommerce-navigation-best-practice
- **Publisher:** Baymard Institute
- **Published/updated:** 2024-08-06; updated 2026-10-13
- **Accessed:** 2026-11-08
- **Evidence class:** E2
- **Finding:** Baymard’s 2026 navigation article describes users failing to combine shared attributes when each led to a separate product category. It recommends implementing overlapping product-type attributes as filters so people can explore one broad list and combine the criteria they need.
- **Interpretation:** Separate stable conceptual categories from orthogonal refinements; test whether real tasks require combining attributes that the navigation currently separates.
- **Applies to:** mobile / desktop; touch / pointer / keyboard; e-commerce taxonomy
- **Generalizability:** medium — e-commerce-specific evidence; likely general where attributes are independent, but not every hierarchy can be replaced by facets.
- **Conflicts/tensions:** F-NB-16: discover user groupings first; F-NB-62 requires logic that matches the domain rather than blanket AND/OR assumptions.
- **Candidate knowledge targets:** information architecture; overcategorization; facets; category hierarchy

## Additional pages fetched and read

The findings cite 64 distinct original pages. These four additional successful fetches bring the total to **68 distinct pages: 42 NN/g and 26 Baymard**. Repeated opens and search-result appearances are not counted as additional pages.

- 10 Usability Heuristics for User Interface Design — https://www.nngroup.com/articles/ten-usability-heuristics/ (published/updated: 1994-04-24; last reviewed 2024-01-30; accessed 2026-11-08).
- 8 Recommendations for Creating Effective Input Fields — https://baymard.com/blog/input-fields (published/updated: 2021-12-06; updated 2025-01-17; accessed 2026-11-08).
- The State of Mobile E-Commerce Search and Category Navigation — https://baymard.com/research-articles/mobile-ecommerce-search-and-navigation (published/updated: 2015-11-17; accessed 2026-11-08).
- Drop-Down Mobile UX: Never Use Native Drop-Downs for Navigation — https://baymard.com/research-articles/mobile-dropdown-navigation (published/updated: 2013-04-23; accessed 2026-11-08).

The NN/g index established the ten-heuristic framework and linked to each explanation, all fetched. Baymard’s input-field synthesis reinforced the form themes. Its 2015 mobile product-finding article supplied historical context; the more recent public topic articles supplied the actionable findings. The native-select navigation article reported constrained overview and mistaken filtering expectations on 2013 mobile interfaces; its particular operating-system geometry is too dated to promote into a current universal rule.

## Coverage and gaps

- **Coverage:** 70 findings, including all ten heuristics; mobile constraints and desktop adaptation; touch targets; menus and tabs; IA/card sorting; cognitive load/disclosure; labels, field effort, validation and error recovery; keyboards, autofill and addresses; search/autocomplete, filtering and sorting; product lists; empty/loading states; response times; undo/confirmation; hover/tooltips; shortcuts; workplace tables; scrolling/pagination; sticky headers; gestures; accordions; breadcrumbs; modals/toasts; onboarding; and deceptive patterns/trust. Forms, navigation, context preservation, and feedback receive the most depth.
- **Fetch failure:** 1 distinct page, https://baymard.com/labs/touch-keyboard-types — web fetch returned “(400) Timeout fetching”. It supplies no cited finding or implementation recipe. The public touch-keyboard research article did load and supports F-NB-54–55.
- **Access limits:** Baymard’s mobile overview and research articles link to Premium for full guidelines. This file records only their accessible summaries, reported observations, and public recommendations. No account, subscription, alternate mirror, or paywall bypass was used. The separate NN/g paid mobile report was not fetched or treated as read.
- **Research limits:** the sources do not establish PWA-specific results for installability, offline synchronization, service-worker lifecycle, push permission prompts, or background delivery. Native tutorial, gesture, and tab examples are labeled as such; transferring them to a PWA is an interpretation. Tablet, hybrid-device, international-address, and assistive-technology coverage is less direct than smartphone/desktop coverage. No normative accessibility audit is implied.
- **Unverified details:** sorting is covered through its relationship to filtering and list management, without a dedicated experiment comparing mobile sort-control designs. List truncation evidence does not settle text ellipsis. No universal bottom-tab count, sticky-bar height, spinner/skeleton winner, mobile table transformation, toast lifetime, or authentication policy follows from these sources.
- **Dates and denominators:** old research is retained with dates and contextual qualifications. Baymard’s inline-validation page says 31% lack validation in the title/key takeaways but 32% in the body; neither prevalence figure is promoted into a finding. The 2023 category-navigation article’s 33% and the 2026 overview’s 22% concern different dated benchmarks; likewise applied-filter prevalence varies across articles. They must not be combined into an undated statistic.

## Disagreements

1. **Positive validation — direct disagreement:** F-NB-22 ([NN/g](https://www.nngroup.com/articles/errors-forms-design-guidelines/)) reserves success indicators for useful additional context and cautions against noise on trivial fields. F-NB-52 ([Baymard](https://baymard.com/research-articles/inline-form-validation)) recommends positive validation for all fields and reports confidence/progress benefits. Preserve both positions; test reassurance, distraction, and announcement behavior in the actual form.
2. **Mobile filtering — contextual tension:** F-NB-26 ([NN/g tray article](https://www.nngroup.com/articles/mobile-faceted-search/)) favors simultaneous visibility and immediate feedback. F-NB-60 ([Baymard’s public synthesis](https://baymard.com/blog/ecommerce-filter-ui)) recommends a deliberate mobile Apply action. F-NB-25 ([NN/g filter timing](https://www.nngroup.com/articles/applying-filters/)) qualifies the choice by multi-selection intent, latency, and stable page position. These differ in pattern, date, and evidence strength; neither ‘always live’ nor ‘always Apply’ is established for every web app.
3. **Required/optional marking — strength and chronology differ:** F-NB-20 ([NN/g, 2019](https://www.nngroup.com/articles/required-fields/)) insists on marking required fields and says optional marking is beneficial but not obligatory; F-NB-49 ([Baymard](https://baymard.com/research-articles/required-optional-form-fields)) strongly recommends marking both in long checkout/account forms. NN/g’s [2016 form overview](https://www.nngroup.com/articles/web-form-design/) is less explicit and emphasizes labeling optional fields. Baymard expressly limits the strongest claim for short familiar forms.
4. **Disclosure versus overview — different task costs:** F-NB-17 supports deferring genuinely secondary material, while F-NB-13 and F-NB-37 warn that hiding destinations or commonly needed sections raises cost. F-NB-63 supports truncation only with discoverable expansion. The resolution depends on what users need to inspect together, not on a blanket preference for fewer visible elements.
5. **Address disclosure — apparent conflict:** F-NB-57 ([lookup](https://baymard.com/research-articles/automatic-address-lookup)) keeps conventional address fields visible for fallback and autofill; F-NB-58 ([secondary address](https://baymard.com/research-articles/address-line-2)) hides a seldom-needed optional line. Treat the core address and optional secondary information separately, and test populated values and local address needs.
6. **Apply buttons — different commitment boundaries:** F-NB-59 discourages redundant Apply steps inside ordinary checkout fields, but explicitly treats account editing differently; F-NB-60 supports Apply for a mobile multi-filter selection. These are different tasks and should not be merged into a universal autosave or explicit-save rule.
7. **Touch sizing — measurement mismatch, not proven empirical contradiction:** F-NB-12 uses NN/g’s physical 1 cm target recommendation. Baymard’s filter-UI synthesis cites a 44 × 44 point platform recommendation. Centimetres, platform points, and CSS pixels are not interchangeable universal thresholds. Neither article is a formal accessibility standard, and the platform document itself was not fetched.
8. **Tutorials and mobile/desktop transfer — scope matters:** F-NB-41’s experiment concerns introductory cards in relatively simple native iPhone apps; it does not disprove contextual help, necessary setup, or specialist training. F-NB-14 rejects unchanged cross-platform layouts, while F-NB-04 supports consistent meanings. Consistency and adaptation can coexist; identical chrome is not the required outcome.

