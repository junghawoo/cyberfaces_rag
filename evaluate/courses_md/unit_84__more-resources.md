---
title: "More Resources"
unit_id: 84
course_id: 3
level: "Developer"
slug: more-resources
is_course: 0
---

# More Resources

## Fetched resources (external URLs)

### AT&T Archives: The UNIX Operating System (link)
*URL:* https://www.youtube.com/watch?v=tc4ROCJYbm0

[YouTube transcript tc4ROCJYbm0]
the usual way to get a large computer application developed involves a big team of people working in close coordination most of the time this works surprisingly well but it does have its problems and large projects tend to get done poorly they take a long time they consume an astonishing amount of money and in many cases the individual team members are dissatisfied so everybody in the Computing business is constantly searching for ways to do a better job of developing Computer Applications there aren't likely to be any final answers both because the problems are hard and because as we find Solutions we try even more ambitious objectives but there are some things that can be done to make life easier for everybody on a large programming project a good programming environment helps a lot and in the next few minutes we're going to show you some of the properties of the Unix operating system that make it a good programming environment for many purposes in Bell Labs as in many Industries almost everyone has some kind of invol involvement with software either they are actually producing software and that is their job or they are impacted by software or they use software in fact at Bell Labs about 50% of the people are actually producing software and everyone else has some kind of involvement with it in fact that's one of our worst problems today is there is a crying need for useful software to do effective jobs we just do not have enough people to write all that software keeping large amounts of software working and keeping it working in the face of change is a big job takes a lot of skilled people to do this now software is different from Hardware when you build hardware and send it out uh you may have to fix it because it breaks but you don't demand for example that your radio suddenly turn into a television and you don't demand that a piece of Hardware suddenly do a completely different function but people do that of software all of the time there's a continual demand for changes enhancements new features that people find necessary once they get used to a system in other words we put the system out there people get used to it their jobs change they come back with more demands for different sorts of of features in the system the result is there's no way to get perfect requirements in the first place and that means that we have to build the software to be very change tolerant because we do not want to throw the software away the year after we wrote it there are a couple ways to do that one is to make the software fairly clear and easy to read and understand and change and you do that with some of the current popular structured programming techniques another way is to write many many small modules of code that way when you have a change perhaps you only throw out a few small modules or make changes in a few modules rather than in thousands and thousands of lines of code what we should be doing in the Computing business is trying to raise the level at which we work so that a programmer can write a few lines of code that turn into many many instructions in the machine that way when changes need to be made one just changes a few lines of code rather than thousands and thousands of them in the mythical man month Fred Brooks estimates that it took 5,000 staff years of effort to produce the operating system for IBM's 360 series computer clearly nobody is going to do that sort of thing very often certainly not for every new type of Hardware or for every new class of application someone once said that software stands between the user and the Machine and to me this conveys this picture of a Great Wall of software up there that you have to overcome to get anything done there's certainly a grain of Truth in the remark anyway um if you stop to look many many operating systems seem to spend a substantial fraction of their time and effort not in helping you but in impeding you in in making your job difficult sort of providing obstacles to be overcome when Ken Thompson and Dennis Richie started building the Unix system in 1969 they found a structure which simplified many aspects of the interactions between computers and people Thompson and Richie were aiming to keep their system simple and they found a collection of Primitives that enable them to do a great deal with a very few Primitives a Unix system is made up sort of of three three layers if you like the central layer the kernel is the thing that controls the resources of the machine then wrapped around that at least in conceptually is something called the shell which is the interface between most users and the kernel part it sits there and waits for you to type commands at it and then it interprets them and then around that sort of yet another layer are useful programs things like editors and compilers for programming languages and document formatting programs and programs that you write yourself and what you can do is to think of these Unix system programs basically as in some sense the building blocks with which you can create things and the thing that distinguishes Unix system from many other system is the degree to which those building blocks can be glued together in a variety of different ways not just obvious ways but in many cases very unobvious ways to get different jobs done uh the system is very flexible in that respect I I think the notion of pipeline is the fundamental contribution of the system is you can take a bunch of programs two or more programs and stick them together end to end so that the data simply flows from the one on the left to the one on the right and the system itself looks after all of the connections all of the synchronization making sure that the data goes from the one into the other the programs themselves don't know anything about the connection as far as they're concerned they're just talking to the terminal now let me give you an example um of how this works in practice the system as I mentioned is used a lot for Document Preparation kinds of things uh programs for helping you type letters or produce technical papers or write books in all of those things of course people when they're typing in the machine make spelling mistakes so let's see how we could use some of these building block Notions in practice to help you develop a program for finding spelling mistakes suppose I take a sentence this is a sentence which is in a paper that John mashy and I wrote um some years ago now if you look at it carefully you'll see that there are actually a couple of spelling mistakes in there now suppose that we wanted to find the spelling mistakes using a machine how would we do that well basically what we would do the simplest thing I can think of is to split the the sentence there into words individual words and then compare the words against a dictionary and every time we find a word which is in that sentence but not in a dictionary it's at least a plausible Contender for being a spelling mistake now how do we do that what I want to show is that you can do that using just existing Unix programs just gluing them together to get the job done suppose that we say first we'll take a program called make words and we'll run that on the sentence now what that does is to break the thing up into one word per line now I'll take the output and I'll pipe it into another program which will simply convert it into lower case the reason I want to convert it into lower case is that my dictionary doesn't have any capitalizations and so words like Bell and Unix which are capitalized here would show up as spelling mistakes unless I did this now the next thing that I want to do my dictionary is in fact sorted in alphabetical order as dictionaries are and so it's a lot easier for me to compare the words of my document to the words in the dictionary if they're sorted so I'm going to run them into sort and finally if you look at it carefully it doesn't show up very easily here but the there are in fact there is a duplicate word there systems appears twice and in a real document words like th would show up many times so we'd like to get rid of duplicates so let's throw that through another program called unique so what we've got so far is we've got the words of my document in this case the sentence one word per line in lower case neatly sorted and all of the duplicate words thrown away so there's only one word one instance of each different word and then what I'm going to do is run it into one last program called mismatch which will simply print all of the words that came down this Pipeline and print out the ones that were in the document that we in the dictionary so what we have here is five separate programs cooperating to do this job and in one giant pipeline now if you look at the list that came out you'll see that indeed we got Laboratories and provide which were our two spelling mistakes of course we got two other words as well and this tells you not only what what's good about the approach but also what's bad about it um time sharing is not a spelling mistake but it's a perfectly fine example of technical jargon the sort of thing that means something to everybody in the computer business it means nothing whatsoever to people who are not computer types and the word Unix is a fine example of something that's not going to be found in a normal dictionary so what do we do First We Take the misspelled words and we go back to the original document and we correct them so we don't have any spelling mistakes secondly we take the words that like time sharing and Unix that are not spelling mistakes but which showed up here and we put them back into our dictionary so that the next time somebody has a document that contains Unix or time sharing they don't show up at spelling mistakes so we've not only done our own job but we've improved the tool that we're using in the process so you notice that I did that whole job without writing any programs at all the whole thing is cobbled together out of programs that already existed and all I did was to use the fact that the system provides this mechanism of the pipe pipeline so I can take programs and stick them together one after another to get my job done and I think this is one of the reasons why the system is so productive that there's a large collection of things that people have already built that we use and as we build our new things then they become part of the repertoire of things that people subsequently can build on during the last decade we have discovered a number of new powerful pattern matching algorithms that are useful for ating patterns in text many of these algorithms have been developed using insights obtained from Theory obtained by studying automa and language Theory as our knowledge of pattern matching algorithms increases we can very quickly take this knowledge and package it in the form of Unix programs and we can spread these Unix programs to the entire Community very quickly Unix systems has many features which make it easier for the programmer to write programs these include format lless files the hierarchical directory structure the ability to pipeline the output of one command as the input of another device independent IO all of these things make programming considerably easier than on most other systems the heart of the system is really the file system the the ability to store information for extended periods of time and the reason one of the reasons the system works as well as it does is that the file system is well-designed and many systems you have to say an awful lot about a file before you can do anything with it you have to say where it is and how big it is and what kind of information it's going to that's going to be in it all kinds of things that are basically utterly completely irrelevant here you don't have to do any of that a file is as big as it is it doesn't matter where it is as long as you know what it's called and so you basically don't have to think of any of those complexities that you have in other systems when you want information in the file you put it there when you want it back you get it out again and you don't have to think about size or number of Records or number of fields or anything like that unless it's really gerain to your program for most purposes it's utterly irrelevant a file is simply a sequence of btes its main attribute is its size by contrast in more conventional systems uh file has dozen or so attributes to specify or create a file it takes endless amounts of chitchat if you want a Unix system file you simply ask for a file and you can use it interchangeably wherever you want to file the Unix system consists of a hierarchy of directories which a directory is simply a file that contains the names of either other directories or files and this whole thing goes on recur cursively when you log into a Unix system you normally are sitting in a place that's called your home directory or users directory and I can say PWD which means print the name of my working directory and it'll tell me where I am it says at the moment that I'm in user bwk that's where I start when I log in now I can go up a level in that I can change to parent level and now if I print my working directory I'm in/ user and I can go up one more level to the root of the whole file system let me go back down to bwk and I can list the direct the files that I have in that directory and I find there among other things a directory called TV and I can list the files that are there and I'll find among other things the sentence that we printed in the spelling mistake finding program let me look at that and sure enough there it is so as you can see the file system hierarchy makes it possible for users to organize information into its natural grouping and to go up or down and find things quickly and easily the Unix system interface for most people is through a program called the shell or the command interpreter basically it's simply a program that watches what you type and treats it as request to run particular programs now there's nothing magic about running programs the programs that you run are actually just the names of files in the file system the shell searches in the file system in a particular way to find a file whose name is the name of the program that you think you're running and it goes and executes it and in fact it's not possible for you as a user just by executing a program to tell how that particular program has been implemented for example it might have been written in a language like Fortran or C or it may have in fact been written as something like the spell program that we talked about earlier which is a combination of other programs stuck together with pipes or some similar thing and all put in a single file as a shell sequence or sequence of commands what Brian did earlier was he typed all the commands the the five program names uh for his spelling checker on one line using the pipeline facilities now that's nice except that you may want to check documents uh often and you don't want to have to type that long sequence of commands so it's possible to put all of these commands in a file and tell the shell when uh I type the name of that file I want you to execute the commands that are inside that file let me show you an example of this we have a program called spline which uh fits uh curves to a set of data points and I've got a set of five data points that we're going to see what the curve looks like I'm going to run spline through uh a program that turns uh this into graphics called graph and I'm going to run that through a special program that turns the graphic language into uh something specific for this terminal I only need to type plot and data because inside the file plot is this string of commands and here is a result of plotting those five data points on this particular terminal the ability to put commands in files and only have to type the file name to get these commands executed makes the Computing business a lot easier often you're doing things that are repetitive and you don't want to have to type uh long lists of things this makes our life much easier and allows us to tailor our environment for the way we want to work another nice feature of the Unix programming environment is the concept of input output redirection normally when you type a command the output from it goes to your terminal and the input comes from your keyboard however the shell can be told by a simple notation that when you run a program you wish the output to be directed into a file or that the input be taken from a file for example to print the output of my spelling program on the line printer instead of putting it on my terminal all I have to do is say my spell sentence greater than device line printer rather than my spell sentence and the output goes into a file what looks like a file except that it's actually a file that causes the line printer to spring into action and print my three or four spelling mistakes on the line printer on many systems redirection of input and output is literally impossible because the programs have wired into them the notion that they have to read or write the user's terminal and there's simply no way to convince them otherwise they have to do that here that is not the case here any program can have its input or output redirected because the input and output redirection is handled not by the individual program but by the sh and so that way it applies to all programs without any exception at all and in fact this goes a little further than you might expect because not only are parts of the disk files as they are in other systems but in addition the iio devices the peripheral devices connected to the computer are also files in the file system for example the line printer and the tape drive and even the thing that dials telephone numbers are all devices in the file system and the same program that will copy information from one dis file to another dis file will also copy information from a dis file to the line printer or from the Magnetic Tape drive to the printer the same program exactly a good operating system is easiest for a programmer to use if the programming language fits with the style of the system so along the way in the course of the unic system development Dennis Richie created the C language C is a very nice highlevel language with many of the modern programming constructs in it the thing that's very important about it is that it lets you avoid the details of the machine when you want to but when you need to and sometimes when you're writing an operating system you really do need to you can get at the details of the machine and control everything but you're not forced to do that and that's important because that means you can write operating systems in this language and still have something that can be portable to other machines the Unix system has been moved to many many different kinds of computers again that means that people can ignore the details of what a machine is underneath and get on with their job now so at that level C is by far the favorite language at the next level the shell programming language is very popular in fact on some machines people find that the shell meets all of their programming needs they are writing lots of procedures to help them manage their work they don't even have to go to a language at the level of of C as it happens though because the system is such a pleasant programming environment programmers all over the world have imported or added their own languages so for instance you can find Fortran algol lisp basic in fact almost any language you can think of exists on some Unix system somewhere what's important about the uni system is not so much what Richie and Thompson put into it as what they were able to leave out of it rather than produce a large number of Primitives each one complex they were able to choose a small number of simple Primitives which could be fitted naturally together to accomplish complex tasks this structure of the operating system makes it natural and easy for people who create applications to produce applications in that same style for example as the scale of integration of silicon circuits gets ever larger here we find it necessary to have more and more sophisticated design aids to help people create large-scale integrated circuits our existing design AIDS are Advanced and effective but advances in vsi create a need for even better tools rather than produce those tools in the form of one humongous program designed to do everything the people here have been producing small packages each design to do some individual function that's helpful in the design of integrated circuits then these individual packages can be combined using shell procedures to design a part of a circuit or a circuit and the parts of a circuit can be combined to make a whole circuit Steve Johnson is one of the people who has been involved in this effort he is currently working on a program called algen which takes Boolean equations as input and produces logic circuit designs as output because tool building is such a way of life on the Unix system over the years we've developed tools that actually help us make other tools these involve things like parser generators lexical analyzer generators and other programs that help us uh organize and develop tools uh these tools have been used in the development of lgen and many other applications here we see the Boolean equations for a simple dat down here we have the equations for for the carry out and the sum in the middle we have some descriptions as to how we would like the cell to be laid out geometrically you see we would like the two inputs on the left side the carry in on the bottom the carry out on the top and the output on the right side the input equations first have to be processed so that they can be more easily represented in Silicon this process is very similar to recognizing common sub expressions in the input of a compiler input language the Boolean equations are read and processed by a program called Yak which was originally developed to help us build compilers but has in fact been used in a large number of application programs as well Yak is based on the theory of LR one parsing uh represents it builds a small finite State machine uh which is able to control the actions of the program which reads the input detect errors accurately and structure the input in such a way that the program can then go ahead and and perform its uh operations on it and after these equations have been processed it's then necessary to worry about the geometric layout of the circuit uh this is done in the next two portions of Elgen the first program worries about the ordering of these columns uh it uses a technique called graph partitioning to attempt to iteratively come up with a good solution to what is in fact an extremely difficult problem in theory after the columns have been ordered then the tracks where the signals run are laid out as well by another program and finally in some sense we now have the circuit designed and it's simply a question of realizing it with the particular rules for our fabrication process uh and that is done by a fourth program so once again we we have an example of taking a very complex problem dividing it into pieces representing each piece with a separate program and then using the facilities of the Unix system to glue the pieces together into a coherent hole again Computing is going to be more and more interwoven with people's lives as the years go by so computer technology is going to have to evolve to be easier for people to use the uni system is not the End of the Road in this regard but I think it's a good step along the way

### Advantage of Linux (link)
*URL:* https://www.educba.com/advantage-of-linux/

# Advantages of Linux | Top 18 Important Advantages Of Linux

Advantages of Linux | Top 18 Important Advantages Of Linux
Home
Software Development
Software Development Tutorials
Linux Tutorial
Advantages of Linux
Advantages of Linux
Article by
Priya Pedamkar
Introduction to Advantages of Linux
Linux is an operating system like Windows; Mac OS X was developed by Linus Torvalds in 1991. The operating system is the interface between the software and the hardware. It provides services for applications and manages computer hardware. Initially, Linux was just an operating system, but now it has become the platform to run desktops, embedded systems, and servers. It was developed as an alternative to Minix (a UNIX clone by Andrew S. Tanenbaum).
Linux has many variations and distributions because of its modular design. A kernel is at the base or core of the Linux system. It schedules applications or processes, manages basic peripheral devices, handles network access and oversees file system services. Linux provides many advantages over other operating systems, so it is used almost in every field nowadays, from smartphones to supercomputers, cars to home appliances.
Watch our Demo Courses and Videos
Valuation, Hadoop, Excel, Mobile Apps, Web Development & many more.
Advantages of Linux
Let us now discuss some of the advantages of Linux:
1. Open Source
One of the main advantages of Linux is that it is an open-source operating system,m, i.e. its source code is easily available to everyone. Anyone capable of coding can contribute, modify, enhance and distribute the code to anyone and for any purpose.
2. Security
Linux is more secure than other operating systems, such as Windows. Linux is not entirely secure, as there is some malware for it also, but it is less vulnerable than others. Every program in Linux, whether an application or a virus, needs authorization from the administrator in the form of a password. Unless the password is typed, the virus won’t execute. There is no requirement for any anti-virus program in Linux.
3. Revive Older Computer Systems
Linux helps you to use or utilize your old and outdated computer systems as a firewall, router, backup server or file server and many more. There are many distributions available to use according to your system capability. As you can use Puppy Linux for low-end systems.
4. Software Updates
In Linux, you encounter a larger number of software updates. These software updates are much faster than updates in any other operating system. Linux updates can be quickly done without facing any major issues or concerns.
5. Customization
A feature that gives a major advantage over other operating systems is customization. You can customize any element and add or delete it according to your need, as it is an open-source operating system. Also, various wallpapers and attractive icon themes can be installed to give an amazing look to your system.
6. Various Distributions
There are many distributions available, also called distros of Linux. It provides various choices or flavours to the users. You can select any bistros according to your needs. Some bistros of Linux are Fedora, Ubuntu, Arch Linux, Debian, Linux Mint and many more. If you are a beginner, you can use Ubuntu or Linux Mint. If you are a good programmer, you may use Debian or Fedora.
7. Free to Use (Low Cost)
Linux is freely available on the web to download and use. You do not need to buy the license for it as Linux and many of its software come with GNU General Public License. This proved to be one of the significant advantages Linux faces over Windows and other operating systems. You need to spend a huge amount to buy the license for Windows, which is not the case with Linux.
8. Large Community Support
Forums by excited users are made on the web to help and solve the problem any other user is facing. There are a lot of dedicated programmers there to help you out whenever and wherever possible.
9. Stability (Reliability)
Linux also provides high stability; this is a good advantage, i.e. it does not need to be rebooted after a short period. Your Linux system rarely slows down or freezes. For developers and sysadmins putting that stability to work in production,
Linux VPS hosting
is a natural next step giving you dedicated resources with full root access on a Linux environment. As in Windows, you need to reboot your system after installing or uninstalling an application or updating your software, but this is not the case with Linux. You can work without any disturbance on your Linux systems.
10. Privacy
Linux ensures the privacy of users’ data as it never collects much data from the user while using its distributions or software. However, this is not true for many other operating systems.
11. Performance
Linux provides high performance on various networks and workstations. It allows many users to work simultaneously and handles them efficiently.
12. Network Support
Linux supports network functionality as it was written by programmers over the internet. Linux helps you set up client and server systems on your computer systems easily and quickly.
13. Flexibility
Linux provides a high range of flexibility as you can install only the required components. There is no need to install a complete suite. You can also keep Linux files under multiple partitions, so there is no major loss if one corrupts. You only need to repair that particular partition, not the complete file, which is not the case with other operating systems.
14. Compatibility
Linux runs or executes all possible file formats and is compatible with many file formats.
15. Fast and Easy Installation
Linux can be easily installed from the web and does not require any prerequisites as it can run on any hardware, even your oldest systems.
16. Proper use of Hard Disk
Linux performs all the tasks efficiently even after the hard disk is almost complete. This increases the performance of Linux; hence Linux provides high performance also.
17. Multitasking
Linux is a multitasking operating system as it can perform many tasks simultaneously without decreasing speed, such as downloading a large file would not slow down the system.
18. Run Multiple Desktops
Linux provides various desktop environments to make it easy to use. While installing Linux, you can choose any desktop environment according to your wishes, such as KDE (K Desktop Environment) or GNOME (GNU Network Object Model Environment).
Recommended Articles
This has been a guide to the Advantages of Linux. Here we have discussed the introduction and different advantages of Linux, respectively. You may also look at the following articles to learn more –
Linux System Commands
Kali Linux Commands
Cheat Sheet of Linux
Linux vs Windows 10
Primary Sidebar
Loading . . .
Question:
Answer:
Quiz Result
Total Questions
Correct Answers
Wrong Answers
Percentage
Submit
Next Question
X
This website or its third-party tools use cookies, which are necessary to its functioning and required to achieve the purposes illustrated in the cookie policy. By closing this banner, scrolling this page, clicking a link or continuing to browse otherwise, you agree to our
Privacy Policy
OK
Free Software Development Course
Web development, programming languages, Software testing & others
By continuing above step, you agree to our
Terms of Use
and
Privacy Policy
.
*Please provide your correct email id. Login details for this Free course will be emailed to you
X
*Please provide your correct email id. Login details for this Free course will be emailed to you
X
EDUCBA Login
Username
Password
Forgot Password?
Submit
X
*Please provide your correct email id. Login details for this Free course will be emailed to you
X
*Please provide your correct email id. Login details for this Free course will be emailed to you
x
🚀 Limited Time Offer!
-
🎁
ENROLL NOW

### Linux Timeline (link)
*URL:* https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Linux_Distribution_Timeline.svg/170px-Linux_Distribution_Timeline.svg.png

[fetch failed: HTTP 400]

### Linux vs. Unix: What's the difference? (link)
*URL:* https://opensource.com/article/18/5/differences-between-linux-and-unix

# Linux vs. Unix: What's the difference? | Opensource.com

Linux vs. Unix: What's the difference? | Opensource.com
Skip to main content
Search
Linux vs. Unix: What's the difference?
Dive into the differences between these two operating systems that share much of the same heritage and many of the same goals.
504 readers like this.
Image by:
Opensource.com
If you are a software developer in your 20s or 30s, you've grown up in a world dominated by Linux. It has been a significant player in the data center for decades, and while it's hard to find definitive operating system market share reports, Linux's share of data center operating systems could be as high as 70%, with Windows variants carrying nearly all the remaining percentage. Developers using any major public cloud can expect the target system will run Linux. Evidence that Linux is everywhere has grown in recent years when you add in Android and Linux-based embedded systems in smartphones, TVs, automobiles, and many other devices.
Even so, most software developers, even those who have grown up during this venerable "Linux revolution" have at least heard of Unix. It sounds similar to Linux, and you've probably heard people use these terms interchangeably. Or maybe you've heard Linux called a "Unix-like" operating system.
So, what is this Unix? The caricatures speak of wizard-like "graybeards" sitting behind glowing green screens, writing C code and shell scripts, powered by old-fashioned, drip-brewed coffee. But Unix has a much richer history beyond those bearded C programmers from the 1970s. While articles detailing the history of Unix and "Unix vs. Linux" comparisons abound, this article will offer a high-level background and a list of major differences between these complementary worlds.
Unix's beginnings
The history of Unix begins at AT&T Bell Labs in the late 1960s with a small team of programmers looking to write a multi-tasking, multi-user operating system for the PDP-7. Two of the most notable members of this team at the Bell Labs research facility were Ken Thompson and Dennis Ritchie. While many of Unix's concepts were derivative of its predecessor (
Multics
), the Unix team's decision early in the 1970s to rewrite this small operating system in the C language is what separated Unix from all others. At the time, operating systems were rarely, if ever, portable. Instead, by nature of their design and low-level source language, operating systems were tightly linked to the hardware platform for which they had been authored. By refactoring Unix on the C programming language, Unix could now be ported to many hardware architectures.
In addition to this new portability, which allowed Unix to quickly expand beyond Bell Labs to other research, academic, and even commercial uses, several key of the operating system's design tenets were attractive to users and programmers. For one, Ken Thompson's
Unix philosophy
became a powerful model of modular software design and computing. The Unix philosophy recommended utilizing small, purpose-built programs in combination to do complex overall tasks. Since Unix was designed around files and pipes, this model of "piping" inputs and outputs of programs together into a linear set of operations on the input is still in vogue today. In fact, the current cloud serverless computing model owes much of its heritage to the Unix philosophy.
Rapid growth and competition
Through the late 1970s and 80s, Unix became the root of a family tree that expanded across research, academia, and a growing commercial Unix operating system business. Unix was not open source software, and the Unix source code was licensable via agreements with its owner, AT&T. The first known software license was sold to the University of Illinois in 1975.
Unix grew quickly in academia, with Berkeley becoming a significant center of activity, given Ken Thompson's sabbatical there in the '70s. With all the activity around Unix at Berkeley, a new delivery of Unix software was born: the Berkeley Software Distribution, or BSD. Initially, BSD was not an alternative to AT&T's Unix, but an add-on with additional software and capabilities. By the time 2BSD (the Second Berkeley Software Distribution) arrived in 1979, Bill Joy, a Berkeley grad student, had added now-famous programs such as
vi
and the
C shell
(/bin/csh).
In addition to BSD, which became one of the most popular branches of the Unix family, Unix's commercial offerings exploded through the 1980s and into the '90s with names like HP-UX, IBM's AIX, Sun's Solaris, Sequent, and Xenix. As the branches grew from the original root, the "
Unix wars
" began, and standardization became a new focus for the community. The POSIX standard was born in 1988, as well as other standardization follow-ons via The Open Group into the 1990s.
More Linux resources
Linux commands cheat sheet
Advanced Linux commands cheat sheet
Free online course: RHEL Technical Overview
Linux networking cheat sheet
SELinux cheat sheet
Linux common commands cheat sheet
What are Linux containers?
Our latest Linux articles
Around this time AT&T and Sun released System V Release 4 (SVR4), which was adopted by many commercial vendors. Separately, the
BSD family
of operating systems had grown over the years, leading to some open source variations that were released under the now-familiar
BSD license
. This included FreeBSD, OpenBSD, and NetBSD, each with a slightly different target market in the Unix server industry. These Unix variants continue to have some usage today, although many have seen their server market share dwindle into the single digits (or lower). BSD may have the largest install base of any modern Unix system today. Also, every Apple Mac hardware unit shipped in recent history can be claimed by BSD, as its OS X (now macOS) operating system is a BSD-derivative.
While the full history of Unix and its academic and commercial variants could take many more pages, for the sake of our article focus, let's move on to the rise of Linux.
Enter Linux
What we call the Linux operating system today is really the combination of two efforts from the early 1990s. Richard Stallman was looking to create a truly free and open source alternative to the proprietary Unix system. He was working on the utilities and programs under the name GNU, a recursive acronym meaning "GNU's not Unix!" Although there was a kernel project underway, it turned out to be difficult going, and without a kernel, the free and open source operating system dream could not be realized. It was Linus Torvald's work—producing a working and viable kernel that he called Linux—that brought the complete operating system to life. Given that Linus was using several GNU tools (e.g., the GNU Compiler Collection, or
GCC
), the marriage of the GNU tools and the Linux kernel was a perfect match.
Linux distributions came to life with the components of GNU, the Linux kernel, MIT's X-Windows GUI, and other BSD components that could be used under the open source BSD license. The early popularity of distributions like Slackware and then Red Hat gave the "common PC user" of the 1990s access to the Linux operating system and, with it, many of the proprietary Unix system capabilities and utilities they used in their work or academic lives.
Because of the free and open source standing of all the Linux components, anyone could create a Linux distribution with a bit of effort, and soon the total number of distros reached into the hundreds. Of course, many developers utilize Linux either via cloud providers or by using popular free distributions like Fedora, Canonical's Ubuntu, Debian, Arch Linux, Gentoo, and many other variants. Commercial Linux offerings, which provide support on top of the free and open source components, became viable as many enterprises, including IBM, migrated from proprietary Unix to offering middleware and software solutions atop Linux. Red Hat built a model of commercial support around Red Hat Enterprise Linux, as did German provider SUSE with SUSE Linux Enterprise Server (SLES).
Comparing Unix and Linux
So far, we've looked at the history of Unix and the rise of Linux and the GNU/Free Software Foundation underpinnings of a free and open source alternative to Unix. Let's examine the differences between these two operating systems that share much of the same heritage and many of the same goals.
From a user experience perspective, not very much is different! Much of the attraction of Linux was the operating system's availability across many hardware architectures (including the modern PC) and ability to use tools familiar to Unix system administrators and users.
Because of
POSIX
standards and compliance, software written on Unix could be compiled for a Linux operating system with a usually limited amount of porting effort. Shell scripts could be used directly on Linux in many cases. While some tools had slightly different flag/command-line options between Unix and Linux, many operated the same on both.
One side note is that the popularity of the macOS hardware and operating system as a platform for development that mainly targets Linux may be attributed to the BSD-like macOS operating system. Many tools and scripts meant for a Linux system work easily within the macOS terminal. Many open source software components available on Linux are easily available through tools like
Homebrew
.
The remaining differences between Linux and Unix are mainly related to the licensing model: open source vs. proprietary, licensed software. Also, the lack of a common kernel within Unix distributions has implications for software and hardware vendors. For Linux, a vendor can create a device driver for a specific hardware device and expect that, within reason, it will operate across most distributions. Because of the commercial and academic branches of the Unix tree, a vendor might have to write different drivers for variants of Unix and have licensing and other concerns related to access to an SDK or a distribution model for the software as a binary device driver across many Unix variants.
As both communities have matured over the past decade, many of the advancements in Linux have been adopted in the Unix world. Many GNU utilities were made available as add-ons for Unix systems where developers wanted features from GNU programs that aren't part of Unix. For example, IBM's AIX offered an AIX Toolbox for Linux Applications with hundreds of GNU software packages (like Bash, GCC, OpenLDAP, and many others) that could be added to an AIX installation to ease the transition between Linux and Unix-based AIX systems.
Proprietary Unix is still alive and well and, with many major vendors promising support for their current releases well into the 2020s, it goes without saying that Unix will be around for the foreseeable future. Also, the BSD branch of the Unix tree is open source, and NetBSD, OpenBSD, and FreeBSD all have strong user bases and open source communities that may not be as visible or active as Linux, but are holding their own in recent server share reports, with well above the proprietary Unix numbers in areas like web serving.
Where Linux has shown a significant advantage over proprietary Unix is in its availability across a vast number of hardware platforms and devices. The Raspberry Pi, popular with hobbyists and enthusiasts, is Linux-driven and has opened the door for an entire spectrum of IoT devices running Linux. We've already mentioned Android devices, autos (with Automotive Grade Linux), and smart TVs, where Linux has large market share. Every cloud provider on the planet offers virtual servers running Linux, and many of today's most popular cloud-native stacks are Linux-based, whether you're talking about container runtimes or Kubernetes or many of the serverless platforms that are gaining popularity.
One of the most revealing representations of Linux's ascendancy is Microsoft's transformation in recent years. If you told software developers a decade ago that the Windows operating system would "run Linux" in 2016, most of them would have laughed hysterically. But the existence and popularity of the Windows Subsystem for Linux (WSL), as well as more recently announced capabilities like the Windows port of Docker, including LCOW (Linux containers on Windows) support, are evidence of the impact that Linux has had—and clearly will continue to have—across the software world.
This article was originally published in May 2018 and has been updated by the editor.
What to read next
11 surprising ways you use Linux every day
What technology runs on Linux? You might be astonished to know just how often you use Linux in your daily life.
Origin stories about Unix
Brian Kernighan, one of the original Unix gurus, shares his insights into the origins of Unix and its associated technology.
6 signs you might be a Linux user
If you're a heavy Linux user, you'll probably recognize these common tendencies.
Tags
Linux
Phil Estes
Phil is a Distinguished Engineer & CTO, Container and Linux OS Architecture Strategy for the IBM Watson and Cloud Platform division. Phil is currently an OSS maintainer in the Docker (now Moby) engine project, the CNCF containerd project, and is a member of both the Open Container Initiative (OCI) Technical Oversight Board and the Moby Technical Steering Committee.
More about me
8 Comments
These comments are closed.
Related Content
What's new in GNOME 44?
5 reasons virtual machines still matter
Remove the background from an image with this Linux command
This work is licensed under a Creative Commons Attribution-Share Alike 4.0 International License.

### UNIX Introduction (link)
*URL:* http://www.ee.surrey.ac.uk/Teaching/Unix/unixintro.html

# UNIX Tutorial - Introduction

UNIX Tutorial - Introduction
UNIX Introduction
What is UNIX?
UNIX is an  operating system which was first developed in the 1960s, and has been under constant development ever since. By operating 
  system, we mean the suite of programs which make the computer work. It is a stable, multi-user, multi-tasking system for servers, desktops and laptops.
UNIX systems also have a graphical user interface (GUI) similar to Microsoft Windows which provides an easy to use environment. However, knowledge of UNIX is required for operations 
  which aren't covered by a graphical program, or for when there is no  windows 
  interface available, for example, in a telnet session.
Types of UNIX
There are many different versions of UNIX, although they share common similarities. The  most popular varieties of UNIX are  Sun Solaris,  GNU/Linux, and MacOS X.
Here in the School, we use  Solaris on our servers and workstations, and Fedora  Linux on the servers and desktop PCs.
The UNIX operating system
The UNIX operating system is made up of three parts; the kernel, the shell 
  and the programs.
The kernel
The kernel of UNIX is the hub of the operating system: it allocates time and 
  memory to programs and handles the filestore and communications in response 
  to system calls.
As an illustration of the way that the shell and the kernel work together, 
  suppose a user types
rm myfile
(which has the effect of removing 
  the file
myfile
). The shell searches the filestore for the 
  file containing the program
rm
, and then requests the kernel, through 
  system calls, to execute the program
rm
on
myfile
. When the process
rm myfile
has finished running, the shell then returns the UNIX 
  prompt % to the user, indicating that it is waiting for further commands.
The shell
The shell acts as an interface between the user and the kernel. When a user 
  logs in, the login program checks the username and password, and then starts 
  another program called the shell. The shell is a command line interpreter (CLI). 
  It interprets the commands the user types in and arranges for them to be carried 
  out. The commands are themselves programs: when they terminate, the shell gives 
  the user another prompt (% on our systems).
The adept user can customise his/her own shell, and users can use different 
  shells on the same machine. Staff and students in the school have the
tcsh shell
by default.
The tcsh shell has certain features to help the user inputting commands.
Filename Completion - By typing part of the name of a command, filename or 
  directory and pressing the [
Tab
] key, the tcsh shell will complete the rest 
  of the name automatically. If the shell finds more than one name beginning with 
  those letters you have typed, it will beep, prompting you to type a few more 
  letters before pressing the tab key again.
History - The shell keeps a list of the commands you have typed in. If you 
  need to repeat a command, use the cursor keys to scroll up and down the list 
  or type history for a list of previous commands.
Files and processes
Everything in UNIX is either a file or a process.
A process is an executing program identified by a unique PID (process identifier).
A file is a collection of data. They are created by users using text editors, 
  running compilers etc.
Examples of files:
a document (report, essay etc.)
the text of a program written in some high-level programming language
instructions comprehensible directly to the machine and incomprehensible 
    to a casual user, for example, a collection of binary digits (an executable 
    or binary file);
a directory, containing information about its contents, which may be a 
    mixture of other directories (subdirectories) and ordinary files.
The Directory Structure
All the files are grouped together in the directory structure. The file-system 
  is arranged in a hierarchical structure, like an inverted tree. The top of the 
  hierarchy is traditionally called
root
(written as a slash / )
In the diagram above, we see that the home directory of the undergraduate student
"ee51vn"
contains two sub-directories (
docs
and
pics
) and a file called
report.doc
.
The full path to the file
report.doc
is
"/home/its/ug1/ee51vn/report.doc"
Starting an UNIX terminal
To open an UNIX terminal window, click on the "Terminal" icon from Applications/Accessories menus.
An UNIX Terminal window will then appear with a  % prompt, waiting for 
  you to start entering commands.
M.Stonebank@surrey.ac.uk, © 9th October 2000

### Unix (link)
*URL:* https://en.wikipedia.org/wiki/Unix

# Unix - Wikipedia

Unix - Wikipedia
Jump to content
From Wikipedia, the free encyclopedia
Family of computer operating systems
Operating system
Unix
UNIX System III
running on a
PDP-11
simulator
Developer
Ken Thompson
,
Dennis Ritchie
,
Brian Kernighan
,
Douglas McIlroy
, and
Joe Ossanna
at
Bell Labs
Written in
C
and
assembly language
OS family
Unix
Source model
Historically
proprietary software
, while some Unix projects (including
BSD
family and
Illumos
) are
open-source
and historical Unix source code is archived.
Initial release
Development started in 1969
First manual published
internally
in November 1971
(
1971-11
)
[
1
]
Announced outside Bell Labs in October 1973
(
1973-10
)
[
2
]
Available in
English
Kernel
type
Varies;
monolithic
,
microkernel
,
hybrid
Influenced by
CTSS
,
[
3
]
Multics
Default
user interface
Command-line interface
and
Graphical
(
Wayland
and
X Window System
;
Android
SurfaceFlinger
;
macOS
Quartz
)
License
Varies; some versions are
proprietary
, others are
free/libre
or
open-source software
Official website
www
.opengroup
.org
/unix-systems
Unix
(
/
ˈ
j
uː
n
ɪ
k
s
/
ⓘ
,
YOO
-niks
; trademarked as
UNIX
) is a family of
multitasking
,
multi-user
computer
operating systems
that derive from the original
AT&T
Unix, the development of which started in 1969
[
1
]
at the
Bell Labs
research center by
Ken Thompson
,
Dennis Ritchie
, and others.
[
4
]
Initially intended for use inside the
Bell System
, AT&T
licensed
Unix to outside parties in the late 1970s, leading to a variety of both academic and commercial Unix variants from vendors including
University of California, Berkeley
(
BSD
),
Microsoft
(
Xenix
),
Sun Microsystems
(
SunOS
/
Solaris
),
HP
/
HPE
(
HP-UX
), and
IBM
(
AIX
).
The early versions of Unix, which are retrospectively referred to as "
Research Unix
", ran on computers such as the
PDP-11
and
VAX
; Unix was commonly used on
minicomputers
and
mainframes
from the 1970s onwards.
[
5
]
It distinguished itself from its predecessors as the first
portable
operating system: almost the entire operating system is written in the
C programming language
(in 1973), which allows Unix to operate on numerous platforms.
[
6
]
Unix systems are characterized by a
modular design
that is sometimes called the "
Unix philosophy
". According to this philosophy, the operating system should provide a set of simple tools, each of which performs a limited, well-defined function.
[
7
]
A unified and
inode
-based
filesystem
and an
inter-process communication
mechanism known as "
pipes
" serve as the main means of communication,
[
4
]
and a
shell
scripting and command language (the
Unix shell
) is used to combine the tools to perform complex workflows.
Version 7
in 1979 was the final widely released Research Unix, after which AT&T sold
UNIX System III
, based on Version 7, commercially in 1982; to avoid confusion between the Unix variants, AT&T combined various versions developed by others and released it as
UNIX System V
in 1983. However as these were closed-source, the University of California, Berkeley continued developing BSD as an alternative. Other vendors that were beginning to create commercialized versions of Unix would base their version on either System V (like
Silicon Graphics
's
IRIX
) or BSD (like SunOS). Amid the "
Unix wars
" of standardization, AT&T alongside Sun merged System V, BSD,
SunOS
and
Xenix
, solidifying their features into one package as
UNIX System V Release 4
(SVR4) in 1989, and it was commercialized by
Unix System Laboratories
, an AT&T spinoff.
[
8
]
[
9
]
A rival Unix by other vendors was released as
OSF/1
, however most commercial Unix vendors eventually changed their distributions to be based on SVR4 with BSD features added on top.
AT&T sold Unix to
Novell
in 1992, who later sold the UNIX trademark to a new industry consortium called
The Open Group
in 1993,
[
10
]
allowing the use of the mark for certified operating systems that comply with the
Single UNIX Specification
(SUS).
[
8
]
Since the 1990s, Unix systems have appeared on
home computers
:
BSD/OS
was the first to be commercialized for
i386
computers and since then free
Unix-like
clones of existing systems have been developed, such as
FreeBSD
and the combination of
Linux
and
GNU
, the latter of which have since eclipsed Unix in popularity. Unix was, until 2005, the most widely used
server
operating system.
[
11
]
However in the present day, Unix distributions like
IBM AIX
,
Oracle Solaris
and
OpenServer
continue to be widely used in certain fields.
[
12
]
[
13
]
Overview
[
edit
]
Version 7 Unix
, the
Research Unix
ancestor of all modern Unix systems
Unix was originally meant to be a convenient platform for programmers developing software to be run on it and on other systems, rather than for non-programmers.
[
14
]
[
15
]
[
16
]
The system grew larger as the operating system started spreading in academic circles, and as users added their own tools to the system and shared them with colleagues.
[
17
]
At first, Unix was not designed to support
multi-tasking
[
18
]
or to be
portable
.
[
6
]
Later, Unix gradually gained multi-tasking and
multi-user
capabilities in a
time-sharing
configuration, as well as portability. Unix systems are characterized by various concepts: the use of
plain text
for storing data; a
hierarchical file system
; treating devices and certain types of
inter-process communication
(IPC) as files; and the use of a large number of
software tools
, small programs that can be strung together through a
command-line interpreter
using
pipes
, as opposed to using a single monolithic program that includes all of the same functionality. These concepts are collectively known as the "
Unix philosophy
".
Brian Kernighan
and
Rob Pike
summarize this in
The Unix Programming Environment
as "the idea that the power of a system comes more from the relationships among programs than from the programs themselves".
[
19
]
By the early 1980s, users began seeing Unix as a potential universal operating system, suitable for computers of all sizes.
[
20
]
[
21
]
The Unix environment and the
client–server
program model were essential elements in the development of the
Internet
and the reshaping of computing as centered in
networks
rather than in individual computers.
Both Unix and the
C programming language
were developed by AT&T and distributed to government and academic institutions, which led to them both being ported to a wider variety of machine families than any other operating system.
The Unix operating system consists of many libraries and utilities along with the master control program, the
kernel
. The kernel provides services to start and stop programs, handles the
file system
and other common "low-level" tasks that most programs share, and schedules access to avoid conflicts when programs try to access the same resource or device simultaneously. To mediate such access, the kernel has special rights, reflected in the distinction of
kernel space
from
user space
, the latter being a lower priority realm where most application programs operate.
History
[
edit
]
Main article:
History of Unix
The origins of Unix date back to the mid-1960s when the
Massachusetts Institute of Technology
,
Bell Labs
, and
General Electric
were developing
Multics
, a
time-sharing
operating system for the
GE 645
mainframe computer.
[
22
]
Multics featured
several innovations
, but also presented severe problems. Frustrated by the size and complexity of Multics, but not by its goals, individual researchers at Bell Labs started withdrawing from the project. The last to leave were
Ken Thompson
,
Dennis Ritchie
,
Douglas McIlroy
, and
Joe Ossanna
,
[
18
]
who decided to reimplement their experiences in a new project of smaller scale. This new operating system was initially without organizational backing, and also without a name.
The new operating system was a single-tasking system.
[
18
]
In 1970, the group coined the name
Unics
for
Uniplexed Information and Computing Service
as a
pun
on
Multics
, which stood for
Multiplexed Information and Computer Services
.
Brian Kernighan
takes credit for the idea, but adds that "no one can remember" the origin of the final spelling
Unix
.
[
23
]
Dennis Ritchie,
[
18
]
Doug McIlroy,
[
1
]
and
Peter G. Neumann
[
24
]
also credit Kernighan.
The operating system was originally written in
PDP-7
assembly language
, and ported to
PDP-11
assembly language in 1970, but in 1973, Version 4 Unix was rewritten in
C
.
Ken Thompson
faced multiple challenges attempting the kernel port due to the evolving state of C, which lacked key features like structures at the time.
[
18
]
[
25
]
Version 4 Unix, however, still had much PDP-11 specific code, and was not suitable for porting. The first port to another platform was a port of Version 6, made four years later (1977) at the
University of Wollongong
for the
Interdata 7/32
,
[
26
]
followed by a Bell Labs port of Version 7 to the
Interdata 8/32
during 1977 and 1978.
[
27
]
In 2026, a previously unknown magnetic tape containing Version 4 Unix was discovered at the University of Utah and recovered successfully at the Computer History Museum in California. The tape represents the earliest known surviving distribution of Version 4 and provides additional insight into the early development of Unix.
[
28
]
Bell Labs produced several versions of Unix that are collectively referred to as
Research Unix
. In 1975, the first source license for
UNIX
was sold to
Donald B. Gillies
at the
University of Illinois Urbana–Champaign
(UIUC) Department of Computer Science.
[
29
]
During the late 1970s and early 1980s, the influence of Unix in academic circles led to large-scale adoption of Unix (BSD and System V) by commercial startups, which in turn led to Unix fragmenting into multiple, similar – but often slightly and mutually incompatible – systems including
DYNIX
,
HP-UX
,
SunOS
/
Solaris
,
AIX
, and
Xenix
. In the late 1980s, AT&T
Unix System Laboratories
and
Sun Microsystems
developed System V Release 4 (SVR4), which was subsequently adopted by many commercial Unix vendors.
In the 1990s, Unix and
Unix-like
systems grew in popularity and became the operating system of choice for
over 90% of the world's top 500 fastest supercomputers
,
[
30
]
as BSD and
Linux
distributions were developed through collaboration by a worldwide network of programmers. In 2000,
Apple
released
Darwin
, also a Unix system, which became the core of the Mac OS X operating system, later renamed
macOS
.
[
31
]
Unix-like operating systems are widely used in modern
servers
,
workstations
, and
mobile devices
.
[
32
]
Standards
[
edit
]
The
Common Desktop Environment
(CDE), part of the
COSE initiative
In the late 1980s, an open operating system standardization effort now known as
POSIX
provided a common baseline for all operating systems;
IEEE
based POSIX around the common structure of the major competing variants of the Unix system, publishing the first POSIX standard in 1988. In the early 1990s, a separate but very similar effort was started by an industry consortium, the
Common Open Software Environment
(COSE) initiative, which eventually became the
Single UNIX Specification
(SUS) administered by
The Open Group
. Starting in 1998, the Open Group and IEEE started the
Austin Group
, to provide a common definition of POSIX and the Single UNIX Specification, which, by 2008, had become the Open Group Base Specification.
In 1999, in an effort towards compatibility, several Unix system vendors agreed on SVR4's
Executable and Linkable Format
(ELF) as the standard for binary and object code files. The common format allows substantial binary compatibility among different Unix systems operating on the same CPU architecture.
The
Filesystem Hierarchy Standard
was created to provide a reference directory layout for
Unix-like
operating systems; it has mainly been used in Linux.
Components
[
edit
]
See also:
List of Unix commands
This section
needs
more citations
.
Please help
improve this article
by
adding citations to reliable sources
in this section. Unsourced material may be challenged and removed.
Find sources:
"Unix"
–
news
·
newspapers
·
books
·
scholar
·
JSTOR
(
October 2023
)
(
Learn how and when to remove this message
)
The Unix system is composed of several components that were originally packaged together. By including the development environment, libraries, documents and the portable, modifiable source code for all of these components, in addition to the
kernel
of an operating system, Unix was a self-contained software system. This was one of the key reasons it emerged as an important teaching and learning tool and has had a broad influence. See
§ Impact
, below.
The inclusion of these components did not make the system large –  the original V7 UNIX distribution, consisting of copies of all of the compiled binaries plus all of the source code and documentation occupied less than 10 MB and arrived on a single nine-track
magnetic tape
, earning its reputation as a portable system.
[
33
]
The printed documentation, typeset from the online sources, was contained in two volumes.
The names and filesystem locations of the Unix components have changed substantially across the history of the system. Nonetheless, the V7 implementation has the canonical early structure:
Kernel
–  source code in /usr/sys, composed of several sub-components:
conf
–  configuration and machine-dependent parts, including boot code
dev
–  device drivers for control of hardware (and some pseudo-hardware)
sys
–  operating system "kernel", handling memory management, process scheduling, system calls, etc.
h
–  header files, defining key structures within the system and important system-specific invariables
Development environment
–  early versions of Unix contained a development environment sufficient to recreate the entire system from source code:
ed
–  text editor, for creating source code files
cc
–
C language
compiler (first appeared in V3 Unix)
as
–  machine-language assembler for the machine
ld
–
linker
, for combining object files
lib
–  object-code libraries (installed in /lib or /usr/lib).
libc
, the system library with C run-time support, was the primary library, but there have always been additional libraries for things such as mathematical functions (
libm
) or database access. V7 Unix introduced the first version of the modern "Standard I/O" library
stdio
as part of the system library. Later implementations increased the number of libraries significantly.
make
–  build manager (introduced in
PWB/UNIX
), for effectively automating the build process
include
–  header files for software development, defining standard interfaces and system invariants
Other languages
–  V7 Unix contained a Fortran-77 compiler, a programmable arbitrary-precision calculator (
bc
,
dc
), and the
awk
scripting language; later versions and implementations contain many other language compilers and toolsets. Early BSD releases included
Pascal
tools, and many modern Unix systems also include the
GNU Compiler Collection
as well as or instead of a proprietary compiler system.
Other tools
–  including an object-code archive manager (
ar
), symbol-table lister (
nm
), compiler-development tools (e.g.,
lex
&
yacc
), and debugging tools.
Commands
–  Unix makes little distinction between commands (user-level programs) for system operation and maintenance (e.g.,
cron
), commands of general utility (e.g.,
grep
), and more general-purpose applications such as the text formatting and typesetting package. Nonetheless, some major categories are:
sh
–  the "shell" programmable
command-line interpreter
, the primary user interface on Unix before window systems appeared, and even afterward (within a "command window").
Utilities
–  the core toolkit of the Unix command set, including
cp
,
ls
,
grep
,
find
and many others. Subcategories include:
System utilities
–  administrative tools such as
mkfs
,
fsck
, and many others.
User utilities
–  environment management tools such as
passwd
,
kill
, and others.
Document formatting
–  Unix systems were used from the outset for document preparation and typesetting systems, and included many related programs such as
nroff
,
troff
,
tbl
,
eqn
,
refer
, and
pic
. Some modern Unix systems also include packages such as
TeX
and
Ghostscript
.
Graphics
–  the
plot
subsystem provided facilities for producing simple vector plots in a device-independent format, with device-specific interpreters to display such files. Modern Unix systems also generally include
X11
, and, in newer systems,
Wayland
, as a windowing system and
GUI
;
macOS
includes its own window system,
Quartz
. Many modern Unix systems support
OpenGL
and, in newer systems,
Vulkan
or, in macOS,
Metal
.
Communications
–  early Unix systems contained no inter-system communication, but did include the inter-user communication programs
mail
and
write
. V7 introduced the early inter-system communication system
UUCP
, and systems beginning with BSD release 4.1c included
TCP/IP
utilities.
Documentation
–  Unix was one of the first operating systems to include all of its documentation online in machine-readable form.
[
34
]
The documentation included:
man
–  manual pages for each command, library component,
system call
, header file, etc.
doc
–  longer documents detailing major subsystems, such as the C language and troff
Impact
[
edit
]
See also:
Unix-like
Ken Thompson
and
Dennis Ritchie
, principal developers of
Research Unix
Photo from
USENIX
1984, including
Dennis Ritchie
(center)
The Unix system had a significant impact on other operating systems. It achieved its reputation by its interactivity, by providing the software at a nominal fee for educational use, by running on inexpensive hardware, and by being easy to adapt and move to different machines. Unix was originally written in
assembly language
, but was soon rewritten in
C
, a
high-level programming language
.
[
35
]
Although this followed the lead of
CTSS
,
Multics
and
Burroughs MCP
, it was Unix that popularized the idea.
Unix had a drastically simplified file model compared to many contemporary operating systems: treating all kinds of files as simple byte arrays. The file system hierarchy contained machine services and devices (such as
printers
,
terminals
, or
disk drives
), providing a uniform interface, but at the expense of occasionally requiring additional mechanisms such as
ioctl
and mode flags to access features of the hardware that did not fit the simple "stream of bytes" model. The
Plan 9
operating system pushed this model even further and eliminated the need for additional mechanisms.
Unix also popularized the hierarchical file system with arbitrarily nested subdirectories, originally introduced by Multics. Other common operating systems of the era had ways to divide a storage device into multiple directories or sections, but they had a fixed number of levels, often only one level. Several major proprietary operating systems eventually added recursive subdirectory capabilities also patterned after Multics. DEC's
RSX-11M
's "group, user" hierarchy evolved into
OpenVMS
directories,
CP/M
's volumes evolved into
MS-DOS
2.0+ subdirectories, and HP's
MPE
group.account hierarchy and IBM's
SSP
and
OS/400
library systems were folded into broader POSIX file systems.
Making the command interpreter an ordinary user-level program, with additional commands provided as separate programs, was another Multics innovation popularized by Unix. The
Unix shell
used the same language for interactive commands as for scripting (
shell scripts
– there was no separate job control language like IBM's
JCL
). Since the shell and OS commands were "just another program", the user could choose (or even write) their own shell. New commands could be added without changing the shell itself. Unix's innovative command-line syntax for creating modular chains of producer-consumer processes (
pipelines
) made a powerful programming paradigm (
coroutines
) widely available. Many later command-line interpreters have been inspired by the Unix shell.
A fundamental simplifying assumption of Unix was its focus on
newline
-
delimited
text for nearly all file formats. There were no "binary" editors in the original version of Unix – the entire system was configured using textual shell command scripts. The common denominator in the I/O system was the byte – unlike
"record-based" file systems
. The focus on text for representing nearly everything made Unix pipes especially useful and encouraged the development of simple, general tools that could easily be combined to perform more complicated
ad hoc
tasks. The focus on text and bytes made the system far more scalable and portable than other systems. Over time, text-based applications have also proven popular in application areas, such as printing languages (
PostScript
,
ODF
), and at the application layer of the
Internet protocols
, e.g.,
FTP
,
SMTP
,
HTTP
,
SOAP
, and
SIP
.
Unix popularized a syntax for
regular expressions
that found widespread use. The Unix programming interface became the basis for a widely implemented operating system interface standard (POSIX, see above). The
C programming language
soon spread beyond Unix, and is now ubiquitous in systems and applications programming.
Early Unix developers were important in bringing the concepts of
modularity
and
reusability
into
software engineering
practice, spawning a "software tools" movement. Over time, the leading developers of Unix (and programs that ran on it) established a set of cultural norms for developing software, norms which became as important and influential as the technology of Unix itself; this has been termed the
Unix philosophy
.
The
TCP/IP networking protocols
were quickly implemented on the Unix versions widely used on relatively inexpensive computers, which contributed to the
Internet
explosion of worldwide, real-time connectivity and formed the basis for implementations on many other platforms.
The Unix policy of extensive on-line documentation and (for many years) ready access to all system source code raised programmer expectations, and contributed to the launch of the
free software movement
in 1983.
Free Unix and Unix-like variants
[
edit
]
See also:
Operating system § Unix and Unix-like operating systems
Console screenshots of
Debian
(top, a popular
Linux distribution
) and
FreeBSD
(bottom, a popular
Unix-like
operating system)
In 1983,
Richard Stallman
announced the
GNU
(short for "GNU's Not Unix") project, an ambitious effort to create a
free software
Unix-like
system – "free" in the sense that everyone who received a copy would be free to use, study, modify, and redistribute it. The GNU project's own kernel development project,
GNU Hurd
, had not yet produced a working kernel, but in 1991
Linus Torvalds
released the
Linux kernel
as free software under the
GNU General Public License
. In addition to their use in the
GNU
operating system, many GNU packages – such as the
GNU Compiler Collection
(and the rest of the
GNU toolchain
), the
GNU C library
and the
GNU Core Utilities
– have gone on to play central roles in other free Unix systems as well.
Linux distributions
, consisting of the Linux kernel and large collections of compatible software, have become popular both with individual users and in business. Popular distributions include
Red Hat Enterprise Linux
,
Fedora
,
SUSE Linux Enterprise
,
openSUSE
,
Debian
,
Ubuntu
,
Linux Mint
,
Slackware Linux
,
Arch Linux
and
Gentoo
.
[
36
]
A free derivative of BSD Unix,
386BSD
, was released in 1992 and led to the
NetBSD
and
FreeBSD
projects. With the 1994 settlement of a lawsuit brought against the University of California and Berkeley Software Design Inc. (
USL v. BSDi
) by
Unix System Laboratories
, it was clarified that Berkeley had the right to distribute BSD Unix for free if it so desired. Since then, BSD Unix has been developed in several different product branches, including
OpenBSD
and
DragonFly BSD
.
Because of the modular design of the Unix model, sharing components is relatively common: most or all Unix and Unix-like systems include at least some BSD code, while some include GNU utilities in their distributions. Linux and BSD Unix are increasingly filling market needs traditionally served by proprietary Unix operating systems, expanding into new markets such as the
consumer desktop
,
mobile devices
and
embedded devices
.
In a 1999 interview, Dennis Ritchie voiced his opinion that Linux and BSD Unix operating systems are a continuation of the basis of the Unix design and are derivatives of Unix:
[
37
]
I think the Linux phenomenon is quite delightful, because it draws so strongly on the basis that Unix provided. Linux seems to be among the healthiest of the direct Unix derivatives, though there are also the various BSD systems as well as the more official offerings from the workstation and mainframe manufacturers.
In the same interview, he states that he views both Unix and Linux as "the continuation of ideas that were started by Ken and me and many others, many years ago".
[
37
]
OpenSolaris
was the
free software
counterpart to
Solaris
developed by
Sun Microsystems
, which included a
CDDL
-licensed kernel and a primarily
GNU
userland. However,
Oracle
discontinued the project upon their acquisition of Sun, which prompted a group of former Sun employees and members of the OpenSolaris community to fork OpenSolaris into the
illumos
kernel. As of 2014, illumos remains the only active, open-source System V derivative.
ARPANET
[
edit
]
Main article:
ARPANET
In May 1975, RFC 681 described the development of
Network Unix
by the Center for Advanced Computation at the
University of Illinois Urbana-Champaign
.
[
38
]
The Unix system was said to "present several interesting capabilities as an ARPANET mini-host". At the time, Unix required a license from
Bell Telephone Laboratories
that cost US$20,000 for non-university institutions, while universities could obtain a license for a nominal fee of $150. It was noted that Bell was "open to suggestions" for an ARPANET-wide license.
The RFC specifically mentions that Unix "offers powerful local processing facilities in terms of user programs, several
compilers
, an
editor
based on
QED
, a versatile document preparation system, and an efficient
file system
featuring sophisticated access control,
mountable
and de-mountable volumes, and a unified treatment of peripherals as
special files
." The latter permitted the
Network Control Program
(NCP) to be integrated within the Unix file system, treating
network connections
as special files that could be accessed through standard Unix
I/O calls
, which included the added benefit of closing all connections on program exit, should the user neglect to do so. In order "to minimize the amount of code added to the basic Unix
kernel
", much of the NCP code ran in a
swappable
user process, running only when needed.
[
38
]
Branding
[
edit
]
See also:
List of Unix systems
Promotional
license plate
by
Digital Equipment Corporation
. Actual license plate is used by
Jon Hall
.
HP 9000
workstation
running
HP-UX
, a certified Unix operating system
AT&T originally did not allow licensees to use the Unix name; thus Microsoft called its variant Xenix, for example.
[
39
]
In October 1988, they allowed licensees to use the UNIX trademark for systems based on System V Release 3.2, if certain conditions were met.
[
40
]
In October 1993,
Novell
, the company that owned the rights to the Unix System V source at the time, transferred the
trademarks
of Unix to the
X/Open
Company (now
The Open Group
),
[
41
]
and in 1995 sold the related business operations to
Santa Cruz Operation
(SCO).
[
42
]
[
43
]
Whether Novell also sold the
copyrights
to the actual software was the subject of a federal lawsuit in 2006,
SCO v. Novell
, which Novell won. The case was appealed, but on August 30, 2011, the United States Court of Appeals for the Tenth Circuit affirmed the trial decisions, closing the case.
[
44
]
Unix vendor
SCO Group Inc.
accused Novell of
slander of title
.
The present owner of the trademark
UNIX
is The Open Group, an industry standards consortium. Only systems fully compliant with and certified to the
Single UNIX Specification
qualify as "UNIX" (others are called "
Unix-like
").
By decree of The Open Group, the term "UNIX" refers more to a class of operating systems than to a specific implementation of an operating system; those operating systems which meet The Open Group's Single UNIX Specification should be able to bear the
UNIX 98
or
UNIX 03
trademarks today, after the operating system's vendor pays a substantial certification fee and annual trademark royalties to The Open Group.
[
45
]
Systems that have been licensed to use the UNIX trademark include
AIX
,
[
46
]
EulerOS
,
[
47
]
HP-UX
,
[
48
]
Inspur K-UX
,
[
49
]
IRIX
,
[
50
]
macOS
,
[
51
]
Solaris
,
[
52
]
Tru64 UNIX
(formerly "Digital UNIX", or
OSF/1
),
[
53
]
and
z/OS
.
[
54
]
Notably, EulerOS and Inspur K-UX are Linux distributions certified as UNIX 03 compliant.
[
55
]
[
56
]
Sometimes a representation like
Un*x
,
*NIX
, or
*N?X
is used to indicate all operating systems similar to Unix. This comes from the use of the asterisk (
*
) and the question mark characters as wildcard indicators in many utilities. This notation is also used to describe other Unix-like systems that have not met the requirements for UNIX branding from the Open Group.
The Open Group requests that
UNIX
always be used as an adjective followed by a generic term such as
system
to help avoid the creation of a
genericized trademark
.
Unix
was the original formatting,
[
disputed
–
discuss
]
but the usage of
UNIX
remains widespread because it was once typeset in
small caps
(
Unix
). According to
Dennis Ritchie
, when presenting the original Unix paper to the third Operating Systems Symposium of the American
Association for Computing Machinery
(ACM), "we had a new typesetter and
troff
had just been invented and we were intoxicated by being able to produce small caps".
[
57
]
Many of the operating system's predecessors and contemporaries used all-uppercase lettering, so many people wrote the name in upper case due to force of habit. It is not an acronym.
[
58
]
Trademark names can be registered by different entities in different countries and trademark laws in some countries allow the same trademark name to be controlled by two different entities if each entity uses the trademark in easily distinguishable categories. The result is that Unix has been used as a brand name for various products including bookshelves, ink pens, bottled glue, diapers, hair driers and food containers.
[
59
]
Several plural forms of Unix are used casually to refer to multiple brands of Unix and Unix-like systems. Most common is the conventional
Unixes
, but
Unices
, treating Unix as a
Latin
noun of the
third declension
, is also popular. The pseudo-
Anglo-Saxon
plural form
Unixen
is not common, although occasionally seen.
Sun Microsystems
, developer of the Solaris variant, has asserted that the term
Unix
is itself plural, referencing its many implementations.
[
60
]
See also
[
edit
]
Comparison of operating systems
and
free and proprietary software
List of operating systems
,
Unix systems
, and
Unix commands
List of Unix programming books
Plan 9 from Bell Labs
Timeline of operating systems
Unix time
Market share of operating systems
Year 2038 problem
References
[
edit
]
^
a
b
c
McIlroy, M. D.
(1987).
A Research Unix reader: annotated excerpts from the Programmer's Manual, 1971–1986
(PDF)
(Technical report). CSTR. Bell Labs. 139.
Archived
(PDF)
from the original on 11 November 2017.
^
Ritchie, D. M.
;
Thompson, K.
(1978).
"The UNIX Time-Sharing System"
(PDF)
.
The Bell System Technical Journal
.
57
(6, part 2) (published July–August 1978).
doi
:
10.1145/361011.361061
.
S2CID
53235982
.
^
Ritchie, Dennis M.
(1977).
The Unix Time-sharing System: A retrospective
(PDF)
. Tenth Hawaii International Conference on the System Sciences
. Retrieved
October 23,
2025
.
a good case can be made that [UNIX] is in essence a modern implementation of MIT's CTSS system
^
a
b
Ritchie, D.M.
;
Thompson, K.
(July 1978).
"The UNIX Time-Sharing System"
.
Bell System Tech. J
.
57
(6):
1905–
1929.
Bibcode
:
1978BSTJ...57.1905R
.
CiteSeerX
10.1.1.112.595
.
doi
:
10.1002/j.1538-7305.1978.tb02136.x
. Retrieved
December 9,
2012
.
^
Schwartz, John (June 11, 2000).
"Microsoft's Next Trials"
.
The Washington Post
. Archived from
the original
on December 13, 2024
. Retrieved
December 17,
2024
.
^
a
b
Ritchie, Dennis M.
(January 1993).
"The Development of the C Language"
(PDF)
. Retrieved
23 October
2025
.
^
Raymond, Eric
(19 September 2003).
The Art of Unix Programming
. Addison-Wesley.
ISBN
978-0-13-142901-7
.
Archived
from the original on 12 February 2009
. Retrieved
9 February
2009
.
^
a
b
Anthes, Gary (June 4, 2009).
"Timeline: 40 Years Of Unix"
.
Computerworld
. Retrieved
December 4,
2024
.
^
Lewis, Peter H. (June 12, 1988).
"Is Unix's Time Finally at hand?"
.
The New York Times
. Archived from
the original
on February 5, 2011
. Retrieved
December 17,
2024
.
^
Chuck Karish.
"The name UNIX is now the property of X/Open – comp.std.unix | Google Groups"
. Retrieved
June 1,
2026
.
^
Bangeman, Eric (February 22, 2006).
"Windows passes Unix in server sales"
.
Ars Technica
. Retrieved
December 5,
2024
.
^
Garvin, Skip (September 19, 2019).
"Top IBM Power Systems myths: "IBM AIX is dead and Unix isn't relevant in today's market" (part 2)"
.
IBM Blog
. Retrieved
December 5,
2024
.
^
"Unix is dead. Long live Unix!"
.
^
Raymond, Eric Steven
(2003).
"The Elements of Operating-System Style"
.
The Art of Unix Programming
. Retrieved
August 16,
2020
.
^
Brand, Stewart
(1984).
Tandy/Radio Shack Book: Whole Earth Software Catalog
. Quantum Press/Doubleday.
ISBN
9780385191661
.
UNIX was created by software developers for software developers, to give themselves an environment they could completely manipulate.
^
Spolsky, Joel
(December 14, 2003).
"Biculturalism"
.
Joel on Software
. Retrieved
March 21,
2021
.
When Unix was created and when it formed its cultural values,
there were no end users
.
^
Powers, Shelley
; Peek, Jerry;
O'Reilly, Tim
; Loukides, Mike (2002).
Unix Power Tools
. O'Reilly Media, Inc.
ISBN
978-0-596-00330-2
.
^
a
b
c
d
e
Ritchie, Dennis M.
"The Evolution of the Unix Time-sharing System"
(PDF)
. Retrieved
23 October
2025
.
^
Kernighan, Brian W. Pike, Rob.
The UNIX Programming Environment.
1984. viii
^
Fiedler, Ryan (October 1983).
"The Unix Tutorial / Part 3: Unix in the Microcomputer Marketplace"
.
BYTE
. p. 132
. Retrieved
January 30,
2015
.
^
Brand, Stewart
(1984).
Tandy/Radio Shack Book: Whole Earth Software Catalog
. Quantum Press/Doubleday.
ISBN
9780385191661
.
The best thing about UNIX is its portability. UNIX ports across a full range of hardware—from the single-user $5000 IBM PC to the $5 million Cray. For the first time, the point of stability becomes the software environment, not the hardware architecture; UNIX transcends changes in hardware technology, so programs written for the UNIX environment can move into the next generation of hardware.
^
Stuart, Brian L. (2010).
Principles of operating systems: design & applications
. Boston, Massachusetts: Thompson Learning. p. 23.
ISBN
978-1-4188-3769-3
.
^
Dolya, Aleksey (29 July 2003).
"Interview with Brian Kernighan"
.
Linux Journal
.
Archived
from the original on 18 October 2017.
^
Rik Farrow.
"An Interview with Peter G. Neumann"
(PDF)
.
;login:
.
42
(4): 38.
That then led to Unics (the castrated one-user Multics, so- called due to Brian Kernighan) later becoming UNIX (probably as a result of AT&T lawyers).
^
Georgiadis, Evangelos (2024).
"Dismantling Scaffolding"
. Letters to the Editor.
Communications of the ACM
.
67
.
doi
:
10.1145/3654698
.
ISSN
0001-0782
.
^
Reinfelds, Juris.
"The First Port of UNIX"
(PDF)
. Retrieved
June 30,
2015
.
^
"Portability of C Programs and the UNIX System"
.
Bell Labs
. Retrieved
October 23,
2025
.
^
KUTV, Avery Sloane & Jared Turner (January 8, 2026).
"Rare computer software language found hidden in University of Utah closet"
.
KUTV
. Retrieved
January 10,
2026
.
^
Thompson, Ken
(16 September 2014).
"personal communication, Ken Thompson to Donald W. Gillies"
.
UBC ECE website
. Archived from
the original
on 22 March 2016.
^
"Operating system Family - Systems share"
. Top 500 project.
^
"Loading"
. Apple Developer.
Archived
from the original on 9 June 2012
. Retrieved
22 August
2012
.
^
"Unix's Revenge"
. asymco. 29 September 2010.
Archived
from the original on 9 November 2010
. Retrieved
9 November
2010
.
^
"Unix: the operating system setting new standards"
.
IONOS Digitalguide
. May 29, 2020
. Retrieved
May 10,
2022
.
^
Shelley Powers
; Jerry Peek;
Tim O'Reilly
; Michael Kosta Loukides; Mike Loukides (2003).
Unix Power Tools
. O'Reilly Media, Inc. p. 32.
ISBN
978-0-596-00330-2
. Retrieved
August 8,
2022
.
^
Ritchie, Dennis
(1979).
"The Evolution of the Unix Time-sharing System"
.
Bell Laboratories
. Retrieved
23 October
2025
.
Perhaps the most important watershed occurred during 1973, when the operating system kernel was rewritten in C.
^
"Major Distributions"
.
Distro Watch
.
^
a
b
Benet, Manuel (1999).
"Interview With Dennis M. Ritchie"
.
LinuxFocus
.
Archived
from the original on 4 January 2018
. Retrieved
16 August
2020
.
^
a
b
Holmgren, Steve (May 1975).
Network Unix
.
IETF
.
doi
:
10.17487/RFC0681
.
RFC
681
. Retrieved
April 22,
2021
.
^
Libes, Sol (November 1982).
"Bytelines"
.
BYTE
. pp.
540–
547.
^
"AT&T Expands Unix Trademark Licensing Program"
(Press release). October 31, 1988.
^
Chuck Karish (October 12, 1993).
"The name UNIX is now the property of X/Open"
.
Newsgroup
:
comp.std.unix
.
Usenet:
29hug3INN4qt@rodan.UU.NET
. Retrieved
February 21,
2020
.
^
"Novell Completes Sale of UnixWare Business to The Santa Cruz Operation | Micro Focus"
.
www.novell.com
.
Archived
from the original on 20 December 2015
. Retrieved
20 December
2015
.
^
"HP, Novell and SCO To Deliver High-Volume UNIX OS With Advanced Network And Enterprise Services"
. Novell.com. September 20, 1995.
Archived
from the original on January 23, 2007
. Retrieved
November 9,
2010
.
^
Jones, Pamela
.
"SCO Files Docketing Statement and We Find Out What Its Appeal Will Be About"
.
Groklaw
. Groklaw.net. Archived from the original on June 21, 2024
. Retrieved
April 12,
2011
.
^
The Open Group.
"The Open Brand Fee Schedule"
.
Archived
from the original on December 31, 2011
. Retrieved
December 26,
2011
.
The right to use the UNIX Trademark requires the Licensee to pay to The Open Group an additional annual fee, calculated in accordance with the fee table set out below.
^
The Open Group.
"AIX 6 Operating System V6.1.2 with SP1 or later certification"
.
Archived
from the original on April 8, 2016.
^
The Open Group (September 8, 2016).
"Huawei EulerOS 2.0 certification"
.
^
The Open Group.
"HP-UX 11i V3 Release B.11.31 or later certification"
.
Archived
from the original on April 8, 2016.
^
The Open Group.
"Inspur K-UX 2.0 certification"
.
Archived
from the original on July 9, 2014.
^
The Open Group.
"IRIX 6.5.28 with patches (4605 and 7029) certification"
.
Archived
from the original on March 4, 2016.
^
"macOS version 10.12 Sierra on Intel-based Mac computers"
. The Open Group.
Archived
from the original on October 2, 2016.
^
The Open Group.
"Oracle Solaris 11 FCS and later certification"
.
Archived
from the original on September 24, 2015.
^
Bonnie Talerico.
"Hewlett-Packard Company Conformance Statement"
. The Open Group.
Archived
from the original on December 10, 2015
. Retrieved
December 8,
2015
.
^
Vivian W. Morabito.
"IBM Corporation Conformance Statement"
. The Open Group
. Retrieved
January 21,
2018
.
^
Peng Shen.
"Huawei Conformance Statement"
. The Open Group
. Retrieved
January 22,
2020
.
^
Peng Shen.
"Huawei Conformance Statement: Commands and Utilities V4"
. The Open Group
. Retrieved
January 22,
2020
.
^
Raymond, Eric S. (ed.).
"Unix"
.
The Jargon File
.
Archived
from the original on June 4, 2011
. Retrieved
November 9,
2010
.
^
Troy, Douglas (1990).
UNIX Systems
. Computing Fundamentals. Benjamin/Cumming Publishing Company. p. 4.
ISBN
978-0-201-19827-0
.
^
"Autres Unix, autres moeurs (OtherUnix)"
.
Bell Laboratories
. April 1, 2000
. Retrieved
October 23,
2025
.
^
"History of Solaris"
(PDF)
.
Archived
(PDF)
from the original on March 18, 2017.
UNIX is plural. It is not one operating system but, many implementations of an idea that originated in 1965.
Further reading
[
edit
]
General
Ritchie, D.M.
;
Thompson, K.
(July–August 1978).
"The UNIX Time-Sharing System"
.
Bell System Technical Journal
.
57
(6). Archived from
the original
on November 3, 2010.
"UNIX History"
.
www.levenez.com
. Retrieved
March 17,
2005
.
"AIX, FreeBSD, HP-UX, Linux, Solaris, Tru64"
.
UNIXguide.net
. Retrieved
March 17,
2005
.
"Linux Weekly News, February 21, 2002"
.
lwn.net
. Retrieved
April 7,
2006
.
Lions, John
:
Lions'
"Commentary on the Sixth Edition UNIX Operating System"
.
with Source Code
, Peer-to-Peer Communications, 1996;
ISBN
1-57398-013-7
Books
Salus, Peter H.
:
A Quarter Century of UNIX
, Addison Wesley, June 1, 1994;
ISBN
0-201-54777-5
Television
Computer Chronicles
(1985). "
UNIX
".
Computer Chronicles
(1989). "
Unix
".
Talks
Ken Thompson (2019).
"VCF East 2019 -- Brian Kernighan interviews Ken Thompson"
(Interview).
Marshall Kirk McKusick (2006).
History of the Berkeley Software Distributions (three one-hour lectures)
.
External links
[
edit
]
Unix
at Wikipedia's
sister projects
Definitions
from Wiktionary
Media
from Commons
Quotations
from Wikiquote
Textbooks
from Wikibooks
Data
from Wikidata
The Evolution of the Unix Time-sharing System
The Creation of the UNIX Operating System
The Unix Tree: source code and manuals from historic releases
Unix History Repository — a git repository representing a reconstructed version of the Unix history
on
GitHub
The Unix 1st Edition Manual
1st Edition manual rendered to HTML
AT&T Tech Channel Archive: The UNIX Operating System: Making Computers More Productive (1982)
on
YouTube
(film about Unix featuring Dennis Ritchie, Ken Thompson, Brian Kernighan, Alfred Aho, and more)
AT&T Tech Channel Archive: The UNIX System: Making Computers Easier to Use (1982)
on
YouTube
(complementary film to the preceding "Making Computers More Productive")
audio bsdtalk170 - Marshall Kirk McKusick at DCBSDCon -- on history of tcp/ip (in BSD) -- abridgement of the three lectures on the history of BSD.
A History of UNIX before Berkeley: UNIX Evolution: 1975-1984
BYTE Magazine, September 1986: UNIX and the MC68000
–  a software perspective on the MC68000 CPU architecture and UNIX compatibility
v
t
e
Unix
and
Unix-like
operating systems
and
compatibility layers
Architecture
Filesystem
History
Philosophy
Security
Shell
Operating
systems
BSD
386BSD
FreeBSD
NetBSD
OpenBSD
DragonFly BSD
Darwin
macOS
iOS
audioOS
iPadOS
tvOS
watchOS
bridgeOS
DYNIX
NeXTSTEP
SunOS
Ultrix
Linux
Android
Arch
ChromeOS
Debian
Fedora
Gentoo
Red Hat
Slackware
SUSE
Ubuntu
Other distributions
System V
A/UX
AIX
HP-UX
IRIX
OpenServer
Solaris
OpenSolaris
Illumos
Tru64 UNIX
UnixWare
Other
Coherent
Domain/OS
GNU
Hurd
LynxOS
Minix
MOS
OSF/1
QNX
BlackBerry 10
Research Unix
SerenityOS
Xenix
more...
Compatibility
layers
Cygwin
Darling
Eunice
GNV
Interix
MachTen
Microsoft POSIX subsystem
MKS Toolkit
PASE
P.I.P.S.
PWS/VSE-AF
UNIX System Services
UserLAnd Technologies
Windows Services for UNIX
Windows Subsystem for Linux
Italics
indicate discontinued systems.
Category
Commons
v
t
e
Unix
command-line
utilities
and
shell builtins
File system
cat
chattr
chmod
chown
chgrp
cksum
cmp
cp
dd
du
df
file
fuser
ln
ls
mkdir
mv
pax
pwd
rm
rmdir
split
tee
touch
type
umask
Processes
at
bg
crontab
fg
kill
nice
ps
time
User environment
env
exit
logname
mesg
talk
tput
uname
who
write
Text processing
awk
basename
comm
csplit
cut
diff
dirname
ed
ex
fold
head
iconv
join
m4
more
nl
paste
patch
printf
read
sed
sort
strings
tail
tr
troff
uniq
vi
wc
xargs
Shell builtins
alias
cd
echo
test
unset
wait
Searching
find
grep
Documentation
man
Software development
ar
ctags
lex
make
nm
strip
yacc
Miscellaneous
bc
cal
dc
expr
lp
od
sleep
true and false
Categories
Standard Unix programs
Unix SUS2008 utilities
List
v
t
e
Ken Thompson
Operating systems
Unix
Plan 9 from Bell Labs
Inferno
Programming languages
B
Go
Software
Belle
ed
grep
sam
Space Travel
Thompson shell
Associated institutions
Bell Labs
Google
Other
UTF-8
v
t
e
Rob Pike
Operating systems
Plan 9 from Bell Labs
Inferno
Programming languages
Newsqueak
Limbo
Sawzall
Go
Software
acme
Blit
sam
rio
8½
Publications
The Practice of Programming
The Unix Programming Environment
Other
Renée French
Mark V. Shaney
UTF-8
v
t
e
Time-sharing
operating systems
Time-sharing system evolution
BBN Time-Sharing System
Berkeley Timesharing System
Burroughs MCP
CDC Kronos
Compatible Time-Sharing System (CTSS)
COS
CP/CMS
Cray Time Sharing System (CTSS)
DTSS
EMAS
ITS
LTSS
MCTSS
MTS
Multics
MUSIC/SP
NLTSS
NOS
NOS/VE
OpenVMS
ORVYL and WYLBUR
OS4000
Pick
RAX
RSTS/E
TENEX
TSO
TSOS
TOPS-10
TOPS-20
TSS
TSS/8
Unix
UTS
VM
VP/CSS
VPS/VM
VS/9
WAITS
Category
v
t
e
Operating systems
General
Comparison
Forensic engineering
History
List
Timeline
Usage share
User features comparison
Variants
Disk operating system
Distributed operating system
Embedded operating system
Hobbyist operating system
Just enough operating system
Mobile operating system
Network operating system
Object-oriented operating system
Real-time operating system
Supercomputer operating system
Kernel
Architectures
Exokernel
Hybrid
Microkernel
Monolithic
Multikernel
vkernel
Rump kernel
Unikernel
Components
Device driver
Loadable kernel module
User space and kernel space
Process management
Concepts
Computer multitasking
(
Cooperative
,
Preemptive
)
Context switch
Interrupt
IPC
Process
Process control block
Real-time
Thread
Time-sharing
Scheduling
algorithms
Fixed-priority preemptive
Multilevel feedback queue
Round-robin
Shortest job next
Memory management
,
resource
protection
Bus error
General protection fault
Memory paging
Memory protection
Protection ring
Segmentation fault
Virtual memory
Storage
access,
file systems
Boot loader
Defragmentation
Device file
File attribute
Inode
Journal
Partition
Virtual file system
Virtual tape library
Supporting concepts
API
Computer network
HAL
Live CD
Live USB
Shell
CLI
User interface
PXE
Authority control databases
International
VIAF
GND
National
United States
France
BnF data
Czech Republic
Spain
Norway
Catalonia
Other
IdRef
Retrieved from "
https://en.wikipedia.org/w/index.php?title=Unix&oldid=1361545562
"
Categories
:
Unix
1969 software
Products introduced in 1969
Operating system families
Time-sharing operating systems
Hidden categories:
Pages using the Phonos extension
CS1: unfit URL
Articles with short description
Short description is different from Wikidata
Wikipedia indefinitely move-protected pages
Use mdy dates from October 2018
Use American English from August 2018
All Wikipedia articles written in American English
Pages including recorded pronunciations
Articles needing additional references from October 2023
All articles needing additional references
All accuracy disputes
Articles with disputed statements from September 2019
Pages using Sister project links with hidden wikidata
Search
Search
Unix
110 languages
Add topic

### Unix History (link)
*URL:* https://www.levenez.com/unix/

# UNIX History

UNIX History
Unix History
Unix Timeline
Below, you can see the preview of the
Unix History
(move on the white zone to get a bigger image):
This is a simplified diagram of unix history. There are numerous derivative 
			systems not listed in this chart, maybe 10 times more! In the recent past, 
			many electronic companies had their own unix releases.
			This diagram is only the tip of an iceberg, with a penguin on it ;-).
If you want to print this timeline, you can
freely
download one of the following PDF files:
A4
Letter
Plotter
A4
Letter
History
Index
Warning
:
				it seems that
Adobe Reader
has some problems reading the large plotter version of the Unix History chart,
				but happily you can use another
PDF viewer
for this task. By the way, if you are on macOS, just use Safari :-)
Here is the
ChangeLog
of this history.
Note 1
: an arrow indicates an inheritance like a compatibility, it is
not only a matter of source code
.
Note 2
: this diagram shows complete systems and [micro]kernels like Mach, Linux,
					the Hurd... This is because sometimes kernel versions are more appropriate to
					see the evolution of the system.
Note 3
: I have now a
page
where I explain how I
					build this chart.
Another chart on the wall
If you have put this diagram on the wall of your office and have taken a photo
                    of it, please send me a copy and I'll put it on this
page
. ;-)
My other charts:
Computer Languages History
.
Windows History
.
Some Home Pages
Brian Kernighan
Dennis Ritchie
Ken Thompson
Bill Joy
Steve Jobs
Linus Torvalds
Richard Stallman
You can also find
here
some unix people.
You may be wondering
"Why does Steve Jobs appear in this unix history?"
.
            Simply because he has made the best unix computer ever : a NeXTcube
            powered with the NeXTSTEP operating system. And now :
Mac OS X
.
Some Unixes
Unix History on Google
Here is a listing of the unixes that are present in my chart :
1BSD
2BSD
3BSD
4BSD
4.4BSD Lite 1
4.4BSD Lite 2
386 BSD
Acorn RISC iX
Acorn RISC Unix
AIX
AIX PS/2
AIX/370
AIX/6000
AIX/ESA
AIX/RT
AMiX
Android
AOS Lite
AOS Reno
AppleTV
ArchBSD
ASV
Atari Unix
A/UX
BBX
BOS
BRL Unix
BSD Net/1
BSD Net/2
BSD/386
BSD/OS
CB Unix
Chorus
Chorus/MiX
Coherent
CTIX
CXOs
Darwin
Debian GNU/Hurd
DEC OSF/1 ACP
Dell Unix
DesktopBSD
Digital Unix
DragonFly BSD
Dynix
Dynix/ptx
ekkoBSD
Eunice
FireFly BSD
FreeBSD
FreeDarwin
GNU
GNU-Darwin
Gnuppix
GNU/Hurd-L4
HPBSD
HP-UX
HP-UX BLS
IBM AOS
IBM IX/370
Inferno
Interactive 386/ix
Interactive IS
iOS
iPhone OS
iPod OS
IRIS GL2
IRIX
Junos OS
Linux
Lites
LSX
macOS
(Mac OS X)
Mach
MERT
MicroBSD
MidnightBSD
Mini Unix
Minix
Minix-VMD
MIPS OS RISC/os
MirBSD
Mk Linux
more/BSD
Monterey
mt Xinu
MVS/ESA OpenEdition
NetBSD
NeXTSTEP
NonStop-UX
Open Desktop
Open UNIX
OpenBSD
OpenDarwin
OpenIndiana
OpenServer
OpenSolaris
OPENSTEP
OS/390 OpenEdition
OS/390 Unix
OSF/1
OS X
PC-BSD
PC/IX
Plan 9
Plurix
PureDarwin
PWB
PWB/UNIX
QNX
QNX RTOS
QNX/Neutrino
QUNIX
Redox
ReliantUnix
Rhapsody
RISC iX
RT
SCO UNIX
SCO UnixWare
SCO Xenix
SCO Xenix System V/386
Security-Enhanced Linux
Silver OS
Sinix
Sinix ReliantUnix
Solaris
SPIX
SunOS
Triance OS
Tru64 Unix
Trusted IRIX/B
Trusted Solaris
Trusted Xenix
TS
Tunis
UCLA Locus
UCLA Secure Unix
Ultrix
Ultrix 32M
Ultrix-11
Unicos
Unicos/mk
Unicos/mp
Unicox-max
UNICS
UniSoft UniPlus
UNIX 32V
UNIX Interactive
UNIX System III
UNIX System IV
UNIX System V
UNIX System V Release 2
UNIX System V Release 3
UNIX System V Release 4
UNIX System V/286
UNIX System V/386
UNIX Time-Sharing System
UnixWare
UNSW
USG
Venix
Xenix OS
Xinu
xMach
z/OS Unix System Services
Here is now some unixes that are not [yet] in my chart.
            If you want to find more unixes, try
Google
:-)
ABCenix
ACIX
AD
ÆrieBSD
Altos System V
ANALIX
ARIX
AurOS
Bitrig
BKUNIX
BOS/X
BS2000/OSD-BC
C Executive
CLIX
Consensys Unix
Concentrix
ConvexOS
COSIX
CPIX
Cromix
CX/UX
DCC-IX
DC/OSx
ÐÐÐÐÐ¡
DG/UX
DISTRIX
DNIX
Domain/OS
DRM System
DTIX
DVIX
EDIX
ENIX
EP/IX
Esix SVR4
Eurix
FOR:PRO
FreeMiNT
FTX
Genix
Haiku
HCR
Helios
HEP-UPX
HI-UX
IDRIS
Illumos
INOS
LSX
LynxOS
MachTen
MacMach
MAXION/OS
MCS
Micronix
Microport SVR4
MicroPort Unix
Mimos
MMOS
MOS
MP-RAS UNIX
MST UNIX
Mulplix
Munix
NachOS
NCR Unix/NS
NDIX
News-OS
NUXI
Oasis
ONIX
OPUS
OS 9
OS/MP
OSx
PacBSD
PCUNIX
PNX
Punix
QNIX
REAL
Regulus
RetroBSD
RT/EMT
RTUX
SerenityOS
SORIX
Sortix
SOX
Sphinx
SPP-UX
Stellix
SUNIX
Super-UX
System B
Thix
TI System V
TNIX
Topix
TOS
Tribblix
Tropix
UHC Unix
Umax
UniFLEX
Uniq
Unisis
Unity
UNOS
USIX
UTEK
UTS
UTX/32S
UX
UXP/DS
UZIX
VM/IX
VOLVIX
Xoftnix
Zeus
Some useful UNIX links
Unix on Wikipedia
The Creation of the UNIX Operating System
from Lucent.
An Oral History of Unix
from Princeton.
UNIX Past
from The Open Group.
The Unix Heritage Society
by Warren Toomey.
FreeBSD Release Information
from FreeBSD.
Formal NetBSD Releases
from NetBSD.
AIX release and service delivery strategy
from IBM.
Darwin/Mac OS X: The Fifth BSD
from Applelust.
Sun History
from SUN.
The History of Solaris
(PDF) from
Witty's Place
.
HP-UX History
from HP.
Unix and Multics
by Tom Van Vleck.
Linux Kernel Archives
.
20 Years of Berkeley Unix
by Marshall Kirk McKusick.
Operating System Technical Comparison
from Milo.
Chronology of Events in the History of Microcomputers
by Ken Polsson.
Grokline's UNIX Ownership History Project
.
IRIX Versions and History
by Ryan Thoryk.
Mind Map of Linux distributions
by Ravi Kumar.
GNU/Linux distro timeline
by Andreas Lundqvist.
BSD timeline
by Donjan Rodic
Linux timeline
and
BSD timeline
by Andreas Lundqvist and Donjan Rodic, continued by Fabio Loli.
Linux Kernel 2.6.8.1 map
by OSU.
Yet Another Linux Distro Timeline
by greengrass44.
Restoration of 1st Edition UNIX kernel sources
from
pdf document.
História dos UNIXes Brasileiros
by Newton Faller
The UNIX system family tree: Research and BSD
by Wolfram Schneider
HPBSD: Utah's 4.3bsd port for HP9000 series machines
by Mike Hubler
PA-RISC Operating Systems
from
OpenPA.net
AIX support lifecycle information
.
Some links about some UNIX lawsuits
Unix Lawsuits on Google
USL vs. BSDI documents
from
Dennis Ritchie
.
Liberal license for ancient UNIX sources
from Caldera.
SCO Files Lawsuit Against IBM
from SCO.
SCO Suspends Distribution of Linux Pending Intellectual Property Clarification
from SCO.
OSI Position Paper on the SCO-vs.-IBM Complaint
from Open Source Initiative.
A History of UNIX and UNIX Licences
by Peter Salus.
Novell Challenges SCO Position, Reiterates Support for Linux
from Novell.
Apple in court dispute over Unix
from CNet.
SCO Announces Immediate Termination of IBM's Right to Use and Distribute AIX Software and Files for Permanent Injunction
from SCO.
SCO Registers UNIX Copyrights and Offers UNIX License
from SCO.
Red Hat Takes Aim at Infringement Claims
from Red Hat.
SCO Announces Intellectual Property License for Linux
from SCO.
IBM's counterclaims
from IBM.
The SCO Group Announces Final Termination of IBM / Sequent's Contract to Use or License Dynix Software
from SCO.
To the Linux Community
from SGI.
OSDL releases position paper disputing SCO Linux claims
from OSDL.
Letter from SCO to IBM
Open Letter on Copyrights
from SCO.
SCO Announces New Initiatives to Enforce Intellectual Property Rights
from SCO.
Novell's Unique Legal Rights
from Novell.
Groklaw's New Group Project -- The Timeline Project
.
SCO v. IBM
from SCO.
Some links
Non-Unix
OS History
by Patrick Mulvany.
My other links
Search in all
levenez.com
Computer Languages History
.
Unix Hierarchy
(an old paper).
NeXT History
(in french).
Windows History
.
Another Chart On The Wall
.
statistics
of this site.
other unix products
.
last update : January 27, 2026
Please send comments to
Éric Lévénez
You can freely use this diagram for non-commercial purpose.

### Unix History Timeline (link)
*URL:* https://upload.wikimedia.org/wikipedia/commons/7/77/Unix_history-simple.svg

[fetch failed: HTTP 429]

### What Is Difference Between UNIX And Linux (link)
*URL:* https://www.softwaretestinghelp.com/unix-vs-linux/

# Unix Vs Linux: What is Difference Between UNIX and Linux

Unix Vs Linux: What is Difference Between UNIX and Linux
Skip to content
By
Sruthy
By Sruthy
Sruthy, with her 10+ years of experience, is a dynamic professional who seamlessly blends her creative soul with technical prowess. With a Technical Degree in Graphics Design and Communications and a Bachelor’s Degree in Electronics and Communication, she brings a unique combination of artistic flair…
Full Bio >
Follow
Learn about our
editorial policies
.
Updated April 1, 2025
Unix Vs Linux: Learn what is the Core Difference between UNIX and Linux Architecture, Kernel, And Commands
Linux is nothing but a UNIX clone which is written Linus Torvalds from scratch with the help of some hackers across the globe.
Unix and Unix-like operating systems are a family of computer operating systems that derive from the original Unix System from Bell Labs which can be traced back to 1965.
Linux is the most popular variant and there comes in many different distributions.
=>
Click here for Complete Unix Tutorial series
Unix is a family of multitasking, portable, multi-user computer operating systems, which also have time-sharing configurations.
Unix systems use a centralized OS kernel which is responsible for managing the entire system.
The programming interface, file abstraction, built-in networking and persistent background processing called daemons are the other features and capabilities that are supported by a Unix OS.
Table of Contents:
What is UNIX?
What is Linux?
Difference Between Unix and Linux
Linux vs Unix Kernel
Unix Vs Linux Commands
Conclusion
What is UNIX?
Unix is considered as the mother of most of the operating systems.
The design of Unix systems is based on “Unix Philosophy” which includes the following characteristics:
Usage of plain text for data storage.
Hierarchical file system.
Handling devices and some specific kinds of inter-process communication (IPC) as files.
Employing a huge number of software tools.
Multiple small, simple, and modular programs can be threaded together via a command-line interpreter using pipes, contrasting to using a single monolithic program which comprises of all the same functionality.
It’s worth mentioning here the below quote about Unix Philosophy:
“Although that philosophy can’t be written down in a single sentence, as its heart is the idea that the power of a system comes more from the relationships among programs than from the programs themselves. Many UNIX programs do quite trivial things in isolation, but, combined with other programs, become general and useful tools.”
– Brian Kernighan & Rob Pike
Unix Architecture
The below diagram will depict the Unix architecture.
[image
source
]
The master control program of Unix is its Kernel. The kernel has full control over the entire system. It has subsystems that offer services to file system handling, resource handling, memory management, start & stop programs, and a few other low-level core tasks.
The kernel is the heart of the OS and acts as an interface between the user and hardware. Each kernel subsystem has certain features like concurrency, virtual memory, paging, and a virtual file system.
In the outer layers of the architecture, we have the shell, commands, and application programs. Shell is the interface between the user and the kernel. Shell and the user type in the commands, interpret these commands and call the computer programs accordingly.
Examples
of the Unix operating systems are Solaris and HP-UX. The largest distributors of UNIX systems include IBM, HP, and SUN.
Recommended Read =>
Free Unix Training Tutorials
What is Linux?
By now you would have got a fair idea about Unix. Let’s now explore Linux in detail.
People do confuse a lot between the terms Unix and Linux and they generally ask questions like
“Is Unix Different from Linux?”
/
“Are Linux and Unix the same thing?”
/
“Is Linux like Unix?”/ “Is Linux built on Unix?”
.
Here is the answer to all such questions. First, let me clear your confusion in a one-liner. Linux and Unix are different but they do have a relationship with each other as Linux is derived from Unix.
Linux is not Unix, but it is a Unix-like operating system. Linux system is derived from Unix and it is a continuation of the basis of Unix design. Linux distributions are the most famous and healthiest example of direct Unix derivatives.
BSD (Berkley Software Distribution) is also an example of a Unix derivative.
At this juncture, we need to make you clear about what is Unix-like.
A Unix-like OS (also called UN*X or *nix) is one that works in a way similar to Unix systems, however, it is not necessary that they conform to Single UNIX Specification (SUS) or similar POSIX (Portable Operating System Interface) standard.
SUS is a standard that is required to be met for any OS to qualify for using the ‘UNIX’ trademark. This trademark is granted by ‘The Open Group’.
Few Examples
of currently registered UNIX systems include macOS, Solaris, and AIX. If we consider the POSIX system, then Linux can be regarded as Unix-like OS.
As per the Linux kernel official README file,
Linux is a UNIX clone
that is developed from scratch by Linus Torvalds and his team. It targets POSIX compliance. The Linux kernel code was completely written from scratch. It is designed in such a way so that it acts like Unix but it does not have the original Unix code in it.
It is also significant to note that
Linux is just the kernel and not the complete OS
. This Linux kernel is generally packaged in Linux distributions which thereby makes it a complete OS.
Thus, Linux is only the Kernel, while Linux distributions can be treated as the OS. On the other hand, UNIX in itself is a complete OS as everything (all required applications tied together) comes from a single vendor.
For Example,
Solaris.
Linux distribution (also called a distro in short) is an operating system that is created from a collection of software built upon the Linux Kernel and is a package management system.
A standard Linux distribution consists of a Linux kernel, GNU system, GNU utilities, libraries, compiler, additional software, documentation, a window system, a window manager, and a desktop environment.
Most of the software included in Linux distribution is free and open source. They may include some proprietary software like binary blobs which is essential for a few device drivers.
Linux-based OS Architecture
[image
source
]
Thus, Linux distributions actually make the Linux kernel completely usable as an operating system by adding different applications to it. Various flavors of Linux distributions serve a wide range of user needs.
For Example
, we have OpenWrt Linux-based OS for embedded devices, Linux Mint for Personal computers, and Rocks Cluster Distribution for supercomputers. In total, around 600 Linux distributions do exist.
It will be interesting for you to know that Google’s popular Android mobile OS is based on Linux. Every iteration of the Android OS is built on the current Linux kernel.
Difference Between Unix and Linux
Linux
Unix and other Variants
Linux refers to the kernel of the GNU/Linux operating system.  More generally, it refers to the family of derived distributions.
Unix refers to the original operating system developed by AT&T.  More generally, it refers to family of derived operating systems.
Original code developed by Linus and the GNU Foundation
Original code developed by AT & T
The Linux trademark is owned by Linus Trovalds, and managed by the Linux Mark Institute under the Linux Foundation.
The UNIX trademark is certified by the Open Group.  List of certified operating systems.
The Linux Standard Base (LSB), available as ISO/IEC 23360, is a standardization effort by a number of Linux distributors.  LSB is mostly an extension of POSIX but has some differences.  However, there isn’t a strong need for LSB certification as the various distributions use the same kernel in any case.
UNIX certification based on the ‘Single Unix Specification’ which is an extension of IEEE 1003 (POSIX), also available as ISO/IEC 9945.  POSIX specifies programming APIs and shell and utility interfaces.  POSIX was developed as a way to allow interoperability between different UNIX vendors.
GNU/Linux and derivates like Debian and Fedora
System-V Unix and derivatives like IBM-AIX and HP-UX; Berkeley Unix and derivatives like FreeBSD and macOS
Open Source under the copyleft General Public License
Berkeley Unix is partially open source under the BSD License.  System-V Unix source may be procured under a proprietary commercial license.
Different variants maintained by different communities; with the kernel merging into the branch maintained by Linus
Different variants maintained by different companies; each maintains their own kernel
Designed as a general-purpose scalable platform for a broad set of applications.
Typically designed for a narrow audience with a defined set of target platforms and applications.
Broadly available as configurable software download and installer.
Typically shipped along with hardware e.g. MacBook
Free community support.  Paid support available from a number of service providers.
Paid commercial support.  Often leads to vendor lock-in.
Interfaces often evolve
Interfaces usually stable
Frequent updates, with quick bug fixes
Infrequent updates, and fixes may take time
Supports almost all file systems used across operating systems
Most versions support two or perhaps three file systems
Breadth of system administration tools often with limited focus e.g. Suse YAST
Each version typically has a mature system administration tool e.g. HP SAM
Preferred OS for cloud deployment and data centers primarily for economic reasons
Preferred OS for special purpose server requirements due to application availability, and internet servers for legacy reasons
Scalability achieved using clusters, grids or cloud.
Scalability achieved using clusters or grids
(A cluster is a collection of homogenous computers, a grid is a collection of distributed computers, and a cloud service is a collection of virtualized clusters.)
Most of the command line and graphical utilities are similar to Unix
Most of the command line and graphical utilities are similar to Linux
We hope you must have understood the core differences between Unix and Linux from this article.
Let us now see some more important differences between Linux and Unix in the below tabular format:
Features
Linux
Unix
Developer
Inspired by MINIX (a Unix-like OS), Linux was originally developed by Finnish-American software engineer Linus Torvalds. Since it is an open source, we have community developers for Linux.
Originally derived from AT&T Unix, it was developed at Bell Labs by Kenneth Lane Thompson, Dennis Ritchie, and 3 others.
Written in
C and other programming languages.
C and assembly language.
OS family
Unix-like
Unix
Working state
Current
Current
Source Model
Open source
Mixed. Traditionally closed source, however, few Unix projects are open source which include illumos OS and BSD (Berkley Software Distribution) OS.
Available in
Multilingual
English
Initial release
Linux is newer when compared to Unix. It was derived from Unix and was released in September 1991.
Unix is older. Was released in October 1973 for outside parties. Before that, it was used internally in Bell Labs since its inception in 1970.
Kernel Type
Monolithic kernel
Kernel Type varies. It can be monolithic, microkernel and hybrid.
License
GNUv2(GPL General Public License) and others.
Licensing varies. Few versions are proprietary while others are free/OSS.
Official Website
https://www.kernel.org/
http://opengroup.org/unix
Default user interface
Unix shell
CLI (Command Line Interface) and Graphical (X Windows system)
Text Mode Interface
By default, the shell is BASH (Bourne Again Shell). Moreover, is compatible with many command interpreters.
Originally the Bourne shell. It is also compatible with many command interpreters.
Cost
Can be obtained and used freely. There are priced versions of Linux as well. But, generally, Linux is cheaper than Windows.
Proprietary operating systems have different cost structures set accordingly by the vendors selling it.
Examples
Debian, Ubuntu, Fedora, Red Hat, Android, etc.
IBM AIX, Solaris, HP-UX, Darwin, macOS X, etc.
Architecture
Was originally created for Intel’s x86 hardware, ports available for a lot of CPU types.
Compatible with PA and Itanium machines. Solaris is also available on x86/x64. OSX is PowerPC.
Threat detection and solution
As Linux is mainly driven by open source community, many developers across different parts of the world are working on the code. Hence threat detection and solution is quite fast in case of Linux.
Due to the proprietary nature of Unix, users need to wait for proper bug fixing patches.
Security
Both Linux and Unix based OS is generally regarded as very well protected against malware. This is attributable to lack of root access, quick updates and comparatively low market share (as compared to windows). As of 2018, there has been none widespread Linux virus.
Unix is also considered to be very safe. It is even harder to infect as the source is also not available. There is no actively spreading virus for Unix nowadays.
Price
Linux is free. However, corporate support is available at a price.
Unix is not free. However, some Unix versions are free for development use (Solaris). In a collaborative environment, Unix costs $1,407 per user and Linux costs $256 per user.
Hence, UNIX is extremely expensive.
Linux vs Unix Kernel
As Linux alone is just a kernel, it is worth discussing the major differences between the Linux Kernel and the Unix kernel.
There are three types of kernel i.e. monolithic, micro and hybrid (combination of monolithic and micro) as seen in the below image.
[image
source
]
In monolithic kernel architecture, the entire OS works in a single kernel space. It single-handedly defines a high-level virtual interface on top of the computer hardware.
Though the Linux kernel derives most of its characteristics from Unix/ Unix-like kernels, however, there are some significant points of differences between the two.
In microkernel architecture, the core services of the OS run in one process while the other services run in different processes.
In µ kernel, the near-minimum amount of mechanisms are included in the kernel mode. These mechanisms include basic IPC (inter-process communication), scheduling, and low-level address space management.
In terms of source code size, generally, a microkernel is smaller than a monolithic kernel.
Features
Linux Kernel
Unix Kernel
Kernel approach
Linux follows the monolithic kernel approach.
Unix kernel can be monolithic, microkernel or hybrid.
For Example, macOS has a hybrid kernel, Solaris has the monolithic kernel, and AIX has a monolithic kernel with dynamically loadable modules.
Adding/removing features of the kernel
Provides a great feature through which the kernel components like device drives can be dynamically added and removed as modules. This feature is called as loadable kernel modules (LDM). This eliminates the need to compile the whole kernel again. This feature in turn gives great flexibility to Linux.
Traditional Unix systems kernel need static linking of new systems being added.
Streams
In Linux, there are no streams I/O subsystem.
In most of the Unix kernels, streams I/O subsystem is included which turns out to be the desired interface for writing device drivers, terminal drivers, etc.
Preemptive vs non-preemptive approach
Normally a Linux kernel is non-preemptive. However, in recent times, Linux real-time OS has started using preemptive kernels.
Some Unix systems are fully preemptive.
For example, Solaris 2.x. etc.
Kernel threading
Linux uses kernel thread just for running some kernel code periodically.
Many Unix-like operating systems use kernel thread for the purpose of process context switching.
Ways to handle the multi-threaded environment
Through multi-threading, more than one independent execution flows which are called lightweight processes (LWP) are created.
In Linux, LWP is created by calling clone () function. These processes in Linux can share physical memory, opened files, address space, etc.
In Unix, the LWP is based on kernel threads.
Unix Vs Linux Commands
There are certain differences between the shell commands i.e. even among the versions of the same Unix variant. However, what varies most is the internal shell that is built in rather than the presentation.
On the whole, efforts are made to keep Linux as close as possible to Unix by complying with the POSIX standards. Hence, the terminal commands in Linux distros and Unix operating systems are not the same, but, there are not many differences too.
Each Linux distribution in itself has its way of execution.
For Example
, in CentOS which is a Linux family OS, we use yum (yellow dog update modifier) commands for the installation of new packages, while in Debian which is another OS from the Linux family, we use apt-get commands for installation.
In IBM AIX, which is a proprietary Unix OS, we use the
-finger
command to check who is logged into the system. But this command is not used in Linux. In Linux, we use the
pinky
command to fetch the same result.
In Ubuntu/Debian (a Linux OS), we have
fdisk, parted, gparted
commands for the ‘create’ task. On the other hand, in Solaris (a Unix OS), we have a
format, fmthard
for the ‘create’ task
.
You can refer to the list of Linux and Unix commands, you will find that the Linux and Unix commands are similar but not the same.
Examples
So far, in this article, we have seen the generalized core differences between Linux and Unix. These differences can be more specific if we compare the exact versions of the two. Let us see this through some examples.
Solaris vs Linux
Solaris, which is now called Oracle Solaris is a Unix family OS. Let’s compare Linux with Solaris.
Linux supports more system architectures than Solaris does. Hence, Linux is more portable.
While talking about stability and hardware integration, Solaris seems to be better here. Linux also has a faster rate of development when compared to Solaris.
There are a few other technical differences between the two, but here we are limiting our comparison only to performance.
MacOS vs Linux
MacOS is a certified Unix OS. It has its own kernel named XNU. It is used in Apple’s computers which are considered the most reliable PCs.
MacOS is relatively easy to set up. On the other side, Linux is cheaper and has a lot of open-source software available as against Apple’s proprietary solutions. Also, Linux is more flexible as it can be executed on almost any hardware whereas MacOS can run only on Apple hardware.
For Example
, iPhones.
MacOS uses HFS+ as a default file system whereas Linux uses ext4.
Conclusion
Unix is very old and is said to be the mother of all operating systems. Linux kernel is also derived from Unix. The major difference between Unix and Linux-based operating systems is not in the presentation part, but on how they work internally, i.e. mainly at the kernel part.
The difference between the two will also depend upon which exact versions of Linux and Unix you are comparing.
It’s also essential to state that Linux (and many other Unix-like OS) are free to obtain and modify, whereas Unix operating systems are not. Cost is always a major concern when deciding what technology to use, and Linux has an edge in this regard.
Linux is more flexible and free when compared to true Unix systems and that is why Linux has gained more popularity. While discussing the commands in Unix and Linux, they are not the same but are very much similar. The commands in each distribution of the same family OS also vary.
Solaris, HP, Intel, etc. employ Unix internet servers, workstations, and personal computers. While, Linux is widely employed for computer software & hardware, gaming, tablet, mainframes, etc.
Some studies say that Linux is growing faster than any other OS in the past few years. Hence, in the future, Linux may tend to leave UNIX installations far behind.
References:
Linux,
Unix,
Linux distribution,
Book: The Unix Programming Environment
Hope you enjoyed this informative article on Unix and Linux differences!!
=>
Click here for the Complete Unix Tutorial series
PREV Tutorial
|
NEXT Tutorial
Was this helpful?
Submit
Cancel
Thanks for your feedback!
Recommended Reading
Unix Pipes Tutorial: Pipes in Unix Programming
Overview of Pipes in Unix Programming: In this tutorial, we will learn more about Unix Pipes. Later, we will work with some of the remaining filter commands and see an example of piping them together. Unix Video #20:  Pipes in Unix A series of filter commands can be piped together…
What is Unix: A Brief Introduction to Unix
Introduction to Unix Operating System: Let's start with Tutorial #1: 'What is Unix' in this series. In this tutorial, you will be able to understand the basic concepts of operating systems, the features of Unix, along its Architecture. => Click here for the Complete Unix Tutorial series Unix Video #1:…
Unix Text Processing Commands: Unix Filters with Examples
Overview of Unix Filters Text Processing Utilities: In this tutorial, we will learn about filters and work with various filter commands. Filters are commands that read input from stdin and write output to stdout. By default, when using a shell terminal, the stdin is from the keyboard, and the stdout is…
File Manipulation in Unix: Overview of Unix File System
Overview of Unix File System: In this tutorial, we will dive deep into Unix File System. The file system is central to how Unix organizes information, and all the information that needs to be stored and retrieved uses the file system. In this tutorial, we cover Unix file structure, types…
READ MORE FROM THIS SERIES:
How to Install Software in Linux (3 Proper Ways)
UNIX Tutorial for Beginners (20+ In-depth Unix Training Videos)
Unix Commands: Basic and Advanced Unix Commands with Examples
Unix File System Commands Touch, Cat, Cp, Mv, Rm, Mkdir (Part B)
Unix Processes Control Commands Like Ps and Top (Part C)
Unix Utilities Programs Commands: Which, Man, Find Su, Sudo (Part D)
File Manipulation in Unix: Overview of Unix File System
Unix File Access Permissions: Unix Chmod, Chown and Chgrp
How to Compare Two Files in Unix: File Comparison Commands
Unix Special Characters or Metacharacters for File Manipulation
How to Use Unix Regular Expressions
Unix Shell Scripting Tutorial with Examples
Working with Vi Editor in Unix
Working with Unix Variables: Features of Shell Scripting
Unix Shell Script Arithmetic and Boolean Operators Examples
Unix Conditional Statements: If Then Else and Relational Operators
Using Switch Case in Unix Shell Scripting: Case-esac Statement
Unix Shell Loop Types: Do While Loop, For Loop, Until Loop in Unix
Unix Shell Script Functions with Parameters and Return
Unix Text Processing Commands: Unix Filters with Examples
Unix Pipes Tutorial: Pipes in Unix Programming
More Unix Filter and Awk, Sed Commands in Text Processing
Command Line Arguments in Unix Shell Script with Example
Processes in Unix: Process Control and Debugging Commands
Advanced Unix Shell Scripting: Arrays, File and String Test Operators, Special V…
What is Unix: A Brief Introduction to Unix
Unix Vs Linux: What is Difference Between UNIX and Linux
Unix Permissions: File Permissions in Unix with Examples
Grep Command in Unix with Simple Examples
Cut Command in Unix with Examples
Tar Command in Unix To Create Backups (Examples)
Find Command in Unix: Find Files with Unix Find File (Examples)
Ls Command in Unix with Examples
Unix Cat Command Syntax, Options with Examples
Unix Sort Command with Syntax, Options and Examples
Linux vs Windows Difference: Which Is The Best Operating System?
Linux Commands Tutorial: Learn Basic Linux Commands For Beginners
12 SCP Command Examples To Securely Transfer Files In Linux
Ubuntu Vs Windows 10 – Which Is A Better OS
Leave a Comment
Cancel reply
Comment
Name
Email
Δ
About SoftwareTestingHelp
Helping our community since 2006!
Most popular portal for Software professionals with
400 million+ visits and 500,000+ followers!
You will absolutely love our creative content on QA, Dev, Software Tools & Services Reviews!
Learn In This Article:
What is UNIX?
What is Linux?
Difference Between Unix and Linux
Linux vs Unix Kernel
Unix Vs Linux Commands
Conclusion

### What Is Linux? (link)
*URL:* https://www.linux.com/what-is-linux/

# What is Linux? - Linux.com

What is Linux? - Linux.com
X
Topic
AI/ML
Cloud
Desktop
Embedded/IoT
Governance
Hardware
Linux
Networking
Open Source
Security
System Administration
Audience
Developers
DevOps
Enterprise
Enthusiast
Resources
Tutorials
Training
Certification
Events
Forums
Q&A
What is Linux?
About Us
Search
Sign in
Welcome! Log into your account
your username
your password
Forgot your password? Get help
Password recovery
Recover your password
your email
A password will be e-mailed to you.
X
Linux.com
Topic
AI/ML
Cloud
Desktop
Embedded/IoT
Governance
Hardware
Linux
Networking
Open Source
Security
System Administration
Audience
Developers
DevOps
Enterprise
Enthusiast
Resources
Tutorials
Training
Certification
Events
Forums
Q&A
What is Linux?
About Us
Home
What is Linux?
What is Linux?
Looking to get started in Linux? Develop a good working knowledge of Linux using both the graphical interface and command line across the major Linux distribution families with The Linux Foundation’s
Intro to Linux
online course. Enroll for free
here
. (Este curso también está disponible en español.
Haga clic aquí para Introducción a Linux.
)
From smartphones to cars, supercomputers and home appliances, home desktops to enterprise servers, the Linux operating system is everywhere.
Linux has been around since the mid-1990s and has since reached a user-base that spans the globe. Linux is actually everywhere: It’s in your phones, your thermostats, in your cars, refrigerators, Roku devices, and televisions. It also runs most of the Internet, all of the world’s top 500 supercomputers, and the world’s stock exchanges.
But besides being the platform of choice to run desktops, servers, and embedded systems across the globe, Linux is one of the most reliable, secure and worry-free operating systems available.
Here is all the information you need to get up to speed on the Linux platform.
What is Linux?
Just like Windows, iOS, and Mac OS, Linux is an operating system. In fact, one of the most popular platforms on the planet, Android, is powered by the Linux operating system. An operating system is software that manages all of the hardware resources associated with your desktop or laptop. To put it simply, the operating system manages the communication between your software and your hardware. Without the operating system (OS), the software wouldn’t function.
The Linux operating system comprises several different pieces:
Bootloader –
The software that manages the boot process of your computer. For most users, this will simply be a splash screen that pops up and eventually goes away to boot into the operating system.
Kernel –
This is the one piece of the whole that is actually called ‘Linux’. The kernel is the core of the system and manages the CPU, memory, and peripheral devices. The kernel is the lowest level of the OS.
Init system –
This is a sub-system that bootstraps the user space and is charged with controlling daemons. One of the most widely used init systems is systemd, which also happens to be one of the most controversial. It is the init system that manages the boot process, once the initial booting is handed over from the bootloader (i.e., GRUB or GRand Unified Bootloader).
Daemons –
These are background services (printing, sound, scheduling, etc.) that either start up during boot or after you log into the desktop.
Graphical server –
This is the sub-system that displays the graphics on your monitor. It is commonly referred to as the X server or just X.
Desktop environment –
This is the piece that the users actually interact with. There are many desktop environments to choose from (GNOME, Cinnamon, Mate, Pantheon, Enlightenment, KDE, Xfce, etc.). Each desktop environment includes built-in applications (such as file managers, configuration tools, web browsers, and games).
Applications –
Desktop environments do not offer the full array of apps. Just like Windows and macOS, Linux offers thousands upon thousands of high-quality software titles that can be easily found and installed. Most modern Linux distributions (more on this below) include App Store-like tools that centralize and simplify application installation. For example, Ubuntu Linux has the Ubuntu Software Center (a rebrand of GNOME Software) which allows you to quickly search among the thousands of apps and install them from one centralized location.
Why use Linux?
This is the one question that most people ask. Why bother learning a completely different computing environment, when the operating system that ships with most desktops, laptops, and servers works just fine?
To answer that question, I would pose another question. Does that operating system you’re currently using really work “just fine”? Or, do you find yourself battling obstacles like viruses, malware, slow downs, crashes, costly repairs, and licensing fees?
If you struggle with the above, Linux might be the perfect platform for you. Linux has evolved into one of the most reliable computer ecosystems on the planet. Combine that reliability with zero cost of entry and you have the perfect solution for a desktop platform.
That’s right, zero cost of entry… as in free. You can install Linux on as many computers as you like without paying a cent for software or server licensing.
Let’s take a look at the cost of a Linux server in comparison to Windows Server 2016. The price of the Windows Server 2016 Standard edition is $882.00 USD (purchased directly from Microsoft). That doesn’t include Client Access License (CALs) and licenses for other software you may need to run (such as a database, a web server, mail server, etc.). For example, a single user CAL, for Windows Server 2016, costs $38.00. If you need to add 10 users, for example, that’s $388.00 more dollars for server software licensing.  With the Linux server, it’s all free and easy to install. In fact, installing a full-blown web server (that includes a database server), is just a few clicks or commands away (take a look at Easy LAMP Server Installation to get an idea how simple it can be).
If zero cost isn’t enough to win you over–what about having an operating system that will work, trouble free, for as long as you use it? I’ve used Linux for nearly 20 years (as both a desktop and server platform) and have not had any issues with ransomware, malware, or viruses. Linux is generally far less vulnerable to such attacks. As for server reboots, they’re only necessary if the kernel is updated. It is not out of the ordinary for a Linux server to go years without being rebooted. If you follow the regular recommended updates, stability and dependability are practically assured.
Open source
Linux is also distributed under an open source license. Open source follows these key tenets:
The freedom to run the program, for any purpose.
The freedom to study how the program works, and change it to make it do what you wish.
The freedom to redistribute copies so you can help your neighbor.
The freedom to distribute copies of your modified versions to others.
These points are crucial to understanding the community that works together to create the Linux platform. Without a doubt, Linux is an operating system that is “by the people, for the people”. These tenets are also a main factor in why many people choose Linux. It’s about freedom and freedom of use and freedom of choice.
What is a “distribution?”
Linux has a number of different versions to suit any type of user. From new users to hard-core users, you’ll find a “flavor” of Linux to match your needs. These versions are called distributions (or, in the short form, “distros”). Nearly every distribution of Linux can be downloaded for free, burned onto disk (or USB thumb drive), and installed (on as many machines as you like).
Popular Linux distributions include:
LINUX MINT
MANJARO
DEBIAN
UBUNTU
ANTERGOS
SOLUS
FEDORA
ELEMENTARY OS
OPENSUSE
Each distribution has a different take on the desktop. Some opt for very modern user interfaces (such as GNOME and Elementary OS’s Pantheon), whereas others stick with a more traditional desktop environment (openSUSE uses KDE).
You can check out the top 100 distributions on the
Distrowatch
.
And don’t think the server has been left behind. For this arena, you can turn to:
Red Hat Enterprise Linux
Ubuntu Server
Centos
SUSE Enterprise Linux
Some of the above server distributions are free (such as Ubuntu Server and CentOS) and some have an associated price (such as Red Hat Enterprise Linux and SUSE Enterprise Linux). Those with an associated price also include support.
Which distribution is right for you?
Which distribution you use will depend on the answer to three simple questions:
How skilled of a computer user are you?
Do you prefer a modern or a standard desktop interface?
Server or desktop?
If your computer skills are fairly basic, you’ll want to stick with a newbie-friendly distribution such as Linux Mint, Ubuntu (Figure 3), Elementary OS or Deepin. If your skill set extends into the above-average range, you could go with a distribution like Debian or Fedora. If, however, you’ve pretty much mastered the craft of computer and system administration, use a distribution like Gentoo. If you really want a challenge, you can build your very own Linux distribution, with the help of Linux From Scratch.
If you’re looking for a server-only distribution, you will also want to decide if you need a desktop interface, or if you want to do this via command-line only. The Ubuntu Server does not install a GUI interface. This means two things your server won’t be bogged down loading graphics and you’ll need to have a solid understanding of the Linux command line. However, you can install a GUI package on top of the Ubuntu Server with a single command like sudo apt-get install ubuntu-desktop. System administrators will also want to view a distribution with regards to features. Do you want a server-specific distribution that will offer you, out of the box, everything you need for your server? If so, CentOS might be the best choice. Or, do you want to take a desktop distribution and add the pieces as you need them? If so, Debian or Ubuntu Linux might serve you well.
Installing Linux
For many people, the idea of installing an operating system might seem like a very daunting task. Believe it or not, Linux offers one of the easiest installations of all operating systems. In fact, most versions of Linux offer what is called a Live distribution, which means you run the operating system from either a CD/DVD or USB flash drive without making any changes to your hard drive. You get the full functionality without having to commit to the installation. Once you’ve tried it out, and decided you wanted to use it, you simply double-click the “Install” icon and walk through the simple installation wizard.
Typically, the installation wizards walk you through the process with the following steps (We’ll illustrate the installation of Ubuntu Linux):
Preparation: Make sure your machine meets the requirements for installation. This also may ask you if you want to install third-party software (such as plugins for MP3 playback, video codecs, and more).
Wireless setup (if necessary): If you are using a laptop (or machine with wireless), you’ll need to connect to the network, in order to download third-party software and updates.
Hard drive allocation (Figure 4): This step allows you to select how you want the operating system to be installed. Are you going to install Linux alongside another operating system (called “dual booting”), use the entire hard drive, upgrade an existing Linux installation, or install over an existing version of Linux.
Location: Select your location from the map.
Keyboard layout: Select the keyboard for your system.
User setup: Set up your username and password.
That’s it. Once the system has completed the installation, reboot and you’re ready to go. For a more in-depth guide to installing Linux, take a look at “How to Install and Try Linux the Absolutely Easiest and Safest Way” or download the Linux Foundation’s PDF guide for Linux installation.
Installing software on Linux
Just as the operating system itself is easy to install, so too are applications. Most modern Linux distributions include what most would consider an app store. This is a centralized location where software can be searched and installed. Ubuntu Linux (and many other distributions) rely on GNOME Software, Elementary OS has the AppCenter, Deepin has the Deepin Software Center, openSUSE has their AppStore, and some distributions rely on Synaptic.
Regardless of the name, each of these tools do the same thing: a central place to search for and install Linux software. Of course, these pieces of software depend upon the presence of a GUI. For GUI-less servers, you will have to depend upon the command-line interface for installation.
Let’s look at two different tools to illustrate how easy even the command line installation can be. Our examples are for Debian-based distributions and Fedora-based distributions. The Debian-based distros will use the apt-get tool for installing software and Fedora-based distros will require the use of the yum tool. Both work very similarly. We’ll illustrate using the apt-get command. Let’s say you want to install the wget tool (which is a handy tool used to download files from the command line). To install this using apt-get, the command would like like this:
sudo apt-get install wget
The sudo command is added because you need super user privileges in order to install software. Similarly, to install the same software on a Fedora-based distribution, you would first su to the super user (literally issue the command su and enter the root password), and issue this command:
yum install wget
That’s all there is to installing software on a Linux machine. It’s not nearly as challenging as you might think. Still in doubt? Recall the Easy Lamp Server Installation from earlier. With a single command:
sudo taskel
You can install a complete LAMP (Linux Apache MySQL PHP) server on either a server or desktop distribution. It really is that easy.
More resources
If you’re looking for one of the most reliable, secure, and dependable platforms for both the desktop and the server, look no further than one of the many Linux distributions. With Linux you can assure your desktops will be free of trouble, your servers up, and your support requests minimal.
For more information to help guide you through your lifetime with Linux, check out the following resources:
Linux.com
: Everything you need to know about Linux  (news, tutorials and more)
Howtoforge
: Linux tutorials
Linux Documentation Project
: How-tos, guides, and FAQs
Linux Knowledge Base and Tutorial
: Plenty of tutorials and in-depth guides
LWN.net
: Linux kernel news and more
Copyright © 2026 The Linux Foundation®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our
Trademark Usage
page. Linux is a registered trademark of Linus Torvalds.

### What Is Unix, and Why Does It Matter? (link)
*URL:* https://www.howtogeek.com/182649/htg-explains-what-is-unix/

# What Is Unix, and Why Does It Matter?

What Is Unix, and Why Does It Matter?
Close
Close
By
Chris Hoffman
Published
Sep 22, 2016, 9:34 AM EDT
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
Unix's Design Lives On Today
Tracing the Unix Descendants
The Rise of DOS and Windows NT
Why it Matters
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
Most operating systems can be grouped into two different families. Aside from Microsoft's Windows NT-based operating systems, nearly everything else traces its heritage back to Unix.
Linux, Mac OS X, Android, iOS, Chrome OS, Orbis OS used on the PlayStation 4, whatever firmware is running on your router -- all of these operating systems are often called "Unix-like" operating systems.
Unix's Design Lives On Today
Related:
What Does "Everything Is a File" Mean in Linux?
Unix was developed in AT&T's Bell Labs back in the mid-to-late 1960's. The initial release of Unix had some important design attributes that live on today.
One is the "Unix philosophy" of creating small, modular utilities that do one thing and do them well. If you're familiar with using a Linux terminal, this should be familiar to you -- the system offers a number of utilities that can be combined in different ways through
pipes and other features
to perform more complex tasks. Even graphical programs are likely calling simpler utilities in the background to do the heavy lifting. This also makes it easy to
create shell scripts
, stringing together simple tools to do complicated things.
Unix also had a single file system that programs use to communicate with each other. This is
why "everything is a file" on Linux
- including hardware devices and special files that provide system information or other data. It's also why only Windows has drive letters, which it inherited from DOS -- on other operating systems, every file on the system is part of a single directory hierarchy.
Tracing the Unix Descendants
Like any history going back over 40 years, the history of Unix and its descendants is messy. To simplify things, we can roughly group Unix's descendants into two groups.
One group of Unix descendants were developed in academia. The first was BSD (Berkeley Software Distribution), an open-source, Unix-like operating system. BSD lives on today through FreeBSD, NetBSD, and OpenBSD. NeXTStep was also based on the original BSD, Apple's Mac OS X was based on NeXTStep, and iOS was based on Mac OS X. Many other operating systems, including the Orbis OS used on the PlayStation 4, are derived from types of BSD operating systems.
Related:
The Great Debate: Is it Linux or GNU/Linux?
Richard Stallman's GNU project was also started as a reaction to AT&T's increasingly restrictive Unix software licensing terms. MINIX was a Unix-like operating system created for educational purposes, and Linux was inspired by MINIX.
The Linux we know today is really GNU/Linux
, as it's made up of the Linux kernel and a lot of GNU utilities. GNU/Linux isn't directly descended from BSD, but it is descended from Unix's design and has its roots in academia. Many operating systems today, including Android, Chrome OS, Steam OS, and a huge amount of embedded operating systems for devices, are based on Linux.
On the other hand, there were the commercial Unix operating systems. AT&T UNIX, SCO UnixWare, Sun Microsystems Solaris, HP-UX, IBM AIX, SGI IRIX -- many big corporations wanted to create and license their own versions of Unix. These aren't quite as common today, but some of them are still out there.
Image Credit:
Wikimedia Commons
The Rise of DOS and Windows NT
Related:
Why Windows Uses Backslashes and Everything Else Uses Forward Slashes
Many people expected Unix to become the industry standard operating system, but DOS and "IBM PC compatible" computers eventually exploded in popularity. Microsoft's DOS became the most successful DOS of them all. DOS was never based on Unix at all, which is
why Windows uses a backslash for file paths while everything else uses a forward slash
. This decision was made back in the early days of DOS, and later versions of Windows inherited it, just as BSD, Linux, Mac OS X, and other Unix-like operating systems inherited many aspects of Unix's design.
Windows 3.1, Windows 95, Windows 98, and Windows ME were all based on DOS underneath. Microsoft was developing a more modern and stable operating system at the time, which they named Windows NT -- for "Windows New Technology." Windows NT eventually made its way to regular computer users as Windows XP, but it was available for corporations as Windows 2000 and Windows NT before that.
All of Microsoft's operating systems are based on the Windows NT kernel today. Windows 7, Windows 8, Windows RT, Windows Phone 8, Windows Server, and the Xbox One's operating system all use the Windows NT kernel. Unlike most other operating systems, Windows NT wasn't developed as a Unix-like operating system.
Microsoft didn't start with a completely clean slate, of course. To maintain compatibility with DOS and old Windows software, Windows NT inherited many DOS conventions like drive letters, backslashes for file paths, and forward slashes for command-line switches.
Why it Matters
Have you ever taken a look at the Mac OS X terminal or file system and noticed how similar it was to Linux's, and how different they both were from Windows? Well, this is why --  both Mac OSX and Linux are Unix-like operating systems.
Knowing this bit of history helps you understand what a "Unix-like" operating system is, and why so many operating systems seem so similar to each other while Windows seems so different. This explains why the terminal on Mac OS X will feel so familiar to a Linux geek, while
the Command Prompt and PowerShell on Windows
are so different from other command-line environments.
This was just a quick history that will help you understand how we got to where we are today without getting bogged down in the details. If you want more information, you can find entire books on the history of Unix.
Image Credit:
Peter Hamer on Flickr
,
Takuya Oikawa on Flickr
,
CJ Sorg on Flickr
Features
Android
Linux & macOS Terminal
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
Android's best AirTag rival is getting a sequel, and it's only $20
New on Disney+ and Hulu in July 2026—Hot picks and everything else coming
The $40K used SUV that remembers what luxury should feel like
