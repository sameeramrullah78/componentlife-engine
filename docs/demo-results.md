# Demo Results

The repository includes three synthetic scenarios that exercise different parts of the ComponentLife v0.1 logic.

| Demo | Expected result | Purpose |
|---|---|---|
| Healthy alternator | `SUITABLE_PROFILE` | Demonstrates high-confidence reference alignment |
| Degraded alternator | `FURTHER_TESTING_REQUIRED` | Demonstrates multimodal anomalies and low dimension scores |
| Uncertain alternator | `INCONCLUSIVE` | Demonstrates that missing evidence reduces confidence rather than forcing a decision |

Generated Markdown and JSON examples are stored in `examples/sample_reports/`.

These outputs are software demonstrations using synthetic data and synthetic reference values. They are not automotive validation evidence.
