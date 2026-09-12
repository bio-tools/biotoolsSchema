# Contributing

We welcome contributions to biotoolsSchema.

This repository defines and publishes the XML Schema Definition (XSD), JSON Schema, and controlled vocabulary export used by the bio.tools registry.

Before opening a PR, please read the relevant documentation:

- [What is biotoolsSchema?](https://biotoolsschema.readthedocs.io/en/latest/what_is_biotoolsschema.html)
- [How to contribute to biotoolsSchema](https://biotoolsschema.readthedocs.io/en/latest/what_is_biotoolsschema.html#how-to-contribute-to-biotoolsschema)



## Architecture

The repository has one authorative source for controlled vocabulary values:

```text
src/enums/*.json
        |
        |  build-schema --version version
        v
dist/biotools-<version>.xsd
dist/biotools-<version>.schema.json
dist/biotools_vocab.py
```

Relevant files:

```text
src/enums/*.json
    Single source of truth for controlled vocabularies.
    There is one JSON file per vocabulary.

src/biotools.xsd.tmpl
    Hand-maintained XSD structure. It contains enum placeholders in the form:
    {{ENUM_XSD:<vocabulary-name>}}

src/biotools.schema.tmpl.json
    Hand-maintained JSON Schema structure. It contains enum references in the
    form:
    {"$enumRef": "<vocabulary-name>"}

src/btschema/build.py
    Generates the final XSD, JSON Schema, and Python vocabulary export.
```


Two hand-maintained structural templates (XSD, JSON Schema) each receive enum values injected from the same `src/enums/*.json` files at build time.

The generated XSD and JSON Schema contain static enumerations. Consumers do not resolve vocabulary values dynamically at runtime; the allowed values are baked into each published schema artifact.

### Controlled vocabularies

Controlled vocabularies include licenses, programming languages, operating systems, tool types, maturity, cost, accessibility,  ELIXIR platform/node/community values, identifier types, documentation types, publication types, link types, relation types, and credit types. Most vocabularies are maintained manually in their corresponding `src/enums/<vocabulary>.json` file after review and approval by the bio.tools team.


The license vocabulary is different:

- `src/enums/license.json` is derived from the [SPDX license-list-data.
- `src/enums/license_curated_extra.json` contains non-SPDX values accepted by bio.tools, such as `Proprietary`, `Freeware`, `Not licensed`, and `Other.`
- `fetch-spdx` command fetches and normalizes SPDX license data.
- `.github/workflows/refresh_licenses.yml`runs the SPDX update process every month and opens a PR when the generated license file changes.

Deprecated SPDX license identifiers are handled as such:

- The XSD and JSON Schema exclude deprecated license identifiers from newly valid records.
- `biotools_vocab.py` includes deprecated license identifiers so existing bio.tools records that still use them remain representable in the registry.

## Development setup

Use Python 3.12 or later.

Create and activate a virtual environment, and install the project:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Building artifacts

Build all generated artifacts into `dist/`:

```bash
build-schema
```

By default, this produces

```
dist/biotools-dev.xsd
dist/biotools-dev.schema.json
dist/biotools_vocab.py
```
You can provide a schema version:

```bash
build-schema --version 4.0.0
```
This produces:

```text
dist/biotools-4.0.0.xsd
dist/biotools-4.0.0.schema.json
dist/biotools_vocab.py
```
To write artifacts to another directory:

```bash
build-schema --version 4.0.0 --output-dir /tmp/biotoolsSchema-build
```

To build a single artifact type:

```bash
build-schema --only [(xsd, jsonschema, vocab)]
```

**Do not manually edit generated files. Make changes to the relevant source template or vocabulary file, then regenerate the artifacts.**


## Updating SPDX licenses

```bash
fetch-spdx            # writes src/enums/license.json
fetch-spdx --check    # exit 1 if src/enums/license.json is stale (used by CI)
```

The check command exits with:

```text
0  The committed license vocabulary is current.
1  The committed license vocabulary differs from the fetched SPDX data.
```

## Adding or changing terms

### Before adding a value

First confirm that the proposed value:

- Has a clear and stable meaning.
- Is appropriate for the relevant field.
- Does not duplicate an existing value with different spelling, casing, or punctuation.
- Uses the established identifier convention for that vocabulary.


If you are unsure whether a term belongs in a controlled vocabulary, open an issue before preparing a pull request.

### Editing a manually maintained vocabulary

For terms other than SPDX licenses, edit the corresponding file in:

```text
src/enums/
```

Preserve existing structure. Add the new value to the active `values` list unless it is intentionally being retained only for backwards compatibility.

After editing:

```bash
build-schema
```

Include the resulting changes to generated artifacts in the pull request.

## Testing

```bash
pip install -e ".[dev]"
pytest tests
```

- `test_enum_consistency.py` - asserts the built XSD and built JSON Schema contain the exact same value as `src/enums/` (excluding deprecated licenses). Same for `biotools_vocab.py` but including deprecated licenses to keep existing bio.tools records representable.
- `test_examples_validate_xsd.py` - validates the official bio.tools example XML files against the freshly built XSD.
- `test_examples_validate_jsonschema.py` - validates representative tool records against the freshly built JSON Schema.
- `test_spdx_license_fetch.py` - shape-checks the committed license list.
