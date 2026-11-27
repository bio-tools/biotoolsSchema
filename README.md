# biotoolsSchema

biotoolsSchema describes software for bio.tools, the ELIXIR Tools and Data Services Registry. It uses the EDAM ontology to describe operations, inputs, and outputs. Together, the schema and EDAM underpin the Tool Information Standards. [bio.tools](https://bio.tools) · [EDAM](https://github.com/edamontology/edamontology) · [Tool Information Standards](https://github.com/bio-tools/Tool-Information-Standards)

## Current JSON Schema

The canonical schema uses JSON Schema Draft 2020-12. Every tool requires `name`, `description`, and `homepage`. [Batch schema](jsonschema/biotoolsj.json) · [Single-tool schema](jsonschema/biotools-tool.json)

- Validate a file or batch with the CLI, edit a record in the local browser form, or get autocomplete in VS Code. [Setup and examples](jsonschema/README.md#tooling)
- Build versioned JSON Schema and Python vocabulary artifacts. GitHub Actions runs tests, builds artifacts, and prepares draft releases for version tags. [Contributor guide](CONTRIBUTING.md)
- The vocabulary includes `Preprint` and an expanded SPDX license list. A monthly workflow proposes updates and retains previously accepted license IDs when SPDX deprecates them. [License maintenance](CONTRIBUTING.md#licenses)

## Legacy releases

The XML 3.3.0 release and older versions are available with their schemas, examples, and documentation. Earlier JSON consumers can follow the Draft 4 migration guide. [Stable XML](stable/README.md) · [Version archive](versions/) · [Draft 4 migration](jsonschema/README.md#migrating-from-the-draft-4-schema) · [Changelog](CHANGELOG.md)
