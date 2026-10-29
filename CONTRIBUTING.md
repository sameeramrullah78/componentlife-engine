# Contributing

ComponentLife Engine is currently a controlled proof-of-concept repository.

## Development workflow

1. Create a branch from `main`.
2. Add or update tests for behavioural changes.
3. Run `pytest`.
4. Do not commit real customer or proprietary production data.
5. Submit a pull request describing the problem, proposed change, tests performed, and impact on analytical behaviour.

## Coding principles

- Keep condition and confidence separate.
- Prefer explainable engineering features over opaque scoring.
- Keep thresholds in reference/configuration data rather than hiding them in UI code.
- Treat unsupported evidence as `INCONCLUSIVE`.
- Preserve traceability from input data to final assessment.
