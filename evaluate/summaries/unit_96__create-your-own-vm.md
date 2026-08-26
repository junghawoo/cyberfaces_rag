---
title: "Create your own VM"
unit_id: 96
course_id: 3
level: "Developer"
slug: create-your-own-vm
is_course: 0
---

# Create your own VM

Tutorial for creating and using virtual machines, covering benefits, VM software options, setup procedures, and practical applications for experimenting with operating systems and software testing.

**Source:** "Beginner Geek: How to Create and Use Virtual Machines" by Chris Hoffman (How-To Geek, Jul 13, 2017); Oracle VirtualBox (https://www.virtualbox.org/). **Related content:** Module 2 (Linux information). **Note:** Docker now overshadows traditional VM portability benefits.

## Virtual Machine Concepts and Benefits

**Virtual Machine definition:** Virtualized environment behaving like separate computer system with virtual hardware, runs as process in window on current OS. **Host:** actual OS on computer; **Guest:** OS running inside VM. **Virtual hard drive:** multi-gigabyte file on real hard drive, presented to guest OS as real hardware.

**Key benefits:** Portability across systems (transfer without hardware changes); explore operating systems without changing host system; test malware safely; run old OS versions for legacy software; sandbox software testing (prevents tampering with real system); run unsupported/insecure OSes safely (contained harm).

**Limitations:** Virtualization overhead (slower than real hardware); not ideal for demanding games or graphics-intensive applications; limited by hard drive space and system resources when running multiple VMs simultaneously.

## Virtual Machine Software Options

**VirtualBox** (Windows, Linux, macOS): Open-source, completely free, very popular, recommended starting point, particularly strong on Windows/Linux. **VMware Player** (Windows, Linux): Free basic tool, advanced features in paid VMware Workstation. **VMware Fusion** (macOS): Paid, polished integration for Mac users. **Parallels Desktop** (macOS): Paid, polished alternative for running Windows software on Mac.

**Linux:** KVM (integrated virtualization). **Windows 8/10:** Microsoft Hyper-V (Professional/Enterprise versions only; less user-friendly interface). **Other options:** Many additional VM solutions available with varying interfaces.

## VM Setup Process

**Via VirtualBox wizard:** (1) Create new VM, select OS type/version via name field (auto-detection or manual dropdown); (2) Allocate memory (changeable later); (3) Create virtual hard disk: choose dynamically allocated (grows as needed to maximum) or fixed-size (better performance, recommended); (4) Set virtual disk size; (5) Configure installation media (ISO file or physical disc); (6) Start VM.

**Key recommendation:** Fixed-size disks perform better and clarify disk space usage despite initial storage overhead.

## Advanced Resources

VirtualBox documentation: user manuals, end-user/technical documentation, source code repository, changelog, training labs, tutorials, videos, quizzes.

**Related guides:** Speeding up VMs, Hyper-V VMs, installing Android in VirtualBox, sharing computer files with VM, portable VirtualBox, VirtualBox tricks and advanced features.

## Summarized attachments
- **Beginner Geek: How to Create and Use Virtual Machines** (https://www.howtogeek.com/196060/beginner-geek-how-to-create-and-use-virtual-machines/, link): Comprehensive article by Chris Hoffman from How-To Geek explaining virtual machine concepts, benefits (OS exploration, software testing, sandboxing, legacy OS support), host vs. guest OS architecture, virtual hard drives, limitations (virtualization overhead, graphics performance), comparison of VM software options (VirtualBox, VMware Player/Fusion, Parallels Desktop, Hyper-V), and step-by-step VM setup procedures including OS selection, memory allocation, virtual disk configuration, and installation media setup.
