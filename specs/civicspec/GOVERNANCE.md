# Governance and review

This initial governance contract is experimental. Repository owners appoint maintainers and define delegated release authority. No named committee, elected council, or external certification is implied.

| Responsibility | Decision |
| --- | --- |
| Contributor | Proposes definitions, examples, code, evidence, or a correction |
| Reviewer | Checks sources and semantics, reproduces relevant checks, records unresolved questions |
| Maintainer | Accepts scoped changes and compatibility decisions under owner-delegated authority |
| Release owner | Publishes a tested inventory and channel revision; records rollback |
| Integrator | Authorizes fleet adoption, corpus access, local review policy, budgets, and publication of civic claims |

One person may hold several roles, but consequential interpretation and label decisions should receive an independent evidence review. Automated review is assistance; the record must make its scope visible.

## Three independent decisions

Publishing a specification makes a revision available. Adopting a release authorizes a particular consumer to use it. Accepting a civic assertion determines whether a claim meets a product's evidence and publication policy. None automatically performs the other two.

## Change decisions

Document the proposal, evidence, alternatives, counterexamples, affected requirements, compatibility, reviewer, decision, and date in an issue/PR or equivalent durable record. Accept local adapter changes locally when possible. Global term changes must explain why a local profile is insufficient. A code or term can be experimental, accepted, deprecated, or superseded; replacement relationships do not erase history.

Where reviewers disagree, retain the competing interpretations and the evidence needed to resolve them. Do not force consensus by removing an inconvenient source or silently redefining the reference label.

## Release decisions

Follow [the publication protocol](docs/publication.md). Candidate releases are opt-in. Stable remains unset until declared evidence, evaluation, compatibility, and operational gates pass. Public availability does not mean every source family, jurisdiction, or ontology term is supported.

Breaking changes require migration and rollback guidance even before version 1.0. Revocation prevents new use under the consumer policy; it must not destroy the archived manifest or source evidence.
