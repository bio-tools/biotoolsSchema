# Changelog for biotoolsSchema
Description of changes are grouped as follows:
* **Added:** new features
* **Changed:** changes to existing functionality
* **Deprecated:** a once-stable feature that has been removed
* **Removed:** a deprecated feature that has been removed
* **Fixed:** a bug fix
* **Misc:** some miscellaneous other change

# November 17, 2016 biotoolsSchema-2.0.0.xsd released

## Added
1. Added "Not available" to patterns for 'doiType' (simple type) and 'pmid' and 'pmcid' (elements) to support the specification that a publication is "Not available" for a tool (as required by the bio.tools information standard (https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst).

## Added / changed / removed
1. 'publication->type' enum, mulitple modifications:
1.1 "Primary" (no change) The principal publication about the software itself; the article to cite when acknowledging use of the software.
1.2 "Deployment" (new!) A publication describing a deployment of the software in some usable form, including for example a webserver providing the tool functions, or the inclusion of the tool in a larger package or suite.
1.3 "Method" (new!) A publication describing a scientific method or algorithm implemented by the software.
1.4 "Usage" (new!) A publication describing the application of the software to scientific research, a particular task or dataset.
1.5 "Comparison" (was "Benchmark") A publication which assessed the performance of the software relative to other tools.
1.6 "Review" (no change) A publication where the software was reviewed.
1.7 "Other" (removed!)
	
## Removed
1. 'summary->doi' removed (use instead 'summary->identifier->value' and set 'summary->identifier->type' = toolid)
2. 'summary->versionID' removed (this no longer supported by bio.tools)
3. 'nameType' simple type removed (facets are defined on individual elements now - this is clearer / more usable). Elements refactored are:
	3.1 'summary->name' element (now xs:token)
	3.2 'summary->version' element (now xs:token)
	3.3 'contact->name' element (now xs:token)
	3.4 'credit->name' element (now xs:token)
	
## Changed
1. 'summary->version' moved to 'identifier->version' (and still optional, i.e. 0 or 1) 
2. 'name' element 'maxlen' facet set to 50.
3. 'version' element 'maxlen' facet set to 50.
4. Various elements of type string are now type xs:token:
        4.1 'shortDescription
5. 'linkType->comment' type set to textType (consistent with other free-text comments) ('linkType' is complex type used by 'link->comment' and 'documentation->comment' elements)
	
# November 17, 2016 biotoolsSchema-2.0.0.xsd released
Sorry, no bandwidth to provide summary of changes : please see the schema documentation.  changelog will be maintained properly henceforth!

# November 8, 2016 biotoolsSchema-2.0-beta04.xsd released
Sorry, no bandwidth to provide summary of changes : please see the schema documentation.

# November 3, 2016 biotoolsSchema-2.0-beta03.xsd released
Sorry, no bandwidth to provide summary of changes : please see the schema documentation.

# October 22, 2016 biotoolsXSD officially renamed to biotoolsSchema, biotoolsSchema-2.0-beta02.xsd released
Sorry, no bandwidth to provide summary of changes : please see the schema documentation.

# August 12, 2016  biotoolsXSD-2.0-beta01.xsd released
A complete revision of the schema.  Too many changes to list, therefore the highlights only are summarised below.  For more information please read the schema documentation.

## Added : new or restructured element groupings (see schema docs for details)
1. 'summary': "Basic information about the software."
2. 'function': "Details of the function(s) that this software provides, expressed in terms from the EDAM ontology."
3. 'labels': "Miscellaneous scientific, technical and administrative details of the software, expressed in terms from controlled vocabularies."
4. 'relation': "Details of a relationship this software shares with other software registered in bio.tools."
5. 'commandLineSpec': "Details of the command-line interface to a tool, if appropriate."
6. 'apiSpec': "Details of the API to a service, if appropriate, including service endpoints."
7. 'image': "Details for a virtual machine image or container for the software."
8. 'download': "Link to a miscellaneous download for the software, e.g. source code."  A controlled vocabulary for download types is defined.
9. 'documentation': "A link to documentation about the software including training materials."  A controlled vocabulary for documentation types is defined.
10. 'publication': "A publications about the software.".  A controlled vocabulary for publication types is defined.
11. 'contact': "Details of a contact for the software, e.g. developer or helpdesk."  A controlled vocabulary for contact types/roles is defined.
12. 'credit': "An individual or organisation that should be credited for the software."

## Added : new elements
1. 'biotoolsID': "Unique ID that is assigned upon registration of the software in bio.tools."
2. 'doi': "Canonical Digital Object Identifier of the software assigned by the software developer or service provider."
3. 'shortDescription': "Short and concise textual description of the software function."
4. 'repository': "Repository where source code, data and other files may be downloaded."
5. 'socialMedia': "A website used by the software community including social networking sites, discussion and support fora, WIKIs etc."
6. 'function->comment': " Concise textual description of the function(s), if this is not already obvious from the resource description."
7. 'goTermID': "Gene function including molecular function, cellular component and biological process.  Miscellaneous ontology annotation. The ID of Gene Ontology (GO) concept(s) are specified."
8. 'soTermID': Features which can be located on a biological sequence. The ID of Sequence Ontology (SO) concept(s) are specified.
9. 'taxId': NCBI taxonomy ID of taxonomic group the software (particularly database portals) caters for.
10. 'status': Label describing miscellaneous status of the software."  A controlled vocabulary is defined.
11. 'credit->orcidId' : "Unique identifier (ORCID iD) of a person that is credited."
12. 'credit->gridId' : "Unique identifier (GRID ID) of an organisation that is credited."

## Added : new enum values
1. New values to <license> enum:
"Other"
"Proprietary"
"Common Development and Distribution License (CDDL-1.0)"

2. New values to <language> enum:
"AWK"
"MATLAB"
"JSP"
"PyMOL"

## Changed : element name changes
1. 'resources' -> 'tools'
2. 'resource' -> 'tool'
3. 'functionName' -> 'operation'
4. 'resourceType' -> 'toolType'
5. 'platform' -> 'operatingSystem'

## Changed : other
1. 'operation', 'data', 'format' and 'topic' elements now include 'uri' and 'term' elements.
2. 'collection' : now restricted to accept a bio.tools ID of a software collection, rather than free-text.

## Removed
1. 'publications' element group replaced by 'publication' with new structure.
2. 'uses' element group replaced by 'relation'.
3. 'interface' element group removed, now handled by 'download' and 'documentation'.  Note that 'interfaceType' is removed completely (now subsumed in 'toolType').
4. 'elixirInfo' element group, 'maturity' and 'cost' removed, now handled by 'status'.
5. 'docs' element group replaced by 'documentation'.
6. 'credits' element group replaced by 'credit'.
7. 'canonicalID' replaced by 'doi'.
8. 'accessibility' now handled via 'status'.
9. 'tag' removed: annotations are now restricted to controlled vocabulary terms defined in 'labels'.
10. 'functionHandle' and 'dataHandle' removed, now handed by 'commandLineSpec'.
11. 'functionDescription' and 'dataDescription' removed, now handled by 'function->comment'.
12. 'sourceRegistry' removed, now handled by 'collection'.




# October 17th, 2015  biotoolsXSD-1.4.xsd released
## Added
* New 'docs->docsDownloadSource' optional element : "Source code downloads page (URL)"
* New 'docs->docsDownloadBinaries' optional element : "Software binaries downloads page (URL)"
* New 'docs->docsGithub optional' element : "Github page (URL)"
* "Maintainer" added to 'contactRole' enum
* "Other" added to 'resourceType" enum

## Changed
* 'publications' is now optional
* 'functionHandle' element 'maxLen' facet increased to 300 (via 'maxLen' facet on 'name' simpleType; also set to 300)
* Parentheses added to 'pattern' restriction on 'name' element, which is now  [\p{Zs}A-Za-z0-9+\.,\-_:;()]*

## Misc
* docsDownload purpose changed from "Software or data downloads page (URL)" to "General downloads page (URL)"



# September 22nd, 2015  biotoolsXSD-1.3.xsd released

## Added
* "Artistic License 2.0" added to 'license' enum
* "Icarus" added to 'language' enum
* 'id' attribute added to 'resource' element.  This is the unique ID (URI) of the resource.
* Default value of "None" added to publicationsPrimaryID and publicationsOtherID



## Changed
**safe changes:**
* 'name' element 'maxLen' facet restriction increased to 200 characters
* '+' added to 'name' simpleType pattern restriction, which is now [\p{Zs}A-Za-z0-9+\.,\-_:;]* 

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

