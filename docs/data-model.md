# Data Model

## Raw test CSV

| Field | Unit | Meaning |
|---|---|---|
| `timestamp` | seconds | Time from start of controlled test |
| `rpm` | RPM | Rotational speed |
| `voltage` | V | Alternator output voltage |
| `current` | A | Alternator output current |
| `ripple_mv` | mV | AC ripple |
| `vibration_rms` | mm/s | Demonstration vibration RMS channel |
| `temp_c` | °C | Measured component temperature |

## Reference profile CSV

| Field | Meaning |
|---|---|
| `metric` | Extracted feature name |
| `mean` | Demo reference population mean |
| `std` | Demo reference population standard deviation |
| `sample_count` | Number of reference samples represented |

The reference profile included in this repository is synthetic and is not a commercial threshold library.

## Assessment JSON

Top-level fields: `engine_version`, `source_file`, `reference_file`, `features`, `comparison`, `anomalies`, `fingerprint`, `confidence`, `classification`, and `disclaimer`.
