# Contract templates

These JSON files are labeled examples, not schema definitions or records of successful operations.

| Template | Intended use |
| --- | --- |
| [Lesson](lesson.example.json) | Record a failure hypothesis, scope, expected/observed behavior, counterexamples, and proposed correction |
| [Change proposal](change-proposal.example.json) | Track compatibility, evidence, evaluation, migration, and approval separately |
| [Run receipt](run-receipt.example.json) | Record actual inputs, versions, costs, checks, outputs, and unknowns |
| [Discovery](discovery.example.json) | Illustrate a registry before its channels have been populated |
| [Release manifest](release-manifest.example.json) | Illustrate release metadata before real revisions and hashes exist |

Fill fields from actual evidence. Do not substitute fake hashes or timestamps for null values. A cost of zero is different from an unknown cost. A proposed change grants no authority to release itself.

The operative public candidate pointer is [the repository discovery file](../.well-known/civicspec.json). Its manifest contains real byte counts and hashes; the two release templates here intentionally do not. Full production schemas for these record types remain roadmap R02.
