# What is biotoolsSchema?
**biotoolsSchema** is a formalised XML schema (XSD) which defines a description model for bioinformatics software.  It can be used to describe bioinformatics tools - application software with well-defined data processing functions (inputs, outputs and operations).   This includes simple tools with one or a few closely related functions, and complex, multimodal tools with many functions, tools available available for immediate use as online services, or in a form which which you can download, install, configure and run yourself.  

biotoolsSchema defines 50 important scientific, technical and administrative attributes.  It concentrates upon the salient common features, with a minimal core of 7 attributes, mandating the necessary and sufficient information to support cataloguing and discovery of software.  It is used by the [Tools & Data Services Registry](https://bio.tools).

Comprehensive documentation is available:
* http://biotoolsschemadocs.readthedocs.io/en/latest/
* https://bio.tools/schema  (version 1.4, currently in production in bio.tools)
* https://github.com/bio-tools/biotoolsSchema/blob/master/versions/biotools-2.0.0/docs/biotools-2.0.0.html (version 2.0.0, latest stable version)


# Information requirements
https://bio.tools specifies an information requirement for "standard" and "beta" (less well annotated) entries, as indicated in the respective columns.  Attributes defined as mandatory in the latest stable version [biotools-2.0.0](https://github.com/bio-tools/biotoolsSchema/blob/master/versions/biotools-2.0.0/) are those in the "beta" column.

Attribute | Description | Format | beta | standard | element
--------- | ----------- | ------ | -----| -------- | -------
name (1 only) | Canonical resource name | Text | y | y | `<name>`
toolID (1 only) | Unique tool ID | Text | y | y | `<toolID>`
homepage (1 only) | Resource homepage | URL | y | y | `<homepage>`
description (1 only) | Short textual description of the resource | Text | y | y | `<description>`
tool type (1 or more) | Type of tool.  A tool may have more than one type reflecting its different facets. | enum (see below) | y | y | `<toolType>`
topic (1 or more) | General scientific domain(s) the resource serves, e.g. "Proteomics" | Term and / or URI of [EDAM Topic](http://edamontology.org/topic_0004) concept(s)* | y | y | `<topic>`
function (1 or more) | The basic resource function(s), e.g. "Multiple sequence alignment" | Term and / or URI of [EDAM Operation](http://edamontology.org/operation_0004) concept(s) | y | y | `<function><operation>`
input data (0 or more) | Type(s) of data: primary inputs (if any), e.g. "Protein sequences" | Term and / or URI of [EDAM Data](http://edamontology.org/data_0006) concept(s) | - | y |  `<function><input><data>`
output data (0 or more) | Type(s) of data: primary outputs (if any), e.g. "Protein sequence alignment" | Term and / or URI of [EDAM Data](http://edamontology.org/data_0006) concept(s) | - | y | `<function><output><data>`
contact (1 or more) | Primary contact, e.g. a person, helpdesk or mailing list | Email address and / or URL of contact** | - | y | `<contact>`
publication (0 or more) | Publications about the software | PMID, PMCID or DOI | - | y | `<publication>`

*EDAM is a simple ontology of well established, familiar concepts that are prevalent within bioinformatics, including types of data and data identifiers, data formats, operations and topics. EDAM provides a set of terms with synonyms and definitions - organised into an intuitive hierarchy for convenient use.  You can read find [EDAM on GitHub](https://github.com/edamontology/edamontology).

**one of contactEmail or contactURL must be specified

  
## Tool types 
Valid values of toolType in in the candidate stable schema ([biotools-2.0.0](https://github.com/bio-tools/biotoolsSchema/blob/master/versions/biotools-2.0.0/).

type | Description 
---- | ----------- 
Command-line tool | A tool with a text-based (command-line) interface.
Database portal | A Web application, suite or workbench providing a portal to a biological database.
Desktop application | A tool with a graphical user interface that runs on your desktop environment, e.g. on a PC or mobile device.
Library | A collection of components that are used to construct other tools.  bio.tools scope includes component libraries performing high-level bioinformatics functions but excludes lower-level programming libraries.
Ontology | A collection of information about concepts, including terms, synonyms, descriptions etc. | 2.0.0
Plug-in | A software component encapsulating a set of related functions, which are not standalone, i.e. depend upon other software for its use, e.g. a Javascript widget, or a plug-in, extension add-on etc. that extends the function of some existing tool.
Script | A tool written for some run-time environment (e.g. other applications or an OS shell) that automates the execution of tasks. Often a small program written in a general-purpose languages (e.g. Perl, Python) or some domain-specific languages (e.g. sed).
SPARQL endpoint | A service that provides queries over an RDF knowledge base via the SPARQL query language and protocol, and returns results via HTTP.
Suite | A collection of tools which are bundled together into a convenient toolkit.  Such tools typically share related functionality, a common user interface and can exchange data conveniently.  This includes collections of stand-alone command-line tools, or Web applications within a common portal.
Web application | A tool with a graphical user interface that runs in your Web browser.
Web API | An application programming interface (API) consisting of endpoints to a request-response message system accessible via HTTP.  Includes everything from simple data-access URLs to RESTful APIs.
Web service | An API described in a machine readable form (typically WSDL) providing programmatic access via SOAP over HTTP.
Workbench | An application or suite with a graphical user interface, providing an integrated environment for data analysis which includes or may be extended with any number of functions or tools.  Includes workflow systems, platforms, frameworks etc.
Workflow | A set of tools which have been composed together into a pipeline of some sort.  Such tools are (typically) standalone, but are composed for convenience, for instance for batch execution via some workflow engine or script.




