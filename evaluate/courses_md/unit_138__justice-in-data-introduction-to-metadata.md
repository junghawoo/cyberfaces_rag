---
title: "Justice in Data: Introduction to Metadata and Provenance"
unit_id: 138
course_id: 10
level: "Foundation"
slug: justice-in-data-introduction-to-metadata
is_course: 0
---

# Justice in Data: Introduction to Metadata and Provenance

## Extracted resources (local files)

### Introduction to Metadata and Provenance Recording
*Source file:* `CTW-metadata_FINAL.pdf`  ·  *type:* file

Introduction to 
Metadata 
and Provenance

Team Presentation
2
Sharma 
Chakravarthyame
Professor

Presentation Outline
●
What is metadata?
●
Why is it important?
●
Implication of not having metadata
●
What is provenance?
●
Where is it useful?
●
Meta data and FAIR principles
●
Conclusions

What is Metadata?

Not Just a question of 
Finding Data
●One may argue that with Google and other search 
tools available, why do we have to worry about how to 
find data
●But remember that 
“data ” was being collected and 
used even before the advent of Google and other 
search engines/tools
●Those tools may help you 
find some of the data
, but 
understanding them, figuring out where they came 
from (lineage or provenance), how trustworthy they are 
separate problems (not addressed by search)
●Also, even with those tools one may not  be able to 
locate data in the hidden web or part of a database
●Hence, metadata is needed 
5

Interesting 
(from gis.stackExchage.com
●
How do I extract metadata from Google Earth?
I downloaded the satellite image from Google Earth Pro.
The data I want to know is that the date, resolution, and the server from which the image was 
taken (as far as I know, there are Google Earth servers around the world, and the 
resolution provided by each server varies. Therefore, I would like to know which server 
the image I downloaded is from.)
●
I would like to know how to get the data for these images.
Answer:
Google does not provide "metadata" for the many images that get combined into its satellite 
view mosaics. But in Google Earth Pro, using a combination of the historical imagery tool, the 
image date reported in the status bar, and the copyright strings, you can usually figure out the 
date and provider of many images. That said, if the imagery is very high res (like the 15cm 
imagery in many cities), then it's probably aerial imagery, which is mosaiced from many photos 
over many dates, and does not provide useful imagery dates. To reduce the amount of that data 
shown, use the Historical Imagery tool, and turn off the "3D buildings" layer.
Without proper metadata, you need to resort to guesswork (may be educated guesswork)
6

Dat a Vs. Meta data
●Data is what one uses for their understanding, 
analysis,  and applying ML and other tools for 
deriving inferences
●Data is also used for visualization and 
presentation in different ways
●For example, using census data, you can obtain 
demographics information, income averages at 
different levels, density of population etc.
●However, given a census data such as
32, Private, 192965, HS -grad, 9, Separated, Sales, Not
-in -family, White, Female, 0, 0, 45, United
-
States, <=50K
○
How do you use it? Without additional explanation?
7

Dat a Vs. Meta da ta
●
As you can see, data by itself, is difficult or impossible to 
understand as to what they represent or mean
●
Not useful for any meaningful analysis!
●
Merely providing raw data is almost useless for everyone 
except for the person who generated it 
○
If it can be remembered
●
Given the size, ubiquity, and complexity of data available for 
use, there has to be some way to add additional information 
to understand, interpret, and use it meaningfully
●
Simply put, this is the 
role of metadata
!
○
“data about data
” or data that describes other data
●
The concept seems to have come from metadata  for library 
catalogs
8

Descriptive Meta
da ta
●Certainly, metadata is useful for humans who will be 
using the data for analysis or any other purpose
●For example, the description of fields for the above census 
data will help humans understand it.
workclass:
P rivate , Se lf-e m p -n ot-in c, Se lf-e m p -in c, Fe d e ral-g ov, Local-g ov, State -g ov, W ith ou t-p ay, Ne ve r-
worke d .
fnlwgt:
con tin u ou s.
education: 
Bach e lors, Som e -colle g e , 11th , HS-g rad , P rof-sch ool, Assoc-acd m , Assoc-voc, 9th , 7th -8th , 12th , 
Maste rs, 1st-4 th , 10 th , Doctorate , 5th -6th , P re sch ool.
education
-num: con tin u ou s.
marital -status: Marrie d -civ-sp ou se , Divorce d , Ne ve r-m arrie d , Se p arate d , W id owe d , Marrie d -sp ou se -ab se n t, 
Marrie d -AF-sp ou se .
Occupation:
Te ch -su p p ort, Craft-re p air, Oth e r-se rvice , Sale s, Exe c-m an ag e rial, P rof-sp e cialty, Han d le rs-
cle an e rs, Mach in e -op -in sp ct, Ad m -cle rical, Farm in g -fish in g , Tran sp ort-m ovin g , P riv-h ou se -se rv, P rote ctive -
se rv, Arm e d -Force s.
relationship:
W ife , Own -ch ild , Hu sb an d , Not-in -fam ily, Oth e r-re lative , Un m arrie d .
race: W h ite , Asian -P ac-Islan d e r, Am e r-In d ian -Eskim o, Oth e r, Black.
sex: Fe m ale , Male .
capital -gain: con tin u ou s.
capital -loss: con tin u ou s
…
9

Metadata Definition  (fgdc.gov)
●Metadata is
information about data. Similar to a library 
catalog record, metadata records document the who, what, 
when, where, how, and why of a data resource. 
●Geospatial metadata describes maps, Geographic 
Information Systems (GIS) files, imagery, and other location
-
based data resources.
●Example: creation date of the GIS data, GIS data author, 
contact information, source agency, map projection and 
coordinate system, scale, error, explanation of symbology 
and attributes, data dictionary, data restrictions, and 
licensing.
○A lot of structural metadata comes with gmail (hidden)
■Machine generated
10

Metadata Definition  (NIST)
●Information describing the characteristics of data 
including, for example, structural metadata 
describing data structures (e.g., data format, 
syntax, and semantics) and descriptive metadata 
describing data contents
●Metadata are also data. They are pieces of information that 
have dome meaning in relation to another piece of 
information. They can be created, managed, stored, and 
preserved like any other data
11

Metadata 
●Metadata can be applied to anything
○A computer file can be described in the same way 
that a book or piece of art can be described. For 
example, both can have a title, an author, and a year 
created.
Metadata should be documented for 
research outputs of any kind
●Metadata generally has little value on their own
○Metadata adds value to other information, but are 
usually not
valuable in themselves. There are 
exceptions to this rule, such as text transcription of 
an audio file
12

Types of  Metadata 
●Descriptive metadata
○consist of information about the content 
and context of your data.
○Examples: title, creator, subject keywords, 
and description (abstract)
●Structural metadata
○describe the physical structure of 
compound data.
○Examples: camera used, aperture, exposure, 
file format, and relation to other data or files
13

Types of  Metadata 
●Administrative metadata
○are information used to manage your data.
○Examples: when and how they were 
created, who can access them, software 
required to use them, and copyright 
permissions
14

Recommended Minimum Metadata elements 
●
The following are recommended as a minimum set of metadata 
elements. It is important to select a metadata standard or schema 
appropriate to your discipline and/or repository and consult that 
schema for complete information on each element. You may choose 
to use more elements based on the needs of your project, the 
expectations of your discipline, and/or the requirements of your 
repository
Title/Name
– Nam e g ive n to th e re sou rce .
Description
– A d e scrip tion of th e re sou rce an d its sp atial, te m p oral or su b je ct cove rag e .
Format
– File form at, p h ysical m e d iu m , d im e n sion s or file size of th e re sou rce , an d /or h ard ware an d 
software n e e d e d to acce ss th e d ata.
Metadata
– De scrip tion of th e m e tad ata to b e p rovid e d alon g with th e g e n e rate d d ata an d a 
d iscu ssion of th e m e tad ata stan d ard s u se d , in clu d in g th e ve rsion of th e sch e m a an d wh e re th e 
sch e m a can b e fou n d .
Identifier
– A u n iq u e id e n tification cod e , su ch as a Dig ital Ob je ct Id e n tifie r (DOI), assig n e d to th e 
re sou rce , u su ally g e n e rate d b y th e re p ository.
Rights Holder
– Th e e n titie s or p e rson s wh o h old th e rig h ts to th e d ata.
Rights – In form ation ab ou t th e rig h ts h e ld in an d ove r th e re sou rce .
Contact Information
– Id e n tity of, an d m e an s to com m u n icate with , th e p e rson s or e n titie s 
associate d with th e d ata.
15

Complete Metadata
●Without going into details, metadata can be categorized 
based on the function it serves in information management
○
Administrative metadata
○
Descriptive metadata
○
Legal metadata (includes licensing)
○
Preservation metadata
○
Process metadata
○
Provenance metadata
○
Reference metadata
○
Statistical metadata
○
Structural metadata
○
Use metadata
16

Metadata Standards and Schema
●
In order to be useful, metadata needs to be
standardized
○
Th is in clu d e s ag re e in g on lan g u ag e , sp e llin g , d ate form at, e tc. 
○
If n o stan d ard is u se d , it can b e ve ry d ifficu lt to com p are d ata 
se ts.
●
A ke y com p on e n t of m e tad ata is th e schema
○
Me tad ata sch e m a ou tlin e th e ove rall stru ctu re for th e 
m e tad ata
○
A m e tad ata sch e m e d e scrib e s h ow th e m e tad ata is se t u p , 
an d u su ally ad d re sse s stan d ard s for com m on com p on e n ts of 
m e tad ata like d ate s, n am e s, an d p lace s 
○
Th e re are also d iscip lin e -sp e cific sch e m as u se d to ad d re ss 
sp e cial e le m e n ts sp e cific to or n e e d e d b y a g ive n d iscip lin e
17

Metadata Standards and Schema
●
Dublin core  
○
used by libraries; can be adapted to other disciplines
●
MODS (metadata Object Description Schema)
○
Richer than Dublin core
●
Darwin Core
○
Used for describing biological specimens
●
NASA’s Standards
○
NASA has a variety of data format and metadata standards, as 
well as "heritage" standards that were in use by NASA Earth 
Science Data Systems (ESDS) prior to the start of the legacy 
ESDS Standards Process Group (SPG)
●
FGDC (Fe d e ral Ge og rap h ic Data Com m itte e )
○
Th is sch e m a is for g e osp atial d ata. 
○
You will le arn ab ou t tools for cre atin g th is
18

Meta data for consumption
●What if a non -human (e.g., computer) wants to use 
the metadata and perform some operations or 
analysis on data based on it?
○The format that is good for humans may not be 
appropriate for non
-humans!
●Hence, there is also need for metadata that can be 
used/consumed by computers
○RDF (Resource Description Format) is one of them
○RDF specifies triples with resources in subject and 
object fields (can be url
’s)
○Has been used for taxonomy and extensively in 
semantic web (web 2.0 and web 3.0)
19

Metadata 
●RDF (Resources Data Framework) from W3C
+
is a standard model for data interchange on the 
web
+
Other technologies, such as OWL (Web Ontology 
Language), build on RDF and provide language for 
defining structured, web
-based ontologies which 
enable richer integration and interoperability 
of 
data among descriptive communities
+ search engines can use the information available 
to 
make search more focused
+
RDF can be used to integrate data from multiple 
sources
20

Metadata 
●RDF (Resources Data Framework) from W3C.org/RDF/
+
Can be used to build labeled directed graphs
+
is domain -independent
●Can also think of meta metadata! 
●Similar to higher order logics!
●Meta data can be generated manually or thorough 
automation
○
Manual creation increases accuracy and can provide better 
description as compared to automated which may  
generate basic information such a file size, extension, 
creation date etc.
○
AmazonTurk is often used for manually generating various 
types of metadata
21

Metadata 
●RDF (Resources Data Framework) from W3C
+ originally designed as a data model for metadata 
(representing information about resources in web)
+ commonly used for description and exchange of 
graph data
+ consists of triples: (each can be a url)
subject or source, relationship,  object or target
+ SPARQL (similar to SQL) is the query language
+ triples can be combined to form a knowledge 
graph
-
Has a large footprint
22

Metadata  
●While metadata provides unique
contextual information 
about a set of data
, it d oe s n ot, strictly sp e akin g , p rovid e 
con te n t ab ou t th at d ata. 
●Me tad ata can te ll you wh e n a m e ssag e was se n t, b u t it 
won ’t te ll you th e actu al te xt of th e m e ssag e . 
●Sim ilarly, m e tad ata can te ll you wh e re a p ictu re was take n , 
b u t it won ’t le t you se e th e actu al p ictu re . (Of cou rse , a lot of 
valu ab le in form ation can still b e u n cove re d from m e tad ata.)
●Ou r in te re st is to u se m e tad ata to fin d , acce ss, an d 
u n d e rstan d d ata th at we u se for variou s p u rp ose s.
○
In te rop e rab ility an d re u sab ility can b e m ad e p ossib le with 
ap p rop riate m e tad ata
○
To su p p ort FAIR p rin cip als
23

Metadata Uses  
●Metadata are used for 
○enabling data discovery, 
○understanding data, 
○analysis and synthesis, 
○maintaining longevity of
data, 
○tracking the progress of a research project, and 
○demonstrating the return on investment for 
research at an institution.
24

FGDC-CSDGM Standard  
(usgs.gov)
●
Examples of metadata records in FGDC
-CSDGM for different types 
of information products. View the metadata record in its native 
XML code or with a stylesheet applied to be easier to read.
○
Biological data with taxonomy (Biological Data Profile) 
[XML][Stylesheet ]
○
Geospatial data [ XML][Stylesheet ]
○
Tabular non -spatial data [ XML][Stylesheet ]
○
Project level [ XML] [Stylesheet ]
○
Systems Level Applications or Collections
[XML]
○
Aerial Photography describing this
image [XML]
○
Water Sampling Site [
XML]
○
Database [XML][Stylesheet ]
○
Models [ Stylesheet ]
25

Data Provenance
●Also termed “data lineage ” (think of ancestry.com 
for data and metadata)
●Refers to a record trail that accounts for the origin of a 
piece of data (in a document, database, or repository) 
together with an explanation of how and why it got to 
the present place
●Word documents carry some provenance information 
as part of its property including versions
●Sometimes referred to as 5 Ws (who, why, what, 
where, and when)
●Provenance is an important issue for scientific data 
where it is central to the validation of data
26

Importance of Data Provenance
●Data traceability lets investigators see how 
information has evolved over time
●Very important in many contexts
○Health care
○USGS data as well (remember the wrong place was 
bombed in Yugoslavia in 1999 because updates were 
not performed in a database or no one looked at the 
data provenance!)
●Traceability and trustworthiness
depends on data 
provenance
○E.g., clinical trial data is more trustworthy if the trial is 
large, replicable, randomized, and controlled
27

Metadata Synergy with FAIR Principle    
(roadtofair.hypotheses.org)
F 1: (meta)data are assigned 
globally unique and
persistent
identifier
○u rl, orcid -id , DOI n u m b e r, …
F 2: Data are d e scrib e d with rich m e tad ata
○“In trin sic:” (au tom atically g e n e rate d ) an d 
“con te xtu al” m e tad ata (e .g ., p rotocol u se d )
F 3: Me tad ata cle arly an d e xp licitly in clu d e th e id e n tifie r 
of th e d ata th e y d e scrib e
○As th e y are se p arate file s
F 4 : Me tad ata are re g iste re d or in d e xe d in a se arch ab le 
re sou rce
○For fin d ab ility!
28

Effect of FAIR Principle on Metadata     
(roadtofair.hypotheses.org)
A 1: (meta)data are retrievable by their identifier 
using a 
standardized communications protocol
○Use of h ttp (s) or ftp 
A 1.1: Th e p rotocol is op e n , fre e , an d u n ive rsally 
im p le m e n tab le
○HTTP , FTP , SMTP (n on -p rop rie tary)
A 1.2: Th e p rotocol allows for an au th e n tication an d 
au th orization p roce d u re , wh e re n e ce ssary
○HMAC au th e n tication , HTTP S, FTP S
A 2: Me tad ata is acce ssib le e ve n wh e n th e d ata are n o 
lon g e r availab le
○Me tad ata h as its own valu e !
29

Effect of FAIR Principle on Metadata     
(roadtofair.hypotheses.org)
I 1: (Meta)data use a formal, 
accessible, shared, and 
broadly applicable language 
for knowledge 
representation.
○RDF, OW L, DAML+OIL, JSON
I 2: (Me ta)d ata u se vocab u larie s th at follow FAIR 
p rin cip le s
○Use con trolle d vocab u lary
I 3: (Me ta)d ata in clu d e q u alifie d re fe re n ce s to oth e r 
(m e ta)d ata
○Cross-re fe re n ce s. Data se t d e p e n d e n cie s
30

Effect of FAIR Principle on Metadata     
(roadtofair.hypotheses.org)
R 1: (Meta)data are richly described with a 
plurality of 
accurate and relevant attributes
○Mach in e or h u m an d e cid ab le u se fu ln e ss con te xt 
R 1.1: (Me ta)d ata are re le ase d with a cle ar an d acce ssib le 
d ata u sag e lice n se
○Th is can b e vie we d as “le g al” in te rop e rab ility
R 1.2: (Me ta)d ata are associate d with d e taile d 
p rove n an ce
○Cle ar story of orig in /h istory as p art of m e tad ata
R 1.3: (Me ta)d ata m e e t d om ain -re le van t com m u n ity 
stan d ard s
○Be st p ractice s or sp e cific stan d ard s u se d for m e tad ata
31

Metadata, a Pillar of FAIR 
●Along with unique and persistent identifiers, 
metadata is considered the cornerstone of the FAIR 
principles, guiding scientific data management and 
stewardship
●Challenges
○Produce richly described metadata (metadata 
authoring)
○Evaluating digital object FAIRness levels (FAIR 
assessment)
●Some of this will be discussed in the next module
32

In Contrast 
●A lot of data and data sets we (computer science 
researchers) use do not follow FAIR principles (at all)
●As for as I know, metadata guidelines do not exist in the 
same way as it is available for USGS data
●I am not sure what the reasons are
●Most of our data set search is using google with keywords 
and going to known repositories that have collected large 
number of data sets
○
Data sets can be uploaded or submitted by users
○
They are maintained by universities or other groups
33

Repositories  
●My Google search using 
“CS data set repositories
” produced
This is a list of repositories where researchers can find 
and submit computer science data and source code.
○GitHub. GitHub is a code hosting platform for 
version control and collaboration. ...
○Kaggle. ...
○Google Code Project hosting. ...
○Launchpad. ...
○SourceForge. ...
○UCI Machine Learning Repository.
●Apr 5, 2023
34

Repositories  
●What is CS repository?
○A repository, or repo, is computer storage for 
maintaining data or software packages. 
○This location contains files, databases, or information 
organized for quick access over a network or directly.
●Other known repositories
○SNAP Stanford Large Network Dataset Collection
○https://snap.stanford.edu/data/
35

A Sample  
36
Name
Type
Nodes
Edges
Description
email-EuAll
Directed
265,214
420,045
Email network from a 
EU research 
institution
email-Enron
Undirected
36,692
183,831
Email communication 
network from Enron
wiki-Talk
Directed
2,394,385
5,021,410
Wikipedia talk 
(communication) 
network
comm-f2f-Resistance
Weighted, Directed, 
Temporal
451
3,126,993
Dynamic face-to-face 
interaction network 
between group of 
people
Communication networks

Another Sample  
37
Name
Type
Nodes
Edges
Description
amazon0302
Directed
262,111
1,234,877
Amazon product co-purchasing 
network from March 2 2003
amazon0312
Directed
400,727
3,200,440
Amazon product co-purchasing 
network from March 12 2003
amazon0505
Directed
410,236
3,356,824
Amazon product co-purchasing 
network from May 5 2003
amazon0601
Directed
403,394
3,387,388
Amazon product co-purchasing 
network from June 1 2003
amazon-meta
Metadata
548,552
1,788,725
Amazon product metadata: product 
info and all reviews on around 
548,552 products.
Product co-purchasing networks

Summary  
●Efforts in creating metadata using guidelines along with 
FAIR principles go a long way in the access and meaningful 
use of available data
●When the data sets are very large and complex, this 
becomes even more important
●It is important to pay attention to both metadata creation 
as well as whether they conform to FAIR principles
●You will be learning more about metadata creation and 
tools available for that in the next module
●Data provenance is critical for many applications
38

Thanks!
Any questions?
39

## Fetched resources (external URLs)

### Introduction to Metadata and Provenance Pre-Survey (link)
*URL:* https://utaedu.questionpro.com/a/TakeSurvey?tt=U8wDUycttYAECHrPeIW9eQ%3D%3D

[survey link — skipped]

### Introduction to Metadata and Provenance Recording (link)
*URL:* https://www.youtube.com/watch?v=l1AxKlE-Jk8

[YouTube transcript l1AxKlE-Jk8]
okay so this is uh the topic before we break for lunch and I think in the afternoon you will learn more about how to create this what are the different tools that are available for creating metadata environments in your domain and so so I'm going to sort of introduce the basic idea of what method is why it is important to accountancies so here is the uh list of what we are going to look at briefly and also look at you know the connection between metadata and fair principles okay so what is metadata I think by now you already know that you've used that if you have been using that so to me it is not just a question of finding data so one mask you know we have Google and other research tools available search tools why do we have to worry about data that's really one aspect but this is an actual question for the current generation who have grown up after the Google was born or don't know much about what was then important but remember that data was being collected and used even before they are going to Google and other search engines and tools so you know that's important to find the data if not as easily as you can today those tools may help you find some of the metadata but understanding them figuring out where they came from lineage or provenance for trustworthy they are that that's very important in many domains or separate problems not addressable search such throws upon it may throw up a lot of data I mean one fashion I tell my students say searching this poor but you need to be able to filter or discriminate what you get out of search not everything that comes up is the leveling are meaningful tissue near gasket cabin also even with those tools one may not be able to locate data in the hidden part or part of the databases that are not visible so that's one of the reasons why we need a better uniform mechanism not only to locate data but understanding it continuously so here is an interesting exchange they found which sort of sheds some light on the need for metadata why we are so preoccupied with metadata because it takes a lot of effort but someone could put all that information that someone needs to use it so here is saying exchange how do we extract metadata from Google Earth this is from your domain I downloaded recycle image from Google Earth Pro I want to know big resolution server from which they made the second uh as far as I know Google has server so in the world and the resolution provide those are very therefore I like to know some information so which meant that you know this information was not really available when the search and used the one one of the answers that was given part of this is the following Google does not provide metadata for many images that get combined into speculate views our message but in the Google Earth Pro using a combination of historical Matrix to the image date reported in the status bar and the copyright exchange you can usually figure out the date and provider that said if the measuring is for the hyper solution so suddenly there is a need because without proper metadata what you're doing is some kind of question maybe educator guess what you have to know how to do that without that information the verified production we posted it means that information is not available quantifies the need for why metadata it's important where it should be available so date of assessment data so data is what we use for understanding analysis and applying the analysis we're going to do with a CIA machine learning or anything else for deriving influencers or for visualization or whatever you're trying to do data is also used for visualization and presentation for example using the sensor data example that we had you can obtain demographics information but if you are given just a piece of data such as this one how do you use it without any additional explanation or information so that is where data itself is many terms useless unless you know what the data is and and you can figure out what it is when you move it so this is a real problem and at the end I'll show you some examples of how computer science people manage not as good as you guys to have a very very strict way of doing things so oops so as you can see data by itself is difficult and impossible to understand not useful for analysis nearly converting the data is almost useless for everyone except the person who can make it it and even that person has to do whether it falls if they are generating another 15 minutes given the size ubiquity and complexity of data available to the news there has to be some way to add additional information to understand The Interpreter music and that's where the role of metadata comes in so simply for this is the role of motor data which essentially is data network data or data that describes other data so the concept seems to have come from not it's not new it comes from library catalogs so it always existed even before computers and one of the issues they face of the same thing they have a lot of information that they did not know how to find searching everything so Library Capital Access created as metadata and I'll be the best multiplication I think so so the notion of metadata and the need for metadata is not just because you have Digital Data this is applicable to non-digital data as well which is so suddenly metadata is useful for a few months we'll be using the data for analysis or any of the process for example once you have the description of the Census Data you know how to use it so here is what we showed this is perhaps a very simple minimal rate of disappointment does not show any lineage and will show any prominence uh does not show Russians and other things who collected it when it was perfect so here is a definition of metadata from your similarities metadata is information about data similar to a library catalog record metadata records document that helps document who what when where someone's life after data features geospatial metadata describes Maps geographic information systems files Imaging and other location-based data sources creation date of the GS data is an example of JS data contact information Source agency not conviction coordination system you scale error explanation of symbology all of these are important for someone in that domain to understand what was related represents but that is the the more complex the domain is the metadatically a lot of structural metadata comes with Gmail so method is not unique to us.js so it's one everything we do when you send a Gmail for example if you go to Gmail you can look at the metadata that is generated for every email that is sent to you this is mainly machine generated so essentially it contains you know IP addresses date storms and various other than how many how many nodes it made and hospital to read the destination I think so but all of them are useful information for somebody who wants to go following six for example with Gmail this is very useful in a lot of criminal cases where they want to detect the lineage of the Gmail very opportunity where it can both came for for other data sets the purpose is different list which is another agency which which is a national instrument standards has a similar definition information describing the transcript of data including structural metadata and the saving data structures data formats syntax semantics and descriptive metadata they're being so some of the definitely there is agreement on the definition of documented data is metadata is also big so if material data is not something unique or different uh it is a it is Data but the intent and purpose of the data is slightly different from the data itself the pieces of information that I've done that have some meaning in relation to another piece of information they can be creative Minister and preserve it so metadata can be applied to anything so any piece of information any piece of data even physical entities can form metadata so a computer file can be described in the same way that a book or a piece of art can be linked for example both can have a title after the year metadata should be documented by the search of website so even the output that you do from the analysis is in the form of data and if somebody wants to understand the data of this has to be some information about data instrumented metadata typically has little very little value on their own but not always the case metadata adds value to other pieces of information that are usually not valuable in themselves there are exceptions of course such as text transcription of an audio file even though this is seen as metadata this is critical to understand the direct search ing somewhere so you can have metadata or a painting so whenever there is an option by one of the things painted so there is a a lineage and trustworldiness of whether this is the correct thing comes from the source it is described so there is there are different types of metadata descriptive metadata consists of information about the content and context of your data title creative subject keywords and description structural metadata describe the physical structure exposure 5.9 connection to other beta calls I mean these are just examples there is also in the literature it's the administrative metadata or information used to manage your operator when and how they will create a who can access them software required to use them in copyright permissions for example this can also be used for performance so here is a sort of recommended list of minimum metadata in the means that through the company any piece of data so the following are recommended as a minimized set of metadata elements it's important to select a metadata standard or schema appropriate to your discipline and Repository and conserve that scheme after complete information on each and you may choose to use more elements based on the need of your project the expectations that we are displaying so this is very important I know it is somewhat difficult to enforce this and some of the repositories may do that if they may not let you upload data into the repository unless you fill in the appropriate forms of metadata associated with it and in an application so that is certainly enforceable to some extent but may not be always writer name name given to the resource description format file format is very important because there's the the extensions of the file format many times are used to understand the type of file Market contains in the format in which it is stored and if you don't use a consistent extension then it can lead to inconsistent metadata description can be provided along with the converted data and registration of the metadata strong is used including the version of the schema and variable Kingdom identifier so this is a unique persistent identifier such as DOI or Arc ID these have been discussed earlier assigned to the resource usually generated by the repository rights folder the increase of persons hold the rest of the datum is important because sometimes they ask you to cite in a specific way when you use the information from that Source provides information about the rights held in and over the resource contact information so this is kind of a minimal requirement here or more detail complete list of metadata that can be associated with the piece of data I won't go into the details of this but we can see that metadata can be categorized has been categorized into on the function itself in Information Management administrative metadata the one I have tried to highlight and green are the ones that I think should be minimally given as product material descriptive material legal Navigator prominent structural metadata use metadata these are very important each one of them I'm sure there is a one armor of strangers associated with how to give it but what kind of paper they should also be templates associated with that using which you can create this metadata and submit it to the system better data standards and scheme so we saw the concept of schema when when we talked about less ingredients so keep my schema is nothing but a or my prescription just like we had a automatic description for a cable you also can have a format description for metadata so in order to be useful metal data needs to be standardized so we see standardization comes in not only just for applications but I think you know data itself and this insurance agreeing on a language spelling terminology date format if no standard is used it can be very difficult to compare a different data search the key company of metadata is the schema material schema outline that there are structured by the data and methods can discuss how the metadata is set up and usually addresses standard extra common components of metadata like waves names and places and deployments there are also discipline specific schemas used to address special elements so certainly uh it is not the same metadata that needs to be given for every piece of data in a in a gene domain with some kind of information biological domain it may be different in computer science I will show you a little bit later it is somewhat different so here are some standards that I've solved that are used that already available so this is an old one you know just a completeness doubling code seems to be a standard used by libraries that means this is a a enriched advice W4 so that will call as I said used for disturbing biological specimens and very intent maybe strategic distance from usds and you know where interests us are standards there's also variety of data formats that it uses perhaps it and then if EDC has its owned from whiskey noise for geospatial data we will learn about tools for creating that the optimal so certainly this is your you want to focus on so who consumes metadata so the important thing many times understand is not just the humans just like data is maybe you know visualized understood but consumed for analysis metadata can also be done in the same way so what if a human what is the non-permanent wants to use the metadata and perform some operations around us the format that is good for management may not be appropriate so this is an important issue that comes up because we want to use automation uh computation as much as possibly do that we can do things on manual offense there's also need for metadata that can be used understood the consumed by computers and rdf was specifically proposed known as the research description format is one of them rdf specifies strippers with resources in subject and object they can be here also this is used for describing resources where you can find additional information has been used for taxonomy very widely and extensively it is also used in semantic learning at 2.0 under three points so this is quite commonly used in many from the science applications that deal with semantically audio is a standard model for data interchange on the web other Technologies such as owing based on rdf and provide language for defining structures web-based ontologies which enabled virtual integration and interactive ability of data I don't know whether rdf is popular in your domain on your make sure but that is something that that is available is widely used search engine can use the information available to make such you know focused rdf can be used to integrate data from multiple sources rdf can be used to build what we call label detected graph so it's a triple which essentially describes run edge with the source node and the destination mode and the properties of the social destinations including the edge in terms of labels or resources where additional information is capable so is domain independent so it can be used in Unity Bank can also think of metadata for metadata so similar to we have this higher order Logics we have in promotional logic first order logic secondary logical logic and that is very similar to um data metadata meta metadators and sugar so metadata can be generated either manually or through application and the difference is manual creation increases accuracy and can provide better description so automated generation typically cannot provide description but provide other components as compared to automated means which may generate information such as file size extension creation date version number Etc which are useful but they are not the same as the description I'm not sure how many of you might have heard of something called the Amazon character this is something we use for other research very often so if we want something to be annotated manually and we want to do it for large amounts of data using expertise from the cloud so kind of that's also think you can use something on a Samsung Tab this is available Amazon so you can you can upload this information and you can invite people to do this on location you can pay them you can say you know for each question answered we'll pay you 10 cents and then we can also put certain qualifications that we should have in our budget so that not everyone comes and does it and also will limit the amount of things they do this is very widely used in manually allocating what we call fake news there's plenty of them these days going around so there's a lot of research going on what news is fake and what news is not fake but the ground Truth for that is extremely difficult to understand the whole thing what is true so that's where we use manual annotation and manual schemes using on a long tripod designed as a data model for metadata representing information about resources anymore commonly used for description in the exchange of graph data because triples they express grabs one exact time I'm using that you can build an entire level set so vacancies of triples and some of them can be girls or the user languages language that is developed called Sparkle which is similar to SQL as the 3D language to pretty or audience triples can be combined to form another job so I don't know if you are familiar with the notion of acknowledge graph is is quite widely used so this is the general graph which control in general information this was available earlier as a free thing I think Google docket at some point time they use it for the research so they use it for their search for example they create this knowledge graph from Wikipedia using information in the Wikipedia they can identify entities and relationships and other things on constructive cloud and then use this club so that's why that's one of the reasons perhaps why Google search is so much better than other search engines that we see today and it uses a lot of different kinds of information increases together while metadata provides unique contextual information about a set of data it does not strictly speaking provide content so metadata does not contain the content it is the data above the control metadata can tell you when a message was sent but it won't tell you what the actual message is so metal it is still very useful for various purposes where privacy is involved where you don't look at the message but you can look at them actually similarly metadata can tell you where a picture was taken but it won't let you see the actual picture of course a lot of valuable can serve them power interest is to use metadata to find access and understand data that we use for business purposes interoperability reusability can be made possible with copyright metadata and to support principles so the uses of metadata are typically enabling data Discovery understanding data doing analysis on synthesis maintaining longevity of data tracking the progress of research project and demonstrating the return on investments for research I think in institution lineage and various trustworthiness of the data so these are the various universities so here also I just put this so that so here are some standards that I took from USPS that will show you different type of standards and we support XML support that is available for that that we discussed earlier so for example if you click on if I click on this XML you will see the x amount of fund so this is what I'm here to show you earlier which is not very human friendly but if I click on the strike sheet the same information is shown what contained in the external I showed you in a human readable initially appealing form so this is the piece of information that it contains so you can see here the metadata that is associated that is stored as an XML file that can be processed by an application or a piece of software but that can also be visualized by the human and understand what it's about so that that is the that is the importance of using something like XML or Json so maximally is popular because it has no excessiveness you can express hierarchiven from geospatial data let me just show you one um so here is an example of mineral resource data of where we use biological survey the other wall and here is the metadata associated with that which is pretty long you can see this metadata is very extensive I don't know how much time on the effect it takes for new people to digest this for doing the analysis but there is extensive metadata that's available similarly for any of these formats or public scene let me see what it looks like um geochemical database from ionic cell popular service as the information as well so so this is how I guess you may be using some of this in the upcoming form creating these metadata so coming to data performance best way I can try to make you understand this is thinkable ancestry.com so that's what it is so data lineage is trying to identify the lineage of the data and how it has come to this point and where it started so that that is the whole point of that so get your opponents or lineage is the decremental finding something Romance the first year record trade that accounts for the origin of the piece of data in the document database that are translated together with an explanation with file and Y we talk in the Philippines Word documents carry some so if you look at the word documents going into the properties for example there is some metadata associated with every document in spreadsheets have some information even the X-ray and the MRI you take have some metadata associated with it which machine to create what kind of resolution all this is not visible to everyone but it is available Word documents carry that sometimes referred to as find them useful why what wave and when prominence is an important issue for scientific data where it is simpler to the validation of the result so you cannot validate yourself for crystallographing without understanding where these data volcanated and how that makes you understand whether the data is legit or not certainly agency like CIA has a lot of difficulty with lineage data because it's very difficult and they have to make so this notion of confidence that is associated with data in human income or data um Dr Sharma I just wanted to let you know it's about eight minutes nine minutes now past 12 30. oh I I thought I was going to patrol 45 now oh is it 12 40 okay yeah we can we can do that too no use it I I'm not sure I I might have missed already I that that was in the back of my mind so you can tell me that I let me see I have I'll just finish this one and leave it the other sponsor all examples so wow okay so data traceability is very important tolerance in 10k for example because you are making life and investigations uh treatment decision based upon that USBC data as well I mean I just put it because you know a wrong place was pumping because in 1999 because it is not updated in the database for the prominence was not clear caseability interest service depending upon data performance for example clinical data trail clinical trial data is not just where the if the trial is large reputable randomized Define this one um I think this because this has been gone over on the first day I remember my professor from my small so this is the same things you know what is the Synergy with fake principles and you know find for findability there are some for accessibility and or uh so I skipped off so what the Hobbies along with unique and persistent identifiers metadata is considered the communist or concrete principles guiding set would get done the challenges though is produced actually described at the data evaluation evaluating detail object fairness some of this will be discussed the document so just briefly this is an article I just want to give you a contrast with how metadata is managed in our domain uh if you Google this setup works this is what you get it just lists a bunch of stuff and let me just show one example I'll wrap it up so this is a repository that is used by a lot of computer science research this is maintained by Stanford but you can see that the amount of better data is very limited but here is name type description of the entire data set not the individual fields so this is the level of metadata that you see in our domain unfortunately sometimes we have a data set that we don't have enough metadata information to understand and use it so that is a big problem in in our domain so again here is another one I've been not going to that you can click on this and see those policies so just to summarize you know efforts in creating the data using Netherlands along with the long way in the access and meaningfulness now that is the key when the data sets are very large and complex this is even more important it's important to pay attention to both metadata creation as well as whether they can want to make principles we'll be learning more about metadata creation data planning system so I'm going to wrap up I'm sorry I misunderstood I I didn't remember this one I'm going to stop here I answer any questions and I thought I did not put into the optimum time
