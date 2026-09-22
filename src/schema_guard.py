#!/usr/bin/env python3
"""Load JSON schema and data documents (validation logic lands next)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    if not path.is_file():
        raise FileNotFoundError(f"file not found: {path}")
    text = path.read_text(encoding="utf-8-sig")
    try:
        return json.loads(text)
    except json.JSONDecodeError as ex:
        raise ValueError(f"invalid JSON in {path}: {ex}") from ex


def summarize(label: str, value: Any) -> str:
    if isinstance(value, dict):
        return f"{label}: object with {len(value)} key(s)"
    if isinstance(value, list):
        return f"{label}: array with {len(value)} item(s)"
    return f"{label}: {type(value).__name__}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Load JSON schema and data files")
    parser.add_argument("--schema", required=True, help="Path to schema JSON")
    parser.add_argument("--data", required=True, help="Path to data JSON")
    args = parser.parse_args(argv)

    try:
        schema = load_json(Path(args.schema))
        data = load_json(Path(args.data))
    except (FileNotFoundError, ValueError) as ex:
        print(f"error: {ex}", file=sys.stderr)
        return 2

    print(summarize("schema", schema))
    print(summarize("data", data))
    print("loaded OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
