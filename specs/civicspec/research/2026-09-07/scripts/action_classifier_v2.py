"""Post-first-holdout refinement. Frozen before second cold sample inspection."""
import re
from action_classifier import normalize,refined as v1,LABELS as BASE_LABELS
LABELS={**BASE_LABELS,'authorize_grant_application':'grant_application','authorize_solicitation':'solicitation_authorization','clarify_appointment_term':'appointment_amendment','adopt_budget':'budget_adoption','authorize_external_request':'external_request'}
def refined(text:str)->str:
 t=normalize(text)
 early=v1(text)
 if early in {'tabled','ambiguous','reject_bids','waive_reading','no_responses'}:return early
 if re.search(r'(?:enter|adjourn\w*) (?:into|to) (?:an? )?executive session',t):return 'executive_session'
 if 'clarif' in t and 'appointment term' in t:return 'appointment_amendment'
 if re.search(r'adopt.*?final.*?budget|adopt.*?budget.*?fiscal year',t):return 'budget_adoption'
 if re.search(r'authoriz.*?(?:issuance|issue).*?request for bids|solicit.*?sealed bids',t) and not re.search(r'awarding a contract|award.*?bid',t):return 'solicitation_authorization'
 if re.search(r'approval of the application|approv.*?grant application',t):return 'grant_application'
 if re.search(r'authoriz.*?send a request|authorize.*?submit.*?request',t):return 'external_request'
 if re.search(r'authoriz.*?sign.*?agreement|approv.*?bid from',t):
  return 'contract_award' if 'bid from' in t else 'contract_authorization'
 if 'budget amendments' in t and re.search(r'resolved.*?authoriz',t):return 'spending_authorization'
 if re.search(r'adopt.*?bond resolution',t):return 'debt_authorization'
 if re.search(r'approv.*?amount not to exceed|approv.*?expend',t):return 'spending_authorization'
 return early
