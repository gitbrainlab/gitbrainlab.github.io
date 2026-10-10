# CivicSpec

**A shared specification for evidence-backed civic knowledge, built for people and agents.**

CivicSpec describes how to turn public records into connected, reviewable accounts of government activity: who acted, in what capacity, on which matter, what was decided, what conditions remain, and what later evidence establishes. It connects documents and recordings to events, assertions, questions, corrections, and the versions of the tools that interpreted them.

An approved contract is not evidence of a payment. Two votes on one matter may decide different motions. A missing record is a coverage gap before it is a conclusion. CivicSpec makes these distinctions explicit so useful analysis survives beyond one model, application, or conversation.

## Status

**Experimental publication: `0.1.0-rc.2`.** This self-contained directory in GitBrainLab’s public documentation repository is the current public home. A dedicated CivicSpec repository can be adopted later through an explicit registry migration. The candidate is a specification and reference toolkit, not a production extractor, certified legal-compliance system, or deployed signal desk. The stable channel is unset. Consumers must explicitly opt into the candidate.

The new [Controlled English profile](docs/controlled-english.md) combines technical writing rules, explicit requirements, civic terminology and a source-linked claim ledger. Its [60-case real-corpus study](evaluations/controlled-english-2026-10-10/REPORT.md) includes two sequential reserved-source tests and publishes remaining failures. The preservation guard is suitable for a reviewed trial; the reference action recognizer remains unsuitable for automatic fact publication. See [implementation guidance](docs/controlled-english-integration.md) and [migration notes](migrations/0.1.0-rc.2.md).

The September 2026 research ontology and the October 2026 adoption contract have separate version histories. Historical mapping results are not production extraction accuracy. See [validation and limitations](docs/validation.md), [research provenance](research/README.md), and [license status](LICENSE_STATUS.md).

## Start here

| You want to… | Read or run |
| --- | --- |
| Understand the model | [Concepts and relationships](docs/model.md) |
| Read the complete requirements | [Adoption and maintenance specification](docs/specification.md) |
| Follow evidence into an assertion | [Worked examples](docs/tutorial.md) and [example files](examples/README.md) |
| Equip an agent | [Agent guide](docs/agents.md), [core instructions](bootstrap/core-instructions.md), and [AGENTS.md](AGENTS.md) |
| Use controlled technical English | [Language profile](docs/controlled-english.md), [runtime supplement](bootstrap/controlled-english.md), and [test results](evaluations/controlled-english-2026-10-10/REPORT.md) |
| Integrate an existing pipeline | [Integration guide](docs/integration.md) |
| Discover and pin a release | [Publication protocol](docs/publication.md) and [release index](releases/README.md) |
| Improve the specification | [Contribution guide](CONTRIBUTING.md) and [roadmap](ROADMAP.md) |

## Run the reference checks

Use Python 3.11 or later. From the host repository, first run `cd specs/civicspec`, then:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

The checks validate the draft example schema, source hashes and exact text selectors, fixture expectations, research-file hashes, repository links, and the controlled-English evaluation contract. The tests deliberately corrupt examples to ensure failures are caught. The default suite does not fetch the real corpus, run a model, or verify real-world civic claims. The optional corpus replay runs deterministic excerpt-level action probes. No model API key or database is required.

After publication, verify the candidate manifest and its local components with:

```sh
python scripts/verify_release.py --root .
```

If HEAD has advanced beyond the candidate's component revision, use `python scripts/verify_published.py` in a full Git checkout to verify the retained release instead.

For agent bootstrap, use the [repository discovery document](.well-known/civicspec.json). On GitHub the machine-readable URL is `https://raw.githubusercontent.com/gitbrainlab/gitbrainlab.github.io/main/specs/civicspec/.well-known/civicspec.json`. Resolve it once, verify the manifest digest, then fetch components at the manifest's full source commit. Do not mix files from a moving `main` branch during a run. No separate website or custom domain is required for this publication.

## What is included

- A complete 23-section adoption contract and fourteen core semantic invariants.
- Public synthetic examples with exact evidence ranges and a limited executable JSON Schema.
- Agent onboarding, role responsibilities, lesson/change workflows, and integration guidance.
- Historical ontology, mapping, vocabulary, and classifier research files with retained hashes.
- A versioned publication protocol, validation utilities, CI, contribution templates, and concrete improvement work.

Production schemas, accepted municipal identities, source adapters, end-to-end SHACL validation, and independently adjudicated performance benchmarks remain work to do. Each gap has an explicit scope and acceptance criteria in the [roadmap](ROADMAP.md). Contributions can improve definitions, examples, evaluation, accessibility, adapters, or implementation; all are useful.

## A useful question

“Did the board approve the project, authorize borrowing, receive funds, or pay an invoice?”

CivicSpec should answer each part with its own evidence, date, conditions, and uncertainty. It should also say what evidence would resolve the parts it cannot yet answer.

## Hosting layout

CivicSpec lives under `specs/civicspec/` in [GitBrainLab’s public documentation repository](https://github.com/gitbrainlab/gitbrainlab.github.io/tree/main/specs/civicspec). Paths in these guides are relative to that directory unless stated otherwise. The host activates a dedicated CivicSpec workflow and issue templates under its root `.github/` directory. This placement publishes the specification without changing other GitBrain projects.
