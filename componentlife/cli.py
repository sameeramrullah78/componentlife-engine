from __future__ import annotations
import argparse
from componentlife.pipeline import assess_component
from componentlife.reporting.report_generator import to_markdown, save_markdown, save_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a ComponentLife v0.1 demo alternator assessment.")
    parser.add_argument("test_csv", help="Path to alternator test CSV")
    parser.add_argument("--reference", required=True, help="Path to demo reference profile CSV")
    parser.add_argument("--markdown", help="Optional Markdown report output")
    parser.add_argument("--json", dest="json_path", help="Optional JSON report output")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = assess_component(args.test_csv, args.reference)
    print(to_markdown(result))
    if args.markdown:
        save_markdown(result, args.markdown)
    if args.json_path:
        save_json(result, args.json_path)


if __name__ == "__main__":
    main()
