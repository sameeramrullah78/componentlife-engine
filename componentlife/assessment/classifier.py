from __future__ import annotations

SUITABLE_PROFILE = "SUITABLE_PROFILE"
REVIEW = "REVIEW"
FURTHER_TESTING_REQUIRED = "FURTHER_TESTING_REQUIRED"
INCONCLUSIVE = "INCONCLUSIVE"


def classify_condition(fingerprint: dict[str, float], confidence: dict[str, float | str], anomalies: list[dict[str, object]]) -> dict[str, str]:
    conf_score = float(confidence["score"])
    dimension_scores = [float(v) for k, v in fingerprint.items() if k != "repeatability"]
    if conf_score < 60:
        return {"category": INCONCLUSIVE, "reason": "Evidence quality or reference coverage is insufficient for a reliable demo classification."}
    min_score = min(dimension_scores) if dimension_scores else 0.0
    critical = any(a["severity"] == "critical" for a in anomalies)
    if critical or min_score < 45:
        return {"category": FURTHER_TESTING_REQUIRED, "reason": "One or more diagnostic dimensions show a substantial deviation from the demo reference population."}
    if anomalies or min_score < 70:
        return {"category": REVIEW, "reason": "The component remains assessable but one or more degradation indicators require review."}
    return {"category": SUITABLE_PROFILE, "reason": "No material deviation was detected in the supported demo dimensions."}
