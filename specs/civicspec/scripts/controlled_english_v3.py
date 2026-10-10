"""Third candidate: bounded ambiguity detection and payment-motion recognition.

Refined after the first reserved set. Frozen before the second reserved set.
This scalar probe can flag some multi-treatment spans but cannot split events.
"""
import re
from controlled_english_v2 import classify as second_combination


def classify(text):
    t=re.sub(r'\s+',' ',text).lower()
    agenda_motion=re.search(r'motion to amend the agenda',t)
    minutes_motion=re.search(r'accept.{0,25}\bminutes\b',t)
    if agenda_motion and minutes_motion:
        return 'ambiguous'
    if len(re.findall(r'motion(?: for that)? second',t))>=2:
        return 'ambiguous'
    if re.search(r'appoint\w*',t) and re.search(r'\bnext is a vote\b.{0,100}\bbond resolution\b',t):
        return 'ambiguous'
    if re.search(r'\bmotion to pay\b.{0,45}\b(?:vouchers|bills)\b',t):
        return 'spending_authorization'
    return second_combination(text)
