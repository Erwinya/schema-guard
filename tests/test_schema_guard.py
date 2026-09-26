import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import schema_guard  # noqa: E402


class ValidateTests(unittest.TestCase):
    def test_valid_sample(self) -> None:
        schema = schema_guard.load_json(ROOT / "samples" / "ncr.schema.json")
        data = schema_guard.load_json(ROOT / "samples" / "ncr.valid.json")
        schema_guard.validate(data, schema)

    def test_invalid_enum(self) -> None:
        schema = schema_guard.load_json(ROOT / "samples" / "ncr.schema.json")
        data = schema_guard.load_json(ROOT / "samples" / "ncr.invalid.json")
        with self.assertRaises(schema_guard.SchemaError) as ctx:
            schema_guard.validate(data, schema)
        self.assertIn("enum", str(ctx.exception))

    def test_missing_required(self) -> None:
        schema = {"type": "object", "required": ["title"], "properties": {"title": {"type": "string"}}}
        with self.assertRaisesRegex(schema_guard.SchemaError, "missing required"):
            schema_guard.validate({}, schema)

    def test_cli_valid(self) -> None:
        code = schema_guard.main(
            [
                "--schema",
                str(ROOT / "samples" / "ncr.schema.json"),
                "--data",
                str(ROOT / "samples" / "ncr.valid.json"),
            ]
        )
        self.assertEqual(code, 0)

    def test_cli_invalid(self) -> None:
        code = schema_guard.main(
            [
                "--schema",
                str(ROOT / "samples" / "ncr.schema.json"),
                "--data",
                str(ROOT / "samples" / "ncr.invalid.json"),
            ]
        )
        self.assertEqual(code, 1)

    def test_bad_json_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.json"
            bad.write_text("{not json", encoding="utf-8")
            with self.assertRaises(ValueError):
                schema_guard.load_json(bad)


if __name__ == "__main__":
    unittest.main()
