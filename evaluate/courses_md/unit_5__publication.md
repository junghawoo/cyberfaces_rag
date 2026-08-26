---
title: "FAIR Climate and Water Science: Publication"
unit_id: 5
course_id: 4
level: "Developer"
slug: publication
is_course: 0
---

# FAIR Climate and Water Science: Publication

**Description:** This module teaches how to publish data and source code to various repositories such as github, MyGeoHub, and HydroShare for DOI, sharing, and versioning control.

## Extracted resources (local files)

### Publishing data and code to github and MyGeoHub
*Source file:* `how_to_publish.pdf`  ·  *type:* file

HOW TO PUBLISH YOUR 
CODE
ITAP Research Computing
I Luk Kim

Publishing Methods
§Github
§MyGeoHub – Publication
§MyGeoHub – Tool (Jupyter Notebook based)

How to publish your code
GitHub

GitHub
§ What is Git and GitHub?
– Git
• Version control system
• You can download code from remote repositories, or others can download yours
• Can be used to track code changes (versions)
– GitHub
• A website providing remote storage for git
• Free to use
• Provides Wiki, bug tracking, etc
§ Pros
– Easy to publish by uploading your code.

GitHub
§ Publishing steps overview
①Create a new repository on GitHub
②Download code and git data to your local machine
③Modifying existing files or adding yours
④Upload them to the remote repository

Creating a new repository.
•
Visit https://github.com/new
•
Enter “Repository name”
•
Check “Initialize this repository with a README”
•
Click [Create repository]

Created repository
Git repo URL

Git – commands
$ git clone <git repo url>
$ git add <filename to be added>
$ git commit –m <commit message>
$ git push
• Git clone : download data from the remote to local repository
• Git add : add files to my local repo
• Git commit : save the current changes as a version
• Git push : upload to the remote repository

GitHub
§ GitHub provides GUI tool
§ GitHub Desktop
– https://desktop.github.com/
§ Please Install it, and create
a GitHub account before
the class

GitHub Desktop start page – clone a repository

Clone a repository – select the created repository

Cloned repository – Go to your local repository directory

Copy your code to the local repository directory. Edit README.md file.

Applied changes
Enter summary, then click [Commit to master]
This only updates the local repository

Push to the remote repository

Updated GitHub repository

How to publish your code
MyGeoHub - Publication

MyGeoHub - Publication
§ MyGeoHub – Publication
– MyGeoHub Project supports “Publication” feature
– You can publish datasets or code with a digital object identifier (DOI)
§ Pro
– Easy to publish. Upload data, then fill out metadata fields
– Support DOI, versions, usage, citations…

MyGeoHub publication example
DOI
https://mygeohub.org/publications/8/about?v=2

MyGeoHub - Publication
§ Publication step overview
①Create a new project or use existing one
②Upload your code to ‘iData Storage’
③Submit a new publication with the uploaded files and metadata
④Wait for approval by admin
⑤Publish with DOI

Create a new project
https://mygeohub.org/projects
MyGeoHub Menu -> COMMUNITY -> Project

Upload your code to project iData storage
https://mygeohub.org/projects/cybertrainingdemo

Start a new publication

Select file for the publication

Content - Select the upload file

Description – enter all 3 information

Authors – select authors

Extras – add extra files

License – choose license

Tags – enter tags

Notes – add release notes

Review – submit draft for review

Publication review submitted

How to publish your code
MyGeoHub – Tool
(Jupyter Notebook)

MyGeoHub – Tool (Jupyter Notebook)
§ Jupyter Notebook?
– Web-based interactive computational platform
– You can upload/create various types of files such as python code, documents, maps, plots, etc
– Moreover, you can run python code interactively in a browser 
– Reference
•
https://jupyter.org/
•
https://jupyter.readthedocs.io/en/latest/
•
https://jupyter.org/widgets
§ MyGeoHub – (Jupyter Notebook based) Tool
– You can publish your code so that others can see and run them lively
– With a “App Mode”, your tool can be looked like a web application by hiding code & toolbar
– Along with Jupyter Notebook, you can make a tool with other languages, such as Java, R, etc.
§ Pros
– Interactive tool
– You can publish your code as a web application
– Also provides DOI
– Choice of open/closed source (e.g., before and after publication)

Tool example
https://mygeohub.org/resources/geoviewer

MyGeoHub – Tool (Jupyter Notebook)
§ Publishing steps overview
①Create a new tool
•
This will create default folders in MyGeoHub repository
②Launch existing Jupyter Notebook tool to implement and test
③Clone the created tool files from the tool repo (svn)
④Create a new Notebook, implement your code
⑤Change Invoke script
⑥Commit your changes to the tool repo
⑦Ask review (by admin), publish your tool

Create new tool
•
Menu [RESOURCES] -> click [TOOLS], click [Start a 
new Tool]
•
https://mygeohub.org/tools/create

Create a new tool

https://mygeohub.org/tools/ctpubdemo/status
Tool created

Launch existing Jupyter Notebook tool to implement
•
MyGeoHub Dashboard
•
My tools -> All Tools -> search “jupyter” then click 
“Jupyter Notebook with anaconda 5.1”

Jupyter Notebook tool index page

Open a new terminal

svn checkout <your tool repo url> <tool directory>
yirugi@MyGeoHUB:~$ svn checkout https://mygeohub.org/tools/ctpubdemo/svn/trunk ctpubdemo
Authentication realm: <https://mygeohub.org:443> A demo tool for cyber training class Subversion Repository
Password for 'yirugi': ********
A    ctpubdemo/doc
A    ctpubdemo/src
A    ctpubdemo/bin
A    ctpubdemo/data
A    ctpubdemo/middleware
A    ctpubdemo/examples
A    ctpubdemo/rappture
A    ctpubdemo/src/Makefile
A    ctpubdemo/middleware/invoke
Checked out revision 1.
yirugi@MyGeoHUB:~$
MyGeoHub – Tool (Jupyter Notebook)
§ Download tool files to your workspace
Tool repo url : https://mygeohub.org/tools/<tool name>/svn/trunk
If you don’t have MyGeoHub password,
Go to MyGeoHub dashboard -> Account -> Request token

Local repository created

Downloaded basic directories of the tool
Jupyter notebook files
Tool invoke script

Create a new notebook file under bin/ directory

New notebook
1.
Add your code
2.
Enter a name of this file
3.
Save

Close and Halt

Goto /middleware directory, click invoke to change invoke script

/usr/bin/invoke_app "$@" -C rappture -t ctpubdemo
/usr/bin/invoke_app "$@" -C "start_jupyter -T @tool bin/mycode.ipynb" -u anaconda3-5.1
/usr/bin/invoke_app "$@" -C "start_jupyter -A -T @tool bin/mycode.ipynb" -u anaconda3-5.1
•
Notebook Mode : Others can see your code, and run interactively
•
App Mode : Your code and toolbar will be hidden, and your code runs automatically
Change to one of followings
Change the invoke script

yirugi@MyGeoHUB:~$ cd ctpubdemo/
yirugi@MyGeoHUB:~/ctpubdemo$ svn add bin/mycode.ipynb
A         bin/mycode.ipynb
yirugi@MyGeoHUB:~/ctpubdemo$ svn commit -m "initial version"
Authentication realm: <https://mygeohub.org:443> A demo tool for cyber training 
class Subversion Repository
Password for 'yirugi': ********
Adding         bin/mycode.ipynb
Sending        middleware/invoke
Transmitting file data ..
Committed revision 2.
$ svn add <filename to be added>
$ svn commit –m <commit message>
• svn add : add files to my local repo
• svn commit : save the current changes as a version
SVN commit steps
$ cd <tool directory>
• Go to your tool directory

https://mygeohub.org/tools/ctpubdemo/status
Ask review your code

Waiting for the review and deployment

After approval and deployment, you can launch your tool

Click “Create this page” to enter metadata of your tool

Enter description, contribution, etc of your tool

Click “I approve it” to request publishing your tool

EA/EOU
THANK YOU
I Luk Kim
kim1634@purdue.edu

## Image text (OCR)

### `baldos_and_hertel.jpg`
se eisnle

Global Change and
the Challenges

of Sustainably
Feeding a Growing
Planet

### `FAIR_data_principles.jpg`
Bee J \ccessible —

R
oy
%

e
