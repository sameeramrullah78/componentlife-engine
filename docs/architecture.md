# Architecture

## Objective

ComponentLife v0.1 demonstrates a traceable analytical pipeline for a reclaimed alternator tested under controlled conditions.

## Layers

### 1. Test data ingestion
`componentlife.ingestion.csv_loader`

Responsibilities: load CSV data, verify required fields, coerce numeric values, preserve missing evidence rather than silently filling large gaps, and compute data completeness.

### 2. Pre-processing
`componentlife.preprocessing`

The prototype performs only conservative short-gap interpolation. Production development should add sensor calibration, anti-aliasing, physical range validation, synchronized acquisition, and protocol-aware segmentation.

### 3. Feature extraction
`componentlife.features`

Electrical: mean voltage, voltage standard deviation, mean current, current standard deviation, ripple mean, ripple variation.

Mechanical: vibration mean, vibration peak, vibration variation, dominant frequency estimate.

Thermal: start/end temperature, temperature rise, temperature-rise rate, maximum temperature.

### 4. Reference comparison
`componentlife.reference`

Each supported feature is compared with a component-family reference profile. The included reference profile is synthetic and illustrative.

### 5. Anomaly detection
`componentlife.analytics.anomaly`

The prototype flags reference deviations using simple z-score bands. Production development should replace these demonstration rules with validated, component-specific analytical methods.

### 6. Degradation fingerprint
`componentlife.analytics.fingerprint`

The engine produces six dimensions: electrical output, electrical stability, ripple behaviour, mechanical condition, thermal behaviour, and repeatability.

### 7. Confidence assessment
`componentlife.analytics.confidence`

Condition and confidence are kept separate. Confidence combines data quality, repeatability, reference coverage, and agreement across diagnostic dimensions.

### 8. Condition classification
`componentlife.assessment.classifier`

Returns one of `SUITABLE_PROFILE`, `REVIEW`, `FURTHER_TESTING_REQUIRED`, or `INCONCLUSIVE`.

### 9. Reporting
`componentlife.reporting`

Outputs Markdown, JSON, and a Streamlit dashboard.

## Future architecture

```text
Physical Test Bench
    |
Edge Controller
    |
Synchronized Sensor Stream
    |
Feature Pipeline
    |
Component-Family Reference Models
    |
Adaptive Test Selector <----+
    |                        |
Condition Engine             |
    |                        |
ComponentLife Passport       |
    |                        |
Field Outcome ---------------+
```
