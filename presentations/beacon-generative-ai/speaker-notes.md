# Generative AI, with receipts.

Wesley R. Elsberry · Michigan State University BEACON large group

**Status:** speaker review draft. Default timing: 30-minute core plus discussion.

## Speaker input still needed

- Confirm commercial/private-sector scope versus government comparison.
- Supply personal RealPage assessment and focal public statement.
- Confirm meeting date and available time.
- Confirm date and anecdote of first CiteGeist use; repository history begins 19 March 2026.

## Suggested pacing

- Opening and adoption: 7 minutes.
- Values and workbench: 11 minutes.
- Applications: 8 minutes.
- Limits and discussion setup: 4 minutes.
- For a shorter talk, keep sections 1, 3–4, 6–8, 10, 12, and 18.

## 01 · Adoption — What are we delegating?

Ask the room for one task they already delegate. Distinguish a model from the application wrapped around it. This progression is a teaching model, not a historical law.

Sources:

## 02 · What the measurements mean — Adoption is real. Measures differ.

Keep the public-sector example as a brief comparison unless the speaker confirms government adoption is a main topic. Census changed question wording in November 2025; do not present this as an uninterrupted growth series or a GenAI penetration rate.

Sources: https://www.census.gov/library/stories/2026/05/ai-use-businesses.html, https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report/microsoft-365-copilot-experiment-cross-government-findings-report-html

## 03 · RealPage: the public account — From specialized agents to a platform.

RealPage is a commercial software company serving rental housing. Treat this as a case study, not a representative sample of all industry. Avoid conflating generative/agentic systems with other algorithmic products or inferring internal practice from marketing.

Sources: https://www.realpage.com/news/realpage-unveils-next-generation-ai-workforce-at-realworld-2025/, https://www.realpage.com/news/realpage-introduces-lumina-ai-suite/

## 04 · Reading the claims carefully — What would make the promise testable?

Personal RealPage assessment is pending speaker input. These questions are proposed discussion framing, not attributed personal testimony. Ask which failure would matter most to a resident versus an operator.

Sources: https://www.realpage.com/lp/ai-workforce-agents/, https://www.realpage.com/news/realpage-introduces-lumina-ai-suite/

## 05 · A bridge to research practice — Make scientific virtues operational.

This connection is especially relevant to BEACON, but it does not imply Pennock or MSU endorses these tools. The mapping is ClaimWright’s practical interpretation.

Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC5236068/, https://github.com/welsberr/ClaimWright/blob/836cbe8924efc694bfe5e1d6cd6c11014b7297bc/README.md

## 06 · ClaimWright — Write the agreement before the output.

Avoid presenting the full claim lifecycle as an automatically enforced finite-state machine. The README explicitly identifies a configurable enforcement engine as future work. Human review remains part of the agreement.

Sources: https://github.com/welsberr/ClaimWright/blob/836cbe8924efc694bfe5e1d6cd6c11014b7297bc/README.md

## 07 · Policy gating & enforcement — A gate must be able to say “stop.”

The simulation is illustrative JavaScript, not the ClaimWright or GroundRecall engine. Demonstrate that a DOI alone does not clear a publication gate. Policy evaluation alone is not enforcement; inspect which call paths actually honor its result.

Sources: https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/docs/policy-plugin-spec.md

## 08 · GroundRecall + Epistemap — Remember why, not just what.

A practical retrieval loop: search, inspect provenance and date, check the current artifact, then use the result. Graph diagnostics can expose missing evidence; they cannot make bad source material reliable. Private release tags must survive export.

Sources: https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/README.md, https://github.com/welsberr/Epistemap/blob/4f5a7cd10c8aa2bc4cf4999fd9d483882c5640a6/README.md

## 09 · doclift + Didactopus — Keep the source trail through transformation.

Explain sidecars as small companion files recording structure and conversion decisions. Separate the original source from the extracted text, interpretation, and teaching artifact. A detected prerequisite still deserves review.

Sources: https://github.com/welsberr/doclift/blob/85ccadc30d0ae405846efc7d2fd4b70cdbbdd545/README.md, https://github.com/welsberr/Didactopus/blob/f0b0e8ac55459e05bdf16604ec971ea266278b84/README.md

## 10 · CiteGeist — From a rough reference to a defensible citation.

CiteGeist’s README describes substantial implemented plumbing and remaining gaps in evaluation depth and researcher ergonomics. Do not collapse metadata matching, disambiguation, and reading for support into one “verified” badge.

Sources: https://github.com/welsberr/CiteGeist/blob/8d4b7996fab39be384be6f1acfbbdd55f6fc9756/README.md

## 11 · The visible trajectory — A workbench became a publication pipeline.

Invite the speaker to add the first actual CiteGeist use and the personal before/after account. Dates here are artifact evidence, not a causal study of AI productivity.

Sources: https://github.com/welsberr/CiteGeist/commit/4f3ac4d, evidence/bibliography-build.json, https://welsberr.github.io/preprints/operational-premise-taxonomy/mechanism-aware-ai-assurance-opt-preprint-20260702.pdf, https://github.com/welsberr/ClaimWright/blob/836cbe8924efc694bfe5e1d6cd6c11014b7297bc/README.md

## 12 · Application: TalkOrigins — A bibliography people can inspect and reuse.

Open the public page if useful, but the screenshot-free presentation works offline. Explain the stale search-engine copy found during preparation: direct live checking returned the expanded page. More citations can increase review burden; volume is not the quality measure.

Sources: evidence/bibliography-build.json, https://talkorigins.org/origins/biblio/abiogenesis.html

## 13 · Application: evolution education — Publish explanations with a route back to evidence.

This is an observed public site, not evidence of measured gains in learning. Show the beginner route to instructors and graduate students. Site frameworks can support release boundaries, but each build must still be checked.

Sources: https://evo-edu.org/notebook/, https://github.com/welsberr/SciSiteForge/blob/b61a4cb8b2e3e028f922ebc9d6a2b388c063f2e7/README.md

## 14 · Application: learning to reusable skill — Make the learning process inspectable.

Useful BEACON research question: does a graph-grounded mentor improve unaided transfer compared with answer generation alone? Clearly distinguish the proposed human experiment from the included deterministic/synthetic demo.

Sources: https://github.com/welsberr/Didactopus/blob/f0b0e8ac55459e05bdf16604ec971ea266278b84/README.md, https://github.com/welsberr/Didactopus/blob/f0b0e8ac55459e05bdf16604ec971ea266278b84/examples/ocw-information-entropy-skill-demo/skill_demo.md

## 15 · Application: AI assurance — Name the mechanism and its failure modes.

Use this as a conceptual bridge back to industry promises. Do not present the preprint as peer-reviewed validation. The bibliography and governed-memory tools support traceability; no controlled attribution of the paper to a particular tool is claimed.

Sources: https://welsberr.github.io/preprints/operational-premise-taxonomy/mechanism-aware-ai-assurance-opt-preprint-20260702.pdf

## 16 · Keep the limits visible — The controls create work, too.

These are proposed evaluation dimensions, not a reported benchmark result for this stack. State the gap openly: much of the demonstrated progress is integration and artifact production.

Sources: https://github.com/welsberr/CiteGeist/blob/8d4b7996fab39be384be6f1acfbbdd55f6fc9756/README.md, https://github.com/welsberr/Epistemap/blob/4f5a7cd10c8aa2bc4cf4999fd9d483882c5640a6/README.md, https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/docs/policy-plugin-spec.md

## 17 · A BEACON-sized experiment — Try a bounded, falsifiable comparison.

Ask a postdoc, instructor, and graduate student what evidence would change their practice. The proposal should be scaled to available time; a small pilot can estimate review burden before a larger study.

Sources:

## 18 · Discussion — What would earn your trust?

Return to the task named at the beginning. Invite disagreement and specific failure cases. Leave the source appendix available for questions.

Sources:
