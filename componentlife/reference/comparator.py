from __future__ import annotations
from pathlib import Path
import math
import pandas as pd
from componentlife.preprocessing.normalization import z_score, reference_score


def load_reference_profiles(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    required = {"metric", "mean", "std", "sample_count"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Reference file missing columns: {sorted(missing)}")
    return df


def compare_features(features: dict[str, float], reference_df: pd.DataFrame) -> dict[str, dict[str, float]]:
    ref = reference_df.set_index("metric")
    comparison: dict[str, dict[str, float]] = {}
    for metric, value in features.items():
        if metric not in ref.index or not isinstance(value, (int, float)) or math.isnan(value):
            continue
        mean = float(ref.loc[metric, "mean"])
        std = float(ref.loc[metric, "std"])
        sample_count = float(ref.loc[metric, "sample_count"])
        comparison[metric] = {
            "value": float(value),
            "reference_mean": mean,
            "reference_std": std,
            "z_score": float(z_score(float(value), mean, std)),
            "reference_score": float(reference_score(float(value), mean, std)),
            "sample_count": sample_count,
        }
    return comparison


def reference_coverage(features: dict[str, float], comparison: dict[str, dict[str, float]]) -> float:
    numeric = [k for k, v in features.items() if isinstance(v, (int, float)) and not math.isnan(v)]
    if not numeric:
        return 0.0
    metric_coverage = len(comparison) / len(numeric)
    avg_count = sum(v["sample_count"] for v in comparison.values()) / len(comparison) if comparison else 0.0
    sample_strength = min(1.0, avg_count / 30.0)
    return 100.0 * (0.7 * metric_coverage + 0.3 * sample_strength)
