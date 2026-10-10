# Controlled English and real-corpus backtest

Date: October 10, 2026. Final language profile: `civicspec-controlled-english/0.1-draft.3`. This study executed three reference-implementation versions and two sequential reserved-source tests. It supports a reviewed trial of the preservation contract. It **does not approve the scalar action recognizer for automatic publication**, and it does not establish an LLM prompting benefit.

## What actually ran

- 60 source-grounded cases from 38 source versions: 31 public ASR-reader exports and seven official PDFs.
- 24 previously labeled development cases, then 20 cases from 11 additional municipalities, then 16 cases from eight further municipalities.
- An unchanged historical classifier and three deterministic candidate probes, each receiving only the selected source text.
- 803 applicable synthetic, single-field semantic-loss mutations per profile, plus 120 valid-control records per profile.
- Byte and selector verification for all 38 source versions and all 60 excerpts.
- Zero independent model API calls. No original-audio listening. One assistant developed implementations and annotations; no independent gold labels.

The source registry, case labels, freeze receipts, per-case predictions and mutation results are published alongside this report. Complete source archives are excluded. The [reproduction guide](../../docs/controlled-english-integration.md) explains offline preservation tests and optional verified public-source reconstruction.

## Design and ordering

The initial [protocol](protocol.json) retained the 24 prior labels and their original scope groups. Draft 1 was frozen before its development execution. Draft 2 was frozen before reading the first reserved transcript contents. The first reserved sources excluded every development municipality and all 87 previously downloaded transcript keys. Metadata ranking used a declared SHA-256 seed and distinct municipalities across body classes.

The first reserved test exposed multiple-treatment failures. It then became development/regression material for draft 3. A [second protocol](protocol-round-3.json) selected eight more distinct governing-body municipalities before draft 3 was frozen. That final sample excluded all earlier municipalities and previously fetched transcript keys. Draft 3 was frozen before the new transcript contents were read. Labels were frozen before prediction execution.

For each reserved meeting, selection took the first procedural window and the first nonoverlapping finance/condition window, each containing up to 13 ASR segments. If no procedural anchor existed, selection used a middle window. No difficult case was replaced. This rule produced 20 cases in the first set and 16 in the second. It is a purposive challenge sample, not a random population survey. Thirteen ASR segments can cover very different durations and multiple civic events.

The prior development PDF cases use exact page-text character ranges. Development transcript spans retain the prior selectors. Those hand-located spans are not a test of whole-document discovery or recall.

## Action recognition results

Entries show **correct / incorrect / abstaining** among supported positives. An action label describes the operative treatment under examination; it does not establish passage, legal effect, payment or performance. A future discussion without an operative motion can require abstention. A multi-treatment passage requires an ambiguity result from this scalar probe when one label would lose a distinct treatment.

| Sample | Historical unchanged | Draft 1 | Draft 2 | Draft 3 |
| --- | --- | --- | --- | --- |
| Development, 11 positives | 5 / 1 / 5 | 6 / 1 / 4 | 11 / 0 / 0 | 11 / 0 / 0 |
| First reserved, 6 positives | 0 / 1 / 5 | 2 / 2 / 2 | 2 / 2 / 2 | 6 / 0 / 0 **after reuse for refinement** |
| Second reserved, 5 positives | 1 / 0 / 4 | 2 / 2 / 1 | 2 / 2 / 1 | 3 / 1 / 1 |

| Negative controls: correct abstentions | Historical unchanged | Draft 1 | Draft 2 | Draft 3 |
| --- | --- | --- | --- | --- |
| Development, 5 | 5 | 5 | 5 | 5 |
| First reserved, 8 | 8 | 8 | 8 | 8 |
| Second reserved, 8 | 8 | 7 | 7 | 7 |

The remaining scope groups are not credited as successes: eight development cases outside the historical scope; four first-reserved cases outside scope and two unresolved-source cases; two second-reserved cases outside scope and one unresolved-source case. Their raw predictions remain in the results files. No reference label was changed to improve a score.

Draft 3 improved the final fresh positive count from 2/5 to 3/5 versus draft 1. The unchanged historical classifier abstained more often but did not produce the hearing false positive seen in all three candidates. Broader phrase recognition therefore improved some coverage while introducing a false-positive tradeoff. The sample is too small and selectively constructed to estimate production accuracy.

## Meaning-preservation results

Each mutation changes or removes one populated field in a copy of a source-anchored ledger. These are **injected errors**, not errors observed in bot outputs. The same applicable fields and original labels are used across versions. Unpopulated collections do not receive vacuous detection credit.

| Sample | Draft 1 detected | Draft 2 detected | Draft 3 detected | Valid controls falsely rejected, each version |
| --- | --- | --- | --- | --- |
| Development | 155 / 313 | 313 / 313 | 313 / 313 | 0 / 48 |
| First reserved | 130 / 269 | 269 / 269 | 269 / 269 | 0 / 40 |
| Second reserved | 110 / 221 | 221 / 221 | 221 / 221 | 0 / 32 |
| Total | 395 / 803 | 803 / 803 | 803 / 803 | 0 / 120 |

Draft 1 protected actor, action, target, basis, polarity, conditions, quantities and evidence. It did not protect modality, outcomes, attribution, time, source state, coverage, relations or unresolved issues. Draft 2 added those fields; draft 3 retained that protection and clarified treatment cardinality.

This is a contract-coverage result. Comparing a structured value with a retained original is substantially easier than extracting that value correctly or detecting a misleading summary. The result does not establish semantic understanding. The 803 related mutations are not 803 independent civic observations. The two controls per case are an unchanged ledger and a wording-only change; the wording control demonstrates that free prose is outside this guard's scope, not that the alternative prose is safe to publish.

## Observed failures and revisions

| Evidence case | Observed failure | Revision or disposition |
| --- | --- | --- |
| T02, Hyde Park | Amended grant application became generic amendment | Draft 2 prioritizes the application target while retaining amendment context |
| D02, Niskayuna | Approval heading concealed operative tabling | Draft 2 recognizes the tabled action; draft source status remains separate |
| D03/D04, Ballston Spa | Contract addendum and conditional hiring were missed | Draft 2 recognizes these forms; conditions stay in the ledger |
| D07, Ballston Spa | Convened executive-session wording was missed | Draft 2 extends the entry-form recognizer without inferring a closed-session decision |
| H051/H061/H101 | One source window contains several treatments | Draft 3 flags selected multi-motion forms; production event splitting remains open |
| H072 | Motion to pay vouchers was missed | Draft 3 recognizes a payment-authorization motion without claiming payment |
| J021, final reserved | Minutes appear before the approval request | Still abstains; context-aware reference resolution is needed |
| J032, final reserved | A future scheduling intention becomes a hearing action label | Still a false positive; explicit modality/state extraction is needed |
| J061, final reserved | Minutes, corrections and abstracts collapse into minutes approval | Still incorrect; event segmentation and correction lineage are needed |

Additional observations include conflicting portal/body labels (H101), a school-district presentation within a town meeting (J022), public-reader redactions (H081), amounts with different roles (H092), time- and recipient-dependent payment rules (J042), and a single motion with multiple document targets (J081). These support stronger requirements; they are not independently verified legal or financial findings.

## Decision and limitations

The declared non-regression and preservation gates pass for draft 3 relative to draft 2. The absolute production gate does not pass: two incorrect action labels and one supported-case abstention remain in the final reserved set. Keep the recognizer in diagnostic or reviewed shadow use. Publish the experimental profile and implementation guidance with these limitations attached.

Use the preservation guard to detect specified changes in an existing ledger. It cannot prove the initial ledger is complete, accurate or correctly scoped. The nested dictionaries remain loosely typed; the guard is ordinary Python value equality rather than a complete typed semantic comparator. It cannot validate a prose-only contradiction, prove an empty list represents a real absence, resolve uncertain ASR, or adjudicate conditions and legal authority. Stronger production schemas and independently reviewed source extraction remain necessary.

Freeze receipts are audit records produced within this session, not external attestations or proof of evaluator independence. The first reserved set is no longer a holdout for draft 3. All published cases are now teaching/regression material for future agents. The second reserved set contains only governing-body sources, and neither set establishes statewide representativeness. Selection favored procedural and finance/condition language. No confidence intervals or accuracy certification are appropriate here.

The next model experiment must separate the effect of controlled wording from the effect of new schemas, rules and validators. The [model-study protocol](model-study.json) is specified but not executed. It records the required arms, controls, independent labeling, costs, and adoption gates.

Final implementation review identified an additional type-comparison risk: ordinary Python equality treats booleans and corresponding integers as equal. The separately versioned `cce-preservation-guard/1.1` wrapper adds canonical JSON comparison. Its [qualification receipt](typed-guard-qualification.json) records replay of all 803 mutations and 120 controls, plus four synthetic type substitutions (0/false, 1/true, integer/string, integer/float). This is a post-study implementation check, not another unseen-source result. Frozen profiles, action predictions and original study results remain unchanged. Use the wrapper for reviewed integration trials.

## Files and reproduction

- [Initial protocol](protocol.json), [third-round protocol](protocol-round-3.json).
- [Draft 1 freeze](freeze-v1.json), [draft 2 freeze](freeze-v2.json), [draft 3 freeze](freeze-v3.json).
- [Development cases](development-cases.json), [first reserved cases](reserved-cases.json), [second reserved cases](validation2-cases.json).
- [Development sources](development-sources.json), [first reserved sources](reserved-sources.json), [second reserved sources](validation2-sources.json).
- [Round 1](round-1.json), [first two versions](results.json), [complete final results](results-final.json).
- [Source verification receipt](source-verification.json).

Source hashes and selectors permit reproduction against the same bytes. Mutable public endpoints may change or disappear. The replay fails on such changes and requires an authorized retained snapshot; it never treats changed bytes as the original test corpus. PDF reconstruction used `pypdf==6.10.0`. The source archives and selected transcript text caches are not included in this public package.
