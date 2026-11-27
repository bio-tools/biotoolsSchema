# bio.tools JSON Schema

[`biotoolsj.json`](biotoolsj.json) is the development schema for tool metadata. It uses Draft 2020-12 and stores shared rules such as version labels and input/output definitions under `$defs`. All references resolve within the file. [JSON Schema reference](https://json-schema.org/draft/2020-12/json-schema-core#section-8.2).

The schema root validates an array of tools. Use the `#/$defs/tool` fragment for a single tool. Every tool requires `name`, `description`, and `homepage`. Repeatable fields such as `version`, `topic`, and `publication` use arrays, including when they have only one entry.

- [Minimal single tool](examples/minimal.json)
- [Collection with an annotated tool](examples/collection.json)

## Tooling

From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python jsonschema/validate.py jsonschema/examples/{minimal,collection}.json
```

The CLI accepts single tools and arrays. It reports errors by file and JSON path. Run `python jsonschema/serve.py` and open the printed local URL to edit, validate, and download a tool record in the browser.

VS Code offers completions for `*.tool.json` and `*.tools.json`. GitHub Actions checks the schema, runs the tests, and builds release artifacts. See the [contributor guide](../CONTRIBUTING.md) for build and SPDX refresh commands.

To list ELIXIR communities directly from the schema:

```sh
jq -r '."$defs".tool.properties.elixirCommunity.items.enum[]' jsonschema/biotoolsj.json
```

## Migrating from the Draft 4 schema

Use a Draft 2020-12 validator and update references to `#/definitions/tool` to `#/$defs/tool`. The JSON property names and array structure carry over. The schema now checks URL schemes and identifier patterns, requires `term` or `uri` for EDAM concepts, and requires an identifier for each publication. A credit can be identified by name, email, or URL. Both bare ORCID iDs and ORCID URLs are accepted.
