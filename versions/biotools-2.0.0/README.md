# biotools-2.0.0

See https://github.com/bio-tools/biotoolsschema/.

biotoolsSchema is a formalised XML schema (XSD) which defines a description model for bioinformatics software.  It can be used to describe bioinformatics tools - application software with well-defined data processing functions (inputs, outputs and operations).   This includes simple tools with one or a few closely related functions, and complex, multimodal tools with many functions, tools available available for immediate use as online services, or in a form which which you can download, install, configure and run yourself.  

biotoolsSchema defines 50 important scientific, technical and administrative attributes.  It concentrates upon the salient common features, with a minimal core of 7 attributes, mandating the necessary and sufficient information to support cataloguing and discovery of software.

The ELIXIR Tools & Data Services Registry (https://bio.tools/) is undergoing a phased migration to biotoolSchema 2.0 beginning in Nov 2016.

File | Description
---- | -----------
biotools-2.0.0.xsd | XML schema
docs/biotools-2.0.0.html | Full schema documentation
example_files/biotools-2.0.0.xml | Sample XML format file, including all non-mandatory elements and including 2 elements if marked as repeatable in the schema.
example_files/biotools-2.0.0_mandatoryFieldsOnly.xml | Sample XML format file, including only mandatory elements and including only 1 element if marked as repeatable in the schema.





