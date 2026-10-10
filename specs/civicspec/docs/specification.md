# CivicSpec Adoption and Maintenance Specification

Status: Experimental public adoption contract, release candidate 0.1.0-rc.1. Public edition dated October 10, 2026, hosted under `specs/civicspec` in `gitbrainlab/gitbrainlab.github.io`. This public edition preserves the 23-section adoption contract and updates its publication location and audience. It extends the September research baseline; it does not declare production ontology conformance or a deployed signal desk. See [validation scope](validation.md) for checks implemented in this repository.

## 1 Purpose and required outcome

Participating civic systems, including the TDOG signal-desk deployment that motivated this work, shall use CivicSpec to build an evidence-linked account of government activity across sources and time. Bots must be able to distinguish who acted, in which capacity, on which matter, what was proposed, what was decided, what conditions remain, and what later evidence establishes about execution or results. Every consequential statement must remain traceable to its supporting source and interpretation history.

Implement CivicSpec as a maintained contract shared by the bot farm. Its durable components are definitions, controlled vocabularies, source profiles, evidence selectors, extraction adapters, reference cases, validation rules, reviewed lessons and release history. Individual bot conversations are working context, not the authoritative store for those components.

The initial outcome is a published, immutable experimental release; a verified discovery path; bot startup and output contracts; a candidate-assertion pipeline operating alongside current outputs; and an evidence-based process for improving that pipeline. Production promotion follows demonstrated acceptance criteria.

The words MUST, MUST NOT, SHOULD and MAY indicate required behavior, recommended behavior and optional behavior under this proposed contract. An assigned implementer must identify actual owners and services during discovery instead of assuming proposed paths or roles already exist.

## 2 Publication comes first

CivicSpec needs a stable home before autonomous consumers depend on it. The current public source is [`specs/civicspec` in gitbrainlab/gitbrainlab.github.io](https://github.com/gitbrainlab/gitbrainlab.github.io/tree/main/specs/civicspec). Publication uses the existing GitBrainLab documentation infrastructure. This directory is self-contained and can move to a dedicated repository through an explicit registry migration. A public candidate makes the contract inspectable; production approval and consumer adoption remain separate decisions.

| Surface | Selected location | Responsibility |
| --- | --- | --- |
| Authoritative source and documentation | This repository | Definitions, schemas, profiles, examples, tests, migration guidance and release history |
| Repository discovery document | `.well-known/civicspec.json` | Locate candidate/stable channels and pinned manifests |
| Candidate manifests | `releases/{release_id}/manifest.json` | Inventory exact component bytes at the manifest's full source commit |
| Private evidence and operational records | Each deployment's existing stores | Source snapshots, review records, incidents, lessons and operational receipts |
| Agent coordination | Each deployment's authorized catalog/bridge | Exchange bounded proposals and separate adoption receipts |

The [publication guide](publication.md) defines the GitHub transport binding. A custom documentation domain is optional and has not been deployed by this repository publication. Any future website must be generated from an identified source revision. Do not create another canonical repository or edit a website independently of its release source.

Publish an explicit component inventory. Include public documentation, schemas, definitions, synthetic examples, release notes and validation utilities. Keep credentials, private operational locations and unrestricted corpus archives outside the repository. Real source examples require documented provenance and a publication basis. [License status](../LICENSE_STATUS.md) is explicit; no new open-source license is inferred from public availability.

## 3 Initial baseline and version boundaries

Preserve the September 7 CivicSpec Ontology Backtest as an immutable research baseline. This public repository includes a [selected definition/mapping/classifier subset](../research/README.md), not its full source corpus or independently reproducible case package. The reference mapping is `layered_v5_replay` with 168 field paths. Preserve original ontology, mappings, vocabulary, classifier files and their hashes. The October 10 backtest is a separate evaluation artifact.

The October evaluation found 206 mapped field occurrences out of 215 in 24 selected cases, 18 recognized controlled-value occurrences out of 30, and an unchanged action classifier with 5 correct, 5 abstaining and 1 incorrect result in 11 supported positive cases. Five negative controls abstained; eight cases were outside that classifier's scope. These are separate results from a purposeful single-reviewer sample. They are not an end-to-end production accuracy estimate. The original 551/551 post-refinement field replay must not be described as extraction accuracy.

Maintain separate identifiers for:

- The ontology and mapping profile.

- The wire-schema contract.

- The release bundle and its content digest.

- The source adapter and extractor implementation.

- The prompt or skill instructions and model identifier/configuration when a model is used.

- The reference-case set and its label revision.

- The publication/rule profile and its applicability interval.

This adoption document's `0.1.0-rc.1` is its own contract version. It does not rename the September ontology to version 0.6 or claim any proposed extension is already accepted.

## 4 Repository and release layout

The implementation repository should contain the following logical components. Exact directory names may follow an existing repository convention; the release manifest must expose equivalent entries.

| Component | Required contents |
| --- | --- |
| `docs/` | Purpose, terminology, semantics, identity rules, provenance, lifecycle rules, publication, operations, migration and contributor guidance |
| `bootstrap/` | Short invariant instructions, role guidance, examples index and failure-handling instructions |
| `schemas/` | JSON Schema contracts for manifests, assertions, sources/selectors, lessons, change proposals, run receipts and evaluation reports |
| `ontology/` | Versioned ontology terms and any graph constraints; clearly state which are executable and tested |
| `vocab/` | Controlled values with definitions, aliases, scope, status, replacement and version history |
| `profiles/` | Jurisdiction, public-body, document-family and producer-era profiles; format rules separate from legal rules |
| `adapters/` | Source-to-contract mappings and adapters, including raw-to-reader transformations |
| `examples/` | Synthetic public examples; access-controlled real examples reside separately |
| `tests/` | Structural checks, semantic regressions, negative cases, source-selector checks and protocol tests |
| `evaluations/` | Dataset manifests, sampling plans, metrics, limitations and release-specific results |
| `migrations/` | Compatibility mappings, impact descriptions, reversible transformations and rollback instructions |
| `releases/` | Immutable manifests, inventory digests and release notes |

Build human-readable documentation and machine-readable files from the same source revision. A prose rule and its executable counterpart must link to the same requirement identifier. If an executable check is incomplete, state its actual coverage rather than asserting complete enforcement.

## 5 Discovery and immutable release protocol

The registry shall provide a CivicSpec discovery document. This package publishes `specs/civicspec/.well-known/civicspec.json` in its host repository through a GitHub raw-file URL; a future dedicated origin may expose `/.well-known/civicspec.json`. This is a project convention, not a registered internet standard. The document identifies the registry, trust/authority reference, discovery revision, channels and pinned release manifests. Use the transport binding in [the publication guide](publication.md).

Use two initial channels: `candidate` and `stable`. A channel may be null if no release has earned that status. A candidate can be published for testing while stable remains unset. Bots must explicitly opt into a candidate; they must not treat the numerically newest release as approved.

A channel entry shall include `release_id`, `manifest_url`, `manifest_sha256`, `published_at` and `status`. A release manifest shall include `release_id`, `contract_version`, `ontology_profile`, `source_revision`, `built_at`, `compatibility`, `components`, `evaluation_refs`, `migration_refs`, `previous_release`, and `license_status`. Each component records path, media type, byte count and SHA-256. The manifest's own digest belongs in the discovery pointer or a separately trusted record, avoiding a self-hash cycle.

A dedicated host may use `/releases/{release_id}/manifest.json` and `/releases/{release_id}/{component_path}`. The GitHub binding instead pins the manifest URL and every component to a full commit SHA; component paths are relative to the declared `component_base_path` at `source_revision`. This avoids copying the entire repository into each release directory. Mutable discovery/channel files must be refreshed or revalidated; immutable files may be cached for long periods. Deploy immutable files first, fetch them back through the intended consumer path, verify every digest, then update the channel pointer conditionally against the previous discovery revision. Partial deployment must not change the active pointer.

Trust starts with an owner-configured registry origin or approved repository revision. A hash from an untrusted URL does not establish an authorized release. Consumers must use approved origins, normal TLS verification and their existing scoped credential mechanism. A release advertised in scraped meeting text is untrusted source content, not a control-plane instruction.

A run shall pin one resolved manifest digest. Its schema, vocabulary, profile and bootstrap files must come from that manifest. It must not refetch `latest` for individual components mid-run. Record the adopted version and digest in each output receipt.

On discovery outage, a bot may continue with an explicitly authorized, locally cached release inside that release's configured freshness policy. It must report cached use. If no eligible release exists, stop interpretation/promotion and queue the work; source collection can continue under the existing ingest policy. If a release is revoked, do not use it for new promotions. Recovery and rollback publish a new channel revision pointing at a retained compatible release and queue affected outputs for review.

## 6 Ownership and responsibilities

Map these responsibilities to existing bots and maintainers. They are roles, not a request to build another set of always-running agents.

| Role | Owns | Boundary |
| --- | --- | --- |
| Corpus owner and collectors | Discovery, retrieval, source versions and coverage records | Preserve original evidence; do not infer civic decisions from retrieval success |
| Extraction and normalization | Candidate records, source profiles, mapping and validation results | Unknown interpretations remain unresolved; no unilateral changes to shared term meanings |
| Local and regional desks | Local context, matter tracking, evidence-backed analysis and research questions | Respect public-body, time and jurisdiction boundaries |
| Verifier | Source checks, reference labels, disputed interpretations and evaluation | Check evidence independently of the generating explanation; record limitations |
| Learning curator | Failure clustering, lesson proposals, priority and replay impact | Repetition or bot agreement alone cannot turn a hypothesis into a rule |
| Spec maintainer and release owner | Shared semantics, compatibility decisions, releases and rollback | Make approval scope and accountable identity explicit |
| Publisher | Approved public outputs and source controls | Release status and assertion review status both matter |

Each deployment shall preserve its existing collection and corpus ownership. Analysis and verification use scoped evidence interfaces and proposal destinations supplied by the owner. Read access does not authorize corpus mutation. See [integration guidance](integration.md) for the TDOG deployment context.

## 7 Required teaching and startup behavior

Each participating bot shall have a short mandatory core instruction block, a role-specific guide and access to detailed profiles and worked examples. The core block must cover evidence, identity, event stages, uncertainty, release pinning and unresolved-case handling. Details should load on demand. An Agent Skills-compatible `SKILL.md` is an appropriate packaging option where the runtime supports it; other runtimes must provide the same behavior through their startup/task loader.

At onboarding, run the bot on the existing challenge cases with expected answers hidden from the extraction pass. Compare its output with reviewed reference labels and give source-grounded feedback. Once examples are used to teach or tune the bot, classify them as training/regression material. Maintain a separate unseen evaluation set. Passing an onboarding exercise does not certify every future output.

On each task the bot shall:

1. Resolve and pin an allowed release, corpus snapshot and applicable local profiles.

2. Record its role, capabilities, budgets and permitted write destinations.

3. Search for relevant sources and retrieve bounded evidence at the pinned snapshot.

4. Extract source observations and candidate assertions before drafting a narrative.

5. Apply deterministic structural, identity, selector and controlled-code checks.

6. Request additional evidence or emit a learning issue for unresolved distinctions.

7. Produce outputs, evidence dependencies, validation results and a run receipt.

Retain the existing search-before-read pattern and the owner-configured limits on each evidence read. Large sources can be referenced or processed in source-local jobs. An incomplete bounded read must be reported as incomplete coverage, not as evidence that content is absent.

## 8 Core semantic invariants

| Requirement | Required distinction |
| --- | --- |
| CS-01 | A government is distinct from its public bodies, offices, committees, districts and geographic service areas. |
| CS-02 | A meeting, a session, a recording, a document work and a document version are distinct objects. |
| CS-03 | A matter can recur across meetings; an agenda position alone does not identify it globally. |
| CS-04 | Each motion, amendment, procedural treatment and vote is represented in its own context and sequence. |
| CS-05 | Proposed effects, recorded outcomes, legal effect, authority to execute, actual execution, financial flows and physical completion are separate dimensions. |
| CS-06 | A source's assertion, the extractor's interpretation and a reviewer's finding are separate records. |
| CS-07 | Unknown, not found, denied, not applicable, zero and false are different states. |
| CS-08 | A statement can be affirmative, negative, hypothetical or contested; keyword presence does not establish an affirmative event. |
| CS-09 | A conditional authorization retains its conditions until evidence addresses them. |
| CS-10 | Counts, measurements and money retain units, bases, periods, qualifiers and arithmetic discrepancies. |
| CS-11 | A document's draft/final/corrected status, its meeting date, approval date, posting date and observation date remain distinct. |
| CS-12 | Current legal text cannot silently govern a historical event; local practices cannot silently become statewide requirements. |
| CS-13 | Structural validity and a source hash do not establish factual truth or legal compliance. |
| CS-14 | Corrections create a new version and explicit supersession/contradiction relationships; evidence history is preserved. |

These invariants must be part of mandatory runtime guidance and tested where mechanically enforceable. A bot must not replace them with a summary that omits the operative distinctions.

## 9 Identity and joins

Keep current application identifiers as aliases. Introduce canonical identity through an explicit resolution layer rather than replacing recording keys or treating municipality plus date as a unique meeting identifier. The backtest found 42 same-place/same-date groups containing 131 records; distinct source keys remained unique.

Government identity must include its jurisdiction class and independently supported identifiers. Public-body identity must include its parent or responsible government, body identity and validity interval. An officer's capacity and membership are time-qualified. A school district and a town sharing a name are not identical. County labels and geographic overlap establish neither organizational parentage nor authority.

Meeting identity must account for body, source-reported date/time, session, rescheduling and split recordings. Matter identity must account for issuing body, identifier scheme, printed identifier and identity period. Do not invent an identifier year from meeting date. Preserve unresolved mentions in source scope.

Every proposed merge shall record candidate IDs, evidence, rule/profile version, reasons, alternatives, reviewer and affected records. Accepted merges must remain reversible through aliases and resolution history. An automatic merge policy may handle narrowly defined existing identifiers within its approved scope; ambiguous names, cross-body matches and changes affecting consequential published conclusions require review. Do not emit blanket equivalence relationships.

Documents found under a later agenda URL may contain earlier minutes. Extract the meeting context from document content and linked metadata; retain URL and filename as observations. Body-label mismatches between a portal and a document create a resolution task rather than an automatic choice.

## 10 Source and evidence contract

Each source version shall record a stable source ID, byte digest and media type, source location, retrieval time, access scope, provider identifiers, and known publication/version metadata. Source bytes and derived text have separate identities. An ASR-reader JSON hash must never be labeled an original-audio hash.

Each evidence selector shall specify the exact representation being selected and one or more reproducible locators: retained-text character range, page and page-text range, transcript segment IDs/indices plus timestamps, or structured row/column identifiers. Record a quote or selected-text digest when release policy permits it. Character offsets refer to a named text representation with a declared indexing convention; they do not refer to arbitrary PDF bytes.

Represent transformations such as OCR, ASR, normalization, segmentation and redaction as activities with input/output identities and implementation versions. Preserve original ordering when timestamps move backward. A repaired time alignment is a derived representation; it does not overwrite the source.

For a public quotation, validate the selector against the exact public representation being linked. If a passage is withheld in that representation, either provide an authorized reproducible alternative or identify the traceability limitation and withhold the unsupported quotation. Do not bypass a privacy transformation simply to make the quote check pass.

Copies and mirrors of one source are not independent corroboration. When audio, draft minutes, approved minutes and later corrections disagree, retain the competing assertions and source relationships. Authority and evidentiary preference belong to a documented profile and review decision, not a universal rule that every PDF outranks every transcript.

## 11 Assertion and event contracts

The implementation must define and validate a machine-readable envelope for each assertion. The following fields are the minimum logical contract; the repository schemas may use an equivalent documented encoding.

| Field group | Required content |
| --- | --- |
| Identity | Assertion ID, subject reference, predicate ID, typed value and context references |
| Meaning | Assertion basis, attribution, polarity, modality and relevant conditions |
| Time | Source/event time assertions, effective interval when established, observed time and recorded time |
| Evidence | Source-version and representation references, exact selectors and selector verification result |
| Interpretation | Mapping/profile, extractor, prompt/model where used, run ID and spec release digest |
| Review | Candidate/accepted/rejected/disputed/superseded status, review events, rationale and unresolved issues |
| Lineage | Supports, contradicts, derived-from, supersedes and dependency references |
| Publication | Access/release class and whether the assertion is eligible for a particular product view |

Use controlled predicates and typed value forms. Monetary values use decimal strings plus currency and amount role. Physical measurements use value, unit, population/basis, reported versus computed status and source scope. Codes identify their vocabulary and version. Free text can preserve a statement, but it must not receive structured-field coverage credit for missing semantics.

Events require separate subject/target references and sequence relationships. Represent action interpretation compositionally as operator, target kind, outcome, modality, conditions and authority context. A passed vote does not alone establish legal effectiveness, execution or performance. Missing dimensions remain unknown rather than inheriting a neighboring action's state.

Each VoteEvent must point to the specific treatment it decides. Preserve aggregate counts, named votes, absences, abstentions, recusals and attendance changes as separate observations. Where a document states a default vote for a list of resolutions, record that inheritance and its selector; do not fabricate individual roll calls. Do not attach the next agenda item's vote to the preceding discussion.

Reference examples are included in `examples/`. They use `urn:example:` identifiers and demonstrate the proposed wire contract; they are not accepted production assertions or newly assigned canonical municipal IDs.

## 12 Finance projects and obligations

Separate financial observations from the underlying financial instruments or accounts. Each observation must preserve entity, period, fund/account if known, amount role, currency, qualifier, source timing and aggregation relationship. Amounts from different bases or stages must not be summed merely because they share a project label.

For grants distinguish application, award, acceptance, appropriation, disbursement and expenditure. For debt distinguish project authorization, borrowing authorization, instrument issuance, proceeds receipt, outstanding principal and debt service. Keep short-term instruments, renewals, refinancing/conversion and long-term instruments as related records with their own dates, terms and evidence. A project ceiling is not necessarily new borrowing; a financing transition does not by itself establish either a saving or a loss.

For procurement distinguish solicitation, bid receipt, recommendation, award, contract authorization, executed contract, change order, invoice, payment and delivery. For employment distinguish proposal, appointment, conditions, stated effective date and evidenced commencement. For physical projects distinguish planned, authorized, underway, completed-as-reported and independently verified completion.

An obligation shall identify the actor, required act, beneficiary/scope, trigger, conditions, due rule and authority. A promise or a source's description of a duty does not prove performance or legal enforceability. Tracking an overdue evidence request must not automatically produce an allegation of misconduct.

## 13 Questions and useful signal production

Use the ontology to organize questions and missing evidence as well as extracted facts. Each tracked matter should expose the latest supported state, unresolved alternatives, expected next evidence, and the scope/date of the answer.

Initial competency questions shall include:

- Which body acted on this matter, and in what capacity?

- Was the passage a public comment, a proposal, a procedural motion or a recorded decision?

- Which vote decided the amendment and which decided the underlying matter?

- Which conditions remain unresolved after approval?

- Is the amount a forecast, ceiling, authorization, reported award, reported receipt or expenditure?

- What changed between the agenda, draft minutes, approved minutes and later records?

- What evidence would establish the next stage, and where should the existing collector look for it?

- Does a cross-place pattern have sufficiently comparable definitions, periods, coverage and direct evidence?

Every answer should return assertion/evidence dependencies, its as-of basis, missing coverage and unresolved conditions. A source update or accepted correction shall enqueue only affected assertions, matter timelines, answers and publications for reevaluation. Retraction and correction metadata must propagate to cached outputs; deleting history is not the correction mechanism.

## 14 Publication indicators and legal rules

Keep source observation, rule evaluation and reviewed conclusion separate. A collection result must identify checked venues, retrieval attempts, coverage and time. Not found in a checked venue is not equivalent to unavailable everywhere.

A rule evaluation shall include jurisdiction/public-body applicability, authority/version, effective interval, relevant facts, evidence for dates, exemptions or conditions, outcome and unresolved inputs. Outcomes shall support satisfied, not satisfied, unknown and not applicable. A legal conclusion requires the separate review policy appropriate to its consequence.

For the New York profile, implement the currently reviewed requirements with historical applicability preserved. Public Officers Law 106(3) allows unabridged audio/video or written transcripts to count as minutes for that subdivision; a recording match alone does not establish completeness or timely availability. Section 103(e) uses a 24-hour threshold with practicability and website conditions. Before scoring, verify the relevant rule text and event-date applicability.

Every dashboard metric shall publish its denominator, eligibility/cohort filter, as-of time and rule/profile version. The October backtest's 1-versus-57 timely-minutes counts reconciled: 56 positives were younger than 14 days, leaving one eligible older meeting. Preserve this as a regression against mixing cohorts, not as an open arithmetic bug. The 62 sampled negative indicators with recording matches remain a review queue, not proven compliance mistakes.

## 15 Learning event and lesson contract

Learning is triggered by a new source pattern, unresolved mapping, unexpected code, failed selector, contradiction, reviewer correction, failed regression or changed source. Capture these events during ordinary processing. Cluster and reason over them in bounded batches under the existing capacity governor. Routine unchanged-source checks should not require a model call.

A lesson record shall contain `lesson_id`, `deduplication_key`, `kind`, `scope`, `source_refs`, `case_refs`, `expected_behavior`, `observed_behavior`, `hypothesis`, `proposed_change`, `counterexamples`, `affected_components`, `impact_query`, `created_by`, `created_at`, `review_status` and `decision_history`. Expected behavior must identify whether it is an adjudicated requirement or a proposed interpretation. A bot's confidence score is not adjudication.

Classify the learning target:

| Learning kind | Destination and promotion rule |
| --- | --- |
| New evidence or civic event | Add a source-pinned candidate assertion; apply existing review/publishing policy |
| Formatting or extraction pattern | Scoped adapter change with regression evidence |
| Entity alias or merge | Identity-resolution proposal with reversible history and impact analysis |
| Missing term or distinction | Namespaced extension proposal; shared vocabulary changes require maintainer acceptance |
| Changed legal/practice rule | Versioned rule profile with jurisdiction/time and reviewed authority |
| Incorrect published claim | Incident/correction record, affected-output review and accountable disposition |
| Documentation-only clarification | Documentation patch; verify it does not change semantics before treating it as nonsemantic |

Repeated observations can prioritize a lesson but cannot independently validate it. Ten bots repeating one error are not ten corroborating sources. Do not train on accepted outputs without preserving the underlying source/reviewer basis; doing so can amplify an initial mistake.

## 16 Controlled change and release workflow

Use the states observed, triaged, proposed, evaluated, approved, released, monitored, rejected or superseded. Each transition records actor, time, inputs, decision and evidence. State transitions are append-only events; materialized queues are rebuildable views. Use unique event IDs, idempotency keys and conditional writes so retries or concurrent curators do not silently overwrite decisions.

A semantic change proposal must state the problem, affected scope, exact proposed definitions or code, alternative interpretations, positive and negative examples, compatibility impact, migration requirements, expected cost and evidence needed for acceptance. Keep locality explicit. Prefer a producer/body/document-family adapter when a global semantic change is unnecessary.

Evaluate the unchanged baseline first, then the candidate. Preserve original sources and label revisions. A correction to a reference label must have its own review trail and must be reported separately from an extractor improvement. Add a regression case for every corrected semantic failure; documentation-only typos do not require new behavioral tests.

An automated curator may prepare patches, run tests and submit bounded proposals under its current authority. It may release narrowly scoped changes only where the owner has explicitly delegated that class of release and its gates pass. Changes to shared meaning, canonical identity policy, legal rule interpretation or publication policy require the designated maintainer's approval. A bot must not grant itself that authority or modify the gate to pass its own patch.

Release notes must state changed behavior, evidence, known limitations, compatibility, migration/backfill scope and rollback. A release is immutable after publication. Before version 1.0, publish explicit compatibility ranges and migration rules; do not rely on the apparent stability of a 0.x version. After declaring a stable API, use major/minor/patch meaning consistently. The active channel change and each bot's adoption are separate recorded events.

## 17 Validation and evaluation gates

Validation must have independent layers:

1. Syntax/schema: types, required fields, formats and supported contract version.

2. Referential integrity: resolvable IDs, source versions, sequences and dependency edges.

3. Evidence integrity: reproducible selectors, quotes and transformation lineage.

4. Semantic constraints: correct treatment/vote association, stage separation, units, conditions, identity scope and unknown handling.

5. Review/publication policy: permitted review states, access classes and attribution.

6. Task performance: extraction, abstention, coverage, calibration where justified, and question answerability on labeled cases.

JSON Schema can enforce envelope structure. If an RDF graph is emitted, execute the required SHACL checks for its declared conformance profile. Neither a successful schema check nor SHACL conformance proves source truth. The current backtest did not run a SHACL engine; importing its shape file does not satisfy that future gate.

Use the October 24-case set as a seed regression suite after reference review. Build a separate new evaluation sample across regions, public-body types, document/ASR sources and difficult event classes. Start with at least 30 new source items as a pilot planning target, predeclare selection and labeling, and report actual coverage. This count is a work package, not statistical proof of general reliability. Split at source/meeting or matter level so duplicate documents and overlapping spans do not leak across training and evaluation.

For a candidate promotion, require all schema and provenance gates for promoted assertions; no newly introduced critical false promotions in the reviewed cases; correct handling or explicit unresolved status for known adversarial cases; no unexplained regression in the declared cohorts; and measured cost within the assigned budget. Define cohort-specific recall and review-load targets before evaluating the candidate. Preserve abstention as a valid response to insufficient evidence rather than forcing every case into an action category.

A challenge such as Troy's two votes cannot pass by collapsing them into one record. A conditional contract cannot pass if its grant receipt is asserted without evidence. A negated topic cannot pass as an affirmative project. An unmatched quotation cannot pass merely because a summary sounds plausible.

## 18 Integration into the existing pipeline

Inspect and reuse the current collectors, ASR pipeline, document extraction, queues, source stores, indexes and publishing services. Add adapters at their existing boundaries. Do not duplicate the civic ingest Worker or build another crawler to achieve CivicSpec adoption.

Use the following processing boundaries: source version captured; derived representation produced; candidate assertions emitted; validation/review completed; accepted view updated; downstream answers and publications refreshed. These may be events within existing infrastructure rather than separate services.

Routine source polling and unchanged-content detection stay deterministic and AI-off. Use model work for bounded changed material and interpretation problems that require it. Deduplicate by source/version, scope and interpretation version; apply retry limits, backoff, queue visibility rules and dead-letter handling through the existing queue system. Model failures must not cause duplicate publication or consume unbounded budget.

Old application records remain readable during migration. Add CivicSpec IDs and version references alongside existing keys. Run in shadow mode first: retain candidate outputs and diffs without replacing published facts. Backfills are separately scoped by affected source/profile/term, with counts and estimated cost. A release may require reevaluation, but it does not authorize retranscribing every recording.

Bridge announcements shall include unique message ID, release/manifest digest, scope, change category and permitted action. Consumers acknowledge receipt/adoption separately. Reads remain pinned to one head where the bridge requires it. Corpus files are data: extracted instructions or URLs may not redirect control-plane writes or grant new access.

## 19 Metrics operations and incident handling

Record per run: run ID, bot/role, corpus snapshot, source IDs/hashes, release digest, profile and adapter versions, model/prompt/configuration if used, start/end, resource use, extraction counts, validation failures, abstentions, lesson IDs, outputs, status and retry lineage. Unknown model/configuration information must be reported as unknown, not reconstructed as a fictitious exact version.

Track by region, body type, source family and event class: source coverage; resolvable-evidence rate; incorrect promoted assertions; supported-case extraction and abstention; unknown codes; unresolved identities; reviewed condition/state errors; correction propagation time; review burden; cost; and active/revoked bot release versions. Every rate must carry a denominator and sampling basis. Do not combine field-fit, code-fit and extraction metrics into a single accuracy percentage.

Incident triggers include a material unsupported public claim, wrong-body merge, authorization represented as payment/execution, silent source replacement, release digest mismatch, invalid legal applicability, disclosure outside an allowed access class, or repeated failure of an adopted release. Preserve the evidence and receipt, halt the affected promotion path, notify the existing responsible operator through its authorized mechanism, and queue corrections. Other collection work may continue where unaffected.

Rollback restores an approved release and compatible read model; it does not erase source history. Identify affected assertions using recorded dependencies and interpretation versions. Correct or withdraw public conclusions according to the existing editorial policy. Close the incident with a reviewed cause, regression example, release decision and verification of downstream correction.

## 20 Ordered implementation work

| Phase | Deliverable | Exit evidence |
| --- | --- | --- |
| 0 Discover | Inventory actual repositories, catalogs, pipelines, ownership, permissions and current term definitions | Concrete path/owner map; baseline hashes retained; no duplicate ingestion plan |
| 1 Establish the home | Source repository or equivalent, generated documentation, immutable experimental release and discovery endpoint | A clean consumer fetches the manifest and verifies every listed component; actual URLs recorded |
| 2 Make bots understand | Core instructions, role guides, profiles, examples and onboarding exercises | Each pilot bot emits an adoption receipt and correctly explains the material distinctions or abstains |
| 3 Integrate in shadow | Adapters, assertion store/view, validators, receipts and lesson queue | Existing output compared with CivicSpec output; no unsupported replacement of published facts |
| 4 Evaluate | Reviewed seed cases, unseen sample, costs, errors and critical-failure report | All declared gates run; failures resolved or scoped out explicitly; promotion decision recorded |
| 5 Adopt gradually | Approved release and controlled rollout by source/body cohort | Version uptake visible; bounded rollback tested; affected outputs traceable |
| 6 Maintain | Event-driven lessons, bounded curation, regression/release workflow and impact-based refresh | A real correction proceeds from evidence through a tested release to verified affected-output refresh |

The first public release should identify the project as experimental and show exactly which profiles and checks are supported. Stable may remain unset during the pilot. A useful public specification can precede production adoption.

## 21 Acceptance checklist and return package

The implementing bot farm shall return:

- Actual repository, documentation, discovery and immutable manifest URLs, with access mode and release status.

- Release inventory, source revision, manifest digest, component hashes and a clean-consumer verification receipt.

- Ownership and authority map; exact adopted versions for participating bots.

- Implemented schema/semantic checks and explicit unsupported areas.

- Shadow-run diffs, reviewed reference results, unseen evaluation results, denominator definitions and cost measurements.

- A demonstrated lesson/change cycle and one rollback/correction-propagation exercise.

- Migration/backfill plan tied to affected sources rather than a blanket corpus rewrite.

- Remaining decisions with evidence, impact, accountable owner and bounded next action.

The work is complete when a new bot can discover an authorized release, understand and apply its contract, produce reproducible source-backed candidates, surface unknowns, contribute an evaluated lesson and recover after an incorrect release without relying on an old conversation.

## 22 Immediate backlog from the backtest

| Priority | Item | Required result |
| --- | --- | --- |
| 1 | Split treatment/vote and action interpretation | Troy retains distinct votes; Hyde Park retains amended grant-application approval |
| 1 | Resolve public bodies separately from recording keys | Same-date records and school/town entities are not silently merged |
| 1 | Bind public quotations to the displayed representation | Withheld/transformed passages are explicit; quote checks resolve to the visible evidence |
| 2 | Add scoped measurement, polarity and document-state mappings | 49 versus 46 remains a discrepancy; negation and draft status stay queryable |
| 2 | Reconcile vocabulary and classifier releases | A supported parser label cannot silently be missing from its declared code vocabulary |
| 2 | Make time cohorts and publication-rule inputs explicit | Timeliness denominators reconcile; recordings are evaluated with completeness/time/applicability evidence |
| 2 | Strengthen cross-place pattern evidence | Each comparison exposes supporting cases, comparable scope and coverage limits |

These are implementation priorities, not automatic authorization to change production schemas or public claims without the applicable release/publishing policy.

## 23 References and supplied artifacts

Source history: the September 7 CivicSpec Ontology Backtest and the October 10 CivicSpec TDOG Backtest. The public [research subset](../research/README.md) preserves selected original definitions, mappings and classifiers with hashes. The private case/source archives are not published here. [Validation documentation](validation.md) distinguishes reported historical observations from the executable checks available in this checkout. The supplied synthetic examples and tooling do not implement a production extractor.

Relevant primary specifications: [Agent Skills specification](https://agentskills.io/specification) for portable instructions and supporting resources; [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) for structured contracts; [W3C PROV-O](https://www.w3.org/TR/prov-o/) for provenance alignment; [W3C SHACL](https://www.w3.org/TR/shacl/) for RDF graph constraints; and [Semantic Versioning 2.0.0](https://semver.org/) for declared interface versioning. These are design references. CivicSpec conformance to an external standard must be tested and described at its actual scope.

For the New York publication-rule examples, consult [Public Officers Law 106](https://www.nysenate.gov/legislation/laws/PBO/106) and [Public Officers Law 103](https://www.nysenate.gov/legislation/laws/PBO/103), including the applicable historical version. Definitions and legal interpretations remain separate from source-format adapters.
