---
title: "Justice in Data: FAIR Data Principles"
unit_id: 130
course_id: 10
level: "Foundation"
slug: justice-in-data-fair-data-principles
is_course: 0
---

# Justice in Data: FAIR Data Principles

## Extracted resources (local files)

### FAIR Data Principles Slides
*Source file:* `FAIR_Principles_FINAL.pdf`  ·  *type:* file

FAIR Data Principles

Lecture Objectives
●Define the FAIR data principles
●Describe the importance of incorporating FAIR data 
principles into research.
2

BACKGROUND
●
In the case of Research & Development (R&D), over $2.1 Trillion is spent globally 
every year. This R&D often results in datasets which are useful for further research. 
●
If this data cannot be found, cannot be accessed, does not interoperate, therefore is 
unable to be reused, 
huge financial loss for global research 
setback to scientific progress.
●
Even though the FAIRness of data is so important, only 28% of researchers are 
familiar with the principles, according to the 2021 State of Open Data report by Digital 
Science.
3

WHAT IS FAIR? 
We rely on computational support from machines. FAIR data 
can enable computational systems to find, access, interoperate, 
and reuse data with no or minimal human intervention.
F
A
I
R
Findable Accessible Interoperable Reusable
“With big data, comes big responsibility”
4

WHY ARE FAIR PRINCIPLES REQUIRED ? 
●As our world has continually become more digitized, we have begun facing 
new challenges for a digital world. One of these challenges is how to handle 
data
●Research data is an asset and digital research data can be stored, reused, 
repurposed 
●Access to this data facilitates knowledge, discovery, improves research 
transparency 
●Sharing aids innovations/solves problems – avoids repetition
5

IMPORTANT DEFINITIONS
WHAT IS A REPOSITORY ?
A repository is a free online collection of 
documents, often scholarly. The data 
repository is a large database infrastructure —
several databases — that collect, manage, and 
store data sets for data analysis, sharing and 
reporting. There are several kinds:
•
Repositories maintained by a single 
university, for its own students' dissertations and 
theses, and/or its own staff's published research. 
This often includes versions of papers published 
in scholarly journals
•
General repositories, with very large and 
diverse collections
Example : GitHub, Zenodo (Zenodo -
Research. Shared.)
6

Interface of “zenodo”
7

MACHINE-READABLE DATA
●
Data in a format that can be easily processed by a computer without human intervention.
●
Scans (photographs) of text are not machine-readable (but are human readable!) but the 
equivalent text in a format such as a simple ASCII text file can be machine readable.
Two Groups of Machine-readable data : 
●
Human-readable data that is marked up so that it can also be read by machines e.g., HTML 
(HyperText Markup Language) is the code that is used to structure a web page and its 
content. For example, content could be structured within a set of paragraphs, a list of 
bulleted points, or using images and data tables.
●
Data file formats intended principally for processing by machines e.g., CSV (Comma 
Separated Values) file format.
8
IMPORTANT DEFINITIONS

PERSISTENT IDENTIFIERS
●
A persistent identifier (PI or PID) is a long-lasting reference to a document, file, web page, or 
other digital object.
Permalinks
●
Permalinks are URLs that are intended to remain the same, limiting the amount of URL changes 
that can render objects unfindable. These links are often short and easy for people to type. These 
URLs need to be actively maintained to continue to be persistent.
●
Example : University research work repository: ResearchWorks — UW Libraries (washington.edu)
Digital Object Identifiers (DOIs)
●
A DOI is a persistent, unique digital identifier associated with an object, which contains metadata 
that makes the object easier to find. 
●
DOIs create a link to the content’s location on the internet, so that the DOI will always point to the 
correct unique object. 
●
If a journal changes publisher, the DOI will remain the same, and the link will still take a reader to 
the paper, wherever it is hosted.
●
Example : Citation (APA example): Mitchell, T. (1997). Sahel Precipitation Index [Data set]. The 
Joint Institute for the Study of the Atmosphere and Ocean 
(JISAO). https://doi.org/10.6069/H5MW2F2Q
9
IMPORTANT DEFINITIONS

PERSISTENT IDENTIFIERS
ROR (Research Organization Registry)
●
A unique identifier for every research organization in the world.
●
The University of Texas at Arlington’s ROR ID: https://ror.org/019kgqr73
ORCID (Open Researcher and Contributor ID)
●
“ORCID provides a persistent digital identifier (an ORCID iD) that you own and control, and 
that distinguishes you from every other researcher. You can connect your iD with your 
professional information — affiliations, grants, publications, peer review, and more.”
https://orcid.org/
●
Your ORCID allows you to store together all your research outputs within your account and 
share them between platforms.
10
IMPORTANT DEFINITIONS

DATA
●Data is raw and unorganized facts that are useless
without proper processing and organizing them to
retrieve some information for future use.
●It can simply be a piece of information, a list of
grocery
items,
or
observations,
a
story
or
a
description of a certain scenario.
METADATA
●Metadata is a data about data. Metadata shows
basic information about data, which can make
finding and working with specific instances of data
easier.
●It
may
be
created
manually
or
by
automatic
information processing.
11
IMPORTANT DEFINITIONS

12

Brainstorming session
Before going into details of FAIR principles, feel free to ask any questions. 
13

FAIR PRINCIPLES

FINDABLE
●
When data is enriched with metadata to describe the data and identified using unique and persistent 
identifiers (PIDs), such as DOIs both humans and computers could easily find and consume data. 
●
Machine-readable metadata are essential for automatic discovery of datasets and services, so this is 
an essential component of the FAIR process.
•
Data and metadata are assigned a unique and persistent identifier(PID). 
•
Persistent identifiers help accurate mapping of information between the systems and support the research process. 
•
ORCID identifier is an example of common PIDs used in research.
Metadata and data are searchable online i.e. registered in a searchable resource.
FINDABLE means that the data is discoverable by both, humans and machines. 
15

Findable (Principles)
•
F1: (Meta) data are assigned globally unique and persistent identifiers
One particular person on planet earth has this globally unique and persistent 
identifier(PID): https://orcid.org/0000-0001-8888-635X
•
F2: Data are described with rich metadata
Metadata can (and should) be generous and extensive, including descriptive information about the context,
quality and condition, or characteristics of the data.
Rich metadata implies that you should not presume that you know who will want to use your data, or for
what purpose.
•
F3: Metadata clearly and explicitly include the identifier of the data they describe
The metadata and the data set they describe are separate files. The association between a metadata file
and the data set is obvious thanks to the mention of the data set’s PID in the metadata.
Make sure that the metadata contains the data set’s PID.
•
F4: (Meta)data are registered or indexed in a searchable resource
Identifiers and rich metadata descriptions alone will not ensure ‘findability’ on the internet. Perfectly good
data resources may go unused simply because no one knows they exist.
There are many ways in which digital resources can be made discoverable, including indexing
16

Example:
●
A student’s final year project is to investigate the relationship between urbanization and extreme rainfall.
●
The student uses “zenodo” to look for similar journal publications.
●
Opening a relevant journal paper, information such as DOI, publication date, versions, indexing etc. can also 
be seen.
Unique identifier
Indexed in OpenAIRE
OpenAIRE provides Integrated scientific 
information - where the publication, 
datasets, and project information for each 
funder, project, or content provider are all 
in one place
17

A Question About Findable Principles
What qualities of identifiers do the FAIR principles recommend?
A. Continue to operate indefinitely
B. Unambiguously identify data and metadata 
C. Continue to operate for the foreseeable future 
Correct Answers
B,C
18

ACCESSIBLE
●
Accessible means that the data are persisted in appropriate storage and this does not mean that the 
data have to be openly available for everyone. 
●
However, information on the proper data access mechanism should be available. For example, 
sensitive data should be properly marked with the pertinent sensitivity (public, confidential, highly 
confidential, restricted, etc.) class and security level (e.g. 1-5 with 1 being mission critical and 5 being 
public access). 
●
If the material contains sensitive personal data, or special category data, for example, a confidentiality 
assessment needs to be made before the material can be released to anyone. 
●
Metadata, however, are not sensitive, so even if the data cannot be made freely accessible, you can 
use metadata to show that the material exists and under which conditions you may access and reuse it. 
All data should be made available to others. Humans and machines alike should be able to gain 
access to your data.
Metadata are retrievable by machines and humans through a well-defined, standardized protocol and that the protocol is open, free, and universally 
implementable.
Remember that not all data has to be made open. Data can be restricted and still be FAIR.
As Open as Possible, As Closed as Necessary
19

Accessible (Principles)
•
A1: (Meta)data are retrievable by their identifier using a standardized communication protocol

Most users of the internet retrieve data by ‘clicking on a link’.

Principle A1 states that FAIR data retrieval should be mediated without specialized or proprietary tools or 
communication methods.
•
A1.1: The protocol is open, free and universally implementable
To maximize data reuse, the protocol should be free (no-cost) and open (-sourced) and thus globally 
implementable to facilitate data retrieval. 
Anyone with a computer and an internet connection can access at least the metadata. 
•
A1.2: The protocol allows for an authentication and authorization procedure where necessary
It often makes sense to request users to create a user account for a repository. This allows to authenticate 
the owner (or contributor) of each dataset, and to potentially set user-specific rights. Hence, this criterion will 
also affect your choice of the repository where you will share your data.
•
A2: Metadata should be accessible even when the data is no longer available
For “zenodo”, data and metadata will be retained for the lifetime of the repository. 
Metadata are stored in high-availability database servers which are separate to the data itself.
20

Example:
To find a relevant article on “zenodo”, we will simply be 
using an internet connection and type the name
This journal has restricted access. You 
will need to request access to the data.
This journal has closed access. You can 
see the publication, however, cannot 
access the data. 
This can give an idea that a particular 
research has been done.
21

A Question About Accessible Principles
What is the value of having a landing page even after the data is no longer available? Choose the 
correct one
A. To provide evidence that a particular line of research had been conducted 
B. To minimize updates to training materials
Correct Answer
A
22

Interoperable
The main responsibility for this rests on the organization that makes the data accessible. But it also
means that data producers and consumers should use standardized ways to enter information such as
dates, time periods, and geographic coordinates, etc.
Proprietary software such as software you need to buy a license for or pay a 
fee to access.
You use well-known and open formats and software, when 
possible. For example, pdf, csv, jpeg.
Data can be integrated with other data and systems, both internal and
external to an organization. This can be achieved through using metadata
standards, nomenclature, and governed vocabularies
means that the data can be exchanged and used across different applications and systems 
— also in the future
Metadata include certified references to other metadata.
23

Interoperable (Principles)
•
I1: (Meta)data use a formal, accessible, shared, and broadly 
applicable language for knowledge representation
Obvious issues arise when different languages are used to describe the data or when spelling errors make the comparison of 
descriptions and variable names more difficult. 
It is critical to use controlled vocabularies and a well-defined framework to describe and structure (meta)data in order to ensure 
findability and interoperability of datasets.
•
I2: (Meta)data use vocabularies that follow the FAIR principles

The controlled vocabulary used to describe data sets needs to be documented. This documentation needs to be easily 
findable and accessible by anyone who uses the data set.
•
I3: (Meta)data include qualified references to other (meta)data
Scientists should clearly identify relationships between datasets in the metadata, e.g., by naming their persistent identifiers and 
describing their scientific link to each other (e.g.‘ is new version of‚,‘ is supplement to‚,‘ relates to‘, etc.)
24

Example:
●
A journal paper on “zenodo” with different versions 
and detail of identifiers. 
Detail of related identifiers. 
All the previous versions are available. 
25

A Question About Interoperable Principles
What can be done to make data more interoperable? Select all that apply.
A. License it with a Creative Commons licence
B. Use standard vocabularies in data and metadata 
C. Put a PID on it 
D. Include clear instructions on how to obtain access in the metadata
E. Make the data self-describing 
Correct Answers
B, C, E
26

Reusable
The data should conform to community standards and include clear terms and conditions on how the data
may be accessed and reused, preferably by applying machine-readable standard licenses.
Data and metadata are richly described with several accurate and relevant attributes.
means that the data are well documented and provide rich information about the context of data creation.
Data and metadata are released with a clear and accessible data usage license.
Data and metadata are associated with detailed provenance i.e. that explains how, why and who created and processed 
the data.
All data meets domain-relevant community standards.
The ultimate goal of FAIR is to optimize the reuse of data.
To achieve this, metadata and data should be well-described so that they can be replicated and/or combined in different settings. Reusable means that
the data are well documented and provide rich information about the context of data creation.
The conditions for how the data may be used should also be specified.
•
Additional conditions for reusability are that the data are described with sufficient and relevant metadata, that both humans and
computers can read the metadata.
•
For instance, the purpose of the collected data, the context for the data collection as well as which equipment and software were
used for the data collection and analysis.
27

Reusable (Principles)
•
R1: (Meta)data are richly described with a plurality of accurate and relevant attributes
The (meta)data creators should be as detailed as possible when adding (meta)data. This can lead to the 
provision of (context) information that may first appear to be irrelevant.
Scope: For what purpose was data created / collected? 
Does the dataset contain raw data or processed data or both? 
•
R1.1: (Meta)data are released with a clear and accessible data usage license
The legal conditions under which data may be used should be clearly defined for machines and man. This 
must be represented in the metadata.
•
R1.2: (Meta)data are associated with detailed provenance
For the collection of provenance information, researchers should clearly describe their role in the data 
generation workflow, how they wish to be cited, and who was involved. 
They should also state whether the dataset contains foreign data. 
The description should be in a human- and machine-readable format.
•
R1.3: (Meta)data meet domain-relevant community standards
Scientists should prepare their (meta)data according to their community standards and best practices for 
data archiving and publication.
Depending on the area of expertise, several standards / best practices may have been established in the 
research discipline.
28

Example:
Downloading temperature dataset from GOES satellite. This example is from GitHub repository.   
Data usage license. 
Description of the data 
The owner mentioning how to cite his 
work 
29

A Question About Reusable Principles
What issues do you need to consider when you are preparing your own data for reuse? Select all that apply.
A. How you will clearly indicate how others are allowed to use it 
B. Which metadata standards and controlled vocabularies provide accurate and relevant information about the 
content and context of the research data 
C. The file formats which are prepared for reuse 
D. Completeness of data documentation for future users 
E. None of the above
Correct Answers: 
•A, B, C, D 
30

Ensure Your Data Support the FAIR Principles
Dataset/Files
•
Your dataset should be open (if available).
•
Your dataset should have a DOI.
•
All files should be in open formats.
•
Your data should be discoverable through an open search protocol (for example, 
via Google).
Metadata
•
The metadata should include useful disciplinary notation and terminology.
•
The metadata should include machine-readable standards where available (e.g.
ORCIDs (for authors and/or data contributors)).
•
Provide a citation format for the data.
•
Indicate any terms of use clearly.
31

Ensure Your Data Support the FAIR Principles
Tips for Preparing Your Data for Sharing
•
Describe methods of data collection and file structures.
•
Reference articles and include ORCIDs of all data 
contributors.
Documenting your data and files
•
You should include raw or processed data or both, 
depending on what is most useful or common in a 
discipline.
•
Your file formats should be common and open.
•
Organize the files logically according to your project.
Preparing your data files
•
Zip up all files into one package or dataset.
•
Select a well-known data repository and upload your data.
•
Make sure the repository provides a DOI to access and re-
use the data.
•
Provide a license attribution for your data, so users can 
easily copy and attribute.
Depositing your data in a repository
32

HOW COMPLYING WITH FAIR HELPS : 
•
Given our reliance on digital data, it’s increasingly important to make data as FAIR as
possible.
•
Employing the FAIR principles makes data more valuable by improving its findability
through unique identifiers and allowing for easier combination and integration.
•
By making your data FAIR and accessible to other researchers, you are improving
transparency of your research and increasing knowledge synthesis efforts.
New 
discoveries
Can create 
new 
collaborations
Reduces 
research 
duplication
Enables 
verification 
of results
33

HOW COMPLYING WITH FAIR HELPS : 
•
Achieving maximum impact from research.
•
Increasing the visibility and citations of research.
•
Improving the reproducibility and reliability of research.
•
Attracting new partnerships with researchers and policy and broader communities.
•
Enabling new research questions to be answered
34

Thanks!
Questions?
35

## Fetched resources (external URLs)

### FAIR Data Principles Pre-Survey (link)
*URL:* https://utaedu.questionpro.com/a/TakeSurvey?tt=HdfSgNqMzlUECHrPeIW9eQ%3D%3D

[survey link — skipped]

### FAIR Data Principles Recording (link)
*URL:* https://www.youtube.com/watch?v=yE451byTkLM

[YouTube transcript yE451byTkLM]
so this next section is called Fair data principles so we will start off with um the pre-survey for this which Dr Forbes has just dropped into the into the um chat so if you can take five minutes to go through that pre-survey that's listed in the chat and then we will get started and if you're having any issues with the pre-survey for fair data principles please let me know all right so I'll give you just one more minute to finish up that pre-survey if you have not yet had an opportunity to do that okay so let's carry on with our discussion of fair data principles if anybody is still trying to um fill out the survey please let me know and I can I can pause again no okay so when we're talking about Faraday principles I gave you a brief overview in the previous Slide by the previous section but we'll talk a little a little bit more in depth about this now so the overall objectives for this lecture are that you will be able to define the fair data principles and that you'll be able to describe the importance of incorporating Fair data principles into your research so um just for a background um in research and development over 2.1 trillion dollars is spent uh globally every year and this research often produces data sets that are useful for for for sorry for further research um historically though this data that's been produced with usually publicly funded research dollars often um was kept on personal computers or university-owned computers or um you know or in drawers and nobody would pay attention or nobody would have access to it so the idea was that um you know we were spending all of this money to generate research data but only one person or one research group was able to benefit from it because that that publicly funded data was kept by that individual or by that University and not shared broadly whereas now we um have kind of developed the end the idea that you know if the public publicly funded dollars are paying for it then it should be a public good that anybody can use right and that's kind of part of what gave rise to this concept of fair data principles so um that's uh kind of been a a catalyst for this transition but then there's also then the realization that one data set can be analyzed in a number of different ways to provide different insights and different results whereas um for for example I might look at a data set and analyze it in one way and get one results about a specific thing that I'm very interested in but I could potentially give that data set to Dr Park who has a very different focus and depending on what the data set is I'm not saying this is going to be universally applicable but he might be able to look at that same data set and look at a different variable that I am not that interested in as a water resources engineer and he might analyze that that variable differently and come up with a different finding and so instead of you know me keeping this data set in my drawer or on my hard drive that only I have access to the fair data principles are trying to make this research data available um broadly so that everybody can if they're interested in Access and conduct their own research on this data so if this data can't be found freely and available online it cannot be accessed it does not interoperate and therefore it's unable to be reused this overall these conditions results and a huge financial loss for Global Research and then also it hinders scientific progress right and that's one of the things as technology is increasing rapidly the research needs to keep up with it so that we um you know can stay on the Forefront and so um even though we Now understand how important Fair data is only 28 percent of researchers are even aware of the fair data principles and try to incorporate them into their research so with this bootcamp you are going to be increasing that 28 of researchers overall over the years hopefully we bumped this up to to a higher number and we get more people on board with this concept so I know I mentioned it in an earlier lecture but what is fair fair stands for findable accessible interoperable and reusable so the um idea behind this is that we rely on um computers to do a lot to help us do a lot of our research and that if we are able to use these Fair data principles they can enable um computers to find access interoperate and reuse data with minimal or with either no or minimal human intervention and I'm not saying like this is an AI thing where we're going to suddenly not be doing research ourselves it just means that we can write the codes um in whatever computer language you are familiar with we use Python for this bootcamp but we can write codes to do the analysis that we want it to do and then we can let the computer run that code do that analysis and we can focus our energies and our efforts on something else um while that computer is doing all of that analysis and um this uh quote here is uh comes from Spider-Man if anyone is familiar with that uh similar to Spider-Man but it says with big data comes big responsibility so as a researcher um you might feel disconnected sometimes if you are sitting in your in your office in your lab um and you know there's no one really around but you are dealing with data and that data can enrich our understanding of the world and therefore you have a responsibility to um conduct your research in a fair way so why are fair principles required um as our world has becoming increasingly digitized we um are increasingly dealing with new challenges in this digital world one of these challenges is data and all of the data that we have generated um it is an asset research it is an asset and digital research data can be stored reused and repurposed like I said there are if we have two different eyes looking at a single data set you might see something different right and access to this data can facilitate knowledge Discovery and improves research transparency um and if we are able to share our data um then it can lead to more Innovations and more problem solving and again it avoids repetition it's not um you know the U.S um the National Science Foundation through um the US government is funding research on oh I don't know um uh I was gonna say like um cattle breeding habits or something like this and then you know then the um you know whatever the equivalent is of the National Science Foundation in um another country doesn't have to fund that same research if we can just share and if we're talking about you know similar species that have similar behaviors or or whatnot um then that these uh these datas can help the static and help everybody okay so we'll go through some some definitions that are relevant to Fair data principles first and foremost is um what is a repository with um we're talking about data management data storage we are often talking about a repository so a repository is a free online collection of documents um often scholarly that are citable and these um they're published in Ace in a way that allows them to be accessed by everybody and allows them to be found by everybody basically um and so there are a lot of different repositories available online so some are maintained by a single University such as um you know a lot of universities have um repositories that focus on using data or managing data for their own students and their own faculty but then there are a very large number of more General repositories that people use all over the world so for example you've probably heard of GitHub or zenodo so zenodo is a very common one worldwide this is just a picture of um what the the front page for a published um research data shows so this shows here a recent upload it tells you the date what version it is that it's open access and one that so has all of this um this information available to you and then you can download this data for your own use if you were interested in it so next we have some more definitions so um with Fair data we talk a lot about machine readable data so this is data that's in a format that can be easily processed by a computer without human intervention so in a lot of cases scans of texts are not machine readable but you can read you know a human can always read them right so what we're looking to do is put all of our data in a form that the computer can read the data right and one of the most the simplest forms of of that is a as a text file right so if we can convert for example a photograph into a text file then the computer can read it but what we want to do with all of our data is make it in a way that the computer can read it so there are two um two different groups of machine readable data one is human readable data that is marked up so that it can be also be read by machines such as HTML which is the code that is used for for basically building all of the websites on the internet um and then we also have data file formats that are intended principally for processing by machines for example um csvs comma separated file are comma separated values file format and there are a number of different data formats that are um and intended principally for processing by machines next we have persistent identifiers this is a really important um Concept in uh and published research published data um if you are conducting research or have conducted research you've probably heard about these in some sense so a persistent identifier is a long lasting reference to a document file web page or digital digital object it's something that is persistent is expected to essentially never change over a lifetime at least um and then similarly we have permalinks permalinks are URLs that are intended to remain the same limiting the amount of URL changes that can render objects unfindable so these links are um are short and easy for people to type and they uh need to be actively maintained in order to continually be cons uh persistent so the one that I think is probably most common for people to be familiar with is called a DOI or a digital object identifier and a DOI is a persistent unique digital identifier associated with an object which contains metadata that makes the object easier to find so dois are essentially a also a type of a permanent link to a data set or a published paper or anything that's published on the internet so it's really convenient if you have the the DOI for any type of published um work you can usually just pop that DOI right into for example Google and it'll find whatever you're looking for almost instantly so even if uh a journal changes Publishers or or anything the DUI is always going to remain the same and you'll always be able to find that data um that easily in that deal easily so here we have an example of a DOI so this link down at the bottom httpbs um doi.org so the DOI that they're actually talking about is this you can't see this um it's everything after the slash so after doi.org slash this 10.6069 that's the start of the DOI so the DOI is this entire last bit after the doi.org slash um and that's the the bit that you can um the piece that you can pop into any search engine and find what you are looking for okay next slide on um persistent identifiers there is a another um type of persistent identifier called a research organization registry so this is a unique identifier for every research organization in the world so I have a link here to the University of Texas at Arlington's RoR ID and so this our rorid is another persistent identifier for every research entity and it tells you if you click on it information about that research organization and this just increases transparency with different research organizations and then also allows a worldwide registry of you know the entities actually attempting to conduct research um this is also one you may be familiar with it's called an orc ID or an open researcher and contributor ID so the orc ID is essentially a persistent identifier for a human uh researcher right so I have an orc ID um Junaid has an orc ID Dr Forbes has an orc ID I would assume and this is sort of like your um research resume online that you have your orc ID everything that you publish um is connected to your orc ID so that anybody can find your entire body of work at any given time um and it's it's um increasingly being linked to all of your Publications that you would submit are asking for you to have an orc ID any questions um before I carry on on these different sort of basic definitions that we've gone through so far does anybody have an orc ID oh go ahead oh the research organization registry is for each researcher or it's foreign organization it's for an organization yes so um the university that you are at likely has in RoR ID the orc ID is for an individual so I see a few people um in the chat saying they don't have orc IDs so if you are um you know actively pursuing a career in research or are a researcher now I highly recommend um you consider signing up for an orc ID it's it's free and it's definitely sort of expected more and more these days I think um I kind of record something like that like um in Texas A M we have some kind of um user ID for students that a PhD students that do research that you can assess all the library and information um online yes I think uh we have something like that okay interesting it sounds like it's um maybe sort of like a researcher ID just for Texas A M system yeah yeah so this sum org ID is worldwide okay yeah yeah so it's um yeah it's like uh everyone all over the world can can participate in this but yeah it sounds um maybe similar but on a worldwide worldwide scale to what you're talking about oh okay yeah okay so let's carry on so more important definitions um so with all of our research we're working with data data is raw and unorganized facts that that are useless without proper processing and organizing into um some way to retrieve some information from YouTube future future use um there are all types of data some is very simple like a list of grocery items it says here that is also data but it can also be um a an observation of some phenomenon that's happening in nature even you know a list of stream flows that's data right and then also we have metadata listed here metadata is I always talk about it as data about data it shows all of the basic information about the data which makes the data easier to find and to work with so that you can fully understand what is going on with the data if you have a list of stream flows for example but you don't know that it's streamflow you don't know where that streamflow is um taken from you don't know the units of that Stream flow um it's kind of useless right it's just a list of numbers right so you need that metadata all of that data about that streamflow data in order to actually work with it and that's kind of what the idea behind metadata is and there are ways to create the metadata manually but they're also more ways increasingly ways to automate it to make it easier for people because it's um it is a task so this is a slide kind of just showing you about the flow of data from when you first get it to when you publish your article so you um you know first you're going to be generating your data and preparing your data files and then you might deposit it into a data repository and that data will be checked and curated by that that repository and they'll publish it for you it'll give you that DOI that anybody can find your your data set through that DOI um and then it's sort of parallel to the article flow writing an article where you're going to take your data that you um worked with to write an experimental article you'll submit that manuscript to the publisher that um article will be reviewed and then also published so it's a similar uh flow between publishing a data set to publishing an article they're complementary and increasingly I would say um journals are expecting you to publish your data set that you used or make freely available your data set that you used to conduct your research that is published in your your manuscript so that they can assess your your research findings and then also they can be duplicated by anybody that's interested in it and do in attempting to do that so um are there any questions about what we've talked about so far is the next section is to go into the details of the fair principles yes Juan Sebastian oh hi uh hello uh is there like a name that's to measure um like Fair principles of some organization or some country like yeah for saying in the U.S said the figure before like the 28 just the 20 percent of the researchers now about their principles but um yeah it's like an index to measure that um I am not aware of any index that would allow you to um assess the fairness of a data set um at this point it's I think kind of assessed on an individual um basis but that would be I think an interesting thing to be developed perhaps that can be uh one of your tasks as a researcher to publish a index for it because it would be an easy way yeah yeah to assess okay thanks yeah thanks uh Joel do you have a question no it's not okay all right so any other questions we should we carry on yeah all right so next we will go into the details of fair principles um and I I know this is going to be a lot um but don't worry we will you'll see it's it's a lot of words it's a lot of Concepts that are probably fairly new to you but that's the point of this boot camp is to introduce you to them and then give you an opportunity to learn them a more in a Hands-On way and work with them throughout the week so this is the introduction um but you will you'll learn how to make data more findable through the data access you'll learn how to make it um more accessible also partially through the data access and through our discussions on data management and Publishing data data usage licenses um you'll learn how to make it interoperable largely through the use of metadata and programming and then also reusable as well through more discussion on publishing an organization of data metadata and whatnot so I know this is um going to be maybe a little bit daunting but um by the end of the week you'll you'll kind of understand how it can be accomplished so first up is findable so findable means that the data is discoverable by both humans and machines so um what you have here the kind of the big bold points these are the main points that um according to the fair principles need to be accomplished in order for um the data to be considered findable so first the data would need to be assigned a persistent identifier so this is any number of um the persistent identifiers that we talked about previously but commonly a DOI and or a permalink which a DOI is a type of permalink so this just helps um to make sure that your data set's not lost essentially that can always be found and I'm an orc ID is a an example of a persistent identifier used in research for people for the researchers themselves so the data is searchable so the metadata and the data are searchable online which means that they are registered in a searchable resource so if I want to find your data set and I go to a search engine where I would expect to um have a link to that data set I can find it right the data are described with Rich metadata so this is providing enough information about the the metadata that both humans and computers can easily find and consume the data that I don't have to worry about what this data actually means where it came from how I can use it all that metadata is there and available for me um and that the the metadata is machine readable so that um it can be easily discovered and um and sort of ingested in the research process so to go into even more detail we have um the findable principles we have um this F stands for findable so the first one metadata are assigned globally unique and persistent identifiers so not only is your data set published online but your data set is accompanied by metadata that um people can find so one example here is an orc ID which I suppose we can go here um this is uh just a random orc ID page if you haven't seen this before but this is the persistent identifier for Eric Schultz um it gives a little biography of him that he um would have written himself it gives it an employment history and then down at the bottom education and then grants he's received these are all tied to his orc ID and then here is a list of 127 of his published works so these can be data and data sets and papers so this is what a an orc ID looks like a persistent identifier for a a person for a researcher so um F2 the second definable principle is that data is described with Rich metadata metadata can and should be generous and extensive including descriptive information about the context quality and condition or characteristics of the data Rich metadata implies that you should not presume that you know who will want to use your data or for what purpose so you're describing it as fully as possible the third findable point is that metadata clearly and explicitly includes the identifiers of the data they describe um so the metadata and the data set should be separate files in that the association between a metadata file and the data set is obvious thanks to the mention of the data sets permanent identifier in the metadata so that makes if you have the permanent identifier listed in the metadata that means there's always a link between the two and you can find them the fourth principle under findable is that metadata are registered or indexed in a searchable resource so identifiers enrich metadata descriptions alone will not ensure findability on the internet perfectly good data resources may go unused simply because no one knows they exist right so it is um just making sure that your metadata is also available in a searchable resource in addition to being on your data set being available so this is just an example of um a a student's project on a zenodo so it says a student's final year project to investigate the relationship between urbanization and extreme rainfall the student uses zanodo to look for similar Journal Publications and then this um a student can find a relevant Journal paper which includes the DOI which is listed here the publication date different versions indexing Etc you can also see all of this information and this data set here is index particular specifically in open air which provides integrated scientific information so this is a another publication a way of indexing Publications so before we carry on I have a question here about um the findable the F portion of the fair data principles so what qualifies qualities of identifiers do the fair fair uh principles recommend we have a a continue to operate indefinitely be unambiguously identified data and metadata and then C continue to operate for the foreseeable future so um which this is a select all type answer which of these do you think um applies to qualities of identifiers that the fair principles recommend any thoughts so um what qualities of identifiers do the fair principles recommend so these are the persistent identifiers that we talked about right so um continue to operate indefinitely um that would be nice but we and definitely is is a long time right so we don't have that um sort of ability to say that yes this this persistence identify although we call it that will persist indefinitely um because we can't necessarily know what's going to happen right um but then we have B unambiguously identified data and metadata that's um absolutely true right we want to be very clear that this is our data and it is connected to this metadata and they are fully described so that um you know everybody can use them and C we have continued to operate for the foreseeable future so yes that is also true here we want when we're talking about persistence it's um for as long as we can um you know possibly tell possibly C so that's kind of why I said maybe like a lifetime um a lifetime of of availability right so that um that's the type of persistence that we're talking about as opposed to you know indefinitely into the future forever and ever because obviously things things do change whether we um want them to or not in some cases especially when we're talking about um you know access to accessibility online Okay so next let's talk about accessible so um the accessible uh portion of the fair data principles is that all data should be made available to others humans and machines alike should be able to gain access to your data and one of the big points here is that not all data has to be made open right so it doesn't always Fair data doesn't always have to be freely available open to everybody all the time because there are um reasons why we might not want data to be freely open and that might be due to funding concerns that might be due to security concerns um and whatnot there's a number of reasons why we don't necessarily want everybody all over the world to access all the research data period um so but you can um have your data still be fair even if it is restricted for Access due to certain concerns so I'm in order for data to be accessible the metadata has to be retrievable um by machines and humans through a well-defined standardized protocol and the protocol is open free and universally universally implementable the metadata is also accessible so accessible means that the data are persisted in an appropriate storage um placed usually online and this does not mean that the data has to be available to everyone but there should be information about how to access the data if if you are one of the individuals that who should be who one of the individuals who should have access to the data so for example sensitive data should be properly marked with the pertinent sensitivity for example public confidential highly confidential Etc and a security level so that if you are interested in that data you might have the means to to gain access to it if you believe you should um and if the material contains sensitive personal data or special category data for example a confidentiality assessment needs to be made before the material can be released to anyone so we do have an interest in protecting personal data um and last point on this page is that metadata however are not sensitive so even if the data can cannot be made freely accessible you can use metadata to show that the material exists and under which conditions you may access and reuse it so the the data itself might be sensitive but the metadata is um still should be available so that people understand what is in the data so for the print accessible principles we have the first one is metadata are retrievable either identifier using a standardized communication protocol most univ sorry most users of the internet retrieve data by clicking on a link essentially this principle states that the fair data retrieval should be mediated without Specialized or proprietary tools or communication methods the data retrieval should be pretty straightforward that everybody um who is supposed to have access to the data would be able to access it without needing to pay for something extra special or do um or to ask for a sort of a third party to help them gain access to that data um the protocol is open free and universally universally implementable to maximize data reuse the protocol should be free and open sourced and thus globally implementable to facilitate data retrieval anyone with a computer and an internet connection can access at least the metadata the protocol allows for an authentication and authorization procedure where necessary it often makes sense to request users to create a user account for a repository this allows the repository or the the data owners to authenticate the contributor of each data set and to potentially set user-specific rights so this is kind of tying to the data usage licensing as well so this criteria will also affect your choice of the repository where you will share your data so some repositories are don't don't require you to create an account to access the data and if that's something that works for you and you are want to have your data freely available for anybody to access that might be an option or maybe you want to have a little bit more Security in front of your your data set where you ask um or you choose to deposit it into a repository that does require the creation of accounts um and then the last step here are the last uh the last principle listed here is that metadata should be accessible even when the data is no longer available so this idea is that the metadata is stored in a highly available database server which is separate to the data itself so in cases where the data is no longer able to be available the metadata would still be available and for example we've talked about zenodo a couple different times the metadata and the data will be retained for the lifetime of rep of the repository so as long as zenodo lasts your data your data will last Okay so as an example to find a relevant article on zenodo we will simply be using an internet connection and type the name so this is a a screenshot of the zenodo app where it says here we searched a monsoon rainfall data um and it's closed access you can see here you can see the publication however you cannot access the data um but this having this listed here it gives the idea that this research has been done even if we don't have access to it and then over here we have another picture of a uh a data set where it has restricted access and it tells you right under the data set description how you can gain access and it has it says you may request access to the files in this upload provided that you fulfill the conditions below um and so if you wanted to have access to this status that you could request access and convince essentially the owners that you um you are amongst the list of people who should have access to it okay so a question about accessibility so what is the value of having a landing page even after the data is no longer available so which of these two um do you think is the correct answer a to provide evidence that a particular line of research has been conducted or B to minimize updates to training materials I think any thoughts on this one a yes thank you there's a couple people who dropped in the chat that a yes although we do like to minimize updates to training materials as often as possible the primary value of um having landing pages for data sets and for metadata is just to show that the research has been done and that you know we can understand what's been done and maybe what's but what the potential is to carry on different lines of This research in the future or to use the findings from that research in our own research so yes a thank you all so next we have interoperable so interoperable means that the data can be exchanged and used across different applications and systems also in the future so for me this is the one that's a little bit um like the least obvious if you will so um in order for data to be interoperable data is not created with proprietary software meaning um you don't need to buy a license to or pay a fee in order to access this software with which the data was created um there it talks about metadata formats to make sure that the um the format of the metadata is sort of easy for people to understand using standard language standard nomenclature and sort of vocabularies that are common to the The Domain in which you're doing research to use open formats and software so it's using file formats that most people know how to open so PDFs csvs jpegs are all comment are all open source text files open source something like Excel which maybe a lot of us use is actually not technically open source right it's a Microsoft product that you need to have a license to access but csvs on the other hand um R opens open uh an open format so metadata have certified references so this is where your metadata includes references to references to other metadata where appropriate um so the main responsibility for making data interoperable um rests on the organization that makes the data accessible but it also means that data producers and consumers should use standardized ways to enter information such as dates time periods and Geographic coordinates and so on and so forth just to make sure that everything is sort of uniform that we can can understand how to work with it as best as possible as clearly as possible so we have a few interoperable principles to go through so the first one is that metadata uses a formal accessible shared and broadly applicable language for a knowledge representation so this can create an obvious issue when different languages are used to describe the data or when spelling errors make the comparison of descriptions and variable names more difficult so um whichever domain you are working in um or whatever location you are working in it's um you know a good idea to use the the common language of of scientific uh research or or um for the the place that you're conducting the research for essentially to make sure that they have um easy access to to understanding your metadata and then also in addition to not only you know talking about the language of speaking and writing but also to use the vocabularies that are are used um within your domain so just to talk about the Stream flow example like if I'm going to talk about streamflow I should probably use the word streamflow and not make up my own new terminology to describe Stream flow in my metadata right I want to make I want to use the words that most people will be able to understand what I'm talking about as much as possible um and then also to The Next Step next phase is to use vocabularies that follow the fair data principles so in this case make sure that the vocabulary you're using um is documented right um and that the documentation for that vocabulary is easily findable and accessible by anyone who uses the data set so there are different ways to ensure that this is done in some cases it's just um using whatever common words are used in your domain but in some um some domains they had actually created sort of like these controlled vocabularies to which you can look up and see like which terminology do they as a research domain want people to use um and that is actually it's sort of like a dictionary if you will a a domain specific dictionary so that is is available in some cases so the last step under interoperable is that metadata should include qualified references to other metadata scientists should clearly identify relationships between data sets in the metadata in the metadata for example by naming their persistent identifiers and describing their scientific link to each other so there's always the idea that research Builds on past research you know we're standing on the shoulders of giants etc etc so um you should include in your metadata a sort of description of what the the past um history of this data set is so for example this is a new version of this former work by so-and-so it's a supplement to this other work by so-and-so where it relates to this work uh by so and so so and so and you can create um you can include dois in this so that other people can then um go look at these other research results or products and maybe it will enrich their understanding of what you are talking about so um one of the ways that we can do this is through this is another zenodo example um you can uh when you publish in data repositories they keep usually a record of different versions so in this example um this data set has 150 versions already um and each version is accessible and you can see which all of these versions have been created and what uh what they look like how they've changed and whatnot and then um when you're talking about related identifiers also on oops this example is the nodo we see um that this is a continuation um this work was continued by this other work here and it's a supplement to this other work so it's just listing um kind of all the different pieces that go into your work so it creates a a Universal picture basically a complete picture so next we have a a short question about interoperable it's just uh to break it up a little bit so what can be done to make data more interoperable this is a select all that apply so we have a license it with a Creative Commons license b u standard vocabularies in data and metadata C put a persistent identifier on it D include clear instructions on how to obtain access in the metadata and E make the data self-describing so what do we think b d and e that's pretty close so um so B is definitely correct e is definitely correct um but the I think you're remembering yes we have a little bit of overlap one Sebastian's bringing in C into the discussion so um and we have an A so we haven't talked yet about licensing at all we will talk about that next um so D it says include clear instructions on how to obtain access in the metadata so D is not an interoperable um Point D is comes from our Fair our our accessible points so when we're talking about interoperability um obtaining access to the data set in the metadata that's an access issue not an interoperable issue um so for our correct answer here we want b c and e where we're going to use standard vocabularies so that everybody can kind of understand it we're going to put a persistent identifier um on it so that people can um uh the machines can find it essentially and then also we're going to um e make the data self-describing so that um you know again it kind of gets back to this a machine being able to understand what's going on here so thank you for um everybody who uh provided their input on this question so next we and last of the fair principles we have reusable so reusable means that the data are well documented and provide Rich information about the context of data creation so the ultimate goal of fair the fair data principles is to optimize the ReUse of data so that's what this principle is kind of bringing everything together to talk about so we have data and metadata are richly described with several accurate and relevant attributes this again is kind of getting to the metadata data and metadata are released with clear and accessible data usage licensing that's where we're talking gonna come into play talking about licensing data and metadata are associated with detailed provenance I.E that explains how why and who created and processed the data so that's what I was talking about earlier the kind of story of the data and then all data meets domain relevant Community standards so um to go through kind of quickly uh the reusable principles we have the first one metadata I richly described with a plurality of accurate and relevant attributes the metadatic creators should be as detailed as possible when adding metadata this can lead to the the provision of context-specific information that may first appear to be irrelevant um so this is when you're talking about for what purposes the data was created or collected and um kind of answering the questions about whether the data is raw or processed or both and also if you're if it is processed data you're talking about the uh the process that was undertaken next we have the metadata are released with a clear and accessible data usage licensing this will describe the legal conditions under which data may be used and it should be clearly defined both for machines and for humans this should be also represented very clear really in the metadata the license should be listed next metadata are associated with detailed provenance for the collection of provenance information researchers should clearly describe their role in the data generation workflow how they wish to be cited and who was involved they should also State whether the data set contains foreign data and um should also again go back going back to the human and machine readable issues to make sure that they can be understood by by all um lastly we have the metadata should meet the domain relevant Community standards so scientists should prepare their metadata according to their Community standards and best practices for data archiving and publication and then depending on the area of expertise several standards may have been established for your discipline so it's kind of just a matter of um talking to your your colleagues to see what they recommend using or looking around and seeing what is most common to be used in your in your domain so um this is an example of downloading temperature data set from the go satellite this is from a GitHub repository but here we have a description of the data so everyone can understand what it is it has a very clear indication of what the license is in this case it's an MIT license um and then it says exactly here how to cite the work right here's a suggested citation and a suggested acknowledgment which would go in into come into play if you were ever to use this for another purpose so next we have a question about making data reusable so how or what issues do you need to consider when you are preparing your own data for reuse this is another select all that apply so how things uh issues you need to consider how you will clearly indicate how others are allowed to use it which metadata standards and controlled vocabularies provide accurate and relevant information about the content and context of the research data the file formats which are prepared for reuse completeness of data documentation for future users and then e none of the above what do we think we have a c and d Okay so this is the only one you did not select is b c d a CD okay so it looks like we have a lot of agreement on um a c and d for the most part and then we have um so a is a little bit of questions about a so a is important because that's where it comes into play talking about data usage licensing so this is where we need to indicate how others will use it this is coming to the data usage licensing and then the which metadata standards and controlled vocabularies provide accurate and relevant information about the content and context of the research data this also um comes into play as well with uh reusability and just making sure that you are describing your data in a way that other people in your domain who are likely to reuse your data can also understand it so yes it is all of the above except for E of course that's a through D here in this case and then I think everybody understands um or understood that C and D were also um issues that needed to be considered okay so um this is just a a summary of how you can ensure that your data supports Fair data principles so when you're talking about data sets and files your data should be open should have a DOI it should be an open formats again something like a CSV a text file a JPEG and it should be discoverable through an open search protocol for example Google or any other search engine your metadata should include useful uh words from your your research domain it should include a machine readable standards where available um for example org IDs or other types of persistent identifiers it should provide a citation for the data so that others understand how you they can give credit and it should include or indicate any terms of use clearly I.E the data usage license so this is just a list of tips for preparing your data to make sure that it meets the fair data principles so when you're preparing your data files you should include raw or process data or both um depending on what's common for your discipline but if you are including that process data you need to explain how it was processed um your file format should be common and open you should organize all files logically according to your project to make them as clear as possible for people to understand you should describe the methods for documenting your data and files to describe the methods of data collection and file structures that's part of provenance reference articles that include orc IDs of all data contributors depositing your data into in a repository zip all your files into one package or data set so they're easy to to download a select a well-known data repository and upload your data which the repository you select might be dependent upon your domain there are some that are more commonly used for different types of of research areas or different research areas make sure the repository repository provides a doi to access and reuse the data that's a persistent identifier issue provide a license attribution for your data so users can easily copy and attribute your research data that you generated so how how complying with Fair helps um it's increasingly important to make data as Fair as possible because we are definitely increasingly living in a digital world these days um and if we employ the fair data principles you make the data more valuable by improving its findability through unique identifiers and allowing for easier combination and integration this allows us to develop a lot more enriched research and by making your data fair and accessible to other researchers you are improving transparency of your research and increasing the knowledge synthesis effort again integration of data Concepts um is really important for you know these kind of uh huge discoveries that we have yet to make so for the researchers because obviously making Fair data your data fair is a lot of work which is why some people are have shied away from it but as a researcher who Embraces Fair data principles you will be able to achieve the Maximum Impact from your research you'll increase the visibility of your research and the ability for people to cite your research by clearly giving them a suggestion for how to cite it you'll improve the reproducibility reproducibility and the reliability of your research you may be able to attract new partners Partnerships with other researchers and policy and broader communities by making your research freely available out there to find and for people to understand um and you may also be enabling new research questions to be answered through your work so I know we went a little bit over time but I will stick around for a few minutes if anybody has any questions but I I know that was a lot and um it'll be a lot to um to digest in such a short period of time but as I said this was supposed to be an introduction and hopefully over this week you'll kind of understand more and more how we can integrate these these Concepts into our research practices and make it um not so scary perhaps if you will because I know it's it's um a lot right at the first
