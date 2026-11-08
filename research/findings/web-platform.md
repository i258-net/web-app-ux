# Web-platform research findings

Assignment: WP. Scope: responsive web applications and PWAs across mobile, tablet, and desktop. Access date: 2026-11-08. This is research working material, not authoritative guidance.

80 findings: 9 E1 specification findings, 54 E3 platform-documentation findings, and 17 E4 practitioner/tutorial recommendations. No E2 empirical-study claims or E5 product observations are made. E1 describes normative text in the cited version, including draft status; it does not establish implementation availability. Compatibility statements are dated snapshots from MDN explicit text or its browser-compat-data, not inferred from a specification or an older web.dev tutorial.

## A — Responsive design and input

### F-WP-01: Responsive design adapts to user constraints, beyond phone layouts

- **Source:** Introduction | web.dev — <https://web.dev/learn/design/intro>; Welcome to Learn Responsive Design! | web.dev — <https://web.dev/learn/design/welcome>
- **Publisher:** Google (web.dev)
- **Published/updated:** source 1: 2021-11-03; source 2: 2021-10-14
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — course framing and design recommendation, without a described comparative study.
- **Finding:** The course describes responsive design as adapting to different devices and user needs, including dimensions, languages, preferences, and interaction mechanisms.
- **Interpretation:** Begin with a usable narrow layout, then improve use of available space and capabilities; retain desktop and keyboard workflows.
- **Applies to:** all platforms; touch, pointer, keyboard, AT; general responsive apps
- **Generalizability:** high — these constraints affect web applications across device categories.
- **Conflicts/tensions:** Mobile-first can become mobile-only if wide-window tasks and non-touch input are omitted.
- **Candidate knowledge targets:** Responsive foundations; mobile-first scope

### F-WP-02: Choose breakpoints when content needs a layout change

- **Source:** Media queries | web.dev — <https://web.dev/learn/design/media-queries>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2025-08-23
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — tutorial recommendation about breakpoint selection.
- **Finding:** Media queries can respond to viewport dimensions; the course recommends letting content determine breakpoints rather than using named device sizes. It demonstrates relative units and min-width queries.
- **Interpretation:** Resize until navigation, text, or controls need a different arrangement; do not equate a CSS-pixel width with a particular device.
- **Applies to:** all platforms; all inputs; layout adaptation
- **Generalizability:** high — content constraints are more stable than device model lists.
- **Conflicts/tensions:** A small set of design-system breakpoints may aid consistency but must still fit the actual content.
- **Candidate knowledge targets:** Content-driven breakpoints; responsive evaluation

### F-WP-03: Use intrinsic layouts before multiplying breakpoint rules

- **Source:** Macro layouts | web.dev — <https://web.dev/learn/design/macro-layouts>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-11-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — layout tutorial and implementation advice.
- **Finding:** Grid and Flexbox can distribute available space and wrap content intrinsically; the course combines flexible layouts with media queries for larger structural changes. It starts from a simple source order.
- **Interpretation:** Prefer layouts that naturally fit their container; check that the single-column DOM order remains meaningful when columns are added.
- **Applies to:** all platforms; all inputs; page-level layout
- **Generalizability:** high — intrinsic layout works across diverse viewport sizes.
- **Conflicts/tensions:** Visual rearrangement can conflict with reading and keyboard order (F-WP-15).
- **Candidate knowledge targets:** Intrinsic layout; DOM order; macro layout

### F-WP-04: Use container queries for components and media queries for viewport or user conditions

- **Source:** CSS container queries - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries>; Micro layouts | web.dev — <https://web.dev/learn/design/micro-layouts>
- **Publisher:** MDN Web Docs contributors; Google (web.dev)
- **Published/updated:** source 1: Jul 8, 2026; source 2: 2021-11-03
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents container-query selection and containment behavior.
- **Finding:** Size container queries style descendants according to an eligible ancestor container, rather than the viewport. An inline-size query container can be established with container-type: inline-size; names can select a particular container. Media queries address viewport and user/device conditions.
- **Interpretation:** Use container queries when the same card can appear in a sidebar and main region at the same viewport width; use media queries for page-wide structure, color preference, reduced motion, and input capabilities.
- **Applies to:** all platforms; all inputs; reusable components
- **Generalizability:** high — component space and viewport space are distinct constraints.
- **Conflicts/tensions:** Containment and eligible-ancestor selection need deliberate setup; a component cannot simply query its own size to style itself.
- **Candidate knowledge targets:** Container versus media queries; component responsiveness

### F-WP-05: Internationalization requires document direction and logical layout

- **Source:** Internationalization | web.dev — <https://web.dev/learn/design/internationalization>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-11-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — course recommendations with CSS/HTML examples.
- **Finding:** The module describes setting language with lang, direction with dir, and using logical properties such as margin-inline-start instead of assuming left-to-right physical directions. Some scripts use vertical writing.
- **Interpretation:** Test RTL and alternate writing directions with real content; align navigation and spacing with reading direction rather than hard-coded left/right rules.
- **Applies to:** all platforms; all inputs; multilingual applications
- **Generalizability:** high — language direction is independent of device size.
- **Conflicts/tensions:** Directional icons and domain-specific diagrams may require meaning-aware treatment, rather than automatic mirroring.
- **Candidate knowledge targets:** Internationalization; logical properties; directionality

### F-WP-06: Allow translated text and scripts to change component dimensions

- **Source:** Internationalization | web.dev — <https://web.dev/learn/design/internationalization>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-11-03
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — practical localization guidance, not measured expansion ratios.
- **Finding:** Languages vary in word length, writing conventions, font coverage, and space needed for marks above or below characters. Text embedded in images is harder to translate.
- **Interpretation:** Avoid fixed-height text containers and string-length assumptions; test long labels, diacritics, font fallbacks, and localized imagery.
- **Applies to:** all platforms; all inputs; localized labels and content
- **Generalizability:** high — fixed assumptions about English text commonly fail across scripts.
- **Conflicts/tensions:** Compact controls and fixed grids compete with translation space; no universal expansion percentage is established here.
- **Candidate knowledge targets:** Localization resilience; text overflow; font coverage

### F-WP-07: Bound fluid typography and retain a relative-size contribution

- **Source:** Typography | web.dev — <https://web.dev/learn/design/typography>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-09
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — typography tutorial offering a fluid-type technique.
- **Finding:** The module combines viewport-relative font sizing with relative units and uses clamp() to set minimum, preferred, and maximum values. Pure viewport sizing can produce unsuitable extremes.
- **Interpretation:** Use a bounded expression with a rem contribution, such as clamp(1rem, .75rem + 1.5vw, 2rem), then test browser zoom and text enlargement. This expression is an implementation starting point, not an accessibility guarantee.
- **Applies to:** all platforms; all inputs; fluid typography
- **Generalizability:** high — type must remain usable across width and user settings.
- **Conflicts/tensions:** Large viewport terms can dampen the effect of zoom; minimum/maximum limits require testing.
- **Candidate knowledge targets:** Fluid type; clamp; zoom resilience

### F-WP-08: Constrain reading measure without suppressing text enlargement

- **Source:** Typography | web.dev — <https://web.dev/learn/design/typography>; Accessibility | web.dev — <https://web.dev/learn/design/accessibility>
- **Publisher:** Google (web.dev)
- **Published/updated:** source 1: 2021-12-09; source 2: 2021-12-23
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — course advice about readable typography and accommodating user needs.
- **Finding:** The typography module recommends managing line length and line height; the accessibility module emphasizes respecting users who need larger text or zoom. The ch unit measures the advance width of the zero glyph, not an exact count of arbitrary characters.
- **Interpretation:** Use a comfortable maximum text measure, scalable spacing, and wrapping containers; test enlargement instead of fixing a precise character count as a universal rule.
- **Applies to:** all platforms; keyboard, pointer, touch, AT; reading and forms
- **Generalizability:** high — readable text and enlargement matter at every viewport size.
- **Conflicts/tensions:** A visually balanced heading at one width may overflow after localization or zoom.
- **Candidate knowledge targets:** Reading measure; typography; text resizing

### F-WP-09: Reserve image space and let images shrink within their container

- **Source:** Responsive images | web.dev — <https://web.dev/learn/design/responsive-images>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-09
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform guidance explains image sizing and layout-shift prevention.
- **Finding:** The module recommends intrinsic width and height attributes so a browser can reserve aspect-ratio space, and responsive CSS such as max-inline-size: 100% with automatic block size.
- **Interpretation:** Prevent image-driven layout shifts and accidental page-wide overflow while preserving aspect ratio.
- **Applies to:** all platforms; all inputs; raster images and content feeds
- **Generalizability:** high — stable image geometry benefits most responsive pages.
- **Conflicts/tensions:** Art-directed crops may need breakpoint-specific aspect-ratio treatment rather than one fixed ratio.
- **Candidate knowledge targets:** Image dimensions; CLS; responsive media

### F-WP-10: Let the browser choose image resources with srcset and accurate sizes

- **Source:** Responsive images | web.dev — <https://web.dev/learn/design/responsive-images>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-09
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — documents browser resource-selection inputs.
- **Finding:** srcset provides image candidates using density or width descriptors. For width candidates, sizes describes the expected rendered width; selection can consider factors beyond viewport width, including pixel density.
- **Interpretation:** Supply real layout sizes rather than downloading a desktop image to every phone; avoid assuming one resource is guaranteed for a named device.
- **Applies to:** all platforms; all inputs; image delivery
- **Generalizability:** high — resource selection must accommodate density and layout variation.
- **Conflicts/tensions:** Incorrect sizes can waste bytes or reduce sharpness; CSS resizing alone does not reduce transferred image size.
- **Candidate knowledge targets:** Responsive images; srcset; sizes; bandwidth

### F-WP-11: Use picture for deliberate art direction and format alternatives

- **Source:** The picture element | web.dev — <https://web.dev/learn/design/picture-element>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2026-07-16
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform tutorial explains picture/source selection semantics.
- **Finding:** The picture element can offer source alternatives by media conditions and type, allowing different crops or formats. Its img remains the required fallback and carries the alternative text.
- **Interpretation:** Change a crop when the subject becomes unreadable in a narrow slot, while keeping equivalent meaning and useful fallback content.
- **Applies to:** all platforms; all inputs including AT; art-directed images
- **Generalizability:** high — source selection is broadly useful, although cropping choices depend on content.
- **Conflicts/tensions:** A different crop must not remove information that surrounding text assumes is visible.
- **Candidate knowledge targets:** Art direction; image fallback; alternative text

### F-WP-12: Lazy-load offscreen images while protecting the critical image

- **Source:** Responsive images | web.dev — <https://web.dev/learn/design/responsive-images>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-09
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform loading and fetch-priority guidance.
- **Finding:** The module covers loading="lazy" for images outside the initial viewport and warns against lazy-loading the main hero image; fetchpriority="high" can prioritize a critical image and should be used sparingly.
- **Interpretation:** Reduce unnecessary early transfer while making the likely LCP image discoverable and promptly fetched.
- **Applies to:** all platforms; all inputs; image-heavy pages
- **Generalizability:** high — critical-path loading affects most pages with images.
- **Conflicts/tensions:** Blanket lazy loading can worsen LCP; making every asset high priority defeats prioritization.
- **Candidate knowledge targets:** Image loading; LCP; resource priority

### F-WP-13: Scalable icons still need clear meaning and accessible names

- **Source:** Icons | web.dev — <https://web.dev/learn/design/icons>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-09
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — icon-format and labeling recommendations without a usability study.
- **Finding:** The module favors scalable vector icons and discusses visible text labels, accessible names for icon-only controls, and hiding decorative icons from assistive technology.
- **Interpretation:** Use familiar icons with labels for important actions; expose one meaningful name instead of making AT announce redundant icon decoration.
- **Applies to:** all platforms; touch, pointer, keyboard, AT; controls and navigation
- **Generalizability:** high — resolution independence does not solve recognition or naming.
- **Conflicts/tensions:** Minimal chrome and icon-only toolbars can conflict with discoverability and localization.
- **Candidate knowledge targets:** Icons; accessible naming; action clarity

### F-WP-14: Respond to color preference and theme native controls coherently

- **Source:** Theming | web.dev — <https://web.dev/learn/design/theming>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-09
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — documents prefers-color-scheme and color-scheme behavior.
- **Finding:** prefers-color-scheme selects styles according to a user preference for light or dark presentation. color-scheme advertises supported schemes so browser-rendered controls can adapt.
- **Interpretation:** Define readable color tokens and test both content and built-in controls; offer an explicit preference when product needs justify it.
- **Applies to:** all platforms; all inputs; themes and forms
- **Generalizability:** high — user preferences cut across viewport sizes.
- **Conflicts/tensions:** A dark background alone does not ensure contrast, legible imagery, or coherent form controls.
- **Candidate knowledge targets:** Theming; color preferences; native controls

### F-WP-15: Responsive rearrangement must preserve semantic and focus order

- **Source:** Accessibility | web.dev — <https://web.dev/learn/design/accessibility>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-23
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — course accessibility recommendations, not a normative WCAG audit.
- **Finding:** The module stresses semantic HTML, keyboard access, useful labels, and a source order that remains understandable when layout changes. Visual CSS reordering does not automatically change the document reading order.
- **Interpretation:** Evaluate wide and narrow layouts with keyboard and AT as well as visually; keep meaningful focus visibility and do not disable zoom to make a layout fit.
- **Applies to:** all platforms; keyboard, AT, touch, pointer; responsive interfaces
- **Generalizability:** high — modality and reading order remain relevant at every breakpoint.
- **Conflicts/tensions:** Visual density improvements may create a confusing tab sequence if DOM order is ignored.
- **Candidate knowledge targets:** Semantic structure; focus order; zoom

### F-WP-16: Viewport width cannot determine input modality

- **Source:** Interaction | web.dev — <https://web.dev/learn/design/interaction>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-23
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform guidance explicitly distinguishes screen size and input capabilities.
- **Finding:** The course describes devices with multiple input mechanisms, including touchscreens with keyboards or mice. A wide display can accept touch, and a narrow browser window can be used with a mouse.
- **Interpretation:** Never use a mobile-width breakpoint as a test for touch or a desktop-width breakpoint as proof of hover; support switching inputs without losing core actions.
- **Applies to:** all platforms; touch, mouse, pen, keyboard; hybrid devices
- **Generalizability:** high — window dimensions and available hardware are independent.
- **Conflicts/tensions:** Density decisions tied to width can make touchscreen laptops unusable.
- **Candidate knowledge targets:** Input-modality independence; hybrid-device evaluation

### F-WP-17: pointer reports the primary pointing device accuracy, not the current action

- **Source:** Media Queries Level 4 — <https://www.w3.org/TR/mediaqueries-4/>
- **Publisher:** World Wide Web Consortium (W3C)
- **Published/updated:** 2026-02-19 (Candidate Recommendation Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E1 — normative media-feature definitions in a Candidate Recommendation Draft.
- **Finding:** pointer has none, coarse, and fine values for the UA-selected primary pointing device. coarse means limited accuracy, fine means accurate pointing, and none means no primary pointing device. The UA can report a less capable value for accessibility; zoom does not change the feature. These features do not detect keyboard availability.
- **Interpretation:** Use @media (pointer: coarse) to provide a coarse-primary adaptation; retain usable controls for other inputs and avoid treating the result as a touch-event detector or a measure of the user’s skill.
- **Applies to:** all platforms; pointing devices; adaptive controls
- **Generalizability:** high — standardized capability semantics, with UA discretion.
- **Conflicts/tensions:** A fine primary pointer does not exclude a secondary touchscreen (F-WP-19).
- **Candidate knowledge targets:** Pointer media query; coarse targets; capability detection

### F-WP-18: hover means convenient hover on the primary pointer

- **Source:** Media Queries Level 4 — <https://www.w3.org/TR/mediaqueries-4/>
- **Publisher:** World Wide Web Consortium (W3C)
- **Published/updated:** 2026-02-19 (Candidate Recommendation Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E1 — normative hover media-feature definition in a Candidate Recommendation Draft.
- **Finding:** hover: hover means the primary pointing device can conveniently hover; hover: none includes no pointer or a pointer that cannot conveniently hover. Long-press hover emulation may still count as none. hover: none does not guarantee that the CSS :hover pseudo-class never matches.
- **Interpretation:** Treat hover as an optional enhancement; do not infer that touch-triggered hover states cannot occur or use hover as the only way to reveal an essential action.
- **Applies to:** all platforms; primary pointing device; hover interactions
- **Generalizability:** high — capability definition applies across device categories.
- **Conflicts/tensions:** A touchscreen laptop may have a hover-capable primary mouse while touch remains available.
- **Candidate knowledge targets:** Hover capability; essential-action access

### F-WP-19: any-pointer is a union and can match coarse and fine together

- **Source:** Media Queries Level 4 — <https://www.w3.org/TR/mediaqueries-4/>
- **Publisher:** World Wide Web Consortium (W3C)
- **Published/updated:** 2026-02-19 (Candidate Recommendation Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E1 — normative aggregate pointer semantics in a Candidate Recommendation Draft.
- **Finding:** any-pointer describes all available pointing devices. Both any-pointer: coarse and any-pointer: fine can match when different devices are available; none matches only when there are no pointing devices. It is not a report of the device currently being used.
- **Interpretation:** Use any-pointer: coarse when a touch-friendly adaptation should remain available alongside a mouse; design simultaneous matches deliberately rather than as mutually exclusive modes.
- **Applies to:** all platforms; multiple pointers; hybrid-device controls
- **Generalizability:** high — essential distinction for mixed-input hardware.
- **Conflicts/tensions:** any-pointer cannot establish keyboard presence, current touch use, or a need to hide mouse functions.
- **Candidate knowledge targets:** Aggregate input capability; mixed pointers

### F-WP-20: any-hover cannot reveal every non-hover input when another device can hover

- **Source:** Media Queries Level 4 — <https://www.w3.org/TR/mediaqueries-4/>
- **Publisher:** World Wide Web Consortium (W3C)
- **Published/updated:** 2026-02-19 (Candidate Recommendation Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E1 — normative aggregate hover semantics and limitations in a Candidate Recommendation Draft.
- **Finding:** any-hover: hover matches if any available pointing device can conveniently hover. any-hover: none means none can hover; it does not mean that at least one device lacks hover. A mouse plus a non-hover touchscreen therefore matches hover.
- **Interpretation:** Even a positive any-hover result is insufficient justification for hover-only functionality; a user may choose the touchscreen at any moment.
- **Applies to:** all platforms; multiple pointers; touchscreen laptops and tablets with mice
- **Generalizability:** high — aggregate capability necessarily loses information about non-hover devices.
- **Conflicts/tensions:** The convenient enhancement for a mouse must coexist with click, tap, and keyboard access.
- **Candidate knowledge targets:** Any-hover limitation; modality-safe enhancement

### F-WP-21: Make hover enhancements optional and targets usable with coarse input

- **Source:** Interaction | web.dev — <https://web.dev/learn/design/interaction>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-23
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — interaction design recommendations from a tutorial.
- **Finding:** The module recommends adequately sized targets and alternatives to hover-dependent interactions, adapting to pointer accuracy rather than assuming input from screen size.
- **Interpretation:** Keep critical information and actions reachable by tap, click, and focus/activation; allow larger targets to benefit users even when a fine pointer is available.
- **Applies to:** all platforms; touch, pen, mouse, keyboard, AT; menus and actions
- **Generalizability:** high — core operation should survive changes in input.
- **Conflicts/tensions:** Smaller fine-pointer targets may improve density but must not erase a coarse-input path.
- **Candidate knowledge targets:** Target usability; hover alternatives; progressive enhancement

### F-WP-22: Reduced motion is a request to reduce nonessential movement

- **Source:** prefers-reduced-motion CSS media feature - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Jun 10, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents the preference and accessibility-oriented use.
- **Finding:** prefers-reduced-motion: reduce reflects a user preference to minimize nonessential motion. Large panning and scaling animations can trigger discomfort; the page shows replacing or reducing such effects.
- **Interpretation:** Honor the preference in transitions, parallax, loading shimmer, and autoanimation; preserve status feedback with static or restrained alternatives.
- **Applies to:** all platforms; all inputs; animation and status feedback
- **Generalizability:** high — the preference is independent of device size and task.
- **Conflicts/tensions:** Removing all feedback can harm clarity; reducing motion need not remove information.
- **Candidate knowledge targets:** Reduced motion; vestibular accessibility; animation

### F-WP-23: Reduced-data preference is not a network-speed measurement

- **Source:** Media Queries Level 5 — <https://www.w3.org/TR/mediaqueries-5/>
- **Publisher:** World Wide Web Consortium (W3C)
- **Published/updated:** 2026-02-19 (Working Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E1 — normative preference semantics in a Working Draft; implementation availability is separate.
- **Finding:** prefers-reduced-data distinguishes no-preference from reduce, which indicates a preference for reduced data use. It concerns desired consumption, rather than an estimate of current connection speed.
- **Interpretation:** Offer lighter imagery or optional media when the preference is available, and keep the baseline economical regardless of whether a signal is exposed.
- **Applies to:** all platforms; all inputs; data-sensitive delivery
- **Generalizability:** medium — proposed semantics are clear but support is limited (F-WP-24).
- **Conflicts/tensions:** A draft media feature must not be treated as a universally deployed capability.
- **Candidate knowledge targets:** Data preferences; progressive delivery

### F-WP-24: prefers-reduced-data is not a dependable cross-browser production signal

- **Source:** prefers-reduced-data CSS media feature - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-data>; MDN browser-compat-data: css/at-rules/media.json — <https://raw.githubusercontent.com/mdn/browser-compat-data/main/css/at-rules/media.json>
- **Publisher:** MDN Web Docs contributors; MDN browser-compat-data contributors
- **Published/updated:** source 1: Jun 16, 2026; source 2: not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN explicit support warning and its browser-compat-data, checked on 2026-11-08.
- **Finding:** The fetched MDN page says this feature is not supported by any user agent. Its compatibility data lists Chromium support behind a flag and Firefox/Safari as unsupported; this does not establish default-on interoperable support.
- **Interpretation:** Use conservative defaults and an explicit lower-data option; do not require this query to protect users with data constraints.
- **Applies to:** all platforms; all inputs; progressive enhancement
- **Generalizability:** medium — compatibility is a dated snapshot, not a permanent product rule.
- **Conflicts/tensions:** The responsive course presents the concept; availability must be checked separately from specification semantics.
- **Candidate knowledge targets:** Compatibility caveat; lower-data mode

### F-WP-25: Viewport segments describe exposed screen regions, not a device category

- **Source:** horizontal-viewport-segments CSS media feature - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/horizontal-viewport-segments>; env() CSS function - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/env>; Screen configurations | web.dev — <https://web.dev/learn/design/screen-configurations>
- **Publisher:** MDN Web Docs contributors; Google (web.dev)
- **Published/updated:** source 1: Apr 20, 2026; source 2: Oct 8, 2026; source 3: 2021-12-23
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN defines segment queries/environment variables and labels the feature experimental and of limited availability, checked on 2026-11-08.
- **Finding:** horizontal-viewport-segments and its vertical counterpart query the number of segments in a viewport. Indexed env(viewport-segment-*) variables describe region geometry. The MDN reference marks segment queries experimental and limited; one segment does not identify whether hardware is foldable.
- **Interpretation:** Keep a continuous-layout fallback; where supported, place related content within segments and keep controls away from hinges or obscured regions.
- **Applies to:** foldable/segmented viewports; all inputs; adaptive layout
- **Generalizability:** medium — meaningful only when the browser exposes multiple viewport segments.
- **Conflicts/tensions:** The older course describes proposals; current MDN status is more useful than assuming universal availability or permanent nonexistence.
- **Candidate knowledge targets:** Foldables; viewport segments; hinge-safe layout

### F-WP-26: Responsive patterns must retain access to overflow and navigation

- **Source:** User interface patterns | web.dev — <https://web.dev/learn/design/ui-patterns>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2021-12-23
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — pattern examples and recommendations without comparative usability testing.
- **Finding:** The module demonstrates navigation adaptations, responsive tabular content, and horizontally scrollable collections with scroll snapping. Different content structures require different responses to limited space.
- **Interpretation:** Preserve table relationships and make horizontal content discoverable; keep navigation controls operable and identifiable when their presentation changes.
- **Applies to:** all platforms; all inputs; tables, navigation, carousels
- **Generalizability:** high — access requirements generalize, but the best pattern is task-specific.
- **Conflicts/tensions:** Overflow can preserve useful density while concealing content; examples are not proof that a carousel is the best solution.
- **Candidate knowledge targets:** Responsive patterns; overflow discoverability; navigation

## B — PWA architecture, installation, and lifecycle

### F-WP-27: A PWA can be a progressively enhanced multipage website

- **Source:** What is a progressive web app? - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/What_is_a_progressive_web_app>; Foundations | web.dev — <https://web.dev/learn/pwa/foundations>; Getting started | web.dev — <https://web.dev/learn/pwa/getting-started>
- **Publisher:** MDN Web Docs contributors; Google (web.dev)
- **Published/updated:** source 1: Dec 4, 2025; source 2: 2021-11-03; source 3: 2021-11-03
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN platform description and web.dev architecture guidance.
- **Finding:** PWAs use web technologies and progressive enhancement to offer app-like capabilities. The foundations module describes both multipage and single-page architectures; a client-side SPA is not a prerequisite.
- **Interpretation:** Maintain useful URLs, links, and baseline functionality, then add installation, offline behavior, and capabilities when available.
- **Applies to:** all platforms; all inputs; PWA architecture
- **Generalizability:** high — installation model does not dictate routing architecture.
- **Conflicts/tensions:** An app-like appearance can encourage rebuilding browser behavior that ordinary document navigation already supplies.
- **Candidate knowledge targets:** PWA foundations; progressive enhancement; architecture

### F-WP-28: Installation and offline readiness are independent

- **Source:** Making PWAs installable - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Oct 6, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN explicitly distinguishes service workers from installation requirements.
- **Finding:** MDN states that a service worker is not required for installability. Many PWAs use one to provide offline behavior, but installation itself does not establish a usable offline experience.
- **Interpretation:** Evaluate offline launch and task completion separately from the presence of an installed icon; describe exactly what content has been downloaded.
- **Applies to:** all supporting platforms; all inputs; installed/offline apps
- **Generalizability:** high — installation is not evidence of cached functionality.
- **Conflicts/tensions:** PWA marketing often conflates installation with offline guarantees.
- **Candidate knowledge targets:** Installability versus offline; acceptance criteria

### F-WP-29: Choose storage according to assets versus structured data

- **Source:** Assets and data | web.dev — <https://web.dev/learn/pwa/assets-and-data>; Offline data | web.dev — <https://web.dev/learn/pwa/offline-data>
- **Publisher:** Google (web.dev)
- **Published/updated:** source 1: 2021-11-18; source 2: 2022-01-10
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform tutorial describes available storage mechanisms.
- **Finding:** Cache Storage holds request/response pairs; IndexedDB supports structured data used by pages and workers. Web Storage is synchronous and is not the service-worker data store.
- **Interpretation:** Cache the shell and selected responses separately from drafts, records, and pending mutations; use asynchronous storage for substantial app data.
- **Applies to:** all platforms; all inputs; offline data architecture
- **Generalizability:** high — these storage roles apply broadly to web apps.
- **Conflicts/tensions:** Local storage choices do not provide durability against eviction or user deletion (F-WP-36).
- **Candidate knowledge targets:** Cache Storage; IndexedDB; draft persistence

### F-WP-30: Service workers are event-driven and background execution is bounded

- **Source:** Service workers | web.dev — <https://web.dev/learn/pwa/service-workers>; Offline and background operation - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation>
- **Publisher:** Google (web.dev); MDN Web Docs contributors
- **Published/updated:** source 1: 2021-12-03; source 2: Sep 13, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — documented worker lifecycle and background-operation constraints.
- **Finding:** A registered service worker has installation and activation stages; the first page is not normally controlled until a later navigation unless control is claimed. Browsers can stop workers between events, and background sync execution/retries are managed and limited by the browser.
- **Interpretation:** Persist essential state rather than keeping it only in worker memory; show pending work and a foreground retry path instead of promising immediate or unlimited background completion.
- **Applies to:** all platforms exposing the relevant APIs; all inputs; offline/background work
- **Generalizability:** high — worker lifetimes differ from an always-running application process.
- **Conflicts/tensions:** A successful queue write is not equivalent to server acceptance; background API availability must be feature-detected.
- **Candidate knowledge targets:** Service-worker lifecycle; background reliability; pending states

### F-WP-31: Cache-first fits reusable assets whose freshness can be controlled

- **Source:** Caching - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching>; Caching | web.dev — <https://web.dev/learn/pwa/caching>
- **Publisher:** MDN Web Docs contributors; Google (web.dev)
- **Published/updated:** source 1: Jun 12, 2025; source 2: 2021-12-03
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — documented caching strategy behavior and resource examples.
- **Finding:** Cache-first returns a cached response when present and otherwise uses the network, normally caching the result. MDN illustrates it for resources whose cached form remains useful; versioning can make static assets safe to reuse.
- **Interpretation:** Use it for versioned shell assets and stable resources, with explicit expiration or replacement policy for mutable content.
- **Applies to:** all platforms with service-worker caching; all inputs; asset delivery
- **Generalizability:** high — strategy semantics are general; suitability depends on freshness needs.
- **Conflicts/tensions:** Low latency can conceal stale mutable data indefinitely without invalidation.
- **Candidate knowledge targets:** Cache-first; asset versioning; freshness policy

### F-WP-32: Network-first prioritizes freshness and provides a cached fallback

- **Source:** Caching - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching>; Caching | web.dev — <https://web.dev/learn/pwa/caching>
- **Publisher:** MDN Web Docs contributors; Google (web.dev)
- **Published/updated:** source 1: Jun 12, 2025; source 2: 2021-12-03
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — documented network-first strategy semantics.
- **Finding:** Network-first attempts the network, updates the cache when successful, and uses a cached response when the network fails. It fits resources for which up-to-date content is preferred while an older copy remains useful offline.
- **Interpretation:** Use it for changeable content with a clearly labeled stale fallback; decide timeout and error behavior for slow connections.
- **Applies to:** all platforms with service-worker caching; all inputs; fresh content with offline fallback
- **Generalizability:** high — tradeoff follows from strategy behavior.
- **Conflicts/tensions:** Users can wait on a slow network before seeing useful cached content; strict freshness may require network-only behavior.
- **Candidate knowledge targets:** Network-first; stale-state indication; timeout policy

### F-WP-33: Stale-while-revalidate serves now and refreshes a later request

- **Source:** Caching - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching>; Caching | web.dev — <https://web.dev/learn/pwa/caching>
- **Publisher:** MDN Web Docs contributors; Google (web.dev)
- **Published/updated:** source 1: Jun 12, 2025; source 2: 2021-12-03
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — documented stale-while-revalidate behavior.
- **Finding:** This strategy serves an available cached response immediately while fetching a replacement in the background; the updated cache normally benefits a subsequent request. Without a cached response it needs the network.
- **Interpretation:** Use for content where temporary staleness is acceptable, and communicate or apply updates separately if the current view must change. Do not use an old success response as proof of a new transaction.
- **Applies to:** all platforms with service-worker caching; all inputs; latency-sensitive reusable content
- **Generalizability:** high — response behavior is clear, but freshness tolerance is domain-specific.
- **Conflicts/tensions:** Fast paint and immediate correctness can conflict; automatic cache refresh does not automatically refresh the visible UI.
- **Candidate knowledge targets:** Stale-while-revalidate; cache/UI synchronization

### F-WP-34: Workbox implements strategy machinery rather than product policy

- **Source:** Workbox | web.dev — <https://web.dev/learn/pwa/workbox>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2022-01-10
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform documentation describes the library’s modules.
- **Finding:** Workbox provides modules for precaching, request routing, runtime strategies, expiration, and communication with service workers, reducing repeated service-worker implementation code.
- **Interpretation:** Choose cache rules, offline promises, data boundaries, and update timing explicitly; a library default does not establish the correct UX for a resource.
- **Applies to:** platforms supporting required worker APIs; all inputs; PWA implementation
- **Generalizability:** high — tooling can implement but cannot decide product freshness requirements.
- **Conflicts/tensions:** Precache convenience can increase transfer/storage cost if everything is included.
- **Candidate knowledge targets:** Workbox; cache governance; implementation tools

### F-WP-35: Offline behavior should preserve useful tasks and explain unavailable ones

- **Source:** Offline data | web.dev — <https://web.dev/learn/pwa/offline-data>; Best practices for PWAs - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Best_practices>; App design | web.dev — <https://web.dev/learn/pwa/app-design>
- **Publisher:** Google (web.dev); MDN Web Docs contributors
- **Published/updated:** source 1: 2022-01-10; source 2: Jun 30, 2025; source 3: 2024-09-20
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — documentation’s practical UX recommendations without a described study.
- **Finding:** The sources recommend custom offline experiences, locally useful content, and appropriate handling of offline changes rather than leaving users with a generic browser error page.
- **Interpretation:** State what is available, retain drafts, distinguish saved locally from synced, and expose retry or recovery paths. Validate conflicts when connectivity returns.
- **Applies to:** all platforms; all inputs; intermittent connectivity and offline tasks
- **Generalizability:** high — users need accurate task status regardless of network quality.
- **Conflicts/tensions:** A branded offline screen is a baseline, not evidence that an important task can complete offline.
- **Candidate knowledge targets:** Offline UX; local versus synced status; recovery

### F-WP-36: Browser storage is best effort and Safari can evict inactive script data

- **Source:** Storage quotas and eviction criteria - Web APIs | MDN — <https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Jan 5, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN explicitly documents storage/eviction behavior; compatibility checked on 2026-11-08.
- **Finding:** Storage is best effort by default; persistence can be requested but is not assured, quotas can cause write failures, and users can delete data. MDN describes Safari’s proactive eviction of script-created data after seven days of browser use without user interaction when tracking prevention is enabled; server-set cookies are exempt from that rule.
- **Interpretation:** Handle failed writes, rehydrate safely, and offer server sync or export for valuable work. Do not promise that local drafts or downloaded data are permanent.
- **Applies to:** all platforms; all inputs; client persistence, with the stated Safari rule
- **Generalizability:** high — nondurability is broad; Safari timing is a dated browser-specific detail.
- **Conflicts/tensions:** The fetched text does not establish a blanket exemption for installed iOS Home Screen apps; installation must not be presented as a backup guarantee.
- **Candidate knowledge targets:** Storage durability; Safari eviction; persistence/error recovery

### F-WP-37: Browser promotion criteria are distinct from manual install-any-site

- **Source:** Making PWAs installable - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Oct 6, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — explicit MDN installability and browser-support text, checked on 2026-11-08.
- **Finding:** MDN lists HTTPS or local development via localhost/127.0.0.1. Chromium promotion requires name or short_name, 192px and 512px icons, start_url, display and/or display_override, and prefer_related_applications false or absent. It separately documents browsers allowing manual installation of sites that do not meet manifest criteria.
- **Interpretation:** Provide a complete manifest and secure delivery, but distinguish promotability, a manual browser action, and the resulting experience when writing evaluations.
- **Applies to:** supporting browsers; all inputs; PWA installation
- **Generalizability:** medium — criteria and manual-install support can change by browser.
- **Conflicts/tensions:** Passing a manifest checklist does not establish offline quality or a useful reason to install.
- **Candidate knowledge targets:** Install criteria; manifest validation; installation terminology

### F-WP-38: iOS installation uses platform-specific Share-menu paths

- **Source:** Making PWAs installable - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable>; Installing and uninstalling web apps - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Installing>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** source 1: Oct 6, 2026; source 2: Sep 17, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — explicit MDN iOS support text, checked on 2026-11-08.
- **Finding:** MDN states that iOS 16.3 and earlier support PWA installation only through Safari; on iOS 16.4 and later it lists Safari, Chrome, Edge, Firefox, and Orion via the Share menu. The custom beforeinstallprompt flow is not supported on iOS. The installing/uninstalling guide describes iOS removal through the Home Screen icon and notes that uninstall UI differs across browser/OS combinations.
- **Interpretation:** Use contextual Add to Home Screen instructions when relevant; never display a button that assumes prompt() will work on iOS. Offer relevant removal help without implying that uninstalling an app deletes a server account.
- **Applies to:** iOS; touch and AT; installation guidance
- **Generalizability:** medium — browser/platform integration is a dated compatibility fact.
- **Conflicts/tensions:** A single universal install CTA can promise a flow that the current browser does not provide.
- **Candidate knowledge targets:** iOS installation; platform-specific onboarding

### F-WP-39: Desktop installation differs between Firefox and Safari

- **Source:** Making PWAs installable - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable>; Installing and uninstalling web apps - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Installing>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** source 1: Oct 6, 2026; source 2: Sep 17, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — explicit MDN desktop support text, checked on 2026-11-08.
- **Finding:** MDN says desktop Firefox does not support installing PWAs using a manifest. It says Safari on macOS Sonoma with Safari 17 and later supports Add to Dock for web apps with or without a manifest; Chromium browsers support manifest-based installation on supported desktop OSes. The installing guide describes Firefox extensions as a separate installation route.
- **Interpretation:** Keep the browser experience complete and tailor installation help to capabilities. Lack of manifest-driven installation does not imply Firefox cannot run offline-capable websites.
- **Applies to:** desktop; pointer, keyboard, AT; installation
- **Generalizability:** medium — dated browser integration status rather than a permanent architectural constraint.
- **Conflicts/tensions:** Older web.dev course compatibility passages omit newer Safari installation; prefer current MDN for this comparison.
- **Candidate knowledge targets:** Desktop install compatibility; progressive enhancement

### F-WP-40: Only offer a programmatic install action when its event is available

- **Source:** BeforeInstallPromptEvent - Web APIs | MDN — <https://developer.mozilla.org/en-US/docs/Web/API/BeforeInstallPromptEvent>; MDN browser-compat-data: api/BeforeInstallPromptEvent.json — <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/BeforeInstallPromptEvent.json>; Installation prompt | web.dev — <https://web.dev/learn/pwa/installation-prompt>
- **Publisher:** MDN Web Docs contributors; MDN browser-compat-data contributors; Google (web.dev)
- **Published/updated:** source 1: Oct 25, 2023; source 2: not shown; source 3: 2022-03-09
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN API text/compatibility data plus documented prompt lifecycle, checked on 2026-11-08.
- **Finding:** The nonstandard beforeinstallprompt event can be retained after preventing default behavior and used to invoke prompt() from app UI. A captured event can prompt only once. MDN compatibility data lists Chrome support and no Firefox or Safari support.
- **Interpretation:** Reveal the actionable custom install control only after receiving the event; clear the retained event after use and offer separate manual instructions where appropriate.
- **Applies to:** browsers exposing beforeinstallprompt; all inputs; installation promotion
- **Generalizability:** medium — this is not a universal installation API.
- **Conflicts/tensions:** An install affordance must not remain enabled after its one-use event has been consumed.
- **Candidate knowledge targets:** Custom install UI; capability-gated actions

### F-WP-41: Promote installation after demonstrated value and outside the core task

- **Source:** Patterns for promoting PWA installation | Articles | web.dev — <https://web.dev/articles/promote-install>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2019-06-04
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — practitioner promotion patterns; no controlled conversion study is described.
- **Finding:** The article recommends dismissible, non-disruptive promotions, waiting for interest signals for banners/snackbars, remembering dismissal, and keeping promotions outside primary task flows. It warns that promotion on page load can overwhelm or be missed.
- **Interpretation:** Avoid an automatic custom prompt on first load; invite installation after a meaningful task or return visit, with a clear benefit and a durable dismissal choice.
- **Applies to:** all platforms with suitable install paths; all inputs; onboarding
- **Generalizability:** high — timing principles generalize, while conversion effects require product testing.
- **Conflicts/tensions:** This is guidance, not a universal browser rule forbidding first-visit installation; user-initiated installation should remain available.
- **Candidate knowledge targets:** Install-prompt timing; respectful promotion; task continuity

### F-WP-42: Display modes change which navigation controls users receive

- **Source:** App design | web.dev — <https://web.dev/learn/pwa/app-design>; display - Web app manifest | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display>
- **Publisher:** Google (web.dev); MDN Web Docs contributors
- **Published/updated:** source 1: 2024-09-20; source 2: Aug 8, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — documented display modes and browser UI implications.
- **Finding:** browser presents normal browser UI; minimal-ui retains a minimal set of navigation controls whose details vary; standalone omits standard browser controls such as the URL bar; fullscreen is more immersive. The course warns about the loss of familiar browser navigation in app windows.
- **Interpretation:** Supply discoverable in-app back/home/navigation and ways to share or open relevant URLs. A fresh installed launch may have no previous in-app history, so Back needs a safe fallback.
- **Applies to:** installed and browser web apps; all inputs; navigation chrome
- **Generalizability:** high — missing browser affordances materially affect tasks.
- **Conflicts/tensions:** Standalone polish can conflict with web expectations for back, refresh, URL inspection, and sharing; system back behavior is a separate platform feature.
- **Candidate knowledge targets:** Display-mode UX; app navigation; direct launch

### F-WP-43: The manifest display request has a normative fallback chain

- **Source:** Web Application Manifest — <https://www.w3.org/TR/appmanifest/>
- **Publisher:** World Wide Web Consortium (W3C)
- **Published/updated:** 2026-11-06 (Working Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E1 — normative display-mode processing in the Web Application Manifest Working Draft.
- **Finding:** User agents must support browser display mode. Unsupported display requests fall back through fullscreen, standalone, minimal-ui, and browser as applicable. The specification defines distinct display modes rather than guaranteeing identical OS chrome.
- **Interpretation:** Treat display as a request with fallbacks and test the actual launch result; maintain usable navigation when more or less browser UI is present than expected.
- **Applies to:** manifest-processing user agents; all inputs; installed launch
- **Generalizability:** high — processing rules are formal, but the cited document remains a Working Draft.
- **Conflicts/tensions:** Normative fallback behavior is not evidence that every mode is implemented in every browser.
- **Candidate knowledge targets:** Manifest display fallback; resilient app chrome

### F-WP-44: display_override is an ordered preference list, with a display fallback

- **Source:** display_override - Web app manifest | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display_override>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Nov 13, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN reference explains processing and marks the member experimental, checked on 2026-11-08.
- **Finding:** display_override lists display modes in preferred order; the first supported mode is chosen before the normal display fallback behavior. MDN labels it experimental.
- **Interpretation:** Keep a valid display baseline and avoid assuming that advanced modes such as window-controls-overlay will be honored.
- **Applies to:** supporting installed web apps; all inputs; advanced display modes
- **Generalizability:** medium — optional modes and support vary.
- **Conflicts/tensions:** A custom title-bar layout can fail if it assumes overlay behavior without checking actual mode and geometry.
- **Candidate knowledge targets:** Display override; progressive window enhancement

### F-WP-45: start_url is resolved against the manifest but constrained to the installing document origin

- **Source:** Web Application Manifest — <https://www.w3.org/TR/appmanifest/>; start_url - Web app manifest | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/start_url>
- **Publisher:** World Wide Web Consortium (W3C); MDN Web Docs contributors
- **Published/updated:** source 1: 2026-11-06 (Working Draft); source 2: Aug 31, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E1 — normative start_url processing algorithm in a Working Draft; MDN is supporting documentation.
- **Finding:** The manifest algorithm resolves start_url relative to the manifest URL, requires its origin to match the document URL’s origin, and otherwise falls back to the document URL. User agents can allow user changes to the launch URL.
- **Interpretation:** Choose a durable launch route that handles logged-out, offline, and resumed states; do not rely on a cross-origin manifest location to authorize a cross-origin launch URL.
- **Applies to:** manifest-processing platforms; all inputs; installed entry routes
- **Generalizability:** high — origin/fallback rules are formal; launch policy can still vary.
- **Conflicts/tensions:** MDN’s Description follows the document-origin rule, while its Best practices text says manifest origin; resolve this internal inconsistency using the specification.
- **Candidate knowledge targets:** Start URL; deep launch; origin constraints

### F-WP-46: Manifest scope is a navigation boundary, not a security boundary

- **Source:** scope - Web app manifest | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/scope>; Web Application Manifest — <https://www.w3.org/TR/appmanifest/>
- **Publisher:** MDN Web Docs contributors; World Wide Web Consortium (W3C)
- **Published/updated:** source 1: Jun 23, 2025; source 2: 2026-11-06 (Working Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN reference distinguishes app scope behavior; specification provides supporting processing detail.
- **Finding:** scope determines URLs considered part of the app experience. Out-of-scope navigation remains possible and can expose browser UI or another context. Manifest scope is separate from service-worker registration scope; its URL-path matching is not access control.
- **Interpretation:** Use a deliberate trailing-slash path boundary, test external/authentication links, and enforce authorization on the server rather than through manifest configuration.
- **Applies to:** installed web apps; all inputs; internal/external navigation
- **Generalizability:** high — app identity and security boundaries must be kept separate.
- **Conflicts/tensions:** Cross-origin login or help links can shift users out of the app window; exact presentation is browser-dependent.
- **Candidate knowledge targets:** App scope; external links; authentication handoff

### F-WP-47: Manifest shortcuts are optional routes and may be truncated

- **Source:** shortcuts - Web app manifest | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/shortcuts>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Nov 30, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents shortcut members and presentation limitations.
- **Finding:** shortcuts supply named actions and URLs within app scope for OS launch menus. Ordering expresses priority; the available number and presentation depend on the browser/OS.
- **Interpretation:** Put the most useful tasks first and make each route safe to open directly; retain the same actions inside the application.
- **Applies to:** supporting installed apps; pointer, touch, keyboard, AT; OS quick actions
- **Generalizability:** high — optional OS entry points cannot replace in-app discoverability.
- **Conflicts/tensions:** Users may never see every declared shortcut; direct launch must not depend on a preexisting navigation stack.
- **Candidate knowledge targets:** App shortcuts; deep links; quick actions

### F-WP-48: A newly installed worker normally waits before replacing active clients

- **Source:** Update | web.dev — <https://web.dev/learn/pwa/update>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2022-03-10
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — documented service-worker update lifecycle.
- **Finding:** An updated service worker installs and normally waits while the previous worker controls clients. skipWaiting() can accelerate activation, but risks pairing pages loaded from one version with a worker from another.
- **Interpretation:** Version assets coherently and decide how multiple open windows transition; do not assume a deployment instantly updates every running session.
- **Applies to:** service-worker apps; all inputs; release lifecycle
- **Generalizability:** high — long-running clients are normal on both mobile and desktop.
- **Conflicts/tensions:** Immediate activation can break in-progress work; waiting can leave users on an older version.
- **Candidate knowledge targets:** Worker updates; version coherence; multiple clients

### F-WP-49: Offer an update at a safe point and preserve the user’s work

- **Source:** Update | web.dev — <https://web.dev/learn/pwa/update>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2022-03-10
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — update-notification and reload recommendations from a tutorial.
- **Finding:** The module shows observing updatefound and worker state changes, notifying users when a new version is ready, and providing an update action. An update check need not block the initial interface.
- **Interpretation:** Explain that a reload is needed, let users choose a safe moment, persist drafts, and coordinate reload behavior across open views where relevant.
- **Applies to:** service-worker apps; all inputs; update notification
- **Generalizability:** high — preserving work matters regardless of release mechanism.
- **Conflicts/tensions:** An urgent fix may justify stronger messaging, but forced reload can destroy unsaved task state.
- **Candidate knowledge targets:** Update-ready UI; safe reload; draft protection

### F-WP-50: Badges are supplementary status, not the sole notification channel

- **Source:** Enhancements | web.dev — <https://web.dev/learn/pwa/enhancements>; Update | web.dev — <https://web.dev/learn/pwa/update>
- **Publisher:** Google (web.dev)
- **Published/updated:** source 1: 2024-09-20; source 2: 2022-03-10
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform course explains the optional Badging API integration.
- **Finding:** The enhancements module describes setting or clearing app-icon badges to indicate unread or pending activity, subject to the available platform integration. The update module calls badging a best-effort mechanism: a platform may show a dot instead of the requested number.
- **Interpretation:** Feature-detect and clear stale badges; keep meaningful status available inside the app so users do not need to notice an OS icon.
- **Applies to:** platforms exposing badging; all inputs; asynchronous status
- **Generalizability:** medium — platform integration and visibility vary; no browser support matrix is inferred here.
- **Conflicts/tensions:** A badge count may become misleading after a stale/offline launch; intrusive attention signals can compete with the current task.
- **Candidate knowledge targets:** Badging; redundant status; notification hygiene

### F-WP-51: Receiving a system share is distinct from sending one

- **Source:** OS Integration | web.dev — <https://web.dev/learn/pwa/os-integration>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2022-04-15
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform documentation describes share integration and manifest share targets.
- **Finding:** Web Share sends data to another target, while a manifest share_target describes how an installed app can receive shared data on supporting systems. The integration creates an external app entry point.
- **Interpretation:** Validate incoming data and make a direct share launch understandable; retain upload, paste, or normal navigation paths for users without the integration.
- **Applies to:** supporting installed platforms; all inputs; inter-app handoff
- **Generalizability:** medium — capabilities are optional and platform-specific; this finding makes no unverified browser matrix claim.
- **Conflicts/tensions:** Treating outbound sharing support as proof of receiving-share support can produce dead-end UX.
- **Candidate knowledge targets:** Share target; inter-app entry; fallback input

### F-WP-52: display-mode detects the current presentation, not universal installation status

- **Source:** Detection | web.dev — <https://web.dev/learn/pwa/detection>; Web Application Manifest — <https://www.w3.org/TR/appmanifest/>
- **Publisher:** Google (web.dev); World Wide Web Consortium (W3C)
- **Published/updated:** source 1: 2024-09-18; source 2: 2026-11-06 (Working Draft)
- **Accessed:** 2026-11-08
- **Evidence class:** E1 — normative display-mode definition in the manifest Working Draft; course demonstrates matchMedia use.
- **Finding:** The display-mode media feature describes the actual current presentation. The manifest specification notes that fullscreen can match when the Fullscreen API is used, even without manifest installation. The course uses matchMedia to adapt presentation.
- **Interpretation:** Use display-mode to tailor chrome, with changes observed as needed; do not treat it as a universal installed/not-installed flag or infer other apps installed on the device.
- **Applies to:** all implementing browsers; all inputs; launch/presentation adaptation
- **Generalizability:** high — actual presentation and installation identity are distinct.
- **Conflicts/tensions:** A fullscreen browser session can resemble an installed mode; manual installs and browser launches further complicate installation inference.
- **Candidate knowledge targets:** Display-mode detection; installation inference limits

### F-WP-53: OS capabilities should enhance a complete baseline

- **Source:** Capabilities | web.dev — <https://web.dev/learn/pwa/capabilities>; OS Integration | web.dev — <https://web.dev/learn/pwa/os-integration>
- **Publisher:** Google (web.dev)
- **Published/updated:** source 1: 2022-04-20; source 2: 2022-04-15
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform documentation explains capability and permission patterns.
- **Finding:** The course covers file handling, protocol integration, and other optional capabilities. APIs can require feature detection, secure contexts, permissions, user activation, or installed app registration; related capabilities are not interchangeable.
- **Interpretation:** Request access in the context of a user task, explain denial/recovery, and provide ordinary file inputs or web navigation when enhanced integration is unavailable.
- **Applies to:** all platforms; all inputs; files, protocols, and OS integration
- **Generalizability:** high — capability availability and user permission are separate decisions.
- **Conflicts/tensions:** A successful feature check does not guarantee permission, and one file API does not imply support for all file integration features.
- **Candidate knowledge targets:** Capability enhancement; permissions; file fallback

### F-WP-54: Installed desktop windows remain resizable and can multiply

- **Source:** Window management | web.dev — <https://web.dev/learn/pwa/windows>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2022-04-15
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — application window design advice and API examples.
- **Finding:** The module discusses launching/managing app windows, adapting to different window dimensions, and using document titles to distinguish windows and current content.
- **Interpretation:** Support narrow desktop windows and wide mobile contexts, give each route a meaningful title, and avoid assuming a single global active window when preserving task state.
- **Applies to:** desktop and other windowed environments; pointer, keyboard, touch, AT; installed apps
- **Generalizability:** high — window size and multiplicity are ordinary web constraints, while advanced management is optional.
- **Conflicts/tensions:** Shared storage or a worker update can affect several windows while each has different unsaved state.
- **Candidate knowledge targets:** Window responsiveness; titles; multi-window state

### F-WP-55: Experiments and origin trials cannot be required for the core task

- **Source:** Experimental features | web.dev — <https://web.dev/learn/pwa/experimental>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2022-04-15
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform documentation explains flags, experiments, and origin trials.
- **Finding:** Experimental features may be exposed through flags or time-limited origin trials and can change or disappear before general release. The course recommends progressive enhancement around experimental capabilities.
- **Interpretation:** Keep an alternative path and check current availability; do not ask ordinary users to enable browser flags to complete a primary workflow.
- **Applies to:** all platforms; all inputs; experimental capabilities
- **Generalizability:** high — experiments are deliberately not a durable availability contract.
- **Conflicts/tensions:** A compelling capability demo is not evidence of broad production support.
- **Candidate knowledge targets:** Experimental features; fallback policy; capability maturity

### F-WP-56: Test installed, offline, update, and serving behavior explicitly

- **Source:** Tools and debug | web.dev — <https://web.dev/learn/pwa/tools-and-debug>; Serving | web.dev — <https://web.dev/learn/pwa/serving>; Best practices for PWAs - Progressive web apps | MDN — <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Best_practices>
- **Publisher:** Google (web.dev); MDN Web Docs contributors
- **Published/updated:** source 1: 2022-05-15; source 2: 2022-01-10; source 3: Jun 30, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform tooling and serving guidance.
- **Finding:** The course covers developer tools for manifests, service workers, cache inspection, and offline simulation. Its Serving module explains that a worker fetch handler can return network, cached, or generated responses and warns that bugs can prevent the app document from loading. MDN recommends testing responsiveness, accessibility, installation, and offline behavior.
- **Interpretation:** Test first visit versus controlled revisit, direct deep routes, correct manifest/worker responses, multiple windows, update/reload, failed network requests, and storage loss. A responsive viewport preview alone cannot verify installed behavior.
- **Applies to:** all target browsers/platforms; all inputs; PWA QA and hosting
- **Generalizability:** high — lifecycle and serving failures are independent of visual layout quality.
- **Conflicts/tensions:** Tool checks can reveal implementation errors but do not prove real-device UX or background reliability; this research includes no device testing.
- **Candidate knowledge targets:** PWA validation; secure serving; lifecycle test matrix

### F-WP-57: iOS push requires a Home Screen web app

- **Source:** PushManager - Web APIs | MDN — <https://developer.mozilla.org/en-US/docs/Web/API/PushManager>; MDN browser-compat-data: api/PushManager.json — <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/PushManager.json>
- **Publisher:** MDN Web Docs contributors; MDN browser-compat-data contributors
- **Published/updated:** source 1: Sep 28, 2026; source 2: not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN browser-compat-data explicitly records the iOS restriction, checked on 2026-11-08.
- **Finding:** MDN’s PushManager compatibility entry lists Safari on iOS support from 16.4 with the note that notifications are supported in web apps saved to the Home Screen. It lists desktop Safari support from 16 with a macOS Ventura-or-later qualification.
- **Interpretation:** Do not promise browser-tab push on iOS; explain installation and permission in context and retain an in-app way to see important events.
- **Applies to:** iOS and Safari desktop under stated versions; all inputs; push notifications
- **Generalizability:** medium — exact support is a dated compatibility snapshot.
- **Conflicts/tensions:** Older claims that Safari has no push support are too broad; presence of PushManager still does not imply permission has been granted.
- **Candidate knowledge targets:** iOS push limitation; installed prerequisite; notification fallback

## C — Navigation, state, focus, keyboards, and scrolling

### F-WP-58: Preserve meaningful session history when routing without document loads

- **Source:** History API - Web APIs | MDN — <https://developer.mozilla.org/en-US/docs/Web/API/History_API>; HTML Standard — <https://html.spec.whatwg.org/multipage/nav-history-apis.html>
- **Publisher:** MDN Web Docs contributors; WHATWG
- **Published/updated:** source 1: Jul 26, 2024; source 2: 2026-11-06 (Living Standard)
- **Accessed:** 2026-11-08
- **Evidence class:** E1 — normative History state/URL processing in the HTML Living Standard; MDN explains the API.
- **Finding:** pushState() creates a session-history entry, while replaceState() updates the current entry; state is serialized and URLs are subject to rewrite constraints, including same-origin restrictions for ordinary HTTP(S) documents. Back/forward traversal and popstate support restoring app state. Calling pushState() alone does not emit popstate.
- **Interpretation:** Give meaningful destinations real URLs and appropriate entries; use replacement for updates that should not create another Back step. Restore the route and relevant state on traversal.
- **Applies to:** all platforms; all inputs; client-side routing
- **Generalizability:** high — browser history is a fundamental navigation contract.
- **Conflicts/tensions:** A visually changed screen without a history entry can make Back leave the app unexpectedly; excessive entries make Back tedious.
- **Candidate knowledge targets:** History semantics; deep links; router state

### F-WP-59: Navigation API centralizes navigation but is not unrestricted history access

- **Source:** Navigation API - Web APIs | MDN — <https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API>; MDN browser-compat-data: api/Navigation.json — <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/Navigation.json>
- **Publisher:** MDN Web Docs contributors; MDN browser-compat-data contributors
- **Published/updated:** source 1: Jan 14, 2026; source 2: not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN API description and browser-compat-data, checked on 2026-11-08.
- **Finding:** Navigation API exposes same-origin, same-frame history entries and a navigate event with interception, state, focus, and scroll handling. It does not expose the initial load as a navigate event or allow arbitrary history reordering/deletion. MDN labels it Baseline 2026; its data lists Chrome 102, Firefox 147, and Safari 26.2 for Navigation.
- **Interpretation:** Feature-detect for older browsers; intercept only when canIntercept permits it, preserving normal link, download, hash, and external-navigation semantics. Use its focus/scroll lifecycle deliberately.
- **Applies to:** modern browsers with Navigation API; all inputs; SPA routing
- **Generalizability:** medium — core support has broadened, but older browsers and individual subfeatures need separate checks.
- **Conflicts/tensions:** Calling it Chromium-only is outdated relative to the fetched MDN data; the top-level interface entry does not prove every extension has identical support.
- **Candidate knowledge targets:** Navigation API; interception; history/focus/scroll

### F-WP-60: Back/forward cache restores a page snapshot rather than refetching it

- **Source:** Back/forward cache | Articles | web.dev — <https://web.dev/articles/bfcache>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2026-10-16
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform documentation explains page lifecycle and cache behavior.
- **Finding:** bfcache keeps a whole-page snapshot, including DOM and JavaScript heap, for possible restoration during history traversal. It differs from HTTP and service-worker caches and is not guaranteed to retain a page. pageshow with persisted indicates restoration. The article recommends avoiding unload handlers.
- **Interpretation:** Make restored pages usable immediately, then refresh sensitive or stale state as appropriate; test both snapshot restoration and a normal reload path.
- **Applies to:** browsers using bfcache; all inputs; back/forward navigation
- **Generalizability:** high — fast return navigation must still maintain correct state.
- **Conflicts/tensions:** A very fast restoration can expose stale authenticated data if the app assumes every return triggers a fresh request; no browser-specific eligibility matrix is asserted here.
- **Candidate knowledge targets:** bfcache; pageshow; stale-state recovery

### F-WP-61: Unsaved-change warnings have generic wording and unreliable delivery

- **Source:** Window: beforeunload event - Web APIs | MDN — <https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Oct 26, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — explicit MDN event restrictions and usage recommendations, checked on 2026-11-08.
- **Finding:** beforeunload warnings require prior user interaction (sticky activation), show browser-controlled generic text rather than an author’s custom message, and may not fire reliably, especially when a mobile app is killed. MDN recommends registering only while there are unsaved changes and removing the handler after saving; visibilitychange is a more reliable signal for automatic state saving.
- **Interpretation:** Save recoverable drafts proactively and attach the warning only while dirty. Do not rely on an unload dialog as the sole protection or design copy that depends on controlling its wording.
- **Applies to:** all platforms, especially mobile; all inputs; unsaved edits
- **Generalizability:** high — termination and dialog constraints affect any editor-like workflow.
- **Conflicts/tensions:** The warning is a last-chance guard, not durable persistence; lifecycle and bfcache guidance should not be reduced to a permanent browser exclusion rule.
- **Candidate knowledge targets:** Unsaved changes; beforeunload; draft autosave

### F-WP-62: Manual scroll restoration transfers responsibility to the app

- **Source:** History: scrollRestoration property - Web APIs | MDN — <https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** May 23, 2025
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents the property’s auto and manual values.
- **Finding:** history.scrollRestoration="auto" lets the browser restore scroll position during history traversal; "manual" disables that automatic restoration.
- **Interpretation:** Keep the browser default unless routing requires custom behavior. If choosing manual, restore the correct list position and route context after content is ready, including Back from detail pages.
- **Applies to:** all implementing browsers; all inputs; history traversal and long content
- **Generalizability:** high — return position affects continuity across many tasks.
- **Conflicts/tensions:** Unconditional scroll-to-top on every route event can destroy the expected return context.
- **Candidate knowledge targets:** Scroll restoration; list-detail continuity

### F-WP-63: View transitions enhance navigation without replacing its semantics

- **Source:** View Transition API - Web APIs | MDN — <https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API>; prefers-reduced-motion CSS media feature - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** source 1: Sep 28, 2026; source 2: Jun 10, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents same-document and cross-document transition models and motion preference.
- **Finding:** View Transition API supports animated changes within a document and transitions between documents. Its visual transition mechanism is separate from application routing and semantic content updates; feature availability can differ by part of the API.
- **Interpretation:** Use transitions as an enhancement, retain working navigation/focus/history without them, and provide a reduced-motion variant. Do not assume one support check proves every cross-document or advanced feature.
- **Applies to:** supporting browsers; all inputs; SPA and MPA transitions
- **Generalizability:** high — semantic navigation remains necessary regardless of animation.
- **Conflicts/tensions:** A smooth visual change can conceal poor focus placement or disorient users who request less motion.
- **Candidate knowledge targets:** View transitions; navigation continuity; reduced motion

### F-WP-64: :focus-visible uses browser heuristics rather than a keyboard-only test

- **Source:** :focus-visible CSS pseudo-class - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Oct 16, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents the pseudo-class and user-agent heuristics.
- **Finding:** The pseudo-class matches focus when the browser determines that a visible indicator is appropriate. Input elements that expect keyboard entry may match even after pointer focus; it is not simply a keyboard-versus-mouse switch.
- **Interpretation:** Keep a clear visible focus style and test controls with keyboard, pointer, touch, and AT. Avoid removing outlines globally and then assuming this selector repairs every case.
- **Applies to:** all platforms; keyboard, AT, pointer, touch; focus styling
- **Generalizability:** high — visible orientation is essential for many navigation methods.
- **Conflicts/tensions:** Aesthetic suppression of focus can conflict with browser/user expectations and accessibility preferences.
- **Candidate knowledge targets:** Focus visibility; modality heuristics

### F-WP-65: inputmode hints a virtual keyboard and does not validate input

- **Source:** inputmode HTML global attribute - HTML | MDN — <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Apr 17, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents attribute values and their limitations.
- **Finding:** inputmode hints which virtual keyboard is appropriate. numeric and decimal have different intended keys; decimal separators depend on locale and minus keys may be absent. The attribute imposes no validity constraints.
- **Interpretation:** Use text inputs with a suitable inputmode for identifiers such as account numbers, retain leading zeros, and validate according to the actual data model. Test localized keyboards and required symbols.
- **Applies to:** mobile/tablet and other virtual-keyboard contexts; touch, keyboard, AT; forms
- **Generalizability:** high — keyboard hints and semantic validation are distinct.
- **Conflicts/tensions:** A numeric keyboard can make valid negative or formatted values hard to enter; inputmode is not a guarantee of an exact key layout.
- **Candidate knowledge targets:** Virtual keyboard hints; form semantics; numeric entry

### F-WP-66: autocomplete describes field purpose rather than choosing keyboard layout

- **Source:** autocomplete HTML attribute - HTML | MDN — <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Aug 27, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents autofill tokens and browser behavior.
- **Finding:** autocomplete supplies semantic tokens for browser autofill, including contact/address fields, current-password, new-password, and one-time-code. section-* and shipping/billing distinguish groups. MDN notes browsers/password managers may ignore off for login fields.
- **Interpretation:** Use correct field-purpose tokens to reduce typing and support credentials/OTP flows; combine them with appropriate input types and inputmode instead of using them as keyboard-layout controls.
- **Applies to:** all platforms; virtual/physical keyboards, AT; forms and authentication
- **Generalizability:** high — semantic field purpose benefits both mobile entry and desktop autofill.
- **Conflicts/tensions:** Turning autofill off is not a dependable way to prevent credential suggestions and can increase user effort.
- **Candidate knowledge targets:** Autofill; password managers; OTP; semantic forms

### F-WP-67: enterkeyhint labels the virtual keyboard action key

- **Source:** enterkeyhint HTML global attribute - HTML | MDN — <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Apr 17, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents the enumerated keyboard-label hint.
- **Finding:** enterkeyhint suggests labels or icons such as enter, done, go, next, previous, search, and send for the virtual keyboard Enter key. It describes presentation, not automatic implementation of those actions.
- **Interpretation:** Match the hint to the form’s real next action and implement submit/focus behavior consistently; ensure the action remains available as an accessible control.
- **Applies to:** virtual-keyboard platforms; touch, keyboard, AT; sequential forms and search
- **Generalizability:** high — labeling should accurately describe the resulting action.
- **Conflicts/tensions:** A Send label with a newline action, or Next with nowhere to go, creates misleading feedback.
- **Candidate knowledge targets:** Keyboard action labels; form progression

### F-WP-68: interactive-widget distinguishes visual resize, layout resize, and overlay

- **Source:** &lt;meta name="viewport"&gt; HTML attribute value - HTML | MDN — <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Sep 23, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents viewport metadata semantics; no browser support matrix is inferred.
- **Finding:** interactive-widget controls the effect of UI such as a virtual keyboard: resizes-visual is the default and changes the visual viewport; resizes-content also changes the layout viewport/initial containing block; overlays-content resizes neither. Layout viewport resizing affects viewport-unit computation.
- **Interpretation:** Choose a keyboard strategy consciously for chat inputs and fixed controls, then verify it in target browsers. Do not assume the metadata is honored everywhere merely because it is documented.
- **Applies to:** supporting virtual-keyboard contexts; touch, keyboard, AT; keyboard-aware layouts
- **Generalizability:** medium — behavior depends on browser support and the selected viewport policy.
- **Conflicts/tensions:** An overlay policy can hide the focused input unless the application manages occlusion.
- **Candidate knowledge targets:** Interactive widget; visual/layout viewport; keyboard occlusion

### F-WP-69: VirtualKeyboard API offers layout control with narrow compatibility

- **Source:** VirtualKeyboard API - Web APIs | MDN — <https://developer.mozilla.org/en-US/docs/Web/API/VirtualKeyboard_API>; MDN browser-compat-data: api/VirtualKeyboard.json — <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/VirtualKeyboard.json>
- **Publisher:** MDN Web Docs contributors; MDN browser-compat-data contributors
- **Published/updated:** source 1: Nov 6, 2025; source 2: not shown
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN API description and compatibility data, checked on 2026-11-08.
- **Finding:** The secure-context, experimental API can set navigator.virtualKeyboard.overlaysContent=true, expose boundingRect/geometrychange, and provide keyboard-inset-* CSS variables. MDN compatibility data lists Chrome 94 and no Firefox/Safari support for the interface. Opting into overlay stops the browser from resizing the viewport for the keyboard.
- **Interpretation:** Feature-detect, maintain a browser-managed fallback, and keep focused fields/actions visible if taking responsibility for layout. Do not build a universal keyboard solution around this API alone.
- **Applies to:** supporting Chromium contexts; virtual keyboard; editors/chat
- **Generalizability:** medium — strong control is available only in the documented support subset.
- **Conflicts/tensions:** Overlay control shifts work from the browser to the application; interface support does not guarantee every method/subfeature behaves identically.
- **Candidate knowledge targets:** VirtualKeyboard API; keyboard geometry; fallback layout

### F-WP-70: Edge-to-edge layouts must preserve a safe area for essential controls

- **Source:** &lt;meta name="viewport"&gt; HTML attribute value - HTML | MDN — <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport>; env() CSS function - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/env>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** source 1: Sep 23, 2026; source 2: Oct 8, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents viewport-fit and environment-variable substitution.
- **Finding:** viewport-fit=cover fills the display and calls for safe-area insets so important content is not cut off. env(safe-area-inset-top/right/bottom/left) exposes safe distances; an env fallback is used when a variable is absent, not when a valid value happens to be zero.
- **Interpretation:** Allow backgrounds to extend while padding primary controls using safe-area values and baseline spacing, for example max(1rem, env(safe-area-inset-bottom, 0px)). Test rotation and installed/browser presentations.
- **Applies to:** cutout/nonrectangular displays and edge-to-edge windows; all inputs; fixed chrome
- **Generalizability:** high — critical content must remain inside the visible usable region.
- **Conflicts/tensions:** Safe areas and virtual-keyboard geometry are related layout concerns but are not interchangeable universal keyboard signals.
- **Candidate knowledge targets:** Safe areas; viewport-fit; edge-to-edge controls

### F-WP-71: Dynamic viewport units track browser chrome, not a universal keyboard height

- **Source:** The large, small, and dynamic viewport units | Blog | web.dev — <https://web.dev/blog/viewport-units>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2022-11-29
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — platform explanation of large, small, and dynamic viewport units and caveats.
- **Finding:** svh uses the small viewport with browser UI expanded; lvh uses the large viewport with retractable UI retracted; dvh adapts between those states. Dynamic updates can be throttled rather than occurring at every animation frame. The article states that virtual keyboards normally do not affect these viewport units by themselves.
- **Interpretation:** Use 100dvh when a screen should follow available height as browser chrome changes, or svh when stability is preferable. Handle keyboard occlusion separately rather than assuming dvh solves it.
- **Applies to:** mobile and other dynamic-browser-chrome contexts; all inputs; full-height layouts
- **Generalizability:** high — the distinction prevents common full-screen layout errors; actual policy still needs browser testing.
- **Conflicts/tensions:** 100dvh can resize content while scrolling, whereas svh may leave space; neither choice alone proves the focused field is visible above a keyboard.
- **Candidate knowledge targets:** Dynamic viewport units; full-height layout; keyboard limits

### F-WP-72: touch-action declares browser gesture handling before a gesture starts

- **Source:** touch-action CSS property - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/touch-action>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Apr 20, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents gesture negotiation and accessibility implications.
- **Finding:** The browser intersects touch-action values on the target and relevant ancestors when deciding gesture handling; changing the value midgesture does not affect that gesture. none disables browser panning/zooming; manipulation permits panning and pinch zoom while excluding additional gestures such as double-tap zoom.
- **Interpretation:** Declare only the restrictions required by a custom gesture and retain scrolling/zooming wherever possible. Test embedded draggable surfaces within scrollable pages.
- **Applies to:** touch/pointer-event browsers; touch and pen; custom gestures
- **Generalizability:** high — browser gestures must coexist with application gestures.
- **Conflicts/tensions:** Global touch-action:none can remove essential zoom and scrolling access merely to simplify custom event handling.
- **Candidate knowledge targets:** Touch gestures; pinch zoom; gesture negotiation

### F-WP-73: overscroll-behavior separates scroll chaining from overscroll effects

- **Source:** overscroll-behavior CSS property - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Oct 13, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents auto, contain, and none behavior.
- **Finding:** contain stops scroll chaining to an ancestor while retaining local boundary effects; none also suppresses those effects. The property can affect browser overscroll navigation and pull-to-refresh behavior.
- **Interpretation:** Use containment deliberately for dialogs or nested scrollers; keep the main document’s familiar gestures unless the task needs a different behavior and an alternative is clear.
- **Applies to:** scroll-container contexts; touch, trackpad, pointer, keyboard; nested scrolling
- **Generalizability:** high — boundary behavior influences modal and document navigation.
- **Conflicts/tensions:** Preventing accidental page movement can also remove expected refresh/navigation gestures.
- **Candidate knowledge targets:** Scroll containment; nested scrolling; gesture expectations

### F-WP-74: Scroll snap supplies native alignment and needs reachable content

- **Source:** CSS scroll snap - CSS | MDN — <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap>
- **Publisher:** MDN Web Docs contributors
- **Published/updated:** Aug 21, 2026
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — MDN documents snap positions, padding/margins, and stop behavior.
- **Finding:** CSS scroll snap defines alignment positions for overflowing content. scroll-padding changes the optimal viewing region on the container, while scroll-margin adjusts a child’s visual area; snap-stop can constrain skipping past items.
- **Interpretation:** Use native scrolling rather than recreating it with drag handlers, account for sticky headers, and verify access to all content with touch, trackpad, keyboard, zoom, and long/variable-size items.
- **Applies to:** all implementing browsers; all inputs; carousels and paged scrollers
- **Generalizability:** high — native alignment is useful, but the appropriate strictness is content-dependent.
- **Conflicts/tensions:** The MDN demo’s mandatory snapping is an example, not evidence that forced snapping is best for every reading or data task.
- **Candidate knowledge targets:** Scroll snap; sticky-header offsets; reachable overflow

## D — Performance and perceived responsiveness

### F-WP-75: LCP has good, needs-improvement, and poor boundaries at 2.5 and 4 seconds

- **Source:** Largest Contentful Paint (LCP) | Articles | web.dev — <https://web.dev/articles/lcp>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2025-09-04
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — Google’s documented Core Web Vital definition and thresholds.
- **Finding:** Largest Contentful Paint measures when the largest qualifying image or text block in the viewport is rendered. Good is LCP ≤ 2.5 seconds; needs improvement is > 2.5 and ≤ 4.0 seconds; poor is > 4.0 seconds.
- **Interpretation:** Prioritize delivery and rendering of the main content; do not count a quick shell or spinner as proof that the useful page has loaded.
- **Applies to:** mobile and desktop; all inputs; loading performance
- **Generalizability:** high — metric thresholds are standardized platform guidance, not task-completion guarantees.
- **Conflicts/tensions:** A visually fast loading result can still have slow interactions or disruptive layout shifts.
- **Candidate knowledge targets:** LCP; main-content loading; performance thresholds

### F-WP-76: INP measures interaction-to-next-paint, with 200 and 500 ms boundaries

- **Source:** Interaction to Next Paint (INP) | web.dev — <https://web.dev/articles/inp>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2025-09-02
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — Google’s documented Core Web Vital definition and thresholds.
- **Finding:** Interaction to Next Paint assesses responsiveness to qualifying click, tap, and keyboard interactions over a visit, including delay, processing, and presentation. Good is INP ≤ 200 ms; needs improvement is > 200 and ≤ 500 ms; poor is > 500 ms. It measures the next paint, not completion of every asynchronous effect of an action.
- **Interpretation:** Give prompt visible feedback and reduce main-thread work; separately measure server-backed completion and correctness for long tasks.
- **Applies to:** mobile and desktop; click, tap, keyboard; runtime responsiveness
- **Generalizability:** high — interactive responsiveness matters broadly, while visit measurement needs real interactions.
- **Conflicts/tensions:** A quick disabled-button repaint can satisfy immediate feedback while a transaction remains slow or fails.
- **Candidate knowledge targets:** INP; main-thread responsiveness; immediate feedback

### F-WP-77: CLS measures visual instability, with boundaries at 0.1 and 0.25

- **Source:** Cumulative Layout Shift (CLS) | Articles | web.dev — <https://web.dev/articles/cls>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2023-04-12
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — Google’s documented Core Web Vital definition and thresholds.
- **Finding:** Cumulative Layout Shift is a unitless measure of unexpected layout movement. Good is CLS ≤ 0.1; needs improvement is > 0.1 and ≤ 0.25; poor is > 0.25. Qualifying shift scoring is not a count of shifted pixels.
- **Interpretation:** Reserve space for images, embeds, and asynchronous content, and prevent late UI insertion from moving an intended click target.
- **Applies to:** mobile and desktop; all inputs; rendering stability
- **Generalizability:** high — unexpected movement affects reading and interaction across tasks.
- **Conflicts/tensions:** A low aggregate score does not prove that a particular critical control never moved at a bad time.
- **Candidate knowledge targets:** CLS; layout stability; reserved geometry

### F-WP-78: Assess all three Core Web Vitals at the 75th percentile in the field

- **Source:** Web Vitals | Articles | web.dev — <https://web.dev/articles/vitals>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2024-10-31
- **Accessed:** 2026-11-08
- **Evidence class:** E3 — Google’s documented aggregation and measurement guidance.
- **Finding:** A good assessment requires meeting the recommended target for each Core Web Vital at the 75th percentile of page loads, segmented by mobile and desktop. Field data captures real conditions; laboratory tools are useful diagnostically, but a noninteractive Lighthouse load cannot directly measure INP, with TBT serving as a lab proxy.
- **Interpretation:** Report LCP, INP, and CLS together for real users and distinguish lab estimates from field outcomes; do not average away a slow tail or combine mobile and desktop into one pass claim.
- **Applies to:** mobile and desktop; all inputs; performance evaluation
- **Generalizability:** high — aggregation rules are essential to interpreting these metrics.
- **Conflicts/tensions:** Passing the three metrics does not assess navigation clarity, accessibility, offline recovery, or end-to-end task success.
- **Candidate knowledge targets:** Core Web Vitals assessment; p75; field versus lab

### F-WP-79: The 0.1, 1, and 10 second limits are response-time heuristics

- **Source:** Response Time Limits: Article by Jakob Nielsen - NN/G — <https://www.nngroup.com/articles/response-times-3-important-limits/>
- **Publisher:** Nielsen Norman Group
- **Published/updated:** 1993-01-01; web-application update added 2014 (visible article dates)
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — historical expert synthesis citing earlier research, without a newly described study in this article.
- **Finding:** Nielsen gives approximately 0.1 s for feeling instantaneous/direct manipulation, 1 s for maintaining flow despite noticeable delay, and 10 s for retaining attention. The 2014 addition recommends visible working feedback beyond 1 s, and progress plus a clear interruption path beyond 10 s.
- **Interpretation:** Acknowledge input immediately, show meaningful status for longer work, and let users leave or cancel long operations when appropriate. Treat the values as rough interaction-design limits, separate from Core Web Vital definitions.
- **Applies to:** all platforms; all inputs; task response and progress feedback
- **Generalizability:** high — useful broad heuristics, but tolerance depends on task and expectation.
- **Conflicts/tensions:** These limits are not an SLA, a universal empirical cutoff, or substitutes for INP/LCP thresholds.
- **Candidate knowledge targets:** Response-time heuristics; progress; cancellation

### F-WP-80: Skeletons can convey incoming structure; superiority to spinners is unverified here

- **Source:** prefers-reduced-motion: Sometimes less movement is more | Articles | web.dev — <https://web.dev/articles/prefers-reduced-motion>
- **Publisher:** Google (web.dev)
- **Published/updated:** 2019-03-11
- **Accessed:** 2026-11-08
- **Evidence class:** E4 — practitioner explanation of perceived-speed techniques; no controlled comparison is reported.
- **Finding:** The article describes combining skeleton screens, contextual metadata, and low-quality image previews to convey what is coming while loading and make an experience feel faster. It also explains that decorative or excessive animation can distract or trigger motion sickness.
- **Interpretation:** Use a stable, truthful placeholder when structure is predictable; give useful task/status information and reduce shimmer or motion for users who request it. Test the actual waiting experience rather than assuming a skeleton always beats a spinner.
- **Applies to:** all platforms; all inputs; perceived loading responsiveness
- **Generalizability:** medium — suitability depends on predictability, wait length, motion sensitivity, and task.
- **Conflicts/tensions:** No fetched source establishes a universal skeleton-versus-spinner advantage, effect size, or duration rule.
- **Candidate knowledge targets:** Skeleton screens; perceived responsiveness; loading evidence limits

## Coverage and gaps

- **Source audit:** 96 unique resources fetched successfully: 91 HTML pages and 5 MDN browser-compat-data JSON documents. Findings cite 84 of those resources. Counts treat English-language refetches as the same document and exclude unsuccessful requests. Compatibility was checked on 2026-11-08. The MDN compatibility tables were not rendered in the fetched HTML, so the underlying MDN browser-compat-data JSON was fetched for BeforeInstallPromptEvent, Navigation, PushManager, VirtualKeyboard, and media features. No third-party compatibility inference is substituted.
- **Responsive course coverage:** Read the course index and all 16 modules: welcome, intro, media-queries, internationalization, macro-layouts, micro-layouts, typography, responsive-images, picture-element, icons, theming, accessibility, interaction, ui-patterns, media-features, and screen-configurations. Container-query behavior was supplemented with MDN; primary/aggregate input features and reduced-data semantics were checked against Media Queries Levels 4 and 5.
- **PWA course coverage:** Read the course index and all 22 modules: welcome, progressive-web-apps, getting-started, foundations, app-design, assets-and-data, service-workers, caching, serving, workbox (skim), offline-data, installation, web-app-manifest, installation-prompt, update, enhancements, detection, os-integration, windows, experimental, capabilities, and tools-and-debug. Reviewed the requested MDN PWA guides and manifest references, including installation/removal, offline/background operation, caching, best practices, display, display_override, start_url, scope, and shortcuts.
- **Navigation and layout coverage:** History/Navigation, bfcache, unload warnings, scroll restoration, transitions, focus heuristics, form keyboard hints/autofill, viewport policy, VirtualKeyboard, safe areas, dynamic viewport units, touch-action, overscroll, scroll snap, and reduced motion are covered. Core Web Vital category endpoints and the 75th-percentile rule were checked in the metric and overview pages. The fetched response-time source is NN/g’s Response Times: The 3 Important Limits, linked in F-WP-79.
- **Failed requests and replacements:** Four guessed web.dev paths returned HTTP 404: `https://web.dev/articles/viewport-units` (replaced by the fetched `https://web.dev/blog/viewport-units`); `https://web.dev/articles/patterns-for-promoting-pwa-installation` (replaced by the fetched `https://web.dev/articles/promote-install`); `https://web.dev/articles/viewport-resize-behavior` (supplemented by the fetched Chrome article at `https://developer.chrome.com/blog/viewport-resize-behavior` and the cited MDN viewport reference); and `https://web.dev/articles/virtual-keyboard` (supplemented by the cited MDN VirtualKeyboard reference and fetched Chrome documentation at `https://developer.chrome.com/docs/web-platform/virtual-keyboard`). Failed URLs are recorded only as failures and are not evidence citations. All requested subject areas were reachable through the successful sources.
- **Limits of this evidence:** No browser/device experiments, usability tests, assistive-technology audit, or performance measurements were conducted. A top-level API’s support entry does not establish support for every subfeature, embedded WebView, enterprise configuration, or older browser. Advanced badging, share-target, file/protocol, and window integration are described conditionally; their complete current browser matrices were not verified. The storage source does not establish a blanket installed-iOS exemption from proactive eviction. Exact cache timeouts, conflict resolution, target dimensions, type scales, and breakpoint values remain product decisions requiring task/context evidence.
- **Perceived-performance gap:** The fetched web.dev article discusses skeletons and previews, but no fetched controlled study compares skeletons against spinners. No universal superiority, duration cutoff, or percentage improvement is claimed. The NN/g limits are historical expert synthesis, not a new experiment or a web specification.

## Disagreements

- **Older course compatibility versus current MDN:** The installation-prompt course still says Chrome/Edge on iOS do not support installation, while current MDN describes supporting Share-menu installation from iOS 16.4 (F-WP-38). The update course groups background APIs, including push, under a Chromium-only claim, while MDN documents conditional Safari push support (F-WP-57). These older passages are not used as current compatibility evidence. Desktop Safari installation is likewise assessed with current MDN (F-WP-39).
- **Internal MDN start_url inconsistency:** The Description constrains start_url to the installing page’s origin, while Best practices describes the manifest’s origin. F-WP-45 follows the normative manifest algorithm: resolve against the manifest URL, then compare origin with the document URL. A cross-origin-hosted manifest does not change that constraint.
- **App-like presentation versus web navigation:** Standalone/fullscreen presentation removes familiar URL/back/refresh/share affordances. The resulting obligation to supply navigation and safe direct-launch behavior can outweigh the aesthetic benefit of less browser chrome (F-WP-42–47, F-WP-58–62). Display-mode expresses current presentation rather than installation identity (F-WP-52).
- **Speed/offline continuity versus freshness and durability:** Cache-first and stale-while-revalidate reduce waiting but can expose stale data; network-first can delay useful cached content. Installation and an offline shell do not guarantee completed background mutations, persistent storage, or coherent updates across existing windows (F-WP-28–36, F-WP-48–49).
- **Capability detection versus actual human interaction:** Primary and aggregate pointer queries provide useful capabilities but cannot identify the current input or exclude touch when a mouse is also present. A fine/hover result is insufficient justification for small exclusive targets or hover-only actions (F-WP-16–21).
- **Available space versus stable, accessible presentation:** Fluid type, snapping, viewport-height changes, foldable segments, and motion can improve fit or orientation yet conflict with zoom, long content, predictable scroll position, or reduced-motion preferences. Evaluate the combined behavior, including keyboards and safe areas, rather than accepting a visually smooth narrow-screen demo as proof (F-WP-07–08, F-WP-22–26, F-WP-63–74).
- **Specified semantics versus shipped support:** Media Queries Level 5 and the manifest are cited as Working Drafts. In particular, reduced-data semantics are useful to define, while MDN does not establish dependable default-on support (F-WP-23–24). Specification status and implementation availability must remain separate in the knowledge base.
