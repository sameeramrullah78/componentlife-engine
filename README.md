# ComponentLife Engine

**ComponentLife Engine v0.1** is a proof of concept for the first technical innovation in the ComponentLife product roadmap:

> **Controlled alternator sensor data → feature extraction → reference comparison → degradation fingerprint → confidence assessment → explainable condition result.**

The repository demonstrates how ComponentLife can turn electrical, mechanical, and thermal measurements from a reclaimed automotive alternator into a structured condition-intelligence output.

## What this version demonstrates

Version 0.1 implements:

- CSV ingestion for controlled alternator test data
- data-quality validation
- electrical feature extraction
- vibration feature extraction
- thermal feature extraction
- comparison with a demo reference population
- anomaly detection
- a six-dimension degradation fingerprint
- confidence scoring
- condition classification
- Markdown and JSON reporting
- a Streamlit demonstration dashboard
- synthetic demo datasets
- automated tests and GitHub Actions CI

## What this version does not claim

This repository is a **technical demonstrator**, not a certified automotive diagnostic product. It does **not** predict exact remaining mileage or remaining useful life, certify that a reclaimed component is safe or suitable for installation, replace professional inspection/grading/testing/traceability, contain commercially validated degradation thresholds, contain real customer data, or expose future production models and proprietary field datasets.

All included reference values and datasets are synthetic / illustrative and exist only to demonstrate the software architecture.

## Why this is the first ComponentLife build

The v0.1 engine answers five practical questions:

1. What was measured?
2. How does the component compare with a reference population?
3. Which diagnostic dimensions appear abnormal?
4. How confident is the assessment?
5. What condition category should be returned?

That foundation can later support adaptive test selection, physical test-bench integration, physics-informed machine learning, second-life outcome learning, ComponentLife Passport services, and enterprise APIs.

## Architecture

```text
Controlled Test Data
        |
        v
CSV Ingestion + Validation
        |
        v
Signal / Data Pre-processing
        |
        v
Feature Extraction
  |        |        |
Electrical Mechanical Thermal
        |
        v
Reference Population Comparison
        |
        v
Anomaly Detection
        |
        v
Degradation Fingerprint
        |
        v
Confidence Engine
        |
        v
Condition Classification
        |
        v
Markdown / JSON Report + Dashboard
```

See [`docs/architecture.md`](docs/architecture.md) for the detailed design.

## Repository structure

```text
componentlife-engine/
├── README.md
├── LICENSE
├── NOTICE.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── .github/workflows/tests.yml
├── componentlife/
│   ├── pipeline.py
│   ├── cli.py
│   ├── ingestion/
│   ├── preprocessing/
│   ├── features/
│   ├── reference/
│   ├── analytics/
│   ├── assessment/
│   └── reporting/
├── dashboard/app.py
├── data/
│   ├── demo_reference/
│   └── demo_tests/
├── docs/
├── examples/
└── tests/
```

## Quick start

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows**
```powershell
.venv\Scripts\activate
```

### 2. Install

```bash
pip install -e ".[dev,dashboard]"
```

### 3. Run tests

```bash
pytest
```

### 4. Run the command-line demo

```bash
componentlife-assess data/demo_tests/healthy_alternator.csv \
  --reference data/demo_reference/reference_profiles.csv
```

```bash
componentlife-assess data/demo_tests/degraded_alternator.csv \
  --reference data/demo_reference/reference_profiles.csv
```

```bash
componentlife-assess data/demo_tests/uncertain_alternator.csv \
  --reference data/demo_reference/reference_profiles.csv
```

Write reports to disk:

```bash
componentlife-assess data/demo_tests/degraded_alternator.csv \
  --reference data/demo_reference/reference_profiles.csv \
  --markdown report.md \
  --json report.json
```

### 5. Run the dashboard

```bash
streamlit run dashboard/app.py
```

## Data format

The v0.1 CSV schema is:

```csv
timestamp,rpm,voltage,current,ripple_mv,vibration_rms,temp_c
0,1800,14.18,40.1,92,0.51,24.0
1,1800,14.20,40.0,91,0.52,24.1
```

Required columns:

| Column | Description |
|---|---|
| `timestamp` | Seconds from start of test |
| `rpm` | Alternator rotational speed |
| `voltage` | Output voltage |
| `current` | Output current |
| `ripple_mv` | AC ripple in millivolts |
| `vibration_rms` | Vibration RMS in mm/s |
| `temp_c` | Measured component temperature in °C |

See [`docs/data-model.md`](docs/data-model.md).

## Degradation fingerprint

The engine produces six explainable dimensions:

1. Electrical output
2. Electrical stability
3. Ripple behaviour
4. Mechanical condition
5. Thermal behaviour
6. Repeatability

Each dimension is scored from 0–100 relative to the supplied reference profile. The score is not intended to be a certified health percentage; it is a normalized comparison indicator for the prototype.

## Confidence engine

The confidence score combines data completeness, repeatability, reference coverage, and agreement between diagnostic dimensions. Confidence is deliberately separate from condition, allowing the classifier to return **Inconclusive** instead of forcing a definitive result when evidence is weak.

## Condition categories

- `SUITABLE_PROFILE`
- `REVIEW`
- `FURTHER_TESTING_REQUIRED`
- `INCONCLUSIVE`

These categories are demonstration outputs only.

## Included demo outcomes

The current synthetic demo set is regression-tested to produce:

- `healthy_alternator.csv` → **SUITABLE_PROFILE**
- `degraded_alternator.csv` → **FURTHER_TESTING_REQUIRED**
- `uncertain_alternator.csv` → **INCONCLUSIVE**

See [`docs/demo-results.md`](docs/demo-results.md) and `examples/sample_reports/`.

## IP boundary

Suitable for a public technical demonstration:

- architecture
- CSV schema
- synthetic datasets
- baseline feature extraction
- demonstration scoring logic
- dashboard
- API-ready data structures

Keep private for production development:

- experimentally validated degradation thresholds
- real component reference populations
- customer data
- proprietary feature combinations
- production model weights
- adaptive-test decision rules
- condition-to-outcome datasets
- trained production AI models

See [`NOTICE.md`](NOTICE.md).

## Roadmap

- **v0.1:** Degradation Fingerprint + Confidence Engine
- **v0.2:** Adaptive Test Recommendation Engine
- **v0.3:** Physical Sensor / Test-Bench Integration
- **v0.4:** Physics-Informed Machine Learning
- **v0.5:** ComponentLife Passport + Outcome Tracking
- **v1.0:** Commercial Alternator Condition-Intelligence Platform

See [`docs/roadmap.md`](docs/roadmap.md).

## Security and responsible use

Do not upload customer, vehicle-owner, or commercially confidential information to a public repository. See [`SECURITY.md`](SECURITY.md).

## License

This demonstrator is published under a **proprietary evaluation license**. It is not an open-source licence. See [`LICENSE`](LICENSE).

Copyright © 2026 ComponentLife. All rights reserved.
