from __future__ import annotations
import statistics


def confidence_score(data_quality: float, repeatability: float, reference_coverage: float, fingerprint: dict[str, float]) -> dict[str, float | str]:
    dimension_values = [float(v) for k, v in fingerprint.items() if k != "repeatability"]
    if len(dimension_values) >= 2:
        spread = statistics.pstdev(dimension_values)
        signal_agreement = max(0.0, min(100.0, 100.0 - 2.0 * spread))
    else:
        signal_agreement = 0.0
    confidence = 0.30 * data_quality + 0.25 * repeatability + 0.25 * reference_coverage + 0.20 * signal_agreement
    confidence = max(0.0, min(100.0, confidence))
    label = "HIGH" if confidence >= 80 else "MODERATE" if confidence >= 60 else "LOW"
    return {
        "score": round(confidence, 2),
        "label": label,
        "data_quality": round(data_quality, 2),
        "repeatability": round(repeatability, 2),
        "reference_coverage": round(reference_coverage, 2),
        "signal_agreement": round(signal_agreement, 2),
    }
