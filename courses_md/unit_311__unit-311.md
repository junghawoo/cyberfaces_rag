---
title: "Unit 311"
unit_id: 311
---

# Unit 311

## Extracted resources (local files)

### field
*Source file:* `Academic HPC Resources and Containers.pdf`  ·  *type:* file

Academic HPC Resources and 
Containers
Christopher Thompson, Jungha Woo
08/05/2025

Academic HPC Services (“your own campus”)
●How campus cluster programs work
●Types of services offered by RCAC, SDSC, TACC, etc

ACCESS (“beyond your campus”)
●Anvil  (list other resources, but highlight is on Anvil)
●Allocation types & process

What Are Containers?
●How they different from regular programs & VMs
●Why use them?  (Reproducibility, portability, etc)

Basics of Running Containers on Anvil
●Simple examples
●Demo of command line operations

What Containers Are Available?
●Some popular examples used by researchers
●Registries like DockerHub, Github registry, Anvil registry, 
etc

Advanced Container Running Examples
●Dockerfiles
●Extending existing containers
●Mounting directories into containers

Running Services with Containers
●What is Kubernetes
●Anvil Composable and Rancher

Questions?

### HPC_Cloud_Anvil_tutorial.pdf
*Source file:* `HPC_Cloud_Anvil_tutorial.pdf`  ·  *type:* pdf

HPC and Cloud Computing on 
Anvil and Containerization 
Basics
Christopher Thompson, Jungha Woo
Purdue University
08/05/2025

Outline
• Research computing in academics
• What are containers, and why should you use them?
• Using containers on the Anvil cluster
• Where to find common containers
• Creating your own containers
• Guest speaker: Iman Haqiqi, HPC and container use case in GLASSNET
2

Academic HPC Services
• Where do you go when you outgrow 
your lab computers?
• HPC:  High Performance Computing  
aka clusters or "super computers"
Data centers
...full of racks
...full of nodes
...full of CPUs
Many users, all sharing these nodes
3

Academic HPC Services
4

Academic HPC Services
• Where do you go for these HPC resources?
• "The Cloud?" (AWS, Azure, GCP, etc)
o $$$ Does your grant have the money? 
"But it's only $0.0017 an hour!"
o Separate cost meters for... compute, storage, 
network transfer, etc
o Can you support your own efforts?  Do you have an 
expert on your team?
o Special needs?  Restricted data (ex: HIPAA)?
Large memory requirements?    $$$$$
• Welcome to... Academic Research Computing!
o Local:  resources & data, support, community
o Simplified costs, sometimes free, usually cheaper
5
vs

Campus Clusters
• Different institutions provide access by:
o"Free" (funded through general IT funds)
o Researchers purchase nodes (Purdue's method)
▪Time-shared. Buy the node, get guaranteed access, share idle time with others.
▪Operating costs (power, staffing, support, etc) covered through this and general funds.
o Billed by usage (similar to commercial clouds, hopefully cheaper...)
• Where to look for it?
o"Research Computing" or "Academic Computing"
o Ask your IT dept
o Ask your own department's IT
6

Academic HPC Services – SSH
• Traditional access method: terminal
• Centrally managed environment
o Installed programs, libraries
o Backups and snapshots
o Monitoring for problems, downtime
• Only small, quick run directly
• Large jobs are scheduled:
o Submit with input files
o Wait in queue for resources
o Scheduled to run... somewhere
o Output returned to user, notified finished
7

Academic HPC Services – Remote Desktops
• Interactive desktop session, via web or remote desktop client
• Leave programs running, reattach later. (but watch out for maintenance!)
8

Academic HPC Services – Web-Based Services
• Web-based HPC access:
oJupyter Notebooks
o Domain-specific gateways
o Open OnDemand
9

ACCESS – HPC for All
• What if your institution doesn't have a research 
computing program?
• The NSF ACCESS Program
o NSF funds computing resources around the country
o Provided free to US researchers & educators
▪https://allocations.access-ci.org/allocations-policy#eligibility
o Submit proposals requesting compute time
o Awarded by committee
• Purdue's Anvil cluster is an ACCESS resource
o 90% of its compute time devoted to users from 
ACCESS program, not just local Purdue researchers
10
https://access-ci.org

Getting Access to ACCESS
• Users are awarded computing resources in 
"allocations" of SUs ("service units")
o Each computing resource decides what 1 SU means to 
them, but generally 1 SU = 1 CPU hour
• Requests are awarded in 4 different levels
o https://allocations.access-ci.org/project-types
• Each level requires more justification (and 
documentation) than the previous tier
• Explore tier allows anyone to try out resources, 
work on testing their code, preparing plan for 
requesting larger allocation and gathering statistics 
for accurate usage at full-scale of simulation
11
https://access-ci.org
Tier 1:  EXPLORE
Tier 2: DISCOVER
Tier 3: ACCELERATE
Tier 4: MAXIMIZE

What Are Containers?
• Containers are a sandboxed environment to package together and 
distribute your programs with everything needed to run them
• How are the different from regular programs?
• Why should you use them in research and academic computing?
12

Traditional Executables
• Code run by operating system directly (also called 
"bare metal")
• Environment (operating system, shared libraries) 
controlled by admins, not normal users
oAt mercy of what admins want to install, or
o Try to compile and maintain your own versions in your 
home directory or scratch space?  Messy!  Fragile!
• Environment is very specific to that computer.
o More your program somewhere else with different 
library versions, everything could break!
13
Computer
Hardware
Kernel
Core OS 
Utilities
Shared 
Libraries
Program 1
Program 2
Program N
...

Virtual Machines (VMs)
• Your code runs inside a simulation of an entire 
computer, even a sim of the hardware
• User gets complete control of environment where 
their code runs
o Install and run anything you want in your VM
• Portability:  give away copies of your VM as an 
"image" that anyone else can run, identical to your 
copy
• Inefficient:  Does your code really need to depend on 
simulating an entire computer?  Does your scientific 
code really need an entire copy of the operating 
system to do its job?
14
Computer
Hardware
Kernel
Core OS 
Utilities
Shared 
Libraries
VM Engine
VM 1
Hardware
Kernel
CoreOS + Libs
P1
P2
P3
VM 2
Hardware
Kernel
CoreOS + Libs
P1
P2
P3

Containers
• Best of both worlds: lightweight while retaining control and 
reproducibility.
• Runs as a normal program on host computer but sandboxed 
from the rest of the files and operating system.
• An engine program (like Docker) is bridge from container to 
host system's kernel, so containers don't need to simulate 
hardware.
• User has control of everything inside the container "image."  
o Packaged with everything they need to run, including core operating 
system utilities, configs, data files, etc.
o Separate filesystem, cannot access files of host computer.
• Can distribute the image for anyone to run the exact same way 
every time on any system.
15
Computer
Hardware
Kernel
Core OS 
Utilities
Shared 
Libraries
P 1
P 2
P N
...
Container 
Engine
Container 1
Container 2
Container N
Utils
& libs
Utils
& libs
Utils
& libs
...

Containers
• User writes a script for exact steps to install and configure 
their program.
• Container is "built" from this blueprint script into an 
"image."
• Every running copy of container uses this image to create 
exact replica of identical environment each time, 
regardless of where it is being run.
• Large community of containers already exist for nearly 
every commonly used software.
• Anyone can "pull" a published container image and be 
running in minutes a complex program or workflow with 
no need to do difficult setup.
16
Container 
definition & 
build files
Ready-to-use 
container images

Why use Containers?
• Portability:
o Develop your code on your own machine
o"Containerize" it, run exact same setup everywhere
o Grad students and lab assistants stay in sync
o Start using your code on new environments like HPC 
quickly, no friction from locally installed dependencies
• Reproducibility:
o Publish your container image, and anyone can run 
your exact code in the exact environment to recreate 
your experiments
o Publish your container definition file (ex: Dockerfile) 
and anyone can build upon your work to make their 
own version, collaborate with your lab.
17
Download 
container to 
other computers

Container Systems
• Containers have been around for decades, a core 
feature of Linux to compartmentalize programs (LXC)
• Only became widely popular in recent years because 
of success of Docker runtime and community
• Can be installed nearly everywhere:
o Windows (with WSL), Macs, Raspberry Pi, etc
• Many other container "engines" now exist:
o Singularity / Apptainer
o podman, containerd
• Docker-style containers are defacto standard, but 
most other engines allow you to download ("pull") 
Docker images into their systems and run them.
18

Docker or Singularity: Which Should I Use?
• Typical Users Should Use:
Docker when:
• Working on personal machines or cloud 
instances
• Building and testing containers locally
• Learning or sharing portable 
environments
• HPC Users Should Use:
Singularity (Apptainer) when:
• Running code on supercomputers, 
academic clusters, or Slurm-based 
schedulers
• Sharing containers with researchers in 
secure multi-user systems
• You don’t have (or shouldn’t have) root 
access
19

20
Use Case
Docker
Singularity (Apptainer)
General users
 Best choice for local 
development, tutorials, and 
standard workloads
 Not commonly needed unless 
targeting HPC or secure 
environments
HPC users
 Often not allowed due to root 
privileges required
 Specifically designed for HPC 
clusters and supercomputers
Root access required?
 Yes — Docker needs root 
privileges (even when running as 
user via docker group)
 No — Singularity runs without 
requiring root, making it secure for 
shared environments
Runs on clusters like 
Slurm/Anvil/Jetstream
 Not directly supported — 
needs extra tools or admin 
support
 Fully supported and often pre-
installed on HPC systems
Security in multi-user systems
 Risky — Docker daemons 
allow privilege escalation
 Secure — Singularity runs as 
the invoking user, no daemon 
involved
File system access (home, 
/scratch, etc.)
 Requires manual volume 
mounting
 Automatically binds common 
directories like $HOME, /scratch
Container hub support
 Docker Hub, GHCR, etc.
 Can pull Docker images 
directly (singularity pull 
docker://...)
Ease of building containers
Easier for building and sharing
 Building containers usually 
requires root, often done on a 
When to Use Docker or Singularity?

Basics of Running Containers on Anvil
Apptainer (formerly Singularity) on Anvil
• Apptainer containers are supported on Anvil 
clusters
• Docker is not allowed due to security restrictions
• No root access needed to run Apptainer containers
• Designed for HPC and secure multi-user 
environments
 Using and Building Containers
• Popular containers (e.g., from NVIDIA NGC) are 
available as pre-installed modules — just load them
• You can also build your own containers
•
 Apptainer can build from Docker images
 You can convert Singularity → Docker, but it’s 
not easy
21

Anvil Open OnDemand
Open OnDemand
• An open-source HPC portal 
• allows users to interact with HPC resources 
through a web browser 
• easily manage files or submit jobs.
• You need to create an ACCESS account at 
https://operations.access-ci.org/identity/new-user 
• Anvil Open OnDemand Guide 
https://www.rcac.purdue.edu/knowledge/anvil/ac
cess/login/ood  
• Anvil Open OnDemand 101 Training 
https://www.rcac.purdue.edu/training/anvil-open-
ondemand-101 
22
https://ondemand.anvil.rcac.purdue.edu/

Accessing Files and Terminal via Open OnDemand
23
Uploading & Downloading Files, and Submitting Jobs
You can upload files from your computer to Anvil, 
and download files from Anvil to your computer.
To submit a job, you can open a Terminal in your 
browser in two ways:
Click “Clusters → Anvil Shell Access”
Or use the “Open in Terminal” button
This Terminal lets you run commands just like a 
regular computer, including submitting your job to run 
on Anvil.

Purdue’s Container Support for ACCESS Users
• Purdue Research Computing has built some of the most popular 
Apptainer containers, making them easy for ACCESS users to use.
• It developed Lmod module support for NGC containers to make high-
performance computing (HPC) more accessible, especially for new 
and educational users via the ACCESS program.
• Purpose
• Simplify the use of NVIDIA GPU-accelerated software
• Reduce the learning curve of tools like Docker and Singularity
• Make AI, ML, and scientific computing software available with a single 
command
24

Purdue Created Lmod Modules for ACCESS Users
25
Benefits for ACCESS Users
No container expertise required — just load like 
any software:
• module load ngc pytorch
Instant access to optimized software: AI 
frameworks like PyTorch, TensorFlow, RAPIDS
Runs securely inside a Singularity container
Home/scratch directories automatically 
mounted
GPU-ready with no extra configuration
Supports batch jobs and interactive sessions on 
clusters like Anvil
Technical Convenience
Purdue maintains pre-tested container 
environments
All dependencies and environment variables are 
handled behind the scenes
Promotes reproducibility and faster onboarding 
for classes, research, and workshops

NGC Containers Available on the Anvil 
• autodock
• chroma
• gamess
• gromacs
• julia
• lammps
• milc
• namd
• nvhpc
• parabricks
• paraview
• pytorch
• qmcpack
• quantum_espresso
• rapidsai
• relion
• tensorflow
• torchani
26

What is Lmod?
• Lmod is a tool that helps you easily load or unload software on a 
shared computing system (like Anvil). Instead of manually editing 
settings like PATH or environment variables, you just run simple 
commands like:
• It adjusts your environment for you — cleanly and safely.
• https://www.rcac.purdue.edu/knowledge/anvil/software/modules
27
module load python

What are NGC Containers?
• NVIDIA NGC offers ready-to-use software containers. These 
containers are like "portable labs" — preloaded with AI tools, 
libraries, and drivers all optimized to run on NVIDIA GPUs. They're 
great for machine learning, data science, and scientific computing.
• NGC Container Environment Modules
Purdue’s system makes it easy to use NGC containers with Lmod modules. You 
don’t need to learn Docker or Singularity commands. Just load the container as 
if it were regular software:
28
module load ngc python

How It Works Behind the Scenes
When you load a module like ngc pytorch, it:
• Starts the container automatically
• Connects your home directory and scratch folders inside the container
• Sets up the environment so you can run code seamlessly
It feels just like you're using software installed on the system — but it's 
actually running inside a secure, pre-built NVIDIA container.
• ngc sets up the container infrastructure (paths, commands, GPU 
support).
• pytorch defines a particular container image and runtime 
configuration to launch it.
29

Three Container-Based Examples
The HPC and Cloud Computing on Anvil module includes the file 
NGC_examples.zip. You can upload this file to your Anvil Home directory and 
follow the provided instructions.
After unzipping the provided archive, navigate to the NGC_examples directory. It 
includes:
1.
Matrix_Multiplication
• Runs PyTorch matrix multiplication using an NGC Docker container
2.
MNIST  digit classification
• Uses an NGC Docker container to perform MNIST digit classification
3.
Buidling an Apptainer for MNIST digit classification
• Builds an Apptainer/Singularity image for MNIST digit classification
• Submit the job with:
 
 
sbatch submit.sh 
• You can also run the image from your local machine
30

Example 1: Matrix Multiplication
31
Matrix_multiply.py
Submit.sh
Matrix Multiply.py does:
•
Device Detection:
Checks if a GPU (CUDA) is 
available and sets it as the 
computation device; 
otherwise, uses the CPU.
•
Matrix Initialization:
Creates two large 
3000×3000 matrices filled 
with random values directly 
on the selected device.
•
Matrix Multiplication:
Performs matrix 
multiplication using 
torch.matmul, leveraging 
GPU acceleration if 
available.
•
Computation Summary:
Prints confirmation, the 
shape of the result matrix, 
and the total sum of all 
values in the output.

Matrix Multiplication Outputs
32
You can submit a job using “sbatch submit.sh” command. 
Final output file name is pytorch-matmul-{Jobid}.out.

SimpleCNN Architecture
Layer
Input Size
Output Size
Notes
Conv2d(1, 32, 3, 1)
28×28×1
26×26×32
No padding, 3x3 kernel
MaxPool2d(2)
26×26×32
13×13×32
Halves spatial dimensions
Conv2d(32, 64, 3, 1)
13×13×32
11×11×64
Another 3x3 conv
MaxPool2d(2)
11×11×64
5×5×64
Halves again
Flatten
-
1600
64 channels × 5 × 5
Linear(1600, 128)
1600
128
Fully connected layer
Linear(128, 10)
128
10
Final logits for 10 classes
33
Concept
What it means
in_channels=1
1 input channel → grayscale image
Conv2d
Learns spatial filters (kernels)
MaxPool2d
Reduces spatial size (downsampling)
Flatten
Converts image tensor to 1D vector
Linear
Fully connected classifier head
Batch size
Defined by DataLoader, not Conv2d

Example 2: Training a Simple CNN on MNIST Digits
 MNIST Digit Classification
A classic task in machine learning: recognizing 
handwritten digits (0–9) from images.
 What is the MNIST Dataset?
•
Stands for Modified National Institute of 
Standards and Technology
•
Contains 70,000 grayscale images of handwritten 
digits
•
Each image is 28×28 pixels
•
Commonly used for:
•
Teaching and learning ML fundamentals
•
Benchmarking classification models
•
Prototyping neural networks
34

Example 2: Training a Simple CNN on MNIST Digits
35
Key concepts we can learn
•
Data loading & normalization 
•
Implementing a simple CNN with Conv, ReLU, Pool 
layers 
•
Training loop: forward pass → loss → backprop → 
optimization 
•
Saving trained model for later inference

Example 2: Training a Simple CNN on MNIST Digits
36
The code downloads the MNIST dataset, trains a convolutional neural network (CNN) for three epochs, 
and evaluates it on a sample image of the digit 7.

Example 2: Test Images and Inference Outputs
37
Input images
Output Predictions
Trained 10 epochs, resize to 28 by 28
Trained 3 epochs, did not resize input image
Trained 1 epoch, did not resize input image
Handwritten on a PowerPoint slide
Handwritten on a PowerPoint slide, black 
background, white text color

Example 3: Creating an Apptainer
38
This builds an Apptainer image based on the NVIDIA Python Docker image. However, the generated
Image is not saved. “—nv” option is to run PyTorch w/ Nvidia GPU support.
•
If no GPU is available and no NVIDIA drivers are present, then: The Singularity fails to find NVIDIA 
tools/libraries and typically encounters an error. 
•
Don’t use –nv on CPU-only hosts. 
This builds an Apptainer image based on the NVIDIA Python Docker image and saves it locally.
More information on Apptainer is available at
https://www.rcac.purdue.edu/knowledge/negishi/run/examples/apps/apptainer

Example 3: Creating an Apptainer
Does building a Singularity (.sif) image from an NGC Docker container require 
Docker Engine, NVIDIA drivers, or NVIDIA Container Toolkit?
• No, you do not need Docker Engine or NVIDIA Container Toolkit on your host to build a .sif 
file from an NGC container using apptainer build.
• But you do need:
• Internet access (to pull from NGC / Docker Hub)
• A working Apptainer/Singularity install
• (Optional) NVIDIA drivers on the execution host only if you plan to use GPU with --nv
Why this works
• apptainer build pytorch.sif docker://nvcr.io/nvidia/pytorch:22.01-py3 does:
• Pull the Docker image layer-by-layer via HTTP (no Docker daemon needed)
• Converts it to a .sif container image
• Resolves environment variables and metadata from the Dockerfile
• All this happens within Apptainer’s user-space, using skopeo and oci-image-
tools internally
39

Submitting an Apptainer Job: Using a Submit File
40
Submitting a Job on the Anvil Cluster
•
Use the submit file to run your Singularity container on Anvil.
•
The output from mnist_train_and_infer.py will be saved in the 
same directory as your submission file.
Before submitting, consider updating:
•
Allocation (project ID)
•
Requested wall time
•
Number of nodes

What Containers Are Available?
Researchers across domains use pre-built containers for speed, reproducibility, and 
ease of setup. Here are some widely used examples:
• NVIDIA NGC
Optimized for AI, ML, and HPC workloads (e.g., PyTorch, TensorFlow, RAPIDS)
• BioContainers
Containers for genomics, proteomics, and other bioinformatics tools
• Neurodocker
Builds containers for neuroimaging tools like FSL, AFNI, FreeSurfer
• GeoDocker
Geospatial analysis tools (e.g., GDAL, GeoServer, PostGIS)
• OpenFOAM
CFD simulation toolkit packaged for easy deployment
• Quantum Chemistry Containers
e.g., Gaussian, ORCA, Q-Chem in supported HPC environments
41

Container Registries: Where Images Live
• Registries store and distribute container images
• They allow you to pull, share, and version containers across systems
Common Examples:
• Docker Hub – Most widely used public registry
• GitHub Container Registry (GHCR) – Integrated with GitHub for CI/CD 
workflows
• NVIDIA NGC – Optimized containers for AI/ML and HPC
• Anvil Registry – Hosts curated containers for the Anvil HPC environment
• Use registries to pull existing images or push your own for reuse and 
collaboration
42

More Resources to Learn About Containers
Comprehensive slides about Docker/Singularity containers on Anvil are 
available at 
• https://www.rcac.purdue.edu/training/containers101 
• What are containers, and why should we use them? 
• Docker and Singularity 
• Singularity basics
• Using containers on RCAC clusters
• Deployed containers on RCAC clusters
• https://www.rcac.purdue.edu/training/biocontainers101
• Deployed biocontainers on RCAC clusters
• Build your biocontainers
43

Creating a New Docker Container
• Dockerfile (or ".def" file for Apptainer)
• A script for:
o Installing dependencies
o Running one-time setup steps
o Copying files into container
o Creating directories, moving files, etc
o Any command needed to setup env
• Each line creates a "layer" upon which the next 
command builds to add new files or modify files 
from earlier layers.
• Define properties like:
o Command to run when it starts
o Ports to open for network programs
o Paths that are expected to be mounted at runtime
44
hello.sh
Dockerfile

Extending Existing Containers
• Found a container you 
like, but just want to add 
a little more?
o Don't reinvent the 
wheel!
• Start Dockerfile with 
"FROM" that uses it as a 
base.
• Your Dockerfile lines just 
add more layers to the 
final container image.
45
Starting with v4.4.2 of the R language as the base, this 
Dockerfile pre-installs a bunch of specific R libraries.

Mounting Files into Docker Containers
• Apptainer automatically includes some common areas (ex: HOME, pwd) at 
runtime for convenience.
• Docker does not mount anything from host computer filesystem by default!
• Two main forms of Docker mounts for dynamic files:
o Bind – a regular directory (or file) from host system
o Volume – a location managed by Docker engine, given a name but user doesn't care 
where it is located
• docker … -v {path or volume name}:{/path/inside/container} …
• --mount and --volume (or -v) arguments at command line
• Apptainer 'mount' options are more complex:  
https://apptainer.org/docs/user/main/bind_paths_and_mounts.html
46

More RCAC Training 
Training Opportunities
For full details, visit: rcac.purdue.edu/training
Anvil Training Sessions:
• Anvil 101
• Anvil Open OnDemand 101
• Containerized Bioinformatics Applications for HPC
• Interactive Computing on the Anvil Composable Subsystem
Purdue Training Sessions:
• Unix 101, Unix 102, Unix 201
• Jupyter Kernels and HPC
• Running Bioinformatics Analyses in HPC
• Open OnDemand 101
47

Thank you!
Questions?
Chris Thompson
thompscs@purdue.edu
Jungha Woo
wooj@purdue.edu

Extra Slides
49

Purdue is Providing ACCESS Resources
50

NVIDIA NGC (NVIDIA Gpu Cloud): What It Provides
51
Format
Source Platform
Who Converts It?
Intended For
Docker
Native format from 
NGC
Provided directly 
by NVIDIA
For users with Docker or 
Kubernetes setups (e.g. 
cloud, desktop)
Singularity 
(.sif)
Not directly 
provided by NVIDIA
You (via apptainer 
build)
For HPC clusters where 
Docker is not allowed (e.g. 
Anvil)
• What NGC Hosts:
• NVIDIA publishes containers as Docker images to nvcr.io
• Example: nvcr.io/nvidia/pytorch:22.01-py3
• You can pull it with Docker:
docker pull nvcr.io/nvidia/pytorch:22.01-py3 
• Or convert it to Singularity format:
apptainer build pytorch22.01.sif docker://nvcr.io/nvidia/pytorch:22.01-py3

Load NGC Container Using Module System
• Lmod 
Lmod is a software tool that enables users to dynamically modify their environment (e.g., 
PATH, environment variables) using module files. 
• NGC Containers
NVIDIA NGC provides pre-built containers with optimized software for various scientific and AI 
workloads.
• NGC Container Environment Modules
These are Lmod modulefiles that enable users to load and unload NGC containers in the same 
manner as they would load any other software package using Lmod. This simplifies the process 
of using containers in HPC workflows.
• How it works
When a user loads an NGC container module, the Lmod system translates this into actions that 
start the container, map necessary directories, and set up the environment within the 
container to match the module's specifications.
52

### HPC_Cloud_Anvil_tutorial.pdf
*Source file:* `HPC_Cloud_Anvil_tutorial.pdf`  ·  *type:* pdf

HPC and Cloud Computing on 
Anvil and Containerization 
Basics
Christopher Thompson, Jungha Woo
Purdue University
08/05/2025

Outline
• Research computing in academics
• What are containers, and why should you use them?
• Using containers on the Anvil cluster
• Where to find common containers
• Creating your own containers
• Guest speaker: Iman Haqiqi, HPC and container use case in GLASSNET
2

Academic HPC Services
• Where do you go when you outgrow 
your lab computers?
• HPC:  High Performance Computing  
aka clusters or "super computers"
Data centers
...full of racks
...full of nodes
...full of CPUs
Many users, all sharing these nodes
3

Academic HPC Services
4

Academic HPC Services
• Where do you go for these HPC resources?
• "The Cloud?" (AWS, Azure, GCP, etc)
o $$$ Does your grant have the money? 
"But it's only $0.0017 an hour!"
o Separate cost meters for... compute, storage, 
network transfer, etc
o Can you support your own efforts?  Do you have an 
expert on your team?
o Special needs?  Restricted data (ex: HIPAA)?
Large memory requirements?    $$$$$
• Welcome to... Academic Research Computing!
o Local:  resources & data, support, community
o Simplified costs, sometimes free, usually cheaper
5
vs

Campus Clusters
• Different institutions provide access by:
o"Free" (funded through general IT funds)
o Researchers purchase nodes (Purdue's method)
▪Time-shared. Buy the node, get guaranteed access, share idle time with others.
▪Operating costs (power, staffing, support, etc) covered through this and general funds.
o Billed by usage (similar to commercial clouds, hopefully cheaper...)
• Where to look for it?
o"Research Computing" or "Academic Computing"
o Ask your IT dept
o Ask your own department's IT
6

Academic HPC Services – SSH
• Traditional access method: terminal
• Centrally managed environment
o Installed programs, libraries
o Backups and snapshots
o Monitoring for problems, downtime
• Only small, quick run directly
• Large jobs are scheduled:
o Submit with input files
o Wait in queue for resources
o Scheduled to run... somewhere
o Output returned to user, notified finished
7

Academic HPC Services – Remote Desktops
• Interactive desktop session, via web or remote desktop client
• Leave programs running, reattach later. (but watch out for maintenance!)
8

Academic HPC Services – Web-Based Services
• Web-based HPC access:
oJupyter Notebooks
o Domain-specific gateways
o Open OnDemand
9

ACCESS – HPC for All
• What if your institution doesn't have a research 
computing program?
• The NSF ACCESS Program
o NSF funds computing resources around the country
o Provided free to US researchers & educators
▪https://allocations.access-ci.org/allocations-policy#eligibility
o Submit proposals requesting compute time
o Awarded by committee
• Purdue's Anvil cluster is an ACCESS resource
o 90% of its compute time devoted to users from 
ACCESS program, not just local Purdue researchers
10
https://access-ci.org

Getting Access to ACCESS
• Users are awarded computing resources in 
"allocations" of SUs ("service units")
o Each computing resource decides what 1 SU means to 
them, but generally 1 SU = 1 CPU hour
• Requests are awarded in 4 different levels
o https://allocations.access-ci.org/project-types
• Each level requires more justification (and 
documentation) than the previous tier
• Explore tier allows anyone to try out resources, 
work on testing their code, preparing plan for 
requesting larger allocation and gathering statistics 
for accurate usage at full-scale of simulation
11
https://access-ci.org
Tier 1:  EXPLORE
Tier 2: DISCOVER
Tier 3: ACCELERATE
Tier 4: MAXIMIZE

What Are Containers?
• Containers are a sandboxed environment to package together and 
distribute your programs with everything needed to run them
• How are the different from regular programs?
• Why should you use them in research and academic computing?
12

Traditional Executables
• Code run by operating system directly (also called 
"bare metal")
• Environment (operating system, shared libraries) 
controlled by admins, not normal users
oAt mercy of what admins want to install, or
o Try to compile and maintain your own versions in your 
home directory or scratch space?  Messy!  Fragile!
• Environment is very specific to that computer.
o More your program somewhere else with different 
library versions, everything could break!
13
Computer
Hardware
Kernel
Core OS 
Utilities
Shared 
Libraries
Program 1
Program 2
Program N
...

Virtual Machines (VMs)
• Your code runs inside a simulation of an entire 
computer, even a sim of the hardware
• User gets complete control of environment where 
their code runs
o Install and run anything you want in your VM
• Portability:  give away copies of your VM as an 
"image" that anyone else can run, identical to your 
copy
• Inefficient:  Does your code really need to depend on 
simulating an entire computer?  Does your scientific 
code really need an entire copy of the operating 
system to do its job?
14
Computer
Hardware
Kernel
Core OS 
Utilities
Shared 
Libraries
VM Engine
VM 1
Hardware
Kernel
CoreOS + Libs
P1
P2
P3
VM 2
Hardware
Kernel
CoreOS + Libs
P1
P2
P3

Containers
• Best of both worlds: lightweight while retaining control and 
reproducibility.
• Runs as a normal program on host computer but sandboxed 
from the rest of the files and operating system.
• An engine program (like Docker) is bridge from container to 
host system's kernel, so containers don't need to simulate 
hardware.
• User has control of everything inside the container "image."  
o Packaged with everything they need to run, including core operating 
system utilities, configs, data files, etc.
o Separate filesystem, cannot access files of host computer.
• Can distribute the image for anyone to run the exact same way 
every time on any system.
15
Computer
Hardware
Kernel
Core OS 
Utilities
Shared 
Libraries
P 1
P 2
P N
...
Container 
Engine
Container 1
Container 2
Container N
Utils
& libs
Utils
& libs
Utils
& libs
...

Containers
• User writes a script for exact steps to install and configure 
their program.
• Container is "built" from this blueprint script into an 
"image."
• Every running copy of container uses this image to create 
exact replica of identical environment each time, 
regardless of where it is being run.
• Large community of containers already exist for nearly 
every commonly used software.
• Anyone can "pull" a published container image and be 
running in minutes a complex program or workflow with 
no need to do difficult setup.
16
Container 
definition & 
build files
Ready-to-use 
container images

Why use Containers?
• Portability:
o Develop your code on your own machine
o"Containerize" it, run exact same setup everywhere
o Grad students and lab assistants stay in sync
o Start using your code on new environments like HPC 
quickly, no friction from locally installed dependencies
• Reproducibility:
o Publish your container image, and anyone can run 
your exact code in the exact environment to recreate 
your experiments
o Publish your container definition file (ex: Dockerfile) 
and anyone can build upon your work to make their 
own version, collaborate with your lab.
17
Download 
container to 
other computers

Container Systems
• Containers have been around for decades, a core 
feature of Linux to compartmentalize programs (LXC)
• Only became widely popular in recent years because 
of success of Docker runtime and community
• Can be installed nearly everywhere:
o Windows (with WSL), Macs, Raspberry Pi, etc
• Many other container "engines" now exist:
o Singularity / Apptainer
o podman, containerd
• Docker-style containers are defacto standard, but 
most other engines allow you to download ("pull") 
Docker images into their systems and run them.
18

Docker or Singularity: Which Should I Use?
• Typical Users Should Use:
Docker when:
• Working on personal machines or cloud 
instances
• Building and testing containers locally
• Learning or sharing portable 
environments
• HPC Users Should Use:
Singularity (Apptainer) when:
• Running code on supercomputers, 
academic clusters, or Slurm-based 
schedulers
• Sharing containers with researchers in 
secure multi-user systems
• You don’t have (or shouldn’t have) root 
access
19

20
Use Case
Docker
Singularity (Apptainer)
General users
 Best choice for local 
development, tutorials, and 
standard workloads
 Not commonly needed unless 
targeting HPC or secure 
environments
HPC users
 Often not allowed due to root 
privileges required
 Specifically designed for HPC 
clusters and supercomputers
Root access required?
 Yes — Docker needs root 
privileges (even when running as 
user via docker group)
 No — Singularity runs without 
requiring root, making it secure for 
shared environments
Runs on clusters like 
Slurm/Anvil/Jetstream
 Not directly supported — 
needs extra tools or admin 
support
 Fully supported and often pre-
installed on HPC systems
Security in multi-user systems
 Risky — Docker daemons 
allow privilege escalation
 Secure — Singularity runs as 
the invoking user, no daemon 
involved
File system access (home, 
/scratch, etc.)
 Requires manual volume 
mounting
 Automatically binds common 
directories like $HOME, /scratch
Container hub support
 Docker Hub, GHCR, etc.
 Can pull Docker images 
directly (singularity pull 
docker://...)
Ease of building containers
Easier for building and sharing
 Building containers usually 
requires root, often done on a 
When to Use Docker or Singularity?

Basics of Running Containers on Anvil
Apptainer (formerly Singularity) on Anvil
• Apptainer containers are supported on Anvil 
clusters
• Docker is not allowed due to security restrictions
• No root access needed to run Apptainer containers
• Designed for HPC and secure multi-user 
environments
 Using and Building Containers
• Popular containers (e.g., from NVIDIA NGC) are 
available as pre-installed modules — just load them
• You can also build your own containers
•
 Apptainer can build from Docker images
 You can convert Singularity → Docker, but it’s 
not easy
21

Anvil Open OnDemand
Open OnDemand
• An open-source HPC portal 
• allows users to interact with HPC resources 
through a web browser 
• easily manage files or submit jobs.
• You need to create an ACCESS account at 
https://operations.access-ci.org/identity/new-user 
• Anvil Open OnDemand Guide 
https://www.rcac.purdue.edu/knowledge/anvil/ac
cess/login/ood  
• Anvil Open OnDemand 101 Training 
https://www.rcac.purdue.edu/training/anvil-open-
ondemand-101 
22
https://ondemand.anvil.rcac.purdue.edu/

Accessing Files and Terminal via Open OnDemand
23
Uploading & Downloading Files, and Submitting Jobs
You can upload files from your computer to Anvil, 
and download files from Anvil to your computer.
To submit a job, you can open a Terminal in your 
browser in two ways:
Click “Clusters → Anvil Shell Access”
Or use the “Open in Terminal” button
This Terminal lets you run commands just like a 
regular computer, including submitting your job to run 
on Anvil.

Purdue’s Container Support for ACCESS Users
• Purdue Research Computing has built some of the most popular 
Apptainer containers, making them easy for ACCESS users to use.
• It developed Lmod module support for NGC containers to make high-
performance computing (HPC) more accessible, especially for new 
and educational users via the ACCESS program.
• Purpose
• Simplify the use of NVIDIA GPU-accelerated software
• Reduce the learning curve of tools like Docker and Singularity
• Make AI, ML, and scientific computing software available with a single 
command
24

Purdue Created Lmod Modules for ACCESS Users
25
Benefits for ACCESS Users
No container expertise required — just load like 
any software:
• module load ngc pytorch
Instant access to optimized software: AI 
frameworks like PyTorch, TensorFlow, RAPIDS
Runs securely inside a Singularity container
Home/scratch directories automatically 
mounted
GPU-ready with no extra configuration
Supports batch jobs and interactive sessions on 
clusters like Anvil
Technical Convenience
Purdue maintains pre-tested container 
environments
All dependencies and environment variables are 
handled behind the scenes
Promotes reproducibility and faster onboarding 
for classes, research, and workshops

NGC Containers Available on the Anvil 
• autodock
• chroma
• gamess
• gromacs
• julia
• lammps
• milc
• namd
• nvhpc
• parabricks
• paraview
• pytorch
• qmcpack
• quantum_espresso
• rapidsai
• relion
• tensorflow
• torchani
26

What is Lmod?
• Lmod is a tool that helps you easily load or unload software on a 
shared computing system (like Anvil). Instead of manually editing 
settings like PATH or environment variables, you just run simple 
commands like:
• It adjusts your environment for you — cleanly and safely.
• https://www.rcac.purdue.edu/knowledge/anvil/software/modules
27
module load python

What are NGC Containers?
• NVIDIA NGC offers ready-to-use software containers. These 
containers are like "portable labs" — preloaded with AI tools, 
libraries, and drivers all optimized to run on NVIDIA GPUs. They're 
great for machine learning, data science, and scientific computing.
• NGC Container Environment Modules
Purdue’s system makes it easy to use NGC containers with Lmod modules. You 
don’t need to learn Docker or Singularity commands. Just load the container as 
if it were regular software:
28
module load ngc python

How It Works Behind the Scenes
When you load a module like ngc pytorch, it:
• Starts the container automatically
• Connects your home directory and scratch folders inside the container
• Sets up the environment so you can run code seamlessly
It feels just like you're using software installed on the system — but it's 
actually running inside a secure, pre-built NVIDIA container.
• ngc sets up the container infrastructure (paths, commands, GPU 
support).
• pytorch defines a particular container image and runtime 
configuration to launch it.
29

Three Container-Based Examples
The HPC and Cloud Computing on Anvil module includes the file 
NGC_examples.zip. You can upload this file to your Anvil Home directory and 
follow the provided instructions.
After unzipping the provided archive, navigate to the NGC_examples directory. It 
includes:
1.
Matrix_Multiplication
• Runs PyTorch matrix multiplication using an NGC Docker container
2.
MNIST  digit classification
• Uses an NGC Docker container to perform MNIST digit classification
3.
Buidling an Apptainer for MNIST digit classification
• Builds an Apptainer/Singularity image for MNIST digit classification
• Submit the job with:
 
 
sbatch submit.sh 
• You can also run the image from your local machine
30

Example 1: Matrix Multiplication
31
Matrix_multiply.py
Submit.sh
Matrix Multiply.py does:
•
Device Detection:
Checks if a GPU (CUDA) is 
available and sets it as the 
computation device; 
otherwise, uses the CPU.
•
Matrix Initialization:
Creates two large 
3000×3000 matrices filled 
with random values directly 
on the selected device.
•
Matrix Multiplication:
Performs matrix 
multiplication using 
torch.matmul, leveraging 
GPU acceleration if 
available.
•
Computation Summary:
Prints confirmation, the 
shape of the result matrix, 
and the total sum of all 
values in the output.

Matrix Multiplication Outputs
32
You can submit a job using “sbatch submit.sh” command. 
Final output file name is pytorch-matmul-{Jobid}.out.

SimpleCNN Architecture
Layer
Input Size
Output Size
Notes
Conv2d(1, 32, 3, 1)
28×28×1
26×26×32
No padding, 3x3 kernel
MaxPool2d(2)
26×26×32
13×13×32
Halves spatial dimensions
Conv2d(32, 64, 3, 1)
13×13×32
11×11×64
Another 3x3 conv
MaxPool2d(2)
11×11×64
5×5×64
Halves again
Flatten
-
1600
64 channels × 5 × 5
Linear(1600, 128)
1600
128
Fully connected layer
Linear(128, 10)
128
10
Final logits for 10 classes
33
Concept
What it means
in_channels=1
1 input channel → grayscale image
Conv2d
Learns spatial filters (kernels)
MaxPool2d
Reduces spatial size (downsampling)
Flatten
Converts image tensor to 1D vector
Linear
Fully connected classifier head
Batch size
Defined by DataLoader, not Conv2d

Example 2: Training a Simple CNN on MNIST Digits
 MNIST Digit Classification
A classic task in machine learning: recognizing 
handwritten digits (0–9) from images.
 What is the MNIST Dataset?
•
Stands for Modified National Institute of 
Standards and Technology
•
Contains 70,000 grayscale images of handwritten 
digits
•
Each image is 28×28 pixels
•
Commonly used for:
•
Teaching and learning ML fundamentals
•
Benchmarking classification models
•
Prototyping neural networks
34

Example 2: Training a Simple CNN on MNIST Digits
35
Key concepts we can learn
•
Data loading & normalization 
•
Implementing a simple CNN with Conv, ReLU, Pool 
layers 
•
Training loop: forward pass → loss → backprop → 
optimization 
•
Saving trained model for later inference

Example 2: Training a Simple CNN on MNIST Digits
36
The code downloads the MNIST dataset, trains a convolutional neural network (CNN) for three epochs, 
and evaluates it on a sample image of the digit 7.

Example 2: Test Images and Inference Outputs
37
Input images
Output Predictions
Trained 10 epochs, resize to 28 by 28
Trained 3 epochs, did not resize input image
Trained 1 epoch, did not resize input image
Handwritten on a PowerPoint slide
Handwritten on a PowerPoint slide, black 
background, white text color

Example 3: Creating an Apptainer
38
This builds an Apptainer image based on the NVIDIA Python Docker image. However, the generated
Image is not saved. “—nv” option is to run PyTorch w/ Nvidia GPU support.
•
If no GPU is available and no NVIDIA drivers are present, then: The Singularity fails to find NVIDIA 
tools/libraries and typically encounters an error. 
•
Don’t use –nv on CPU-only hosts. 
This builds an Apptainer image based on the NVIDIA Python Docker image and saves it locally.
More information on Apptainer is available at
https://www.rcac.purdue.edu/knowledge/negishi/run/examples/apps/apptainer

Example 3: Creating an Apptainer
Does building a Singularity (.sif) image from an NGC Docker container require 
Docker Engine, NVIDIA drivers, or NVIDIA Container Toolkit?
• No, you do not need Docker Engine or NVIDIA Container Toolkit on your host to build a .sif 
file from an NGC container using apptainer build.
• But you do need:
• Internet access (to pull from NGC / Docker Hub)
• A working Apptainer/Singularity install
• (Optional) NVIDIA drivers on the execution host only if you plan to use GPU with --nv
Why this works
• apptainer build pytorch.sif docker://nvcr.io/nvidia/pytorch:22.01-py3 does:
• Pull the Docker image layer-by-layer via HTTP (no Docker daemon needed)
• Converts it to a .sif container image
• Resolves environment variables and metadata from the Dockerfile
• All this happens within Apptainer’s user-space, using skopeo and oci-image-
tools internally
39

Submitting an Apptainer Job: Using a Submit File
40
Submitting a Job on the Anvil Cluster
•
Use the submit file to run your Singularity container on Anvil.
•
The output from mnist_train_and_infer.py will be saved in the 
same directory as your submission file.
Before submitting, consider updating:
•
Allocation (project ID)
•
Requested wall time
•
Number of nodes

What Containers Are Available?
Researchers across domains use pre-built containers for speed, reproducibility, and 
ease of setup. Here are some widely used examples:
• NVIDIA NGC
Optimized for AI, ML, and HPC workloads (e.g., PyTorch, TensorFlow, RAPIDS)
• BioContainers
Containers for genomics, proteomics, and other bioinformatics tools
• Neurodocker
Builds containers for neuroimaging tools like FSL, AFNI, FreeSurfer
• GeoDocker
Geospatial analysis tools (e.g., GDAL, GeoServer, PostGIS)
• OpenFOAM
CFD simulation toolkit packaged for easy deployment
• Quantum Chemistry Containers
e.g., Gaussian, ORCA, Q-Chem in supported HPC environments
41

Container Registries: Where Images Live
• Registries store and distribute container images
• They allow you to pull, share, and version containers across systems
Common Examples:
• Docker Hub – Most widely used public registry
• GitHub Container Registry (GHCR) – Integrated with GitHub for CI/CD 
workflows
• NVIDIA NGC – Optimized containers for AI/ML and HPC
• Anvil Registry – Hosts curated containers for the Anvil HPC environment
• Use registries to pull existing images or push your own for reuse and 
collaboration
42

More Resources to Learn About Containers
Comprehensive slides about Docker/Singularity containers on Anvil are 
available at 
• https://www.rcac.purdue.edu/training/containers101 
• What are containers, and why should we use them? 
• Docker and Singularity 
• Singularity basics
• Using containers on RCAC clusters
• Deployed containers on RCAC clusters
• https://www.rcac.purdue.edu/training/biocontainers101
• Deployed biocontainers on RCAC clusters
• Build your biocontainers
43

Creating a New Docker Container
• Dockerfile (or ".def" file for Apptainer)
• A script for:
o Installing dependencies
o Running one-time setup steps
o Copying files into container
o Creating directories, moving files, etc
o Any command needed to setup env
• Each line creates a "layer" upon which the next 
command builds to add new files or modify files 
from earlier layers.
• Define properties like:
o Command to run when it starts
o Ports to open for network programs
o Paths that are expected to be mounted at runtime
44
hello.sh
Dockerfile

Extending Existing Containers
• Found a container you 
like, but just want to add 
a little more?
o Don't reinvent the 
wheel!
• Start Dockerfile with 
"FROM" that uses it as a 
base.
• Your Dockerfile lines just 
add more layers to the 
final container image.
45
Starting with v4.4.2 of the R language as the base, this 
Dockerfile pre-installs a bunch of specific R libraries.

Mounting Files into Docker Containers
• Apptainer automatically includes some common areas (ex: HOME, pwd) at 
runtime for convenience.
• Docker does not mount anything from host computer filesystem by default!
• Two main forms of Docker mounts for dynamic files:
o Bind – a regular directory (or file) from host system
o Volume – a location managed by Docker engine, given a name but user doesn't care 
where it is located
• docker … -v {path or volume name}:{/path/inside/container} …
• --mount and --volume (or -v) arguments at command line
• Apptainer 'mount' options are more complex:  
https://apptainer.org/docs/user/main/bind_paths_and_mounts.html
46

More RCAC Training 
Training Opportunities
For full details, visit: rcac.purdue.edu/training
Anvil Training Sessions:
• Anvil 101
• Anvil Open OnDemand 101
• Containerized Bioinformatics Applications for HPC
• Interactive Computing on the Anvil Composable Subsystem
Purdue Training Sessions:
• Unix 101, Unix 102, Unix 201
• Jupyter Kernels and HPC
• Running Bioinformatics Analyses in HPC
• Open OnDemand 101
47

Thank you!
Questions?
Chris Thompson
thompscs@purdue.edu
Jungha Woo
wooj@purdue.edu

Extra Slides
49

Purdue is Providing ACCESS Resources
50

NVIDIA NGC (NVIDIA Gpu Cloud): What It Provides
51
Format
Source Platform
Who Converts It?
Intended For
Docker
Native format from 
NGC
Provided directly 
by NVIDIA
For users with Docker or 
Kubernetes setups (e.g. 
cloud, desktop)
Singularity 
(.sif)
Not directly 
provided by NVIDIA
You (via apptainer 
build)
For HPC clusters where 
Docker is not allowed (e.g. 
Anvil)
• What NGC Hosts:
• NVIDIA publishes containers as Docker images to nvcr.io
• Example: nvcr.io/nvidia/pytorch:22.01-py3
• You can pull it with Docker:
docker pull nvcr.io/nvidia/pytorch:22.01-py3 
• Or convert it to Singularity format:
apptainer build pytorch22.01.sif docker://nvcr.io/nvidia/pytorch:22.01-py3

Load NGC Container Using Module System
• Lmod 
Lmod is a software tool that enables users to dynamically modify their environment (e.g., 
PATH, environment variables) using module files. 
• NGC Containers
NVIDIA NGC provides pre-built containers with optimized software for various scientific and AI 
workloads.
• NGC Container Environment Modules
These are Lmod modulefiles that enable users to load and unload NGC containers in the same 
manner as they would load any other software package using Lmod. This simplifies the process 
of using containers in HPC workflows.
• How it works
When a user loads an NGC container module, the Lmod system translates this into actions that 
start the container, map necessary directories, and set up the environment within the 
container to match the module's specifications.
52

### HPC_Cloud_Anvil_tutorial.pdf
*Source file:* `HPC_Cloud_Anvil_tutorial.pdf`  ·  *type:* pdf

HPC and Cloud Computing on 
Anvil and Containerization 
Basics
Christopher Thompson, Jungha Woo
Purdue University
08/05/2025

Outline
• Research computing in academics
• What are containers, and why should you use them?
• Using containers on the Anvil cluster
• Where to find common containers
• Advanced container examples
• Running services for your users with Kubernetes
• Guest speaker: Iman Haqiqi, Containerization for the GLASSNET
2

Academic HPC Services
• Where do you go when you outgrow 
your lab computers?
• HPC:  High Performance Computing  
aka clusters or "super computers"
Data centers
...full of racks
...full of nodes
...full of CPUs
Many users, all sharing these nodes
3

Academic HPC Services
• Where do you go for these HPC resources?
• "The Cloud?" (AWS, Azure, GCP, etc)
o $$$ Does your grant have the money? 
"But it's only $0.0017 an hour!"
o Separate cost meters for... compute, storage, 
network transfer, etc
o Can you support your own efforts?  Do you have an 
expert on your team?
o Special needs?  Restricted data (ex: HIPAA)?
Large memory requirements?    $$$$$
• Welcome to... Academic Research Computing!
o Local:  resources & data, support, community
o Simplified costs, sometimes free, usually cheaper
4
vs

Academic HPC Services
• HPC on campus through Research Computing
o1 or 2 slides showing different institution models for cluster access
▪Some schools give it out freely from general funds, some schools sell nodes like us, etc
o 1 or 2 slides showing actual types of services
▪SSH, remote desktop, interactive, queues, other services like OOD, gateways
o Brief mentions, not detailed
o Now we know what kind of services exist, 
maybe locally maybe not, 
leads into what is ACCESS...
5

ACCESS – HPC for All
• What if your institution doesn't have a research 
computing program?
• The NSF ACCESS Program
o NSF funds computing resources around the country
o Provided free to US researchers & educators
▪https://allocations.access-ci.org/allocations-policy#eligibility
o Submit proposals requesting compute time
o Awarded by committee
• Purdue's Anvil cluster is an ACCESS resource
o 90% of its compute time devoted to national users from 
ACCESS program, not just local Purdue researchers
6
https://access-ci.org

Getting Access to ACCESS
• Users are awarded computing resources in 
"allocations" of SUs ("service units")
o Each computing resource decides what 1 SU means to 
them, but generally 1 SU = 1 CPU hour
• Requests are awarded in 4 different levels
o https://allocations.access-ci.org/project-types
• Each level requires more justification (and 
documentation) than the previous tier
• Explore tier allows anyone to try out resources, 
work on testing their code, preparing plan for 
requesting larger allocation and gathering statistics 
for accurate usage at full-scale of simulation
7
https://access-ci.org
Tier 1:  EXPLORE
Tier 2: DISCOVER
Tier 3: ACCELERATE
Tier 4: MAXIMIZE

What Are Containers?
• Containers are a sandboxed environment to package together and 
distribute your programs with everything needed to run them
• How are the different from regular programs?
• Why should you use them in research and academic computing?
8

Traditional Executables
• Code run by operating system directly (also called 
"bare metal")
• Environment (operating system, shared libraries) 
controlled by admins, not normal users
oAt mercy of what admins want to install, or
o Try to compile and maintain your own versions in your 
home directory or scratch space?  Messy!  Fragile!
• Environment is very specific to that computer.
o More your program somewhere else with different 
library versions, everything could break!
9
Computer
Hardware
Kernel
Core OS 
Utilities
Shared 
Libraries
Program 1
Program 2
Program N
...

Virtual Machines (VMs)
• Your code runs inside a simulation of an entire 
computer, even a sim of the hardware
• User gets complete control of environment where 
their code runs
o Install and run anything you want in your VM
• Portability:  give away copies of your VM as an 
"image" that anyone else can run, identical to your 
copy
• Inefficient:  Does your code really need to depend on 
simulating an entire computer?  Does your scientific 
code really need an entire copy of the operating 
system to do its job?
10
Computer
Hardware
Kernel
Core OS 
Utilities
Shared 
Libraries
VM Engine
VM 1
Hardware
Kernel
CoreOS + Libs
P1
P2
P3
VM 2
Hardware
Kernel
CoreOS + Libs
P1
P2
P3

Containers
• Best of both worlds: lightweight while retaining control and 
reproducability.
• Runs as a normal program on host computer, but sandboxed 
from the rest of the files and operating system.
• An engine program (like Docker) is bridge from container to 
host system's kernel, so containers don't need to simulate 
hardware.
• User has control of everything inside the container "image."  
o Packaged with everything they need to run, including core operating 
system utilities, configs, data files, etc.
o Separate filesystem, cannot access files of host computer.
• Can distribute the "image" for anyone to run the exact same 
way every time on any system.
11
Computer
Hardware
Kernel
Core OS 
Utilities
Shared 
Libraries
P 1
P 2
P N
...
Container 
Engine
Container 1
Container 2
Container N
Utils
& libs
Utils
& libs
Utils
& libs
...

Containers
• User writes a script for exact steps to install and configure 
their program.
• Container is "built" from this blueprint script into an 
"image."
• Every running copy of container uses this image to create 
exact replica of identical environment each time, 
regardless of where it is being run.
• Large community of containers already exist for nearly 
every commonly used software.
• Anyone can "pull" a published container image and be 
running in minutes a complex program or workflow with 
no need to do difficult setup.
12
Diagram showing flow 
from 
--> writing Dockerfile
--> Building image
--> pushing image
--> pulling image 
(other people)

Why use Containers?
• Portability:
o Develop your code on your own machine
o"Containerize" it, run exact same setup everywhere
o Grad students and lab assistants stay in sync
o Start using your code on new environments like HPC 
quickly, no friction from locally installed dependencies
• Reproducibility:
o Publish your container image, and anyone can run 
your exact code in the exact environment to recreate 
your experiments
o Publish your container definition file (ex: Dockerfile) 
and anyone can build upon your work to make their 
own version, collaborate with your lab.
13
Diagram showing container 
image being shipped from 
local laptop to different 
places like
•
Lab machines
•
HPC cluster
•
Collaborator laptops

Container Systems
• Containers have been around for decades, a core 
feature of Linux to compartmentalize programs (LXC)
• Only became widely popular in recent years because 
of success of Docker runtime and community
• Can be installed nearly everywhere:
o Windows (with WSL), Macs, Raspberry Pi, etc
• Many other container "engines" now exist:
o Singularity / Apptainer
o podman, containerd
• Docker-style containers are defacto standard, but 
most other engines allow you to download ("pull") 
Docker images into their systems and run them.
14

Docker or Singularity: Which Should I Use?
• Typical Users Should Use:
Docker when:
• Working on personal machines or cloud 
instances
• Building and testing containers locally
• Learning or sharing portable 
environments
• HPC Users Should Use:
Singularity (Apptainer) when:
• Running code on supercomputers, 
academic clusters, or Slurm-based 
schedulers
• Sharing containers with researchers in 
secure multi-user systems
• You don’t have (or shouldn’t have) root 
access
15

16
Use Case
Docker
Singularity (Apptainer)
General users
 Best choice for local 
development, tutorials, and 
standard workloads
 Not commonly needed unless 
targeting HPC or secure 
environments
HPC users
 Often not allowed due to root 
privileges required
 Specifically designed for HPC 
clusters and supercomputers
Root access required?
 Yes — Docker needs root 
privileges (even when running as 
user via docker group)
 No — Singularity runs without 
requiring root, making it secure for 
shared environments
Runs on clusters like 
Slurm/Anvil/Jetstream
 Not directly supported — 
needs extra tools or admin 
support
 Fully supported and often pre-
installed on HPC systems
Security in multi-user systems
 Risky — Docker daemons 
allow privilege escalation
 Secure — Singularity runs as 
the invoking user, no daemon 
involved
File system access (home, 
/scratch, etc.)
 Requires manual volume 
mounting
 Automatically binds common 
directories like $HOME, /scratch
Container hub support
 Docker Hub, GHCR, etc.
 Can pull Docker images 
directly (singularity pull 
docker://...)
Ease of building containers
Easier for building and sharing
 Building containers usually 
requires root, often done on a 
When to Use Docker or Singularity?

Basics of Running Containers on Anvil
Apptainer (formerly Singularity) on Anvil
• Apptainer containers are supported on Anvil 
clusters
• Docker is not allowed due to security restrictions
• No root access needed to run Apptainer containers
• Designed for HPC and secure multi-user 
environments
 Using and Building Containers
• Popular containers (e.g., from NVIDIA NGC) are 
available as pre-installed modules — just load them
• You can also build your own containers
•
 Apptainer can build from Docker images
 You can convert Singularity → Docker, but it’s 
not easy
17

Anvil Open OnDemand
Open OnDemand
• An open-source HPC portal 
• allows users to interact with HPC resources 
through a web browser 
• easily manage files or submit jobs.
• You need to create an ACCESS account at 
https://operations.access-ci.org/identity/new-user 
• Anvil Open OnDemand Guide 
https://www.rcac.purdue.edu/knowledge/anvil/ac
cess/login/ood  
• Anvil Open OnDemand 101 Training 
https://www.rcac.purdue.edu/training/anvil-open-
ondemand-101 
18
https://ondemand.anvil.rcac.purdue.edu/

Accessing Files and Terminal via Open OnDemand
19
Uploading & Downloading Files, and Submitting Jobs
You can upload files from your computer to Anvil, 
and download files from Anvil to your computer.
To submit a job, you can open a Terminal in your 
browser in two ways:
Click “Clusters → Anvil Shell Access”
Or use the “Open in Terminal” button
This Terminal lets you run commands just like a 
regular computer, including submitting your job to run 
on Anvil.

Purdue’s Container Support for ACCESS Users
• Purdue Research Computing has built some of the most popular 
Apptainer containers, making them easy for ACCESS users to use.
• It developed Lmod module support for NGC containers to make high-
performance computing (HPC) more accessible, especially for new 
and educational users via the ACCESS program.
• Purpose
• Simplify the use of NVIDIA GPU-accelerated software
• Reduce the learning curve of tools like Docker and Singularity
• Make AI, ML, and scientific computing software available with a single 
command
20

Purdue Created Lmod Modules for ACCESS Users
21
Benefits for ACCESS Users
No container expertise required — just load like 
any software:
• module load ngc pytorch
Instant access to optimized software: AI 
frameworks like PyTorch, TensorFlow, RAPIDS
Runs securely inside a Singularity container
Home/scratch directories automatically 
mounted
GPU-ready with no extra configuration
Supports batch jobs and interactive sessions on 
clusters like Anvil
Technical Convenience
Purdue maintains pre-tested container 
environments
All dependencies and environment variables are 
handled behind the scenes
Promotes reproducibility and faster onboarding 
for classes, research, and workshops

NGC Containers Available on the Anvil 
• autodock
• chroma
• gamess
• gromacs
• julia
• lammps
• milc
• namd
• nvhpc
• parabricks
• paraview
• pytorch
• qmcpack
• quantum_espresso
• rapidsai
• relion
• tensorflow
• torchani
22

What is Lmod?
• Lmod is a tool that helps you easily load or unload software on a 
shared computing system (like Anvil). Instead of manually editing 
settings like PATH or environment variables, you just run simple 
commands like:
• It adjusts your environment for you — cleanly and safely.
• https://www.rcac.purdue.edu/knowledge/anvil/software/modules
23
module load python

What are NGC Containers?
• NVIDIA NGC offers ready-to-use software containers. These 
containers are like "portable labs" — preloaded with AI tools, 
libraries, and drivers all optimized to run on NVIDIA GPUs. They're 
great for machine learning, data science, and scientific computing.
• NGC Container Environment Modules
Purdue’s system makes it easy to use NGC containers with Lmod modules. You 
don’t need to learn Docker or Singularity commands. Just load the container as 
if it were regular software:
24
module load ngc python

How It Works Behind the Scenes
When you load a module like ngc pytorch, it:
• Starts the container automatically
• Connects your home directory and scratch folders inside the container
• Sets up the environment so you can run code seamlessly
It feels just like you're using software installed on the system — but it's 
actually running inside a secure, pre-built NVIDIA container.
• ngc sets up the container infrastructure (paths, commands, GPU 
support).
• pytorch defines a particular container image and runtime 
configuration to launch it.
25

Three Container-Based Examples
The HPC and Cloud Computing on Anvil module includes the file 
NGC_examples.zip. You can upload this file to your Anvil Home directory and 
follow the provided instructions.
After unzipping the provided archive, navigate to the NGC_examples directory. It 
includes:
1.
Matrix_Multiplication
• Runs PyTorch matrix multiplication using an NGC Docker container
2.
MNIST  digit classification
• Uses an NGC Docker container to perform MNIST digit classification
3.
Buidling an Apptainer for MNIST digit classification
• Builds an Apptainer/Singularity image for MNIST digit classification
• Submit the job with:
 
 
sbatch submit.sh 
• You can also run the image from your local machine
26

Example 1: Matrix Multiplication
27
Matrix_multiply.py
Submit.sh
Matrix Multiply.py does:
•
Device Detection:
Checks if a GPU (CUDA) is 
available and sets it as the 
computation device; 
otherwise, uses the CPU.
•
Matrix Initialization:
Creates two large 
3000×3000 matrices filled 
with random values directly 
on the selected device.
•
Matrix Multiplication:
Performs matrix 
multiplication using 
torch.matmul, leveraging 
GPU acceleration if 
available.
•
Computation Summary:
Prints confirmation, the 
shape of the result matrix, 
and the total sum of all 
values in the output.

Matrix Multiplication Outputs
28
You can submit a job using “sbatch submit.sh” command. 
Final output file name is pytorch-matmul-{Jobid}.out.

Example 2: Training a Simple CNN on MNIST Digits
 MNIST Digit Classification
A classic task in machine learning: recognizing 
handwritten digits (0–9) from images.
 What is the MNIST Dataset?
•
Stands for Modified National Institute of 
Standards and Technology
•
Contains 70,000 grayscale images of handwritten 
digits
•
Each image is 28×28 pixels
•
Commonly used for:
•
Teaching and learning ML fundamentals
•
Benchmarking classification models
•
Prototyping neural networks
29

Example 2: Training a Simple CNN on MNIST Digits
30
Key concepts we can learn
•
Data loading & normalization 
•
Implementing a simple CNN with Conv, ReLU, Pool 
layers 
•
Training loop: forward pass → loss → backprop → 
optimization 
•
Saving trained model for later inference

Example 2: Training a Simple CNN on MNIST Digits
31
The code downloads the MNIST dataset, trains a convolutional neural network (CNN) for three epochs, 
and evaluates it on a sample image of the digit 7.

Example 2: Test Images and Inference Outputs
32
Input images
Output Predictions
Trained 10 epochs, resize to 28 by 28
Trained 3 epochs, did not resize input image
Trained 1 epoch, did not resize input 
image
Handwritten on a PowerPoint slide
Handwritten on a PowerPoint slide, black 
background, white text color

Example 3: Creating an Apptainer
33
This builds an Apptainer image based on the NVIDIA Python Docker image. However, the generated
Image is not saved. “—nv” option is to run PyTorch w/ Nvidia GPU support.
•
If no GPU is available and no NVIDIA drivers are present, then: The Singularity fails to find NVIDIA 
tools/libraries and typically encounters an error. 
•
Don’t use –nv on CPU-only hosts. 
This builds an Apptainer image based on the NVIDIA Python Docker image and saves it locally.
More information on Apptainer is available at
https://www.rcac.purdue.edu/knowledge/negishi/run/examples/apps/apptainer

Example 3: Creating an Apptainer
Does building a Singularity (.sif) image from an NGC Docker container require 
Docker Engine, NVIDIA drivers, or NVIDIA Container Toolkit?
• No, you do not need Docker Engine or NVIDIA Container Toolkit on your host to build a .sif 
file from an NGC container using apptainer build.
• But you do need:
• Internet access (to pull from NGC / Docker Hub)
• A working Apptainer/Singularity install
• (Optional) NVIDIA drivers on the execution host only if you plan to use GPU with --nv
Why this works
• apptainer build pytorch.sif docker://nvcr.io/nvidia/pytorch:22.01-py3 does:
• Pull the Docker image layer-by-layer via HTTP (no Docker daemon needed)
• Converts it to a .sif container image
• Resolves environment variables and metadata from the Dockerfile
• All this happens within Apptainer’s user-space, using skopeo and oci-image-
tools internally
34

Submitting an Apptainer Job: Using a Submit File
35
Submitting a Job on the Anvil Cluster
•
Use the submit file to run your Singularity container on Anvil.
•
The output from mnist_train_and_infer.py will be saved in the same 
directory as your submission file.
Before submitting, consider updating:
•
Allocation (project ID)
•
Requested wall time
•
Number of nodes

What Containers Are Available?
Researchers across domains use pre-built containers for speed, reproducibility, and 
ease of setup. Here are some widely used examples:
• NVIDIA NGC
Optimized for AI, ML, and HPC workloads (e.g., PyTorch, TensorFlow, RAPIDS)
• BioContainers
Containers for genomics, proteomics, and other bioinformatics tools
• Neurodocker
Builds containers for neuroimaging tools like FSL, AFNI, FreeSurfer
• GeoDocker
Geospatial analysis tools (e.g., GDAL, GeoServer, PostGIS)
• OpenFOAM
CFD simulation toolkit packaged for easy deployment
• Quantum Chemistry Containers
e.g., Gaussian, ORCA, Q-Chem in supported HPC environments
36

Container Registries: Where Images Live
• Registries store and distribute container images
• They allow you to pull, share, and version containers across systems
Common Examples:
• Docker Hub – Most widely used public registry
• GitHub Container Registry (GHCR) – Integrated with GitHub for CI/CD 
workflows
• NVIDIA NGC – Optimized containers for AI/ML and HPC
• Anvil Registry – Hosts curated containers for the Anvil HPC environment
• Use registries to pull existing images or push your own for reuse and 
collaboration
37

More Resources to Learn About Containers
Comprehensive slides about Docker/Singularity containers on Anvil are 
available at 
• https://www.rcac.purdue.edu/training/containers101 
• What are containers, and why should we use them? 
• Docker and Singularity 
• Singularity basics
• Using containers on RCAC clusters
• Deployed containers on RCAC clusters
• https://www.rcac.purdue.edu/training/biocontainers101
• Deployed biocontainers on RCAC clusters
• Build your biocontainers
38

Advanced Container Running Examples
• Dockerfiles
• Extending existing containers
• Mounting directories into containers
•
39

Running Services with Containers
• What if you want to run service for users in your domain/community?
oExample: the JupyterHub you used in yesterday's tutorial
• What if you want to scale up lots of copies for big project?
• What is Kubernetes, Anvil Composable, Rancher
• Just a few quick slides with screenshots & practical examples
• A subtle way to end hour with a sales pitch for RSE services...
o ...i.e., we can use our container hosting to get your model / data / whatever 
to users in your domain
40

More RCAC Training 
Training Opportunities
For full details, visit: rcac.purdue.edu/training
Anvil Training Sessions:
• Anvil 101
• Anvil Open OnDemand 101
• Containerized Bioinformatics Applications for HPC
• Interactive Computing on the Anvil Composable Subsystem
Purdue Training Sessions:
• Unix 101, Unix 102, Unix 201
• Jupyter Kernels and HPC
• Running Bioinformatics Analyses in HPC
• Open OnDemand 101
41

Thank you!
Questions?
Chris Thompson
thompscs@purdue.edu
Jungha Woo
wooj@purdue.edu

Extra Slides
43

Purdue is Providing ACCESS Resources
44

NVIDIA NGC (NVIDIA Gpu Cloud): What It Provides
45
Format
Source Platform
Who Converts It?
Intended For
Docker
Native format from 
NGC
Provided directly 
by NVIDIA
For users with Docker or 
Kubernetes setups (e.g. 
cloud, desktop)
Singularity 
(.sif)
Not directly 
provided by NVIDIA
You (via apptainer 
build)
For HPC clusters where 
Docker is not allowed (e.g. 
Anvil)
• What NGC Hosts:
• NVIDIA publishes containers as Docker images to nvcr.io
• Example: nvcr.io/nvidia/pytorch:22.01-py3
• You can pull it with Docker:
docker pull nvcr.io/nvidia/pytorch:22.01-py3 
• Or convert it to Singularity format:
apptainer build pytorch22.01.sif docker://nvcr.io/nvidia/pytorch:22.01-py3

Load NGC Container Using Module System
• Lmod 
Lmod is a software tool that enables users to dynamically modify their environment (e.g., PATH, 
environment variables) using module files. 
• NGC Containers
NVIDIA NGC provides pre-built containers with optimized software for various scientific and AI 
workloads.
• NGC Container Environment Modules
These are Lmod modulefiles that enable users to load and unload NGC containers in the same 
manner as they would load any other software package using Lmod. This simplifies the process 
of using containers in HPC workflows.
• How it works
When a user loads an NGC container module, the Lmod system translates this into actions that 
start the container, map necessary directories, and set up the environment within the container 
to match the module's specifications.
46

SimpleCNN Architecture
Layer
Input Size
Output Size
Notes
Conv2d(1, 32, 3, 1)
28×28×1
26×26×32
No padding, 3x3 kernel
MaxPool2d(2)
26×26×32
13×13×32
Halves spatial dimensions
Conv2d(32, 64, 3, 1)
13×13×32
11×11×64
Another 3x3 conv
MaxPool2d(2)
11×11×64
5×5×64
Halves again
Flatten
-
1600
64 channels × 5 × 5
Linear(1600, 128)
1600
128
Fully connected layer
Linear(128, 10)
128
10
Final logits for 10 classes
47
Concept
What it means
in_channels=1
1 input channel → grayscale image
Conv2d
Learns spatial filters (kernels)
MaxPool2d
Reduces spatial size (downsampling)
Flatten
Converts image tensor to 1D vector
Linear
Fully connected classifier head
Batch size
Defined by DataLoader, not Conv2d

### HPC_Cloud_Anvil_tutorial_07282025-1.pdf
*Source file:* `HPC_Cloud_Anvil_tutorial_07282025-1.pdf`  ·  *type:* pdf

HPC and cloud computing on 
Anvil and containerization 
basics
Christopher Thompson, Jungha Woo
Purdue University

Outline
• Research computing in academics
• What are containers, and why should you use them?
• Using containers on Anvil
• Where to find common containers
• Advanced container examples
• Running services for your users with Kubernetes
• Should we mention GLASSNET 15min talk here, too?
2

Academic HPC Services
• Where do you go when you outgrow your lab computers?
• HPC:   High Performance Computing  (aka, clusters, or "super 
computers")
• "The Cloud?" (AWS, Azure, GCP, etc)
o$$$ Does your grant have the money? "But it's only $0.0017 an hour!"
o Separate cost meters for... compute, storage, network transfer, etc
• Welcome to.... Research Computing!
o Local:  resources & data, support, community
oSimplified costs
3

Academic HPC Services
• Where do you go when you outgrow your lab computers?
oHPC:   High Performance Computing  (aka, clusters, or "super computers")
• "The Cloud?" (AWS, Azure, GCP, etc)
o $$$ Does your grant have the money? "But it's only $0.0017 an hour!"
oSeparate cost meters for... compute, storage, network transfer, etc
• Welcome to.... Research Computing!
o Local:  resources & data, support, community
oSimplified costs
4

Academic HPC Services
• HPC on campus through Research Computing
5

ACCESS (“beyond your campus”)
• Anvil (list other resources, but highlight is on Anvil)
• Allocation types & process
6

What Are Containers?
• How they different from regular programs & VMs
• Why use them? (Reproducibility, portability, etc)
•
7

Basics of Running Containers on Anvil
• Anvil User Guide https://www.rcac.purdue.edu/knowledge/anvil 
• Simple examples
• Demo of command line operations
• NGC Container execution
• Apptainer example on Anvil -to run PyTorch w/ Nvidia GPU support ( Nvidia 
container registry, NGC docker containers) :
• $ apptainer exec --nv docker://nvcr.io/nvidia/pytorch:22.01-py3 python --version
•
•
8

Anvil Open OnDemand ondemand.anvil.rcac.purdue.edu
Open OnDemand
• An open-source HPC portal 
• allows users to interact with 
HPC resources through a 
web browser 
• easily manage files or 
submit jobs.
• Anvil Open OnDemand 
Guide 
https://www.rcac.purdue.ed
u/knowledge/anvil/access/l
ogin/ood  
9

File Browser and Terminal 
10
You can upload files from your local machine to the 
Anvil, and download files from Anvil to your local 
machine.
You can open a Terminal inside the browser. This 
enables you to submit a job from the command line.

NVIDIA NGC: What it Provides
11
Format
Source Platform
Who Converts It?
Intended For
Docker
Native format from 
NGC
Provided directly 
by NVIDIA
For users with Docker or 
Kubernetes setups (e.g. 
cloud, desktop)
Singularity 
(.sif)
Not directly 
provided by NVIDIA
You (via apptainer 
build)
For HPC clusters where 
Docker is not allowed (e.g. 
Anvil)
• What NGC Hosts:
• NVIDIA publishes containers as Docker images to nvcr.io
• Example: nvcr.io/nvidia/pytorch:22.01-py3
• You can pull it with Docker:
docker pull nvcr.io/nvidia/pytorch:22.01-py3 
• Or convert it to Singularity format:
apptainer build pytorch22.01.sif docker://nvcr.io/nvidia/pytorch:22.01-py3

Load NGC Container Using module system
• Lmod 
Lmod is a software tool that enables users to dynamically modify their environment (e.g., PATH, 
environment variables) using module files. 
• NGC Containers
NVIDIA NGC provides pre-built containers with optimized software for various scientific and AI 
workloads.
• NGC Container Environment Modules
These are Lmod modulefiles that enable users to load and unload NGC containers in the same 
manner as they would load any other software package using Lmod. This simplifies the process 
of using containers in HPC workflows.
• How it works
When a user loads an NGC container module, the Lmod system translates this into actions that 
start the container, map necessary directories, and set up the environment within the container 
to match the module's specifications.
12

Example code 
• Unzip the compressed example code 
• NGC_examples directory 
• Matrix_multiplication: Use NGC Docker container for PyTorch matrix 
multiplication code
• MNIST: Use the NGC Docker container for MNIST digit classification 
• Apptainer1: Create an Apptainer/Singularity image for MNIST digit 
classification
• Submit a job using “sbatch submit.sh” from the terminal.
• You can run an Apptainer/Singularity image from your local machine 
13

NGC Container Example 1: Matrix Multiplication
• Module system
• The Anvil cluster utilizes 
Lmod to manage the 
user environment.
• provides users with 
access to the necessary 
software packages and 
versions
• https://www.rcac.purdu
e.edu/knowledge/anvil/s
oftware/modules
• Module load
• Module purge
• To unload all loaded 
modules and reset 
everything to the 
original state.
14

Matrix Multiplication Outputs
15

Example 2: Training a Simple CNN on MNIST Digits
16
MNIST
•
Dataset of 70,000 handwritten digits 
(0–9)
•
Images are 28×28 pixels, grayscale
•
Widely used for teaching, 
benchmarking, and neural network 
experiments
Key Concepts Students Learn
•
Data loading & normalization 
•
Implementing a simple CNN with Conv, ReLU, Pool layers 
•
Training loop: forward pass → loss → backprop → optimization 
•
Saving trained model for later inference

Example 2: Training a Simple CNN on MNIST Digits
17
This code downloads 
the MNIST dataset 
and trains a CNN 
model for three 
epochs.
Then, it tests an 
image of digit seven.

Example 2: Test images and inference outputs
18
Input images
Output Predictions
Trained 10 epochs, resize to 28 by 28
Trained 3 epochs, did not resize input image
Trained 1 epoch, did not resize input image
Handwritten on a PowerPoint slide
Handwritten on a PowerPoint slide, black 
background, white text color

Example 3: Creating an Apptainer
19
This builds an Apptainer image based on the NVIDIA Python Docker image. However, the generated
Image is not saved. “—nv” option is to run PyTorch w/ Nvidia GPU support.
•
If no GPU is available and no NVIDIA drivers are present, then: The Singularity fails to find NVIDIA 
tools/libraries and typically encounters an error. 
•
Don’t use –nv on CPU-only hosts. 
This builds an Apptainer image based on the NVIDIA Python Docker image and saves it locally.
More information on Apptainer is available at
https://www.rcac.purdue.edu/knowledge/negishi/run/examples/apps/apptainer

Example 3: Creating an Apptainer
• Does building a Singularity (.sif) image from an NGC Docker container require 
Docker Engine, NVIDIA drivers, or NVIDIA Container Toolkit?
• No, you do not need Docker Engine or NVIDIA Container Toolkit on your host to build a .sif 
file from an NGC container using apptainer build.
• But you do need:
• Internet access (to pull from NGC / Docker Hub)
• A working Apptainer/Singularity install
• (Optional) NVIDIA drivers on the execution host only if you plan to use GPU with --nv
Why this works
• apptainer build pytorch.sif docker://nvcr.io/nvidia/pytorch:22.01-py3 does:
• Pull the Docker image layer-by-layer via HTTP (no Docker daemon needed)
• Converts it to a .sif container image
• Resolves environment variables and metadata from the Dockerfile
• All this happens within Apptainer’s user-space, using skopeo and oci-image-
tools internally
20

Submit an Apptainer Job: Submit File
21
Use the submit file if you want to execute your Singularity container on 
the Anvil cluster. 
The output of mnist_train_and_infer.py will be generated in the same 
directory as your submission file.
You may want to update 
•
Allocation 
•
Request time
•
Request Node

What Containers Are Available?
• Some popular examples used by researchers
• Registries like DockerHub, Github registry, Anvil registry, etc
•
22

More Resources to Learn About Containers
Comprehensive slides about Docker/Singularity containers on Anvil are 
available at 
• https://www.rcac.purdue.edu/training/containers101 
• What are containers, and why should we use them? 
• Docker and Singularity 
• Singularity basics
• Using containers on RCAC clusters
• Deployed containers on RCAC clusters
• https://www.rcac.purdue.edu/training/biocontainers101
• Deployed biocontainers on RCAC clusters
• Build your biocontainers
23

Advanced Container Running Examples
• Dockerfiles
• Extending existing containers
• Mounting directories into containers
•
24

Running Services with Containers
• What is Kubernetes
• Anvil Composable and Rancher
•
25

Thank you!
Questions?
thompscs@purdue.edu
wooj@purdue.edu

27

SimpleCNN architecture
Layer
Input Size
Output Size
Notes
Conv2d(1, 32, 3, 1)
28×28×1
26×26×32
No padding, 3x3 kernel
MaxPool2d(2)
26×26×32
13×13×32
Halves spatial dimensions
Conv2d(32, 64, 3, 1)
13×13×32
11×11×64
Another 3x3 conv
MaxPool2d(2)
11×11×64
5×5×64
Halves again
Flatten
-
1600
64 channels × 5 × 5
Linear(1600, 128)
1600
128
Fully connected layer
Linear(128, 10)
128
10
Final logits for 10 classes
28
Concept
What it means
in_channels=1
1 input channel → grayscale image
Conv2d
Learns spatial filters (kernels)
MaxPool2d
Reduces spatial size (downsampling)
Flatten
Converts image tensor to 1D vector
Linear
Fully connected classifier head
Batch size
Defined by DataLoader, not Conv2d

### HPC_Cloud_Anvil_tutorial_07282025.pdf
*Source file:* `HPC_Cloud_Anvil_tutorial_07282025.pdf`  ·  *type:* pdf

HPC and cloud computing on 
Anvil and containerization 
basics
Christopher Thompson, Jungha Woo
Purdue University

Academic HPC Services (“your own campus”)
• How campus cluster programs work
• Types of services offered by RCAC, SDSC, TACC, etc
2

ACCESS (“beyond your campus”)
• Anvil (list other resources, but highlight is on Anvil)
• Allocation types & process
3

What Are Containers?
• How they different from regular programs & VMs
• Why use them? (Reproducibility, portability, etc)
•
4

Basics of Running Containers on Anvil
• Anvil User Guide https://www.rcac.purdue.edu/knowledge/anvil 
• Simple examples
• Demo of command line operations
• NGC Container execution
• Apptainer example on Anvil -to run PyTorch w/ Nvidia GPU support ( Nvidia 
container registry, NGC docker containers) :
• $ apptainer exec --nv docker://nvcr.io/nvidia/pytorch:22.01-py3 python --version
•
•
5

Anvil Open OnDemand ondemand.anvil.rcac.purdue.edu
Open OnDemand
• An open-source HPC portal 
• allows users to interact with 
HPC resources through a 
web browser 
• easily manage files or 
submit jobs.
• Anvil Open OnDemand 
Guide 
https://www.rcac.purdue.ed
u/knowledge/anvil/access/l
ogin/ood  
6

NVIDIA NGC: What it Provides
7
Format
Source Platform
Who Converts It?
Intended For
Docker
Native format from 
NGC
Provided directly 
by NVIDIA
For users with Docker or 
Kubernetes setups (e.g. 
cloud, desktop)
Singularity 
(.sif)
Not directly 
provided by NVIDIA
You (via apptainer 
build)
For HPC clusters where 
Docker is not allowed (e.g. 
Anvil)
• What NGC Hosts:
• NVIDIA publishes containers as Docker images to nvcr.io
• Example: nvcr.io/nvidia/pytorch:22.01-py3
• You can pull it with Docker:
docker pull nvcr.io/nvidia/pytorch:22.01-py3 
• Or convert it to Singularity format:
apptainer build pytorch22.01.sif docker://nvcr.io/nvidia/pytorch:22.01-py3

Load NGC Container Using module system
• Lmod 
Lmod is a software tool that enables users to dynamically modify their environment (e.g., PATH, 
environment variables) using module files. 
• NGC Containers
NVIDIA NGC provides pre-built containers with optimized software for various scientific and AI 
workloads.
• NGC Container Environment Modules
These are Lmod modulefiles that enable users to load and unload NGC containers in the same 
manner as they would load any other software package using Lmod. This simplifies the process 
of using containers in HPC workflows.
• How it works
When a user loads an NGC container module, the Lmod system translates this into actions that 
start the container, map necessary directories, and set up the environment within the container 
to match the module's specifications.
8

Example code 
• Unzip the compressed example code 
• NGC_examples directory 
• Matrix_multiplication: Use NGC Docker container for PyTorch matrix 
multiplication code
• MNIST: Use the NGC Docker container for MNIST digit classification 
• Apptainer1: Create an Apptainer/Singularity image for MNIST digit 
classification
• Submit a job using “sbatch submit.sh” from the terminal.
• You can run an Apptainer/Singularity image from your local machine 
9

NGC Container Example 1: Matrix Multiplication
• Module system
• The Anvil cluster utilizes 
Lmod to manage the 
user environment.
• provides users with 
access to the necessary 
software packages and 
versions
• https://www.rcac.purdu
e.edu/knowledge/anvil/s
oftware/modules
• Module load
• Module purge
• To unload all loaded 
modules and reset 
everything to the 
original state.
10

Matrix Multiplication Outputs
11

Example 2: Training a Simple CNN on MNIST Digits
12
MNIST
•
Dataset of 70,000 handwritten digits 
(0–9)
•
Images are 28×28 pixels, grayscale
•
Widely used for teaching, 
benchmarking, and neural network 
experiments
Key Concepts Students Learn
•
Data loading & normalization 
•
Implementing a simple CNN with Conv, ReLU, Pool layers 
•
Training loop: forward pass → loss → backprop → optimization 
•
Saving trained model for later inference

Example 2: Training a Simple CNN on MNIST Digits
13
This code downloads 
the MNIST dataset 
and trains a CNN 
model for three 
epochs.
Then, it tests an 
image of digit seven.

Example 2: Test images and inference outputs
14
Input images
Output Predictions
Trained 10 epochs, resize to 28 by 28
Trained 3 epochs, did not resize input image
Trained 1 epoch, did not resize input image
Handwritten on a PowerPoint slide
Handwritten on a PowerPoint slide, black 
background, white text color

Apptainer Example 1 : Creating an apptainer
15
This builds an Apptainer image based on the NVIDIA Python Docker image. However, the generated
Image is not saved. “—nv” option is to run PyTorch w/ Nvidia GPU support. 
This builds an Apptainer image based on the NVIDIA Python Docker image and saves it locally.
More information on Apptainer is available at
https://www.rcac.purdue.edu/knowledge/negishi/run/examples/apps/apptainer

Apptainer Example 1 : Creating an apptainer
• Does building a Singularity (.sif) image from an NGC Docker container require 
Docker Engine, NVIDIA drivers, or NVIDIA Container Toolkit?
• No, you do not need Docker Engine or NVIDIA Container Toolkit on your host to build a .sif 
file from an NGC container using apptainer build.
• But you do need:
• Internet access (to pull from NGC / Docker Hub)
• A working Apptainer/Singularity install
• (Optional) NVIDIA drivers on the execution host only if you plan to use GPU with --nv
Why this works
• apptainer build pytorch.sif docker://nvcr.io/nvidia/pytorch:22.01-py3 does:
• Pull the Docker image layer-by-layer via HTTP (no Docker daemon needed)
• Converts it to a .sif container image
• Resolves environment variables and metadata from the Dockerfile
• All this happens within Apptainer’s user-space, using skopeo and oci-image-
tools internally
16

Apptainer Example 1 : Submit File
17
Use the submit file if 
you want to execute 
your Singularity 
container on the Anvil 
cluster. 
The output of 
mnist_train_and_infer.p
y will be generated in 
the same directory as 
your submission file.
You may want to 
update 
•
Allocation 
•
Request time
•
Request Node

What Containers Are Available?
• Some popular examples used by researchers
• Registries like DockerHub, Github registry, Anvil registry, etc
•
18

Advanced Container Running Examples
• Dockerfiles
• Extending existing containers
• Mounting directories into containers
•
19

Running Services with Containers
• What is Kubernetes
• Anvil Composable and Rancher
•
20

Thank you!
Questions?
thompscs@purdue.edu
wooj@purdue.edu

22

### HPC_Cloud_Anvil_tutorial_07312025.pdf
*Source file:* `HPC_Cloud_Anvil_tutorial_07312025.pdf`  ·  *type:* pdf

HPC and cloud computing on 
Anvil and containerization 
basics
Christopher Thompson, Jungha Woo
Purdue University

Outline
• Research computing in academics
• What are containers, and why should you use them?
• Using containers on Anvil
• Where to find common containers
• Advanced container examples
• Running services for your users with Kubernetes
• Should we mention GLASSNET 15min talk here, too?
2

Academic HPC Services
• Where do you go when you outgrow 
your lab computers?
• HPC:  High Performance Computing  
aka clusters or "super computers"
o Data centers
...full of racks
...full of nodes
...full of CPUs
oMany users, all sharing these nodes
3

Academic HPC Services
• Where do you go for these HPC resources?
• "The Cloud?" (AWS, Azure, GCP, etc)
o $$$ Does your grant have the money? 
"But it's only $0.0017 an hour!"
o Separate cost meters for... compute, storage, 
network transfer, etc
o Can you support your own efforts?  Do you have an 
expert on your team?
o Special needs?  Restricted data (ex: HIPAA)?
Large memory requirements?    $$$$$
• Welcome to... Academic Research Computing!
o Local:  resources & data, support, community
o Simplified costs, sometimes free, usually cheaper
4
vs

Academic HPC Services
• HPC on campus through Research Computing
o1 or 2 slides showing different institution models for cluster access
▪Some schools give it out freely from general funds, some schools sell nodes like us, etc
o 1 or 2 slides showing actual types of services
▪SSH, remote desktop, interactive, queues, other services like OOD, gateways
o Brief mentions, not detailed
o Now we know what kind of services exist, 
maybe locally maybe not, 
leads into what is ACCESS...
5

ACCESS – HPC for All
• What if your institution doesn't have a research 
computing program?
• The NSF ACCESS Program
o NSF funds computing resources around the country
o Provided free to US researchers & educators
▪https://allocations.access-ci.org/allocations-policy#eligibility
o Submit proposals requesting compute time
o Awarded by committee
• Purdue's Anvil cluster is an ACCESS resource
o 90% of its compute time devoted to national users from 
ACCESS program, not just local Purdue researchers
6
https://access-ci.org

Getting Access to ACCESS
• Users are awarded computing resources in 
"allocations" of SUs ("service units")
o Each computing resource decides what 1 SU means to 
them, but generally 1 SU = 1 CPU hour
• Requests are awarded in 4 different levels
o https://allocations.access-ci.org/project-types
• Each level requires more justification (and 
documentation) than the previous tier
• Explore tier allows anyone to try out resources, 
work on testing their code, preparing plan for 
requesting larger allocation and gathering statistics 
for accurate usage at full-scale of simulation
7
https://access-ci.org
Tier 1:  EXPLORE
Tier 2: DISCOVER
Tier 3: ACCELERATE
Tier 4: MAXIMIZE

What Are Containers?
• Containers are a sandboxed environment to package together and 
distribute your programs with everything needed to run them
• How are the different from regular programs?
• Why should you use them in research and academic computing?
8

Traditional Executables
• Code run by operating system directly (also called 
"bare metal")
• Environment (operating system, shared libraries) 
controlled by admins, not normal users
oAt mercy of what admins want to install, or
o Try to compile and maintain your own versions in your 
home directory or scratch space?  Messy!  Fragile!
• Environment is very specific to that computer.
o More your program somewhere else with different 
library versions, everything could break!
9
Diagram showing layers:
Programs
Core OS + libraries
Kernel
hardware

Virtual Machines (VMs)
• Your code runs inside a simulation of an entire 
computer, even a sim of the hardware
• User gets complete control of environment where 
their code runs
o Install and run anything you want in your VM
• Portability:  give away copies of your VM as an 
"image" that anyone else can run, identical to your 
copy
• Inefficient:  Does your code really need to depend on 
simulating an entire computer?  Does your scientific 
code really need an entire copy of the operating 
system to do its job?
10
Diagram showing layers 
from before but now 
program on host is a 
nested copy (VM):
====== VM ========
Programs
Core OS + libraries
Kernel
Simulated Hardware
==================
Core OS + libaries
Kernel
Real hardware

Containers
• Best of both worlds: lightweight while retaining control 
and reproducability.
• Runs as a normal program on host computer, but 
sandboxed from the rest of the files and operating 
system.
• An "engine" program (like Docker) is bridge from 
container to host system's kernel, so containers don't 
need to simulate hardware.
• User has control of everything inside the container 
"image."  
o Packaged with everything they need to run, including core 
operating system utilities, configs, data files, etc.
• Can distribute the "image" for anyone to run the exact 
same way every time on any system.
11
Diagram showing layers 
with containers nested 
inside host system:
==== container ===
Programs
Core OS + libraries
=================
Container Engine
Kernel
Real hardware

Containers
• User writes a script for exact steps to install and 
configure their program.
• Container is "built" from this blueprint into an 
"image."  Every running copy of container uses this 
image to create exact replica of environment each 
time, regardless of where it is being run.
• Large community of containers already exist for 
nearly every commonly used software.
• Anyone can "pull" a published container image and 
be running in minutes a complex program or 
workflow with no need to do difficult setup.
12
Diagram showing flow 
from 
--> writing Dockerfile
--> Building image
--> pushing image
--> pulling image 
(other people)

Why use Containers?
• Portability:
o Develop your code on your own machine
oContainerize it, run exact same setup everywhere
o Grad students and lab assistants stay in sync
o Start using your code on new environments like HPC 
quickly, no friction from locally installed dependencies
• Reproducability:
o Publish your container image, and anyone can run 
your exact code in the exact environment to recreate 
your experiments
o Publish your container definition file (ex: Dockerfile) 
and anyone can build upon your work to make their 
own version, collaborate with your lab.
13
Diagram showing container 
image being shipped from 
local laptop to different 
places like
•
Lab machines
•
HPC cluster
•
Collaborator laptops

Types of Containers
• Containers have been around for decades, a core 
feature of Linux compartmentalizing programs (LXC)
• Only became widely popular in recent years because 
of success of Docker
• Can be installed nearly everywhere that has a Linux or 
Unix core
o Windows (with WSL), Macs, Raspberry Pi, etc
• Many other container "engines" now exist:
o podman, Singularity / Apptainer, the new thing coming to 
next Mac OS
• Docker-style containers are defacto standard, but 
most other engines allow you to download ("pull") 
Docker images into their systems and run them.
14
Logos over here of 
different systems like 
docker, 
podman, 
apptainer

Basics of Running Containers on Anvil
• Apptainer/Singularity containers can run on Anvil. Docker containers 
are not allowed for security reasons.
• Note: Apptainer was formerly known as Singularity
• Apptainer containers do not require root to run.
• Can integrate easily with HPC and secure multi-user systems.
• Popular Singularity containers are already available as modules. You 
need to load them. 
• NVIDIA NGC containers 
• If you want to run your containers, you can build them 
• Singularity containers can be built with Docker images
15

Anvil Open OnDemand ondemand.anvil.rcac.purdue.edu
Open OnDemand
• An open-source HPC portal 
• allows users to interact with HPC resources 
through a web browser 
• easily manage files or submit jobs.
• You need to create an ACCESS account at 
https://operations.access-ci.org/identity/new-user 
• Anvil Open OnDemand Guide 
https://www.rcac.purdue.edu/knowledge/anvil/ac
cess/login/ood  
• Anvil Open OnDemand 101 Training 
https://www.rcac.purdue.edu/training/anvil-open-
ondemand-101 
16

File Browser and Terminal 
17
You can upload files from your local machine to the 
Anvil, and download files from Anvil to your local 
machine.
You can open a Terminal inside the browser by 
clicking “Clusters -> Anvil Shell Access” button. Or you 
can use the “Open in Terminal” button.  This enables 
you to submit a job from the command line.

Purdue Provides Containers for ACCESS Users
• Purdue Research Computing has built some of the most popular 
Apptainer containers, making them easy for ACCESS users to use.
• It developed Lmod module support for NGC containers to make high-
performance computing (HPC) more accessible, especially for new 
and educational users via the ACCESS program.
• Purpose
• Simplify the use of NVIDIA GPU-accelerated software
• Reduce the learning curve of tools like Docker and Singularity
• Make AI, ML, and scientific computing software available with a single 
command
18

Purdue Created Lmod Modules for ACCESS Users
19
• No container expertise required — just load like any software:
• module load ngc pytorch
• Instant access to optimized software: AI frameworks like PyTorch, TensorFlow, RAPIDS
• Runs securely inside a Singularity container
• Home/scratch directories automatically mounted
• GPU-ready with no extra configuration
• Supports batch jobs and interactive sessions on clusters like Anvil
Benefits for ACCESS Users
• Purdue maintains pre-tested container environments
• All dependencies and environment variables are handled behind the scenes
• Promotes reproducibility and faster onboarding for classes, research, and workshops
Technical Convenience

NGC Containers Available on the Anvil 
• autodock
• chroma
• gamess
• gromacs
• julia
• lammps
• milc
• namd
• nvhpc
• parabricks
• paraview
• pytorch
• qmcpack
• quantum_espresso
• rapidsai
• relion
• tensorflow
• torchani
20

What is Lmod?
• Lmod is a tool that helps you easily load or unload software on a 
shared computing system (like Anvil). Instead of manually editing 
settings like PATH or environment variables, you just run simple 
commands like:
• It adjusts your environment for you — cleanly and safely.
21
module load python

What are NGC Containers?
• NVIDIA NGC offers ready-to-use software containers. These 
containers are like "portable labs" — preloaded with AI tools, 
libraries, and drivers all optimized to run on NVIDIA GPUs. They're 
great for machine learning, data science, and scientific computing.
• NGC Container Environment Modules
Purdue’s system makes it easy to use NGC containers with Lmod modules. You 
don’t need to learn Docker or Singularity commands. Just load the container as 
if it were regular software:
22
module load ngc python

How It Works Behind the Scenes
When you load a module like ngc pytorch, it:
• Starts the container automatically
• Connects your home directory and scratch folders inside the container
• Sets up the environment so you can run code seamlessly
It feels just like you're using software installed on the system — but it's 
actually running inside a secure, pre-built NVIDIA container.
• ngc sets up the container infrastructure (paths, commands, GPU 
support).
• pytorch defines a particular container image and runtime 
configuration to launch it.
23

Example code 
• Unzip the compressed example code 
• NGC_examples directory 
• Matrix_multiplication: Use NGC Docker container for PyTorch matrix 
multiplication code
• MNIST: Use the NGC Docker container for MNIST digit classification 
• Apptainer1: Create an Apptainer/Singularity image for MNIST digit 
classification
• Submit a job using “sbatch submit.sh” from the terminal.
• You can run an Apptainer/Singularity image from your local machine 
24

NGC Container Example 1: Matrix Multiplication
• Module system
• The Anvil cluster utilizes 
Lmod to manage the 
user environment.
• provides users with 
access to the necessary 
software packages and 
versions
• https://www.rcac.purdu
e.edu/knowledge/anvil/s
oftware/modules
• Module load
• Module purge
• To unload all loaded 
modules and reset 
everything to the 
original state.
25

Matrix Multiplication Outputs
26

Example 2: Training a Simple CNN on MNIST Digits
27
MNIST
•
Dataset of 70,000 handwritten digits 
(0–9)
•
Images are 28×28 pixels, grayscale
•
Widely used for teaching, 
benchmarking, and neural network 
experiments
Key Concepts Students Learn
•
Data loading & normalization 
•
Implementing a simple CNN with Conv, ReLU, Pool layers 
•
Training loop: forward pass → loss → backprop → optimization 
•
Saving trained model for later inference

Example 2: Training a Simple CNN on MNIST Digits
28
This code downloads 
the MNIST dataset 
and trains a CNN 
model for three 
epochs.
Then, it tests an 
image of digit seven.

Example 2: Test images and inference outputs
29
Input images
Output Predictions
Trained 10 epochs, resize to 28 by 28
Trained 3 epochs, did not resize input image
Trained 1 epoch, did not resize input image
Handwritten on a PowerPoint slide
Handwritten on a PowerPoint slide, black 
background, white text color

Example 3: Creating an Apptainer
30
This builds an Apptainer image based on the NVIDIA Python Docker image. However, the generated
Image is not saved. “—nv” option is to run PyTorch w/ Nvidia GPU support.
•
If no GPU is available and no NVIDIA drivers are present, then: The Singularity fails to find NVIDIA 
tools/libraries and typically encounters an error. 
•
Don’t use –nv on CPU-only hosts. 
This builds an Apptainer image based on the NVIDIA Python Docker image and saves it locally.
More information on Apptainer is available at
https://www.rcac.purdue.edu/knowledge/negishi/run/examples/apps/apptainer

Example 3: Creating an Apptainer
• Does building a Singularity (.sif) image from an NGC Docker container require 
Docker Engine, NVIDIA drivers, or NVIDIA Container Toolkit?
• No, you do not need Docker Engine or NVIDIA Container Toolkit on your host to build a .sif 
file from an NGC container using apptainer build.
• But you do need:
• Internet access (to pull from NGC / Docker Hub)
• A working Apptainer/Singularity install
• (Optional) NVIDIA drivers on the execution host only if you plan to use GPU with --nv
Why this works
• apptainer build pytorch.sif docker://nvcr.io/nvidia/pytorch:22.01-py3 does:
• Pull the Docker image layer-by-layer via HTTP (no Docker daemon needed)
• Converts it to a .sif container image
• Resolves environment variables and metadata from the Dockerfile
• All this happens within Apptainer’s user-space, using skopeo and oci-image-
tools internally
31

Submit an Apptainer Job: Submit File
32
Use the submit file if you want to execute your Singularity container on 
the Anvil cluster. 
The output of mnist_train_and_infer.py will be generated in the same 
directory as your submission file.
You may want to update 
•
Allocation 
•
Request time
•
Request Node

What Containers Are Available?
• Some popular examples used by researchers
• Registries like DockerHub, Github registry, Anvil registry, etc
•
33

More Resources to Learn About Containers
Comprehensive slides about Docker/Singularity containers on Anvil are 
available at 
• https://www.rcac.purdue.edu/training/containers101 
• What are containers, and why should we use them? 
• Docker and Singularity 
• Singularity basics
• Using containers on RCAC clusters
• Deployed containers on RCAC clusters
• https://www.rcac.purdue.edu/training/biocontainers101
• Deployed biocontainers on RCAC clusters
• Build your biocontainers
34

Advanced Container Running Examples
• Dockerfiles
• Extending existing containers
• Mounting directories into containers
•
35

Running Services with Containers
• What if you want to run service for users in your domain/community?
oExample: the JupyterHub you used in yesterday's tutorial
• What is Kubernetes, Anvil Composable, Rancher
• Just a few quick slides with screenshots & practical examples
• A subtle way to end hour with a sales pitch for RSE services...
o ...i.e., we can use our container hosting to get your model / data / whatever 
to users in your domain
36

Thank you!
Questions?
thompscs@purdue.edu
wooj@purdue.edu

Extra slides
38

NVIDIA NGC (NVIDIA Gpu Cloud): What it Provides
39
Format
Source Platform
Who Converts It?
Intended For
Docker
Native format from 
NGC
Provided directly 
by NVIDIA
For users with Docker or 
Kubernetes setups (e.g. 
cloud, desktop)
Singularity 
(.sif)
Not directly 
provided by NVIDIA
You (via apptainer 
build)
For HPC clusters where 
Docker is not allowed (e.g. 
Anvil)
• What NGC Hosts:
• NVIDIA publishes containers as Docker images to nvcr.io
• Example: nvcr.io/nvidia/pytorch:22.01-py3
• You can pull it with Docker:
docker pull nvcr.io/nvidia/pytorch:22.01-py3 
• Or convert it to Singularity format:
apptainer build pytorch22.01.sif docker://nvcr.io/nvidia/pytorch:22.01-py3

Load NGC Container Using module system
• Lmod 
Lmod is a software tool that enables users to dynamically modify their environment (e.g., PATH, 
environment variables) using module files. 
• NGC Containers
NVIDIA NGC provides pre-built containers with optimized software for various scientific and AI 
workloads.
• NGC Container Environment Modules
These are Lmod modulefiles that enable users to load and unload NGC containers in the same 
manner as they would load any other software package using Lmod. This simplifies the process 
of using containers in HPC workflows.
• How it works
When a user loads an NGC container module, the Lmod system translates this into actions that 
start the container, map necessary directories, and set up the environment within the container 
to match the module's specifications.
40

SimpleCNN architecture
Layer
Input Size
Output Size
Notes
Conv2d(1, 32, 3, 1)
28×28×1
26×26×32
No padding, 3x3 kernel
MaxPool2d(2)
26×26×32
13×13×32
Halves spatial dimensions
Conv2d(32, 64, 3, 1)
13×13×32
11×11×64
Another 3x3 conv
MaxPool2d(2)
11×11×64
5×5×64
Halves again
Flatten
-
1600
64 channels × 5 × 5
Linear(1600, 128)
1600
128
Fully connected layer
Linear(128, 10)
128
10
Final logits for 10 classes
41
Concept
What it means
in_channels=1
1 input channel → grayscale image
Conv2d
Learns spatial filters (kernels)
MaxPool2d
Reduces spatial size (downsampling)
Flatten
Converts image tensor to 1D vector
Linear
Fully connected classifier head
Batch size
Defined by DataLoader, not Conv2d

### HPC_Cloud_Anvil_tutorial_08012025.pdf
*Source file:* `HPC_Cloud_Anvil_tutorial_08012025.pdf`  ·  *type:* pdf

HPC and cloud computing on 
Anvil and containerization 
basics
Christopher Thompson, Jungha Woo
Purdue University

Outline
• Research computing in academics
• What are containers, and why should you use them?
• Using containers on Anvil
• Where to find common containers
• Advanced container examples
• Running services for your users with Kubernetes
• Guest speaker: Iman Haqiqi, Containerization for the GLASSNET
2

Academic HPC Services
• Where do you go when you outgrow 
your lab computers?
• HPC:  High Performance Computing  
aka clusters or "super computers"
Data centers
...full of racks
...full of nodes
...full of CPUs
Many users, all sharing these nodes
3

Academic HPC Services
• Where do you go for these HPC resources?
• "The Cloud?" (AWS, Azure, GCP, etc)
o $$$ Does your grant have the money? 
"But it's only $0.0017 an hour!"
o Separate cost meters for... compute, storage, 
network transfer, etc
o Can you support your own efforts?  Do you have an 
expert on your team?
o Special needs?  Restricted data (ex: HIPAA)?
Large memory requirements?    $$$$$
• Welcome to... Academic Research Computing!
o Local:  resources & data, support, community
o Simplified costs, sometimes free, usually cheaper
4
vs

Academic HPC Services
• HPC on campus through Research Computing
o1 or 2 slides showing different institution models for cluster access
▪Some schools give it out freely from general funds, some schools sell nodes like us, etc
o 1 or 2 slides showing actual types of services
▪SSH, remote desktop, interactive, queues, other services like OOD, gateways
o Brief mentions, not detailed
o Now we know what kind of services exist, 
maybe locally maybe not, 
leads into what is ACCESS...
5

ACCESS – HPC for All
• What if your institution doesn't have a research 
computing program?
• The NSF ACCESS Program
o NSF funds computing resources around the country
o Provided free to US researchers & educators
▪https://allocations.access-ci.org/allocations-policy#eligibility
o Submit proposals requesting compute time
o Awarded by committee
• Purdue's Anvil cluster is an ACCESS resource
o 90% of its compute time devoted to national users from 
ACCESS program, not just local Purdue researchers
6
https://access-ci.org

Getting Access to ACCESS
• Users are awarded computing resources in 
"allocations" of SUs ("service units")
o Each computing resource decides what 1 SU means to 
them, but generally 1 SU = 1 CPU hour
• Requests are awarded in 4 different levels
o https://allocations.access-ci.org/project-types
• Each level requires more justification (and 
documentation) than the previous tier
• Explore tier allows anyone to try out resources, 
work on testing their code, preparing plan for 
requesting larger allocation and gathering statistics 
for accurate usage at full-scale of simulation
7
https://access-ci.org
Tier 1:  EXPLORE
Tier 2: DISCOVER
Tier 3: ACCELERATE
Tier 4: MAXIMIZE

What Are Containers?
• Containers are a sandboxed environment to package together and 
distribute your programs with everything needed to run them
• How are the different from regular programs?
• Why should you use them in research and academic computing?
8

Traditional Executables
• Code run by operating system directly (also called 
"bare metal")
• Environment (operating system, shared libraries) 
controlled by admins, not normal users
oAt mercy of what admins want to install, or
o Try to compile and maintain your own versions in your 
home directory or scratch space?  Messy!  Fragile!
• Environment is very specific to that computer.
o More your program somewhere else with different 
library versions, everything could break!
9
Diagram showing layers:
Programs
Core OS + libraries
Kernel
hardware

Virtual Machines (VMs)
• Your code runs inside a simulation of an entire 
computer, even a sim of the hardware
• User gets complete control of environment where 
their code runs
o Install and run anything you want in your VM
• Portability:  give away copies of your VM as an 
"image" that anyone else can run, identical to your 
copy
• Inefficient:  Does your code really need to depend on 
simulating an entire computer?  Does your scientific 
code really need an entire copy of the operating 
system to do its job?
10
Diagram showing layers 
from before but now 
program on host is a 
nested copy (VM):
====== VM ========
Programs
Core OS + libraries
Kernel
Simulated Hardware
==================
Core OS + libaries
Kernel
Real hardware

Containers
• Best of both worlds: lightweight while retaining control 
and reproducability.
• Runs as a normal program on host computer, but 
sandboxed from the rest of the files and operating 
system.
• An "engine" program (like Docker) is bridge from 
container to host system's kernel, so containers don't 
need to simulate hardware.
• User has control of everything inside the container 
"image."  
o Packaged with everything they need to run, including core 
operating system utilities, configs, data files, etc.
• Can distribute the "image" for anyone to run the exact 
same way every time on any system.
11
Diagram showing layers 
with containers nested 
inside host system:
==== container ===
Programs
Core OS + libraries
=================
Container Engine
Kernel
Real hardware

Containers
• User writes a script for exact steps to install and 
configure their program.
• Container is "built" from this blueprint into an 
"image."  Every running copy of container uses this 
image to create exact replica of environment each 
time, regardless of where it is being run.
• Large community of containers already exist for 
nearly every commonly used software.
• Anyone can "pull" a published container image and 
be running in minutes a complex program or 
workflow with no need to do difficult setup.
12
Diagram showing flow 
from 
--> writing Dockerfile
--> Building image
--> pushing image
--> pulling image 
(other people)

Why use Containers?
• Portability:
o Develop your code on your own machine
oContainerize it, run exact same setup everywhere
o Grad students and lab assistants stay in sync
o Start using your code on new environments like HPC 
quickly, no friction from locally installed dependencies
• Reproducibility:
o Publish your container image, and anyone can run 
your exact code in the exact environment to recreate 
your experiments
o Publish your container definition file (ex: Dockerfile) 
and anyone can build upon your work to make their 
own version, collaborate with your lab.
13
Diagram showing container 
image being shipped from 
local laptop to different 
places like
•
Lab machines
•
HPC cluster
•
Collaborator laptops

Types of Containers
• Containers have been around for decades, a core 
feature of Linux to compartmentalize programs 
(LXC)
• Only became widely popular in recent years 
because of success of Docker
• Can be installed nearly everywhere:
o Windows (with WSL), Macs, Raspberry Pi, etc
• Many other container "engines" now exist:
o podman, Singularity / Apptainer, the new thing coming 
to next Mac OS
• Docker-style containers are defacto standard, but 
most other engines allow you to download 
("pull") Docker images into their systems and run 
them.
14
Logos over here of 
different systems like 
docker, 
podman, 
apptainer

Which Should I Use, Docker or Singularity?
• Typical Users Should Use:
Docker when:
• Working on personal machines or cloud 
instances
• Building and testing containers locally
• Learning or sharing portable 
environments
• HPC Users Should Use:
Singularity (Apptainer) when:
• Running code on supercomputers, 
academic clusters, or Slurm-based 
schedulers
• Sharing containers with researchers in 
secure multi-user systems
• You don’t have (or shouldn’t have) root 
access
15

16
Use Case
Docker
Singularity (Apptainer)
General users
 Best choice for local 
development, tutorials, and 
standard workloads
 Not commonly needed unless 
targeting HPC or secure 
environments
HPC users
 Often not allowed due to root 
privileges required
 Specifically designed for HPC 
clusters and supercomputers
Root access required?
 Yes — Docker needs root 
privileges (even when running as 
user via docker group)
 No — Singularity runs without 
requiring root, making it secure for 
shared environments
Runs on clusters like 
Slurm/Anvil/Jetstream
 Not directly supported — 
needs extra tools or admin 
support
 Fully supported and often pre-
installed on HPC systems
Security in multi-user systems
 Risky — Docker daemons 
allow privilege escalation
 Secure — Singularity runs as 
the invoking user, no daemon 
involved
File system access (home, 
/scratch, etc.)
 Requires manual volume 
mounting
 Automatically binds common 
directories like $HOME, /scratch
Container hub support
 Docker Hub, GHCR, etc.
 Can pull Docker images 
directly (singularity pull 
docker://...)
Ease of building containers
Easier for building and sharing
 Building containers usually 
requires root, often done on a 
When to Use Docker or Singularity?

Basics of Running Containers on Anvil
• Apptainer/Singularity containers can run on 
Anvil. 
• Docker containers are not allowed for security 
reasons on clusters.
• Apptainer containers do not require root to run.
• Can integrate easily with HPC and secure multi-
user systems.
• Apptainer was formerly known as Singularity
• Popular Singularity containers are already 
available as modules. You need to load them. 
• NVIDIA NGC containers 
• If you want to run your containers, you can 
build them 
• Singularity containers can be built with Docker 
images
• A Docker image can also be built from a Singularity 
image, but it isn't easy!
17

Anvil Open OnDemand ondemand.anvil.rcac.purdue.edu
Open OnDemand
• An open-source HPC portal 
• allows users to interact with HPC resources 
through a web browser 
• easily manage files or submit jobs.
• You need to create an ACCESS account at 
https://operations.access-ci.org/identity/new-user 
• Anvil Open OnDemand Guide 
https://www.rcac.purdue.edu/knowledge/anvil/ac
cess/login/ood  
• Anvil Open OnDemand 101 Training 
https://www.rcac.purdue.edu/training/anvil-open-
ondemand-101 
18

File Browser and Terminal 
19
You can upload files from your local machine to the 
Anvil, and download files from Anvil to your local 
machine.
You can open a Terminal inside the browser by 
clicking “Clusters -> Anvil Shell Access” button. Or you 
can use the “Open in Terminal” button.  This enables 
you to submit a job from the command line.

Purdue Provides Containers for ACCESS Users
• Purdue Research Computing has built some of the most popular 
Apptainer containers, making them easy for ACCESS users to use.
• It developed Lmod module support for NGC containers to make high-
performance computing (HPC) more accessible, especially for new 
and educational users via the ACCESS program.
• Purpose
• Simplify the use of NVIDIA GPU-accelerated software
• Reduce the learning curve of tools like Docker and Singularity
• Make AI, ML, and scientific computing software available with a single 
command
20

Purdue Created Lmod Modules for ACCESS Users
21
• No container expertise required — just load like any software:
• module load ngc pytorch
• Instant access to optimized software: AI frameworks like PyTorch, TensorFlow, RAPIDS
• Runs securely inside a Singularity container
• Home/scratch directories automatically mounted
• GPU-ready with no extra configuration
• Supports batch jobs and interactive sessions on clusters like Anvil
Benefits for ACCESS Users
• Purdue maintains pre-tested container environments
• All dependencies and environment variables are handled behind the scenes
• Promotes reproducibility and faster onboarding for classes, research, and workshops
Technical Convenience

NGC Containers Available on the Anvil 
• autodock
• chroma
• gamess
• gromacs
• julia
• lammps
• milc
• namd
• nvhpc
• parabricks
• paraview
• pytorch
• qmcpack
• quantum_espresso
• rapidsai
• relion
• tensorflow
• torchani
22

What is Lmod?
• Lmod is a tool that helps you easily load or unload software on a 
shared computing system (like Anvil). Instead of manually editing 
settings like PATH or environment variables, you just run simple 
commands like:
• It adjusts your environment for you — cleanly and safely.
23
module load python

What are NGC Containers?
• NVIDIA NGC offers ready-to-use software containers. These 
containers are like "portable labs" — preloaded with AI tools, 
libraries, and drivers all optimized to run on NVIDIA GPUs. They're 
great for machine learning, data science, and scientific computing.
• NGC Container Environment Modules
Purdue’s system makes it easy to use NGC containers with Lmod modules. You 
don’t need to learn Docker or Singularity commands. Just load the container as 
if it were regular software:
24
module load ngc python

How It Works Behind the Scenes
When you load a module like ngc pytorch, it:
• Starts the container automatically
• Connects your home directory and scratch folders inside the container
• Sets up the environment so you can run code seamlessly
It feels just like you're using software installed on the system — but it's 
actually running inside a secure, pre-built NVIDIA container.
• ngc sets up the container infrastructure (paths, commands, GPU 
support).
• pytorch defines a particular container image and runtime 
configuration to launch it.
25

Example code 
• Unzip the compressed example code 
• NGC_examples directory 
• Matrix_multiplication: Use NGC Docker container for PyTorch matrix 
multiplication code
• MNIST: Use the NGC Docker container for MNIST digit classification 
• Apptainer1: Create an Apptainer/Singularity image for MNIST digit 
classification
• Submit a job using “sbatch submit.sh” from the terminal.
• You can run an Apptainer/Singularity image from your local machine 
26

NGC Container Example 1: Matrix Multiplication
• Module system
• The Anvil cluster utilizes 
Lmod to manage the 
user environment.
• provides users with 
access to the necessary 
software packages and 
versions
• https://www.rcac.purdu
e.edu/knowledge/anvil/s
oftware/modules
• Module load
• Module purge
• To unload all loaded 
modules and reset 
everything to the 
original state.
27

Matrix Multiplication Outputs
28

Example 2: Training a Simple CNN on MNIST Digits
29
MNIST
•
Dataset of 70,000 handwritten digits 
(0–9)
•
Images are 28×28 pixels, grayscale
•
Widely used for teaching, 
benchmarking, and neural network 
experiments
Key Concepts Students Learn
•
Data loading & normalization 
•
Implementing a simple CNN with Conv, ReLU, Pool layers 
•
Training loop: forward pass → loss → backprop → optimization 
•
Saving trained model for later inference

Example 2: Training a Simple CNN on MNIST Digits
30
This code downloads 
the MNIST dataset 
and trains a CNN 
model for three 
epochs.
Then, it tests an 
image of digit seven.

Example 2: Test images and inference outputs
31
Input images
Output Predictions
Trained 10 epochs, resize to 28 by 28
Trained 3 epochs, did not resize input image
Trained 1 epoch, did not resize input image
Handwritten on a PowerPoint slide
Handwritten on a PowerPoint slide, black 
background, white text color

Example 3: Creating an Apptainer
32
This builds an Apptainer image based on the NVIDIA Python Docker image. However, the generated
Image is not saved. “—nv” option is to run PyTorch w/ Nvidia GPU support.
•
If no GPU is available and no NVIDIA drivers are present, then: The Singularity fails to find NVIDIA 
tools/libraries and typically encounters an error. 
•
Don’t use –nv on CPU-only hosts. 
This builds an Apptainer image based on the NVIDIA Python Docker image and saves it locally.
More information on Apptainer is available at
https://www.rcac.purdue.edu/knowledge/negishi/run/examples/apps/apptainer

Example 3: Creating an Apptainer
• Does building a Singularity (.sif) image from an NGC Docker container require 
Docker Engine, NVIDIA drivers, or NVIDIA Container Toolkit?
• No, you do not need Docker Engine or NVIDIA Container Toolkit on your host to build a .sif 
file from an NGC container using apptainer build.
• But you do need:
• Internet access (to pull from NGC / Docker Hub)
• A working Apptainer/Singularity install
• (Optional) NVIDIA drivers on the execution host only if you plan to use GPU with --nv
Why this works
• apptainer build pytorch.sif docker://nvcr.io/nvidia/pytorch:22.01-py3 does:
• Pull the Docker image layer-by-layer via HTTP (no Docker daemon needed)
• Converts it to a .sif container image
• Resolves environment variables and metadata from the Dockerfile
• All this happens within Apptainer’s user-space, using skopeo and oci-image-
tools internally
33

Submit an Apptainer Job: Submit File
34
Use the submit file if you want to execute your Singularity container 
on the Anvil cluster. 
The output of mnist_train_and_infer.py will be generated in the same 
directory as your submission file.
You may want to update 
•
Allocation 
•
Request time
•
Request Node

What Containers Are Available?
• Some popular examples used by researchers
• Registries like DockerHub, Github registry, Anvil registry, etc
•
35

More Resources to Learn About Containers
Comprehensive slides about Docker/Singularity containers on Anvil are 
available at 
• https://www.rcac.purdue.edu/training/containers101 
• What are containers, and why should we use them? 
• Docker and Singularity 
• Singularity basics
• Using containers on RCAC clusters
• Deployed containers on RCAC clusters
• https://www.rcac.purdue.edu/training/biocontainers101
• Deployed biocontainers on RCAC clusters
• Build your biocontainers
36

Advanced Container Running Examples
• Dockerfiles
• Extending existing containers
• Mounting directories into containers
•
37

Running Services with Containers
• What if you want to run service for users in your domain/community?
oExample: the JupyterHub you used in yesterday's tutorial
• What if you want to scale up lots of copies for big project?
• What is Kubernetes, Anvil Composable, Rancher
• Just a few quick slides with screenshots & practical examples
• A subtle way to end hour with a sales pitch for RSE services...
o ...i.e., we can use our container hosting to get your model / data / whatever 
to users in your domain
38

Thank you!
Questions?
Chris Thompson
thompscs@purdue.edu
Jungha Woo
wooj@purdue.edu

Extra slides
40

Purdue is Providing ACCESS resources
41

NVIDIA NGC (NVIDIA Gpu Cloud): What it Provides
42
Format
Source Platform
Who Converts It?
Intended For
Docker
Native format from 
NGC
Provided directly 
by NVIDIA
For users with Docker or 
Kubernetes setups (e.g. 
cloud, desktop)
Singularity 
(.sif)
Not directly 
provided by NVIDIA
You (via apptainer 
build)
For HPC clusters where 
Docker is not allowed (e.g. 
Anvil)
• What NGC Hosts:
• NVIDIA publishes containers as Docker images to nvcr.io
• Example: nvcr.io/nvidia/pytorch:22.01-py3
• You can pull it with Docker:
docker pull nvcr.io/nvidia/pytorch:22.01-py3 
• Or convert it to Singularity format:
apptainer build pytorch22.01.sif docker://nvcr.io/nvidia/pytorch:22.01-py3

Load NGC Container Using module system
• Lmod 
Lmod is a software tool that enables users to dynamically modify their environment (e.g., PATH, 
environment variables) using module files. 
• NGC Containers
NVIDIA NGC provides pre-built containers with optimized software for various scientific and AI 
workloads.
• NGC Container Environment Modules
These are Lmod modulefiles that enable users to load and unload NGC containers in the same 
manner as they would load any other software package using Lmod. This simplifies the process 
of using containers in HPC workflows.
• How it works
When a user loads an NGC container module, the Lmod system translates this into actions that 
start the container, map necessary directories, and set up the environment within the container 
to match the module's specifications.
43

SimpleCNN architecture
Layer
Input Size
Output Size
Notes
Conv2d(1, 32, 3, 1)
28×28×1
26×26×32
No padding, 3x3 kernel
MaxPool2d(2)
26×26×32
13×13×32
Halves spatial dimensions
Conv2d(32, 64, 3, 1)
13×13×32
11×11×64
Another 3x3 conv
MaxPool2d(2)
11×11×64
5×5×64
Halves again
Flatten
-
1600
64 channels × 5 × 5
Linear(1600, 128)
1600
128
Fully connected layer
Linear(128, 10)
128
10
Final logits for 10 classes
44
Concept
What it means
in_channels=1
1 input channel → grayscale image
Conv2d
Learns spatial filters (kernels)
MaxPool2d
Reduces spatial size (downsampling)
Flatten
Converts image tensor to 1D vector
Linear
Fully connected classifier head
Batch size
Defined by DataLoader, not Conv2d

### HPC_Cloud_Anvil_tutorial_08032025.pdf
*Source file:* `HPC_Cloud_Anvil_tutorial_08032025.pdf`  ·  *type:* pdf

HPC and cloud computing on 
Anvil and containerization 
basics
Christopher Thompson, Jungha Woo
Purdue University

Outline
• Research computing in academics
• What are containers, and why should you use them?
• Using containers on Anvil cluster
• Where to find common containers
• Advanced container examples
• Running services for your users with Kubernetes
• Guest speaker: Iman Haqiqi, Containerization for the GLASSNET
2

Academic HPC Services
• Where do you go when you outgrow 
your lab computers?
• HPC:  High Performance Computing  
aka clusters or "super computers"
Data centers
...full of racks
...full of nodes
...full of CPUs
Many users, all sharing these nodes
3

Academic HPC Services
• Where do you go for these HPC resources?
• "The Cloud?" (AWS, Azure, GCP, etc)
o $$$ Does your grant have the money? 
"But it's only $0.0017 an hour!"
o Separate cost meters for... compute, storage, 
network transfer, etc
o Can you support your own efforts?  Do you have an 
expert on your team?
o Special needs?  Restricted data (ex: HIPAA)?
Large memory requirements?    $$$$$
• Welcome to... Academic Research Computing!
o Local:  resources & data, support, community
o Simplified costs, sometimes free, usually cheaper
4
vs

Academic HPC Services
• HPC on campus through Research Computing
o1 or 2 slides showing different institution models for cluster access
▪Some schools give it out freely from general funds, some schools sell nodes like us, etc
o 1 or 2 slides showing actual types of services
▪SSH, remote desktop, interactive, queues, other services like OOD, gateways
o Brief mentions, not detailed
o Now we know what kind of services exist, 
maybe locally maybe not, 
leads into what is ACCESS...
5

ACCESS – HPC for All
• What if your institution doesn't have a research 
computing program?
• The NSF ACCESS Program
o NSF funds computing resources around the country
o Provided free to US researchers & educators
▪https://allocations.access-ci.org/allocations-policy#eligibility
o Submit proposals requesting compute time
o Awarded by committee
• Purdue's Anvil cluster is an ACCESS resource
o 90% of its compute time devoted to national users from 
ACCESS program, not just local Purdue researchers
6
https://access-ci.org

Getting Access to ACCESS
• Users are awarded computing resources in 
"allocations" of SUs ("service units")
o Each computing resource decides what 1 SU means to 
them, but generally 1 SU = 1 CPU hour
• Requests are awarded in 4 different levels
o https://allocations.access-ci.org/project-types
• Each level requires more justification (and 
documentation) than the previous tier
• Explore tier allows anyone to try out resources, 
work on testing their code, preparing plan for 
requesting larger allocation and gathering statistics 
for accurate usage at full-scale of simulation
7
https://access-ci.org
Tier 1:  EXPLORE
Tier 2: DISCOVER
Tier 3: ACCELERATE
Tier 4: MAXIMIZE

What Are Containers?
• Containers are a sandboxed environment to package together and 
distribute your programs with everything needed to run them
• How are the different from regular programs?
• Why should you use them in research and academic computing?
8

Traditional Executables
• Code run by operating system directly (also called 
"bare metal")
• Environment (operating system, shared libraries) 
controlled by admins, not normal users
oAt mercy of what admins want to install, or
o Try to compile and maintain your own versions in your 
home directory or scratch space?  Messy!  Fragile!
• Environment is very specific to that computer.
o More your program somewhere else with different 
library versions, everything could break!
9
Diagram showing layers:
Programs
Core OS + libraries
Kernel
hardware

Virtual Machines (VMs)
• Your code runs inside a simulation of an entire 
computer, even a sim of the hardware
• User gets complete control of environment where 
their code runs
o Install and run anything you want in your VM
• Portability:  give away copies of your VM as an 
"image" that anyone else can run, identical to your 
copy
• Inefficient:  Does your code really need to depend on 
simulating an entire computer?  Does your scientific 
code really need an entire copy of the operating 
system to do its job?
10
Diagram showing layers 
from before but now 
program on host is a 
nested copy (VM):
====== VM ========
Programs
Core OS + libraries
Kernel
Simulated Hardware
==================
Core OS + libaries
Kernel
Real hardware

Containers
• Best of both worlds: lightweight while retaining control 
and reproducability.
• Runs as a normal program on host computer, but 
sandboxed from the rest of the files and operating 
system.
• An "engine" program (like Docker) is bridge from 
container to host system's kernel, so containers don't 
need to simulate hardware.
• User has control of everything inside the container 
"image."  
o Packaged with everything they need to run, including core 
operating system utilities, configs, data files, etc.
• Can distribute the "image" for anyone to run the exact 
same way every time on any system.
11
Diagram showing layers 
with containers nested 
inside host system:
==== container ===
Programs
Core OS + libraries
=================
Container Engine
Kernel
Real hardware

Containers
• User writes a script for exact steps to install and 
configure their program.
• Container is "built" from this blueprint into an 
"image."  Every running copy of container uses this 
image to create exact replica of environment each 
time, regardless of where it is being run.
• Large community of containers already exist for 
nearly every commonly used software.
• Anyone can "pull" a published container image and 
be running in minutes a complex program or 
workflow with no need to do difficult setup.
12
Diagram showing flow 
from 
--> writing Dockerfile
--> Building image
--> pushing image
--> pulling image 
(other people)

Why use Containers?
• Portability:
o Develop your code on your own machine
oContainerize it, run exact same setup everywhere
o Grad students and lab assistants stay in sync
o Start using your code on new environments like HPC 
quickly, no friction from locally installed dependencies
• Reproducibility:
o Publish your container image, and anyone can run 
your exact code in the exact environment to recreate 
your experiments
o Publish your container definition file (ex: Dockerfile) 
and anyone can build upon your work to make their 
own version, collaborate with your lab.
13
Diagram showing container 
image being shipped from 
local laptop to different 
places like
•
Lab machines
•
HPC cluster
•
Collaborator laptops

Types of Containers
• Containers have been around for decades, a core 
feature of Linux to compartmentalize programs 
(LXC)
• Only became widely popular in recent years 
because of success of Docker
• Can be installed nearly everywhere:
o Windows (with WSL), Macs, Raspberry Pi, etc
• Many other container "engines" now exist:
o podman, Singularity / Apptainer, the new thing coming 
to next Mac OS
• Docker-style containers are defacto standard, but 
most other engines allow you to download 
("pull") Docker images into their systems and run 
them.
14
Logos over here of 
different systems like 
docker, 
podman, 
apptainer

Which Should I Use, Docker or Singularity?
• Typical Users Should Use:
Docker when:
• Working on personal machines or cloud 
instances
• Building and testing containers locally
• Learning or sharing portable 
environments
• HPC Users Should Use:
Singularity (Apptainer) when:
• Running code on supercomputers, 
academic clusters, or Slurm-based 
schedulers
• Sharing containers with researchers in 
secure multi-user systems
• You don’t have (or shouldn’t have) root 
access
15

16
Use Case
Docker
Singularity (Apptainer)
General users
 Best choice for local 
development, tutorials, and 
standard workloads
 Not commonly needed unless 
targeting HPC or secure 
environments
HPC users
 Often not allowed due to root 
privileges required
 Specifically designed for HPC 
clusters and supercomputers
Root access required?
 Yes — Docker needs root 
privileges (even when running as 
user via docker group)
 No — Singularity runs without 
requiring root, making it secure for 
shared environments
Runs on clusters like 
Slurm/Anvil/Jetstream
 Not directly supported — 
needs extra tools or admin 
support
 Fully supported and often pre-
installed on HPC systems
Security in multi-user systems
 Risky — Docker daemons 
allow privilege escalation
 Secure — Singularity runs as 
the invoking user, no daemon 
involved
File system access (home, 
/scratch, etc.)
 Requires manual volume 
mounting
 Automatically binds common 
directories like $HOME, /scratch
Container hub support
 Docker Hub, GHCR, etc.
 Can pull Docker images 
directly (singularity pull 
docker://...)
Ease of building containers
Easier for building and sharing
 Building containers usually 
requires root, often done on a 
When to Use Docker or Singularity?

Basics of Running Containers on Anvil
Apptainer (formerly Singularity) on Anvil
• Apptainer containers are supported on Anvil 
clusters
• Docker is not allowed due to security restrictions
• No root access needed to run Apptainer containers
• Designed for HPC and secure multi-user 
environments
 Using and Building Containers
• Popular containers (e.g., from NVIDIA NGC) are 
available as pre-installed modules — just load them
• You can also build your own containers
•
 Apptainer can build from Docker images
 You can convert Singularity → Docker, but it’s 
not easy
17

Anvil Open OnDemand ondemand.anvil.rcac.purdue.edu
Open OnDemand
• An open-source HPC portal 
• allows users to interact with HPC resources 
through a web browser 
• easily manage files or submit jobs.
• You need to create an ACCESS account at 
https://operations.access-ci.org/identity/new-user 
• Anvil Open OnDemand Guide 
https://www.rcac.purdue.edu/knowledge/anvil/ac
cess/login/ood  
• Anvil Open OnDemand 101 Training 
https://www.rcac.purdue.edu/training/anvil-open-
ondemand-101 
18

File Browser and Terminal 
19
You can upload files from your local machine to the 
Anvil, and download files from Anvil to your local 
machine.
You can open a Terminal inside the browser by 
clicking “Clusters -> Anvil Shell Access” button. Or you 
can use the “Open in Terminal” button.  This enables 
you to submit a job from the command line.

Purdue Provides Containers for ACCESS Users
• Purdue Research Computing has built some of the most popular 
Apptainer containers, making them easy for ACCESS users to use.
• It developed Lmod module support for NGC containers to make high-
performance computing (HPC) more accessible, especially for new 
and educational users via the ACCESS program.
• Purpose
• Simplify the use of NVIDIA GPU-accelerated software
• Reduce the learning curve of tools like Docker and Singularity
• Make AI, ML, and scientific computing software available with a single 
command
20

Purdue Created Lmod Modules for ACCESS Users
21
• No container expertise required — just load like any software:
• module load ngc pytorch
• Instant access to optimized software: AI frameworks like PyTorch, TensorFlow, RAPIDS
• Runs securely inside a Singularity container
• Home/scratch directories automatically mounted
• GPU-ready with no extra configuration
• Supports batch jobs and interactive sessions on clusters like Anvil
Benefits for ACCESS Users
• Purdue maintains pre-tested container environments
• All dependencies and environment variables are handled behind the scenes
• Promotes reproducibility and faster onboarding for classes, research, and workshops
Technical Convenience

NGC Containers Available on the Anvil 
• autodock
• chroma
• gamess
• gromacs
• julia
• lammps
• milc
• namd
• nvhpc
• parabricks
• paraview
• pytorch
• qmcpack
• quantum_espresso
• rapidsai
• relion
• tensorflow
• torchani
22

What is Lmod?
• Lmod is a tool that helps you easily load or unload software on a 
shared computing system (like Anvil). Instead of manually editing 
settings like PATH or environment variables, you just run simple 
commands like:
• It adjusts your environment for you — cleanly and safely.
• https://www.rcac.purdue.edu/knowledge/anvil/software/modules
23
module load python

What are NGC Containers?
• NVIDIA NGC offers ready-to-use software containers. These 
containers are like "portable labs" — preloaded with AI tools, 
libraries, and drivers all optimized to run on NVIDIA GPUs. They're 
great for machine learning, data science, and scientific computing.
• NGC Container Environment Modules
Purdue’s system makes it easy to use NGC containers with Lmod modules. You 
don’t need to learn Docker or Singularity commands. Just load the container as 
if it were regular software:
24
module load ngc python

How It Works Behind the Scenes
When you load a module like ngc pytorch, it:
• Starts the container automatically
• Connects your home directory and scratch folders inside the container
• Sets up the environment so you can run code seamlessly
It feels just like you're using software installed on the system — but it's 
actually running inside a secure, pre-built NVIDIA container.
• ngc sets up the container infrastructure (paths, commands, GPU 
support).
• pytorch defines a particular container image and runtime 
configuration to launch it.
25

Three Container-Based Examples
The HPC and Cloud Computing on Anvil module includes the file 
NGC_examples.zip. You can upload this file to your Anvil Home directory and 
follow the provided instructions.
After unzipping the provided archive, navigate to the NGC_examples directory. It 
includes:
1.
Matrix_Multiplication
• Runs PyTorch matrix multiplication using an NGC Docker container
2.
MNIST  digit classification
• Uses an NGC Docker container to perform MNIST digit classification
3.
Buidling an Apptainer for MNIST digit classification
• Builds an Apptainer/Singularity image for MNIST digit classification
• Submit the job with:
 
 
sbatch submit.sh 
• You can also run the image from your local machine
26

NGC Container Example 1: Matrix Multiplication
27
Matrix_multiply.py
Submit.sh
Matrix Multiply.py does:
•
Device Detection:
Checks if a GPU (CUDA) is 
available and sets it as the 
computation device; 
otherwise, uses the CPU.
•
Matrix Initialization:
Creates two large 
3000×3000 matrices filled 
with random values directly 
on the selected device.
•
Matrix Multiplication:
Performs matrix 
multiplication using 
torch.matmul, leveraging 
GPU acceleration if 
available.
•
Computation Summary:
Prints confirmation, the 
shape of the result matrix, 
and the total sum of all 
values in the output.

Matrix Multiplication Outputs
28
You can submit a job using “sbatch submit.sh” command. 
Final output file name is pytorch-matmul-{Jobid}.out.

Example 2: Training a Simple CNN on MNIST Digits
 MNIST Digit Classification
A classic task in machine learning: recognizing 
handwritten digits (0–9) from images.
 What is the MNIST Dataset?
•
Stands for Modified National Institute of 
Standards and Technology
•
Contains 70,000 grayscale images of handwritten 
digits
•
Each image is 28×28 pixels
•
Commonly used for:
•
Teaching and learning ML fundamentals
•
Benchmarking classification models
•
Prototyping neural networks
29

Example 2: Training a Simple CNN on MNIST Digits
30
Key concepts we can learn
•
Data loading & normalization 
•
Implementing a simple CNN with Conv, ReLU, Pool 
layers 
•
Training loop: forward pass → loss → backprop → 
optimization 
•
Saving trained model for later inference

Example 2: Training a Simple CNN on MNIST Digits
31
The code downloads the MNIST dataset, trains a convolutional neural network (CNN) for three epochs, 
and evaluates it on a sample image of the digit 7.

Example 2: Test Images and Inference Outputs
32
Input images
Output Predictions
Trained 10 epochs, resize to 28 by 28
Trained 3 epochs, did not resize input image
Trained 1 epoch, did not resize input image
Handwritten on a PowerPoint slide
Handwritten on a PowerPoint slide, black 
background, white text color

Example 3: Creating an Apptainer
33
This builds an Apptainer image based on the NVIDIA Python Docker image. However, the generated
Image is not saved. “—nv” option is to run PyTorch w/ Nvidia GPU support.
•
If no GPU is available and no NVIDIA drivers are present, then: The Singularity fails to find NVIDIA 
tools/libraries and typically encounters an error. 
•
Don’t use –nv on CPU-only hosts. 
This builds an Apptainer image based on the NVIDIA Python Docker image and saves it locally.
More information on Apptainer is available at
https://www.rcac.purdue.edu/knowledge/negishi/run/examples/apps/apptainer

Example 3: Creating an Apptainer
Does building a Singularity (.sif) image from an NGC Docker container require 
Docker Engine, NVIDIA drivers, or NVIDIA Container Toolkit?
• No, you do not need Docker Engine or NVIDIA Container Toolkit on your host to build a .sif 
file from an NGC container using apptainer build.
• But you do need:
• Internet access (to pull from NGC / Docker Hub)
• A working Apptainer/Singularity install
• (Optional) NVIDIA drivers on the execution host only if you plan to use GPU with --nv
Why this works
• apptainer build pytorch.sif docker://nvcr.io/nvidia/pytorch:22.01-py3 does:
• Pull the Docker image layer-by-layer via HTTP (no Docker daemon needed)
• Converts it to a .sif container image
• Resolves environment variables and metadata from the Dockerfile
• All this happens within Apptainer’s user-space, using skopeo and oci-image-
tools internally
34

Submit an Apptainer Job: Submit File
35
Submitting a Job on the Anvil Cluster
•
Use the submit file to run your Singularity container on Anvil.
•
The output from mnist_train_and_infer.py will be saved in the same 
directory as your submission file.
Before submitting, consider updating:
•
Allocation (project ID)
•
Requested wall time
•
Number of nodes

What Containers Are Available?
Popular Containers in Research
Researchers across domains use pre-built containers for speed, reproducibility, and ease of setup. 
Here are some widely used examples:
• NVIDIA NGC
Optimized for AI, ML, and HPC workloads (e.g., PyTorch, TensorFlow, RAPIDS)
• BioContainers
Containers for genomics, proteomics, and other bioinformatics tools
• Neurodocker
Builds containers for neuroimaging tools like FSL, AFNI, FreeSurfer
• GeoDocker
Geospatial analysis tools (e.g., GDAL, GeoServer, PostGIS)
• OpenFOAM
CFD simulation toolkit packaged for easy deployment
• Quantum Chemistry Containers
e.g., Gaussian, ORCA, Q-Chem in supported HPC environments
36

Container Registries: Where Images Live
• Registries store and distribute container images
• They allow you to pull, share, and version containers across systems
Common Examples:
• Docker Hub – Most widely used public registry
• GitHub Container Registry (GHCR) – Integrated with GitHub for CI/CD 
workflows
• NVIDIA NGC – Optimized containers for AI/ML and HPC
• Anvil Registry – Hosts curated containers for the Anvil HPC environment
• Use registries to pull existing images or push your own for reuse and 
collaboration
37

More Resources to Learn About Containers
Comprehensive slides about Docker/Singularity containers on Anvil are 
available at 
• https://www.rcac.purdue.edu/training/containers101 
• What are containers, and why should we use them? 
• Docker and Singularity 
• Singularity basics
• Using containers on RCAC clusters
• Deployed containers on RCAC clusters
• https://www.rcac.purdue.edu/training/biocontainers101
• Deployed biocontainers on RCAC clusters
• Build your biocontainers
38

Advanced Container Running Examples
• Dockerfiles
• Extending existing containers
• Mounting directories into containers
•
39

Running Services with Containers
• What if you want to run service for users in your domain/community?
oExample: the JupyterHub you used in yesterday's tutorial
• What if you want to scale up lots of copies for big project?
• What is Kubernetes, Anvil Composable, Rancher
• Just a few quick slides with screenshots & practical examples
• A subtle way to end hour with a sales pitch for RSE services...
o ...i.e., we can use our container hosting to get your model / data / whatever 
to users in your domain
40

More RCAC Training 
Training Opportunities
For full details, visit: rcac.purdue.edu/training
Anvil Training Sessions:
• Anvil 101
• Anvil Open OnDemand 101
• Containerized Bioinformatics Applications for HPC
• Interactive Computing on the Anvil Composable Subsystem
Purdue Training Sessions:
• Unix 101, Unix 102, Unix 201
• Jupyter Kernels and HPC
• Running Bioinformatics Analyses in HPC
• Open OnDemand 101
41

Thank you!
Questions?
Chris Thompson
thompscs@purdue.edu
Jungha Woo
wooj@purdue.edu

Extra Slides
43

Purdue is Providing ACCESS Resources
44

NVIDIA NGC (NVIDIA Gpu Cloud): What It Provides
45
Format
Source Platform
Who Converts It?
Intended For
Docker
Native format from 
NGC
Provided directly 
by NVIDIA
For users with Docker or 
Kubernetes setups (e.g. 
cloud, desktop)
Singularity 
(.sif)
Not directly 
provided by NVIDIA
You (via apptainer 
build)
For HPC clusters where 
Docker is not allowed (e.g. 
Anvil)
• What NGC Hosts:
• NVIDIA publishes containers as Docker images to nvcr.io
• Example: nvcr.io/nvidia/pytorch:22.01-py3
• You can pull it with Docker:
docker pull nvcr.io/nvidia/pytorch:22.01-py3 
• Or convert it to Singularity format:
apptainer build pytorch22.01.sif docker://nvcr.io/nvidia/pytorch:22.01-py3

Load NGC Container Using Module System
• Lmod 
Lmod is a software tool that enables users to dynamically modify their environment (e.g., PATH, 
environment variables) using module files. 
• NGC Containers
NVIDIA NGC provides pre-built containers with optimized software for various scientific and AI 
workloads.
• NGC Container Environment Modules
These are Lmod modulefiles that enable users to load and unload NGC containers in the same 
manner as they would load any other software package using Lmod. This simplifies the process 
of using containers in HPC workflows.
• How it works
When a user loads an NGC container module, the Lmod system translates this into actions that 
start the container, map necessary directories, and set up the environment within the container 
to match the module's specifications.
46

SimpleCNN Architecture
Layer
Input Size
Output Size
Notes
Conv2d(1, 32, 3, 1)
28×28×1
26×26×32
No padding, 3x3 kernel
MaxPool2d(2)
26×26×32
13×13×32
Halves spatial dimensions
Conv2d(32, 64, 3, 1)
13×13×32
11×11×64
Another 3x3 conv
MaxPool2d(2)
11×11×64
5×5×64
Halves again
Flatten
-
1600
64 channels × 5 × 5
Linear(1600, 128)
1600
128
Fully connected layer
Linear(128, 10)
128
10
Final logits for 10 classes
47
Concept
What it means
in_channels=1
1 input channel → grayscale image
Conv2d
Learns spatial filters (kernels)
MaxPool2d
Reduces spatial size (downsampling)
Flatten
Converts image tensor to 1D vector
Linear
Fully connected classifier head
Batch size
Defined by DataLoader, not Conv2d

## Non-text files (not extracted)

- `NGC_examples.zip` (zip)
