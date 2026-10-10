# Historical research baseline

The `2026-09-07/` directory contains twelve selected files copied byte for byte from the September 7 CivicSpec Ontology Backtest. [baseline-manifest.json](baseline-manifest.json) records their original byte counts and hashes, plus the source archive digest. The public validation command verifies those retained bytes.

| Files | Purpose |
| --- | --- |
| [Layer definitions](2026-09-07/ontology/layers.json) and [graph](2026-09-07/ontology/layer-graph.ttl) | Research concepts, dependencies, and standards alignment |
| [Constraints](2026-09-07/ontology/constraints.md) and [SHACL shapes](2026-09-07/ontology/shapes.ttl) | Historical integrity boundaries and proposed shapes |
| [Questions](2026-09-07/ontology/question-definitions.json) | Research competency-question seeds |
| [Mapping profiles](2026-09-07/mappings/profiles-v5.json) | Original comparative profiles including `layered_v5_replay` |
| [Original vocabulary](2026-09-07/mappings/controlled-vocab.json) and [v4 vocabulary](2026-09-07/mappings/controlled-vocab-v4.json) | Preserve distinct historical controlled-value inventories |
| [Classifier](2026-09-07/scripts/action_classifier.py) and [v2 classifier](2026-09-07/scripts/action_classifier_v2.py) | Retained research implementations; not production adapters |
| [Onboarding template](2026-09-07/profiles/onboarding-template.yaml) | Historical profile setup template |
| [Standards register](2026-09-07/sources/standards.json) | Linked primary design references |

## Scope and limitations

The full case corpus, source snapshots, private operational archives, generated graph, and historical execution environment are not included. Case IDs and implementation-status strings inside these files refer to the original experiment. The historical classifiers may expect files outside this selected subset; they are not invoked by the public quickstart. This checkout does not reproduce the full historical backtest.

The `https://example.invalid/civicspec/v0.5/` namespace is retained research notation. It is not a newly established production namespace or a claim that the public adoption contract is version 0.5. Do not rewrite these files to make them look current. New semantics belong in separately reviewed paths with a crosswalk and migration note.

The historical shapes were not executed by a SHACL engine in the original reported run or by this repository's reference suite. Hash verification preserves the artifact; it does not establish semantic correctness, legal conformance, or source truth. See [validation](../docs/validation.md) and roadmap R06/R11.
