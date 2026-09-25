# Generative AI, with receipts.

A dependency-free, static scrollytell for Wesley R. Elsberry’s MSU BEACON large-group discussion. Intended URL: <https://welsberr.github.io/presentations/beacon-generative-ai/>.

## Edit and build

Edit `content.json`, then run `python3 build.py`. This regenerates `index.html`, `speaker-notes.md`, and `speaker-notes.html`. `scenes` holds the main talk; `deep_dives` holds optional appendix chapters, their canonical callers, and their scenes. Main scenes select contextual dive links by ID. Content fields contain trusted, author-written HTML; this is not a runtime input system. Styles and interaction code live in `style.css` and `presentation.js`.

Serve the repository root with any static HTTP server. GitHub Pages serves the files directly; there are no runtime packages, CDN scripts, API keys, externally hosted fonts, analytics, or model calls.

## Present

Scroll normally, use the previous/next buttons or left/right keys, or select a section. `Alt+N` toggles all speaker notes. Links support direct section URLs. Keyboard shortcuts do not override links, form controls, or expanded-note controls. Printing uses a dedicated stylesheet; all main text and references remain readable without JavaScript. On narrow screens, illustrations move into the reading flow.

The main talk has 21 sections. Seven optional Deep Dives (19 short sections) follow its conclusion, before the source ledger: ClaimWright/policy, GroundRecall/Epistemap, doclift/Didactopus, CiteGeist, TalkOrigins updates/translation, GenieHive/local LLMs, and SciSiteForge/publication. They are outside the default 30-minute core.

Open a Deep Dive from a main section and each return link leads back to that caller. Keyboard activation, reload, and browser history retain the caller. Session storage is optional and contains only section IDs; no information is submitted. Without JavaScript, native links open each dive and return to its canonical introducing section. The directory and section selector also expose the appendix. The progress bar measures the main talk or the current dive separately.

The gate demonstration is a teaching simulation. Its release decisions are local JavaScript, not the GroundRecall or ClaimWright enforcement engine.

## Editorial status

Speaker review draft, checked 25 September 2026. The speaker’s firsthand account of internal adoption has been incorporated. Awaiting meeting date and duration and the first personal CiteGeist-use date. The current timeline uses the earliest repository commit, explicitly labeled as such. The planned speaking time is approximately 30 minutes plus discussion.

The first part covers private-sector adoption, as clarified by the speaker. A general evaluation preface comes before the industry overview and RealPage example. It frames capability, quality, cost, review, and correction as shared design questions that also apply to the speaker’s own work. RealPage’s public announcements illustrate its product direction and are attributed company statements. Two separate sections present the speaker’s account of an unnamed employer’s internal adoption: management’s productivity and quality goals, a shift toward directing AI coding and domain-focused review, cost containment, and shared concerns about accuracy, efficiency, accountability, and durable knowledge. The account keeps the employer unnamed, presents productivity and quality as objectives, and does not imply organizational use of the speaker’s personal tools.

The TalkOrigins workflow section covers English source review, bibliography updates, translation into Spanish/French/German/Portuguese, local LLM workers, and scoped publication. The appendix distinguishes model runtimes, GenieHive routing, and queue scheduling. The public translation count is a dated 8 July 2026 generation snapshot, not an expert-review claim. `evidence/talkorigins-workflow.json` records a sanitized inspection summary and public evidence links.

The source ledger is in `content.json` and the rendered appendix. Pinned repository references document the inspected versions. `evidence/bibliography-build.json` contains only aggregate, nonprivate counts and the source manifest checksum. Counts refer to placements across topic bibliographies, not unique papers or verified scientific claims. `evidence/repository-snapshots.json` records inspected commit identifiers. Private memory records and local operational paths are excluded.

The social card was generated with AI for this presentation. It is original decorative typography, not documentary evidence.

## Validation

Validated with local Chromium: 21 main scenes, 19 appendix scenes, 26 source records, unique IDs and valid internal anchors; all 16 release-gate input combinations; section navigation, diagram changes, notes toggle, and keyboard next; widths 320, 390, 760, 768, 1024, and 1440 pixels without horizontal overflow; print controls hidden; no-JavaScript text availability; no JavaScript errors. Representative desktop and mobile screenshots were visually reviewed. Deep Dive checks exercise every contextual entry and caller return, keyboard activation, reload, browser history, directory return, unavailable session storage, and native no-JavaScript links. Run `python3 tests/verify_deep_dives.py <presentation-url>` in a development environment with Playwright and Chromium installed; these are test-only dependencies. This verifies the presentation, not the underlying research tools or their scientific claims.

## MSU web guidance

The color and typography adaptation follows MSU’s official brand and web accessibility guidance. See [DESIGN-GUIDANCE.md](DESIGN-GUIDANCE.md) for source links, adopted rules, and scope. Metropolis fonts are served locally. The scrollytell layout, gate demonstration, navigation, and print view are retained.
