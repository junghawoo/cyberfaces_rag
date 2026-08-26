---
title: "Justice in Data: Introduction to Databases and Data Storage"
unit_id: 134
course_id: 10
level: "Foundation"
slug: justice-in-data-introduction-to-databases
is_course: 0
---

# Justice in Data: Introduction to Databases and Data Storage

## Extracted resources (local files)

### Introduction to Databases and Data Storage Slides
*Source file:* `CTW-intro-databases-storage_FINAL.pdf`  ·  *type:* file

Multi-Source Data Analysis

Team Presentation
2
Sharma Chakravarthy
Professor

What Am I assuming
Nothing on databases!
As this audience is predominantly undergraduates, 
I am not making any assumptions on what you 
know
In some sense, this is a continuation of data 
analysis tutorial continuing with the details of data 
storage  and the use of DBMSs
Before we get into that, I will present a Multi-
source data analysis and its Challenges, and
Why we prefer Python for data analysis
3

Presentation Outline
Multi-source data Analysis
Why use Python
Data Storage
From flat files DBMSs
Need for DBMSs
Conceptual Components of DBMSs
Model
Representation
Query language or program

Introduction to Relational DBMS (RDBMS)
Why Relational DMSSs are popular?
Commercial RDBMSs

NoSQL DBMSs

Introduction of GIS and ArcGIS
Conclusions
4

Multi-Source Data Analysis and Visualization
CoWiz++ Dashboard

COVID Data: Analysis Goals
2021
-2021
Counties with maximum/minimum number of cases, deaths, recoveries, tests?
Statistical Visualization of Raw Data
Regions with maximum rise/decline in daily cases in the periods pre and post the 
vaccination drive (or lockdown)?
Temporal Aggregate Analysis and Visualization
Regions that got significantly affected due to major events like July 4th, Labor Day, 
Memorial Day, Halloween, Thanksgiving, …?
Event-Based Aggregate Analysis and Visualization
Populous Regions more susceptible to the virus spread due to the presence of 
institutions with large work force and heavy traffic movement? 
Parameter-Based Aggregate Analysis and Visualization
CoWiz
CoWiz
CoWiz++

CoWiz: Analyzing the Impact of Events (Flow)
Event for Analysis
Thanksgiving Weekend in the US (Nov 26, 2020 – Nov 30, 2020)
Equal Period Length: 10 Days
Nov 10, 2020 – Nov 19, 2020
Dec 3, 2020 – Dec 12, 2020
Severity 
Rate
(Severity of 
the Spread)
US COUNTIES
Edge exists if counties have 
similar % Change in the 
number of new cases in the 
Target Period as compared 
to the Base Period
County Communities: 
Geographical Regions with 
similar % change in new cases;
Classifying Regions with 
varying effects of event
Target Period
(Period After the Event
Number of New Cases compared 
against the Base Period)
Base Period
(Period Prior to the Event
Number of New Cases form the 
basis of Comparison)
Geographical Visualization
73, 2023
ng Workshop

CoWiz Dashboard Interface    
(https://itlab.uta.edu/CoWiz/)
S 2022
2022

Data Collection, Pre-processing, and 
Consolidation

Data is not in one place
Multiple Participants/Entities, Features and Relationships
ng Workshop
3, 2023
Covid-19 Data
Positive Cases
Deaths
Recoveries
Hospitalizations
Tests
Vaccinations
Demographics
(Race, Age, Gender, …)
Locations
(Counties/States, Universities, …)
…
0

Where is the Data?
Single Source 
Makes it easier
One format to deal with
No merging
Multiple Sources
Different information about the same entity provided 
by multiple data sources
−Potentially multiple formats
−Selection and merging data
3, 2023
ng Workshop
1

[Covid Tracking] Where is the Data? 
Daily Covid-19 Data: CDC
Positive Cases, Deaths, Tests, Hospitalizations, Recoveries, …
Daily Covid-19 Vaccinations Data: OWID
Vaccines Doses, People Vaccinated (as Number/Percentage), … 
Daily Trips by Distance Data: US Dept. of Transport
Stay longer than 10 minutes away from home
Anonymized data mobile devices
Pop. staying at home, Number of trips (<1 mile, …, >=500 miles) 
Daily Mobility Reports (Visits and Length of Stay): Google
Percentage Change from Baseline: Jan 3 – Feb 6, 2020
Data from users who have opted-in to Location History
6 Places: Grocery, Parks, Transit Stations, Residential, … 
Other Sources: Restaurant Occupancy, Census, Daily Tweets, 
Spending Categories, …
3, 2023
ng Workshop
2

Data Pre-processing Challenges
Data File Format
Delimiter: comma, tab, …
Value Format
Example: Numeric, Text, Location (Latitude, Longitude), …
Different Attribute Formats
Date: MM-DD-YYYY, YYYY-MM-YY, …
Temperature: Celsius, Fahrenheit
Measurement Units
State: NAME (Texas), CODE (TX), FIPS Code (48)
Missing Attribute Values
Not Applicable, Not Recorded, …
3, 2023
ng Workshop
3

Data Pre-processing Challenges
For multiple input files, based on which ‘common 
columns/attributes’ to combine?
Equivalent to RDBMS Join Attribute
Which ‘columns’ to shortlist?
Interesting Features?
3, 2023
ng Workshop
4

Multiple Data Files →Merged Data File for Analysis
State
Date
A
X
Texas
2020-02-03
a1
x1
State
Date
B
Texas
2020-02-03
b1
State
Date
C
Texas
2020-02-03
c1
State
Date
D
Texas
2020-02-03
d1
State
Date
A
B
C
D
Texas
2020-02-03
a1
b1
c1
d1
Joining Attributes: State, Date
3, 2023
ng Workshop
5

Complete Details for Covid Data Files

Daily Covid-19 Data, Reported by Centers for Disease Control (CDC)

Daily covid-19 related data like positive cases, deaths, tests conducted, hospitalizations 
and recoveries. Click here for Attribute Description

Daily Covid-19 Vaccinations Data, Collected by Our World in Data (OWID)

Official state-wide reports compiled for vaccinations. Click here for Attribute Description

Daily Trips by Distance Data, Reported by US Department of Transportation

Trips by Distance, and number of people staying home and not staying home estimated 
for the Bureau of Transportation Statistics by the Maryland Transportation Institute and 
Center for Advanced Transportation Technology Laboratory at the University of 
Maryland. Click Here for Attribute Description

Daily Community Mobility Reports in Different Categories of Places, Google

Show how visits and length of stay at different places change compared to a baseline. 
The baseline is the median value, for the corresponding day of the week, during the 5-
week period Jan 3–Feb 6, 2020.

Google calculates changes using the same kind of aggregated and anonymized data used 
to show popular times for places in Google Maps. Click Here for More Information
3, 2023
ng Workshop
6

Snapshot of Input Data Files
US State Vaccinations Data: 2800+ Rows, 14 Attributes
CDC data for Cases, Deaths, Hospitalizations: 20000+ Rows, 41 Attributes
3, 2023
ng Workshop
7

Snapshot of Input Data Files
Trips by Distance Data: 39000+ Rows, 18 Attributes
Google Mobility Data: 18000+ Rows, 9 Attributes
3, 2023
ng Workshop
8

Need for Configuration File
One place to change all requirements
Avoids hardcoding
paths, constants, input parameters, etc..
Ease of specifying Data parameters
Input data file path, 
Attribute formats, 
Shortlisted Features (columns), 
Shortlisted Data (rows) based on conditions,
Output data file name, and so on.
Can easily handle and merge multiple data files
Adds flexibility to add new data files.
3, 2023
ng Workshop
9

Sample Configuration File for Covid Data Merge
3, 2023
ng Workshop
0

Sample Merged Covid Data File
Merged Covid Data for US States: 18000+ Rows, 14 Attributes
(For Feb 15, 2020 to Feb 15, 2021)
3, 2023
ng Workshop
1

Is the Data Source getting Updated?
Static Data vs. Dynamic Data
Dynamic Data
Asynchronous Updates
−Every source can potentially have different frequency of 
updates.
Automated web crawl to collect the data updates
−Crontab jobs scheduled at a specific time of the day.
Parameterized on-demand calls to external APIs
−Fetch the news related to “covid” from “April 15, 2022” to 
“April 15, 2023”
3, 2023
ng Workshop
2

Modular Dashboard Architecture
S 2022
2022
User Inputs
Display Component
User Interaction 
Component
Client Module (Web-based)
Pre-Processing 
Component 
(Layer Generation, …)
Storage
Visualization 
Generation 
Component
(Maps, Animations, …)
Base Data Processing 
Component
Retrieval and Storage 
Component
Analysis 1 Component
Analysis n Component
Visualization Management Module
Data Analysis Module
Live Data
Other Data
Lookup Component
Is Visualization 
Present?
NO
YES

S 2022
Demo
https://itlab.uta.edu/CoWiz/
2022
YouTube Video 
https://youtu.be/4vJ56FYBSCg,https
://youtu.be/V_w0QeyIB5s

Why Use Python for Data Analysis

6
Why Python for Data Analysis
Python
RStudio
Pandas (actually Python + pandas)
Others
Python is a programming languages with “batteries 
included” as they say
R was developed (as open source and free) for statistical 
analysis to go beyond systems like SPSS etc..
R is also a programming language
RStudio is an  IDE   for R
Supports Python as well

7
Python vs. R (or RStudio)
Both R and Python support Data Frames with 
some syntax difference (load .csv files)
Data Frames: Two-dimensional, size-mutable, 
potentially heterogeneous tabular data.
Functions can be applied on each statistic in R and 
Python (again with some difference in calls and 
parameter settings)
R uses pipes  (a Unix/Linux feature)
R uses cluster package and Python uses scikit-learn 
package
R has more data analysis capability built-in; Python 
is limited to available packages

8
Python vs. R (or RStudio)
Both R and Python can scrape web (download pages)
R uses rvest for scrapping downloaded page, where as 
Python uses BeautifulSoap (most commonly used web 
scraping package)
Summary
R is more functional, Python is more OO
R has more data analysis functionality built-in, Python 
relies on packages
Python has “main” packages for data analysis tasks, R has 
a larger ecosystem of small packages.
R has more statistical support, in general
It’s usually more straightforward to do non-statistical 
tasks in Python
RStudio supports both R and Python

9
R (or RStudio) vs. Pandas
Pandas is a fast, powerful, flexible and easy to use open 
source data analysis and manipulation tool, built on top of 
the Python programming (financial, time series data)
Numpy runs vector and matrix operations very efficiently, 
while Pandas provides the R-like data frames allowing 
intuitive tabular data analysis. A consensus is that Numpy is 
more optimized for arithmetic computations (scientific 
computing)
Pandas is slower than Numpy
Comparison with SQL:  all of the above run in main 
memory and does not deal with very large disk-resident 
data 
Hence, scalability is an issue (memory, although getting larger 
will not handle large data sets)

0
R (or RStudio) vs. Pandas
Pandas was created for the purpose of giving you 
an object similar to the R data frame inside 
Python. So if you prefer to work in Python (which a 
lot of programmers do) but like the R data frame 
(which is more intuitive to statisticians and 
modelers) then you get the best of both worlds.
Bottom line: People are known to go back and 
forth between R and Python + Pandas depending 
on what they are doing
In this course we will use Python for uniformity 
and consistency

1
Python
Built for programmers and developers. It is a standard 
programming language than R
Python seems to be better in performance than R 
(despite being an interpreted language. More later)
Python, can be used for coding any computation 
(being a programming language), but can also be used 
for system management (for scripting) and web 
services
Please do not get confused between Panda (dedicated 
video encoding in the cloud) and Pandas (High-
performance, easy-to-use data structures and data 
analysis tools for the Python programming language)
We use Pandas!

Python Batteries
/2023
r name
2

3
Summary
Python is easier to learn and allows you to  
perform data analysis  without writing a lot of 
code
R is still used if you need to do heavy statistical 
computations
People go between Python and R
Other languages such as Java do not have 
extensive packages (libraries) – especially 
visualization -- that  can be used immediately
Also code footprint is small for Python as 
compared to other programming languages

Introduction to Databases and Data Storage

35
Recap: Data and its Management

File-based data storage and management implies

burden of processing is on the user

Applications need to be aware of the format (even if it is .csv)

On the other hand, Database Management Systems (DBMSs) 

reduces  duplication of data (hence data integrity)

Manages duplications (uses referential integrity) 

Querying is easier  (use of SQL)

Non-procedural querying using SQL

Extensive utilities (bulk loading, …)

Data warehouses 

Were developed to fill analysis void

Supports multi-dimensional analysis (using CUBE, ROLLUP operators)

Combines data from multiple sources (DBMSs)

Big Data (4 V’s): 

Volume

Velocity

variety, and 

veracity

Recap: Vocabulary
We will briefly understand
Data storage
Database Management Systems (DBMS)
NoSQL Databases
GIS and ArcGIS
Cloud-based Data Warehousing (DW)
Data Mining (DM)
Data Stream Management Systems (DSMS)
Cloud Computing
36

Recap: Files for data storage
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
Application has to be aware of the format to interpret and 
use it correctly
Slide 37

e 38
Record Formats:  Fixed Length
Information about field types same for all 
records in a file; stored in system catalogs.
Base address (B)
L1
L2
L3
L4
F1
F2
F3
F4
Address = B+L1+L2

File-based Applications
Applications need to be aware of data 
representation or format in a file (even if they 
are .csv files used for data analysis)
Makes it difficult to change the format once designed; 
enhancement is difficult
If the format is changed or extended, all
applications have to change
Application management is difficult, labor intensive, 
and prone to errors
Strong coupling or dependency makes application 
developer’s life difficult
Difficult to manage duplication and maintain 
consistency
Slide 39

Payroll Example
I was part of the payroll processing in India in the 
70’s  (file-based data was used)
Multiple files were used to process payroll
Personal information
Wages information
Hours worked by an individual
We were also using tape drives at that time as the 
capacity of disks were small
We had to update these files as well and write  NEW 
master files, if successful, for the next run
This process would take at least a day and 
maintaining the files for the next run (creating a new 
master) was very critical
Slide 40

Additional Critical Issues
In addition to processing issues, there were a 
number of other issues that were difficult to manage 
using the (flat) file-based approach
Managing duplicate information
Maintaining consistency in the presence of duplication
Concurrent usage of data by multiple users
Determining how to combine data (from different files) 
for each application
Recovery of data in the presence of failures
−This was a very difficult issue
Querying data across files
−Needs a new application for each query!
Managing large amounts of data
Slide 41

Data repository
A data repository is a storage space for researchers 
to deposit data sets associated with their research 
(data library or data archive)
A Datawarehouse is a large repository that aggregates 
data usually from multiple sources or segments of a 
business, without the data being necessarily related
A data lake is a large repository that stores data that is 
classified and tagged with metadata
Data marts are targeted subsets of data
Git or GitHub can be seen as a repository for data as 
well as code
−Done at an individual or organizational level
−Can be done in a more broader way
−Is organized and versions can be maintained
Slide 42

GIS Data Sources (repositories)
Natural earth data – public domain
USGA earth explorer – largest free sources od data
OpenStreetMap – crowd sources data
Esri Open Data Hub – can search using map, 
topic or location
NASA’s Socioeconomic Data and applications 
Center (SEDAC) – shows human interactions with 
environment. Has a map viewer
Open Topography – high spatial resolution 
topographic data (LiDAR Data) and tools
NASA Earth Observations (NEO) – mostly climate 
related
Slide 43

DBMS to the Rescue of …

… all problems associated with file-based data management

By decoupling the data representation from application software
This is a very common practice in computer science (adding a level of 
indirection and associated software for mapping)

This requires a data model to represent the application at a higher 
level of abstraction
That is easy to understand and perform computations
Abstraction levels, many a times, for different purposes

This also requires software that can hide the physical representation 
of the data model or the abstraction  
Think of a compiler that converts your program to executable code
Think of a web GUI that allows you access by filling  boxes instead of 
writing a query
This is in contrast with command prompt style used earlier
Slide 44

DBMSs can be understood
From a end user’s perspective
Understand the need for a DBMS
Applications for which it is suited
How do you go from application requirements to a 
DBMS design and use
Relational model and its simplicity
Using SQL to query and generate reports
How to use a DBMS
−Whether is Oracle or ArcGIS
From a system perspective
Implementation of components
Interaction of components

Need for Data Models
Additional requirements we listed earlier were 
derived from enterprise applications
Banking 
Airline reservation
Employee data management and payroll 
Managing inventory and other related services for a 
corporation
Earlier, files were created manually without any 
principled process and only based on the knowledge 
of the application by the developer
How many files, their contents, formats
This kind of ad hoc design could not  be carried over 
to larger above applications
Slide 46

Data Models
A new approach was needed for taking care of all the 
complex requirements
First, applications had to be modeled in a systematic way 
to make sure data is captured completely along with 
inter-relationship among data
Functionality on the captured data should satisfy 
application requirements
Data models were born (in the 60’s)
Hierarchical (led to the development of hierarchical DBMS)
Network (led to the development of Network DBMSs)
Relations (led to the development of Relational DBMSs)
−Widely used today 
−ArcGIS supports all commercial RDBMSs
others
Slide 47

EER and UML
The need and the goal was to model real-world 
applications as closely as possible
For that, EER or Extended Entity Relationship model 
was developed in 1970 to capture entities and 
relationships between entities in an organization
A simple model, yet powerful model
A popular model still being used today for the design of 
RDBMSs
−Several tools are available (e.g. Erwin)
Real-world objects as Entities and their relationships 
are captured using the model
−This model is converted (algorithmically) into relations, 
hierarchies, or networks
Slide 48

NAM
E
GENDE
R
Born-in
(1,1)
(0,M
)
NAM
E
(0,N
)
Married-to
Parent-of
Sibling-of
Child-of
(0,N
)
(1,2)
(1,2)
(0,M
)
(0,M
)
PERSON
Founded
Located-in
Headquartered-
at
YEAR-
ESTD
STAFF-
SIZE
FIEL
D
COMPANY
(0,M
)
(0,N
)
STAT
E
POPULATIO
N
NAM
E
COUNTR
Y
CITY
NAM
E
YEAR-
ESTD
UNIVERSITY
Start-
Year
(1,1)
(1,1)
(0,M
)
(0,M
)
(1,M
)
(1,M
)
(0,N)
(0,N)
End-Year
Start-
Year
End-Year
Studied-at
A EER Diagram for Company Founders

What Is not captured in a EER model (Database)
We cannot model actions in a database; instead, 
we capture the underlying data that corresponds 
to actions; actions need to be modeled and 
implemented as applications on top of the 
Database! 
For example, 
Logging in is an action. It is done through an 
application.
However, a number of data elements are used 
with constraints: user name, password, captcha, 
how often a pwd need to be changed, etc..
These data items and their relationships are 
modeled using the model (EER or anything else)

What Is not captured in a EER model (Database)
Another  example 
Although invoice is used in real-life, the contents 
of an invoice is what is captured in the database so 
that an invoice can be generated
If you capture all the items purchased (basket), 
with date, and other information,  receipt or 
invoice can be generated
Temporally changing data can be captured using 
date and timestamp as properties

In addition to modeling data
We need to make sure all needed computations 
can be supported with the data captured. This is 
done using a query language or writing 
applications
If you modeled a database, you should be able to 
ask
−which book is borrowed by who?
−generate a report of customers who have not paid 
the last credit card bill (or last 2 credit card bills)
−Track a UPS shipment to know the current status
−10 most popular movies (overall or in each genre)
−Generate honors students in the COE

EER and UML
UML (Unified Modeling Language), based on the EER 
model is widely used for modeling large programming 
applications
OMG-backed industry standard
Has support for: user view, behavioral view, structural view, 
and implementation view
For building a GIS, an object-oriented GIS data model and 
system architecture using UML  can be implemented
Abstract classes are widely used to provide flexibility to 
changes
You can export Workspace XML from UML Model
You can import Workspace XML into an empty GDB 
(geodatabase) using ArcCatalog
UML Poster diagrams are used for Large-Scale ArcGIS 
schema design
Slide 53

Unified modelling language class diagram to urban land information system
Slide 54
https://www.researchgate.net/figure/Unified-modelling-language-class-diagram-to-urban-land-information-system_fig3_340045502

Is the WWW a DBMS?
Fairly sophisticated search available
crawler indexes pages on the web
Keyword-based search for pages
But, currently
data is mostly unstructured and untyped
search only:
−can’t modify the data
−can’t get summaries, complex combinations of data
few guarantees provided for freshness of data, 
consistency across data items, fault tolerance, …
Web sites typically have a DBMS in the background to 
provide these functions.
=

Q: How do you write 
programs over a 
subsystem when it 
promises you only “???” ?
A: Very, very carefully!!
Is a File System a DBMS?
Thought Experiment 1:
You and your project partner are editing the same file.
You both save it at the same time.
Whose changes survive?
=
•Thought Experiment 2:
–You’re updating a file.
–The power goes out.
–Which of your changes survive?
A) Yours B) Partner’s C) Both D) Neither E) ???
A) All
B) None C) All Since Last Save D) ???

Relational Model
A data model is a collection of concepts for describing 
data
Concepts (set) + operations (union, intersection, 
difference,…)
The relational model of data is the most widely 
used model today.
Is based on the mathematical concept of sets and 
set operations (provides a theoretical foundation)
A  relation  (which is a set) can be alternatively 
viewed as table with rows and columns making it 
easier for people to understand
Can be seen as a spreadsheet although was used 
much earlier
Slide 57

Why is Relational DBMS Popular?
Although the abstraction used had mathematical 
underpinnings, a relation was easy to visualize as a table
Everyone understands rows and columns and the data is 
stored in that way
Students relation
Notions of schema (intension) and extension (data)
Slide 58
sid
name
login
age
gpa
53666
Jones
jones@cs
18
3.4
53688
Smith smith@eecs
18
3.2
53650
Smith smith@math
19
3.8

Why is Relational DBMS Popular?
Easy to use query language
SQL allows users’ to access data without having to learn 
operators and semantics
A powerful associative query language
Programming and understanding data storage formats not 
required (unlike earlier DBMSs)
Powerful SQL optimizer allows users’ to write queries and 
the system optimizes it (unlike previous DBMSs)
Data and metadata are represented using the same 
model and are queried using SQL
Vert importantly, supports multiple users, recovery from 
failures, and consistency of data
Slide 59

In SQL
You express what to retrieve and NOT how to do it
List female students in the college of engineering 
whose CGPA >  3.8
List all students in the CS dept. in 2022 who got A 
from every course they took under instructor B
Generate a report listing average salary of faculty 
in each department in the COE
Of scouse, these need to be converted into SQL
But that is much easier than writing a program
Now you can even do it with a GUI
Burden of efficient retrieval is on the DBMS
Slide 60

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
61

What Is a DBMS?
A very large, integrated collection of data
MyMav, used by UTA, is an Oracle DBMS underneath 
Whatever system you use for registration and payment of 
fees etc.. are likely to be a DBMS
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
Slide 62

Why Use a DBMS?
Data independence and efficient access.
Reduced application development time.
Data integrity and security.
Uniform data administration.
Concurrent access, recovery from crashes.
Persistence, scalability, portability
Access control
Application development time is reduced!
Information processing was raised to a new level of 
abstraction!
Slide 63

RDBMSs
Need Schema
EER modeling, normalization, and generation of schema 
Schema is flat
Schema difficult to change
What is a schema
Description of a table (or relation) in terms of 
attribute names and their types
This is also known as the conceptual schema
4

RDBMSs
Table and its schema (remember table needs to be 
populated)
5
CREATE TABLE Students
(sid: CHAR(20), 
name: CHAR(20), 
login: CHAR(10),
age: INTEGER,
gpa: REAL)  
CREATE TABLE Enrolled
(sid: CHAR(20), 
cid: CHAR(20), 
grade: CHAR(2))  
sid
name
login
age
gpa
53666
Jones
jones@cs
18
3.4
53688
Smith smith@eecs
18
3.2
53650
Smith smith@math
19
3.8

RDBMSs

Support limited Data types
Text and numeric data types, data-time data types
Not geared for others (voice, image, logs, graphs, objects etc..)
Lacks general search capability (e.g., find all occurrences  in the 
database)
Blobs (Bi large objects)

SQL can be embedded in many programming languages

Other embedded-SQL languages exits for each vendor

Commercial DBMSs
Oracle
DB2 (from IMB)
SQLServer (from Microsoft)
Sybase

Public domain DBMSs
MySQL, Postgres, …
6

RDMSs 
Were optimized 
For joins (not for self-joins! And not for large number of joins)
Fast retrieval (geared towards reducing I/O)
For management of data over a long period of time
Generating reports
OLTP,  OLAP (dimensional analysis, data warehouses, marts)
High concurrency
Guaranteed Recovery (ACID properties)
Limitations
Partitioning (or distribution or scaling) is not automatic
Query processing need redesign for taking advantage of 
partitioning
Distributed databases make data unavailable due to 
distributed commit (3 phase commit)

Vertical and horizontal scaling
/2023
Chakravarthy
8
Both are difficult with RDBMSs!

Relational Model: Summary
A tabular representation of data.
Simple and intuitive, currently the most widely 
used.
Integrity constraints can be specified by the DBA, 
based on application semantics.  DBMS checks for 
violations.  
Powerful and easy-to-use query languages exist
Can scale to enterprise data
Tons of utilities available
OODBMS features were incorporated in to RDBMS 
making them less desirable

Other SQL Databases
Vertica
Stores data in column format so it can be queried for 
best performance
Unlike a RDBMS only needed columns are used for 
answering a query
Data encoding and compression are used 
Seems to support Geospatial analytics
Easily load and export shapefiles
Perform fast spatial joins using ST_intersects and 
STV_intersects 
Takes 2 geometry objects and returns true if they 
intersect

Other SQL Databases
SybaseIQ (now SAP)
s a column-based, petabyte scale, relational database 
software system used for business intelligence, data 
warehousing, and data marts
Other column-oriented databases are
Apache Hbase
MonetDB
MariaDB, etc.
Column-oriented provides good compression
It saves storage (less important)
Reduced I/O (more important)

Introduction to GIS  
A Geographic Information System is a multi-
component environment used to create, 
manage, visualize and analyze data and its spatial 
counterpart
Most data sets can be assigned a spatial location
Does your data need to be analyzed in a GIS 
environment?
It depends on how you want to understand the 
analysis
Here is a simple example
Slide 72

Introduction to GIS  
Slide 73
Country
Conflicts
Country
Conflicts
EGYPT
5246
LIBERIA
980
SUDAN
4751
SENEGAL
933
UGANDA
3134
CHAD
895
ZAIRE
3087
TOGO
848
TANZANIA
2881
GABON
824
LIBYA
2355
MAURITANIA
811
KENYA
2273
ZIMBABWE
795
SOMALIA
2122
MOZAMBIQUE
792
ETHIOPIA
1878
IVORY COAST
758
SOUTH AFRICA
1875
MALAWI
629
MOROCCO
1861
CENTRAL AFRICAN 
REPUBLIC
618
ZAMBIA
1554
CAMEROON
604
ANGOLA
1528
BURUNDI
604
ALGERIA
1421
RWANDA
487
TUNISIA
1363
SIERRA LEONE
423
BOTSWANA
1266
LESOTHO
363
CONGO
1142
NIGER
358
NIGERIA
1130
BURKINA FASO
347
GHANA
1090
MALI
299
GUINEA
1015
THE GAMBIA
241
BENIN
998
SWAZILAND
147
Table 1.1: Index of total African conflict for the 1966-78 period (Anselin and O’Loughlin 1992).
Identify top 4 countries with
Highest conflicts
This can be done by sorting on 
the conflicts column
Suppose you want to find whether
The high conflicts countries are
Geographically Clustered

Introduction to GIS  
Slide 74
For the second question,  a map of the countries would be helpful
Suppose you want to find whether
The high conflicts countries are
Geographically Clustered 
For this, the spatial elements of data should
Be readily accessible in digital form
This is difficult to accomplish with tables or
spreadsheets
A more complex data storage 
mechanism is required. This is the 
core of a GIS environment: a spatial 
database that facilitates the storage 
and retrieval of data that define the 
spatial boundaries, lines or points of 
the entities we are studying. This may 
seem trivial, but without a spatial 
database, most spatial data 
exploration and analysis would not be 
possible!

What is GIS?   From USGS
In the strictest sense, a GIS is a computer system 
capable of assembling, storing, manipulating, and 
displaying geographically referenced information, i.e. 
data identified according to their locations. 
Practitioners also regard the total GIS as including 
operating personnel and the data that go into the 
system.” USGS
A geographic information system (GIS) is a computer-
based tool for mapping and analyzing things that 
exist and events that happen on earth. GIS 
technology integrates common database operations 
such as query and statistical analysis with the unique 
visualization and geographic analysis benefits 
offered by maps.” ESRI
Slide 75

GIS Software
Many GIS software applications are available –
both commercial and open source. 
Two popular applications are ArcGIS and QGIS
ArcGIS
Developed by ESRI
The ArcGIS desktop environment encompasses a suite 
of applications which include ArcMap, ArcCatalog, 
ArcScene and ArcGlobe. ArcGIS comes in three 
different license levels (basic, standard and advanced) 
and can be purchased with additional add-on packages
ArcGIS is only available for Windows operating systems
ArcGIS Pro can run on Mac using virtualization
software
Slide 76

GIS Software
QGIS
It encompasses most of the functionality included 
in ArcGIS
If you are looking for a GIS application for your 
Mac or Linux environment, QGIS is a wonderful 
choice given its multi-platform support
Built into the current versions of QGIS are 
functions from another open source 
software: GRASS
GRASS has been around since the 1980’s and has 
many advanced GIS data manipulation functions 
however, its use is not as intuitive as that of QGIS 
or ArcGIS (hence the preferred QGIS alternative).
Slide 77

Differences from Traditional DBMS
Software
Different software packages are important for GIS. Central to this is 
the GIS application package. Such software is essential for creating, 
editing and analyzing spatial and attribute data, therefore these 
packages contain a myriad of GIS functions inherent to them. 
Extensions or add-ons are software that extends the capabilities of 
the GIS software package. 
Component GIS software is the opposite of application 
software. Component GIS seeks to build software applications that 
meet a specific purpose and thus are limited in their spatial analysis 
capabilities. 
Utilities are stand-alone programs that perform a specific function. 
For example, a file format utility that converts from on type of GIS file 
to another. There is also web GIS software that helps serve data 
through Internet browsers.

Data 
Slide 78

Geodatabase

At its most basic level, an ArcGIS geodatabase is a collection of 
geographic datasets of various types held in a common file 
system folder, or a multiuser relational database management 
system such as IBM Db2, Microsoft SQL Server, Oracle, 
PostgreSQL, or SAP HANA

Data
Data is the core of any GIS. There are two primary types of data that are 
used in GIS. 
A geodatabase is a database that is in some way referenced to locations on 
the earth. Geodatabases are grouped into two different types: 
−vector and raster. 
Vector data is spatial data represented as points, lines and polygons. 
Raster data is cell-based data such as aerial imagery and digital elevation 
models. 
Coupled with this data is usually data known as attribute data.
−This is a Relational DBMS that we have introduced and discussed!
Attribute data generally defined as additional information about each 
spatial feature housed in tabular format. 
Documentation of GIS datasets is known as metadata. 
Metadata contains such information as the coordinate system, when the 
data was created, when it was last updated, who created it and how to 
contact them and definitions for any of the code attribute data.
Slide 79

Summary
ArcGIS Desktop consists of several integrated 
applications, including ArcMap, ArcCatalog, 
ArcToolbox, ArcScene, ArcGlobe, and ArcGIS Pro
ArcCatalog is the data management application, used 
to browse datasets and files on one's computer, 
database, or other sources.
A number of software extensions can be added to 
ArcGIS Desktop that provide added functionality, 
including 3D Analyst, Spatial Analyst, Network Analyst, 
Survey Analyst, Tracking Analyst, and Geostatistical 
Analyst
From the end user perspective ArcGIS has very wide 
ranging functionality packaged up into a generic set of 
menu-driven GIS applications that implement key 
geographic workflow
Slide 80

Newer applications
May not exactly fit the RDBMS model
No schema (or loose schema or need schema flexibility)
One shot computation (instead of management)
Weak concurrent usage (freshness is not critical)
Recovery is of a different nature (fault tolerance instead of 
strict consistency)
Custom computation; may be difficult to express in SQL
Needs custom optimization rather than general-purpose 
optimization
Data sizes beyond what DBMSs could handle
Quick response time
ACID properties were not needed as in an RDBMS
Answer: NoSQL systems
Data model, Customizable ACID properties (CAP), no recovery
/2023
Chakravarthy
1

Why NoSQL?
The concept of NoSQL databases became popular with 
Internet giants like Google, Facebook, Amazon, etc.. who 
deal with huge volumes of data
The system response time becomes slow when you use 
RDBMS for massive volumes of data.
To resolve this problem, we could "scale up" our systems 
by upgrading our existing hardware.
This process is expensive
The alternative for this issue is to distribute database 
load on multiple hosts whenever the load increases. 
This method is known as "scaling out."
/2023
Chakravarthy
2

An example
Suppose I want to keep track of customer orders, 
items in each order, how each order was paid.
This is a complex objects that looks like:
/2023
Chakravarthy
3
Order ID: 1001
Customer: Mary
Line items:
item 1 qty per item total;
item 2 qty per item total;
…
Payment info:
cc: visa
cc #:
exp date:
Objects representation
Orders table
Customers table
Items table
Credit_info  table
Normalized Relational 
representation
To put together an object,
You have to do multiple
joins on the above tables!
Can avoid that of I store my data as objects!

Brief History of NoSQL Databases
1998- Carlo Strozzi use the term NoSQL for his 
lightweight, open-source relational database
2000- Graph database Neo4j is launched
2004- Google BigTable is launched
2005- CouchDB is launched
2007- The research paper on Amazon Dynamo is 
released
2008- Facebook open sources the Cassandra project
2009- The term NoSQL was reintroduced
/2023
Chakravarthy
4

NoSQL Databases
Google  came up with BigTable as an alternative to 
using RDBMS
Amazon came up with Dynamo
These did not use SQL (write your own code)
The term was conjured up as a hashtag (#nosql) 
for a meeting!
Initial group of systems
MongoDB
CouchDB
Hypertable 
Cassandra
Dynomo
Apache Hbase, Voldemort, 
/2023
Chakravarthy
5

Definition of a NoSQL Database
It is difficult to give a definition as  there is no consensus
Hence, characteristics of NoSQL databases
Non-relational (uses different data models)
Primarily open-source (as of now)
No complex features like query languages, query optimizers
Cluster friendly (shared-nothing architecture)
Schema less (or loose schema) no normalization
Elasticity (both storage and server capacity can be added on-the-fly)
Sharding (non-monolithic data representation)
BASE (Basically Available, Soft state, Eventual consistency) and CAP
(Consistency, Availability, and Partition tolerance) instead of ACID
If you think  about hierarchical and network databases, they 
will qualify as NoSQL, but lacked some of the characteristics 
mentioned above!
/2023
Chakravarthy
6

NoSQL in pictures
/2023
Chakravarthy
7

Data Models
Documents
mongoDB, CouchDB. Riak, lotus notes, 
Raven DB
Column-family
Cassandra
Apache Hbase, HyperTable
Key-value
Project Voldemort
Riak. Redis (based on Amazon Dynamo)
Graph
Neo4j, GraphDB, FlockDB, OrientDB
/2023
Chakravarthy
8

Key-Value store
10026
Value
30075
Value
50097
Value
Value can be anything you want (single number to 
complex object to an image)
String, json object, BLOB etc..
See how this will keep all information about an order 
together with order id.
You can think of key-value store as a hash map!
/2023
Chakravarthy
9

Key-Value store (2)
A hash representation is used
Caching is used to enhance performance
Operations
Get(key)
Put(key)
Multi-get(key1, key2,  …, keyn)
Delete(key)
As data size increases, additional performance 
issues come up
Keeping keys Unique  may be difficult
Examples: Oracle NoSQL, Riak and amazon Dynamo 
/2023
Chakravarthy
0

Key-Value store (3)
You can envision how partitioning and scalability is 
achieved
You can partition data and store separately
If the keys are unique, updates can be processed in 
parallel and happens only in one partition!
Scalability comes from hash-based approach and 
simplicity of management!
May be good for some applications!
/2023
Chakravarthy
1

Document store
Key-value pair where the value part is stored as a document
Inspired by Lotus notes!
Documents in Jason or XML
Jason or JavaScript Object Notation, is an open standard 
format that uses human-readable text to transmit data 
objects consisting of attribute–value pairs. It is used 
primarily to transmit data between a server and web 
application, as an alternative to XML.
/2023
Chakravarthy
2

Document store (2)
No schema or flexible schema
Query or update portions of the document structure
Implicit usage  of attributes (metadata) in the absence 
of schema is important
“price”  not “cost”
Apache CouchDB 
JSON to store data
JavaScript as its query language using Map/Reduce and 
HTTP for an API
MangoDB is also popular
Blogging platforms, 
/2023
Chakravarthy
3

Metadata and similarities
Although key-value and document store are 
considered two data models, they have some 
similarities
Both have keys,
Some metadata (e.g., customer_id: 6543 is used for 
indexing (otherwise, have to do sequential search)
Both allow complex structures to be grouped and 
stored as a single structure
Sometimes called aggregate-oriented databases
/2023
Chakravarthy
4

Column-family Databases
Inspired by Google’s Big Table
Different from RDBMS column storage such as 
Sybase IQ , vertica
Column families are defined
Columns can be defined dynamically
Storage is more like an array; first dimension is the 
row identifier or row key, second is the 
combination of the column-family and column 
identifier. The third optional dimension is the 
timestamp and versions.
/2023
Chakravarthy
5

Column-family Databases (2)
/2023
Chakravarthy
6
Name
“sharma”
Billing address
“500 UTA Blvd., 
640 ERB”
Payment
“procard”
Oder 101
value …
Order 102
Value …
Order 103
Value …
Order 104
Value …
2001
2005
Column 
Family 1
Column 
Family 2
Row key

Column-family Databases (3)
It is also an aggregate-oriented representation
Can easily distribute data
Partitioning and distributing facilitates search
However, in all of the above
Sorting and grouping is not easy
Report generation is not straight forward
Have to slice and dice data for this!
Can be done, but takes more computation and 
effort!
Examples: Apache Hbase, MariaDB, Hypertable
/2023
Chakravarthy
7

Graph Databases
Data modes uses nodes, relations, K-V on both
Representation is different from that of tables
Representation of graph as a table requires too many joins 
for traversal
FlockDB developed and used by twitter is a good example
Keeps track of who follows whom
Traversal from a start node or a set of nodes
Ability to add more nodes and edges
Graph operations are optimized for this representation
Useful for social network analysis!
/2023
Chakravarthy
8

Graph with attributes
Captures entities and their relationships
Mostly used for social networks
/2023
Chakravarthy
9

An example 
/2023
Chakravarthy
100

Graph Databases (2)
May have their own query language for specifying 
queries
Graph representation is becoming more popular as 
it is easy to see and understand relationships
“Retrieve all founders of a company who attended 
Stanford”
“Query capabilities allow users to look for nodes, 
scan neighboring nodes, retrieve edges, and 
retrieve attribute values. Users can also perform 
more complex queries.”
/2023
Chakravarthy
01

Disadvantages of NoSQL
No standardization rules
Limited query capabilities
RDBMS databases and tools are comparatively mature
It does not offer any traditional database capabilities, like 
consistency when multiple transactions are performed 
simultaneously.
When the volume of data increases it is difficult to maintain 
unique values as keys
Doesn't work as well as relational data
The learning curve is stiff for new developers
Open source options, hence not so popular for enterprises.
/2023
Chakravarthy
02

Summary
In addition to the databases discussed, there has been 
several other types of databases
Main-memory databases (for performance)
Stream Databases (for dealing with data streams)
Spatial representations and computations
Databases also support ACID properties which are important 
for some of the enterprise applications
Support for Concurrent users and recovery are equally 
important to the above applications
Indexing is used to speed up query processing
Mirroring and hot-standbys are used for mission-critical 
applications (think of what happened on 9/11)
/2023
Chakravarthy
03

Thanks!
Any questions?
104

## Fetched resources (external URLs)

### Introduction to Databases and Data Storage Pre-Survey (link)
*URL:* https://utaedu.questionpro.com/a/TakeSurvey?tt=gGAP/e%2B2rngECHrPeIW9eQ%3D%3D

[survey link — skipped]

### Introduction to Databases and Data Storage Recording (link)
*URL:* https://www.youtube.com/watch?v=DOEgAO6mrPc

[YouTube transcript DOEgAO6mrPc]
let's move quickly onto our databases and data storage so again we discuss a little bit of this on Monday kind of broader view from a 40 000 feet aerial view today we'll try to understand databases little bit closer and also see you know why you know you even in GIS you use relational databases all relational databases are supported in in the gis systems and so it's useful to understand what the relational dbms is and Powerpuff data storage is another thing where because we deal with a number of data depositories different file formats so that is also important to understand the implications of that any questions so far okay so just to recap what we said what I said on Monday so we went with a bunch of things so uh we went to a you know pile based data storage and management what does that implied wait show you a little bit more today we will focus more on the dbms not on the others uh and if time permits we will try to cover no secret highlighted in blue so as we said basic abstraction for storing anything is the value and it has not changed all types of piles are stored and all your shape files and image files and mapped files so who decides how to store things I mean so the user or the community decides how it should be stored because that is going to be extremely important if you don't store it in a format that is uniformly agreed upon then you're running a lot of problems in application development so that's why you have all these file extensions for different types of shape files for example So based on the extension you know what is the format inside that and how to interpret it and how to use it in a particular application so that's so typically in a file you store things as records fields and values for structured data applications have to be aware of the problem this is very important it doesn't matter which application it is they need to know what the format is before they can process and make sense of that so here is a a very simple way to understand what a record format looks like so you can think everything you store as records so your file may have a million record or 10 million records and each record may be four Fields five feeds are 10 fields if you think of just an employee information then maybe five or six speeds and they have to be stored on the disk in a file which is stored on the disk and then this is what you get when you read it you get this information to the memory and then you have to use that information so information about the field types is the same for all the records in a file and this is typically stored in system catalog so you can think of piston catalogs as one kind of metadata that is used inside a dbms to interpret or understand what a file format is how it looks or another table is whatever the contains of the table itself data metadata is used everywhere but maybe in slightly different ways so when you come to file based applications as we said the application has to read the record record at the time or a block at the time and then interpret the fields and then take action so understanding the representation is key to the application so application is very tightly integrated with the representation form it doesn't matter dot CSV file makes it easier to separate them using a split in Python on a comma with the comma separated file or a white space if it is a cap separated file so you can do that easily but you still have to know the representation of the product makes it difficult to change the format so this dependency this tight control between what type coupling between the file representation application makes it very difficult to change the file format when it's designed provisional enhancement is difficult that is why a lot of different types of files you have the format has to be what we get to if the format is changed extended you have to change all applications so this is the biggest software engineering or software development problem if there are 10 applications using that file if you change the file format all 10 applications that will go and revise their code to understand the new format and other requirements so very rarely you want to do that application management is a difficult labor intensive and throughout the errors strong coupling or dependency makes this difficult so difficult to manage duplication and maintain control if data is spread over many files and the same information as we saw in in the example that I showed you is present in manager to make sure it is represented correctly without inconsistency and uh and manage properly which is very difficult so the question is what is the answer so here is an example that I want to give you because you know I I was part of this process so we were doing payroll processing for example in the 70s using file based data we had to use multiple files because you know personal information is in one file wages and other information models work and information using a different file so all these files have to be processed together in order to generate pay steps and not only that we had to create a new file updated file at the end of the process to do it so the next step on top of that they were also using Cape drives which I briefly mentioned at that time as the capacity of the discs were very small so we had to update these files as well Android what we call the new Master if our computation was successful this process would take at least a day and maintaining the files for the next one was critical if there was a a any kind of error and we have to abort it then we had to go to the backup file and then restart the whole process scale the process completed so this is a very difficult process so this is one of the reasons why we have all the things we have dbmss standards metadata and other things to avoid or mitigate this as much as we can there are additional critical issues that are also not properly handled by the file based storage uh they are as I said managing duplicate information and when you have duplicate information consistency is a big issue so if you have student information you know duplicated in multiple places if you won't change addressing on file you have to make sure the address is also changed in the other file otherwise you have two addresses for the same person or two whole numbers for the same person which causes problems concurrent usage this is a very important thing if hundreds of users thousands of users are going to use a particular system file based applications are not geared up to the Android one you cannot have you cannot have the same file opening from multiple users and be reading at different places and doing different things that's a big difficulty with private system it just means how to combine data is another issue recovery is another issue in the present paper so it is possible that in a power failure happens or you know some other kind of programming failure happens you might have been contradict you know Windows when there is a failure you lose all the information that you are doing editing in other things and you have to go back and start with your laptop this is an acceptable for the mission critical applications and also you cannot query you can only run applications of 3D data across files so needs a new application for each query and managing large amounts of data is different so there were a bunch of issues that were not properly handled by by representation so what is a data repository you can think of a file as part affected and Repository or a data repositories storage page for researchers to deposit data sets associated with you so it can be one file or a bunch of files from how some some relationship between them so that they can be used together and multiple data sets so we have already seen only a database as a mechanism but aggregating data from multiple sources and creating a single view of the database we also have about data Lakes data marks git and GitHub can also be seen as a positive ways for data so you most of you are familiar with GitHub this is mainly used not only for data but also for home mainly used for code data can also be the description and documentation can all be done so many times they don't have the individual or organization level can also be done product is organized and versions can be maintained and various all kinds of checks and balances that can be implemented to make sure what is stored in the gate is is correct so I just put this because even if I don't know about these data such as you based on very familiar with me so so these are all the positives uh for your domain or the area of the number of them very large natural data U.S until you have to explore and so on and so forth so you may be I'll be using and accessing some of these depositories and you might also looked at some of the metadata associated with this repositories will come through some of those issues later so so how do we overcome the problems that we mentioned earlier so all problems associated with Spider-Man can be overcome with the interruption of the database management system that's the death of the whole purpose in which it came about by decoupling the data representation is the key if the application software does not have to know the data representation then there is no dependency you can change your data or you can change your application software without having to worry about that but in order to do that so this is a very commonly used practitioner in computer science so we call it benefit one level of indirection which means that there is a price to pay but life is made very difficult very easy so this requires data model to represent the application at a higher level of abstraction so this is the key is to have an abstraction that can be mapped to a representation and it can be done by the software so that's easy to understand and perform computation the data number so data model has to be simple and easy if it is very complicated then it poses its own problems you may end up having different levels of abstractions for different purposes so the bottom line is this required software that can hide the physical representation of the data model or the obstruction so one way to understand it easily is think of a compiler you write your program in Python but computers don't understand python so it has to be converted into a machine language and assembly code in between and that is done by a SIM card so this compiler is what we call the middleware that takes you from a higher level of abstraction of expressing things in in Houston statements and objects and functions to machine executable code so that is run abstraction that you use you know you can think of each right as a different kind of abstraction meant for different purpose think of a web GUI that allows you to access by filling boxes since you are writing a query that's another kind of abstraction where you interact with drop down menus and boxes rather than writing Equity but somebody translates that some software translates that into a executable query behind the scenes so this is very different from you know how we were using computers before using command prompt style and writing commands the dbms can be understood in two different ways from an end user's perspective and a system simple so here we are only interested in new understanding dbms as an end user which means that you may want to understand why debians are needed for which kind of applications it is used how do you go from an application requirement to even this design uh what models are used we will focus on the relational model how do you query you don't have to write an application but you express is still of Express queries in a standard language or the SQL and that's easier how to use the dbms whether it is okay traditional dbm is like article or a jsdbms that we normally use we won't worry about systems perspective which is more about how do you implement a dbms and what are the issues the need for date amount so additional requirements we listed earlier were derived from Enterprise application so this is how the need for dbmss and and the banking applications Airline reservation employee data management so what why were these applications important because they had very stringent requirements so if you take banking for example renewal deposit an amount into your account you want to make sure it it happens and if you get a receipt that amount is added to that one you don't want the bank coming back and saying hey my software failed in between so your account does not have the proper balance that is not acceptable same thing is true for England reservations it cannot come back and say sorry because of some failure we could not do that so these were very important critical requirements like my Mavis another example so these were not guaranteed by systems or any system when even today operating systems do not guarantee this when an operating system fails you lose all their work that you have done up to the point unless you save it yourself but this saving manually saving is the problem that cannot be uh used by these applications it has to be automated it has to be it has to work perfectly so this is the main thing so there are a lot of mission critical applications uh give you Misses are used are nuclear power plant control and various other things and they have very Skilling requirements for this so earlier files were created manually without any principal process and only based on the knowledge of the application by the developer how many files the contents formats so this was a very ad hoc process to say the least so think of ad hoc design that could not be carried over to Mission people systems or Enterprise applications so that is the full motivation for a new approach was needed for taking care of the complex requirements and you see that not only interesting system in GIS systems as well first Applications had to be moderate in a systematic way to make sure data is captured and completely captured completely along with interrelationships among data functionality on the data should also be captured what you want to do with the data when you capture the data data models was born so we have hierarchical data model which led to the development of the optical dvms Network model and finally relations to the development of relational dbmss today this is the most widely used pbms we will see why so widely used today 5 years supports all commercial relational bbms and there are other assets here so just briefly uh you need to understand what kind of things are used for modeling the need and the goal was to model real world applications so even if you take Eis you are going from a real world application need for putting some information on the map that that is the real world application you may have map information separately you may have the data that you want to put on it separately but the application is to integrate them and view them in some way and that has to be modeled in some way so what we call Extended entity relationship module was developed in 1970 to capture entities this was a very simple yet postal model a popular model is still being used today for the design of relationships and others many tools are available for this Real World objects are expressed as entities and their relationships are captured using the model this model is converted automatically algormanically interrelations hierarchy sometimes so that is the advantage so if you can Express still doing the ER model is done by humans but converting them into relation system using another so here is just an example of a ER diagram for a company founder so if you are so here is a person as an entity and there are different relationship a sibling of a person is a person the person is married to another person a person studies at the University is located in a city a company is located in a city and a person among the company so this is the model which is easy to understand and interpret and using this from this model you can generate hierarchical Network or relational or schema as we call it in order to implement that now we have been using this we'll see uml is used in your JS applications on other programs so what is not captured in in the database or the model is the actions there is no way to capture actions in a database or in a file because actions are typically done through applications through interactions so here is a good example we all log into various systems it is done through implication but a number of data elements are required with additional constraints for doing that such as username password captcha so we also in a password need to be changed so what is captured in the previous module I showed you is the pieces of data not the action the action has to be implemented as an application so the same thing is true in all your databases you essentially capture the data so whether it's a line on the polygon or the other way it is it's a piece of data manifestation of that India visually understandable thing is done by the software or the application that renders it here is another example I'll skip that so in addition to modeling data you also want to reading this database for various things so this is these are the things like you want to know which book is Borrowed by two in a library database you want to generate report of customers who have not paid the last credit card bill or class two credit card bills you may want to track a UPS shipment to know the current status 10 most popular movies generate on the students in the College of Engineering so this is what we want to do and make sure the data you have captured yes can provide these answers to these queries otherwise your data capturing symptoms the second model that is widely used today is what is known as the human unified modeling language based on ER this is a object Management Group industry standard it has support for a lot of things because it's it's used in such large software system development uh for building a JS and object oriented GS data modeling system architecture using Uno can be used notion of abstract classes are there it's also there in in Java and python for example I you can export workspace XML from uable model you can import into a GDB you can use uml poster patterns for generating box clip so uml is widely used today here is an example of a uml language class diagram to Urban line information system that I found I may not be able to understand it completely but you guys will be able to understand it backup so this is how instead of the ER model this is the uml module that is used which goes little bit further in representing interactions and behavior and use cases and other things that can be implemented into a system so uh is worldwide web a dbms so sometimes this is the question you have fairly sophisticated search there is a crawler that indexes the pages you can look here at this but currently you cannot uh the data is mostly unstructured and typed you can only search you cannot modify data you can't get somebody's complex nominations of data so actually what it is is you have a dbms behind a web in some cases in some cases it may be something different Google example uses other systems in addition to dbm says few guarantees are provided for freshness of data consistency soil tolerance and so on a lot of critical requirements of a dbms or missing from the verified web which may be presented well is a file system a dbms I'll I'll skip this you can see that in the intersection plan so let's go to the relational Market what is the relational module that is widely used today uh this is a data model and data model is nothing but a set of Concepts and operations on those Concepts luckily in the relational model there's only one concept the notion of a set that's one of the reasons why it's easy to understand and a bunch of operations will be clearly understand it also has a good mathematical formation from set 3D so this is the widely used multiple way based upon the mathematical concept can be altered so the important thing is this can be a relation of a set can be viewed as a table it goes in columns making it easier for a common man to understand without having to understand the mathematics behind it can be seen as a spreadsheet all the specific came oscillator so here is an example of a relation so you can think of it as a table with those in columns so here is a student ID name plugin age and GPA so this is also known as this schema that the first header is known as the schema that describes the attributes are these are the fields when when this information is stored in a file these are the fields and this is a record the actual values them stands data is known as the extension which has to be populated based on the skin why is relationally being found because there is an easy to use Query language called SQL structure query language you can access data without having to learn operators and semantics without having to write a query in the traditional sensor a program in operational sense this is a very powerful associative query language programming understand data storage formats not required it has a very powerful optimizer that lets you write a not a good query but the system optimizes it behind the scenes data and metadata are represented using the same model relational model and can be queried that's one advantage very importantly supports multiple users recovery from failures and consistency these are the very important requirement in SQL you can write queries for expressing things like list three main students in the College of Engineering pools cumulative GPA Institute now this can be relatively easily translated into a school pretty without having to write a program list all students in the sales department in 2022 who got a from every course they took under instructory this may look like a complex query but a complex thing to see but you can do that and the good thing is the algorithm for retrieving the what you want generate a report listing average salary faculty in each department in the College of Engineering so if you have to do this some of this may involve multiple bytes or multiple relations your application has to figure out how to combiner so dbms does all of them for you behind the scenes of course they sleep they cannot link to SQL but that's much easier burden of efficient retrieval Ease on the dbms on the end user so as I said there may be multiple levels of obstruction at least in the dbms world we have two levels physical schema and conceptual schema the set view comes at the conceptual schema level physical schema is how the information is represented and both are shielded from the user view so the user does not have to know the user only has to understand the conceptual View and the risk is transparent to the usual making it much easier to deal with different types of data different kinds of data so you can also think of data exchange formats that we will discuss as schema so schema is just a a way to express the intent what we want to represent not the content so intent versus content so we have seen this already a dbms is an integrated collection data that's the key and it should model a real world Enterprise so we use entities and relationships a dbms is nothing but a piece of software you can think of it as the middleware that is sitting between you and the actual data that is stored on the disk and it is managing everything that you asked to the dbms and vacation gives you that information this is also proof of GS in GEOS you're doing higher level applications and you're not worried about how many files are used underneath whether in order to do this you have to access a relational database plus some other kinds of files that show spatial information whether it's a vector kind of information so these are the advantages for using a dbms data Independence very important efficiency data integrity uniform data Administration very importantly content access recovery from purchase any kind of product it can be a portfolio it can be an operating system failure it can be a program where it can be a disk crash it provides persistence scalability and portability is also impacting because you want this data to be available for a long period of time so you do processing only in memory so you bring the relevant data for processing in memory but at the end of the day the data is stored after all the changes and manipulations in the list which is available for the next session you can also provide a bunch of access control and privacy and other issues so that is one of the major reasons for doing this so a relational dbms needs a schema a schema is the description of the table and as I said this is all the conceptual security but here is an example of a table and sort of the schema for this table so when you first Express you express the schema which says here is a table whose name is student Sid has character type of midi characters name age is an integer GPA is the real number this gives you the schema you can also think of it as a metadata but the actual values have to be populated into the dbms at different points in time multiple so you know this database is changing every semester new students are coming in some students are graduating so there's a constant change to the database and it keeps the current instances to build the computation that you need to do so the kind of data types that are supported may be limited like for example it doesn't support spatial data types but you can represent it in in some other format either as a file or as a relation and then write an application for that text and numeric data types date date time formats not geared for storing uh large files typically the way this is done is to put a handle to these images or other files and store the path or the handle so that you can access it because a lot of these things are vaguely updated but they are accessed or retrieved blocks that's General such capability meaning if you do not have Google like search objects SQL can be embedded in many programming languages there are a number of commercial dbmss which you might be familiar with article is as the largest market share sorry db2 is on IBM SQL Server is from Microsoft cybase has a smaller market share that's still there some of that from the Enterprise by sap there are some publicly available deepliness of like MySQL postgres csued from the literature I see GIS you have some support postgres database more than MySQL so RDM infances were optimized uh and use for management of data over a long period of time this is important generating reports different kinds of analysis High concurrency meaning number of users can be very large and it can support them guaranteed recovery we call it acid property but this is a very important requirement for a lot of machine physical applications there are some limitations partitioning for example is not automatic publishing of data media processing we need design for taking advantage of publishing there were distributed databases that make data available so there's a lot of work beyond the simple rdbms that went on so this is what we call what from horizontal scaling vertical scaling is for increasing the amount of CPUs that you use to provide more juice personal scaling is adding more data typically adding more disks both of them are a little bit difficult for RDA means to stay because that's why you don't see all the immune system hundreds of processors unlike Map Reviews and other distributed functioning and processing states where you can scale to hundreds and thousands of processes so to summarize the relational nozzle it's a capital representation of data I think the reason why it is popular and widely used it is very simple and intricate you can support Integrity constraints this is another thing that is important because you know once you put in inconsistent or incorrect information into database it saves forever and it's very difficult to check that because all your subsequent complications and other things are based upon that information so it's very important so data entry you know we call it data entry is a he's a tough job and dbms has some built-in tools to check and make sure the data is consistent and follow second organizational or other individ constraints you cannot do everything in an automatic manner but this is an important area powerful and easy to use spring language can scale tons of utilities are available on that a lot of object-oriented features have been incorporated into relational bbms so there was a big push for odbms that didn't happen still there are a few commercial systems the problem other tpmss SQL base or comic boards for various purposes and one of them one of them is the notion of column format is one example the skills data in column format unlike in relational database which stores data in a row form each product is the role of the table and records are stored whereas here each column is stirred separately and that has certain advantages about processing and certain kinds of computations uh data encoding and compression can be done better with column representation or what I have seen is that this representation can support some geospatial analytics I'm not sure how widely it is used by the main experts I'm not sure we believe load and Export shape files you can perform spatial joints as they call it to see whether two objects intersect and on with the answer another similar one is the cybase IQ now this product sap this is also a column based better life scale relational dbms the other column oriented dbms Source we see Apache touch base in nanodb so that the reason to go for culinary intake even though it provides would be completion is not just to save storage saving storage is important but more important is when the amount of storage is less the amount of IO input output that you have to do is also less that is the higher cost that is the kind of the Achilles in for dbmss staging data from disk to main memory and back and that is still not as advanced as the CPL the most log does not apply to describe a bandwidth for example and that is a serious temptation so I have put together a few slides I'm not sure whether it captures everything that you need to know you may know more than this but this is sort of looking from a computer science person who is interested in the database aspects of ID system so it's a geographic information system is a multi-competent environment used to create management data and if spatial type so certainly it has a lot more data in addition to tabular data so all the spatial data is not stored in the relational format because it's very inefficient to do processing unless you use special ways of doing it most professors can be assigned a special occasion so the question is does your data necessarily need to be analyzed in a clearance environment and I'd say it depends upon how we want to understand so if you use an example I thought which seems to at least for me indicates suppose say you have this data contrary some number of contracts and so this is a piece of data that is not special in any way and you want to identify top four countries with highest number so that's very easy to do you can sort on the and get that information so that's that's easy to do you don't need anything more but suppose say you want to find whether the high complex countries but geographically cluster so this is a different query or different things that you want to understand and that cannot be done by a low small billions so if you want to do that then you have to have the map of the countries on the way to understand the country name to the map associated with the country naming whatever way you want to do it and here is one way to do that so here is a way place where the uh the go on dark shadings uh indicate the level of conflict and the map feature clearly shows the juxtaposition of countries with different conflict values and from this you can immediately answer whether these countries are geography class so to be this is the difference between what a relational dbms can do versus block a gsdbms is capable of being with additional information stored in a way that can be combined with the relational information so that that's what happens here a lot of data that are still in the numeric or the relational form but you also have special data in different ways now you have to integrate them or put them together in a meaningful way to make some sense of it so this is to me is the power of GIS this is a very simple example but you can take it to different levels so a more complex data storage mechanism is required this is the core of the gsmen spatial database that facilitate the storage and retrieval of data that Define the spatial boundaries lines of points identities this may seem trivial but without a spatial database no special data exploration and memory problem to read this is the sort of the print essential feature of a GIS to going from a so you can sort of see the previous one as histograms or tab visualization but those visualizations are different from spatial visualization so what is JS there are two definitions that I took from usjs sign from SC which is one of the leading vendor of JS in the scripture sensor GL secondary system capable of assembling storing manipulating means playing geometrically referenced information data identified according to their locations at Christians also record the DSs including operating testing is a computer-based tool for mapping and enhancing things that exist and events that happen on Earth vs technology integrates common database operations such as midi and specific analysis with the limit usually so this is the kind of the summary of what a GIS is so GS software many JS software applications are available as far as I can see some commercials some open source are two popular one seems to be RPS which is commercial and previous easy development so history has been around for a long time so it provides a lot of different uh components architecture and other things it's only available for Windows and it can be used on Mac using virtualization tools I think lately it might be available in Linux as well I'm sure 2DS is a open source software and I'm not sure I I believe uh RPS is widely used in education and we are using it for this program for sure but uh if someone wants to play with it there may be a live version of copy or sex available plus this may be available so to me what is the difference of GIS from a traditional degree English two things one is the software applications that support on top of that plus the data itself so different software packages are important for years Center to this is the JS application package search for instance for creating editing amazing spatial internet so traditional DBA measures only supported for kind of a a traditional data types like numeric data which are not meant to be visualized spatially therefore these packages contain a million of GPS functions in here extensions or add-ons or software that extends the capabilities so extensibility is an important thing irrespective of how many tools are there someone wants to extend it in some way for a particular need on a particular purpose and that should be possible component we assorted is the opposite of application software because kind of this software are developed and available to me these are similar to The Python packages that you use so the larger the availability of these packages the back of the piece right then you can use it you don't have to understand how to use it not how to write these packages so you don't want to understand so kindness is implemented but you need to understand how it can be used for environmental access you release a standalone program that perform a specific function for example a file format typically that converts from one type of PS1 to another so again this can be easily made available there are also utilities for traditional dbms for example to speak a relation into a CSV file or a type file or some other kind of file there are also FDA software that helps database is the terminology that I see constantly with respect to GIS systems and geodatabase seems to be a collection of files Plus relational database systems as a single thing called the geodivers so it has collection of geographic data sets Plus ability to access and store relational data in any one of the databases available like IBM lib2 Microsoft server also prosperous it's a public level data seems to be at the Port of JS I'm in addition to the relational format with our Vector data and rascular data corporate with what is known as the attribute or metadata so these things we are not familiar then I can explain that so metadata will come to that contains such information as the coordinate system when the data was created when it was last updated to created it and how to contact them and definitions for any code to summarize I'm going to summarize this and stop it as I said and we won't get to know SQL but that is not very critical because there you data new the usage is not as much so I create the stock consists of several integrated applications you might be familiar with most of them our Catholic is the management application means to dwells so for data sets and data files of this last quantity you have to have a a good way to locate them or search them or browse them a number of software extensions can be added including 3D Administration data means of simple things from the end user perspective RPS that's very very functionality package of the genetic setup menu during applications so uh the next thing was the uh so since we are reaching 10 30 I'm going to stop here and just showing that balance someone had a question in the chat too asking about the unified modeling language [Music] actions in a database so uml is certainly capable of look at me I mean it's meant more for modeling and implementation in a programming language not just data so it captures behavior and interactions and use cases so that they can be implemented in the same way in in the programming language earlier you know it was very widely used from java implementations but it is application independent and language independent it can be used for me yes you can do that so to summarize in addition to the database of discus there are several other types just for completeness main memory database or stream databases spatial representation there has been a lot of work going on databases also support topical Asic properties of indexing that we did not get into is very important perhaps it's used a lot in the case mirroring and hot swing bytes are used for Mission critical applications and that's very very important and very critical for some of the application so with that I'm going to stop here um

### Multi-Source Data Analysis Recording (link)
*URL:* https://www.youtube.com/watch?v=j6ZecMIBSn0

[YouTube transcript j6ZecMIBSn0]
uh good morning folks uh yesterday I'm assuming you had a good day you learned a lot about Python and how to use it so JS applications today we are going to cover the introduction to databases and data storage in the morning and after the morning break we will do the interoperability in terms I thought that before we do the databases I wanted to cover a couple of things on multi-source data analysis as you are now they're familiar with python and can appreciate it so this is one of the things we developed as part of our our lab and it's interesting because we are using multiple data sources and all the issues of how to mark them how to clean them comes up so I'll start with that and then proceed so so uh as usual I'm not assuming anything about databases and your understanding so we'll do this and also I'll try to give you some idea of why we preserve python why why does it have an advantage compared with others so this is the presentation outline and there's a lot of material to be covered I will even if I don't get to cover the last one no sequel It's not so critical but I will be interested in making sure we cover the rest of the stuff so so as you know that any data analysis may involve more than one source the examples that I showed you on Monday just involved a single data set and then doing some analysis on that data set but this one is different and easier to understand so this came about during covid when you are looking at various data types for understanding Kobe we felt that you know that could be done a little bit differently than how they were doing so we set out to say how we can do that plus we also felt that some of the work we were doing could be used for that so we wanted to do a statistical visualization of our data this week he also wanted to do with temporal aggregation its analysis and visualization for example regions with maximum noise between in Daily cases pre and post-vaccination but some some of this was difficult to find event-based aggregate analysis essentially you know there was a lot of news and talk about you know for every long weekend you know people congregate and it is a spike in the in the public cases one can can you visually understand and see that so and finally parameter-based aggregation neutralization so we developed movies at the dashboard plus that first and then extended it to Publix plus plus 22 mobility and other things for example you know there were interesting news that came places where there were a lot of employers you know things were happening because people are moving around people are driving without seeing other areas less populous areas that was not happening so how can you analyze and visualize that so event for analysis was typically we decided that we will take two periods of time what we call the base period and a Target period and then we compare what was the difference between the covet cases in different ways in these two clips so one was maybe before an image one was after moment and the way we did was with respect to counties so U.S has 3 000 plus counties and there is information demographic information available about these countries and also the information on political supported on the on the county basis so so these are geographical regions that can be shown on the map very nicely and there was a characterization by CDC and some entity that you know whether there was no increase flat or increase or uptake for Spike versus decrease downtake on big dip so this is how and we wanted to show it in this kind of visualization which you guys can relate to better than I do so that you can see where the spikes are where it is flat and very smart but we wanted to do it on a on a period uh completing these periods and doing some additional analysis underneath so this is the dashboard that we developed that I will come back to this later we also Incorporated such and things like you know how we extracted real-time data actually this data came almost in real time uh World Health Organization was updating it every six hours or so so we collected that data every six hours and showed certain ticker this was actually actual real-time data from Twitter feeds for the period that one gave and showing the top five or ten on the football look at it and these are the two visualization that means they interactive map-based visualization the other one is a timeline series for various features from different parts of the world so a bunch of data sources were used you can see that there are a number of vapor sources from which we had to collect data aggregate them use the right data that are of important first and then do the analysis and then take the script so data collection click fast so this is one of the important steps this is not a JS example you you've seen that yesterday you'll see more of that this is more of a a traditional data usage so data is not in one place multiple participants entities creatures and relationships so here are the various data sources that come this diagram is also newspaper we will refer to this data interoperability for example that someone has to take these data even if they're in different formats figure out how to reduce it to a common format and then use it for whatever factors you are going to do so this is a very common way to look at interoperability down the road today votes for applications and for data themselves so if the data comes from a single source life is much easier to deal with one data format you pick whatever information you need from that and do some cleaning pre-processing and there is no need for nurture but if the data comes from multiple sources different information about the same entity provided by multiple data sources they can be in different formats here to selection online so this is another thing we will discuss later if they are why the the importance of Standards why the use of metadata formats for making sure that some of the entities same entities are generated in the same manner that is going to be critical form for wider usage so we here is just where the data came from our CDC uh owuid uh different increases of information but there is some commonality among them daily trips by distance data using the Department of Transportation daily Mobility reports using Google and other sources you know census daily page spending categories so these were all the data sources and remember these sources were being updated every day or at a at some frequency that you have to integrate into our system so data preprocessing challenges are the data file pump so whether it's a comma Supply case File we'll see that again tab separated and what kind of data is there whether it is numeric text or it's a location information latitude longitude that that is used for map display for example and then different types of date forms so it could be ending ddy by what temperature units measurement units Main and different codes used for Commodities and other things missing attributes attributes so this this was also there you'll see in one of the timeline cities where we have some missing information as well so for multiple input files based on which common so the question was which common attributes to combine this also is an issue when you use a database management system if the data comes from different sources we'll see that again when we discuss a little bit of standards and metadata which follows the shortlist what are the interesting features that you want to choose from so here is a example of the much of multiple data files luckily all of them were in the CSV format but they contain different pieces of information but luckily some things were common like State and date were the same in all the files so that made it much easier for us to join so to say these files or data sets on some attributes to to derived all the information that we needed for a text we update so this is a pre-processing step that is done or sometimes this is done using tools that are already available but in many cases you may have to do it yourself so this is the complete list I won't go through that so so some of them reported per day basis some of them reported but some other frequency so you have to deal with all of them and figure out a way to incrementally add so that's an important thing so it's it is that you are getting data for a particular 24 hour period and that has to be added to the existing data for it to be current or fresh so here's a snapshot of some of the input data files I I won't go into that so it's just a question of you know every day you may be getting different sizes 2800 rows twenty thousand rows that you need to merge and aggregate 39 000 rows Etc so this is this has to be done properly and correctly in order for your analysis and regulating into that so we also use in some of these things something called the configuration file you can think of that as a kind of a metal information that is used by the applications so that you don't have a hardcore things in the in the application so this is an important issue that we try to teach our students is to not hardwire a lot of things into your code because if something needs to be changed then you have to go and change all the application code and that may be used in multiple times so that's a very big software engineering issue that needs to be addressed so avoid cardboarding as much as possible whether it is a path uh direct or bypass whether the constants or input parameters collect them into a parameter file that can be read so if you want to change something you just go and change the parameter file or the config file and then the code runs as is without going to change so that's an important thing to remember even in your domain you will certainly encounter these issues so here is just a sample configuration file I won't go into the actual topics human readable you can think of as I said as a metadata information file contains information that is read and understood and what is important here is to kind of name them properly so that it's easy for someone to understand how to change it not just put values one after and then without any explanation so that's going to be important so this is a sample much file for one year February 15 19 Edition this is a shop file and this is the file that is eventually used so the other issue that comes is static Pursuit and new data so I'll mention this so if the data doesn't change then you have less number of issues to be worked for analysis and visualization if the data is changing then you have to worry about asynchronous updates or resource can potentially have different frequency of duct page so typically this is handled by using what we call are in Windows you can you can write the rules or application that we can schedule at particular times of the day for doing this is typically used for backup parametraced on the main parts to external apis this is also important if you want to extract real-time information from a data source then you have to provide the correct information to get that property income so this three years so here is the architecture this is another thing that's very important so a lot of data is coming from the internet for everything we do click processing um layer here means something else then what you guys you're seeing the gis domain this is the layers of multi-layer network class based data processing company and various analysis that you can perform on that and then you store the analyzed information and there is a separate visualization module that generates the visualization and the specific client module which is web-based that display the information the architecture is also important because you don't want to do all these things in one place if I want to add another analysis it should be possible to just extend this module without having to affect anything else similarly for visualization and this one may have to be strictly modified to accommodate them so and then there are a bunch of optimization and other issues that we incorporate uh which I'm not going to show kind of uh the flow is user use some imports then you check whether that information is readily available if so you display it if not you go through the processing and display it and we take something so this is the demo I'll see whether I can show you um how it works in a simple manner so this is the dashboard that comes this is the uh pretty good information I was talking about that came in and right now since the data has stopped we are we are not doing that so one is a interactive map visualization as it's one so if if you go here for example it will take you to a thing where you can select an interval per base period and the same interval is used for the Target paid so you can pick so you can pick any any interval from one day to uh 30 days that we have let me just pick seven days so the base period is something that should be picked up so right now the Kobe data has has stopped around October 2022 I think so um so I'm going to use a previous uh so this is Labor Day I'm going to show something between uh what the period before Labor Day and after lady or just put in one it automatically fills this in and then I have to go back and do the same September I do September 8th and you can pick what you want to see whether you want to see only the highest increase or the lowest increase or all of them so we just put and submit it so it will it will go through the analysis uh retrieving the data merging data has already been done to some extent it will do the analysis and display the map based information so what this means is that when you compare these two periods uh uh September 2022 and October 2022. this was the increase in Kobe according to this scale so uh Spike means greater than 100 uptick means 50 to 100 percent increase in zero to hundred percent flat zero percent control now you can also go to each one of the counties and it will tell you which account it is and what is the change uh population density uh median household income percentage of high schools they're just gonna this kind of indicates the demographics of the county and there may be some relationship between the demographics and what is happening in the company and other things so so this is one of the visualizations and then you can change it if you want if you're welcome to go to this uh URL and play with it and give us big benefits so that's that's one of the uh things we did the second one quickly is an animated timeline where what you can do is to select a number of regions so for example uh let me choose that maybe I think was Canada and limited States select up to five entries from what I understand so it will show you what countries you have chosen they can also choose the features as we call it whether you want to look at total number of covet cases new cases that were reported per day basis documents new debts coverage reproduction so there are a bunch of things so I'll just pick new cases and can you can compare two features or we can look at two features and units and then you can submit and what you're seeing here is a timeline analysis for all the data probably data we have from October 2020 to May 2022 that's the data we have and now you can see in some way you can compare these two you can see that in the beginning new cases in Canada were far less than the United States but as the uh find progresses you can see the changes in them both in new debts and other things I think there were issues that there were things that things were not initially handled about whatever it is so you can get a visualization and some of these dips that you see are the missing information or information not reported for that particular date and this is the information so this is just a example to show what it takes to go from well from data sources looking at choosing data sources analyzing and all the way to the implementation of data analysis so we also did a video you can you can go to the YouTube and look at the video for demonstration purposes so the second thing I'm going to address is uh quickly why we use Python but did you now you're familiar pythonia played with pythonia view some packages this is interesting to understand so kind of the choices that you are looking at in addition to apart from other languages uh that is python there is r on R Studio they spindles actually python plus vandas and others so python is what they call a programming language with batteries into it kind of this is important because from if you're not a computer science person your goal is to focus on the domain what you want in the domain not worry about the programming language understand the programming language to the extent that you become an expert in it or is another system that was developed for statistical analysis to go beyond SPSS SPSS were the main package that was available Matlab production purpose or is also a programming package our schedule is just an IDE part R which also supports python so both so why python versus r both are and python support data frames with some syntax differences so data frames essentially are very useful to load CSP files into a tabular format and then process them so essentially data frames are two dimensional size mutable meaning the size can change uh potentially heterogeneous template data so it can store petrogenous pieces of information there functions can be applied on this one in R and python are uses bytes which is a Linux feature R uses cluster package and python uses a different package I think the main difference is R has more data analysis capability that is built into that python is based upon available packages but there are tons of packages that are available in Python that can be readily used the other thing that many times is very important and useful for update on high since is to obtain information from the web we call it scraping the web which is not an easy task crawling the web is different from scraping the web uh so this is how to get the information that you see and that may change so our uses a different package python uses a different package this is the most commonly used web scraping package so beautiful so I don't know why the name is so to summarize R is more functional python is considered No Object oriented R has no data analysis functionality built in Python relies on packages python has main packages for data analysis testers RF has a large request system certainly if you're a statistician their performance seems to be R because they have more control over what they do but if you're not in expecting the area python is the difference so RS most respables about the internal it's usually investigate what you have to do non-statistical expression our studio support so when it comes to pandas fantasy is a fast powerful flexible and easy to use open source data analysis and non-pilation proof yesterday this is another package mainly meant for numerical analysis probability lens vector and method of operations very efficiently by pandas provides data prints so pandas is considered slowier than this package so if you have a choice of using the same functions from both foreign there is also SQL we will see as part of this module all of the above running main memory and does not deal with Distributing test theories for databases which deals with distance in data defense scalability is an issue in all of this so we you know fasting on Monday I showed you we gave a a small data 32 000 rows mainly because if I gave them three million rows their laptops on most of the missions cannot accommodate all of them in main memory and processor so this is a an issue that we have to constantly address so Finance was created for purpose of giving you an object similar to the r data frame inside project so if you prefer to work in playtime but like the our data frame then under sees what we will use so the bottom line is people are known people back and forth between these two depending upon what they need to do so you already have started using it so python is built by programmers and Delta so it's a general purpose programming language unlike SQL it's a standard programming language and R python seems to be better in performance than r python can be used for coding as well as system management or scripting as we call it so there's also another thing called Panda so don't get confused with that so this is the main advantage of the use of python it comes with a bunch of packages for the previous demo I showed you we have used flask and gender uh you can use you know other interfaces play Touches for machine learning pandas matplotlab or data science so a number of things comes with python that makes your life much easier than using a language like Java to summarize python is easier to learn and allows you to work on data analysis without creating a lack of code this is the key the amount of code you have to write is mainly the connecting Port between the use of packages or is still used if you need every statistical analysis other languages such as Java even though you can do it they support and the availability of packages for visualization for example is very limited so python is a good choice but we're doing a lot of things that are already available in Python series okay
