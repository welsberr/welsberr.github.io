# BEACON followup presenter runbook

This is a working demonstration. Instructor and scientific review, source-use review, and two timed rehearsals remain. The initial ClaimWright check returned a hard gate; the SciSiteForge build is a draft. Publication of the demonstration does not imply approval of the instructional material.

## Start the local presentation

From this directory run `python3 runner/server.py` and open `http://127.0.0.1:8769/`. The server binds only to loopback. In the review scene, the button runs the bundled population-genetics API tests; the displayed result is marked live. If a source checkout is available, the runner compares its API with the bundled copy; otherwise it reports that the independent comparison is unavailable. Set `BEACON_SOURCE_API` to the source API path to override the default location. It does not run the assistant, GroundRecall, or a publication gate. Other evidence panels display the recorded development run. Each live check appends a sanitized record under `~/.local/state/beacon-followup/check-runs.jsonl`.

Scroll or use the previous/next buttons or arrow keys. Alt+N toggles speaker notes. Open the activity from scene 4; select “Add a run” several times to accumulate rows for both treatments and their paired differences. Each new run uses the next seed. The pooled difference is the fitness-difference mean minus the equal-fitness mean. The plot shows cumulative means and their difference after each run; use the expandable explanation to introduce Monte Carlo simulation. The activity runs locally using a copy of the Evo-Edu population-genetics API. The full Allele Tracker link requires network access and its external dependencies. Links leaving the talk open named tabs for the activity, source pages, evidence, site preview, or presenter notes. The activity’s return link brings the talk tab to scene 4. Reopening the activity link reloads that tab and clears its in-page results.

The GitHub Pages version is static: the activity and recorded evidence work there, while the live-check button requires the local runner.

## Fallback

If the local runner or network is unavailable, serve this directory with any ordinary static server. The review scene will display the recorded result and the activity will still run locally. Do not label recorded results as live. If JavaScript is unavailable, the narrative and source trail remain readable, but the activity and buttons do not operate.

## Before the talk

1. Review the activity's scientific content and its interpretation with a subject expert. Confirm permission to reuse or distribute the copied API and source references.
2. Resolve citation support and review the actual source, rather than promoting a metadata candidate. Confirm that the challenge's revised wording is defensible.
3. Complete the ClaimWright human review and rerun it against the final artifact. Inspect and review the SciSiteForge local preview before release.
4. Decide whether to demonstrate the assistant in its own application; no live assistant bridge is implemented here. Prepare a bounded task, a resettable workspace, and a recorded checkpoint before adding one.
5. Rehearse live and recorded routes with a timer. Check projection, controls, network, fonts, and the actual result panels. The 20-minute target has not yet been measured.
6. Review the exact public bundle after subsequent changes; keep private memory, credentials, and unreviewed raw output out of it.

The Avida-ED manual conversion is a separate example, not the source of the population-genetics lesson. The conversion flagged no text-quality problems, but figures and rights still require inspection. The selected GroundRecall result was a lead and the current app guide was checked independently.

## Rebuild the SciSiteForge preview

Run `python3 "$SCISITEFORGE_DIR/scripts/build.py" --config demo/scisiteforge.json --output forge-preview` with `SCISITEFORGE_DIR` set to your SciSiteForge checkout. For nested local use, adjust the generated `index.html` root-relative `/theme/` links to `theme/` and its home link from `/` to `./`. Remove the default license claim and empty contact links until the appropriate terms and contacts are confirmed. Add `target="beacon_activity"` to the `../preview/` activity links in the generated landing page. In `translation-status/index.html`, use `../theme/` for assets, `../` for the preview home, and `../../preview/` with the same named target for the activity. The build does not deploy anything.

## Rebuild the pack viewer

After changing any file in `pack/`, re-run Didactopus `validate_pack`, update the recorded validation and file hashes, then run `python3 tools/build_pack_viewer.py`. Run `python3 tools/build_pack_viewer.py --check` to detect stale viewer content or validation. The viewer is static and works offline. Structural validation does not replace scientific or instructional review.

## Optional Avida-ED 5 follow-on

After the core discussion, use the optional three scenes if time permits (roughly 5–6 additional minutes). Open the prototype in its named tab before the talk; the first launch may reload while the service worker enables shared memory. Show a 0% run with seed 42 and, if time permits, compare a completed 1% run. A prepared comparison is useful if the live run takes too long.

Use the project’s evidence page to distinguish direct implementation from adapted localization methods, context and guidance, and tools without an established direct role. End with the visual audit’s concrete repairs and the documented Analysis/tutorial-parity gaps. The prototype is not a classroom-ready replacement and this case does not measure productivity or learning gains.

## Optional TalkOrigins and OPT walkthroughs

After the core presentation, jump directly to either optional branch. The TalkOrigins branch has five scenes; OPT has two. The expanded durations have not been rehearsed. The links preserve the main presentation in its tab.

For TalkOrigins, open the Abiogenesis HTML and BibTeX outputs, then show the recorded CiteGeist DOI verification for Hodgson and Baker (1967). It is a separate lookup for the walkthrough; it did not change the site and does not establish claim support. Show the original research scene and the historical 20-concept, ten-language record: phrase inventory, linked multilingual sources, provisional versus approved workbench statuses, and separate bookseller/Library of Congress title evidence. Then show the distinct later runner glossary and its four-language table; do not imply the two files are identical or that one was generated from the other. Trace the selected language targets into the model prompt and discuss review. The Spanish sentence is a recorded local probe listed before the compendium was added; it does not prove glossary adherence. The maintainer note reports a later page smoke test using glossary terms. The workflow and translation snapshot are dated records; the status link is a separate live view.

For OPT, show the substantive revision first, then the blocked PDF check and the passing check against the same hash. Explain the extraction-binding repair, its limits, and the separate final author approval. The chronological records distinguish the earlier pending release from the later publication.

## Optional Ballot Commons walkthrough

The presenter authorized use of his own address in the real case. The recorded October 2026 address-only lookup led to a precinct-matched public ballot preview; the voter-specific school-district ballot was not established. The election is historical. The detailed private report is not included in the public bundle.

Open the case viewer to show the evidence chain, then the separate fictional strict ledger output. The fictional jurisdiction check passed, while a candidate-position claim required review and strict mode returned status 2. These checks do not verify the real ballot. The repository’s own schemas and checks are evidenced; do not attribute them to a named external stack tool without a supporting record. The example has not been timed in rehearsal.
