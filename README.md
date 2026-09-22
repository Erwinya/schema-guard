# schema-guard

Validate JSON documents against a **small JSON Schema subset** (`type`, `required`, `properties`, `items`, `enum`) with no third-party dependencies.

## Status

CLI scaffolding and JSON loading are in place. Schema validation rules will land in a follow-up commit.

## Run

```powershell
python src\schema_guard.py --schema samples\ncr.schema.json --data samples\ncr.valid.json
```

## Requirements

- Python 3.10+
- Standard library only

## License

MIT
