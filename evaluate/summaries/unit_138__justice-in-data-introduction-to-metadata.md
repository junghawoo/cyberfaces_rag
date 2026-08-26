---
title: "Justice in Data: Introduction to Metadata and Provenance"
unit_id: 138
course_id: 10
level: "Foundation"
slug: justice-in-data-introduction-to-metadata
is_course: 0
---

# Justice in Data: Introduction to Metadata and Provenance

Foundation-level presentation on metadata and data provenance by Sharma Chakravarthyame (Professor), part of "Justice in Data" course addressing data governance and information management.

**Presentation Outline:** What is metadata? Why important? Implications of missing metadata. Data provenance definition. Provenance applications. Metadata-FAIR principles alignment. Conclusions.

**Metadata Definition:**
Information about data. Library catalog record analogy: documents who, what, when, where, how, why of data resource. "Data about data" describes other data. Geospatial metadata describes maps, GIS files, imagery, location-based resources. Example GIS metadata: creation date, author, contact information, source agency, map projection, coordinate system, scale, error, symbology explanation, attribute data dictionary, restrictions, licensing.

**Metadata Necessity:** Google and search tools cannot provide understanding, lineage, trustworthiness, or hidden web access (databases). Without metadata, raw data appears meaningless. Census data example (32, Private, 192965, HS-grad, 9, Separated, Sales, Not-in-family, White, Female, 0, 0, 45, United States, <=50K) is incomprehensible without field descriptions: workclass (Private, Self-emp-not-inc, Federal-gov, Local-gov, State-gov, Without-pay), fnlwgt (continuous), education (Bachelors, Masters, Doctorate, HS-grad, 11th, 9th, 7th-8th, 12th, Assoc-acdm, Assoc-voc, 1st-4th, 5th-6th, Preschool), education-num (continuous), marital-status (Married-civ-spouse, Divorced, Never-married, Separated, Widowed), occupation (Tech-support, Craft-repair, Sales, Exec-managerial, Prof-specialty, Farming-fishing, Transport-moving, Protective-serv, Armed-Forces), sex (Female, Male), race (White, Asian-Pac-Islander, Black, Amer-Indian-Eskimo, Other), capital-gain/capital-loss (continuous).

**Types of Metadata:**
- Descriptive: Content/context (title, creator, subject keywords, abstract)
- Structural: Physical structure of compound data (camera, aperture, exposure, file format, relations)
- Administrative: Management information (creation, access control, software requirements, copyright)
- Preservation: Archival sustainability
- Process: Computational/analytical procedures
- Provenance: Data lineage and origin tracking
- Reference: External linkages
- Statistical: Data quality metrics
- Use: Access/application patterns

**Metadata Standards/Schemas:**
Dublin Core (libraries, adaptable), MODS (richer description), Darwin Core (biological specimens), NASA standards (heritage ESDS standards, SPG), FGDC/CSDGM (Federal Geographic Data Committee, geospatial data), examples: biological data with taxonomy, tabular non-spatial data, project level, aerial photography, water sampling sites, models.

**Recommended Minimum Elements:**
Title/Name, Description (spatial/temporal/subject coverage), Format (file type, physical medium, dimensions, software requirements), Metadata (standard/schema version location), Identifier (DOI), Rights Holder, Rights (licensing), Contact Information.

**Machine-Readable Metadata:**
RDF (Resource Description Framework, W3C standard, www.w3c.org/RDF/) for computer consumption. Originally designed for web resource metadata. Labeled directed graphs (domain-independent). Consists of triples: subject (source URL), relationship, object (target URL). SPARQL query language (SQL-equivalent). Combines to form knowledge graphs. Large footprint. Supports semantic web (Web 2.0, 3.0), ontology definition via OWL (Web Ontology Language), taxonomy development, multi-source data integration, enhanced search focus.

**Data Provenance (Data Lineage):**
Record trail of data origin, evolution, and current location with explanations. "Who, Why, What, Where, When" (5 Ws). Word documents carry version-based provenance. Central to scientific data validation. Examples: health care records (patient history), USGS data (1999 Yugoslavia bombing incident caused by database update failures and missing provenance checking). Data traceability shows information evolution. Importance in contexts: health care, USGS mapping, decision-critical applications.

**Metadata Uses:** Enable data discovery, understanding, analysis/synthesis, data longevity maintenance, research project progress tracking, institutional return on investment demonstration. Metadata adds value to other information but rarely valuable independently (exceptions: text transcription of audio files).

**FAIR Principles Support:** Metadata enables Findability, Accessibility, Interoperability, Reusability through standardization and provenance documentation.

**Generation Methods:** Manual (accurate, detailed, labor-intensive via AmazonTurk) vs. automated (basic file size, extension, creation date, low accuracy).

## Summarized attachments

- **Introduction to Metadata and Provenance Recording** (`CTW-metadata_FINAL.pdf`, PDF): Foundation presentation by Sharma Chakravarthyame covering metadata definition (data about data), why metadata is important for discovery and understanding, nine types of metadata (descriptive, structural, administrative, preservation, process, provenance, reference, statistical, use), metadata standards (Dublin Core, MODS, Darwin Core, NASA, FGDC), machine-readable metadata (RDF, SPARQL), and data provenance tracking with 5 Ws (Who, Why, What, Where, When) in scientific and institutional contexts.
