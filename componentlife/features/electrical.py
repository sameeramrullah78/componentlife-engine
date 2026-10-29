from __future__ import annotations
import math
import pandas as pd


def _safe_std(series: pd.Series) -> float:
    value = float(series.std(ddof=0))
    return 0.0 if math.isnan(value) else value


def electrical_features(df: pd.DataFrame) -> dict[str, float]:
    voltage = df["voltage"].dropna()
    current = df["current"].dropna()
    ripple = df["ripple_mv"].dropna()
    return {
        "mean_voltage": float(voltage.mean()) if len(voltage) else float("nan"),
        "voltage_std": _safe_std(voltage) if len(voltage) else float("nan"),
        "mean_current": float(current.mean()) if len(current) else float("nan"),
        "current_std": _safe_std(current) if len(current) else float("nan"),
        "mean_ripple_mv": float(ripple.mean()) if len(ripple) else float("nan"),
        "ripple_std_mv": _safe_std(ripple) if len(ripple) else float("nan"),
    }
