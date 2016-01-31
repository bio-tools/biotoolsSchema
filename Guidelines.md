# Usage Guidelines
This is a **WORK IN PROGRESS** but will provide guidelines on the usage of biotoolsXSD for annotating bioinformatics software resources, particularly for registration in the [bio.tools](https://bio.tools) registry.

# General guidelines
General guidelines are given below.

## Resource IDs
The guidelines will cover:
* Format of resource ID in bio.tools (version is optional)
  * bio.tools/toolName/version
  * bio.tools/serviceProviderName/serviceName/version
* how IDs are created
* persistence of corresponding tool pages
* implications of changing toolName, serviceProviderName, serviceName, version

## Resource relationships
The guidelines will describe how bio.tools entries can / should / must be related to one another:
* Tool isNewVersionOf Tool
* Tool isOldVersionOf Tool
* Service usesAsDataSource Database
* Service uses Tool
* Platform includes Tool
* Platform includes Service
* Platform includes Database
* Container includes Tool
* Container includes Service
* Container includes Database

And maybe
* Workflow uses Tool
* Workflow uses Service
* Workflow uses Database


# Resource type-specific guidelines
Below are guidelines for the different types of resources that may be registered in the [bio.tools](https://bio.tools) registry.

## Databases
## Command-line tools
## Web applications
## Desktop GUIs
## Web services (REST/URL-based API)
## Web services (SOAP+WSDL)
## Workflows
## Workbench, e.g. Galaxy instance 
## Software suites, distros, platforms etc.
## Containers
## Libraries

