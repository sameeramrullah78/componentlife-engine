from __future__ import annotations

DIMENSION_METRICS = {
    "electrical_output": ["mean_voltage", "mean_current"],
    "electrical_stability": ["voltage_std", "current_std"],
    "ripple_behaviour": ["mean_ripple_mv", "ripple_std_mv"],
    "mechanical_condition": ["vibration_mean", "vibration_peak", "vibration_std"],
    "thermal_behaviour": ["temp_rise_c", "temp_rise_per_min", "max_temp_c"],
}


def build_fingerprint(comparison: dict[str, dict[str, float]], features: dict[str, float]) -> dict[str, float]:
    fingerprint: dict[str, float] = {}
    for dimension, metrics in DIMENSION_METRICS.items():
        scores = [float(comparison[m]["reference_score"]) for m in metrics if m in comparison]
        fingerprint[dimension] = round(sum(scores) / len(scores), 2) if scores else 0.0
    fingerprint["repeatability"] = round(float(features.get("repeatability_score", 0.0)), 2)
    return fingerprint
