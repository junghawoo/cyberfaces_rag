---
title: "Share Your Success Story"
unit_id: 286
course_id: 0
level: "Expert"
slug: share-your-success-story
is_course: 1
---

# Share Your Success Story

## Extracted resources (local files)

### biocontainers101.pdf
*Source file:* `biocontainers101.pdf`  ·  *type:* pdf

Biocontainers 101
Using Containers in Bioinformatics
Yucheng Zhang
Senior Life Science Scientist
ITaP Research Computing
ITaP Research Computing Virtual Workshop Series 
Yucheng Zhang, Lev Gorenstein
Feb. 25, 2022

Outline
• What are containers and why should we use them? 
• Singularity basics
• Public container repositories
• Pull and use public biocontainers
• Deployed biocontainers on RCAC clusters
• Build your own biocontainers

What are containers? 
A container is an abstraction for a set of technologies that aim to solve the 
problem of how to get software to run reliably when moved from one computing 
environment to another.
A container image is simply a file (or collection of files ) saved on disk that 
stores everything you need to run a target application or applications.
Registry is a place to store (and share) container images.

Why should we use containers?
Ø Getting organized: containers keep things 
organized by isolating programs and their 
dependencies inside containers. 
Ø Build once, run almost anywhere: containers 
allow us to package up our complete software 
environment and ship it to numerous operating 
systems.
Ø Reproducibility: containers can ensure identical 
versions of apps, libraries, compliers, etc. 
Source: https://support.terra.bio/hc/en-
us/articles/360037340472-Docker-container-overview

A real example

Why should we use containers on our clusters?
Enable you to install and use software easier
v Some software or packages has specific requirements for certain libraries 
such as GLIBC. Because our cluster’s OS version is old, its libraries may not 
be compatible with your software. In such case, installing software into our 
clusters will be very challenging. 
v However,  if you build a container, you can get the latest everything and 
aren't limited by the cluster's OS version. You are the master of your 
containers.

source: https://github.com/harvardinformatics/bioinformatics-coffee-hour/blob/master/singularity/images/installing_software.gif

Docker 
The concept of containers emerged in 1970s, but they were 
not well known until the emergence of Docker containers in 
2013.
Docker is an open source platform for building, deploying, 
and managing containerized applications. 
Some concerns about the security of 
Docker containers on HPC: Docker gives 
superuser privileges, but we do not want 
users to have full, unrestricted admin/ root 
access.

Singularity 
v Singularity was developed in 2015 as an open-source project 
by researchers at Lawrence Berkeley National Laboratory led 
by Gregory Kurtzer. 
v Singularity is emerging as the containerization framework of 
choice in HPC environments. 
1. Enable researchers to package entire scientific workflows, 
libraries, and even data.
2. Users do not need to ask their system admin (e.g., RCAC) 
to install software for them.
3. Can use docker images.
4. Secure! 
5. Does not require root privileges.

Singularity basics 
Detailed singularity user guide is available 
at: sylabs.io/guides/3.8/user-guide
v Build
v Pull
v Shell
v Exec
The main singularity command
singularity [options] <subcommand> [subcommand options …]

Singularity workflow on HPC
1 (Optional). Build singularity containers on a 
computer system where you have root or sudo
privilege, e.g., your personal computer with singularity 
installed.
2. Pull the public containers or transfer your own 
containers to HPC.
3. Run singularity containers on the HPC system.

singularity pull
Download a container from a given URI. 
singularity pull [output file] <URI>
Supported URIs include:
vLibrary: pull an image from singularity library
library://<user>/<collection>/<image>[:tag]
vDocker hub: pull an image from Docker Hub.
docker://<repository>/<image>[:tag]
vQuay.io: pull an image from Quay.io registry 
docker://quay.io/<repository>/<image>[:tag]
vhttp, https: pull an image using the http(s?) protocol
e.g., https://library.sylabs.io/v1/imagefile/library/default/alpine:latest

Three useful image registries
1. Docker Hub (https://hub.docker.org) 
v Online repository of Docker container images.
v As of Feb. 17, 2022, 8,842,825 available container images. 
2. BioContainers (https://biocontainers.pro/registry)  
v A community-driven project for bioinformatics containers.
v 10.6K tools,45.4K versions,222.5Kcontainers and packages.
v The Bioconda package index lists all software available. 
v The Biocontainers registry provides a searchable interface.
3. GALAXY project (https://depot.galaxyproject.org/singularity/) 
v The BioContainers community also stored each singularity image in Galaxy 
depot. 
v Can be pulled or ran using the HTTP protocol.

singularity pull example
Let’s pull bowtie2 from three different resources. 
Ø Docker hub (https://hub.docker.com/r/biocontainers/bowtie2/tags)
singularity pull bowtie.2.4.1.sif  docker://biocontainers/bowtie2:v2.4.1_cv1
Ø Bioconda package index (https://bioconda.github.io/recipes/bowtie2/README.html)
singularity pull bowtie.2.4.5.sif docker://quay.io/biocontainers/bowtie2: 2.4.5--py37hafa4d4c_1
Ø GALAXY project (https://depot.galaxyproject.org/singularity)
singularity pull bowtie.2.4.5.sif https://depot.galaxyproject.org/singularity/bowtie2:2.4.5--py39hbb4e92a_0
Recommendation: add the --disable-cache option to prevent image layers from being cached in 
${HOME}/.singularity/cache
singularity pull --disable-cache name_to_save.sif URI
singularity pull [options] name_to_save.sif URI

singularity shell
Go inside the container and start an interactive shell 
singularity shell myimage.sif
Type “exit” in the interactive shell to go back to host system

Bind mounts
v Programs running inside a container will not have access to directories 
and files outside of your home and the current directory. 
v Singularity allows you to map directories on your host system to 
directories within your container using bind mounts.
singularity shell --bind hostdir1:containerdir1 --bind hostdir2:containerdir2 myimage.sif
Singularity binds several directories into the container image 
automatically. $HOME, /tmp and $PWD is the default list. 
We also configured singularity to bind /apps, /depot, and /scratch on our 
clusters.

singularity exec
Run a command within a container
singularity exec myimage.sif command
For example:
singularity exec blast.2.11.0.sif blastx -query input.fasta -db swissprot -out blast.out
--bind option is also very useful for singularity exec
For example:
singularity exec --bind $HOME/data/:/data/ blast.2.11.0.sif blastx -query /data/input.fasta -db nr
## input.fasta is located in the host directory $HOME/data/

RCAC Biocontainers
For example:
$ module load biocontainers
$ module load bamtools/2.5.1
$ bamtools -h
A collection of pre-downloaded container 
images wrapped into handy modulefiles so 
they look and feel like native applications.

Alphafold
Deployed in all clusters, support both CPU and GPU. 
$ module load biocontainers
$ module load alphafold/2.1.1
https://github.com/deepmind/alphafold
The full database (~2.2TB) has been downloaded and setup for users.  
Usage: 
run_alphafold.sh --flagfile=$AlphaDB --fasta_paths=XX --output_dir=XX ...
$AlphaDB (/depot/itap/datasets/alphafold/full_db.ff) is a configuration file passed to AlphaFold
containing the location of the database. Typically it should not be edited. Users can add other 
parameters based on your needs.

HOMER
$ module load biocontainers
$ module load homer/4.11
Selected database have been downloaded for users. 
ORGANISMS: yeast, worm, mouse, arabidopsis, zebrafish, rat, human and fly. 
PROMOTERS: yeast, worm, mouse, arabidopsis, zebrafish, rat, human and fly. 
GENOMES: hg19, hg38, mm10, ce11, dm6, rn6, danRer11, tair10, and sacCer3.  
Check installed databases:
$ configureHomer.pl -list
Software for motif discovery and next-gen sequencing analysis

$ module load biocontainers
$ module load gtdbtk/1.7.0
GTDB-Tk reference data (R202) has been downloaded for users. 
Example usage:
$ gtdbtk identify --genome_dir genomes --out_dir identify --extension gz --cpus 8
$ gtdbtk align --identify_dir identify --out_dir align --cpus 8
$ gtdbtk classify --genome_dir genomes --align_dir align --out_dir classify --extension gz --cpus 8
Toolkit for assigning objective taxonomic classifications to 
bacterial and archaeal genomes based on the Genome Database 
Taxonomy GTDB.

HUMAnN 3
$ module load biocontainers
$ module load humann/3.0.0
Full ChocoPhlAn, UniRef90, EC-filtered UniRef90, UniRef50, EC-filtered UniRef50, and 
utility_mapping databases have been downloaded for users.  
Check the database and config by: 
$ humann_config --print
HUMAnN Configuration ( Section : Name = Value )
database_folders : nucleotide = /depot/itap/datasets/humann/chocophlan
database_folders : protein = /depot/itap/datasets/humann/uniref
database_folders : utility_mapping = /depot/itap/datasets/humann/utility_mapping
Quantify species’ contributions to community function

Run_dbcan
$ module load biocontainers
$ module load run_dbcan/3.0.2
Latest version of database has been downloaded and setup, including CAZyDB.09242021.fa, 
dbCAN-HMMdb-V10.txt, tcdb.fa, tf-1.hmm, tf-2.hmm, and stp.hmm.
Usage: 
$ run_dbcan protein.faa protein --out_dir test1_dbcan
$ run_dbcan genome.fasta prok --out_dir test2_dbcan
Automated CAZyme annotation
https://github.com/linnabrown/run_dbcan

R-RNAseq
$ module load biocontainers
$ module load r-rnaseq/4.1.1-1
OR  $ module load r-rnaseq/4.1.1-1-rstudio
Commands:
1. R
2. Rscript
3. rstudio (only exist in rstudio version)  
Customized R container for RNAseq analysis. 
BiocManager
1.30.16
readr
2.0.2
ComplexHeatmap 2.9.4
readxl 1.3.1
DESeq2 1.34.0
purrr 0.3.4
edgeR 3.36.0
dplyr
1.0.7
DEXSeq 1.40.0
pheatmap
1.0.12
stringr 1.4.0
limma 3.48.3
forcats 0.5.1
tibble 3.1.5
ggplot2 3.3.5
tidyr
1.1.4
openxlsx
4.2.5
Thanks to Lev Gorenstein’s r/4.1.1 base image, users can also install other packages, same 
with non-containerized R.

R-scRNAseq
$module load biocontainers
$module load r-scrnaseq/4.1.1-1
OR $module load r-scrnaseq/4.1.1-1-rstudio
Commands:
1. R
2. Rscript
3. rstudio (only exist in rstudio version)  
Customized R container for scRNAseq analysis. 
BiocManager
1.30.16
schex
1.8.0
tidyr
1.1.4
Seurat 4.1.0
CoGAPS 3.14.0
readr 2.0.2
SeuratObject
4.0.4
celldex 1.4.0
readxl 1.3.1
SeuratWrappers 0.3.0
dittoSeq
1.6.0
purrr 0.3.4
monocle3 
1.0.0
DropletUtils
1.14.2
dplyr 1.0.7
SingleCellExperiment 1.16.0
miQC
1.2.0
stringr 1.4.0
scDblFinder
1.8.0
Nebulosa
1.4.0
forcats 0.5.1
SingleR 1.8.1
tricycle 
1.2.0
ggplot2 3.3.5
scCATCH 3.0
pheatmap
1.0.12
openxlsx 4.2.5
scMappR 1.0.7
limma
3.48.3, 3.50.0
rliger 1.0.0
tibble 3.1.5
Thanks to Lev Gorenstein’s r/4.1.1 base image, users can also install other packages, same with non-containerized R.

Build your own containers with singularity
The first step is to install singularity on your personal computer.
We have singularity version 3.8.0 on the cluster. To guarantee 
compatibility, please be sure to follow the installation guide for version 
3.8 on your system (https://sylabs.io/guides/3.8/user-
guide/quick_start.html).
$ sudo singularity build image.sif image.def
v Need to build using a computer with elevated privileges, then copy to cluster.
v If no access to such a computer, can also build in the cloud.

Remote builder
If you need to build an image from a system where you don’t have admin privileges, we can build 
remotely using the Sylabs Remote Builder. 
To remotely build an image using singularity, go through the following steps: 
1. Go to: https://cloud.sylabs.io/, and create a Sylabs account. 
2. Create a new “Access Token”, and copy it to clipboard.
3. Login to our clusters, and run `singularity remote login` in terminal and paste the access token at 
the prompt.
4. Then you can remotely build your own singularity image on the cluster.
singularity build -r myimage.sif myimage.def
or  singularity build --remote myimage.sif myimage.def
Once finished, the image will be downloaded automatically so that it’s ready to use.

Singularity definition file 
A definition file, or def file, is a recipe to build a 
container image with singularity. It is divided 
into two parts:
1. Header: the Header describes the core 
operating system to build within the 
container.
2. Section: each section is defined by 
a % character followed by the name of the 
particular section. Different sections add 
different content or execute commands at 
different times during the build process.
def file for prokka 1.14.6 prepared by NIH HPC staff
Header
Section
Detailed instruction on how to prepare a definition 
file is available at 
https://sylabs.io/guides/latest/user-
guide/definition_files.html.

Preferred bootstrap agents
1. library: images hosted in Sylabs Cloud Library 
2. docker:  images hosted in Docker Hub
3. localimage: images saved on your machine
Information about more bootstrap agents can be found in Singularity user guide.

Bootstrap: docker
From: ubuntu:20.04
%labels
Author "Yucheng Zhang <zhan4429@purdue.edu>"
Version v0.935
%help
Singularity container with ANGSD v0.935. This container also installed htslib and samtools.
%post
# update the system and install building essentials
apt-get -y update
apt-get -y install --no-install-recommends --no-install-suggests libssl-dev libcurl4-gnutls-dev libbz2-dev  \
liblzma-dev libz-dev samtools gcc g++ git ca-certificates build-essential  make zip wget unzip locales locales-all
# clean up
apt-get -y autoremove && apt-get clean. && rm -rf /var/lib/apt/lists/*
# Install htslib
SRC=/usr/local/src
mkdir -p $SRC && cd $SRC
git clone --recursive https://github.com/samtools/htslib.git
cd htslib && make
# Install angsd
cd $SRC && git clone https://github.com/ANGSD/angsd.git
cd angsd && make HTSSRC=$SRC/htslib
#Symbolic link
chmod +x $SRC/angsd/misc/realSFS
cd /usr/local/bin
ln -s $SRC/angsd/angsd .   && ln -s $SRC/angsd/misc/realSFS . 
ANGSD
Program for analyzing NGS data

aTRAM
automated target restricted 
assembly method
Bootstrap: docker
From: continuumio/miniconda3
%labels
Author "Yucheng Zhang <zhan4429@purdue.edu>"
Version 2.4.3
%help
This container contains the latest version (v2.4.3) of aTRAM. 
%post
conda install git
cd /opt/   &&  git clone https://github.com/juliema/aTRAM.git
cd aTRAM
&&   chmod +x *.py
conda install python=3 numpy biopython psutil
conda install -c bioconda blast velvet trinity abyss spades exonerate
%environment
export PATH=/opt/aTRAM/:$PATH

Bootstrap: localimage
From: r-base:4.1.1.sif
%post
Rscript -e "install.packages('tidyverse')"
Rscript -e "install.packages('openxlsx', dependencies = TRUE)"
Rscript -e 'if (!requireNamespace("BiocManager", quietly = TRUE))
install.packages("BiocManager")' \
&& Rscript -e 
'BiocManager::install(c("limma","edgeR","DESeq2","ComplexHeatmap","DEXSeq"))'
If users want to build your own R containers, welcome to use our r-base images and recipes that are 
stored in /depot/itap/biocontainers/recipes/

Bootstrap: localimage
From: r_4.1.1_rstudio.sif
%post
# update the system and install building essentials
apt-get -y update
apt-get install -y gdal-bin libgdal-dev libudunits2-dev  ## here you install required libraries
# clean up
apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
## Seurat3
Rscript -e "install.packages('Seurat')"
## monocle3
Rscript -e 'if (!requireNamespace("BiocManager", quietly = TRUE))
install.packages("BiocManager")' \
&& Rscript -e "BiocManager::install(c('BiocGenerics', 'DelayedArray', 'DelayedMatrixStats','limma', 
'S4Vectors', 'SingleCellExperiment','SummarizedExperiment', 'batchelor','Matrix.utils'))"
Rscript -e "devtools::install_github('cole-trapnell-lab/leidenbase')"
Rscript -e "devtools::install_github('cole-trapnell-lab/monocle3’)”

Cluster user guide 
Singularity section contains instructions for using Singularity on RCAC clusters.
Biocontainer collection section contains instructions and examples for running 
bioinformatic containers.   
Email
rcac-help@purdue.edu is our email support address. Send us an email any time. 
Coffee hour consultations
In response to COVID-19, we are temporarily switching all our Coffee Hour 
Consultations to online only (https://www.rcac.purdue.edu/coffee). We offer several slots 
(2:00 to 3:30pm) each afternoon (Monday to Thursday) for private one-on-one 
consultations or questions of up to 30 minutes.
Additional bioinformatic tools
Contact me (zhan4429@purdue.edu) or Lev (lev@purdue.edu), if you want additional 
software added into RCAC biocontainers.

### introduction.md
*Source file:* `introduction.md`  ·  *type:* md

---
title: "Introduction"
teaching: 10
exercises: 3
---

:::::::::::::::::::::::::::::::::::::: questions 

- Why QGIS?
- How to start QGIS on HPC Clusters?
- How to load and visualize data in QGIS?
- How to process and export data in QGIS?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Explain why we should use QGIS
- Demonstrate how to start QGIS on HPC Clusters
- Demonstrate how to load and visualize data in QGIS
- Demonstrate how to process and export data in QGIS

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction to QGIS

GIS stands for ‘Geographical Information System’. We can use a GIS application, such as ArcGIS and QGIS to manipulate spatial information. 

QGIS is a free and open-source software that runs on various operating systems. It offers a wide range of functionality, such as vector and raster analysis, geoprocessing, geocoding, georeferencing, web mapping, and 3D visualization. QGIS also supports many data formats and standards, such as Shapefile, GeoTIFF, GeoJSON, WMS, WFS, and PostGIS.

Why QGIS? It's free and flexible.

 1. Cost-free: Enjoy QGIS without any financial burden. It's completely free, no hidden fees.
 2. Free as in "Do It Your Way": You could extend QGIS to meet your specific needs, sponsor development or contribute your own code.
 3. Works where you work: Run QGIS on macOS, Windows, and Linux (so available for HPC Clusters). 
 4. Always getting better: Benefit from rapid development because anyone can add new features and improve on existing ones.
 6. Never get stuck: Access extensive documentation and a large and active supportive community is there for help. 
 7. Easily integrate Artificial Intelligence (AI) and GeoAI.

## Open QGIS on Clusters

We can start QGIS via ThinLinc Client or Gateway. 

#### 1. Start QGIS via ThinLinc

Follow up with [the Setup page](https://rcac-geo.github.io/workshop-qgis/index.html#software-setup), and connect with ThinLinc. There are two ways to start QGIS via ThinLinc. The two ways are fundamentally the same but one is interactive, and the other is typing code.

##### (1) Interactive Way

To open QGIS as an interactive job, we could go to "Cluster Software" and select "QGIS", as the figure below:

<img width="391" alt="Picture1" src="https://github.com/user-attachments/assets/1df48747-d717-442e-9af5-c25d4dc9f78d" />

Then select the "workshop" queue as below:

<img width="406" alt="Screenshot 2025-02-24 at 4 15 16 PM" src="https://github.com/user-attachments/assets/72d72419-4484-4e6e-9fed-3ec2fdf4920d" />

Then hit "No":

<img width="529" alt="Screenshot 2025-02-24 at 4 15 41 PM" src="https://github.com/user-attachments/assets/e3ea5e98-e83e-4d77-ba9c-bba7c62fbea3" />

Now input two cores and five minutes and hit Okay. You don't need to specifically request memory because memory will be relocated proportional with cores. But if you do, include unit such as "4G".

<img width="608" alt="Screenshot 2025-02-24 at 4 16 10 PM" src="https://github.com/user-attachments/assets/55a2b0be-3bc1-447c-a44d-04c4ec6a7e60" />

##### (2) Typing Code Way

We could start the Terminal as below:

<img width="186" alt="Screenshot 2025-02-25 at 9 51 03 AM" src="https://github.com/user-attachments/assets/c06429f8-15b6-4242-b416-080085cf8f23" />

To look up QGIS module, we could do:

```sh
module spider qgis
```

To start an interactive job and open QGIS:

```sh
sinteractive -A workshop -N1 -c8 -t8:00:00
module load qgis
qgis
```



#### 2. Start QGIS via Gateway

Gateway, also named Open OnDemand, is a Web interface includes file explorer, interactive apps including QGIS.​ We have to use our own accounts to login Gateway, not the training accounts we used for this workshop. 
Go to [Negishi Gateway](https://gateway.negishi.rcac.purdue.edu), login with our purdue accounts (when we have account on Clusters) and connect QGIS as the figure below.

<img width="911" alt="Screenshot 2025-02-25 at 10 05 05 AM" src="https://github.com/user-attachments/assets/f575bf3a-e6bd-468b-92ad-4a3b93405788" />


::::::::::::::::::::::::::::::::::::: callout

We could also open QGIS with Gateway, in the [Typing Code Way](https://rcac-geo.github.io/workshop-qgis/introduction.html#typing-code-way). We could start a terminal as below.

![Start Terminal in Gateway](https://github.com/user-attachments/assets/aac3d529-c726-4793-b3db-e90e55a260fc)


::::::::::::::::::::::::::::::::::::::::::::::::


## View Spatial Data

In Geographic Information Systems (GIS), data is primarily represented in two fundamental formats: vector and raster.

#### Vector Data

* Representation:
   - Vector data uses geometric objects—points, lines, and polygons—to represent spatial features.
   - Points represent individual locations (e.g., a city, a tree).
   - Lines represent linear features (e.g., roads, rivers).
   - Polygons represent areas (e.g., lakes, buildings, administrative boundaries).   
* Characteristics:
  - Precision: Vector data is excellent for representing discrete features with clear boundaries, offering high precision.
  - Scalability: Vector data can be scaled up or down without losing quality.
  - Data Storage: Typically, vector data requires less storage space than raster data for representing discrete features.
  - Use Cases: Best suited for representing features with distinct boundaries, such as roads, property lines, and political boundaries.
* Vector File Types:
  - Shapefile (.shp): A very common geospatial vector data format for GIS software. It actually consists of several files (.shp, .shx, .dbf, etc.)
  - GeoJSON (.geojson): A popular open standard format that uses JavaScript Object Notation (JSON) to represent geographic features.
  - KML/KMZ: Used by Google Earth for displaying geographic data.
  - File format is handled by GDAL/OGR package with a [full list](https://gdal.org/en/stable/drivers/vector/)



#### Raster Data

* Representation:
  - Raster data represents spatial information as a grid of cells (pixels). Each cell contains a value representing a specific attribute (e.g., elevation, temperature, land cover).   
* Characteristics:
  - Continuous Data: Raster data is ideal for representing continuous attributes, such as elevation, temperature, and satellite imagery.
  - Data Storage: Raster data can require significant storage space, especially at high resolutions.
  - Analysis: Raster data is well-suited for spatial analysis involving calculations and modeling.
  - Use Cases: Best suited for representing continuous surfaces, such as elevation models, satellite imagery, and aerial photographs.
* Raster File Types:
  - TIFF: Basic image format, no geographic information.
  - GeoTIFF: A TIFF file with added geospatial metadata, enabling it to be used in GIS applications.
  - COG (Cloud Optimized GeoTIFF): A type of GeoTIFF with a specific data structure optimized for fast access in cloud environments, often using tiled data storage.
  - File format is handled by GDAL/OGR package with a [full list](https://gdal.org/en/stable/drivers/raster/)
 
#### Key Differences 

* Structure: Vector data uses geometric shapes, while raster data uses a grid of cells.
* Data Type: Vector is for discrete features, raster is for continuous phenomena.
* Precision: Vector is generally more precise, while raster's precision depends on cell size.
* Storage: Vector often uses less storage for discrete features. Raster data storage size is heavily dependant on resolution.

#### Load Spatial Data
##### (1) Load vector data from files
* Step1: Layer -> Add Layer -> Add Vector Layer
  
<img width="554" alt="Picture2" src="https://github.com/user-attachments/assets/58bc28a8-7fe8-4dfd-8a54-495dbbfe1e6d" />

* Step2: Input your path of "alaska.shp" and hit "add"
  
![](https://github.com/user-attachments/assets/b68a9319-68f0-4502-9bb5-d3d6b87b33d0)

* Step 3: You will see the shapefile has been added to Layers as below.

![](https://github.com/user-attachments/assets/c5ba1734-88ee-4cc8-a79c-dd2f2b0cb1fb)


::::::::::::::::::::::::::::::::::::: challenge 
## Challenge 1: Try yourself
try yourself to add airports.shp to layers.

:::::::::::::::::::::::: solution 

<img width="613" alt="Picture3" src="https://github.com/user-attachments/assets/f4d958c0-3acb-42a9-855e-4505cbca2c04" />

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: callout

When adding a data source, QGIS attempts to identify its Coordinate Reference System (CRS) from sources like a shapefile's .prj file. If no CRS information is found, QGIS prompts you to specify it. You can modify this behavior in Settings -> Options -> CRS to automatically assign either the project's CRS or a designated default CRS. (Graser et al., 2017)

::::::::::::::::::::::::::::::::::::::::::::::::

##### (2) Load CSV files
* Step 1: Layer -> Add Layer -> Add Delimited Text Layer 
* Step 2: Make changes as the red box in the picture below.

<img width="893" alt="Screenshot 2025-02-25 at 2 41 23 PM" src="https://github.com/user-attachments/assets/4ccee5c6-a3d0-4292-8751-04b044d875b0" />


* Step 3: You will see the shapefile has been added to Layers as below.
  
<img width="612" alt="Picture4" src="https://github.com/user-attachments/assets/db0dd043-5c42-48c2-b929-c48f24f010b6" />

##### (3) Load Raster files
* Step1: Layer -> Add Layer -> Add Raster Layer
* Step2: Input your path of "landcover.img" and hit "add"

![](https://github.com/user-attachments/assets/6566ea7f-8ca9-4def-96b3-ae16671039bf)

* Step 3: You will see the raster has been added to Layers as below.

<img width="428" alt="Picture5" src="https://github.com/user-attachments/assets/a849f162-7ad8-473b-a1e3-d6ad34a82e31" />

::::::::::::::::::::::::::::::::::::: challenge 
## Challenge 1: Try yourself
try yourself to add SR_50M_alaska_nad.tif (Hillshade GeoTiff) to layers.

:::::::::::::::::::::::: solution 

![](https://github.com/user-attachments/assets/e10386e9-d1c0-4736-8b9e-6618cf1a5db4)

:::::::::::::::::::::::::::::::::
## Challenge 2: A Question?

Did you find anything weird about the Hillshade image showing above?

:::::::::::::::::::::::: solution 

Yep, the hillshade should be in the North instead of the South. Let's check data Properties and change looking.

![](https://github.com/user-attachments/assets/ff8ff053-8a82-4335-a06d-e4086adb8986)

![](https://github.com/user-attachments/assets/67208203-a4ac-40c6-838f-8fe9d0a3ae10)

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

## Process Spatial Data
#### Filter Vector Data

Scenario: My Grandma wants to have a trip in Alaska but doctor said she shouldn't go to places with high elevation due to the heart problem. So I will find airports with low elevantion for her. For example, I found the airport with elevation lower than 1000 ft.

Solution: 

* Step1: Right click the data "airports" and select "Filter"

![](https://github.com/user-attachments/assets/b330ca5e-42e5-4d01-b587-4e74762b0375)


* Step2: Select "ELEV" from "Fields", and input the Specific Filter Expression as below:

![](https://github.com/user-attachments/assets/98e26b3a-6329-41eb-b769-3cb38434cce5)

* Step3: Hit "OK" and now only airport with elevation lower than 1000 ft show up.
* Step4-Export data: right click the data and selelct "Export" -> "Save Features As". Input information as figure below and hit "OK".

![](https://github.com/user-attachments/assets/5be55894-3ede-42bd-a888-36efda92b202)
  
#### Raster Calculation

Scenario: I'd like find some sunny slope where my Grandma and I can go skiing. So I found the places where Hillshade is smaller than 100, for example.

Solution:

* Step1: Turn on the Processing Toolbox if it's off, and Search "Raster Calculator".

![](https://github.com/user-attachments/assets/fb3965b0-0754-4f43-b7af-d9f30a4c1ac4)
![](https://github.com/user-attachments/assets/26b8ed3a-0484-4c83-be15-a50e89d9c5b9)


* Step2: Input the "Input Layers", "Expression", "Output CRS", and "Calculated" as the Output file.

![](https://github.com/user-attachments/assets/50d49743-2cb9-466a-806e-a077f31629d0)


* Step3: Hit "Run" and change the looking of output.

![](https://github.com/user-attachments/assets/a6e51da6-479c-4008-ad97-05333452897d)

* You have already written out the output file. But if you didn't, you could always export the data via right clicking it and select "Export" -> "Save As". Then input information as figure below and hit "OK".

![](https://github.com/user-attachments/assets/8074e204-dc55-4533-af9b-0dc1e85fc0d0)

  
::::::::::::::::::::::::::::::::::::: keypoints 

- QGIS is a free and open-source software that runs on various platforms, such as Windows, Mac, and Linux.
- QGIS has a large and active community of users and developers who contribute to its features, plugins, documentation, and support. 
- We can use QGIS via ThinLinc Client or Gateway on HPC Clusters. 
- We learned how to load and visualize vector and raster data.
- We learned how to process data and export them.

::::::::::::::::::::::::::::::::::::::::::::::::

## Image text (OCR)

### `Website_new.png`
RESEARCH COMPUTING
CYBERINFRASTRUCTURE SYMPOSIUM

### `Website_new.png`
RESEARCH COMPUTING
CYBERINFRASTRUCTURE SYMPOSIUM

## Fetched resources (external URLs)

### MakeIDeploy? (link)
*URL:* https://makeideploy.today/?tz=US%2FEast-Indiana

Make I Deploy Today?
Follow flow 🌊
Press
Space
or
Click Mouse
👆
Share:
Facebook
Twitter
Source
:
Github
Timezone
:
Wetin be your Timezone
Africa/Abidjan
Africa/Accra
Africa/Addis_Ababa
Africa/Algiers
Africa/Asmara
Africa/Asmera
Africa/Bamako
Africa/Bangui
Africa/Banjul
Africa/Bissau
Africa/Blantyre
Africa/Brazzaville
Africa/Bujumbura
Africa/Cairo
Africa/Casablanca
Africa/Ceuta
Africa/Conakry
Africa/Dakar
Africa/Dar_es_Salaam
Africa/Djibouti
Africa/Douala
Africa/El_Aaiun
Africa/Freetown
Africa/Gaborone
Africa/Harare
Africa/Johannesburg
Africa/Juba
Africa/Kampala
Africa/Khartoum
Africa/Kigali
Africa/Kinshasa
Africa/Lagos
Africa/Libreville
Africa/Lome
Africa/Luanda
Africa/Lubumbashi
Africa/Lusaka
Africa/Malabo
Africa/Maputo
Africa/Maseru
Africa/Mbabane
Africa/Mogadishu
Africa/Monrovia
Africa/Nairobi
Africa/Ndjamena
Africa/Niamey
Africa/Nouakchott
Africa/Ouagadougou
Africa/Porto-Novo
Africa/Sao_Tome
Africa/Timbuktu
Africa/Tripoli
Africa/Tunis
Africa/Windhoek
America/Adak
America/Anchorage
America/Anguilla
America/Antigua
America/Araguaina
America/Argentina/Buenos_Aires
America/Argentina/Catamarca
America/Argentina/ComodRivadavia
America/Argentina/Cordoba
America/Argentina/Jujuy
America/Argentina/La_Rioja
America/Argentina/Mendoza
America/Argentina/Rio_Gallegos
America/Argentina/Salta
America/Argentina/San_Juan
America/Argentina/San_Luis
America/Argentina/Tucuman
America/Argentina/Ushuaia
America/Aruba
America/Asuncion
America/Atikokan
America/Atka
America/Bahia
America/Bahia_Banderas
America/Barbados
America/Belem
America/Belize
America/Blanc-Sablon
America/Boa_Vista
America/Bogota
America/Boise
America/Buenos_Aires
America/Cambridge_Bay
America/Campo_Grande
America/Cancun
America/Caracas
America/Catamarca
America/Cayenne
America/Cayman
America/Chicago
America/Chihuahua
America/Coral_Harbour
America/Cordoba
America/Costa_Rica
America/Creston
America/Cuiaba
America/Curacao
America/Danmarkshavn
America/Dawson
America/Dawson_Creek
America/Denver
America/Detroit
America/Dominica
America/Edmonton
America/Eirunepe
America/El_Salvador
America/Ensenada
America/Fort_Nelson
America/Fort_Wayne
America/Fortaleza
America/Glace_Bay
America/Godthab
America/Goose_Bay
America/Grand_Turk
America/Grenada
America/Guadeloupe
America/Guatemala
America/Guayaquil
America/Guyana
America/Halifax
America/Havana
America/Hermosillo
America/Indiana/Indianapolis
America/Indiana/Knox
America/Indiana/Marengo
America/Indiana/Petersburg
America/Indiana/Tell_City
America/Indiana/Vevay
America/Indiana/Vincennes
America/Indiana/Winamac
America/Indianapolis
America/Inuvik
America/Iqaluit
America/Jamaica
America/Jujuy
America/Juneau
America/Kentucky/Louisville
America/Kentucky/Monticello
America/Knox_IN
America/Kralendijk
America/La_Paz
America/Lima
America/Los_Angeles
America/Louisville
America/Lower_Princes
America/Maceio
America/Managua
America/Manaus
America/Marigot
America/Martinique
America/Matamoros
America/Mazatlan
America/Mendoza
America/Menominee
America/Merida
America/Metlakatla
America/Mexico_City
America/Miquelon
America/Moncton
America/Monterrey
America/Montevideo
America/Montreal
America/Montserrat
America/Nassau
America/New_York
America/Nipigon
America/Nome
America/Noronha
America/North_Dakota/Beulah
America/North_Dakota/Center
America/North_Dakota/New_Salem
America/Ojinaga
America/Panama
America/Pangnirtung
America/Paramaribo
America/Phoenix
America/Port-au-Prince
America/Port_of_Spain
America/Porto_Acre
America/Porto_Velho
America/Puerto_Rico
America/Punta_Arenas
America/Rainy_River
America/Rankin_Inlet
America/Recife
America/Regina
America/Resolute
America/Rio_Branco
America/Rosario
America/Santa_Isabel
America/Santarem
America/Santiago
America/Santo_Domingo
America/Sao_Paulo
America/Scoresbysund
America/Shiprock
America/Sitka
America/St_Barthelemy
America/St_Johns
America/St_Kitts
America/St_Lucia
America/St_Thomas
America/St_Vincent
America/Swift_Current
America/Tegucigalpa
America/Thule
America/Thunder_Bay
America/Tijuana
America/Toronto
America/Tortola
America/Vancouver
America/Virgin
America/Whitehorse
America/Winnipeg
America/Yakutat
America/Yellowknife
Antarctica/Casey
Antarctica/Davis
Antarctica/DumontDUrville
Antarctica/Macquarie
Antarctica/Mawson
Antarctica/McMurdo
Antarctica/Palmer
Antarctica/Rothera
Antarctica/South_Pole
Antarctica/Syowa
Antarctica/Troll
Antarctica/Vostok
Arctic/Longyearbyen
Asia/Aden
Asia/Almaty
Asia/Amman
Asia/Anadyr
Asia/Aqtau
Asia/Aqtobe
Asia/Ashgabat
Asia/Ashkhabad
Asia/Atyrau
Asia/Baghdad
Asia/Bahrain
Asia/Baku
Asia/Bangkok
Asia/Barnaul
Asia/Beirut
Asia/Bishkek
Asia/Brunei
Asia/Calcutta
Asia/Chita
Asia/Choibalsan
Asia/Chongqing
Asia/Chungking
Asia/Colombo
Asia/Dacca
Asia/Damascus
Asia/Dhaka
Asia/Dili
Asia/Dubai
Asia/Dushanbe
Asia/Famagusta
Asia/Gaza
Asia/Harbin
Asia/Hebron
Asia/Ho_Chi_Minh
Asia/Hong_Kong
Asia/Hovd
Asia/Irkutsk
Asia/Istanbul
Asia/Jakarta
Asia/Jayapura
Asia/Jerusalem
Asia/Kabul
Asia/Kamchatka
Asia/Karachi
Asia/Kashgar
Asia/Kathmandu
Asia/Katmandu
Asia/Khandyga
Asia/Kolkata
Asia/Krasnoyarsk
Asia/Kuala_Lumpur
Asia/Kuching
Asia/Kuwait
Asia/Macao
Asia/Macau
Asia/Magadan
Asia/Makassar
Asia/Manila
Asia/Muscat
Asia/Nicosia
Asia/Novokuznetsk
Asia/Novosibirsk
Asia/Omsk
Asia/Oral
Asia/Phnom_Penh
Asia/Pontianak
Asia/Pyongyang
Asia/Qatar
Asia/Qyzylorda
Asia/Rangoon
Asia/Riyadh
Asia/Saigon
Asia/Sakhalin
Asia/Samarkand
Asia/Seoul
Asia/Shanghai
Asia/Singapore
Asia/Srednekolymsk
Asia/Taipei
Asia/Tashkent
Asia/Tbilisi
Asia/Tehran
Asia/Tel_Aviv
Asia/Thimbu
Asia/Thimphu
Asia/Tokyo
Asia/Tomsk
Asia/Ujung_Pandang
Asia/Ulaanbaatar
Asia/Ulan_Bator
Asia/Urumqi
Asia/Ust-Nera
Asia/Vientiane
Asia/Vladivostok
Asia/Yakutsk
Asia/Yangon
Asia/Yekaterinburg
Asia/Yerevan
Atlantic/Azores
Atlantic/Bermuda
Atlantic/Canary
Atlantic/Cape_Verde
Atlantic/Faeroe
Atlantic/Faroe
Atlantic/Jan_Mayen
Atlantic/Madeira
Atlantic/Reykjavik
Atlantic/South_Georgia
Atlantic/St_Helena
Atlantic/Stanley
Australia/ACT
Australia/Adelaide
Australia/Brisbane
Australia/Broken_Hill
Australia/Canberra
Australia/Currie
Australia/Darwin
Australia/Eucla
Australia/Hobart
Australia/LHI
Australia/Lindeman
Australia/Lord_Howe
Australia/Melbourne
Australia/NSW
Australia/North
Australia/Perth
Australia/Queensland
Australia/South
Australia/Sydney
Australia/Tasmania
Australia/Victoria
Australia/West
Australia/Yancowinna
Brazil/Acre
Brazil/DeNoronha
Brazil/East
Brazil/West
CET
CST6CDT
Canada/Atlantic
Canada/Central
Canada/Eastern
Canada/Mountain
Canada/Newfoundland
Canada/Pacific
Canada/Saskatchewan
Canada/Yukon
Chile/Continental
Chile/EasterIsland
Cuba
EET
EST
EST5EDT
Egypt
Eire
Etc/GMT
Etc/GMT+0
Etc/GMT+1
Etc/GMT+10
Etc/GMT+11
Etc/GMT+12
Etc/GMT+2
Etc/GMT+3
Etc/GMT+4
Etc/GMT+5
Etc/GMT+6
Etc/GMT+7
Etc/GMT+8
Etc/GMT+9
Etc/GMT-0
Etc/GMT-1
Etc/GMT-10
Etc/GMT-11
Etc/GMT-12
Etc/GMT-13
Etc/GMT-14
Etc/GMT-2
Etc/GMT-3
Etc/GMT-4
Etc/GMT-5
Etc/GMT-6
Etc/GMT-7
Etc/GMT-8
Etc/GMT-9
Etc/GMT0
Etc/Greenwich
Etc/UCT
Etc/UTC
Etc/Universal
Etc/Zulu
Europe/Amsterdam
Europe/Andorra
Europe/Astrakhan
Europe/Athens
Europe/Belfast
Europe/Belgrade
Europe/Berlin
Europe/Bratislava
Europe/Brussels
Europe/Bucharest
Europe/Budapest
Europe/Busingen
Europe/Chisinau
Europe/Copenhagen
Europe/Dublin
Europe/Gibraltar
Europe/Guernsey
Europe/Helsinki
Europe/Isle_of_Man
Europe/Istanbul
Europe/Jersey
Europe/Kaliningrad
Europe/Kiev
Europe/Kirov
Europe/Lisbon
Europe/Ljubljana
Europe/London
Europe/Luxembourg
Europe/Madrid
Europe/Malta
Europe/Mariehamn
Europe/Minsk
Europe/Monaco
Europe/Moscow
Europe/Nicosia
Europe/Oslo
Europe/Paris
Europe/Podgorica
Europe/Prague
Europe/Riga
Europe/Rome
Europe/Samara
Europe/San_Marino
Europe/Sarajevo
Europe/Saratov
Europe/Simferopol
Europe/Skopje
Europe/Sofia
Europe/Stockholm
Europe/Tallinn
Europe/Tirane
Europe/Tiraspol
Europe/Ulyanovsk
Europe/Uzhgorod
Europe/Vaduz
Europe/Vatican
Europe/Vienna
Europe/Vilnius
Europe/Volgograd
Europe/Warsaw
Europe/Zagreb
Europe/Zaporozhye
Europe/Zurich
GB
GB-Eire
GMT
GMT+0
GMT-0
GMT0
Greenwich
HST
Hongkong
Iceland
Indian/Antananarivo
Indian/Chagos
Indian/Christmas
Indian/Cocos
Indian/Comoro
Indian/Kerguelen
Indian/Mahe
Indian/Maldives
Indian/Mauritius
Indian/Mayotte
Indian/Reunion
Iran
Israel
Jamaica
Japan
Kwajalein
Libya
MET
MST
MST7MDT
Mexico/BajaNorte
Mexico/BajaSur
Mexico/General
NZ
NZ-CHAT
Navajo
PRC
PST8PDT
Pacific/Apia
Pacific/Auckland
Pacific/Bougainville
Pacific/Chatham
Pacific/Chuuk
Pacific/Easter
Pacific/Efate
Pacific/Enderbury
Pacific/Fakaofo
Pacific/Fiji
Pacific/Funafuti
Pacific/Galapagos
Pacific/Gambier
Pacific/Guadalcanal
Pacific/Guam
Pacific/Honolulu
Pacific/Johnston
Pacific/Kiritimati
Pacific/Kosrae
Pacific/Kwajalein
Pacific/Majuro
Pacific/Marquesas
Pacific/Midway
Pacific/Nauru
Pacific/Niue
Pacific/Norfolk
Pacific/Noumea
Pacific/Pago_Pago
Pacific/Palau
Pacific/Pitcairn
Pacific/Pohnpei
Pacific/Ponape
Pacific/Port_Moresby
Pacific/Rarotonga
Pacific/Saipan
Pacific/Samoa
Pacific/Tahiti
Pacific/Tarawa
Pacific/Tongatapu
Pacific/Truk
Pacific/Wake
Pacific/Wallis
Pacific/Yap
Poland
Portugal
ROC
ROK
Singapore
Turkey
UCT
US/Alaska
US/Aleutian
US/Arizona
US/Central
US/East-Indiana
US/Eastern
US/Hawaii
US/Indiana-Starke
US/Michigan
US/Mountain
US/Pacific
US/Pacific-New
US/Samoa
UTC
Universal
W-SU
WET
Zulu
Light
:
🌞
Language
:
PCM
SW
YO
IG
HA
ZU
AM
APIs:
REST
|
Slack
🧩
Extensions:
Chrome
|
Edge

## Non-text files (not extracted)

- `SQL-MindMap.gif` (gif)
