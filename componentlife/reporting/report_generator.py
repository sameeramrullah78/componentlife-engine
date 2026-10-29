from __future__ import annotations
import json
from pathlib import Path


def to_markdown(result: dict) -> str:
    lines = [
        "# ComponentLife Condition Assessment", "",
        "> Proof-of-concept output using synthetic / illustrative reference data.", "",
        f"**Source file:** `{result['source_file']}`", "",
        f"**Condition category:** `{result['classification']['category']}`", "",
        f"**Assessment confidence:** {result['confidence']['score']:.1f}% ({result['confidence']['label']})", "",
        f"**Interpretation:** {result['classification']['reason']}", "",
        "## Degradation Fingerprint", "", "| Dimension | Score / 100 |", "|---|---:|",
    ]
    for key, value in result["fingerprint"].items():
        lines.append(f"| {key.replace('_', ' ').title()} | {float(value):.1f} |")
    lines += ["", "## Confidence Factors", "", "| Factor | Score |", "|---|---:|",
              f"| Data quality | {result['confidence']['data_quality']:.1f}% |",
              f"| Repeatability | {result['confidence']['repeatability']:.1f}% |",
              f"| Reference coverage | {result['confidence']['reference_coverage']:.1f}% |",
              f"| Signal agreement | {result['confidence']['signal_agreement']:.1f}% |", "", "## Detected Anomalies", ""]
    if result["anomalies"]:
        lines += ["| Metric | Severity | z-score | Observed value |", "|---|---|---:|---:|"]
        for item in result["anomalies"]:
            lines.append(f"| {item['metric']} | {item['severity']} | {float(item['z_score']):.2f} | {float(item['value']):.3f} |")
    else:
        lines.append("No warning-level anomalies were detected against the supplied demo reference profile.")
    lines += ["", "## Important limitation", "", "This result is a software demonstration. It is not a safety certification, remaining-useful-life prediction, or guarantee of component serviceability.", ""]
    return "\n".join(lines)


def save_markdown(result: dict, path: str | Path) -> None:
    Path(path).write_text(to_markdown(result), encoding="utf-8")


def save_json(result: dict, path: str | Path) -> None:
    Path(path).write_text(json.dumps(result, indent=2), encoding="utf-8")
