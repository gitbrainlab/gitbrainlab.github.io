# Worked examples

All examples here are synthetic. They establish no facts about an actual municipality, meeting, contract, or person. The four machine-readable assertions are in [assertions.example.json](../examples/assertions.example.json), with exact source text in [synthetic-source.txt](../examples/synthetic-source.txt).

## 1. Two votes, one matter

The source first says that a motion to add Ordinance 46 to the agenda passed with six affirmative votes. It then says the ordinance passed with four affirmative votes, two abstentions, and one absence.

The expected representation has one shared matter and two distinct treatments and vote IDs:

| Assertion | Matter | Treatment | Vote | Affirmative count |
| --- | --- | --- | --- | --- |
| `urn:example:assertion:1` | Ordinance 46 | Agenda inclusion | `urn:example:vote:1` | 6 |
| `urn:example:assertion:2` | Ordinance 46 | Ordinance passage | `urn:example:vote:2` | 4 |

The JSON illustrates affirmative counts only. The quote retains the other counts, but this is not a complete roll-call model. A production adapter must encode noes, abstentions, absences, recusals, and attendance where supported. Neither count establishes legal effect or execution by itself. Requirements: CS-03, CS-04, CS-05, CS-10.

## 2. Conditional approval

The engineering addendum is approved conditional on receiving a grant and proceeding with the project. Assertion 3 retains both conditions. It supplies no evidence that the grant was received, the contract was executed, or the work began.

A useful answer is: “The source reports conditional approval; grant receipt and project commencement are unresolved.” A useful follow-up asks the existing collector for the award/disbursement record or executed contract, within a bounded scope. It does not create those facts from the approval sentence. Requirements: CS-05, CS-07, CS-09.

## 3. Negated topic

A speaker says the subject is not a data center. Assertion 4 preserves the attribution and negative polarity. The phrase `data center` is discoverable as a topic, but this sentence does not establish an affirmative data-center project. It also does not independently prove the speaker's classification is correct. Requirements: CS-06, CS-08.

## 4. Reproduce the evidence selection

Every assertion carries a source hash, representation hash, and zero-based, end-exclusive Unicode code-point range. Here the source already is the retained UTF-8 text, so the two hashes match legitimately. In OCR or ASR they ordinarily refer to different byte objects.

```python
import hashlib
import json
from pathlib import Path

root = Path("examples")
raw = (root / "synthetic-source.txt").read_bytes()
text = raw.decode("utf-8")
data = json.loads((root / "assertions.example.json").read_text())
evidence = data["assertions"][0]["evidence"][0]
selector = evidence["selector"]
assert hashlib.sha256(raw).hexdigest() == evidence["representation_sha256"]
assert text[selector["start"]:selector["end"]] == selector["quote"]
```

Changing line endings changes the digest. JavaScript string offsets are UTF-16 code units; use an explicit code-point conversion before comparing these selectors. Normalization, redaction, and timestamp repair produce new representations rather than silent edits to the source.

## 5. Finance: roles before arithmetic

Consider a separate synthetic scenario: a board authorizes a project ceiling of $10 million, permits up to $8 million in borrowing, later issues a $3 million short-term note, and records a $1 million contractor payment. Those are four observations with different roles. They do not sum to $22 million in spending. Conversion to a long-term instrument is another event with its own principal, dates, terms, and relationships.

This scenario is conceptual; no production finance schema or statewide policy calculation is implemented here. A contribution under [R09](../ROADMAP.md) should preserve instruments, funds, fiscal years, cash/accrual bases, state aid eligibility/receipt, and attribution before comparing taxpayer effects. Requirements: CS-05, CS-10, CS-12.

## 6. A lesson becomes a proposal

The [lesson template](../contracts/lesson.example.json) describes an extractor that notices an amendment but loses the underlying application decision. The [change proposal](../contracts/change-proposal.example.json) separates that hypothesis from an approved fix. The templates intentionally have no real evidence or successful evaluation attached.

To make the lesson actionable, attach permission-cleared source spans, expected and observed outputs, counterexamples, affected versions, and an impact query. Evaluate the unchanged baseline and the candidate on reviewed cases. Preserve uncertainty if the longer source context still does not establish which action occurred. Only the applicable reviewer/release policy can promote the change.
