from pathlib import Path
from componentlife.pipeline import assess_component

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "data/demo_reference/reference_profiles.csv"

def assess(name: str):
    return assess_component(ROOT / f"data/demo_tests/{name}.csv", REF)

def test_healthy_sample_is_suitable():
    result = assess("healthy_alternator")
    assert result["classification"]["category"] == "SUITABLE_PROFILE"
    assert result["confidence"]["score"] >= 80

def test_degraded_sample_requires_further_testing():
    result = assess("degraded_alternator")
    assert len(result["anomalies"]) >= 1
    assert result["classification"]["category"] == "FURTHER_TESTING_REQUIRED"

def test_uncertain_sample_is_inconclusive():
    result = assess("uncertain_alternator")
    assert result["classification"]["category"] == "INCONCLUSIVE"
    assert result["confidence"]["score"] < 60
