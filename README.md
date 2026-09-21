# schema-guard

Validate JSON documents against a **small JSON Schema subset** (`type`, `required`, `properties`, `items`, `enum`) with no third-party dependencies.

## Status

Project scaffolding is in place. Validator CLI and sample schemas will land in follow-up commits.

## Planned run

```powershell
python src\schema_guard.py --schema samples\ncr.schema.json --data samples\ncr.valid.json
```

## Requirements

- Python 3.10+
- Standard library only

## License

MIT
