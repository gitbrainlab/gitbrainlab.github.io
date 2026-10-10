"""Deterministic, excerpt-level action classification. No LLM calls, case IDs, or municipality rules.
Input spans are prelocated; scores are NOT end-to-end document extraction accuracy.
"""
import re
LABELS={
 'approve_minutes':'minutes_approval','waive_minutes_reading':'waive_reading',
 'authorize_borrowing':'debt_authorization','amend_prior_bond_resolution':'amendment',
 'amend_project_cost_authorization':'amendment','amend_hearing_schedule':'amendment',
 'authorize_execution_of_cba':'contract_authorization','authorize_contract_execution':'contract_authorization',
 'award_contract':'contract_award','reject_all_bids':'reject_bids',
 'authorize_purchase_and_payment':'spending_authorization','authorize_grant_spending':'spending_authorization',
 'authorize_reserve_expenditure':'spending_authorization','approve_transfer':'spending_authorization',
 'appoint_employee':'appointment','appoint_employee_conditionally':'conditional_appointment',
 'table_matter':'tabled','ambiguous_tabling_sequence':'ambiguous',
 'purchase_recommendation':'recommendation','report_delivery_delay':'status_report',
 'report_no_responses':'no_responses','enter_and_exit_executive_session':'executive_session',
 'reschedule_meeting':'scheduling',
}
def normalize(text:str)->str:
 return re.sub(r'\s+',' ',text).lower()
def baseline(text:str)->str:
 t=normalize(text)
 for token,label in [('bond','debt_authorization'),('contract','contract_authorization'),('approve','approval'),('appoint','appointment'),('purchase','spending_authorization'),('grant','spending_authorization'),('minutes','minutes_approval'),('motion','approval')]:
  if token in t:return label
 return 'abstain'
def refined(text:str)->str:
 t=normalize(text)
 # Documentary ambiguities and procedural outcome precede proposed resolution text.
 if 'motion to table' in t and re.search(r'the tabled resolution was .*?brought to a vote',t):return 'ambiguous'
 if re.search(r'\b(tabled by|motion .*? to table|motion to table)\b',t):return 'tabled'
 if re.search(r'(reject\w* (?:all )?(?:the )?bids|rejection of bids)',t):return 'reject_bids'
 if re.search(r'(zero|no) responses',t):return 'no_responses'
 if re.search(r'dispense with (?:the )?reading',t):return 'waive_reading'
 if re.search(r'accept meeting minutes|approve the minutes',t):return 'minutes_approval'
 if 'executive session' in t and ('enter into' in t or 'enter the' in t):return 'executive_session'
 if re.search(r'appoint\w* ',t):
  return 'conditional_appointment' if 'subject to final approval' in t else 'appointment'
 if ('quote' in t or 'recommended' in t) and re.search(r'decision for purchase be made|suggested.*?funds be used',t):return 'recommendation'
 if re.search(r'truck.*?expected.*?now|supply chain.*?late|forecast|delivery.*?delay',t):return 'status_report'
 if ('amend' in t and 'resolution' in t) or ('increase in the maximum cost' in t):return 'amendment'
 if re.search(r'awarding.*?bid|award.*?contract|awarded.*?bid',t) and not 'not award' in t:return 'contract_award'
 if 'collective bargaining' in t and ('authoriz' in t or 'approv' in t):return 'contract_authorization'
 if re.search(r'authoriz.*?(?:execute|enter into).*?(?:agreement|contract)|authoriz.*?contract.*?mayor',t):return 'contract_authorization'
 if re.search(r'authoriz.*?(?:serial bonds|issuance.*?bonds)|bond resolution.*?finance',t):return 'debt_authorization'
 if re.search(r'authoriz.*?(?:spen|expend|payment|purchase)|new server.*?not to exceed',t):return 'spending_authorization'
 if 'meeting' in t and re.search(r'(reschedul|updated october|change.*?date)',t):return 'scheduling'
 return 'abstain'
