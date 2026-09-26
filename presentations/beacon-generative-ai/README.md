# Generative AI, with receipts.

A dependency-free, static scrollytell for Wesley R. Elsberry’s MSU BEACON large-group discussion. Intended URL: <https://welsberr.github.io/presentations/beacon-generative-ai/>.

## Edit and build

Edit `content.json`, then run `python3 build.py`. This regenerates `index.html`, `speaker-notes.md`, and `speaker-notes.html`. `scenes` holds the main talk; `deep_dives` holds optional appendix chapters, their canonical callers, and their scenes. Main scenes select contextual dive links by ID. Content fields contain trusted, author-written HTML; this is not a runtime input system. Styles and interaction code live in `style.css` and `presentation.js`.

Serve the repository root with any static HTTP server. GitHub Pages serves the files directly; there are no runtime packages, CDN scripts, API keys, externally hosted fonts, analytics, or model calls.

## Present

Scroll normally, use the previous/next buttons or left/right keys, or select a section. `Alt+N` toggles all speaker notes. Links support direct section URLs. Keyboard shortcuts do not override links, form controls, or expanded-note controls. Printing uses a dedicated stylesheet; all main text and references remain readable without JavaScript. On narrow screens, illustrations move into the reading flow.

The main talk has 20 sections. Seven optional Deep Dives (19 short sections) follow its conclusion, before the source ledger: ClaimWright/policy, GroundRecall/Epistemap, doclift/Didactopus, CiteGeist, TalkOrigins updates/translation, GenieHive/local LLMs, and SciSiteForge/publication. They are outside the default 30-minute core. The [repository capability review and alternatives feature analysis](comparison/) is a separate, author-approved companion report.

Open a Deep Dive from a main section and each return link leads back to that caller. Keyboard activation, reload, and browser history retain the caller. Session storage is optional and contains only section IDs; no information is submitted. Without JavaScript, native links open each dive and return to its canonical introducing section. The directory and section selector also expose the appendix. The progress bar measures the main talk or the current dive separately.

The gate demonstration is a teaching simulation. Its release decisions are local JavaScript, not the GroundRecall or ClaimWright enforcement engine.

## Editorial status

Author-approved public revision, 26 September 2026. The speaker’s firsthand account of internal adoption remains anonymous. The timeline uses the earliest repository commit, explicitly labeled as such, rather than asserting a first personal-use date. The planned speaking time is approximately 30 minutes plus discussion.

The first part covers private-sector adoption. A general evaluation preface frames capability, quality, cost, review, and correction as shared design questions that also apply to the speaker’s own work. Company-specific material has been removed for broader sharing. Two sections retain the speaker’s account of an unnamed employer’s internal adoption: management’s productivity and quality goals, a shift toward directing AI coding and domain-focused review, cost containment, and shared concerns about accuracy, efficiency, accountability, and durable knowledge. The account presents productivity and quality as objectives and does not imply organizational use of the speaker’s personal tools.

The original tracked presentation is preserved at Git tag `beacon-generative-ai-original-2026-09-26`, pointing to commit `3ef36fb3890cfe7b0978f9bd827c13fe63a0e522`. An offline tar archive and checksum are retained by the maintainer. The canonical presentation URL serves this revised edition.

The TalkOrigins workflow section covers English source review, bibliography updates, translation into Spanish/French/German/Portuguese, local LLM workers, and scoped publication. The appendix distinguishes model runtimes, GenieHive routing, and queue scheduling. The public translation count is a dated 8 July 2026 generation snapshot, not an expert-review claim. `evidence/talkorigins-workflow.json` records a sanitized inspection summary and public evidence links.

The source ledger is in `content.json` and the rendered appendix. Pinned repository references document the inspected versions. `evidence/bibliography-build.json` contains only aggregate, nonprivate counts and the source manifest checksum. Counts refer to placements across topic bibliographies, not unique papers or verified scientific claims. `evidence/repository-snapshots.json` records inspected commit identifiers. Private memory records and local operational paths are excluded.

An Acknowledgements section follows the source ledger, credits OpenAI Codex, states the assistance/review boundary, and gives a short development timeline from repository commits (25 September 2026, EDT). Its editable text and milestones live in `content.json` and also appear in the speaker notes.

The social card was generated with AI for this presentation. It is original decorative typography, not documentary evidence.

## Validation

Browser regression checks cover 20 main scenes, 19 appendix scenes, 25 source records, unique IDs and valid internal anchors; section navigation; widths 320, 390, 760, 768, 1024, and 1440 pixels without horizontal overflow; no-JavaScript text availability; and JavaScript errors. Deep Dive checks exercise every contextual entry and caller return, keyboard activation, reload, browser history, directory return, unavailable session storage, and native no-JavaScript links. Run `python3 tests/verify_deep_dives.py <presentation-url>` in a development environment with Playwright and Chromium installed; these are test-only dependencies. This verifies the presentation, not the underlying research tools or their scientific claims. The companion report documents the separate ClaimWright and GenieHive software validation.

## MSU web guidance

The color and typography adaptation follows MSU’s official brand and web accessibility guidance. See [DESIGN-GUIDANCE.md](DESIGN-GUIDANCE.md) for source links, adopted rules, and scope. Metropolis fonts are served locally. The scrollytell layout, gate demonstration, navigation, and print view are retained.
