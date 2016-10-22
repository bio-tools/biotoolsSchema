# Usage Guidelines
This is a **WORK IN PROGRESS** but will provide guidelines on the usage of biotoolsSchema for annotating bioinformatics software resources, particularly for registration in the [bio.tools](https://bio.tools) registry. 

**IMPORTANT** these are very rough notes and describe in places future plans.

Basic details that will be included:
*  Semantics of resource / interface type (consider consolidated into a single, inuititive set)
*  Text from schema 
*  Facets and patterns
*  Enumerations
*  Samples (but improve these by using real world examples)

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

# biotoolsSchema element-specific guidelines
Below are guidelines for different elements (fields of information) defined by the biotoolsSchema XSD schema.

## <id>
* Describe the ID URL pattern used by bio.tools:
  * bio.tools/toolName/version
  * bio.tools/serviceProviderName/serviceName/
  * bio.tools/database/databaseName/
* "toolName" is identical to <name> (see below)
* "serviceProviderName" is specified upon registration (how?) and is identical to bio.tools subdomain (if the registrant wants this).  The value is normally the standard acronym (e.g. EMBL-EBI) or short form name of the institute.  
* "version" may be specified for tools only.  It is optional and is identical to <version> (see below).

## <name>
* Describe the facet and regex in English.  
* What to do if the unique name has been taken. 
* Stress this is used in the resource ID - and the implications of changing it.

* <homepage>
* What to do for tools that do not have an obvious homepage (with an example of such).

## <description>
* Style guidelines - what this should / should not normally contain.

## <resourceType>
* Include table explaining the enum, with examples of each type!  
* Explaim cases where more than 1 resource type could apply (e.g. a database, that provides an API and various Web apps), and that all types should be specified in such cases. 

## <version>
* Describe the facet and regex in English.  
* Stress this will be used in the resource ID (if specified) and the implications of changing it.


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

