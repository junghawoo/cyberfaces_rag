---
title: "Justice in Data: Principles of Interoperability"
unit_id: 137
course_id: 10
level: "Foundation"
slug: justice-in-data-principles-of-interoperability
is_course: 0
---

# Justice in Data: Principles of Interoperability

## Extracted resources (local files)

### Introduction to Interoperability Slides
*Source file:* `CTW-interoperability_FINAL.pdf`  ·  *type:* file

Interoperability

Team Presentation
2
Sharma 
Chakravarthyame
Professor

What am I assuming?
●Nothing about interoperability!
●As this audience has undergraduates and might have not 
been exposed to the concepts of standards, integration, 
and interoperability at any level, we will explore these 
from the beginning
●You might have already used some of the data exchange 
formats such as JSON or XML in your work
●Understanding of these will help you in using existing data 
and packages, as well as during the development of new 
applications that needs to work with other applications

Presentation Outline
●
Standards, Integration, and Interoperability
○
Familiar examples
●
Why is it important?
○
Example from Health care domain video
●
Going into details
○
Application interoperability
○
Data usage in interoperability
○
How does FAIR principles affect 
interoperability
●
Conclusions

Standards, Integration, 
and Interoperability

Standard s
●Everyone has heard of 
“standard s”
●something set up or established by an authority as 
a rule for the measure of quantity, weight, extent, 
value, or quality
●constituting or conforming to a standard especially 
as established by law or custom or community
●In various domains
●IEEE, ANSI, ISO 9000. ISO/IEC, ASCII, OGC (30+ 
standards)
●Examples
○USB A, B, C, SATA, SCSI, XML, HTML, SQL
6

Standard s
●Following a standard has many benefits
●Supports multiple things with a 
standard
in te rface 
to con n e ct an d in te ract with ou t an y ad d ition al 
e ffort
●Clu tch , b re ak, an d acce le rator is a g re at e xam p le
●Not followin g a stan d ard h as im p lication s
●Ele ctrical con n e ction , Ap p le in te rface , …
●Ne e d to carry con ve rte rs
●Gre at Baltim ore fire of 190 4 (30 % of th e h ose s 
wou ld n ot con n e ct!)
●You m ig h t h ave h e ard of “Stan d ard ” wars 
○Be tam ax vs VHS, …
7

Standard s
●Our interest is in standards for
●Using available data 
●Sharing data
●Application interaction
●Application & data Integration, and 
●Interoperability
●Standard is applicable to both data and 
applications, and metadata (
as we shall see )
●Who creates standards?
○An entity such as IEEE, ANSI, OGC
○Consensus
○Evolution
8

Software Standard
●A software standard is
a standard, protocol, 
or other common format of a document, 
file, or data transfer accepted and used by 
one or more software
...
[W iki]
●Stan d ard s are critical to th e u n d e rstan d in g , 
com p atib ility of h ard ware , software , an d 
e ve ryth in g in b e twe e n . 
●In d u stry stan d ard s e n ab le th e e sse n tial 
e le m e n ts of a com p u te r an d re late d 
in frastru ctu re to work tog e th e r.
9

Standard s
●Standards allow technology to work seamlessly and 
establish trust for smooth operation
●Provides a common language 
●Makes interoperability of components, created 
independently, possible
●Guarantees behavior that is well understood
●Javadoc is not a standard (a guideline)
○Introduced for the time in  a language for generating 
documentation 
■Is automatically generated
○If followed, no need for separate documentation
■Which is rarely done properly!
10

JavaDoc Example
/**
* Hero is the main entity we'll be using to . . .
* 
* Please see the {@link com.baeldung.javadoc.Person} class for true identity
* @author Captain America
*
*/
public class SuperHero extends Person {
// fields and methods
}
/** * <p>This is a simple description of the method. . . 
* <a href="http://www.supermanisthegreatest.com">Superman!</a> 
* </p> 
* @param
in com in g Dam ag e th e am ou n t of in com in g d am ag e 
* @return
th e am ou n t of h e alth h e ro h as afte r attack 
* @see <a href="http://www.link_to_jira/HERO-4 0 2">HERO-4 0 2</a> 
* @since 1.0 
*/ 
public
int successfullyAttacked
(int in com in g Dam ag e ) { 
// d o th in g s 
return
0 ; 
}
Min ib ase Javad oc e xam p le :   h ttp s://in st.e e cs.b e rke le y.e d u /~cs186/sp 0 7/h om e work/javad oc/g lob al/Min ib ase .h tm l v
11

Standard s (in lighter vein)
12
An old saying: The good thing about standards is 
that there are so many of them!
From: 
URL: https://guides.library.umass.edu
/standards

Integration
●Following standards allows us to connect or 
integrate devices easily
●However, we are dealing with not only 
devises, but data, software, and applications
●Although there are guidelines for software 
development, rarely applications that are 
developed independently 
can work with 
e ach oth e r (e .g ., e xch an g e in form ation ) 
with ou t an y ad d ition al su p p ort
●Th is re q u ire s integration
of ap p lication s
13

Integration
●For application integration, the issue is the 
data
generated and consumed
b y an ap p lication
●As data can b e g e n e rate d in m an y form ats 
(b in ary, cu stom ize d , XML, Json , e tc.), con su m in g 
th e m b y oth e r applications requires additional 
software to understand and interpret 
it
●This is usually done by integrating the two 
applications by adding appropriate new software 
in each application
○This may have to be done for 
each pair 
of 
applications!
○Referred to as the 
quadratic cost
14

W hat is quadratic cost?
15

Software Integration
●Software integration can be thought of as the 
process of connecting one (software) 
application with another.
○
Typically through their application 
programming interfaces 
(or APIs). 
○Once connected, the applications can 
share 
data and provide updates to one another in, or 
near, real -time.
○This could include integration with data 
repositories and different types of databases
16

Example
●Point of sales (typically known as market
-
basket data) is collected by every  vendor
●Customer information is also available with the 
vendor as part of another system
●To understand the customer preferences 
(termed CRM or customer relationship 
management), the above data (may be in 
different formats) needs to be accessed and 
processed together
●One way to do this is through APIs and 
understanding the individual data formats for 
integration
17

Example
●Let us take a look at the above concepts leading 
to the concept of interoperability with this video 
from YouTube 
(https://www.youtube.com/watch?v=eLK0UL2WYN8
)
●Although this video is from the healthcare 
domain, it is easy to understand the underlying 
problems, issues, solution, and its applicability 
to other domains
●The principle explained in this video may be 
applicable to other domains in slightly different 
ways
18

YouTube Video
19

Interoperability 
(A Familiar Example) 
●Think of a speech given in UN general assembly in 
a specific language 
●To translate this language to different languages, 
you need one interpreter
for each language into 
which it is translated
(typically, integration).
●
Alternatively,
●It can be translated into a 
single common 
language
(Esperanto? ) if everyone can 
understand that common language 
○providing interoperability
20

Interoperability 
●Integration makes sense if you have a small 
number of applications to work together
○
Quadratic cost kicks in when number of applications gets 
large
●Interoperability is preferred for large number of 
applications (less resource needed and scales 
better) with different types of data being used 
/generated by applications
○
When a new application is added, it has to 
ONLY
u n d e rstan d th e com m on lan g u ag e .
○
Syste m or software d e ve lop e d for th is is te rm e d th e 
m id d le ware
○
Qu ad ratic cost is re d u ce d to lin e ar cost
21

How Important is interoperability? 
●In the 70 ’s and 80 ’s DOD was using hundreds 
of programming languages in its components
●As well as Multiple databases (including 
hierarchical and network)
○Same data/information was stored in multiple 
databases
○Different attribute names were used for the same 
thing making it difficult to merge (semantics)
○Lots of research was done on schema integration, 
heterogeneous and distributed DBMSs to 
overcome this problem
○Millions of $$$ were spent on this!
22

How Important is interoperability? 
●The same data (e.g., a plane or a ship) were 
represented using different attribute names and 
levels of details
○Missions generally included resources from 
multiple units of the DoD
●Schema integration became an important topic 
of research
●Heterogeneity of models had to be addressed
●Heterogeneous and federated DBMS concepts 
were explored
●Prototypes and systems were build to 
demonstrate the concepts
23

How Important is interoperability? 
●DoD initiated the development of a new 
programming language to be used across DoD
○Named Ada (after 
Ada Lovelace who was the first 
woman computer programmer
) was d e ve lop e d 
an d m an d ate d for u se in DoD
○Ad a is cu rre n tly u se d across DoD as th e ap p lication 
d e ve lop m e n t lan g u ag e
■
Un fortu n ate ly, n ot wid e ly u se d ou tsid e of DoD
●DoD also fu n d e d th e d e ve lop m e n t of Oracle 
Relational DBMS
○
Oracle is wid e ly u se d across DoD
○
It is also a p op u lar DBMS (h as h ig h e st m arke t sh are )
24

Levels of Interoperability 
●Foundational
○“tightly integrated
”. Does not require the ability  for 
the receiving system to interpret data
●Structural
○Refers to the structure or format of data exchange. 
Defines the syntax of the data exchange
●Semantic
○Ability of two or more systems to exchange 
information and use the information that has been 
exchanged
○Includes structural interoperability
○Provides highest level of interoperability
25

From Open to FAIR 
●Open data is available without restriction whereas FAIR 
data defines specific conditions to be accessed and 
utilized (FAIR principles can apply to metadata as well!)
●On the other hand,
●FAIR data is also widely available and utilized, by 
incorporating the following usability requirements that 
go beyond permission alone
○
FAIR data must be defined and entered into online public 
records for the purpose of discovery and citation
○
FAIR data must be made accessible such that it can be 
opened, read, and processed
○
FAIR data must be recorded and presented in a way that 
can be understood and utilized (meta data)
26

From Open to FAIR 
●Data interoperability is the ability of a data set to 
work with other systems or multiple datasets 
without special effort
●Data interoperability has also been defined as  
“a 
feature of datasets 
… whereby data can be easily 
retrieved, processed, re
-used, and re -packages 
(“operated ”) by other systems  
[From Open Data MOOC]
●Ab ove ch aracte ristics of d ata is close r to FAIR 
p rin cip le s
○Me ta d ata can e xist b oth for d ata an d d ata se ts
27

Facilitating interoperability 
●Through data exchange formats
○Using a standard or known data exchange 
format makes it easier for applications to 
facilitate interoperability
○A transition from earlier binary exchange to a 
human -readable exchange format took place
○Typically known as markup languages
■HTML, XML, RDF/XML
28

Data Exchange 
●Common data exchange languages/formats 
include 
○XML, JSON, YAML, .CSV, .tsv, RDF, etc.
●We are already familiar with .csv and .tsv files
○These format files can be used directly in Python 
and other libraries used by Python (Pandas, etc.)
○Meta data is still needed (semantic or at least 
structural) for using them effectively
○There has been a move towards human
-readable 
formats as compared to earlier exchange of binary 
data
29

Data Formats  
(from harvard.edu) 
●XML (eXtended Markup Language)
+
Flexible
+
Uses Standard published by W3C working groups
+
Human readable and editable
+
Error checking by using STDs, display using style 
sheets
+
Can represent hierarchies
+ Tools available for creation, parsing, search/query
-
Bulky (payload/formatting ratio)
-
Parsing and search/query can be CPU intensive 
30

XML example (review of a paper) 
<conference shortName="PAKDD2022">
<submission id="121" title="Object Detection via Inner
-inter Relational Reasoning Network">
<question number="1" text="Summarize the paper's main contribution and impact.">
<answer>Your answer</answer>
</question>
<question number="2" text="List three, or more, strong aspects of this paper. Please number each point.">
<answer>Your answer</answer>
</question>
<question number="3" text="List three, or more, weak aspects of this paper. Please number each point.">
<answer>Your answer</answer>
</question>
<question number="4" text="Detailed comments to the authors.">
<answer>Your answer</answer>
</question>
<question number="5" text="Relevance.">
<options>
<option>Less Relevant</option>
<option>Relevant</option>
<option>Highly Relevant</option>
</options>
<answer>Your answer</answer>
</question>
…
</su b m ission >
</con fe re n ce >
31

Data Formats  
( 
●XML (eXtended Markup Language)
○Extensively researched on its usage
○Most DBMSs support XML 
natively
○Most DBMSs support DOM (Document Object  
Model created from XML) objects and querying 
them using Xpath
■DOM is created in memory
■Allows one to programmatically read, 
manipulate, and modify an XML document
32

Data Formats 
●JSON (JavaScript Object Notation)
+
language -independent data format
+
Many programming languages support 
generation/parsing
+
Human readable and editable
+
simpler than XML
-
Bulky (payload/formatting ratio), better than XML
-
Parsing and search/query can be CPU intensive 
-
Not as flexible as XML for some types of data 
structures and binary data
33

Data Formats 
●JSON Example
○
This example defines an employees object: an array of 3 
employee records (objects):
●
{
"employees":[
{"firstName":"John",
"lastName":"Doe"},
{"firstName":"Anna",
"lastName":"Smith"},
{"firstName":"Peter",
"lastName":"Jones"}
]
}
●JSON Syntax Rules
○
Data is in name/value pairs
○
Data is separated by commas
○
Curly braces hold objects
○
Square brackets hold arrays
34

Data Formats 
●CORBA (Common Object Request Broker 
Architecture) 
– for completeness, older
+
Although binary, includes protocol and architectural 
standards
+
Language and OS independent
+
Compact data representation
+
Java support
+
open source versions available
-
High learning curve
-
Not well supported by OS vendors 
-
Firewalls can impede usage
35

USGS  (from open geospatial consortium or ogc.org)
●
USGS data services gets over 1M hits per day
●
OGC standards are used for geospatial information 
interoperability
●
OGC conducted the USGS interoperability assessment to  assess 
if OGC standards are implemented in USGS servers
●
OGC advanced the following activities:
○
Compliance Testing
: OGC te ste d USGS We b se rvice s ag ain st th e OGC 
Com p lian ce En g in e . OGC p rovid e d re com m e n d ation s b ack to th e se rvice 
p rovid e rs. Mod ification of th e te st scrip ts an d fe e d b ack was p rovid e d to th e 
OGC com p lian ce d e ve lop m e n t te am .
○
Developing of use cases and investigation of usability with communities 
of use : OGC issu e d a Call for P articip ation (CFP ) for a Virtu al Exe rcise . OGC 
an alyzed th e p articip an t’s e xp e rie n ce s wh e n in te ractin g with USGS d ata 
se rvice s an d p rod u cts. OGC e xtracte d u se case s an d p rovid e d 
re com m e n d ation to USGS.
○
Development of a CAT 3.0 test suite
. USGS was in te re ste d in g e ttin g 
starte d with th e d e ve lop m e n t of CAT 3.0 te st. It was cre ate d in GitHu b .
36

Conclusions
●
Data by itself is of limited use unless it can be found, accessible,  
understood, and can be used meaningfully
●
Following the standards, using published data exchange 
formats with language support for them makes analysis much 
easier and takes less effort
●
FAIR principles are one way to make data accessible and 
useable for Millions of users as is done by  USGS
●
Hence, it is critical and we understand the importance of 
standards, integration issues, and why interoperability is needed
●
In the next  module, we will discuss meta data and their 
provenance
37

Thanks!
Any questions?
38

EXTRA ITEMS

40

Diagrams and infographics
41

✋👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆
💑💑💑💑💑💑💑💑💑💑💑💑💑💑💑💑💑💑💑💑💑
🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔🍔
🔌🔌🔌🔌and many more...
😉😉
42

## Fetched resources (external URLs)

### Principles of Interoperability Pre-Survey (link)
*URL:* https://utaedu.questionpro.com/a/TakeSurvey?tt=kbj%2BWAg8pCQECHrPeIW9eQ%3D%3D

[survey link — skipped]

### Principles of Interoperability Recording (link)
*URL:* https://www.youtube.com/watch?v=p58kV6sFFgU

[YouTube transcript p58kV6sFFgU]
in this portion we are going to cover two things one is interoperability and the metadata and performance now you have already seen some or some things in the previous section and others where we have alluded to you know why we need this kind of thing and what is the purpose we will try to understand more of what are the things that are needed what things have to be in place between the builders so if that's me and again I'm not making any assumptions on what you know so that hopefully you know even though you might be somewhere a bunch of stuff that I'm going to throw up so we cannot sort of discuss interoperability without conditioning a little bit about standards and integration and how there are different from the probability if you look at some familiar examples I'm sure you have been using a bunch of things without even knowing how they work together and why and solve their need to work together so that's that's important to understand other daily things that we use so the other question why is this important we will look at a video I think it's a very educational video bringing out clearly the need and the difference between integration even though it's for healthcare domain it's applicable to in your opinion of their domains as well and then we'll go into some details application interoperability data usage and finally how trade principles which is the kind of the basic underlying theme of this Workshop how it affects interoperability and Robin space relationship between them it's implications so standards integration in an interoperability so everyone has heard of standards we use that in our daily life some things set up or established when County and Cebu for the measure of quantity weight extend value so we know what one pound is released a standard as to how much pound is how much a kilo is how much is a meter and how much you say yeah all those things are established and we use it totally take it for granted sort of one other example I can try to do is subject so standards constituting or conforming to a standard especially as established by either law or custom or a community agreement to do so and you can see the prevalence of standards in various domains arguably is saying Institute of electrical and electronic engineering and see ISO 9000 ASCII ODC which is related to your domain so every domain has different standards for different purposes so some of the examples that you have used on a regular basis you know we all use USB USB compliant devices we also use disk erasers that are set on scuzzy compliant you might have use XML which is a data exchange standard HTML which we are all familiar with from the web the school is the standard so we are familiar with a lot of these things on a daily basis on the use it but we don't perhaps think a lot about why they were developed the purpose and what happens if we don't sell them so following the standard has a bunch of benefits so that is certainly true if each one did according to their own way of thinking then it will be very difficult to do any interaction or exchanger business uh Comics or any of those things can be really different supports multiple things with a standard interface to connect and interact without any additional Network so this is the key or the purpose of a standard so you should be able to use it without having to worry about it a very good example I feel is the way we have clutch and break and accelerator in an automobile so just think of a situation where this was not standardized or every manufacturer was using a different way of doing it even different locations for them there would be a total chaos so even though we don't think about these things when we use them this is a standard that has been accepted in whatever way because of the community or by law or whatever it is this is one of the very useful and important standards that make our life and everything as much easier so that that's important to understand the purpose and the utility so what happens if you don't follow the standard so we are also aware of familiar with some of these in our daily experience and life and here are a couple of examples you know electrical connection for whatever reason different countries have decided to come up with a different standard for historical reasons for their own country and the downside of that is you have to carry converters when we travel it would have been nice if the whole world like like the clouds are the same thing another good example is you know Apple having its own interface which is not compatible with anybody anything and anybody else so you know so people like European Union is trying to fix that up sort of making them so that that's a very important so you can see in our daily life what happens if we don't have a standard and and what are the effects of them I was surprised to read that you know there was a fire in 1904 in Baltimore and it was a disaster partly because 30 percent of the forces would not connect to the uh thing that they were supposed to panic which essentially State the standardization either was not there or what not being followed or enforced not being used so this is this is a trial shooting right it's a tragedy that can be avoided by making huge standards are followed and and used correctly so you might have heard of other things like standard laws one famous example I can think of is metamax versus VHS so this is between you know industrial Giants who wanted to make their Innovation the standard for the for everyone and you know again some of these sort of not necessarily decided based upon the technology and other things the principal Invaders of the practice but this goes to the essence of understanding why standards are useful because then you have to make a choice when you buy something whether it can uh I can give you this particular product or this other particular products are you have to buy multiple that so standards are very important and very integrated in our daily life so our interest uh in standards is saying slightly different purposes using available data we want to use available data and what happens if we don't have standards for them sharing data so it's very common as we saw in the previous examples when you have multiple files or multiple types of information that you have they need to be merged or shared and combined and that is going to be an issue application interaction so we'll see more of this these applications need to interact they need to confirm something that means one has to understand what it is I mean think of it as a as a natural language you know if somebody speaks Mandarin to me I won't be able to understand so I do not understand that particular format of that particular language and vice versa so so this is very important even for an application because they will exchange communication data data integration application and data integration in general and interoperability so standard is applicable to both data applications and we'll see it can even be applied to metadata we'll see metadata Creation in the afternoon and you'll see you know the task release and uniformity in between each method it is creator and the question is who is responsible for creating those standards and how it is in so it is typically an entity such as IEEE and CR ogc will come up with this you know with consensus with with the right background so there is there can be something purely based on consensus and usage or it can be an evolution into what it has come through and everyone understands it and uses it so it's no longer a problem so you can also apply the north campus standby through a software in addition to devices and other things a software standard is a standard protocol or other in common format of a document file or data transfer accepted and used by one armor software so essentially this is a standard in order to make sure that one software can understand the linger from what the avical software and vice versa and without that we will be developing software independently and it will be very difficult to integrate them or communicate between them so standards are also critical to the understanding compatibility of Hardware software and everything in between industry standards enable the Essential Elements of the computer and related infrastructure collectible so you will see in our Network standards you know other kinds of standards that that are commonly used standards typically allow technology to work seamlessly and also establish trust for smooth operation it can provide a Common Language makes interoperability of the components created independently that's very important because we create a lot of things independently without knowing who is going to use it or how it is going to be used and if it has to be used in a meaningful way by a large volume of people or masses then it has to conform to certain standards so that it can be used very effectively it also guarantees Behavior that's Valencia soil when you know what what a USB a is and what a USBC is you know the difference between AMC and you understand the behavior very clearly you know one is faster one is not just so fast and compatibility and other issues apart from that your understanding very clearly so one interesting side note is in all uh apart from the standards for application exchange even when you develop software one of the biggest challenges for software engineering people is so to make sure that the software is understood not just the interfaces but the software itself can be understood this is very useful for my developers point of view right I mean there are people who use the software and there are people who maintain the software to extend the software will be what is the software so these are two different groups of people and you want to make sure that there are standards or perhaps guidelines to do that so jam up so the first programming language that you introduced for the first time in a language what to do for generating documentation automatically until then you know documentation was secretly created by Developers and as we know most of the times it is not done it is done after the fact and it's not captured completely and the cost associated with software is mainly because of this reason there's not enough documentation so sometimes redeveloping things is cheaper than fixing something that is very difficult to understand especially if there's conflicts if followed this made it there was no need for a separate documentation and based upon my experience and others people rarely do documentation properly so here is a example of uh guidelines you know you can so you can sort of sprinkle various comments and other things comments have been around that comment themselves do not create any additional document so here for example some of the things that are highlighted in in board letters is is primarily meant for a software that will go through this code and generate appropriate documentation for the use of this and this is very important I I don't know I mean at least in the computer science and software engineering we struggled a lot about this we struggle a lot because documentation is very poor and even when it exists it is not complete and that makes very difficult to maintain manage just to give an example Oracle dbms for example is one million plus lines of code so this is being developed over the last 40 years so multiple groups of people have implemented revised extended and do that now there's a new batch of people who have to maintain and extend that and for that understanding the current core is extremely important before we make any changes in a product that is being used by hundreds of thousands of people so that is the that is the uh so agencies like NASA worry a lot about software quality and trustworthiness because when they send somebody up they want to make sure that the software works the way it should work and there are no other things happening so here we saw once you put in the right information that is according the guideline this is what you get here is an example of what you get so this is automatically generated this is an example that we use a software that we use for communities but you can find this for a lot of different kinds of software primarily developing Java so it tells you what is the plus it tells you what object it is it tells you uh so it can give you plus use whether it is implicated index and all things and so it will tell you what are the fields associated with this class uh what is the Constructor methods associated with that and various other details that you can look at and this can be done without having to write a separate documentation we this is one of the most important and then can you can dig deep and go into the details of each one of them and so this assumes this assumes that some guideline or some standard has been followed in the creation of these things without which this cannot be done so that is the sort of the importance as I see in terms of why these are important so just to uh in a lighter way how standards proliferate so certainly we have a lot of standards and you know you have some number of standards and you create you feel that you need a universal standard now you have one more standard so I uh also uh as you say saying that goes this way the good thing about standards is that there are so many up there so apart from that I think standards we understand uh will see that is extremely important extremely beneficial and every attempt should be made at least in these figment so I just want to contrast this with Hardware domain versus software domain because there is a big difference when when Hardware when chipsets and chips are Manufacturing standards are enforced very effectively because if it doesn't if it's not done then there's no way to use it and there will be heavy offers whereas when it comes to Software it's a very tricky thing because software can be changed on a daily basis whereas you cannot manufacture the same internship on a daily but you can manufacture but you don't revise it you revise it periodically and the new version is out there for a year or 200 so that is not true for software the ability for us to keep changing them incrementally and whenever we want make standardization much more difficult makes the cost of software development so much difficult any questions support okay so now let's come to integration so standards are mainly used for a specific thing integration means you have you are connecting or integrating something with something following standards allow us to connect or integrate devices easily absolutely we are dealing with not only devices but data software and application so it's not just a two piece of hardware for which standards are I think much more understood and enforced although there are guidelines for software development rarely applications that are developed independently can work with each other whether it's the exchange of information or calling one from the other without any additional support this is the key when you want to integrate you need to make sure independently the software can work together and if they don't then you have to provide some additional support this requires integration of applications that are developed independently and what does it mean it means that for application integration the issue is the data generated and consumed by an application which has to be properly dealt with as data can be generated in many formats it can be in a binary format it can be in a customized format external Json data exchange formats you need to worry about that consuming data by our applications requires additional software to understand an interpreter so when you make a call and send certain pieces of information the other side has to understand and interpret it so that can make you suffer this is usually done by integrating the two applications by adding property new or additional software in each application so essentially you add additional features of software that is capable of understanding what is saying by A to B and B to a so that they can exchange information in a way they can understand easier so the the difficulty or the cost is this may have to be done for each pair of applications so if you have only two applications uh maybe it's easier to do but if you have five applications then the number of such software pieces that had to be developed for each one to understand all the others is going to become extremely complex and this is typically referred to as the quadratic pasture as you know quadratic curve which is a a discrete raises much faster than a linear curve and here is a sure so this is not so you can think of a linear curve which is typically at 45 degrees angle and that increases so when you when the number of applications increase the number of things you need to do is linear Place 120 your five applications you need to try things but if you are doing the quadratic then the number of things you have to do increase the significantly to the power of two this is the problem with integrating applications on a pay-by-pay basis which is extremely difficult so this is the underlying problem and the cost associated with also software development cost not only is the development contesting in debugging making sure everything is working so software integration can be thought out as the process of connecting one piece of software application with another typically through their application programming interfaces are what we call Api so typically applications publish their apis so that some other application can call it without having to know the details of the application which may be proprietary in nature in many cases it is so apas are a mechanism to publicly Advocates or publish what interfaces they provide so that you can use this system now use the software using those apis without having thoughts essentially it's a black box model so in a Black Box model you don't know or you're not allowed to know what is inside but what blocks but you know how to use it you know how to operate it you know how to connect it with other systems that will work together so that is the core idea so once connected the applications can share data and provide a page to the manager in ordinary account so that is needed in many cases this could include integration with data repositories and different types of databases because of your access data from a database you have to use an API for example for that I'm going to get the information in whatever the format it sensor understand it and you could also to hit you say a simple example that you can relate with so earlier I mentioned something by Market Basket data so this is what we call the point of sales data that is typically connected by every vendor or every customer so every client a customer walks through a a short buys certain things checks out at the counter uh these points of sales information is is collected this essentially says you know this is the location in which this was bought in this particular counter and these are the items that were bought and this is the price of this items you also have separately customer information with the uh with the vendor as part of our system so we have always thought so they want to put informational things and to understand the customer preferences you may want to put these two together so maybe one application is dealing with the points of sales generates the data and makes it available in some way another application has the customer information but if you want to put these two together then you have to build some additional software brought in in order to do that one way to do this is through apis and understanding the individual data Finance from the future so this is just one example you can think of very many places where this kind of thing happens because not all data is collected in one place and stored in one format storing one application so let us take a look at the above Concepts leading to the concept of interoperability why we are not happy with integration is there a better way other than integration to deal with this problem and we're going to watch a video on to understand that I think this is a good video that brings up although this video is from that Healthcare domain I think it's easy to understand the underlying problems as your solution and it's softly together means the principle explained in this video may be applicable to different domains in different ways so let's take a few minutes to move on watch this and then we'll discuss this I don't know if they're supposed to be sound but um I don't hear any sound for the video excuse me I don't hear any sound for the video I didn't know if there was supposed to be any yeah there is uh the audio is very important how do I how do I make it uh come true I think when you're sharing your screen there's a checkbox for sharing computer sound when you go back to the share button at the top I think okay okay I think wow I have done that let me start this from the beginning oh no tell me whether you standards and interoperability in digital Health yes when people discuss digital health the term standards and interoperability often come up what do they mean and why do they matter could such abstract technological processes actually help save lives we will answer this question in three parts first we will look at a case study to explore why it's important to get digital Health applications to communicate with each other second we will see how connecting digital Health applications through integration leads to significant cost scalability and management challenges third we will show how to overcome these challenges through standards and interoperability let's start with part one the case study scenario in the fictional country of Onessa Lucy the national immunization officer adonessa's Ministry of Health and Isaac The District Health officer of umbaya a planning an upcoming child vaccination campaign to get child immunization numbers up nationally Lucy has been put in charge of managing the national campaign across all the districts she starts by working in the most populated District first Isaac's District of umbaya Isaac's District includes some rural areas as well as some smaller City centers and in this campaign he will need to provide immunization to children in all areas of his district through facilities and mobile clinics Lucy visits Isaac's District Health office to help him gather the information he needs to do his district planning for the child immunization campaign they want to use two different data points to assist with planning the first is they need to know how many children need to be vaccinated the second is they need to know how many vaccines Isaac currently has for each of the service delivery sites if they can't compare this information they might not order enough vaccines for the children in his district putting their lives at risk these two data points exist in two different Global Goods applications open lmis a supply chain application and dhis-2 a district health information application open lmis can give them a view of the vaccine supply chain how many vaccines are available to be used and where they are stored dhis2 can give them a view of the number of children in the district catchment area who are eligible for vaccines but they can't see this information together because it is in two different applications currently to analyze the data in this format it takes significant manual labor and even still sometimes the data sets do not align properly resulting in less reliable and error-prone information ultimately all this tedious effort leads to Too Much Time managing and cleaning large and often inaccurate data sets and not enough time making evidence-based life-saving decisions but why can't these two applications automatically exchange information with each other well when open lmis tells dhis-2 there are five DPT vaccines in umbaya clinic this month dhis-2 cannot understand open lmis's shared messages because they use different vocabulary and grammar to describe the same data values so how can we help people like Isaac and Lucy get these systems to communicate let's explore that next [Music] in part one we saw the challenges faced by Health System managers trying to make digital Health applications work for their health programs and left off with Lucy and Isaac struggling to get their applications to exchange data now in part two we will examine the way Lucy and Isaac initially try to solve this data exchange challenge but face problems with this approach later when talking to the ministry software development team Isaac and Lucy learned that they can directly integrate the two applications dhis-2 and open lmis to enable communication of data they explained that to integrate the two applications they will need to write custom code between the applications to translate how the data is being described by each application using a bi-directional connection this sounds like a good strategy for solving this simple use case however Isaac doesn't just manage immunization but all the health programs in his district many of which are supported by their own applications that could benefit from communicating with each other and Lucy doesn't just work in this District but manages the whole country's immunization program and she needs many other districts applications to be able to communicate as well so Lucy and Isaac asked the software development team about integrating their other applications when working with the team on integrating the larger set of applications they encounter new challenges when they connected just two of their applications open lmis and dhis-2 they needed just one bi-directional connection to exchange data so the cost was low however this problem compounds when you add additional applications when they add a fourth system they need to maintain six bi-directional connections and a fifth needs ten and if one application changes all the other applications need to change as well since they are now connected this is extremely expensive and will quickly use up their entire budget why does the cost and complexity rise so significantly with each additional application the software development team explains that it is due to a problem known as the quadratic cost problem named after the mathematical concept they illustrate here the number of bi-directional connections increase quadratically not linearly with each integration of a new application when you have a country with as many systems as onnessa by the time you need any more than three applications the cost and complexity rise much faster than the number of digital Health applications you are trying to connect there must be a better way integration is not sustainable writing software to directly connect to applications or integration may be able to connect your applications but there will still be the quadratic cost problem is there a way for multiple applications to communicate with each other that addresses the quadratic cost problem yes we will explore this in the next part [Music] now in part three we will see how Lucy and Isaac learn about investing in an approach that addresses these challenges and allows multiple applications to exchange data the software development team explains that the solution is standards and interoperability first they show Lucy and Isaac what standards are and then they explain to them how it will help with interoperability what are standards in software standards are a set of rules that allow information to be shared in a uniform and consistent manner across any application they are approved and published by an authoritative official organization as the systems are currently configured for Lucy and Isaac's immunization campaign open lmis and dhis-2 cannot currently communicate with each other remember dhis-2 has been trying to ask open lmis a simple question how many DPT vaccines are at bioclinic this month but they cannot understand each other without a common set of Standards the software development team instructs Lucy and Isaac on the importance of two specific types of Standards to enable interoperability semantic and syntactic standards that help applications establish a common vocabulary are known as semantic standards for the two applications Lucy and Isaac are using in their immunization campaign they need to agree on two vocabulary lists in order for the applications to communicate one for the vaccines and one for facilities for example the semantic standard to refer to the DPT vaccine is vax dot DPT and for the umbaya health facility is facility 145 once they agree on a semantic standard they both use the same terms to describe the same commodity when dhis-2 asks open lmis how many vacs.dptpt vaccines are at facility 145 this month open lmis response to dhis2 with a question what do you want to know about vax.dptpt and facility 145 with semantic standards even though both applications are now using the same words open lmis still don't understand what is being asked open lmis can understand the vocabulary of backs.dptpt and facility 145 but not how they relate knowing what the terms mean isn't enough so the software development team explained to Lucy and Isaac that these applications also need to have common grammar to communicate meaning standards that do this are known as syntactic standards they help you determine how the words fit together the software development team shows Lucy and Isaac what happens when they have both semantic and syntactic standards with both sets of standards in place the dhis-2 and open lmis applications can share data automatically and seamlessly so when dhis-2 asks open lmis how many vax dot DPT vaccines there are at facility 145 open lmis can provide dhis2 with that data responding that there are five facts.dptpt vaccines at facility 145. now that Isaac and Lucy understand standards they must determine all the different semantic and syntactic standards they would like to adopt in Onessa the software development team explains that investing in standards will make it easier and more cost efficient to enable interoperability between all their digital Health applications interoperability is the ability of multiple applications to communicate with one another by accessing exchanging and making use of data in a coordinated manner to achieve health goals to ensure true interoperability at a large scale between all their systems Lucy and Isaac learned that they need to invest in a component known as a health information Exchange a health information exchange or hie is part of a country's Enterprise architecture that connects multiple applications and allows them to move data between one another using standards bundled together to provide implementation guidance for the software Developers this approach overcomes the quadratic cost problem open hie is an example of such an architecture one of the things that hies do is store lists of terms and Concepts mapping how these lists relate to each other across different applications standards make this mapping process easier the hie receives the data from each of our applications and keeps track of how they relate and will translate between the different applications in real time this enables the three or more applications to communicate through our hie as a central translator now any new application that gets added only needs to be able to communicate with the hie and if an application changes only the hie needs to be updated while all the other applications can still communicate this is one way to keep costs down and avoid the quadratic cost problem we saw in part two now that Isaac and Lucy understand how standards let applications communicate both vocabulary and grammar and that an hie lets many applications easily exchange data in a cost-effective way they want to invest in building one and are ready to learn more about how the components of an hie architecture can interact with their applications once they know this they can work with the Mohs digital Health lead to ensure that the investment roadmap for their National hie will meet their needs the next year when Isaac and Lucy need to do their planning they can pull the data they need from the different systems together this lets them see how many children need to be vaccinated how many vaccines they have available and how many they need to order with their applications linked Isaac and Lucy can ensure that all the children in their district and country are vaccinated and can grow up healthy moreover by using an hie to help interoperate their applications data is showing them population level Trends they couldn't see before and now they can make time sensitive evidence-based decisions that impact the lives in every District at every age group and at each point of the health Journey okay so I want to pause here for a second to get any questions and comments I'm assuming that you know this has clarify a bunch of things about standards integration and interactivity any questions okay standards and interoperably okay so let's continue with doing so another easy to understand example is think of a speech given in you and general assembly in a specific language to translate this language to different languages you need one interpreter of each language into which it is translated so this is typically integration and if you want to do it for many languages you need so many translators and and this number goes up if there are five different language being spoken and it has to be translated into five other languages alternatively it can be translated into a single common language if possible if everyone can understand the common language to provide in traffic control so this is the essence of intraubility and the middle way or the exchange that you saw in the video try not to do that some effort is needed but that effort is much much less than the airwise integration of doing things so so integration makes sense if you have a small number of applications to work together but the quadratic cost kicks in in the number of application systems to be integrated get structure so that is really where the utility of developing either in exchange or adding in Midway that can translate from one to another is extremely beneficial so in Turkey is preferred for a large number of applications less resources needed and scales better with different types of data being used generated both applications when a new application is added it has to only understand the common language not every other language so that's the main idea behind it system of software developed for this candidates many times called the middleware and the goal is to reduce the quadratic plus to linear cost so how important is interoperability so here is an example of that I can sort of relate to in the 70s and 80s in the Department of Defense because using hundreds of programming languages in its units Air Force was using few languages military was using another few languages maybe was using a different set of languages and each one was developing things in their own languages as well as multiple databases so this was another issue you know there was a lot of people if you know I was part of some of them so they were using relation databases had article databases together different pieces of information sometimes same data or information was stored in multiple databases using different attribute names are making it difficult to understand the semantics just like the semantic exchange that we saw structured in semantic standards it's not enough to just think about friction the vocabulary should need to be seen if something is called you know ship ID in one place Sid in another place you don't know that ship ID is the same as SL today this was a real problem because lots of research came about on schema integration heterogeneous and distributed dbms to work from this problem so schema integration was done for a long period how to take schema from the different even relational dbmss and figure out how to merge them to a single view that can be useful forever so this is a real problem that was faced by by devotee and things have changed so millions of dollars was spent on this so some of the things be what he did was uh so there was inconsistency as well as different names so missions so when when you think of missions that are so big Liberty essentially are the they create what is known as what time and peacetime missions these are done very in advance and kept and they're periodically evaluated part of the execution and they use resources for multiple branches of RP building and so this was very difficult to do in the province of information being scattered so schema integration became an important topic heterogeneity of data models affected by address heterogeneous inflorative Concepts were explored another kind of Civilian example you can think of which was widely used in some of the research was you know all of you are familiar with restaurant rear systems right and in order to show you the the review or Michelin review of restaurant systems they have to pull data from multiple sources and these multiple sources are independently developed and do not contain the same information at the same format information or even the same vocabulary so that has to be in some way reconciled by this midi wave that brings all of them together to do that prototypes and systems were built to demonstrate the concepts so um so what see what they did to alleviate response in some years they initiated the development of a new programming language to be used across of branches of beauty and it was named data I mean if you are familiar with it and it is a language was named after the lady made the roles the customers and those development report it took like 10 years by a committee European American and others and they looked at different programming languages looked at different requirements of devotee and then figured out you know what features this language should have and why it is important for the purpose of bigger than anything so it was a huge effort and at the end this language becomes very bulky they have added so many features from so many different languages that it became made but it was completed completely as well developed even a new company was born Russian rose that only implemented Ada on machines and then sold it data is currently used across the body as the application development language unfortunately it's not widely used outside of people another thing they did was they also funded the development of particle relational database in the 80s and this DB means it's very widely used across it at least a single model instead of using much still the issue of making sure that the vocabulary is the same and the attributes can be identified and they can be matched is still a problem that has to be addressed on top of that so it's also a very popular dbms with the sales market share so there has been a lot of instances in the in the in real world where interoperability or inability to have systems interact with us a big hurry and a lot of mistakes on other things happen because of that so another example for making it is a mutantly use Google flights and other similar systems for exploring things everyone uses so how does this work again uh this requires access to multiple independent data sources and like they have to access American Airlines their Italians all different airlines and they have their own independent it's a black box as I said they provide apis to Green a particular slide and then get information about that and the cost and other things but they cannot see the algorithms that is used behind it output from these may not be the same how is a single integrated view preventative purpose so what we see is a a single view irrespective care lines which tells you in a nice way how this is essentially is the is a good example of interoperable systems using emitter way here perhaps they don't use a a data exchange format that is agreed upon that the middleware understands each one's output and tries to convert it into a common thing because they are not sending information from one application to the other but it is being consumed by the by the end application for you to provide that information so this will be simpler uh the so since we are discussing prominent later of the the prominence for this kind of record it was started by a few graduate students in Stanford in the in the 80s early 80s I would say they thought about this particular problem and came up with a prototype system in which they even showed it and became Venture capitalism and then everyone experiences you name it every every uh web GUI provider who does this kind of integration users in probability principles underneath surprisingly you might have noticed that Southwest does not allow this and hence that information is typically not available when you go to these places you will never get Southwest flights you have to go support click again website and look it up and that is because they don't publish their apis for these people to use so again all those things are part of the intraoperability things that we will discussing many questions yeah okay so there are different levels of interoperability as we understood from The View also there is something called foundational which is tightly integrated does not require the ability problem savings to open integrate data they're communicating the same way structural refers to structure of format of data exchange defines the syntax of the data exchange semantic ability of the tool system to exchange information and use the information that have been exchanged using a common probability sometimes taxonomy and and what's been very important for interoperability and service typically semantic include structural interoperability and that is the highest level of interpreads as development so this is this should have been clear from revenue so finally uh what I would like to do is okay how does all this relate to fail which is the underlying theme for this Workshop so from open to fail so open data is available without restriction but there is no guarantee about how it has been generated and what format it is in and all those things are not there whereas trade data define specific conditions to be accessed and utilize so these are known as the principle that you've already seen in the earlier or tutorials in this Workshop you can certainly apply the same principles to metadata as well if need on the other side pay data also is also widely available and utilized by incorporating the following usability requirements which is not available on not to read about in the open data Predator must be defined and entered into online public records for the purpose of distribution solution so the first step in the use of any data is to find such a data axis and being able to restore it in some means whether it is using a URL or using a set of keywords that are associated with that data set or a citation it doesn't matter but it should be discoverable pay data must be made accessible so that it can be open with and processed so certainly proprietary data that is not available in Smart Way data presented in a way that can be understood and utilized that means there should be sufficient metadata associated with the data approximal to consuming in the network foreign so data Integrity has also been defined as a feature of data sets Way by data can be easily retrieved practice we used and it is not very different from the fair principles about characteristics of data skills that black metadata can exist for both data and data sets let's suppose so how do you facilitate interoperability one of the ways is through detections for much so if you use a data exchange format that is a standard format then the other system may already have support for that so typically when you have a popular data exchange format a lot of different systems natively Provide support for the actual room power to either integrate the preset information so using a standard or known data exchange format makes it easier for applications to facilitate interactivity support for known on a breed of performance can be bring to you to systems which is done for these systems to be used widely a transition from earlier binary exchange to a human datability so this is important so what we have seen is that uh before all these interoperability and other things uh the only way a systems exchange was through binary data so some someone need to write a file rather than read a binary file but one has to know exactly what is contained in that I do understand the music and the most uh difficulty with that was that it was not human readable so when when somebody wants to exchange any invoice and somebody wants to make a payment if all of them are coming in in the binary way then it's very difficult to see and understand correct no matter what is happening so human readability becomes very important and with human readability it is possible to understand for someone but it could be also be able to be processed by the computers in order to do that so typical languages so this markup languages uh became popular HTML external rdf XML you might have used some of them HTML especially is the one that is used by web for example and this was derived from surprisingly you know the grouping way in which documents were roof read and annotations that were made that is that was one of the markup languages that became expenditure stable so common data exchange languages are the foreign language CSV tsp files rdf is more used for metadata we'll see none of that in the next session next we are already familiar with CSV and kg tsv is tab separated these format files can be used either again Python and other libraries is perfect and because python supports these formats natively so you don't have to add any additional piece of software and you can improve these things directly into the data structures in the language metadata is still needed for understanding uh how you need to analyze them so you may get a data file with lots of data like we saw in the census example or in the other application I showed you but you need to understand what they mean so semantic or key structural for using them there has been a conscious you know towards human readable performance so briefly just looking at some of the advantages and disadvantage of these so XML the acronym comes from extended markup language one is it's very flexible use a standard published by WCC which is the World Wide Web Consortium and where it's working groups it's human readable although not very easy but readable and editable error checking by using STDs display using stylesheets dtds so there is a lot of support there's a lot of development utilities around it because this was very popular built but we're still trying for usage at some point and we'll see that almost every dbms vendor has incorporated it natively into the system can represent hierarchies or you could create document models with that there are plenty of tools available for creation parsing searching and reading the downside is that it's a little bit multi meaning payload to formatting ratio is verified meaning the payload is small but we have to put a lot of formatting information passing and such query search chart reading can be CPU intensive so that's another that plays into this you know for smaller applications smaller amounts of data exchange which is more difficult but if you want to exchange very large amounts of data in this format and if you have to especially get it from the disk then as we saw earlier the io cost person and that is one of the reasons that dbms are striking or convert this into relations and various other things to avoid them so here you see an example of a XML that we normally reuse for reviewing the paper so whenever there's a view of the people from any conference they send you these review templates and it has the conference name now title as you can see summarize the paper's main contributions so your answer is where you add your text what you have to put in and then you submit it so this is so you can see the formatting is very uh is there is a fixed format rule for format but it is pretty bulky so one is the conference name it ends with so it starts with a less than and ends with a less than slash submission submission and everything has to match so oh generating this is nothing then once you generated and then this can be processed by the by a program automatically and then it can generate the list of the conference for the content so this is very widely used today for all contents reviews so economies is also very widely used so extensively it will slash on its usage as I said most dbms that support XML natively meaning you can store XML as a as an attribute of an object and then you can pass that as an object you can re-read that as an object so there's a difference between storing natively your search like when you store an image they are not stored natively they are stored as a file which means that you cannot predict you can only really Define name but not the content whereas when things are stored natively we can feel them mostly women support what is known as the document object model which is the model used to create external documents I'm creating them using something called extract so this was very popular and a lot of people went into this dam is created in memory so it has some limitations on public a document you can do others from the problematically read manipulate and modifying someone document oops so that is so this is a data exchange format which is quite widely used so it can you can exchange any information in this format and the tags as we saw here can be used as as the vocabulary so even though it's it's well even though it's easy for humans to read it so you can use these tags that are there submission question number two interpret options to interpret the data in some way if it is additive and then so that will create the common vocabulary to be used okay the second one is Json this is known as the JavaScript object notation so this is supposed to be language independent data format even external language independent many programming languages support generation personal Json natively so again this is the human readable and editable file and this is slightly simpler to understand than XML but it has some limitations as well so it's also bulky but the payload to formatting ratio is better than XML parsing and such can be CPU you can say not as flexible as MLM for side of keys and other things that things for separating them so but this is another one that is widely used here is an example so this is a this is an example of a Json file or text files so it starts with uh if this defines employee object and array of three employee records so start with the brace ends with the bass on brackets mean array and then there is a tab just like the options that there was a tag plus name colon the value we also important value and same thing so they have syntax rules data is named by your page so you can easily import it into a dictionary for example in in Python data is separated by commas curly braces for object Square objects so this is a very popular format even though this takes little more space than uh because of the tags and everything but this also helps in interpreting and understanding but certainly a little bit simpler than XML so I'm including this only for completeness known as Global this was enrolled a data format that was used by C C plus plus but it was extensively used in the 80s and 90s I don't see much use of this today except in all those systems so this is known as the common object request book or the architecture mainly used for interoperability was widely used earlier although binary so there's a binary exchange of information into historical and architecture standard so we can you can query from through the language and understand what it is supposed to be language and voice independent compact date of representation so this does not have the bulk the other human readable representation Style Java support sheet open source options available but there is a high learning curve to understand and use it not well supplicate by operating system vendors firewalls turning producer so this is just for completeness so here are a few slides that talk about uh what what USPS has done with respect to in trouble so usds per day bojia standards are used for your spatial information so they have from policy 30 plus standards that you have to pick and choose and use for a particular data representation in data furnace OTC conducted the interoperability assessment to see whether these standards are being followed are implemented by USGS servers because these servers service a lot of people and it's critical to make sure that they so they came up with complaints testing developing use cases and investigation usability development of cat feed test Suite so all these two have done with a project to make sure that the servers conform to the standards and things that are made profitable so to conclude uh data by itself is of limited use unless it can be found accessibility understood and can be used meaning for you now that's very evident from this discussion following the standards using published data action performance with language support for them makes usage and Analysis much easier and takes careful so that is the gain on the benefit of individual Society in conforming to the three principles are one-way connected actionable invisible there are millions of events from various years since it is critical and we understand the importance of standards integration issues and why in capabilities needed then the next module we'll discuss me today to another appointments so with this I will top of this particular pathway can answer any questions that you have before we start the next model
