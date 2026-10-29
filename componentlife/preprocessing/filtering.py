from __future__ import annotations
import pandas as pd


def interpolate_short_gaps(df: pd.DataFrame, columns: list[str] | None = None, limit: int = 3) -> pd.DataFrame:
    """Interpolate only short internal gaps; larger gaps remain visible to confidence scoring."""
    result = df.copy()
    columns = columns or ["rpm", "voltage", "current", "ripple_mv", "vibration_rms", "temp_c"]
    for col in columns:
        result[col] = result[col].interpolate(method="linear", limit=limit, limit_area="inside")
    return result
