from pathlib import Path
from componentlife.pipeline import assess_component
from componentlife.reporting.report_generator import to_markdown

ROOT = Path(__file__).resolve().parents[1]
reference = ROOT / "data/demo_reference/reference_profiles.csv"

for name in ["healthy_alternator", "degraded_alternator", "uncertain_alternator"]:
    path = ROOT / f"data/demo_tests/{name}.csv"
    result = assess_component(path, reference)
    print("=" * 80)
    print(name)
    print(to_markdown(result))
