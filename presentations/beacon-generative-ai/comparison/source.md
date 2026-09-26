# What this framework contributes

An evidence-based comparison of eight repositories and their alternatives, prepared after the Michigan State University BEACON discussion. Assessment date: **26 September 2026**. **Author-approved public report.**

## Assessment {#assessment}

The modest version of Wesley Elsberry’s assessment is supported: these projects form a useful, deliberately integrated approach to responsible AI-assisted work, and people with similar needs may find value in them. Their strongest potential contribution is the connection between evidence, review, durable memory, learning, and release decisions. The evidence does **not** establish that the components are unprecedented, generally superior, or the easiest choices for another laboratory.

The timing claim about Didactopus is accurate when stated precisely. A first-class knowledge-graph implementation was committed on **16 March 2026**, **19 calendar days** before Karpathy’s **4 April** LLM Wiki gist. That establishes an earlier recorded implementation than this particular publication. It does not establish priority for knowledge graphs, learning graphs, or LLM-assisted knowledge management. [Didactopus commit](https://github.com/welsberr/Didactopus/commit/41ca57d60fa2a68d323a140950f18f5eec44f0f9); [Karpathy’s gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

“The infrastructure was still developing” is a reasonable description of the environment. “Little comparable infrastructure existed” would be too broad. Persistent agent memory was already a research topic in [MemGPT (2023)](https://arxiv.org/abs/2310.08560), and temporal graph memory in [Zep (2025)](https://arxiv.org/abs/2501.13956). Provenance standards, policy engines, reference managers, and adaptive tutoring have longer histories. Contemporary products still differ substantially in how they combine these capabilities.

A defensible self-description would be:

> I specified and iteratively developed this workflow around my own research, learning, and publication needs, with AI assistance. Some implementations preceded particular later descriptions of similar patterns. Existing packages overlap substantially with individual components. What I can offer is a working integration with explicit evidence, review, and release practices—not a demonstrated best-in-class replacement for every component. Its usefulness to another group should be established through a small, reproducible trial.

The first sentence reflects the developer’s account. Repository history can establish recorded changes and implementation choices; it cannot independently apportion intellectual contribution between a human and an assistant. A stronger contribution record would preserve requirements, design decisions, rejected alternatives, review corrections, and AI assistance alongside commits.

## What the remembered article supports {#article}

The confirmed article is [“Why your AI agent sucks,” Supercompanies with Greg & Taylor, 27 August 2026](https://supercompanies.substack.com/p/why-your-ai-agent-sucks). Its Section example concerns accessible company material that remains difficult for an agent to interpret: obsolete versus current, internal versus client-facing, and draft versus authoritative. The author describes work still needed in Section’s own information environment.

That is a close match to the problem GroundRecall addresses through explicit status, provenance, review, and release metadata. It supports the relevance of the design. It is a practitioner account, not a systematic survey demonstrating that other packages lack solutions. Existing governance features also do not automatically make an organization’s content authoritative: people must establish owners, label material, resolve conflicts, and maintain the rules.

Three meanings of “governance” need to remain separate:

| Question | Example control |
|---|---|
| Who may access or change this? | Identity, permissions, tenant separation |
| Why should this be believed or reused? | Evidence, review state, conflicting claims, freshness |
| Where may this information go? | Release classification, redaction, export and publication gates |

An access-control system can be strong without providing scholarly claim review. Conversely, a well-designed review schema is not a security boundary unless the relevant operations enforce it.

## Repository comparison at a glance {#comparison}

“Best alternative” here means the strongest starting point for the named task among the reviewed candidates. These are fit judgments, not measured rankings. Some alternatives replace a component; others are building blocks to combine.

| Repository | Start by comparing with | Reason to retain this project |
|---|---|---|
| [ClaimWright](#claimwright) | Open Policy Agent; Cedar; NeMo Guardrails | Research-specific operating agreement and publication review |
| [GroundRecall](#groundrecall) | SuperLocalMemory; Graphiti/Zep; Mem0; Cortex; Letta | Claim lifecycle, stewardship, policy-aware reuse and release |
| [Epistemap](#epistemap) | RDFLib + PROV-O + pySHACL | Shared graph and assessment vocabulary across this workflow |
| [Didactopus](#didactopus) | OATutor; NotebookLM / Google Notebook | Reviewed source-to-curriculum pipeline and learner evidence |
| [CiteGeist](#citegeist) | Zotero + Better BibTeX; JabRef; GROBID | Scriptable citation repair, provenance and archive integration |
| [doclift](#doclift) | Apache Tika; Docling; Unstructured | Legacy-document review bundles and downstream adapters |
| [GenieHive](#geniehive) | LiteLLM; GPUStack | Role-based routing over an existing local model fleet |
| [SciSiteForge](#scisiteforge) | Quarto; Jupyter Book / MyST | Legacy science-archive integration and custom public interfaces |

### ClaimWright: research policy and accountable release {#claimwright}

The [public snapshot](https://github.com/welsberr/ClaimWright/tree/366d19e47cc9db8cc6f75b0c262cf84b6c0b4917) supplies a collaboration agreement, claim states, several dimensions of confidence, role definitions, policy files, a substrate checker, and an executable offline publication gate. The gate binds review records to artifacts and policy versions, retains similarity findings, checks destination requirements, and preserves pass, hard-gate and deny outcomes. It does not enforce every policy described in prose.

**Availability gap closed on 26 September 2026.** The gate was previously on a public feature branch and draft PR, rather than public `main`; the first version of this report described it too narrowly as local-only. After inspection, fixes and **23 passing tests** in both the working repository and a clean checkout, [PR #1](https://github.com/welsberr/ClaimWright/pull/1) was merged. [GitHub CI](https://github.com/welsberr/ClaimWright/actions/runs/36220079481) checks the published revision. The [validation record](https://github.com/welsberr/ClaimWright/blob/366d19e47cc9db8cc6f75b0c262cf84b6c0b4917/docs/validation-2026-09-26.md) describes tested cases and limits.

| Alternative | Feature difference and best fit |
|---|---|
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | General policy decisions over structured inputs, with [decision logging](https://www.openpolicyagent.org/docs/management-decision-logs). Strong candidate for reusable enforcement across services or CI. A team must still write the research-specific policy and enforce decisions at each operation. |
| [Cedar](https://docs.cedarpolicy.com/) | A focused authorization language and schema validation: useful for deciding which principal may perform which action on which resource. It does not supply ClaimWright’s scholarly review agreement. |
| [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | Programmable input, dialogue, retrieval, tool-execution, and output rails. Better aligned with runtime assistant behavior; it is complementary to artifact-level publication review. |

**Assessment:** retain ClaimWright for its policy content and human accountability model. Reuse a general policy engine where that reduces custom enforcement code. Do not infer scientific truth, adequate attribution, or actual human approval merely because a review record validates. The published CLI now has regression evidence for pass, blocked and denied workflows. External adoption still needs user trials and a supported release process; a merged revision is not a security certification. Non-text artifacts remain gated because this version cannot verify their extracted text.

### GroundRecall: governed research memory {#groundrecall}

The [public snapshot](https://github.com/welsberr/GroundRecall/tree/68ef5744306f247ddbf9cc3a114d7a520331f4c2) represents artifacts, observations, claims, concepts, and relations; combines indexed search with graph context; and supports review, promotion, confidence, supersession, and release-aware workflows. Its [policy interface](https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/docs/policy-plugin-spec.md) distinguishes allow, review, soft gate, hard gate, and deny decisions. This is more specific than retaining conversation summaries.

| Alternative | Feature difference and best fit |
|---|---|
| [SuperLocalMemory](https://github.com/qualixar/superlocalmemory) | The closest broad local-memory comparison reviewed: SQLite storage, several retrieval channels including graphs, workspaces, governance, audit and retention controls. Its current documentation materially weakens any claim that governed local memory is absent elsewhere. Compare its actual admission and context rules with GroundRecall’s claim-review and release semantics. |
| [Graphiti](https://github.com/getzep/graphiti) / Zep | Strong comparison for temporal graph memory: source episodes, changing facts, validity intervals and hybrid retrieval. Graphiti is the self-managed library; Zep provides a managed service with additional operational features. Graph provenance does not by itself reproduce a particular human promotion or publication policy. |
| [Mem0](https://github.com/mem0ai/mem0) | Focuses on extracting and retrieving reusable memory. Its [graph option](https://docs.mem0.ai/open-source/features/graph-memory) supplements vector retrieval. Appropriate when automatic memory integration is the main need; determine separately how review, classification and public release will be enforced. |
| [Cortex](https://github.com/Obelyth/Cortex) | Particularly relevant for accountable notes: Git-backed Markdown, trusted and guest MCP access, a proposal/acceptance queue, and quoted-source checks. It demonstrates that review-before-write and verifiable citations are available in other projects. Its note-oriented model differs from GroundRecall’s explicit claims and relations. |
| [Letta](https://docs.letta.com/v1-sdk/concepts/stateful-agents) | Agent-managed persistent context blocks and retrievable history. A useful choice when the application is organized around persistent agents rather than a shared research claim store. |

Knowledge graphs are therefore **not universal**, but neither are they rare enough in the reviewed set to establish distinctiveness on their own. The worthwhile comparison is what a relation means, how it was derived, when it is invalidated, and which uses are permitted.

GroundRecall’s enforcement is integration-dependent. Its public HTTP adapter owns policy configuration and caller identity, but describes itself as a bounded local/private pilot. The policy specification documents selected integrated operations, not an independently audited guarantee that every path is covered. New uncommitted broker and application work was excluded from this assessment. See the [pinned HTTP adapter](https://github.com/welsberr/GroundRecall/blob/68ef5744306f247ddbf9cc3a114d7a520331f4c2/src/groundrecall/mcp_http.py).

**Assessment:** this is among the most defensible projects to demonstrate to peers, especially through a stale-source or prohibited-export example. Test it against SuperLocalMemory and Cortex for review/governance, and Graphiti for temporal retrieval. None of these comparisons establishes a winner without common tasks. SuperLocalMemory’s older-version benchmark figures were not treated as validation of its current version; Cortex’s citation checks establish textual occurrence, not truth or entailment.

### Epistemap: a shared representation {#epistemap}

The [public snapshot](https://github.com/welsberr/Epistemap/tree/4f5a7cd10c8aa2bc4cf4999fd9d483882c5640a6) supplies typed graph bundles, nodes, edges, provenance references, status, confidence assessments, traversal and diagnostic utilities. Its value within this collection is a shared vocabulary for moving evidence between applications. It deliberately sits below decisions such as whether a learner has mastered a concept or a claim should be promoted.

The strongest standards-based alternative is a composition: [RDFLib](https://rdflib.readthedocs.io/en/stable/) for RDF graphs and querying, [W3C PROV-O](https://www.w3.org/TR/prov-o/) for provenance, and [pySHACL](https://github.com/RDFLib/pySHACL) for validating graph constraints. That route offers wider semantic-web interoperability; a team must define its domain vocabulary and mappings. Epistemap offers a smaller, opinionated application schema already aligned with the other repositories.

**Assessment:** retain it where those adapters save real work. Prefer the standards stack where exchange with institutional repositories or external graph tools dominates. Exporting to PROV-O/SHACL could make these complementary. Provenance graphs predate this project; neither typed confidence nor a Bayesian assessment field should be presented as a calibrated probability of truth without validation.

### Didactopus: learning from sources rather than collecting answers {#didactopus}

The [public snapshot](https://github.com/welsberr/Didactopus/tree/f0b0e8ac55459e05bdf16604ec971ea266278b84) connects source ingestion to reviewed domain packs, concepts and prerequisites, merged learning graphs, practice, assessment, and learner evidence. Mentor, practice and evaluator roles make the intended learning process explicit. This is a useful distinction from simply asking a model to explain a document. Demonstrations and software tests do not establish improved student learning or protection against cognitive offloading.

| Alternative | Feature difference and best fit |
|---|---|
| [OATutor](https://github.com/CAHLR/OATutor) | Open adaptive tutoring with knowledge components, Bayesian knowledge tracing, authored problems and hints, and classroom/research integration. Its repository links published research and existing course content. A stronger starting point for an instructor seeking an established tutoring experiment; subject-specific content still requires work. |
| [NotebookLM / Google Notebook](https://support.google.com/gemininotebook/answer/16206563?hl=en) | A hosted source-study interface with quizzes, flashcards, mind maps and other generated study materials. Convenient for students exploring supplied sources. The inspected help documents do not establish an equivalent user-controlled graph schema, review-to-promotion pipeline, or learner-evidence export contract. |

Karpathy’s [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) is a design pattern for maintaining linked knowledge from sources, not a packaged adaptive tutor. It is useful related work, but a weak sole comparator for Didactopus’s learning goals.

**Assessment:** offer Didactopus as a researchable source-to-learning workflow, not a demonstrated remedy for reduced cognition. For a course, begin with one concept cluster, instructor-reviewed prompts and assessments, and an unaided delayed test. Compare both the learning outcome and the instructor’s preparation burden with OATutor or a simpler study workflow.

### CiteGeist: a bibliography workbench {#citegeist}

The [public snapshot](https://github.com/welsberr/CiteGeist/tree/8d4b7996fab39be384be6f1acfbbdd55f6fc9756) combines rough citation intake, identifier resolution, metadata enrichment, conflicts and field provenance, citation discovery, and reviewed export through CLI/MCP workflows. Its practical niche is repairing and maintaining bibliographies in an automated publication pipeline, including the TalkOrigins work described in the presentation.

| Alternative | Feature difference and best fit |
|---|---|
| [Zotero](https://www.zotero.org/support/) + [Better BibTeX](https://retorque.re/zotero-better-bibtex/) | Strong default for a research group’s shared reference collection, attachments, annotation and writing integration. Better BibTeX adds customizable citation keys and automated exports. CiteGeist’s case rests on the particular scripted reconciliation and provenance workflow, not exclusive access to BibTeX automation. |
| [JabRef](https://www.jabref.org/) | A BibTeX-oriented desktop manager with [catalog search, identifier lookup and import inspection](https://docs.jabref.org/collect/import-using-online-bibliographic-database). A close alternative for people wanting visible review and bibliographic editing without assembling an agent workflow. |
| [GROBID](https://grobid.readthedocs.io/en/latest/Introduction/) | A specialized parser for scholarly PDFs and reference strings, with structured outputs and metadata consolidation. It can replace or strengthen extraction within a workbench; it is not a complete substitute for collection stewardship and publication review. |

**Assessment:** keep CiteGeist for archive-scale maintenance and explicit reconciliation records; start a new lab with Zotero or JabRef unless its requirements justify the extra infrastructure. Measure difficult citation matches, incorrect confident matches, field conflicts and human correction time. Matching a DOI verifies an identity candidate; it does not verify that the cited work supports the surrounding claim.

### doclift: legacy sources with review context {#doclift}

The [public snapshot](https://github.com/welsberr/doclift/tree/85ccadc30d0ae405846efc7d2fd4b70cdbbdd545) targets older Word and WordPerfect documents. It wraps conversion tools, produces text/Markdown and review sidecars, and carries conversion warnings and document structure into downstream workflows. Its current value is the review bundle and integration, not a new document parsing engine. Planned format or OCR work should remain labeled as planned.

| Alternative | Feature difference and best fit |
|---|---|
| [Apache Tika](https://tika.apache.org/3.3.0/formats.html) | Broad format detection and text/metadata extraction, including legacy Word and WordPerfect. A strong first comparison for heterogeneous archival collections. |
| [Docling](https://docling-project.github.io/docling/) | Structured conversion with layout, tables and OCR capabilities. Its current [CLI lists DOC and RTF inputs](https://docling-project.github.io/docling/reference/cli/), so “supports old Word files” is not a sufficient differentiator for doclift. |
| [Unstructured](https://docs.unstructured.io/open-source/core-functionality/partitioning) | Partitions documents into typed elements. Its DOC path uses LibreOffice conversion before DOCX processing, overlapping doclift’s use of existing converters. |

**Assessment:** preserve doclift’s manifests, quality flags, and adapters where they simplify historical-source review. Compare the same damaged documents, tables and footnotes before choosing an extraction backend. A successful conversion exit code is not evidence that the reading order, figures, or citations survived accurately.

### GenieHive: directing work to local models {#geniehive}

The [public snapshot](https://github.com/welsberr/GenieHive/tree/a664348180501277d5ec793b7a548d9d4931b977) provides a registry of hosts/services and role-based routing across configured model endpoints, with health, loaded-model and benchmark information. Its optional Foundation profile adds client keys, model/operation scopes, request auditing and opt-in budgets; these are disabled in the casual example configuration. It proxies supported inference requests; it does not itself become the process supervisor for every upstream model server. Local model hosting in the TalkOrigins translation workflow also depends on those model runtimes and the separate translation queue.

**Availability gap closed on 26 September 2026.** Versioned role/model evaluation contracts and case-level results are now on public `main`, with dataset and evaluator identity, pass thresholds and declared hard-failure overrides. **119 tests passed** in the working repository and a clean checkout, and [GitHub CI passed](https://github.com/welsberr/GenieHive/actions/runs/36220017827). The [validation record](https://github.com/welsberr/GenieHive/blob/a664348180501277d5ec793b7a548d9d4931b977/docs/validation-2026-09-26.md) distinguishes deterministic checks from model qualification. The public catalog contains four synthetic starter cases; the larger role matrix remains planned. No live model quality, GPU performance or production routing was evaluated in this validation.

| Alternative | Feature difference and best fit |
|---|---|
| [LiteLLM](https://docs.litellm.ai/docs/routing) | A close gateway comparison for routing, fallback and provider abstraction. Its [virtual-key facilities](https://docs.litellm.ai/docs/proxy/virtual_keys) add model access and budget controls. Compare required deployment dependencies and edition-specific features before treating it as an interchangeable service. |
| [GPUStack](https://docs.gpustack.ai/latest/overview/) | A broader model-deployment and GPU-cluster manager, including inference-engine orchestration, scheduling, monitoring and access control. Better aligned with managing the fleet itself than merely directing requests to already-running services. |

**Assessment:** GenieHive is a plausible lightweight fit for the developer’s existing machines and roles. Routing, load awareness and cost control are established categories; its advantage must be shown through lower operational effort or better task outcomes in this particular setting. The newly published evaluation contracts improve traceability, but a deterministic contract pass does not establish semantic correctness or authorize model promotion. Native protocol support and stronger deployment controls must be assessed from implemented adapters, not roadmap aspirations.

### SciSiteForge: publishing a science archive {#scisiteforge}

The [public snapshot](https://github.com/welsberr/SciSiteForge/tree/b61a4cb8b2e3e028f922ebc9d6a2b388c063f2e7) collects a static science/OER publishing approach: site shells, bibliography integration, language status/fallback conventions, and patterns for notebooks and interactive applications. Some capabilities are patterns implemented in consuming sites rather than a centrally packaged framework. The entire TalkOrigins update and translation system should not be attributed to this repository alone.

| Alternative | Feature difference and best fit |
|---|---|
| [Quarto](https://quarto.org/docs/books/) | A strong default for a new scholarly site or course book, with citations, cross-references, executable content, multiple output formats and web navigation. It reduces the amount of publishing infrastructure a course team must maintain. |
| [Jupyter Book / MyST](https://mystmd.org/guide) | A strong comparison for computational teaching materials, notebooks, structured citations and cross-references, interactive web content and publication exports. Existing content may need conversion into the chosen authoring system. |

**Assessment:** retain SciSiteForge where legacy URLs, archive structure, bibliography pages and custom public applications drive requirements. For a new course without that legacy, start by evaluating Quarto or MyST. The value of the existing TalkOrigins integration is real as a local accomplishment, but another institution’s migration cost and usability remain unmeasured.

## What to offer a course or laboratory {#adoption}

The most useful invitation is to evaluate a small part of the workflow with ordinary course material. Adoption need not require all eight repositories.

1. **Teach the policy first.** Give students a short ClaimWright-derived agreement: disclose assistance, retain sources, separate drafts from accepted knowledge, and remain responsible for claims. This can be used with other tools.
2. **Demonstrate one governed-memory case.** Introduce an obsolete source and a corrected source, then show retrieval, review and correction. Add a synthetic restricted item and test whether an inappropriate export is denied. Compare the same case with the closest alternative.
3. **Evaluate one learning module.** Compare Didactopus with an existing course workflow using unaided explanation, delayed recall and transfer—not just completion speed or satisfaction. This is a proposed evaluation, not a claim of established efficacy.
4. **Count the whole cost.** Record setup and maintenance time, student friction, review effort, model use, failures and recovery. Provider savings can be outweighed by maintenance; a richer graph can be outweighed by annotation burden.

For external adoption, the immediate deliverables are versioned releases, synthetic example data, a short installation path, policy-denial examples, export/restore instructions, and a clear support boundary. A documented failure and correction is more informative than another capability list.

## Evidence, provenance and limits {#provenance}

This is a bounded documentary and source-code comparison with targeted software regression validation for ClaimWright and GenieHive. It is not a systematic market review, security audit, usability study, or performance benchmark. Official documentation and repository source were preferred over third-party rankings. Own-project history and selected implementation files were inspected locally; public main revisions were checked separately. Alternatives were assessed from their official documentation/source pages, without installing and running a common evaluation suite. Their feature descriptions therefore establish **documented capability**, not independently verified reliability.

The current alternatives comparison asks what a prospective adopter can use **now**. It does not reconstruct every competitor’s feature set on the date each personal repository began. “Not located in the inspected documentation” is not equivalent to “impossible in that product.” Compositions of tools may satisfy requirements even when no single package does.

**Stewardship:** Wesley R. Elsberry is the human editorial steward and developer of the compared repositories. OpenAI Codex performed the research assistance, code/history inspection, comparison drafting and page construction. Elsberry reviewed the report and approved its public release on 26 September 2026. This relationship is a relevant competing interest; the report is not an independent external product review. No empirical superiority, student benefit, or security certification is claimed.

**Confidence labels:** high means direct source or history support for a narrowly stated fact; moderate means a reasoned comparison of documented features with incomplete operational evidence; unestablished means the evidence needed for the conclusion was not obtained. These labels are editorial judgments, not numerical probabilities. Each evidence record below inherits this stewardship statement and the recorded UTC assessment time.

### P1 — chronology and the 19-day figure

**Confidence: high for recorded ordering; unestablished for idea priority.** The initial Didactopus commit on 12 March is not, by itself, the graph implementation. Commit [`6c04e1e`](https://github.com/welsberr/Didactopus/commit/6c04e1e7bf0f54adaad831bf65f54f29ea04dc5f), recorded 12 March at 21:21:59 EDT, adds learning-graph code. Commit [`41ca57d`](https://github.com/welsberr/Didactopus/commit/41ca57d60fa2a68d323a140950f18f5eec44f0f9), 16 March at 21:46:33 UTC, makes knowledge graphs first-class domain-pack components. The original gist page displays creation on 4 April. The figure is the calendar-date subtraction **4 April − 16 March = 19 days**; it is not an exact elapsed-hour claim. Git dates do not independently establish first public availability or the origin of an idea.

### P2 — governance is relevant and overlaps alternatives

**Confidence: high for the article’s scope and documented overlap; moderate for comparative fit.** Evidence: the linked Section article, GroundRecall policy specification and public HTTP adapter, plus the linked SuperLocalMemory, Cortex, Graphiti, Mem0 and Letta documentation. The article supplies a practitioner example, not prevalence estimates. The comparison checks access, evidence status and release separately. No end-to-end adversarial security tests were run.

### P3 — graph representation and learning

**Confidence: high for documented structures; unestablished for learning superiority.** Evidence: pinned Epistemap and Didactopus repositories, PROV-O, RDFLib, pySHACL, OATutor and Google’s study-tool help. The older standards and tutoring work establish relevant prior approaches. Their existence does not prove that a specific alternative replaces every local adapter. No human learning trial was conducted or inferred from demonstrations.

### P4 — bibliography, conversion, serving and publishing

**Confidence: moderate for best-fit recommendations; high for the recorded software test outcomes.** Evidence: pinned CiteGeist, doclift, GenieHive and SciSiteForge snapshots, official alternative documentation, and the linked GenieHive validation and CI records. No shared document corpus, citation gold standard, latency/cost test or site migration trial was run. Reported personal applications motivate the comparison; they do not establish a causal productivity gain or transferable cost advantage.

### P5 — availability and contribution claims

**Confidence: high for verified branch updates and recorded test results; limited for authorship attribution.** Public-main hashes and local hashes are recorded below. The initial audit found ClaimWright’s publication gate absent from `main` (but already on a public feature branch) and GenieHive’s evaluation work unpushed. Both gaps were closed after inspection and fixes on 26 September 2026. The counts **23** and **119** are passing test cases reported by Cargo and pytest, respectively; they are not measures of coverage, model quality or product superiority. Clean-checkout runs and GitHub CI corroborate these software checks. Uncommitted work in other repositories remains excluded. A Git author field does not apportion human and AI contribution.

### Repository snapshots

The following table is generated from the inspected inventory. “First commit” is a recorded repository event, not a claim that all current features existed then. Full hashes, evidence paths and assessment timestamp are available in [provenance.json](provenance.json).

<!-- SNAPSHOTS -->

### Review and maintenance

Recheck feature documentation and public releases before an adoption decision. Revise this report if an implementation contradicts its documentation, a public release closes a stated availability gap, or a common evaluation produces contrary results. The report contains no benchmark chart or reproduced source figure. All tables are original qualitative comparisons; the chronology calculation is documented in P1.

### Acknowledgements and development record

OpenAI Codex assisted with research, repository inspection, source comparison, drafting, and HTML rendering. Wesley R. Elsberry supplied the questions and personal experience, reviewed the result, and approved publication. Corrections remain welcome. This report is a companion to the [BEACON presentation](../); it is not an MSU endorsement of the projects.

Development on 26 September 2026 proceeded through local history and public-source checks, identification and user confirmation of the Section article, comparison drafting, and local rendering review. A subsequent maintainer-authorized update tested, corrected and published the ClaimWright and GenieHive changes, then revised this report’s availability findings. The author then approved promotion of the report alongside a revised presentation for broader public release. The exact update and automated-check timestamps are recorded in the accompanying provenance and review files.
