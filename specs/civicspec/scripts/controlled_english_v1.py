"""Frozen first combination. Deterministic excerpt probe, not an LLM or full extractor."""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research/2026-09-07/scripts'
sys.path.insert(0, str(RESEARCH))
spec = importlib.util.spec_from_file_location('cce_historical_v2', RESEARCH / 'action_classifier_v2.py')
historical = importlib.util.module_from_spec(spec)
spec.loader.exec_module(historical)


def classify(text):
    t = re.sub(r'\s+', ' ', text).lower()
    if re.search(r'\b(?:motion to table|tabled by)\b', t):
        return 'tabled'
    if re.search(r'\b(?:approv\w*|accept\w*)\b.{0,65}\bminutes\b', t):
        return 'minutes_approval'
    if re.search(r'\b(?:schedul\w*|set|hold)\b.{0,55}\bpublic hearing\b', t):
        return 'schedule_public_hearing'
    return historical.refined(text)


def historical_classify(text):
    return historical.refined(text)
