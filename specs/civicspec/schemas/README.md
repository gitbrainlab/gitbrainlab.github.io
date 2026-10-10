# Schema scope

[assertion-fixture.schema.json](assertion-fixture.schema.json) is a JSON Schema Draft 2020-12 contract for the four **synthetic teaching assertions** in this repository. It validates their envelope, typed count/code values, evidence selectors, candidate status, and ineligibility for real civic publication.

It is intentionally narrow: `count` and `code` values only, fixture text selectors, synthetic IDs, and null operational metadata. It is not the complete production assertion/source/event/lesson schema required by the adoption specification. It must not be used as a production conformance gate by removing synthetic constraints.

The validator additionally checks hashes, exact quote/range agreement, IDs, and the specific fixture expectations. JSON Schema cannot verify those byte relationships or determine real-world truth on its own. Full schemas, event references, vocabularies, and migration tests are roadmap R02/R03/R07.
