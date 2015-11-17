# What is biotoolsXSD?
**biotoolsXSD** is a formalised XML schema (XSD) which defines a resource description model for bioinformatics.  It can be used to describe software including databases, tools, services and so on, available under a variety of interfaces. 

biotoolsXSD defines 55 important scientific, technical and administrative attributes.  It concentrates upon the salient common features, with a minimal core of 10 attributes, mandating the necessary and sufficient information to support resource search and discovery.  

biotoolsXSD is used by the [Tools & Data Services Registry](https://bio.tools).

# Motivation
Bioinformaticians routinely use a large and diverse set of tools and data, and demand powerful and convenient means to organise, find, understand, compare, select, use and connect the available resources. These tasks rely on consistent, machine-understandable resource descriptions. The need - filled by biotoolsXSD - is for an information model that puts the description of a broad range of resources  on a consistent syntactic basis.

# Applications 
biotoolsXSD is applicable to diverse bioinformatics software and interface types (see 'Documentation and website' below.)



# Documentation and website

Full user documentation of biotoolsXSD is available at 

https://bio.tools/schema


## Mandatory attributes
Attribute | Description
--------- | -----------
name | Canonical resource name
homepage | Resource homepage (URL)
description | Short textual description of the resource
resourceType | Basic resource type (see below)
interfaceType | Resource interface type (see below)
topic | General domain the resource serves or other general category for it: EDAM** Topic term(s)
functionName | Name(s) of the resource function(s): EDAM Operation term(s)
input->dataType | Type of input data (if any): EDAM Data term(s)
output->dataType | Type of ouput data (if any): EDAM Data term(s)
contactEmail* | Email address of contact
contactURL* | URL of contact

*one of contactEmail or contactURL must be specified

**EDAM is a simple ontology of well established, familiar concepts that are prevalent within bioinformatics, including types of data and data identifiers, data formats, operations and topics. EDAM provides a set of terms with synonyms and definitions - organised into an intuitive hierarchy for convenient use.  You can read find [EDAM on GitHub](https://github.com/edamontology/edamontology).

  

## Resource types (valid values of resourceType)
type | Description
--------- | -----------
Database | A collection of data, datasets, a registry etc.
Tool | Software which you can download, install, configure and run yourself.
Service | Software provided as a service and available for immediate use, e.g. on the Web.
Workflow | A definition of a collection of tools, services etc. for running in a workflow system.
Platform | An integrated environment, including suites, workbenches, workflow systems, frameworks etc.
Container | A collection of data, tools, services etc. in a portable environment, e.g. VMs, Docker.
Library | A package of code for building/extending tools, including widgets, plug-ins, toolkits etc.
Other | Other type of resource not listed above.

## Interface types (valid values of interfaceType)
type | Description
--------- | -----------
Command line | Text-based interface to a tool or service.
Web UI | Graphical user interface available on the Web.
Desktop GUI | Graphical user interface that runs on your own machine.
SOAP WS | Programmatic access provided via SOAP and WSDL file.
HTTP WS | Access provided via HTTP, including simple URLs, RESTful APIs etc.
API | Application programmers interface to a programming library.
QL | Query language interface to a database, e.g. SQL, SPARQL etc.


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
* Chris Morris (STFC, UK)
* Frederik Coppens (ELIXIR-BE)
* Heinz Stockinger (ELIXIR-CH)
* Helen Parkinson (EMBL-EBI, UK)
* Julie McMurry (EMBL-EBI, UK)
* Rodrigo Lopez (EMBL-EBI)
* Veit Schwämmle (SDU-BMB, DK)
* Delegates of the many BioMedBridges and ELIXIR workshops 

