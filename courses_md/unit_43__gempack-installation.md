---
title: "GEMPACK installation and user manual"
unit_id: 43
course_id: 2
level: "Foundation"
slug: gempack-installation
is_course: 0
---

# GEMPACK installation and user manual

## Fetched resources (external URLs)

### GEMPACK Documentaiton (link)
*URL:* https://www.copsmodels.com/gpmanual.htm

# GEMPACK User Manual

GEMPACK User Manual
Brief Contents
Detailed Contents
Index
GEMPACK manual
Mark Horridge, Michael Jerie,  Dean Mustakinov, Florian Schiffmann
31 Dec 2024
ISBN  978-1-921654-90-9
This online version of the GEMPACK documentation is designed for effective searching and navigation
within your browser. You can click on on any blue link to jump to the indicated place, and use the
Back button to return. Use the middle mouse button to open a link in a new tab. A yellow panel is
visible at top right, with links to the Contents page and Index. To find information on a
particular topic, go to the Index first. You can also use your browser's Edit..Find command to
search through the entire document.
You can use your browser's View menu to adjust the text size. Or, using your keyboard, press CTRL
and + or CTRL and - to zoom in or out. If your mouse has a wheel, hold down the CTRL key, and then
scroll the wheel to zoom in or out. You may need to wait a second or two to see the effect.
This manual refers to GEMPACK Release 12.2 and later — but will be useful too for earlier releases.
Each section or subsection has a "topic ID" which appears in green at the end of section headings.
GEMPACK programs may emit warning or error messages that refer you to sections of this manual.
The references may include section numbers, section titles and topic IDs, but the topic ID is
most likely to remain unchanged through successive revisions of the manual.
If you want to print out sections, use the matching PDF file, GPmanual.pdf.
We thank Ken Pearson and Jill Harrison who wrote large parts of previous GEMPACK manuals; much of
their work is incorporated here.
A condition of your GEMPACK licence is that
acknowledgement of GEMPACK must be made when reporting results that have been obtained with GEMPACK.
To cite this manual, use:
Horridge J.M.,  Jerie M.,   Mustakinov D. &  Schiffmann F. (2024),
GEMPACK manual
, GEMPACK Software, Centre of Policy Studies, Victoria University, Melbourne,  ISBN  978-1-921654-34-3, https://ideas.repec.org/p/cop/wpaper/gpman.html
Other GEMPACK-related citations are suggested in section
1.7
.
Brief Table of Contents
1 Introduction
[gpd1.1]
2 Installing  GEMPACK on Windows PCs
[gpd6.1]
3 How to carry out simulations with models
[gpd1.2]
4 Building or modifying models
[gpd1.3]
5 Header Array files
[harfiles]
6 Constructing HAR files
[gpd1.4]
7 GEMPACK file types, names and suffixes
[gpd1.5.8]
8 Overview of running TABLO and the TABLO language
[gpd2.1]
9 Additional information about running TABLO
[gpd2.2]
10 The TABLO language: basic syntax
[gpd2.3]
11 Syntax and semantic details
[gpd2.4]
12 TABLO statements for post-simulation processing
[gpd5.2]
13 Ranking sets via data (finding winners and losers)
[gpd5.3]
14 Condensing models
[condense]
15 Verifying economic models
[gpd2.6]
16 Intertemporal models
[gpd2.7]
17 Less obvious examples of the TABLO language
[gpd2.8]
18 Linearizing levels equations
[gpd2.9]
19 Overview of simulation reference chapters 20 to 35
[gpd3.1]
20 Command (CMF) files
[gpd3.2]
21 TABLO input files and auxiliary files
[gpd3.3]
22 CMF statements for data files, updated data files and display files
[gpd3.4]
23 Specifying the closure
[gpd3.5.1a]
24 Specifying the shocks
[gpd3.5.5]
25 Actions in GEMSIM and TABLO-generated programs
[gpd3.6]
26 Multi-step solution methods
[gpd3.7]
27 Solution (SL4) files
[gpd3.8]
28 SLC, UDC, AVC and CVL files
[slcfiles]
29 Subtotals via GEMSIM or TABLO-generated programs
[gpd3.11]
30 Solving models and simulation time
[gpd3.12]
31 Solving a model in parallel on a machine with two or more processors
[gpd9.2]
32 Memory management
[gpd3.13]
33 Options for GEMSIM and TABLO-generated programs
[gpd3.14]
34 Run-time errors
[gpd3.15]
35 Summary of command file statements
[gpd3.18]
36 GEMPACK Windows programs
[gpd4.2]
37 Command-line programs for working with header array files
[gpd4.4]
38 Syntax of GEMPACK text data files
[gpd4.6]
39 SLTOHT: processing simulation results
[gpd4.8]
40 SLTOHT for spreadsheets
[gpd4.9]
41 ACCUM and DEVIA : accumulation and differences
[gpd4.10]
42 Hands-on tutorials for models supplied with GEMPACK
[gpd8.1]
43 Getting started with GEMPACK via WinGEM
[gpd8.2]
44 Command prompt: hands-on computing
[gpd8.3]
45 Using RunGEM for simulations
[gpd8.5]
46 Using AnalyseGE to analyse simulation results
[gpd8.6]
47 Print edition ends here
[endprint]
48 Working with GEMPACK command-line programs
[gpd1.5]
49 Miscellaneous information
[miscstuff]
50 Code options when running TABLO
[gpd2.5]
51 Simulations for models with complementarities
[gpd3.16]
52 Subtotals with complementarity statements
[gpd5.7]
53 More examples of post-simulation processing
[postsim2]
54 Using MODHAR to create or modify header array files
[gpd4.3]
55 Ordering of variables and equations in solution and equation files
[ordering]
56 SEENV: to see the closure on an environment file
[gpd4.12]
57 Automated homogeneity testing
[autohomog]
58 Several simultaneous Johansen simulations via SAGEM
[gpd3.10]
59 Equations files and LU files
[gpd3.9]
60 Example models supplied with GEMPACK
[models]
61 Pivoting, memory-sharing, and other solution strategies
[pivots]
62 Limited executable-image size limits
[exelimits]
63 Some technical details of GEMPACK
[technical]
64 Rarely used features of GEMPACK programs
[legacy]
65 Choosing sets of variables interactively
[gpd4.17]
66 Older ways to choose closure and shocks
[oldshkclos]
67 Improving your TAB and CMF files
[better]
68 Shock statements designed for use with RunDynam
[rdynshoks]
69 GEMPACK on Linux, Unix or Mac OS X
[unix]
70 TEXTBI : extracting TAB, STI and CMF files from AXT, SL4 and CVL files
[gpd4.14]
71 History of GEMPACK
[oldnewfeat]
72 TABLO-generated programs and GEMSIM - timing comparison
[gpd8.4]
73 Fortran compilers for Source-code GEMPACK
[fortrans]
74 LTG variants and compiler options
[gpd6.7.5a]
75 Fine print about header array files
[gpd4.5]
76 Converting binary files: LF90/F77L3  to/from Intel/LF95/GFortran
[gpd4.15]
77 Translation between GEMPACK and GAMS data files
[gdxhar]
78 Recent GEMPACK with older RunGTAP or RunDynam
[gpd5.12]
79 SUMEQ: information from equations files
[gpd4.13]
80 Older GEMPACK documents
[gemdocs]
81 References
[references]
82 Index
[index]
83 End of document
[docend]
Detailed Table of Contents
1 Introduction
[gpd1.1]
1.1 Organization of this manual
[manualoutline]
1.2 Using this manual
[usingmanual]
1.2.1 For experienced GEMPACK users
[gpd1.1.5.2]
1.2.2 For new GEMPACK users -- getting started
[gpd1.1.5.1]
1.3 Supported Operating Systems
[supportedos]
1.4 The GEMPACK programs
[gpd9.1.5]
1.4.1 The original command-line programs
[gpd9.1.5.1]
1.4.2 The Windows programs
[gpd9.1.5.2]
1.4.3 TABLO-generated programs
[gpd1.1.7.1]
1.5 Models supplied with GEMPACK
[gpd1.1.8]
1.6 Different versions of GEMPACK and associated licences
[gpd1.1.9]
1.6.1 Source-code versions and licences
[gpd1.1.9.1]
1.6.2 Unlimited executable-image version and licence
[gpd1.1.9.3]
1.6.3 Limited executable-image version and licence
[gpd1.1.9.2]
1.6.4 Using Exe-image and Source-code GEMPACK together
[gpeisc]
1.6.5 When is a licence needed
[gpd1.1.9.7]
1.6.6 Introductory licence
[gpd1.1.9.5]
1.7 Citing GEMPACK
[citinggempack]
1.8 Communicating with GEMPACK
[gpd1.1.2]
1.8.1 GEMPACK web site
[gpd1.1.3]
1.8.2 GEMPACK-L mailing list
[gpd1.1.4]
1.9 Training Courses
[training]
1.10 Acknowledgments
[ackintro]
2 Installing  GEMPACK on Windows PCs
[gpd6.1]
2.1 Preparing to install GEMPACK
[gpd6.2]
2.1.1 System requirements
[gpd6.2.1]
2.1.2 Your GEMPACK licence file
[gplic]
2.1.3 Where to install
[instdir]
2.1.4 Notes for IT support
[itsupport]
2.1.5 [Source-code only] Testing the Fortran installation
[gpd6.3.3]
2.1.6 Configure Anti-virus programs
[antivirus]
2.2 Installing GEMPACK
[gpd6.4]
2.2.1 If a warning appears after installing
[pcawarning]
2.2.2 [Source-code only] If an error occurs
[gpd6.4.1.1]
2.2.3 Some GEMPACK licences require activation
[activation]
2.2.4 GEMPACK licence
[gpd6.4.4]
2.2.5 Changes to your PATH and Environment
[gpd6.4.4a]
2.2.6 System environment settings for performance
[mathlibperf]
2.3 Testing the Installation
[gpd6.5]
2.4 [Source-code only] Re-Testing the Installation
[gpd6.5s]
2.5 If you still have problems
[witsend]
2.6 More simulations to test GEMPACK and WinGEM
[gpd6.5.3]
2.7 Working with GEMPACK
[gpd6.6]
2.7.1 New model's directory location
[gpd6.6.2]
2.7.2 [Source-code only] GEMSIM or TABLO-generated programs ?
[gpd6.6.3]
2.7.3 Text editor
[gpd6.6.4]
2.7.4 If you installed in a new directory (not C:\GP)
[gpd6.4.3]
2.7.5 If a program runs out of memory
[gpd6.6.5]
2.7.6 Copying GEMPACK programs to other PCs
[gpd6.6.9]
2.8 Manually setting the PATH and GPDIR
[gpd6.4.2]
2.8.1 Checking and setting PATH and GPDIR
[gpd6.4.2.1]
2.8.2 Trouble-shooting environment variables
[envvartrouble]
2.9 Technical Topics
[gpd6.7]
2.9.1 [Source-code only] Running BuildGP
[gpd6.7.3]
2.9.2 File association
[gpd6.6.7]
2.9.3 Keep and Temporary directories and GEMPACK Windows programs
[gpd6.6.8]
2.9.4 Installing GEMPACK on a network
[gpd6.8]
2.9.5 Uninstalling GEMPACK
[gpd6.7.6]
2.9.6 Finding GEMPACK Version and Release Information
[identver]
3 How to carry out simulations with models
[gpd1.2]
3.1 An example simulation with stylized Johansen
[gpd1.2.1]
3.1.1 Introduction to the stylized Johansen model
[gpd1.2.1.1]
3.1.2 The simulation
[gpd1.2.1.2]
3.2 Preparing a directory for model SJ
[gpd1.2.4.2]
3.3 Using GEMPACK: WinGEM or command prompt?
[gpd1.2.3]
3.4 Stylized Johansen example simulation
[gpd1.2.4]
3.4.1 Starting WinGEM
[gpd1.2.4.1]
3.4.2 Setting the working directory
[gpd1.2.4.3]
3.4.3 Looking at the data directly using ViewHAR
[gpd1.2.4.4]
3.5 Implementing and running model SJ
[gpd1.impsj]
3.5.1 TABLO-generated program or GEMSIM?
[gpd1.2.4.5]
3.5.2 Source-code method: using a TABLO-generated program
[gpd1.2.4.6]
3.5.3 Executable-image method: using GEMSIM
[gpd1.2.4.7]
3.5.4 Step 3 - View the Solution using ViewSOL
[gpd1.2.viewsol]
3.6 The steps in carrying out a simulation
[gpd1.2.5]
3.6.1 Steps 1 and 2 using a TABLO-generated program (source-code GEMPACK)
[gpd1.2.5.1]
3.6.2 Steps 1 and 2 using GEMSIM
[gpd1.2.5.2]
3.6.3 Other Simulations
[gpd1.2.5.othsims]
3.7 Interpreting the results
[gpd1.2.7]
3.8 Specifying a simulation
[gpd1.2.8]
3.8.1 Specifying a simulation via a GEMPACK command file
[gpd1.2.8.1]
3.9 The updated data - another result of the simulation
[gpd1.2.9]
3.10 Preparing tables and graphs for a report
[gpd1.2.10]
3.10.1 Example 1:  Copying from ViewSOL to Spreadsheet and WordProcessor
[gpd1.2.viewsolexport]
3.10.2 Example 2:  Using the GEMPACK Program SLTOHT and Option SSS
[gpd1.2.sltoht1]
3.10.3 Example 3:  Using the Program SLTOHT and Option SES
[gpd1.2.sltoht2]
3.10.4 Graphs
[gpd1.2.10.1]
3.11 Changing the closure and shocks
[gpd1.2.11]
3.12 How Johansen and multi-step solutions are calculated
[gpd1.2.13]
3.12.1 The linearized equations of a model
[gpd1.2.13.1]
3.12.2 Johansen solutions
[gpd1.2.13.2]
3.12.3 Multi-step simulations and accurate solutions of nonlinear equations
[gpd1.2.13.3]
3.12.4 Smiling or frowning face numbers are reported
[gpd5.9.2.1]
3.12.5 Fatal error if accuracy too low (GEMSIM and TG-programs)
[gpd5.9.2.2]
3.13 GEMPACK programs - an overview
[gpd1.2.14]
3.13.1 Working with TABLO input files
[gpd1.2.14.1]
3.13.2 Carrying out simulations
[gpd1.2.14.2]
3.13.3 Looking at, and processing, simulation results
[gpd1.2.14.3]
3.13.4 Working with data
[gpd1.2.14.4]
3.13.5 Windows modelling environments
[gpd1.2.14.5]
3.13.6 Other programs for special tasks
[gpd1.2.14.6]
3.13.7 Programs for use on non-Windows PCs
[gpd1.2.14.7]
3.14 Different GEMPACK files
[gpd1.2.15]
3.14.1 The most important files
[gpd1.2.15.1]
3.14.2 Files for communication between programs
[gpd1.2.15.2]
3.14.3 LOG files
[gpd1.2.15.3]
3.14.4 Stored-input (STI) files
[gpd1.2.15.4]
3.14.5 Files for power users
[gpd1.2.15.5]
3.14.6 Summary of files
[gpd1.2.15.7]
3.14.7 Work files
[gpd1.2.15.6]
3.14.8 Files you can eventually delete
[junkfiles]
3.15 For new users - what next?
[gpd1.2.16]
4 Building or modifying models
[gpd1.3]
4.1 Writing down the equations of a model
[gpd1.3.1]
4.1.1 Writing down the equations of Stylized Johansen
[gpd1.3.1.1]
4.2 Data requirements for the linearized equations
[gpd1.3.2]
4.2.1 Data requirements for Stylized Johansen
[gpd1.3.2.1]
4.3 Constructing the TABLO input file for a model
[gpd1.3.3]
4.3.1 Viewing the TABLO input file
[gpd1.3.3.1]
4.3.2 Constructing part of the TABLO input file for Stylized Johansen
[gpd1.3.3.2]
4.3.3 "Mixed" TABLO input file for the Stylized Johansen model
[gpd1.3.3.3]
4.3.4 Completing the TABLO input file for Stylized Johansen
[gpd1.3.3.4]
4.3.5 Change or percentage-change variables
[gpd1.3.3.5]
4.3.6 Variable or parameter ?
[gpd1.3.3.6]
4.3.7 TABLO language - syntax and semantics
[gpd1.3.3.7]
4.4 Linearized TABLO input files
[gpd1.3.4]
4.4.1 A linearized TABLO input file for Stylized Johansen
[gpd1.3.4.1]
4.4.2 Noteworthy features in the linearized TABLO input file
[gpd1.3.4.2]
4.4.3 Analysing simulation results
[gpd1.3.4.3]
4.4.4 Writing UPDATE statements
[gpd1.3.4.4]
4.4.5 Numerical versions of linearized equations
[gpd1.3.4.5]
4.4.6 Numerical examples of update statements
[gpd1.3.4.6]
4.4.7 How equations are recalculated in a multi-step calculation
[gpd1.3.4.7]
4.5 Levels TABLO input files
[gpd1.3.5]
4.5.1 Levels TABLO input file for Stylized Johansen
[gpd1.3.5.1]
4.6 TABLO linearizes levels equations automatically
[gpd1.3.7]
4.7 Creating the TABLO input file and command files for your own model
[gpd1.3.9]
4.7.1 Correcting errors in TABLO input files
[gpd1.3.9.1]
4.7.2 Correcting errors in command files
[gpd1.3.9.2]
5 Header Array files
[harfiles]
5.0.1 Data on Header Array files
[gpd4.3.1]
5.0.2 Array type
[gpd4.3.1.1]
5.0.3 Set and element labelling on header array files
[gpd4.5a]
5.0.4 Long names
[gpd4.3.1.2]
5.0.5 File history and creation information
[gpd9.7.5.3]
5.1 Ways to create or modify header array files
[gpd4.3.2]
5.1.1 Creating an initial HAR file of raw data
[gpd4.3.2a]
5.1.2 Processing raw data to create a HAR file that model can use
[gpd4.3.2b]
6 Constructing HAR files
[gpd1.4]
6.1 Constructing the header array data file for Stylized Johansen
[sjmkdat]
6.2 Editing the header array data file for Stylized Johansen
[sjmoddat]
6.2.1 Other ViewHAR capabilities
[gpd1.4.5.8]
6.3 Checking data is balanced
[gpd1.4.7]
6.3.1 SJCHK.TAB to check balance for Stylized Johansen
[gpd1.4.7.1]
6.3.2 SJCHK.TAB to check balance of updated data
[gpd1.4.7.2]
6.3.3 GTAPVIEW for checking and summarising GTAP data
[gpd1.4.7.3]
6.3.4 Checking the balance of ORANIG data
[gpd1.4.7.4]
6.4 Which program to use in file conversion?
[gpd1.4.8]
6.5 Further information
[gpd1.4.9]
7 GEMPACK file types, names and suffixes
[gpd1.5.8]
7.0.1 Files with system-determined suffixes
[gpd1.5.8.1]
7.0.2 Suffixes of other files
[gpd1.5.8.2]
7.0.3 Files -- binary, header array or text?
[gpd1.5.8.3]
7.0.4 Why so many files?
[gpd1.5.8.4]
7.1 Allowed file and directory names
[gpd1.5.9]
7.1.1 File names containing spaces
[gpd1.5.9.4]
7.1.2 Characters in stored-input files and command files
[gpd1.5.9.5]
7.1.3 Files that could be deleted
[cleanupfiles]
8 Overview of running TABLO and the TABLO language
[gpd2.1]
8.1 Running TABLO on an existing model
[gpd2.1.1]
8.1.1 Example models ORANIG01 and GTAP61
[gpd2.1.1.1]
8.1.2 TAB file and WFP/PGS on command line
[gpd5.10.1.2]
8.1.3 Running TABLO from TABmate with no STI file
[tablocode]
8.1.4 Preliminary pass to count statements
[gpd2.1.1.2]
8.2 Compiling and linking TABLO-generated programs
[gpd2.1.2]
8.3 Writing a TABLO input file for a new model
[gpd2.1.4]
8.4 Modern ways of writing TABLO input files (on a PC)
[gpd2.1.5]
8.4.1 Using TABmate
[gpd2.1.5.1]
8.4.2 Using TABmate to find a closure and suggest substitutions
[autoclosure]
8.4.3 Using TABmate to create a CMF file
[autocmf]
8.4.4 Using TABmate to reformat your code
[beautyparlour]
8.4.5 Using ViewHAR to write TABLO code for data manipulation
[gpd2.1.5.2]
8.5 Condensing a large model
[gpd2.1.6]
8.5.1 Condensation in STI file: a legacy technique
[oldsticond]
9 Additional information about running TABLO
[gpd2.2]
9.1 TABLO options
[gpd2.2.1]
9.1.1 TABLO input file written on the auxiliary files
[gpd2.2.1.1]
9.1.2 TABLO file and TABLO STI file stored on solution file
[gpd2.2.1.2]
9.1.3 Specialised check options
[gpd2.2.1.3]
9.1.4 Doing condensation or going to code generation
[gpd2.2.1.4]
9.1.5 TABLO code options
[gpd2.2.1.5]
9.1.6 Identifying and correcting syntax and semantic errors
[gpd2.2.1.6]
9.2 TABLO linearizes levels equations automatically
[gpd2.2.2]
9.2.1 Change or percentage-change associated linear variables
[gpd2.2.2.1]
9.2.2 How levels variable statements are converted
[gpd2.2.2.2]
9.2.3 How levels equation statements are converted
[gpd2.2.2.3]
9.2.4 Linearizing levels equations
[gpd2.2.2.4]
9.2.5 Linearizing a sum
[gpd2.2.2.5]
9.2.6 Algorithm used by TABLO
[gpd2.2.2.6]
9.2.7 TABLO can write a linearised TAB file
[gpd9.7.19]
9.3 Reporting Newton error terms in models with levels equations
[gpd5.9.14]
9.3.1 Example: reporting Newton errors with SJLVLBER.CMF
[gpd5.9.14.1]
9.3.2 Command file statements for reporting Newton error terms
[gpd5.9.14.2]
10 The TABLO language: basic syntax
[gpd2.3]
10.1 SET
[gpd2.3.1]
10.1.1 Set expressions (includes unions, intersections and complements)
[gpd2.3.1.0]
10.1.2 Equal sets
[gpd2.3.1.2]
10.1.3 Data-dependent sets
[gpd2.3.1.3]
10.1.4 Set examples from ORANIG model
[gpd2.3.1.5]
10.1.5 Set examples from GTAP model
[gpd2.3.1.6]
10.1.6 Set products
[gpd2.3.1.4]
10.1.7 Multidimensional sets and tuples
[tuples]
10.1.8 Ranked sets
[gpd2.3.1.6a]
10.2 SUBSET
[gpd2.3.2]
10.2.1 Subset examples from ORANIG model
[gpd2.3.2.1]
10.2.2 Subset examples from GTAP model
[gpd2.3.2.2]
10.3 COEFFICIENT
[gpd2.3.3]
10.4 VARIABLE
[gpd2.3.4]
10.5 FILE
[gpd2.3.5]
10.5.1 SSE output
[gpd5.9.1]
10.6 READ
[gpd2.3.6]
10.7 WRITE
[gpd2.3.7]
10.8 FORMULA
[gpd2.3.8]
10.9 EQUATION
[gpd2.3.9]
10.9.1 FORMULA & EQUATION
[gpd2.3.9.1]
10.10 UPDATE
[gpd2.3.10]
10.11 ZERODIVIDE
[gpd2.3.11]
10.11.1 More about zerodivides
[gpd2.4.13]
10.12 DISPLAY
[gpd2.3.12]
10.13 MAPPING
[gpd2.3.13]
10.13.1 Formulas for mappings, and reading and writing mappings
[gpd2.3.13.1]
10.13.2 Projection mappings from a set product
[gpd2.3.13.2]
10.14 ASSERTION
[gpd2.3.14]
10.15 TRANSFER
[gpd2.3.15]
10.16 OMIT, SUBSTITUTE and BACKSOLVE
[gpd2.3.16_17_18]
10.16.1 Example - condensation in the TABLO input file for model ORANIG
[gpd2.3.18.1]
10.17 COMPLEMENTARITY
[gpd2.3.19]
10.18 POSTSIM
[gpd2.3.19a]
10.19 Setting default values of qualifiers
[gpd2.3.20]
10.19.1 Default statements for bounds on coefficients
[gpd5.8.2]
10.20 TABLO statement qualifiers - a summary
[gpd2.3.21]
10.20.1 Spaces and qualifier syntax
[gpd2.3.21.1]
11 Syntax and semantic details
[gpd2.4]
11.1 General notes on the TABLO syntax and semantics
[gpd2.4.1]
11.1.1 TABLO statements
[gpd2.4.1.1]
11.1.2 Lines of the TABLO input file
[gpd2.4.1.2]
11.1.3 Upper and lower case
[gpd2.4.1.3]
11.1.4 Comments
[gpd2.4.1.4]
11.1.5 Strong comment markers
[gpd2.4.1.5]
11.1.6 Reserved (special) characters
[gpd2.4.1.6]
11.1.7 Chinese and accented characters
[nonascii]
11.2 User defined input
[gpd2.4.2]
11.2.1 Names
[gpd2.4.2.1]
11.2.2 Abbreviating lists of set elements
[gpd2.4.2.0]
11.2.3 Labelling information (text between hashes #)
[gpd2.4.2.2]
11.2.4 Arguments: indices, set elements or index expressions
[gpd2.4.2.3]
11.2.5 Index expressions with elements from run-time sets
[gpd2.4.2.4]
11.3 Quantifiers and quantifier lists
[gpd2.4.3]
11.4 Expressions used in equations, formulas and updates
[gpd2.4.4]
11.4.1 Operations used in expressions
[gpd2.4.4.1]
11.4.2 Brackets in expressions
[gpd2.4.4.3]
11.4.3 Sums over sets in expressions
[gpd2.4.4.2]
11.4.4 MaxS, MinS and Prod operators
[gpd2.4.4.2a]
11.4.5 Conditional quantifiers and SUMs, PRODs, MAXS and MINS
[gpd2.4.4.5]
11.4.6 Conditional expressions
[gpd2.4.4.6]
11.4.7 Index-IN-Set condition for IF expressions
[gpd2.4.4.6b]
11.4.8 Linear variables in expressions
[gpd2.4.4.7]
11.4.9 Constants in expressions
[gpd2.4.4.8]
11.4.10 Indices in expressions
[gpd2.4.4.9]
11.4.11 Index-expression conditions
[gpd2.4.4.10]
11.5 Functions
[gpd2.4.4.4]
11.5.1 ID01 and ID0V functions
[gpd2.4.4.4.1]
11.5.2 RANDOM function
[gpd2.4.4.4.2]
11.5.3 Statistical functions
[statistical]
11.5.4 NORMAL  and  CUMNORMAL functions
[gpd2.4.4.4.3]
11.5.5 Functions for log-normal distribution
[gpd9.7.9]
11.5.6 $POS function
[gpd2.4.4.4.4]
11.5.7 ROUND, TRUNC0 and TRUNCB functions
[gpd2.4.4.4.5]
11.6 Coefficients and levels variables
[gpd2.4.5]
11.6.1 Coefficients -- what are they ?
[gpd2.4.5.1]
11.6.2 Model parameters
[gpd2.4.5.2]
11.6.3 Integer coefficients in expressions and elsewhere
[gpd2.4.5.3]
11.6.4 Where coefficients and levels variables can occur
[gpd2.4.5.4]
11.6.5 Reporting levels values when carrying out simulations
[gpd2.4.5.5]
11.6.6 How do you see the pre-simulation and post-simulation levels values?
[gpd2.4.5.6]
11.6.7 Specifying acceptable range of coefficients read or updated
[gpd2.4.5.7]
11.7 Sets
[gpd2.4.6]
11.7.1 Set size and set elements
[gpd2.4.6.1]
11.7.2 Obsolete "maximum size" in SET statements
[gpd2.4.6.2]
11.7.3 Set unions, intersections and equality
[gpd2.4.6.3]
11.7.4 Set complements and relative complements
[gpd2.4.6.4]
11.7.5 Longer set expressions
[gpd2.4.6.4b]
11.7.6 Sets whose elements depend on data
[gpd2.4.6.5]
11.7.7 Writing the elements of one set
[gpd2.4.6.6]
11.7.8 Writing the elements of all (or many) sets
[gpd2.4.6.7]
11.7.9 Empty sets
[gpd2.4.6.8]
11.7.10 Reading set elements from a file
[gpd2.4.6.9]
11.7.11 Creating element names for set products
[gpd2.4.6.10]
11.8 Subsets
[gpd2.4.7]
11.9 Mappings between sets
[gpd2.4.8]
11.9.1 Defining set mapping values
[gpd2.4.8.1]
11.9.2 Checking values of a mapping
[gpd2.4.8.2]
11.9.3 Insisting that a set mapping be onto
[gpd2.4.8.3]
11.9.4 Using set mappings
[gpd2.4.8.4]
11.9.5 Set Mappings can only be used in index expressions
[gpd2.4.8.5]
11.9.6 Two or more set mappings in an index expression
[gpd2.4.8.6]
11.9.7 Set mappings in arguments
[gpd2.4.8.7]
11.9.8 Set mappings on LHS of a Formula
[mapfmlhs]
11.9.9 Other semantics for mappings
[gpd2.4.8.8]
11.9.10 Writing the values of set mappings
[gpd2.4.8.9]
11.9.11 Reading part of a set mapping BY_ELEMENTS
[gpd2.4.8.10]
11.9.12 Mapping values can be given by values of other mapping or index
[gpd2.4.8.11]
11.9.13 Writing a set mapping to a text file
[gpd2.4.8.12]
11.9.14 Long name when a set mapping is written to a header array file
[gpd2.4.8.14]
11.9.15 ViewHAR and set mappings
[gpd2.4.8.15]
11.10 Files
[gpd2.4.9]
11.10.1 Text files
[gpd2.4.9.1]
11.11 Reads, writes and displays
[gpd2.4.10]
11.11.1 How data is associated with coefficients
[gpd2.4.10.1]
11.11.2 Partial reads, writes and displays
[gpd2.4.10.2]
11.11.3 Seeing the values of integer coefficients of dimension 3 or higher
[gpd5.8.5]
11.11.4 FORMULA(INITIAL)s
[gpd2.4.10.3]
11.11.5 Coefficient initialisation
[gpd2.4.10.4]
11.11.6 Display files
[gpd2.4.10.5]
11.11.7 Transferring long names when executing write statements
[gpd2.4.10.6]
11.11.8 Reads only if header exists -- read qualifier ifheaderexists
[gpd5.8.1]
11.12 Updates
[gpd2.4.11]
11.12.1 Purpose of updates
[gpd2.4.11.1]
11.12.2 Which type of update?
[gpd2.4.11.2]
11.12.3 What if an initial value is zero ?
[gpd2.4.11.3]
11.12.4 UPDATE semantics
[gpd2.4.11.4]
11.12.5 Example 1 of deriving update statements: sum of two flows
[gpd2.4.11.5]
11.12.6 Example 2 of deriving update statements: powers of taxes
[gpd2.4.11.6]
11.12.7 Example 3 of deriving update statements: an update (change) statement
[gpd2.4.11.7]
11.12.8 Writing updated values from FORMULA(INITIAL)s
[gpd2.4.11.8]
11.13 Transfer statements
[gpd2.4.12]
11.13.1 XTRANSFER Statements on command files
[gpd2.4.12.1]
11.14 Complementarity semantics
[gpd2.4.14]
11.14.1 Condensation and complementarities
[gpd2.4.14.1]
11.14.2 Linking the complementarity to existing linear variables
[gpd2.4.14.2]
11.15 The RAS_MATRIX function
[gpd9.7.10]
11.15.1 The RAS procedure
[gpd9.7.10.1]
11.15.2 An intuitive way to think of the RAS
[gpd9.7.10.2]
11.15.3 RAS iterations
[gpd9.7.10.3]
11.15.4 RAS syntax in TABLO
[gpd9.7.10.4]
11.15.5 The RAS report
[gpd9.7.10.5]
11.15.6 Warnings of potential problems
[gpd9.7.10.6]
11.16 Ordering
[gpd2.4.15]
11.16.1 Ordering of the input statements
[gpd2.4.15.1]
11.16.2 Order in which reads, formulas, equations and updates are performed
[gpd2.4.15.6]
11.17 TABLO input files with no equations
[gpd2.4.16]
11.18 Loops in TAB files
[loop-tab]
12 TABLO statements for post-simulation processing
[gpd5.2]
12.1 Simple examples of PostSim statements
[postsimexm]
12.2 PostSim TAB file statements, syntax and semantic rules
[gpd5.2.5]
12.2.1 Statements allowed in post-simulation sections of a TAB file
[gpd5.2.5.1]
12.2.2 Syntax and semantics for formulas in PostSim part of TAB file
[gpd5.2.5.2]
12.2.3 Semantics for reads in PostSim part of TAB file
[gpd5.2.5.3]
12.2.4 Semantics for assertions in PostSim part of TAB file
[gpd5.2.5.4]
12.2.5 Semantics for zerodivides in PostSim part of TAB file
[gpd5.2.5.5]
12.2.6 Default statements and certain qualifiers not relevant in PostSim part
[gpd5.2.5.6]
12.2.7 PostSim sets, subsets, coefficients not allowed in the ordinary part
[gpd5.2.5.7]
12.2.8 PostSim qualifier for write or display
[gpd5.2.5.8]
12.2.9 Implications for condensation
[gpd5.2.5.9]
12.3 PostSim extra statements in a command file
[gpd5.2.6]
12.3.1 Suppressing post-simulation processing
[gpd5.2.7]
12.4 PostSim parts of TAB file and AnalyseGE
[gpd5.2.9]
12.4.1 Coefficients or expressions selected from the TABmate form
[gpd5.2.9.1]
12.4.2 Expressions evaluated from the AnalyseGE form
[gpd5.2.9.2]
12.4.3 UDC files now redundant?
[gpd5.2.9.3]
12.5 Technical details: When and how is post-simulation part done?
[gpd5.2.8]
12.5.1 PostSim sets and subsets not on equations file
[gpd5.2.10]
12.6 Advantages of PostSim processing in TAB file
[gpd5.2.4]
13 Ranking sets via data (finding winners and losers)
[gpd5.3]
13.1 Example: identifying winners and/or losers
[gpd5.3.1]
13.1.1 Ranking example OG01PS.TAB
[gpd5.3.1.1]
13.2 Ranked set statements -- syntax and semantics
[gpd5.3.2]
13.3 Converting non-intertemporal sets to intertemporal sets and vice versa
[gpd5.3.3]
13.3.1 TABLO statements
[gpd5.3.3.1]
13.3.2 Household income example in detail
[gpd5.3.3.2]
14 Condensing models
[condense]
14.1 Condensing models
[gpd1.3.8]
14.1.1 Substituting out variables
[gpd1.3.8.1]
14.1.2 Condensation examples
[gpd1.3.8.2]
14.1.3 Backsolving for variables
[gpd1.3.8.3]
14.1.4 Condensation examples using backsolving
[gpd1.3.8.4]
14.1.5 Results on the solution file in condensation examples
[gpd1.3.8.5]
14.1.6 Should all substitutions be backsolves?
[gpd1.3.8.6]
14.1.7 Omitting variables
[gpd1.3.8.7]
14.1.8 Automatic substitutions
[gpd1.3.8.7b]
14.1.9 Condensation actions can be put on the TABLO input file
[gpd1.3.8.8]
14.1.10 More details about condensation and substituting variables
[gpd2.2.3]
14.1.11 Looking ahead to substitution when creating TABLO input files
[gpd2.2.3.1]
14.1.12 System-initiated formulas and backsolves
[gpd2.2.3.2]
14.1.13 Treating substitutions as backsolves - option ASB
[gpd2.2.3.4]
14.1.14 Condensation statements on a TABLO input file
[gpd2.2.4]
14.1.15 Ignoring TABLO condensation
[gpd2.2.4.1]
14.1.16 Condensation information file
[gpd9.7.8]
14.1.17 Submatrix nonzeros information file
[smnzinffile]
14.1.18 CondOpt tool to find optimal condensation
[condopt]
15 Verifying economic models
[gpd2.6]
15.1 Is balanced data still balanced after updating?
[gpd2.6.1]
15.1.1 Balance after n-steps
[gpd2.6.1.1]
16 Intertemporal models
[gpd2.7]
16.1 Introduction to intertemporal models
[gpd2.7.1]
16.2 Intertemporal sets
[gpd2.7.2]
16.2.1 Set size and set elements - fixed or determined at run time
[gpd2.7.2.1]
16.3 Use an INTEGER coefficient to count years
[gpd2.7.3]
16.4 Enhancements to semantics for intertemporal models
[gpd2.7.4]
16.5 Recursive formulas over intertemporal sets
[gpd2.7.5]
16.6 Constructing an intertemporal data set satisfying all model equations
[gpd2.7.6]
16.6.1 Example using the CRTS intertemporal model
[gpd2.7.6.1]
16.7 ORANI-INT: A multi-sector rational expectations model
[gpd2.7.7]
17 Less obvious examples of the TABLO language
[gpd2.8]
17.1 Flexible formula for the size of a set
[gpd2.8.1]
17.2 Adding across time periods in an intertemporal model
[gpd2.8.2]
17.3 Conditional functions or equations
[gpd2.8.3]
17.3.1 Other methods
[gpd2.8.3b]
17.4 Aggregating data and simulation results
[gpd2.8.4]
17.5 Use of special sets and coefficients
[gpd2.8.5]
18 Linearizing levels equations
[gpd2.9]
18.1 Differentiation rules used by TABLO
[gpd2.9.1]
18.2 Linearizing equations by hand
[gpd2.9.2]
18.2.1 General procedure - change differentiation
[gpd2.9.2.1]
18.2.2 Rules to use
[gpd2.9.2.2]
18.2.3 Linearizing equations in practice
[gpd2.9.2.3]
18.2.4 Linearizing using standard references
[gpd2.9.2.4]
18.3 Linearized equations on information file
[gpd2.9.3]
18.4 Linearized equations via AnalyseGE
[gpd2.9.3b]
18.5 Be careful when using linearized equations
[gpd2.9.4]
18.6 Keep formulas and equations in synch
[gpd2.9.4b]
19 Overview of simulation reference chapters 20 to 35
[gpd3.1]
20 Command (CMF) files
[gpd3.2]
20.1 Data manipulation using GEMSIM or TABLO-generated programs
[gpd3.2.2]
20.2 Simulations using GEMSIM or TABLO-generated programs
[gpd3.2.1]
20.3 SAGEM simulations
[gpd3.2.3]
20.4 File names
[gpd3.2.4]
20.4.1 Naming the command file
[gpd3.2.4.1]
20.4.2 File names containing spaces
[gpd3.2.4.2]
20.5 Using the command file stem for names of other output files
[gpd3.2.5]
20.5.1 Default:  solution file stem = command file stem
[gpd3.2.5.1]
20.5.2 Default:  log file stem = command file stem
[gpd3.2.5.2]
20.5.3 Default:  display file stem = command file stem
[gpd3.2.5.3]
20.5.4 Using <CMF> in command files
[gpd3.2.5.4]
20.5.5 Position of <CMF> in command file statements
[gpd9.7.16]
20.6 Log files and reporting CPU time
[gpd3.2.6]
20.7 General points about command file statements
[gpd3.2.7]
20.8 Eliminating syntax errors in GEMPACK command files
[gpd3.2.8]
20.9 Replaceable parameters in CMF files
[cmfparm]
20.9.1 The newcmf= option
[newcmf]
21 TABLO input files and auxiliary files
[gpd3.3]
21.1 GEMSIM and GEMSIM auxiliary files
[gpd3.3.1]
21.2 TABLO-generated programs and auxiliary files
[gpd3.3.2]
21.3 How are the names of the auxiliary files determined?
[gpd3.3.3]
21.4 Check that auxiliary files are correct
[gpd3.3.4]
21.4.1 Model information (MIN) file date
[gpd3.3.4.1]
21.5 Carrying out simulations on other machines
[gpd3.3.5]
21.5.1 Copying TABLO-generated programs to other PCs
[gpd3.3.5.1]
21.5.2 GEMPACK licence may be required
[gpd3.3.5.2]
22 CMF statements for data files, updated data files and display files
[gpd3.4]
22.1 Data files and logical files
[gpd3.4.1]
22.1.1 Input and output data files
[gpd3.4.1.1]
22.1.2 Using the same filename twice in CMF files
[dupefilenames]
22.2 Updated data files
[gpd3.4.2]
22.2.1 Naming updated files
[gpd3.4.2.1]
22.2.2 Updated data read from the terminal
[gpd3.4.2.2]
22.2.3 Intermediate data files
[gpd3.4.2.3]
22.2.4 Long names on updated data files
[gpd3.4.2.4]
22.3 Display files
[gpd3.4.3]
22.3.1 Options for display files
[gpd3.4.3.1]
22.4 Checking set and element information when reading data
[gpd3.4.4]
22.4.1 Check-on-read problems with RunDynam and similar programs
[gpd3.4.4.1]
22.4.2 Checks when reading set element names from a file
[gpd3.4.4.2]
22.4.3 Checks on run-time elements used in TABLO input file
[gpd3.4.4.3]
22.5 Names of intermediate data files
[gpd3.4.5]
22.5.1 Default names for intermediate files when using a command file
[gpd3.4.5.1]
23 Specifying the closure
[gpd3.5.1a]
23.1 The closure
[gpd3.5.1]
23.1.1 Miniature ORANI model
[gpd3.5.1.1]
23.2 Specifying the closure via a command file
[gpd3.5.2]
23.2.1 Listing exogenous variable names and components.
[gpd3.5.2.1]
23.2.2 Closure swap statements
[gpd3.5.2.1a]
23.2.3 Order of command file statements can be important
[gpd3.5.2.4]
23.2.4 Closure specified using data files
[gpd3.5.2.5]
23.2.5 Using a saved closure
[gpd3.5.2.2]
23.2.6 List of exogenous/endogenous variables when closure is invalid
[gpd3.5.2.6]
23.2.7 Initial closure check and singular matrices
[gpd3.5.2.7]
24 Specifying the shocks
[gpd3.5.5]
24.1 Specifying simple shocks
[gpd3.5.5.1]
24.2 Reading nonuniform shocks from a file
[gpd3.5.5.2]
24.3 Using the "select from" shock statement
[gpd3.5.5.1b]
24.4 Shock components must usually be in increasing order
[gpd3.5.5.3]
24.5 When to use "select from"
[gpd9.7.17]
24.6 Other points about shocks
[gpd3.5.5.4x]
24.6.1 Using SEENV to generate shock statements
[gpd3.5.5.4seenv]
24.6.2 Shock statements using component numbers and/or lists of values
[gpd3.5.5.4b]
24.6.3 Shocking a variable with no components exogenous
[gpd3.5.5.5]
24.7 FINAL_LEVEL statements : alternatives to shock statements
[gpd3.5.6]
24.8 Shocks from a coefficient
[shcoeff]
24.8.1 Examples
[shcoeff1]
24.8.2 Motivation
[shcoeff2]
24.8.3 Formal rules
[shcoeff3]
24.8.4 Fine print
[shcoeff4]
24.9 CHANGE or PERCENT_CHANGE shock statements
[gpd3.5.7]
24.10 Rate% shock statement
[gpd5.9.16]
24.10.1 Fine print about rate% shock statements
[gpd5.9.16.1]
24.11 Shock files: fine print
[gpd3.5.8b]
24.12 Checking the closure and shocks
[gpd3.5.9]
24.13 Levels variable names can be used in command files
[gpd3.5.10]
24.14 Clarification concerning shocks on a command file
[gpd3.5.11]
24.14.1 Shock statement when only some components are exogenous
[gpd3.5.11.1]
24.14.2 At least one shock statement is required.
[gpd3.5.11.2]
25 Actions in GEMSIM and TABLO-generated programs
[gpd3.6]
25.1 Possible actions in GEMSIM and TABLO-generated programs
[gpd3.6.1]
25.1.1 Multi-step simulations with economic models
[gpd3.6.1.1]
25.1.2 Creating an equations file
[gpd3.6.1.2]
25.1.3 Other actions
[gpd3.6.1.3]
25.1.4 Data manipulation
[gpd3.6.1.4]
25.1.5 "extra" (TABLO-like) actions
[gpd3.6.1.5]
25.1.6 Checking the closure and shocks
[gpd3.6.1.6]
25.1.7 Postsim passes and actions
[gpd3.6.1.6a]
25.1.8 Controlling whether and how the actions are carried out
[gpd3.6.1.7]
25.1.9 Some reads and FORMULAS may be omitted
[gpd3.6.1.8]
25.1.10 Writes and displays at all steps of a multi-step simulation
[gpd3.6.1.9]
25.1.11 Echoing activity
[gpd3.6.1.10]
25.1.12 Writes to the terminal
[gpd3.6.1.11]
25.2 How these programs carry out multi-step simulations
[gpd3.6.2]
25.2.1 Processing the closure and shocks
[gpd3.6.2.1]
25.2.2 Results of a 4-step simulation looked at in detail
[gpd3.6.2.2]
25.2.3 Do the accurate results satify the linear equations?
[gpd3.6.2.3]
25.3 Assertions
[gpd3.6.3]
25.3.1 When an assertion fails
[gpd5.9.7]
25.3.2 Assertions, writes on preliminary pass and PostSim pass 2
[gpd5.9.8]
25.4 Range tests
[gpd3.6.4]
25.4.1 Specifying the allowed range for a coefficient or levels variable
[gpd3.6.4.1]
25.4.2 Tests carried out
[gpd3.6.4.2]
25.4.3 An example
[gpd3.6.4.3]
25.4.4 Associated statements in command files
[gpd3.6.4.4]
25.5 Transfer statements
[gpd3.6.5]
25.6 TABLO-like statements in command files
[gpd3.6.6]
25.6.1 TABLO-like checks of extra statements
[gpd3.6.6.1]
25.6.2 Qualifiers
[gpd3.6.6.2]
25.6.3 Other points
[gpd3.6.6.3]
25.7 Coefficients are fully initialised by default
[gpd3.6.7]
25.8 How accurate are arithmetic calculations?
[gpd3.6.8]
25.8.1 Example 1 - GTAPVIEW
[gpd3.6.8.1]
25.8.2 Example 2 - checking balance of ORANIG data
[gpd3.6.8.2]
26 Multi-step solution methods
[gpd3.7]
26.1 What method and how many steps to use ?
[gpd3.7.1]
26.1.1 Example - GTAP liberalization simulation
[gpd3.7.1.1]
26.1.2 Command file statements for method and steps
[gpd3.7.1.2]
26.2 Extrapolation accuracy summaries and files
[gpd3.7.2]
26.2.1 Accuracy estimates and summaries for variables
[gpd3.7.2.1]
26.2.2 Accuracy estimates and summaries for updated data
[gpd3.7.2.2]
26.2.3 Extrapolation accuracy files
[gpd3.7.2.3]
26.2.4 Accuracy summary information is on solution file
[gpd5.9.11]
26.2.5 Fine print on how extrapolation is done
[gpd5.9.10]
26.2.6 Command file statements affecting extrapolation accuracy reports
[gpd3.7.2.4]
26.3 Splitting a simulation into several subintervals
[gpd3.7.3]
26.3.1 Overall accuracy summary when more than one subinterval
[gpd3.7.3.1]
26.4 Automatic accuracy for simulations
[gpd3.7.4]
26.4.1 Specifying which solutions to use
[gpd3.7.4.1]
26.4.2 Incompatibilities
[gpd3.7.4.2]
26.4.3 Adaptive stepsize method
[gpd3.7.4.4]
26.4.4 Stopping if subintervals become too small
[gpd3.7.4.5]
26.4.5 Controlling which values are tested
[gpd3.7.4.6]
26.4.6 Checking progress during a run
[gpd3.7.4.7]
26.5 Runge-Kutta solution methods
[rungekutta]
26.5.1 Adaptive stepsize for Runge-Kutta
[adaptiverk]
26.5.2 Which RK integrator to choose?
[whichrk]
26.6 Newton's method for levels models
[gpd3.7.5]
26.6.1 Newton's method and ORANIF
[gpd3.7.5.1]
26.6.2 Convergence
[gpd3.7.5.2]
26.6.3 General advice
[gpd3.7.5.3]
26.6.4 Newton's method is not reliable with mixed models
[gpd3.7.5.4]
26.6.5 Command file statements for Newton's method
[gpd5.9.13]
26.7 Homotopy methods and levels equations
[gpd3.7.6]
26.7.1 Example 1 - solving a system of levels equations
[gpd3.7.6.1]
26.7.2 Example 2 - finding an intertemporal data set
[gpd3.7.6.2]
26.7.3 Example 3 - use when adding behaviour to a model
[gpd3.7.6.3]
26.7.4 Formal documentation about ADD_HOMOTOPY
[gpd3.7.6.4]
26.7.5 Names for homotopy variables added to levels equations
[gpd5.8.6]
26.7.6 ADD_HOMOTOPY and NOT_ADD_HOMOTOPY default statements
[gpd3.7.6.5]
26.8 Options for saving solution and updated data files
[gpd3.7.7]
26.8.1 Saving solutions or updated data after each multi-step calculation
[gpd3.7.7.1]
26.8.2 Saving updated values from all FORMULA(INITIAL)s
[gpd3.7.7.2]
26.9 Solutions report perturbations of the initial values
[gpd3.7.8]
26.9.1 Change differentiation keeps a constant error
[gpd3.7.8.1]
26.9.2 How can homotopies help?
[gpd3.7.8.2]
27 Solution (SL4) files
[gpd3.8]
27.1 Command file statements related to solution files
[gpd3.8.1]
27.2 Contents of solution files
[gpd3.8.2]
27.2.1 TAB and STI files stored on solution file
[gpd3.8.2.1]
27.2.2 Command file stored on solution file
[gpd3.8.2.2]
27.3 Displaying Levels results
[gpd3.8.3]
27.3.1 Levels results in ViewSOL for change linear variables
[gpd5.9.3]
27.4 SEQ files
[seqfiles]
28 SLC, UDC, AVC and CVL files
[slcfiles]
28.1 Solution coefficients (SLC) files
[gpd3.8.4]
28.1.1 Solution and SLC files are complete record of the simulation
[gpd3.8.4.1]
28.1.2 SLC files may contain updated values
[gpd5.9.5.1]
28.1.3 SLC, UDC and AVC files contain values of PostSim coefficients
[gpd5.9.5.3]
28.1.4 System-initiated coefficients on SLC file
[gpd9.7.21.1]
28.2 Updated and average coefficient values (UDC and AVC) files
[gpd3.8.5]
28.2.1 How values on UDC files are calculated
[gpd3.8.5.1]
28.2.2 Presim values calculated from, yet different to, the updated data
[gpd3.8.5.2]
28.2.3 Are values on UDC files different from those in updated data?
[gpd3.8.5.3]
28.3 Coefficient values (CVL) files from data manipulation TAB files
[gpd3.8.6]
28.3.1 Coefficient values (CVL) files for analysing why a simulation crashes
[gpd3.8.7]
29 Subtotals via GEMSIM or TABLO-generated programs
[gpd3.11]
29.1 Subtotals from GEMSIM and TABLO-generated programs
[gpd3.11.1]
29.2 Meaning of subtotals results
[gpd3.11.2]
29.3 Subtotal example
[gpd3.11.3]
29.4 More substantial examples
[gpd3.11.4]
29.5 Processing subtotal results
[gpd3.11.5]
29.6 Subtotals results depend on the path
[gpd3.11.6]
29.6.1 Example showing how the path can affect subtotals results
[gpd3.11.6.1]
29.6.2 Subtotal commands which include (partially) endogenous variables
[endogsubtot]
30 Solving models and simulation time
[gpd3.12]
30.1 How GEMPACK programs solve linear equations
[gpd3.12.1]
30.1.1 GEMPACK 12 LU factorization
[gp12lu]
30.1.2 Sparse-linear-equation solving routines MA48 and MA28
[gpd3.12.1.1]
30.1.3 Which to use?  MA48 or MA28
[gpd3.12.1.2]
30.1.4 Accuracy warnings from iterative refinement
[gpd9.7.6]
30.1.5 Iterative refinement and residual ratios
[itref2]
30.2 Gragg's method and the midpoint method
[gpd3.12.2]
30.3 Reusing pivots
[gpd3.12.3]
30.4 Ignoring/keeping zero coefficients
[gpd3.12.5]
30.4.1 More details about the "iz1=no" option
[gpd3.12.5a]
30.5 LU decomposition
[gpd5.5]
30.5.1 Memory for LU decomposition in simulations
[gpd5.5.1]
30.6 Equation solving problems
[gpd3.12.6]
30.6.1 Warnings about equations not being satisfied very accurately
[gpd3.12.6.1]
30.6.2 Warnings about variation between passes in endogenous results
[gpd3.12.6.2]
30.6.3 Gragg and midpoint are not suitable in some cases
[gpd3.12.6.3]
30.7 Work files
[gpd3.12.7]
31 Solving a model in parallel on a machine with two or more processors
[gpd9.2]
31.1 You need plenty of memory
[gpd9.2.1]
31.2 Telling the program to run in parallel
[gpd9.2.2]
31.2.1 Problems with the program deciding how many servants
[gpd9.2.2.1]
31.3 Restrictions
[gpd9.2.3]
31.4 Servants work in their own directories
[gpd9.2.4]
31.5 Master log file is complete
[gpd9.2.5]
31.6 When the servants start and finish
[gpd9.2.6]
31.6.1 If there are several subintervals
[gpd9.2.6.1]
31.6.2 If there are complementarity statements
[gpd9.2.6.2]
31.6.3 If using automatic accuracy
[gpd9.2.6.3]
31.7 If a fatal error occurs
[gpd9.2.7]
31.8 Fine print
[gpd9.2.8]
31.8.1 Displays and writes to terminal at all steps
[gpd9.2.8.1]
31.8.2 Multi-step calculations may not be independent of each other
[gpd9.2.8.2]
31.9 Some elapsed times
[gpd9.2.9]
31.9.1 Comments on the elapsed times reported
[gpd9.2.9.1]
31.10 Using master/servant under RunDynam
[gpd9.2.10]
32 Memory management
[gpd3.13]
32.1 Automatic memory allocation
[gpd3.13.1]
32.2 Preliminary pass
[gpd3.13.2]
32.3 MMNZ: Allocating memory for the LU decomposition
[gpd3.13.3]
32.4 Reporting memory used by TABLO-generated programs and GEMSIM
[gpd3.13.4]
32.4.1 RunDynam manages MMNZ start values
[rundynam.mmnz]
32.4.2 TGMEM1 and TGMEM2 parts of memory
[gpd3.13.4.1]
33 Options for GEMSIM and TABLO-generated programs
[gpd3.14]
33.1 Options affecting simulations
[gpd3.14.1]
33.2 Options affecting extrapolation accuracy summaries and files
[gpd3.14.2]
33.3 Saving updated values from all FORMULA(INITIAL)s
[gpd3.14.3]
33.4 Options affecting the actions carried out
[gpd3.14.4]
33.5 Options affecting how writes and displays are carried out
[gpd3.14.5]
33.6 Options affecting CPU and activity reporting
[gpd3.14.6]
33.7 Special options for SAGEM
[gpd3.14.7]
33.7.1 SAGEM options
[gpd3.14.7.1]
34 Run-time errors
[gpd3.15]
34.1 Simulation fails because of a singular LHS matrix
[gpd3.15.1]
34.1.1 Trying to fix a singular matrix problem
[gpd3.15.1.1]
34.2 Structurally singular matrices
[gpd3.15.2]
34.2.1 Solving modified equations when LHS matrix is structurally singular
[gpd3.15.2.1]
34.3 Reporting arithmetic errors
[gpd9.7.4]
34.3.1 Updates -- fine print
[gpd9.7.4.1]
34.3.2 Other arithmetic errors
[gpd9.7.4.2]
34.4 Suppressing arithmetic errors in GEMSIM and TABLO-generated programs
[gpd5.9.15]
35 Summary of command file statements
[gpd3.18]
35.1 Command files for GEMSIM and TABLO-generated programs
[gpd3.18.1]
35.2 Command file statements
[gpd3.18.2]
35.2.1 Method and steps
[gpd3.18.2.1]
35.2.2 Checking set and element labelling when reading data from HAR files
[gpd3.18.2.2]
35.2.3 Checking element names when reading sets from HAR files
[gpd3.18.2.3]
35.2.4 Automatic accuracy
[gpd3.18.2.4]
35.2.5 Data files
[gpd3.18.2.5]
35.2.6 Equations files and BCV files
[gpd3.18.2.6]
35.2.7 Other files
[gpd3.18.2.7]
35.2.8 TABLO-like statements in command files
[gpd3.18.2.8]
35.2.9 Closure related
[gpd3.18.2.9]
35.2.10 Harwell parameter
[gpd3.18.2.10]
35.2.11 Verbal description
[gpd3.18.2.11]
35.2.12 Shock related
[gpd3.18.2.12]
35.2.13 Cumulatively-retained rows
[gpd3.18.2.13]
35.2.14 Variables on extrapolation accuracy file
[gpd3.18.2.14]
35.2.15 Subtotals
[gpd3.18.2.15]
35.2.16 Complementarity
[gpd3.18.2.16]
35.2.17 LU decomposition and advanced use of pivots
[cmfsum.pivots]
35.2.18 Newton's Method
[cmfsum.newton]
35.2.19 Memory management
[cmfsum.sharemem]
35.2.20 GEMSIM and TABLO-generated program options
[gpd3.18.2.17]
35.2.21 Automatic Homogeneity Testing
[cmfautohomog]
35.2.22 For debugging
[gpd3.18.2.18]
35.2.23 General points
[gpd3.18.2.19]
35.3 Complete command file example for GEMSIM and TABLO-generated programs
[gpd3.18.3]
35.4 Command files for SAGEM
[gpd3.18.4]
35.5 Command file statements for SAGEM
[sagem.cmfs]
35.5.1 Equations file, Solution file and Harwell Parameter
[gpd3.18.4.1]
35.5.2 Verbal description      (mandatory)
[gpd3.18.4.2]
35.5.3 Closure related
[gpd3.18.4.3]
35.5.4 Shock related
[gpd3.18.4.4]
35.5.5 Individually-retained and cumulatively-retained rows/columns
[gpd3.18.4.5]
35.5.6 Subtotals
[gpd3.18.4.6]
35.5.7 SAGEM options
[gpd3.18.4.7]
35.5.8 General points
[gpd3.18.4.8]
35.6 Complete command file example for SAGEM
[gpd3.18.5]
36 GEMPACK Windows programs
[gpd4.2]
36.1 WinGEM -- the Windows interface to GEMPACK
[gpd4.2.1]
36.2 ViewHAR for looking at or modifying data on a header array file
[gpd4.2.2]
36.2.1 The Charter
[gpd4.2.2.1]
36.3 ViewSOL for looking at simulation results on a solution file
[gpd4.2.3]
36.4 TABmate for working on TABLO input files or command files
[gpd4.2.4]
36.5 RunGEM for model users
[gpd4.2.5]
36.5.1 TABmate and RunGEM for model developers?
[gpd4.2.5.1]
36.5.2 Preparing a model for use with RunGEM
[gpd4.2.5.2]
36.5.3 Systematic sensitivity analysis via RunGEM
[gpd4.2.5.3]
36.5.4 Systematic sensitivity analysis
[gpd4.2.5.4]
36.6 AnalyseGE -- assisting in the analysis of simulation results
[gpd4.2.6]
36.6.1 Using AnalyseGE with data manipulation TAB files
[gpd4.2.6.1]
36.6.2 Using AnalyseGE when a simulation crashes
[gpd4.2.6.2]
36.6.3 Subtotals in AnalyseGE
[gpd5.6.1]
36.6.4 Decomposing selected expression
[gpd5.6.2]
36.6.5 Analysing closure problems with AnalyseGE
[anal-clos]
36.7 RunDynam for recursive dynamic models
[gpd4.2.7]
37 Command-line programs for working with header array files
[gpd4.4]
37.1 SEEHAR:  prepare a print file or CSV spreadsheet file
[gpd4.4.1]
37.1.1 SEEHAR - options
[gpd4.4.1.1]
37.1.2 Displays and labelled output from SEEHAR into spreadsheets
[gpd4.4.1.2]
37.1.3 GAMS output from SEEHAR, TABLO-generated programs and GEMSIM
[gpd4.4.1.3]
37.1.4 Converting header array files to data bases - SEEHAR option SQL
[gpd4.4.1.4]
37.1.5 SEEHAR command-line options
[seehar12]
37.2 CMPHAR: comparing data on header array files
[gpd4.4.2]
37.2.1 CMPHAR report
[gpd4.4.2.1]
37.2.2 Significant differences
[gpd4.4.2.2]
37.2.3 Comparing solution files
[gpd4.4.2.3]
37.2.4 CMPHAR files on the command line
[gpd5.10.1.4]
37.2.5 CMPHAR reports difference metric values
[gpd5.10.5]
37.3 CMBHAR: combining similar header array files
[gpd4.4.4]
37.3.1 CMBHAR for accumulating or differencing timeseries of solutions
[cmbharaccum]
37.3.2 SplitHAR to reverse the action of CMBHAR
[splithar]
37.4 SUMHAR: summarising a header array file
[gpd4.4.3]
37.4.1 SUMHAR command-line options
[sumhar12]
37.5 MergeHAR: combining headers from two HAR files into one
[mergehar]
37.6 DiffHAR: compare two header or SL4 files
[diffhar]
37.7 DumpSets: extract sets from HAR file
[dumpsets]
38 Syntax of GEMPACK text data files
[gpd4.6]
38.1 The "how much data" information
[gpd4.6.1]
38.1.1 Real or integer data
[gpd4.6.1.1]
38.1.2 Examples of "how much data" information
[gpd4.6.1.2]
38.1.3 Character string data
[gpd4.6.1.3]
38.1.4 Header and longname
[gpd4.6.1.4]
38.1.5 Coefficient
[gpd4.6.1.5]
38.1.6 Comments
[gpd4.6.1.6]
38.1.7 Complete example of GEMPACK text data file
[gpd4.6.1.7]
38.2 Data values in text files
[gpd4.6.2]
38.2.1 Array sizes
[gpd4.6.2.1]
38.2.2 Actual data values of the array
[gpd4.6.2.2]
38.2.3 Row order
[gpd4.6.2.3]
38.2.4 Column order
[gpd4.6.2.4]
38.2.5 Spreadsheet order
[gpd4.6.2.5]
38.2.6 Real numbers
[gpd4.6.2.6]
38.2.7 Repeated values in arrays
[gpd4.6.2.7]
38.2.8 Character strings
[gpd4.6.2.8]
38.2.9 Multi-dimensional real arrays
[gpd4.6.2.9]
38.2.10 Maximum length of lines of a file
[gpd4.6.2.10]
38.2.11 Differences between row order and spreadsheet style data
[gpd4.6.2.11]
38.2.12 Text editors and text files
[gpd4.6.2.12]
38.2.13 Advice for CSV files
[gpd4.6.2.13]
38.2.14 Element name/number labels
[gpd4.6.2.14]
38.3 Using TABLO to read, manipulate, and write HAR or text files
[gpd1.4.4]
39 SLTOHT: processing simulation results
[gpd4.8]
39.1 Introducing SLTOHT
[gpd4.8.1]
39.1.1 Ways to run SLTOHT
[runningsltoht]
39.2 Using SLTOHT to make a HAR file
[sltohthar]
39.2.1 Totals solution to HAR file using SLTOHT from WinGEM
[gpd4.8.2.1]
39.2.2 Cumulative + levels solution to HAR file via WinGEM
[gpd4.8.2.3]
39.2.3 Subtotals + cumulative solution to HAR file
[gpd4.8.2.4]
39.3 Mapping files
[gpd4.8.3]
39.3.1 Header mapping file
[gpd4.8.6.1]
39.4 Running SLTOHT from the command line
[gpd5.10.1.3]
39.5 Running SLTOHT interactively
[gpd4.8.4]
39.5.1 Choosing solutions for output
[gpd4.8.4.1]
39.6 Undefined solution values
[gpd4.8.4.2]
39.7 Levels results - options NLV, LV and SHL
[gpd4.8.5]
39.8 How SLTOHT arranges several solutions in HAR file output
[gpd4.8.6]
39.9 GEMPACK text data file output using options SIR, SIC or SS
[gpd4.8.7]
39.10 Other SLTOHT options
[gpd4.8.9]
39.10.1 SLTOHT option VAI: variable arguments ignored in HAR output
[gpd4.8.6.2]
39.10.2 SLTOHT option NEL
[gpd4.8.9nel]
39.10.3 SLTOHT option SEP
[gpd4.8.9sep]
39.10.4 SLTOHT option HSS: produce both HAR and spreadsheet outputs
[gpd4.8.9hss]
39.10.5 SLTOHT option SHK: shock CMF output
[gpd4.8.8]
39.10.6 SLTOHT option DES
[gpd4.8.9des]
40 SLTOHT for spreadsheets
[gpd4.9]
40.0.1 WinGEM example: Totals solution to CSV file for spreadsheet (SES)
[gpd4.8.2.2]
40.1 Spreadsheet mapping files
[gpd4.9.1]
40.1.1 Example of a spreadsheet mapping file (option SSS)
[gpd4.8.3.1]
40.1.2 Syntax rules for spreadsheet mapping files
[gpd4.9.1.1]
40.2 Options spreadsheet (SS) and short spreadsheet (SSS)
[gpd4.9.2]
40.2.1 Component numbers rather than element names (SS or SSS)
[gpd4.9.2.1]
40.3 Output of tables using options SES or SSE
[gpd4.9.3]
40.3.1 Output of levels results using option SES
[gpd4.9.3.1]
40.3.2 Three and higher dimensional arrays of results
[gpd4.9.3.2]
40.4 Side-by-side results (SES, SS, SSS or SSE output)
[gpd4.9.4]
40.5 Tables suitable for producing graphs
[gpd4.9.5]
41 ACCUM and DEVIA : accumulation and differences
[gpd4.10]
41.1 Use with dynamic forecasting models
[gpd4.10.1]
41.1.1 Using ACCUM to prepare a spreadsheet table for the forecast
[gpd4.10.1.1]
41.2 ACCUM
[gpd4.10.2]
41.2.1 Columns showing totals and averages
[gpd4.10.2.1]
41.2.2 Year-on-year results or accumulated results (option ACC)
[gpd4.10.2.2]
41.2.3 Accumulated indexes (option ACI)
[gpd4.10.2.3]
41.2.4 Handling subtotals results in ACCUM
[gpd4.10.2.4]
41.3 Using DEVIA to prepare a spreadsheet table for the differences
[gpd4.10.3]
41.3.1 Making sure DEVIA knows change/percent-change variables (option SOL)
[gpd4.10.3.1]
41.3.2 Year-on-year differences (option NAC)
[gpd4.10.3.2]
41.3.3 Subtotals results in DEVIA
[gpd4.10.3.3]
41.3.4 Do subtotals for policy shocks add up to the policy deviation?
[dyndevsubtot]
41.4 Suppressing arithmetic errors in ACCUM, DEVIA and CMBHAR
[gpd5.10.3]
42 Hands-on tutorials for models supplied with GEMPACK
[gpd8.1]
42.1 Overview of chapters 43 to 46
[gpd8.1b]
43 Getting started with GEMPACK via WinGEM
[gpd8.2]
43.1 GEMPACK examples for new users
[gpd8.2.1]
43.2 Locating the example files
[gpd8.2.2]
43.2.1 Editing text files in WinGEM
[gpd8.2.2.1]
43.3 Examples using the Stylized Johansen model SJ
[gpd8.2.4]
43.3.1 Starting WinGEM
[gpd8.2.4.1]
43.3.2 Preparing a directory for model SJ
[gpd8.2.4.2]
43.3.3 Setting the working directory
[gpd8.2.4.3]
43.3.4 Looking at the data directly using ViewHAR
[gpd8.2.4.4]
43.3.5 TABLO-generated program or GEMSIM?
[gpd8.2.4.5]
43.3.6 The example simulation using a TABLO-generated program
[gpd8.2.4.6]
43.3.7 The example simulation using GEMSIM
[gpd8.2.4.7]
43.3.8 Source-code version : use GEMSIM or TABLO-generated program?
[gpd8.2.4.8]
43.3.9 The updated data -- another result of the simulation
[gpd8.2.4.9]
43.3.10 Several Johansen simulations
[gpd8.2.4.10]
43.3.11 Changing the closure and shocks
[gpd8.2.4.11]
43.3.12 Correcting errors in TABLO input files
[gpd8.2.4.12]
43.3.13 Creating the base data header array file
[gpd8.2.4.13]
43.3.14 Modifying data on a header array file
[gpd8.2.4.14]
43.3.15 Condensing the model
[gpd8.2.4.15]
43.3.16 Transferring simulation results to a spreadsheet using SLTOHT
[gpd8.2.4.16]
43.3.17 Using SEEHAR to look at data
[gpd8.2.4.17]
43.3.18 Analysing simulation results using AnalyseGE
[gpd8.2.4.18]
43.3.19 What next ?
[gpd8.2.4.19]
43.4 Miniature ORANI model examples
[gpd8.2.5]
43.4.1 Preparing a directory for model MO
[gpd8.2.5.1]
43.4.2 Set the working directory
[gpd8.2.5.2]
43.4.3 Examine the database for MO
[gpd8.2.5.3]
43.4.4 Implementing the model MO using TABLO
[gpd8.2.5.4]
43.4.5 Simulation using the command file MOTAR.CMF
[gpd8.2.5.5]
43.4.6 Several Johansen simulations using SAGEM
[gpd8.2.5.6]
43.4.7 Homogeneity test using SAGEM
[gpd8.2.5.7]
43.4.8 Modifying the closure for MO
[gpd8.2.5.8]
43.5 Examples for global trade analysis Project model GTAP94
[gpd8.2.6]
43.5.1 Examining the GTAP data directly
[gpd8.2.6.1]
43.5.2 A GTAP3x3 simulation reducing one distortion
[gpd8.2.6.2]
43.5.3 Implementation of GTAP3x3
[gpd8.2.6.3]
43.5.4 Running a simulation with condensed GTAP3x3
[gpd8.2.6.4]
43.5.5 GTAP multi-fibre agreement simulation with a 10x10 aggregation
[gpd8.2.6.5]
43.5.6 Implementation of GTAP1010
[gpd8.2.6.6]
43.5.7 Running a simulation with condensed GTAP1010
[gpd8.2.6.7]
43.5.8 Running ViewSOL to look at the results
[gpd8.2.6.8]
43.5.9 Comparison of times for GEMSIM and TG program
[gpd8.2.6.9]
43.5.10 GTAP APEC liberalization (including results decomposition)
[gpd8.2.6.10]
43.5.11 Carrying out the APEC liberalization simulation (with subtotals)
[gpd8.2.6.11]
43.5.12 Looking at the results via ViewSOL
[gpd8.2.6.12]
43.6 Examples for global trade analysis Project model GTAP61
[gpd8.2.7]
43.6.1 Preparing a directory for model GTAP61
[gpd8.2.7.1]
43.6.2 Set the working directory
[gpd8.2.7.2]
43.6.3 Examine the TAB file
[gpd8.2.7.3]
43.6.4 View the data files for GTAP61
[gpd8.2.7.4]
43.6.5 Implement the model using TABLO
[gpd8.2.7.5]
43.6.6 Running a simulation with condensed GTAP61
[gpd8.2.7.6]
43.7 Examples with the ORANIG98 model
[gpd8.2.8]
43.7.1 Preparing a directory for model ORANIG98
[gpd8.2.8.1]
43.7.2 Set the working directory
[gpd8.2.8.2]
43.7.3 Examine the TAB file and the data
[gpd8.2.8.3]
43.7.4 Implement the model using TABLO
[gpd8.2.8.4]
43.7.5 Running a simulation with condensed ORANIG98
[gpd8.2.8.5]
43.7.6 Comparison of times for GEMSIM and TG program
[gpd8.2.8.6]
43.7.7 Decomposition of simulation results
[gpd8.2.8.7]
43.8 Examples with the ORANIG01 model
[gpd8.2.9]
43.8.1 Preparing a directory for model ORANIG01
[gpd8.2.9.1]
43.8.2 Set the working directory
[gpd8.2.9.2]
43.8.3 Examine the TAB file and data
[gpd8.2.9.3]
43.8.4 Implement the model using TABLO
[gpd8.2.9.4]
43.8.5 Running simulations with ORANIG01
[gpd8.2.9.5]
43.9 Examples with the ORANIF model
[gpd8.2.10]
43.9.1 Preparing a directory for model ORANIF
[gpd8.2.10.1]
43.9.2 Set the working directory
[gpd8.2.10.2]
43.9.3 Examine the TAB file and the data
[gpd8.2.10.3]
43.9.4 Implement the model using TABLO
[gpd8.2.10.4]
43.9.5 Running a simulation with condensed ORANIF
[gpd8.2.10.5]
43.9.6 Comparison of times for GEMSIM and TG program
[gpd8.2.10.6]
43.10 Other example models
[gpd8.2.11]
43.11 Building your own models
[gpd8.2.12]
43.12 Using RunGEM for simulations
[gpd8.2.13]
44 Command prompt: hands-on computing
[gpd8.3]
44.1 Examples using the Stylized Johansen model SJ
[gpd8.3.1]
44.1.1 Preparing a directory for model SJ
[gpd8.3.1.1]
44.1.2 Looking at the data directly
[gpd8.3.1.2]
44.1.3 An example simulation with Stylized Johansen
[gpd8.3.1.3]
44.1.4 The example simulation using a TABLO-generated program
[gpd8.3.1.4]
44.1.5 The example simulation using GEMSIM
[gpd8.3.1.5]
44.1.6 Source-code version : use GEMSIM or TABLO-generated program?
[gpd8.3.1.6]
44.1.7 The updated data - another result of the simulation
[gpd8.3.1.7]
44.1.8 Preparing tables and graphs for a report
[gpd8.3.1.8]
44.1.9 Changing the closure and shocks
[gpd8.3.1.9]
44.1.10 Several simulations using SAGEM
[gpd8.3.1.10]
44.1.11 Condensing the model
[gpd8.3.1.13]
44.2 Miniature ORANI model examples
[gpd8.3.2]
44.2.1 Preparing a directory for model MO
[gpd8.3.2.1]
44.2.2 Implementation of the model MO using TABLO
[gpd8.3.2.2]
44.2.3 Simulation using the TABLO-generated program MO (or GEMSIM)
[gpd8.3.2.3]
44.2.4 Several simulations at once with SAGEM
[gpd8.3.2.4]
44.2.5 Homogeneity test using SAGEM
[gpd8.3.2.5]
44.2.6 Modifying a closure
[gpd8.3.2.6]
44.3 Other models supplied
[gpd8.3.3]
44.4 Working with TABLO input files
[gpd8.3.4]
45 Using RunGEM for simulations
[gpd8.5]
45.1 Stylized Johansen
[gpd8.5.1]
45.1.1 Preparing the model files for RunGEM
[gpd8.5.1.1]
45.1.2 Starting RunGEM
[gpd8.5.1.2]
45.1.3 Modifying the closure and shocks
[gpd8.5.1.3]
45.2 ORANIG98 model
[gpd8.5.2]
45.2.1 Prepare the model files for RunGEM
[gpd8.5.2.1]
45.2.2 Starting RunGEM
[gpd8.5.2.2]
45.2.3 Wage cut simulation
[gpd8.5.2.3]
45.2.4 Long run simulation
[gpd8.5.2.4]
45.3 Preparing models for use by others with RunGEM
[gpd8.5.3]
45.4 TABmate + RunGEM
[gpd8.5.4]
45.5 RunGEM for students
[gpd8.5.5]
46 Using AnalyseGE to analyse simulation results
[gpd8.6]
46.1 Analysing a Stylized Johansen simulation
[gpd8.6.1]
46.1.1 Starting AnalyseGE
[gpd8.6.1.1]
46.1.2 Looking at the shocks for the simulation
[gpd8.6.1.2]
46.1.3 Real GDP in Stylized Johansen
[gpd8.6.1.3]
46.1.4 What happens to real GDP from the income side?
[gpd8.6.1.4]
46.1.5 Summary of real GDP analysis from income side
[gpd8.6.1.5]
46.1.6 Real GPD from the income side via equation E_realva
[gpd8.6.1.6]
46.1.7 Real GDP from the expenditure side
[gpd8.6.1.7]
46.1.8 Demand for factors in each sector - A first look
[gpd8.6.1.8]
46.1.9 What happens to the prices of labor and capital?
[gpd8.6.1.9]
46.1.10 Demand for factors in each sector - A final look
[gpd8.6.1.10]
46.1.11 Prices of the factors again
[gpd8.6.1.11]
46.1.12 What happens to the prices of the commodities?
[gpd8.6.1.12]
46.1.13 What happens to household demand for the commodities?
[gpd8.6.1.13]
46.1.14 What happens to total demand for the commodities?
[gpd8.6.1.14]
46.1.15 Results for factor prices - why opposite signs?
[gpd8.6.1.15]
46.1.16 Conclusion
[gpd8.6.1.16]
46.1.17 Proof that real GDP and price indices are equal from both sides
[gpd8.6.1.17]
46.2 What next ?
[gpd8.6.2]
47 Print edition ends here
[endprint]
48 Working with GEMPACK command-line programs
[gpd1.5]
48.1 Responding to prompts
[gpd1.5.1]
48.1.1 Responding to prompts (upper case or lower case)
[gpd1.5.1.1]
48.1.2 Default response to questions and prompts
[gpd1.5.1.2]
48.1.3 How the current directory affects filename responses
[gpd1.5.1.3]
48.1.4 How the current directory affects filenames in command files
[gpd1.5.1.4]
48.1.5 Directories must already exist
[gpd1.5.1.5]
48.1.6 GEMPACK programs echo current directory
[gpd1.5.1.6]
48.2 Comments in input from the terminal
[gpd1.5.2]
48.3 Interactive and batch operation, stored-input and log files
[gpd1.5.3]
48.3.1 Invalid input when using options 'sif' or 'asi'
[gpd1.5.3.1]
48.3.2 Differences between batch and interactive program dialogues
[gpd1.5.3.2]
48.3.3 Terminal output and log files
[gpd1.5.3.3]
48.3.4 Interrupting command-line programs
[gpd6.7.1.4]
48.3.5 Controlling screen output from command-line programs
[gpd6.7.1.5]
48.3.6 LOG files and early errors
[gpd1.5.3.4]
48.4 Other program options
[gpd1.5.4]
48.4.1 Other options common to all programs
[gpd1.5.4.1]
48.4.2 Options specific to different programs
[gpd1.5.4.2]
48.5 Specifying various files on the command line
[gpd1.5.5]
48.5.1 command-line option "-los" (alternative to "-lon")
[gpd1.5.5.1]
48.5.2 command-line option "-lic" to specify the GEMPACK licence
[gpd1.5.5.2]
48.5.3 Abbreviations for LOG file name on command line
[gpd1.5.5.3]
48.5.4 The command line with other programs
[gpd5.10.1.2a]
49 Miscellaneous information
[miscstuff]
49.1 Details about file creation information
[gpd9.7.5]
49.2 Programs report elapsed time
[gpd9.7.2]
49.3 Windows PCs, Fortran compilers and memory management
[gpd1.5.6]
49.3.1 64-bit processors and operating systems on PCs
[gpd9.4]
49.3.2 Large-Address-Aware (LAA) programs
[laa-exe]
49.3.3 Memory limits with Release 11/12 of GEMPACK
[gpd9.4.1]
49.3.4 Other size limits
[gpd9.4.1.1]
49.3.5 Limits for GEMSIM
[gpd9.4.1.2]
49.4 Error messages
[gpd1.5.7]
49.5 Programs set exit status
[gpd9.7.20.2]
50 Code options when running TABLO
[gpd2.5]
50.0.1 Code options in TABLO affecting the possible actions
[gpd2.5.1.1]
50.0.2 Code option in TABLO affecting compilation speed
[gpd2.5.1.2]
50.0.3 Other code options in TABLO
[gpd2.5.1.4]
51 Simulations for models with complementarities
[gpd3.16]
51.1 The basic ideas
[gpd3.16.1]
51.1.1 If only we knew the post-simulation states
[gpd3.16.1.1]
51.1.2 Finding the post-simulation states
[gpd3.16.1.2]
51.1.3 Combining the two ideas
[gpd3.16.1.3]
51.2 States of the complementarity
[gpd3.16.2]
51.2.1 Complementarities with only one bound
[gpd3.16.2.1]
51.3 Writing the TABLO code for complementarities
[gpd3.16.3]
51.3.1 Import quota example
[gpd3.16.3.1]
51.3.2 Example: MOIQ (miniature ORANI with import quotas)
[gpd3.16.3.2]
51.3.3 Specifying bounds for the complementarity variable
[gpd3.16.3.3]
51.3.4 Scale the complementarity expression if possible
[gpd3.16.3.4]
51.3.5 Levels variables are required
[gpd3.16.3.5]
51.3.6 Complementarities are related to MAX and MIN
[gpd3.16.3.6]
51.3.7 Equivalent ways of expressing complementarities with a single bound
[gpd3.16.3.7]
51.4 Hands-on examples with MOIQ
[gpd3.16.4]
51.4.1 Decreasing a quota volume - command file MOIQ1C.CMF
[gpd3.16.4.1]
51.4.2 Decreasing both quota volumes - command file MOIQ1D.CMF
[gpd3.16.4.2]
51.4.3 No approximate run - command file MOIQ1CX.CMF
[gpd3.16.4.3]
51.5 Other features of complementarity simulations
[gpd3.16.5]
51.5.1 Closure and shocks
[gpd3.16.5.1]
51.5.2 Running TABLO and simulations
[gpd3.16.5.2]
51.5.3 Program reports state changes
[gpd3.16.5.3]
51.5.4 Program checks states and bounds at end of run
[gpd3.16.5.4]
51.5.5 Checking the simulation results
[gpd3.16.5.5]
51.5.6 Omitting the accurate run
[gpd3.16.5.6]
51.5.7 Subtotals when there are complementarities
[gpd3.16.5.6a]
51.6 Command file statements for complementarity simulations
[gpd3.16.6]
51.7 Technical details about complementarity simulations
[gpd3.16.7]
51.7.1 How the closure and shocks change for the accurate simulation
[gpd3.16.7.1]
51.7.2 Extra variables introduced with each complementarity
[gpd3.16.7.2]
51.7.3 Step may be redone during approximate run
[gpd3.16.7.3]
51.7.4 Several subintervals and automatic accuracy
[gpd3.16.7.4]
51.7.5 Checks that the pre- and post-simulation states are accurate
[gpd3.16.7.5]
51.8 Complementarity examples
[gpd3.16.8]
51.8.1 Example: MOIQ (miniature ORANI with import quotas)
[gpd3.16.8.1]
51.8.2 Example: MOTRQ (miniature ORANI with tariff-rate quotas)
[gpd3.16.8.2]
51.8.3 Example: MOTR2 (alternative COMPLEMENTARITY statement)
[gpd3.16.8.3]
51.8.4 Example: G5BTRQ (GTAP with bilateral tariff-rate quotas)
[gpd3.16.8.4]
51.8.5 Alternative form of the complementarity - G5BTR2.TAB
[gpd3.16.8.5]
51.8.6 Example: G5GTRQ (GTAP with global and bilateral trqs)
[gpd3.16.8.6]
51.8.7 Example: G94-XQ (GTAP94 with bilateral export quotas)
[gpd3.16.8.7]
51.8.8 Example: G94-IQ (GTAP94 with bilateral import quotas)
[gpd3.16.8.8]
51.9 Piecewise linear functions via complementarities
[gpd3.16.9]
51.9.1 Max and min
[gpd3.16.9.1]
51.9.2 Progressive income tax schedule
[gpd3.16.9.2]
51.9.3 Other piecewise linear functions
[gpd3.16.9.3]
51.10 Example: ORANIGRD (ensuring investment stays non-negative)
[gpd3.16.10]
51.10.1 OGRD1.TAB and negative investment
[gpd3.16.10.1]
51.10.2 OGRD2.TAB - A complementarity to ensure non-negative investment
[gpd3.16.10.2]
51.11 Complementarities - speeding up single Euler calculations
[gpd9.7.18]
51.11.1 Accuracy of approximate and accurate runs using Euler
[gpd9.7.18.1]
52 Subtotals with complementarity statements
[gpd5.7]
52.1 Telling the software when to calculate subtotals
[gpd5.7.1]
52.2 Calculating subtotals on the approximate run - recommended
[gpd5.7.2]
52.2.1 Decomposed results do not sum to accurate cumulative solution
[gpd5.7.2.1]
52.3 Calculating subtotals on the accurate run - not recommended
[gpd5.7.3]
52.3.1 Decomposing accurate - include extra variables in subtotals
[gpd5.7.3.1]
52.4 Examples: MOIQ3.CMF and related simulations
[gpd5.7.4]
52.4.1 Example: MOIQ3AC.CMF simulation
[gpd5.7.4.1]
52.4.2 Several subintervals
[gpd5.7.4.2]
52.4.3 MOIQ3.CMF subtotals calculated during approximate run
[gpd5.7.4.3]
52.4.4 MOIQ3AC.CMF subtotals calculated during accurate run (not recommended)
[gpd5.7.4.4]
52.4.5 Subtotals from accurate run not robust
[gpd5.7.4.5]
52.4.6 Subtotals from approximate run are robust
[gpd5.7.4.6]
52.4.7 The initial closure is shown on solution files
[gpd5.7.4.7]
52.5 Variables with no components exogenous allowed in subtotals
[gpd5.7.5]
53 More examples of post-simulation processing
[postsim2]
53.1 Examples -- summaries of the updated data
[gpd5.2.1]
53.1.1 Adding some PostSim processing to ORANIG03.TAB
[gpd5.2.1.1]
53.1.2 ORANIG03 -- table of winning and losing industries
[gpd5.2.2.3]
53.1.3 Adding some PostSim processing to GTAP61.TAB
[gpd5.2.1.2]
53.1.4 New file can contain both the original and updated data
[gpd5.2.1.3]
53.2 Examples -- post-simulation processing of variable results
[gpd5.2.2]
53.2.1 GTAP -- table of important regional results
[gpd5.2.2.1]
53.2.2 TERM -- table of important regional results
[gpd5.2.2.2]
53.2.3 ORANIG03 -- tariff cut simulation results
[gpd5.2.2.4]
53.3 Sophisticated post-simulation processing
[gpd5.2.3]
53.3.1 GTAP -- sophisticated post-simulation processing in DECOMP.TAB
[gpd5.2.3.1]
53.3.2 Example -- SJPS.TAB and SJPSLB.CMF
[gpd5.2.8.1]
53.3.3 Other examples
[gpd5.2.8.2]
54 Using MODHAR to create or modify header array files
[gpd4.3]
54.1 An overview of the use of MODHAR
[gpd4.3.3]
54.1.1 Creating a new header array file
[gpd4.3.3.1]
54.2 Modifying an existing header array file
[gpd4.3.4]
54.2.1 Adding arrays from other files using MODHAR
[gpd4.3.4.1]
54.3 Using MODHAR commands
[gpd4.3.5]
54.4 Commands for creating a new header array file
[gpd4.3.6]
54.4.1 Commands for modifying an existing header array file
[gpd4.3.6.1]
54.4.2 Commands for adding arrays to the new file
[gpd4.3.6.2]
54.5 Operations on headers or long names
[gpd4.3.7]
54.6 Commands for complicated modification or addition
[gpd4.3.8]
54.6.1 MODHAR sub-commands for mw or aw
[gpd4.3.8.1]
54.6.2 Examples
[gpd4.3.8.2]
54.6.3 Writing arrays to the new header array file
[gpd4.3.8.3]
54.6.4 Option ADD when modifying data in MODHAR
[gpd4.3.8.4]
54.7 Finishing up
[gpd4.3.9]
54.7.1 Exit commands
[gpd4.3.9.1]
54.7.2 History of the new file
[gpd4.3.9.2]
54.8 Complete example of a MODHAR run
[gpd4.3.10]
54.9 Text files
[gpd4.3.11]
54.10 Example: Constructing the header array data file for Stylized Johansen
[gpd1.4.2]
54.11 Example: Modifying data using MODHAR
[gpd1.4.3]
55 Ordering of variables and equations in solution and equation files
[ordering]
55.1 Ordering of variables
[gpd2.4.15.2]
55.1.1 Ordering of components of variables
[gpd2.4.15.3]
55.2 Ordering of the equation blocks
[gpd2.4.15.4]
55.2.1 Ordering of the equations within one equation block
[gpd2.4.15.5]
56 SEENV: to see the closure on an environment file
[gpd4.12]
56.1 Command file output
[gpd4.12.1]
56.2 Spreadsheet output
[gpd4.12.2]
56.3 Shock statements for the bottom of a command file
[gpd4.12.3]
57 Automated homogeneity testing
[autohomog]
57.1 What do we mean by nominal and real homogeneity
[homotheory]
57.2 Specifying Types of Variables in TAB file
[homotest1]
57.2.1 Ordinary change variables
[homotestdelvar]
57.2.2 Levels variables
[homotest1.0a]
57.2.3 Leaving some VPQ types unspecified is OK
[homotest1.0b]
57.2.4 Domestic and foreign dollars
[homotest1.1]
57.2.5 Sometimes, non-homogeneity does not matter
[homotestdc]
57.2.6 Some variables must be of Unspecified type
[homotest1.2]
57.3 Homogeneity check or simulation
[homochoice]
57.4 Carrying out a homogeneity check
[homocheck]
57.4.1 Interpreting the Homogeneity Report HAR file
[homotest2]
57.4.2 Understanding equation summaries at header 0000
[homotest2.1]
57.4.3 Example
[homotest2.1.1]
57.4.4 Fixing apparent problems
[homotest2.2]
57.4.5 Best to work with the uncondensed system
[homotest2.3]
57.5 Automated homogeneity simulations
[aut-homosim]
57.5.1 Program works out the shocks
[aut-homosim1]
57.5.2 Checking the simulation results
[aut-homosim2]
57.6 Detailed example MOLN.TAB
[moln-homo]
57.6.1 Suboptimalities in MOLN-R11-VPQ.TAB
[moln-r11]
57.6.2 Homogeneity of MOLN.TAB
[moln-homo1]
57.6.3 Homogeneity problems with MOLN-R11-VPQ.TAB
[moln-homo2]
57.7 Detailed example ORANIG-VPQ.TAB
[oranig-vpq]
58 Several simultaneous Johansen simulations via SAGEM
[gpd3.10]
58.1 The solution matrix
[gpd3.10.1]
58.1.1 Individual column results
[gpd3.10.1.1]
58.1.2 Cumulative or row totals results
[gpd3.10.1.2]
58.1.3 Subtotal solutions
[gpd3.10.1.3]
58.1.4 Contents of a SAGEM solution file
[gpd3.10.1.4]
58.1.5 Viewing the results of a simulation
[gpd3.10.1.5]
58.2 SAGEM Subtotals
[gpd3.10.2]
58.2.1 Subtotals using SAGEM
[gpd3.10.2.1]
58.2.2 Subtotals and sets of shocks in general
[gpd3.10.2.3]
58.2.3 Viewing subtotals or individual column results using ViewSOL
[gpd3.10.2.5]
58.3 No individual column results from multi-step simulations
[gpd3.10.3]
58.4 When to use SAGEM to calculate individual column results
[whensagem]
59 Equations files and LU files
[gpd3.9]
59.1 Equations files
[gpd3.9.1]
59.1.1 Using an equations file in SAGEM
[gpd3.9.1.1]
59.1.2 Differences in step 1 if an equations file is saved
[gpd3.9.1.2]
59.1.3 Model name, version and identifier
[gpd3.9.1.3]
59.2 Starting from existing equations and SLC files
[gpd9.7.22]
59.2.1 Restrictions
[gpd9.7.22.1]
59.2.2 BCV files no longer produced or supported
[gpd9.7.21]
59.3 LU files
[gpd3.9.3]
60 Example models supplied with GEMPACK
[models]
60.1 Models usually supplied with GEMPACK
[gpd8.1c]
60.2 Stylized Johansen  SJ
[gpd8.1.1]
60.3 Miniature ORANI  MO
[gpd8.1.2]
60.4 Trade model TRADMOD
[gpd8.1.3]
60.5 ORANI-type single-country model  ORANI-G
[gpd8.1.4]
60.5.1 ORANIG01 model
[gpd8.1.4.1]
60.5.2 ORANIG98 model
[gpd8.1.4.2]
60.6 Single country model of Australia  ORANI-F
[gpd8.1.5]
60.7 Global trade analysis Project  GTAP
[gpd8.1.6]
60.7.1 GTAP61 model
[gpd8.1.6.1]
60.7.2 GTAP94 model
[gpd8.1.6.2]
60.8 Dervis, de Melo, Robinson model of Korea -- DMR
[gpd8.1.7]
60.9 Intertemporal forestry model  TREES
[gpd8.1.8]
60.10 Single sector investment model  CRTS
[gpd8.1.9]
60.10.1 Using levels equations and ADD_HOMOTOPY in CRTS
[gpd8.1.9.1]
60.11 Five sector investment model  5SECT
[gpd8.1.10]
60.12 Complementarity examples
[gpd8.1.11]
60.13 ORANI-INT: an intertemporal rational expectations version of ORANI
[gpd8.1.12]
60.14 ORANIG-RD : A recursive dynamic version of ORANI-G
[gpd8.1.13]
61 Pivoting, memory-sharing, and other solution strategies
[pivots]
61.1 Re-using pivots (MA48)
[gpd9.5]
61.1.1 Advanced pivot re-use strategy
[gpd9.5.1]
61.1.2 Examples
[gpd9.5.1.1]
61.1.3 New command file statements for pivot re-use
[gpd9.5.2]
61.1.4 Modifying pivots when new entries are in the diagonal blocks
[gpd9.5.3]
61.1.5 Never modify pivots if a triangular block would become non-triangular
[gpd9.5.4]
61.1.6 Start of second and subsequent subintervals
[gpd9.5.5]
61.2 Time taken for the different steps
[gpd3.12.4]
61.2.1 Total time for multi-step compared to 1-step
[gpd3.12.4.1]
61.2.2 Using existing files to speed up step 1
[gpd3.12.4.2]
61.2.3 Memory reallocation now done within the MA48 routines
[gpd5.5.2]
61.2.4 LU decomposing transpose of LHS may be much quicker
[gpd5.5.3]
61.2.5 Alternative pivot strategy in MA48
[gpd5.5.4]
61.2.6 Linearization used can affect accuracy
[gpd3.12.6.4]
61.2.7 Example of increasingly large oscillations
[gpd3.12.6.5]
61.2.8 Scaling equations
[gpd3.12.6.6]
61.3 When memory is short (GEMSIM or TG-programs) - Memory sharing
[gpd5.4.2]
61.3.1 When memory sharing may be useful
[gpd5.4.2.1]
61.3.2 Running in virtual memory is usually very slow
[gpd5.4.2.2]
61.3.3 Restrictions
[gpd5.4.2.3]
61.3.4 What arrays share memory
[gpd5.4.2.4]
61.3.5 Main memory saving comes during LU decomposition
[gpd5.4.2.5]
61.3.6 Memory saving if using MA48 and MMNZ2 is smaller than MMNZ
[gpd5.4.2.6]
61.3.7 CPU time penalty
[gpd5.4.2.7]
61.3.8 Large work files are needed
[gpd5.4.2.8]
61.3.9 GTAP examples
[gpd5.4.2.9]
61.3.10 USAGE examples
[gpd5.4.2.10]
61.3.11 Less total memory is used than in Release 8.0
[gpd5.4.2.11]
61.3.12 Technical notes about memory sharing
[gpd5.4.2.12]
61.3.13 Technical fine print about TABLO-generated programs
[gpd5.4.2.13]
62 Limited executable-image size limits
[exelimits]
62.0.1 No limits on data manipulation programs or SAGEM
[datalimits]
63 Some technical details of GEMPACK
[technical]
63.1 Handling integers and reals in GEMSIM and TG-programs
[gpd9.7.11]
63.1.1 Some TAB files may need changes
[gpd9.7.11.1]
63.1.2 Release 10 details of real and integer arithmetic
[gpd9.7.11.2]
63.1.3 Integers and reals allowed
[gpd9.7.11.3]
63.2 GEMSIM calculations
[gpd9.7.12]
63.2.1 How GEMSIM and TG-programs do arithmetic
[gpd9.7.12.1]
64 Rarely used features of GEMPACK programs
[legacy]
64.1 Stopping and restarting TABLO
[gpd2.2.5]
65 Choosing sets of variables interactively
[gpd4.17]
65.1 Simple choices
[gpd4.17.1]
65.2 Specifying components of one variable
[gpd4.17.2]
65.3 The lists option - choosing a set actively
[gpd4.17.3]
65.3.1 Lists option - the subcommands in more detail
[gpd4.17.3.1]
65.4 The some option - responding to prompts
[gpd4.17.4]
66 Older ways to choose closure and shocks
[oldshkclos]
66.1 Reading closure or shocks from a text file
[gpd3.5.textfile]
66.2 Shock files -- fine print
[gpd3.5.8]
66.2.1 All components shocked case and "select from file" case
[gpd3.5.8.1]
66.2.2 Shocking some components (not "select from file")
[gpd3.5.8.2]
66.3 Choosing the closure and shocks interactively
[gpd3.5.4.3]
66.4 Using component numbers to specify closure or shocks
[gpd3.5.3]
66.4.1 Examples of component numbers
[gpd3.5.3.1]
66.5 Other situations where you choose sets of variables
[gpd3.5.4]
66.5.1 Example of choosing sets in SAGEM
[gpd3.5.4.2]
67 Improving your TAB and CMF files
[better]
67.1 Common errors
[better1]
68 Shock statements designed for use with RunDynam
[rdynshoks]
68.1 Shock statements for RunDynam
[rdynshocks]
68.1.1 Ashock and Tshock statements for dynamic models
[gpd3.5.5.4]
68.2 Shock statements using a slice from a header array file
[gpd5.9.17]
68.2.1 Use with RunDynam and similar programs
[gpd5.9.17.1]
68.2.2 Syntax rules for slice shock statements
[gpd5.9.17.2]
68.3 Other additional and target shock-type statements
[gpd9.7.7]
69 GEMPACK on Linux, Unix or Mac OS X
[unix]
69.1 Linux filenames
[unixshell]
70 TEXTBI : extracting TAB, STI and CMF files from AXT, SL4 and CVL files
[gpd4.14]
71 History of GEMPACK
[oldnewfeat]
71.1 Birth of GEMPACK
[beginnings]
71.2 New Features of GEMPACK Release 5.2 (1996)
[new4rel5.2]
71.3 New Features of GEMPACK Release 6 (1998)
[new4rel6]
71.4 New Features of GEMPACK Release 7 (2000)
[new4rel7]
71.5 New Features of GEMPACK Release 8 (2002)
[new4rel8]
71.6 New features in Release 9.0 (2005)
[gpd5.1.4]
71.6.1 New Release 9 command file statements
[gpd5.14]
71.7 New features in Release 10.0 (2008)
[gpd9.1.4]
71.7.1 Support for new Windows versions
[gpd9.8.1]
71.7.2 Changes to GEMPACK Windows programs
[gpd9.8.2]
71.7.3 New command file statements
[gpd9.9.2]
71.8 New Features in Release 11.0 (2011)
[rel11-new]
71.8.1 Other improvements since Release 10
[rel10plus]
71.9 New Features in Release 11.2 (2013)
[rel112-new]
71.10 New Features in Release 11.3 (2014)
[rel113-new]
71.11 New Features in Release 11.4 (2016)
[rel114-new]
71.12 New Features in Release 12.0 (2018)
[rel120-new]
71.12.1 Release 12 code reorganisation and consequences
[rel12code]
71.12.2 Other minor changes for Release 12
[misc12]
71.13 New Features in Release 12.1 (2019)
[rel121-new]
71.14 New Features in Release 12.2 (2024)
[rel122-new]
72 TABLO-generated programs and GEMSIM - timing comparison
[gpd8.4]
73 Fortran compilers for Source-code GEMPACK
[fortrans]
73.0.1 64-bit compilers
[gpd9.3]
73.0.2 Should I consider moving to 64-bit intel or GFortran now?
[gpd9.3.2]
74 LTG variants and compiler options
[gpd6.7.5a]
74.0.1 Compiling and linking TABLO-generated programs
[gpd6.7.1.1]
74.0.2 TABLO-generated programs
[gpd6.7.1.2]
74.0.3 Trapping for LTG errors in DOS batch files
[gpd6.7.2.1]
74.1 Variants of LTG
[gpd6.7.5]
74.1.1 Keep/Delete Fortran LTG: LTGKPFOR.BAT and LTGNOFOR.BAT (all compilers)
[gpd6.7.5.2]
74.1.2 No Modules LTG: LTGNOMOD.BAT and LTGFNMOD.BAT (all compilers)
[gpd6.7.5.3]
74.2 Fortran compiler options
[gpd6.6.6]
74.2.1 Optimization levels
[gpd6.6.6.1]
74.2.2 Compiling TABLO-generated programs
[gpd6.6.6.2]
74.3 Compiler options â Technical information
[gpd6.7.7]
74.3.1 Compiler options for the Intel compilers
[gpd6.7.7.1]
74.3.2 Compiler options for the GFortran compilers
[gpd6.7.7.1b]
74.3.3 Changing the optimization setting (all compilers)
[gpd6.7.7.4]
75 Fine print about header array files
[gpd4.5]
75.0.1 Effect of set and element information on GEMPACK programs
[gpd4.5.1]
75.0.2 Checking set and element information when reading data
[gpd4.5.2]
75.0.3 Adding set and element information to an existing HAR file
[gpd4.5.3]
75.0.4 Compatibility with earlier releases of GEMPACK
[gpd4.5.4]
75.0.5 Technical point
[gpd4.5.5]
75.1 Sparse header arrays
[gpd9.6]
75.1.1 Writing sparse headers
[gpd9.6.1]
75.1.2 Download programs which can read sparse headers
[gpd9.6.2]
75.1.3 Converting HAR files from sparse to non-sparse format, or vice-versa
[sprs2full]
76 Converting binary files: LF90/F77L3  to/from Intel/LF95/GFortran
[gpd4.15]
76.1 Lahey and Fujitsu binary files
[gpd4.15.0]
76.2 Converting between Lahey and Fujitsu binary files
[gpd4.15.1]
76.3 GEMPACK programs on PCs can handle both type of files
[gpd4.15.2]
76.3.1 Names and location of these converted files
[gpd4.15.2.1]
76.3.2 Deleting temporary copies of these files
[gpd5.10.2]
77 Translation between GEMPACK and GAMS data files
[gdxhar]
77.1 Programs GDX2HAR and HAR2GDX
[gdxhar1]
77.1.1 GDX FORMAT CHANGE
[gdxformat]
77.2 Translating between GEMPACK and GAMS text data files
[gdxhar2]
78 Recent GEMPACK with older RunGTAP or RunDynam
[gpd5.12]
78.1 RunGTAP
[gpd5.12.2]
78.2 RunDynam etc
[gpd5.12.1]
79 SUMEQ: information from equations files
[gpd4.13]
79.0.1 Map of an equations file produced via SUMEQ
[gpd4.13.1.1]
79.1 SUMEQ and the homogeneity of models
[gpd4.13.2]
79.1.1 Why using SUMEQ is better than carrying out a simulation
[gpd4.13.2.1]
79.1.2 Homogeneity example with miniature ORANI
[gpd4.13.2.2]
79.1.3 SUMEQ for homogeneity - summary
[gpd4.13.2.3]
80 Older GEMPACK documents
[gemdocs]
80.1 Very old GEMPACK documents
[gedseries]
81 References
[references]
82 Index
[index]
83 End of document
[docend]
1    Introduction
[gpd1.1]
Click here
for detailed chapter contents
GEMPACK (
G
eneral
E
quilibrium
M
odelling
PACK
age) is a suite of economic
modelling software designed for building and solving applied general
equilibrium models. It can handle a wide range of economic behaviour and
contains powerful capabilities for solving intertemporal models. GEMPACK
calculates accurate solutions of an economic model, starting from an algebraic
representation of the model equations. These equations can be written as levels
equations, linearized equations or a mixture of these two.
The software includes a range of utility programs for handling the economic
data base and the results of simulations, and is fully documented with plenty
of examples.
GEMPACK provides
a simple language in which to describe and document the equations of your economic model;
a program which converts the equations of your model to a form ready for running simulations;
options for varying the choice of endogenous, exogenous and shocked variables;
powerful tools to help you understand or analyze simulation results;
utility programs to assist in managing model databases. The data can be
inspected, modified, or converted to other formats, such as spreadsheets;
programs to generate reports from simulation results or from inital data.
The latest Release of GEMPACK is 12.2 (2024). New 12.2 features  are listed in section
71.14
.
New features of GEMPACK Release 12.1 (2019) are listed in section
71.13
.
New features of GEMPACK Release 12 (2018) are listed in section
71.12
.
New features introduced for versions of GEMPACK Release 11 (2011-16) are listed in sections
71.8
and
71.9
.
The remainder of this chapter contains the following sections:
1.1
Organization of this manual
1.2
Using this manual
1.3
Supported Operating Systems
1.4
The GEMPACK programs
1.5
Models supplied with GEMPACK
1.6
Different versions of GEMPACK and associated licences
1.7
Citing GEMPACK
1.8
Communicating with GEMPACK
1.10
Acknowledgments
1.1    Organization of this manual
[manualoutline]
Remaining chapters of this manual are organized as follows:
Chapter
2
is a guide  to installing GEMPACK on your Windows PC.
Chapters
3
to
7
are an
Introduction to
GEMPACK
.
New users should first work through these
. Chapter
3
tells you how
to carry out simulations with models, while chapter
4
tells you how to build or modify
models. Chapter
6
describes data files and how to construct them. Chapter
7
describes GEMPACK file types, names and suffixes.
Chapters
8
to
18
are a comprehensive description
of the
TABLO language
, used to specify GEMPACK models. They also include instructions for
running the TABLO program.
Chapters
19
to
35
tell how to run simulations,
using GEMSIM, TABLO-generated programs or SAGEM. They also describe the Command (CMF) Files used to
specify details of simulations.
Chapters
36
to
41
describe other GEMPACK
programs. Chapter
36
describes Windows programs such as WinGEM, ViewHAR, Charter,
ViewSOL, TABmate, RunGEM, AnalyseGE and RunDynam. Chapters
37
to
41
describe command-line programs, including   SLTOHT, ACCUM and DEVIA.
Chapters
42
to
46
contain a guide to the example
models supplied with GEMPACK, and hands-on instructions for using WinGEM, AnalyseGE, RunGEM, and
other GEMPACK programs.
The remaining chapters include more technical material,
References
, and the
Index
.
1.2    Using this manual
[usingmanual]
This manual is available in two formats which you can view on your PC:
An HTML document, gpmanual.htm.  Each GEMPACK Windows program should
provide a link to this file, via the
Help
menu.
A PDF document, gpmanual.pdf. You can print out excerpts from this (but
not the
whole
document — it is very long!).
In each case the
Contents
and
Index
sections should help you find the information
you need.
Each section or subsection has a "topic ID" which appears in green at the end of section headings.
GEMPACK programs may emit warning or error messages that refer you to sections of this manual. The
references may include section numbers, section titles and topic IDs, but the topic ID is most
likely to remain unchanged through successive revisions of the manual.
Previous GEMPACK documentation was contained in a number of separate manuals called
GPD-1
to
GPD-9
. Now most of these documents have been revised
1
and consolidated into this single manual. A list of GEMPACK documents (including the former GPD
documents) is given in chapter
80
.
1.2.1    For experienced GEMPACK users
[gpd1.1.5.2]
If you have worked with an earlier version of GEMPACK, the first thing you will want to see is a
list of the new features. The latest new feature list is at the webpage
http://www.copsmodels.com/gprelnotes.htm
.
There is a summary in section
71.12
below. Features introduced for previous GEMPACK Releases are listed in chapter
71
.
1.2.2    For new GEMPACK users — getting started
[gpd1.1.5.1]
We suggest you read the
Introduction to GEMPACK
chapters
3
to
7
,
working through the examples.
We have built these chapters around the sorts of modelling tasks you will want to do.
The most important of these tasks are:
Carrying out simulations with an existing model. Looking at and analysing the results.
Building a new model or modifying an existing model.
As part of building a new model or modifying an existing model, you may need to build or modify the
data files for the model.
We suggest that you begin with the first of these tasks (simulations). Chapter
3
tells
you how to carry out simulations with existing models, and how to look at the results. We suggest
that you read this in detail and carry out the simulations described there for yourself. This chapter includes detailed
hands-on instructions for using the relevant GEMPACK programs. You will find sufficient detail
there to carry out all the steps involved.
The simulations in chapter
3
are based on the Stylized Johansen model, which is a
small model. Even if your purpose in using GEMPACK is to work with another model (possibly ORANI-G or
GTAP), we strongly recommend that you work through chapter
3
in detail first. After
that, you will be in a position to carry out simulations with your chosen model.
At the end of chapter
3
we give suggestions as to what to do next. Roughly speaking,
the possibilities are:
If you mainly want to carry out simulations with another standard model, you will find a list of
the models supplied with GEMPACK in section
1.5
. You will find detailed hands-on
guidance in chapters
42
to
46
about carrying out standard simulations with many of these models.
When you are ready to build your own model (or modify someone else's), or if you just want to
understand how a model is implemented in GEMPACK, you should read chapter
4
. Perhaps
read it quickly the first time and then go back for a more detailed study.
If you need to build or modify the data files for a model, you should read chapter
6
.
When you want to know more about the GEMPACK utility programs (say, for report generation or
post-simulation processing of results), look at the detailed documentation
in Chapters
39
to
41
.
When you want to know more about running the GEMPACK programs, read chapter
48
. This
chapter gives detailed suggestions for more efficient use of the programs whether you are running
them interactively or in batch mode.
We now encourage you to skip the rest of this chapter and to go straight to chapter
3
.
1.3    Supported Operating Systems
[supportedos]
The complete range of GEMPACK features is available only on PCs running Microsoft Windows.
Nevertheless GEMPACK will run (with some limitations) on other operating systems, such as MacOS or Linux
(see chapter
69
for more details).
GEMPACK supports both 32-bit and 64-bit versions of Windows 7 to 10.
The 64-bit versions are more suitable for large modelling tasks (see section
49.3.1
), particularly
if you wish to exploit the parallel-processing capability of modern PCs  — see chapter
31
.
1.4    The GEMPACK programs
[gpd9.1.5]
GEMPACK includes a number of separate programs.
They fall into two broad groups:
1.4.1    The original command-line programs
[gpd9.1.5.1]
The original GEMPACK programs, all written in Fortran, are command-line programs (without a
graphical interface). They form the core of GEMPACK and are still directly used by experienced
modellers. They are portable between different operating systems. The chief programs are:
Program
Description
TABLO
translates a TAB file into an executable program  (or, optionally, into bytecode [GEMSIM Auxiliary files]). See chapter
8
.
GEMSIM
an interpreter: executes bytecode versions of TABLO-generated programs.
SLTOHT
translates an SL4 (Solution) file into a HAR or a text file. See chapters
39
and
40
.
SEEHAR
translates a HAR file into a text file. See chapter
37
.
1.4.2    The Windows programs
[gpd9.1.5.2]
Additional GEMPACK programs only run on Windows PCs. These
have a more modern graphical interface, and are written in Pascal [Delphi]. Some of these Windows
programs make some use of the core command-line programs listed above: they are really "wrappers"
or "shells" which provide a more convenient interface to the original GEMPACK programs. The main
Windows programs are:
Program
Description
Using core programs:
TABmate
A text editor tailored to GEMPACK use.
TABLO
ViewHAR
Used to view and modify HAR data files.
none
ViewSOL
Used to view simulation results.
SLTOHT (sometimes)
AnalyseGE
Used to analyse simulation results: presents an integrated view of input data, model equations, and results.
TABLO, SLTOHT and others
WinGEM
A portal to all the other GEMPACK programs, which guides the user through the stages of specifying a model, creating data files, and running simulations.
all
RunGEM
A convenient interface for running simulations and viewing results.
SLTOHT and others
Another Windows program, RunDynam, is used to organize, perform, and interpret multi-period
simulations with recursive-dynamic CGE models. RunDynam is not included in the standard GEMPACK
package — it may be purchased separately. See section
36.7
for more about RunDynam.
1.4.3    TABLO-generated programs
[gpd1.1.7.1]
There is another class of programs in GEMPACK called TABLO-generated programs. These programs are
not supplied as part of the GEMPACK software — you create them yourself.
A TABLO-generated program is a Fortran program, written by the program TABLO, designed to solve a
particular model specified in a TABLO input (TAB) file supplied by you. You need a Source-code
version of GEMPACK to write TABLO-generated programs — see sections
1.6.1
and
3.5.1
below. These Fortran programs can be compiled and linked to the GEMPACK
libraries of subroutines using your Fortran compiler to make an Executable image. The
Executable-Image (EXE) can be used to run simulations instead of (and faster than) the program GEMSIM.
1.5    Models supplied with GEMPACK
[gpd1.1.8]
A variety of example CGE models are supplied with GEMPACK including:
small pedagogical models
Stylized Johansen
and
Miniature ORANI
versions of the
ORANI-G
model of the Australian economy, including
ORANIG-RD
,
a Recursive Dynamic (forecasting) version.
TRADMOD
, a flexible multi-country trade model documented in
Hertel  et al. (1992)
,
well-known models such as
GTAP
, the Global Trade Analysis Project's model for analysing trade issues,
and
DMR
, the  Dervis, De Melo, Robinson model of Korea,
TERM
, a multi-regional model of a single country
four intertemporal models
TREES
,
CRTS
,
5SECT
, and
ORANI-INT
.
models using complementarities to simulate quotas, such as
MOIQ
(based on Miniature ORANI),
and several GTAP-based models
various models illustrating  GEMPACK's 'post-simulation' feature
Chapter
60
contains more details. Hands-on examples using some of these models appear
in chapters
42
to
46
.
1.6    Different versions of GEMPACK and associated licences
[gpd1.1.9]
Currently there are four main types of GEMPACK licence:
The
Source-code
version is the most powerful and expensive option. You can produce a
model-specific EXE program which solves large models quickly, and can be shared with other
people. A Fortran compiler is needed.
The
Unlimited executable-image
version also allows you to create and solve large models,
using the general-purpose program GEMSIM. No Fortran compiler is needed — you cannot turn your
model into an EXE file.
The cheaper
Limited executable-image
version allows you to create and solve models
up
to a certain size
.
The cheapest
Introductory
licence is needed by persons (with no other GEMPACK licence) who
wish to solve a large model using a model-specific EXE program generated by another (source-code)
GEMPACK user.
GEMPACK licences are usually site licences, that is, multi-user licences which can be used on any
number of computers at the same site within the relevant organisation. However, individual licences
are also available for some licence types.
More details about these licence types follow. Alternatively, consult these web-pages:
Different versions of GEMPACK:
http://www.copsmodels.com/gpver.htm
Feature summary:
http://www.copsmodels.com/gemfeat.htm
Current prices:
http://www.copsmodels.com/gpprice.htm
Licence conditions:
http://www.copsmodels.com/gp-lictext.htm
To find out which version of GEMPACK you are running now, see section
2.9.6
.
1.6.1    Source-code versions and licences
[gpd1.1.9.1]
Source-code licences provide the most flexibility for modellers. The size of the models that can
be handled is limited only by the amount of memory on your PC. Large models are usually solved
using TABLO-generated programs — which are model specific and can solve large models
considerably faster than the general-purpose program GEMSIM. A suitable Fortran compiler is
required — see:
http://www.copsmodels.com/gpfort.htm
which lists both free and commercial compilers.
The Source-code version is the only GEMPACK version that can run "natively"
on non-Windows computers: see chapter
69
.
1.6.2    Unlimited executable-image version and licence
[gpd1.1.9.3]
Like the Source-code version, the Unlimited Executable-image
2
version allows you to create and solve models of any size — as long as your PC has sufficient
memory. No Fortran compiler is needed: all simulations are carried out with
the GEMPACK program GEMSIM.  With large models (for example, 115 sector ORANI-G or 15-region,
15-commodity GTAP), GEMSIM is noticeably slower than the corresponding TABLO-generated program
(which can only be created with a Source-code licence). [Some CPU times are reported in chapter
72
.]
If users with an Unlimited Executable-image version find that their simulations are taking an
unacceptably long time, they can upgrade to a Source-code version.
1.6.3    Limited executable-image version and licence
[gpd1.1.9.2]
With this version, all simulations are carried out with the GEMPACK program GEMSIM. "Limited"
means that the size of models that can be solved is limited.
Modellers with the Limited Executable-image version of GEMPACK can carry out the full range of
modelling tasks, including building and solving new models, and modifying existing ones. The only
restrictions are on the size of the models that can be handled.
The size of models that can be solved is limited to what we call
"medium-sized" models.  For example, this version is able to solve most single-country models with
up to about 40 sectors (for example, it will solve 37-sector ORANI-G), and it
will usually solve 12-region, 12-commodity GTAP; but it will not solve
50-sector ORANIG or 15-region, 20-commodity GTAP.  The full details of size limits for simulations
with the Limited Executable-image version can be seen in chapter
62
.
This version of GEMPACK is often supplied at training courses.
If users with a Limited Executable-image version find that their models have become too large, they
can upgrade to a Source-code or Unlimited Executable-image version.
1.6.4    Using Exe-image and Source-code GEMPACK together
[gpeisc]
A Source-code GEMPACK licence is a site licence covering the whole of some department or section
of an organization. The standard installation procedure is not very quick and requires that a
suitable Fortran compiler is installed.
An efficient alternative might be for a small core group of modellers to install
the full Source-code GEMPACK (with Fortran compiler) and for an outer group of less frequent (or
less advanced) users to use the Unlimited Exe-image version of GEMPACK (without Fortran compiler).
No additional licence is needed, because a Source-code licence file will also enable use of the
Unlimited Exe-image version.
For example, a university department with a Source-code GEMPACK licence might install full
Source-code GEMPACK (with Fortran compiler) on the PCs of several academic staff, while students
used the same licence file to run the Unlimited Executable-Image Version. The Executable-Image
Version is also well-suited to a Computer Lab environment.
For more details, see
http://www.copsmodels.com/gpeisc.htm
.
1.6.5    When is a licence needed
[gpd1.1.9.7]
A GEMPACK licence is required:
to run TABLO or GEMSIM
to run a TABLO-generated program using a larger dataset
to use some more advanced features of GEMPACK Windows programs
All three tasks above can be accomplished using either an Executable-image or a Source-code licence.
But tasks 2 and 3 (but not 1) could also be accomplished using the cheaper Introductory licence described next.
1.6.6    Introductory licence
[gpd1.1.9.5]
This type of licence is typically needed by someone who has not installed any full
version of GEMPACK, but
who has obtained GEMPACK-related material (for example, a TABLO-generated program and/or some data
files) from another GEMPACK user.
Some type of GEMPACK licence may be required to run a TABLO-generated program  or
to use  more advanced features of some GEMPACK Windows programs. The
Introductory licence
is the cheapest way to meet this requirement. It was previously called
Large-simulations licence
.
TABLO-generated programs distributed to others.
A GEMPACK user with a Source-code licence can create executable images of TABLO-generated programs
to solve the models they build or modify.  These TABLO-generated programs can be distributed to
others (including others who do not have a GEMPACK licence) so that they can carry out simulations
with the model. However,
if the model  is larger than
medium sized
(as defined in chapter
62
), running simulations will require
some
type of GEMPACK licence. For example,
any Source-code or Executable-image licence will do, even older ones.
But the Introductory GEMPACK licence, designed  for just this purpose, is the cheapest solution.
For example, a modeller who (freely) downloaded the  TABLO-generated program GTAP.EXE,
would, with
no
GEMPACK licence be restricted to using data no larger than 12 regions and sectors.
If she purchased an Introductory GEMPACK licence, she could solve models of any size (that her PC could manage).
Note also:
(a) An Introductory GEMPACK licence will not allow you to create or modify models.
(b) An Introductory GEMPACK licence will not allow you to run TABLO or GEMSIM.
(c) You do not require a licence file for GEMPACK utility programs such SLTOHT.
Other programs (ViewHAR, AnalyseGE etc).
A trial version of GEMPACK can be freely downloaded from
the GEMPACK web site: see
http://www.copsmodels.com/gpeidl.htm
.
After the trial licence expires, you will no longer be able to
create or edit new models. However, most Windows programs
will continue to work, as they do not require a GEMPACK
licence for much of their functionality. However some of
the more advanced features of these programs require a
moderately recent GEMPACK licence
3
. For example,
ViewHAR can be used to modify the data on a Header Array file. However, if the resulting file is
large, you will not be able to save it without some kind of GEMPACK licence.
AnalyseGE normally requires a licence,unless the Solution file
being analysed is very small.
Systematic sensitivity analysis in RunGEM also requires a licence.
SAGEM also requires some type of GEMPACK licence when used with large models.
The Introductory licence is the least expensive way to satisfy these requirements.
1.7    Citing GEMPACK
[citinggempack]
When you report results obtained using GEMPACK, we ask you to acknowledge this
by including a reference to GEMPACK in your paper or report. This
acknowledgement is a condition of all GEMPACK licences.
For example, please include a sentence or footnote similar to the following:
The results reported here were obtained using the GEMPACK economic modelling
software [
Horridge et al. (2018)
].
and include amongst your references:
Horridge J.M.,  Jerie M.,   Mustakinov D. &  Schiffmann F. (2018),
GEMPACK manual
,
GEMPACK Software, Centre of Policy Studies, Victoria University, Melbourne,  ISBN  978-1-921654-34-3
An older reference is
Harrison and Pearson (1996)
.
For a general account of CGE solution software, focussing on GEMPACK, GAMS and MPSGE, you could cite
Horridge et al. (2012)
.
If you use complementarities in your model, consider citing
Harrison, Horridge, Pearson and Wittwer (2002)
.
For subtotal results, cite
HHP
. An extended reference list is
here
.
1.8    Communicating with GEMPACK
[gpd1.1.2]
Latest contact details are at
http://www.copsmodels.com/gpcont.htm
.
1.8.1    GEMPACK web site
[gpd1.1.3]
The GEMPACK Web site is at
http://www.copsmodels.com/gempack.htm
.
This contains up-to-date information about GEMPACK, including information about different versions,
prices, updates, courses and bug fixes. We encourage GEMPACK users to visit this site regularly.
In particular, this site contains a list of Frequently Asked Questions  (FAQs) and answers at
http://www.copsmodels.com/gp-faq.htm
.
This is updated regularly. It is a supplement to the GEMPACK documentation. If you are having
problems, you may find the solution there. We welcome suggestions for topics to include there.
There are also alternative GEMPACK web sites at
http://www.gempack.com
and
http://www.gempack.com.au
and you can send email to   info@gempack.com   or   support@gempack.com.
At present these alternative web sites merely point to the main GEMPACK site. Email to
gempack.com is forwarded to the GEMPACK team.
1.8.2    GEMPACK-L mailing list
[gpd1.1.4]
GEMPACK-L is a mailing list designed to let GEMPACK users communicate amongst themselves, sharing
information, tips, etc. The GEMPACK developers occasionally make announcements on it (new
releases, bugs, courses, etc). The list is moderated to prevent spam.
We encourage all GEMPACK users to subscribe to it. Once you have subscribed, you will receive as
mail any messages sent to the list. For more details, see
http://www.copsmodels.com/gp-l.htm
.
1.9    Training Courses
[training]
Most GEMPACK users get started by attending a GEMPACK-based training course. A range of courses is
offered at different locations around the world by the Centre of Policy Studies — see
http://www.copsmodels.com/courses.htm
, while others are offered by GTAP (Global Trade
Analysis Project) — see
http://www.gtap.agecon.purdue.edu/events/
.
1.10    Acknowledgments
[ackintro]
The improvement of GEMPACK over many years owes a great deal to its users. Some
have contributed very useful suggestions, whilst others have patiently supplied
us with details needed to reproduce, and ultimately fix, annoying program bugs.
We are very grateful to these people, some of whom are listed below.
Greg Watts
Guy Jakeman
Hom Pant
Iain Duff
Ian Webb
James Giesecke
Joe Francois
Jorge Hernandez
Janine Dixon
Antti Simola
George Philippidis
Laurent Cretegny
Tran Hoang Nhi
Alan Powell
Michael Bourne
George Verikios
Joseph Francois
Kevin Hanslow
Lars-Bo Jacobsen
Lindsay Fairhead
Marinos Tsigas
Martina Brockmeier
Matt Clark
Maureen Rimmer
Terry Maidment
Michael Kohlhaas
Owen Gabbitas
Peter Dixon
Agapi Somwaru
Alan Fox
Alex Whitmarsh
Ashley Winston
Athoula Naranpanawa
Ernesto Valenzuela
Federica Santuccio
Frank van Tongeren
Peter Johnson
Peter Wilcoxen
Philip Adams
Robert Ewing
Robert McDougall
Ronald Wendner
Steven Rose
Kevin Hanslow
Tom Hertel
Tom Rutherford
Yiannis Zahariadis
Glyn Wittwer
Markus Lips
Hans van Meijl
Chantal Nielsen
Wusheng Yu
2    Installing  GEMPACK on Windows PCs
[gpd6.1]
Click here
for detailed chapter contents
This chapter tells you how to install GEMPACK Release 12 on a Windows PC. To install an earlier
Release of GEMPACK, please refer to the install documents that accompanied the earlier Release.
Some parts of the install procedure differ between the Executable-Image and the Source-Code
versions of GEMPACK — the text below will indicate these differences.
All components of GEMPACK are contained in a single install package, which you might download or
receive on a USB drive.
The install package for Executable-Image GEMPACK might have a name like gpei-12.0-000-install.exe.
The install package for Source-Code GEMPACK might have a name like gpsc-12.0-000-install.exe.
The package will install
Windows (GUI) programs such as ViewHAR, ViewSOL, TABmate, AnalyseGE, WinGEM and RunGEM.
electronic versions of the GEMPACK user documentation (HTM and PDF files).
many examples of models built using GEMPACK.
The Executable-Image package will also install a number of vital command-line programs such as
TABLO.EXE and GEMSIM.EXE. The Source-Code package instead installs
Fortran source code
files
for these programs: during installation these sources are compiled to produce TABLO.EXE and
GEMSIM.EXE.
2.1    Preparing to install GEMPACK
[gpd6.2]
2.1.1    System requirements
[gpd6.2.1]
Requirements for  installing GEMPACK are:
The PC must be running Windows 7  or later.
The PC must have at least 2GB free hard disk space.
The PC should have at least 4GB of memory (RAM), and preferably 8GB. Click on Help | About in the
main menu of My Computer. This will tell you how much physical memory is available to Windows. The
amount of memory you have limits the size of models you can build and run. Small models may use
less than 128 MB of RAM, while large models may need 2GB or more. Windows itself uses up much
memory. And to do useful things with GEMPACK, you'd very often need to have several GEMPACK
Windows programs and perhaps an MSOffice application open at the same time. Each running program
uses up RAM.
If you are installing Source-Code GEMPACK you need
first
to install and test one of the
supported Fortran compilers listed at
http://www.copsmodels.com/gpfort.htm
. That
page links to compiler-specific instructions.
You will need administrator access to the PC. In a work environment, you may need IT Support to
obtain administrator access.
64-bit versions of GEMPACK will only work on a 64-bit version of Windows. 32-bit versions of
GEMPACK will work on either 32-bit or 64-bit Windows. The install package will detect your Windows
version and suggest the right version for you.
2.1.2    Your GEMPACK licence file
[gplic]
The installation procedure will ask where to locate your GEMPACK licence file — so you should
find it yourself before installing. This small file will have suffix ".GEM" and was probably sent
to you as a zipped email attachment, or might be located on the USB drive containing the install
package. During installation, a copy of the file, named LICEN.GEM, is placed in the GEMPACK folder
(ie, the folder where GEMPACK is installed).
You could also use the LICEN.GEM file in the GEMPACK directory from a previous install of Release
12 GEMPACK (but a Release 11 or earlier licence will not work).
If you cannot find  your GEMPACK licence file, you can still install GEMPACK. In this case:
The Executable-Image installer will create a temporary licence file which last a few months but restricts model size.
Source-Code GEMPACK cannot be used without a licence.
Then, after installation, you should manually place a copy of your licence file, renamed if
necessary to LICEN.GEM, into your GEMPACK folder.
2.1.3    Where to install
[instdir]
First decide where to install GEMPACK, bearing the following in mind:
The ideal plan is to install GEMPACK in a folder C:\GP to which the user has read/write/modify
access.
If you have another or earlier release of GEMPACK already installed in C:\GP, you should probably
leave it on your hard disk until you have successfully installed and tested Release 12.0 (in case
an unexpected problem occurs). You should rename the directory containing the previous release, so
you can install Release 12.0 of GEMPACK in C:\GP. For example, if you currently have Release 11.0
GEMPACK in C:\GP, rename that directory to, say, C:\GP110, and install Release 12.0 into C:\GP. If
you use the same GEMPACK directory as before, other GEMPACK-related Windows programs such as
RunDynam and RunGTAP will automatically use the latest version of GEMPACK.
The name of the GEMPACK directory should not contain Chinese or other non-English characters or
parentheses ["(",")"]. Also, it's best to avoid extremely long folder names. See section
7.1
for more details.
It's best if both the GEMPACK programs and the user's model files are stored on a local hard drive
(not a network drive).
You should configure your antivirus program to exclude from real-time scanning both the GEMPACK
directory (usually C:\GP) and folders containing the user's model files and simulations. See
section
2.1.6
below.
2.1.4    Notes for IT support
[itsupport]
You can install GEMPACK as Administrator, and run as Limited or Standard user, as long as
permissions are set to allow Limited or Standard users to access needed files. Users of GEMPACK
need to be able to read and execute the programs in the GEMPACK directory. In their working
directories, Limited Users need full rights to read, write, execute and delete files.
Users of Source-code GEMPACK need to be able to create their own EXE files using their Fortran compiler.
The software requires that users be able to open and use a command prompt (cmd.exe) window, and to run BAT scripts.
Please assist the user by switching off "Hide file extensions of known file types" (From Explorer, Tools...Folder
Options...View).
If you are installing GEMPACK on a network please see section
2.9.4
.
2.1.5    [Source-code only] Testing the Fortran installation
[gpd6.3.3]
Skip this section if you are installing  Executable-Image  GEMPACK.
Before installing  Source-Code GEMPACK you need to test your Fortran installation by compiling and
running a small 'Hello World!' program. The webpage
http://www.copsmodels.com/gpfort.htm
links to compiler-specific instructions for
installing and testing your Fortran.
It is important that the 'Hello World!' test succeeds
before you install GEMPACK.
The test requires that specific Fortran files are present on the PATH. These files are:
ifortvars.bat for the Intel compiler.
gfortvars.bat for the GFortran compiler.
The GFortran installer should automatically add the right folders to your PATH.
For Intel, you need to edit the PATH variable [the web instructions tell you how].
2.1.6    Configure Anti-virus programs
[antivirus]
Some user report that anti-virus programs delete GEMPACK
programs or prevent GEMPACK programs from being installed. To avoid
such problems you could, before installing GEMPACK:
Create the GEMPACK folder into which you plan to install (normally C:\GP).
Configure your anti-virus program to exclude your GEMPACK folder from real-time virus checking.
There are some instructions how to do this on the GEMPACK web site at
http://www.copsmodels.com/gpconfav.htm
.
You may choose also to exclude from virus-checking the folders where
GEMPACK-related work will be done — anti-virus programs can slow
down simulations (especially RunDynam simulations). See point 3, section
30
.
2.2    Installing GEMPACK
[gpd6.4]
Exit from all Windows programs before beginning the install procedure.
Use Windows Explorer to locate the GEMPACK install package; double-click to run it.
The "User Elevation" dialog will appear; you may need to supply the Administrator
password, or simply agree to run the install.
Welcome and Copyright warning. To agree to the copyright conditions click Next.
Destination Location. Here you choose where GEMPACK will be installed; we refer to this directory
as the GEMPACK directory. We recommend that you accept the suggested C:\GP directory. You may
choose another existing or new directory by clicking the Browse button. If you do so, when you
return to the original screen check carefully that the folder or directory name is what you want.
Sometimes the install program adds \GP to the end of the name you have selected. In choosing a
folder name, avoid names that contain non-English characters or parentheses. Avoid installing
under the Program Files directory: Windows may prevent you changing files there.
Changes to your PATH and Environment. The Install program can make changes to your PATH and the
Environment variable called GPDIR. We
strongly recommend
that you agree to these changes.
If you do not, you must make these changes yourself later: see section
2.8
.
System environment settings for performance. For most installations no changes to the default settings are required. In some circumstances setting the variables on this page could result in shorter simulation times for the models you run on your computer hardware. See section
2.2.6
below for more details.
Selecting a GEMPACK licence file. If the Installer does not find an existing LICEN.GEM in the
GEMPACK directory you may click Browse to select your licence file for installation. If there
already is a LICEN.GEM file in your chosen GEMPACK directory, the Installer will not overwrite it,
and the Browse button will be disabled. If the existing licence file is an old or wrong licence it
is your responsibility to later place the correct Release 12 licence file into your GEMPACK
directory, renamed if necessary to LICEN.GEM.
[Source-code only] Select Fortran Compiler. Indicate which Fortran compiler you will use. This
compiler should be installed and working, as described above.
Ready to begin installation. You may review your settings; click Back to make changes or Next
to begin the installation. The Install program copies many files to your GEMPACK directory. If
installing from a USB drive, leave it inserted until the installation is complete.
[Source-code only] Continue with compiling libraries and executable images. After file copying is
finished you are prompted to launch BuildGP by clicking Next. When you click on Next, the install
program will exit and the BuildGP program will be launched. BuildGP builds the GEMPACK libraries
and executable images of the Fortran-based GEMPACK programs. This will take several minutes. If
all goes well, you will eventually see a message saying that the libraries and images have been
built successfully. In that case, just click OK and go on to section
2.8
. If there is
a problem, see section
2.2.2
.
[Source-code only] Continue with compiling libraries and executable images. After file copying is
finished you are prompted to launch BuildGP by clicking Next. When you click on Next, the install
program will exit and the BuildGP program will be launched. BuildGP builds the GEMPACK libraries
and executable images of the Fortran-based GEMPACK programs. This will take several minutes. If
all goes well, you will eventually see a message saying that the libraries and images have been
built successfully. In that case, just click OK and go on to section
2.8
. If there is
a problem, see section
2.2.2
.
For some versions of GEMPACK, you are required to "activate" your licence. A dialog will appear
which asks for your name, city and email address. Fill these in; then click the Request Activation
Code button. You should soon receive an email containing a 12-letter code, which you enter (or
paste) into the activation program. If all is well, your licence will be permanently activated on
that PC. For more details see section
2.2.3
.
2.2.1    If a warning appears after installing
[pcawarning]
Sometimes, just after installing GEMPACK, a warning screen appears, titled "Program Compatibility
Assistant" and announcing that
"This program might not have installed correctly"
. You are
offered two options (a) "Reinstall using recommended settings", or (b) "This program installed
correctly. We believe that the warning is needless and that you should click
"This program
installed correctly"
.
2.2.2    [Source-code only] If an error occurs
[gpd6.4.1.1]
If an error occurs during the BuildGP process, you will be told the name of the procedure when the
error occurred. We suggest that you note this name on paper, then exit from BuildGP. Usually an
Error log is shown. This should give you some idea what is happening.
Possible Checks and Actions to try:
Check that there is plenty of room on your hard disk — if not, you will need to delete some files
to create space.
Check that Fortran is installed and on your path (see section
2.1.5
).
Check that the name of the GEMPACK directory does not contain spaces or Chinese or other
non-English characters (See section
7.1
).
Install all over again. Or, you could try re-running just the final, BuildGP, stage. To do this,
open a command prompt (DOS box) in your GEMPACK directory and type "BuildGP". Check the GEMPACK
directory and compiler choices, then click .Start Build..
If an error reappears, please notify support@gempack.com. If an Error log has been created, please
send it with details of what happened.
BuildGP checks that there is enough free disk space on the drive you chose for the GEMPACK
directory. You can override these checks if you disagree or you can exit from BuildGP, clear some
more disk space and then rerun BuildGP. You can read more about BuildGP in section
2.9.1
.
2.2.3    Some GEMPACK licences require activation
[activation]
Some GEMPACK and RunDynam licences require to be "activated" in order to continue using TABLO or
GEMSIM on your PC.
Limited-size, Introductory and 'Course' licences (handed out at a training course) do not require
activation.
At the final stage of installation, you will be asked if you wish to activate your licence on the
PC you are using. This is the best time to do it.
However, you could choose to run the activation program (GPactivate.exe) later (perhaps after
installing the correct licence file). You can go on using a licence which has not been activated
for a 'grace period' of 30 days.
For a given PC and licence, activation is permanent, and does not need to be repeated. But you may
need to activate again if you install an upgraded version of GEMPACK, or dramatically change your
PC hardware.
There is a generous limit on the number of times per year each licence can be activated. You can
activate an individual licence on several PCs — the limit is greater for site licences. If you
exceed the limit you can email GEMPACK sales to ask for the limit to be increased.
More information about licence activation can be found at
http://www.copsmodels.com/gpactivation.htm
.
2.2.4    GEMPACK licence
[gpd6.4.4]
Your GEMPACK licence must be called LICEN.GEM and it must be placed in your GEMPACK directory
(that is, the directory in which you installed GEMPACK). The installer may have already done this:
if so, skip this section.
If you already have a Release 12 licence on your computer in another directory, please copy the
file LICEN.GEM to your current GEMPACK directory.
See section
1.6
for details about GEMPACK licences.
2.2.5    Changes to your PATH and Environment
[gpd6.4.4a]
If (against our advice) you did
not
allow the Install program to make changes to your PATH and the
Environment variable called GPDIR,  you must now make these changes yourself: see section
2.8
.
2.2.6    System environment settings for performance
[mathlibperf]
When performing a simulation GEMPACK uses fast math libraries for matrix operations. The settings on this installer page control
how the fast math libraries operate and can affect the time a simulation takes to complete. For most GEMPACK
installations the default settings will give good performance. If you are in doubt we recommend you accept the default
settings and experiment with modifying the associated environment variables later. The environment variables can be
temporarily changed in a command-prompt shell or permanently changed using you system settings for environment
variables.
Circumstances where you might benefit from customized settings include:
(1) You are installing Source-code GEMPACK with the Intel Fortran compiler and MKL,
(2) You are running simulations with Tablo-generated programs made with Intel Fortran and MKL,
(3) You plan to run simulations with a large model which will benefit from modified settings.
OMP_NUM_THREADS
For most circumstances where you are using GEMPACK with the OpenBLAS math library (included with GEMPACK) we recommend
the default value of OMP_NUM_THREADS = 4. If you are running a very large model you might benefit from increasing the
number of threads. The optimal value depends on the program and compiler used to make the program (GEMSIM or a
Tablo-generated program) that will be used to solve your model and also on the model. GEMPACK programs compiled with
the Intel Fortran compiler and MKL might benefit from increasing the value. Installations on a server where
multiple simulations will be run simultaneously might need to cap the number of threads in order to balance the load
across simulations and users. Sensible server settings will depend on the number of available cores and the expected
number of simultaneous simulations. If you want to explore changing the default value for any of these reasons we
recommend you experiment with a typical simulation on your computer.
OPENBLAS_CORETYPE
Most users will not need to change this setting. The variable OPENBLAS_CORETYPE allows you to instruct the OpenBLAS
library to use particular CPU instructions for performing operations. The CPU instructions that are available are
determined by the CPU type in your computer. If GEMPACK recognises the CPU type GEMPACK will internally set the value of
OPENBLAS_CORETYPE to use fast instructions and therefore give good performance. In some circumstances GEMPACK may not
recognise your CPU type and revert to safe but slower instructions. In some cases it may be safe to manually set
OPENBLAS_CORETYPE = Haswell and so benefit from faster instructions.
MKL_ENABLE_INSTRUCTIONS
Most users will not need to change this setting. Similar to OPENBLAS_CORETYPE above, the MKL_ENABLE_INSTRUCTIONS
variable allows you to instruct the MKL math library to use particular CPU instructions for performing operations.
Currently GEMPACK does not internally set a value for MKL_ENABLE_INSTRUCTIONS.  If you run simulations with a GEMPACK
program (GEMSIM or Tablo-generated) compiled with Intel Fortran and MKL we recommend you experiment with different
values of MKL_ENABLE_INSTRUCTIONS appropriate for your CPU before permanently setting the environment variable.
2.3    Testing the Installation
[gpd6.5]
The following test should be performed whether you have the Executable-Image or the Source-Code version of GEMPACK.
The test runs a simulation with the small Stylized Johansen model [SJ].
Create a folder, for example, C:\TEMP, where you can do the test.
Copy the following files from the Examples subdirectory of your GEMPACK folder (probably C:\GP\EXAMPLES)
to your test folder (eg C:\TEMP):
SJ.TAB
SJ.HAR
SJLB.CMF
Open a command prompt (DOS box) by going Start..Run and type in "cmd" and hit OK.
This will start a command prompt running. Type in the command
cd /d C:\TEMP
to move to your test folder (assuming that you are testing in C:\TEMP). Then type
dir sj*.*
You should see that the example files listed above are in the test folder.
Step 1: running TABLO
Now type:
tablo -pgs SJ
You should see many messages flash past. If the messages end with
(Information file is 'C:\temp\SJ.inf'.)
 (The program has completed without error.)
  Total elapsed time is: less than one second.
go straight on to Step 2 below.
If on the other hand you see:
'tablo' is not recognized as an internal or external command,
operable program or batch file.
then the GEMPACK folder is
not
on your PATH. Please check the steps in
section
2.8
and then repeat this part of the testing.
If the messages ended with something like:
%% Stopping now because of fatal GEMPACK licence problem reported earlier.
  [Search for "%%" in the LOG file to see the earlier message.]
  (ERROR RETURN FROM ROUTINE: TABLO )
  (E-Licence information unavailable.)
  (The program terminated with an error.)
then your GEMPACK folder contains no licence (or the wrong licence). The error message will tell
you where TABLO looked for the licence file. Please check that your Release 12 licence file (it
must be called LICEN.GEM) is in your GEMPACK directory. If TABLO looks for LICEN.GEM in a
directory which is different from the one in which you installed GEMPACK, check the parts of
section
2.8
which relate to the Environment variable GPDIR. Repeat this testing once
you have remedied any problems.
Step 2: running GEMSIM
Assuming  Step 1 (TABLO) worked OK, type
gemsim -cmf sjlb.cmf
You should see many messages flash past, ending with
(The program has completed without error.)
  Total elapsed time is: less than one second.
 (Output has also been written to log file 'C:\temp\sjlb.log'.)
Congratulations — you have just run a simulation!
If this simulation does not work, start again  at section
2.2
.
If again you have problems, see section
2.5
.
If you have the Executable-Image version of GEMPACK, go straight on to section
2.6
.
If you have the Source-Code version of GEMPACK, you need to do the further tests in the next section.
2.4    [Source-code only] Re-Testing the Installation
[gpd6.5s]
This test agains runs a simulation with the small Stylized Johansen model [SJ]. However, while the
previous test used GEMSIM (useful whether you have either the Executable-Image or the Source-Code
version of GEMPACK), the next test uses a Tablo-generated program (SJ.EXE) to run the simulation.
You need the Source-Code version of GEMPACK to create Tablo-generated programs.
Again use the command prompt (DOS box) in your test folder, as described previously.
Step 1: running TABLO
Type in the command
tablo -wfp SJ
You should see messages flash past, ending with
Successful completion of TABLO.
  The program is
    'sj.for'.
  This program
      o can create the Equations file
      o can carry out multi-step simulations
  ************************************************
 (Information file is 'C:\temp\sj.inf'.)
  (The program has completed without error.)
  Total elapsed time is: less than one second.
Step 2: running LTG
Assuming  Step 1 (TABLO) worked OK, type
LTG SJ
You should see your Fortran compiler (Intel or GFortran) at work, ending with the message:
sj.EXE made successfully
If there is a problem, please check that you have installed Fortran correctly as described in section
2.1.5
.
Step 3: running a simulation with SJ.EXE
Assuming  Step 2 (LTG) worked OK, type
SJ -cmf sjlb.cmf
You should see many messages flash past. If the message ends with:
(The program has completed without error.)
  Total elapsed time is: less than one second.
 (Output has also been written to log file 'C:\temp\sjlb.log'.)
the test was successful and you should go on to section
2.6
.
2.5    If you still have problems
[witsend]
If, after re-checking all steps on the install procedure, you still have problems, please run ViewHAR and select
Help | About ViewHAR/Diagnostics | Diagnostics
Save this information in a file, and email it to support@gempack.com.
Be sure to describe just when and how the problem appeared.
2.6    More simulations to test GEMPACK and WinGEM
[gpd6.5.3]
After you have installed GEMPACK correctly, you will want to start using it! If you are new to
GEMPACK, we recommend that you work through the introductory Chapters
3
and
4
of the main GEMPACK manual.
To test that GEMPACK and WinGEM are working correctly, we suggest that you carry out the
simulations with Stylized Johansen in section
3.4
. If you have source-code GEMPACK,
run the simulations using a TABLO-generated program as described in section
3.5.2
. If
you have Executable-Image GEMPACK, use GEMSIM as described in section
3.5.3
. In
either case, check that the results of the simulation are as expected (see, for example, section
3.7
).
If any of these tests does not work, re-check the installation steps described above.
2.7    Working with GEMPACK
[gpd6.6]
The following sections contain other information relevant to working with GEMPACK.
2.7.1    New model's directory location
[gpd6.6.2]
We suggest that you put each new model you build in a separate directory on the hard disk, outside
of the GEMPACK directory (usually C:\GP). Your PATH setting should ensure that the GEMPACK
programs are found correctly. Conversely if your PATH and GPDIR are not set correctly, the GEMPACK
programs will not run.
When you use WinGEM with any model, make sure that you set WinGEM's working directory to point to
the directory containing the files for this model (as spelled out in section
3.4.2
).
2.7.2    [Source-code only] GEMSIM or TABLO-generated programs ?
[gpd6.6.3]
Both source-code and executable versions of GEMPACK allow you to use the program GEMSIM
to run TABLO programs which solve your model or perform other tasks. There are 2 stages:
TABLO:
first converting your TABLO program to GSS/GST files that GEMSIM can use.
GEMSIM:
to run a simulation or perform a calculation.
The source-code version of GEMPACK offers the alternate 3-stage approach of:
TABLO:
first converting your TABLO program to a Fortran program.
LTG:
then converting (compiling) the Fortran program to an EXE file.
RUN:
then running the EXE file to solve your model or perform another task.
Compared to GEMSIM, the TABLO-generated programs [EXE files] run faster with models that have a
large database (some CPU times are reported in Chapter
72
). However, the additional
LTG stage can take some time — this is roughly proportional to the size of the TAB file. If you
are going to run the EXE a number of times
1
, and if your model has a large database, you will soon recoup the

time spent doing LTG. But if you are:
in the model development stage, where you keep changing the TAB file;
running a model with a smaller database; or
running a program that merely manipulates data.
you may well find the simpler GEMSIM approach to be quicker.
2.7.3    Text editor
[gpd6.6.4]
When installing and using GEMPACK, you will need to be able to edit text files. This is best done
using a text editor (that is, an editor designed especially for handling text files).
We recommend that you use GEMPACK's text editor: TABmate. TABmate has syntax highlighting which is
helpful if you are writing or debugging TABLO Input files. TABmate can also be used for other text
files, can open several files at the same time and has various Tools which are useful for GEMPACK
development.
Other text editors include NotePad (which is supplied with Windows) and VIM and EMACS (which each
have their devoted followers). If you use a word processor (such as Microsoft Word) to edit text
files, be careful to save the resulting file as a text file.
2.7.4    If you installed in a new directory (not C:\GP)
[gpd6.4.3]
If you did NOT install GEMPACK in C:\GP, you may need to help some Windows programs to find and
use GEMPACK programs. For example, in RunDynam, click on the Options menu and use menu items such as Which
ViewSOL to use to tell the program which versions of ViewSOL, ViewHAR and AnalyseGE to use.
In RunGTAP, Click on Tools..Options and then use the various Change buttons to tell RunGTAP where to
find Gemsim, ViewHAR, ViewSOL, TABmate, AnalyseGE, Tablo etc.
2.7.5    If a program runs out of memory
[gpd6.6.5]
GEMPACK programs may require more memory than is available on your computer. If so you will
receive a message saying that the program is stopping because it is unable to allocate sufficient
memory. Often this error occurs because you have forgotten to condense your model, or have not
condensed it enough (see chapter
14
).
Other possible remedies include:
Free up more memory by closing down any other running applications; then try to rerun the task.
Buy more memory; however, 32-bit Windows cannot support more than 4 GB, and will only allocate 2
GB to a program.
If your PC has at least 4GB of memory and you are running 64-bit Windows,
check that you are running 64-bit GEMPACK [and for source-code, a 64-bit compiler].
2.7.6    Copying GEMPACK programs to other PCs
[gpd6.6.9]
If you have a GEMPACK site licence, you are entitled to install GEMPACK on PCs covered by your
site licence, for example, within the same department or institute. An individual GEMPACK licence
entitles you to install GEMPACK only on other PCs used by you.
You are allowed to send copies of your TABLO-generated programs to other people. However, such
programs may require an Introductory licence if they are used with a larger model. The model size
limits are set out in Chapter
62
.
Versions of TABLO and GEMSIM programs must match exactly. Hence, do not send GSS/GST files
generated by TABLO to others — the GSS/GST files would only work if used with the right GEMSIM
version (that matched your TABLO). Rather send only the TAB file — then the recipient can use
their matching TABLO and GEMSIM programs.
2.8    Manually setting the PATH and GPDIR
[gpd6.4.2]
For GEMPACK to run, you must make sure that the GEMPACK directory (usually C:\GP) is on your PATH,
and that the Environment variable GPDIR is set to the GEMPACK directory.
If you did not allow the installer to make changes to your PATH and the Environment variable GPDIR (see
section
2.2
), you must make the required changes yourself, as described next.
2.8.1    Checking and setting PATH and GPDIR
[gpd6.4.2.1]
The usual method to change the PATH and set the Environment variable GPDIR is by editing the System
Properties. The important changes are that
the directory into which you installed GEMPACK (the GEMPACK directory) must be on the system Path.
the system environment variable GPDIR must be set equal to the GEMPACK directory.
You will need administrator access to make these changes. Follow the steps below to check that
the installer made these changes, or to make them yourself:
For users of Windows 7 or later, if you are not using an administrator level account you will be
prompted for an administrator password during this procedure. Right click on Computer. From the
right click menu select Properties then click on the Advanced tab. This brings up the System
Properties dialogue window, click on Environment Variables to bring up the Environment Variables
dialogue window. Notice that the top half of the window contains user variables, the bottom
contains system variables.
Edit the system Path variable and add the GEMPACK directory, noting the following. Entries must be
separated by a semicolon ";". New entries may be added between any existing entries, however we
recommend adding to the beginning of the Path. For example, suppose your GEMPACK directory is
C:\GP, then the system path should look like C:\GP;C:\mingw-w64;%SystemRoot%... . If you have a
previous GEMPACK directory on the Path delete it and add the new GEMPACK directory to the
beginning of the system Path.
Add a new (or edit the existing) system environment variable GPDIR to have value set to the
GEMPACK directory. This must be the same directory you added to the beginning of the system Path
in the previous step.
Click on the Ok button to accept these changes to the Environment.
These changes will take effect when you next start a program or open a new command prompt. Test
these changes by opening a new command prompt and entering "SET". This should show the altered path and the
environment variable GPDIR.  If you don't see the changes you expect got to the environment
trouble-shooting section and work through the points in the next section
2.8.2
.
2.8.2    Trouble-shooting environment variables
[envvartrouble]
If you have made changes to the system Path or variable GPDIR which have had the effect you
expected, please try the following:
Reboot your computer and check the values of the system Path and GPDIR again, by opening a new DOS
box and entering "SET".  Usually this is not necessary, however on rare occasions we have noticed
that environment changes are slow to propagate to the rest of the system.
Check the user Path and GPDIR variables; if a value has been set for both a user and system
variable of the same name then, with the exception of the Path variable, the user variable will
dominate. This could explain why GPDIR does not have the value you expect. To check the values of
user variables for user account Jane for example, you must be logged on as Jane. On Windows 7 and
later you can edit the user variables by going to Control Panel, then find User Accounts which
depending on the display mode may be in the group User Accounts and Family Safety. From the User
Accounts dialogue window click on "Change my environment variables". Check that GPDIR is not set
as a user variable, if it is delete it. Bad user enironment variables are more likely to be a
problem for upgrade installations rather than new installations.
Check the values of the system Path and GPDIR variables by working through section
2.8.1
.
2.9    Technical Topics
[gpd6.7]
In this section we discuss various technical topics. We expect that most GEMPACK users can happily
ignore these.
2.9.1    [Source-code only] Running BuildGP
[gpd6.7.3]
The program BuildGP is designed to carry out the following tasks:
Check your system to see: if Fortran is installed, if there is enough disk space, whether the
licence is in the correct place, and if the PATH and GPDIR environment variables are correctly set.
Make the GEMPACK libraries by compiling many groups of subroutines.
Make the Fortran-based GEMPACK programs (executable images) by compiling the programs and
linking to the libraries.
Usually BuildGP does all these automatically when you install GEMPACK. However, there may be
situations when you need to run BuildGP yourself. For example, if you discovered a GEMPACK bug,
you might be sent a patch file to repair the problem. Detailed instructions would come with the
patch file. We provide only brief notes here.
Run the program BUILDGP.EXE in the GEMPACK directory from the command prompt or from My Computer
or Windows Explorer.
Check that BuildGP correctly displays your GEMPACK directory and compiler (GFortran or Intel).
Now click on the Start build button.
If you installed GEMPACK successfully with one compiler (say, GFortran), and you later wished to
use another compiler (say, Intel), you do not need to install again. It is enough to merely re-run
BuildGP. If you want to repeatedly switch between compilers, see the notes at
http://www.copsmodels.com/gpmultifort.htm
.
2.9.2    File association
[gpd6.6.7]
"File association" is the Windows mechanism due to which (for example):
the ViewHAR icon is displayed beside HAR files in Explorer
if you double-click a HAR file, it opens in ViewHAR
These happen because files suffixed HAR are "associated" with ViewHAR.exe.
Usually the "association" is set up at install time. Only one program can be
associated with each file type — so programs might compete to possess more
popular suffixes. To stop such contests, Windows may prevent a program from
changing an existing association. This may mean, for example, that the GEMPACK
installer cannot associate TABmate with TAB files (because Microsoft wants the
TAB suffix for Visual Studio). In such cases, you must set up the association
manually. You can change the HAR file association as
follows:
in Windows Explorer, right-click on a HAR file and choose Open with....
check box Always use the selected program should be ticked.
Use the Browse button to select the latest ViewHAR.exe.
2.9.3    Keep and Temporary directories and GEMPACK Windows programs
[gpd6.6.8]
Programs often need to have folders to store user configuration choices, or to write temporary files.
Windows provides default folders for these purposes.
GEMPACK Windows programs store user configuration choices in INI files which are (by default)
located below a folder chosen by Windows. We call that folder the "Keep" folder. For example, for user "John", the INI file
for TABmate might be located at:
C:\Users\John\My Documents\GPKEEP\TABmate\TABmate.ini
Similarly GEMPACK Windows programs by default write temporary files in a subdirectory
of the temporary folder provided by Windows
2
.
For very unusual cases, GEMPACK gives a way to avoid problems with the Keep and the default Temporary
directories by setting environment variables called GPKEEP and GPTEMP. Set a new environment
variable called GPKEEP if you want to change the usual Keep Directory. Set a new environment
variable called GPTEMP if you want to change the default temporary directory without changing the
environment variable TMP.
In RunGEM, WinGEM, AnalyseGE and RunDynam there are Menu Options within the programs which allow
you to set your Temporary directory to a directory of your choosing. The program remembers this
Temporary directory setting. When you start the programs for the first time, the default temporary
directory is set from the value of the TMP or TEMP environment variable.
If you are having problems with these features of one of the GEMPACK Windows programs, consult the
relevant Help file for details and advice.
2.9.4    Installing GEMPACK on a network
[gpd6.8]
Some organisations have found it desirable to run the  Source-code Version of GEMPACK
and the associated Fortran compiler from a network. For example, this can reduce the need for
separate copies of the compiler.
Below are some pointers to using GEMPACK and/or Fortran on a network.
Everyone needs read and execute permissions for the GEMPACK folder but only the administrator may need write
access.
GEMPACK programs do not write to any subdirectories of the Windows directory.
A range of
environment changes
, such as to PATH and GPDIR, will need to be made
for each user. The
Keep and Temporary directories
and the TMP or TEMP environment
variables need to point to folders that are unique to each user.
Input, temporary and output files for a simulation should be located on the PC which is running
the simulation — the aim is to avoid large amounts of data travelling over the network.
2.9.5    Uninstalling GEMPACK
[gpd6.7.6]
To uninstall GEMPACK from your computer, use the standard Add/Remove Programs method.
If that fails you could simply:
Delete the whole GEMPACK directory (and its subdirectories).
Remove the changes to your PATH and environment (see section
2.8.1
).
Delete any desktop links to GEMPACK programs.
2.9.6    Finding GEMPACK Version and Release Information
[identver]
Especially when troubleshooting, it may be useful to check which version of GEMPACK
(or of a particular GEMPACK program) you are using. You may wish to know the:
GEMPACK release no., such as 10.0,  11.2, or 12.0;
GEMPACK version
— either Executable-image or Source-code
GEMPACK licence type, which should  match your GEMPACK version.
Version no. for an individual program; for example TABmate Version 1.32
Most GEMPACK Windows programs (like ViewHAR and TABmate) give two methods to gather the
information above.
First
, the
GEMPACK Licence
command (usually under the Help Menu) shows:
the name of your licence file, which will be located in your GEMPACK folder.
the GEMPACK release no. of that licence file. Eg, A GEMPACK 10 licence can be used to run programs
from GEMPACK Release 10
or earlier
Releases.
the GEMPACK Version of that licence file — usually Executable-image or Source-code. An
Executable-Image licence will not suffice to use Source-Code GEMPACK.
whether your licence has expired or is size-limited to smaller models.
your licence details and no. (eg: GFM-0094). The last four digits of this are your customer no.
if TABLO.EXE is present in your GEMPACK folder, additional lines at the bottom of the Licence
Information window show the Version and Release information for that copy of TABLO.EXE — which
should match the Version and Release of your licence file.
Figure 2.1 GEMPACK licence command
Second
, the
About/Diagnostics
command (also usually under the Help Menu) shows:
the name and Version no. of the program; eg, ViewHAR Version 3.13
the location and filename of the EXE file
if TABLO.EXE is present in your GEMPACK folder,  the GEMPACK Version and Release information for that copy of TABLO.EXE
a Diagnostics button that displays much more information, which can be saved in a file.
If you have a problem, GEMPACK support may ask you to send them this "diagnostics file".
Figure 2.2 About/diagnostics
Program Version and GEMPACK Release Information for
Command-line or Fortran-based GEMPACK
programs
is contained in the first 4 or 5 lines of the log file (if there is one) or in the
first 4 or 5 lines of screen output when you run that program from the command-line. Usually this
information has scrolled off the top of the Command prompt window before you have time to read it.
You may need to scroll back to see it. Or, to capture the output to a file, type:
sltoht <nul: >temp.log
and then examine the top of file temp.log. You might see something like:
<SLTOHT   Version 5.52  January 2011>
   This program accesses some of the routines in the GEMPACK software release
 <GEMPACK Release 11.1.200   May 2012>
In ViewHAR the History command will show you Program Version and GEMPACK Release Information about
the program that created a HAR file
— see section
49.1
. The same information
is echoed to the log whenever a Command-line GEMPACK program reads a HAR file.
3    How to carry out simulations with models
[gpd1.2]
Click here
for detailed chapter contents
This chapter is where we expect new users of GEMPACK to start learning about
simulations. We describe how simulations are carried out, and explain some of
the terms used in GEMPACK, such as: implementation, simulation, levels and
percentage-change variables.
In section
3.1
, there is a very brief overview of the Stylized
Johansen model and the simulation that you will carry out. The rest of this
chapter consists of detailed instructions for carrying out the simulations and
interpreting their results.
We encourage you to work through this whole chapter before starting to work
with GEMPACK on your own model. At the end of this chapter we suggest different
directions you may wish to go in.
Implementation
A model is implemented in GEMPACK when
the equations describing its economic behaviour are written down in an algebraic form, following a
syntax described later in this document, and
data describing one solution of the model are assembled, to be used as a starting point for
simulations.
For most GEMPACK models, the equations are written down in a linearized form, usually expressed in
terms of percentage changes in the variables. But you can choose instead to write down
the original (or "levels") equations. In either case you need to write them down
in a text file which we call a
TABLO Input file
or
TAB file
, since TABLO is the name
of the GEMPACK program which processes this information.
The procedure for implementing models is described in detail in chapter
4
.
Simulation
Once a model is implemented, the model can be used to carry out simulations. Many simulations are
the answer to "What if" questions such as "If the government were to increase tariffs by 10
percent, how much different would the economy be in 5 years time from what it would otherwise have
been?".  From the original solution supplied as the starting point, a simulation calculates a new
solution to the equations of the model. GEMPACK usually reports the results of a simulation
as percentage changes from the original solution.  Levels results may also be available.
Solving models
within GEMPACK is always done in the context of a simulation. You specify the values of certain of
the variables (the exogenous ones) and the software calculates the values of the remaining
variables (the endogenous ones).
The new values of the exogenous variables are usually given by specifying the percentage changes
(increases or decreases) from their values in the original solution.
Levels and Percentage-Change Variables
When the model is implemented, the equations may be linearized (that is, differentiated). The
variables in these linearized equations are usually interpreted as percentage changes in the
original variables. The original variables (prices, quantities etc) are referred to as the
levels
variables and the (usually nonlinear) equations relating these levels variables are called the
levels equations.
For example, the levels equation
V  =  P Q
relates the dollar value V of a commodity to its price P ($ per ton) and its quantity Q (tons). The
linearized version of this is
p_V  =  p_P + p_Q
(as explained later in chapter
4
below) which says that, to first order, the
percentage change p_V in the dollar value is equal to the sum of the percentage changes p_P in the
price and p_Q in the quantity.
Data
The data for a model often consists of input-output data (giving dollar values) and parameters
(including elasticities). The data given are usually sufficient to read off an initial solution to
the levels equations. (Usually all basic prices are taken as 1 in the initial solution.)
3.1    An example simulation with stylized Johansen
[gpd1.2.1]
In this chapter we show you how to carry out simulations with an existing model (that is, one built
by someone else). We use as an example the Stylized Johansen model described in Chapter 3 of Dixon
et al (1992), hereafter referred to as
DPPW
. The model equations are listed in table
4.1
in section
4.1
.
The Stylized Johansen model is chosen because it is simple.
Once you know how to carry out simulations with it in GEMPACK, you will find it easy to carry out
simulations with other, more complicated models (including ones you build yourself).
3.1.1    Introduction to the stylized Johansen model
[gpd1.2.1.1]
The Stylized Johansen model is a very simple model of a single country. It recognises two
sectors "s1" and "s2" each producing a single commodity, one final demander (households) and two primary
factors (labor and capital). There are no exports or imports. Output of each sector is a Cobb-Douglas aggregate of
labor, capital, and intermediate inputs. Household demands are also Cobb-Douglas.
The initial input-output data base is shown below in Table
3.1
.
For example, households consume 4 (million)
dollars' worth of commodity 2 and industry 2 uses 3 (million) dollars' worth of labor. Note that
the first two row totals (value of sales each of good) equal the first two column totals (costs of each sector).
Table 3.1 Input-output data base for Stylized Johansen
Demanders:
Industry 1
Industry 2
Households
Total Sales
Inputs
Commodity
1
4.0
2.0
2.0
8.0
Commodity
2
2.0
6.0
4.0
12.0
Labor
3
1.0
3.0
4.0
Capital
4
1.0
1.0
2.0
Total Production
8.0
12.0
6.0
In the GEMPACK implementation, the levels variables are as in Table
3.2
below.
Table 3.2 Levels variables of Stylized Johansen
GEMPACK  variable
Meaning
DPPW
Notation
Y
Value of household income
Y
PC(i)
Price of commodity i
P
i
(i=1,2)
PF(f)
Price of factor f
P
f
(f=3,4)
XCOM(i)
Supply of commodity i
X
i
(i=1,2)
XFAC(f)
Supply of factor f
X
f
(f=3,4)
XH(i)
Household use of commodity i
X
i0
(i=1,2)
XC(i,j)
Intermediate input of commodity i to industry j
X
ij
(i,j=1,2)
XF(f,j)
Input of factor f to industry j
X
fj
(f=3,4;j=1,2)
DVCOMIN(i,j)
Dollar values for intermediate inputs
(i,j=1,2)
DVFACIN(f,j)
Dollar values for factor use by industry
(f=3,4;j=1,2)
DVHOUS(i)
Dollar values for household consumption
(i=1,2)
Note that most of the variables have one or more arguments (indicating associated sectors and/or
factors). We refer to such variables as
vector
or
matrix
variables.
For example, PC(i) is   a vector variable with 2 components, one for each sector, namely PC("s1") and
PC("s2"). XF(f,j) is a matrix variable with the following 4 components:
component 1 XF("labor","s1")
input of labor (factor 1) to sector 1
component 2 XF("capital","s1")
input of capital (factor 2) to sector 1
component 3 XF("labor","s2")
input of labor (factor 1) to sector 2
component 4 XF("capital","s2")
input of capital (factor 2) to sector 2
Variables which have no arguments ('Y' is the only one here) are referred to as
scalar
or
macro
variables.
Corresponding to each levels variables, there is an associated percentage change variable.
TABLO adds the prefix "p_" to the name of the levels variable to indicate a percentage change. For
example, p_XF is the percentage change in the levels variable XF.  In
DPPW
, lower case letters are
used to denote percentage-change variables.
More details about the model are given in chapter
4
. A full TABLO Input file can be
found in section
4.3.3
.
3.1.2    The simulation
[gpd1.2.1.2]
In the example simulation with the Stylized Johansen model used throughout most of this chapter, we
choose a closure in which supplies of the two factors, labor and capital, are the exogenous
variables. This means we will specify the percentage changes in the variable XFAC, namely p_XFAC,
and solve the model to find the percentage changes in all the other variables.  You will also be
able to see the levels results (for example, the post-simulation value of household income).
For this simulation, we increase the supply of labor by 10 per cent and hold the supply of capital
fixed.
The starting points for any simulation with the Stylized Johansen model are
the TABLO Input file, SJ.TAB, and
the data file, SJ.HAR.
3.2    Preparing a directory for model SJ
[gpd1.2.4.2]
We assume that you have already installed GEMPACK correctly as described in chapter
2
.
To keep all example files for the Stylized Johansen model together in one area,
you should first create a separate directory (folder)  for these files and copy the
relevant files into this directory.
Use  Windows Explorer (or My Computer) to create a new folder or subdirectory
called   \sj   and copy all the   sj*.*   files from the directory containing
the GEMPACK model examples (usually C:\GP\EXAMPLES) to this directory  \sj.
3.3    Using GEMPACK: WinGEM or command prompt?
[gpd1.2.3]
There are two ways of operating GEMPACK:
through the WinGEM interface. Initially this method is easier, since WinGEM
helps you with the names of the programs and files used by GEMPACK.
at the Command line, ie, working in a DOS box within Windows.  We will refer to
this method as
Command Prompt
. Many advanced users find this approach
quicker and more flexible. They use DOS commands but also launch Windows
programs such as TABmate, ViewHAR and ViewSOL from the command line.
We describe both methods, but suggest that you first work through this chapter using the WinGEM method — then, if you wish,
repeat the exercise using the Command prompt instructions which are shown like this:
Command-prompt users
should read (but not do) the WinGEM instructions, then should
execute the corresponding DOS commands, which will be shown just after the WinGEM instructions.
3.4    Stylized Johansen example simulation
[gpd1.2.4]
3.4.1    Starting WinGEM
[gpd1.2.4.1]
In Windows, double-click on the   WinGEM   icon to start GEMPACK for Windows.  The main WinGEM menu should appear, as a
ribbon menu across the top of the screen:
WinGEM  -  GEMPACK for Windows
File   Simulation   HA Files   Other tasks   Programs   Options   Window   Help
3.4.2    Setting the working directory
[gpd1.2.4.3]
WinGEM uses the idea of a working directory to simplify choosing files and running programs.  This
working directory is where all the files for the model you are using are stored.
For the Stylized Johansen model examples here, the working directory needs to be the directory \SJ
you have just created.  To set this, first click on
File
in the main WinGEM menu. This will
produce a drop-down menu. In the drop-down menu, click on the menu item
Change both default directories
.
The notation we use for this sequence of clicks (first
File
then
Change both default directories
) is
File | Change both default directories
.
In the file selection box that appears, choose drive
C:
(or the drive containing your directory
\SJ if it is on a different drive).  Then double-click on
C:\
(this will be at the top of the
list of directories shown) and then double-click on the subdirectory
SJ
.  [Make sure that the
directory name shown in blue above the selection box changes to C:\SJ  (or D:\SJ etc if your \SJ
directory is on another drive).]  Click on the
Ok
button.
Command-prompt users
should open a DOS box in the C:\sj directory.
1
3.4.3    Looking at the data directly using ViewHAR
[gpd1.2.4.4]
The input-output data used in the Stylized Johansen model are contained in the data file SJ.HAR.
This is a special GEMPACK binary file - called a Header Array file - so you cannot just look at it
in a text editor. Instead you will look at SJ.HAR using the ViewHAR program.
Select from the main WinGEM menu:
HA Files | View VIEWHAR
The ViewHAR window will appear. Click on
File | Open
and select the file SJ.HAR.
This will open the file SJ.HAR and show its contents on the Contents screen.
Command-prompt users
can open SJ.HAR by typing "viewhar SJ.HAR" into the DOS box.
Each row of the ViewHAR Contents screen corresponds to a different array of
data on the file. Look at the "Name" column to see what data are in these arrays.
Header
Type
Size
Name
1
CINP
RE
SECTxSECT
Intermediate inputs of commodities to ind.
2
FINP
RE
SECTxFACT
Intermediate inputs of primary factors - dollar
3
HCON
RE
SECT
Household use of commodities - dollar values
The first array is the "Intermediate inputs of commodities to industries - dollar values". The
Header
CINP
is just a label for this array (headers can have up to 4 characters). The array is of
Type
RE
— an array of real numbers with set and element labelling (see chapter
5.0.3
).
Double-click on
CINP
to see the numbers in this array.
DVCOMIN
s1
s2
Total
s1
4.00
2.00
6.00
s2
2.00
6.00
8.00
Total
6.00
8.00
14.00
Compare these numbers with the input-output data for Stylized Johansen shown in Table
3.1
. The actual data in the file at this header is just the 2x2 matrix.  ViewHAR
calculates and shows the row and column totals.
To return to the Contents Screen, click on
Contents
in the ViewHAR menu, or click twice on any number.
Look at the other Header Arrays called FINP and HCON to see where their numbers fit in the
input-output data base.
Close ViewHAR by selecting
File | Exit
.
3.5    Implementing and running model SJ
[gpd1.impsj]
There are three steps involved in carrying out a simulation using GEMPACK.
Step 1
- Implement the model (using TABLO)
Step 2
- Solve the equations of the model (ie, run a simulation)
Step 3
- View the results
3.5.1    TABLO-generated program or GEMSIM?
[gpd1.2.4.5]
The details of steps 1 and 2 vary according to whether you have the Executable-image or the Source-code version of GEMPACK.
With either version, you can use GEMSIM to run simulations.
The Source-code version also allows you to create a model-specific, TABLO-generated, EXE file,
which you can run to solve the model. Especially for larger models,
the TABLO-generated program will usually solve quicker.
The Source-code method is described next.
If you have the Executable-image version of GEMPACK, you will need to skip onto the
GEMSIM instructions in section
3.5.3
.
3.5.2    Source-code method: using a TABLO-generated program
[gpd1.2.4.6]
In the next examples we are assuming that you have the Source-code version of GEMPACK and have a
Fortran compiler on your DOS PATH.
From the WinGEM menu at the top of the screen choose
Simulation
.   In the drop-down menu the
choices are
TABLO Implement
Compile & Link
TABmate Implement
-------------------
Run TG Program
GEMSIM Solve
SAGEM Johansen Solve
---------------------
View Solution (ViewSOL)
AnalyseGE
The items from this menu you will be using in this simulation are
TABLO Implement
Compile & Link
Run TG Program
View Solution (ViewSOL)
.
In the TABLO-generated program method, the GEMPACK program TABLO is used to convert the algebraic
equations of the economic model into a Fortran program (.FOR file) specific to your model. This Fortran program
(which is referred to as the
TABLO-generated program
or
TG Program
in the above menu) is compiled
and linked to a library of GEMPACK subroutines. The EXE file of the TABLO-generated program
produced by the compiler is used to run simulations (instead of using the program
GEMSIM). This method provides faster execution times for large models than the GEMSIM alternative
but means you must have an appropriate Fortran compiler.
WinGEM will guide you through the various steps and indicate what to do next.
Step 1 - Implementing the model SJ using TABLO
Step 1(a) - Run TABLO to create the TABLO-generated program
The TABLO Input file is called SJ.TAB. It contains the theory of the Stylized Johansen model. Choose
Simulation | TABLO Implement
A window for TABLO will appear. Click on the
Select
button to select the name of the TABLO
Input file  SJ.TAB
2
. This is all TABLO needs to implement this model.
3
At top right of the TABLO window are choice buttons for
FORTRAN
and
GEMSIM
.
Check that the first,
FORTRAN
, option is selected (we want you to create the TABLO-generated
Fortran program).
Click on the
Run
button. The program runs TABLO in a DOS box and when complete, returns you
to the TABLO window with the names of files it has created: the Information file SJ.INF and the Log
file. Look at both of these files by clicking the
View
buttons beside them.
The Information file SJ.INF gives information about the TABLO Input file such as whether there are
any syntax or semantic errors during checking  by TABLO.
Search the file for
%%
to see if there are any errors. Search the file for "syntax error" to
see how many syntax errors and semantic problems there are (hopefully none). Go to the end of the
file to see what actions can be carried out by the TABLO-generated program produced in this TABLO
run.
Command-prompt users
can perform Step 1(a)  by typing "tablo  -wfp sj -log sj.log".
To see LOG or INF files, type "tabmate SJ.INF" or "tabmate SJ.LOG".
Step 1(b) - Compile and Link the TABLO-generated Program
When you have looked at these two files, click on the
Go to Compile and Link
button at the
bottom of the TABLO window to run the Fortran compiler. (Alternatively you can start this window by
choosing
Simulation | Compile and Link...
from WinGEM's main menu.)
In the Compile and Link window, the file SJ.FOR is already selected as the TG Program Name. Click
on the button
Compile and Link
and wait a little while the compiler converts the Fortran file
SJ.FOR into the SJ.EXE program that you can run.
When finished, click on the button
Go to 'Run TG Program'
to proceed to the next step in
running a simulation.
Command-prompt users
can perform Step 1(b)  by typing
"LTG sj". Type "dir sj.exe" to check that file SJ.EXE has been produced.
Step 2 - Solve the equations of the model using TABLO-generated program
The
Go to 'Run TG Program'
button takes you to the window for running
the TABLO-generated program SJ.EXE. (Alternatively you can start this window by
choosing
Simulation | Run TG Program...
from WinGEM's main menu.)
First
Select
the Command file called SJLB.CMF.  Since Command files are text files, look at
this Command file in the text editor by clicking the
Edit
button.
How is the closure specified? What shock is applied?
What data file is used by this model? How many steps are used in the multi-step solution?
Details about using a GEMPACK Command file to specify a simulation are given in section
3.8
below. For the present, we suggest that you take this on trust
and continue with the simulation.
Select
File | Exit
to close the editor and return to the "Run TG Program" window.
Click on
Run
to run SJ.EXE with the Command file SJLB.CMF.
When SJ.EXE finishes running, an accuracy summary window will pop up. This gives a
graphical view as to how accurately the equations have been solved
4
.

You can ignore this for the present (it is discussed in section
3.12.3
) so click OK.
If SJ.EXE produces the Solution file, click on
Go to ViewSOL
5
.
If there is an error, view the Log file.
Command-prompt users
can examine  the Command file SJLB.CMF by typing "TABmate SJLB.CMF".
Run the simulation  by typing "sj -cmf SJLB.CMF".
Then, to see the results, type "ViewSOL SJLB.SL4".
Now please skip the next (GEMSIM) section and go on to the ViewSOL instructions in
3.5.4
.
3.5.3    Executable-image method: using GEMSIM
[gpd1.2.4.7]
In the WinGEM menu at the top of the screen choose
Simulation
.   In the drop-down menu the
choices are
6
.
TABLO Implement
Compile & Link
TABmate Implement
-------------------
Run TG Program
GEMSIM Solve
SAGEM Johansen Solve
---------------------
View Solution (ViewSOL)
AnalyseGE
The items from this menu you will be using in this simulation are
TABLO Implement
GEMSIM Solve
View Solution (ViewSOL).
WinGEM will guide you through the various steps and indicate what to do next.
Step 1 - Implementing the model SJ using TABLO (for GEMSIM output)
The TABLO Input file is called SJ.TAB. It contains the theory of the Stylized Johansen model. Choose
Simulation | TABLO Implement...
A window for TABLO will appear. Click on the
Select
button to select the name of the TABLO
Input file  SJ.TAB
7
.  This is all TABLO needs to implement this model
8
.
At top right of the TABLO window are choice buttons for
FORTRAN
and
GEMSIM
.
Check that the second,
GEMSIM
, option is selected (we want you to create the GEMSIM Auxiliary
files).
By "implement" we mean convert the TABLO Input file into binary computer files which are used by
the simulation program GEMSIM in the next step. These files are referred to as Auxiliary files (or
sometimes as the GEMSIM Statement and Table files) and in this case, are called SJ.GSS and SJ.GST.
Click on the
Run
button. The program TABLO runs in a DOS box and when complete returns you
to the TABLO window with the names of files it has created: the Information file SJ.INF and the Log
file. Look at both of these files by clicking the
View
buttons beside them. To close the file,
click on the X in the top right-hand corner of the view, or click
File..Exit
using the File menu.
The Information file SJ.INF gives information about the TABLO Input file such as whether there are
any syntax or semantic errors found during checking by TABLO.
Search the file for   %%   to see if there are any errors. Search the file for "syntax error" to
see how many syntax errors and semantic problems there are (hopefully none). Go to the end of the
file to see what actions GEMSIM can carry out with the Auxiliary files produced in this TABLO run.
When you have looked at these two files, click on the
Go to GEMSIM
button at the bottom of the
TABLO window to go on to the next step in running a simulation:
Command-prompt users
can perform Step 1  by typing "tablo  -pgs sj -log sj.log".
To see LOG or INF files, type "tabmate SJ.INF" or "tabmate SJ.LOG".
Step 2 - Solve the equations of the model using GEMSIM
The
Go To GEMSIM
button takes you to the GEMSIM window. (Alternatively
you can start this window by choosing
Simulation | GEMSIM Solve
from
WinGEM's main menu.)
First
Select
the Command file called SJLB.CMF.  Since Command files are
text files, look at this Command file in the text editor by clicking the
Edit
button.
How is the closure specified? What shock is applied?
What data file is used by this model? How many steps are used in the multi-step
solution?
Details about using a GEMPACK Command file to specify a simulation are given
in section
3.8
below.  For the present, we
suggest that you take this on trust and continue with the simulation.
Select
File | Exit
to close the editor and return to the GEMSIM window.
Click on
Run
to run GEMSIM with the Command file SJLB.CMF.
When GEMSIM finishes running, an accuracy summary window will pop up. This gives a
graphical view as to how accurately the equations have been solved
9
.

You can ignore this for the present (it is discussed in section
3.12.3
) so click
OK
.
If GEMSIM produces the Solution file, click on
Go to ViewSOL
10
.
If there is an error, view the Log file.
Command-prompt users
can examine the Command file SJLB.CMF by typing "TABmate SJLB.CMF".
Run the simulation  by typing "sj -cmf SJLB.CMF".
Then, to see the results, type "ViewSOL SJLB.SL4".
3.5.4    Step 3 - View the Solution using ViewSOL
[gpd1.2.viewsol]
You cannot view the Solution file SJLB.SL4 in a text editor because
it is a binary file, not a text file. Instead we use ViewSOL to examine the Solution file.
In WinGEM, the
Go to ViewSOL
button starts the program ViewSOL running and opens the Solution file
SJLB.SL4 .  [Alternatively you can start this window by choosing
Simulation | View Solution (ViewSOL)
from WinGEM's main menu.]
Command-prompt users
should type "ViewSOL SJLB.SL4".
You will see the Contents page listing many of the variables of the model.  ViewSOL has 3 slightly
different formats for this Contents list.  Select
Format...
from ViewSOL's main menu and there
click on
Arrange vectors by name
(in the panel headed Vector options); then click
Ok
which
will put you back to the Contents list.
To see the results of one of these variables listed by name, just double-click on the corresponding
row in the Contents list.  First double-click on the p_XCOM row to see the results for this
variable (demand for the two commodities).  Select 3 decimal places (see the third drop-down list
box along the top row of the current ViewSOL window - the only one with a single figure in it).
Then you should see something like the following:
p_XCOM
sjlb
Pre sjlb
Post sjlb
Ch/%Ch sjlb
s1
5.885
8.000
8.471
0.471
s2
6.899
12.000
12.828
0.828
Across the s1 row you see the percentage change result (5.885%), the pre-simulation levels value
(8.000), the post-simulation levels value (8.471) and the change (0.471); these are the results for
the total supply of commodity s1.
Then click on
Contents
to return to the Contents list.
To see the p_XFAC results, double-click on this row.  You will see
p_XFAC
sjlb
Pre sjlb
Post sjlb
Ch/%Ch sjlb
labor
10.000
4.000
4.400
0.400
capital
0
2.000
2.000
0
This time all the numbers are in red which is used to remind you that, for this simulation, both
components of this variable p_XFAC are exogenous.  You should easily be able to understand all of
these results.
Then click on
Contents
to return to the Contents list (or click twice on any number).
To see the p_XC(i,j) results [intermediate inputs of commodity i into industry j], double-click on
this row.  Now you see
p_XC
s1
s2
s1
5.885
5.885
s2
6.899
6.899
and, in the second drop-down box you should see
"1  sjlb"
.  This indicates that you are just
seeing the linearized simulation results (the percentage changes in the four components of this
variable).  You can't see the pre- and post-simulation levels results at the same time since this
variable p_XC is a matrix variable.  To see the pre-simulation levels results, click on the second
drop-down list box (the one showing "1  sjlb") and select the second alternative ("2 Pre sjlb").
Then you will see the pre-simulation levels results.  You might also like to look at the
post-simulation levels results and the changes.
Then click on
Contents
to return to the Contents list.
When you have finished looking at the results, exit from ViewSOL.
3.6    The steps in carrying out a simulation
[gpd1.2.5]
This section recapitulates the steps (that you just followed) to implement a model and carry out a simulation.
In all cases, after the TABLO Input file for a model has been written, there are 3 steps on the
computer to carry out a first simulation with the model. These steps are:
Step 1
- Implement the model
Step 2
- Simulation (Solve the equations of the model)
Step 3
- View the results with ViewSOL or perhaps AnalyseGE.
Step 1 always involves running the program TABLO.
The details of Steps 1 and 2 are a little different depending on whether you have a Source-code or
Executable-image version of GEMPACK, as we explain below.
Next we describe the Source-code procedure. The Executable-image version of steps 1 and 2
is described in section
3.6.2
.
3.6.1    Steps 1 and 2 using a TABLO-generated program (source-code GEMPACK)
[gpd1.2.5.1]
The steps are illustrated in Figure
3.1
below.
Figure 3.1 The steps in carrying out a simulation using a TABLO-generated program
Step 1. Computer Implementation of the Model
Step 1(a) - Run TABLO to create TABLO-generated program
Process the TABLO Input file for the model by running the program TABLO.  Select the option WFP
which tells TABLO to write a Fortran program (referred to as the TABLO-generated program of the
model) which captures the theory of the model.
Step 1(b) - Compile and Link the TABLO-generated program [LTG]
Compile and link the TABLO-generated program of the model, produced in Step 1(a). This will produce
an EXE file of the TABLO-generated program
11
.
Step 2. Simulation (Solve the equations of the model)
Run the EXE file of the TABLO-generated program, as produced in Step 1(b). Take inputs from
a Command file which tells the program which base data files are to be read and describes the
closure (that is, which variables are exogenous and which are endogenous) and the shocks.  This
program then computes the solution to your simulation and writes the results to a Solution file
Step 3. Printing or Viewing the Results of the Simulation
The last step is to view simulation results with ViewSOL or AnalyseGE
12
. An alternative is to use the program SLTOHT to process results (for example, to produce tables

for reports), as introduced in section
3.10
below.
3.6.2    Steps 1 and 2 using GEMSIM
[gpd1.2.5.2]
The steps using GEMSIM are illustrated in
Figure
3.2
.
Figure 3.2 The steps in carrying out a simulation using GEMSIM
Step 1. Computer Implementation of the Model
Process the TABLO Input file for the model by running the GEMPACK program TABLO. Select the option
PGS which asks TABLO to produce the GEMSIM Auxiliary files for the GEMPACK program GEMSIM (see Step
2). These files capture the theory of the model, as written in the TABLO Input file.
Selecting option PGS rather than the option WFP as in section
3.6.1
above is what
initiates the GEMSIM route rather than the TABLO-generated program route.
Step 2. Simulation (Solve the equations of the model)
Run the GEMPACK program GEMSIM
13
and tell it to use the GEMSIM Auxiliary (GSS/GST) files produced in Step 1.
Take inputs from a Command file which tells the program which base data files are to be read and
describes the closure (that is, which variables are exogenous and which are endogenous) and the
shocks. GEMSIM then computes the solution to your simulation and writes the results to a Solution
file.
Step 3. Printing or Viewing the Results of the Simulation
The last step is to view simulation results with ViewSOL or AnalyseGE
14
. An alternative is to use the program SLTOHT to process results (for example, to produce tables

for reports), as introduced in section
3.10
below.
Comparing the steps in the two cases
Note that Step 1 above is very similar to Step 1(a) in the TABLO-generated program case (see
section
3.6.1
above). The LTG step 1(b) in section
3.6.1
has no analogue in the
GEMSIM case since GEMSIM is a general-purpose program which can be used to solve any model. Step 2
is different only in that GEMSIM is run rather than the TABLO-generated program. Step 3 is
identical in the two cases.
3.6.3    Other Simulations
[gpd1.2.5.othsims]
Once you have carried out one simulation with a model, you will probably want to carry out others,
for example, to change the closure and/or shocks, or even to run from different base data. In such
cases, you do not have to repeat Steps 1(a) and 1(b). All you have to do is carry out Steps 2 and
3. A hands-on example is given in section
3.11
below. (Of course Step 1
must be repeated if you change the TABLO Input file in any way.)
3.7    Interpreting the results
[gpd1.2.7]
You have already looked at the results via ViewSOL (see Step 3 in
section
3.5.4
). From the ViewSOL
Contents page you clicked on and examined variables such as Macros, p_XH, p_PC, p_XF, p_DVHOUS. We have copied
some of the results from ViewSOL to a spreadsheet (via the Copy menu item in ViewSOL). These are
shown in Table
3.3
below.
We think that you will find the tables fairly easy to interpret.
Table 3.3 Results (ViewSOL) from the solution file SJLB.SL4
Macros
sjlb
Pre sjlb
Post sjlb
Chng sjlb
p_Y
5.8853
6.0000
6.3531
0.3531
p_XH
sjlb
Pre sjlb
Post sjlb
Chng sjlb
s1
5.8853
2.0000
2.1177
0.1177
s2
6.8993
4.0000
4.2760
0.2760
p_PC
sjlb
Pre sjlb
Post sjlb
Chng sjlb
s1
0.0000
1.0000
1.0000
0.0000
s2
-0.9486
1.0000
0.9905
-0.0095
p_XF
s1
s2
labor
10.0000
10.0000
capital
0.0000
0.0000
p_DVHOUS
sjlb
Pre sjlb
Post sjlb
Chng sjlb
s1
5.8853
2.0000
2.1177
0.1177
s2
5.8853
4.0000
4.2354
0.2354
The results show what happens if the supply of labor is increased by 10 per cent and the supply of
capital is held fixed. For example,
Look at the simulation result for 'p_Y', the percentage change in the levels variable 'Y'. The
dollar value of total nominal household expenditure will increase by 5.8853 per cent from its
pre-simulation value  of  6.0000 to its post-simulation value of 6.3531.
Look at the results for p_XH. The result for commodity 2, p_XH ("s2"), shows that households will
consume 6.8993 per cent more of commodity 2 than they did previously.
Look at the results for p_PC. The price of commodity 2 will fall by 0.9486 per cent.
The simulation results for p_DVHOUS show that the dollar value of household consumption of
commodity 2 will rise by 5.8853 per cent from its pre-simulation value of  4.0000 to its
post-simulation value of 4.2354.
Recall that, within GEMPACK, all simulations are set up and solved as perturbations from an initial
solution, and results are usually reported as changes or percentage changes from this original
solution. In this case the original solution values are as shown in Table
3.2
above, which shows million dollar values of activity.  Suitable levels values for quantities can be
obtained by assuming that, initially,
all prices are 1.
(This just sets the units in which quantities are measured.) Then, for example, since households
consume 4 million dollars' worth of commodity 2, this means that they consume 4 million units of
that commodity.
Hence the three simulation results mentioned above mean that, once labor is increased by 10 per
cent and capital is held fixed:
1.
Total nominal household expenditure Y has increased to approximately 6.353 million dollars
(5.8853 per cent more than the original value of 6 million dollars).
(The other three values given with p_Y in Table
3.3
are
6.0000
which is the pre-simulation level of Y,
6.3531
which is the post-simulation level of Y and
0.3531
the change between these two values.)
2.
Household consumption (XH) of commodity 2 has increased to 4.2760 million units (6.8993 per cent
more than the original 4 million units).
3.
The commodity price (PC) of commodity 2 has fallen from one dollar per unit to approximately
99.051 cents per unit (a fall of 0.9486 per cent).
4.
The dollar value of household consumption (DVHOUS) of the commodity produced by sector "s2" has
risen from 4 million dollars to approximately 4.2354 million dollars (an increase of 5.8853 per
cent).
The updated values in (2), (3) and (4) above should be related since dollar value should equal
price times quantity.  The levels equation for commodity 2 ("s2") is
DVHOUS("s2") = PC("s2) x XH("s2")
Note that this equation is true for the post-simulation values, since, from (2) and (3) above, the
post-simulation price times the post-simulation quantity is
0.99051 x 4.2760 = 4.2354
which is equal to the post-simulation dollar value in (4). This confirms that the solution shown in
ViewSOL satisfies the levels equation connecting price,
quantity and dollar value of household consumption of this commodity. You might like to check some
of the other levels equations in this way.
3.8    Specifying a simulation
[gpd1.2.8]
In order to specify the details for carrying out a simulation, you must
say which model to use,
say which base data to begin from (that is, the pre-simulation solution),
say which closure (that is, which variables are endogenous and which are exogenous), and
say which variables to shock, and by how much, and
specify the names of the various output files.
Figure 3.3 The information required to specify a simulation
Within GEMPACK, the normal way of specifying this information to the software is via a Command (CMF)
file.  Indeed, when you carried out the example simulation above, this is exactly what happened in
Step 2 above since there you ran either the TABLO-generated program or GEMSIM and took inputs from
the Command file SJLB.CMF.
The instructions in this Command file must be prepared in advance in a text editor.
The next  section explains the statements in this GEMPACK Command file SJLB.CMF.
3.8.1    Specifying a simulation via a GEMPACK command file
[gpd1.2.8.1]
In Step 2 of the example simulation, the program took all the information required to specify the
simulation from the GEMPACK Command file SJLB.CMF. The file SJLB.CMF is shown in full in Figure
3.4
below.
Figure 3.4 The GEMPACK command file SJLB.CMF
! The following GEMPACK Command file (usually called SJLB.CMF)  
!  carries out a multi-step simulation 
!  for the Stylized Johansen model.  
!  Auxiliary files (usually tells which TAB file)
auxiliary files = sj ;  
! Data files
file iodata = SJ.HAR ;
updated file iodata = <cmf>.upd ;  
! Closure
exogenous p_xfac ;
rest endogenous ; 
! Solution method information
method = euler ;
steps = 1 2 4 ;
! Simulation part
! Name of Solution file is inferred from name of Command file
! (See section
20.5
.)
shock  p_xfac("labor") = 10 ;  
verbal description =
Stylized Johansen model. Standard data and closure.
10 per cent increase in amount of labor. (Capital remains unchanged.) ;
! Options.extrapolation accuracy file = yes ;
log file = yes ;
! End of Command file
The statements in SJLB.CMF are discussed briefly below.
The statement
auxiliary files = sj ;
tells GEMSIM or the TABLO-generated program to use the Auxiliary files produced in Step 1. (This
effectively tells which TABLO Input file (or model) to work with, since these files are just a
processed version of the TABLO Input file SJ.TAB for the Stylized Johansen model.)  [If you are
using the TABLO-generated program SJ.EXE, the Auxiliary files are SJ.AXS and SJ.AXT produced when
you ran TABLO in Step 1.  If you are using GEMSIM, the Auxiliary files are SJ.GSS and SJ.GST
produced when you ran TABLO in Step 1.]. You can find more details about these Auxiliary files in
21
.
The statement
file iodata = SJ.HAR ;
tells SJ.EXE or GEMSIM to read base data from the file SJ.HAR (which contains the data in Table
3.1
above).
The line
! Data files
above this line is a comment since it begins with an exclamation mark  !.  While such comments are
ignored by the software, they are very important in organising and documenting the Command file and
in making it an intelligible record of the simulation.  [You can see several other comment lines in
the file.]
The statements:
exogenous p_xfac ;
rest endogenous ;
give the closure (that is, which variables to take as exogenous and which to take as endogenous),
while the statement
shock p_xfac("labor") = 10 ;
gives the shock needed to increase the supply of labor by 10 per cent.
When the TABLO-generated program SJ or GEMSIM carries out a simulation, as well as being able to
report the changes in the endogenous variables, the program produces an updated version of the
original data file(s). The data in these updated data files represent post-simulation values (that
is, the ones that would hold after the shocks have worked their way through the economy). For
Stylized Johansen, this contains post-simulation dollar values of the entries in Table
3.1
above. The statement
updated file iodata = <cmf>.upd ;
names the file to contain this updated data [examined in section
3.9
below]. The
<cmf> in this line indicates that this part of the name comes from the name of the Command
file. Since the Command file is usually called SJLB.CMF, the program replaces <cmf> by SJLB
(the name of the Command file ignoring its suffix .CMF) so that the updated iodata file will be
called SJLB.UPD. The <cmf> syntax is explained further in section
20.5
.
The most important output from a simulation is the Solution file which contains the results for the
percentage changes in prices and quantities. Here we have omitted the name of the Solution file so
the name of this file is taken from the name of the Command file. Because the Command file is
called SJLB.CMF, the Solution file will be called SJLB.SL4 (the same basic name SJLB followed by
.SL4 which is the standard GEMPACK suffix for Solution files). Another alternative is to add a
statement of the form
solution file = ... ;            ! Not included in this SJLB.CMF
in the Command file. Such a statement is allowed, but it is customary to omit it so that the name
of the Solution file is inferred from the name of the Command file.
You are required to give a verbal description of the simulation. This description, which can be
several lines of text, goes on the Solution file and is visible from ViewSOL
and other programs. You can use this to remind yourself (and others) about salient
features of the simulation. The statement
verbal description = .Stylized Johansen model. 
 Standard data and closure.
 10 per cent increase in amount of labor (Capital remains unchanged.)
 1,2,4-step solutions plus extrapolation. ;
in SJLB.CMF give 4 lines of text for the verbal description in this case. The semicolon ';'
indicates the end of this description — indeed all statements in GEMPACK Command files must end
with a semicolon ';'.
With GEMPACK, you can choose one of 4 related solution methods for each simulation. These are
introduced in section
3.12.3
below. The statements
method = euler ;
steps = 1 2 4 ;
in the Command file tell the program to use Euler's method based on 3 separate solutions using 1, 2
and 4 steps respectively. (See section
3.12.3
below for an explanation about step
numbers.)
The accuracy of the solution depends on the solution method and the numbers of steps. SJ.EXE or
GEMSIM can be asked to provide information about the accuracy on an Extrapolation Accuracy file.
The statement
extrapolation accuracy file = yes ;
asks the program to produce such a file. The information on this file is described in section
3.12.3
below. (The name of this file is the same as that of the Solution file except
that it has a different suffix, namely '.XAC', which makes the full name SJLB.XAC.)
The statement
log file = yes ;
asks the software to produce a LOG file showing all the screen activity as the program runs.  This
LOG file is called SJLB.LOG - it takes its name from the name SJLB.CMF of the Command file but
changes the suffix from .CMF to .LOG.  This LOG file is a useful record of the simulation.
Further details of Command files and running simulations are given in chapters
19
and following,
which describe running simulations with
GEMSIM, TABLO-generated Programs and SAGEM. A summary of the statements that can be used in a
GEMPACK Command file for running TABLO-generated programs or GEMSIM is given in chapter
35
.
In particular, we know that new users of GEMPACK find the auxiliary files (the statement above is
"auxiliary files = sj ;") and the file statements (the statements above are "file iodata = SJ.HAR;
" and "updated file iodata = <cmf>.upd ;") confusing initially. More details about these can
be found in chapters
21
and
22
.
3.9    The updated data - another result of the simulation
[gpd1.2.9]
Once the simulation shocks have worked their way through the economy, prices and quantities change
(as reported by the simulation results). These price and quantity changes imply changes in the
values contained in the original data base for the model. When you carry out a simulation, the
GEMPACK programs compute these new values. These new values are written to a file which is referred
to as the updated data or post-simulation data.
As you saw in section
3.8
above, the line
updated file iodata = <cmf>.upd ;
in the Command file SJLB.CMF means that, when you ran the simulation, the software produced the
updated data file  SJLB.UPD.  This file contains the data as it would be after the shocks (in this
case, the increase in labor supply) have worked their way through the model.
You learned in section
3.4.3
how to use ViewHAR  to look at the
base (or pre-simulation) data file SJ.HAR. This file is the starting point for the simulation; and,
when you look at this file you see the numbers shown in Table
3.1
above.
You can also use ViewHAR to look at the updated data in file SJLB.UPD.
If you are using WinGEM, select from the main WinGEM menu :
HA Files | View VIEWHAR
.
The ViewHAR window will appear. Click on
File | Open...
and select the file SJLB.UPD.
Command-prompt users
can open SJLB.UPD by typing "viewhar SJLB.UPD" into the DOS box.
In ViewHAR's contents screen, each  row corresponds to a different array of data on the file. Look at the column under the
heading "Name" to see what data are in these arrays. Look at values within the three arrays.
You can check that these post-simulation values are consistent with the results of the simulation
as discussed in section
3.7
above.  For example, the p_DVHOUS results in Table
3.3
show that the value of household expenditure on commodity s2 increased by
5.8853 percent from its pre-simulation value of 4 to its post-simulation value of 4.2354 (which
agrees with the Commodity 2 Households value in the table above).
The most obvious results of a simulation are the percentage changes in the variables.  The updated
data (which is always obtained when you run a simulation) is another important "result" of the
simulation, one which is sometimes overlooked.  You can look at this updated data to see how the
data base has changed as a result of the simulation.
3.10    Preparing tables and graphs for a report
[gpd1.2.10]
When you have run some simulations and analysed the simulation results, the
next step is usually to write a report containing a selection of the results in
tables or graphs.
This section describes how you can transfer simulation results into a
spreadsheet program, such as Microsoft Excel. You can use the  spreadsheet
program to produce tables and graphs which  can be copied and pasted into your
report.
All the examples below start with the Solution file for Stylized Johansen SJLB.SL4 created in the
example simulation described above.
Example 1 illustrates how to copy directly from ViewSOL into the spreadsheet program.
Examples 2 and 3 use the command-line program SLTOHT which is
documented in sections
39
and
40
.
Once you have suitable tables in your spreadsheet program, you can use it to create graphs of the results.
3.10.1    Example 1:  Copying from ViewSOL to Spreadsheet and WordProcessor
[gpd1.2.viewsolexport]
Open file SJLB.SL4 in ViewSOL. Select
Format
and then select
Arrange vectors by
size and set
.
In Contents screen, click on the line
Vectors size: 2  SECT 4
The Data Window shows the results for all vector variables which range over the set SECT. Use the Decimal Places
list box (in middle of upper toolbar) to display at least 4 decimal places.
In the ViewSOL menu, select
Export | Copy
. This copies the table of numbers to the clipboard.
Open your spreadsheet program and paste into a new spreadsheet. Use the spreadsheet editing to make
the table ready for the report. Copy the table from your spreadsheet and paste it into the report
document in your word processor, in the usual Windows way. You should see a table like the
following.
p_DVHOUS
p_PC
p_XCOM
p_XH
s1
5.8853
0
5.8853
5.8853
s2
5.8853
-0.9486
6.8993
6.8993
ViewSOL has many different Formats that you can use to set up the data to export. Consult the
ViewSOL Help for details.
3.10.2    Example 2:  Using the GEMPACK Program SLTOHT and Option SSS
[gpd1.2.sltoht1]
In the previous example, you interactively pasted from ViewSOL into a spreadsheet
the results for
one
variable.
The SLTOHT method, described here, is more fiddly to set up. However, once you have created
a
Spreadsheet Mapping file
(see below) you can, in one operation, import results for
many
variables
into a spreadsheet. This means that you can automate the production of quite complex reports.
SLTOHT produces a CSV (Comma Separated Value) file. This is a text file which can be opened in your
spreadsheet program to import the numbers generated by the simulation. Many arrays, even big arrays with many
rows and columns, can be imported, and then (perhaps after some reformatting) moved to your report.
In your text editor, create the file  sj1.map  which contains just the two lines:
p_xcom
p_xf
This is an example of a Spreadsheet Mapping file (see sections
39.3
and
40.1
) used by the program SLTOHT to pick out particular variables on the Solution file.
If you are working in WinGEM, select from the main WinGEM menu
Other tasks... | Solution file to Header/Text (SLTOHT)
Click on the
Select
button and choose the Solution file  SJLB.SL4.
Choose to print
Totals solutions
. Click the
Ok
button.
In the SLTOHT window, select from the menu
Options | SLTOHT Options
.
A screen of SLTOHT option choices will appear. Click on
SSS    Short SpreadSheet output
and select a Comma as separator. (A comma is the default choice.)
Click on
Ok
to accept these options and return to the main SLTOHT screen.
In the SLTOHT window, select from the menu
Options | Use mapping file
and select the file SJ1.MAP.
Run
the program SLTOHT. This will create the CSV text file called SJLB.CSV. When the program has
completed,
View
the text file SJLB.CSV, which is shown below (after the Command prompt case).
Command prompt Users
can start SLTOHT running by typing "sltoht"
and entering the responses:
SSS      ! Option SSS   
,        ! Data separator is a comma
-SHL     ! Do not include levels results
<carriage-return>    ! Finish option selection
sjlb     ! Name of Solution file
c        ! Cumulative totals
y        ! Yes, use an existing Spreadsheet mapping file
sj1.map  ! Spreadsheet mapping file name
sjlb.csv  ! Name of Output file (CSV)
Look at the file sjlb.csv in your text editor.
The output in file  sjlb.csv  should look like the box below with the labels and numbers separated
by commas. Only the values for variables p_XCOM and p_XF are shown because these were the only two
variables in the Spreadsheet Mapping file.
CSV file SJLB.CSV
Solution,sjlb,
 p_XCOM(s1),  5.8852696    ,
 p_XCOM(s2),  6.8992925    ,
 p_XF(labor:s1),  9.9999990    ,
 p_XF(capital:s1),-4.48017488E-07,
 p_XF(labor:s2),  10.000002    ,
 p_XF(capital:s2), 4.48017488E-07,
Start your spreadsheet program (for example Excel) and open the file SJLB.CSV (as a text file with
commas for separators). If you format the number cells to show three decimal places, you get a
neat spreadsheet table with the labels in one column and the values in the second column. (In a
report you would probably want to replace the column of labels with more meaningful labels.)
Document table
Solution
sjlb
p_XCOM(s1)
5.885
p_XCOM(s2)
6.899
p_XF(labor:s1)
10.000
p_XF(capital:s1)
0.000
p_XF(labor:s2)
10.000
p_XF(capital:s2)
0.000
3.10.3    Example 3:  Using the Program SLTOHT and Option SES
[gpd1.2.sltoht2]
There are various different options available in SLTOHT used to produce different kinds of tables
as described in chapter
40
. Option SES (Spread Sheet with Element labels) produces
a table of results using the element names as row and column labels.
In your text editor, create the file  sj2.map  which contains just the two lines:
p_xcom : p_pc
p_xc
If you are using WinGEM, in the SLTOHT window, select from the WinGEM menu
Options | SLTOHT Options
. A screen of SLTOHT option choices will appear. Click on
SES
and select a Comma as separator. (A comma is the default choice.)
Click on
Ok
to accept these options and return to the main SLTOHT screen.
In the SLTOHT window, select from the menu
Options | Use mapping file
and select the file SJ2.MAP.
Run
the program SLTOHT.
SLTOHT will tell you that, by default, this will produce output file SJLB.CSV which already exists.
[You created it in Example 2 above.] Click on
Yes
to say that you wish to change the name of the
output file, and choose the name  SJLB2.CSV.
When the program has completed,
View
the text file SJLB2.CSV, which is shown below (after the
Command prompt case).
Command prompt Users
can start SLTOHT running by typing "sltoht"
and entering the responses:
SES      ! Option SES 
,        ! Data separator is a comma
-SHL     ! Do not include levels results
<carriage-return>    ! Finish option selection
sjlb     ! Name of Solution file
c        ! Cumulative totals
y        ! Yes, use an existing Spreadsheet mapping file
sj2.map  ! Spreadsheet mapping filename
sjlb2.csv  ! Name of Output file (CSV)
Open the file  sjlb2.csv  in your spreadsheet program. The values for variables p_XCOM and p_PC are
shown side by side and then the array p_XC is shown below, all with element labels.
! Table of 2 variables.
p_XCOM
p_PC
s1
5.885
0.000
s2
6.899
-0.949
! Variable p_XC # Intermediate inputs of commodity i to industry j #
! Variable p_XC(SECT:SECT) of size 2x2
s1
s2
s1
5.885
5.885
s2
6.899
6.899
You can import either of these tables into your word processor.
3.10.4    Graphs
[gpd1.2.10.1]
Once you have suitable tables in your spreadsheet program, you can use it to create graphs of the results.
Alternatively the Charter program supplied with GEMPACK (see section
36.2.1
) can be used to produce
simple graphs directly from ViewHAR or ViewSOL.
3.11    Changing the closure and shocks
[gpd1.2.11]
You can carry out several simulations on the same model by changing the closure and/or the shocks
in the Command file.
Note that, if you change the closure and/or shocks, but do not change the model (that is, do not
change the TABLO Input file), you do not need to repeat Step 1 (running TABLO) in section
3.6
. You only need to do Steps 2 and 3 there.
The following example shows you how to make a new Command file in the text editor and then run
another simulation using SJ.EXE (or alternatively GEMSIM).
The new simulation is to increase the price of labor by 3 per cent and to increase the supply of
capital by 10 per cent. In order to increase the price of labor, the variable p_PF("labor") needs
to be exogenous. You need to change the closure and also apply these different shocks.
To change the command file SJLB.CMF, copy it to a new name SJLB2.CMF as follows:
If you are working in WinGEM, in the main WinGEM menu, choose
File | Edit file...
then
open the file  SJLB.CMF. Click on
File | Save As...
and save the file under the new name
SJLB2.CMF.
If you are working at the Command prompt, type "copy sjlb.cmf sjlb2.cmf".
Then use the text editor to modify this file, following the steps below.
(1) In the original closure, both components of p_XFAC (supplies of labor and capital) are
exogenous.  Here you keep the supply of capital exogenous, but set the price (rather than the
supply) of labor exogenous.  [p_PF is the variable in the model denoting the percentage change in
the price of the factors, labor and capital.]
Find the statement
exogenous   p_xfac ;
and change this to
exogenous   p_pf("labor")   p_xfac("capital")   ;
(Be careful not to leave a space between the variable name p_pf and the bracket. However, it does
not matter if you use upper or lower case, or a mixture, in Command files.)
(2) Shock p_pf("labor"), the price of labor, by 3 per cent and shock p_xfac("capital"), the supply
of capital, by 10 per cent.
You will need two separate shock commands:
shock   p_pf("labor")   =  3  ;
 shock  p_xfac("capital") = 10 ;
[Remember to put a semicolon  ";"  after each statement.]
(3) Change the verbal description to describe the new closure and shocks.  [This starts after
"verbal description ="  and ends with a semi-colon ";".  There can be several lines of text in it.]
Exit from the editor after saving your changes.
If you are working in WinGEM:
If you have Source Code GEMPACK, click on
Simulation | Run TG program...
and then
Select
the TG EXE file to be  SJ.EXE.
If you have an Executable-Image version, click on
Simulation | GEMSIM Solve...
.
Now both cases continue in the same way.
Select   the Command file SJLB2.CMF.
Run   the program with this Command file SJLB2.CMF.  This is Step 2 of the simulation steps listed
in section
3.6
.
If there are errors when this runs, you will see a window headed "Error during Simulation".  To
correct the errors in the Command file, click on the button
Edit Command file
to use split screen
editing.  The Command file SJLB2.CMF will be shown in the top part of the screen and the LOG file
in the bottom part of the screen. The errors will be marked in the LOG file, usually near the end
of the file. When you have identified what is causing an error, you must make the appropriate
change in the Command file in the top part of the screen (not the LOG file). The
Next
error
button may help you to find errors. [If you have problems identifying or correcting the
errors, you can find more assistance in section
4.7.2
below.] When you have corrected
all errors, use
File | Exit
and save the changes you have made to the Command file
SJLB2.CMF.  Then close the error window by clicking on
Close
in it.  Now click on
Run
to run
the simulation again.
When SJ.EXE (or GEMSIM) has run successfully, click on
Go to ViewSOL
to look at the results.
If you are working at the Command prompt,
Edit the Command file  sjlb2.cmf  to make the changes above.
To run the simulation, type in at the Command prompt:
sj  -cmf  sjlb2.cmf
to run sj.exe or, to run GEMSIM:
gemsim -cmf sjlb2.cmf
View the Log file to see if there are any errors.
If there are errors, the errors will be marked in the LOG file (which is probably called
sjlb2.log), usually near the end of the file. When you have identified what is causing an error,
you must make the appropriate change in the Command file (not the LOG file). After you correct an
error, rerun the simulation. [If you have problems identifying or correcting the errors, you can
find more assistance in section
4.7.2
below.]
When  sj.exe  (or GEMSIM) has run successfully, use ViewSOL to examine  the Solution file sjlb2.sl4.
3.12    How Johansen and multi-step solutions are calculated
[gpd1.2.13]
Johansen solutions are approximate results of a simulation.  In contrast, multi-step solutions can
be made arbitrarily accurate by taking enough steps. In this section we describe the main ideas
involved in calculating these different solutions.
3.12.1    The linearized equations of a model
[gpd1.2.13.1]
Johansen solutions are calculated by solving the linearized equations
15
of the model once;
multi-step solutions are obtained by solving these equations several times.
The system of linearized equations of any model can be written in the form
C z = 0                                     (1)
where
C
is the n x m matrix of coefficients of the equations, known as the Equations .Matrix (which is
closely related to the Equations file
16
,
z
is the m x 1 vector of all the variables (usually in percentage change form) of the model,
n
is the total number of equations, and
m
is the total number of variables.
We call C the
Equations Matrix
of the model
17
. It is often useful to think of this matrix as a rectangular array or tableau
18
with the vector variables across the top and the equation blocks along the left-hand side. Each vector
variable occupies as many columns as its number of components, and each equation block occupies as
many rows as the number of actual equations in it.
To illustrate this, part of the tableau for the 27 x 29 Equations Matrix C for the Stylized
Johansen model (from the TABLO Input file SJ.TAB) is shown in Table
3.4
.
Notice that we use the words "variable" and "equation" in two different senses. For example, we
usually say that Stylized Johansen is a model with 29 variables and 27 equations, where we count as
variables all the components of the vector variables and we count as equations all the individual
equations in the equation blocks. In this sense, the number of variables is the number of columns
in the Equations Matrix while the number of equations is the number of rows. Alternatively we may
say that the TABLO Input file for Stylized Johansen has 11 variables (meaning vector variables) and
10 equations (meaning equation blocks).  Usually the context will make clear which of these two
meanings is intended.
Table 3.4 Tableau of the equations matrix for Stylized Johansen
1     2       2       2            4        2
              p_Y   p_PC   p_PF    p_XCOM....   p_DVFACIN p_DVHOUS  
  cols -->      1   2  3   4  5     6  7          24..27  28  29
        rows  ___________________________________________________
           1 |   |       |       |       |      |        |      | 
 Comin     2 |   |       |       |       |      |        |      |
     4     3 |   |       |       |       |      |        |      |
           4 |___|_______|______ |_______|______|________|______|
           5 |   |       |       |       |      |        |      |
 Facin     6 |   |       |       |       |      |        |      |
     4     7 |   |       |       |       |      |        |      |
           8 |___|_______|______ |_______|______|________|______|
 House     9 |   |       |       |       |      |        |      |
     2    10 |___|_______|_______|_______|______|________|______|
             |   |       |       |       |      |        |      |
     :       |   |       |       |       |      |        |      |
     :       |   |       |       |       |      |        |      |
             |___|_______|_______|_______|______|________|______|
 Numeraire 27|   |       |       |       |      |        |      |
     1       |___|_______|_______|_______|______|________|______|
In general, n is less than m in the system of equations in (1) above, so when you carry out a
simulation (Johansen or multi-step) you must specify
(m-n) of the variables as exogenous and the remaining variables as endogenous, and
shocks (usually percentage changes) to some of the exogenous variables.
For Stylized Johansen, the total number of variables (m) is 29 and the total number of equations
(n) is 27, so we need 2 exogenous variables. We can shock either 1 or 2 of these exogenous
variables.
The numerical values of some of the entries in the Equations Matrix can be seen in section
4.4.5
below.
3.12.2    Johansen solutions
[gpd1.2.13.2]
Johansen solutions are defined to be solutions obtained by solving the linearized equations of the
model
just once
. Because the levels equations of the model are usually nonlinear, the results of
this calculation are only approximations (sometimes good approximations and sometimes not-so-good)
to the corresponding solution of the levels equations of the model.
Once the exogenous/endogenous split has been chosen, the system of equations
C z = 0
in (1)
above, becomes .
A z
1
= -D z
2
(2)
where z
1
and z
2
are respectively the (column) vectors of endogenous and exogenous variables,. A is
n x n
and D is
n x (m-n)
.
The matrix A is referred to as the LHS Matrix (Left Hand Side Matrix) of the simulation. The LHS
matrix A consists of the columns of the Equations matrix corresponding to the endogenous variables
in the given closure. Similarly the columns of the matrix D are just the columns of C corresponding
to the exogenous variables in the closure. The shocks are the values to use for z
2
. Once these are
known, we have a system
A z
1
= b                               (3)
to solve (where the RHS vector b is an  n x 1 vector equal to  -Dz
2
). It is the solution z
1
of this
matrix equation (3) which is the
Johansen solution
of the simulation
19
.
3.12.3    Multi-step simulations and accurate solutions of nonlinear equations
[gpd1.2.13.3]
The idea of a multi-step simulation is to break each of the shocks up into several smaller pieces.
In each step, the linearized equations are solved for these smaller shocks. After each step the
data, shares and elasticities are recalculated to take into account the changes from the previous
step. In general, the more steps the shocks are broken into, the more accurate will be the results.
Figure
3.5
below makes this easy to visualise. In that figure we consider just one
exogenous variable X (shown on the horizontal axis) and one endogenous variable Y (vertical axis);
these are constrained to stay on the curve g(X,Y) = 0. We suppose that they start from initial
values X
0
,Y
0
at the point A and that X is shocked from value X
0
to value X
1
. Ideally we should
follow the curve g(X,Y)=0 in solving this. In a Johansen (that is, a 1-step) solution we follow the
straight line which is a tangent to the curve at point A to reach point B
J
and so get solution Y
J
.
Figure 3.5 Illustration of Euler's method
In
Euler's method
the direction to move at each step is essentially that of the tangent to the
curve at the appropriate point.  In a 2-step Euler solution (see Figure above), we first go half
way along this tangent to point C
2
, then recompute the direction in which to move, and eventually
reach point B
2
, giving solution Y
E2
. The exact solution is at B where Y has value Y
1
. In a 4-step
Euler simulation we follow a path of 4 straight-line segments, and so on for more steps.
The default method used by GEMPACK is
Gragg's method
which uses an even more accurate method
than Euler's method for calculating the direction in which to move at each step.  When the shocks
are broken into N parts, Euler's method does N separate calculations while Gragg's method does N+1.
Usually the computational cost of this extra calculation is more than repaid by the extra accuracy
obtained.  More information about Gragg's method (and the similar
midpoint method
) can be found in
section
30.2
.
So one way of increasing accuracy is to increase the number of steps. It turns out, however, that
the best way to obtain an accurate solution is to carry out 2 or 3 different multi-step
calculations with different numbers of steps and to then calculate the solution as an appropriate
weighted average of these. This is what is meant by the
extrapolated solution
.
To illustrate this, we have shown below the different results for the percentage change in
household expenditure 'p_Y' in the Stylized Johansen model for the simulation in section
3.1
above, in which labor supply is increased by 10 per cent and capital remains in
fixed supply. The table below shows Euler and Gragg results for different step numbers and
extrapolations based on them. Note that the exact result is 5.88528.
Multi-step results for different methods and step numbers
   Method     Number of steps
                1         2         4          6        100
    Euler    6.00000   5.94286   5.91412    5.90452    5.88644
    Gragg    5.89091   5.88675   5.88545    5.88529  
Extrapolated results
    From Euler 1,2-step results        5.88571    
    From Euler 1,2,4-step results      5.88527
    From Gragg 2,4,6-step results      5.88529
Note that, in this case,
the 4-step Gragg result is more accurate than the 100-step Euler result, and
the result extrapolated from 1,2,4-step Euler results is much more accurate than the 100-step Euler
result (even though the latter takes about 100/7 times as long to compute).
These results are typical of what happens in general.
The general messages are:
Gragg's method is usually much more accurate than Euler's (for the same number of steps).
If in doubt, extrapolate.
Extrapolating from 3 different solutions is better than from 2. For example, extrapolating from
Gragg 2,4 and 6-step solutions is usually better than from just 4 and 6-step solutions.
When you extrapolate, if you ask for an
Extrapolation Accuracy file
(or .XAC file)
20
, this

file shows how accurate the solution is for each endogenous variable. The separate columns show the
results for the different multi-step solutions calculated, and the last column of results is the
extrapolated result. When you extrapolate from 3 different multi-step results (which is what we
recommend), the last two columns give conservative information about the accuracy of each result.
(If they show M figures agreement, this means that the 2 different extrapolations based
respectively on just the first two and just the first and third agree to this number of figures.)
For example, for the 1,2,4-step Euler results for household expenditure 'p_Y' reported above for
the SJLB.CMF simulation (see sections
3.4
), the relevant line in
the Extrapolation Accuracy file would
21
be
p_Y     1       6.00000    5.94286   5.91412   5.88527   CX  4  L5
The results are the 1,2,4-step results and the extrapolation based on them. The comment "CX   4" is
an abbreviation meaning that you can have confidence in the extrapolated result (this is the 'CX')
and that the two extrapolations (the first based just on the 1,2-step results and the second based
on the 2,4-step results) agree to 4 figures (or more). Note that the agreements are reported as
figures, not decimal places.  (For example 123.4567 and 123.4014 agree to 4 figures, but only one
decimal place.)  The abbreviations (such as 'CX') used on this file are explained at the top of the
file. (The first "1" in the line displayed above means that this line refers to the first - in this
case, the only - component of variable p_Y.) The "L5" at the end of this line means that you can be
confident of 5 figures accuracy in the level of income Y. [See section
26.2.1
for more
details.]
At the end of the file is a summary (we refer to it as the
Extrapolation Accuracy Summary
) which
states how many components fall into each category (EMA, CX etc). For a simulation with Stylized
Johansen, this may look something like that shown below.
SUMMARY OF CONVERGENCE RESULTS                 Number  Min Figs Agree
      ------------------------------           ------  --------------
 EMA  Last two results equal to machine accuracy  3         6
 FC0  Fair confidence that the result is zero     2
 CX   Confidence in the extrapolated result      22         2  
   2 results are judged accurate to 2 figures.
   4 results are judged accurate to 3 figures.
   16 results are judged accurate to 4 figures.
   3 results are judged accurate to 6 figures.
 
  Above is for linearised variables.
  Below are for levels values of percent-change and change results.

   1 results are judged accurate to 4 figures.
   21 results are judged accurate to 5 figures.
   5 results are judged accurate to 6 figures.
   
    (The summary above covers the XAC-retained variables.)
The first part is a summary of the number of times different comments (in the example above, "EMA",
"FC0" and "CX") have been used for the different results. The second part tells how many results
(linearised, then levels) have been judged accurate to different numbers of figures.
More details about Extrapolation Accuracy Summaries and Extrapolation Accuracy files are given in
section
26.2
.
The only restriction on step numbers is that, for Gragg's method and the midpoint method, the step
numbers must either be all odd or all even (for example, 2,4,6 or 3,5,7). Note also that a 1-step
Gragg or midpoint is a little unusual and is probably best avoided (since it is more like Euler
than Gragg or midpoint).
More details are given in section
30.2
and some of the theory behind multi-step
methods can be found in
Pearson (1991)
.
3.12.3.1    Extrapolation formula for 3 Euler simulations
[extrapformula]
As an example, suppose we ran 3 Euler simulations with n1, n2 and n3  steps,
yielding (for some variable) solution values of s1, s2 and s3, respectively.
Then the extrapolated result E can be calculated as a weighted average of s1, s2 and s3:
E = W1*s1 + W2*s2 + W3*s3
where the weights add to 1. The formula for W1, W2 and W3 are:
W1 = n1*n1*(n3-n2)/denom;
W2 = n2*n2*(n1-n3)/denom;
W3 = n3*n3*(n2-n1)/denom;
where    denom:=(n3-n1)*(n2-n1)*(n3-n2);
Some example numbers are given in the table below. Note that W2 is negative.
Table 3.5 Extrapolation weights for 3 Euler simulations
n1
n2
n3
Total
Steps:
4
8
16
Weights:
0.333
-2.000
2.667
1.000
Steps:
8
16
32
Weights:
0.333
-2.000
2.667
1.000
Steps:
10
20
30
Weights:
0.500
-4.000
4.500
1.000
Steps:
15
20
25
Weights:
4.500
-16.000
12.500
1.000
Steps:
99
100
101
Weights:
4900.500
-10000.000
5100.500
1.000
3.12.4    Smiling or frowning face numbers are reported
[gpd5.9.2.1]
If you use WinGEM, RunGEM or RunGTAP, you know that after each simulation is completed, you see
smiling or frowning faces which indicate how accurately the simulation was solved (provided that
you are extrapolating from 3 multi-step calculations).
Within ViewSOL, the accuracy summary can be displayed via an icon:
on the upper toolbar.
At the end of the simulation, and at the end of each subinterval if there is more than one, GEMSIM
and TABLO-generated programs report (to the terminal and to the LOG file) the face number (between
1 and 10, where 10 is accurate and 1 is very inaccurate). Separate face numbers are shown for the
variable and the data accuracy. If there is more than one subinterval, the face number for the
overall variable accuracy is shown at the end of the Overall Accuracy Summary (see section
26.3.1
).
3.12.5    Fatal error if accuracy too low (GEMSIM and TG-programs)
[gpd5.9.2.2]
Suppose that you are extrapolating from 3 multi-step calculations.
If the accuracy is extremely low, it is highly unlikely that the simulation results are of any
value. Accordingly, the program stops with a fatal error in order to draw your attention to this
poor accuracy (but the solution file is still saved).
This can happen at the end of the whole simulation, or it can happen at the end of any subinterval
which is solved inaccurately. However it does not happen at the end of a subinterval if you are
using automatic accuracy since then you may redo the subinterval in question.
We believe it is your responsibility to decide whether or not a simulation has been solved
sufficiently accurately. You should always look at the information provided by the software,
especially the Accuracy Summaries (see sections
26.2
and
26.3.1
). We are
reluctant to intervene and, as when equations are not satisfied very accurately (see section
30.6.1
), we end with a fatal error only in what we consider are extreme cases. At
present, if any of the face numbers is 3 or less, we stop with a fatal error. Choosing 3 here does
not mean that we think face numbers 4,5 and 6 are ok (since often they will not be) - rather we
leave the decision to you in such cases.
3.13    GEMPACK programs - an overview
[gpd1.2.14]
As you have already seen, GEMPACK is not a single program. There are a number
of different programs making up GEMPACK. In this section we give a brief
overview of these different programs, grouped by task.
You have not yet used all of the programs below. As you become more experienced with GEMPACK, you
may need to come back to this section to check out those programs you have not used.
3.13.1    Working with TABLO input files
[gpd1.2.14.1]
TABmate
is a special editor for TABLO Input (TAB) files. Use TABmate to create
and modify the theory of a model - that is, the TABLO Input file for the model.
TABLO
converts the model TAB file into a TABLO-generated program or
Auxiliary files for GEMSIM. You must do this before you can carry out a simulation with a model.
[See Step 1 in section
3.6
.]
In fact TABmate runs the program TABLO in the background. So TABmate and TABLO can perform very
similar functions. You can use either TABLO or TABmate to carry out Step 1 for simulations (see
section
3.6
).
3.13.2    Carrying out simulations
[gpd1.2.14.2]
You can use either GEMSIM or the relevant TABLO-generated program to carry out Step 2 for
simulations (see section
3.6
). Which you use depends on how you ran TABLO in Step 1
(see section
3.6.1
or
3.6.2
above).
GEMSIM.
Run GEMSIM to carry out a simulation. Specify the Auxiliary files, starting data files,
closure and shocks in a Command file.
TABLO-generated program.
Run the EXE file of the TABLO-generated program to carry out a
simulation. Specify the starting data files, closure and shocks in a Command file. You can only
create TABLO-generated programs if you have a Source-code version of GEMPACK.
3.13.3    Looking at, and processing, simulation results
[gpd1.2.14.3]
ViewSOL
is for looking at results — see Step 3 in section
3.6
.
AnalyseGE
is for analysing simulation results. You can view model
equations, simulation results and the values of items in the data base. Section
36.6
introduces AnalyseGE. A hands-on introduction to AnalyseGE in the
context of a simulation with Stylized Johansen can be found in section
46.1
.
SLTOHT
is a command-line program that converts simulation results (on a Solution file)
either (a) into tables of results which you can import into a spreadsheet, or (b) into a Header
Array file. See section
3.10
above and chapters
39
and
40
for information
about SLTOHT.
When you report simulation results, you will probably use other standard tools (including
spreadsheet programs such as Excel) for making tables and graphs.
3.13.4    Working with data
[gpd1.2.14.4]
In GEMPACK data for models are usually held on Header Array files. Because these are binary (ie, non-text) files,
you need special programs to work with the data in this form.
ViewHAR
is for looking at data on Header Array files.
You used ViewHAR to look at original and updated data in the Stylized Johansen example above.
ViewHAR can also be used to create a Header Array file and to modify
data on a Header Array file (see section
6.1
below and section
6.2
).
CMPHAR
can be used to compare the data on two Header Array files — see section
37.2
.
CMBHAR
can be used to combine the data on two or more Header Array files (for example, data
representing two or more years). See section
37.3
.
Data comes from various sources. You may use other standard tools and programs (including
spreadsheet programs such as Excel) when working with data.
3.13.5    Windows modelling environments
[gpd1.2.14.5]
WinGEM
provides a Windows environment for carrying out modelling and associated tasks.
RunGEM
provides a Windows environment for carrying out simulations with a fixed model.
Users with little experience of modelling can carry out simulations by choosing just the closure
and shocks.  See section
36.5
and chapter
45
.
RunDynam
and variants including   RunGDyn are sold as as a separate product.
They are Windows interfaces for use with recursive dynamic models such as  USAGE and dynamic GTAP.
See section
36.7
.
3.13.6    Other programs for special tasks
[gpd1.2.14.6]
These are programs used for specialised tasks, usually by power users. You will not need to use any
of them until you are more experienced with GEMPACK.
ACCUM
and
DEVIA
are used for working with recursive dynamic models such as USAGE which are
solved annually over a period of several years. ACCUM and DEVIA collect the results for several
years. [See chapter
41
.]
SUMEQ
is for looking at data on an Equations file. SUMEQ can also be used to diagnose homogeneity
problems with a model — see chapter
79
.
SEENV
is for working with Environment files (which store the set of exogenous and endogenous
variables in one closure for a model) — see chapter
56
.
3.13.7    Programs for use on non-Windows PCs
[gpd1.2.14.7]
Windows programs, such as WinGEM,  ViewHAR or ViewSOL, will not run on non-Windows PCs
22
-- so other, command-line programs are needed to turn data (HAR) and results (SL4) files into text
files that you can view. These are:
SEEHAR
turns a Header Array file into a viewable text file — see section
37.1
.
3.14    Different GEMPACK files
[gpd1.2.15]
As you have seen, GEMPACK programs produce and use several different types of files (for example,
Solution files and Header Array files). New users often ask us "Why are there so many different
files?".
In this section we give more details about these different files and how they are used.
In our experience, some users are keen to have detailed information about this topic while others
are not very interested. Since a detailed knowledge about this topic is not essential for doing
effective modelling, you should feel free to skip this section or to skim it very quickly. You can
always refer back to it later on, if and when you need to.
A table summarising the different files is given in section
3.14.6
below.
3.14.1    The most important files
[gpd1.2.15.1]
We begin with the most important files, namely TABLO Input files, data files, Command files and
Solution files, all of which you have met earlier in this chapter.
TABLO Input files.
These contain the theory (equations etc) for a model. Alternatively they may be
for data manipulation. These files have suffix
.TAB
. These files are inputs to the program TABLO.
The program TABmate (see section
36.4
) can be used to create and or modify these files.
Data files.
These may be Header Array files or text files. The suffix is not prescribed by the
software, though suffix
.HAR
is recommended (.DAT is sometimes used). Data files can be inputs to a
simulation (the original input-output data, the parameters) and updated versions are output from a
simulation. Updated data files are usually given the suffix
.UPD
. Chapter
6
below
contains an introduction to the different ways in which you can create data files and modify data
on existing data files.
Command files.
These contain the details of a simulation, including closure, shocks, starting data
and solution method (see section
3.8
). The suffix is not prescribed by the software,
though
.CMF
is usual
23
. Command files are inputs for GEMSIM and TABLO-generated programs.

The statements allowed in Command files are documented in chapter
35
.
Solution files.
These are the main outputs from a simulation. They contain the change or
percentage change results for all the linearized variables. They may also contain levels results.
These files have suffix
.SL4
. They are inputs to various post-simulation programs
such as ViewSOL, SLTOHT, and AnalyseGE. Solution files are documented in chapter
27
.
Equations files.
These contain numerical versions of the linearized equations of a model. They are
usually only produced when you wish to use SAGEM to obtain several Johansen (approximate) solutions
of a model, as explained in chapter
58
. You may also create an Equations
file if your model is not homogeneous in prices or quantities (see section
79.1
).
Equations files have suffix
.EQ4
.  Equations files are documented in chapter
59
.
Shock files.
Sometimes it is necessary to shock the different components of a variable by
different amounts. If the variable has a large number of components, or if the shocks are
calculated by a program, it is convenient to put the numerical values of the shocks onto a
so-called "shocks file". This file may be a text file or a Header Array file. The suffix for shocks
files is not prescribed by the software, though often
.SHK
is used. The use of shock files is
documented in sections
24
to
66.2
.
Solution Coefficients (SLC) files.
These are output from a simulation. They contain the
pre-simulation values of all data and of all Coefficients in the TABLO Input file for the model.
These files have suffix
.SLC
and have the same name (apart from suffix) as the Solution file from
the simulation
24
. The program AnalyseGE reads both the Solution and SLC file when you analyse the

results of a simulation
25
. You can also examine SLC files with ViewHAR. SLC files are documented in section
28.1
.
Extrapolation Accuracy files.
You can ask
26
for an Extrapolation Accuracy file to be produced when
you extrapolate from 3 separate multi-step calculations (as you have seen in section
3.12.3
above). These text files show estimates as to how accurate the different simulation
results are. They have suffix
.XAC
and have the same name (apart from suffix) as the
Solution file from the simulation. Extrapolation Accuracy files are documented in section
26.2
.
3.14.2    Files for communication between programs
[gpd1.2.15.2]
There are a number of files which are used for communication between programs. The most important
of these are the Auxiliary files which allow communication between TABLO and GEMSIM or the
TABLO-generated program.
Auxiliary files.
These are either
Auxiliary files for a TABLO-generated program.
These are produced when TABLO writes a
TABLO-generated program (see section
3.6.1
above). These files have suffix
.AXS
(Auxiliary Statement file) and
.AXT
(Auxiliary Table file).
GEMSIM Auxiliary files.
These are produced when TABLO writes output for GEMSIM (see section
3.6.2
above). These files have suffix
.GSS
(GEMSIM Statement file) and
.GST
(GEMSIM Table file).
TABLO-generated program (Fortran file).
This is the Fortran (.FOR) file for the TABLO-generated
program which is produced by TABLO (see section
3.6.1
above). Auxiliary files (.AXS and .AXT files) are
always produced at the same time. In Step 1(b) for simulations (see section
3.6.1
),
this program is compiled and linked to produce the EXE file of the TABLO-generated
program
27
. It is this EXE file which is run to carry out a simulation.
When the EXE file of a TABLO-generated program is used to carry out a simulation, the
Auxiliary files (AXS and AXT files) are required. They communicate vital information from the TABLO
Input file to the simulation.
Similarly, if GEMSIM is used to carry out a simulation, the GEMSIM Auxiliary files (GSS and GST files) are
required.
3.14.3    LOG files
[gpd1.2.15.3]
Often a program runs very quickly and/or puts a lot of information on the screen. If you need to
check this output (for example, to see where an error occurs), you can ask for a LOG file to be
created
28
. You can then look at this log file in your favourite text editor. The suffix for LOG files

is not prescribed by the software, though suffix
.LOG
is usual.
3.14.4    Stored-input (STI) files
[gpd1.2.15.4]
These days, GEMPACK Windows programs such as TABmate, RunDynam or WinGEM are the main interface
seen by most GEMPACK users — but a lot of the work they seem to perform is in fact carried out by
command-line programs running in the background.
In previous times, before the GEMPACK Windows programs were available, GEMPACK users usually ran
programs like TABLO, GEMSIM and SLTOHT from the command line. The program would ask a sequence of
questions — the responses were usually single letters (to indicate options) or filenames (for
input and output).
Obviously it could be very tedious to repeatedly run programs in this way.
Stored-input
files or
STI
files were a way to reduce the drudgery — they consist of a text file which
stores the necessary responses to the questions that the program asked. Then, to repeat an SLTOHT
job, one merely typed, say:
sltoht -sti report3.sti
where report3.sti is a text file of the responses needed to generate some report. To produce
report3.sti you would, the first time you ran this job, either note responses on a scrap of paper
(the old way) or activate the SIF option in SLTOHT which will record your responses in a file.
STI files are rather hard to read and understand — you only see one half of a conversation.
For modern GEMPACK users the most-frequently encountered STI files may be those used for input to
TABLO which specify the condensation (section
14.1.2
gives an example). For new models
you can and should specify condensation actions — such as Omit, Substitute and BackSolve — within
the TAB file, but this option is relatively new, so many older models still use a STI file to store
the condensation.
Apart from this, the main remaining uses of STI files are:
to automate the running of SLTOHT or some other command-line programs which need to be run repeatedly
to activate some rarely used options in TABLO or other programs. A few options are only accessible via STI files (or by direct
responses to program queries).
Stored-input files are further described in section
48.3
. They usually have suffix
.STI
(although other suffixes may be used). You will need to learn about STI files as you
become more experienced. You can find introductory examples of creating and working with them in
sections
14.1.2
,
14.1.4
and
54.11
.
3.14.5    Files for power users
[gpd1.2.15.5]
A number of files can be created in order to speed up or simplify subsequent tasks. These are
typically used mainly by experienced GEMPACK users so you don't need to know any details
about them at this stage. Examples are Stored-input files (see section
3.14.4
above),
Environment files (see section
23.2
) and various Mapping files (see sections
39.3
,
39.8
and
40.1
).
3.14.6    Summary of files
[gpd1.2.15.7]
Table 3.6 Summary of the different files
File Type and Suffix
Input to
Output from
TABLO Input file  (TAB)
TABLO, TABmate
TABmate
Data files (often HAR)
Simulations, Data-manipulation TAB files, ViewHAR, CMBHAR, SEEHAR etc
Simulations, Data-manipulation TAB files,ViewHAR, SLTOHT etc
Command files (usually CMF)
TABLO-generated programs, GEMSIM, SAGEM
text editor
Solution files  (SL4)
ViewSOL, ViewHAR, AnalyseGE, SLTOHT
TABLO-generated programs, GEMSIM, SAGEM
Equations files  (EQ4)
SAGEM, SUMEQ
TABLO-generated programs, GEMSIM
Shock files (often  SHK)
TABLO-generated programs, GEMSIM, SAGEM
text editor, TABLO-generated programs, GEMSIM
SLC files  (SLC)
AnalyseGE
TABLO-generated programs and GEMSIM
Extrapolation Accuracy files (XAC)
TABLO-generated programs and GEMSIM
Auxiliary files (GSS/GST or AXS/AXT)
GEMSIM or TABLO-generated program
TABLO
TABLO-generated Fortran program  (FOR)
Compile and link - Step 1(b) in section
3.6.1
TABLO
LOG files   (usually LOG)
Any command-line GEMPACK program
Stored-input files (usually STI or SIF)
Any command-line GEMPACK program
Text editor,  or any GEMPACK program
(see options SIF and ASI in section
48.3
).
3.14.7    Work files
[gpd1.2.15.6]
Many programs create and use working files while they are running. These work files can be large.
Usually these work files are deleted when the program finishes so you do not see them or need to
know about them. Occasionally these files are left around on your hard disk if the program finishes
with an error. See below or section
30.7
for more details.
3.14.8    Files you can eventually delete
[junkfiles]
Especially when running multiperiod simulations, GEMPACK tends to create many output files — most of which will not
be needed in a few days time. A list of these 'junk files' appear below. A command-line program, GPDEL, is provided, which will
remove many of these files. From a command prompt in your working folder, type:
GPDEL
to see instructions for using it. Alternatively, TABmate's
Tools..Delete Junk files
menu item offers another way to cull files.
Table 3.7 Files you can eventually delete
Filename pattern
Description
*.BAK
Backups of files modified by TABmate and ViewHAR
*.LOG
Log files made by many GEMPACK programs
*.MDV *.MDC *.MDE
Tables of variables, coefficients and equations made by TABmate
*.CLO
Closure report from TABmate
*.INF *.MNC
Output from TABLO
*.TBR *.TBT
Temporary files made by TABLO
*.UD3 *.UD4 *.UD5
*.UD6  *.UD7 *.UD8 *.UD9
Temporary files of updated coefficients produced during a simulation
*assert-fail.har
Diagnostic files
produced when an assertion fails
*assert-arith-fail.har
Diagnostic files
produced when there is an arithmetic error or overflow
*.CWK *.DWK  *.IWK
*.PWK   *.SWK  *.E2K
*.EXS  *.EL2 *.RDT
Temporary work files
produced during a simulation — usually only visible if a simulation crashes.
*.SLC  *.UDC  *.AVC  *.CVL
Files of coefficient values  produced mainly for use by AnalyseGE, details
here
.
optin_1 optin_2 opt80
opt80_2  parcomp.*
Temporary files produced while compiling TABLO-generated Fortran programs
3.15    For new users - what next?
[gpd1.2.16]
Congratulations. You have just learnt the most important things about GEMPACK, namely how to set up
and carry out simulations, and how to look at the results.
Where you go next in learning about GEMPACK depends on your main purpose in using the software.
If you mainly want to carry out simulations with another standard model, you will find a list of
the models supplied with GEMPACK in section
1.5
. If the model you wish to work with is
one of these, you will find detailed hands-on guidance in chapter
43
about carrying out standard
simulations with many of these models. If you wish to work with another model, the model developers
have probably supplied and documented one or more standard simulations. We suggest that you start
with those.
With a well-documented model and good software, it is relatively easy to carry out simulations and
produce, and report, a large number of results. It is less easy to really understand these results.
The GEMPACK program AnalyseGE (see section
36.6
) provides valuable assistance to you
in this task. You can find a hands-on introduction to AnalyseGE in the context of a Stylized
Johansen simulation in section
46.1
.
Pearson  et al. (2002)
provides a hands-on
introduction to AnalyseGE in the context of simulations with GTAP. We encourage you to explore the
use of AnalyseGE as you analyse the results of simulations you carry out.
If you want to build your own model (or modify someone else's), or if you just want to understand
how a model is implemented in GEMPACK, you should read chapter
4
. Perhaps read it
quickly the first time and then go back for a more detailed study.
If you need to build or modify the data files for a model, you should read chapter
6
.
When you want to know more about the GEMPACK utility programs (say, for report generation or
post-simulation processing of results), look at the detailed documentation
in Chapters
36
to
40
.
When you want to know more about running the GEMPACK programs, read chapter
48
. This
chapter gives detailed suggestions for more efficient use of the programs whether you are running
them interactively or in batch mode.
Whatever your main interest, we strongly encourage you to at least skim chapter
4
first, and then go on to your main interest. You must be familiar with at least the basics of TABLO
Input (TAB) files in order to work properly with, and understand, any model implemented via GEMPACK.
4    Building or modifying models
[gpd1.3]
Click here
for detailed chapter contents
In order to build a model within GEMPACK, it is necessary to prepare a TABLO Input file containing
the equations of the model and to construct one or more data files whose purpose is essentially to
give one solution of the levels equations of the model.
The preparation of a TABLO Input file involves
writing down the equations in a suitable form. You can use levels equations, linearized equations
or a mixture of these. We discuss this in section
4.1
below.
working out the data requirements of the model. This is discussed in section
4.2
below.
We describe the preparation of TABLO Input files in section
4.3
and the preparation of
the actual data files in chapter
6
. We illustrate each step in the process by doing it
for the Stylized Johansen model.
Of course, to modify an existing model, you modify the TABLO Input file (to change the theory of
the model) and/or the data file(s).
The TABLO Input file given for Stylized Johansen in section
4.3.3
is a mixed one (in
the sense that it contains a mixture of linearized and levels equations). In sections
4.4.1
and
4.5.1
we describe alternative TABLO Input files for Stylized
Johansen consisting only of linearized or levels equations respectively.
TABLO linearizes all levels equations in TABLO Input files and converts all levels variables to the
associated linear ones (change or percentage change in the associated levels variables). This is
described in section
4.6
.
We conclude this chapter in section
4.7
where we give you advice about building your
own model by writing a TABLO Input file from scratch or by modifying an existing one. We include
hands-on examples showing how to identify and correct errors in TABLO Input files and Command files.
If you are familiar with using GAMS for general equilibrium modelling, you may prefer to work
through the document
Kohlhaas and Pearson (2002)
instead of, or before, reading this chapter. The
many similarities between GEMPACK and GAMS make it relatively easy for a GAMS modeller to begin
using GEMPACK productively.
Table 4.1 Levels and linearized equations of the Stylized Johansen model
In Table
4.1
, upper-case Roman letters represent the levels of the variables; lower-case
Roman letters are the corresponding percentage changes (which are the variables
of the linearized version shown in the second column).  The letters P, X and D
denote prices, quantities and dollar values respectively, while the symbols A
and a denote parameters.  Subscripts 1 and 2 refer to the (single) commodities
produced by industries 1 and 2 (subscript i), or to the industries themselves
(subscript j); i = 3 refers to labour while i = 4 refers to the model's one
(mobile-between-industries) type of capital; subscript  j = 0  identifies
consumption.  Because the first three equation blocks are identically linear in
the logarithms they are natural candidates for presentation and explanation of
the model.
4.1    Writing down the equations of a model
[gpd1.3.1]
TABLO Input files contain the equations of a model written down in a syntax which is very similar
to ordinary algebra. Once you have written down the equations of your model in ordinary algebra, it
is a simple matter to put them into a TABLO Input file, as we illustrate in section 3.3 below.
You are free to use levels or linearized versions of the equations or a mixture of these two types.
For example, if a certain dollar value D is the product of the price P and quantity Q, the levels
equation is
D = P * Q
(where the "*" indicates multiplication), and the associated linearized equation is
p_D = p_P + p_Q
where "p_" denotes "percentage change in". The linearized version says that, to first order of
approximation, the percentage-change in the dollar value is the sum of the percentage changes in
the price and the quantity. Whichever version of the equation you include, GEMPACK can still
produce accurate solutions of the underlying levels equations (which are usually nonlinear).
We say more about the process of linearizing equations in section 3.7 below.
The best way of making the above clear is to take a concrete example, as we do below, using
Stylized Johansen as our example model.
4.1.1    Writing down the equations of Stylized Johansen
[gpd1.3.1.1]
We start from the equations as written down in Chapter 3 of
DPPW
(to which we refer
readers interested in the derivation of, and motivation behind, these equations). An excerpt from
that chapter, SJ.PDF, is included in the "examples" subfolder of your GEMPACK directory.
The equations of the model are shown in Table
4.1
. In that table, both the levels
and linearized versions of each equation are shown, taken essentially unchanged from
DPPW
1
.  Notice

that upper case letters (for example, X) denote levels quantities while lower case letters (for
example, x) denote percentage change in the corresponding levels quantity.
For our first implementation of Stylized Johansen (see section
4.3
below), we have
chosen a mixed representation, based on the shaded blocks in Table
4.1
. That is,
we decided to use the levels versions of some of the equations (most are accounting identities and
one is the numeraire equation) and the linearized versions of the top three equations (which are
behavioural equations). Later, in sections
4.4
and
4.5
respectively, we
describe implementations based on exclusively linearized equations (section
4.4
) and
exclusively levels equations (section
4.5
). Of course, each of these 3
implementations is valid and all three produce the same results.
The notation in
DPPW
involves a liberal use of subscripts which are not suitable for the linear
type of input usually required by computers (and required in the TABLO Input file). Hence we use a
different notation. The levels variables of the model are as follows. In
DPPW
subscripts
1 and 2 refer to sectors (commodity or industry), subscripts 3 and 4 refer to factors (3 is labor
and 4 is capital) while subscript 0 refers to households.
Table 4.2 Levels variables for Stylized Johansen
GEMPACK variable
Meaning
DPPW
Notation
Y
Value of household income
Y
PC(i)
Price of commodity i
P
i
(i=1,2)
PF(f)
Price of factor f
P
f
(f=3,4)
XCOM(i)
Supply of commodity i
X
i
(i=1,2)
XFAC(f)
Supply of factor f
X
f
(f=3,4)
XH(i)
Household use of commodity i
X
i0
(i=1,2)
XC(i,j)
Intermediate input of  commodity i to industry j
X
ij
(i,j=1,2)
XF(f,j)
Input of factor f to industry j
X
fj
(f=3,4;j=1,2)
DVCOMIN(i,j)
Dollar values for intermediate inputs
(i,j=1,2)
DVFACIN(f,j)
Dollar values for factor use by industry
(f=3,4;j=1,2)
DVHOUS(i)
Dollar values for household consumption
(i=1,2)
Table 4.3 Parameters for Stylized Johansen levels equations
Parameters
Description
DPPW
Notation
ALPHACOM(i,j)
Commodity exponents in production  function for sector j (E3.1.4)
ALPHA
ij
(i,j=1,2)
ALPHAFAC(i,j)
Factor exponents in production function for sector j (E3.1.4)
ALPHA
fj
(f=3,4; j=1,2)
We introduce sets SECT, the set of two sectors say "s1" and "s2", and FAC, the set of the two
factors "labor" and "capital".
Below in Table
4.4
, we have rewritten the selected equations from Table
4.1
, this time using the GEMPACK variables and notation as in Tables
4.2
and
4.3
.  Note that below we also use the GEMPACK
convention that "p_" indicates percentage change in the relevant levels variable. For example,
p_XH(i) denotes the percentage change in XH(i), household consumption of commodity i. In these
equations we use  "*" to denote multiplication and "/" to denote division. We also use
SUM(i,<set>,<expression>) to denote sums (usually expressed via Greek sigma) over all i
in the set <set>; here <set> is SECT or FAC.
Note that below we also use the GEMPACK convention that "p_" indicates percentage change in the
relevant levels variable. For example, p_XH(i) denotes the percentage change in XH(i), household
consumption of commodity i. In these equations we use  "*" to denote multiplication and "/" to
denote division. We also use SUM(i,<set>,<expression>) to denote sums (usually
expressed via Greek sigma) over all i in the set <set>; here <set> is SECT or FAC.
Table 4.4 Stylized Johansen equations in GEMPACK notation
Equation                                      Subscripts         No. in DPPW
(E1)  p_XH(i)   = p_Y - p_PC(i)                       i in SECT          E3.2.1
(E2)  p_XC(i,j) = p_XCOM(j) - [p_PC(i) - p_PC(j)]     i,j in SECT        E3.2.2, E3.2.3
(E3)  p_XF(f,j) = p_XCOM(j) - [p_PF(f) - p_PC(j)]     f in FAC,j in SECT E3.2.2, E3.2.3
(E4)  p_PC(j)   = SUM(i,SECT, ALPHACOM(i,j)*p_PC(i)) 
                + SUM(f,FAC,  ALPHAFAC(f,j)*p_PF(f))  j in SECT          E3.2.3
(E5)  XCOM(i)   = XH(i) + SUM(j,SECT, XC(i,j))        i in SECT          E3.1.6  
(E6)  XFAC(f)   = SUM(j,SECT, XF(f,j))                f in FAC           E3.1.7  
(E7)  PC("s1")  = 1.                                                     E3.1.23 
(E8)  XC(i,j)   = DVCOMIN(i,j) / PC(i)                i,j in SECT           -
(E9)  XH(i)     = DVHOUS(i) / PC(i)                   i in SECT             -
(E10) XF(f,j)   = DVFACIN(f,j) / PF(f)                f in FAC, j in SECT   -
These equations appear essentially as above in the TABLO Input file (see section
4.3.3
below).
4.2    Data requirements for the linearized equations
[gpd1.3.2]
As a general rule, GEMPACK requires an initial levels solution of the model. Thus it is necessary
to provide data from which initial (that is, pre-simulation) values of all levels variables and the
values of all parameters of the model can be inferred. As we shall see in section
4.2.1
for Stylized Johansen, it is frequently the case that the data required are
mainly dollar values (rather than separate prices and quantities), and
certain parameters (such as elasticities).
Once dollar values are known, it is often possible to set basic prices equal to 1 (this amounts to
a choice of units for the related quantities), from which the quantities can be derived by dividing
the dollar value by the price.  [The choice of 1 for the basic price is, of course, arbitrary.  Any
other fixed value would be as good.]
4.2.1    Data requirements for Stylized Johansen
[gpd1.3.2.1]
Suppose that we know the following pre-simulation dollar values.
DVCOMIN(i,j)    Intermediate inputs
DVHOUS(i)       Household consumption
DVFACIN(f,j)    Factor use by industry
Then, if we set all the prices to one for
PC(i)           Price of commodities
PF(f)           Price of factors
we can infer all other levels variables in Table
4.2
as follows.
XC(i,j) = DVCOMIN(i,j) / PC(i)      Intermediate inputs     
XH(i)   = DVHOUS(i) / PC(i)         Household use     
XF(f,j) = DVFACIN(i,j) / PF(f)      Factor use     
Y       = SUM(i, SECT, DVHOUS(i))   Household expenditure
The only other quantities in the equations (E1)-(E10) are the parameters ALPHACOM(i,j) and
ALPHAFAC(f,j) in (E4). Because there is a Cobb-Douglas production function involved, it is
well-known that these are cost shares, namely
ALPHACOM(i,j) = DVCOMIN(i,j) / DVCOSTS(j),     
ALPHAFAC(f,j) = DVFACIN(f,j) / DVCOSTS(j),
where DVCOSTS(j) is an abbreviation for
SUM(i, SECT, DVCOMIN(i,j)) + SUM(f, FAC,  DVFACIN(f,j)),
the total costs in industry j.  [These results are easily obtained from equations (E3.1.10) and
(E3.1.12) in
DPPW
.]
Thus the only data requirements are the dollar values
DVHOUS(i),  DVCOMIN(i,j)  and  DVFACIN(f,j)
One instance of the data required is as shown in the body of Table
3.1
in section
3.1.1
above.
In the TABLO Input file, the pre-simulation values of these data will be read and the values of all
others will be calculated from them.
4.3    Constructing the TABLO input file for a model
[gpd1.3.3]
The TABLO Input file of the model is the means of communicating the theory of the model to the
computer, in particular to the GEMPACK program TABLO. It consists of the equations written in a
syntax which is very similar to ordinary algebra. It also contains a description of the data to be
read, where it is to be read from, and how this data is to be used to calculate values of
parameters and pre-simulation values of the other levels variables occurring in the equations.
The main part of a TABLO Input file is the equations, which usually come at the end of the file.
Before the equations must come
the VARIABLEs (levels or linearized);
the SETs used to describe the different arguments of variables;
the data to be read;
calculations of the pre-simulation values of any levels variables not read in as data (calculations
are done via FORMULAs);
calculations (via FORMULAs) of any parameters whose values are not read in;
logical names of the associated data files;
the headers on the data file(s) where the different pieces of data are to be found (if the data
files are GEMPACK Header Array files — see chapter
5
).
The order of these in the TABLO Input file is somewhat flexible but follows the general rule that
items cannot be used until they have been declared. Thus the SET statements (saying which sets are
involved) usually come first. Then the declarations of data files (via FILE statements) often come
next, followed by the declarations of the VARIABLEs and parameters.
These ideas are best learnt and understood by example. Hence we launch straight into the
preparation of the TABLO Input file for Stylized Johansen.
4.3.1    Viewing the TABLO input file
[gpd1.3.3.1]
When working with GEMPACK, many of the input files that you create are text files, so you need a
text editor.  You can use any text editor you are familiar with.
GEMPACK includes two text editors, TABmate and GemEdit. We suggest you use TABmate since it has
coloured highlighting of TABLO syntax, and a powerful Gloss feature which displays all parts of the
TABLO code where a chosen variable or coefficient is used. If TABmate is not the default editor in
WinGEM, select, in the WinGEM main menu,
Options | Change editor...
then select your editor
Use TABmate
.   You should only have to do this once: WinGEM should
remember which editor you  chose.
Open the TABLO Input file for Stylized Johansen SJ.TAB in the TABmate editor. In WinGEM, to edit a
text file, select in the WinGEM menu,
File | Edit file
...
The edit box should show various files in the directory C:\SJ. If the Open box does not start at
the correct directory C:\SJ, set the Working directory again as described in section
3.4.2
.
Select the file SJ.TAB, the TABLO Input file for the Stylized Johansen model.
Search the TABLO Input file for "EQUATION House" using   Search | Find. We will discuss the details
of this equation in the next section.
4.3.2    Constructing part of the TABLO input file for Stylized Johansen
[gpd1.3.3.2]
In this subsection we consider just two equations of Stylized Johansen, namely (E9) and (E4) in
section
4.1.1
above. We show how these are written in the TABLO Input file. (We show
the full TABLO Input file in section
4.3.3
and then discuss the rest of this file in
section
4.3.4
below.)
Equation (E9)
Consider the very simple equation (E9) relating prices, quantities and dollar values of household
consumption.
In the TABLO Input file this equation is written as
2
EQUATION House # Household demand for commodity i #
    (all,i,SECT) XH(i) = DVHOUS(i) / PC(i) ;
where
EQUATION is a keyword indicating that what follows is an equation,
House is the name by which this equation is known in the model,
the words between the hashes # form optional additional labelling information which is associated
with the equation,
the quantifier (all,i,SECT) indicates that there are really several equations, one for each sector,
and
the semicolon
;
marks the end of this part of the equation statement.
For this equation to be meaningful, we must explain in the TABLO Input file all the names used in
the equation.
The levels variables are declared (that is, explained) via the statements
VARIABLE (all,i,SECT) XH(i)  .    # Household demand for commodity i # ; 
VARIABLE (all,i,SECT) DVHOUS(i).  # Dollar value of household use of commodity i # ; 
VARIABLE (all,i,SECT) PC(i)       # Price of commodity i # ;
Notice that, by convention, these declarations also declare associated linear variables p_XH,
p_DVHOUS and p_PC which denote the percentage-change in the relevant levels variables. These linear
variable names are used in reporting simulation results (see the results in section
3.7
above, for example) and are available for use in linearized equations in the TABLO
Input file (see, for example, the EQUATION named "Price_formation" discussed later in this section)
without further explicit declaration.
The fact that SECT is a set with two sectors "s1" and "s2" in it is indicated via the SET statement
SET SECT  # Sectors #   (s1-s2) ;
We must also indicate how pre-simulation values of the levels variables can be read or calculated
from the data base. We do this via the statements
READ DVHOUS  from FILE iodata HEADER "HCON" ; 
FORMULA (all,i,SECT)   PC(i) = 1 ; 
FORMULA (all,i,SECT)   XH(i) = DVHOUS(i)/PC(i) ;
In the first of the above statements,
READ is the keyword,
iodata is the (logical) name by which the particular data file containing this input-output data is
known in the TABLO Input file, and
the Header "HCON" tells where on the file the relevant array of data is to be found.
In the second and third statements, FORMULA is the keyword.
The third of these contains the same expression as the equation we are considering. Indeed, we can
combine the EQUATION and FORMULA into a single statement on the TABLO Input file, namely.
3
FORMULA & EQUATION House # Household demand for commodity i #
  (all,i,SECT)   XH(i) = DVHOUS(i) / PC(i) ;
The statement
FILE iodata # input-output data for the model # ;
declares "iodata" as the logical name
4
of the file containing the actual data.
This ends the discussion of the equation (E9) and of all the statements needed for the EQUATION
House.
Using the Gloss feature in TABmate
In TABmate, there is a quick way of finding all places where a name such as XH occurs in the TABLO
Input file SJ.TAB. In TABmate, click on   TABLO Check   in the bar near the top of the TABmate
screen
5
. Click on the word EQUATION in the "EQUATION House" and then click on   Gloss   in the bar

near the top of the TABmate screen. A box (shown below) appears showing all names used in the
EQUATION House in the TABLO Input file.
FORMULA & EQUATION House # Household demand for commodity i # 
   (all,i,SECT) XH(i) = DVHOUS(i) / PC(i) ;
Line
~41: SET SECT # Sectors # (s1-s2) ;
~69: Coefficient Variable (GE 0) (all,i,SECT) XH(i) # Household demand for commodity i # ;
~86: Coefficient Variable (GE 0) (all,i,SECT) DVHOUS(i)
                                        # Dollar value of household use of commodity i # ;
~59: Coefficient Variable (GE 0) (all,i,SECT) PC(i) # Price of commodity i # ;
Click on the X in the top right-hand corner of the Glossary box to exit from the Gloss box.
Click on the word XH in the "EQUATION House" and then click on the  Gloss  button. The Gloss box
(shown below) appears showing all occurrences of the name XH in the TABLO Input file.
Coefficient   XH
Line
~69: Variable (GE 0) (all,i,SECT) XH(i) # Household demand for commodity i # ;
~138: FORMULA & EQUATION House # Household demand for commodity i #
   (all,i,SECT) XH(i) = DVHOUS(i) / PC(i) ;
~142: FORMULA & EQUATION Com_clear # Commodity market clearing #
   (all,i,SECT) XCOM(i) = XH(i)+SUM(j,SECT,XC(i,j));
Try clicking on the word DVHOUS to see where DVHOUS is used in the TABLO Input file SJ.TAB.
Equation (E4)
Now consider the equation (E4) "price formation for commodities". This is written in the TABLO
Input file as
EQUATION (LINEAR) Price_formation 
         (all,j,SECT) p_PC(j) = SUM(i,SECT, ALPHACOM(i,j)*p_PC(i)) +
                                SUM(f,FAC,  ALPHAFAC(f,j)*p_PF(f)) ;
in which
the qualifier (LINEAR) indicates that this is a linearized equation (not a levels equation),
the fact that p_PC(i) and p_PF(f) are percentage-changes in the levels variables PC(i) and PF(f) is
guaranteed by the convention that, once these levels variables have been declared via
VARIABLE (all,i,SECT) PC(i) # Price of commodity i # ; 
VARIABLE (all,f,FAC)  PF(f) # Price of factor f # ;
the associated linear variables p_PC(i) and p_PF(f) are automatically considered declared.  In this
equation, ALPHACOM and ALPHAFAC are parameters. To calculate ALPHACOM and ALPHAFAC from the data
base, FORMULA statements are used:
FORMULA  .# Share of intermediate commodity i in costs of industry j # 
(all,i,SECT)(all,j,SECT)  ALPHACOM(i,j) = DVCOMIN(i,j) /
    [SUM(ii,SECT,DVCOMIN(ii,j)) + SUM(ff,FAC,DVFACIN(ff,j)) ] ;
FORMULA  .# Share of factor input f in costs of industry j # 
(all,f,FAC)(all,j,SECT)  ALPHAFAC(f,j) = DVFACIN(f,j) /
    [SUM(ii,SECT,DVCOMIN(ii,j)) + SUM(ff,FAC,DVFACIN(ff,j)) ] ;
where FORMULA is the keyword. The fact that ALPHACOM and ALPHAFAC are parameters can be indicated
via the statements
COEFFICIENT(PARAMETER) (all,i,SECT)(all,j,SECT) ALPHACOM(i,j) ;
COEFFICIENT(PARAMETER) (all,f,FAC) (all,j,SECT) ALPHAFAC(f,j) ;
in which COEFFICIENT is the keyword and (PARAMETER) is a qualifier.
If you are using the TABmate editor, try using the  Gloss  button. Click on the word p_PC in the
EQUATION Price_formation and click on the Gloss button to see all occurrences of p_PC in the TABLO
Input file SJ.TAB. Click on the word "FAC" and  Gloss  to see all occurrences of the set FAC.
This ends the discussion of the equation (E4) and of all the statements needed for the EQUATION
Price_formation.
Statements in a TABLO Input File
The main types of statements in a TABLO Input file, namely EQUATIONs, FORMULAs, READs, VARIABLEs,
COEFFICIENTs, SETs and FILEs have been introduced in connection with equations House (E9) and
Price_formation (E4) above
Each entity (VARIABLE, COEFFICIENT, etc) must be declared in the TABLO Input file before it is used
in EQUATIONs and FORMULAs. This partly determines the order of the statements in the TABLO Input
file.
We suggest that you now look at the complete TABLO Input file for this model, as set out in section
4.3.3
below, or using the editor TABmate (or your text editor). This file is usually
called SJ.TAB when supplied with the GEMPACK Examples. You will find all the statements shown above
in that file.
Since declarations must come before use, you will find the TABLO statements in pretty much the
reverse order from that in which we have introduced them above.
We discuss the rest of this TABLO Input file in section
4.3.4
.
6
4.3.3    "Mixed" TABLO input file for the Stylized Johansen model
[gpd1.3.3.3]
!-------------------------------------------------------------------! 
!                  Mixed TABLO Input file for the                   ! 
!                    Stylized Johansen model                        !
!                                                                   !
!         following the description in Chapter 3 of the text        ! 
!   "Notes and Problems in Applied General Equilibrium Economics"   ! 
!       by P.Dixon, B.Parmenter, A.Powell and P.Wilcoxen [DPPW]     ! 
!              published by North-Holland 1992.                     ! 
!                                                                   ! 
!-------------------------------------------------------------------!  
! Text between exclamation marks is a comment.                      ! 
! Text between hashes (#) is labelling information.                 !  
!-------------------------------------------------------------------! 
!     Set default values                                            ! 
!-------------------------------------------------------------------! 
VARIABLE (DEFAULT = LEVELS) ; 
EQUATION (DEFAULT = LEVELS) ; 
COEFFICIENT (DEFAULT = PARAMETER) ; 
FORMULA (DEFAULT = INITIAL) ;
!-------------------------------------------------------------------! 
!      Sets                                                         ! 
!-------------------------------------------------------------------!  
! Index values i=1,2 in DPPW correspond to the sectors called s1,s2. 
  Index values i=3,4 in DPPW correspond to the primary factors, 
  labor and capital.   The set SECT below doubles as the set of  
  commodities  and the set of industries. !  
SET SECT # Sectors # (s1-s2)  ;  
SET FAC # Factors  # (labor, capital) ;  
SET NUM_SECT # Numeraire sector - sector 1 #  (s1) ;  
SUBSET  NUM_SECT is subset of SECT ;
!-------------------------------------------------------------------! 
!      Levels variables                                             ! 
!-------------------------------------------------------------------!  
! In the DPPW names shown below, : denotes subscript.               ! 
! For example, x:j indicates that j is a subscript.                 ! 
VARIABLE               Y    # Total nominal household expenditure #
                              ! This is also Y in DPPW ! ; 
VARIABLE (all,i,SECT)  PC(i)   # Price of commodity i #
                                ! This is p:i (i=1,2) in DPPW ! ; 
VARIABLE (all,f,FAC)   PF(f)   # Price of factor f #
                                ! This is p:i (i=3,4) in DPPW ! ; 
VARIABLE (all,i,SECT)  XCOM(i)   ! This is x:i (i=1,2) in DPPW !
       # Total demand for (or supply of) commodity i # ;
VARIABLE (all,f,FAC)   XFAC(f)   ! This is x:i (i=3,4) in DPPW !
      # Total demand for (or supply of) factor f    # ; 
VARIABLE (all,i,SECT)  XH(i)   # Household demand for commodity i #
                                ! This is x:i0 (i=1,2) in DPPW ! ; 
VARIABLE (all,i,SECT) (all,j,SECT)     XC(i,j)
      # Intermediate inputs of commodity i to industry j #
     ! This is x:ij (i,j=1,2) in DPPW ! ; 
VARIABLE (all,f,FAC)(all,j,SECT)       XF(f,j)
      # Factor inputs to industry j #
     ! This is x:ij (i=3,4; j=1,2) in DPPW ! ;
!-------------------------------------------------------------------! 
!     Dollar values read in from database                           ! 
!-------------------------------------------------------------------! 
VARIABLE (all,i,SECT)(all,j,SECT)      DVCOMIN(i,j)
      # Dollar value of inputs of commodity i to industry j # ; 
VARIABLE (all,f,FAC)(all,j,SECT)       DVFACIN(f,j)
     # Dollar value of factor f used in industry j # ; 
VARIABLE (all,i,SECT)                  DVHOUS(i)
      # Dollar value of household use of commodity i # ;  
!-------------------------------------------------------------------!
!     Parameters                                                    ! 
!-------------------------------------------------------------------! 
COEFFICIENT (all,i,SECT)(all,j,SECT)  ALPHACOM(i,j)
   # Share of intermediate use of commodity i in costs of industry j # ;
COEFFICIENT (all,f,FAC)(all,j,SECT)   ALPHAFAC(f,j)
   # Share of factor input f in costs of industry j # ;  
!-------------------------------------------------------------------! 
!      File                                                         ! 
!-------------------------------------------------------------------!  
FILE iodata # input-output data for the model # ;
!-------------------------------------------------------------------! 
!      Reads from the data base                                     ! 
!-------------------------------------------------------------------!  
READ DVCOMIN from FILE iodata HEADER "CINP" ; 
READ DVFACIN from FILE iodata HEADER "FINP" ; 
READ DVHOUS  from FILE iodata HEADER "HCON" ;
!-------------------------------------------------------------------!
!      Formulas                                                     ! 
!-------------------------------------------------------------------! 
FORMULA (all,i,SECT) PC(i) = 1.0 ; 
FORMULA (all,i,FAC) PF(i) = 1.0 ; 
FORMULA (all,i,SECT)(all,j,SECT) ALPHACOM(i,j) = DVCOMIN(i,j) /
            [SUM(ii,SECT,DVCOMIN(ii,j)) + SUM (ff,FAC,DVFACIN(ff,j))] ;
FORMULA (all,f,FAC)(all,j,SECT) ALPHAFAC(f,j) = DVFACIN(f,j) /
            [SUM(ii,SECT,DVCOMIN(ii,j)) + SUM (ff,FAC,DVFACIN(ff,j))] ;

! Formula to give initial value of Y !
FORMULA Y = SUM(i,SECT,DVHOUS(i)) ;
!-------------------------------------------------------------------! 
!       Formulas and levels equations                               ! 
!-------------------------------------------------------------------! 
FORMULA & EQUATION Comin
     # Intermediate input of commodity i to industry j #
   (all,i,SECT)(all,j,SECT) XC(i,j) = DVCOMIN(i,j) / PC(i) ;  
FORMULA & EQUATION Facin      # Factor input f to industry j #
 (all,f,FAC)(all,j,SECT) XF(f,j) = DVFACIN(f,j) / PF(f) ;
FORMULA & EQUATION House      # Household demand for commodity i #
 (all,i,SECT) XH(i) = DVHOUS(i) / PC(i) ;         
FORMULA & EQUATION Com_clear ! (E3.1.6) in DPPW !
    # Commodity market clearing #
 (all,i,SECT) XCOM(i) = XH(i) + SUM(j,SECT,XC(i,j)) ;  
FORMULA & EQUATION Factor_use ! (E3.1.7) in DPPW !
     # Aggregate primary factor usage #
 (all,f,FAC) XFAC(f) = SUM(j,SECT,XF(f,j)) ;
!-------------------------------------------------------------------! 
!      Equations                                                    ! 
!-------------------------------------------------------------------! 
EQUATION(LINEAR)  Consumer_demands ! (E3.2.1) in DPPW !
     # Household expenditure functions #
 (all,i,SECT) p_XH(i) = p_Y - p_PC(i) ;
EQUATION(LINEAR)  Intermediate_com
! From (E3.2.2) with i=1,2 in DPPW. The term p_PC(j) is included
   because of (E3.2.3) in DPPW. !
    # Intermediate demands for commodity i by industry j #
(all,i,SECT)(all,j,SECT) p_XC(i,j) = p_XCOM(j) - (p_PC(i) - p_PC(j)) ;
EQUATION(LINEAR)  Factor_inputs
! From (E3.2.2) with i=3,4 in DPPW. The term p_PC(j) is included
   because of (E3.2.3) in DPPW. !
    # Factor input demand functions #
(all,f,FAC)(all,j,SECT) p_XF(f,j) = p_XCOM(j) - (p_PF(f) - p_PC(j)) ;
EQUATION(LINEAR) Price_formation   ! (E3.2.3) in DPPW !
     # Unit cost index for industry j #
 (all,j,SECT) p_PC(j) = SUM(i,SECT,ALPHACOM(i,j)*p_PC(i)) + 
                               SUM(f,FAC,ALPHAFAC(f,j)*p_PF(f)) ;
EQUATION Numeraire  ! (E3.1.23) in DPPW !
     # Price of commodity 1 is the numeraire #
 (all,i,NUM_SECT)  PC(i) = 1 ;
!--------------end of TABLO Input file------------------------------!
4.3.4    Completing the TABLO input file for Stylized Johansen
[gpd1.3.3.4]
Notice that the TABLO Input file consists of a number of statements, each beginning with its
relevant keyword (such as SET or VARIABLE). Some statements include a qualifier such as (LINEAR) in
EQUATION(LINEAR). Each statement ends with a semicolon ';'. Text between exclamation marks '!' is
treated as a comment; such text can go anywhere in the TABLO Input file. Text between hashes '#' is
labelling information; the positioning of this labelling information is restricted (see chapter
10
for full details).
The TABLO Input file is not case-sensitive so for example, XH and Xh would be identical so far as
TABLO is concerned.
First come the DEFAULT statements. In TABLO Input files, EQUATIONs and VARIABLEs can be linear or
levels. It is possible to distinguish each type by using the appropriate qualifier (LEVELS) or
(LINEAR) after the keyword each time, as in, for example,
VARIABLE (LEVELS) Y # Nominal household expenditure # ; 
VARIABLE (LINEAR) (all,f,FAC) p_PF(f) # Price of factors # ;
When most variables being declared are levels variables, it seems wasteful to have to keep
repeating the qualifier (LEVELS). There are DEFAULT statements which allow you to reduce the number
of qualifiers required in your TABLO Input files. If you put the statement
VARIABLE (DEFAULT = LEVELS) ;
early in a TABLO Input file, then, after it, any VARIABLE declaration is taken as the declaration
of a levels variable unless a different qualifier (LINEAR) is present. Similarly for EQUATIONs
coming after the statement
EQUATION (DEFAULT = LEVELS) ;
Of course, if most equations in your TABLO Input file are linearized ones, you could put the
opposite default statement
EQUATION (DEFAULT = LINEAR) ;
near the start of your file, and then you would only have to flag, using the qualifier (LEVELS),
the levels equations.
Similarly, the statements
COEFFICIENT (DEFAULT = PARAMETER) ; 
FORMULA (DEFAULT = INITIAL) ;
set the default types for COEFFICIENTs declared and FORMULAs. The only COEFFICIENTs in the TABLO
Input file in section
4.3.3
above are parameters, while the only FORMULAs are used to
set initial values (that is, pre-simulation values) of levels variables, or to set the values of
the parameters. You will see non-parameter COEFFICIENTs and non-initial FORMULAs in section
4.4.1
below, when you look at linearized TABLO Input files.
Next come the declarations of the SETs, namely SECT (sectors) and FAC (primary factors). A further
set NUM_SECT to stand for the single numeraire sector (sector s1) is also defined; this is only
used for the last of the equations, the numeraire equation. The reason for the SUBSET statement
will be explained when we discuss that equation below.
Then come the declarations of the VARIABLEs. Note that the arguments (if any) of each are clearly
described, using the "(all,<index>,<set-name>)" quantifier(s) at the start of the
declarations.
These quantifiers refer to the SETs, which is why the SET declarations must precede the VARIABLE
declarations.  The variables declared are all levels variables (because of the DEFAULT statement
earlier). Although not explicitly mentioned here, the associated linear variables p_Y, p_XH etc are
taken as automatically declared by convention, and can be used in subsequent EQUATIONs without
further explicit declaration.
Then comes the declaration of the parameters - which must always be declared as COEFFICIENTs. The
qualifier (PARAMETER) is not needed here because of the earlier DEFAULT(COEFFICIENT=PARAMETER)
statement.
Next comes the declaration of the single data FILE required. This file is given the logical name
'iodata'. The actual name of the file on your computer containing this data is not limited by this
logical name. You can give the actual file any convenient name. GEMSIM or the TABLO-generated
program will prompt you for this actual name when you run it; the prompt will use the logical name
'iodata' from the TABLO Input file. Or, if you use a GEMPACK Command file (as we recommend), you
will need to use the logical name as well as the actual name in the relevant statement (for
example, "file  iodata  =  SJ.HAR ;").  See section
22.1
for more details.
Then come READ statements telling the program to read in initial (that is, pre-simulation) values
of certain levels variables. Each READ statement says from where the data is to be read (that is,
which file and which header on the file).
Next come some FORMULAs assigning initial values to other levels variables. The left-hand side of a
FORMULA (that is, the part before the '=' sign) must be a simple VARIABLE or COEFFICIENT, but the
right-hand side can be a complicated expression. In such an expression, the symbols for the
arithmetic operations are '+' and '-' for addition and subtraction, '*' and '/' for multiplication
and division, and '^' for exponentiation. Note that '*' must be shown explicitly wherever
multiplication is required. Notice also the use of the syntax
SUM(<index>,<set-name>, <expression to be summed> )
to express sums over sets.
Finally come the EQUATIONs (see (E1) to (E10) in section
4.1.1
above). As explained in
section
4.3.2
, some of these double as FORMULAs, in which case the statement must
begin with FORMULA & EQUATION to indicate that there are really two statements here.
The syntax of the last equation (the numeraire equation) may surprise you.  We could have expressed
this as
PC("s1") = 1 ;
using the sector element name "s1" to indicate which price is fixed at one. Instead we have
introduced the new set NUM_SECT consisting of just this sector "s1" and written the equation as
(all,i,NUM_SECT)  PC(i) = 1 ;
This illustrates the point of SUBSET declarations. The VARIABLE PC has been declared to have one
argument ranging over the set SECT, but here we need to give it an argument ranging over the
smaller set NUM_SECT. The earlier SUBSET statement
SUBSET  NUM_SECT  is subset of  SECT ;
alerts TABLO to the fact that an argument ranging over NUM_SECT is always in the set SECT. Without
this, the use of PC(i) with i ranging over NUM_SECT would trigger a semantic error since TABLO
checks that all arguments range over appropriate sets.
As stated earlier, the order of the statements in the TABLO Input file can be varied. For example,
especially with larger models, some COEFFICIENTs may only be relevant to a small number of the
EQUATIONs and it may be better to declare these and assign values to them just before the relevant
EQUATION or group of EQUATIONs.
WRITE statements send the values of COEFFICIENTs (or levels VARIABLEs) to a file so
you can examine them (or use them as a input to another program). Try this out by adding the
following statements at the end of the TABLO Input file for Stylized Johansen and then re-running
Steps 1, 2 and 3 in chapter
3
.
File (new) Output;
Write ALPHACOM to file Output header "ACOM";
Write ALPHAFAC to file Output header "AFAC";
You'll also need to add into the CMF the line:
file Output = <cmf>out.har;
Complete documentation of TABLO Input files is given in chapters
8
to
18
,
which you will need to consult when you start to build a new model.
4.3.5    Change or percentage-change variables
[gpd1.3.3.5]
Many levels variables (for example, prices, quantities, dollar values) are always positive and so
it is natural for the associated linear VARIABLE to be a percentage change.
However, when the relevant levels variable can be positive or zero or negative (examples are the
Balance of Trade and an ad valorem tax rate), it is wiser to specify that the associated linear
VARIABLE is an ordinary change.  This is because, in such a case, if the levels value happens to be
zero at the start of any step of a multi-step simulation, the associated percentage change could
not be calculated (since it would require division by zero).  Also, there are often numerical
problems (which slow or hinder convergence of the solutions) when a percentage-change variable
changes sign in the levels; these problems may be overcome if an ordinary change variable is used because then TABLO works
with a slightly different linearization of the EQUATIONs involving this VARIABLE.
7
In summary, we suggest the following guidelines.
For levels variables which are always positive (or always negative), work with the associated
percentage change as a linear VARIABLE.
For levels variables which may change sign, declare  the associated linear VARIABLE to be an
ordinary change. In this case, when declaring the levels variable, insert the qualifier (CHANGE)
after the keyword VARIABLE.
The  (CHANGE) qualifier tells TABLO to automatically declare the associated  linear variable as an
ordinary change (the prefix "c_" is usually added to the levels name).
8
For example, if you have a declaration
VARIABLE (CHANGE) BT  # Balance of trade # ;
in your TABLO Input file, the associated change linear variable c_BT is automatically available for
use in linearized equations and will be used in reporting simulation results. Alternatively a
linear change variable can be declared directly, using the two qualifiers LINEAR and CHANGE as in.
VARIABLE (LINEAR,CHANGE) delB  # Change in trade balance # ;
(When you declare a linear change variable explicitly, you are not required to begin the name with
"c_".)
4.3.6    Variable or parameter ?
[gpd1.3.3.6]
When you build a model, you have in mind the sorts of questions you will be using the model to
answer. You may be thinking of holding some quantities constant and varying others.
Within GEMPACK, the quantities you may wish to vary will be declared as VARIABLEs while those which
cannot vary can be declared as COEFFICIENT(PARAMETER)s.
Traditionally GEMPACK users declare as VARIABLEs (rather than as parameters) any quantity which
might conceivably vary.
9
For example, you may have a model which includes tax rates which you do not (at present) intend to
vary. You could declare them as COEFFICIENT(PARAMETER)s but it may be more useful to declare them
as VARIABLEs. In the latter case, you can convey the fact that they do not vary by indicating that
the VARIABLEs are exogenous and not shocked.
10
Later, if you wish to model the consequences of these tax rates changing, you do not have to change
the model.
In Stylized Johansen, there are only two exogenous variables, the supplies of the primary factors
labor and capital, so this issue does not arise. However, it does arise in most of the more serious
models implemented via GEMPACK. For example, in ORANI-G (see section
60.5
), many
quantities which do not change in most simulations (for example, household subsistence demands,
various technology terms and various shifters) are declared as Variables rather than as Parameters.
4.3.7    TABLO language - syntax and semantics
[gpd1.3.3.7]
Full details of the syntax and semantics used in TABLO Input files are given
in chapters
10
to
11
.
The description there  applies to all TABLO Input files - that is, to
those containing just levels equations, just linearized ones and to those (such as the one in
section
4.3.3
above) containing a mixture of levels and linearized equations. We will
introduce more information about the syntax and semantics in sections
4.4
and
4.5
below (where we describe alternative TABLO Input files for Stylized Johansen,
firstly one containing just linearized equations and secondly one containing just levels equations).
4.4    Linearized TABLO input files
[gpd1.3.4]
The majority of the more well-known models implemented in GEMPACK use a TABLO Input file
containing only linearized equations; we refer to such TABLO Input files as linearized TABLO Input
files.
We illustrate this by giving in full in section
4.4.1
below such a TABLO Input file
for Stylized Johansen. This file is usually called SJLN.TAB when supplied with the GEMPACK Example
files.
In comparison with the mixed TABLO Input file for Stylized Johansen in section
4.3.3
above, the main differences to note are as follows.
The linear VARIABLEs are declared explicitly.
The levels variables do not seem to be present. But in fact, in a linearized TABLO Input file, many
of these are declared as COEFFICIENTs. Thus, in TABLO Input files, COEFFICIENTs have two
functions:
1. They can denote the (pre-simulation) values of a levels variable.
2. They can
denote parameters.
In a linearized TABLO Input file, the requirement that an initial solution be obtainable from the
data base means that the values of all COEFFICIENTs occurring in the linearized EQUATIONs must have
their values defined (via READs or FORMULAs).
It is necessary to provide UPDATE statements to tell how the data read from the data base changes
in response to small changes in the relevant linear VARIABLEs. (It helps to think in terms of a
multi-step simulation as described in section
3.12.3
above. After each step, the data
base has to be updated to take into account changes in all the linear VARIABLEs over the step.) We
give a more detailed discussion of UPDATE statements in section
4.4.4
below. One role
of UPDATE statements is to provide the link between the linear VARIABLEs and the COEFFICIENTs (that
is, levels variables).
We give the full TABLO Input file in section
4.4.1
and then discuss noteworthy
features of it in section
4.4.2
below.
Advice about linearizing equations by hand can be found in section
18.2
.
4.4.1    A linearized TABLO input file for Stylized Johansen
[gpd1.3.4.1]
!-------------------------------------------------------------------!
!               Linearized TABLO Input file for the                 !
!                       Stylized Johansen model                     !
!           following the description in Chapter 3 of the text      !
!    "Notes and Problems in Applied General Equilibrium Economics"  !
!       by P.Dixon, B.Parmenter, A.Powell and P.Wilcoxen [DPPW]     !
!                published by North-Holland 1992.                   !
!-------------------------------------------------------------------!
! Text between exclamation marks is a comment.                      !                        
! Text between hashes (#) is labelling information.                 !
!-------------------------------------------------------------------!
!      Sets                                                         !
!-------------------------------------------------------------------!
! Index values i=1,2 in DPPW correspond to the sectors called s1,s2.
  Index values i=3,4 in DPPW correspond to the primary factors, labor 
  and capital.   The set SECT below doubles as the set of 
  commodities  and the set of industries. !
SET
 SECT # Sectors # (s1-s2)  ;
 FAC # Factors  # (labor, capital) ;
 NUM_SECT # Numeraire sector - sector 1 #  (s1) ;
SUBSET  NUM_SECT is subset of SECT ;
!-------------------------------------------------------------------!
!  File                                                             !
!-------------------------------------------------------------------!
 FILE iodata # the input-output data for the model # ;
!-------------------------------------------------------------------!
VARIABLE ! All variables are percent changes in relevant levels quantities !
!  In the DPPW names shown below,  : denotes subscript.             !
!  Thus, for example,   x:j indicates that j is a subscript.        !
 (ORIG_LEVEL=Y) p_Y  # Total household expenditure [DPPW y]#; 
 (ORIG_LEVEL=1) (all,i,SECT) p_PC(i) 
     # Price of commodities [DPPW p:i (i=1,2)]#;
 (ORIG_LEVEL=1) (all,f,FAC) p_PF(f)  
     # Price of factors [DPPW p:i  (i=3,4)]#;
 (ORIG_LEVEL=DVCOM) (all,i,SECT) p_XCOM(i)  
     # Total demand for (or supply of) commodities [DPPW x:i (i=1,2)]#;
 (ORIG_LEVEL=DVFAC) (all,f,FAC) p_XFAC(f)  
     # Total demand for (or supply of) factors [DPPW x:i  (i=3,4)]#;
 (ORIG_LEVEL=DVHOUS) (all,i,SECT) p_XH(i)  
     # Household consumption of commodities [DPPW x:i0  (i=1,2)]#;
 (ORIG_LEVEL=DVCOMIN) (all,i,SECT)(all,j,SECT) p_XC(i,j)  
     # Intermediate commodity inputs [DPPW x:ij  (i,j=1,2)]#;
 (ORIG_LEVEL=DVFACIN) (all,f,FAC)(all,j,SECT) p_XF(f,j)  
     # Intermediate factor inputs [DPPW x:ij  (i=3,4; j=1,2)]#;
!-------------------------------------------------------------------!
!  Base data, updates and reads                                     !
!   (Base data is as in Table E3.3.1 of DPPW)                       !
!-------------------------------------------------------------------!
 COEFFICIENT (GE 0)  (all,i,SECT)(all,j,SECT) DVCOMIN(i,j)  
   # Dollar value of inputs of commodity i to industry j # ;
 UPDATE (all,i,SECT)(all,j,SECT) DVCOMIN(i,j) = p_PC(i)*p_XC(i,j) ;

 COEFFICIENT (GE 0)  (all,f,FAC)(all,j,SECT)  DVFACIN(f,j)  
   # Dollar value of inputs of factor f to industry j # ;
 UPDATE (all,f,FAC)(all,j,SECT)  DVFACIN(f,j) = p_PF(f)*p_XF(f,j) ;

 COEFFICIENT (GE 0)  (all,i,SECT) DVHOUS(i)  
   # Dollar value of household use of commodity i # ;
 UPDATE (all,i,SECT)             DVHOUS(i) = p_PC(i)*p_XH(i) ;
!-------------------------------------------------------------------!
!  Reads from the data base                                         !
!-------------------------------------------------------------------!
 READ DVCOMIN FROM FILE iodata HEADER "CINP" ;
 READ DVFACIN FROM FILE iodata HEADER "FINP" ;
 READ DVHOUS  FROM FILE iodata HEADER "HCON" ;
!-------------------------------------------------------------------!
!  Other coefficients and formulas for them                         !
!-------------------------------------------------------------------!
 COEFFICIENT  Y    # Total nominal household expenditure # ;
 FORMULA Y = SUM(i,SECT,DVHOUS(i)) ;

 COEFFICIENT (all,i,SECT) DVCOM(i) # Value of total demand for commodity i # ;
 FORMULA     (all,i,SECT) DVCOM(i) = SUM(j,SECT, DVCOMIN(i,j)) + DVHOUS(i) ;
 
 COEFFICIENT (all,f,FAC) DVFAC(f) # Value of total demand for factor f # ;
 FORMULA     (all,f,FAC) DVFAC(f) =  SUM(j,SECT,DVFACIN(f,j)) ;

 COEFFICIENT(PARAMETER)   (all,i,SECT)(all,j,SECT) ALPHACOM(i,j)  
   # alpha(i,j) - commodity parameter in Cobb-Douglas production function # ;
   ! = initial share of commodity i in total inputs to industry j  
     This is  alpha:ij  (i=1,2; j=1,2) in (E3.1.4) of DPPW ! 
 FORMULA(INITIAL)(all,i,SECT)(all,j,SECT) ALPHACOM(i,j) = DVCOMIN(i,j)/DVCOM(j);
 
COEFFICIENT(PARAMETER)   (all,f,FAC)(all,j,SECT) ALPHAFAC(f,j)  
   # alpha(f,j) - factor parameter in Cobb-Douglas production function. #;
   ! = initial share of factor f in total inputs to industry j  
     This is  alpha:ij  (i=3,4; j=1,2) in (E3.1.4) of DPPW !  
 FORMULA(INITIAL)(all,f,FAC)(all,j,SECT) ALPHAFAC(f,j) = DVFACIN(f,j)/DVCOM(j);

 COEFFICIENT   (all,i,SECT)(all,j,SECT) BCOM(i,j)  
   # beta(i,j) - share of industry j in total demand for commodity i # ; 
   ! This is  beta:ij  (i=1,2; j=1,2) in (E3.2.4) of DPPW !  
 FORMULA   (all,i,SECT)(all,j,SECT) BCOM(i,j) = DVCOMIN(i,j)/DVCOM(i) ;

 COEFFICIENT   (all,i,SECT)  BHOUS(i)  
   # beta(i,0) - share of households in total demand for commodity i # ; 
   ! This is  beta:i0  (i=1,2) in (E3.2.4) of DPPW !  
 FORMULA   (all,i,SECT) BHOUS(i) = DVHOUS(i)/DVCOM(i) ;

 COEFFICIENT   (all,f,FAC)(all,j,SECT) BFAC(f,j)  
   # beta(f,j) - share of industry j in total demand for factor f #; 
   ! This is  beta:ij  (i=3,4; j=1,2) in (E3.2.5) of DPPW !  
 FORMULA   (all,f,FAC)(all,j,SECT) BFAC(f,j) = DVFACIN(f,j)/DVFAC(f) ;
!-------------------------------------------------------------------!
!  Equations (Linearized)                                           !
!-------------------------------------------------------------------!
EQUATION  Consumer_demands # Household expenditure functions [DPPW E3.2.1]# 
(all,i,SECT) p_XH(i) = p_Y - p_PC(i) ;

EQUATION  Intermediate_com # Intermediate demands [DPPW E3.2.2 i=1,2]#
! The term p_PC(j) is included because of (E3.2.3) in DPPW. !
(all,i,SECT)(all,j,SECT) p_XC(i,j) = p_XCOM(j) - (p_PC(i) - p_PC(j)) ;

EQUATION  Factor_inputs # Factor input demand functions [DPPW E3.2.2 i=3,4]#
! The term p_PC(j) is included because of (E3.2.3) in DPPW. !
(all,f,FAC)(all,j,SECT) p_XF(f,j) = p_XCOM(j) - (p_PF(f) - p_PC(j)) ;
EQUATION  Price_formation  # Unit cost index for industry j [DPPW E3.2.3]#
    (all,j,SECT) p_PC(j) = SUM(i,SECT,ALPHACOM(i,j)*p_PC(i)) +
                           SUM(f,FAC,ALPHAFAC(f,j)*p_PF(f)) ;

EQUATION Com_clear # Commodity market clearing [DPPW E3.2.4]#
   (all,i,SECT) p_XCOM(i) = BHOUS(i)*p_XH(i) + SUM(j,SECT,BCOM(i,j)*p_XC(i,j)); 
 
EQUATION Factor_use # Aggregate primary factor usage [E3.2.5 in DPPW]#
   (all,f,FAC) p_XFAC(f) = SUM(j,SECT,BFAC(f,j)*p_XF(f,j)) ; 
 
EQUATION NUMERAIRE # Numeraire is price of commodity 1 [DPPW E3.2.6]#
   (all,i,NUM_SECT)  p_PC(i) = 0; 
   ! Alternatively, this could be written as   p_PC( "s1" ) = 0 !
!-------------------------------------------------------------------!
!      Balance check for data base                                  !
!-------------------------------------------------------------------!
! In a balanced data base, total demand for commodity i, DVCOM(i) 
   should equal DVCOST(i), the total cost of inputs to industry i !
![[!
! To check that total demand = total costs to industry i
   remove the strong comment markers ![[! ... !]]! around  this section   !
COEFFICIENT (all,i,SECT) DVCOST(i) # Total cost of inputs to industry i# ;
 FORMULA   (all,i,SECT)
     DVCOST(i) = SUM(u,SECT,DVCOMIN(u,i)) + SUM(f,FAC,DVFACIN(f,i)) ;
  ! Check that the values  of DVCOM and DVCOST are equal !
  DISPLAY DVCOM ;
  DISPLAY DVCOST ; !]]! 
!---------end of TABLO Input file--------------------------------------!
4.4.2    Noteworthy features in the linearized TABLO input file
[gpd1.3.4.2]
1.  DEFAULT statements
Notice that there are no DEFAULT statements at the start of the linearized file in section
4.4.1
. This is because of the convention that all TABLO Input files are assumed to
begin with defaults appropriate for linearized TABLO Input files
11
, namely as if there were the following statements at the start.
VARIABLE (DEFAULT = LINEAR) ; 
EQUATION (DEFAULT = LINEAR) ; 
VARIABLE (DEFAULT = PERCENT_CHANGE) ; 
COEFFICIENT (DEFAULT = NON_PARAMETER) ; 
FORMULA (DEFAULT = ALWAYS) ;
The purpose of the last of these is discussed under the heading "FORMULAs" below.
2.  VARIABLEs
The linear variables are declared explicitly. We have chosen to use the same names as are declared
implicitly in the mixed TABLO Input file in section
4.3.3
above. (This makes results
from the 2 files easier to compare.) But we could have chosen different names.
The  (ORIG_LEVEL=...)  qualifiers tell the software what to take as the
pre-simulation values for the various levels variables.  For example,
VARIABLE  (ORIG_LEVEL=Y)  p_Y  # Total nominal household expenditure # ;
indicates that the pre-simulation levels value of the variable p_Y is Y.  Without this ORIG_LEVEL
qualifier, you would not see the pre-simulation, post-simulation and changes results in Table
3.3
above when you run a simulation.  Similarly
VARIABLE  (ORIG_LEVEL=1)  (all,i,SECT)  p_PC(i) # Price of commodities # ;
tells the software that it can take 1 as the pre-simulation levels values of the PC(i) for each
commodity i.  Starting with these prices equal to one explains why it is sensible to take the
pre-simulation values of the supplies XCOM(i) to be equal to the pre-simulation dollar values
DVCOM(i), as indicated in
VARIABLE  (ORIG_LEVEL=DVCOM)  (all,i,SECT)  p_XCOM(i) #...# ;
These ORIG_LEVEL qualifiers are not necessary in the mixed TABLO Input file SJ.TAB shown in
section
4.3.3
above since there the linear variable p_Y is derived automatically from
Y via the declaration of the levels variable Y, so the software knows the connection between Y and
p_Y. [See section
10.4
for documentation about the ORIG_LEVEL qualifier.]
3.  COEFFICIENTs
Many of the levels quantities which were declared as levels variables in the mixed TABLO Input file
in section
4.3.3
are declared here as COEFFICIENTs. (For example, the dollar values
DVHOUS and DVCOM. The first is READ from the data base and the second has its values assigned via a
FORMULA.)
It may help to think of these COEFFICIENTs as holding pre-simulation values of the levels
variables. However this is not entirely accurate in a multi-step simulation as we see below in the
discussion of FORMULAs and UPDATEs.
4.  FORMULAs
Most of the FORMULAs in the linearized file are re-evaluated at each step of a multi-step
simulation. This is what the qualifier (ALWAYS) denotes in the DEFAULT statement shown in (1.)
above.  After each step of a multi-step simulation, the data base is updated and all
FORMULA(ALWAYS)s are re-evaluated. For example, this ensures that DVCOM is always an accurate
reflection of the DVCOMIN and DVHOUS values on the currently updated data base. [A numerical
example is in section
4.4.7
.]
However some FORMULAs, those with qualifier (INITIAL), are only evaluated on the first step of a
multi-step simulation. FORMULAs giving the value of parameters (such as those for ALPHACOM and
ALPHAFAC) should only be applied initially (that is, at the first step) since the value of a
parameter should not be changed.
5.  UPDATEs
The purpose of an UPDATE statement is to tell the software how a COEFFICIENT (that is, a levels
variable) changes in response to the small changes in the linear VARIABLEs at each step of a
multi-step simulation.
For example, consider DVHOUS(i), the dollar value of household consumption of commodity i.
(a) Suppose there were an explicit linear VARIABLE, say p_DVHOUS(i), declared giving the percentage
change in DVHOUS(i). (In fact there is no such VARIABLE in the linearized TABLO Input file.) Then,
in response to a change in this, the new value of DVHOUS(i) should be given by
new_DVHOUS(i) = old_DVHOUS(i)*[1 + p_DVHOUS(i)/100]
(On any step, the old value is the value before the step and the new value is the one put on the
data base updated after the step.) We would need an UPDATE statement to indicate this. The
statement could be
UPDATE (all,i,SECT) DVHOUS(i) = p_DVHOUS(i) ; .
(b) In fact there is no linear VARIABLE declared in the linearized TABLO Input file giving the
percentage change in DVHOUS(i). However there are explicit linear VARIABLEs p_PC(i) and p_XH(i)
showing the percentage changes in the relevant price and quantity. If p_DVHOUS(i) were declared,
there would be a linear EQUATION connecting it to p_PC(i) and p_XH(i). This EQUATION would say that
p_DVHOUS(i) = p_PC(i) + p_XH(i)
Thus, the procedure for updating DVHOUS(i) is
new_DVHOUS(i) = old_DVHOUS(i)*[1 + {p_PC(i)+p_XH(i)}/100]
In fact the UPDATE statement is
UPDATE (all,i,SECT) DVHOUS(i) = p_PC(i) * p_XH(i) ;
This is interpreted by TABLO as having the correct effect (see section
4.4.6
for a
numerical example). At first you may be puzzled by the multiplication sign "*" here since the
percentage change in DVHOUS(i) is the SUM of p_PC(i) and p_XH(i).  However, this form of UPDATE is
called a PRODUCT UPDATE because it is used to update a COEFFICIENT (that is, a levels variable)
which is the product of 2 or more levels variables whose percentage changes are explicit linear
VARIABLEs. Here, in the levels,
DVHOUS(i) = PC(i) * XH(i)
and the "*" used in a PRODUCT UPDATE is to remind you of this levels
12
formula.
6.  Levels Prices and Quantities not Needed
Notice that no COEFFICIENTs have been declared to hold the levels values of prices or quantities.
[For example, there is no COEFFICIENT XH(i) even though there is a VARIABLE p_XH(i).]  This is a
fairly common feature of linearized TABLO Input files. In such files,
normally linear VARIABLEs are declared to show percentage changes (or changes) in prices and
quantities, but no explicit linear VARIABLEs are declared to show percentage changes in dollar
values.
COEFFICIENTs holding levels dollar values are declared but there are not normally COEFFICIENTs
holding levels prices or quantities.
7.  Names for Levels and Linearized VARIABLEs
As you have seen above, the levels variables required in a linearized TABLO Input file appear as
COEFFICIENTs while the percentage-change (or change) variables required appear as linear VARIABLEs.
It may happen that you need on the TABLO Input file a levels variable as a COEFFICIENT and its
percentage change (or change) as a VARIABLE. In this case, since TABLO Input files are not
case-sensitive, you cannot follow the convention of using upper case for the levels variables or
COEFFICIENTs (for example, XHOUS) and the same name partly or wholly in lower case for the
associated linear VARIABLEs (for example, xhous). The problem is most likely to occur for values,
which often occur both as COEFFICIENTs and VARIABLEs.
We suggest 3 alternative ways around this problem.
1: Follow a convention that value coefficients start with "V", while the associated percentage change
variable begins with "w".For example,
COEFFICIENT  VHOUTOT       VARIABLE  whoutot
2: Use the natural name for the COEFFICIENT version and attach 'p_' (for percentage change) or 'c_'
(for change) at the start for the VARIABLE. For example,
COEFFICIENT  XHOUS(i)      VARIABLE  p_XHOUS(i)
3: Use the natural name for the VARIABLE version and attach '_L' (for levels) to the
end for the COEFFICIENT. For example,
VARIABLE  xhous(i)         COEFFICIENT  XHOUS_L(i).
Although TABLO Input files are not case-sensitive (meaning that xhous and XHOUS are treated as
being the same), we find it makes linearized TABLO Input files more readable if we consistently put
linear VARIABLE names in lower case, or consistently put the first letter of all linear VARIABLE
names in lower case and the rest in upper case.
4.4.3    Analysing simulation results
[gpd1.3.4.3]
Now that you understand about TABLO Input files, you will want to begin
learning how to analyse simulation results, ie, to explain them using the
equations of the model (as in the TABLO Input file), and the base data.
In section
46.1
you can find a detailed hands-on analysis, using the
AnalyseGE program, of the 10 percent labor increase simulation with Stylized Johansen (based on the
linear TABLO Input file SJLN.TAB in section
4.4.1
above).
4.4.4    Writing UPDATE statements
[gpd1.3.4.4]
The purpose of an UPDATE statement is to tell how much some part of data read changes in response
to changes in the model's variables in the current step of a multi-step simulation. An introductory
example was given in section
4.4.2
above.
Consider a COEFFICIENT V whose value(s) are read. There are three possibilities for the UPDATE
statement for V.
1. If there is a linear VARIABLE, say w, in the TABLO Input file which represents the percentage
change in V, then use an UPDATE statement of the form
UPDATE V = w ;
2. If, in the levels, V is equal to the product of two or more percentage-change variables, say p and q, use
an UPDATE statement of the form
UPDATE V = p*q ;
This type of UPDATE statement is referred to as a PRODUCT UPDATE since it involves updating a
Levels variable which is a product of other Levels quantities (often a value V is, in levels, the product
of price P and quantity Q).
3. Otherwise work out an expression for the change in V in terms of linear VARIABLEs in the TABLO
Input file and use a CHANGE UPDATE statement of the form
UPDATE (CHANGE)  V = <expression for change in V> ;
Of these, the second case is by far the most common and probably will cover over 90% of your UPDATE
statements.
13
All three UPDATE statements in the linearized TABLO Input file for Stylized Johansen are of this
form (see section
4.4.1
above). Of course if
COEFFICIENT V has one or more arguments, the UPDATE statements also contain the appropriate
quantifiers, for example (all,i,SECT). Note also that only COEFFICIENTs whose values are READ or assigned via a
FORMULA(INITIAL) in the TABLO Input file should be UPDATEd.
In case 3 above, the expression for the change in V is obtained by linearizing the levels equation
connecting V to other levels variables whose associated linear variables have been declared in the
TABLO Input file. See section
11.12.7
for a worked example.
More details about Updates, including examples, can be found in section
11.12
.
4.4.5    Numerical versions of linearized equations
[gpd1.3.4.5]
In this section we look at numerical versions of the linearized equations in SJLN.TAB. In two
subsections below, we look at the numerical consequences of Update statements in SJLB.TAB (section
4.4.6
) and at how the values of the Coefficients and the numerical equations are
recalculated during each step of a multi-step calculation (section
4.4.7
).
Some users are keen to have detailed information about these topics; others are
not. Since a detailed knowledge about these topics is not
essential for doing effective modelling, you should
feel free to skip these
sections
. You can always refer back to them later on, if necessary.
Here we look at the numerical version of the linearized equation for market clearing of commodities
Com_clear. The equation is
Equation Com_clear   (all,i,SECT) 
   p_XCOM(i) = BHOUS(i)*p_XH(i) + SUM(j,SECT,BCOM(i,j)*p_XC(i,j)) ;
There are really 2 equations here, one for each sector ("s1", "s2").  The BHOUS and BCOM
Coefficients are shares. When evaluated at the base data values (see Table
3.1
above), they have the values
BHOUS("s1") = 2/8 = 0.25
BHOUS("s2") = 4/12 = 0.333333
BCOM("s1","s1") = 4/8   = 0.5
BCOM("s1","s2") = 2/8   = 0.25
BCOM("s2","s1") = 2/12 = 0.166667
BCOM("s2","s2") = 6/12 = 0.5
At the start of the simulation (ie, on the first Euler step — see section
3.12.3
above), the two equations are
p_XCOM("s1") = 0.25       * p_XH("s1") + 0.5           * p_XC("s1","s1") + 0.25 * p_XC("s1","s2")
p_XCOM("s2") = 0.333333* p_XH("s2") + 0.1666667* p_XC("s2","s1") + 0.5  *  p_XC("s2","s2")
This is why we call BHOUS and BCOM coefficients since their values are what are usually called the
coefficients in the above equations
14
. The unknowns p_XCOM("s1"), p_XH("s1"), p_XC("s1","s1") and p_XC("s1","s2") are the Variables in the

first of these equations.
When GEMPACK solves the equations above, all the variables are put onto one side so that the
equation says that some expression is equal to zero. The equations above are rewritten as
1.0*p_XCOM("s1") - 0.25*p_XH("s1") - 0.5*p_XC("s1","s1") - 0.25*p_XC("s1","s2") = 0
1.0*p_XCOM("s2") - 0.333333*p_XH("s2") - 0.1666667*p_XC("s2","s1") - 0.5*p_XC("s2","s2") = 0
If you look at Table
3.4
above which represents the Equations Matrix for the
linearized system, the equation Com_clear("s1") is one row of the Equations matrix. The
coefficients of variable p_XH("s1") give the column for p_XH("s1") in the Equations matrix so that
you can see that  the number -0.25 goes in the Com_clear("s1") row and the p_XH("s1") column [from
the second term in the first equation].
The number 1.0 goes in the Com_clear("s2") row and the p_XCOM("s2") column [the first term in the
second equation].
and similarly for the other terms in the equations.
4.4.6    Numerical examples of update statements
[gpd1.3.4.6]
Here we consider the 4-step Euler calculation with Stylized Johansen in which the supply of labor
is increased by 10 percent (and the supply of capital is fixed).
We look at the effect of the Update statements after the first step of this 4-step calculation.
During the first step, the supply of labor is only increased by 2.5 percent (one quarter of the
total shock). The software solves the linear equations (those in section
4.4.5
above)
to work out the consequential changes in the other quantities and prices. Some results from solving
these equations are as follows:
p_PC("s1") = 0
p_PC("s2") = -0.25
p_XH("s1") = 1.5
p_XH("s2") = 1.75
The Update statement for DVHOUS(i) is
UPDATE  (all,i,SECT)  DVHOUS(i) = p_PC(i) * p_XH(i) ;
which means (see point 5. in section
4.4.2
above) that
new_DVHOUS(i) = old_DVHOUS(i)*[1 + {p_PC(i)+p_XH(i)}/100] .
Hence the updated values for DVHOUS after the first step are
DVHOUS("s1") = 2*[1+{0+1.5}/100]        = 2*1.015 = 2.03
DVHOUS("s2") = 4*[1+{-0.25+1.75}/100] = 4*1.015 = 4.06
Similarly the other percentage changes in prices and quantities during this first step are used to
update the values of the other Coefficients DVCOMIN(i,j) and DVFACIN(f,j) which are read from the
data base.
15
4.4.7    How equations are recalculated in a multi-step calculation
[gpd1.3.4.7]
As we indicated in section
3.12.1
above, the values of the Coefficients may change
from step to step of a multi-step calculation.
Here we look at this for the second step of the 4-step Euler calculation discussed in section
4.4.6
above.
The values of all Coefficients read from the data base are updated at the end of the first step of
this calculation. During the second step, these Coefficients take these updated values.
The values taken during step 2 of all other Coefficients which are not Coefficient(Parameter)s are
inferred from the relevant Formulas.
16
For example, the DVCOM(i) values during step 2 are calculated by applying the TABLO Input file
FORMULA (all,i,SECT) DVCOM(i) = SUM(j,SECT, DVCOMIN(i,j)) + DVHOUS(i);
The updated values for DVHOUS (see section
4.4.6
above) and DVCOMIN are put into the
right-hand side of this Formula to give the values for DVHOUS(i) used during the second step.
Similarly for all other Coefficients.
Thus, for example, the values of the BHOUS(i) are recalculated during this second step. These
recalculated values are put into the relevant equations (namely the Com_clear equations).
Hence the numerical linear equations solved during step 2 may be different from those solved during
step 1.
In fact, for the Stylized Johansen model, the Coefficients BHOUS, BCOM and BFAC, which look as if
they may change from step to step, do not change.
17
This behaviour (which is not typical of GE models) is a consequence of the fact that all behaviour
in Stylized Johansen is Cobb-Douglas.
More details about the values used and calculated during the different steps of this 4-step
calculation can be found in section
25.2.2
.
4.5    Levels TABLO input files
[gpd1.3.5]
We illustrate the construction of TABLO Input files containing only levels equations by looking at
such a file for Stylized Johansen in section
4.5.1
. The main difference in general
from mixed TABLO Input files is in connection with behavioural equations (such as CES
specifications). You should expect the levels files to contain explicit calibration FORMULAs of the
kind familiar to levels modellers for calculating the values of the parameters of these functions.
A surprise with the Cobb-Douglas specification in Stylized Johansen is that, although such
parameters appear in the levels equations, we do not need to calculate their values since these
parameters do not appear in the linearized equations produced by TABLO. But this would not be the
case if Cobb-Douglas were replaced by CES.
4.5.1    Levels TABLO input file for Stylized Johansen
[gpd1.3.5.1]
The main difference from the mixed TABLO Input file shown in section
4.3.3
comes from
using the levels version of the behavioural equations (the first three blocks in Table
4.1
. These involve two parameters not present in the linearized versions of these
equations, namely
ALPHA
i0
parameters in the consumer demand equations
Q
j
parameters in the intermediate demand equations.
These are called ALPHAH(i) and Q(j) respectively in the levels TABLO Input file given later in this
section. As part of the calibration phase, you would expect to have to give FORMULAs for
calculating the values of these. For example, using the TABLO Input file notation,
ALPHAH(i) = PC(i)*XH(i)/Y = DVHOUS(i)/SUM(ii,SECT,DVHOUS(ii))
and it would also be possible to write down a formula for the Q(j). However, in GEMPACK, the levels
equations are only used as a means of writing down the linearized equations (TABLO does this by
symbolically differentiating the levels equations — see section
4.6
below). Once this
has been done, the levels equations are ignored. Thus, since the linearized versions of these
equations no longer involve these ALPHAH and Q parameters, it is not necessary to give FORMULAs for
them.
18
Of course, in a more complicated model, you may not be sure if similar parameters are going to
appear in the linearized system.  When in doubt, you can write down the TABLO Input file leaving
out calibration FORMULAs for such parameters and process the file by running TABLO. If the values
are needed in the linearized system, TABLO will tell you and not allow you to proceed until you
have supplied calibration FORMULAs.
Another noteworthy feature of the levels TABLO file shown below is in the EQUATION E_W for the
quantity called W(j) there. Variable W(j) has been introduced to simplify the "intermediate
demands" and "price formation" equations. The equation E_W uses the PROD operator to express W(j)
as the product of the relevant quantities.
19
The full levels TABLO Input file is shown below.
.!-------------------------------------------------------------------!
!                   Levels TABLO Input File for the                 !
!                      Stylized Johansen Model                      !
!                                                                   !
!      following the description in Chapter 3 of the text           !
!   "Notes and Problems in Applied General Equilibrium Economics"   !
!     by P.Dixon, B.Parmenter, A.Powell and P.Wilcoxen [DPPW]       !
!             published by North-Holland 1992                       !
!-------------------------------------------------------------------!

!   Text between exclamation marks is a comment                     !
!   Text between hashes (#) is labelling information                !

!-------------------------------------------------------------------!
!    Set defaults for Levels model                                  !
!-------------------------------------------------------------------!
EQUATION(DEFAULT=LEVELS) ;
VARIABLE(DEFAULT=LEVELS) ;
FORMULA(DEFAULT=INITIAL) ;
COEFFICIENT(DEFAULT=PARAMETER) ;

!-------------------------------------------------------------------!
!      Sets                                                         !
!-------------------------------------------------------------------!
! Index values i=1,2 in DPPW correspond to the sectors called s1,s2.
  Index values i=3,4 in DPPW correspond to the primary factors,
  labor and capital.   The set SECT below doubles as the set of 
  commodities  and the set of industries. !

SET SECT # Sectors # (s1-s2)  ;
SET FAC # Factors  # (labor, capital) ;

!-------------------------------------------------------------------!
!      Levels variables                                             !
!-------------------------------------------------------------------!
! In the DPPW names shown below, : denotes subscript.               !
! For example, x:j indicates that j is a subscript.                 !

Variable (GE 0)        Y    # Total nominal household expenditure # 
                            ! This is also Y in DPPW ! ;

Variable (GE 0) (all,i,SECT)  PC(i)   # Price of commodity i #
                               ! This is p:i (i=1,2) in DPPW ! ;
Variable (GE 0) (all,f,FAC)   PF(f)   # Price of factor f #
                               ! This is p:i (i=3,4) in DPPW ! ;
Variable (GE 0) (all,i,SECT)  XCOM(i) 
    # Total demand for (or supply of) commodity i #
                               ! This is x:i (i=1,2) in DPPW ! ;
Variable (GE 0) (all,f,FAC)   XFAC(f) 
    # Total demand for (or supply of) factor f    #
                               ! This is x:i (i=3,4) in DPPW ! ;

Variable (GE 0) (all,i,SECT)  XH(i)   # Household demand for commodity i #
                               ! This is x:i0 (i=1,2) in DPPW ! ;
Variable (GE 0) (all,i,SECT) (all,j,SECT)     XC(i,j) 
    # Intermediate inputs of commodity i to industry j #
    ! This is x:ij (i,j=1,2) in DPPW ! ;
Variable (GE 0) (all,f,FAC)(all,j,SECT)       XF(f,j) 
    # Factor inputs to industry j #
    ! This is x:ij (i=3,4; j=1,2) in DPPW ! ;
Variable (all,j,SECT)  W(j)    #Price expression#;

!-------------------------------------------------------------------!
!     Dollar values read in from database                           !
!-------------------------------------------------------------------!
Variable (GE 0) (all,i,SECT)(all,j,SECT)      DVCOMIN(i,j) 
    # Dollar value of inputs of commodity i to industry j # ;
Variable (GE 0) (all,f,FAC)(all,j,SECT)       DVFACIN(f,j)
    # Dollar value of factor f used in industry j # ;
Variable (GE 0) (all,i,SECT)                  DVHOUS(i) 
    # Dollar value of household use of commodity i # ;

!-------------------------------------------------------------------!
!     Parameters                                                    !
!-------------------------------------------------------------------!
COEFFICIENT (all,i,SECT)   ALPHAH(i)     #Household parameter#;
COEFFICIENT
 (all,i,SECT) (all,j,SECT) ALPHACOM(i,j) #Commodity parameter#;
COEFFICIENT
 (all,f,FAC) (all,j,SECT)  ALPHAFAC(f,j) #Factor parameter#;
COEFFICIENT (all,j,SECT)   Q(j)          #Scale parameter#;

!-------------------------------------------------------------------!
!      File                                                         !
!-------------------------------------------------------------------!
FILE iodata # input-output data for the model # ;

!-------------------------------------------------------------------!
!      Reads from the data base                                     !
!-------------------------------------------------------------------!
READ DVCOMIN from FILE iodata HEADER "CINP" ;
READ DVFACIN from FILE iodata HEADER "FINP" ;
READ DVHOUS  from FILE iodata HEADER "HCON" ;

!-------------------------------------------------------------------!
!     Formulas to calculate the Initial solution                    !
!-------------------------------------------------------------------!
! FORMULAs for Y, ALPHAH(i) and Q(j) are only needed if require
   change differentiation or add the Newton correction terms. !

!   1. Formulas for initial prices   !
!....................................!

FORMULA (all,i,SECT) PC(i) = 1 ;
FORMULA (all,f,FAC)  PF(f) = 1 ;
FORMULA (all,j,SECT) W(j) = 1 ;
FORMULA (all,j,SECT) Q(j) = 1 ;

.!   2. Formulas which are also equations   !
!..........................................!

FORMULA & EQUATION Comin 
# Intermediate input of commodity i in industry j #
 (all,i,SECT)(all,j,SECT)
 XC(i,j) = DVCOMIN(i,j) / PC(i) ;
! Quantity   = Dollar value / price !

FORMULA & EQUATION Facin # Factor input f in industry j #
 (all,f,FAC)(all,j,SECT)
 XF(f,j) = DVFACIN(f,j)/PF(f) ;

FORMULA & EQUATION House # Household demand for Commodity i #
 (all,i,SECT)
 XH(i) = DVHOUS(i)/PC(i) ;

FORMULA & EQUATION Com_clear #Commodity market clearing #
! (E3.1.6) in DPPW !
(all,i,SECT)   XCOM(i) = XH(i) + SUM(j,SECT, XC(i,j)) ;

FORMULA & EQUATION Factor_use # Aggregate primary factor usage #
! (E3.1.7) in DPPW ! 
(all,f,FAC)   XFAC(f) = SUM(j,SECT, XF(f,j)) ;

!  3. Formula for initial value of Y !
!....................................!
FORMULA Y = SUM(i,SECT,PC(i)*XH(i)) ;

!  4. Formulas for the parameters   !
!...................................!

FORMULA (all,i,SECT)(all,j,SECT)
 ALPHACOM(i,j) = XC(i,j)/XCOM(j) ;

FORMULA (all,f,FAC)(all,j,SECT)
 ALPHAFAC(f,j) = XF(f,j)/XCOM(j) ;

FORMULA (all,i,SECT)
 ALPHAH(i) = PC(i)*XH(i)/Y ;

!-------------------------------------------------------------!
!  Levels Equations    (Numbers refer to DPPW)                !
!-------------------------------------------------------------!
EQUATION Consumer_demands #Household expenditure functions #
! (E3.1.9) in DPPW ! 
 (all,i,SECT)  XH(i) = ALPHAH(i)*Y/PC(i)  ;

EQUATION Intermediate_com
 # Intermediate demand for commodity i by industry j # 
! (E3.1.10) in DPPW !
 (all,i,SECT) (all,j,SECT)
 XC(i,j) = ALPHACOM(i,j)*Q(j)*XCOM(j)*W(j)/PC(i) ;

EQUATION E_W # Define W(j) to simplify other equations #
 (all,j,SECT)
 W(j) = PROD(t,SECT,PC(t)^ALPHACOM(t,j)) *
                      PROD(u,FAC,PF(u)^ALPHAFAC(u,j)) ;

EQUATION Factor_inputs  # Factor input demand functions #
                                      !(E3.1.10) in DPPW ! 
 (all,f,FAC) (all,j,SECT)
 XF(f,j) = ALPHAFAC(f,j)*Q(j)*XCOM(j)*W(j)/PF(f) ;

EQUATION Price_formation # Unit cost index for industry j #
 (all,j,SECT)   PC(j) = Q(j)*W(j) ; ! (E3.1.12) in DPPW !

EQUATION Numeraire
 # Numeraire for the model is price of commodity 1 (E3.1.23)#
 PC("s1") = 1 ;              
!-------------end of TABLO Input file-------------------------!
4.6    TABLO linearizes levels equations automatically
[gpd1.3.7]
When TABLO processes a TAB file containing levels EQUATIONs and VARIABLEs,
it converts the file to a linearized file (we call it the associated linearized TABLO Input file).
You can see the linearized equations on the INF file and evaluate them in
AnalyseGE (see section
18.3
).
The most important feature of this conversion is that, for each levels VARIABLE, say X, in your
original TABLO Input file, there is an associated linear VARIABLE whose name is that of the
original levels variable with "p_" added at the start.
20
Also, for each levels VARIABLE in the original TABLO Input file, a COEFFICIENT with the same name
as the levels VARIABLE is declared in the associated linearized TABLO Input file.
It is important to realise that the rest of TABLO (the last part of the CHECK and all of the
CONDENSE and CODE stages) proceeds
as if the associated linearized TABLO Input file were the actual TABLO Input file.
This means that warnings and error messages given by TABLO may refer to statements in this
associated linearized file rather than in your original TABLO Input file.
21
Other features of this conversion are explained in section
9.2
.
4.7    Creating the TABLO input file and command files for your own model
[gpd1.3.9]
When you want to build your own model, you will usually construct the TABLO Input file by modifying
one from an existing model. For example, you may wish to add some equations to an existing model.
Alternatively, you can create a TABLO Input file for your model from scratch. Suggestions about
this can be found in section
8.3
.
Whenever you are building or modifying a TABLO Input file, you will probably want to use the
TABmate editor (see section
36.4
) if you are working on a PC. TABmate assists
you to identify and remove syntax or semantic errors from your TABLO Input file, as the examples in
section
4.7.1
below show.
You will also need to write Command files for simulations. In section
4.7.2
below, we
show you how you can identify and correct errors in Command files.
4.7.1    Correcting errors in TABLO input files
[gpd1.3.9.1]
In the example below, we show you how to fix all errors in the TABLO Input file  sjerror.tab  which
is supplied with the GEMPACK Examples.
TABmate can be a great help in finding errors. The example below shows you how to use TABmate to
correct a TABLO Input file SJERROR.TAB which contains some typical errors.
Check how your WinGEM is configured by selecting
Options | Editor for TABLO Check Errors
and then slide your mouse across to click on Use TABmate.
Set your working directory to the subdirectory \SJ as described in section
3.4.2
.
Now open a TABLO window via
Simulation | TABLO Implement...
and then, in this window,
Select  the TABLO Input file SJERROR.TAB.  Click on
Run
to run TABLO.  This run will find
errors and so you should see a new window titled
Error running TABLO
In this window, click
on
Edit TABLO file
.
This will cause TABmate display SJERROR.TAB.
Indeed, TABmate will show you the first error, which occurs at the beginning of the
declaration of variable XCOM. You should see a wriggly red line under the word VARIABLE at the
start of this line (line number 55 of the file). To see the reason for this error, click on the
word VARIABLE which is underlined in red. You will see the reason
Expected  ;
shown (also in red) in the Error status panel in the bottom right-hand half of the TABmate's bottom
panel. [After a few seconds the reason will go away, but you can get it back by clicking on the bottom panel or on the
red-underlined word.]
You can see that a semi-colon is missing from the end of the previous line (the end of the
declaration of variable PF). To remedy this error, insert a semi-colon at the end of that line.
TABmate does not immediately realise that you have fixed this error. However you can ask TABmate to
check the file by clicking on the  TABLO Check button near the middle of the top part of TABmate.
When you click on this Check button, TABmate first saves the TAB file and then runs TABLO to check
the file.
This time it gets past the previous error but finds another error, underlining the word  FACT  in
red and giving  Unknown set  as the reason for this error. A moment's reflection will tell you that
the name of this set is just  FAC  (not FACT), so correct this error by removing the final "T".
Then click on  TABLO Check  button again. This time TABmate tells you  No error found  (in
"go-ahead" green rather than "stop" red).
Now that you have removed all errors, you can return to WinGEM to continue. To do this, close
TABmate (for example, by selecting
File | Exit
from the main TABmate menu). You will see
WinGEM's  Error running TABLO window. In this window, click on  Rerun. Then WinGEM will rerun
TABLO. This time there should be no errors and TABLO will produce either a TABLO-generated program
or else output for GEMSIM as usual.
This illustrates the procedure for removing errors from TABLO Input files.
Run TABLO
Use TABmate (and its TABLO Check button) to remove all errors, then close TABmate.
Click on the Rerun button to rerun TABLO under WinGEM to produce a TABLO-generated program or
output for GEMSIM.
TABLO Check: Behind the scenes
To understand what TABmate is doing when you click "TABLO Check", you could open
a command prompt and type:
tablo -pgs sjerror
TABLO will check the file and report 1 syntax error and 10 semantic errors.
To identify the errors, view the Information file  sjerror.inf:
tabmate sjerror.inf
Search for  %% (two % signs with no space between them). At the first occurrence you should see
something like:
51   VARIABLE (all,i,SECT)  PC(i)   # Price of commodity i #
     52                                  ! This is p:i (i=1,2) in DPPW ! ;
     53   VARIABLE (all,f,FAC)   PF(f)   # Price of factor f #
     54                                  ! This is p:i (i=3,4) in DPPW !
     55   VARIABLE (all,i,SECT)  XCOM(i)
          ?
 %% Syntax error.
 Expected ;.
     56       # Total demand for (or supply of) commodity i #
     57                                  ! This is x:i (i=1,2) in DPPW ! ;
Note the  ?  which points to the first letter of VARIABLE in the declaration of XCOM. The reason
"Expected ;." is shown. You can see that a semi-colon has been left out at the end of the previous
declaration, namely the declaration of VARIABLE PF. To fix the error, you would need to add a semi-colon at
the end of this statement in  sjerror.tab. [There is no point in making any changes to the
Information file sjerror.inf.]
Search again in sjerror.inf for %%. The next error shows something like:
87   COEFFICIENT (all,f,FACT)(all,j,SECT)   ALPHAFAC(f,j)
                             ?
 %% Semantic problem.
 Unknown set.
     88    # Share of factor input f in costs of industry j # ;
Here the  ?  is pointing to the name FACT. The reason is "Unknown set". A moment's reflection will
tell you that the name of this set is just  FAC  (not FACT). Again this needs to be corrected in
sjerror.tab.
Search again in sjerror.inf for %%. The next error shows something like:
109   FORMULA (all,i,FAC) PF(i) = 1.0 ;
                              ?
 %% Semantic problem.
 Unknown coefficient or variable.
The  ?  points to "PF" and the reason is "Unknown coefficient or variable". PF is unknown because
of the first error above (where the semi-colon being omitted means that TABLO did not understand
the statement declaring variable PF). We call this a consequential error since it is only an error
because of an earlier error.
It turns out that all the other errors are consequential errors.
When you click "TABLO Check", TABmate
runs TABLO to check the TAB file, and make an INF file.
scans the INF file to locate errors (and associated messsages).
underlines the errors in the TAB file.
Occasionally TABmate cannot tell (from the INF file) where the error is located.
In that case, the "INF See" button, lets you see the INF file yourself. Then you can use the
"X Next" button to search for %% errors.
4.7.2    Correcting errors in command files
[gpd1.3.9.2]
GEMSIM or the TABLO-generated program processes the Command file very early, checking that the
statements are as expected. We refer to errors identified at this stage as syntax errors in the
Command file. If you have a syntax error in the Command file (for example, do not spell one of the
keywords correctly), the program stops with an error as soon as the whole Command file is processed
in this way. When you have a syntax error in your Command file, the error will be marked in the Log
file by %% to indicate where the error occurs. If you look in the Log file from the simulation,
search for %% to find the error and the message indicating what the error is. Example 1 below is an
example of a syntax error.
If there are no syntax errors, the program begins the simulation. Other errors in the Command file
can be indicated later during the simulation. For example, you may not have a valid closure, or you
may read shocks from a text file which does not have the expected form. In these cases, the error
message may not refer explicitly to the Command file. Look at the Log file to identify the error.
The error is usually indicated near the end of the Log file and is usually (but not always) marked
with %%. You will need to read the error message and interpret it. Example 2 below is an example of
this kind.
Example 1 - Syntax Error
Run GEMSIM or the TABLO-generated program for Stylized Johansen and take inputs from the Command
file  sjlberr1.cmf  (which is supplied with the GEMPACK Examples).
The run should end with an error. To find the error, edit the Log file in your text editor and
search for  %%.
22
You should see something like the following in the Log file:
! Solution method information
 ! Closure

 exogenous p_xfac ;
 rest endogenous ;

 ! Solution method information

 method = euler ;
 ! (Syntax error in next line)
 stps = 1 2 4 ;
  %% Unknown keyword 'stps'

 ! Simulation part

 ! Name of Solution file is inferred from name of Command file.
 ! (See section
20.5
)

 shock p_xfac("labor") = 10 ;

 verbal description =
 Stylized Johansen model. Standard data and closure.
 10 per cent increase in amount of labor.
   (Capital remains unchanged.);

 ! Options
 extrapolation accuracy file = yes ;
 log file = yes ;

 ! End of Command file
  (Finished reading the command file.)

  There is at least one error in your Command file.

 (To see the error(s), look at the LOG file 'gpx60.log'.)
 (Search for %% in this LOG file.)

   (ERROR RETURN FROM ROUTINE: TGRCMF)
   (E-Error in command file input)
   (ERROR RETURN FROM ROUTINE: GEMSIM)
  (The program terminated with an error.)
You can see that the syntax error is the incorrect spelling of "steps".
To fix the problem, edit the Command file to fix this error and rerun the simulation.
If there are several syntax errors in the Command file, they will all be marked.
Example 2 - Error Discovered Later in the Run
Run GEMSIM or the TABLO-generated program for Stylized Johansen and take inputs from the Command
file  sjlberr2.cmf  (which is supplied with the GEMPACK Examples).
The run should end with an error. To find the error, edit the Log file in your text editor and
search for %%. You should see something like the following.
--->  Beginning pass number 1 of 1-pass calculation.

  CHOICE OF ECONOMIC ENVIRONMENT

  (All components of 'p_XFAC' chosen to be exogenous.)
 %% Not all variables have been specified exogenous or endogenous.
  
   (ERROR RETURN FROM ROUTINE: ENINCF)
   (E-not all variables specified exogenous or endogenous)
   (ERROR RETURN FROM ROUTINE: ENINI )
   (ERROR RETURN FROM ROUTINE: TGEN  )
   (ERROR RETURN FROM ROUTINE: GEMSIM)
 (Incomplete new BCV file has been deleted.)
  
 Inputs have been taken from the Command file
 C:\SJ\sjlberr2.cmf
  
  (The program terminated with an error.)
The error in the example above is because the statement
."rest endogenous ;" has been commented out. To fix it remove the exclamation mark at the start of
the line.
In general, once you have identified the source of the error, edit the Command file to fix this
error and rerun the simulation.
Following the error, there is a trace-back string of subroutines. This trace-back string is
probably of no use to you but can be helpful to the GEMPACK developers when tracing bugs in the
GEMPACK code. If you need help with an error, it will be helpful if you save the Log file and send
it to us when you report the problem.
5    Header Array files
[harfiles]
Click here
for detailed chapter contents
This chapter contains an introduction to Header Array files and to the
programs which can be used to create or modify them  (section
5.1
).
Data for GEMPACK models (for example, input-output tables or parameters such as elasticities) are
normally stored on files called Header Array (or HAR) files. Header Array files contain one or
more arrays each containing data values. An individual array of data on a HAR file is
accessed by supplying the unique 4-character identifier (or Header) for that array of values.
In addition to its header, each array of data has an associated
long name
(up to
70 characters long) which can contain a description of the data in the array.
Each array can have set and element labelling (which indicates, for example, the names of the
commodities associated with each number) — see section
5.0.3
for details.
Header Array files are binary files that cannot be viewed or edited using
normal text editors. The data is encoded in binary form
to keep the size of the file small. You need to use a special program,
such as ViewHAR, to examine or modify such files.
Header Array files are binary files so they cannot be printed or edited directly. Because of this,
GEMPACK provides a number of utility programs for accessing them. These include
ViewHAR
For viewing or modifying a HAR file
SEEHAR
For translating HAR files to various text formats
MODHAR
For modifying the data on a HAR file in batch or under Linux
ViewHAR has been introduced in chapter
3
above — further details
can be found   below. For
SEEHAR, see chapter
37
; for MODHAR, chapter
54
.
5.0.1    Data on Header Array files
[gpd4.3.1]
The data values held on an individual array can be either all real numbers, all integer numbers or
all character strings. Depending on the type of data that is to be stored, the number of dimensions
allowed varies.
The dimension limits for Header Arrays are :
For real numbers - up to and including 7 dimensions
For integer numbers - up to and including 2 dimensions
For character strings - only 1-dimensional arrays are allowed
Headers for arrays on any one file must be unique since the header acts as a label or primary key
to identify the associated array.
Once written, an array contains not just the data for the array itself but also self-describing
data, including the type of data values, dimensions of the array and a descriptive
"long
name"
of up to 70 characters.
Header Array files have the advantage that you can access any array just by referring to the header
which uniquely identifies the array in the file. There is no need to consider here the format
1
of the arrays or any other details since they are all taken care of automatically by the software.
Headers consist of up to four characters which are usually letters (A to Z, a to z) or digits (0 to
9). Different arrays must have different headers. The case (upper or lower) of a header is not
significant. (For example, you cannot have one array with header 'ABCD' and another on the same
file with header 'AbCd'.). Headers starting with letters 'XX' are reserved for internal program use.
5.0.2    Array type
[gpd4.3.1.1]
Each array on a Header Array file has an associated type. The type of each array is shown when
ViewHAR lists the contents of a Header Array file.
Arrays of integers have type
2I
,  arrays of character strings have type
1C
.  Arrays
of reals can have any of the types
RE
,
2R
or
RL
2
.  The RE type includes

set and element labelling (row and column labels) — see section
5.0.3
.
5.0.3    Set and element labelling on header array files
[gpd4.5a]
Arrays of real numbers on Header Array files usually contain set and element labelling information.
This set and element labelling consists of
the name of the coefficient associated with the array,
the names of the sets over which the arguments of the array range, and
the elements of these sets involved with the array.
The set elements appear as row and column labels in the ViewHAR display.
TABLO-generated programs and GEMSIM automatically write this information to any arrays they write
to a Header Array file. The information is also shown in various forms of
SEEHAR and SLTOHT output.
Below is an example of labelled CSV output from SEEHAR (using the SES option; see section
37.1
) showing the
element names for the rows and columns. Such a CSV file could be read by Excel, Matlab or other programs.
Table 5.1 Example of labelled CSV output from SEEHAR
Coefficient DVFACIN(FAC:SECT)
 DVFACIN(FAC:SECT),s1        ,     s2    ,
 labor       ,  1.0000000    ,  3.0000000,
 capital     ,  1.0000000    ,  1.0000000,
We refer to this labelling information as
set and element information
on an array.
Set and element labelling information can only be attached to arrays of real numbers — not to
arrays of integers or character strings.
5.0.4    Long names
[gpd4.3.1.2]
Each header has an associated Long Name which can be up to 70 characters long.
You can see these on the ViewHAR Contents page
3
.
When TABLO-generated programs and GEMSIM read and write header arrays, they may
create new long names or transfer the long name from when the data was read
(see section
11.11.7
). Updated data files usually have the same
long names as initial data  (see section
22.2.4
).
5.0.5    File history and creation information
[gpd9.7.5.3]
When a GEMPACK program creates a Header Array file, it adds  Creation Information to it, such as:
the time and date on which the file was created; the program which created the file; and the
GEMPACK Release from which the program EXE was built. See section
49.1
for more details.
A Header Array file can also contain what we call History Information (or simply History). This
History consists of several lines of text (each line is limited to 60 characters) which are stored
on the file. You can  see (or edit) this History if you open the file in ViewHAR and click on the
History menu item. You could make notes there about your file edits.
The top part of the History form shows the file Creation Information.
The idea is that Creation Information and History help to remind you how, when and why you created
the file. If you send the file to someone else, it could tell that person useful information.
When you carry out a simulation, the updated versions of any Header Array data files have History
written on them, as does the Solution file.
5.1    Ways to create or modify header array files
[gpd4.3.2]
5.1.1    Creating an initial HAR file of raw data
[gpd4.3.2a]
The usual way to create header array files containing
raw data
is via ViewHAR. A blank
(zero-filled) array is created in ViewHAR; then numbers from a spreadsheet are pasted into the
array. ViewHAR can also modify single numbers (right-click on the value). These procedures are
described briefly in section
6.1
below, and more fully in ViewHAR's Help. Some
of the possibilities are illustrated in figure
5.1
below.
Figure 5.1 Ways to create an initial HAR file of raw data
On a non-Windows operating system,  the (rather old-fashioned) program MODHAR can be used
to turn raw text data into a HAR file — as described in Chapter
54
.
5.1.2    Processing raw data to create a HAR file that model can use
[gpd4.3.2b]
Usually the raw data requires considerable processing or manipulation before it can be used by a
CGE model. The best way to do this processing is via one or more
data-manipulation
TABLO
programs. These TAB files contain COEFFICIENT, READ, FORMULA, and WRITE statements (but do not
contain VARIABLE or EQUATION statements).
Figure
5.2
below shows a possible procedure. RAWDATA.HAR is created interactively in
ViewHAR, by copying raw data from a spreadsheet. Then the sequence of programs, STEP1.TAB,
STEP2.TAB and STEP3.TAB are used to turn the raw data into MODEL.HAR — which is formatted and
arranged to be used by the actual CGE model (in MODEL.TAB). If the raw data was changed or
updated, you would edit RAWDATA.HAR interactively in ViewHAR, then rerun the three programs STEP1
to STEP3.
Figure 5.2 Steps in processing raw data
Clearly it would be risky or foolish to use ViewHAR to manually edit any of the files
STEP1.HAR, STEP2.HAR or MODEL.HAR — any changes would be overwritten the next time
you re-ran programs STEP1 to STEP3.
Using TABLO programs (rather than Excel) to process data offers three critical advantages:
Most Excel programs work only with fixed dimensions for data arrays. That can be be a problem if
you decide to, say, increase the number of sectors. By contrast, TABLO programs can be written to
work with varying data dimensions.
The TAB files provide a record of the operations that have been performed. By contrast, Excel
operations leave no audit trail.
If input data changes, it is easy to repeat processing by rerunning the TABLO programs. By
contrast, it might be difficult or impossible to precisely repeat a complex sequence of Excel
operations.
See section
38.3
for more about data-manipulation TABLO programs.
6    Constructing HAR files
[gpd1.4]
Click here
for detailed chapter contents
When you prepare the TABLO Input file for a model, you work out how much data is required (see
section
4.2
above) and what it must represent. Then comes the (often difficult and
time-consuming) task of assembling the actual data (numbers); we say nothing about this here.  Once
that has been done, you must create files containing these numbers which can be read by the GEMPACK
programs. These files are usually GEMPACK Header Array files
1
.
Header Array files are binary files which contain one or more arrays containing data values. An
individual array of data on a Header Array file is accessed by referring to the unique 4-character
identifier known as a Header for that array of values. See chapter
5
for
more details.
ViewHAR makes it fairly easy for you to create, view, or modify these files
The use of ViewHAR to create Header Array files, and to modify data on them,
is introduced in sections
6.1
and
6.2
below
2
.
The usual way of creating a Header Array data file is to start with data from
another program or source in XLS or some text format.
For XLS source, blank arrays of the correct size are created in ViewHAR — then
the numbers are pasted from Excel into these arrays. We illustrate this for
Stylized Johansen in section
6.1
below.
Text source can often be edited into a form that ViewHAR can read directly --
the so-called GEMPACK text file format. Otherwise, it may be possible to read
it into a spreadsheet to create XLS source.
Section
6.2
below contains examples which show how ViewHAR can be used to modify data
on Header Array files.
When you construct a data base for a model, it is important to check that it is balanced. We give
some examples in section
6.3
below.
GEMSIM and TABLO-generated programs can be used to write Header Array or text data files. We give a
hands-on example and some details in section
38.3
below.
We provide a table in section
6.4
which summarises the different programs you can use
to convert data files of one type (for example, a text data file) to another type (for example, a
Header Array file).
There are many techniques used in preparing and modifying data. In this chapter we only scratch the
surface. We recommend sources of further information in section
6.5
.
6.1    Constructing the header array data file for Stylized Johansen
[sjmkdat]
You have looked at the Header Array data file SJ.HAR for Stylized Johansen in section
3.4.3
above. In this section we take you through the steps to
construct that file SJ.HAR. We recommend that you carry out these steps on your own computer.
As you have seen in section
4.2.1
above, we need three arrays of data for DVCOMIN,
DVFACIN and DVHOUS; these are of size 2 x 2, 2 x 2 and 2 respectively. The matrices of data
required are as shown in the data base in Table
3.1
of section
3.1.1
.
We assume that you have data in an Excel sheet (SJDAT.XLS in the examples folder), as shown in the table below.
Table 6.1 Excel sheet of data for SJ model
Coefficient:
DVCOMIN
Header:
CINP
Dimensions:
SECT*SECT
Description:
Use of commodities by industries
s1
s2
s1
4
2
s2
2
6
Coefficient:
DVFACIN
Header:
FINP
Dimensions:
FAC*SECT
Description:
Inputs of primary factors
s1
s2
labor
1
3
capital
1
1
Coefficient:
DVHOUS
Header:
HCON
Dimensions:
SECT
Description:
Household use of commodities
s1
2
s2
4
Step 1 — Create a new HAR file in ViewHAR
Open ViewHAR and open the file SJDAT.XLS in Excel (or similar program).
In ViewHAR there are two modes: the simplest is
Read Only
mode where you
can look at a Header Array file and are not allowed to change it. To get to
this mode, select from the File menu
Use simplified, read-only menu
.
The second mode is
Editing
mode where you are allowed to modify data in
the Header Array file. To get to this mode, select from the File menu
Use
advanced, editing menu
. You must be in Editing mode to carry out the
operations described below.
From the File menu, select
Create New File
.
Step 2 — Create the needed sets
We can see from the Excel file that sizes of needed data arrays are given by the 2
sets SECT and FAC. The first step is to create ViewHAR headers for these 2 sets.
Use the command
Sets | Create New Set
to open the Create Set dialog for
the set SECT. Type in
the set name:
SECT
the set size:
2
the description:
Sectors
the header:
SEC
the elements:
S1 S2
(one per line)
Press the Check button to see if the data satisfies GEMPACK's rules.
Press
OK
when you are done. You should see that the file now contains 1 header, "SEC".
Similarly use the Create Set dialog to make a header for the set FAC. Type in
the set name:
FAC
the set size:
2
the description:
Primary factors
the header:
FAC
the elements:
Labour  Capital
(one per line)
For larger sets, it is easier to copy/paste the elements from Excel.
Now use
File | Save as
to save
All
headers in
HAR
format  with the name MySJ.HAR.
Step 3 — Create the needed blank arrays
We can see from the Excel file that the needed data arrays are:
DVCOMIN, dimensions SECT*SECT
Â 
DVFACIN, dimensions FAC*SECT, and
Â 
DVHOUS, dimension SECT
First use the
Edit | Create new header
command to make DVCOMIN. Fill in or choose
the following options:
the Header type:
Real
the header:
CINP
default value:
0
the Coefficient name:
DVCOMIN
the description:
Use of commodities by industries
the no. of dimensions:
2
Choose Sets:
SECT
in both drop down lists.
Press
OK
when you are done. You should see that the file now contains a new
header, CINP. Examine the values of this header — they will be all zero, but at least
you have an array of the right size with the right labels.
Leave this array (of zeros) in view in ViewHAR. Then, in Excel, select the 2x2 array of values
3
for DVCOMIN,
and
Copy
them to the clipboard.
Now go back to ViewHAR (still with the blank DVCOMIN array visible) and choose
Import | Paste to screen from Clipboard
. You should see the right numbers appear.
Now use
File | Save
to save your work
4
so far.
Similarly, create and populate the DVFACIN and DVHOUS arrays.
Use
Edit | Create new header
to make DVFACIN by filling in or choosing:
the Header type:
Real
; the header:
FINP
; the
default value:
0
; the Coefficient name:
DVFACIN
;
the description:
Inputs of primary factors
; and
the no. of dimensions:
2
. For
Choose Sets: select
FAC
in the first drop down list, and
SECT
in the second.
Press
OK
when you are done.
Examine the values of the new FINP header — they will again be all zero. Then,
in Excel, select the 2x2 array of values for DVFACIN, and
Copy
them to
the clipboard. Then back in ViewHAR use
Import | Paste to screen from Clipboard
to bring the numbers into ViewHAR. And again
File | Save
.
For DVHOUS, similarly
Edit | Create new header
choose or fill in
the Header type:
Real
; the header:
HCON
; the
default value:
0
; the Coefficient name:
DVHOUS
;
the description:
Household use of commodities
; and
the no. of dimensions:
1
. For
Choose Sets: select
SECT
in the drop down list.
Press
OK
and view the new header HCON.
Then,
in Excel, select the 2  values for DVHOUS, and
Copy
them to
the clipboard. Then back in ViewHAR use
Import | Paste to screen from Clipboard
to bring the numbers into ViewHAR. And yet again
File | Save
.
The task is complete !
6.1.0.1    Another way to attach set and element labelling information
[sjmkdat2]
In the example above, we first created the sets, then used these to create
blank labelled arrays. A more old-fashioned (but sometimes still useful) way is
to first create blank
un-labelled
arrays, then create the sets, then
attach sets to the arrays as row or column labels. You can do the latter with
the menu item
Edit | Apply/Change Set Labels
. Use the Choose Dimension
box in the bottom left-hand corner to select the first dimension. Then, with
Choose Set drop-down list on the right-hand part of the form, select the right
set. Then use the Choose Dimension box to select the second dimension, and the
Choose Set drop-down list to select the right set for that. And so on, until
all dimensions are labelled.
6.2    Editing the header array data file for Stylized Johansen
[sjmoddat]
You can modify a number in ViewHAR by right-clicking that number (in the Data window)
and typing in a new value.
To modify a whole array, it's usually easier to
Use the command
Export | Copy Screen to Clipboard
Paste the array (with labels and totals) into a blank Excel sheet. Then modify
the numbers as you wish. Make sure that plenty of decimal places are visible.
Back in ViewHAR use
Import | Paste to screen from Clipboard
. You should
see the new numbers appear.
Whether pasting numbers from Excel to ViewHAR, or from ViewHAR to Excel,
you only get the number of decimal places that is visible in the source
. Usually you need
to increase the number of visible decimal places before you copy.
6.2.1    Other ViewHAR capabilities
[gpd1.4.5.8]
ViewHAR offers many other capabilities. You can find more information in section
36.2
,
and complete details in the Help file supplied with ViewHAR.
6.3    Checking data is balanced
[gpd1.4.7]
When you prepare the data file(s) for a model, you must be careful to check that all the different
balancing conditions are satisfied.
For example, for Stylized Johansen, costs in each industry must equal the total
demand for the corresponding commodity. In ORANI-G, which allows each industry
to produce several commodities, there are two balancing conditions: costs in
each industry must equal the value of all outputs from that industry; and
output of each commodity (from several industries) must equal the total demand
for that commodity.
The TAB file for a well-constructed model will contain code to check that such
balance conditions hold, and even assertions (see section
25.3
)
that will stop the model running if they do not hold. Nonetheless, it  is
common (perhaps as part of a sequence of programs to produce a database) to
write a self-contained TABLO Input file to read the data and carry out the
calculations to check the balancing conditions. Such a TAB file will write the
results of its calculations to a file you can look at to check that values are
in balance.
When you are checking balance, you need to keep in mind that GEMPACK programs only produce about 6
figures of accuracy (see section
25.8
).
6.3.1    SJCHK.TAB to check balance for Stylized Johansen
[gpd1.4.7.1]
Supplied with GEMPACK is the file SJCHK.TAB which is used to check the balance
of a data set for Stylized Johansen. View this file to see that
the values of Coefficients DVCOM (value of output of each commodity) and
DVCOSTS (costs in each industry) and the difference of these two (should be
zero) are calculated and written to an output file. An Assertion statement (see
section
25.3
) is included so that the program will stop with an
error if the difference is significant.
You will also see that a check is made to count the number of negative numbers
in the data base (there should be none).
We encourage you to run SJCHK.TAB on SJ.HAR to check the balance.
If you prefer to use WinGEM, first make sure that both default directories
point to the directory in which the Stylized Johansen files are located. First
run TABLO on SJCHK.TAB and produce output for GEMSIM (for simplicity). Then run
GEMSIM using Command file SJCHK.CMF. When GEMSIM has run, click on View
Input/Output files  and look at the values of DVCOM, DVCOSTS, and BALCHECK in
the output file SJCHK.HAR. Also check that there are no negatives in the data
base.
If you are working from the command prompt, change into the directory to which
you copied the Stylized Johansen files. Then run TABLO on sjchk.tab to produce
output for GEMSIM (for simplicity), ie, type:
TABLO -pgs sjchk
Then run GEMSIM taking inputs from the Command file sjchk.cmf, ie, type:
GEMSIM -cmf sjchk.cmf
When GEMSIM has run, look at the values of DVCOM, DVCOSTS, and BALCHECK in the
output file sjchk.har, and also check for negative values.
6.3.2    SJCHK.TAB to check balance of updated data
[gpd1.4.7.2]
Whenever you carry out a simulation, the updated data should satisfy the same balance checks as the
original data — otherwise there is something wrong with the TAB file for your model.
It is easy to use SJCHK.TAB to check the balance of the updated data SJLB.UPD produced in the 10
percent labor increase simulation carried out via SJLB.CMF (see chapter
3
). To do
this, save the file SJCHK.CMF as SJLBCHK.CMF and alter the statement
file iodata = SJ.HAR ;
to read
file iodata = sjlb.upd ;
Then run GEMSIM taking inputs from Command file SJLBCHK.CMF. Look at the output file SJLBCHK.HAR
produced and check that SJLB.UPD is still balanced.
5
A more sophisticated, production-quality model should include such checking code in its
main TAB file. That way, checking occurs every time the model runs — so alerting
you early to potential problems.
6.3.3    GTAPVIEW for checking and summarising GTAP data
[gpd1.4.7.3]
The standard GTAP TAB file referred to as GTAPVIEW provides a summary of any GTAP data set. We have
provided GTPVEW61.TAB with the GEMPACK examples. You can see an example of the use of this TAB file
in section
25.8.1
.
The file GTPVEW61.TAB is an interesting example of a TAB file. For example, look at the set
GDPEXPEND and how the values in Coefficient GDPEXP are built up via several Formulas. This shows a
neat way of arranging summary data into headers on a Header Array file. You may be able to adapt
some of these techniques in your own work.
6.3.4    Checking the balance of ORANIG data
[gpd1.4.7.4]
See section
25.8.2
for details about this.
6.4    Which program to use in file conversion?
[gpd1.4.8]
You need to convert between file formats
at the start of the process of constructing a model database, when raw data in various
formats need to be first stored in HAR files;
after a simulation, when results in SL4 (and perhaps HAR) files need to be
comunicated to other programs, such as Excel, Matlab, or MsWord.
ViewHAR can be used interactively to do many conversions; but if a process is
to be automated, command-line programs (if available) are preferred — they can
be run from batch (BAT) scripts.
Table
6.2
below shows which programs to use in converting files
from one type to another. The table rows (source) and columns (destinations)
are labelled with 3-letter abbreviations, as follows:
HAR
GEMPACK Header array file
XLS
Excel Speadsheet file
CSV
text file as saved or read by Excel; may be comma-, tab- or space-delimited
SQL
text file in "database" format; one number per row; zeros not shown
TXT
GEMPACK text file: a special type of CSV, see chapter
38
GDX
binary data file used by GAMS
SL4
GEMPACK solution file
Table 6.2 Programs to use in file conversion
↓In Out→
HAR
XLS
CSV
SQL
TXT
GDX
HAR
=
har2xls
head2xls
head2csv
seehar
har2csv
har2txt
har2gdx
XLS/X
xls2head
=
Excel
-
Excel
-
CSV
-
-
=
-
-
-
SQL
csv2har
-
-
=
-
-
TXT
modhar
txt2har
ViewHAR
-
ViewHAR
=
ViewHAR
GDX
gdx2har
ViewHAR
-
ViewHAR
ViewHAR
=
SL4
sltoht
ViewHAR
sltoht
ViewHAR
ViewHAR
ViewHAR
In many cases alternative programs could be used; for example, ViewHAR can do most conversions.
The table above shows the most appealing command-line program, if there is one — otherwise
ViewHAR is shown. Note that from 2012 xls2head can read either XLS or XLSX files, but har2xls,
head2xls and ViewHAR create only the older-format XLS files.
The programs gdx2har and har2gdx (see section
77.1
) are command-line Windows-only
programs distributed with GEMPACK. Slightly different versions are distributed with GAMS.
The programs har2csv, csv2har, har2txt, txt2har, har2xls, head2csv, head2xls and xls2head are command-line
Windows-only programs. If they are not already included in your GEMPACK installation, you can
download them from the GEMPACK website at
http://www.copsmodels.com/gpmark9.htm
. To
obtain instructions for using, say, txt2har, you would simply type from the command line:
txt2har
In the table above "SQL" means, text files with lines like this:
"CitrusFruit","France","Germany","2005", 3974.2
meaning that, eg, 3974.2 tonnes of citrus was exported from France to Germany in 2005. Seehar's
SQL option also offers a (fairly heavy-duty) way to turn HAR into SQL (see section
37.1.4
).
For more about MODHAR, see chapter
54
; for  SEEHAR see chapter
37
;
and for SLTOHT see chapters
39
and
40
.
To extract results from SL4 solution files, SLTOHT may be used to convert into one of two formats:
a CSV text spreadsheet file which may be read by Excel — see chapter
40
. A
spreadsheet mapping file
is used to select particular results.
a HAR file — see chapter
39
. A
header mapping file
is used to
select particular results. The HAR file might be processed by a TABLO program or it might be
converted to another format using one of the programs listed in table
6.2
.
See also
Running SLTOHT from the command line
.
6.5    Further information
[gpd1.4.9]
There are many techniques used in preparing and updating data files for models. This chapter is
just a very brief introduction to the topic. Suggestions for finding out more are given below.
Aggregation:
ViewHAR or, better, a command-line program AggHAR can be used to aggregate data.
Both methods are described in the ViewHAR Help.
TABLO Input files:
see example using mappings in section
11.9
.
Disaggregation:
can can be carried out using the (old-fashioned) command-line program DAGG
downloadable from
http://www.copsmodels.com/gpmark.htm
. Alternatively, the newer
command-line program DaggHAR (instructions in DaggHAR.doc) may be more convenient. In most cases,
you will also need to write a TABLO program to do some of the job.
Periodic courses on the preparation of data for CGE models are listed at
http://www.copsmodels.com/pgemdata.htm
7    GEMPACK file types, names and suffixes
[gpd1.5.8]
Click here
for detailed chapter contents
GEMPACK programs use a number of different file types to communicate between themselves or to
store results. Usually the file-name suffix (extension) indicates the file type.
7.0.1    Files with system-determined suffixes
[gpd1.5.8.1]
Some types of files must be given system-determined suffixes.
For example, GEMPACK requires that TABLO Input files have suffix  .TAB.  Below we list the most
important type of files with system-determined suffixes (see also
3.14.1
).
Table 7.1 File type with system-determined suffixes
File type
Suffix
Type
See
TABLO Input file
.TAB
text
section
4.3
TABLO Information file
.INF
text
section
9.1.6
Solution file
.SL4
binary
chapter
27
Equations file
.EQ4
binary
chapter
59
GEMSIM Auxiliary Statement file
.GSS
binary
section
3.14.2
GEMSIM Auxiliary Table file
.GST
binary
section
3.14.2
TABLO-generated Auxiliary Statement file
.AXS
binary
section
3.14.2
TABLO-generated Auxiliary Table file
.AXT
binary
section
3.14.2
TABLO-generated program
.FOR
text
section
3.14.2
Environment file
.EN4
binary
section
23.2.5
Model Information file
.MIN
text
section
21.4.1
Solution Coefficients file
.SLC
binary
section
28.1
Extrapolation Accuracy file
.XAC
text
section
3.12.3
Whenever a program asks you for the name of any of these files with system-determined suffixes, you
should never include the suffix in your input (since the program will add the suffix
automatically). For example, in a Command file put
Solution file = sjlb ;     ! Correct
rather than
Solution file = sjlb.sl4 ;    ! Incorrect
Similar to the .SLC Solution Coefficients file, are .UDC, .AVC, and .CVL files --
see sections
28.2
and
28.3
.
7.0.2    Suffixes of other files
[gpd1.5.8.2]
Even though GEMPACK does not force you to use specific suffixes for other files, there are several
different types of files where it has become customary amongst experienced GEMPACK users to use
certain suffixes.  Examples are in the table below.
Table 7.2 Commonly used suffixes for other files
File type
Usual Suffix(es)
Type
See
Header Array data file
.HAR
binary
chapter
5
Text data file
.TXT
text
chapter
38
Updated Header Array file
.UPD, .HAR
binary
section
3.9
Command file
.CMF
text
chapter
20
Stored-input file
.STI, .INP
text
section
48.3
Spreadsheet Mapping file
.MAP
text
section
40.1
Solution file in HAR form
.SOL
binary
section
39.1
In some cases there are considerable advantages from using these "usual" suffixes. For example,
some Command file syntax is only available if you use suffix .CMF (see section
20.5
).
when you open a Header Array file with ViewHAR, by default it only shows you files with suffixes
.HAR, .DAT, .UPD, .SUM, .SOL, .SLC, .SL4, .CVL, .UDC, .AVC, and .PRM.
when you install GEMPACK, certain file suffixes are "associated" with GEMPACK
programs. For example, .TAB and .CMF files are associated with TABmate — this
means that in Explorer the TABmate icon is shown beside these files and you can
double-click on them to open them in TABmate. Similarly .HAR and .UPD files are
associated with ViewHAR, and .SL4  files are associated with ViewSOL.
Many of the GEMPACK programs suggest suffixes for output files they create. For example, SEEHAR
often suggests suffix .SEE for its output files. We suggest that you go along with these
suggestions unless you have good reasons to do otherwise.
7.0.3    Files — binary, header array or text?
[gpd1.5.8.3]
There are two basic file types on all computers — text files (which are
sometimes called ASCII files) and binary files. Text files are more
portable — they can be viewed or printed using any text editor.  Binary files are more
compact and faster to process, but use one of a number of proprietary
formats — so only special programs can read or create them. GEMPACK uses several files
of each type, as indicated in tables
7.1
and
7.2
.
Header Array (HAR) files (see chapter
6
) are important binary files used often in GEMPACK
to hold data for models. Although not recommended, you can also hold such data in text files:
when used for this they must follow a standard format described in chapter
38
.
7.0.4    Why so many files?
[gpd1.5.8.4]
We have listed many of the important files, and discussed their roles, in section
3.14
above.
Some files are created to facilitate communication between different GEMPACK programs. [For
example, GEMSIM Auxiliary files allow communication between TABLO and GEMSIM.]
Other files are created for users to look at or use. Some contain information which is important in
reporting simulation results while others may allow experienced modellers to carry out tasks more
efficiently. For example, when GEMSIM or a TABLO-generated program runs, it may produce various
files listed below.
The
updated data (UPD) files
provide information about the simulation and can be used as the
starting point for other simulations (see section
3.9
).
The
Equations (EQ4) file
can be used as the starting point for Johansen simulations using SAGEM (see
chapter
58
).
The
Extrapolation Accuracy (XAC) file
can be used to tell if the solution produced is sufficiently
accurate for your purpose (see section
3.12.3
). (If not, you may need to re-run it
with more steps.)
An
Environment (EN4) file
. Saving an Environment file makes it easy to run a different simulation
with the same closure: you simply give the name of the Environment file instead of having to
re-specify which of the variables are exogenous or endogenous. See section
23.2.5
.
7.1    Allowed file and directory names
[gpd1.5.9]
Both Windows
1
and GEMPACK impose certain restrictions on file and directory names:
File names are not case sensitive. So, for example, there is no distinction between
the file names SJ.HAR and sj.har. Thus, if you create a new file called "sj.HAR" you will, in the
process, delete any existing file called SJ.har or sj.HAR.
GEMPACK programs never access or produce files whose names end with one or more spaces. For
example, if you try to create a file called  "xx.out " the trailing space will be omitted and the
file "xx.out" will be created. Also the last character should not be a period (.).
GEMPACK programs do not reliably support file  names containing Chinese or other
non-English characters. We apologise for this inconvenience.
GEMPACK Windows programs (WinGEM, ViewHAR etc) do not reliably support file names
containing "%" or "#" so we advise you to not to use these characters.
You may not use characters
\ / : *  ? & < >
or
|
in file names.
We advise you not to use characters
; ! ( )
or
=
in file names.
VERY long file and folder names should be avoided.
Directory names
are restricted in the same way that file names are. Even if you are trying to
create a file with a legal  name, it may not be possible to create the file in a directory with an
illegal name. For example, Chinese or Scandinavian characters in a directory name may cause problems.
Previous versions of GEMPACK and Fortran imposed tighter restrictions on file and directory names
-- see section 5.9 of
GPD-1
. You might still be using a few older GEMPACK programs.
To maintain compatibility with those:
Stick to letters, digits, "-" and "_" (and avoid spaces) in your file and folder names.
Another virtue of the above rule is that is simpler to remember than the more complex rules above.
7.1.1    File names containing spaces
[gpd1.5.9.4]
To specify a file name containing spaces in a Command (CMF) file, enclose the name inside double quotes:
solution file = "my sj" ;
See section
20.4.2
for details.
If you are running a program interactively, you must not add quotes "" when specifying file names
containing spaces. Similarly you should not add quotes when specifying such file names in
Stored-input (STI) files.
If you are specifying a Command file name, STI file name or LOG file name on the Command line (see
section
48.5
), enclose the name in double quotes "" if it contains a space as in, for
example,
gemsim  -cmf  "c:\my sj\my sjlb.cmf"
7.1.2    Characters in stored-input files and command files
[gpd1.5.9.5]
TAB characters and other control characters (ASCII characters 0-31 and 127) can cause problems in
Stored-input files and Command files. TAB characters are replaced by a single space. Most control
characters are replaced by a single space but will cause a warning message. The program will stop
with an error message if it finds a Control-Z character before the end of the file if there is text
after it, or if there are two or more in the file.
There is no testing for other characters (ASCII characters 128-255) but these would cause problems
if used in file names — see section
7.1
.
7.1.3    Files that could be deleted
[cleanupfiles]
Section
3.14.8
list various filetypes that could be deleted to save space, or prior to backing up.
8    Overview of running TABLO and the TABLO language
[gpd2.1]
Click here
for detailed chapter contents
TABLO is the GEMPACK program which translates the algebraic specification of an economic model into
a form which is suitable for carrying out simulations with the model. The output from TABLO can be
either GSS/GST files used to run the GEMPACK program GEMSIM or alternatively, a Fortran program,
referred to as a TABLO-generated program. When TABLO writes a TABLO-generated program, you must
then compile and link (LTG) the program to create the EXE file of the
TABLO-generated program. Either GEMSIM or the EXE file can be run to carry out simulations.
This chapter contains an introduction to running TABLO, to compiling and linking TABLO-generated
programs, and to writing TABLO Input files.
Chapters
9
to
18
provide complete user documentation of the TABLO program
and the TABLO language. TABLO is the means by which economic models are implemented within
GEMPACK, as described in the introductory chapters
3
to
7
(which you
should read first).
Chapter
9
provides some of the fine print about running TABLO, including how it
linearizes levels equations and about its Condensation stage.
Chapter
10
is a full description of the syntax required in TABLO Input files while
chapter
11
contains a comprehensive description of the semantics (and a few points
about the syntax which may not be clear from chapter
10
) for the current version of
TABLO.
Chapter
12
describes the TABLO statements for post-simulation processing; chapter
13
builds on this to shows how
ranked sets
can be used to present tables of
winning and losing sectors in a simulation.
Chapter
15
provides some assistance with the important task of verifying that your
model is actually carrying out the calculations you intend. Chapter
16
provides some
details about intertemporal (that is, dynamic) modelling in GEMPACK. In chapter
17
we
give examples of ways in which the TABLO language can be used to express relationships which at
first sight are difficult to capture within the syntax and semantics of TABLO Input files.
Chapter
18
gives rules for linearizing levels equations, and indicates how the
linearized equations are shown on the Information file.
We expect that chapters
9
to
18
will be used mainly as a reference
document (rather than being read through in order). Use the Index to help find the relevant part
whenever you need more information about TABLO.
Chapters
19
to
35
describe carrying out simulations on economic models
after they have been implemented using TABLO.
8.1    Running TABLO on an existing model
[gpd2.1.1]
Running TABLO from WinGEM is described in sections
3.5.2
and
3.5.3
.
See the examples in sections
43.3
and
43.4
of running
TABLO for the models Stylized Johansen (SJ) and Miniature Orani (MO).
See the examples in sections
43.5
to
43.8
where TABLO
is run with a Stored-input file in order to condense the models GTAP and ORANIG.
Each of these examples assumes that you wish to run an existing model, or modify slightly an
existing model.
You will find that TABmate (see section
8.4.1
below and
section
36.4
) provides an excellent interface for working with TABLO Input files,
especially for identifying and eliminating syntax and semantic errors.
8.1.1    Example models ORANIG01 and GTAP61
[gpd2.1.1.1]
In chapter
3
the Stylized Johansen model SJ.TAB was used as the main example model.
In following chapters the main example models are
(1)
the ORANI-G model (May 2001) in the TABLO Input file ORANIG01.TAB written by Mark
Horridge and colleagues from the Centre of Policy Studies, and
(2)
the GTAP model Version 6.1 (August 2001) in the TABLO Input file GTAP61.TAB written by
Tom Hertel and colleagues from the Center for Global Trade Analysis at Purdue University (see
Hertel (1997)
and
McDougall (2002)
).
The files for these models are amongst the Examples supplied with GEMPACK (see sections
60.5.1
and
60.7.1
).
Running the ORANIG01 Model
View the ORANIG01 model in TABmate by opening ORANIG01.TAB from the GEMPACK Examples directory
(usually C:\GP\EXAMPLES).
To run TABLO on the TABLO Input file ORANIG01.TAB, you should use the Stored-input file which
carries out condensation.
(1)
If you have a Source-code version of GEMPACK use the file OG01TG.STI to write a
TABLO-generated program. At the Command prompt, the commands to use are
tablo -sti og01tg.sti            (creates TG-program ORANIG01.FOR).
ltg oranig01                     (compiles and links to produce ORANIG01.EXE).
Or you could click the TABLO STI button in TABmate (selecting og01tg.sti) to run both commands above.
(2)
If you have the Executable-Image version of GEMPACK use the file OG01GS.STI. At the
Command prompt, the command to use is
tablo -sti og01gs.sti            (produces output for GEMSIM)
Or you could click the TABLO STI button in TABmate (selecting og01gs.sti) to run the command above.
(3)
If you are working in WinGEM, select the TABLO option
Run from STI file
and
then select the STI file OG01GS.STI or OG01TG.STI and then click on the
Run
button.
Running the GTAP61 Model
Similarly you can view the GTAP61 model by opening the file GTAP61.TAB from the GEMPACK Examples
subdirectory in your text editor. This model also needs a condensation STI file to run
successfully. The Stored-input file called GTAP61TG.STI writes a TABLO-generated program and
GTAP61GS.STI writes auxiliary files for GEMSIM.
(1)
If you have a Source-code version of GEMPACK use the file GTAP61TG.STI. At the Command
prompt, the commands to use are
tablo -sti gtap61tg.sti   (creates TG-program GTAP61.FOR)
ltg gtap61   (compiles and links to produce GTAP61.EXE).
Or you could click the TABLO STI button in TABmate (selecting gtap61tg.sti) to run both commands above.
(2)
If you have the Executable-Image version of GEMPACK use the file GTAP61GS.STI. At the
Command prompt, the command to use is
tablo -sti gtap61gs.sti   (produces output for GEMSIM)
Or you could click the TABLO STI button in TABmate (selecting gtap61gs.sti) to run the command above.
(3)
If you are working in WinGEM, select the TABLO option
Run from STI file
and
then select the STI file GTAP61GS.STI or GTAP61TG.STI and then click on the
Run
button.
Syntax and semantic examples from the TABLO Input files ORANIG01.TAB and GTAP61.TAB are used in
throughout this chapter so that you can check a complete example of the relevant TABLO statements
in a working model.
8.1.2    TAB file and WFP/PGS on command line
[gpd5.10.1.2]
If you do not want to do any condensation actions not included in the TAB file, and you do not
want to specify any options other than PGS or WFP at the Code stage, you can include the name of
the TABLO Input file on the command line when you run TABLO. TABLO then runs in batch mode and
does not expect any other input. If there are condensation actions in the TAB file, running with
-pgs or -wfp will do those condensation actions (but give no opportunity for other condensation
actions) and then go to Code stage.
You specify the name of the TABLO Input file on the command line - don't include the suffix .TAB.
You can specify PGS by putting  -pgs  on the command line.
You can specify WFP by putting  -wfp  on the command line.
Examples
1:
To run TABLO to process SJ.TAB
tablo  sj
This will produce either a TABLO-generated program or output for GEMSIM, depending on which is the
default action for the TABLO.EXE which is running. [The default is TABLO-generated program if
TABLO.EXE is from a Source-code Version of GEMPACK or is GEMSIM if TABLO.EXE is from an
Executable-Image Version of GEMPACK.]
2:
To run TABLO to process SJ.TAB and produce output for GEMSIM
tablo -pgs  sj
3:
To run TABLO to process SJ.TAB and produce output for GEMSIM and
send all output to file SJGS.LOG
tablo  -pgs sj -log sjgs.log
4:
To run TABLO to process SJ.TAB and produce the TABLO-generated program SJ.FOR
tablo  -wfp  sj
or
tablo sj  -wfp
the order is not important.
If you specify the TABLO Input file on the command line
1
, it is the same as running TABLO interactively and hitting carriage-return for every response

(except the TAB file and WFP/PGS choices).
8.1.3    Running TABLO from TABmate with no STI file
[tablocode]
Similar to the above, the
TABLO Code
button in TABmate runs TABLO without a STI file.
The
Options...Code and Other
menu item is used to control whether TABLO produces a Fortran program or
GEMSIM output.
8.1.4    Preliminary pass to count statements
[gpd2.1.1.2]
TABLO carries out a preliminary pass of the TABLO Input file. On this pass, it just counts the
numbers of the different types of statements and allocates memory for the checking which follows on
the second pass.
If a line of your TABLO Input file is too long (see section
11.1.2
), this error is
pointed out on the preliminary pass. In that case, TABLO does no other checking. You must fix this
long line and then run TABLO again. You may find that there are errors above this position in the
TAB file, since TABLO has not really checked anything except line length on the preliminary pass.
8.2    Compiling and linking TABLO-generated programs
[gpd2.1.2]
"Compiling and linking" a TABLO-generated program refers to what has been called Step 1(b) in
sections
3.5.2
and
3.6.1
.
If you are working at the command prompt, the command  LTG as in
LTG  <program-name>      (for example,    ltg oranig01   or   ltg gtap61)
will compile and link a TABLO-generated program.
If you are using WinGEM, you can compile and link via menu item
Compile & Link
... under
WinGEM's
Simulation
menu.
Within TABmate, when either of the
TABLO Code
or
TABLO STI
buttons is used to produce a Fortran program,
LTG may be run automatically (or you may be prompted — see the
Options...Code and Other
menu item.
The input to the compile and link process is the TABLO-generated program (for example,
ORANIG01.FOR). The output is an EXE file for the TABLO-generated program (for example,
ORANIG01.EXE). You run the EXE file to carry out simulations with the model.
8.3    Writing a TABLO input file for a new model
[gpd2.1.4]
If you wish to develop a TAB file for your own model without relying on an existing model,
how do you go about it? Chapter
4
describes how to build a new model using Stylized
Johansen as a simple example. To summarise, the steps are as follows.
Write down your equations in ordinary algebra. Choose whether to write a linearized, mixed or
levels model. You may need to linearize your equations by hand (see section
18.2
).
Compile a list of variables used in these equations.
Compile a list of data needed for the equations (levels values, parameters, other coefficients).
Work out what sets are involved for the equations, variables and data.
Construct your TAB file in TABmate (see section
8.4.1
below) and keep checking
the syntax (clicking the "TABLO check" button) until you have removed all syntax errors. Section
4.7.1
contains a hands-on example showing how to correct errors in TABLO Input files.
Consult chapters
10
and
11
for the TABLO syntax needed to write your TABLO
statements. Use other models as extended examples of how to write TABLO code.
If your model is large, you may need to condense it — see section
8.5
below.
You can run your model within WinGEM or at the Command prompt.The simulation process is described
in chapter
3
and in more detail in chapters
19
to
35
.
8.4    Modern ways of writing TABLO input files (on a PC)
[gpd2.1.5]
Although you can create TAB files with any text editor (such as emacs, NotePad or vi), we suggest
that you use GEMPACK's TABMate text editor.
8.4.1    Using TABmate
[gpd2.1.5.1]
Unless you have a firm preference for another text editor, we recommend that you use the
TABmate editor because it has many in-built functions to assist you including the following.
Coloured highlighting of TABLO syntax, and of Command file syntax.
Easy TABLO syntax checking allowing you to correct errors in the TAB file.
A powerful Gloss feature which displays all parts of the TABLO code where a chosen variable or
coefficient is used (see section
4.3.2
and section
46.1
).
You can have multiple files open and cut-and-paste between them in the usual Windows way.
More details about TABmate can be found in section
36.4
.
8.4.2    Using TABmate to find a closure and suggest substitutions
[autoclosure]
TABmate's
Tools...Closure
command helps you to find a standard closure for your GE model.
It can also be used to find logical errors in your model, to suggest condensation actions, or to help construct a STI file.
The results of the closure analysis are contained in a text report file suffixed CLO.
TABmate starts from the premise that there must be the same number of endogenous variables as
equations in your model. By extension, we can usefully imagine that each equation explains a
particular variable. Variables not explained by any equation are deemed to be exogenous in the
standard closure.
In order for TABmate to know which variable is explained by a given equation, the modeller must
follow a naming convention for equations. The convention is that the equation which explains
variable "p1", say, is named "E_p1" (prefix E_). If you do not follow this convention, the Closure
command will be no use to you, although the rest of TABmate will work normally.
Use the TABmate menu command
Tools...Help on Tools
to find out more about the
Tools...Closure
command.
8.4.3    Using TABmate to create a CMF file
[autocmf]
TABmate's
Tools...View/Create CMF
will create a template CMF file for your model — you
only need to add in the closure, shocks and actual filenames.
8.4.4    Using TABmate to reformat your code
[beautyparlour]
TABLO is not case-sensitive: it will not complain if your TAB file refers to the same variable as
"x1lab", "X1LAB" and "x1Lab". However, consistency is desirable, and can be enforced using
TABmate's
Tools...Beauty Parlour
command. You can choose for, say, variables, to be
rendered consistently in lower-case, or with the capitalization used when they first appeared in
the TAB file.
8.4.5    Using ViewHAR to write TABLO code for data manipulation
[gpd2.1.5.2]
If you have a Header Array data file containing set and element labelling (see section
5.0.3
) and Coefficient names, ViewHAR can be used to write some of the TABLO code.
To test this, run ViewHAR and open the file SJ.HAR from the GEMPACK Examples subdirectory. Select
Export | Create TABLO Code
from the main ViewHAR Menu. This will write some text to the
Clipboard. In TABmate, create a new blank TAB file, and paste in text from the Clipboard. The
following text will be created.
Example of TABLO code written by ViewHAR
Set SECT # description # (s1, s2);
Set FAC # description # (labor, capital);

Coefficient
(All,s,SECT)(All,a,SECT) DVCOMIN(s,a)
 # Intermediate inputs of commodities to industries - dollar values #;
(All,f,FAC)(All,s,SECT) DVFACIN(f,s)
 # Intermediate inputs of primary factors - dollar values #;
(All,s,SECT) DVHOUS(s) # Household use of commodities - dollar values #;.
Read
 DVCOMIN from file InFile header "CINP";
 DVFACIN from file InFile header "FINP";
 DVHOUS from file InFile header "HCON";

Update
(All,s,SECT)(All,a,SECT) DVCOMIN(s,a) = 0.0;
(All,f,FAC)(All,s,SECT) DVFACIN(f,s) = 0.0;
(All,s,SECT) DVHOUS(s) = 0.0;

Formula
(All,s,SECT)(All,a,SECT) DVCOMIN(s,a) = 0.0;
(All,f,FAC)(All,s,SECT) DVFACIN(f,s) = 0.0;
(All,s,SECT) DVHOUS(s) = 0.0;

Write
 DVCOMIN to file OutFile header "CINP" longname
 "Intermediate inputs of commodities to industries - dollar values";
 DVFACIN to file OutFile header "FINP" longname
 "Intermediate inputs of primary factors - dollar values";
 DVHOUS to file OutFile header "HCON" longname
 "Household use of commodities - dollar values";
ViewHAR has done all the dull part of code writing, and you can quickly edit the code by writing in
appropriate filenames, formulas, updates etc to suit your model. This is very useful if you want to
write a data manipulation TABLO Input file.
8.5    Condensing a large model
[gpd2.1.6]
If your model is either too large to run on your computer, or too slow, you should consider
condensation. See section
14.1
for an introduction to condensation, sections
14.1.2
and
14.1.4
for examples of condensation, and section
14.1.10
for further details. Basically you need to consider:
Are there variables you can "omit", that is, variables that in this set of simulations will be
exogenous and not shocked?
Which are the endogenous variables with the largest number of components? These are candidates for
substituting out or backsolving.
To substitute or backsolve a variable, you need to identify a single equation which explains or determines
that variable and is of the
same dimensions
.
TABmate's
Tools...Closure
command (see section
8.4.2
) is
extremely useful in suggesting condensation possibilities. Also very useful is
the Condensation Information file: see section
14.1.16
.
Recent versions of GEMPACK allow you to specify condensation actions within the TAB files via
OMIT, SUBSTITUTE and BACKSOLVE statements: see section
10.16
.
That is the recommended approach.
TABmate's
Tools...Closure
command will produce condensation commands that you can paste into your TAB file.
8.5.1    Condensation in STI file: a legacy technique
[oldsticond]
The older method was to specify condensation actions in a STI or Stored-input file.
As mentioned above, nowadays you should instead place
OMIT, SUBSTITUTE and BACKSOLVE statements within the TAB file.
TABmate's
Tools...Create in-TAB condensation from STI
command will convert
condensation commands from an older STI file into this modern form.
If you still need to work with the old STI file method, the examples in
section
14.1.2
show an older way to create a STI file for
condensation, suitable for small models: you could run TABLO interactively to
carry out condensation and to create a Stored-input file which can be re-used
to carry out this condensation.
TABmate's
TABLO STI
button can create a default STI file — which you could add to.
The
Tools...Closure
command will produce condensation commands that you can
paste into the STI file.
Using a basic STI file as a starting point, you can easily add, using your text editor, other
variables to omit, substitute or backsolve. When this Stored-input file is complete, run TABLO with
this Stored-input file, and continue in the usual way, either compiling, linking and running the
TABLO-generated program, or running GEMSIM.
Example - Stored-input files for ORANIG
Use TABmate to look at the Condensation file for ORANIG01.TAB. There are two
versions: OG01GS.STI which creates output for the GEMPACK program GEMSIM (using the pgs option), and
OG01TG.STI which creates the TABLO-generated program ORANIG01.FOR and its Auxiliary files
ORANIG01.AXS and ORANIG01.AXT (using the wfp option).
9    Additional information about running TABLO
[gpd2.2]
Click here
for detailed chapter contents
Most of the information about running TABLO is given in chapters
3
and
4
. This chapter (which you could skip during a first reading) provides some
additional, advanced information relating to:
the TABLO Options screens (section
9.1
),
how TABLO linearizes levels equations (section
9.2
),
reporting Newton error terms in models with levels equations (section
9.3
).
9.1    TABLO options
[gpd2.2.1]
This section gives details about Options that are available at the TABLO Check stage. Chapter
50
gives details about options available at the TABLO Code stage.
The TABLO program is divided into three distinct stages:  CHECK, CONDENSE and CODE.
In the CHECK stage, TABLO analyses the information on the TABLO Input file and points out any
syntax errors (where the format expected by TABLO has not been followed) or semantic errors  (where
different parts of the input are not consistent with one another).  Errors are output briefly to
the screen and also to an Information file (usually with suffix .INF). Errors can be found by
searching the Information file for %% which precedes each error message. (See section
9.1.6
below for more details.)
The CONDENSE stage is optional. Details of condensation are given in section
14.1
and
in section
14.1.10
below.
The CODE stage either writes output for GEMSIM or writes the TABLO-generated program which
corresponds to the TABLO Input file.
On starting TABLO, you make selections from the TABLO Options menu shown below. Standard Basic
Options LOG, STI, SIF, ASI, BAT, BPR at the top of the screen are described in chapter
48
.
You can choose which stages you carry out using the First Stage options (F1, F2, F3) and the Last
Stage options (L1, L2, L3). The default choices for these options are F1 for the First Stage and L3
for the Last Stage. These mean that TABLO starts with the CHECK stage, then, if no errors are
encountered during the CHECK, carries out CONDENSE (if requested), and then goes on to the CODE
stage.
The option of carrying out some stages only is rarely used (except by GEMPACK developers doing debugging).
There is more about it in section
64.1
.
TABLO OPTIONS
             ( --> indicates those in effect )
 
     BAT Run in batch              STI Take inputs from a Stored-input file
     BPR Brief prompts             SIF Store inputs on a file
     LOG Output to log file        ASI Add to incomplete Stored-input file
 
     First Stage                   Last Stage
     -----------                   ----------
 --> F1 CHECK                      L1 CHECK
     F2 CONDENSATION               L2 CONDENSATION
     F3 CODE GENERATION        --> L3 CODE GENERATION
 
     RMS Require maximum set sizes to be specified
     NTX Dont store TAB file on Auxiliary file
     ICT Ignore Condensation statements on TAB file
     ASB All Substitutions treated as Backsolves
     NWT Add Newton-correction terms to levels equations
     ACD Always use Change Differentiation of levels equations
     SCO Specialized Check Options menu
 
 Select an option   :  <opt>      Deselect an option      : -<opt>
 Help for an option : ?<opt>      Help on all options     : ??
 Redisplay options  : /           Finish option selection:Carriage return
Your selection >

                    Main TABLO Options Menu
Option ACD is discussed in section
9.2.4
below. It
affects the way TABLO linearizes any levels equations which, in turn, can affect the numerical
properties of multi-step calculations.
Option RMS (Require Maximum Set Sizes) affects the CHECK stage of TABLO.
When this option is selected the statement
SET REG # Regions # READ ELEMENTS FROM FILE GTAPSETS Header "H1";
would produce a semantic error. See section
11.7.2
for details.
Option NWT could be used with Newton's method to solve equations (see section
26.6
).
It causes TABLO to add the $del_newton term to all
levels equations.
Option NTX is described in section
9.1.1
below. Option SCO leads to other options as
described in section
9.1.3
below. Options ICT and ASB, which relate to the
Condensation stage of TABLO (see section
14.1.10
below), are described in sections
14.1.15
and
14.1.13
respectively below.
9.1.1    TABLO input file written on the auxiliary files
[gpd2.2.1.1]
The TABLO Input file for your model is written to the Auxiliary Table
file (.AXT for a TABLO-generated program, .GST for GEMSIM) by default. These
files are HAR files — but would only be meaningful to the GEMPACK developers.
You can use the program TEXTBI (see chapter
70
) to recover the Stored-input
file from the Auxiliary Table file.
If, for reasons of confidentiality, you do not wish to send out your TABLO Input file on the
Auxiliary files, you can turn off this default. At the first option screen in TABLO or at the top
of your condensation Stored-input file, select the option
NTX  Don't store the TAB file on Auxiliary file
then continue as usual with the TABLO input.
9.1.2    TABLO file and TABLO STI file stored on solution file
[gpd2.2.1.2]
When the TABLO Input file is stored on the Auxiliary Table (.AXT or .GST) file (see section
9.1.1
above), this TABLO Input file is transferred from the Auxiliary Table file to
the Solution file when you carry out a simulation using GEMSIM or a TABLO-generated program.   This
means that you can use the program TEXTBI (see chapter
70
) to recover that TABLO
Input file from the Solution file.  This may assist in understanding simulation results.
Similarly, if you use a Stored-input file to run TABLO, this Stored-input file is transferred to
the Auxiliary Table file produced by TABLO (unless TABLO option NTX is selected)
This Stored-input file is also transferred to the Solution file when you run a simulation using
GEMSIM or a TABLO-generated program.  You can use TEXTBI (see chapter
70
) to recover
the Stored-input file from the Solution file or from the Auxiliary Table file.  [Strictly speaking,
the Stored-input file put on the Auxiliary Table file is the one used for the CODE stage of TABLO.
If you stopped and restarted TABLO (see section
64.1
) condensation actions may not be
on the Stored-input file put on the Auxiliary Table or Solution file.]
Note that the Stored-input file is only stored on the Auxiliary Table file if you use the STI
option (see section
48.3
) in TABLO by inputting
tablo.sti.sti-file-name
or the -STI option on the command line (see section
48.5
) as in
tablo  -sti  sti-file-name
It does not happen if you use input redirection as in
tablo  <  sti-file-name          ! NOT recommended
since in this case TABLO is not aware that you are using a Stored-input file.
This means that it is usually possible to recover the TABLO file and any condensation actions from
any Solution file.
Since the original data is stored on the SLC file (see section
28.1
), this means that
you can recover everything about a simulation from the Solution and SLC files.
9.1.3    Specialised check options
[gpd2.2.1.3]
Choosing SCO gives access to the Specialised Check Options menu given below. However these options
are rarely used so TABLO uses the default values for these unless you actively choose SCO and one
or more of the Specialised Check options. You can find out more about these options from this menu.
[For example, type  ?SM5  to find out about option SM5.]
Specialised Check Options 
              ( --> indicates those in effect )
  
       Semantic Check Options
       ----------------------
       SM2 Allow duplicate names
       SM3 Omit coefficient initialisation check
       SM4 Omit checking for warnings
       SM5 Do not display individual warnings
  
       Information File Options
       ------------------------
       IN1 Has the same name as the TABLO Input file
       IN2 Only show lines containing errors
       IN3 Omit the model summary in CHECK stage
  
Select an option   :  <opt>  Deselect an option      : -<opt>
Help for an option : ?<opt>  Help on all options     : ??
Redisplay options  : /       Return to TABLO Options : Carriage return
Your selection >

                  Specialised Check Options Menu
9.1.4    Doing condensation or going to code generation
[gpd2.2.1.4]
After the CHECK stage is complete, if no syntax or semantic errors have been found, you are given
the choice below:
Do you want to see a SUMMARY of the model        [s], or
              perform CONDENSATION                 [c], or
              proceed to AUTOMATIC CODE GENERATION [a], or
              EXIT from TABLO                      [e] :

   (Enter a carriage return to proceed directly
      to AUTOMATIC CODE GENERATION)
If you select [a] (or if you type a carriage return), you will skip condensation and go directly to
the Code stage of TABLO.
If you select [c], the following choice is presented. See section
14.1
and section
14.1.10
below for a description of Condensation.
--> Starting CONDENSATION
  
  Do you want to SUBSTITUTE a variable             [s], or
      substitute a variable and BACKSOLVE for it   [b], or
                 OMIT one or more variables        [o], or
                 ABSORB one or more variables      [a], or
                 DISPLAY the model's status        [d], or
                 EXIT from CONDENSATION            [e] :
If you select [e] at either of the last two choices, the TABLO Record file (.TBR) and the Table
file (.TBT) [see section
64.1
] are written and the program TABLO ends.
9.1.5    TABLO code options
[gpd2.2.1.5]
When you proceed to Automatic Code Generation, a Code Options Menu is presented. The main choice
here is whether to produce output for GEMSIM (option PGS) or to write a TABLO-generated program
(option WFP). Because the effect of the other options is intimately bound up with the way GEMSIM or
the resulting TABLO-generated program will run, we postpone a discussion of these options until
chapter
50
.
9.1.6    Identifying and correcting syntax and semantic errors
[gpd2.2.1.6]
If TABLO finds syntax or semantic errors during the CHECK stage, it reports them to the terminal
and also, more usefully, to the Information (.INF) file.
To identify these errors, look at the Information file (via a text editor, or print it out). Syntax
and semantic errors are marked by two percent signs %%, so you can search for them in an editor.
The Information file usually shows the whole TABLO Input file (with line numbers added); lines with
errors are repeated and a brief explanation is given of the reason for each error. (Also a question
mark '?' in the line below the line with an error points to the part of the line where the error
seems to be.)
Usually the change needed to correct the error will be clear from the explanation given. If not,
you may need to consult the relevant parts of chapter
10
(for syntax errors) or chapter
11
(for semantic errors).
One syntax or semantic error may produce many more. If, for example, you incorrectly declare a
COEFFICIENT A6, then every reference to A6 will produce a semantic problem ("Unknown coefficient").
In these cases, fixing the first error will remove all consequential errors.
TABmate (see section
8.4.1
above and
section
36.4
) provides an excellent interface for working with TABLO Input files,
especially for identifying and eliminating syntax and semantic errors.
9.2    TABLO linearizes levels equations automatically
[gpd2.2.2]
This section is only relevant for TABLO Input files which contain explicit levels EQUATIONs or
explicit levels VARIABLEs.
1
During the CHECK stage, when TABLO processes a TABLO Input file containing levels EQUATIONs and
levels VARIABLEs, it converts the file to a linearized file; we refer to this as the associated
linearized TABLO Input file. Although you may not see this associated linearized file (since the
conversion is done internally by TABLO), you should be aware of some of its features.
The most important feature of this conversion is that, for each levels VARIABLE, say X, in your
original TABLO Input file, there is an associated linear VARIABLE whose name is usually that of the
original levels variable with "p_" added at the start.
2
Also, for each levels VARIABLE in the original TABLO Input file, a COEFFICIENT with the same name
as the levels VARIABLE is declared in the associated linearized TABLO Input file.
Other features of this conversion will be explained in sections
9.2.1
to
9.2.4
below.
It is important to realise that the rest of TABLO (the last part of the CHECK and all of the
CONDENSE and CODE stages) proceeds
as if the associated linearized TABLO Input
file were the actual TABLO Input
file.
This means that during CHECK and CONDENSE, warnings and error messages may refer to statements in
this associated linearized file rather than in your original TABLO Input file.
During the CHECK stage, TABLO normally echoes the original TABLO Input file to the Information file
(and flags any errors or warnings there). When there are levels EQUATIONs in the original file, in
the Information file which TABLO writes to describe this model, each levels EQUATION is followed by
its associated linearized EQUATION. So, if you wish to see the associated linearized EQUATIONs you
can do so by looking at the CHECK part of the Information file. In section
18.3
we show
part of the Information file obtained from processing the TABLO Input file SJ.TAB for the mixed
version of Stylized Johansen. You can look there to see the linearized EQUATIONs associated with
some of the levels EQUATIONs from this TABLO Input file, which is shown in full in section
4.3.3
.
9.2.1    Change or percentage-change associated linear variables
[gpd2.2.2.1]
When you declare a levels VARIABLE in your TABLO Input file, you must also decide which form of
associated linear VARIABLE you wish to go in the associated linearized TABLO Input file. If you
want it to be the corresponding percentage change, you don't need to take special action since this
is usually the default. If however you wish it to be the corresponding change, you must notify
TABLO of this by including the qualifier (CHANGE) in your VARIABLE statement. For example, the
statement
VARIABLE (LEVELS,CHANGE) BT  # Balance of Trade # ;
in a TABLO Input file will give rise to a CHANGE variable c_BT in the associated linearized TABLO
Input file.
As explained in section
4.3.5
, there are some circumstances when a change linear
variable is preferable to the percentage-change alternative. When you declare a levels VARIABLE we
suggest the following guidelines.
For a levels variable which is always positive (or always negative), direct TABLO to work with the
associated percentage change as a linear VARIABLE in the associated linearized TABLO Input file.
For a levels variable which may be positive, zero or negative, direct TABLO to work with the
associated change as a linear VARIABLE in the associated linearized TABLO Input file. This can be
achieved by declaring the levels VARIABLE via a VARIABLE(CHANGE) statement, as in, for example,
VARIABLE (LEVELS,CHANGE) BT  # balance of trade # ;
9.2.2    How levels variable statements are converted
[gpd2.2.2.2]
When you declare a levels VARIABLE or write down a levels EQUATION in a TABLO Input file, these
give rise to associated statements in the associated linearized TABLO Input file created
automatically by TABLO. After that, TABLO's processing proceeds as if  you had actually written
these associated statements rather than the levels statements actually written. We look at the
different possibilities below.
Declaration of a Levels VARIABLE
Each declaration of a levels VARIABLE is automatically converted to three statements in the
associated linearized TABLO Input file.
3
These are
(1):
the declaration of a COEFFICIENT(NON_PARAMETER) with the same name as the levels
VARIABLE;
(2):
the declaration of the associated linear VARIABLE if there 

[...truncated...]

### GEMPACK for Mac users (link)
*URL:* https://www.copsmodels.com/gpmacosx.htm

# GEMPACK for Mac OS X

GEMPACK for Mac OS X
GEMPACK for Mac OS X
Last updated 10 June 2013. Products described here are NOT currently supported.
Introduction
The GEMPACK programs consist of:
Command-line programs which can be re-compiled to run on most computers, including the Mac.
GUI programs which run only under Windows. These include useful viewing programs such as ViewHAR, TABmate, and AnalyseGE, and also
   GEMPACK-based programs such as GTAPAgg and RunGTAP. These will not run as "native" Mac applications.
GEMPACK for Mac OS X
'GEMPACK for Mac OS X' is a 'wrapper', prepared by Joe Francois, that allows the GEMPACK GUI programs to be installed and run on the Mac (using
Wine (WineSkin)
) alongside native Mac applications. You need an Intel-based Mac
   running Snow Leopard (OS X 10.6) or later. The package could be used in several ways:
You could use the included executable-image version of GEMPACK to formulate and solve CGE models. Programs such as ViewHAR, TABmate,ViewSOL,
   etc work more or less as they do under Windows. You would need a normal GEMPACK licence (either executable-image or source-code). Some tasks might
   require you to use a command prompt: Wine's DOS-like terminal shell supplied with the package.
You might use included GTAP-related programs such as RunGTAP, a program which runs the standard GTAP model (it needs no licence). Or, you
   might run GTAPAgg, a program to prepare aggregations of the GTAP database. To use this you need to additionally purchase (from
GTAP
) and install a GTAP database licence and a set of GTAP database files.
You might use included GEMPACK viewing programs such as ViewHAR and ViewSOL in conjunction with a separately-purchased source-code version of
   GEMPACK running natively on the Mac. The 'native' programs, all command-line, would include supplied utility programs, and TABLO-generated
   programs to solve your CGE model. You would use the Unix Terminal shell which is part of Mac OS X to run command-line programs, and
   ViewHAR/ViewSOL/AnalyseGE (under Wine) to look at numbers.
Download and Install
The package may be downloaded from
here
[coming soon]. To install, simply:
drag the file GEMPACK to your applications directory.
drag the GEMPACK Apps folder to your applications directory.
But first, print out and study
GPMacOSX.PDF
!
Caveats
Program behaviour under Wine is similar but not identical to behaviour under Windows. A few features do not work under Wine. Support is very
   limited since:
'GEMPACK for Mac OS X' has been prepared as a volunteer effort by Joe Francois.
The GEMPACK developers have little Mac experience and only one Mac PC (a MacBook Pro running Lion).
Kudos !
We thank Joe Francois for assembling this package, which we think will be very helpful to GEMPACK Mac users.
Go back to
Versions of GEMPACK
GEMPACK Home Page

### Get the software! (link)
*URL:* https://www.copsmodels.com/gplapsoft.htm

# Installing GEMPACK on your laptop prior to a training course

Installing GEMPACK on your laptop prior to a training course
Installing GEMPACK on your laptop prior to a training course
GEMPACK-oriented training courses often require that you bring and use your own laptop computer. Most Windows laptops will be adequate (for
   specific requirements see
here
). To do the course exercises, you'll need to install GEMPACK on your laptop. Usually,
   this is rather easy. However, we ask that you install the software
prior to the course
, for two reasons:
Any software problems will surface during the first course sessions -- when the instructors are busiest. Installing beforehand allows problems
   to be identified and addressed before the course starts.
To install the software, you will need "Administrator" access rights. If your laptop belongs to, or was configured by, your organization's IT
   section, you may only have limited or "Standard User" access rights. In that case an Administrator password may be needed to install GEMPACK. This
   could mean that someone from your organization's IT section has to be present during the install. In such a case, installation during the course
   might be impossible. Moreover, particular corporate IT policies occasionally cause problems with GEMPACK. You would need to work with your IT
   section to resolve such problems.
What if my laptop already has GEMPACK on it?
The course requires that you have GEMPACK Release 11.0 or later. To see which version you have, use the menu command
Help...GEMPACK
   licence
from TABmate or ViewHAR. If you have Release 10 or earlier, you must install Release 11. The instruction document mentioned below
   explains how you can rename your existing GEMPACK folder so that you can later go back to the old version, if necessary.
Downloading and Installing the Executable-Image Version of GEMPACK
First, download, print out, and
read
quickinst.pdf
. It contains simplified install instructions
   especially designed for training course use.
Next, download the Trial Edition of the
Limited Executable-Image Version of GEMPACK
from
this page
. It
   mentions a longer install document, GPInstall.pdf, but you should follow the shorter QuickInst instructions. Section 3 of the QuickInst
   instructions explains how to check that your installation is working properly by running a model simulation:
it is important that you complete
   this section
.
The Trial Edition includes all the main GEMPACK programs and can carry out a full range of modelling tasks. There is a model size limitation --
   but this will not cause problems during the course. The Trial Edition comes with a temporary licence lasting 6 months from the download date --
   long enough to complete the course. Often course participants will receive a
longer-lasting licence during the course
.
Other course software
For some courses, you may also need to pre-install other software, such as, for example, the RunDynam program for running dynamic simulations, or
   the RunGTAP program which solves the GTAP model. You will receive specific instructions if you need to install other programs. In any case, you
   should install GEMPACK
first
: the other programs may require that you already have GEMPACK installed.
Participants in the
Practical GE
course held in Melbourne and elsewhere are required to download the
MINIMAL free training software
, and to complete the exercises supplied with it.
Other course files
At the beginning of the course you will be supplied with various other files that are needed for the course exercises.
Course CD
During most courses participants are given a course CD (or USB key) containing: software required for the course; files needed for course
   exercises; and various supplementary material. Such CDs are mainly intended for use
after
the course. You should install the necessary
   software
before
the course.
Upgrading the temporary licence
The trial edition of the
Limited Executable-Image Version of GEMPACK
comes with a temporary licence lasting 6 months from the
   download date -- long enough to complete the training course. Usually course participants will be entitled to a better licence. Specific details
   will vary according to the course. For example:
Often course participants will receive (either beforehand by email, or on arrival at the course) a course-specific licence lasting 12 months
   from the start of the course.
See also
Laptop requirements
Executable-Image Version of GEMPACK
Training course page

## Non-text files (not extracted)

- `Installing GEMPACK.zip` (zip)
