from __future__ import annotations
import pandas as pd


def thermal_features(df: pd.DataFrame) -> dict[str, float]:
    valid = df[["timestamp", "temp_c"]].dropna()
    if len(valid) < 2:
        return {"temp_start_c": float("nan"), "temp_end_c": float("nan"), "temp_rise_c": float("nan"), "temp_rise_per_min": float("nan"), "max_temp_c": float("nan")}
    start_temp = float(valid.iloc[0]["temp_c"])
    end_temp = float(valid.iloc[-1]["temp_c"])
    start_t = float(valid.iloc[0]["timestamp"])
    end_t = float(valid.iloc[-1]["timestamp"])
    minutes = max((end_t - start_t) / 60.0, 1e-9)
    rise = end_temp - start_temp
    return {
        "temp_start_c": start_temp,
        "temp_end_c": end_temp,
        "temp_rise_c": float(rise),
        "temp_rise_per_min": float(rise / minutes),
        "max_temp_c": float(valid["temp_c"].max()),
    }
