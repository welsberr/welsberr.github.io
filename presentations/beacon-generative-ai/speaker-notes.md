# Generative AI, with receipts.

Wesley R. Elsberry · Michigan State University BEACON large group

**Status:** speaker review draft. Default timing: 30-minute core plus discussion.

## Speaker input still needed

- Confirm meeting date and available time.
- Confirm date and anecdote of first CiteGeist use; repository history begins 19 March 2026.

## Suggested pacing

- Opening, adoption, and firsthand experience: 9 minutes.
- Values and workbench: 9 minutes.
- Applications, including the TalkOrigins update workflow: 8 minutes.
- Limits and discussion setup: 4 minutes.
- For a shorter talk, keep sections 1–2, 4–6, 8–10, 12, 14–15, and 21.
- Deep Dives are optional discussion material, outside the 30-minute core. Links return to the section that opened the dive.

## 01 · Adoption — What are we delegating?

Ask the room for one task they already delegate. Distinguish a model from the application wrapped around it. This progression is a teaching model, not a historical law.

Sources:

## 02 · A shared framework for adoption — Start with the work we want to improve.

Introduce these as shared design questions before the industry overview and company example. Apply them to the speaker’s own work as well as organizational adoption. Task-specific comparisons, failure rates, escalation records, and routes to contest or correct outcomes make improvement assessable. Distinguish modeled benefits, observed changes, and causal evidence. These are proposed evaluation criteria, not findings about any company. Keep this preface constructive: the aim is to help people deliver useful work sustainably and learn from problems.

Sources:

## 03 · What the measurements mean — Private-sector adoption is uneven.

Scope confirmed by the speaker: private-sector adoption. Distinguish individual use, company integration, and demonstrated outcomes. Census changed question wording in November 2025; do not present this as an uninterrupted growth series or a GenAI-only adoption rate. The overall range spans the reporting period; the large-firm figure is the report’s size-group example.

Sources: https://www.census.gov/library/stories/2026/05/ai-use-businesses.html

## 04 · RealPage: the public account — From specialized agents to a platform.

RealPage is a commercial software company serving rental housing. Use its public announcements to illustrate a move from specialized agents toward an integrated platform. Attribute product descriptions and deployment figures to the company. Keep the public product account and the speaker’s firsthand development experience clearly attributed to their respective sources.

Sources: https://www.realpage.com/news/realpage-unveils-next-generation-ai-workforce-at-realworld-2025/, https://www.realpage.com/news/realpage-introduces-lumina-ai-suite/

## 05 · My experience: internal adoption — The developer’s work is shifting.

This section paraphrases the speaker’s supplied firsthand account of broad internal AI adoption. Keep the employer unnamed in this account and distinguish personal experience from public product announcements. Higher productivity and quality are management objectives, not measured gains reported by the speaker. The workflow is shifting; do not imply that every developer or task already follows it or that the employer endorses this presentation.

Sources: #internal-adoption

## 06 · The connection to my own work — The same concerns recur at work and at home.

Use this as the transition into the personal workbench. The overlap is in the problems being addressed; it does not imply the employer uses ClaimWright, GroundRecall, or the other personal repositories. For discussion, consider model usage cost alongside human review and rework; this is a proposed evaluation lens, not a reported company accounting practice. Do not invent expenditure figures, savings, or an achieved productivity multiplier.

Sources: #internal-adoption

## 07 · A bridge to research practice — Make scientific virtues operational.

This connection is especially relevant to BEACON, but it does not imply Pennock or MSU endorses these tools. The mapping is ClaimWright’s practical interpretation.

Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC5236068/, https://github.com/welsberr/ClaimWright/blob/836cbe8924efc694bfe5e1d6cd6c11014b7297bc/README.md

Deep Dives: ClaimWright & policy gates

## 08 · ClaimWright — Write the agreement before the output.

Avoid presenting the full claim lifecycle as an automatically enforced finite-state machine. The README explicitly identifies a configurable enforcement engine as future work. Human review remains part of the agreement.

Sources: https://github.com/welsberr/ClaimWright/blob/836cbe8924efc694bfe5e1d6cd6c11014b7297bc/README.md

Deep Dives: ClaimWright & policy gates

## 09 · Policy gating & enforcement — A gate must be able to say “stop.”

The simulation is illustrative JavaScript, not the ClaimWright or GroundRecall engine. Demonstrate that a DOI alone does not clear a publication gate. Policy evaluation alone is not enforcement; inspect which call paths actually honor its result.

Sources: https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/docs/policy-plugin-spec.md

Deep Dives: ClaimWright & policy gates

## 10 · GroundRecall + Epistemap — Remember why, not just what.

A practical retrieval loop: search, inspect provenance and date, check the current artifact, then use the result. Graph diagnostics can expose missing evidence; they cannot make bad source material reliable. Private release tags must survive export.

Sources: https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/README.md, https://github.com/welsberr/Epistemap/blob/4f5a7cd10c8aa2bc4cf4999fd9d483882c5640a6/README.md

Deep Dives: GroundRecall & Epistemap

## 11 · doclift + Didactopus — Keep the source trail through transformation.

Explain sidecars as small companion files recording structure and conversion decisions. Separate the original source from the extracted text, interpretation, and teaching artifact. A detected prerequisite still deserves review.

Sources: https://github.com/welsberr/doclift/blob/85ccadc30d0ae405846efc7d2fd4b70cdbbdd545/README.md, https://github.com/welsberr/Didactopus/blob/f0b0e8ac55459e05bdf16604ec971ea266278b84/README.md

Deep Dives: doclift & Didactopus

## 12 · CiteGeist — From a rough reference to a defensible citation.

CiteGeist’s README describes substantial implemented plumbing and remaining gaps in evaluation depth and researcher ergonomics. Do not collapse metadata matching, disambiguation, and reading for support into one “verified” badge.

Sources: https://github.com/welsberr/CiteGeist/blob/8d4b7996fab39be384be6f1acfbbdd55f6fc9756/README.md

Deep Dives: CiteGeist

## 13 · The visible trajectory — A workbench became a publication pipeline.

Invite the speaker to add the first actual CiteGeist use and the personal before/after account. Dates here are artifact evidence, not a causal study of AI productivity.

Sources: https://github.com/welsberr/CiteGeist/commit/4f3ac4d, evidence/bibliography-build.json, https://welsberr.github.io/preprints/operational-premise-taxonomy/mechanism-aware-ai-assurance-opt-preprint-20260702.pdf, https://github.com/welsberr/ClaimWright/blob/836cbe8924efc694bfe5e1d6cd6c11014b7297bc/README.md

Deep Dives: CiteGeist

## 14 · Application: TalkOrigins — A bibliography people can inspect and reuse.

Open the public page if useful, but the screenshot-free presentation works offline. Explain the stale search-engine copy found during preparation: direct live checking returned the expanded page. More citations can increase review burden; volume is not the quality measure.

Sources: evidence/bibliography-build.json, https://talkorigins.org/origins/biblio/abiogenesis.html

Deep Dives: CiteGeist, TalkOrigins updates & translation

## 15 · Application: maintaining TalkOrigins — An Archive update is a coordinated process.

Explain this as the maintenance workflow used for the modernized Archive. Keep historical author text distinct from newly added study material. Translation covers four active target languages. Workers can use GenieHive or compatible endpoints directly; do not imply every job passes through the router. The deep dives cover queue recovery, the dated public translation milestone, and model hosting. No inference-cost savings or expert translation-quality rate has been measured for this talk.

Sources: https://github.com/welsberr/CiteGeist/blob/8d4b7996fab39be384be6f1acfbbdd55f6fc9756/README.md, https://github.com/welsberr/SciSiteForge/blob/b61a4cb8b2e3e028f922ebc9d6a2b388c063f2e7/docs/GENIEHIVE_TRANSLATION.md, https://github.com/welsberr/GenieHive/blob/705e82a536e1d4ef638ce0fe4275fd755d9113e9/README.md, evidence/talkorigins-workflow.json

Deep Dives: TalkOrigins updates & translation, GenieHive & local LLMs

## 16 · Application: evolution education — Publish explanations with a route back to evidence.

This is an observed public site, not evidence of measured gains in learning. Show the beginner route to instructors and graduate students. Site frameworks can support release boundaries, but each build must still be checked.

Sources: https://evo-edu.org/notebook/, https://github.com/welsberr/SciSiteForge/blob/b61a4cb8b2e3e028f922ebc9d6a2b388c063f2e7/README.md

Deep Dives: SciSiteForge & public artifacts

## 17 · Application: learning to reusable skill — Make the learning process inspectable.

Useful BEACON research question: does a graph-grounded mentor improve unaided transfer compared with answer generation alone? Clearly distinguish the proposed human experiment from the included deterministic/synthetic demo.

Sources: https://github.com/welsberr/Didactopus/blob/f0b0e8ac55459e05bdf16604ec971ea266278b84/README.md, https://github.com/welsberr/Didactopus/blob/f0b0e8ac55459e05bdf16604ec971ea266278b84/examples/ocw-information-entropy-skill-demo/skill_demo.md

Deep Dives: doclift & Didactopus

## 18 · Application: AI assurance — Name the mechanism and its failure modes.

Use this as a conceptual bridge back to industry promises. Do not present the preprint as peer-reviewed validation. The bibliography and governed-memory tools support traceability; no controlled attribution of the paper to a particular tool is claimed.

Sources: https://welsberr.github.io/preprints/operational-premise-taxonomy/mechanism-aware-ai-assurance-opt-preprint-20260702.pdf

Deep Dives: SciSiteForge & public artifacts

## 19 · Keep the limits visible — The controls create work, too.

These are proposed evaluation dimensions, not a reported benchmark result for this stack. State the gap openly: much of the demonstrated progress is integration and artifact production.

Sources: https://github.com/welsberr/CiteGeist/blob/8d4b7996fab39be384be6f1acfbbdd55f6fc9756/README.md, https://github.com/welsberr/Epistemap/blob/4f5a7cd10c8aa2bc4cf4999fd9d483882c5640a6/README.md, https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/docs/policy-plugin-spec.md

Deep Dives: ClaimWright & policy gates, GroundRecall & Epistemap

## 20 · A BEACON-sized experiment — Try a bounded, falsifiable comparison.

Ask a postdoc, instructor, and graduate student what evidence would change their practice. The proposal should be scaled to available time; a small pilot can estimate review burden before a larger study.

Sources:

## 21 · Discussion — What would earn your trust?

Return to the task named at the beginning. Invite disagreement and specific failure cases. Leave the source appendix available for questions.

Sources:

## D1.1 · ClaimWright & policy gates — Write down what “responsible” requires.

Use the repository’s documented full-path example as an illustration. Do not present all declared claim states or checks as automatically enforced features.

Sources: https://github.com/welsberr/ClaimWright/blob/836cbe8924efc694bfe5e1d6cd6c11014b7297bc/README.md

Default return: #claimwright. When opened from another main section, the return link follows that caller.

## D1.2 · ClaimWright & policy gates — Put the check on the path to the action.

Connect back to the main talk’s teaching simulation. This is a design explanation, not a claim that every local tool or operating-system command is governed by GroundRecall.

Sources: https://github.com/welsberr/ClaimWright/blob/836cbe8924efc694bfe5e1d6cd6c11014b7297bc/README.md, https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/docs/policy-plugin-spec.md

Default return: #claimwright. When opened from another main section, the return link follows that caller.

## D2.1 · GroundRecall & Epistemap — Store a claim with the reasons behind it.

This is a conceptual record, not an export of private memory. Explain the separation between a document’s statement and a curator’s interpretation.

Sources: https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/README.md, https://github.com/welsberr/Epistemap/blob/4f5a7cd10c8aa2bc4cf4999fd9d483882c5640a6/README.md

Default return: #memory. When opened from another main section, the return link follows that caller.

## D2.2 · GroundRecall & Epistemap — Search is the beginning of checking.

The preparation example describes work performed for this presentation, not a benchmark. No private records, host names, or internal endpoints are displayed.

Sources: https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/README.md, https://github.com/welsberr/Epistemap/blob/4f5a7cd10c8aa2bc4cf4999fd9d483882c5640a6/README.md

Default return: #memory. When opened from another main section, the return link follows that caller.

## D2.3 · GroundRecall & Epistemap — A correction should reach dependent claims.

Keep implemented diagnostics separate from a claim of automatic, comprehensive stale-claim repair. Human decisions and policy remain necessary.

Sources: https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/README.md, https://github.com/welsberr/Epistemap/blob/4f5a7cd10c8aa2bc4cf4999fd9d483882c5640a6/README.md

Default return: #memory. When opened from another main section, the return link follows that caller.

## D3.1 · doclift & Didactopus — Recover structure without losing the source.

doclift owns legacy-format normalization. Its README lists RTF, higher-fidelity DOCX, old HTML, and OCR as follow-on plans, so do not imply these are all implemented.

Sources: https://github.com/welsberr/doclift/blob/85ccadc30d0ae405846efc7d2fd4b70cdbbdd545/README.md

Default return: #ingestion. When opened from another main section, the return link follows that caller.

## D3.2 · doclift & Didactopus — Turn content into a path through concepts.

This is the documented workflow and a pedagogical rationale, not a demonstrated human learning effect. Mention pack, notebook, and hybrid output modes only if useful.

Sources: https://github.com/welsberr/Didactopus/blob/f0b0e8ac55459e05bdf16604ec971ea266278b84/README.md, https://github.com/welsberr/doclift/blob/85ccadc30d0ae405846efc7d2fd4b70cdbbdd545/README.md

Default return: #ingestion. When opened from another main section, the return link follows that caller.

## D3.3 · doclift & Didactopus — Inspect a worked example end to end.

Offer the repository’s public example artifacts for inspection. Do not describe synthetic learner scores as Wesley’s or any human student’s performance.

Sources: https://github.com/welsberr/Didactopus/blob/f0b0e8ac55459e05bdf16604ec971ea266278b84/README.md, https://github.com/welsberr/Didactopus/blob/f0b0e8ac55459e05bdf16604ec971ea266278b84/examples/ocw-information-entropy-skill-demo/skill_demo.md

Default return: #ingestion. When opened from another main section, the return link follows that caller.

## D4.1 · CiteGeist — A citation starts as a candidate.

Use the two verification questions from the main section. A successful DOI lookup is evidence of identity, not necessarily of correct interpretation or relevance.

Sources: https://github.com/welsberr/CiteGeist/blob/8d4b7996fab39be384be6f1acfbbdd55f6fc9756/README.md

Default return: #citegeist. When opened from another main section, the return link follows that caller.

## D4.2 · CiteGeist — Use a question to grow a bibliography.

The repository supports citation-graph expansion and topic workflows. Avoid presenting a semantic similarity result as an argument that two papers make the same claim.

Sources: https://github.com/welsberr/CiteGeist/blob/8d4b7996fab39be384be6f1acfbbdd55f6fc9756/README.md

Default return: #citegeist. When opened from another main section, the return link follows that caller.

## D4.3 · CiteGeist — Repair an old bibliography; make it reusable.

Connect this worked application to the main TalkOrigins outcome. Citation placements repeat works across topics. The first actual date of personal CiteGeist use still awaits speaker confirmation.

Sources: https://github.com/welsberr/CiteGeist/blob/8d4b7996fab39be384be6f1acfbbdd55f6fc9756/examples/talkorigins/README.md, evidence/bibliography-build.json, https://talkorigins.org/origins/biblio/abiogenesis.html

Default return: #citegeist. When opened from another main section, the return link follows that caller.

## D5.1 · TalkOrigins updates & translation — Preserve the article; make additions legible.

Separate the historical source of record from the modernization output. This workflow description comes from inspected maintainer scripts and public artifacts; it is not a claim that every legacy statement has been newly fact-checked.

Sources: evidence/talkorigins-workflow.json, https://github.com/welsberr/CiteGeist/blob/8d4b7996fab39be384be6f1acfbbdd55f6fc9756/examples/talkorigins/README.md, https://talkoriginsarchive.github.io/foundation/2026-update/

Default return: #talkorigins-workflow. When opened from another main section, the return link follows that caller.

## D5.2 · TalkOrigins updates & translation — Translate changed content as tracked work.

Do not imply queue completion means an expert has approved the prose. Local workers can be directly addressed or reached through GenieHive. Explain a lease as a temporary claim on a work unit that can expire after interruption.

Sources: evidence/talkorigins-workflow.json, https://github.com/welsberr/SciSiteForge/blob/b61a4cb8b2e3e028f922ebc9d6a2b388c063f2e7/docs/GENIEHIVE_TRANSLATION.md

Default return: #talkorigins-workflow. When opened from another main section, the return link follows that caller.

## D5.3 · TalkOrigins updates & translation — Translation coverage and review are different records.

Figures were fetched from the public status page for this presentation. Do not convert “translated” to “expert-reviewed.” The retained evidence summary records the published timestamp and scope.

Sources: https://talkoriginsarchive.github.io/translation-status/, https://github.com/welsberr/SciSiteForge/blob/b61a4cb8b2e3e028f922ebc9d6a2b388c063f2e7/docs/GENIEHIVE_TRANSLATION.md, evidence/talkorigins-workflow.json

Default return: #talkorigins-workflow. When opened from another main section, the return link follows that caller.

## D6.1 · GenieHive & local LLMs — Host the model; route the request.

Explain local hosting without exposing internal addresses, host inventory, or credentials. The model label is an inspected configuration, not a claim that workers are online at presentation time. GenieHive’s node agent does not start or supervise upstream model servers.

Sources: https://github.com/welsberr/GenieHive/blob/705e82a536e1d4ef638ce0fe4275fd755d9113e9/README.md, https://github.com/welsberr/GenieHive/blob/705e82a536e1d4ef638ce0fe4275fd755d9113e9/docs/translation_support.md, evidence/talkorigins-workflow.json

Default return: #talkorigins-workflow. When opened from another main section, the return link follows that caller.

## D6.2 · GenieHive & local LLMs — A steady queue makes local compute useful.

No cost or speed benchmark is claimed. Do not equate an endpoint responding with a high-quality scientific translation. The queue’s recovery mechanism and GenieHive’s request scheduling are separate layers.

Sources: https://github.com/welsberr/GenieHive/blob/705e82a536e1d4ef638ce0fe4275fd755d9113e9/README.md, https://github.com/welsberr/GenieHive/blob/705e82a536e1d4ef638ce0fe4275fd755d9113e9/docs/translation_support.md, evidence/talkorigins-workflow.json

Default return: #talkorigins-workflow. When opened from another main section, the return link follows that caller.

## D6.3 · GenieHive & local LLMs — Make the routing policy inspectable.

Describe these as implemented optional capabilities in the pinned public README, not proof that every local translation worker uses the gateway profile. Connect the proposed deployment questions to the constructive adoption preface.

Sources: https://github.com/welsberr/GenieHive/blob/705e82a536e1d4ef638ce0fe4275fd755d9113e9/README.md

Default return: #talkorigins-workflow. When opened from another main section, the return link follows that caller.

## D7.1 · SciSiteForge & public artifacts — Give readers an explanation and a source trail.

Do not imply the static site publishes the entire private knowledge store. The public Notebook is an observed artifact; it does not demonstrate measured learning gains.

Sources: https://github.com/welsberr/SciSiteForge/blob/b61a4cb8b2e3e028f922ebc9d6a2b388c063f2e7/README.md, https://evo-edu.org/notebook/

Default return: #notebook-outcome. When opened from another main section, the return link follows that caller.

## D7.2 · SciSiteForge & public artifacts — Make the mechanism available for criticism.

The preprint is not peer-reviewed validation or evidence that any individual tool caused the research result. Present it as another inspectable public output.

Sources: https://welsberr.github.io/preprints/operational-premise-taxonomy/mechanism-aware-ai-assurance-opt-preprint-20260702.pdf, https://github.com/welsberr/SciSiteForge/blob/b61a4cb8b2e3e028f922ebc9d6a2b388c063f2e7/README.md

Default return: #notebook-outcome. When opened from another main section, the return link follows that caller.

## Acknowledgements

Wesley R. Elsberry defined the scope, supplied the personal experience, and directed revisions. OpenAI Codex assisted with source research and synthesis, drafting and editing, the HTML/CSS/JavaScript implementation, and browser-based checks. The social-preview artwork was generated with AI.

AI assistance can introduce factual, citation, interpretation, and software errors. Source links and verification notes support independent checking; they do not guarantee accuracy. The author retains responsibility for the presentation’s claims, editorial decisions, and final release. This version remains a speaker-review draft. No endorsement by OpenAI, Michigan State University, or the organizations discussed is implied.

### Development timeline

Repository milestones on 25 September 2026. Times are Eastern Daylight Time (UTC−04:00) and record commits, not continuous working time.

- 05:00 — Initial scrollytell draft: Main narrative, source ledger, speaker notes, and interactive policy-gate example committed. (707cf62)
- 05:25 — Private-sector scope clarified: Adoption framing revised to reflect the speaker’s correction. (4ec2d7b)
- 08:10–08:34 — Experience, design, and editorial refinement: Firsthand adoption experience added; compatible MSU web styles adopted; general evaluation questions moved into an introductory preface. (69bca4b, 2bdc443, 32e692c)
- 11:44–11:45 — Optional detail and the Archive workflow: Seven Deep Dives and the TalkOrigins update/translation section added, with caller-return navigation and a no-JavaScript refinement. (ae16bce, 4034d3f)
