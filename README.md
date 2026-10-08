# schema-guard

Validate JSON documents against a **small JSON Schema subset** (`type`, `required`, `properties`, `items`, `enum`) with no third-party dependencies.

## Status

Complete: validation CLI, packaging, unit tests (including array/number edge cases), and CI.

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

## Exit codes

- `0` — VALID / success
- `1` — INVALID document
- `2` — missing file / bad JSON / usage error

In PowerShell:

```powershell
python src\schema_guard.py --schema samples\ncr.schema.json --data samples\ncr.valid.json
if ($LASTEXITCODE -ne 0) { Write-Host "schema-guard failed with exit $LASTEXITCODE" }
```

## License

MIT
