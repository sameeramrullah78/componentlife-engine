# Methodology

## Technical principle

The prototype treats condition assessment as a sequence of explainable steps:

1. obtain controlled measurements;
2. check whether evidence is sufficiently complete;
3. derive engineering features;
4. compare the component with a relevant reference population;
5. identify material deviations;
6. build a multidimensional degradation fingerprint;
7. quantify confidence;
8. return a condition category.

## Why condition and confidence are separate

A model can produce an apparently normal result from weak evidence. ComponentLife therefore does not treat "looks normal" and "high-confidence normal" as equivalent.

The prototype can return `INCONCLUSIVE` when data are incomplete, repeatability is poor, reference coverage is weak, or diagnostic dimensions conflict strongly.

## Why no remaining-mileage prediction is included

Remaining useful life requires longitudinal evidence connecting pre-installation condition with subsequent operating outcomes. ComponentLife v0.1 does not contain that evidence and therefore does not claim a remaining mileage estimate.

## Demonstration scoring

The included score mapping is intentionally simple: a feature close to its reference mean receives a high score; larger standardized deviation produces a lower score. Production scoring should be developed from experimentally validated component-family datasets.
