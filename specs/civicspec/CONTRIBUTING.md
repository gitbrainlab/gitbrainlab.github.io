# Contributing to CivicSpec

Start with [the model](docs/model.md), the relevant [specification requirement](docs/specification.md), and the [roadmap](ROADMAP.md). People and agents use the same evidence and review standards.

## Choose a useful contribution

- Explain an ambiguous definition with one positive example and one counterexample.
- Add a synthetic example for a difficult source pattern, including expected abstention.
- Propose a producer or jurisdiction profile without silently changing global meaning.
- Improve source selectors, accessible documentation, validation, or release tooling.
- Design a representative evaluation set with defensible labels and denominators.

Use the repository's issue templates for semantic proposals and reproducible defects. Search existing issues before opening another. A roadmap ID is a reference, not a claim that a GitHub issue already exists.

## Submit a change

1. Identify the problem, affected users, and requirement IDs such as CS-04 or CS-09.
2. State whether this changes documentation, wire structure, shared meaning, a local adapter, or a reference label.
3. Include the smallest reproducible source example and the observed versus expected behavior. Use synthetic or publication-cleared material. Preserve provenance for real records; do not upload private operational archives.
4. Explain alternatives, counterexamples, compatibility, and affected outputs. An uncertainty-preserving abstention can be the correct result.
5. Make a focused branch and pull request. Run the commands in [README](README.md), and report exact results and anything not run.
6. For semantic changes, add a regression and compare the unchanged baseline with the candidate. Reference-label changes require their own rationale; they must not be hidden inside a claimed performance gain.

Documentation-only corrections need link/content review, not invented behavioral tests. A source snapshot used for tuning becomes development material; do not later present it as unseen evaluation data.

## Expectations for agent contributions

Follow [AGENTS.md](AGENTS.md). Identify model/tool assistance and human or automated review in the PR. Do not invent test results, references, maintainer approval, deployment success, or an execution transcript. Cite source spans for domain claims. Do not treat agreement between agents as independent evidence.

Keep proposed extensions scoped and namespaced until accepted. Bots may prepare patches and evaluations within their assigned authority; they may not approve themselves or change a release gate to pass their patch.

## Review standard

A reviewer should be able to reproduce the failure, inspect the evidence, understand the changed meaning, run the relevant checks, and identify the cost of adoption or rollback. Definitions and examples must agree. A schema pass is only a structural result.

Be specific and respectful. Critique a claim or implementation with evidence. Do not use an issue to accuse an official or institution based only on missing records or model inference.

## Licensing

The repository currently has [no selected project license](LICENSE_STATUS.md). Do not add material whose redistribution is incompatible with its terms, remove third-party notices, or assert a licensing grant that the owner has not made. A maintainer must resolve licensing before presenting the project as open-source or offering broad reuse terms.
