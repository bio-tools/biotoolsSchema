# What is biotoolsXSD?
**biotoolsXSD** is an XML schema (XSD) used by the ELIXIR Tools & Data Services Registry (https://elixir-registry.cbs.dtu.dk/#/).  biotoolsXSD provides a resource description model for bioinformatics, suitable for the description of databases and tools, provided under a variety of interfaces.

# Motivation
Bioinformaticians routinely use a large and diverse set of tools and data, and demand powerful and convenient means to organise, find, understand, compare, select, use and connect the available resources. These tasks rely on consistent, machine-understandable resource descriptions. The urgent need - filled by biotoolsXSD - is for an information model that puts the description of a broad range of resources  on a consistent syntactic basis.

# Applications 
biotoolsXSD is applicable to diverse bioinformatics software and interface types, including:
* Databases
* Tools	
* Widgets	
* Frameworks	
* Libraries	
* Suites	
* Virtual machines	
* Command line interfaces
* Desktop GUIs
* SOAP Web Services
* REST APIs
* Web User Interfaces
* Functional URLs

# People

## Developers
* Jon Ison (CBS-DTU, DK) *- lead developer*
* Kristoffer Rapacki (CBS-DTU, DK)
* Piotr Chmura (CBS-DTU, DK)
* Emil Rydza (CBS-DTU, DK)
* Matúš Kalaš (University of Bergen, NO)
* Hervé Ménager (Institut Pasteur, FR) 

## Contributors
Thanks to the many people who have contributed - if you're not listed below, please let us know!
* Julie McMurry (EMBL-EBI, UK)
* Helen Parkinson (EMBL-EBI, UK)
* Delegates of the many BioMedBridges and ELIXIR workshops 

# Mandatory attributes
interfaceType | Resource interface type: "Command-line", "Desktop GUI", "SOAP WS", "REST API", "Web UI", "URL", "API", "SQL" or "SPARQL"
name | Canonical resource name
homepage | Resource homepage (URL)
resourceType | Basic resource type: "Dataset", "Database",  "Framework", "Library", "Suite", "Widget", "virtual machine", "Tool", "Tool (query and retrieval)", "Tool (analysis)", "Tool (deposition)", "Tool (visualiser)", "Tool (utility)" or "Other"
description | Short textual description of the resource
topic | General domain the resource serves or other general category for it: EDAM Topic term(s)
function->functionName | Name(s) of the resource function(s): EDAM Operation term(s)
function->input->dataType | Type of input data (if any): EDAM Data term(s)
function->output->dataType | Type of ouput data (if any): EDAM Data term(s)
contact->contactEmail* | Email address of contact
contact->contactURL* | URL of contact

(* one of contactEmail or contactURL must be specified)


# Documentation and website

Full user documentation of biotoolsXSD is available at 

https://elixir-registry.cbs.dtu.dk/#/downloads.

