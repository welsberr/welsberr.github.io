# BEACON followup implementation roadmap

Create a 20-minute interactive scrolly-tell that shows an AI assistant completing a bounded educational task, then lets the audience inspect how the surrounding tools supported the result. Preserve the visual language and navigation of the first BEACON presentation.

**Target:** Thursday, November 19, 2026, based on “this coming Thursday” in the November 15 planning conversation. Confirm the event date and presentation slot against the invitation before freezing the title and timing.

**Planning status:** Roadmap created November 15. Implementation and rehearsal milestones below are pending. The first task is to choose and verify the source exercise; the teaching scenario is a working default.

## Deliverables and scope

Deliver a seven-scene presentation, one completed educational artifact, an inspectable work record, and a rehearsed route through both live execution and recorded results. The local presentation will support explicit actions; a portable static edition will retain the narrative, interactions with recorded evidence, and completed preview.

Use a short legacy teaching exercise to create a prediction–experiment–explanation activity for an existing Evo-Edu app. Prefer population genetics if a suitable exercise and app behavior are available. Keep the implementation to one activity and, only if necessary, one small app change. A new simulation engine or several new apps would exceed this demonstration's scope.

The assistant performs retrieval, synthesis, editing, and tool orchestration. The software supplies durable memory, document conversion records, bibliography records, instructional structure, presentation infrastructure, and executable review checks. Human decisions and unresolved findings remain visible.

The implementer prepares the artifacts and records the checks. Wesley selects the final scientific question, reviews the scientific and instructional content, rehearses the talk, and decides when the public edition is ready to release. Independent preparation can continue while those decisions are pending.

## Presentation continuity

Use the existing [presentation README](../beacon-generative-ai/README.md) and [design guidance](../beacon-generative-ai/DESIGN-GUIDANCE.md) as the baseline:

- Spartan green and white, lime accents, locally served Metropolis headings, and familiar body typography.
- Sticky desktop panels, normal scrolling, and illustrations in the reading flow on narrow screens.
- Previous/next controls, keyboard navigation, direct scene links, speaker notes, and contextual deep-dive return links.
- A source ledger, acknowledgements, print styles, reduced-motion support, and readable narrative without JavaScript.

Build the followup in this sibling directory so the first talk retains its existing content and URL. Reuse the presentation shell with focused adaptations; shared-framework refactoring can follow the talk. Update the followup's title, canonical URL, metadata, scene groups, source records, and credits rather than inheriting the first talk's claims or dates.

The existing builder duplicates visual markup for desktop and mobile, and its JavaScript contains handlers for the original gate simulation. Adapt those areas deliberately: keep a single execution state per step, avoid duplicate control IDs or duplicate jobs, and guard handlers for components that are absent. Preserve the distinction between that teaching simulation and an actual ClaimWright result.

## Scene plan and speaking budget

| Scene | Time | What appears in the panel |
| --- | --- | --- |
| The assignment | 2 minutes | Source exercise, existing app, scientific question, and three success criteria. |
| Recover the context | 2 minutes | GroundRecall result, provenance and date, and a check against current project files. |
| Bring the source forward | 2 minutes | Original exercise, doclift extraction, and a conversion issue or inspection result. |
| Build the investigation | 5 minutes | Didactopus activity structure, assistant work status, and an artifact diff or preview. |
| Challenge the claim | 3 minutes | CiteGeist candidates, supporting passages, and accepted, rejected, or unresolved decisions. |
| Run and review | 3 minutes | Usable activity, relevant checks, and actual ClaimWright findings. |
| Inspect the receipts | 3 minutes | Before/after view, tool contributions, human decisions, and remaining limits. |

The budget includes tool wait time. Optional deep dives sit outside the 20-minute core. Prepare brief narration for waits and use a labeled checkpoint if a step exceeds its rehearsed budget.

## Milestone 1 Choose and verify the task

**Target: Sunday, November 15.**

1. Select one short legacy `.doc` or WordPerfect exercise that doclift supports. Confirm that its relevant text and any figures can be displayed in the talk and included in the intended public edition.
2. Inspect the chosen Evo-Edu app and its current documentation. Identify one scientific question the app can actually investigate. Verify any required API or export behavior before promising it in the storyboard.
3. Retrieve pertinent prior decisions through GroundRecall and check them against the current repository. Select a small set of presentation-safe records; retain links to the fuller local evidence separately.
4. Set three acceptance criteria: the activity expresses a testable question, the app supports the intended investigation, and the instructional claims have a reviewable source trail.
5. Choose a clearly labeled challenge statement, such as a draft assertion of improved student learning without evaluation evidence. Decide what evidence would support it and what narrower wording would be justified.

**Exit condition:** A task brief identifies the source, app, question, expected artifact, acceptance criteria, challenge, and any source-use constraints. If no suitable legacy exercise exists, select a different real source or explicitly demonstrate doclift with a separate labeled example; do not fabricate a historical source.

## Milestone 2 Produce one complete recorded run

**Target: Monday, November 16. Depends on milestone 1.**

Run the workflow outside the presentation first. Use an isolated task directory or worktree so the result can be reset for rehearsal without disturbing ongoing Evo-Edu work.

| Component | Concrete contribution | Evidence to capture |
| --- | --- | --- |
| GroundRecall | Recover relevant prior work and decisions. | Query, selected record references, dates, and current-file verification. |
| doclift | Normalize the exercise into a structured bundle. | Source identity, extracted passage, conversion report, and any unresolved extraction issue. |
| CiteGeist | Resolve references and discover candidate literature. | Candidate identifiers and provenance, inspected evidence, and citation decisions. |
| Didactopus | Structure the draft learning activity and validate the pack. | Learning objective, prerequisites, prompts, pack output, and validation findings. |
| SciSiteForge | Assemble the activity into the site's presentation conventions. | Build inputs, rendered preview, and applicable build checks. |
| ClaimWright | Check the review record bound to the candidate artifact. | Actual checker output, unresolved findings, and the recorded basis for subsequent decisions. |

Record the assistant's edits and the human's review separately. Bibliographic metadata matching does not establish claim support; pack validation does not establish learning effectiveness; a passing publication check does not itself grant publication permission.

**Exit condition:** One real run produces a usable local artifact and complete evidence records. Review the preview in a browser. Mark integration gaps explicitly and fix the necessary ones before wrapping the workflow in a live interface. Capture actual failures or unresolved findings without editing them into successes.

## Milestone 3 Build the static scrolly-tell

**Target: Monday–Tuesday, November 16–17. Shell work can proceed alongside milestone 2.**

Create the seven scenes and speaker notes using the prior presentation's shell. Load the completed run into reusable panels for source comparison, retrieved context, candidate citations, activity structure, preview, checks, and the final work report.

Give each result a text label stating **Live run**, **Recorded rehearsal**, or **Illustrative example**. Show the capture date and relevant source or artifact reference. Readers should be able to inspect a source passage, a citation decision, and a changed artifact without opening a raw terminal transcript.

Use a consistent panel pattern: action or question, current result, evidence link, and unresolved issue when one exists. Show a concise status while work is running. Detailed logs belong in an optional inspector or deep dive.

**Exit condition:** The entire talk works from recorded artifacts, including the final activity preview. Scene navigation and source inspection work without any local tool service. The narrative and source ledger remain readable with JavaScript disabled.

## Milestone 4 Connect bounded live execution

**Target: Tuesday, November 17. Depends on the working workflow and panel contract.**

Implement a small local runner that serves the presentation and exposes only the selected workflow actions. Keep credentials and private project state outside the static presentation. Bind the runner to loopback and validate the origin and session for action requests. The browser submits named actions and validated inputs, not arbitrary shell commands or file paths.

Start with three live actions: retrieve context, produce the bounded draft change, and run the relevant checks. Add live conversion or citation retrieval only after measuring their reliability and latency. Steps may remain recorded when that improves pacing, with their status clearly labeled.

The draft action must invoke the actual assistant workflow. Fixed conversion and validation commands should identify themselves as such. If a suitable assistant connection is unavailable, use the assistant application alongside the presentation and import its outputs, or use labeled recorded results; do not simulate live agent activity.

Keep scrolling and execution independent. Actions start only through explicit controls. Handle pending, running, completed, failed, cancelled, and recorded-checkpoint states. Returning to a scene, resizing the window, reloading, or double-clicking must not create duplicate work. Capture partial output on failure. Treat cancellation as complete only when the underlying work has stopped or its continuing status is explicitly reported.

**Exit condition:** A real action updates its panel, writes its work record, and survives navigation without replaying the job. A failed or slow action offers an explicit switch to a labeled checkpoint. The static edition never attempts to call the local runner.

## Evidence contract and proposed file layout

Use the same result shape for recorded and live runs. Each step record should include its run and step identifiers, mode, timestamps, input references or hashes, tool and version where available, result status, output artifact references, review decisions, and unresolved findings. Record model identity and usage only when the runtime actually supplies them.

Link each result to the exact artifact it describes. A change to the artifact must invalidate or supersede a review that was bound to the previous version. Keep original run records when producing a corrected result. Record the relationship between the two runs.

Proposed files in this directory:

| Path | Purpose |
| --- | --- |
| `content.json`, `build.py` | Scenes, source ledger, notes, metadata, and static generation. |
| `style.css`, `presentation.js` | Familiar presentation design, navigation, and panel behavior. |
| `demo/scenario.json` | Selected exercise, bounded actions, acceptance criteria, and checkpoint references. |
| `demo/result.schema.json` | Shared structure for live and recorded step results. |
| `runner/` | Local execution adapters and action service. |
| `evidence/rehearsal/` | Reviewed, sanitized records usable by the static presentation. |
| `preview/` | Portable completed artifact, including its required assets. |
| `tests/` | Focused checks for navigation, action lifecycle, replay, and export. |
| `RUNBOOK.md` | Startup, preflight, reset, checkpoint selection, and recovery instructions. |

Store private execution logs and working memory outside the publishable site tree. Create the public evidence bundle from an explicit selection of approved fields and artifacts. Review both visible text and downloadable files before publication.

## Milestone 5 Verify and rehearse

**Target: Wednesday, November 18. Depends on milestones 2–4.**

Run checks appropriate to the changes and rehearse the actual presentation path:

- Verify the scientific activity and its acceptance criteria against the source material and working app. Run the existing relevant app tests if application code changes.
- Check scene links, notes, deep-dive returns, source links, print output, keyboard behavior, reduced motion, and responsive layouts. Inspect a narrow screen and the intended projector layout. Announce status changes accessibly without stealing focus from the presenter.
- Verify that desktop and mobile controls share one execution state; reloads and duplicate clicks do not repeat an action; and stale results cannot silently replace a newer run.
- Exercise one real failure or timeout. Switch explicitly to recorded evidence and continue the talk. Test recovery without losing the selected scene or mislabeling a checkpoint as live.
- Disconnect the runner and network, then traverse the portable recorded edition and completed preview. Include source excerpts or permitted local material needed to tell the story offline; external full sources can remain linked.
- Confirm that the public bundle excludes private memory, credentials, machine paths, and unreviewed raw output. Check the exact exported artifact rather than only the live screen.

Complete two timed rehearsals: one with live actions and one using checkpoints. Record actual durations and revision needs. Aim for an 18-minute delivery to leave two minutes for audience interaction and recovery. Shorten narration or reduce live scope when the measured route exceeds 20 minutes.

**Exit condition:** Both routes complete within the allotted time, the final artifact works, and the presenter can explain each tool's contribution from its records. Freeze dependencies, the baseline task, checkpoints, and presentation content after the final rehearsal.

## Milestone 6 Present and prepare the public edition

**Target: Thursday, November 19, with publication after content review.**

Before the talk, run a short preflight: open the presentation, confirm the chosen task baseline, check the local runner and required tools, open the completed preview, and verify the recorded fallback. Use the rehearsed configuration.

During the talk, show live and recorded status explicitly. Preserve the run record and human decisions. Finish on the completed artifact and a concise report of changes, evidence, checks, and remaining limits.

Afterward, select and sanitize the actual demonstration results, identify any rehearsal material retained, and rebuild the static edition. Wesley reviews the concrete public artifact before release. Add a link from the first presentation only when the followup is ready to publish.

**Exit condition:** A reviewed portable presentation preserves the work and its evidence, with accurate credits and an explicit distinction between recorded execution and illustrative material.

## Priority and fallback rules

The critical path is **verified task → complete recorded workflow → static presentation → bounded live actions → timed rehearsal**. Do not spend the rehearsal window expanding the tool integrations.

If the local assistant bridge is not reliable by Tuesday evening, use the presentation to frame the task, perform the bounded work in the assistant application, and return to panels populated from the actual outputs. Keep that transition in the rehearsal. If live execution is unavailable on Thursday, present the recorded workflow openly and retain interactive inspection of the evidence and artifact.

Defer audience branching, a live run of every component, extra app features, live production deployment, new infrastructure, and shared-framework extraction until the core route is reliable. One audience choice between two prepared scientific questions is optional only if both branches have complete artifacts and rehearsals.

## Definition of done

- [ ] One scientifically coherent activity works in the chosen app context.
- [ ] Seven scenes maintain recognizable continuity with the first talk.
- [ ] The audience can trace a source passage, a citation decision, an artifact change, and a check result.
- [ ] Live actions perform real work and cannot be triggered accidentally by navigation.
- [ ] Recorded fallback is complete, portable, and visibly labeled.
- [ ] A substantive challenge leads to a justified revision or an explicit unresolved finding.
- [ ] The final report distinguishes assistant work, software contributions, and human decisions.
- [ ] Two timed rehearsals and the targeted functional and accessibility checks are complete.
- [ ] The static edition is reviewed for public release and preserves the source trail.

The demonstration establishes what this workflow produced and what its records make inspectable. Claims about productivity gains or learning outcomes would require separate evaluation.
