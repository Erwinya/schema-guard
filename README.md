# schema-guard

Validate JSON documents against a **small JSON Schema subset** (`type`, `required`, `properties`, `items`, `enum`) with no third-party dependencies.

## Status

CLI, validation, packaging (`pyproject.toml`), and unit tests are in place.

## Run

```powershell
python src\schema_guard.py --schema samples\ncr.schema.json --data samples\ncr.valid.json
python src\schema_guard.py --schema samples\ncr.schema.json --data samples\ncr.invalid.json
```

Install locally (optional):

```powershell
pip install -e .
schema-guard --schema samples\ncr.schema.json --data samples\ncr.valid.json
```

## Development

```powershell
pip install -e ".[dev]"
pytest
```

## Requirements

- Python 3.10+
- Standard library only (pytest optional for tests)

## License

MIT
