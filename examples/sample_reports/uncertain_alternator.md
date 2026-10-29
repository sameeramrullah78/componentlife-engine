# ComponentLife Condition Assessment

> Proof-of-concept output using synthetic / illustrative reference data.

**Source file:** `/mnt/data/componentlife-engine/data/demo_tests/uncertain_alternator.csv`

**Condition category:** `INCONCLUSIVE`

**Assessment confidence:** 52.2% (LOW)

**Interpretation:** Evidence quality or reference coverage is insufficient for a reliable demo classification.

## Degradation Fingerprint

| Dimension | Score / 100 |
|---|---:|
| Electrical Output | 48.8 |
| Electrical Stability | 51.3 |
| Ripple Behaviour | 0.0 |
| Mechanical Condition | 0.0 |
| Thermal Behaviour | 86.3 |
| Repeatability | 49.5 |

## Confidence Factors

| Factor | Score |
|---|---:|
| Data quality | 48.2% |
| Repeatability | 49.5% |
| Reference coverage | 74.5% |
| Signal agreement | 33.6% |

## Detected Anomalies

| Metric | Severity | z-score | Observed value |
|---|---|---:|---:|
| mean_current | critical | -6.10 | 48.695 |
| current_std | critical | -3.15 | 12.113 |

## Important limitation

This result is a software demonstration. It is not a safety certification, remaining-useful-life prediction, or guarantee of component serviceability.
