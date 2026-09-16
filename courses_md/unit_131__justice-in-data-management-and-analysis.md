---
title: "Justice in Data: Data Management and Analysis"
unit_id: 131
course_id: 10
level: "Foundation"
slug: justice-in-data-management-and-analysis
is_course: 0
---

# Justice in Data: Data Management and Analysis

## Extracted resources (local files)

### Introduction to Data Analysis and Management Slides
*Source file:* `CTW-DS-intro_FINAL.pdf`  ·  *type:* file

Data Management & Analysis:
Provenance and Current Thinking

Team Presentation
2
Sharma Chakravarthy
Professor

What Am I assuming
Nothing!
As this audience is predominantly undergraduates, 
I am not making any assumptions on what you 
know
I do realize that many of you are familiar with 
computer science and some programming 
language. Hopefully, that will help understand this 
material better
Data collection, storage, cleaning, loading, 
management, and analysis have been addressed 
even before the advent of computers
3

Presentation Outline
Motivation
Data, Information, Knowledge, and wisdom
Early Enabler for creating data
Changing requirements and their impact
Progress with respect to changing requirements
From flat files Data Science/Analysis
Our approach for Data Analysis at the Information 
Technology Lab (IT Lab)
Real-world data analysis examples
Census data analysis
Airlines flight analysis
Cowiz++ : Covid Visualization using Multilayer Network 
Analysis and its Demo
Conclusions
4

5
Motivation: The devil is in the detail

You are given a data set. Some description of the data set. And you 
know the application area

Your boss/advisor wants you to figure out how to leverage this data set 
for improving the business or understand what is going on

generating more customers, 

retaining current customers (prevent switching), 

how does this biz fare with competitors, 

is there a booster shot needed 
−of course Pfizer wants it because that is their business
−That is why CDC and FDC analyze the data provided and take input from 
independent advisors (who will do the analysis)

How do you decide?

It is possible to analyze this data in 50 different ways

Which one will you choose and why?

How will you validate your results

How do you justify your validation

At the end of the day you need to convince your boss/advisor, and your 
solution is good and will work with high probability!

6
Analysts without (Application) borders

Gone are the days when you could focus on a topic or even 
a sliver of a topic

Today, problem solving and analysis spans many topics and 
disciplines
Within CS and across other disciplines
The application areas are diverse

Hence, you cannot just focus on programming language or 
operating system or data management

Data analysis uses data cleaning, choosing meaningful 
attributes of data for analysis, mining, machine learning 
algorithms, probability and statistics, drill down, visualization, 
to name a few

Hence, do not become a person with a hammer looking at 
every problem you see as a nail

Instead become a person who can match the tool for the 
specific problem at hand!

7
Analysts without (Application) borders (2)

Sherlock Homes
“it is a capital mistake to theorize before one has data.
interestingly, one begins to twist the facts to suit theories, 
instead of theories to explain facts” 

The above is very true (may be with some rare exceptions)
I see my students explaining the experimental or program results 
even if it does not make sense
Because they have not analyzed the problem and have no idea of 
what to expect and what is an outlier
Many programming mistakes are discovered AFTER the results are 
explained cogently

Hence, two (or more) independent approaches should always be 
used for validation
Theoretical/analytical
Experimental

Always do sanity checks on your outcomes to make sure you have 
not overlooked something

Always make sure your test cases include boundary cases rather 
than regular cases

8
Some Clarifications

Why learn programming for analysis
Although you may be using packages for many tasks, you may 
have to use appropriate data structures and populate them with 
data properly
Choosing appropriate algorithms for what you want to do!
Figuring out plotting and visualization
Generating good understandable reports

Does the data sets used for learning matter?
Yes and no! 
Important to understand the analysis no matter what data set you 
use!
You will be encountering different and complex data sets all the 
time
Do not get hung up on the latest applications
−Process (or analysis) does not change
−Pre-processing and other details may change

9
Some More Clarifications

How will you cover all we are going to encounter in our 
career?
We cannot! But importantly, we do not have to!
The process of analysis will remain the same. Details of analysis 
depends on the business/domain objectives. 
Please focus on learning the analysis, not on the data  sets
Please focus on visualization and presentation

What about different types of pre-processing?
Same as above
May have to add more tools to your pre-processing tool box
At the end of the day, domain knowledge coupled with 
analysis process is what is important to be a successful data 
analyst!

The problem is not new!

Data, Information, Knowledge, and Wisdom

Naisbitt (1982)
We are drowning in information but starved for knowledge
This level of information is clearly impossible to be handled 
by present means
Uncontrolled and unorganized information is no longer a 
resource in an information society, instead it becomes an 
impediment
déjà vu
It is not enough to store, organize, and manage information 
(actually data), but it is critical to extract relevant knowledge
and make it available for decision making in a timely 
manner
11

Data, information, and knowledge
12
Data to information to knowledge to decision to action

Raw Data
Knowledge (if not wisdom!)
Access, Cleansing, validation, 
understand relations,
Understand patterns, 
and if possible 
Derive 
principles
At least  (timely) actionable knowledge (rules, actions, 
Inferences, predictions) for decision making
Casting this problem as Data Processing!
13

Data, Information, Science

Data or raw data or base data: A value and may be its type
480,000, Einstein, Male, 3.14, …
A data by itself is difficult to understand and we are collecting large 
volumes of such data for analysis
−This is where FAIR principles and
−Meta data comes into play

Information: adding additional context to the data (meta data) for 
understanding
480,000 deaths in US from cigarette smoking 
3.14 is the value of pi
Einstein, scientist

Data Science: is the science (techniques, approaches, tools, 
abstractions, algorithms) of going from 
raw/base data information knowledge wisdom!

Not at all new! Only the size, variety, and complexity keeps changing, 
actually increasing! Visualization adds additional 
complexity/computation
14

History of Information
Information 
Analog
Digital   (Only from around 1946)
(has been around for a while)
pre-DBMS         post-DBMS         Post-internet
The Information (book) by James Gleick makes very interesting 
reading
15

History (Contd.)
Claude E. Shannon (Bell Labs) used the word bit in 1948 
as a unit of measurement of information (in 
mathematical theory of information)
There was no way to measure information before
Introduced the notion of redundancy to correct errors in 
transformation of information
Interestingly,
The notion of error correction was used  by drummers in 
Africa by using extra words (for disambiguation)
They have used it for communication from one village to 
another for hundreds of years

Transformative events
Information (symbols. Ciphers, tablets, scripts, 
books, …) were produced manually thereby limiting 
the amount of information produced
Two transformative events in the last 1000 years 
changed that significantly
Can you guess what those two events were?
You know both!
17

Early Transformative event
Two Events leading to the explosion of 
information
1. Circa 1454: Printing press (Johannes Gutenberg)
18

More Recent Transformative event 
2. Around 2000: Internet  
web content
Facebook
you tube
Twitter, …
Other enablers
Inexpensive sensors/devices
Mobile devices capable of recording image, video
Advances in storage technologies (continuous)
However, analysis, fusion, and filtering of data has 
lagged behind!
0
1
2
3
4
5
6
7
8
9
2005
2010
2012
2015
In Zetta Bytes (1 Tera GB)
19

So What?
These events that came about due to technological 
advances also meant that it is just not enough to create 
volumes of data
What do we do with this information?
Satellite images
Hadron collider (CERN) data
USGS (united states geological survey) data
How can it be used for different purposes?
Now the burden of storing, processing, and analysis is 
even greater which meant that, in addition to 
technological advances, we need to develop algorithms, 
mining and other (deep learning) techniques to make 
use of them
This is one of the challenges for Data Science/Analytics!

Ignorance is Bliss
Most of you may not have seen a main frame, let alone 
what a computer looked like prior to that
A lot of people today grow up with a very powerful 
computer in their pocket 
For them, it is difficult to imagine a world where one 
had to go to a computer center to submit a job, wait for 
a day or two to get results!
Imagine the patience required
Indeed we have come a long way, in a very short span of 
time!
Let us understand that provenance a little

Minsk Series of computers (60’s)
not considered a mainframe!

Used vacuum tubes and 
diodes later

Used Nixie tubes for display

Memory was from 4K 
words to 32K words  (36 
bits)

Could program through 
console using machine 
language 

Paper tape and card inputs

Rugged magnetic tapes

No disks!

Ferrite core memories
22

Another early Computer
using printed circuits

Then came IBM 360 (Main frame, 70’s)

Integrated circuits

Large memory (512K)  compare!

Multi-platter disks

Lots of magnetic tapes (0.5 in)

Card readers and printers
24
One of the first commercial disk drives from 
IBM. It has a 5 MB capacity and it’s stored in 
a cabinet roughly the size of a luxury 
refrigerator. In contrast, a 32 GB microSD 
card measures around 5/8 x 3/8 inch and 
weighs about 0.5 gram.
(Photo: Mike Loukides. Disk drive on display at 
IBM Almaden Research)

IBM’s mainframe with Tape drives
25

Early Disk Drives
26
Capacity: 50 MB (needed the size of a washing machine)

Then there was EC 1030 
(Russian copy of IBM 360)
27

Identical to IBM 360 
(instruction set 
compatible!)

Instead of hard-wired, 
it was micro-
programmed

Used the same 
(pirated) 360 OS

Disk drives and lots of 
tapes

Printers

Identical console

Card punchers 
without headers

Now
We have computers in all shapes and sizes
From sensors to server farms (10,000+ machines)
You can even program your dimmer switch!
Reports of flexible/rollable oled screens
Google glasses
VR systems
Embedded systems, process control systems
And it is improving each day!
Think of ChatGPT!
28

29
Data and its Management

File-based data management (complete burden on the user)

Database Management Systems (provided standards, 
integrity, querying, OLTP, interoperability support, etc.)

Data warehouses (multi-dimensional analysis, Cubes, OLAP, 
etc.)

Data mining (early approaches, large data, scalability, etc.)
Machine learning algorithms 

Stream data processing (sensor data, velocity, and QoS 
requirements)

Big Data (4 V’s): volume, velocity, variety, and veracity

Vocabulary
Changes every few years
Flat file systems
Database Management Systems (DBMS) 
Data Warehousing (DW)
Data Mining (DM)
Data Stream Management Systems (DSMS)
NoSQL Databases
Cloud Computing
Big Data Analytics, now
Data Science
Big data analysis
Neural networks, Machine learning, AI
What do these mean?
What changes in requirements and advances in 
technology make these happen?
Or is it just Old wine in a new bottle?
30

File Systems
Basic abstraction for grouping/storing information digitally
Very simple, yet very powerful
Has not changed since its introduction
All types of information (raw and processed) are stored in 
files
text, audio, image, video, program,  MRI, EKG, …
Maps, layers, …
Now, AI created objects
User decides how to store information in a file 
Typically, as records, fields, and values within a record for 
structured data
Application has to be aware of the format to interpret it 
correctly
Slide 31

Application Types
Computation intensive applications
E. g., finite element analysis, Computer aided design, wind tunnel 
testing, simulations, numerical analysis, image rendering
Load all data into memory and process
Data intensive applications
E. g., library of congress book management, Walmart point of 
sales database, Amazon inventory database, airline reservations, 
Homeland security database and others … 
Stage data from disk to memory and process in memory
Computation & data intensive applications (e.g., Big data)
Data mining, drill down and exploration of data warehouse, 
dimensional analysis, Internet search, stream/sensor data 
processing, scientific computations, …
Combination of the above two
Slide 32

File systems and Applications
Applications need to be aware of data 
representation or format in a file (e.g., .csv files 
are used for data analysis)
Makes it difficult to change the format once designed; 
enhancement is difficult
If the format is changed or extended, all
applications have to change
Application management is difficult, labor intensive, 
and prone to errors
Strong coupling or dependency makes application 
developer’s life difficult
Will be discussed in the integration module
Slide 33

Dealing with Data
Multiple ways to overcome
Standards for  representation of data and 
exchange of data
Use of meta data (to understand the data by humans; 
meta data can also be used by the 
application/programs) 
Use of database management systems (DBMS) to store 
and access data (using a standard interface)
Data exchange formats to exchange data (e.g., XML, 
JSON) for which programming languages provide 
support
Related issues
Interoperability
We will be discussing the above in this workshop!
Slide 34

DBMS way to overcome this problem?
The problems associated with files
By decoupling the data representation from 
application software

This is a very common practice in computer science (adding a 
level of indirection or middleware)
We will discuss this further as part of integration and 
interoperability in this workshop
This requires software which can bridge this gap
This is done by providing a higher level of abstraction 
for the user and this abstraction is mapped into files 
by a software (similar to a compiler)
A relation was used as an abstraction (in the Relational model)
Had mathematical underpinning in set theory
Relational Database Management System (RDBMS) was born!
Network and hierarchical DBMSs were pre-cursors!
Now we have newer NoSQL and many other systems
Slide 35

Levels of Abstraction
Many views, 
single conceptual (logical) 
schema and physical 
schema.
Views describe how users see 
the data.                                        
Conceptual schema defines 
logical structure
Physical schema describes the 
files and indexes used.
Schemas are defined using DDL; data is modified/queried using DML.
You can think of data exchange formats that we will discuss as schema
Physical Schema
Conceptual Schema
View 1
View 2
View 3
36

What Is a DBMS?
A very large, integrated collection of data
MyMav, used by UTA, is an Oracle DBMS underneath 
Whatever system you use for registration and payment of 
fees etc. are likely to be a DBMS
Models a real-world enterprise (University registration)

Entities 
−e.g., students, courses, buildings, websites

Relationships 
−e.g., Katy Perry performs at UTA, students take courses,  lenders issue 
mortgages, an employee manages a department
A Database Management System (DBMS) is a software 
package designed to store and manage large amounts of 
data.
Slide 37

Why Use a DBMS?
Data independence and efficient access.
Reduced application development time.
Data integrity and security.
Uniform data administration.
Concurrent access, recovery from crashes.
Persistence, scalability, portability
Application development time is reduced!
Information processing was raised to a new level of 
abstraction!
Slide 38

Evolution of DBMSs
Modeling
Semantics
Program
Tx Mgmt
Application
File I/O
[Adapted from Peter Lyngbaek:OOPSLA:1991]
Modeling
Semantics
Program
Application
Tx Mgmt
File I/O
DBMS
Non-relational (1970)
Application
Modeling
Semantics
Query Opt
Tx Mgmt
File I/O
DBMS
Relational (1980)
Application
Modeling
(static/dynamic)
Query Opt
Tx Mgmt
File I/O
DBMS
OODBMS (1990)
Pre 1970’s
39

Moving On …
Application
Stream Processing
Mining
XML support
Workflow support
Modeling
(static/dynamic)
Query Opt
Tx Mgmt
File I/O
DSMS
Mining
XML support
Workflow support
Modeling
(static/dynamic)
Query Opt
Tx Mgmt
File I/O
Application
DBMS
[2000]
[2009]
….
40

DBMS Architecture
SQL commands from applications
Concurrency 
control
Query Optimization
and Execution
(parser, optimizer,
Plan executor)
Files and Access Methods
Buffer Management
Disk Space Management
DB
Recovery
Manager
Transaction
Manager
Lock
Manager
System catalog, data files,
Index files
Log
Complex, 100,000+ lines of code, high availability, recoverability
41

DBMSs as enterprise workhorse
DBMSs have worked well for over three decades (it still 
does, albeit,  behind the scenes)
Used for payroll, airline reservation, inventory 
management, financial data management, store and 
manage corporate data
Now by Amazon, Ebay, Etsy, …
They served well for efficient storage of large amounts of 
data, access, analysis, generating reports, etc.
However, expectations keep changing as the technology 
advances!
We will discuss more details of DBMSs on Wednesday 
including ArcGIS
42

Databases: Behind the Scenes
From Friendster.com on-line tour
43

Changing requirements
Functionality provided by traditional DBMSs were no 
longer adequate
Exploration of data (instead of Querying) 
−Search vs. querying
Data analysis in an interactive manner
Functionality provided by AI (and related areas) were 
no longer adequate
BI was needed on very large, real-life data sets
Also,
Interactive usage was becoming increasingly 
important
Non-technical users (not just geeks) want an easy-to-
use system
44

Search vs. Querying
There is a difference between the two
When you interact with a DBMS, you ask a query 
in a specified language (e.g., SQL)
Even when you search MyMav, they are translated 
behind the scenes into an SQL query!
Queries give exact matches
Search was around even before Google made it 
indispensable
Text search was popular
Search gives approximate/similar matches
Both Querying and search are “pull” technologies
Slide 45

Drivers
Business information (or BI) systems became as 
important  to corporations as transaction 
systems were earlier
Ability to store multiple years of data on-line
Mass personalization and leveraging data as an 
asset
Identify new and profitable markets, and 
channels to enter them
Increase customer loyalty, profitability, life-time 
value
Decrease risk
Slide 46

Approaches

Data Mining and AI (and database mining)
Association rules/sequence mining (Market basket analysis)
Text mining, Graph mining (people with most friends, …)
Recommendation systems (Netflix, Amazon, …)

Data warehousing, data marts
Consolidated operational systems (DBMSs)
Facilitates business information interface (exploration)

Complex event processing
“Push” vs. “pull” paradigm

Stream Data processing
“real-time” monitoring using sensor data
Now it being applied to other data as well 

Accessibility using web
Web interfaces to data access
Search
Ranking
47

Data Mining
Different from search and Querying as well as big
data Analysis

Data Mining or knowledge discovery
“The key in business is 
to know something 
that nobody else knows”
(Aristotle Onassis)
9

Motivation (Traditional mining)
Fraud division, some large telephone company:
“How do we find these guys? There are 10 billion 
records on 10 million customers in the main 
database. With all this information we have about 
our customers and all the calls they make, can’t you 
just ask the database to figure out which lines have 
been set-up temporarily and exhibited similar calling 
patterns in the same time periods? The information 
is in there, I just know it …”
50

Problem
“Find-similar” problem just described is hard
e.g., “Who should be given incentive?”
e.g., “How can we group usage patterns into k similar groups?”
E.g., “should we approve this purchase by this credit card by this 
user?”
Why?
Massive amounts of data 
More and more online data stored (e.g., Web, corporate 
databases, etc.)
Challenge
Real-time vs. post-mortem (or forensic) analysis
No easy way to describe what to look for
Traditional, interactive approaches fail
Size of data, different purposes, need for domain knowledge
51

Data Mining
Data Mining (DM) is part of the knowledge 
discovery process carried out to extract valid 
patterns and relationships in very large data sets
Usually don’t know what to look for, like a “voyage 
into the unknown”
Regarded as knowledge discovery or learning
from basic facts (axioms) and data
Roots in AI and  statistics
Uses techniques from machine learning, pattern 
recognition, statistics, database, visualization, etc.
52

What to do
A few months before the contract expires, if one can 
predict which customers are likely to quit, 
Give incentive to those who are likely to quit
Don’t do anything for those who are NOT likely to quit
How do I predict future behavior?
Corporate Palm reading !
Human intuition !! 
Data mining (DM) or Knowledge Discovery in Databases 
(KDD)
53

How Did the current Avatar of 
Data Mining come about? 
Mining has been around for quite a while!
Enablers
Reduced cost of storage 
Reduced cost of processing
Ability to store, process, and manage large volumes of 
data (e.g., DW, Internet)
New techniques such as association rules, sequence 
data processing, ontology, stream data processing, 
information fusion
However,
Scalability, visualization of results, variety, filtering 
very large outputs are new and important issues!
54

Technological Advances (around 1985)
Increase in
Network capability
Advances in storage 
technology
Increase in 
Processing
capability
Ability to acquire/store very large amounts of data 
processing power + systems/architecture + Algorithms
55
Application of  
Statistical/
Machine learning
Algorithms + systems 
+ architecture
Data Mining
Advancements are a 
byproduct of changing 
Requirements!

Data Mining
Data Set Description
Final Results
Clustering, Classification,
Association Rule Mining,
Anomaly Detection, Regression
Subgraph Mining, …
Analysis + 
interpreta
tion
56
In data mining, a domain expert assists the analyst to
determine the best mining approach based on the objectives
and data available
Interpretation of the results is the most difficult and important
aspect of data mining

Applications
Customer profiling
Find new customers, 
Market basket analysis
Manage inventory
Risk analysis
Insurance, loan, stock,…
Text analysis
Library, Web,...
Fraud detection
CRM, Scientific discovery, forecasting, …
Slide 57

What is Data Mining Trying to do?

What is Causality? 
“Cause and effect”  e.g., heavy rains cause flooding

What is correlation?
“mutual relationship or connection between two or more things and their 
strength”
e.g., as temperatures go up, ice cream sales go up
Positive and negative correlations

Do  the above two mean the same thing?
NO!  Important to understand why!

Which of the two we want to identify in mining?
Causality!

Which one does mining try to identify?
Correlation!
But we also know that “correlation does not necessarily mean causality”
That is the best we can do

Why?
check out spurious correlations
58

AI and Statistics
If DM is rooted in AI and statistics, what is the need 
for DM?
AI traditionally dealt with small samples
The emphasis was an learning, extrapolation, and 
generalization
The emphasis in DM is on processing  actual data, not 
just samples!
DM tries to leverage the data collected, accumulated 
and derive tangible rules/conclusions (generalization 
is also possible)
59

DM Vs. Machine learning
ML methods form the core of DM
Amount of data makes a (big) difference
accessing examples can be a problem
missing values and incomplete data
DM has more modest goals: automating the 
tedious discovery tasks
Data Mining has evolved significantly from its real 
use in the 60’s
C4.5 for decision trees and K-means for cluster 
analysis
Bayes’ theory and regression analysis date back to, 
respectively,  1763 and 1805!
60

DM Vs. Statistics
Similar goals; different methods
Statistics is mainly about quantifying data
Provides tools
Amount of data used and the type used is 
different
Statistical techniques can be used to derive 
prediction models or confirm results
Challenge to DM: better ties with statistics
61

DM vs. Big Data Analysis
Complex (4V’s), Large amounts of data
Analysis requirements/expectations
choice of modeling and computation using DM 
and any other techniques
Vertical  vs. Holistic analysis 
62

What is NOT Data Mining?
Data warehousing
Ad hoc query (OLTP) /reporting
Online Analytical Processing (OLAP), aggregation, 
summary
Data Visualization
Agents/mediators,
Pervasive computing.
Search / look up, …
63

What DM is not likely to do !
Substitute for human intuition and generalization capability!
Have to wait and see where ChatGPT takes us!
I don’t think a DM system will (ever?) discover  
e = mc2
PV = RT
Gravity, Newton’s law’s of motion, …
It may discover new black holes !
The value of π (pi) is data-driven but was likely discovered 
using intuition!
64

Data Mining Tasks
Prediction Methods (prescriptive)
Use some variables to predict unknown or future 
values of other variables.
Description Methods (descriptive)
Find human-interpretable patterns that describe the 
data.
From [Fayyad, et.al.] Advances in Knowledge Discovery and Data Mining, 1996
65

Types of data analysis
Supervised
Driven by known information about data (labeled data)
Optimize existing solutions/markets
Unsupervised 
Driven by no known (or labeled)  information about data 
Exploration 
Relevance
Finding  new patterns that may be counter-intuitive!
Relies on domain knowledge to validate!
You will learn more about these later in this workshop
66

Sample DM Approaches

Classification 

Supervised. Why?

Clustering 

Unsupervised. Why?

Association rules 

Unsupervised. Why?

Text classification 

Supervised. Why?

Anomaly detection 

Unsupervised. Why?

Graph Mining 

Unsupervised, why?

Neural networks 

Supervised. Why?

Deep Learning 

mostly unsupervised. Why?

Big Data Analytics

Both + descriptive/prescriptive

This is what you will be doing most of the time! 

…
67

Data mining cycle
Select
Preprocess
Transform
Mine
Analyze
Rethink
DB
68

Mining Vs. Big Data Analytics
Data Set Description
Final Results
Clustering, Classification,
Association Rule Mining,
Anomaly Detection, Regression
Subgraph Mining, …
Analysis + 
interpreta
tion
69

Changing requirements (again around 2000)
Availability of inexpensive sensors and gizmos 
(with increasing functionality)
MavHome Project tried to automate a “smart 
home”
Useful for various types of monitoring
−Assisted living, elderly homes, health-care, 
environment monitoring, security monitoring
New (inexpensive) devices
Generate and transmit data 24 x 7
Data semantics is slightly different from earlier 
ones
Can generate disparate data (location, value, 
image, audio etc.)
70

Data Warehousing
Integrating multiple databases for holistic Querying

Why Data Warehouses?
DBMSs were mature 
Enterprises used multiple DBMSs, many a times 
from different vendors
They could be heterogeneous
Queries could not be posed across DBMSs
Inventory, sales, customers etc.
Analysis and report generation using multiple 
DBMSs were also a problem
DW was proposed as a solution
72

Source
DBMS
Source
DBMS
Source
DBMS
Extractor/
Monitor
Extractor/
Monitor
Extractor/
Monitor
WH Integrator
Warehouse
Query Manager
...
Metadata
Report Generator
Analyzer
Data Miner
Data 
Mart
Data 
Mart
DW architecture
73

Complete Decision Support System
Information Sources
Data Warehouse 
Server
(Tier 1)
OLAP Servers
(Tier 2)
Clients
(Tier 3)
Operational
DB’s
Semi-structured
Sources
extract
transform
load
refresh
etc.
Data Marts
Data
Warehouse
e.g., MOLAP
e.g., ROLAP
serve
Analysis
Query/Reporting
Data Mining
serve
serve
74

Today
Earlier, were developed as  separate systems
Today, All major vendors of DBMSs support data 
warehouses 
Data Marts are smaller forms used for a specific 
purpose
Data Lakes, unrelated to data warehouses, are 
storage repositories that mainly store raw data of 
an organization
We will cover cloud data warehouses later in the 
workshop
75

Complex Event processing or CEP
Pro-Active Technology vs. Reactive Technology

Importance
We have been using the “pull” paradigm for a long 
time (for accessing information)
We still use it in a number of places (e.g., web 
search, querying)
Is there a better alternative ?
If so, what is it and how do you quantify it?
How do we generalize it? Implications?
Where is this paradigm useful?
77

Traditional  View (Pull)
78
Traditional System
Repository
Query
Answers
Updates
Transactions
applications
PULL Paradigm

Active Technology View (Push)
79
PUSH paradigm
Self-monitoring /.Reactive
System
Repository
Query
Answers
Updates
Transactions
applications
Business rules
constraints
Invariants
situations to monitor

Push Paradigm (Distributed)
80
PUSH paradigm
Self-monitoring  / Reactive
Application
Optional Repository
Query
Answers
Business rules
constraints
Invariants
situations to monitor
Changes,
Inserts/deletes

JIT (just-In-Time)   Push
Multiple sources over a 
large network
Large number of users
QoS (timing constraints)
Dynamic specification of 
what to monitor
Support both simple 
and complex 
combination of 
information 
Optimization (efficiency)
81
Internet

What has been done
Event specification language
Event operators, their semantics, and implementation
Integrating event processing with DBMSs and 
stand-alone applications
Nested Transaction model for execution
Integrating event processing into Object-oriented 
applications
Distributed event specification, semantics, and 
implementation
Concurrent and simultaneous events, timestamps
Today, CEP is main stream and is supported by 
most DBMS vendors in the form of triggers, etc.
82

Stream Data processing
Different from complex event processing and DBMSs

What’s a Data Stream? 

Examples of data streams:
Readings from a sensor
Changes in stock price
Traffic packets over a link (T1 )
…

It is considered continuous as monitoring is done over long periods 
of time
1
2
3
4
5
6
7
8
9
current
past
future
data stream: a sequence of data items that are ordered by time or an attribute.
a data stream model
84

Database
Streams
Stream
Applications
Memory (low latency)
Disk (high latency)
SQL Processor
Query Engine
Cache/Buffer
DBMS
Current/Earlier DBMS Architecture

Stream
Applications
Database
Streams
Memory (low latency)
Disk (high latency)
Database
Archiving
Input Processor
CQ Engine
Cache/Buffer
DSMS
Stream Data Processing Architecture
Not addressed by traditional DBMS
1.
New algorithms for continuous data
2.
Single pass main-memory algorithms
3.
Processing without losing incoming data
4.
Real-time latency requirements

Applications: Battlefield Monitoring
A
B
C
D
E
Command & Control Center
soldierID, location, heartBeat, bloodPressure
87

Face recognition, automated door entry
Smart sprinklers
Lighting control
Door/lock controllers,
Surveillance system
Robot lawnmower
Climate control
MavHome Project at UTA
88

Applications
1.
Find all soldiers who need help

A soldier is in critical condition and needs 
help if his blood pressure is less than 60 and 
his heartbeat is less than 50.
Find all soldiers who need help and all possible 
helpers who are nearby (within 100 meters)

Distance (wounded soldier, helper) is less 
than 100 meters.
89

Road safety (Traffic Monitoring)
Accident Detection
Traffic flow and 
pattern detection
Notification of 
motorists 
upstream
90

Changing requirements (again around 2002)
Networking was mature, stable, and fast
Internet was mature
Ability to access data from anywhere was 
possible
High-performance computing required clusters
Working in batch mode
Could not increase resources “on demand”
Cost of maintaining clusters was high
What was lacking was an ability to use resources 
as needed, when needed, and pay only for the 
resources used!
91

Cloud computing
Predecessors: HPC and Grid Computing

Need for cloud computing
Consider the official Wimbledon site. This site gets 
extremely high traffic in the two (to three) weeks 
when the championship happens. For these two 
weeks period, this site will have high server usage. 
For rest of the year the site will have low traffic and 
hence most of the resources will be idle
Spare capacity need to be maintained or leased from 
somewhere!
Internet-scale elasticity
Ability to increase capacity need without prior 
indication 
93

Traditional approach
Keep enough spare capacity to deal with the 
needs of 2 to 3 weeks in a year
Expensive
Hardware gets old and obsolete
Maintain and manage people
Software acquisition and maintenance
It is not easy/possible to outsource this just for 2 
weeks
It is not possible to rent just for 2 weeks
4

Drivers
These situations and needs were a side effect of 
Internet availability and ubiquitous usage
Making things available on the web is critical
Enterprises were maintaining expensive IT shops 
and all the cost and headaches that came with 
that
Cloud computing is the answer for this problem!
5

Cloud computing was the answer
Cloud Computing makes computer 
infrastructure and services available "on-
need" or “on-demand” basis
The computing infrastructure could include 
hard disks, development platform, database, 
computing power, or complete software 
applications
To access these resources from the cloud 
vendors, organizations do not need to make 
any large scale capital expenditures
96

What is cloud computing
Organizations need to "pay per use“. That is, 
organizations need to pay only as much for 
the computing infrastructure as they use. 
The billing model of cloud computing is 
similar to the electricity, water, or gas 
payments that we do on the basis of usage.
Terminology 
Vendor: cc service provider
Organization: cc user
97

Cloud computing: components  
To get cloud computing to work, you need: 
Thin clients (or clients with a thick-thin switch) 
Grid computing: link disparate computers to form 
one large infrastructure, harnessing unused 
resources (we will see subtle differences later)
Utility computing: paying for what you use on 
shared servers like you pay for a public utility (such 
as electricity, gas, and so on).
On-demand resource provisioning: not static 
provisioning, no need to indicate resource 
requirements ahead
98

CC Economics
9
Traditional IT
cc
costs
users

Relationship
00

What is Big Data?
Data Science and Analytics

What is Big Data?
02
File/object size, content volume
Processing
Needs/time
Not just the size!
Diversity of data 
Types and holistic
analysis!

Characteristics of Big Data
103
• 4V: Volume, Velocity, Variety, Veracity 
 
 
Volume 
Velocity 
Variety 
Veracity 
 
 
You will see more V’s in the literature (value, …); but I think they do not 
characterize data! (e.g., variability, validity, vulnerability, volatility, 
visualization)
Stream data

Big Data from Science!

CERN - Large Hadron Collider
~10 PB/year at start
~1000 PB in ~10 years
2500 physicists collaborating
Large Synoptic Survey 
Telescope (NSF, DOE, and 
private donors)
~5-10 PB/year at start in 2012
~100 PB by 2025

Pan-STARRS (Haleakala, Hawaii) US 
Air Force
now: 800 TB/year
soon: 4 PB/year
04

Big Data from different sources!
05
12+ TBs of tweet 
data every day
25+ TBs 
of data
Every day
Billions of camera
Images,
Video uploads,
Web usage,
Web logs etc.
Satellite images, 
cartographic 
Information, etc.

Big Data Business sectors
US Health care
$300B per year
Europe public sector administration
250B pounds per year
Global personal location data
$100B+ revenue for service providers
USGS and other geospatial data
US retail
Manufacturing
y

Science
Abstractions
ML, NN
Theory …
Analytics
Video Processing
Stream Processing
Communities, Hubs 
Mining …
Extracted Knowledge
(Visualized) 
Trends, Predictions 
Decision Guidance
Unstructured
Network Data, Logs
Images
X-Ray, MRI Data
Video, Audio
Surveillance, 
Endoscopy
Analysis 
Expectations
Transforming Disparate Data into Actionable Knowledge and Decisions
Weather, Environment
Structured
My view of Big Data
Analytics / Science
The BIG                          Picture!
107

108
What is Data Science?
Data Science or Analysis is not new
Data collection, storage, management, querying, search, and 
report generation has been going on for quite some time 
(actually decades)
Emphasis was on understanding and managing data!
−By slicing and dicing data
−Compare female and male performance in Engineering
Data mining brought an exploratory and discovery component 
that was different from the above
−First on samples, small data sets (early AI)
−Later on real-world and very large data sets
• Market-basket, click-stream, recommendation, etc.
Now, we are combining all aspects of application / business 
with CS and statistics for inferring or discovering embedded 
knowledge

Enablers of Data Science
Convergence of multiple 
technologies
Development of new 
techniques
109
Data
Science /
Analysis
Computer 
Science
Mathematics
Statistics
Probability
Business or 
Application
knowledge
Machine 
Learning
algos
Human in 
The loop
Software
Develop
ment

What is Data Science?
It is not a single approach or a single solution
There is no silver bullet!
It is, in my view, using/extending current approaches and 
developing new ones  (a suite of approaches, if you will) 
for modeling and analyzing a diverse complex data set for 
a given set of analysis requirements/objectives
Given: Complex data set + Analysis objectives
Determine/develop: Modeling (abstractions) and Analysis 
methods (or approach for meaningful analysis) and 
visualizations (for easy understanding)
110

Mining Vs. Big Data Analytics
Data Set Description
Final Results
Clustering, Classification,
Association Rule Mining,
Anomaly Detection, Regression
Subgraph Mining, …
Analysis + 
interpreta
tion
111

In a Nutshell …
Without understanding the past, it is very difficult 
to appreciate the  present and plan for the future!
Technology provides solutions; it does NOT 
necessarily solve problems!
Sharma Chakravarthy
5/21/2023
1990
1980
2000
2010
1970
112
1990
1980
2000
Relational 
DBMS
Consistency, 
Multiple Users, 
Durability, 
Atomicity
Concurrency 
Control, 
Recovery,  
Query 
optimization
Data 
Warehouses
Data 
Mining
Stream Data
Processing
Vertical 
Integration,
Multi-dimensional  
Analysis,
Data freshness
Wrappers,
View 
Maintenance, 
Data Cleaning 
and 
transformation
Unsupervised 
Learning,
Market-basket 
Analysis,
Taxonomy
Apriori 
Property, 
Confidence,
Support,
Negative Border
QoS Specification
(Latency, 
Memory, 
Throughput),
Continuous 
Monitoring
Real-time 
Response
One-pass 
Algorithms,
Scheduling, Load 
Shedding, 
Capacity 
Modeling,
Window 
Abstraction
Big Data Analytics/Science
Handle large Data corresponding to 
4 V’s, Multiple Models,
Holistic Analysis, actionable 
knowledge
Map/ 
Reduce 
paradigm,
Shuffling
Video as 
Stream,
Extende
d Data 
represen
tation 
and CQL
Multiplex 
modeling,
composition
2010
1970

113
Analysis Types
Descriptive
A method for quantitatively describing the main features 
of a collection of data
Statistics and Statistical measures come in handy for this
Descriptive analysis can be applied on the census data 
(comes later)
−Averages
−Frequency distributions
−Percentiles
−Histograms 
−Distributions (normal, positively skewed, negatively 
skewed)
• Of household income
−Uniform, Gaussian, etc.
−Centrality measures

114
Analysis Types
Prescriptive
Finding the best course of action for a given 
situation
Usually preceded by descriptive analysis
Process-intensive task, analyzes potential decisions 
and interactions between decisions (in real-time)
Goal is to prescribe an optimal course of action
Techniques used
−Optimization
−Simulation
−Game theory
−Decision-analysis methods
You should be comfortable doing BOTH!

115
Analysis Type Examples
You have the latest census data
You want to know the top 5 states with largest 
increase in population
Can be done with descriptive analysis
You want to know which state’s household income is 
likely to rise in the next 10 years
You need prescriptive or predictive analysis
You want to explore latest census data in general
You can use BOTH descriptive and prescriptive analysis
But the exploration or search space can be very large 
Need to have some idea of what you are looking for
−Hopefully, not a needle in a haystack!

116
Data Analysis Alternatives
Data analysis can be done in many ways
Manual approach
+ has understanding of the problem, context
+ can use intuition, match real-world semantics
+ can explain your analysis reasoning
- Can be error-prone (monotony sets in)
- Remember the NASA Mars orbiter mishap (1999) 
where British measures were used instead of US 
metric system
- Cannot deal with large amounts of data
- Complex computations are difficult or not possible
Manual involvement is still needed in a some way!

117
Data Analysis Alternatives
Data analysis can be done in many ways
Automated approach
+ avoids computation  errors (assuming program is correct!)
+ Can deal with large volumes of data
+ analyze in multiple ways
+ Takes less time. But
- Someone has to come up with algorithms
- Someone has to design the program/system
- Someone has to validate the system
- Someone has to sanity check before using the results
Human in the loop (or Hybrid mode )
−This is very much the essence of Data Science
• Humans play a small but critical role

118
Data Analysis Alternatives
Advantages of manual approach
Take course grading as an example
It can be done with absolute thresholds 
> 85 A, > 75 B, > 65 C, > 55 D, rest F (in that order)
Humans can deal with small variations (e.g. 84.9, next is 
82)
It can be done using a curve
−> Class average + 1 standard deviation is A, etc.
−Again what if someone missed A grade by 0.1 or 0.2
−Can look for separations for clustering
−Can make exceptions based on interaction (effort put in, 
class participation, types of questions asked, active on 
discussion board, etc.)
What if the class average is 82% and std is 8
−Should one give A to 90 and above only?

119
Data Analysis Alternatives
Advantages of automated approach
+ Fast, can use more data, complex data
+ Can generate reports for human consumption
+ Can generate plots and visualization
+ Can choose alternative analysis techniques 
+ easily compare alternative analysis
However
- Explanation may be difficult (e.g., neural networks)
- Generalization (e.g., neural networks)
- Should not blindly assume the output as correct
- Need sanity check, validation on small sample data
- Need to be aware of changes in context, expectations, 
etc.
Data Analysis is not as easy as you think!

120
Bottom line for Data Analysis
We want to process large amounts of data
We want the flexibility to slice and dice data in many 
ways
We want to do it fast
We want to do it incrementally
We want an efficient approach!
Performance, speedup, and scalability
We also want no liability if something goes wrong 
(blame the system), just kidding!
We want to out compete others in the same business
This tutorial is tailored for data scientists to 
understand the subtleties, issues, and develop useful 
skill sets

121
What tool should we use?
Currently, widely-used tools for data analysis are
Python
RStudio
Pandas (actually Python + Pandas)
Others (SPSS, Matlab, …)
Which one is better?
Depends on who you ask and what the needs are
All are useful for basic data analysis
Learning curve varies
We will discuss this further after you learn Python

Data Analysis Examples
Census Data (Descriptive analysis)

Census Data Analysis
We are given 1990 census data with over 
32,000 rows.
The original data has already been pre-
processed as follows:
Discretized gross income into two ranges with 
threshold 50,000.
Convert U.S. to US to avoid periods.
Convert Unknown to "?"
Sample input (comma separated)
32, Private, 192965, HS-grad, 9, Separated, Sales, Not-in-family, 
White, Female, 0, 0, 45, United-States, <=50K
39, Private, 107302, HS-grad, 9, Married-civ-spouse, Prof-specialty, 
Husband, White, Male, 0, 0, 45, ?, >50K
123

Descriptions of fields (meta data)
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-
gov, Without-pay, Never-worked.
fnlwgt: continuous.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, 
Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, 
Preschool.
education-num: continuous.
marital-status: Married-civ-spouse, Divorced, Never-married, Separated, 
Widowed, Married-spouse-absent, Married-AF-spouse.
Occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, 
Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-
fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
capital-gain: continuous.
capital-loss: continuous
hours-per-week: continuous.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, 
Germany, Outlying-US (Guam-USVI-etc.), India, Japan, Greece, South, China, 
Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, 
Portugal, Ireland, France, Dominican-Republic, Laos,
Ecuador, Taiwan, Haiti, 
Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-
Salvador, Trinidad & Tobago, Peru, Hong, Holand-Netherlands.
124

Analysis 1
1. Count the number of people in the following age 
groups:
< 20, 21 to 40, 41 to 60, > 61. 
Draw the histogram (frequency plot)
125

Analysis 2
2. For the above age groups, find the number of 
people in each of the following professions: private, 
self-employed (both), Government (all), without 
pay. Draw a separate pie chart for each age group
Drill down
126

Analysis 3
3. Identify top 5 occupations for the population
While looping or separately count the number of 
people in each occupation, sort it, and choose the 
top 5 occupation categories
127

Python code and results
1.
Data is  uploaded into the Google colab using the following code 
pd.read_csv(io.StringIO(uploaded["clean-data.txt"].decode("utf-
8")),header=None).
2.
Preprocessing is done to remove rows which contain “?” in their columns, and this    
can be performed using the Pandas library and random sampling is done to get 
300   records.
3.
Pandas library of python is used for processing, manipulating the data and 
matplotlib.plot library is used for visualization using bar charts and pie graphs.The 
entire csv file is converted into dataframe with rows and columns of the Python 
dataframe. 
4.
By iterating the entire pandas dataframe using iterrows() function for the pandas 
dataframe,  the data is assigned to 4 variables based on age criterion such as , “< 
20”,  “21-40”, “41-60”, “>61” using if, elif conditions.
5.
Using nested if, elif conditions within each of the former if , elif conditions, they 
are  further  assigned to 4 variables based on their employment such as “Private”, 
“Self-emp” , “Gov”, and “Without-pay “ using variables, for each of the 4 age  
categories/variables. 
6.
First , we plot a histogram to show the bars basically using two lists for x-axis 
and y-axis, sizes of which indicates  the number of people belonging to each
age group.
128

Histogram (Analysis 1)
129
As we see here most 
people are present in 
the age-group of ‘21-
40’

Drill down Pie chart (Analysis 2)
1) Using Pie charts, we visualize the percentage  of people belonging to 4 
employments within each of the 4 age groups.  The list of numbers of people 
(sizes attribute) belonging to occupation is given in the same order as the ones 
mentioned in the label list of names of occupations(labels)  to the pie() function 
of the matplot.plt library.  The list of numbers (sizes) was created from the 
variables created in the former for loop structure.
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
1) value_counts() is used to count the number of unique values present in a 
particular column. Here it is used to find the number of occupations (using 
number of rows entered) present in the entire population and slicing the top 5 
values  as the top five most employed occupations.
130

131
Pie-Chart Occupation Distribution By Ages

Analysis 3 (Top 5 Occupations)
Pie-Chart Occupation Distribution By Ages
132

Word cloud of Top 5 occupations (Analysis 3)
133

Data Analysis Examples
Airlines Data (Prescriptive analysis)

Airlines data analysis
you are given a large airlines data set indicating the flights operated by 
many airlines. We have replaced the airline name with AL1, AL2, etc. It 
has about 6700 routes of several International and US carriers. The data 
set contains the following information in each line, separated by comma
AL242,AL242,ASF,2966,KZN,2990,,0,CR2
AL242,AL242,ASF,2966,MRV,2962,,0,CR2
AL242,AL242,CEK,2968,KZN,2990,,0,CR2
AL242,AL242,CEK,2968,OVB,4078,,0,CR2
Airline 2-letter (IATA) or 3-letter (ICAO) code of the airline.
Airline ID Unique OpenFlights identifier for the airline.
Source airport 3-letter (IATA) or 4-letter (ICAO) code of the source airport.
Source airport ID Unique OpenFlights identifier for source airport.
Destination airport 3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
Destination airport ID Unique OpenFlights identifier for destination airport (see Airport)
Codeshare "Y" if this flight is a codeshare (that is, not operated by Airline, but another 
carrier), empty otherwise.
Stops Number of stops on this flight
Equipment 3-letter codes for plane type(s) generally used on this flight, separated by spaces
135

Analysis
Analyze two specified airline (AL1 and AL3 in our case)
Construct a graph (or a graph data structure) for the airline 
being analyzed by you. With airport code as the vertex, 
draw an undirected edge between the two airports in each 
line of the input. Since many Python packages/algorithms 
only accept integers as vertex, you may have to map the 3-
letter airport code into an integer. You can use a dictionary 
for this.
Generate characteristics for this airline route 
graph. 
−This will help understand some of the 
characteristics of the data set you are analyzing.
−Interpret them from an airline's operation 
perspective.
136

Analysis
Find the top 3 to 5 nodes (or airports) from where 
there are more flights than others for that airline. 
These are termed hubs by an airline. You can use a 
node centrality detection algorithm for this
Once you have the top k hubs, try to identify the 
airline that you are working on. You can use any 
data that is available on the Internet for this 
purpose. We will give you a file that maps airport 
code to airport names and cities
In the next step of the analysis, your goal is to 
identify or predict the next hub for airline 
expansion. For this, you can use demographic and 
other information that is available on the web.
137

Approach
After cleaning the project, 
Separate your airlines from the data set
Run degree centrality algorithm to find the degree 
associated with each airport
Use the top 5 to identify the airports and the 
airline (using internet and other sources)
For the next hub, use the next 3 airports and check 
population, mean income and education level
−Using them determine which one would be better 
as the next hub
−Other business-related information can also be 
used if available
138

Python code and results

The python package called networkX used for this problem.
Here, We have to predict what are airlines AL1 and AL3 from given 
dataset using data analysis.

Read dataset and choose the rows from dataset for only given airlines.
df1 = pd.read_csv(‘filepath’)
airlineData= df1[df1[“0”]==”Airport_Code”]
Define source and destination vertex for the graph
graphAirport= 
nx.from_pandas_edgelist(airlineData,source,target)
Plot the figure as network graph of edge and vertices.
○nx.draw_networkx(graph_airport,with_labels=True,node_size = 
1000)
The following slide show the result of the plotting of this graph 
obtained .
139

Flight Graph for AL1
140
RESULT

World Cloud showing Hubs for AL1
141

Flight Graph Obtained for AL3
please add your slides here!
142

World Cloud showing Hubs for AL3
143

Characteristics of AL1 graph
Number of Nodes:  434
Number of Edges:  1191
Diameter of graph:  7
Density of layers:  0.01267547173827439
Components of graph:  1
Degrees of Graph:  [2, 135, 118, 1, 184, 4, 69, 124, 75, 1, 94, 1, 
1, 3, 11, 13, …]
Average degree of graph Nodes:  5.488479262672811
Minimum degree of graph Nodes:  1
Maximum degree of graph Nodes:  184
144

Characteristics of AL3 graph
Number of Nodes: 354
Number of Edges: 1003
Diameter of graph: 7
Density of layers: 0.016052880075542966
Components of graph: 2
Degrees of Graph: [2, 210, 132, 3, 127, 88, 1, 2, 25, 1, 1, 2, 
86, 1]
Average degree of graph Nodes: 5.666666666666667
Minimum of graph Nodes: 1
Maximum of graph Nodes: 210
145

Degree Centrality 
⮚
Degree centrality refers to the total number of edges coming out 
from a node to destination nodes.
In our context, refers to the number of destination airports to which a 
source airport is connected with by a given airline is given by degree 
centrality. 
High degree centrality simply refers to busier airport as more airlines are 
operating in these airports for the given airline. 
Function for finding high degree centrality in networkx is:
▪
nx.degree_centrality(graph_airport)
So, the airports with which the airline have more degree centrality can be 
determined as the HUB for that airline.
The following slides comprises the degree_centrality calculation for AL1 and 
AL3
146

Top Hubs for AA 
AIRPORT
DEGREE CENTRALITY
AIRPORT NAMES
DFW
0.42494226327944573
Dallas Fort Worth Airport
CLT 
0.3117782909930716
Charlotte Douglas 
Airport
ORD 
0.2863741339491917
O’Hare Airport, 
Chicago
MIA
0.28175519630484985
Miami International Airport
PHL
0.27251732101616627
Philadelphia Airport
LHR
0.21709006928406466
Heathrow Airport, London
PHX
0.17321016166281755
Phoenix Airport
DCA
0.17321016166281755
Washington Airport
LAX
0.15935334872979215
Los Angeles Airport
JFK
0.14087759815242493
John F Kennedy Airport
LGA 
0.06235565819861432
LaGuardia Airport, New York
SEA 
0.06235565819861432
Seattle Tacoma Airport
BOS 
0.053117782909930716
Boston Logan Airport
NRT 
0.050808314087759814
Narita International Airport
PDX 
0.04157043879907621
Portland Int’l Airport
147

Approach for Predictiing Next Hub For AA
➢The next hub for the american airlines can be chosen from the three major airports with high degree 
centrality which are not recently included in hub of the American Airlines by comparing the education, 
income and population.
➢If it is a domestic next hub, it could be either Seattle or Boston. Other considertaions may be 
included to break the tie.
➢Although London’s population is high, it has 4 airports!
Airports
Population(in 
million)
Education(Bache
lor’s degree in 
percentage)
Average mean 
Income(capita 
per annum in 
USD)
LHR (London)
8.982
59
53,837
SEA (Seattle)
4.01
53.8
59,835
BOS (Boston)
4.7
49.7
44,690

Top hubs for Delta 
AIRPORT
DEGREE CENTRALITY
Airport Name
ATL 
0.594900849858357
Atlanta
DTW 
0.37393767705382436
Detroit
MSP 
0.3597733711048159
Minneapolis-SP
SLC 
0.2492917847025496
Salt lake city
JFK 
0.24362606232294617
John F Kennedy
LGA 
0.17280453257790368
LaGuardia Airport
LAX 
0.1671388101983003
Los Angeles
CVG 
0.1161473087818697
Cincinnati Airport
MCO 
0.09915014164305949
Orlando Airport
AMS 
0.08498583569405099
Amsterdam Airport
CDG 
0.0708215297450425
Paris Charles
BOS 
0.0708215297450425
Boston Logan
SEA 
0.0623229461756374
Seattle-Tacoma
MEM 
0.059490084985835696
Memphis Airport
LAS 
0.056657223796033995
Harry Reid Airport
149

Approach for Predicting of Next Hub For Delta Airlines
➢The next hub for the delta airlines can be chosen from the three major airports with high degree 
centrality which are not recently included in hub of the delta Airlines by comparing the education, 
income and population.
➢‘
➢Similar analysis can be made.
Airports
Population(in 
million)
Education(Bache
lor’s degree in 
percentage)
Average mean 
Income(capita 
per annum in 
USD)
CVG (Cincinnati, 
kentucky)
2.20
37.1
25,846
MCO (Orlando)
0.307
24.41
28,062
AMS(Amsterdam
)
0.821
16.91
44,833

Thanks!
Any questions?
151

## Fetched resources (external URLs)

### Data Management and Analysis Pre-Survey (link)
*URL:* https://utaedu.questionpro.com/a/TakeSurvey?tt=D8UgGg40yIcECHrPeIW9eQ%3D%3D

[survey link — skipped]

### Data Management and Analysis Recording (link)
*URL:* https://www.youtube.com/watch?v=KLf-ZSYqzz8

[YouTube transcript KLf-ZSYqzz8]
hello there um welcome back good afternoon everyone so I see that the survey please survey link has been posted I would appreciate if you can take a few minutes to do that and then we can start the presentation thank you foreign we are done with the survey we can get going and everyone see the slide on my computer that I have shared yes okay so are we done with this alone okay so as the title indicates this is a very introductory tutorial to Digital Data and the prominence and current thinking says you know where we started and where we are today I felt it's important especially you being non-computer students on computer science students it would be useful to know the evolution what we have been doing and where we are I would think that you are really the Blessed ones with the technology and the power of the computers that we have and this was really not so some time ago so that's me so I'm not making any assumptions in this tutorial this is meant for uh undergraduate company Science High School students or not consent students so so the focus will be on the data data collection storage cleaning loading management analysis and how we have been addressing that with computers and even before that since you know you'll be doing lot of different kinds of analysis in your domain and maybe in other domain I think it's important to understand this so the outline is motivation the brief understanding of the terminology what is data information knowledge and wisdom and only enable us for creating data how did we go from analog to digital and what sort of precipitated the need for automation and the important thing I think you will see again and again is the changing requirements we have some things available today it is not enough we need better things more things and that forms a cycle of changes changes to improve different aspects and that has been what is happening over the last 50 60 years so we will Trace sort of the prominence published um black files to what we call data science and Analysis today and if time permits I will go over some real world data analysis examples and then conclude so uh if you have a question please raise your hand it came so that I can see it clearly and then you can turn it up off of that or you can put in the chat there is a modulator you can type me and put towards the end to answer your questions I want to make sure that you know what everything is understood clearly even if I have to go slow and not cover everything so it's not so much I want to cover but to make sure that you understand what you thought so motivation is you know you are given a data set some description of the data set and we know the application area your boss or advisor wants you to figure out how to leverage this data set for improving the business or understanding what's going on yourself so this is the fundamental problem that is driving uh data mining data analysis everything we do and this is an example from the business domain but it could be for research generating no customers retaining current customers preventing them this is very common in the in the mobile phone industry as you may be familiar with how does this business completely to this are there so if you go to vaccine we have covet is there a booster shot needed of course now the company that markets it wants it because that is the business but we have to we do some independent analysis by CDC MPC to determine whether that is actually necessary amount so there are different players trying to do different things and how do we understand about it how do you say is it possible to unless it is possible to analyze this data in so many different ways which one is better which one will you choose and the justifications of it most importantly I think this is many times missed by our students how will you validate to it results this is very important because I what I tell my students and I want everyone to understand is when you run a program you will get a result that doesn't mean the result is correct there is this assumption that just because you got an output it has to be correct that is really not not true in many cases so this is something that you have to constantly worry about at the end of the day you need to convince your boss but Your solution is good and it works with high probability and then you go from there so this is the in a nutshell what is driving data analysis to it and believe it so I kind of I call it public analysis analysts Without Borders just like Doctors Without Borders and the reason for that is that you can no longer just do analysis in your own domain you need an understanding of multiple topics multiple domains and be able to synthesis your analysis and results in many ways so you cannot just focus on a programming language or an operating system or a particular type of data and data analysis itself has many steps cleaning choosing meaningful attributes for data of data for analysis mining machine learning algorithm level State probability and statistic drill down visualization so you have to be careful in what you choose how you choose what you choose so my advice to a lot of students to do this is don't do not become a person with a hammer looking for email if you have enamel camera everything looks like a nail instead become a person who can match the tool for the specific problem this is the most difficult part of it so this is where you have to consciously make sure that you are doing the right thing and not just applying your funeral but what is actually needed so this is just to understand you know Sherlock holmesan say it is a captain mistake to theorize before one has data interestingly one begins to piss the parts because this is very true I have seen students come to me and present their experimental results and to say yeah everything is fine correct when you start taking deeper and asking questions then you realize this may have been accurate I think that that is the process that humans have to do you as students have to constantly question and make sure everything is correct uh many programming mistakes are discovered after the results are explained or sometimes even published that's why we need to worry about independent validation mechanisms so hence two or more independent approaches should always be used for validation we take use in our theoretical and analytical way of figuring out what to expect and see whether they can be much experimentally just using only one of them may not lead to the third thing also do sanity checks on your outcomes to make sure you have an upload something always make sure your test cases include longer cases so there's a tendency for the person who is doing the programming to test only cases that work because they know what they have done and this is a is going to be a class limit State that's why most of the companies you know if you look at Microsoft they have as many testers as many Developers testers should be different from developers so that they are not subject to knowing what has been implemented and testing only those features so some clarifications why learn programming for analysis today you know you have a lot of packages for many thoughts you need to do you may have to use appropriate data structures and populate so it is not that you are developing a lot of code but you need to sort of put together the packages in a way that is appropriate for your analysis choosing appropriate algorithm is probably if you want to be figuring out blocking and visualization generating food and understandable approach does the data set used for learning matter you know it's a it's a difficult question and the answer is yes and no it is important to understand that analysis no matter what data set you use is the same you are doing the analysis and you're interested you should be interested in understanding the process of analysis and what you are trying to do based upon the context and the data set and the application so you'll be encountering different and complex data sets all the time do not get hung upon the latest applications there's a tendency at least amount compressing students to say okay I only want to use python I don't want to be using anything ads I think that that is not the best way it is not the language it's what you want to do with the language some languages some may have a marriage easier learning curve some maybe a little more than that but language has changed today it's python tomorrow it's something else process of analysis does not change some pre-processing and other decades major so if you have any questions please so I see hello from the activities specify your mind yourself so how will you cover all we are going to encounter in our career on this Workshop or from this analysis method the simple answer is we cannot but the more important thing is we do not have it as I said the process Remains the Same details of analysis depends upon the business domain objectives so please focus on learning the analysis process not just on the data sets at some point we need to understand the data set please focus on presentation visualization and how you can correctly analyze and benefit from that what about different types of pre-processing same as above may have to add more tools to your three classes in toolbox at the end of the day domain knowledge coupled with analysis processes what is important to be be successful data analysis when I say data analyst it it can be from any domain it shouldn't really matter at all the reason that you need domain knowledge is that you have to be able to understand the data and what you're expecting or if you get something through the analysis which is counterintuitive or you'll be able to evaluate it now we have started a new program data science program in our department and this have been going on for two years now and I was involved in the development of the course and for this program we specifically admit students from different disciplines I have abscriptions from at least 10 different disciplines in this course and the basic idea is that we need different people from different domains to do the data analysis curriculum and that has been really very difficult because most of the people who try to do the nonsense are completion people they don't know biology they don't know art science they don't know water management and that makes it extremely difficult to do the analysis problem so so this data analysis how much we want to think that you know this is new it is not you know back in 1982 without prevailing my age we are traveling in information but start from knowledge this was a statement made by basement this was 30 years ago this level of information is clearly impossible to be hand driven by present means uncontrolled and unorganized information is no longer a resource in an Information Society instead it becomes an impediment this statement I believe is still true today and it will be true for the foreseeable future so it is not enough to store organize and manage information but it is critical to extract relevant knowledge and make it available for decision making in Italian this is the key I mean just collecting data is not very useful you may have all the data but if you cannot make decisions actionable decisions in a timely manner if there is a flat you will you know wave the help need to be given which places in in that while looking at what is going on today rather than just sitting on data so what is data information and knowledge so this is an old diagram again which sort of classifies it into a hierarchy which is a pretty good organization in my opinion so you have data at the lowest level that you collect we also call it raw data then you have information where you have some additional information on data we will see later that you know metadata can be a way of converting data into an understandable information then there is knowledge that's what we want to derive out of this and finally wisdom I think we still don't know how to automate bearing wisdom humans do it and they still don't understand so exactly we do that so here is another way to look at it to say you know uh data understanding of data versus how they may be connected or related to each other so you have data and you have information which is a small difference understanding what it is but the more important thing is you're trying to understand the patterns in the data that's what we call Knowledge discovery of mining or influence whatever you call it and finally one would be able to understand principles of the fit which is a lot more difficult than one things so we still never say that you are doing wisdom Discovery we are only doing knowledge to study at this point foreign so the basic idea is to go from data to information to knowledge to decision into action irrespective of the field passing this problem as a data processing problem so this is my view of looking at this problem so we have raw data different kinds of raw data we will see another diagram that explains it better and you are interested in knowledge if not Crystal at least timely actionable knowledge it may be in the form of rules actions inferences predictions and you want to make this sense of effort so the reason it has been shown as an inverted triangle is that you are reducing vast amounts of raw data into consumable data now that is the key for what we do as part of data analytics [Music] and it involves various things listed here understanding relations understanding patterns and if possible the right principles so this is the process we have been doing with or without computers right even without computers the process is with computers you can deal with large data different types of data do it faster do it in multiple ways so that that is the basic difference between what we were doing earlier and this is only going to get better so here we say a data or raw data as we call it in your domain you can think of just having two numbers black long if you don't know that they are lifelong it has no meaning even though there are two numbers but knowing that it is lat long gives you a better understanding of where it can be used and how it can be used so suppose I give you these pieces of raw data you know quality thousand Einstein male 3.4 this is rodent this doesn't mean anything by itself but if I add some information a data by itself is difficult to understand and we are collecting a lot of them I think this can be related to the need for fair principles and also metadata so information in some way can be thought of adding additional context to data which can be military understanding for example if I say 480 000 deaths in U.S is from cigarette smoking that puts a context to this number if I say 3.14 is the value of pi that makes it understandable Einstein is scientist and so on so you can see that numbers by themselves whether they are numbers of strings solved other things will not be very helpful without additional information we will come to this on Wednesday I think when we discuss more about metadata so data Sciences the science of going from one form to another form it can be a bunch of techniques it can be approaches tools abstractions but we'll see all of this we'll see some Notions of abstractions in databases for example different Tools in mining find different ways of relatives so not at all new what is new is the size with which we can deal with the variety of data earlier we're only doing with numbers now we can deal with images on video and EKG on the MRI so there are so many different types of data and the complexity they keep changing okay I can keep everything visualization is possible today which was not possible so the whole idea is how to with these things even though the basic process more or less Remains the Same any questions so just to give you you know what is information briefly or well you can divide it into analog and digital so digital came around not very long ago on a large last minute one for a long time and digital kind of one way to think of it is three database Management Systems post database Management systems and close to internet if anybody is interested in understanding a lot about information and how it was done there's a very nice book by this author James clicked uh it's a very interesting thing but it's a very huge book thousand plus pages so Shannon was the first one to introduce the or bit in 1948 as a unit of measurement of information so British taken for granted today you know you have Capital bits in a computer in what we use six to four big computer there was no way to measure information before introduce the notion of redundancy it will come to that in databases between the c channel good things and bad things to correct errors in transformation interestingly the notion of error correction was used by drummer saying if you read that book you'll see in Africa by using extra words but it's a negation labor communicating from one related to 100 for hundreds of years before the ability so here are a couple of questions there were some transformative events in the history of human Saga that really created the the need for dealing with large amounts of data so information were produced manually thereby limiting the amount of information through this so there was a time when books were produced by copying then manually and and then making them available two transformative events in the last 1000 Years changed that significantly can you guess what those three ones are anyone you know it would be one of the is the Industrial Revolution okay that yeah okay I can relate to that anybody else the Industrial Revolution certainly changed a lot of things uh so here is the first one printing this it was in 1454. just to understand the impact of that technology this is way before computers right look at the number of copies of manuscripts that went up from 0 to this is one trillion so this this revolutionized the availability of data in some form and that was first thing that really changed everything because people did not have to copy books and manuscripts anymore they could easily print it and make it available first solution and the next Revolution became almost server 100 years later can anybody guessed it what it is internet again change the availability of information from very small amount into settlements one set ability is a one Tera gigabyte it has lots of zeros in front of it so you can imagine and this is doubling or boring up every year so this is what is happening to data as we speak the amount of data is growing so other enablers inexpensive sensors and devices mobile devices capable of recording amazing video today I'm not sure how much video is taken and whether anybody even bothers to look at it advances in storage we'll come back to this later if you create all this information this you need to store them storage technology as we see it's very primitive not very long ago however analysis fusion and filtering data has lagged behind so producing data is easy relatively easy but what to do with that and how to put it into good views of just use is is a different story and this is what we are constantly struggling with you know today every company thinks that the data they have is proprietary make it perfectly because they are sitting on a gold mine but they don't know how to extract gold from that so these events that came about due to technological advances also meant that it is just not enough to create volumes in data what do we do this with this information on data so there are so I'm just risking some things so satellite images with saturating measures maps and cartography businesses deal with headron collider which is in bomb Switzerland that generates tons of data USGS you're familiar with I don't have the same thing how can it be used for different purposes now the burden of storing processing and Analysis is serum Twitter which meant that in addition to technological advances we need to develop algorithms Mining and other techniques to make use of them so this is what we are trying to understand and I think the the fair principle is critical in in newer area you know on Wednesday I'll say a little bit about how we are managing in computer science without any principle that I know how this is one of the challenges for data science methods so most of you may or may not have seen a Mainframe let alone what a computer looks like before the meeting we are mainly no you know laptops and tablets and mobile phones which are as powerful as some of the high performance computers a lot of people today grew up with a very powerful computer in the pocket for them it's very difficult to imagine a world where one had to go to a computer center to submit a job wait for one or two days get the results this is this is how it was when I was a student both undergraduate and graduate where we had to go to a place where we submit our program in a deck of cards and then go back the next day to pick up an output just imagine one syntax settlement you lost one bit so this is how things were being done indeed we have come a long way let's understand a little bit of the linear so this is how a computer looked like in the 60s and 70s you see this is a computer from Russia I worked on one of these computers in this series so what would be interesting for you to know is that the memory it had it was 32k verbs today we have two meetings so 256 GB pockets could program through console using machine language this was the console it had paper tapes and card inputs it was very it had a very rugged magnetic tapes no discs at all and board members so this is it occupied an entire room and its capability was very very minuscule compared to what we have to do so this is another early version this uses printed circuits where this one did not even use printed circuits here is a IBM 360. one of the very famous mainframes from IBM this came about in the 70s and it was big but much more sophisticated than what I showed you before and it had a large memory which was 54k thanks and it had disks so here is a picture of a disc which is almost like the size of a fridge and it only held five megabits so here is another view of an IBM Mainframe with tape drives were very popular and I don't think any of you might have seen that and this was this could put a lot of data compared to the risks at that time so they were very widely used and they have some limitations and here is another example of a disk drive and this one held 50 megabytes this was like a dishwasher so this is this is where we have come in the last 15 60 years this was another one on which I worked on which is the Russian replica of IBM 360. very interesting story now we have computers in all shapes and sizes from sensors to server forms a few years ago I was in Sweden northern part of Sweden and somebody told me that there is a Facebook server from in the North of Sweden so kind of we took a drive to go and see it was a of course uh area that you could not enter but it was like one kilometer by one kilometer and a building in which I don't know ten thousand hundred thousand servers were asked so why did they choose can anyone guess why they chose Sweden and northern part of Sweden to house their server for this is pretty common by the way anybody well these machines generate a lot of heat pulling these machines is very expensive and in the northern part of Sweden it's cold most of the time so they don't have to spend a lot of money on air conditioning so that is why a lot of these server Farms are located in Norway Sweden Finland and all places where pulling these available in 20 and without much cost today you can even program your dimmer switch reports of flexible available time streams Google Cloud emulator system so I don't know how many have any of you heard of chart GPT if you are not you should look it up this is the latest phase in AI this is something that has been put out by this is all over the news today and we are we are concerned you know the quality of engineering is sending a questionnaire to understand so many faculty from other departments knowing about it and what we can do about it from an instruction descriptive okay coming to data and its management so kind of That's So we have come to the point where we have a machine which has file based data management mostly sitting on a disk and if you want to use file based systems relate they can see later the complete burden of how to use this data is from the user means application developer you have to understand the format of the file you have to understand the record format you have to know each field you have to write your program and if you want to change anything you have to change your program so this is where we started off it then came what we call a database Management systems and it provided a bunch of improvements again we'll see a little bit in this module and a little bit later provide standards Integrity reading capability interoperability Etc again this sort of fell short in many other ways so database which did multi-dimensional analysis and other kinds of things that could not be done by a traditional DPMS then there was Data Mining ugly approaches lab data scalability machine learning algorithms then there were stream data processing for dealing with different kinds of data that were coming today you know people developed for sensor data but today the data coming from Twitter for example can be seen as a stream data because you're generating very large volumes of data in a very short time and the rate at which it comes depends upon how popular the particular topic is ETC and finally we have the notion of the Big Data which is characterized by what we call Four whis volume velocity Variety in words so the vocabulary uh changes every few years and this is true in computer science I don't know about other areas we we have new terminology new themes too so from flat file systems we went to dbms to data warehousing data mining data stream Management Systems nosql databases cloud computing big data analytics data science Big Data analysis during reports so these are the kind of The evolutionary path that has happened from a point of view of data analysis what does it mean it means that what changes in requirements and advances technology make this happen so these things cannot happen without some underlying changes in different types of Technology it could be in Hardware it could be in software it could be in networking it could be in development of new algorithms sophisticated well you cannot think so this goes hand in hand with each other and we will see how this will happen or sometimes you wonder whether it's just Old Line in Indian market so so what is a file system so I I'm trying to understand so when does this just to keep track of it when does this model end we started at 12 45 to 130 so Dr Sharma this will end at 2 15 and we'll have 15 minutes break 2 30. what time do we stop this fabric 2 15. 250. okay so basic abstraction for storing information digitally that is a file very simple yet very powerful and believe it or not this has not changed since its introduction all types of information doesn't matter what kind of information it is has to be stored digitally as a file whether it's text audio image Maps layers now here I click with objects whatever it is user decides how to store information in the file typically as a records feeds and values within your effort for structural data application has to understand that the application types can be broadly classified into three Catfish computation intensive applications there are a lot of different uh computations or applications that rely on heavy computation finite Elemental analysis computative design simulations numerical analysis the sort of the Hallmark of this kind of computation is you load all data into memory and then process you know some of the simulations and the things that we've done can take our some sometimes base then we have the data intensive applications which have lots and lots of data and you have to deal with the data so today almost if you think of Amazon Airline reservations data equivalent faculty usds they're all data intensive applications and the Hallmark of this is you cannot load the whole thing into the memory because we don't have enough memory and then do the computation you have to Stage data from disk to memory and processing this is the difficult part so you have to determine how to State data how to process it and that is where database Management Systems can picture and then of course we have the combination where we have computation and data instances of applications where you need both you have large amounts of data you need heavy computation and sort of you can think of Big Data applications some of the data mining which may use click on terabytes of data will drill down exploration of data warehouse dimensional enhances and so on and so on so kind of all three are there one has to deal with that and then figure out which one you are dealing with and how to build it so applications need to be aware of data so just looking at file system I mean you will see the example sorry or you might have to be familiar with what we call CSV files makes it difficult to change the format once designed enhancement is taken okay so this is the biggest problem once you decide on the format all the applications so think of it if if 50 applications are running over this why and if you change the format you have to revise all the 50 applications this is the biggest problem we have in the software industry we don't want is one change affecting so much if the format is changed all applications have to change application management is difficult labor intensive and tune to errors but there is a very strong coupling or dependency between application and the storage form which makes developers well difficult so we will discuss this again in the integration module how what are the different ways to open Facebook so dealing with data multiple ways to overcome standards for representation of data and exchange of data use of metadata we will also see that later use of database Management Systems will see that one Wednesday and there has been a number of data exchange formats to exchange data such as XML that you might have be familiar with Json for which programming language support is available related issues are interoperability how to make multiple applications work together without having to change them again and again every time something changes the dbms was one of the approaches or opportunities that came about to work from this problem but specifically the problems associated with file representation and file products and how was it done it was done by decoupling the data representation from application software so if you separate them and application software does not have to understand the data representation then you can change data representation without affecting the applications and this is not trivial to do it's a very common practice in computer science we call it a level of indirection you may also think of it as in a material a very specific material we will discuss this further in in another model this requires software which can break this game so so software is the one that sort of reduce the gap between the format representation and what the application means times this is done providing a higher level of abstraction this is very important to see different types of obstruction for the user and this abstraction is mapped into piles of storage bias software and so you can think of it as a compiler so what do compilers do they take your higher level programming language and convert it into machine executable language so there is a conversion you don't write it in machine readable language because it's very cumbersome it's very difficult to do but the compiler helps you you know if you're writing python there is a compiler for python if you write in Java there is a compiler functional so dbms has specifically had mathematical underpinnings based on set theory and this is how the RDA versus were born the details but before that we had other types of dbmss which are not very widely used today but some old utility companies still use it Network and hierarchical dbmss and later we have what we call new SQL and many of those systems any questions okay so we were talking about levels of abstraction so this is how typically it is done even though this diagram is for a dbms we have at least two levels of construction one is the physical abstraction and the conceptual abstraction and then they say I get third level of extraction which is what the user sees or uses and the reason for all of this is these abstractions hide what is underneath and provide a a kind of a a common interface so these are known as conceptual biological abstraction or schema physical absorption so views describe how users see the data and they don't see the actual format in which it is stored so by changing the format you don't affect the user view that that is the most critical part conceptual schema defines logical structure physical schema describe the files and indexes so by adding these layers of abstractions you are making things easy for the end user so the whole point of this is to make the user not worry about the details of storage and implementation but worry about the problem of hand so this is a very common thing so you can also think of data exchange formats that we'll see as one form of schema that can be used for in a slightly different context so what is a dbms briefly it's a very large integrated that that's important collection of data just to give you an understanding you know for those of you who are TTA you guys use my math all the time for registration ladies they give you a messenger meet you don't see it you use a web doing for that but what we have underneath is another predicaments whatever system you use for registration and payment of Peace by clicking you have it and the GBM System model the real world Enterprise in our case we must Administration and it has entities in relationships we'll come to that the important thing to understand is a dbms is a software it's a it's a software package designed to store and manage the optimum subject so that is the UK update this integrated means that you can access multiple pieces of data from one collection that is also true in a system like GIS or rtjs people use why use a video Mouse it provides a bunch of advantages data Independence as I described and it also provides efficient access really not going to that because of the data Independence reduced application time it maintains data integrity and security uniform data Administration multiple users and very importantly recovery from cautious so application development time is reduced information thoughts into a space to a new level of construction so this this was a a big step in the 70s you know debonences World develop in the 70s and became very popular today relational deep images we are used almost by every Enterprise and by every every company that even though it has a web front end behind the web function there is a deep in the solving organisms so just to give you a brief understanding of how this happened so I I just want to know if you're going into details what I want you to understand here is the so whatever is below this line is what has been augmented or implemented the software what is about this line is what the developer does so I want you to pay attention to how what the developer does or the application does is shrinking this is the whole point of almost everything we do in computer science is to reduce the burden on the application developer or user and push more of that burden to the server as we call it or with a system underneath so that that can do the heavy lifting and you only focus on the application you don't have to worry about modeling you don't have to worry about semantics you don't have to worry about transaction management we don't have very more pre-processing so this is what is done all the time this is the evolution that is taking place and the same thing you can see that mining has also been to some extent pushed into that XML support and various other things so so this is what makes it even even in in GIS I'm sure when you deal with a system like JS you are more focused focusing more on the application not on the biodata format as well whether it has multiple data models for example I'm sorry it is used so that is the key for data analysis data usage and so this is an architecture I'll skip usually dbmss are very large they have hundreds of thousands of posts a clear articles like 1 million plus lines of C C plus plus code so it's a huge beast on developing managing and maintaining is a complex task so give your misses have worked well for over actually more than three decades you saved us nowadays it does behind the scenes like my lab use for payroll Airline reservation Inventory management Financial daytime more it's also used by Amazon eBay you name it they serve all part of skin storage all the expectations keep changing of the technology advances we'll discussed more details with epms giving views later so how do databases work behind the scenes here is an example so when you go to your website and when you click a few boxes and some output shows up what is happening behind the scene says a dbms is being used for the data storage these things that you put here are converted into an SQL query and the query is run on the dbms the output base package and shown onwards so this is the typical way today the businesses are used earlier they were used directly by sitting on the server and writing your rescue even that that is done even today in a few places but a lot of usage behind the dbmss comes from how to use it behind the Sims because there is no alternative representation to store Hollywood data in a meaningful way in a way that provides a mental characteristics that we need so functionality provided by traditional DBS As You Are no longer adequate so this worked well for a decade or so then it excelled in quitting even today there is no such in a database you only how to query a database and people wanted exploration not necessarily Search exploration of data in different ways so data analysis need to be done in an interactive manner functionality provided by leandrolet because it was no longer a liquid so these are the sort of the things that prompted what we are going to see next business intelligence was needed on very large dla data sets interactive usage was not there earlier everything was done sitting on a command prompt or running batch programs non-technical users want an easy to use system so this is always the case you cannot assume everyone is proficient in computer usage to receive a discipline is different your domain is different what you want to do is so this slide uh essentially tries to give you an understanding between the difference between search and reading there is a difference so when you interact with a dbms you ask a query that is written in a specified language SQL you might have used it even when you search my map they are translated behind the scenes interest completed and queries give you exact matches as we call it in other words they cannot give you approximate matches or similarity matches either it matches your query matches something in the database and if nothing matches doesn't give you anything this is perhaps one of the basic differences between search and reading search was around even before Google made it indispensable Tech section was very popular search was search gives what we call approximate or similar matches in the sense that if you ask for something and if it does not find it it will give you something similar or closer based upon how similarity or approximation is defined and certainly Google does a very good job if you even if you type a bunch of words it will try to match and give you some meaningful results the important thing I want you to understand is these are known as the full technology because we'll see something that is not those technology later what do we mean by this it means that you have to initiate something you have to write a query and submit you have to type a bunch of words and put it into the Google blog then only you get the result so this is what we call full technology is in contact there is a technology called push technology which is very useful so what are the drivers or enablers for going forward so business Information Systems became as important to corporations as transaction systems so they could not do kind of business analysis using traditional deviant nurses or a person difficult to do they could not store multiple years of data online because of the storage limitations and the performance limitations Mass personalization and leveraging data across seen as an asset identifying new profitable markets and channels to enter them increase customer align value and decrease the list so the approaches that were developed in response to those things were Data Mining and AI there is something known as Market Basket analysis that is what quite greatly used I don't know whether the new platform Limited what it means is you take any any store Walmart there are I don't know how many uh thousands of Walmarts in USA and every Walmart gets customers and they check out so they may check out two items five items 20 items and that is what is called a basket so every Point of Sales is captured and Stone the question is how can you make use of this information to build business better and Association rules were developed in the in the late 90s to do exactly that and almost play every vendor uses this Market Basket of analysis for that and the amount of the other generated it's very large so think of every customer every purchase over a year generates gigabytes of data if you want to do multi-year analysis so they are using this today to determine which items are sold more in which particular store based on the demographics and their information what items are bought to be there for example so that they can store them in the same place so there are a lot of ways in which this is being done text mining graph mining is Smallwood sample uh draft mining has become more popular today because of the social networks people want to mine information from Facebook LinkedIn and Twitter data for example recommendation systems you may be familiar every time you go to Amazon it shows you you know what you could purchase what somebody like you have purchased this is what we call recommendation systems and the difficulty of this is that you have to do it in real time Amazon cannot show it to you after you leave the site so it has to be shown either as soon as you enter the site out it doesn't make sense database housing again was a solution or answer to business requirements and this was different from data mining in other words here we consolidated data from multiple dbms's specific information interface exploration then there was complexity of processing resources pull paradigm stream data accessibility using web ranking is very important because the reason why Google performs so much better than playing than other Alternatives that you see is because of which a good ranking capability which is Bakery so they can somehow rank you know you can try this as an exercise give the same words about being them Google and see the difference in the output you get most of the times Google will give you close to what you are expecting whereas others may or may okay so okay so we will try to look at very briefly I'm going to skip a few slides what data mining is all about some of you may be familiar and I just want to point out that all of these are different from another this is different from search different from Reading as well as Big Data communities we'll see that later so hopefully this tutorial will clarify some of the fundamental concepts of the things you do which means so data mining is predicated on knowing something that nobody else knows the key in business is to know something that others you know so this is a traditional example I'll just summarize it without reading it so you might have seen that especially with the mobile phones is from providers they are the closer you get to your your contract for example they try to offer you some incentive to retain you as possible it is not that they offer this to everyone every customer that's not very beneficial for them so they have to selectively determine who may be switching and who may not be switching and if this sense that this person is likely to switch after the contract they want to retain the customer using some instinctive then the question comes out as how do you determine who is likely to switch and who's not likely to switch so that is the basic sort of thing in mining binding problems who should be given innocent even who should not be how can we do usage patterns into some number of groups should we approve this purchase by this type part by this user this will say even before the mining became very popular we had something called expert systems and American Express was one of the very first companies that use the expert system for a card purchase approval and this has this had to be done in real time within a few seconds and so they were the ones who came up with an expert system to approve a particular practice each purchase whether it's other all the others were you are doing that by putting a limit on how much you can buy so that there is a cap on their liability why massive amounts of data more in your online data challenges little time versus for people post Market forensic analysis so some things can be done as a forensic analysis just to understand things but some things have to be done in real time otherwise the value is not there no easy way to describe what to look for so this is there this is the most critical thing you cannot express this as a query not even as a search so you need to do this analysis without a lot of input and that's why a bunch of different techniques were developed like decision analysis clustering and other things were developed but doing different things using the same data and then figuring out how to use that so traditional interactive approaches were not very useful uh because of the size and other things so so data mining is part of the knowledge Discovery process carried out to extract valid patterns and relationships in very large data sets usually don't know what you're looking for regarded as knowledge Discovery or learning from basic facts or around data it is rooted in Ai and uses a lot of statistics uses techniques from machine learning pattern recognition statistics database representation so this is the example I was telling you how do you want to mean future Behavior and you cannot do a palm reading human intuition or determine so this was done before data mining by humans looking at some data points small set of data points and figuring out what is happening today the same thing is data mining our knowledge display by using more data real data so that the results will be more capturing so mining has been around for quite a while so there were a bunch of enablers without which mining would not have been possible one is the reduced cost of storage so you can go to larger storage systems reduced cost of processing so we have more powerful computers that are cheaper ability to store process and manage to Arch volumes of data and access new techniques such as Association rules I mentioned sleeping developer processing use of oncology Fusion again as we saw earlier the challenges are scalability visualization variety creating very large outputs and those things were that shines so around 1985 we had a bunch of changes that facilitated or enabled the use of data mining in a very large scale until then we were doing expert system by examples and also we are using samples so random sampling was very important and useful because you could use smaller amount of data and hopefully get the same general inference that you would get up on larger data but once the technology improved to store more information Network them and access them increase processing cable C then you were no longer limited to sampling but you could use the entire data so companies love it because they had lots of data and they wanted to use all data so that the results will be more accurate or prediction will be better so ability to approach to very large amounts of data plus architecture of the algorithms gave us the data management advancement Sorry by product of changing environments so typically you know this is what happens in a data mining you have a data description and you have a bunch of mining algorithms it could be clustering it could be classification from Harmony protection immigration Etc and then you get results and then somebody has to interpret these results that is still a difficult problem and has to be done by the human with the right background that's why domain expertise is so critical for for Mining and any of the analysis tasks that we are going to talk about in data mining a domain expect assists the analysis to determine the best training report based objective interpretation of the results is the most difficult and important I mean this reminds me of the story in August visiting India and I visited a company who were who were getting into Data Mining and they had a huge contract from the company here and they wanted to talk to me and I go there and they explained everything and I asked them so how do you do it now they said we are we're not sure how to do it so we know 20 different techniques that are available so we just run the data through all those different techniques and then we'll try to figure out which one is good so this in a nutshell explains why mining is difficult you cannot just run it through buy your 10 different techniques available and Hope somebody can recognize which one is the correct result but that but that happens a lot more than one thinks so you know that mining is used for customer profiling Market Basket analysis risk analysis text analysis fraud detection customer relationship marketing scientific discovery forecasting Etc so what is training what is data mining trying to do so I think this this is an important aspect that I want everyone to understand clearly because so we might have heard of this terminology separately so one is what is causality so everyone understands causality right it is the you know something that makes something happen in real world so there is a causation between X and Y cannot happen with objects flooding but the opposite may or may not be true I think can also be passed by you know every chapter Levy or create a second then we have the notion of the correlation which is a different terminology and sort of the way we understand is therapists say it's a mutual relationship a connection between two or more things and the strength an example is that temperature go up ice cream sells well now you can have incorrelation positive and negative correlations so given these two terminology and their understanding I have a couple of questions for the audience one is do the able to mean the same thing is causality same as formulation anybody oh okay nobody wants to flick a guess okay the answer is no they are not the same and why is that important it's important especially when you are doing mining next question which of the two are we trying to identify through mining are we trying to identify causality or are we trying to identify correlation but but what do you mean by mean by both we are trying to identify the causality and correlation almost right but I would make a small tweak to that a little bit later okay somebody else has face behind you want uh yeah uh I think we try to in research to find uh correlations to maybe explain later the console the causality of the of the research I think you're right you know that that's what I want everyone to understand clearly so but that you have some good answers so we want to identify causality through mining art for any real life publication we are interested in facility right just because you see flooding uh doesn't mean you have a heavy range so we want to understand this but the problem is we don't know how to identify causality in an automatic manner we just don't know still so what does what do we do we try to identify correlation and hope that correlation means there is some tonsality and that is where the domain expertise comes into future you cannot take every correlation and and say this is because of causality that is that that will not be correct I think this is very important to understand otherwise we can make mistakes but we also know that correlation does not necessarily mean causality but many times it means because we can through programming or in by automation we can establish correlation between two things or two data points or two sets of data points so we can identify this but we want this so this is the dilemma and the difficulty for mining so here is this is the best thing you can do why okay here is something that I show this I just show a couple this is this is very uh interesting and hopefully drive from the idea let me see we will I'm sorry okay so here is a website that talks about spurious correlations and I wanted to look at this you're spending on science space and Technology correlates with suicides by hanging strangulation in soup kitchen so this is what correlation gives you and you should not interpret their socosity for this it's obvious but for others it may not be obvious same thing here number of people who drown by falling into a pool for next week films Nicholas Cage appeared in that's it so you you get the picture I think this is this is called the most important thing I will try to tell my students when you are doing mining be aware of it because it's very easy to interpret things wrongly and not understand it and that is why it is so important to for businesses it means sending millions of mails or calling millions of people and not getting the expected result doing a campaign so I I have a a bunch of slides that I'm going to skip because these are mostly for an explanation that you can use and I'm going to go to but so go to the important ones so what is not data mining so it's also important to understand and not get confused between some things we do uh are very determining or not so here are a list of things data what you do in data warehousing is not data mining because you're asking specific queries and doing complex and it's a complex analysis does not mean you are inputting new data ad hoc querying which is typically done or report generation olap which is associated with database data visualization it's not necessarily so you may infer from the visualization by looking at the visualization you may info something like data visualization is just a regular tool agents mediators pervasive computers I just put selective a bunch of stuff because this is this is important to understand that mining is different from other types of activities that we routinely do do a lot so here is uh maybe after gets Dynamic for so what data mining is not likely to work so this is kind of a very tough thing to think about right so this is purely my perspective and you know other things that are still not possible and if so what kind of things are those certainly mining cannot do every kind of influence so here is sort of my take I I don't think it can substitute for human intuition and generalization this is important to understand because when humans come up with a hypothesis of a theory it is not necessarily based upon very large amount of data that that is the key whereas when machines do the same thing they're using very large amounts of data so humans don't work well with very large amounts of data but they can infer things from very small samples small examples that that's one big distinction but I added this line have to wait and see where chat Deputy takes us so charge DPT for those who don't know is an AI system that have been released or sometime now which can do a lot of things lot of things that were not being done earlier we are worried in computer science that you know it can do homeworks it can write essays it can answer any question you want and we are worried about how to deal with that in the instruction so this is a real thing that's going on you should look it up so here are the things I think a data mining system will discover does anyone have an example well here's the first one equal to M system now this is one of the famous equations that Einstein came up with and he did not use a lot of data to come up with this equation which is true and the story is of the what happened is to verify this particular equation scientists have to wait two years for a solar eclipse to happen and only after the show he published this paper based upon his theory and intuition but could not be verified till two years later and then thank you sprint and made the measurements during the solar eclipse and they don't verify the theories in person so I was in a workshop with physicists a few years ago and I asked them this question do you think this can be done using Automation and their answer was they didn't think so similarly we have a lot of things uh this is an equation from chemistry gravity Newton's loss of motion we don't know if GPT is up to the task but it's very unlikely that some of these things can be automated on a human intuition can be substituted by it may be possible to discover things like black holes which observally data dependent and we can plot lots of data another good example I can think of is the value of pi value of pi is data driven we know that but most likely it was discovered not using data but by intuition by looking at a few samples not working well that's not good so uh we have been discussing data mining can you still see my shared slides I I can still see your slides okay thanks so I mean when you think of data mining you can think of predictive and descriptive methods and predictive methods as the name indicates use some variables to predict future variables of the other variables restrictive methods buying patterns that may be of interest that can represent knowledge so here are this kind of a list of or two kinds of data analysis that we do one is known as supervised the other one is unsupervised I think it's important to understand the distinction between these two so that you know what so this is driven by some known information about the data and it's called level data so we associate what is known as a ground truth ground truth is something that we know to be true for this data some of the examples for labeled or supervised is take for example the weather prediction you know the ground Truth for whether prediction once it happens so you have accumulated hundreds of years of weather information knowing all the parameters and what was the actual weather so the question is can we use that information to predict future whether based upon the attributes or parameters associated this is also true for loan sectioning for example when you apply for a loan how does the bank determine whether to approval loan or not because they are sitting of tons of information where they know who paid off the loan and who did not and they have more information about the individuals in terms of demographic symptoms age and profession and others that can be used to determined so there are a lot of examples where we have ground put and if you have ground floor then the question is how do you make use of this ground code to generate a model that can do the prediction so that is the supervisor unsupervised essentially says that I don't know I don't have ground pools but I still want to get some meaningful information or influence from this one driven by now known information about the data it's more of an exploration of relevance and finding new patterns released on the main Mount value so a good example we use is clustering for example you don't know how many clusters are there in a given set of points so you you have to experiment with different ones and see which one makes sense so Association rules is another example of unsupervised learning where we don't know what patterns exist subject mining block mining is another problem so you will go into you'll understand more of this later in this Workshop but you need to understand the difference between these two curves sample name of the pro so there is classification or you need to understand if something I might say super right why you need to answer so classification is essentially classifying unknown data into a set of values that have been determined using another clustering if I'm supervised as I mentioned Association boost is unsupervised text classification can be supervised because you can use some data that can be even manually annotated for example we do that normally detection map mining neural networks are usually supervised because you have labeled data using grateful generator various kinds of things so deep learning Muslim supervised big data analytics can be both both of these so kind of you need to sort of no way to use which technique and life so most of the times you'll be doing both depending upon the data and depending upon what you want to get out of the data so data mining is a process many times we only look at the algorithms that are used for mining but it is not just an algorithm algorithm is one part of it I think what is important to understand is that you have to first select the data so I think you you'll see more of that later so it may be in a database a database it may be in a data warehouse it may be a file it may be somewhere you have to select which data to use you have to do some pre-processing then you have to you may have to transform data to a particular format that is accepted by the mining algorithm and then do the mining and then you analyze and once you analyze you have to see whether that analysis matches with that the main information if not you may have to get through this by creative process to do that so this is this is important to understand it is not just a One-Shot thing just taking whatever the output comes and then saying come there so if you want to understand the difference between Mining and Big Data here is one way to do that in this example you know don't worry about what is inside this one what is important is the the parts of life cycle process so here we have a data set to have a bunch of ways to mine it to get results which again you have to choose which one to apply and only here this is a much broader process or application you may have a set of data description and then you have a bunch of analysis objectives and you may want to convert this data into a model it can be any of the models here we are shown because we are working on this one and then you have to generate various analysis Expressions which may be one of the mining things then you apply them and get the results you want to do some drill down for example and then you want to show this so this is a life cycle of what we want to do for a data to understand it and memorize it in for things and do that so this is a much larger process compared to mining again uh around 2000 there was lockup extensions or or mean things that happen like census and gizmos that that generated a lot of data and how the question was how do you process the kind of data that is generated you are also seeing a similar thing with with Twitter for example of data generator is very large in short span of time so we have a budget called Smart Home Project where we had sensors in different parts of the homes that were generating data and So based upon that we are trying to input our predict the activities of the people who are living in the house for example and that is not an easy task so this is useful for various types of monitoring today this is used for for example monitoring the quality of water again you get samples every every minute or every five minutes monitoring Environmental Quality for example monitoring Bridges they're even used for monitoring of buildings uh different type of things in buildings so that they are continuously uh evaluated or data is collected continuously and and inferences are Beyond to see what is doing something what is happening in your system so this is a very this was a novel application at 2000 and mainly because of the inexpensive sensors you might have heard of RFID tags that's one of the sensors so RFID tax was very popular and today some of the garments include RFID tags in trace the lineage of prominence of you know with this item originated and where all it went through and waited to end so it is used for in Pharmaceuticals for example to tracking drugs that may be coming from sources that are not legit so this can also be useful in Assisted Living Healthcare environment marketing security monitoring so this is mainly because this data is generated 24 7. 365 daysco so the data is coming in at some rate and somebody has to process it you cannot just collect it and keep it data semantics is slightly different from earlier traditional data can generate display data location value image audio so let's see this one computers so data warehousing you will you encounter this because a lot of data today stored in what is known as cloud data warehouses as well so why do we want to uh or widely connected abms is worth picking maturity Enterprises used multiple dbmss many a time from different printers so this was a problem this could happen because of mergers or because one unit is is using one database the other unique is using another database and they cannot talk to each other they could be heterogeneous databases queries could not be posed across dbms as you could not pose a query between inventory and sales for example and that is very important analysis and Report generation using multiple different were also a problem so data warehouses were proposed as a solution to this so briefly this is the kind of architecture that is typically used what you need to understand is that there are multiple data sources most of them are dbmss but it could be of different kinds of businesses and there is a Warehouse integrator and there is some metadata associated with that purpose to operate vectors so you can think of this as a middleware if you will and then there is the actual data warehouse so what happens is data is collected in only needed data for analysis is connected from each database periodically because this has to be done oh in real time actually because these databases are changing every minute but typically this is done once in a few hours so that it's easy to do that and then this database of this created it has its own schema and then there's a query manager on this analyzer we can also run data mining algorithms on Lewisville most data so this architecture is is became very popular this is almost this is supported by almost every vendor today every commercial vendor and it's being used so this is no longer a research project it is available on usage so a complete decision support essentially includes a database in component includes various types of information sources and then this olap is the online analytical processing this is multi-dimensional online process analytical processing and then you can generate much better no complex data analysis from these data and resources into this one so this has become very popular and it's very widely used so to kind of this move one away from Individual dbmss to collection which is why it's called database works today uh even though there were developed a separate system today all major vendors of debris is supported resources data marks or smaller forms used for specific purpose today there is a terminology data Lakes is popular and related to Data Warehouse or storage capacities that mainly store or data of an organization will come a little more of this on cloud database simulator in disruption so give us another technology that was found to be extremely useful remember I mentioned full versus push earlier and this was the thing that again this technology has become mainstream it is available in all dbmss today as triggers if some of you have used triggers in a dbms that's basically this one so what is uh what is this technology so this is the alternative to what we call the print Paradigm that we saw earlier we've been using full Paradigm for a long time we still use it for example when you do anything on the web essentially you're using search or reading which is a filter so the question was is there a better alternative if so what is it and how do we quantify it how do we generalize it where is this Paradigm useful so we did a lot of research in this one some time ago and it was done in the context of a dbms even though it is today used so all the notifications that you today on your phone and other places is based upon this particular technology which is the push technology instead of the tools technology so in a traditional dbms you had to pull answers you have to write a query you have to get answers if you did not write Equity you would not get anything but that was very not very useful what one wanted was the push Paradigm where you get a notification or an answer even though you are not writing a query this is very useful and very powerful we have seen it first in you know Airlines and others do that if there is a change in your life schedule you want to be notified because you don't want to be monitoring that every five minutes every half an hour you want to be notified by using our question so this is the basic idea but in order to incorporate this idea there was a lot of research that can go into by adding components into the system that will facilitate you to do them and some of the components were you have to express what you want in some way either as business rules or constraints or invariant of situations to monitor I mean the system has to understand it keep track of it whenever change happens it has to push that information so this was this was very important even today uh doing it in a most General way for large systems is not very useful you can do it in specific applications very easily this can also be a distributed system that is based upon when we walked and implemented such a system called the just inclined push system way you could subscribe to whatever you wanted on the internet so for example you could subscribe to your page and say tell me when this item this topic on this page changes so you may be a sports fan you may be interested in news you might be interested in something else so you could subscribe to those things and you will be notified automatically when those things change without having to worry about it so this you'll see in so many different places today in so many different ways uh this has also been integrated into dbmss as triggers so it required an even specification language integrating it and developing other ways of doing it or not going to the details but today complexion processing is mainstream it is appropriate one many systems the next topic is the stream data processing the slide Edge I should be should have been here so the question is what is a string data unlike traditional data that you use in my map for example you grow and register for a course you go and change the course you drop a course you add a course a stream data is different from that in the sense that that is coming in as a string this could be from a sensor this could be from a device such as in Twitter it can be from any of those things and the question is your your stock price change for example can be seen as a string your traffic package when you make a phone call how they get routed can be seen as stream routing so it is considered continuous as one of King is 10 or long page okay so this posed a bunch of additional challenges that were not addressed in previous systems for example earlier with the dbms architecture you have to store everything in a dbms and then you could query that now this Paradigm was no longer appropriate for stream data because real-time requirements were Paramount and when you try to put the data into a database and try to retrieve you lose valuable time and it cannot be a real time anymore instead a different architecture was developed when you process the screen data directly and in real time only using main memory so dsms architecture and various substitutions reduction there from this one so not addressed by traditional dbms Neil dargans single pass algorithms processing without losing internet data vacancy requirements were done kid is a good example of why it is important if you are doing the battlefield application uh actually today this is true a lot of children's carry multiple sensors on their body in the battlefield and the information is coming in so you want to know whether a solder is needs help whether he's in good shape so Soldier ID location how create all this is sent from the sensor to a nearby processing center and that has to be processed by various things so this is actually happening so imagine if you have 10 000 soldiers each carrying five to ten sensors and each sending it every 30 seconds or one minute how much of data is coming in so fast here the process is to identify things involved the same thing was used for my home project again sensors were used for climate control or smart sprinklers robot lawn mowers no lock Control Systems Etc today a lot of these are available you can buy some of these things and deploy them in levels and other places so they have become more or less mainstream so this was a research area around late 90s and 2000s so here are some of the applications in the battlefield the main find household there's no needle and also there's no need help and all possible helpers who are within 100 meters so you could you could communicate and see cap so these are the kind of queries of situations that you want to monitor from the data that is coming in continuously and notify the appropriate person to take the appropriate steps so this was also used for road safety I skip that again uh there were some changes so every every several years you see a lot of changes in networking Hardware software and everything so on we're talking to network was getting matured before that network was there but it was not as stable as reliable and as last and without that a lot of things could not be done so this also led to the explosion of the internet for example internet it's not possible without the label underlying Network architecture this project was funded by data defense Advanced research project agency and was developed for military requirements but then it became a dual use technology internet was mature access ability to access data from anywhere else platform this is very critical today you may be taking it for granted you can access any data from anywhere but this was not the case earlier high performance Computing required clusters that was also very expensive with click to maintain and they're working much more do not access resources on demand if you need it new resources to process you could not do that because you cannot provide that on a short notice cost of maintaining clusters was five so what was lacking was an ability to use the sources as needed when needed and pay only for the resources used so this sort of as you can see that you know from only at times this was a big expectation or a child order so cloud computing was born mainly to meet these expectations and today cloud computing is there you might be using it as you know AWS or Google cloud or any one of those things so let's understand what cloud computing is is selectable because you may be using it even for your music so here is a good example to understand why those requirements came out so consider Wimbledon this gets played two weeks in a year three weeks in a year they said gets extremely high traffic in New or three weeks when the championship happens for these two weeks this site will have high several usage for the rest of the year the site will have more traffic and hence most of the resources will idle so this is the problem the problem is the speed capacity so you have to provide capacity for the maximum usage but the maximum usage is not constant so this meant that you had to buy resources in even when you're not listening so this was the case in the previous It Centers used by different companies they have to maintain an I.T Center throughout the year and upgrade it and staff it whether they used it or not so the notion of Internet scale elasticity was born which is the ability to increase capacity without trial indication so you just ask for the capacity and you will get it you don't need to tell anybody in advance that you are going to need this capacity two weeks earlier or two days earlier to the traditional approach up to that point was keeping up straight capacity to deal with the needs of the maximum usage in a year in this of expensive Hardware as you know in our domain gets old and absolute very fast maintaining and managing that is difficult software acquisition and maintenance is also an issue so it was not possible to Outsource this just for first two weeks we could not say can I help Source this for two weeks and not worry about it it's not possible to rent so these situations and needs will a side effect of internet availability and ubiquitous usage making things available on the web is critical Enterprises were maintaining expensive I.T shops and all the thoughts and headaches that came with the cloud computing was promoted as the answer so cloud computing means makes computer infrastructure and services available On Demand on need and On Demand so these are the two key requirements so you should be able to get the results whenever you want and also we'll see without having to indicate earlier the Computing infrastructure could include anything it could be use of storage it may be a development platform it may be a database it may be computing power or complete software implications to access these from the cloud organizations do not need to make any large-scale capitalism kind of this was seen as a a way to level the playing field for small companies earlier entry into a domain by small companies was extremely difficult because of the capital cost involved in setting up the whole thing and this came to do this too so what is cloud computing so you can do paper use organization need to pay only as much for the Computing infrastructure that they use it is not that we are seeing it for the first time we have been doing it for electricity whatever and gas all along we don't tell anybody when we are going to turn on our air conditioning you're not going to tell anybody when we want more water we just use it so this is the model that people wanted for computing resources and cloud computing was the one skill that's what provides this so two new cloud computing or to use cloud computing a bunch of complements are necessary one is what we call a thin plane we have this Thin and Thick line Thin Client is one that does not have much capability that can just communicate with something uh on the back end and then give you the results but most of the times what we use today like a laptop or a desktop or even a phone is not a Thin Client that's a type of lot of capability that for smart ways and things like grid Computing or server forms links displayed computers to form one large infrastructure harnessing on your skin process the notion of utility computing paying for what you use on shared resources thank you pay for your publicity linkage on-demand resource of publishing not static publishing no need to indicate so these is what we are seeing today and that seems we I'm only think why this has not yet happened for internet maybe due to radio political and other things but internet could be done in the same way you just have internet by default and then pay according to the users so for those who understand it so there are you know economists or counting people call something as fixed costs capex and variable cost office so you can see that the in the traditional I.T you have a lot of bits Plus in response square of rectangle represents fixed cost variable costs change depending upon the users but this is always fixed this doesn't change and the question is this was the barrier that was there for entry because without this you could not do this so essentially what cloud computing that did was to only use the variable costs and not preview the fixed cost because are maintained by the cloud service provider and what you pay is for the usage which is available cost then you can determine how much usage you want how much you can afford so this is a big paradigm shift in how Computer Resources were being used wow another way to think about you know our Cloud says you know you are clusters supercomputers which are not there in your own grids clouds and Web 2.0 came along and we are in depth 3.0 some some of these two application oriented whereas what you see today in cloud is service oriented so there's a difference between application oriented and some resoriented Services provided you can buy the service application 19 may have to develop your own applications and manage and maintain um useful so that is sort of the into Computing so two things you need to understand is pay as you use and on-demand production these are the two characteristics that the end users think of but managing and maintaining and supporting that's a different about so what is Big Data so an easy way to think is uh you know the size is big but it's not just the size in addition to the size you have diversity of data and what you're interested in is holistic economics so this makes a huge difference we know how to process individual types within your how to process an image we know how to process a graph we know how to process transactions but we still are not good at processing all of them together or even mind however to get a research so a good example I give for this is the healthcare if you want to do any kind of analysis in healthcare you need to be able to bring together different types of data it may be pathology data it may be x-rayed maybe MRI it may be you know subject related information so you have different types of information that needs to be looked at as a whole not individually and then you can make a informed decision and that is skill is quite elusive today even with all the electronic patient records and other things because there is a big push towards health information exchange which has happened to some extent you can see that but we are not there yet but usually big data is characterized by what we call through these and they scan for volume velocity where I came and velocity so we understand volume volume is the size velocity is what we try to relate as screen data this is this speed at which data comes in a traditional database the speed was slow you know students register for courses only every semester employee information doesn't change very much but with stream and sensor data on Facebook data this velocity is very hard so you need to be able to deal with that variety as they were saying you have audio video images that you need to deal with veracity is another aspect which is the amount of trust or confidence you power in the information so this is also very important because if you take data that that is not trustworthy your analysis results are also not prescribable and you need to be able to differentiate this is one place where the prominence as we call the lineage can play a significant role in understanding with the data attainment whether the source is trusted how much they can be trusted and how much importance can you place on the analysis you're doing so this is important to understand what differentiates what we today call Big Data from other kinds of data so we we are good at processing these things individually but we are not good at age processing them together so in the literature if you see there are so many other ways that people have tried to add to this at least any any word starting with a real Bell okay to add variability but I think they are not they're not characterize Big Data so where do big data come from so we are only against this you know later on colloidal telescopes or various telescope that we send out generate tons of data we have multiple steroids of treat data every day 25 plus terabytes of data every day from other resources billions of camera images satellite images probably so the amount of information generated is is not the problem and this will keep getting larger and larger the problem is how do we use this information rather than just dumping it and forgetting about it then just as an anecdote NASA which collects so they don't store the data on disks why because the size of the data cannot be held on this so they have warehouses but not databases warehouses physical warehouses which thousands of tapes on which the data that we have collector is stored so researchers can go and request that information and get that information so the amount of information is so large that they cannot just keep it online for everyone to use so these are just numbers in terms of this one so the big picture sort of my view of the big picture which is very similar to what I showed you earlier is the problem so it's the same problem but the input has changed the input is no longer a single type of data it can be structured data and it can be image data it can be audio video data it can be unstructured data and you have just not we are just sort of or blindly exploring data but you have some analysis expectations what you are looking for what you want to look for Plus you other kinds of analysis and the ultimate goal is to extract and visualize knowledge in a meaningful way so we call it transforming display data into actionable knowledge so actionable is important if you cannot take action based upon the knowledge then it's not very useful so it can be any kinds of data so this is the sort of the big picture for what all of us do whether you're in but scientists showing so it may be a small subset of this but this is the bigger picture so you have unique signs you need abstractions you need various theories you need analytics different algorithm different types of algorithm faster over events so you need both of them in order to get this one what is data search so data science not new again it's the same things but emphasis based on understanding and managing data the spacing and dicing data compare female and Engineering data mining drop and exploratory and Discovery component now we are combining all aspects of application business with computer science and statistics for inferring or discovering Android move so this is the one of the holy grain for updating lenses so enablers again looking at what kind of Technologies how rock is here similar to what we saw but you'll see that the Technologies are slightly different so this is one way to think of it's a a combination of synergy between computer science mathematics and business application and in terms of various specific techniques machine learning techniques software development humanism this is very important because still data analysis I think cannot be done without a human interview I mean we want to minimize the whole of the human but we still don't know how to eliminate it because somebody has to interpret an understanding think whether it is right or wrong so to me data science and data is not a single approach at a single solution if there is no save at the lake it's a it's a it's a complex of process involving many moving parts using extending not only current approaches but also developing new ones because we still do not have all the technology to combine different types of data and they still need to develop if you will need to switch up approaches or modeling and immune so modeling is very important you cannot just use data without modeling it in some way that helps you process it or analyze it better a diverse complex data set for a given sub analysis so so that's what it is what each of us may be doing Maybe a small component possiber of that so given the one way to describe it is given a complex data set less analysis objectives determine or develop modeling abstractions analysis methods and visualization so kind of this is kind of the task for computer science people but the consumers of all of this will be people who use it in biology of science Water Management plus you may be developing your own techniques that we do not understand or we don't know about so again going to the same diagram so this is a big data analysis process mining so to sort of summarize what I have covered in velocity or whatever so so we have sort of covered what sort of things happening between 1970 and you know today so we started with you know file systems before this so before then gives somebody everything was done using file systems and writing applications and other things and then came hierarchical and network before that and relational so they made life easier supporting events laws so what you see on top or abstractions that are supported for end users what you see at the bottom are obstructions that are supported underneath or automated as part of the software and middleware whatever you want to call it in various ways so the abstractions that were supported for or relational was multiple users will come back to this with later durability and things then came data available vertical integration integration of multiple data sources into useful database multi-dimensional analysis and one of the challenges for how to keep the data fresh if if you are collecting data for multiple sources you have to make sure that data is not old and you it's still a problem today if you think about what Google does right I believe it takes Google about six months to scan the internet what changes six months is a long time so that's why when you get a result from Google it may be a little bit older it may not be fresh but for the kind of things you are doing it doesn't matter but if you are making some important decisions and other things freshness is very important so Google also and all other they use web callers they have very sophisticated algorithms to determine which side should be called more often because that site changes more often than from other sites it's not that they just go in their own robbing fashion that is not the case so so keeping data fresh and this is also a an issue with uh with charge repeating I I don't know you you are aware of it so so it seems you know people were asking questions and and charge GPT uses data that is two years old uh because you know that has not been integrated into its vocabulary in some way so when asked about something the information it was giving was certainly took more than two years old so that that's an issue of questions data mining became very popular and widespread and used on a very large scale in the 90s it was made even before even in the 1960s there were mining algorithms were being developed on supervised Market Basket previous things that came screen data processing you know or real-time data processing or various latency issues uh quality of service specifications then we have a big data analytics I only studied a few things that we do in the itlab that there are more things than this one obviously so the other thing I should maintain is so the whole point I I feel that without understanding the past to some extent if not in detail it's very difficult to appreciate the present and plan for the future so what I have tried to do I think as part of this exercise is to give you a kind of the roadmap about how things happened in in a short way and why we are here what contributed to where we possible the other thing also I think is very important is I I try to emphasize this to my students is technology provides Solutions but it does not necessarily solve problems I think there is a big difference between solving the problem and the technical solution I think it's important for us to understand the difference a very good example is code without solution but it certainly has not reached everyone not because there is no solution but various things cultural political Financial things come in the way of solving problems this is true for every technology developing the technology is one problem using that to solve problems real problems is a unique challenge in itself and I think we as technology developers and users should understand it clearly just because you come up with something doesn't mean the real problem whatsoever okay so now in the rest of the time what I want to do is to focus a little bit more on the details of the analysis which we mentioned earlier so District analysis is a method for quantitatively describing the main features of theater typically use statistics and shows the measures for doing this so for example you can apply descriptive analysis to census data that you are familiar with continued outages frequency distributions percentile systems distributions of household income for various term type in there so so you can you can pay with the data and and descriptive on the other hand is more of prediction of what action you need to take based upon that finding the best course of action for a given situation it may be preceded by descriptive analysis it's a process intensive task analysis potential decisions and interactions between decisions you may have to do it in real time goal is to prescribe an optimal actionable decision you may use optimization simulations you may you don't know what kind of analysis you'll be doing and 10 years ago so here is an example you have the latest census data suppose say you want to know the top five states with largest increase in population now this can be done with descriptive analysis right you can compute uh the changes that have taken place you want to know which states how income is likely to rise in the next 10 years so this this question is different from the previous question that there is a qualitative difference between the two this can be done with descriptive analysis this cannot be done only with this crypto analysis because we are predicting what is happening in the next 10 years we want to explore the rate of something in general you can use both of these both exploration or set space can be large so need to have some idea of what we are looking for and then do that so I hope I'm able to convince or convey the difference between these two types of analysis the other thing that you should also understand is data analysis can be done in many ways you can do it manually it was being done manually and the advantage of doing manually is that the person who is doing it has understanding that the problem and the contact the music tuition that scalable semantics can explain your analysis business but it can be available remember the national Mars British measures were used to insert the use metric system and the elevator explored you cannot deal with large amounts of data humans are not good at dealing with large amounts of data but they can understand small amounts of data in a basement flow complex complications are also difficult so manual environment is still needed in Sunday we cannot completely through it if we look at automated approach that's what a lot of us do today Awards competition others assuming programming is correct this is a perpendicular can deal with very large amounts of data analyzed in multiple ways takes less time but someone has to come up with our variables someone has to design the program or system someone has to validate the system someone has to sign teaching the producing yourself so these are still difficult to do in an automated manner human in the loop or hybrid mode this is very much the essence of data science humans play is small but I think they play critical role in the analysis that is that so there are advantages to all of these different approaches so let me illustrate it with a known example suppose say I'm doing a manual approach or analysis suppose um reading it so you're all familiar with that so I can say it can be done with absolute methods some number you know you'll get a b and Central numbers in PCD but humans can deal with small variations what if somebody gets 84.9 should that person get a B R any so this is where uh human scan adjust or pull things slightly different from another example suppose say I'm using a curve which I typically do say in class average plus one standard deviation is a again what if someone may stay by a very small amount so I can look for separations then make exceptions based on interaction therefore put in plus partition types of persons asked so manual approach has some merits but you cannot scale it what is the class average is 82 percent I have one very real semester where the class average was extremely very unexpected close to 90 percent and the standard deviation is eight so you know everyone has done so well that you don't want to just apply this Rule and just say that's it should one give eight to ninety later so this is the kind of the uh problems or issues that you need to understand when you are doing manually advantages of automatic approach by fast and generate reports for human consumption can visualize we use that abuse spreadsheets and graphs a lot easily come compare alternative analysis but sometimes the difficulty is in the explanation account this is very true one of the reasons now neural networks are very popular deep learning is very popular but still we have a lot of difficulty understanding why it works it works for second Train table data set but if the data set changes you have to come up with the new new element generalization is gifted to not plainly assume that protest correct each Center chip validation on small sample data need to be aware of changes in concept expectations Etc so data analysis in in minutes is not as easy as you think running a program you see the looking at the results is easy but when it comes to actual understanding instituting and Analysis that more has to go into it before you do that so the bottom line is we want to process Raja notchable we want the flexibility to slice and base later in many ways you want to be fast you want to build incrementally that's very important because data is coming and you want to be able to add the latest data and look at how things have happened rather than throwing the classes all data which takes a lot of time we want an efficient proportion if we measure that in terms of performance Cape speed up on scalability we also want liability if something goes wrong so how many times have you ever heard somebody say no oh this was a computer problem it's nothing like a computer problem like exists who will develop the software did not develop it right we want to out complete others in the same business so so then the next question I think this uh maybe that will in this game upload tomorrow's flight time but typically we use Python but the choices are in a python a heart Studio bandas others which one is better actually it depends upon who you ask and What needs of all of useful learning curvaries that is the key so learning case will booster this is so what I have now is in the time lapse two sort of examples so this I'm not assuming any python background for this just to show you I mean these are class projects that I have given to data science course that I was talking about they learned python while learning python they were doing some projects to learn analysis like the way I have respected earlier and these were used as uh sample projects so one was some Census Data analysis one is so we are given so there is data for 1990 even later on so I gave them only 32 000 rows but if you look at the entire sense of data it's much more than that the original data has already been pre-processed as follows so discretized gross income into two ranges so this is not the data was convert to some changes some formats into this one to make it easier than what unknown to question marks sample input comma separated so this is how the input looked like so each line contained some number of attributes as we found it so these are comma separated essentially CSV files 32 thyroid so the question is if you are given only this what do you do with that so this is where wait a minute so if you have given only this it's very difficult to understand what it means this is where as we shall see metadata and creating proper metadata is extremely important for someone to understand even for a simple a data set as this where you can guess a few things but in more complex data sets it's even notice so here is the description so typically this is what you see so these are the descriptions of each field so for example in the in in the 32 is the work class and others so there are so many types of our class education education number marital status observations on so this at least tells you some indication of what it is and then you can use that information to understand the analysis or even what to do the analysis so what I asked him to do was to do two or three kinds of analysis one was they cover the number of people in the following groups in age less than 20 21 to 40 41 to 60 ingredient system just to find the kind of age groups and the population among these age groups from the data that is given there are the histogram to understand it so that was analysis one analysis 2 was for the average age to find the number of people in each of the following professions so kind of this is what we call drilling down so you have a result and you want to understand more about the results in in these groups how many people work for this particular type of employment in this important what do I separate pie chart for each so this was to give them an understanding of one how to use the data understand the data and how to do the just a simple analysis using packages and also how to visualize each other it's easier to understand so this is for drill done analysis 3 was identified top five occupations for the population so this is more of a ranking question so we want to know which type of occupation occupies the highest point and so on so so we also gave some idea of how to do that so I won't go through the python code I think you will learn all about this tomorrow and you'll be able to reduce so here is the histogram analysis so you can clearly see from this there are more people in the age group 21 for the in this data set than other age groups so there are very few people for less than 20 very few people get 16 months at the bulk of the population you've seen this one so again we were using packages to to practice and see how how it will do the analysis and representation to the second analysis essentially use pie charts where you can see that for this group what was the baked on for different kinds of occupations so this is only self-employed private so private seems to be more among the younger people as compared to the older people and you can also see that as the age changed the more people migrated to government jobs so you can see that kind of you know what stability or whatever it is you can see some understanding that about things happening for the last one we had uh top five ranking so proficient specialty job was the highest in class rather than any Syria let's get used Administration and sale so this is how the data so another way to look at it so we also use different visualization techniques so this one is known as World Cloud you you might be familiar with it you will see in in TV news and other things which particular World appears uh more prominently in any discussion and other things you can it's easy to understand for example the size of the the script or the font size not the point but the size indicates that it is it's more prevalent in that so here for example this one has the bigger size then comes classifier than this one so this is a very easy way to visualize favorite results of the analysis so that you can immediately see for example private house like Protection Services very low on forces seems to be very low in this literacy so this was so they did this over a couple of weeks and then made a presentation and submitted the report so kind of what we want them to do is to go through the entire life cycle you know pre-processing the data and even trying it on a small sample for Sandy checking because they want we want to make sure that their results are correct because when they write a small program even if they use packages we know packages are correct that doesn't mean the rest of the program is correct so that's that's an important thing we try to enter so second one this is more about descriptive analysis so to give them a taste of how this analysis differs from the previous one for example so we gave them Airlines data we're a little bit older that was available so they have given large Airlines data indicating the flight socket at Berlin Airlines purposely we replace the airline names with anonymize them if we will because we wanted them to find out which airlines it is the data set contains the following information so it has comma separated field but the results for a a description of what they are so this is the sort of the extent of data data that we typically find in in the computer science student literature which is not a whole lot compared to what you're trying to explain with say against yourself this certainly is useful but not sufficient enough to do anything about the small prominence whether it's nothing even as possible so the analysis that we ask them to do was analyze two specified Airlines given to them construct a graph or a black data structures for the airline with airport code as the vertex drawing and directed graph between two points in each line since many per countries only accept integers that's what extremity map the three letter core we can use dictionary information so we give some gifts as to generate characteristics for both Airline route this will help understand some of the characteristic the data interpret them from an airline's operation perspective and and see whether you can identify which airline it is based upon this information so find the top three to five nodes from where there are no flights than others these are Subs so you can use nerve Central intentions like that so again what to use when to use for what part is is an important aspect so once you have the top kfobs try to identify the airline that you are working on you can use any data that is available on the internet for this purpose we will give you a file that maps report portrait for payments and service in the next step of the analysis your goal is to identify or predict the next step for airline expansion if the airline wants to expand their operations which city would they want to choose and why because this you can use demographic and other information that is available so again this one is not just understanding the data but it is more than that trying to figure something out that is not obviously part of the data that is clean so the approach was given so I'm going to skip some of the things and show you the results I'm going to skip that pattern would explain okay so here is a graph now there are using those tools you can expand our zoom and in blue things you can see some nodes that have very large number of edges so lhr happens to be London Heathrow Airport for example so you can see that this is one of the prominent it works for this Airline DFW has a lot of lines this is another permanent airport Miami is one of them and uh I can see those three clear ones so you can see from this you can get an idea as to which airline this could be based upon the information that you're seeing so again if you use the word cloud you can see more information than the graph you can see the view foreign okay um this is for entry Association of the frequency but you can see it from here you can see Atlanta is one of the big airports JFK um DTW is Detroit this is the slow Source like City so I I think so you can see that from the data set you can get this and then further analysis uh so we also do various kinds of analysis to understand the data set number of nodes number of pages diameter density of layers component clouds average between your so all these information are used to in different ways maximum degree of graph now that means it has 184 flights or connections with them similarly uh from am3 so I I don't expect you to know the new or this notion of decrease centrality but uh this is one that detects how many edges are there for a no and it is ranked by the number of edges which happens to semantically coincide with the pumps for an error So based upon that so for example uh here are the airport and the airport names it is centrality so based upon that you can you can identify which airports are the top three airports and given that you can also identify them as Airlines Jamaican Airlines service or just an exercise in trying to put things together and make sure that your analysis makes sense so similarly for the next one of Delta for example because Atlanta Detroit on Blue Salt Lake City buildings we know this we know this if you if you buy uh so the next one was the more oops oh okay okay approach for predicting the next time this is the important thing the next half for the direct earnings can be chosen from any of these three now these were not the top three hubs here these are taken from this one but this is based upon some additional information in terms of population education level for that particular City average mean income on various other things so based upon that you can choose which ones can be used as Google so kind of these are two one more analysis I'm going to show on Thursday icon is done we will depreciate it not better so I'm going to stop here and it's a little bit earlier than uh I should but I'll be happy to answer questions for the next by 10-15 minutes to clarify anything that that was not clear in the first inclusion
