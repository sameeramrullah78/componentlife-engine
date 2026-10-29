from __future__ import annotations
import numpy as np
import pandas as pd


def vibration_features(df: pd.DataFrame) -> dict[str, float]:
    mask = df["vibration_rms"].notna()
    vibration = df.loc[mask, "vibration_rms"].to_numpy(dtype=float)
    if vibration.size == 0:
        return {"vibration_mean": float("nan"), "vibration_peak": float("nan"), "vibration_std": float("nan"), "dominant_frequency_hz": float("nan")}

    dominant_frequency_hz = 0.0
    timestamps = df.loc[mask, "timestamp"].to_numpy(dtype=float)
    if vibration.size >= 8 and timestamps.size == vibration.size and timestamps.size > 1:
        dt = float(np.median(np.diff(timestamps)))
        if dt > 0:
            centered = vibration - np.mean(vibration)
            spectrum = np.abs(np.fft.rfft(centered))
            freqs = np.fft.rfftfreq(centered.size, d=dt)
            if spectrum.size > 1:
                idx = int(np.argmax(spectrum[1:]) + 1)
                dominant_frequency_hz = float(freqs[idx])

    return {
        "vibration_mean": float(np.mean(vibration)),
        "vibration_peak": float(np.max(vibration)),
        "vibration_std": float(np.std(vibration)),
        "dominant_frequency_hz": dominant_frequency_hz,
    }
