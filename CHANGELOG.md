# Changelog for biotoolsXSD
Description of changes are grouped as follows:
* **Added:** new features
* **Changed:** changes to existing functionality
* **Deprecated:** a once-stable feature that has been removed
* **Removed:** a deprecated feature that has been removed
* **Fixed:** a bug fix
* **Misc:** some miscellaneous other change


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

