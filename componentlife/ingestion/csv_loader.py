from __future__ import annotations
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = ["timestamp", "rpm", "voltage", "current", "ripple_mv", "vibration_rms", "temp_c"]


def load_test_csv(path: str | Path) -> pd.DataFrame:
    """Load and validate a ComponentLife v0.1 alternator-test CSV."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    if len(df) < 10:
        raise ValueError("At least 10 samples are required for a demo assessment.")
    for col in REQUIRED_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    if df["timestamp"].isna().all():
        raise ValueError("timestamp must contain numeric values.")
    return df.sort_values("timestamp").reset_index(drop=True)


def data_completeness(df: pd.DataFrame) -> float:
    """Return required-field completeness as a percentage."""
    total = len(df) * len(REQUIRED_COLUMNS)
    missing = int(df[REQUIRED_COLUMNS].isna().sum().sum())
    return max(0.0, min(100.0, 100.0 * (total - missing) / total))
