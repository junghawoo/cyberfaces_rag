---
title: "Create your own VM"
unit_id: 96
course_id: 3
level: "Developer"
slug: create-your-own-vm
is_course: 0
---

# Create your own VM

## Text content

### Why Virtual Machines?
There are clear benefits to VMs for the curious and tech savvy, you can explore operating systems without changing the one on your computer, weed out any malware safely, and even try out old operating systems for otherwise incompatible software. But let's say you aren't interested in those things, can VMs still help you? Yes! One of the main reasons virtual machines are so well used is they are very portable, able to transfer to whatever system can run it. This is great for projects between multiple people or businesses changing computers, as the hardware can change without any of the contents. Lately, however, this ability has been overshadowed by Docker.
Listed below is how you can create your very own virtual machine to try for yourself. I recommend Linux (specifically I show Ubuntu), and to learn more about Linux check out Module 2.

## Fetched resources (external URLs)

### Beginner Geek: How to Create and Use Virtual Machines (link)
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

### Virtual Box (link)
*URL:* https://www.virtualbox.org/

# Oracle VirtualBox

Oracle VirtualBox
Search:
wiki:
WikiStart
Home
Download
Documentation
Community
Welcome to VirtualBox.org!
Powerful open source virtualization
For personal and enterprise use
VirtualBox is a general-purpose full virtualization software for x86_64 hardware (with version 7.1 additionally for macOS/Arm and with version 7.2 also for Windows/Arm), targeted at laptop, desktop, server and embedded use.
Get Started
Download
Download VirtualBox binaries and platform packages
Community
Become a part of the VirtualBox community. Discuss and solve problems in the forums, access test builds, and more.
Documentation
Learn from a variety of resources including user manuals, end-user and technical documentation, the source code repository timeline, or the changelog.
Training
Access labs, tutorials, and videos to learn how to use VirtualBox. Quizzes are available to test your learning.
Join the VirtualBox community
Millions of users actively use VirtualBox
VirtualBox is a community effort backed by Oracle. Everyone is encouraged to contribute. Oracle helps ensure the product meets professional quality criteria and offers support resources for users.
How to Contribute
Past Contributions
Oracle Support
Recent releases
New
June 30th, 2026
VirtualBox 7.2.12
Oracle today released a 7.2 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
June 16th, 2026
VirtualBox 7.2.10
Oracle today released a 7.2 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
April 21st, 2026
VirtualBox 7.2.8
Oracle today released a 7.2 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
April 21st, 2026
VirtualBox 7.1.18
Oracle today released a 7.1 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
January 20th, 2026
VirtualBox 7.2.6
Oracle today released a 7.2 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
January 20th, 2026
VirtualBox 7.1.16
Oracle today released a 7.1 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
October 21st, 2025
VirtualBox 7.2.4
Oracle today released a 7.2 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
October 21st, 2025
VirtualBox 7.1.14
Oracle today released a 7.1 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
September 10th, 2025
VirtualBox 7.2.2
Oracle today released a 7.2 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
August 14th, 2025
VirtualBox 7.2.0
Oracle today released a significant new version of Oracle VirtualBox, its high performance, cross-platform virtualization software. See the
Changelog
for details.
New
July 15th, 2025
VirtualBox 7.1.12
Oracle today released a 7.1 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
June 3rd, 2025
VirtualBox 7.1.10
Oracle today released a 7.1 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
April 15th, 2025
VirtualBox 7.1.8
Oracle today released a 7.1 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
January 21st, 2025
VirtualBox 7.1.6
Oracle today released a 7.1 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
January 21st, 2025
VirtualBox 7.0.24
Oracle today released a 7.0 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
October 15th, 2024
VirtualBox 7.1.4
Oracle today released a 7.1 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
October 15th, 2024
VirtualBox 7.0.22
Oracle today released a 7.0 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
September 27th, 2024
VirtualBox 7.1.2
Oracle today released a 7.1 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
September 11th, 2024
VirtualBox 7.1.0
Oracle today released a significant new version of Oracle VirtualBox, its high performance, cross-platform virtualization software. See the
Changelog
for details.
New
July 16th, 2024
VirtualBox 7.0.20
Oracle today released a 7.0 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
May 3rd, 2024
VirtualBox 7.0.18
Oracle today released a 7.0 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
New
April 16th, 2024
VirtualBox 7.0.16
Oracle today released a 7.0 maintenance release which improves stability and fixes regressions. See the
Changelog
for details.
Read More
Last modified
11 hours ago
Last modified on 06/30/2026 06:44:15 PM
Note:
See
TracWiki
for help on using the wiki.
Download in other formats:
Plain Text
Powered by
Trac 1.4.3.2
By
Edgewall Software
.
© 2025 Oracle
Support
Privacy
/
Do Not Sell My Info
Terms of Use
Trademark Policy
Automated Access Etiquette
