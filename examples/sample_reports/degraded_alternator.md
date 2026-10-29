# ComponentLife Condition Assessment

> Proof-of-concept output using synthetic / illustrative reference data.

**Source file:** `/mnt/data/componentlife-engine/data/demo_tests/degraded_alternator.csv`

**Condition category:** `FURTHER_TESTING_REQUIRED`

**Assessment confidence:** 64.2% (MODERATE)

**Interpretation:** One or more diagnostic dimensions show a substantial deviation from the demo reference population.

## Degradation Fingerprint

| Dimension | Score / 100 |
|---|---:|
| Electrical Output | 84.7 |
| Electrical Stability | 85.4 |
| Ripple Behaviour | 46.1 |
| Mechanical Condition | 15.6 |
| Thermal Behaviour | 42.9 |
| Repeatability | 20.3 |

## Confidence Factors

| Factor | Score |
|---|---:|
| Data quality | 100.0% |
| Repeatability | 20.3% |
| Reference coverage | 79.4% |
| Signal agreement | 46.4% |

## Detected Anomalies

| Metric | Severity | z-score | Observed value |
|---|---|---:|---:|
| vibration_std | critical | 6.30 | 0.385 |
| vibration_peak | critical | 4.64 | 1.687 |
| mean_ripple_mv | critical | 3.35 | 145.284 |
| temp_rise_per_min | critical | 3.07 | 9.882 |
| temp_rise_c | critical | 3.04 | 49.243 |
| vibration_mean | critical | 3.03 | 0.984 |
| max_temp_c | warning | 2.46 | 74.236 |
| ripple_std_mv | warning | 2.04 | 18.180 |

## Important limitation

This result is a software demonstration. It is not a safety certification, remaining-useful-life prediction, or guarantee of component serviceability.
