from __future__ import annotations


def detect_anomalies(comparison: dict[str, dict[str, float]], warning_z: float = 2.0, critical_z: float = 3.0) -> list[dict[str, object]]:
    anomalies: list[dict[str, object]] = []
    for metric, info in comparison.items():
        z = abs(float(info["z_score"]))
        if z >= critical_z:
            severity = "critical"
        elif z >= warning_z:
            severity = "warning"
        else:
            continue
        anomalies.append({"metric": metric, "value": float(info["value"]), "z_score": float(info["z_score"]), "severity": severity})
    anomalies.sort(key=lambda item: abs(float(item["z_score"])), reverse=True)
    return anomalies
