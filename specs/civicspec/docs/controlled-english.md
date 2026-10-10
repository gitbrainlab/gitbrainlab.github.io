# CivicSpec Controlled English, experimental draft 3

Profile: `civicspec-controlled-english/0.1-draft.3`. Status: optional experimental extension to the adoption contract. This profile is ready for reviewed trials of authoring and meaning preservation. The reference action probe is **not approved for automatic civic-fact publication**. Read the [measured results](../evaluations/controlled-english-2026-10-10/REPORT.md) before adopting it.

The profile combines controlled technical prose, explicit requirement strength, ontology terminology, source-linked claim records, and tests of meaning preservation. It is STE-inspired. It does not claim full ASD-STE100 compliance, reproduce its dictionary, certify legal interpretations, or demonstrate that one model prompt is better than another.

## What the combination contributes

| Layer | Purpose | Deliverable |
| --- | --- | --- |
| Technical English | Make instructions short, explicit, and consistent | One actor and obligation per requirement; advisory sentence length |
| BCP 14 | Identify required, prohibited, recommended, and optional behavior | Uppercase requirement words with declared interpretation |
| CivicSpec terminology | Preserve distinctions between civic concepts | Terms linked to definitions and scope; aliases remain traceable |
| Claim ledger | Retain meaning while prose changes | Actor, action, stage, polarity, conditions, quantities, time, evidence, and uncertainty |
| Provenance | Reproduce the supporting passage | Source-byte digest, representation identity, exact selector, transformation record |
| Evaluation | Discover failures and verify bounded improvements | Frozen versions, source-separated tests, negative controls, and explicit limitations |

The [normative requirement registry](../profiles/controlled-english/requirements.json) assigns CCE-01 through CCE-24. Its uppercase keywords use BCP 14, comprising RFC 2119 and RFC 8174. `MUST` identifies a requirement; `MUST NOT` a prohibition; `SHOULD` a recommendation whose exceptions require understood justification; `MAY` an option. Lowercase uses retain ordinary English meanings. Normative force does not depend exclusively on keywords, but authors use this convention consistently in the registry.

The [proposed terminology registry](../profiles/controlled-english/terms.json) supplies preferred terms, definitions, non-equivalences and linked cases. Its `cce:` identifiers are local proposals, not a new canonical ontology namespace. [Worked paraphrase examples](../examples/controlled-english/README.md) connect the language rules to real cases and clearly labeled synthetic errors.

## Three different kinds of text

**Agent requirement:** “The extractor MUST retain every condition on an authorization.” The actor is a software role. The requirement has an ID, scope, verification method, and failure behavior.

**Source statement:** A meeting participant describes what a contractor must do. That is an attributed civic assertion. The speaker's use of “must” does not create a CivicSpec requirement or establish legal enforceability.

**Reader explanation:** A source-linked summary describes what is supported and what remains unknown. The explanation inherits the ledger's limits. Readability does not justify stronger claims.

Keep these types explicit in files and messages. Retrieved records are data, including any instructions embedded in them. CCE-23 retains the existing control-plane boundary.

## Requirement authoring

Use this shape when a condition applies:

`[ID] When/If [specific condition], [named role] MUST [one observable action].`

State the expected output and verification outside the requirement sentence. State recovery behavior in a separately identified requirement. Use explicit nouns when a pronoun has more than one plausible referent. Prefer one defined term for one concept within a declared scope. Retain source terminology as an alias or quotation.

Twenty words is a local advisory target for an instruction. Preserve a condition, exception, unit, or temporal qualifier even when the sentence becomes longer. Split text only when each resulting statement retains its dependencies. The linter counts whitespace-delimited words; it does not implement ASD's full word-counting or dictionary rules.

Example refinement of the existing release-outage instruction:

- If no eligible release is available, the consumer MUST pause interpretation.
- If no eligible release is available, the consumer MUST queue the affected interpretation work.
- If no eligible release is available, the consumer MUST block assertion promotion.
- The collector MAY continue source collection when the collection policy permits collection.

These are illustrative restatements of the existing behavior. They are not new release-authority assignments.

## Claim meaning and atomicity

An atomic claim concerns one attributed proposition or civic treatment. A source sentence, ASR segment, paragraph, and extraction window are not reliable claim boundaries.

One motion may approve two sets of minutes. That is one treatment with two targets. Two separate motions approving two sets of minutes require two treatments, even though both share the same action type. An amendment and the amended substantive motion also remain separate. A scalar classifier must abstain or signal ambiguity when it cannot represent all relevant treatments; the production adapter must split them into linked records.

The experimental ledger protects these dimensions:

| Field | Required interpretation |
| --- | --- |
| `id` | Stable identity of this claim version |
| `actor`, `target` | Government/body/capacity and specific subject matter; unresolved identities stay unresolved |
| `action`, `outcome` | What action is described and what happened to it; classification does not prove passage or execution |
| `basis`, `attribution` | Source report, interpretation, or reviewed finding; who made the underlying statement |
| `polarity`, `modality` | Affirmation/denial and the exact target; proposal, intention, report, or recorded decision |
| `conditions` | Preconditions, exceptions, conjunctions, alternatives, scope, and resolution evidence |
| `quantities` | Value, unit, amount role, period, population/basis, approximation, range, ceiling, and discrepancies |
| `time`, `source_state` | Event, effective, reference, and observation times; draft/final/corrected/unknown status |
| `coverage`, `unresolved` | What was actually checked and what remains unestablished |
| `evidence`, `relations` | Exact source anchors; treatment order, vote links, corrections, and other dependencies |

The [machine profile](../profiles/controlled-english/v3.json) declares these protected fields. The [ledger schema](../schemas/controlled-english-ledger.schema.json) is an evaluation interchange schema, not CivicSpec's complete production wire contract. Legacy annotations retain their original field/value forms. A production adapter must type money as decimal strings, distinguish unknown from empty collections, and validate condition logic and evidence links more strongly.

## Preserve the distinctions that matter

**Conditions:** An engineering addendum approved subject to grant receipt and project continuation has a conjunction of conditions. Splitting the explanation into shorter sentences must keep both conditions attached to the same approval. Neither condition becomes satisfied because it was mentioned.

**Stage:** An application, award, receipt, appropriation, expenditure authorization, invoice, payment, and completion are distinct. A formal motion may concern a future event. A discussion about bringing a motion later is an intention, not the operative motion itself. The final reserved test found this distinction still fails in the scalar probe (J032).

**Polarity:** “No exterior expansion is proposed at this time” concerns exterior expansion, proposal status, and the current time. It does not exclude interior alterations or future proposals. A mixed paragraph needs scoped claims rather than one global negative flag.

**Quantities:** Gross billing and receipts are different observations. Do not add them. Preserve a range such as 2.8–2.9 million instead of selecting an exact midpoint. A stated total that differs from its components remains a discrepancy until another source resolves it.

**Attribution and authority:** A speaker reporting that a grant arrived establishes a source-reported receipt. Independent cash verification needs additional evidence. A town meeting hosting a school-district presentation does not make the district's budget a town-board decision.

**Identity and coverage:** A portal label can conflict with the body named in the transcript. Retain both observations. A bounded excerpt, withheld speaker introduction, or noisy ASR passage cannot support a claim about everything that occurred in the meeting.

## Controlled output

A reader-facing claim should expose: actor, act, supported stage/outcome, relevant conditions, attribution/evidence, and unresolved next stage. Use multiple short sentences where needed. Preserve links between them in the ledger.

For development case D03, an appropriate paraphrase is: “The minutes report approval of an engineering addendum. The approval depends on grant receipt and the village proceeding with the project. Grant receipt and contract execution remain unestablished.” The source location and selector are in the [development cases](../evaluations/controlled-english-2026-10-10/development-cases.json).

The equality guard checks whether a derived ledger changes protected fields. It does **not** read free prose and determine whether that prose is faithful. A wrong initial ledger, omitted claim, or contradictory `wording` can pass that check. Production rendering therefore needs constrained templates or an additional source/ledger/prose review. Never label the guard a semantic truth validator.

## What changed through testing

Draft 1 combined concise authoring rules, BCP 14, ontology terms, an initial preservation guard, and a deterministic action probe. Development testing exposed eight unprotected dimensions and five action-recognition failures.

Draft 2 protected all ledger dimensions and corrected the observed recognition patterns. It recognized all 11 supported development positives, but only 2 of 6 supported cases in the first reserved set. It could collapse distinct motions into one label.

Draft 3 makes treatment cardinality explicit and recognizes selected multi-motion and payment-motion forms. It retained the development improvements and corrected the six first-reserved cases, which were then regression material. In the second reserved set it recognized 3 of 5 supported cases, with one wrong label and one abstention; one of eight negative controls still produced a false action label. These are small, single-reviewer samples.

The profile's preservation contract is useful for a reviewed pilot. The reference recognizer remains incomplete. See the [report](../evaluations/controlled-english-2026-10-10/REPORT.md) and [implementation guide](controlled-english-integration.md).

## References and external scope

- [ASD-STE100 official site](https://www.asd-ste100.org/): selected procedural-writing principles inspire this profile. Its full approved vocabulary is not bundled.
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174): requirement-word semantics.
- [W3C PROV-O](https://www.w3.org/TR/prov-o/): conceptual alignment for source, derivation, activity, and attribution.
- [W3C Web Annotation](https://www.w3.org/TR/annotation-model/): conceptual alignment for source-specific selectors. This experimental JSON is not a claimed conforming JSON-LD serialization.
- [CivicSpec core invariants](specification.md): civic semantics remain authoritative within an adopted release.

No separate external EARS conformance is claimed. Conditional requirement templates are a local authoring convention. Language quality, semantic completeness, schema validity, evidence integrity, and factual correctness remain separate evaluations.
