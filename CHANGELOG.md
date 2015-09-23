# Changelog for biotoolsXSD
Description of changes are grouped as follows:
* **Added:** new features
* **Changed:** changes to existing functionality
* **Deprecated:** a once-stable feature that has been removed
* **Removed:** a deprecated feature that has been removed
* **Fixed:** a bug fix
* **Misc:** some miscellaneous other change



# September 22nd, 2015  biotoolsXSD-1.3.xsd released

## Added
* "Artistic License 2.0" added to 'license' enum
* 'id' attribute added to 'resource' element.  This is the unique ID (URI) of the resource.


## Changed
**potentially breaking change:**

* 'maturity' element enum values changed to:
  * "Early" (was "Nascent" or "Young" in biotoolsXSD 1.2)
  * "Stable" (was "Established" in biotoolsXSD 1.2)
  * "Deprecated" (was "Retiring" or "Extinct" in biotoolsXSD 1.2)

* 'platform' enum value "Unix" removed (use "Linux" instead)

* 'resourceType' element enum values removed: "Dataset", "Tool (query and retrieval), "Tool (analysis)", "Tool (deposition)", "Tool (visualiser)", "Tool (utility)", "Suite", "Framework", "Virtual machine", "Widget" and "Other"

* New 'resourceType' enum values are as follows:
   * "Database" (was "Database" or "Dataset" in biotoolsXSD 1.2)
   * "Tool" (was "Tool", "Tool (query and retrieval), "Tool (analysis)", "Tool (deposition)", "Tool (visualiser)", "Tool (utility)" or "Workflow" in biotoolsXSD 1.2)
   * "Service" (new in biotoolsXSD 1.3)
   * "Workflow" (no change)
   * "Platform" (new in biotoolsXSD 1.3, was "Framework" or "Suite" in biotoolsXSD 1.2)
   * "Container" (new in biotoolsXSD 1.3, was "Virtual machine" in biotoolsXSD 1.2
   * "Library" (was "Library" or "Widget" in biotoolsXSD 1.2)

* The definition of these resource types are:
   * "Database" - A collection of data, datasets, a registry etc.
   * "Tool" - Software which you can download, install, configure and run yourself.
   * "Service" - Software provided as a service and available for immediate use, e.g. on the Web.
   * "Workflow" - A definition of a collection of tools, services etc. for running in a workflow system.
   * "Platform" - An integrated environment, including suites, workbenches, workflow systems, frameworks etc.
   * "Container" - A collection of data, tools, services etc. in a portable environment, e.g. VMs, Docker.
   * "Library" - A package of code for building/extending tools, including widgets, plug-ins, toolkits etc.

* 'interfaceType' element enum values removed:  "REST API", "URL", "SQL" and "SPARQL"

* New 'interfaceType' enum values are as follows:
   * "Command-line" (no change)
   * "Web UI" (no change)
   * "Desktop GUI" (no change)
   * "SOAP WS" (no change)
   * "HTTP WS" (new in biotoolsXSD 1.3, was "REST API" or "URL" in biotoolsXSD 1.2)
   * "API" (no change)
   * "QL" (new in biotoolsXSD 1.3, was "SQL" or "SPARQL" in biotoolsXSD 1.2)

* The definition of these interface types are:
   * "Command line" - Text-based interface to a tool or service.
   * "Web UI" - Graphical user interface available on the Web.
   * "Desktop GUI" - Graphical user interface that runs on your own machine.
   * "SOAP WS" - Programmatic access provided via SOAP and WSDL file.
   * "HTTP WS" - Access provided via HTTP, including simple URLs, RESTful APIs etc.
   * "API" - Application programmers interface to a programming library.
   " "QL" - Query language interface to a database, e.g. SQL, SPARQL etc.

* 'name' element 'maxLen' facet restriction increased to 200 characters
* '+' added to 'name' simpleType pattern restriction, which is now [\p{Zs}A-Za-z0-9+\.,\-_:;]* 

## Deprecated
* Use of the 'tag' element is deprecated and will be removed in a future version.

## Removed
## Fixed
## Misc



# June 8th, 2015  biotoolsXSD-1.2.xsd released

## Added
* Bash added to enum of 'language' element
* tag maxlen facet set to 50

## Changed
* maxLen facet restriction on all elements of type 'Text' removed (was 512), such that the length restriction of 1000 (defined on 'Text') applies
* Single space added to 'Name' simpleType pattern restriction, which is now  [\p{Zs}A-Za-z0-9\.,\-_:;]*
* The following elements (all simpleType) changed type to simpleType 'Name':
  * 'collection'
  * 'usesName'
  * 'function->input/output->dataHandle'
  * 'elxirInfo->elixirStatus'
  * 'elxirInfo->elixirNode'
  * 'function->functionHandle'

**potentially breaking change:**
* 'tag' element (was complexType ontologyTerm) also changed to simpleType "Name"



# May 5th, 2015  biotoolsXSD-1.1.xsd released

## Added
* "accessibility" (optional) added:  whether resource is accessible to all or not: enum of "Public" or "Private"
* New simple type URLFTP which is URL supporting FTP URLs

## Changed
* 'publications' (1 max.) **is now mandatory**, 'publications->publicationsPrimaryID' is now mandatory (1 max.)
* "None" value added to valid patterns for 'CitationID' simpleType, i.e. 'publications->publicationsPrimaryID' may have a value of "None" if PMID, PMCID or DOI is not available.
* 'Name' element pattern restriction added:  [A-Za-z0-9\.,\-_:;]*
* 'Name' element maxLen facet restriction reduced from 100 to 50 characters
* "Dataset" value added to enum of resourceType
* 'docs->docsDownload' type changed to URLFTP from URL
* 'docs->docsCitationInstructions' changed to URLFTP from URL
* 'docs->docsTermsOfUse' changed to URLFTP from URL
* 'interface->interfaceDocs' changed to URLFTP from URL
* 'resourceType' type changed to 'Name' simpleType (enum of permitted values preserved)
* 'interfaceType' type changed to 'Name' simpleType (enum of permitted values preserved)
* 'maturity' type changed to 'Name' simpleType (enum of permitted values preserved)
* 'platform' type changed to 'Name' simpleType (enum of permitted values preserved)
* 'language' type changed to 'Name' simpleType (enum of permitted values preserved)
* 'license' type changed to 'Name' simpleType (enum of permitted values preserved)
* 'cost' type changed to 'Name' simpleType (enum of permitted values preserved)
* 'description' maxLen facet restriction reduced from 1000 to 512 characters
* 'function->functionDescription' maxLen facet restriction reduced from 1000 to 512 characters
* 'function->input/output->dataDescription' maxLen facet restriction reduced from 1000 to 512 characters

## Fixed
* 'language' enum value of "C Shapr" changed to "C#"
* 'language' enum value of "Assembly" changed to "Assembly language"
* 'language' enum value of "Methematica" changed to "Mathematica"
* 'language' enum value of "R changed to "R"

