# What is biotoolsSchema?

**biotoolsSchema** is a JSON Schema for describing bioinformatics software, including its operations, inputs and outputs. It covers simple tools, software with several functions, online services and locally installed applications.

biotoolsSchema defines over 50 important scientific, technical and administrative attributes that support cataloguing, discovery, use and interoperability of software.  It concentrates upon the salient common features, with a minimal core of 3 attributes only (name, short description and homepage), to provide maximum flexibility for applications.  To enable concise information, standard identifiers are used where possible, including [EDAM ontology](http://github.com/edamontology/edamontology) concept IDs for specialised scientific aspects.  biotoolsSchema defines 18 controlled vocabularies for technical tool aspects.  Verbose information is referred to by URL.

biotoolsSchema is used by [bio.tools](https://bio.tools), the ELIXIR Tools & Data Services Registry.

## Schema and validation

Edit [`jsonschema/biotoolsj.json`](jsonschema/biotoolsj.json) to change the development schema. It uses [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/) and keeps reusable definitions in the same file. The [JSON Schema guide](jsonschema/README.md#tooling) covers command-line validation, the browser form, and CI.

## Published XML releases

The [stable 3.3.0 XML release](stable/), its [technical documentation](https://bio-tools.github.io/biotoolsSchema/), and [older releases](versions/) are available for XML consumers. The [general documentation](https://biotoolsschema.readthedocs.io/en/latest/) describes the metadata model and controlled vocabularies.

## Information standard

biotoolsSchema and the [EDAM ontology](https://github.com/edamontology/edamontology) provide the foundation for the [Tool Information Standards](https://github.com/bio-tools/Tool-Information-Standards).
