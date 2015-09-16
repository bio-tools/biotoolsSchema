# What is biotoolsXSD?
**biotoolsXSD** is a formalised XML schema (XSD) which defines a resource description model for bioinformatics.  It can be used to describe software including databases, tools, services and so on, available under a variety of interfaces. 

biotoolsXSD defines 55 important scientific, technical and administrative attributes.  It concentrates upon the salient common features, with a minimal core of 10 attributes, mandating the necessary and sufficient information to support resource search and discovery.  

biotoolsXSD is used by the Tools & Data Services Registry (https://elixir-registry.cbs.dtu.dk/).  

# Motivation
Bioinformaticians routinely use a large and diverse set of tools and data, and demand powerful and convenient means to organise, find, understand, compare, select, use and connect the available resources. These tasks rely on consistent, machine-understandable resource descriptions. The need - filled by biotoolsXSD - is for an information model that puts the description of a broad range of resources  on a consistent syntactic basis.

# Applications 
biotoolsXSD is applicable to diverse bioinformatics software and interface types, including:
* **Databases** including repositories, datasets, registries etc.
* **Tools**	including downloadable pacakages which you install, configure and run yourself
* **Services** available for immediate use, e.g. on the Web
* **Workflows** definitions that may involve multiple databases, tools and services
* **Platforms** including suites, workbenches, workflow systems, frameworks etc.	
* **Containers** which provide data and services in a portable envionment, e.g. VMs and Docker. 
* **Libraries** of code for building tools, including widgets, plug-ins, toolkits etc.	
* Command line interfaces
* Web User interfaces
* Desktop GUIs
* SOAP Web Services
* HTTP Web Services including simple URL, RESTful APIs etc.



# Documentation and website

Full user documentation of biotoolsXSD is available at 

https://elixir-registry.cbs.dtu.dk/schema


## Mandatory attributes
Attribute | Description
--------- | -----------
name | Canonical resource name
homepage | Resource homepage (URL)
description | Short textual description of the resource
resourceType | Basic resource type: "Dataset", "Database",  "Framework", "Library", "Suite", "Widget", "virtual machine", "Tool", "Tool (query and retrieval)", "Tool (analysis)", "Tool (deposition)", "Tool (visualiser)", "Tool (utility)" or "Other"
interfaceType | Resource interface type: "Command-line", "Desktop GUI", "SOAP WS", "REST API", "Web UI", "URL", "API", "SQL" or "SPARQL"
topic | General domain the resource serves or other general category for it: EDAM Topic term(s)
functionName | Name(s) of the resource function(s): EDAM Operation term(s)
input->dataType | Type of input data (if any): EDAM Data term(s)
output->dataType | Type of ouput data (if any): EDAM Data term(s)
contactEmail* | Email address of contact
contactURL* | URL of contact

(* one of contactEmail or contactURL must be specified)



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
* Heinz Stockinger (ELIXIR-CH)
* Frederik Coppens (ELIXIR-CH)
* Julie McMurry (EMBL-EBI, UK)
* Helen Parkinson (EMBL-EBI, UK)
* Delegates of the many BioMedBridges and ELIXIR workshops 

