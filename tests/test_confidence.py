from componentlife.analytics.confidence import confidence_score

def test_confidence_is_bounded():
    result = confidence_score(
        data_quality=100,
        repeatability=100,
        reference_coverage=100,
        fingerprint={
            "electrical_output": 90,
            "electrical_stability": 90,
            "ripple_behaviour": 90,
            "mechanical_condition": 90,
            "thermal_behaviour": 90,
            "repeatability": 100,
        },
    )
    assert 0 <= result["score"] <= 100
    assert result["label"] == "HIGH"
