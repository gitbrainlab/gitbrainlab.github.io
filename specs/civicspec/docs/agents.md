# Agent adoption and learning

An agent should be able to begin from this repository without access to the original conversation. Its owner supplies an approved registry/repository, allowed release channel, source access, role, budget, and permitted write destinations. CivicSpec does not grant those permissions itself.

## Load a small core, then relevant detail

Load [core instructions](../bootstrap/core-instructions.md), the pinned [specification](specification.md), this guide, and the applicable profile/example index. Keep the core invariants in the task context. Retrieve large profile and source materials only when relevant. Package these resources through your runtime's existing instruction loader; no particular model or agent framework is required.

## Startup and run contract

1. Resolve an owner-authorized release. Candidate use must be explicit. Verify the manifest and component hashes, then pin one release digest for the run.
2. Record role, capabilities, corpus snapshot, source/profile scope, budget, and allowed destinations. If unavailable, report the missing configuration.
3. Search before reading. Fetch bounded evidence using the existing corpus interface. Partial retrieval is partial coverage.
4. Produce attributed, source-pinned candidate assertions before narrative synthesis. Preserve competing claims and unresolved identities.
5. Run structural, reference, evidence, vocabulary, semantic, and publication checks that actually exist. Report unsupported checks separately.
6. Ask a bounded evidence question or record a lesson when meaning cannot be established. Do not force an answer to satisfy a completeness target.
7. Return outputs, dependencies, validation results, unresolved issues, resource use, and version references. The [run receipt template](../contracts/run-receipt.example.json) is a starting shape, not an executed receipt.

## Teach with distinctions, then evaluate separately

Use the [worked examples](tutorial.md) to ask the agent why two votes cannot collapse, why conditional approval is not grant receipt, and why a negated topic is not an affirmative project. Ask it to identify the missing evidence, not just repeat a label. Correct mistakes using source spans and counterexamples.

Once a case has been used for teaching, treat it as training/regression material. Hold back separate sources or meetings for evaluation, with labels hidden from the extraction pass. Include source families and jurisdictions outside the easiest cases. Successful onboarding is a scoped observation, not fleet-wide accuracy certification.

## Roles and authority

| Role | Output | Boundary |
| --- | --- | --- |
| Collector | Source version and coverage receipt | Retrieval does not establish a civic decision |
| Extractor | Candidate assertions and unresolved mappings | Cannot silently redefine a term |
| Desk analyst | Evidence-backed questions, timelines, and comparisons | Cannot make incomparable cohorts equivalent |
| Verifier | Reviewed evidence/labels and disagreements | Must inspect evidence, not rely solely on the generating narrative |
| Curator | Deduplicated lesson and change proposals | Repetition is a prioritization signal, not proof |
| Maintainer | Accepted semantics and release decisions | Acts only under owner-delegated authority |
| Publisher | Eligible outputs and corrections | Spec publication does not authorize every civic claim |

## Learning loop

Capture failures during ordinary work: unknown codes, broken selectors, body ambiguity, contradictory sources, lost conditions, reviewer corrections, or source changes. Deduplicate by source/version and failure class. Batch analysis under the existing cost governor; unchanged inputs should not require repeated model calls.

Use the states `observed → triaged → proposed → evaluated → approved → released → monitored`, with rejected and superseded outcomes. Append actor, time, evidence, decision, and idempotency key at each transition. A proposal includes positive and negative cases, alternatives, compatibility, expected costs, migration scope, and rollback.

The deployment's authorized maintainer promotes shared semantics. An explicitly delegated local adapter change may have narrower automated gates. The generating agent must not grant itself authority, change a reference label silently, or weaken a gate to pass its patch.

After adoption, refresh affected assertions and answers through their recorded dependencies. Preserve prior versions and correction notices. Measure incorrect promotions, abstention, coverage, review burden, correction delay, and cost with separate denominators.

## Initial implementation assignment

Inventory existing ownership and interfaces. Verify this candidate. Implement one source-family adapter in shadow mode and return an adoption receipt, source-backed examples, unknowns, and a diff against current outputs. Demonstrate one lesson proposal and a rollback plan before broad adoption. Do not rebuild working ingestion infrastructure or retranscribe the entire corpus just to add this contract.
