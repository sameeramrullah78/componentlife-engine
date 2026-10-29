from pathlib import Path
from componentlife.ingestion.csv_loader import load_test_csv, data_completeness
from componentlife.features.extractor import extract_features

ROOT = Path(__file__).resolve().parents[1]

def test_healthy_features_are_extracted():
    df = load_test_csv(ROOT / "data/demo_tests/healthy_alternator.csv")
    features = extract_features(df)
    assert 14.0 < features["mean_voltage"] < 14.4
    assert features["mean_ripple_mv"] > 0
    assert features["vibration_mean"] > 0
    assert features["temp_rise_c"] > 0
    assert 0 <= features["repeatability_score"] <= 100

def test_uncertain_dataset_has_lower_completeness():
    healthy = load_test_csv(ROOT / "data/demo_tests/healthy_alternator.csv")
    uncertain = load_test_csv(ROOT / "data/demo_tests/uncertain_alternator.csv")
    assert data_completeness(uncertain) < data_completeness(healthy)
