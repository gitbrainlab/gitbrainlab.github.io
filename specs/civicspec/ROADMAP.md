# Improvement roadmap

These are open work packages, not completed features. Use the IDs in issues and pull requests. No work is assigned until a contributor and maintainer agree on scope. Candidate publication can proceed while these remain open; production adoption depends on the applicable gaps being resolved.

| ID | Priority / area | Useful contribution | Acceptance evidence |
| --- | --- | --- | --- |
| R01 | Before broad reuse: licensing | Propose owner-approved terms for documentation, code, schemas, and third-party examples | Explicit license files, provenance policy, and contribution terms; no implied relicensing |
| R02 | Before production: wire contracts | Extend the fixture envelope into a production assertion/source/event contract with migration rules | Draft 2020-12 schemas, positive/negative instances, operational metadata requirements, compatibility matrix |
| R03 | Before production: identities | Define public-body, meeting-session, matter, membership, and document-version resolution | Same-name town/school and same-day different-body cases remain separate; merges are reversible |
| R04 | High: treatment and action semantics | Model operator, target, outcome, sequence, conditions, and vote linkage compositionally | Two votes on one matter survive; amended approval retains both amendment and underlying action; ambiguity can abstain |
| R05 | High: evidence selectors | Add PDF page, OCR, ASR segment/time, Unicode, normalization, and public-redaction profiles | Each selector resolves against pinned displayed bytes; source and derived hashes stay separate; time repairs are versioned |
| R06 | High: independent evaluation | Publish a permission-cleared, reviewed seed suite and unseen source-level sample | Label provenance, disagreements, sampling, leakage checks, error counts, denominators, abstention and costs reported |
| R07 | High: vocabulary | Reconcile action labels with codes and define extensions/deprecations | No supported parser label silently missing from its declared vocabulary; original research files preserved |
| R08 | High: correction workflow | Demonstrate a real lesson through reviewed patch, regression, release, and affected-output refresh | Append-only decision trail, idempotent retries, dependency query, rollback exercise, correction receipt |
| R09 | High: finance profiles | Define school and municipal project/instrument/aid/levy/debt-service dimensions | Authorization, issuance, proceeds, cash expenditure and reimbursement do not double count; assumptions and periods explicit |
| R10 | High: temporal publication rules | Version jurisdiction/body applicability, exceptions, time cohorts, and legal authority | Recording completeness and publication timing evaluated separately; unknown inputs do not become violations |
| R11 | Medium: RDF interoperability | Adopt a canonical namespace and test PROV/annotation/ORG/SHACL alignment | Executed SHACL positives and failures; documented supported subset; no claim of untested external conformance |
| R12 | Medium: release operations | Add signatures/attestations, revocation, delegated channels, and consumer cache policy | Interrupted deployment, stale discovery, revoked release, digest mismatch, and rollback exercises |
| R13 | Medium: source adapters | Implement one existing producer/document-family adapter at a time | Source-pinned candidates, unknown-code behavior, bounded retries/cost, no duplicate collector |
| R14 | Medium: questions and comparisons | Add answerability/dependency contracts and comparable cross-place cohorts | Answers cite dependencies and missing coverage; updates refresh affected answers; comparisons share definitions and periods |
| R15 | Starter: documentation and examples | Improve glossary, accessibility, diagrams, multilingual and adversarial examples | A new reader can reproduce the example; no invented event or unsupported claim; links/checks pass |
| R16 | High: controlled English and event extraction | Extend the [experimental profile](docs/controlled-english.md) with context-aware motion resolution, typed condition logic and faithful rendering | Resolve J021, J032 and J061 on a new source-separated sample; independent model/label study; no silent promotion of future intentions |

R06 and R15 have a partial new contribution: the [60-case controlled-English study](evaluations/controlled-english-2026-10-10/REPORT.md). Single-assistant labels, remaining recognition failures and the unexecuted model comparison keep independent-evaluation and production-adoption work open.

## Good first tasks

1. Add a text selector example containing emoji and combining marks, showing why UTF-16 offsets cannot be substituted for Unicode code-point offsets.
2. Add draft and corrected minutes that disagree, with supersession and attributed competing assertions.
3. Write a body-identity example where the town board and school board meet on the same day.
4. Add a measurement discrepancy example that retains both a reported total and its inconsistent components.
5. Turn one ambiguous sentence in the model guide into a definition, example, and counterexample.

## Research questions

Which facts can safely be resolved by deterministic producer rules? How should evidence authority vary by source family and purpose? Which ontology changes improve answerability without encouraging overconfident extraction? How can correction costs and review burden be measured alongside recall? What shared core supports both town and school finance while preserving their different institutions and rules?

These questions need source-grounded experiments. A larger field mapping or more confident narrative is not, by itself, an answer.
