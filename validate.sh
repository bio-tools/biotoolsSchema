#!/usr/bin/env bash
for biotools_raw_file in "$@"; do
	jq 'del(.owner, .editPermission, .lastUpdate, .community, .validated, .additionDate, .publication[]?.metadata, .homepage_status, .confidence_flag, .elixir_badge)' $biotools_raw_file >/tmp/$(basename $biotools_raw_file)
	echo "Validating $(basename $biotools_raw_file)"
	jsonschema -i /tmp/$(basename $biotools_raw_file) "$(dirname "${BASH_SOURCE[0]}")/biotools.schema.json"
done
