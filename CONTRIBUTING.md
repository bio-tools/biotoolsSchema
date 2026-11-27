# Contributing to biotoolsSchema

Use Python 3.12 or later and run `python -m pip install -e .` from the repository root in a virtual environment. Edit the canonical JSON Schema for fields, validation rules, and manually maintained vocabularies. [Schema](jsonschema/biotoolsj.json) · [Local validation and editor](jsonschema/README.md#tooling)

## Tests and releases

- Run `python -m unittest discover -s tests` to test validation, the form server, SPDX refresh, and build reproducibility.
- Run `build-schema --version 4.0.0` to write `dist/biotools-4.0.0.schema.json` and `dist/biotools_vocab.py`.
- GitHub Actions validates examples, runs tests, and uploads artifacts on pushes and pull requests. Pushing a version tag such as `v4.0.0` also creates a draft release.

## Licenses

Run `fetch-spdx` to refresh the committed SPDX snapshot and the schema's license list. Use `--ref <tag>` for a specific SPDX release or `--check` to check for drift without writing. Monthly automation proposes updates by pull request when repository permissions allow it. [SPDX snapshot](src/enums/license.json) · [Curated bio.tools values](src/enums/license_curated_extra.json)

Previously accepted license IDs stay valid after SPDX deprecates them. The Python vocabulary includes additional deprecated SPDX IDs so older registry data can still be represented.
