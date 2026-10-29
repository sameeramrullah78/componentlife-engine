from __future__ import annotations
import numpy as np
import pandas as pd
from .electrical import electrical_features
from .vibration import vibration_features
from .thermal import thermal_features


def repeatability_metric(df: pd.DataFrame) -> float:
    columns = ["voltage", "current", "ripple_mv", "vibration_rms"]
    cvs: list[float] = []
    for col in columns:
        series = df[col].dropna().to_numpy(dtype=float)
        if series.size < 3:
            continue
        mean = abs(float(np.mean(series)))
        std = float(np.std(series))
        if mean > 1e-9:
            cvs.append(std / mean)
    if not cvs:
        return 0.0
    avg_cv = float(np.mean(cvs))
    return max(0.0, min(100.0, 100.0 - 400.0 * avg_cv))


def extract_features(df: pd.DataFrame) -> dict[str, float]:
    features: dict[str, float] = {}
    features.update(electrical_features(df))
    features.update(vibration_features(df))
    features.update(thermal_features(df))
    features["repeatability_score"] = repeatability_metric(df)
    features["mean_rpm"] = float(df["rpm"].dropna().mean()) if df["rpm"].notna().any() else float("nan")
    return features
