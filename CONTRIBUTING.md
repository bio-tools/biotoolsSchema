# Contributing to biotoolsSchema

Use Python 3.12 or later. In a virtual environment, run `python -m pip install -e .`.

- Edit [`jsonschema/biotoolsj.json`](jsonschema/biotoolsj.json) for fields, rules, and vocabularies.
- Run `python -m unittest discover -s tests` to check the schema and tooling.
- Run `build-schema --version 4.0.0` to generate the versioned JSON Schema and Python vocabulary module in `dist/`. Push a version tag such as `v4.0.0` to have GitHub Actions prepare a draft release.
- Run `fetch-spdx` to refresh the committed SPDX snapshot and the schema's license enum. Use `fetch-spdx --ref <tag>` for a specific SPDX release or `fetch-spdx --check` to check for drift. The scheduled workflow proposes the same changes in a pull request when GitHub Actions has repository permission to create PRs.

New SPDX licenses and curated bio.tools values are valid in the schema. Previously accepted IDs stay valid if SPDX deprecates them. The generated Python vocabulary also includes the other deprecated SPDX IDs so older registry data can still be represented.

See the [tooling guide](jsonschema/README.md#tooling) for the validation CLI and browser editor.
