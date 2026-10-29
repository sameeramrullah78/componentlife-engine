import json
from pathlib import Path
from componentlife.pipeline import assess_component
from componentlife.reporting.report_generator import to_markdown

ROOT = Path(__file__).resolve().parents[1]

def test_result_is_json_serializable_and_report_is_explainable():
    result = assess_component(
        ROOT / "data/demo_tests/healthy_alternator.csv",
        ROOT / "data/demo_reference/reference_profiles.csv",
    )
    json.dumps(result)
    report = to_markdown(result)
    assert "Degradation Fingerprint" in report
    assert "Confidence Factors" in report
    assert "Important limitation" in report
