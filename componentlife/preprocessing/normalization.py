from __future__ import annotations


def z_score(value: float, mean: float, std: float) -> float:
    if std <= 0:
        return 0.0
    return (value - mean) / std


def reference_score(value: float, mean: float, std: float) -> float:
    """Convert absolute reference deviation into a 0-100 demonstration score."""
    deviation = abs(z_score(value, mean, std))
    return max(0.0, min(100.0, 100.0 - 20.0 * deviation))
