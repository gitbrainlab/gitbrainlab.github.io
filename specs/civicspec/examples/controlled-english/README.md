# Source-grounded paraphrase examples

These are newly authored teaching paraphrases of the evaluation labels. The unsafe sentences are **deliberately invented counterexamples**, not observed bot outputs or accepted civic facts. The source locators and exact selectors are in the [development](../../evaluations/controlled-english-2026-10-10/development-cases.json) and [second-reserved](../../evaluations/controlled-english-2026-10-10/validation2-cases.json) case files. Labels have one assistant reviewer and no original-audio verification.

| Case | Deliberately unsafe paraphrase | Meaning-preserving interpretation | Check |
| --- | --- | --- | --- |
| D03 | The village executed the engineering contract and received the grant. | The minutes report conditional approval of an addendum. Grant receipt and proceeding with the project are conditions; execution remains unestablished. | Keep authorization, conditions and execution separate. |
| J032 | The board scheduled the budget hearing. | A speaker described the intended hearing date and said official scheduling would follow the preliminary budget. The selected passage does not establish that scheduling action. | Preserve prospective modality and its condition. The scalar probe still fails here. |
| J061 | The board approved the minutes and paid all listed amounts. | The source contains separate minutes and abstract motions, corrections to earlier figures, and current figures. Represent these separately; payment is not established. | Preserve treatment identities, period and correction links. The scalar probe still collapses this passage. |
| J022 | The town adopted the school's budget. | A school-district representative presented the district's proposed budget at the town meeting. The passage does not establish a budget-adoption vote. | Preserve speaker capacity and separate host body from subject entity. |

Changing these words alone does not guarantee a bot will infer the right records. Extract and review the ledger, render the explanation, then compare each consequential clause with its evidence. Keep all published examples out of a future unseen model test.
