"""Second candidate, refined on development failures before reserved-source reads.

Labels describe the action mentioned in the selected excerpt, not proven execution
or the outcome of a vote. Rules are deliberately narrow and can abstain.
"""
import re
from controlled_english_v1 import classify as first_combination


def classify(text):
    t = re.sub(r'\s+', ' ', text).lower()
    # An operative treatment takes priority over an approval heading.
    if re.search(r'\baction was tabled\b|\bmotion.{0,45}\bto table\b|\bmove that we table\b', t):
        return 'tabled'
    # "As amended" qualifies the application, not a replacement action class.
    if re.search(r'\b(?:approv\w*|authoriz\w*)\b.{0,160}\bgrant\b.{0,35}\bapplication\b', t):
        return 'grant_application'
    if re.search(r'\bmotion approv\w*\b.{0,45}\bcontract addendum\b', t):
        return 'contract_authorization'
    if re.search(r'\bmotion to hire\b', t):
        return 'conditional_appointment' if re.search(r'\b(?:pending|contingent|subject to)\b', t) else 'appointment'
    if re.search(r'\bconvened in executive session\b', t):
        return 'executive_session'
    return first_combination(text)
