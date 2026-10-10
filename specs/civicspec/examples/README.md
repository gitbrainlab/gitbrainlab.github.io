# Public examples

[synthetic-source.txt](synthetic-source.txt) is invented teaching material. [assertions.example.json](assertions.example.json) contains four manually constructed candidate assertions with exact selectors. They demonstrate two votes on separate treatments of one matter, conditional approval, and a negated topic. They are not outputs from a tested extractor.

Read the [tutorial](../docs/tutorial.md), then run `python scripts/validate.py` from the repository root. The schema deliberately marks every assertion as synthetic and ineligible for a civic fact view. Null times and release references are intentional missing operational context; they are not valid production defaults.

Changing source text or line endings requires updating evidence hashes and selectors. Do not silently change a fixture label to accommodate an extractor. A semantic fixture correction needs a separate rationale, counterexample, and review.

The [contract examples](../contracts/README.md) illustrate lesson, change, run, and release records. More examples—finance stages, identity collisions, corrected minutes, Unicode and ASR alignment—are requested in [the roadmap](../ROADMAP.md).
