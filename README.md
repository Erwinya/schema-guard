# schema-guard

Validate JSON documents against a **small JSON Schema subset** (`type`, `required`, `properties`, `items`, `enum`) with no third-party dependencies.

## Status

CLI, JSON loading, and schema validation are in place. Packaging / tests will land in follow-up commits.

## Run

```powershell
python src\schema_guard.py --schema samples\ncr.schema.json --data samples\ncr.valid.json
python src\schema_guard.py --schema samples\ncr.schema.json --data samples\ncr.invalid.json
```

## Requirements

- Python 3.10+
- Standard library only

## License

MIT
