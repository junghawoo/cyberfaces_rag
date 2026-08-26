---
title: "Containers and Virtual Machines"
unit_id: 78
course_id: 3
level: "Expert"
slug: containers-and-virtual-machines
is_course: 0
---

# Containers and Virtual Machines

## Text content

### Why Virtual Machines?
There are clear benefits to VMs for the curious and tech savvy, you can explore operating systems without changing the one on your computer, weed out any malware safely, and even try out old operating systems for otherwise incompatible software. But let's say you aren't interested in those things, can VMs still help you? Yes! One of the main reasons virtual machines are so well used is they are very portable, able to transfer to whatever system can run it. This is great for projects between multiple people or businesses changing computers, as the hardware can change without any of the contents. Lately, however, this ability has been overshadowed by Docker.
Listed below is how you can create your very own virtual machine to try for yourself. I recommend Linux (specifically I show Ubuntu), and to learn more about Linux check out Module 2.

### Containers and Docker
A Container is very similar to a Virtual Machine in that it puts aside hard drive space, but instead of putting in another OS a container is for bins and applications that are operable through the host OS.  In this way they are less intensive than VMs as they are not going through extra steps in order to run programs, rather than powering a whole extra OS a computer merely needs to run the desired program.  Containers are attractive as they provide a way to make applications and code portable, separate from the computer.
Docker is a company that provides access to containers, even over the cloud.
Linked is how containers are helping EAPS science.

## Fetched resources (external URLs)

### How to Create and Use Virtual Machines (link)
*URL:* https://www.howtogeek.com/196060/beginner-geek-how-to-create-and-use-virtual-machines/

# Beginner Geek: How to Create and Use Virtual Machines

Beginner Geek: How to Create and Use Virtual Machines
Close
Close
By
Chris Hoffman
Published
Jul 13, 2017, 8:43 PM EDT
Chris Hoffman is a former How-To Geek Editor-in-Chief. Since 2011, Chris has personally written over 2,000 articles that have been read more than one billion times---and that's just here at How-To Geek.
With over a decade of writing experience in the field of technology, Chris has written for a variety of publications including
The New York Times
, Reader's Digest, IDG's
PCWorld
,
Digital Trends
, and
MakeUseOf
. Beyond the web, his work has appeared in the print edition of The New York Times (
September 9, 2019
) and in PCWorld's print magazines, specifically in the
August 2013
and
July 2013
editions, where his story was on the cover. He also wrote the USA's most-saved article of 2021, according to
Pocket
.
Chris was a PCWorld columnist for two years. He founded PCWorld's "
World Beyond Windows
" column, which covered the latest developments in open-source operating systems like Linux and Chrome OS. Beyond the column, he wrote about everything from Windows to tech travel tips.
The news he's broken has been covered by outlets like
the BBC
,
The Verge
,
Slate
,
Gizmodo
,
Engadget
,
TechCrunch
,
Digital Trends
,
ZDNet
,
The Next Web
, and
Techmeme
. Instructional tutorials he's written have been linked to by organizations like
The New York Times
,
Wirecutter
,
Lifehacker
,
CNET
,
Ars Technica
, and
John Gruber's Daring Fireball
. His roundups of new features in Windows 10 updates have been
called
"the most detailed, useful Windows version previews of anyone on the web" and covered by prominent Windows journalists like
Paul Thurrott
and Mary Jo Foley on
TWiT's Windows Weekly
. His work has even appeared on
the front page of Reddit
.
Sign in to your
How-To Geek
account
Add Us On
Jump links
Jump Links
What's a Virtual Machine?
Why You'd Want to Create a Virtual Machine
Virtual Machine Apps
Setting Up a Virtual Machine
follow
Follow
followed
Followed
Like
Like
Log in
Here is a fact-based summary of the story contents:
Try something different:
Show me the facts
Explain it like I’m 5
Give me a lighthearted recap
Virtual machines allow you to run an operating system in an app window on your desktop that behaves like a full, separate computer. You can use them play around with different operating systems, run software your main operating system can't, and try out apps in a safe, sandboxed environment.
There are several good free virtual machine (VM) apps out there, which makes setting up a virtual machine something anybody can do. You'll need to install a VM app, and have access to installation media for the operating system you want to install.
What's a Virtual Machine?
A virtual machine app creates a virtualized environment---called, simply enough, a virtual machine---that behaves like a separate computer system, complete with virtual hardware devices. The VM runs as a process in a window on your current operating system. You can boot an operating system installer disc (or live CD) inside the virtual machine, and the operating system will be "tricked" into thinking it's running on a real computer. It will install and run just as it would on a real, physical machine. Whenever you want to use the operating system, you can open the virtual machine program and use it in a window on your current desktop.
In the VM world, the operating system actually running on your computer is called the host and any operating systems running inside VMs are called guests. It helps keep things from getting too confusing.
In a particular VM, the guest OS is stored on a virtual hard drive---a big, multi-gigabyte file stored on your real hard drive. The VM app presents this file the guest OS as a real hard drive. This means you won't have to mess around with partitioning or doing anything else complicated with your real hard drive.
Virtualization does add some overhead, so don't expect them to be as fast as if you had installed the operating system on real hardware. Demanding games or other apps that require serious graphics and CPU power don't really do so well, so virtual machines aren't the ideal way to
play Windows PC games on Linux
or
Mac OS X
---at least, not unless those games are much older or aren't graphically demanding.
Related:
How to Play Windows PC Games on a Mac
The limit to how many VMs you can have are really just limited by the amount of hard drive space. Here's a peek at some of the VMs we use when testing things out while writing articles. As you can see, we've got full VMs with several versions of Windows and Ubuntu installed.
You can also run multiple VMs at the same time, but you'll find yourself somewhat limited by your system resources. Each VM eats up some CPU time, RAM, and other resources.
Why You'd Want to Create a Virtual Machine
Aside from being good geeky fun to play around with, VMs offer a number of serious uses. They allow you to experiment with another OS without having to install it on your physical hardware. For example, they are a great way to mess around with Linux---or a new Linux distribution---and see if it feels right for you. When you're done playing with an OS, you can just delete the VM.
VMs also provide a way to run another OS' software. For example, as a Linux or Mac user, you could install Windows in a VM to run Windows apps you might not otherwise have access to. If you want to run a later version of Windows---like Windows 10---but have older apps that only run on XP, you could install Windows XP into a VM.
Related:
Sandboxes Explained: How They're Already Protecting You and How to Sandbox Any Program
Another advantage VMs provide is that they are "
sandboxed
" from the rest of your system. Software inside a VM can't escape the VM to tamper with the rest of your system. This makes VMs a safe place to test apps---or websites---you don't trust and see what they do.
For example, when
the "Hi, we're from Windows" scammers
came calling,
we ran their software in a VM to see what they would actually do
---the VM prevented the scammers from accessing our computer's real operating system and files.
Related:
The “Tech Support” Scammers Called HTG (So We Had Fun with Them)
Sandboxing also allows you to run insecure OSes more safely. If you still need Windows XP for older apps, you could run it in a VM where at least the harm of running an old, unsupported OS is mitigated.
Virtual Machine Apps
There are several different virtual machine programs you can choose from:
VirtualBox
:
(Windows, Linux, Mac OS X): VirtualBox is very popular because it's open-source and completely free. There's no paid version of VirtualBox, so you don't have to deal with the usual "upgrade to get more features" upsells and nags. VirtualBox works very well, particularly on Windows and Linux where there's less competition, making it a good place to start with VMs.
VMware Player
:
(Windows, Linux): VMware has their own line of virtual machine programs. You can use VMware Player on Windows or Linux as a free, basic virtual machine tool. More advanced features---many of which are found in VirtualBox for free---require upgrading to the paid
VMware Workstation
program. We recommend starting out with VirtualBox, but if it doesn't work properly you may want to try VMware Player.
VMware Fusion
:
(Mac OS X): Mac users must buy VMware Fusion to use a VMware product, since the free VMware Player isn't available on a Mac. However, VMware Fusion is more polished.
Parallels Desktop
:
(Mac OS X): Macs also have Parallels Desktop available. Both Parallels Desktop and VMware Fusion for Mac are more polished than the virtual machine programs on other platforms, since they're marketed to average Mac users who might want to run Windows software.
While VirtualBox works very well on Windows and Linux, Mac users may want to buy a more polished, integrated Parallels Desktop or VMware Fusion program. Windows and Linux tools like VirtualBox and VMware Player tend to be targeted to a geekier audience.
There are many more VM options, of course.
Linux includes KVM, an integrated virtualization solution
. Professional and Enterprise version of Windows 8 and 10---but not Windows 7---include
Microsoft's Hyper-V
, another integrated virtual machine solution. These solutions can work well, but they don't have the most user-friendly interfaces.
Related:
How to Install or Enable Hyper-V Virtualization in Windows 8 or 10
Setting Up a Virtual Machine
Once you've decided on a VM app and gotten it installed, setting up a VM is actually pretty easy. We're going to run through the basic process in VirtualBox, but most apps handle creating a VM the same way.
Open up your VM app and click the button to create a new virtual machine.
You'll be guided through the process by a wizard that first asks which OS you'll be installing. If you type the name of the OS in the "Name" box, the app will most likely automatically select the type and version for the OS. If it doesn't---or it guesses wrong---select those items yourself from the dropdown menus. When you're done, click "Next."
Based on the OS you plan to install, the wizard will preselect some default settings for you, but you can change them over the screens that follow. You'll be asked how much memory to allocate to the VM. If you want something other than the default, select it here. Otherwise, just click "Next." And don't worry, you'll be able to change this value later if you need to.
The wizard will also create the virtual hard disk file to be used by the VM. Unless you already have a virtual hard disk file you want to use, just select the option to create a new one.
You'll also be asked whether to create a dynamically allocated or fixed size disk. With a dynamically allocated disk, you'll set a maximum disk size, but the file will only grow to that size as it needs to. With a fixed size disk, you'll also set a size, but the file created will be that large from its creation.
We recommend creating fixed size disks because, while they eat up a little more disk space, they also perform better---making your VM feel a bit more responsive. Plus, you'll know how much disk space you've used and won't get surprised when your VM files start growing.
You'll then be able to set the size of the virtual disk. You're free to go with the default setting or change the size to suit your needs. Once you click "Create," the virtual hard disk is created.
After that, you're dumped back into the main VM app window, where your new VM should show up. Make sure the installation media you need is available to the machine---usually this involves pointing to an ISO file or real disc through the VM's settings. You can run your new VM by selecting it and hitting "Start."
Of course, we've just touched on the basics of using VMs here. If you're interested in more reading, check out some of our other guides:
The Complete Guide to Speeding Up Your Virtual Machines
How to Create and Run Virtual Machines with Hyper-V
How to Install Android in VirtualBox
How to Share Your Computer's Files With a Virtual Machine
Use Portable VirtualBox to Take Virtual Machines With You Everywhere
10 VirtualBox Tricks and Advanced Features You Should Know About
Have any other uses or tips for using VMs we didn't touch on? Let us know in the comments!
Windows
Features
Mac
Follow
Followed
Like
Share
Facebook
X
WhatsApp
Threads
Bluesky
LinkedIn
Reddit
Flipboard
Copy link
Email
Readers like you help support How-To Geek. When you make a purchase using links on our site, we may earn an affiliate commission.
Read More
.
Close
Desktop
Mobile
Everyone says PowerToys should be included with Windows—here's why it isn't
This is the Linux distro that convinced me to finally uninstall Windows
This "power-saving" setting is slowing down your Windows PC, turn it off now
See More
3 Google Apps you're probably not using, but should
4 more useful Samsung Galaxy Watch features that aren’t enabled by default
I finally found the perfect watch face for my smartwatch
See More
Trending Now
I didn't realize how slow my NAS was until I bought this $50 UniFi switch
Your USB-C cable might be holding back your laptop's best feature
I let Claude read my DNS log, and it told me things about my network I never would've known otherwise

### Using Linux containers to analyze the impact of climate change and soil on New Zealand crops (link)
*URL:* https://opensource.com/article/19/1/using-containers-analyze-climate-change

# Using Linux containers to analyze the impact of climate change and soil on New Zealand crops | Opensource.com

Using Linux containers to analyze the impact of climate change and soil on New Zealand crops | Opensource.com
Skip to main content
Search
Using Linux containers to analyze the impact of climate change and soil on New Zealand crops
Method models climate change scenarios by processing vast amounts of high-resolution soil and weather data.
167 readers like this.
Image by:
Opensource.com
New Zealand's economy is dependent on agriculture, a sector that is highly sensitive to climate change. This makes it critical to develop analysis capabilities to assess its impact and investigate possible mitigation and adaptation options. That analysis can be done with tools such as
agricultural systems models
. In simple terms, it involves creating a model to quantify how a specific crop behaves under certain conditions then simulating altering a few variables to see how that behavior changes. Some of the software available to do this includes
CropSyst
from Washington State University and the Agricultural Production Systems Simulator (
APSIM
) from the Commonwealth Scientific and Industrial Research Organization (CSIRO) in Australia.
Historically, these models have been used primarily for small area (point-based) simulations where all the variables are well known. For large area studies (landscape scale, e.g., a whole region or national level), the soil and climate data need to be upscaled or downscaled to the resolution of interest, which means increasing uncertainty. There are two major reasons for this: 1) it is hard to create and/or obtain access to high-resolution, geo-referenced, gridded datasets; and 2) the most common installation of crop modeling software is in an end user's desktop or workstation that's usually running one of the supported versions of Microsoft Windows (system modelers tend to prefer the GUI capabilities of the tools to prepare and run simulations, which are then restricted to the computational power of the hardware used).
New Zealand has several Crown Research Institutes that provide scientific research across many different areas of importance to the country's economy, including Landcare Research, the National Institute of Water and Atmospheric Research (NIWA), and the New Zealand Institute for Plant & Food Research. In a joint project, these organizations contributed datasets related to the country's soil, terrain, climate, and crop models. We wanted to create an analysis framework that uses APSIM to run enough simulations to cover relevant time-scales for climate change questions (>100 years' worth of climate change data) across all of New Zealand at a spatial resolution of approximately 25km
2
. We're talking several million simulations, each one taking at least 10 minutes to complete on a single CPU core. If we were to use a standard desktop, it would probably have been faster to just wait outside and see what happens.
Enter HPC
High-performance computing (HPC) is the use of parallel processing for running programs efficiently, reliably, and quickly. Typically this means making use of batch processing across multiple hosts, with each individual process dealing with just a little bit of data, using a job scheduler to orchestrate them.
Linux Containers
What are Linux containers?
An introduction to container terminology
Download: Containers Primer
Kubernetes Operators: Automating the container orchestration platform
eBook: Kubernetes patterns for designing cloud-native apps
What is Kubernetes?
Parallel computing can mean either distributed computing, where each processing thread needs to communicate with others between tasks (especially intermediate results), or it can be "embarrassingly parallel" where there is no such need. When dealing with the latter, the overall performance grows linearly the more capacity there is available.
Crop modeling is, luckily, an embarrassingly parallel problem: it does not matter how much data or how many variables you have, each variable that changes means one full simulation that needs to run. And because simulations are independent from each other, you can run as many simulations as you have CPUs.
Solve for dependency hell
APSIM is a complex piece of software. Its codebase is comprised of modules that have been written in multiple different programming languages and tightly integrated over the past three decades. The application achieves portability between the Windows and GNU/Linux operating systems by leveraging the
Mono Project
framework, but the number of external dependencies and workarounds that are required to run it in a Linux environment make the implementation non-trivial.
The build and install documentation is scarce, and the instructions that do exist target Ubuntu Desktop editions. Several required dependencies are undocumented, and the build process sometimes relies on the
binfmt_misc
kernel module to allow direct execution of .exe files linked to the Mono libraries (instead of calling
mono file.exe
), but it does so inconsistently (this has since been fixed upstream). To add to the confusion, some .exe files are Mono assemblies, and some are native (libc) binaries (this is done to avoid differences in the names of the executables between operating system platforms). Finally, Linux builds are created on-demand "in-house" by the developers, but there are no publicly accessible automated builds due to lack of interest from external users.
All of this may work within a single organization, but it makes APSIM challenging to adopt in other environments. HPC clusters tend to standardize on one Linux distribution (e.g., Red Hat Enterprise Linux, CentOS, Ubuntu, etc.) and job schedulers (e.g., PBS, HTCondor, Torque, SGE, Platform LSF, SLURM, etc.) and can implement disparate storage and network architectures, network configurations, user authentication and authorization policies, etc. As such, what software is available, what versions, and how they are integrated are highly environment-specific. Projects like
OpenHPC
aim to provide some sanity to this situation, but the reality is that most HPC clusters are bespoke in nature, tailored to the needs of the organization.
A simple way to work around these issues is to introduce containerization technologies. This should not come as a surprise (it's in the title of this article, after all). Containers permit creating a standalone, self-sufficient
artifact
that can be run without changes in any environment that supports running them. But containers also provide additional advantages from a "reproducible research" perspective: Software containers can be created in a
reproducible way
, and once created, the resulting container images are both
portable
and
immutable
.
Reproducibility:
Once a container definition file is written following best practices (for instance, making sure that the software versions installed are explicitly defined), the same resulting container image can be created in a deterministic fashion.
Portability:
When an administrator creates a container image, they can compile, install, and configure all the software that will be required and include any external dependencies or libraries needed to run them, all the way down the stack to the Linux distribution itself. During this process, there is no need to target the execution environment for anything other than the hardware. Once created, a container image can be distributed as a standalone artifact. This cleanly separates the build and install stages of a particular software from the runtime stage when that software is executed.
Immutability:
After it's built, a container image is immutable. That is, it is not possible to change its contents and persist them without creating a new image.
These properties enable capturing the exact state of the software stack used during the processing and distributing it alongside the raw data to replicate the analysis in a different environment, even when the Linux distribution used in that environment does not match the distribution used inside the container image.
Docker
While operating-system-level virtualization is not a new technology, it was primarily because of Docker that it became increasingly popular. Docker provides a way to develop, deploy, and run software containers in a simple fashion.
The first iteration of an APSIM container image was implemented in Docker, replicating the build environment partially documented by the developers. This was done as a proof of concept on the feasibility of containerizing and running the application. A second iteration introduced multi-stage builds: a method of creating container images that allows separating the build phase from the installation phase. This separation is important because it reduces the final size of the resulting container images, which will not include any dependencies that are required only during build time. Docker containers are not particularly suitable for multi-tenant HPC environments. There are three primary things to consider:
1. Data ownership
Container images do not typically store the configuration needed to integrate with enterprise authentication directories (e.g., Active Directory, LDAP, etc.) because this would reduce portability. Instead, user information is usually hardcoded explicitly in the image directly (and when it's not,
root
is used by default). When the container starts, the contained process will run with this hardcoded identity (and remember,
root
is used by default). The result is that the output data created by the containerized process is owned by a user that potentially only exists inside the container image. NOT by the user who started the container (also, did I mention that
root
is used by default?).
A possible workaround for this problem is to override the runtime user when the container starts (using the
docker run -u…
flag). But this introduces added complexity for the user, who must now learn about user identities (UIDs), POSIX ownership and permissions, the correct syntax for the
docker run
command, as well as find the correct values for their UID, group identifier (GID), and any additional groups they may need. All of this for someone who just wants to get some science done.
It is also worth noting that this method will not work every time. Not all applications are happy running as an arbitrary user or a user not present in the system's database (e.g.,
/etc/passwd
file). These are edge cases, but they exist.
2. Access to persistent storage
Container images include only the files needed for the application to run. They typically do not include the input or raw data to be processed by the application. By default, when a container image is instantiated (i.e., when the container is started), the filesystem presented to the containerized application will show only those files and directories present in the container image. To access the input or raw data, the end user must explicitly map the desired mount points from the host server to paths within the filesystem in the container (typically using
bind
mounts
). With Docker, these "volume mounts" are impossible to pre-configure globally, and the mapping must be done on a per-container basis when the containers are started. This not only increases the complexity of the commands needed to run an application, but it also introduces another undesired effect…
3. Compute host security
The ability to start a process as an arbitrary user and the ability to map arbitrary files or directories from the host server into the filesystem of a running container are two of several powerful capabilities that Docker provides to operators. But they are possible because, in the
security model adopted by Docker
, the daemon that runs the containers must be started on the host with
root
privileges. In consequence, end users that have access to the Docker daemon end up having the equivalent of
root
access to the host. This introduces security concerns since it violates the
Principle of Least Privilege
. Malicious actors can perform actions that exceed the scope of their initial authorization, but end users may also inadvertently corrupt or destroy data, even without malicious intent.
A possible solution to this problem is to implement
user namespaces
. But in practice, these are cumbersome to maintain, particularly in corporate environments where user identities are centralized in enterprise directories.
Singularity
To tackle these problems, the third iteration of APSIM containers was implemented using Singularity. Released in 2016,
Singularity Community
is an open source container platform designed specifically for scientific and HPC environments.
"
A user inside a Singularity container is the same user as outside the container
"
is one of Singularity's defining characteristics. It allows an end user to run a command inside of a container image as him or herself. Conversely, it does not allow impersonating other users when starting a container.
Another advantage of Singularity's approach is the way container images are stored on disk. With Docker, container images are stored in multiple separate "layers," which the Docker daemon needs to overlay and flatten during the container's runtime. When multiple container images reuse the same layer, only one copy of that layer is needed to re-create the runtime container's filesystem. This results in more efficient use of storage, but it does add a bit of complexity when it comes to distributing and inspecting container images, so Docker provides special commands to do so. With Singularity, the entire execution environment is contained within a single, executable file. This introduces duplication when multiple images have similar contents, but it makes the distribution of those images trivial since it can now be done with traditional file transfer methods, protocols, and tools.
The Docker container recipe files (i.e., the
Dockerfile
and related assets) can be used to re-create the container image as it was built for the project. Singularity allows importing and running Docker containers natively, so the same files can be used for both engines.
A day in the life
To illustrate the above with a practical example, let's put you in the shoes of a computational scientist. So not to single out anyone in particular, imagine that you want to use ToolA, which processes input files and creates output with statistics about them. Before asking the sysadmin to help you out, you decide to test the tool on your local desktop to see if works.
ToolA has a simple syntax. It's a single binary that takes one or more filenames as command line arguments and accepts a
-o {json|yaml}
flag to alter how the results are formatted. The outputs are stored in the same path as the input files are. For example:
$ ./ToolA file1 file2
$ ls
file1 file1.out file2 file2.out ToolA
You have several thousand files to process, but even though ToolA uses multi-threading to process files independently, you don't have a thousand CPU cores in this machine. You must use your cluster's job scheduler. The simplest way to do this at scale is to launch as many jobs as files you need to process, using one CPU thread each. You test the new approach:
$ export PATH=$(pwd):${PATH}
$ cd ~/input/files/to/process/samples
$ ls -l | wc -l
38
$ # we will set this to the actual qsub command when we run in the cluster
$ qsub=""
$ for myfiles in *; do $qsub ToolA $myfiles; done
...
$ ls -l | wc -l
75
Excellent. Time to bug the sysadmin and get ToolA installed in the cluster.
It turns out that ToolA is easy to install in Ubuntu Bionic because it is already in the repos, but a nightmare to compile in CentOS 7, which our HPC cluster uses. So the sysadmin decides to create a Docker container image and push it to the company's registry. He also adds you to the
docker
group after begging you not to misbehave.
You look up the syntax of the Docker commands and decide to do a few test runs before submitting thousands of jobs that could potentially fail.
$ cd ~/input/files/to/process/samples
$ rm -f *.out
$ ls -l | wc -l
38
$ docker run -d registry.example.com/ToolA:latest file1
e61d12292d69556eabe2a44c16cbd27486b2527e2ce4f95438e504afb7b02810
$ ls -l | wc -l
38
$ ls *out
$
Ah, of course, you forgot to mount the files. Let's try again.
$ docker run -d -v $(pwd):/mnt registry.example.com/ToolA:latest /mnt/file1
653e785339099e374b57ae3dac5996a98e5e4f393ee0e4adbb795a3935060acb
$ ls -l | wc -l
38
$ ls *out
$
$ docker logs 653e785339
ToolA: /mnt/file1: Permission denied
You ask the sysadmin for help, and he tells you that SELinux is blocking the process from accessing the files and that you're missing a flag in your
docker run
. You don't know what SELinux is, but you remember it mentioned somewhere in the docs, so you look it up and try again:
$ docker run -d -v $(pwd):/mnt:z registry.example.com/ToolA:latest /mnt/file1
8ebfcbcb31bea0696e0a7c38881ae7ea95fa501519c9623e1846d8185972dc3b
$ ls *out
$
$ docker logs 8ebfcbcb31
ToolA: /mnt/file1: Permission denied
You go back to the sysadmin, who tells you that the container uses
myuser
with UID 1000 by default, but your files are readable only to you, and your UID is different. So you do what you know is bad practice, but you're fed up: you run
chmod 777 file1
before trying again. You're also getting tired of having to copy and paste hashes, so you add another flag to your
docker run
:
$ docker run -d --name=test -v $(pwd):/mnt:z registry.example.com/ToolA:latest /mnt/file1
0b61185ef4a78dce988bb30d87e86fafd1a7bbfb2d5aea2b6a583d7ffbceca16
$ ls *out
$
$ docker logs test
ToolA: cannot create regular file '/mnt/file1.out': Permission denied
Alas, at least this time you get a different error. Progress! Your friendly sysadmin tells you that the process in the container won't have write permissions on your directory because the identities don't match, and you need more flags on your command line.
$ docker run -d -u $(id -u):$(id -g) --name=test -v $(pwd):/mnt:z registry.example.com/ToolA:latest /mnt/file1
docker: Error response from daemon: Conflict. The container name "/test" is already in use by container "0b61185ef4a78dce988bb30d87e86fafd1a7bbfb2d5aea2b6a583d7ffbceca16". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
$ docker rm test
$ docker run -d -u $(id -u):$(id -g) --name=test -v $(pwd):/mnt:z registry.example.com/ToolA:latest /mnt/file1
06d5b3d52e1167cde50c2e704d3190ba4b03f6854672cd3ca91043ad23c1fe09
$ ls *out
file1.out
$
Success! Now we just need to wrap our command with the one used by the job scheduler and wrap all of that again with our
for
loop.
$ cd ~/input/files/to/process
$ ls -l | wc -l
934752984
$ for myfiles in *; do qsub -q short_jobs -N "toola_${myfiles}" docker run -d -u $(id -u):$(id -g) --name="toola_${myfiles}" -v $(pwd):/mnt:z registry.example.com/ToolA:latest /mnt/${myfiles}; done
Now that was a bit clunky, wasn't it? Let's look at how using Singularity
simplifies
it.
$ cd ~
$ singularity pull --name ToolA.simg docker://registry.example.com/ToolA:latest
$ ls
input ToolA.simg
$ ./ToolA.simg
Usage: ToolA [-o {json|yaml}] <file1> [file2...fileN]
$ cd ~/input/files/to/process
$ for myfiles in *; do qsub -q short_jobs -N "toola_${myfiles}" ~/ToolA.simg ${myfiles}; done
Need I say more?
This works because, by default, Singularity containers run as the user that started them. There are no background daemons, so privilege escalation is not allowed. Singularity also bind-mounts a few directories by default (
$PWD
,
$HOME
,
/tmp
,
/proc
,
/sys
, and
/dev
). An administrator can configure additional ones that are also mounted by default on a global (i.e., host) basis, and the end user can (optionally) also bind arbitrary ones at runtime. Of course, standard Unix permissions apply, so this still doesn't allow unrestricted access to host files.
But what about climate change?
Oh! Of course. Back on topic. We decided to break down the bulk of simulations that we need to run on a per-project basis. Each project can then focus on a specific crop, a specific geographical area, or different crop management techniques. After all of the simulations for a specific project are completed, they are collated into a MariaDB database and visualized using an
RStudio Shiny
web app.
Image by:
Prototype Shiny app screenshot shows a nationwide run of climate change's impact on maize silage comparing current and end-of-century scenarios.
The app allows us to compare two different scenarios (reference vs. alternative) that the user can construct by choosing from a combination of variables related to the climate (including the current climate and the climate-change projections for mid-century and end of the century), the soil, and specific management techniques (like irrigation or fertilizer use). The results are displayed as raster values or differences (averages, or coefficients of variation of results per pixel) and their distribution across the area of interest.
The screenshot above shows an example of a prototype nationwide run across "arable lands" where we compare the silage maize biomass for a baseline (1985-2005) vs. future climate change (2085-2100) for the most extreme emissions scenario. In this example, we do not take into account any changes in management techniques, such as adapting sowing dates. We see that most negative effects on yield in the Southern Hemisphere occur in northern areas, while the extreme south shows positive responses. Of course, we would recommend (and you would expect) that farmers start adapting to warm temperatures starting earlier in the year and react accordingly (e.g., sowing earlier, which would reduce the negative impacts and enhance the positive ones).
Next steps
With the framework in place, all that remains is the heavy lifting. Run ALL the simulations! Of course, that is easier said than done. Our in-house cluster is a shared resource where we must compete for capacity with several other projects and teams.
Additional work is planned to further generalize how we distribute jobs across compute resources so we can leverage capacity wherever we can get it (including the public cloud if the project receives sufficient additional funding). This would mean becoming job scheduler-agnostic and solve the data gravity problem.
Work is also underway to further refine the UI and UX aspects of the web application until we are comfortable it can be published to policymakers and other interested parties.
If you are interested in our work from a scientific point of view, please
contact me
and I will put you in touch with the project leader. For all other inquiries, you can also contact me and I will do my best to help.
Eric Burgueño will present
Using containers to analyse the impact of climate change and soil on New Zealand crops
at
linux.conf.au
, January 21-25 in Christchurch, New Zealand.
What to read next
Tags
Containers
linux.conf.au
Conferences and events
Eric Burgueño
Hello there! I am an IT professional specialising in GNU/Linux and Open Source. I also have a Law degree, but computers are my true passion.
I have approximate knowledge of many things. I am a science enthusiast and an aspiring polyglot (in both human and computer lingos). I use Oxford commas and indent my code with spaces 😄.
More about me
3 Comments
These comments are closed.
Related Content
How to use Podman in GitLab Runners
3 surprising things Linux sysadmins can do with systemd
Develop on Kubernetes with open source tools
This work is licensed under a Creative Commons Attribution-Share Alike 4.0 International License.
