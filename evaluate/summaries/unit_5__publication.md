---
title: "FAIR Climate and Water Science: Publication"
unit_id: 5
course_id: 4
level: "Developer"
slug: publication
is_course: 0
---

# FAIR Climate and Water Science: Publication

Module teaching publication of data and source code to repositories (GitHub, MyGeoHub, HydroShare) for DOI, sharing, and version control. Presented by I Luk Kim (ITAP Research Computing, Purdue University, kim1634@purdue.edu).

Three publishing methods: GitHub, MyGeoHub Publication, MyGeoHub Tool (Jupyter Notebook-based).

GitHub: Version control system (Git) with remote storage. Pros: easy to publish by uploading code. Workflow: (1) Create repository at https://github.com/new (enter name, initialize with README); (2) Clone remote to local (git clone <repo_url>); (3) Modify/add files; (4) Upload to remote (git add, git commit -m, git push). Git commands: clone (download remote to local), add (add files to local repo), commit (save current changes as version), push (upload to remote). Tool: GitHub Desktop (https://desktop.github.com/).

MyGeoHub Publication: MyGeoHub projects with "Publication" feature. Pros: easy, upload data/code, fill metadata, supports DOI/versions/citations. Workflow: (1) Create new project or use existing (https://mygeohub.org/projects); (2) Upload code to iData Storage; (3) Submit new publication with files/metadata; (4) Wait for admin approval; (5) Publish with DOI. Steps: select file for publication, enter content description, select authors, add extra files, choose license, enter tags, add release notes, submit draft for review. Example DOI: https://mygeohub.org/publications/8/about?v=2.

MyGeoHub Tool (Jupyter Notebook): Web-based interactive computational platform supporting Python, Java, R code. Pros: interactive tool, publish as web application, provides DOI, open/closed source options. Workflow: (1) Create new tool (Menu RESOURCES > TOOLS > Start a new Tool, https://mygeohub.org/tools/create); (2) Launch Jupyter Notebook tool; (3) Clone tool files from svn repo (svn checkout <tool_repo_url> <tool_directory>); (4) Create notebook file in bin/ directory; (5) Change invoke script in middleware directory; (6) Commit changes (svn add, svn commit -m); (7) Request review and publish.

Invoke script options: Notebook Mode (code visible, interactive execution), App Mode (code/toolbar hidden, automatic execution). Invoke command format: /usr/bin/invoke_app with options -T (Notebook Mode), -A (App Mode).

Tool example: https://mygeohub.org/resources/geoviewer. Tool authentication: MyGeoHub Dashboard > Account > Request token if needed.

Related resources: FAIR data principles image, Global Change and Challenges of Sustainably Feeding a Growing Planet book reference (baldos_and_hertel.jpg).

## Summarized attachments
- **Publishing data and code to github and MyGeoHub** (how_to_publish.pdf, file): Tutorial by I Luk Kim (ITAP Research Computing, Purdue University) on publishing methods including GitHub (version control with git clone/add/commit/push commands, GitHub Desktop GUI tool), MyGeoHub Publication (create projects, upload to iData Storage, submit with metadata for DOI approval), and MyGeoHub Tools (Jupyter Notebook-based web applications with Notebook Mode and App Mode invoke scripts). Covers DOI assignment, version control, licensing, authorship, and publication workflows.
- **baldos_and_hertel.jpg** (baldos_and_hertel.jpg, image): Image related to Global Change and Challenges of Sustainably Feeding a Growing Planet book reference.
- **FAIR Data Principles** (FAIR_data_principles.jpg, image): Image illustrating FAIR data principles.
