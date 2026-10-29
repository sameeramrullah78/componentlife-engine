from __future__ import annotations
from pathlib import Path
from componentlife.ingestion.csv_loader import load_test_csv, data_completeness
from componentlife.preprocessing.filtering import interpolate_short_gaps
from componentlife.features.extractor import extract_features
from componentlife.reference.comparator import load_reference_profiles, compare_features, reference_coverage
from componentlife.analytics.anomaly import detect_anomalies
from componentlife.analytics.fingerprint import build_fingerprint
from componentlife.analytics.confidence import confidence_score
from componentlife.assessment.classifier import classify_condition


def assess_component(test_csv: str | Path, reference_csv: str | Path) -> dict:
    raw = load_test_csv(test_csv)
    quality = data_completeness(raw)
    prepared = interpolate_short_gaps(raw)
    features = extract_features(prepared)
    reference = load_reference_profiles(reference_csv)
    comparison = compare_features(features, reference)
    anomalies = detect_anomalies(comparison)
    fingerprint = build_fingerprint(comparison, features)
    coverage = reference_coverage(features, comparison)
    confidence = confidence_score(quality, float(features["repeatability_score"]), coverage, fingerprint)
    classification = classify_condition(fingerprint, confidence, anomalies)
    return {
        "engine_version": "0.1.0",
        "source_file": str(test_csv),
        "reference_file": str(reference_csv),
        "features": features,
        "comparison": comparison,
        "anomalies": anomalies,
        "fingerprint": fingerprint,
        "confidence": confidence,
        "classification": classification,
        "disclaimer": "Proof-of-concept output only. Synthetic/illustrative reference data. Not a certification, safety decision, or remaining-life guarantee.",
    }
