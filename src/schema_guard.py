#!/usr/bin/env python3
"""Validate JSON payloads against a small JSON Schema subset (stdlib only)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


class SchemaError(Exception):
    def __init__(self, path: str, message: str) -> None:
        super().__init__(f"{path}: {message}")
        self.path = path
        self.message = message


def load_json(path: Path) -> Any:
    if not path.is_file():
        raise FileNotFoundError(f"file not found: {path}")
    text = path.read_text(encoding="utf-8-sig")
    try:
        return json.loads(text)
    except json.JSONDecodeError as ex:
        raise ValueError(f"invalid JSON in {path}: {ex}") from ex


def _type_name(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int) and not isinstance(value, bool):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def validate(instance: Any, schema: dict[str, Any], path: str = "$") -> None:
    expected = schema.get("type")
    if expected is not None:
        actual = _type_name(instance)
        allowed = expected if isinstance(expected, list) else [expected]
        ok = actual in allowed or (actual == "integer" and "number" in allowed)
        if not ok:
            raise SchemaError(path, f"expected type {allowed}, got {actual}")

    if "enum" in schema and instance not in schema["enum"]:
        raise SchemaError(path, f"value {instance!r} not in enum {schema['enum']}")

    if schema.get("type") == "object" or "properties" in schema or "required" in schema:
        if not isinstance(instance, dict):
            raise SchemaError(path, "expected object")
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                raise SchemaError(path, f"missing required property '{key}'")
        props = schema.get("properties", {})
        for key, subschema in props.items():
            if key in instance:
                validate(instance[key], subschema, f"{path}.{key}")

    if schema.get("type") == "array" or "items" in schema:
        if not isinstance(instance, list):
            raise SchemaError(path, "expected array")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for i, item in enumerate(instance):
                validate(item, item_schema, f"{path}[{i}]")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate JSON with a schema subset")
    parser.add_argument("--schema", required=True, help="Path to schema JSON")
    parser.add_argument("--data", required=True, help="Path to data JSON")
    args = parser.parse_args(argv)

    try:
        schema = load_json(Path(args.schema))
        data = load_json(Path(args.data))
    except (FileNotFoundError, ValueError) as ex:
        print(f"error: {ex}", file=sys.stderr)
        return 2

    try:
        validate(data, schema)
    except SchemaError as ex:
        print(f"INVALID: {ex}", file=sys.stderr)
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
