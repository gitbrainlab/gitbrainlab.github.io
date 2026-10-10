# Validation, research results, and limitations

## What runs here

| Check | Scope | Does not establish |
| --- | --- | --- |
| JSON Schema 2020-12 | Four synthetic assertions and their evidence envelope | A complete production wire schema or source truth |
| Evidence checks | Fixture-byte hashes and exact Unicode code-point selectors | Original PDF/audio verification or authenticity of a remote source |
| Semantic fixture expectations | Two distinct votes/treatments; retained conditions; negative polarity | General-purpose extraction or legal reasoning |
| Negative regression tests | Rejection of deliberately corrupted examples and unsafe release inventories | Accuracy over real municipal records |
| Research hashes | Unchanged bytes for the selected imported research files | Fresh execution of the historical backtest |
| Repository checks | JSON syntax, schema syntax, local Markdown targets and key documentation | Availability of every external reference or a rendered website |
| Release verification | Manifest/discovery consistency and listed component digests | Authority of an untrusted registry or production approval |

Run the commands in [README](../README.md). The output states the actual local checks performed. CI uses the same commands. There is no network fetch, LLM call, legal scoring, RDF graph execution, or live bot deployment in the reference suite.

The draft fixture schema intentionally permits null operational timestamps and release identifiers only because all its records are visibly synthetic and ineligible for a civic fact view. Do not remove the synthetic marker and treat the result as a production assertion. R02 is the work package for a complete wire contract.

## Historical observations

The October 10 research exercise reported:

| Measure | Result | Interpretation |
| --- | --- | --- |
| Field-path fit | 206 mapped occurrences / 215 | Mapping availability on 24 selected cases |
| Controlled-value fit | 18 recognized occurrences / 30 | Vocabulary coverage, separate from field-path fit |
| Unchanged action classifier | 5 correct, 5 abstaining, 1 incorrect / 11 supported positive cases | Narrow classifier result, not end-to-end accuracy |
| Negative controls | 5 abstained | Result for those five controls only |
| Outside classifier scope | 8 cases | Not reclassified as successes or failures |

These are reported historical results from a purposeful, single-reviewer sample. The private case/source package is not included in this public repository; the table cannot be independently reproduced from this checkout. Selected ontology/mapping/classifier files are retained under [research](../research/README.md). The original 551/551 post-refinement replay is a field-mapping result, not extraction accuracy.

Known follow-ups include separate treatment/vote identity, body resolution, source-to-reader quotation alignment, conditions, polarity, quantities, draft status, vocabulary/classifier mismatch, and comparable cross-place evidence. A 1-versus-57 timeliness count discrepancy was reconciled by differing age cohorts; it must not be described as an unresolved arithmetic defect. Recording matches on negative indicators remain review candidates, not proven violations or proven false positives.

## Evaluation required for adoption

Review the seed labels independently. Publish a permission-cleared evaluation manifest with sample selection, label provenance, disagreements, dates, source families, and applicable profiles. Hold out sources/meetings or matters to prevent duplicate-span leakage. Teaching examples cannot serve as unseen tests.

Measure incorrect promotions, supported-case extraction, abstention, source coverage, evidence resolvability, review burden, and resource use separately. Set cohort-specific targets before evaluating the candidate. A pilot of 30 new source items is a planning starting point in the specification, not a statistical reliability claim.

Stable promotion requires declared gates and operational evidence. A validator can enforce that evidence is present and resolves; it cannot decide that every interpretation is true. Historical SHACL shapes remain unexecuted by this suite. Full conformance and production extraction are explicitly unsupported in this publication.
