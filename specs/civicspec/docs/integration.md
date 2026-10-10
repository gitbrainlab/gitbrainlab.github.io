# Integrating an existing civic pipeline

Adopt CivicSpec at the boundaries your system already has. The implementation can use Workers, queues, relational tables, document stores, or an RDF graph. The contract concerns evidence and meaning; it does not prescribe another crawler or deployment platform.

## Boundary mapping

| Existing boundary | Add | Preserve |
| --- | --- | --- |
| Discovery / collection | Source identity, retrieval/coverage record, byte digest | Existing URLs, keys, access scope, collection ownership |
| OCR / ASR / extraction | Derived-representation identity and transformation receipt | Original bytes, segment order, source timing anomalies |
| Normalization | Scoped profile and candidate assertions | Unmapped fields/codes and uncertain body identity |
| Review / validation | Check results, review events, contradiction links | Candidate state until the applicable gates pass |
| Search / analysis | Matter timeline and answer dependencies | Evidence links, as-of basis, missing coverage |
| Publishing | Product eligibility and correction propagation | Editorial policy and privacy transformations |

## Minimal persistent records

Keep source versions, derived representations, body/matter identities and aliases, assertion versions, review events, interpretation-run receipts, lessons, change decisions, release adoptions, and output dependencies. Existing stores may already hold many of these. Append-only events can rebuild current-state views; do not require an event-sourcing rewrite where versioned tables already preserve the needed history.

Deduplicate work using source version plus interpretation/profile version and task scope. Use idempotent output keys and conditional writes. Retry and dead-letter policy must bound costs and avoid duplicate publication. A changed ontology can require reevaluation without requiring a new ASR job.

## Shadow adoption

1. Choose one public body and source family with accessible, reviewed examples.
2. Record baseline outputs and the exact source/profile/extractor versions.
3. Emit CivicSpec candidates alongside existing outputs. Do not replace public facts during this comparison.
4. Review material differences: identities, votes, amounts, polarity, conditions, and missing evidence.
5. Measure source coverage, failures, abstention, review burden, and cost. Keep cohorts and denominators explicit.
6. Authorize a bounded rollout only after the declared gates pass. Retain a compatible rollback release and dependency query.

## Deployment-specific boundaries

In the TDOG deployment that motivated this specification, collection and durable corpus ownership remain with the established corpus owner. Analysis and verification use the authorized bridge and submit scoped proposals. Operators must supply current access paths and limits from their own configuration. Public documentation intentionally does not publish private bridge locations or credentials.

Other deployments should map the same responsibilities to their own components. Neither read access nor a CivicSpec conformance claim expands write or publication authority.

## Finance and publication lenses

Add domain profiles incrementally. School financing, municipal capital projects, procurement, and publication-timeliness observations share evidence mechanics but require different institutional and temporal definitions. A single generic `approved` flag cannot represent them. See [profiles](profiles.md) and roadmap R09/R10 before building cross-place comparisons.
