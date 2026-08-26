---
title: "Link to FAIR resources"
unit_id: 7
course_id: 4
level: "Foundation"
slug: link-to-fair-resources
is_course: 0
---

# Link to FAIR resources

## Fetched resources (external URLs)

### FAIR resources (link)
*URL:* https://mygeohub.org/cybertraining/fair

# MyGeohub - What is FAIR?

MyGeohub - What is FAIR?
Skip to main content
Need help? Send a trouble report to our support team.
Search
Search
Cyber Training for FAIR Science
Courses
FACT Fellowship
2021 FACT Fellows
2020 FACT Fellows
2022 FACT Fellows
2021 FAIR Workshop
Team
What is FAIR?
What is FAIR?
In 2016, the ‘FAIR Guiding Principles for scientific data management and stewardship’ were published in Scientific Data. The authors intended to provide guidelines to improve the findability, accessibility, interoperability, and reuse of digital assets. The principles emphasise machine-actionability (i.e., the capacity of computational systems to find, access, interoperate, and reuse data with none or minimal human intervention) because humans increasingly rely on computational support to deal with data as a result of the increase in volume, complexity, and creation speed of data.
Supports the reuse of data
Sharing knowledge and collaboration
Leads to quicker discovery
Simplifies the cycle of research
Involves: researchers, publishers, and repositories
Principles for: data, metadata, and infrastructure
Findable.
Accessible.
Interoperable.
Reusable.
Objectives
FAIR-compliant data repositories
will add value to research data, provide metadata and landing pages for discoverability, and support researchers with documentation guidance, citation support, and data curation.
FAIR-compliant Earth and space science publishers
will align their policies to establish a similar experience for researchers. Data will be available through citations that resolve to repository landing pages. Data are not placed in the supplement.
Publishers and repositories are working together towards the advancement of FAIR science
Principles
Findable
The datasets and resources should be easily located by humans and computers …
(meta)data are assigned a globally unique and eternally persistent identifier.
Do you assign a persistent identifier to data products in your repository? If so, which PID type/scheme (e.g. DOI)? Do you assign more than one type?
What kinds of things do you assign PIDs to? What is the granularity (or granularities) of the things you assign PIDs to? Do you assign them to individual data values or items, to individual files, to coherent collections of files, and/or multiple granularities?
data are described with rich metadata.
Do your available data products come with metadata accessible or browsable by human users?
Do you attempt to capture good coverage of what are known as Dublin Core concepts?
Do you attempt to capture detailed metadata that is more specifically relevant to your user community (i.e., that goes beyond Dublin Core)?
What standard or community metadata schemas do you support? Do you specifically support any of the following: If you support any, do you support specific profiles of these metadata schemas?
Does your metadata include geolocation information?
Does it include temporal information (e.g. coverage in time)?
Does your repository accept metadata that is applicable to a specific discipline (and not just generally applicable to all disciplines)? Does your repository disallow or reject metadata that is specific to a particular discipline?
Does your metadata include a concept of authors? Contact points? Are these separate metadata elements?
Do you capture ORCID or other PIDs for authors? If yes: which? Researcher-ID? Scopus-ID?
(meta)data are registered or indexed in a searchable resource.
Does your exportable metadata include the data’s PID (e.g., the data DOI)?
Does your exportable metadata include other persistent identifiers? ORCiDs? Literature (Crossref) DOIs? Sample IGSNs? Author contributions (CRediT)?
metadata specify the data identifier.
Does your repository provide search capabilities of its contents?
Do you make your metadata searchable and/or indexable by any external systems? Which ones?
Do you export your metadata through any of the following mechanisms: OAI-PMH
Linked Data Platform
ResourceSync
Landing Page meta tags or similar embedding mechanisms
Have you reviewed and ensured the existence and accuracy of the re3data record for your repository?
Accessible
After the dataset is found, the user needs to be able to easily access the datasets …
(meta)data are retrievable by their identifier using a standardized communications protocol.
Do you provide a landing page accessible by resolving a PID assigned by your repository?
Do you support any machine-actionable data access mechanisms in which data can be retrieved given its identifier? Which standard mechanisms do you support? Are any considered specific to you your repository?
Do you support access to metadata via URLs and content-negotiation?
Do you embed machine-readable metadata in your Landing Pages? Do you embed via HTML
tags? Do you embed JSON-LD data? XML?
Does access to any data in your repository require authentication and authorization? Which machine-actionable access mechanisms support authentication?
Do you support any open standards for authentication and authorization?
the protocol is open, free, and universally implementable.
To maximise data reuse, the protocol should be free (no-cost) and open (-sourced) and thus globally implementable to facilitate data retrieval. Anyone with a computer and an internet connection can access at least the metadata. Hence, this criterion will impact your choice of the repository where you will share your data.
Examples:
HTTP, FTP, SMTP, …
Telephone (arguably not universally-implementable, but close enough)
A counter-example would be Skype, which is not universally-implementable because it is proprietary
Microsoft Exchange Server protocol is also proprietary
the protocol allows for an authentication and authorization procedure, where necessary.
This is a key, but often misunderstood, element of FAIR. The ‘A’ in FAIR does not necessarily mean ‘open’ or ‘free’. Rather, it implies that one should provide the exact conditions under which the data are accessible. Hence, even heavily protected and private data can be FAIR. Ideally, accessibility is specified in such a way that a machine can automatically understand the requirements, and then either automatically execute the requirements or alert the user to the requirements. It often makes sense to request users to create a user account for a repository. This allows to authenticate the owner (or contributor) of each dataset, and to potentially set user-specific rights. Hence, this criterion will also affect your choice of the repository where you will share your data.
Examples:
HMAC authentication
HTTPS
FTPS
Telephone
metadata are accessible, even when the data are no longer available.
Datasets tend to degrade or disappear over time because there is a cost to maintaining an online presence for data resources. When this happens, links become invalid and users waste time hunting for data that might no longer be there. Storing the metadata generally is much easier and cheaper. Hence, principle A2 states that metadata should persist even when the data are no longer sustained. A2 is related to the registration and indexing issues described in F4.
Examples:
Metadata are valuable in and of themselves, when planning research, especially replication studies. Even if the original data are missing, tracking down people, institutions or publications associated with the original research can be extremely useful.
Interoperable
The datasets need to be in a format that is usable by others, therefore needs to satisfy the following …
(meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.
Humans should be able to exchange and interpret each other’s data (so preferably do not use dead languages). But this also applies to computers, meaning that data that should be readable for machines without the need for specialised or ad hoc algorithms, translators, or mappings. Interoperability typically means that each computer system at least has knowledge of the other system’s data exchange formats. For this to happen and to ensure automatic findability and interoperability of datasets, it is critical to use (1) commonly used controlled vocabularies, ontologies, thesauri (having resolvable globally unique and persistent identifiers, see F1) and (2) a good data model (a well-defined framework to describe and structure (meta)data).
Examples:
The RDF extensible knowledge representation model is a way to describe and structure datasets. You can refer to the Dublin Core Schema as an example.
OWL
DAML+OIL
JSON LD
(meta)data use vocabularies that follow FAIR principles.
The controlled vocabulary used to describe datasets needs to be documented and resolvable using globally unique and persistent identifiers. This documentation needs to be easily findable and accessible by anyone who uses the dataset.
Examples:
Using the FAIR Data Point ensures I2
Links to resources
FAIR Data Point specification
(meta)data include qualified references to other (meta)data.
A qualified reference is a cross-reference that explains its intent. For example, X is regulator of Y is a much more qualified reference than X is associated with Y, or X see also Y. The goal therefore is to create as many meaningful links as possible between (meta)data resources to enrich the contextual knowledge about the data, balanced against the time/energy involved in making a good data model. To be more concrete, you should specify if one dataset builds on another data set, if additional datasets are needed to complete the data, or if complementary information is stored in a different dataset. In particular, the scientific links between the datasets need to be described. Furthermore, all datasets need to be properly cited (i.e., including their globally unique and persistent identifiers).
Examples:
FAIR Data Point
http://www.uniprot.org/uniprot/C8V1L6.rdf
Reusable
The datasets need to be able to be used by various people, therefore must have clear metadata …
meta(data) have a plurality of accurate and relevant attributes.
It will be much easier to find and reuse data if there are many labels are attached to the data. Principle R1 is related to F2, but R1 focuses on the ability of a user (machine or human) to decide if the data is actually USEFUL in a particular context. To make this decision, the data publisher should provide not just metadata that allows discovery, but also metadata that richly describes the context under which the data was generated. This may include the experimental protocols, the manufacturer and brand of the machine or sensor that created the data, the species used, the drug regime, etc. Moreover, R1 states that the data publisher should not attempt to predict the data consumer’s identity and needs. We chose the term ‘plurality’ to indicate that the metadata author should be as generous as possible in providing metadata, even including information that may seem irrelevant.
Some points to take into consideration (non-exhaustive list):
Describe the scope of your data: for what purpose was it generated/collected?
Mention any particularities or limitations about the data that other users should be aware of.
Specify the date of generation/collection of the data, the lab conditions, who prepared the data, the parameter settings, the name and version of the software used.
Is it raw or processed data?
Ensure that all variable names are explained or self-explanatory (i.e., defined in the research field’s controlled vocabulary).
Clearly specify and document the version of the archived and/or reused data.
(meta)data are released with a clear and accessible data usage license.
Under ‘I’, we covered elements of technical interoperability. R1.1 is about legal interoperability. What usage rights do you attach to your data? This should be described clearly. Ambiguity could severely limit the reuse of your data by organisations that struggle to comply with licensing restrictions. Clarity of licensing status will become more important with automated searches involving more licensing considerations. The conditions under which the data can be used should be clear to machines and humans.
Examples:
Commonly used licenses like MIT or Creative Commons can be linked to your data. Methods for marking up this metadata are provided by the DTL FAIRifier.
(meta)data are associated with their provenance.
For others to reuse your data, they should know where the data came from (i.e., clear story of origin/history, see R1), who to cite and/or how you wish to be acknowledged. Include a description of the workflow that led to your data: Who generated or collected it? How has it been processed? Has it been published before? Does it contain data from someone else that you may have transformed or completed? Ideally, this workflow is described in a machine-readable format.
Examples:
https://commons.wikimedia.org/wiki/File:Sampling_coral_microbiome_(27146437650).jpg includes authorship details, and uses the Creative Commons Attribution Share Alike license, which indicates exactly how the data author wishes to be cited.
(meta)data meet domain-relevant community standards.
It is easier to reuse data sets if they are similar: same type of data, data organised in a standardised way, well-established and sustainable file formats, documentation (metadata) following a common template and using common vocabulary. If community standards or best practices for data archiving and sharing exist, they should be followed. For instance, many communities have minimal information standards (e.g., MIAME, MIAPE). FAIR data should at least meet those standards. Other community standards may be less formal, but nevertheless, publishing (meta)data in a manner that increases its use(ability) for the community is the primary objective of FAIRness. In some situations, a submitter may have valid and specified reasons to divert from the standard good practice for the type of data to be submitted. This should be addressed in the metadata. Note that quality issues are not addressed by the FAIR principles. The data’s reliability lies in the eye of the beholder and depends on the intended application.
Examples:
http://schema.datacite.org/ [for general purpose, not domain-specific]
https://www.iso.org/standard/53798.html [geographic information and services]
http://cfconventions.org/ [climate and forecast]
Initiatives
Resources
Article describing the Enabling FAIR Data Project
Outcome of the initial Stakeholder Meeting from Nov 16-17, 2017
DataONE webinar recording
Enabling FAIR Data (high-level) Project Site
