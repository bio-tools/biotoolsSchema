# bio.tools JSON Schema

[`biotoolsj.json`](biotoolsj.json) is the canonical Draft 2020-12 schema for an array of tools. Use [`biotools-tool.json`](biotools-tool.json) or the `#/$defs/tool` fragment for a single tool. Each tool requires `name`, `description`, and `homepage`. Repeatable fields such as `version` and `publication` use arrays even for one value.

[Minimal tool](examples/minimal.json) · [Annotated collection](examples/collection.json)

## Tooling

Set up a virtual environment from the repository root.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

- **CLI.** Run `python jsonschema/validate.py path/to/record.json`. Pass multiple files in one call. Errors include the file and JSON path. Use `--check-schema` to check the schema itself.
- **Browser editor.** Run `python jsonschema/serve.py` and open the printed URL. Create a tool record or open an existing valid one, then validate and download the JSON.
- **VS Code.** Use `*.tool.json` for single tools and `*.tools.json` for batches to get field and vocabulary suggestions.

For example, list the ELIXIR communities directly from the schema with `jq`.

```sh
jq -r '."$defs".tool.properties.elixirCommunity.items.enum[]' jsonschema/biotoolsj.json
```

## Migrating from the Draft 4 schema

Use a Draft 2020-12 validator and change `#/definitions/tool` to `#/$defs/tool`. Field names and array structure carry over. The schema checks URL schemes and identifier syntax, requires a term or URI for EDAM concepts, and requires a DOI, PMID, or PMCID for publications. Credits can use a name, email, or URL. Both bare ORCID iDs and ORCID URLs work.

[Legacy XML releases](../stable/README.md) · [Build, CI, and SPDX maintenance](../CONTRIBUTING.md)
