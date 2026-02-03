"""Command-line interface for DeobfusFrame."""

from __future__ import annotations

import argparse
import sys

from . import default_engine


def _read_input(path: str | None) -> str:
    if path:
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read()
    return sys.stdin.read()


def main() -> int:
    parser = argparse.ArgumentParser(description="DeobfusFrame deobfuscation CLI")
    parser.add_argument("path", nargs="?", help="Input file path (defaults to stdin)")
    parser.add_argument("--rounds", type=int, default=3, help="Max decode rounds")
    parser.add_argument("--min-score", type=float, default=0.5, help="Min detect score")
    args = parser.parse_args()

    text = _read_input(args.path)
    engine = default_engine()
    report = engine.deobfuscate(text, max_rounds=args.rounds, min_score=args.min_score)

    if report.steps:
        for idx, step in enumerate(report.steps, start=1):
            result = step.result
            print(f"[{idx}] {result.name} score={result.score:.2f}")
        print("---")
    print(report.final)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
