# Profiles and extensions

A profile specializes CivicSpec for a jurisdiction, public body, source producer, document family, time period, or domain. Record that scope explicitly. A formatting convention and a legal rule are different kinds of knowledge and require different validation.

## Profile proposal contents

| Field | Required meaning |
| --- | --- |
| Identity and status | Stable profile ID, version, experimental/accepted/deprecated status |
| Applicability | Jurisdiction, body/capacity, source family, producer version/era, effective interval |
| Dependencies | Pinned core contract, vocabulary, related profiles and adapter |
| Mappings | Source fields/patterns to predicates and typed values; preserve unmapped fields |
| Evidence handling | Representation identity, selector convention, transformation and access rules |
| Unknown behavior | Abstain, retain source-local value, propose extension, or request evidence |
| Constraints | Requirement IDs, executable checks, human review and unsupported cases |
| Evaluation | Source-level sample, label version, cases, counterexamples, results and costs |
| Compatibility | Breaking meanings/shapes, migration, affected-output query, rollback |

The historical [onboarding template](../research/2026-09-07/profiles/onboarding-template.yaml) is research material, not an automatically accepted production profile.

## Extension rule

Preserve an unknown source value and propose a scoped extension. The teaching examples use `ext:` to mark unaccepted predicates. Do not add an unknown value to a global vocabulary merely to improve coverage. Define its meaning, contrast it with nearby terms, and test counterexamples before promotion.

An adapter can recognize a producer's phrase while still abstaining on its legal effect. Accepted source-format mappings do not establish legal applicability across jurisdictions or history.

## Capital-finance profile work

For school districts and towns, begin with separate entity and authority profiles. Link project authorization, financing plan, instrument, issuance/refinancing, proceeds, expenditure, aid award/eligibility/receipt, and annual debt service. Preserve fiscal year, fund, accounting basis, principal versus interest, nominal versus modeled present value, and source-reported versus computed amounts.

A short-term-to-long-term conversion is a relationship between financing events. Any claim about taxpayer savings or structural costs requires comparable cash flows, terms, aid treatment, assumptions, and uncertainty. The ontology must support competing hypotheses and evidence rather than encode the conclusion in the taxonomy.

## Publication-rule profile work

Separate observed availability from applicability and legal conclusions. Retain checked venue, first/last observation, relevant event time, body class, rule version, effective interval, conditions, exceptions, and unresolved inputs. A matched recording is not sufficient evidence of completeness or timely availability. Report denominator and age/cohort filters on each metric.
