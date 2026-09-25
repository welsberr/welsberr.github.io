# Generative AI, with receipts.

A dependency-free, static scrollytell for Wesley R. Elsberry’s MSU BEACON large-group discussion. Intended URL: <https://welsberr.github.io/presentations/beacon-generative-ai/>.

## Edit and build

Edit `content.json`, then run `python3 build.py`. This regenerates `index.html`, `speaker-notes.md`, and `speaker-notes.html`. Content fields contain trusted, author-written HTML; this is not a runtime input system. Styles and interaction code live in `style.css` and `presentation.js`.

Serve the repository root with any static HTTP server. GitHub Pages serves the files directly; there are no runtime packages, CDN scripts, API keys, external fonts, analytics, or model calls.

## Present

Scroll normally, use the previous/next buttons or left/right keys, or select a section. `N` toggles all speaker notes. Links support direct section URLs. Keyboard shortcuts do not override links, form controls, or expanded-note controls. Printing uses a dedicated stylesheet; all main text and references remain readable without JavaScript. On narrow screens, illustrations move into the reading flow.

The gate demonstration is a teaching simulation. Its release decisions are local JavaScript, not the GroundRecall or ClaimWright enforcement engine.

## Editorial status

Speaker review draft, checked 25 September 2026. Awaiting the speaker’s own RealPage assessment and focal announcement, meeting date and duration, and the first personal CiteGeist-use date. The current timeline uses the earliest repository commit, explicitly labeled as such. The planned speaking time is approximately 30 minutes plus discussion.

The first part covers private-sector adoption, as clarified by the speaker. RealPage claims are attributed company statements; discussion questions are not represented as findings about private company operations or as personal testimony. No alleged wrongdoing or internal company information is included.

The source ledger is in `content.json` and the rendered appendix. Pinned repository references document the inspected versions. `evidence/bibliography-build.json` contains only aggregate, nonprivate counts and the source manifest checksum. Counts refer to placements across topic bibliographies, not unique papers or verified scientific claims. `evidence/repository-snapshots.json` records inspected commit identifiers. Private memory records and local operational paths are excluded.

The social card was generated with AI for this presentation. It is original decorative typography, not documentary evidence.

## Validation

Validated with local Chromium: 18 scenes, 19 source records, unique IDs and valid internal anchors; all 16 release-gate input combinations; section navigation, diagram changes, notes toggle, and keyboard next; widths 320, 390, 760, 768, 1024, and 1440 pixels without horizontal overflow; print controls hidden; no-JavaScript text availability; no JavaScript errors. Representative desktop and mobile screenshots were visually reviewed. This verifies the presentation, not the underlying research tools or their scientific claims.
