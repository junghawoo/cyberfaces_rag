---
title: "Justice in Data: Introduction to Python Programming"
unit_id: 132
course_id: 10
level: "Foundation"
slug: justice-in-data-introduction-to-python-programming
is_course: 0
---

# Justice in Data: Introduction to Python Programming

## Extracted resources (local files)

### Introduction to Python Slides
*Source file:* `Tuesday - Intro to Python Presentation.pdf`  ·  *type:* file

Introduction to 
Python 
Programming

Presenters
2
Sharma Chakravarthy, PhD
Professor
Steven Tanner McCullough
PhD Student Researcher
June Young Park, PhD
Assistant Professor
Jessica Eisma, PhD
Assistant Professor
Junaid Ahmad
PhD Student Researcher

This lectures objectives
●Apply basic programming 
concepts
●Understand Python syntax and 
logic
●Create a program that can…
●Manipulate Data
●Have decision trees
●Make use of data tools
3
Students should be able to…

Lecture Overview
4
Programming in 
Engineering
Python 
Primer
Programming 
Syntax
In Class 
Example

Introduction
Programming in 
Engineering
Python 
Primer
Programming 
Syntax
In Class 
Example

How do Engineers use programming?
6
Autodesk Revit
Engineering Tools
Apollo Flight Computer
Engineering Applications
ESRI ArcGIS Pro

What about Data Science and 
Civil Engineers?
7
Using ML to accurately predict 
occupant behavior and energy 
consumption
Predicting water supply 
contaminants concentrations within 
a water supply system over time.

How do we interface with computers?
8
●
Users entered commands in 
early Operating Systems
○
Copying files, mathematical 
calculations etc.
●
Graphical Interfaces allowed 
for commands to be 
performed with gestures.
○
Buttons, checkboxes, etc.
○
These gestures just call upon 
scripts of commands
Example of DOS Terminal
Windows Terminal in Win 10 
Windows GUI

How do we interface with computers?
9
●Applications of programming 
include a variety of different 
uses
○
Editors, IDEs, video player, 
compiler, Skype, …
So how are 
these made?

How are these made?
10
●
Computer programs are written 
in a programming language
○
These languages have their own 
rules and grammar
○
This is the syntax of a language
●
The computer then interprets 
this language into its native 
code
○
This code is interpreted in order
○
Logical Intent between 
commands slightly vary between 
languages
Programming!

Introduction
Programming in 
Engineering
Python 
Primer
Programming 
Syntax
In Class 
Example

●Countless languages exist
○
Many derive properties from 
other languages
●Some languages are stronger in 
some areas vs others
○C++ for instance has 
excellent performance
●Python will be our selected 
language
12
What Language to use?
Why Python?

●
Python is a 
‘high-level’ language.
●
Memory self-managed
●
Considerably faster to 
program in than something 
like C++ or Assembly
●
Extremely large online 
community
●
The language with the 
easiest learning curve
Both do the same 
thing!
Popular with researchers, companies 
and governments!
Why Python?
13

• Python was conceived in the 80’s and 
was influenced by many languages 
(ABC, SETL, Perl, …)
• Is an interpreted high-level programming 
language and emphasizes code readability with 
the use of indentation
• As of 2021, 3rd most popular language behind 
Java and C
• Object-oriented
• Variable names are untyped (no need to indicate 
type)
Python History
14

YOU are going to write your Python code using 
Jupyter Notebook
The Version of Jupyter we will be using is built in to 
MyGeoHub
○
Code is written and run in “cells” or short sections 
of code
○
Code can be edited and ran simultaneously or ran 
when needed
○
Platform indifferent – runs in web browser
Source: Donna French
Tutorial: https://docs.python.org/3/tutorial/index.html
Python Primer
15

Navigating Jupyter
16
The start screen for Jupyter works like any file explorer.
Can create & delete folders, simple files.

Navigating Jupyter
17
Creates a new python 
notebook, make sure it is 
just “Python 3” if it is 
created.
Creates a folder in the 
folder you are working in
Launches a 
Terminal/CMD prompt 
environment to work in

Navigating Jupyter
18
This is where you’ll spend most of your time. This is the actual 
notebook editor. Selecting the cell but not clicking inside the 
text box allows you to use some hotkeys to do things.

Navigating Jupyter
19
Press B on the 
keyboard to 
create a cell Below
Double Press D on 
the keyboard to 
Delete a cell
Press A on the 
keyboard to 
create a cell Above

Navigating Jupyter
20
Most used cells are Code and 
Mark down, they can be set in 
this menu.
Cell Markdowns can be 
used to create titles for 
sections of code or lists.
Great for organizing code!
Code Cells do the actual 
computation work of 
what you want to do.

Navigating Jupyter
21
Shift+Enter will run the selected cell. It will 
generate an output below it and then 
create another empty cell underneath, like 
a calculator functionality.
Code Cells will run according 
to Python rules.
Markdown Cells have their 
own rules to create titles, etc…

Jupyter Sessions
22
●When you finish with a script in Jupyter Notebook you need to make sure 
you close the session after.
●Each new Jupyter file will create a new process. 
○Too many can overload your PC (or the server host)
○Running Scripts on a computer has no limit
■MyGeoHub has a limit of 3 per user.

Basics of Programming
23
Do this
Do that
Give this
Programming is the act of giving 
instructions to a computer.
These instructions will always be 
performed in sequential order, one 
after another.
There are slight caveats to this with 
Jupyter notebook

•
Borrow ideas whenever it makes 
sense
•
Things should be as simple as 
possible, but no simpler (Occam’s 
Razor)
•
Platform independence (Windows, 
Unix, Arm…)
•
Zen of Python (a few from Tim 
Peters)
•
Readability counts!
•
Easy Implementation & makes sense!
If your explanation feels like this, then it 
might need revision.
Overall Programming Philosophy
24

Syntax Basics
Programming in 
Engineering
Python 
Primer
Programming 
Syntax
In Class 
Example

●Syntax simply put is the 
grammar of the programming 
language
●How the computer interprets 
your instructions.
●Simplest in Python
●If syntax is not correct, most 
times the program will not 
launch
Overall Philosophy - Syntax
26

Libraries
●
First thing that is done in almost 
every script you will create
●
import <Library Name>
●
Think of libraries as extra tools to 
supplement the tools (Python) 
you currently have
●
Commonly used libraries 
include…
Libraries can be imported with shorter names that you decide.
Import <library> as <nickname>
27
If you think of Python as your desk to work at then…
Libraries are tools you 
use at this desk.

Variables
Programming in 
Engineering
Python 
Primer
Programming 
Syntax
In Class 
Example

●
The next step is to create 
placeholders for the data you are 
working with
●
These are called variables
●
Variables are volatile and will lose 
their values when the script 
finishes
●
Variable assignment always works 
in one direction
Variables
29
A = B
A will be replaced by B
B will not be replaced by A

Data Types
30
• Simple & Complex numbers (1,2,5.12, 15+2i)
Numbers
• Lists, sets, tuples, dictionaries etc… ( [1,2,3,4] )
Grouped Variables / Matrices
• Words, letters etc… (“Hello my name is Mr. Python, Mr. Worldwide”, “A”, “500 
gallons”)
Strings + Characters
• True or False only. (On or Off / 1 or 0)
Boolean

●Python only has 3 Types
○
Floats, Integers and Complex
■
Floating Point, sometimes 
called float,
is the default type for most 
numerical values for variable 
assignment.
■
Integers are used commonly 
as well but will only keep 
track of whole numbers.
■
Complex numbers are used 
less often but allow for 
real/imaginary number pairs 
to be used.
Numbers
31
●Integers have no decimal 
precision.
●Floating Point variables do 
have decimal precision.

Interactive Example
Numbers
32
●
You will be assigned to break out rooms
○
We will come to check in to see how each of you are doing
For The Activity – ( 10 Minutes)
●
Under the Jupyter Notebook tool in Activities
○
Open numbers.ipynb
○
Follow along with the Instructions

Group Variable Data
33
●Python has excellent capabilities for 
data that is grouped in forms like tables
●There are many options for grouped variables
○Lists will likely be the most used
■A more advanced form called DataFrames
will be introduced
○Others exists as well like tuples, sets and 
dictionaries

Grouped 
Data
List
Tuple
Set
Dictionary
Mutable and Ordered.
Denoted by square brackets []
These are true lists that can have each element 
changed without changing the entire list.
L = [ ‘a’ , 2 , ’c’ , 40 ]
Immutable and Ordered.
Denoted by parenthesis ()
Can only change the entire matrix, not single elements.
T = ( 2 , 2 , 4 )
Mutable and Un-ordered
Denoted by curly braces {}  created with set()
Very similar to lists except that an occurrence of a value 
can only happen once, order does not matter.
S = set(1,2,2,3,3,1) = { 1 , 2 , 3 }
Mutable and Ordered
Denoted by curly braces AND string tags
A list with elements that can be categorized with tags.
D = { 'Column 1’ : [1,2] , 'Column 2’ : [3,4] }
Group Variable Data
34

●To grab a single number from a list you need an index
●Python index starts from 0 as most other languages
○Same for arrays,  strings,  lists, … Not sets (Why?)
○Goes from 0 to the length of the list-1.
○Gives ArrayBoundException error in other languages
J
U
S
T
I
C
E
1
0
ARRAY / STRING
(len() -1) 
or 8
index
index
Unique to Python
-1
-len() 
Python Indexing
35

Matrices - Interactive
Data Types
36
●
You will be assigned to break out rooms
○
We will come to check in to see how each of you are doing
For The Activity – ( 10 Minutes)
●
Under the Jupyter Notebook tool in Activities
○
Open matrix.ipynb
○
Follow along with the Instructions

●
Characters are just the computers 
interpretation of numbers as letters on a 
keyboard
○
Denoted by Single Quotes ‘’
○
‘A’ , ‘%’ , ‘5’
○
Numbers can lose their numerical value as a 
character
●
Words and sentences are a list of this 
characters that are strung together, these 
are called strings
○
Denoted by Double quotes “”
○
“Hello everyone!” , “I”
○
Strings are immutable! (Cannot change in place)
H
e
l
l
o
e
v
e
r
y
o
n
e
!
Characters & Strings
37

Strings - Interactive
Data Types
38
●
You will be assigned to break out rooms
○
We will come to check in to see how each of you are doing
For The Activity – ( 10 Minutes)
●
Under the Jupyter Notebook tool in Activities
○
Open Strings.ipynb
○
Follow along with the Instructions

Operator
Description
Example
Result
+
Addition
3+4
7
-
Subtraction
3-4
-1
*
Multiplication   
3*4
12
/
Division
3/4
0.75
%
Modulus 
(Mod)
10%3
1
//
Integer 
Division
3//4
0
**
Exponential
3**4
81
39
Operators
●Operators are simply methods of 
manipulating numbers through 
mathematical means
●Some operators have different 
syntax than what is traditionally 
used in some math type software
○
Exponential uses a double star 
instead of the carrot
●Order of Operations does apply 
here
●If unsure, always use parenthesis!

Conditionals
Programming in 
Engineering
Python 
Primer
Programming 
Syntax
In Class 
Example

●Boolean values are just a 
simple True or False
●They can be depicted as 
a 1 or a 0 as well
●These are very important 
for decision making 
inside of the program
True
False
Logic and Boolean Values

●Conditional statements are simply 
decisions that are made within the 
code
●These are done by using an
if statement
●Code to be run when the decision is 
true must be ‘tabbed’ over
Is X True?
If True
If False
Perform Action 1
Perform Action 2
Start
Conditional
Code to be 
run if true
Output!
End
Conditional Statements
Sometimes 
this is just 
doing 
nothing!

●
If statements can be strung together 
with elif (else if) for extra conditions to 
be checked.
●
These conditions are checked 
sequentially
○
The first True will exit the conditional 
after the code has run and will skip 
the other conditionals
●
An else statement is used for any 
other condition not caught 
previously
skip
skip
Conditional Statements

Boolean_variable = 0
if Boolean_variable:
do_stuff()
else:
do_something_else()
Boolean_variable = 1
Conditional Statements - Syntax
x = 3
if x<2:
do_stuff()
elif x<4:
x = 7
elif x<6:
do_something_else()
else:
do_this()
print(x)
Conditional
Boolean Condition (True/False)
Runs only with decision
Always runs

Loops
Programming in 
Engineering
Python 
Primer
Programming 
Syntax
In Class 
Example

●What if you need to run 
the same operation over 
and over?
●Or you need to perform 
the same operation?
Loops
Do this
Do this again
Do this again
Do this again
Do this again

●Loops are an easy way to iterate 
over large amounts of data
●They will continue running in a 
circular loop until the exit 
condition is reached
●while() loops have a dynamic 
exit condition
●for() loops have a set exit 
condition
Repeat until 
exit
Do this
Give this
Loops

●Loops are comprised of 3 parts
○The Call (Start)
○The Body (Loop)
○The exit condition (Exit)
●The exit condition is formed in 1 of 2 
ways
1.
It is met as a condition in the 
body
2.
It is stated before the body in the 
loop call
Loops
Loop 
Call
Body
Exit Condition
Loop Call + Exit 
Condition
Body
Type 2
Type 1

●
While loops
○
The exit condition can 
dynamically change 
depending on how the 
code runs
Types of loops
●
For loops
○
The exit condition is a set 
number of times to run
○
Built specifically to iterate 
over a list or string

●
Decisions, loops and lists can be 
put inside of one another, this is 
called nesting.
●
An example is provided to the 
right
○
A for loop iterates over each character 
in a string
○
Within the loop a check is performed 
to see if the character is the letter ‘L’
○
Each time that is true it will print that 
letter out
●
A 2D table is a list that contains lists.
Action 1
Loop
Action 2
Decision
Nesting
Jane
Doe
25
John
Brown
30
Jim
Ford
22

●Functions are snippets of 
code that can be called upon 
to re-do a task with variables
●All libraries have functions 
that can be used
○The time.sleep() function 
is one such example
●Custom functions can be 
made to tidy repetitive 
portions of code
Functions

●Syntax
○A command is typed incorrectly
○EX: primt(“Hello World”)
●Logic
○Program compiles but has un-intended consequences
○EX: If i>5: instead of i<5:
●Runtime
○Like logic errors but not hardcoded
○EX: Attempting to access something that does not exist.
Errors

Examples
Programming in 
Engineering
Python 
Primer
Programming 
Syntax
In Class 
Example

●
In data science Pandas is the king of 
data management
○
Pandas is an extension of the traditional 
lists, libraries and dictionaries.
○
Two ‘classes’ are used from this library
■
DataFrames
■
Pandas Series
○
Pandas has built in functions to 
read/write files
●
Usually imported by 
54
Pandas
Special Libraries and Functions
Series
DataFrame
Index
Months
0
January
1
February
2
March
3
April
Index
Months
Days
Etc…
0
January
31
1
February
28
2
March
31
3
April
30
A Series
●
Ordered List
●
1 Dimension
●
Built-in functions 
to clean, organize 
and search data
A DataFrame
●
Multi-dimensional 
series
●
Same functions as 
a series
import pandas as pd

●
NumPy is the basis for most scientific 
computation, many Pandas 
functions are derived from NumPy
○
The primary variable that NumPy 
provides are called arrays.
●
These have many built in functions 
available for matrix manipulation.
○
NumPy arrays are considerably 
faster, great for large data sets
55
import numpy as np
Arrays & Common Functions
Numerical Python - NumPy
Numpy also can…
●
Allows Users to quickly 
create an array
○
Can be arranged numbers 
for visualizations
○
Random numbers for 
testing
●
Grab strictly unique values 
from Arrays
●
Transposing Matrices.
●
Can also work with CSV files
●
Easily implement 
mathematical formulas

●
Many languages have large online 
communities that have existing code, 
examples and support for what you 
want to do most times.
●
Some examples include…
○
The official python wiki
■
Almost every library has its own 
documentation as well
○
stackoverflow.net
■
Search before you post!
○
Other repositories on GitHub
■
Check licenses
56
How to find out more

Interactive
Special Libraries and Functions
57
●
You will be assigned to break out rooms
○
We will come to check in to see how each of you are doing
For The Activity – (Remaining Time)
●
Under the Jupyter Notebook tool in Activities
○
Open extras.ipynb
○
Follow along with the Instructions while we have time to explore 
the extra functions, Pandas and Numpy

58
Any questions?
Thanks!

## Fetched resources (external URLs)

### Introduction to Python Programming Pre-Survey (link)
*URL:* https://utaedu.questionpro.com/a/TakeSurvey?tt=Vsdmb3CeLMEECHrPeIW9eQ%3D%3D

[survey link — skipped]

### Introduction to Python Programming Recording (link)
*URL:* https://www.youtube.com/watch?v=B6NapuHNux4

[YouTube transcript B6NapuHNux4]
um I will be the main presenter for this um uh presentation but um all of the content for this has been developed by all the uh presenters for the topic that we are going to be doing today um so just to kind of have a brief overview um I think it would be nice that after this presentation you should be able to apply basic programming Concepts understand the syntax and logic that python uses which is the language that we will be using and take those and apply those so that you can create a program that can manipulate data make decisions off that data and make use out of those data tools so that you can create your own tools so and I should iterate that this presentation is going to be short compared to what would be considered like a longer python class so there is going to be a lot of like kind of quick explanations if you have a question feel free to ask me and I'll try to do the best that I can to explain it so a quick overview of what we will be looking at we'll have some kind of programming and Engineering I know that not everyone here has an engineering background but you might get a kind of an understanding of like where and why we are using this programming um why we're using Python and kind of a brief introduction to it and then the um real in-depth portion of it where we have all the syntax uh the commands that you'll be using how to use Jupiter notebook and then ultimately we'll kind of dive into some examples that you guys will work with me so um first we'll look at programming and Engineering so um how do we use programming right so probably some of the most famous examples are in Aerospace and um like NASA's um applications like for instance the Apollo flight computer some of us though especially in the Civil field or those that use archees Engineers that need to understand surveying also need to understand [Music] programming so that you can apply those so that you can create these tools same thing with other stuff like civil 3D Autodesk Revit AutoCAD stuff like that so but what about more specific things like what we're doing so like in the energy sector you can use machine learning to accurately predict energy consumption based off of how people act inside of a building or maybe you can predict uh containments in a water supply and how that distributes over a water supply system just some very you know brief examples to kind of get you thinking about it right so how do we interface with computers and this is kind of an important step to this so that we understand what we're doing in Python so with computers back 30 40 years ago you would have a strict command line interface meaning that you had to type in the commands that you wanted it to do this meant maybe mathematical calculations copying files and you can see an example of that here on the right with what was considered the early dos terminal um advances and graphical interfaces sometimes called graphical user interfaces or just guise for short allow these commands to be performed much easier without needing to know the syntax of these commands so maybe you're pressing a button dragging a slider and typing in numbers to do things but all of the stuff that happens behind the scenes is still the same so you can even see an example of this inside of Windows Windows 10 terminal the command prompt as some of you may know it it still functions almost exactly the same as the MS-DOS terminal and it's just a more advanced version that has been changed over the last 20 years so um we have these applications that we use on it and these are things that come in the form of a variety of things um Skype for instance Microsoft teams what we're using right now um video players if you want to watch a movie listen to Skype uh or not Skype um music on like Spotify or apple music using Microsoft Excel Microsoft Word all sorts of these different programs are applications and they are complex sets of scripts and instructions that are programmed together right so text ask answer that question um they these are made with programming right so these are written in a programming language and programming languages are just like any other spoken language they have their own rules and grammar and spelling this is the syntax of this language and this is very important to learn when you are working with a programming language because this is how the computer interprets its instructions so and it's important to note from this the key takeaway from this here is that would you give a list of instructions to a computer it interprets it sequentially um and I think here actually yeah you okay you posted the survey okay I can give y'all a few minutes actually to finish that survey out um I think I just answered one of those questions for y'all whoops I'll wait for everyone to finish their survey here I think and then I will continue just give y'all a couple more minutes on that I apologize for that okay so hopefully I'll hit enough time to get to the survey um so we'll kind of cover over some of those questions that were in it um all of that's covered in the content for this so um okay so yeah um the syntax of the language is all of the rules that are about it um all of the grammar and spelling and things that you need to do to make sure that python understands what you want it to do correctly um and what's important to remember in this is that the computer looks at everything that you enter from the first thing to the last thing um and we'll kind of cover this here a little bit later so let's have an introduction to Python and the language that we'll be using so um you're probably wondering why are we using python there's tons of languages out there some are derivatives of others so you've probably heard of something like C plus plus maybe Java JavaScript c-sharp there's lots of languages that exist out there and some have different strengths and areas an example of this is that C plus plus typically has better performance than a lot of other languages given that you know how to use it however we will not be using that we will be using python for our selective language so why are we using that right um that's because python is known as like a high language high level language meaning that um it's easy to navigate and use um it self-manages its memory so there's not anything that you would have to do in terms of like making sure that your computer doesn't crash a lot of times python will do stuff behind the scenes that allows it to um keep itself from crashing basically that's not to say that it's not possible it's definitely possible to crash it another part of this being a high level language is python requires considerably less work to do things so an example here on the right is uh doing the same thing between Java and python python takes one line whereas Java if you were using the correct syntax and rules and nomenclature may take four to five lines and this can greatly change depending on what language you're using I give examples like C plus plus and assembly assembly takes a really long time to program something and the nice thing with python is it has a really large online community so you can go on to websites like stack Overflow or the python Wiki or any of the libraries and we'll talk about that in a minute they all have wikis communities forums that people post on and ask questions and most times if you have a question about something you can almost find someone that's asking that exact same question and you can get a nice answer for it and really it's arguably one of the more powerful languages that you can learn that has the easiest learning curve and it's important to know if you want to do research as a job python is very popular with researchers companies government work universities that's why we are teaching it because it's very well known to be like used so brief history of python it's influenced by a ton of different languages um and the kind of philosophy behind this language is it focuses on code readability and the use of indentation um and like I mentioned earlier it's very popular right behind the other two foremost used languages as of 2021. um and what's important to note is there's a lot of behind the scenes work that python does that you would normally have to do in another language so an example of this is you can just set a variable to a number without having to say what type of variable it is and I will go into a little bit more uh explanation on this and if you don't even know what I'm talking about that's okay we will go all over that so um so there's tons of tools that you can use to write Python scripts normally when you download python onto your computer you get What's called the idle editor which is the built-in called development environment for python we are not using that we will be using something called Jupiter notebook the website that hosts our course my geohub has its own version of Jupiter and its own version of python so you don't have to install anything everything is run through the web browser and what's unique about Jupiter is that it is run in cells or short sections of code and this code can be edited and ran simultaneously while you are editing another section of code and you can run certain sections of code as you need so what makes that unique is that if say you have a section of code that takes eight hours to run and you had a mistake in a section that only takes five seconds to run you don't have to rerun it for another eight hours you can just fix the short section and rerun that section again and the other thing that's unique about this is it's platforming different what that means is that you could run this on a Mac you can run it on a PC you can run it on a Linux machine if you have a Raspberry Pi stuff like that um it's very nice for that so um normally if you were to open up Jupiter I'm not going to have you guys do that with this I'm just going to give you kind of a brief overview of what you'll be seeing once you start opening this Jupiter when you open it for the very first time and you're not opening a script up it will open into a file explorer and yes what was the question oh oh I'm sorry I'm sorry I saw that in the chat for that was for someone else um yes so you can create scripts create folders um and simple files inside of this so some examples of this if you were to click click the new button inside of this you can create what's called a new notebook um this is just based on the Python 3 Library there's a lot of other options in this here we will not be using those options R is a different language built specifically just for data science you can't do a lot of other things that you can do in Python with it and all these other environments here are built for different types of tools I will not necessarily be going over those but you might use those later in the future um you can create folders for organization and you can also launch a terminal um some of you may know this again like the command prompt or Powershell basically this is something that you would use if you need to install something uh like a library for instance um you won't have to do that for this my geohub will have all of the tools and everything that you need installed for those scripts that we'll be testing today so this is kind of where you're going to be working a lot this is when you are inside of a python notebook you will have these cells here and what you will be seeing a lot of times is this section right here is where you will be typing code this right here so this is a text box and you can select the cell by clicking outside of it right here and you'll know it's a code box that you enter code into because it has an input on it that's what this in means right here this in right and you type code into it and you can create other cells or you can add as many lines as you want into this one cell so there's some hotkeys that I'll give you here B A and D you don't have to remember or memorize these necessarily but these are helpful keys that you can use if you want to create or delete cells and the reason that you would want to do this to create something maybe say below or above is say you have a section of code that you're running right and maybe you want it to do something after generate a new cell and you don't want to have to rerun this code again maybe say it took a long time generate a new cell below and then boom you can type in the new code that you want to run that works with that existing data that works from this so data can carry over between cells maybe say you need to restart again and you need it to do something beforehand you can press a create a cell above it and then type in your code into that if it's getting messy and you've added too many cells you can delete it by pressing D twice on it again you don't need to necessarily have these memorized if you open up the cell menu the all these options are there so the last thing the last couple of things I think I'll go over here are markdowns so what's kind of unique with Jupiter is you can separate out your code and organization into two different types of cell types so these cell code cells that I was talking about is where you do the heavy lifting that's where you're going to be running your actual code but you can organize it with pretty titles lists and so on and so forth with a different style of syntax I will not be teaching that in this but you can look this up it's a very simple syntax if you want to create easy ways to organize your code so you can for instance create a title or a list to organize your code and say this is what the next five sections of code do it's very helpful for yourself it's like if you were to use comments inside of code but it's in a way prettier way um but yes remember that these sections right here are the ones doing the actual work these ones right here will not do anything in terms of python so to run the cells if say you have something happening right so say we just do one plus one right the most simple math task that we can do to get that to run you can either press this button right here or if you press shift enter it will cause that cell to run all of its instructions and then you get an output from it so you have the input up here and the output right below it after you run a cell it will create a new One automatically underneath it so as you do work it will keep generating those um below it excuse me and remember that code cells run according to python tools markdown cells have their own rules markdown cells do not um will not cause a program to crash because they don't run according to python rules so um kind of a quick little tidbit here um I'll remind you guys for all of your sessions but make sure that when you're done with the interactive scripts that you close the session after the reason that we do this is um my geohub has a limit to how many scripts you can have open at a time my geohub calls this sessions um and you will not be able to run the last activity unless you terminate the previous ones that you've done so you do this just when you're inside the script and the top corner here there's a terminate session button just click that and it closes it and then you can close that window out and come back again to run it again if you want if you run this on your home PC if you download python download Jupiter and do all that good stuff um you can run as many of those as you would like just be careful doing that because you can overload your PC if you're not careful um so let's go into the basics of programming to reiterate programming is the act of giving instructions to a computer right and these instructions are interpreted in order do one thing then do the next thing and then give something or do something else but it will always happen in sequential order one after the other um there are some caveats to that with Jupiter notebook because you can run these cells out of order from each other but everything inside of those cells will run according to this rule so the um overall philosophy here that we're going to kind of look at is since we're not computer scientists right we will need to borrow ideas whenever it makes sense so if you see an implementation found online if you see something that someone else's uses um feel free to adapt that to your method of doing this right um try to make things as simple as possible if you have a very complex implementation you may need to rethink that so that also includes platform Independence so if you remember earlier I had mentioned that these things can run Jupiter scripts can run on any type of machine that has a web browser make sure that your tools that you generate are the same way um talking about data Justice and accessibility and fairness of data tools can be the same way you want to make sure that those are accessible to everyone so there's a book called Zen of python it's made by Tim Peters he's a very famous developer of some python libraries um and really the key takeaways from this are the readability of your code you want to make sure that you understand what you are doing um so that you can look at it and glance and have a pretty good idea of okay this does this then this does this and so on and so forth um the implementation you want to make sure implementation is easy if you feel like you're talking about an Evidence board trying to explain your implementation of whatever analysis it is that you're doing you might want to rethink it maybe because it might cause a lot of room for error and that will give you a lot of headaches so getting into the technical session of this so syntax again it's the grammar of the programming language right so it's how the computer interprets what you want it to do it's important to know that the computer will always do what you tell it to do what you tell it to do and what you want it to do maybe two different things so thankfully in Python the syntax is regarded as fairly simple compared to a lot of languages there's a lot of things that are done behind the scenes that are implicit that you don't have to type out so um it's kind of important to know that if your syntax isn't right most times your program won't launch at all and I will give you a lot of examples of common errors that can happen with this so the first thing that you'll do in every script is you import libraries so this will be in almost every script that you create this has the syntax of using the import word command and then a space and then you put your library name and I'll give some examples towards the end of this and you'll get to see this in the interactive scripts think of libraries as extra tools that you use to supplement the tools that you currently have in this case python some of the common libraries include scipy numpy pandas some of these are shorthand for other words like numerical Python and really if you think of python as your desk that you work at libraries are the tools that you use at this desk so python makes it easy to work on things but the tools make it even easier to do these things maybe you're trying to make it pretty graph where you want to do some data analysis or management some examples right here would be import numpy import pandas the as suffix to this allows you to call this as a shorthand and you'll get to see this a little bit later in a script so that you don't have to type out pandas every time you want to use a command you can just type PD again you'll see this in the interactive script so we'll be giving to those here pretty soon so variables variables are going to be the um main thing that you'll be working with they're the placeholders of all things that you'll be working with think of them as like containers basically containers or variables will hold numbers names all sorts of things maybe pictures graphs shapes all sorts of things and you basically give them a name and assign them to something an assignment Works in a very special way so um it's important to know too that these variables are volatile meaning that once you end the script the variables are ejected and deleted from memory so unless you save something to a file you don't normally keep those saved so variable assignment Works in One Direction so those of you that have taken algebra may think that maybe I could flip these two things python will not allow that it is always the left will equal the right not the right will equal the left um say for instance you set x equal to Y right so if x is 1 and Y is 2 X will then equal 2 in this case the left will always be replaced by the right after a few times of trying this you'll get a pretty good idea of how this works so um there's some basic data types that a lot there's a lot of data types that exist but they can be thrown into several containers you have numbers simple complex those with decimals those without grouped variables and these can come Set uh like lists sets tuples dictionaries lots of names for them and we'll go into those more in depth um in a little bit strings care characters which are like [Music] um the names that you may interpret these may also mean numbers too so for instance numbers in a string lose their numerical value I will go into that a little bit later and then Boolean values booleans are just true and false true and false yes no one zero on off and if you feel a little lost that's okay we I think we will get a lot of this sorted out with the um interactive examples so we'll start with numbers so for numbers python has three types of numbers the important takeaway of this is that you will most likely be using the first two types of numbers it has floating points integers and complex numbers if you remember in your math class what complex numbers are you may have remembered them being called imaginary numbers it is the two-part Vector that's um like 1 plus 2i you won't be using those very often you will however be using integers and floating Point numbers and really the um key takeaway of that is integer numbers do not have a decimal point floating Point numbers do and that's really going to be the key takeaway from this there used to be a lot of other differences uh back maybe 10 years ago between how large the numbers could be but that's not the case now the key thing to know is that whether or not it has a decimal place so in this example here X and Y are integers their whole numbers integers and the next number this very precise one that I have here this is a floating Point number um and so we will do the interactive example here so um I normally would have you guys go into breakout rooms but I think with the number of people that we have I think we can keep everyone in here um so for the activity if you go in my geohub and find under Activities The Notebook tool um you can find a kernel file that says the ipymb file called numbers if you click on that it will launch um python notebook and I can show you from my side what that will look like and I will work with this with you all slowly on this here's so yeah so I think someone's unmuted here not good okay all right so and Tuesdays section here I'll show you this here you will have this section called activities there's an intro to Python Programming notebook go over to the right here and there's a button that you can click that drops down in that button right there there's a Jupiter notebook called activities if you click one of these it will launch that so in this case we'll be launching the numbers notebook file let me know if you have any questions or if you don't see this and I will slowly see Monday's lectures it should all be published oop you cannot see Tuesday's content okay why don't we do that if you refresh the page will you be able to access it now ah okay okay I removed that so that you shouldn't have to do that but that's uh you may have to click through all of the things inside of Monday's lectures um hopefully you don't have to do that now yeah okay and yours will look a little different from mine you won't see some of these blank items here is everyone able to get the notebooks open I take it that everyone has okay so in this first script here we will be playing with the variables at numbers um I will work through this very slowly but you are able to work with this with me in this so um feel free to work ahead if you would like but you don't need to if you want to stay and like work with me doing this um and if you have a question you're welcome to unmute yourself and ask me that question so we'll start off here so you can see some examples of what are called code comments this is only uh able to do this within the code cell um and then we'll start by creating some names so an example of this right here is this right here is the variable and we are assigning it to the number 10. yes it is the numbers notebook I think it's y b and these will be kind of nice little notebooks for you to come back to if you have like questions that you may need to reference for creating your own code that's why I have them listed this way so that if you need help with numbers again you can come back to numbers so now this number right here if you run this cell here right if you click uh into that and hit shift enter what will happen is you will not have an output from this python if you assign something you do not get an iPad an output from it if you try to show this number on the screen you can do that you'll get an output so if you try to do that just call this variable by typing in the variable and not assigning it to anything so if you noticed I'm doing the exact same name here it needs to be exactly the same so if you spell this differently if you change this to something else it needs to be the same here and then when you run this you'll get the number back everyone on the same page so far cool so now there are some oh need some help what's the do you have a question um how did you get into the uh my Johor so for my geohub if you are signing into this um yeah I already signed into my geohub okay so it should be under your courses then if you have a course that you're so if you go into your dashboard and on the left here there's a section for courses okay um if you click on that you'll probably have one that you're listed as a student for I'm assuming so um I'm the instructor in this one so I will not be listed as a student and then you can click on this section here to get into your section you should have it enrolled um yes and then once you're here you should be able to see Tuesday's content okay all right and then this right here if you open this up with this Arrow you'll have all these um notebooks here that you can launch okay so here I'll go ahead and do it through the my Geo Hub one actually so it takes a little bit to launch since my geohub is actually the one that's launching this yes um do you have a question the Heat if you have a question you're welcome to type it out in the chat or if you want you can unmute yourself for that Okay so yeah so again we'll just kind of go through that real quick if you run this script here right you can get the number from it right and if you try to call that back on the screen type it this is a number and make sure that you have these underscores here and I'll show you why here in a second then you get the number 10 back so now you have to remember that python does not interpret phrases the same way that we do as people so python does not know what to do with spaces so say for instance you run this script right here python will throw an error and we'll say invalid syntax um python does not know where to assign this number 10 does it go to number does it go to a does it go to is or this and there's some other issues that come up too certain words cannot be used as variable names if you notice in your python uh notebook the word is is actually green and not black this means it's a reserved word and it's used for special functions there's a lot of words that are like that a really good rule of thumb is if it's not black a lot of times it has a special function that you need to understand um so like an example of this would be if you did the Ampersand and said like hello this is totally different you can't use special characters when you're naming your variables um so and yeah it gives you some examples here you're free to look at those um but we'll go past that we'll go to variable assignments and multiple assignments now so like I said earlier variable assignment only works in One Direction so if you try to assign 10 to this is a number algebraically this would make sense however python reads left to right so you can't change the number 10 to something it will always be the number 10. um that's important to know when you're creating your variable assignments or you're assigning things to each other so in this example right here trying to create two variables you can give them whatever names I give you examples and then assign them to each other and then call back both variables and see what happens so I will work through this somewhat slowly and then we'll kind of circle back and see how you guys are doing and if you don't if you just press enter without pressing shift it will create a new line and you can have as many lines as you need to between stuff if it helps you organize and you can place spaces between things you just can't have spaces between variable names that's all okay so this is what I have here so first we're creating a making it one we're creating B making that two and then What's Happening Here is I'm saying B should be equal to a so when I run that I don't get any output from it so we'll look at both variables here so normally if I just done the beginning section it should be one and two that I get back we can call back both of these by calling each one in succession with a comma between them so you would do a comma B and then if you run this cell then it gives you both outputs back in the order that you asked for it so this is a and this is B and y'all are able to see my screen fairly easily I assume right numbers dot IP Y and B does not load this page oh is this is this script not loading for anyone else oh that's good to know oh it is loading okay have you real quick um when you have this open here okay it's loaded okay if you if you're clicking Jupiter notebook activities it will probably bring you into this uh well not this page here but here I'll show you it'll bring you into the file explorer okay okay yeah if you so real quick if you end up on this page here and you're very confused as to what's happening go back you may have clicked on the actual jupyter tool itself that launches it into that file explorer I was talking about earlier um if you click on the scripts it should launch the script let me know if it doesn't or if you have an issue with it um okay so now that we have a and b we notice that a is equal to one and so is B so we changed what B was by setting it equal to a um you can do this through a lot more complex functions we won't really show those if you've used like a TI calculator you'll know a lot of the rules and like conventions that will come from this um one thing that you can do to clean up your code is if you noticed earlier if we can use commas to separate things um commas um commas you are able to separate variables and you can assign them in multiple Fashions on the same line so an example of this here would be variable one variable two and variable three so if you notice variable one will get assigned to 10 and I can add spaces here to help you see that variable 2 gets assigned to 55 variable 3 gets assigned to 2.55 um and so on right so you can call these back just like you did earlier and then you get your variable outputs and the order that you asked for it and this is important because certain things for data science commands that you do you you will get more than one variable back so an example of this may be you ask for the coordinates inside of arcgis for um some sort of geographical data you will get a latitude and a longitude and that gives it to you as a group so the final lesson on this I talked about earlier with number types you have different types here I'm only going to show integers and floating points what's important to know is that python will dynamically change those one will go into the other automatically but the other does not automatically go into the other if that makes sense so what I mean by this is that integers are the simpler type meaning that they don't have a decimal place so when you create it an integer it has no decimal place but a floating Point does so if you look at the types for this you have the integer type and the floating type and what's interesting to note about this is that an integer can become a floating Point very easily natively in Python it just adds a bunch of zeros to the end with a decimal at the end but going the other direction python doesn't know if it needs to round up or down if it needs to just remove everything past the decimal point so a lot of times you have to decide what you're doing there so if I flip everything now you see that the integer is now a floating point and the floating point is now an integer a lot of these things that you learned you will not need to really remember these these are just important so that it's in the back of your head when you're using functions because some functions request an integer some request a float and if you get these errors and you don't know what's going on it's because it specifically needs that type of number and the easy fixes to change that so um and I think that's the end of this here so that's the end of just the numbers portion of this so like I said earlier we will terminate this session by clicking this button right here it will leave the page and then it'll take you back to your dashboard and then you should be able to go back to my geohub if you need to so we'll talk about the next data type here so oops so we have grouped variables so if you remember when we assigned those variables you could use um commas to create groups a little bit easier right um if you group those with parentheses or some sort of brackets you can create a more unique group that can all sit inside of a single variable this would be similar to like something like Microsoft Excel so like a table or a matrix [Music] they all have lots of names the one that you'll be using a lot is called a list and a list is just a as it sounds an ordered number of things could be numbers names coordinates whatever pictures could be anything um there are lots of other um uh like data types for grouped variables that exist I will briefly go over these but the one that you will be using the most is lists and you will use later a more advanced form of dictionaries and lists called Data frames so um for group variables there are groups and then within those you have what are called tuples lists sets and dictionaries um for the most part these are all going to do very very similar things they all just have minor differences so for instance the difference between a tuple and a list is that a tuple is unchangeable or unmutable or in immutable and ordered meaning that the first item that you assign is the first item that is in that list and the order matters if you re-changed the order the list changes these are denoted with soft parentheses or a parentheses or soft brackets an immutable means that if you want to change the Tuple you have to re-change that entire group again however with the list they are mutable meaning that you can change just a single thing inside of that without having to recall everything that you need to re-add to that list if that makes sense and let me see if I can leave that up and I'll kind of pause here if you have quick questions about this um and then you have sets sets are think of it simply as a bag of marbles nothing is um ordered in it you can't figure out what the order is inside of a bag of marbles and if side of that bag of marbles you can only have one color of each marble um sets can only have one occurrence in that list meaning that if you were to create a set with the number two twice in it it will only have one two in it so these are important for if you're filtering uh things out inside of your data you use these as like a set to filter out things that you need or if you need to tag things stuff like that um and dictionaries are last and I'll kind of go over these here in a bit oops let me uh fix my yeah okay um dictionaries are unique in that they are like a list of lists um the only thing that's unique about them is they have what are called keys so instead of calling the first or second thing in that list you can say I want column one and then I want um the the first item and those columns or rows whatever you want to call them can be called anything so you could call it I want the first name for instance or I want the second age right and you can call them whatever you want you can have as many of these as you want so if you heard earlier I talked about an index and that's how you like call certain items from within that variable so say you want just one number from that list you need to know where in that list it is um computers are very unique and that they uh start counting from zero they don't count from one so in this example right here um let me get out my laser pointer in this example we have a set of words so this is uh a list of letters and numbers right that spells out the word justice um but the very first thing here is item zero and then it goes to one two three four and then all the way up to eight even though there are nine items here so this is because the zeroth item is the first item for us and that's just because the way that we Count versus the way that the computer counts um so if you were to call this you would use hard brackets after the list to um call the number for that so we'll open up the matrices interactive example and you'll get a much better example of like how these work so let me open that up with y'all so matrices let's terminate that session I forgot to do that so I will open that with you guys okay so I will work with this uh with y'all and if you would like to try it with me you're welcome to give variables different names you don't have to follow the same naming convention that I do um the reason I give variables those names is it is easier for you to follow and understand what I'm doing so let's try this with a tuple first so I'm going to be creating a tuple so I can just call it a and then equals uh open parentheses so if you notice Jupiter creates the open and end parentheses so you just need to type out the values that you need and then you will separate them out with the commas just like you would with the grouped um uh group variable assignment so in this case it'll be one comma two three and four and if you call back this in the same section you get everything inside of that Tuple if you want um just a single thing from that Tuple and feel free by the way if you have issues in chat uh go ahead and post it let me know I can see the chat in another window so um if you want to call back just a certain thing from that tooth pull you would use those hard brackets that I mentioned and that's going to sit right next to the variable so if I wanted the very first thing and that I would call item 0. that would give me one here if I called item number one which is the second item I would get then number two which is the second thing in that list hopefully that makes sense to everyone now earlier I had mentioned tuples are immutable so you can also use this to try and change a certain item within that list so say I want to change the first item and I want to make that zero this time I get an error now why is that that's because of the immutability that tuples have so um really what this means is that if you have a tuple they're optimized for Speed they're not that much faster than lists so there's not really any reason to generally use these I just want you to understand what they are and how they work because they can be used in a lot of functions and if you don't understand what the difference between a tuple and a list is it may cause you some grief so um tuples are good for if you have a group of variables that will not change and you don't need to change it um make it just because of the speed and the way that they operate and work um so now let's try it with a list let's do all the same things but with a list this time you can use the same name it will change the variable type just like python would do so now it's a list we call it back you get a list and the reason that I know that this is a list is not only because I named it using the list conventions it's because it gives me these hard brackets back so you can tell that it tells you what it is so soft brackets or parentheses means it's a tuple or just a pair um sometimes is what it can be called um or a list which is the hard brackets here so if you try calling something back it works the exact same way get one but because these are mutable if I change the first one to be zero I don't get an error so now if I call this back if I call back the list if you notice now the first one is no longer number one it is zero now um and this is going to be a lot of um you'll be doing a lot of this like in your data science most likely um there are more advanced functions for this that we'll go over that's part of the pandis library that'll be towards the end of this lecture there's two others here so there's sets same thing we can create a set by using the set function the reason you don't use curly braces will be shown right after this actually so four oh whoops uh sets I apologize for that sets you need to give them a list so I uh this was a syntax error that I forgot actually so you have to give a set a list inside of it and then it converts that to a set so now if you try to call that set through an index it gives you an error and the reason for this is because there is now no more order in this you have no idea what the order is um you just know that something is in that set uh so let's see here whoops turn off my camera for a second there um so for mutability um you don't change them the same way you can try assigning it through an index but that won't work so if I do a 0 equal to zero it doesn't know what to replace it doesn't even know how to assign that it doesn't know what to work however if I do a DOT add and then I add the number that I want to add in this case five and if I call it back now five is a part of that list note that if I were to change this to 1 nothing changes on this because one can only be in here twice now that it's already in here or in here once now that it's already in here I can run this as many times as I want and it will never change that because I can't uh a set can only have that happen once so dictionaries are going to be the last one this is going to be kind of like a baby version of a data frame you may have heard of data frames through like maybe a python video or something like that um dictionaries in this case are done using hard bracket or uh not hard brackets um curly braces and what it is basically here is to make this a little bit easier to read you have a dictionary that I'm creating and that is equal to Open brackets then it's the first key so the key is the label for the first list and then in that list I have names comma then the next key a colon so in the colon separates the identifier and the list and then you have another list for that and then what happens is this gives you a way to uniquely call values without having to use strictly numbers and what I mean by this is say for instance I have a dictionary and say I want to know all the first names that come up in that it will return a list of all the first names so now I have a list of all the first names say I uh go even further um and I want all the first names but instead of all of them maybe I just want the first one so it will give my name in this case um if you call a dictionary without a key or if you try to do this out of order so say for instance you do this and do zero it will not know what to do because neither of these right here are zero right so it doesn't know what to do so technically speaking if I change this to be zero should work uh oops so that would be number equals zero um that's pretty much it for the matrices for this there's a lot more stuff that you can do with these and towards the end of this lecture I'll go into the easier to use function types like data frames um so I will terminate this session leave that leave that open then we will continue on to our our point so the next variable type are characters and strings and characters are simply put uh the buttons you see on your keyboard they're numbers letters special characters anything could be considered a character characters have a different numerical value than what's associated with like the the number basically so they have their own number that's associated on the keyboard these are called the ASCII values what's important to note about this is that say for instance you read some data online and your program interprets the numbers as strings and it tries to perform operations on those you will not get the data values that you expect from it because strings work differently on that um what I mean by strings is characters that are strung together to create these strings so these are basically just matrices or lists of characters so what you saw earlier when I had those names inside of those quotes those are um just unique types of matrices are lists that have characters in them and what's important to know is that strings you can't change them in place without special functions so you can't just assign the second term in this um so some examples of this here you can use single or double quotes we will be using double quotes for all of this so This example that's shown on the right here where it says my string oops I'm not wanting the pen I want the laser pointer this right here this is what will be primarily using for this so and I'll show you some examples of this here so we have another example we can go back to your breakout activity um and we will load up strings and this will be the second the last um portion of this and then I'll kind of have a section for questions later towards the end of this lecture here um so for Strings we have lists of characters um the same modification techniques can be applied to these so let me uh close out my PowerPoint and if you have questions feel free to ask so first thing try creating your own name inside of this so I'm going to let you all try and do this first on your own and I will in the next few minutes here I will join in with you I want to see how you all do on your own and let me know if you have questions or issues and if I'm going too fast let me know and I'm happy to slow down and kind of reiterate some more Concepts I'll just leave it on this for now until y'all are so I'll give y'all a couple minutes to work on this um then I believe we are coming up to our break soon yeah it will be at 10 30 so probably after this exercise I'm gonna couple uh cover maybe a couple more things um and then we'll take our break and then we will continue with the lecture so where can we use drinks so let me load up this here so um what do you mean like where can like um like where is it applicable like what like why why are we learning it I guess or do you mean yeah so it's application so okay yeah no that's a good question so strings um this kind of depends on the context of what you're doing so um the reason I bring up strings is several reasons one certain types of stream data may come as a stream um an excellent example of this is say you have a sensor that has GPS data say maybe you're doing some field research and you're using a GPS sensor um data from a GPS device usually comes as a string that you have to interpret and separate um you probably won't be using this that much I think most data scientists unless you're using like text mining will not be using strings that much however you may use text mining maybe you are analyzing contracts for Energy Research or uh for water research or something like that um yeah so that's why another thing too is if you have inside of uh like a like an array or a table and you read uh data from a file um the computer's not always smart enough to interpret that um something is a number and it may interpret it as a string and it's important to note that strings lose their numerical value when they are strings the computer can change that but if you are having issues trying to compare for instance two strings python doesn't know what to do with that like it would um two numbers so and this one's pretty short um this that's that's why this one's pretty short is there's not as many applications maybe for like the data science that you'll be doing um I just show a few examples here because you might for instance have stream data that you may need to split um or if you need to query a database and you need to grab that data back and there's no programming interface for it this is the method that a lot of programming interfaces or apis use um it can be used for extracting numbers or text yeah So like um I show the in the later example there's an example here where I convert a string uh back into a number so say you have a string with the number 500 in quotes right um You can convert that back to the number 500 so that you can use it as a number um but this is a lot of this string modification string uh changing and stuff like that is a lot of ways that application programming interfaces apis uh are developed for how they query databases and I think you'll go over this more later I think in tomorrow's session with querying databases but you usually have to send some sort of request and you have to interpret that back and when you interpret that back um you need to know how do I split this number up that's coming back to me because unfortunately a database when you request information from it may not always send it to you in a format that's just all easy to grab numbers that python knows what to do with so sometimes you have to do a little leg work on separating it and so on um so like an example of this here so I have a sentence here that I'm splitting but say for instance uh we'll call this data right so we'll have data here and say it's maybe temperature um and it's got a comma maybe it's humidity and then maybe it's like you know some sort of latitude uh and then longitude um I don't judge my latitude longitude that it's giving here this is probably not correct but um so say maybe that's the data that comes in from a database right um that's so for hard brackets and why we use that for indexes is just Python's rules um I know that's probably not a satisfying answer um but that is how python interprets that it's always going to be a hard bracket um and that's going to be the same regardless of um whatever type of list or string or whatever it is that you're using so say you have data that comes in right and say we want that data to be split up into something right so if I say split this so set it equal to itself right and I'm splitting it but when I need it to split by is if you notice I put these commas here so I wanted to split every time there's a comma and I want that to make a list out of it so if you do that and then if I get data again now I have a list of these numbers and if I want to grab the first thing in this list then I would just say zero and then it would be 24. so this one comes up as a string I'll show a little bit later in this some of the like built-in functions you can change a string using What's called the um I think just int command I I'd have to look again what I had written and it will python will attempt to convert um that number so and there's tons of other things that you can use yeah yeah you can and I'll show some examples of like what happens after that so say you have a file that Imports right and um it is not interpreting it correctly um you can apply that split to those pieces of data if you need to um I so very briefly um kind of as we're coming up to the break here I think this will be a good place to stop um and I'll just kind of answer some questions before we take our break um has anyone seen like what a DOT CSV file is I presume most of you know what Excel files are right unlike how Excel spreadsheets work so with um what are called CSV files they're kind of like a more rudimentary version of um Excel files they use commas to separate their data out right so CSV stands for comma separated value and [Music] you normally python is pretty smart at interpreting that when we use the pandas Library later pandas is able to interpret those commas pretty accurately and a lot of times it can almost automatically detect the variable types that are in this so for the most part these tools that are here will not be needed if you're just analyzing data but you might need to know this if you are creating your own tool and you need to understand what's happening behind the hood of like what's going on there so like pandas for instance when you create a data frame from a from a CSV file what it does is it looks at the first row and it does exactly what's Happening Here and what it actually does is it goes a step further and it converts these into their respective numbers so in this case this would be an INT an integer an integer and these would be floating Point values nothing more than that so I'll show that example a little bit later as we get closer um and yeah so to Circle back real quick again on why we use the like the hard brackets versus the soft brackets um it again it just comes down to how python interprets that so um soft brackets are used for um exclusively for calling functions so if you noticed earlier I had that thing where we did the set and bracket or uh parentheses right so I will explain functions later but parentheses are used for functions and doing tasks hard brackets are used for indexing and costlink variables so San say we'll give you an example here of what will happen if you use the soft bracket so if I have a list and I say it's one two three four right and if I try to call that back with a uh zero what will happen is is it will say that name a is not defined a is obvious or not a I'm sorry whoopsie a is definitely not defined yes so list is not callable callable means it's not a function it doesn't do commands um python interprets soft brackets as you have some sort of command and you're giving it inputs inside of this hard brackets interpreted as I need something out of this does that make sense and that'll I'll um kind of show that um hear a little bit later so we'll talk about functions and all that um there's a lot of things to cover for python so um I kind of want to make sure everyone's up to speed with where we're at does everyone feel fairly comfortable I know it's a bit overwhelming there is a lot to learn for this and believe me no question is too small for this so yeah sure sure sure so say I have a sentence right and so say I have a sentence and I set that equal to hello and welcome to data science right so if I call that back that creates just a single string for this right if I split this so to do that you can't just type split and then do that right so this is an example of a function right here um I'm not calling anything out of this it is a function that has no inputs right now you set it equal to itself but split and if you don't give it any sort of um separator sometimes it's called a delimiter but it's the separator so in this one right here up here I used the comma but you cannot specify one and what python will do is if you don't specify one it will split it at every space so say I do that and then I call that sentence now I get all the words from that sentence say I want to call a name or a word in that sentence so if I want to call the third word in this I will call item two and then I will get welcome now to take that example a little bit further say these are types of data that come in maybe separated by spaces and maybe you need a certain character from this and it corresponds to something using the sentence example what if I needed just a letter from this so say if I'm in welcome say I want the first e of that letter I can call this again to go within that list right so now with welcome I would call Item one and that will give me the letter e so in this it will be the third thing item two and then within that it will be item or item three and then item two within the third item um and this concept is called nesting um I will explain that later that's kind of a crucial concept if you want to create anything that's like fairly complex so does that make sense cool cool so real quick before we go to the break I'll kind of show another example here of like what may happen um GPS stream data so say you have like GPS stream coming from a sensor this is not always usually what comes from like a lot of data science sources this is like if you're doing your own research and you have your own tools that you've developed and you want to be on the Forefront of like you know something like that right um say you have a bunch of GPS stream data that comes in it has a header so it's got some things that come in maybe a hashtag and then it has you know uh coordinates right and then it has another hashtag and then uh more coordinates again #and then it has like some sort of universal time code or something like that right an example of separating this would be if you were to do uh data list so you don't have to set it equal to itself data list can be equal to GB uh GPS stream dot split get back the data oh whoops I forgot to call the uh separator so when you call it back sometimes it may use a different character that's not a comma or a space you can use anything for that so in this case it's separated by hashtags you know that's just one example of it I don't think GPS stream data actually uses that but it does use unique separators like that so that's just one example um for searching stuff online you will use stuff like this a lot like if you're building your own um application programming interface for a database so this is very important for building and deconstructing search queries and the results from those queries so um I know it doesn't normally seem like something that you would traditionally learn in data science but um it's surprisingly uh relevant any other questions before we head to break that's a good question um so you can if you want so I'd say for instance I want to split this again here you can put the space in there and it will still work um oh whoops uh sorry yeah so you can put the space in there and it will still work um what python does is if you want spaces if you don't put the empty quote strings it assumes it will be an empty white space does that make sense so no you don't have to put that in there to answer your question no you don't have to you can but you don't need to cool okay I think it is about time for the break so if you remember the last thing that we were working on was the uh interactive example for uh strings we were modifying strings and modifying characters and stuff like that um the next thing that we will learn is modifiers or not operators um if you've used a TI calculator then you should understand kind of the basics of like these operators that will happen here and these are just methods of manipulating the data you may have seen some of the examples that I've already shown in this I can show examples of these on screen for you but I don't have an interactive example because there's some other stuff that I want to show first um so you have your standard operators like adding subtracting multiplication division um doing stuff like exponentials and certain types of division um will be done a little bit differently so I assume that probably judging on the fact that I think most of y'all are undergrad but some of y'all might be graduate students you probably took a math class over covid and you probably had to do some math class homework online normally when you do those you would have to enter in like an exponential like a one to the power of something using a carrot you don't do that in Python it's a little bit different there are different rules for that so for instance doing an exponentially uses a double asterisk that means that in this case it would be 3 to the power of four and that would give you 81. um integer division is um essentially if you round down or cut off the um uh decimal portion of the division so no remainder so for instance 3 divided by 4 is less than one it will always round down to zero um modulus and mod is kind of an interesting way to get the remainder of something so if you want something an example of using this would be if you want something to run every third iteration and you're going through a loop which I will explain later that's another good way to do that um and the rest of them work fairly pretty much the way that you would expect it and it works exactly the way that you see it typed here you can type it without assigning it to something and you will just get the number back um but you can also assign it to a variable and you can also insert variables in place of these numbers here um some of these things are different between programming languages but for the most part all of these are pretty much the same and that's what I was talking about with like the use of the carrot what's important to know is that order of operations applies here and if you are unsure or if you think that python does something differently than what you're used to for typical order of operations for math use parentheses you can use soft parentheses inside of your calculations um so like soft brackets or parentheses to denote that you want something to be done first before it does something else just like you would on a calculator so if you used a TI calculator or even like just a a scientific calculator you probably know what I'm talking about same rules apply in Python for that so when it comes to operators it's uh pretty similar to the same way that you would use a calculator with some minor syntax differences so um the next thing that we'll look at is booleans and conditionals so conditionals are your decisions that will happen inside of your um script excuse me sorry booleans are um variables that just have two states they either are true or they are false this can also be decided as like it's on or off this light bulb here is a fantastic example there's no in between it's either it's on it's something or it's nothing off right Um this can be depicted in several ways there's a lot of ways that python can interpret pool booleans so for instance a zero and a one can also be interpreted as true and false true being one false being zero think of it as there's either something there or there is nothing there um and these are very important because this is kind of the core of your decision processes that you will create for your tools for um like your programming um and like it's like the like the very core of this and the way that you do these um is so you can assign a direct variable and just like a number there is a literal true and false value that these are reserved for just true and false values right um let me bring up my laser pointer here actually uh whoops okay that's not helpful oops I apologize okay well that's okay so if you assign it to that then you can change it depending on what happens right so there are other ways to measure the Boolean values that occur in this so an example of this is if you use what's called a conditional statement conditional statements are just simply a way to initiate a decision that happens within the code so uh here let me keep that open um and you initiate these so you start here right and then after you start you um see if I have the laser pointer on that I do not um you check to see is something true and this can be a variety of things it could be a Boolean value but it could also be a comparison is this variable less than five is it greater than 10 something like that is this name equal to this um there's lots of ways that you can do this so when you check this you have two options it's either true or it's false if it's true it does something and then it ends and then you continue on with your code if it's false it does a different thing that is separate from the first thing a lot of times this may mean it's just not doing anything it does nothing so maybe it's is it true it does something if it's not true it doesn't do anything um and these are done what's called using an if statement and the code that you run if it's true needs to be tabbed over so this is what python kind of like to focus on with its um emphasis on indentation so instead of having to explicitly contain that with like special characters you just indent over the code under the if statement as shown here right so this is a good example here this right here is the conditional statement if x is greater than 3 and you see that earlier in this example I am setting x equal to four so that you know yes that is true X is greater than 3. when that prints that will say x is larger than 3. when I run this this code right here will run and you can see the output that I get is exactly what I would expect does everyone feel like they're on the same page so far we'll have some interactive examples for this no questions okay um Okay so conditional statements can have more than one condition right so you can have an is an if or an else if or an elsif and basically what this means is that you can check multiple things in sequence inside of the same decision um and it's important to note that these decisions are checked sequentially so remember I mentioned the code looks at this from top to bottom left to right the first thing that's true will run the code that's true and then it will skip every other condition and exit the conditional statement so on this example here on the right if I have X is greater X is equal to 5 right I switch accidentally flipped these right here so you'll have to ignore that but it is greater than four it is also greater than three but it runs the greater than four code because it's the first one that comes up so when that's the first one that comes up here it skips these next two uh things that happen here so say for instance if I set this to x equals four it would skip the first one and run the second one if I set x equal to zero it would skip the first two and do what's called the else statement the else statement is your catch-all that if you still wanted to do something but not have a specified condition that is met so say you have two conditions like I do here and what if it doesn't meet those right what if you have something that's outside of that well you can use an else statement to catch that so say for instance it's okay well I don't know if it's bigger than three or four okay well I'm not sure then so we'll look at some examples here and I've kind of highlighted these so that you can kind of understand the different terms for this and this is stuff that you will be using a lot more often um when I talk about indentation um code that is below an if statement has to be indented until it is done um and between an if and an else statement you can't have anything that's not indented so if you want for instance to set a Boolean value to false in this case it would be zero it checks to C Is it true obviously it's not so it will go to the next um else statement here it does this item right here and then it exits now notice that I say that Boolean is equal to one after that's just something I wanted to set but because this happens after the if statement it will never do this is that pretty clear so far yes so the difference between an if and an l-sit or an e-lift and an uh else statement um an e-lift statement has another condition it's like if you were to say if and then if again there is a difference between saying if and if again though then saying if and else if so an example of this here I'm gonna take my pen here all of this right here is all one statement that it checks it checks is it greater than two okay we don't know is it greater than 4 is it greater than six and if it's none of those the else statement does not have a condition so you don't have to you don't specify something with it so if it's not less than two less than 4 or less than six then the else statement will run um so the difference between elif and else is else does not have a condition that it needs to meet it's the no conditions are meant um e-lifts are basically if within that same statement you want one of those things to happen depending on the conditions you would say if greater or if less than two if less than four if less than six does that make sense okay cool yeah and uh we'll have some I think some interactive examples and I can show some examples of how it works here so um watching the code like be typed and run and see how it works um I think kind of helps with that so um so we'll talk about another important part of python Loops so say you have something that you want to do to a number or something that you want to do to a list that means that you have to do something over and over and over and over um and does that mean that you should type that same command over and over with a zero and then with a one and then a two and a three no um that would be very tedious and would take an extremely long amount of time to do that um programs give you the functionality to be able to call back the same command over and over a set number of times or over a list and what I mean by this is so say for instance you wanted to do something 10 times right you can use a loop that says I want you to run this code that's indented below me 10 times or you can say I want you to run this until the output is greater than 10. there's two different ways to do that and that's essentially what the difference is between a while and for Loop a for Loop when you call or start the loop it will have its exit condition pre uh predefined meaning that if you say I want a for Loop that runs four ten times so for a number within the range of 10 it will always run 10 times regardless of what's happening in that Loop a while loop however just checks for a true false condition and that's it so it's like a a conditional statement that is also a loop um so Loops have three parts to it um they have their start which is the call and this is usually where you type like while something or for something or something like that then you have the body this is what's indented over and this is the code that you want to actually run and then you have the exit condition and the exit condition for this means how does that Loop know when to stop so for Loops like I mentioned they are called for Loops um usually iterate over something like a list so say you have a list of numbers it will go through each number and once it reaches the end of that list the loop is done it's cut it can also go over just a set number of times depending on how you program it the while loop is a little bit different on that that can change dynamically within Loop so maybe uh this next set of examples here will give a kind of a good idea on this so the while loop here on the right will run until I is uh at least 100 or greater so what's happening right now is that I is slowly increasing so this plus equals one is another unique modifier for operators if you just want to slowly count up with one each time you use plus equals minus equals also works for subtracting one this is great for counters or lengths and stuff like that so what happens is in this Loop here you start at zero right and then the loop is called and then once you have the loop it goes through and does this a bunch of times in fact it does this exactly 100 uh and one time I know it goes yeah it does it 101 times um and the reason for this and the reason I wanted to show this is sometimes this is a common thing that you will run into when you create your own Loops you sometimes will not understand like hey why am I getting 101 and why am I getting 100 um it's this if statement right here and this plus one plus so sometimes you need a plus one two or a minus one to help you iterate through like a list um and I'll show that the for Loop here um just keep an eye on that when you're doing that I just wanted to show that as an example but this iterates 100 times and then the reason it takes a hundred times is it's adding one to I and then after it adds a hundred to it what happens then is now I this condition right here becomes false right I have to excuse my handwriting here that becomes false and then it exits does that make sense probably make it more confusing I think but um if you have a question post it up in chat I'll come back to it at the end of the slide here but so for for Loops they're a little bit different so for for Loops you say four something and something and usually what this means is um you define how long that Loop is going to run so if you were to recreate the top one you would just say for I in range of 100 and then set X plus equals one and that counts up x 100 times and that does the same thing um for for Loops however uh the other thing that you can do is you can iterate over a list so for instance in stuff this list that I've generated here it's going to keep setting this variable X to whatever is inside of stuff so at first it starts at one and then it starts at 2 then it starts at three and you'll see this in the interactive example and it does this all the way until it reaches nine now the reason that nine is the output for this is once this reaches the end of the list the last thing that X is set to is nine because that's the last thing in this list here and that's why you get that when you print that number out the print command is just a simple way by the way to like print a number to a screen um Jupiter is nice and that you can just type the variable name and it will give you that number back thank you so let's turn that off so we'll go to the next page here and we'll talk about what's called nesting um decisions loops and lists can be put inside of one of another um decisions and Loops can be cross crossed between each other so you can put decisions within loops loops within decisions an example of this is right here on the right so say for instance um you have a word called stuff or a stuffed string called hello right and that hello string has a bunch of different letters in it maybe you want to look at every single letter at that and if the letter right so that's looking at every single letter right for I and stuff because this is considered a list of characters if that letter so in this case this is the letters that it will be iterating through here um if that letter is equal to l um then it prints out the letter and when you set something equal you have to say a single equals sign if you are comparing if something is equal you use a double equal sign and that is just so that python knows if you're asking or telling um and so let's see here let's go so this is the reason it's called nesting is because this decision sits within the loop um or it can sit within another um decision and basically what happens is the only way that you can get to action too is through action one and then you can get to action two um be it a loop or whatever um you cannot put loops and decisions within lists that's just it just doesn't work that way but you can put lists within other lists that is an excellent example of that is what a table is so like Microsoft Excel CSV files is a list of lists so like for instance every row is a list of columns so when you give a list of lists like this over here an X and Y value just like you would in Excel like row and column then you can get out what you need from this so this right here is zero zero one two one two so if you were to call for instance in this case one one you'd get brown as your return um does that make sense we'll go over this in um interactive examples too so okay I think everyone's good so um and I'll have time at the end for questions examples whatever you all want to see at the end just let me know so remember earlier I think someone had asked about why we're using hard brackets for our indexes and not soft brackets that is because functions save the space for those soft brackets functions are essentially shortcuts in the code for complex tasks so an example that I have on the right here is say I want to do a bunch of complicated stuff in this case it's very simple for simplicity's sake say I want to take in this variable I want to take itself and add three to it and then return this variable back to the person this function right here requires an input and that input is um contained within soft parentheses so for instance if I were to run this function that I defined which is defined with the def um it adds three to five and then I get a returned output of 8. um there are tons of functions within python you can custom Define your own functions but a lot of the ones that you'll be using will have those soft parentheses and a lot of times they may not have an input so for instance I could have a function that just prints out words and doesn't require any input and that's why you have empty parentheses so like the split function for instance if you don't give it any inputs it automatically assumes you want a space um I won't go real in depth on this there's a lot more that you can learn about functions and kind of their superseding part classes I will not be able to go into that that's a much more complex topic than I think I have the time for but they are a very interesting part that will allow you to really clean up your code so an example of this is say for instance you have this complicated set of programming instructions that you want in several parts of your code to happen at different times maybe it's within different if statements instead of typing it over and over you define it as a function and then you just call right or start the function within those sections that you want it to run so I'll talk about some errors and then we'll kind of get into like more of the fun stuff here so errors that you can encounter as a programmer there's syntax errors these are pretty straightforward you typed something wrong and it doesn't run most times this just means you forgot some sort of character like a colon or you have too many spaces one that's an issue with python because it uses indentations um python wants to make sure that you use proper tab spacing and not like space indentation so don't put like five or six spaces to try and indent your code over it does not like that um logic um is another one so this is the program runs correctly but it does not run or the program runs but it does not run correctly so this is kind of a reiteration on what I was talking about earlier if you give it a set of instructions and the computer correctly interprets those it will run the set of instructions that you gave it now whether or not what you want the computer to do and what you told it to do are two different things that's a different story this is what logic errors are so an example of this is maybe you put a Plus instead of a minus and it's counting up instead of down or it's adding this instead of subtracting it or and a lot of times a greater than equal than sign and maybe you forget which one I'm supposed to use or or maybe you have to kind of think about the logic or something like that and the last one is a runtime error these are a little harder to track down this is a combination of usually syntax and or logic errors but these usually occur because uh and what makes easy unique is that they will crash the program usually um but not on start so maybe it's after it runs some code so it will compile run for a second and then crash um an example of this is trying to access something that doesn't exist uh yes yes it does letter case can cause errors so what's unique about letter case is so like for functions for instance this is case sensitive if I were to add like so if I change up here at the top so like uh if this right here was a capital a this would need to be a capital A as well if I did not use a capital A it would then this would not run it would just crash like it wouldn't even launch um case sensitivity is also important for your variables too so if you name a variable you need to call it the exact same way that you named it including the like upper lower case letters it's it's it's the computers are very literal in that sense that um uh it needs to be like explicitly stated um because you can have a variable that is different with lowercase letters and then one with uppercase letters um and there's a lot of other um caveats to that so um yeah so that's really it for the errors there so we'll talk about like some like kind of fun examples here of like libraries that you'll be using um and then later on throughout today um you will get to have some like real life examples of using like databases to download data from like um the uh United States Geological Survey or through like um Energy building simulations and and stuff like that so um so there are some special libraries and functions that you can get the king of this is pandas pandas is a library that deals with manipulating data so what pandas does uniquely is that it takes the list um type that we learned about and the dictionary type and combines them all together to make this really cool unique class that um has a lot of built-in functions for cleaning up its own data it also has the ability to save to files natively like you don't need to have special functions you just tell it like hey save to file read to file give it the file name and that's it it's it's very simple um Candice has two data types A pandas series and a pandas data frame uh really the only difference that you need to know between these is that a data frame is a series with more than one column that's it oops I didn't mean to skip that um and then I give an example here of importing what like what the library looks like so the library here is pandas and when I use the as that's shorthanding this so that you don't have to call pandas every time you want to use a function from it so you'll see this in the examples here coming up um but an example of this here um would be say you have dirty data that has a bunch of erroneous values or bad values that are in it pandas has a built-in function to be able to clean up some of those values and remove them um pandas has a built-in function to be able to plot its own data so that you can visually see it just like quickly at a glance just like that um pandas also lets you do a lot of data manipulation by looking at the end of a data frame adding stuff to it easily and managing it very easily so this will be kind of like your home for this this is what like almost every data scientist uses um it's even cross-platform I think between outside of python um and so for pandas it's derived from numpy so which is short for numerical python numerical python basically is this library that adds the abilities to have fast Matrix or arrays they call them arrays and a numpy the ability to like store data in big tables and be able to manipulate them in really fast ways so an example of this is say you have a lot of like geological data right um or energy usage data across a bunch of buildings and you have a really large data array um it has short tricks that it uses to be able to manipulate that math if say you need to transpose it say you need to multiply it you need to do element wise operations um this is where a lot of performance improvements come into play um it's also great for generating arrays with just simple numbers in it since python you would normally have to Loop through and create a list this is great for creating a graphs graphs and such like that so if say you need an x-axis that goes from one to ten you create an NPA array that goes from one to ten easy and then this shows like an example of this there's another shorthand you can use for this um the shorthand can be whatever you want it to be but it's pretty standard to use the ones that I've given here because there's a lot of examples that use that shorthand another thing that numpy works really well is you can easily Implement math formulas with it so if you're struggling with the built-in python um uh like operators you can have your own functions from numpy taken place and it just flows more naturally and you use actual function names to say like some average you know stuff like that and numpy's performance for this gives you the ability to do this on really large data sets without bogging down your computer a lot um and we'll we'll use these later you'll see a lot of this reference later um I just want to give you all kind of like a brief like breather on that so um so a lot of things um computer scientists anyone that does any sort of programming it's very hard to um it's very hard to learn everything at once especially through classes you will always have to be learning new tools yeah yeah I'll show you yeah they're very it's very easy to add and use these libraries when you're in your notebook and I'll show you that um and that we'll we'll do that here in the next example that'll be coming up here in a second um many of these languages have large online communities where you can find tons of resources on this um I unfortunately will not be able to go really in depth on a lot of these resources so I will be giving you enough to be hopefully interested and hopefully a little dangerous with this um but if you want to look online to see like Hey how do I do this a little bit better I saw you know we talked about strings a little bit maybe I wanted a little learn a little more about that or maybe I want to learn about arrays or data visualization better there's tons of stuff online great resources for this are usually going to be the um uh the official wiki and all of these libraries have their own wikis that have documentation where they have all of their functions listed examples that are nice and easy to follow and a lot of times there's multiple examples usually showing a situation where you what you're trying to do stack Overflow I think I have it as dot net it's actually.com um stack Overflow is a great website to just search if you um have a question on something um if you have a question on something in python or any sort of programming question chances are someone's probably asked it in stack Overflow so you're welcome to search through it and look and see if someone's asked it and see what the answers would be um another thing that you can do too is you can go and check out other people's like implementations and code on GitHub a lot of times people like to share their code because they want people to see how it's worked people like improving upon it and you're usually welcome to usually use someone else's implementations and codes and methods given that you give them credit and you need to check the licenses that they have too so some examples of licenses I think we I think talk about later the MIT license lets you use and pretty much do anything with someone else's code um but there are some that are more like open source licenses that mean like you can't use it for something that generates money um or you can use it but you can't change it or modify it you know without permission so um just some examples of that there's tons of other sites for this too but stack Overflow YouTube python Wiki those are uh good starting resources that will probably get you just about anything that you need um oops one second okay so we will be getting to kind of the fun portion of this and I will stream this with you so that if you have questions or you want me to show you something I'm happy to show you the functions that you want some of these will be gone over in the next activities in the next um uh like uh lectures but for today's activity we will open the extras python kernel and then we'll follow along with the instructions and I'll kind of work with that with you all so this will explain how to import those libraries and tools um uh like I think someone was asking that in the chat earlier as well as like some special functions that we can use among other things so they do that without further ado discard yes okay let's open up extras great ah okay so this will start off giving some examples of Loops um and I will show you some examples of like um stuff in here but so this will be less of like um like what you guys will be able to type out and more of just kind of running the examples to see what happens so excuse me in the for Loop for instance we can see that I have this list right here right and you can change this to be whatever you want it to be and then I have a counter and what I do here is is that for every word within words the counter increases by one so remember that this right here increases by one right and if I run this then I get four if I were to change this here um and to put this inside of the loop what this will do is this will print this multiple times so now I know it starts at zero then it goes to one then two and three if you want it after it counts so it has more natural counting you put it after and then it goes one two three four um if you want a for Loop to do a set number of actions however you can say within a range of something and this will go from zero to the number that you specify so for instance in this case um for I in range of 2 will run exactly two times so it will run for zero and one and then it stops before it gets to two so it's not inclusive of this number here so when I run that I just get the first two um words on this here and let me leave that chat open here so if you all have questions um you all were able to open this one up right I assume foreign okay cool good um Okay so it should be so it's the extras python notebook um it's inside of the activity section it should be the top one the extras.ipy and B this one right here cool awesome so and most of these cells should all be filled out so if you just want to run it or change the values to see like how it works and what it what it does you're welcome to do that um for a while loop I'm including the booleans that are inside of this um so I have this is a more complex example here basically so what happens is I have this Boolean that is called stay inside the loop and I have it set to true and then I have a counter value that's equal to zero so while this stay in the loop is true which it is right now because I said it at the beginning it will go through and run this this code right here over and over and over until this comes back false so the exit condition for this will come from something inside of this here so you want to be careful that you don't create an infinite Loop because if say for instance I remove this and I just say x equals one if I run this this will run Forever Until I break the cell and if you have that happen that's okay it happens you can press the stop button right here to interrupt the kernel so if you press it it stops this right so now if we go back into this here um what it's going to do is if the counter is less than 10 it will print the number right that's in the counter and then it will increase it by one if the counter is equal to 10 then it will no longer do this section it will do the else so this is what the l section is then what happens is it will set stay in the loop to be false and it will print hey I'm exiting right then once it's left this portion it hits the while and then it doesn't run again it just goes to the end of the script so if you hit shift enter what happens is it prints out the counter it happens in a Flash and then it exits the loop um to show this maybe a little bit more in depth let me show you something here okay I'll show you something that might make this a little bit easier to follow as to what happens so so what's going to happen is every time it runs through it's going to wait for half a second so if you see this is what's happening right now in the loop and then it's done that's it so additional statements you saw what was happening earlier um if you run this it looks to see hey what's the first word in this if statement or this um word that I gave here is it h so that's what this double equal sign is for so it's looking at the first thing in the word which is H and it's checking is it h and then it prints out yes the first word of this is H and that's what the output is if I were to change this to a lowercase case does matter and it says there is no Capital H at the beginning of this word so that's an example of a decision that can happen within this um functions so this is a bit more of maybe a complex function here that I was going to explain um so say for instance I have a function called starts with H like building upon this previous one here starts with H and it does the same thing it's this exact same thing it's just within this definition here I set this list Define it and then I combine this with the for Loop and notice how this for Loop looks really nice and pretty so now it just goes through for every word within words does it start with h and then it runs and then it prints out yes this starts with an h no that does not no that does not and yes this one does so does that kind of make sense so far with what we were at with um like conditionals and Loops I will go into importing libraries and some of the other stuff after this here so that'll be a lot of the built-in functions for python okay if you have a question drop it in the chat and I'll I'll try to come around to it so we're I think we've got about half an hour left so I want to be able to answer any questions that you'll have or examples that you want to see um so import pandas SPD so you're wanting to see how to import these libraries right so at the very beginning of this we will import this so you do import and that shows up as green all lower case and then the library name in this case it's called pandas as PD so you can skip this last portion of this if you do that but that means that instead of calling PD I have to say and this dot data frame and that's how I create a data frame for this here right but that's a lot of typing for that and that might be a little cumbersome so you can use the shorthand to call it something um generally it's accepted to use PD but you could use it as something else so like I could say pan you know um and then I could call hand dot data frame or whatever you know um but this is what's generally accepted for that um and the reason that I am suggesting using that whoops uh the reason I am suggesting using that is almost all the examples that you'll find online will use that PD the the shorthands that I'm giving here so here's an example of what a data frame would look like and when you give off the data frame output for this gives you a nice pretty graph that you can look at here compared to the old list you couldn't really tell what was what so this is one of the benefits for pandas there's a lot of other ones so like uh an example of this is I could do uh let's see here yeah uh to CSV Ile about a CSV I may have to look up the yeah so I saved this file here right this is a file that's saved where the script is and if I want to read if I want to create a new file for that or read that into a new data frame I can say data is equal to um Candice PD read CSV and it's an underscore a lowercase open parenthesis and then I give this exact same file name here I think that should be the correct yeah okay so if you call back data it comes back like this here so what's interesting is now you have an extra column here so the reason for this is that this right here is the index column um pandas did not know how to interpret that so this is actually the index column here there's a lot of ways to set that that's something that you can like look on the like the pandas Wiki to say like index true or unindexed remove index whatever or you can say what is the index um I'm not going to go into that because we have some a few other functions and I'm sure you'll have questions so um numpy same thing import numpy as in E and then if you are unsure what a how to import a library or what the name of it is you can just look it up so if you want to look up numpy in this case I mean if I looked up numpy and I bring this up here the documentation for this will show you how to get started for it so you can see how to install it how to import it right here this is what I was talking about when I say that they have fantastic documentation on this and they tell you exactly what you need to do and how to do it um so in this case just like they had typed I'm importing it the same way and I'm giving it the same shorthand um and now so for numpy you have this interesting way to create these arrays and there's tons of ways that you can do this and manipulate this much easier than it would be doing this with Python's built-in functions you'd have to use a lot of loops and if statements and it gets very complex so say for instance um I want to create a list that goes from zero to zero to 14. I want 15 things in that list I run that and now I get an array which just is just a list from 0 to 14 right but what if I want that to be a rectangular array what if I want it to have um three rows and five columns but still 15 items in it so if I add this extra portion to call it to reshape the array so like if you think of it as one long array right you can shorten it and make it fatter basically so if you do this if you notice now it creates this kind of pretty um like array that might be a little bit easier to follow um numpy is also able to do element wise operations so like for instance if you wanted to do the sine or cosine of this I think actually I have this in this one here uh uh oh I guess I didn't save it um you can do uh like NP sine of a and I think that will give you the sign yeah so that gives you the sign of every number inside that array and it's a very simple easy function to use you just get the sign for every number inside of that um if you wanted to do that built in it's a lot more complex you have to use a for Loop and have an if statement and you know so on and so forth and that gets very complex so these libraries let you have these shorthand functions that save you a lot of time in programming the reason I teach you some of those things is so that you understand what they're doing kind of behind the scenes or under the hood so some extra functions that you may use that may be helpful there's a sleep command the Sleep command puts the process and weights so what happens here is that it literally halts the process for the number of time in seconds sometimes this is important um if you're grabbing data from a database and you are afraid that you're going to overload the database you can slow down the requests by having the process wait this is one way to do it you don't there's tons of other ways to do it but this is probably the simplest way and maybe say you send a request you wait a couple of seconds and then you send a request again you can put that for instance inside a loop so that's done doing import time time does all sorts of time management stuff so this could be uh getting the date and time it could also be the same as um getting the program to wait or measuring how long the program takes to run maybe you want to have a really fast analysis and you're trying to improve uh someone's method right um and you want to time it you would use that date time is another really interesting one that you can use that gets you the exact correct time and date and all the way down to the milliseconds that your clock is running so all the way from years months days hours minutes seconds and all the way down to I think Pico's second or nanoseconds I'm sorry yeah nanoseconds so very precise um You probably won't need that Precision when you're when you're using date time but it is there we've talked about string split I kind of showed you all that a little bit earlier but you already know how that works but say for instance remember earlier I had mentioned what if we had numbers and we want to use those as numbers um if I try to take the first thing in this the 100 and I try to add 10 to it to see what I get I get an unsupported operation meaning that I can't add 10 to a sentence that just doesn't make sense like if you try to take a word and add a number to it it doesn't work that way however if I use What's called the int command integer it forces that number to try and recognize um what kind of number it is so in this case if I run int and then I add 10 I get 110 so it's 10 and then this becomes an actual one a number that's 100. there are some other commands too like um operating system commands so you do this through importing OS this is a lot of stuff that you might see in um trying to read file names creating files copying stuff so if you remember I mentioned earlier the operating system um like the way that people used to use computers they entered in those commands to do basic math functions or create files create folders the OS lets you manipulate the computer's ability to do that so um a good example of this is say you want to know what directory you're working in right so in this case for instance since we're I'm not working on my home computer we're working on my geohub this is the folder that we're working in so that's what the current working directory is so get CWD is uh get current working directory um that's really important for if you have like a script that you you need to know where files are and you need it to read stuff you can take that current working directory and you can add things to it um so that is about it um if you have questions feel free to send them now if you have um uh examples that you would like to see I'm happy to show a few of them and then I think at about noon I think we'll go to lunch here so I think we've got about 15 minutes if you all want to see me try and set something up hopefully y'all are feeling um capable now of being able to um create a simple program yeah so importing a file so um so say for instance maybe you want to import a CSV file right so let's do this I will start this blank and I will create a new Jupiter file and I'll do this from scratch to show you how you would do this so say you uh give me one second here so say you want to create something and you want to import a CSV file so we have let's see where I have some data so let's see yeah I've got some data here so okay so say I create a new Python 3 script so remember I mentioned inside of this you can create your own scripts I create this and it sends me to the editor for that script I can rename this I'm going to call this the intro example uh maybe five or something because I think I had four before the first thing I will do is import pandas as PD right so I import that I run it and boom it's done that's how you know it's done is it has a number next to it um the next thing that I will want to do is I want to create a blank data frame so DF is equal to PD dot data frame and then that's it it's blank you know you don't have to do this section but I like doing that because I feel like I understand what's going on in the code and then you can say DF is equal to e d dot uh read CSV and then you give the file name so here's the thing with file names and file structures if you are working in the same directory that your file is right so in this case I have this file right here this is the python notebook I'm working in and I have all these CSV files that I want to import right tons of CSV files here that I can import so what's import uh data data test so this is for the machine learning example but we'll use this as an example so data is it data test dot CSV and that imported the file into the data frame so now if I just press data frame and I just try to call it back to see what I get I get all of these sets of data for this it's got 16 000 something rows and 27 columns worth of information about in this case building energy so this would be I think I believe this example is for um energy usage in I think maybe kilowatts um so for instance if you wanted to do something with this data a very brief example would be calling a function within the data frame so DF Dot Plot will give you a very dirty uh plot of everything but that will probably take a really long time to run that um oh I guess it didn't for this one so that gives you a really crazy plot but because there's 27 columns it's very dense right so remember earlier I mentioned the key pairs so maybe let's just look at the first one here so the first ones got this name right here right so let's do DF um e so let's open up the hard brackets this right here right and then let's do Dot Plot and then that gives you just the data for this here so you can get some really interesting data just real quickly looking at it faster than you would normally in Excel um these plot functions are built into pandas but they use another Library called matplotlib or python plot or Pi plot for short that's another lecture that we'll be talking about that um and so earlier in the same realm you use that exact a different but very similar um uh command to save that data as a CSV file you can also read those as Excel files I believe it just says read Excel if you want to say that instead I don't have any Excel files saved up here those have more inputs because Excel files can have pages I typically recommend just sticking with csvs for now um just for the Simplicity of it does that explain does that give you a good overview of how to import a file cool yeah and there's tons of other things that you can do so um I'm trying to think of examples of this you could um you import us uh create a current working directory so if say for instance maybe you have multiple files that you want to import right um no no uh well okay the question yes it does look a little different so I can tell you what the differences are and I can show you really quick actually my geohub um has this button right here that takes you to their home page the other option too that comes up that's not normally on your home PC is this terminate session button um if you are working in so let me terminate this real quick and I'll show you what um it looks like normally on a home PC so you can launch this through what's called a anaconda which is a manager for this um you can also install this manually so normally when I launch this uh you create this through um a powersh uh not Powershell um command prompt or Powershell and what you do is you launch Jupiter notebook you have to install all this stuff on your home PC and you'd have to look up how to how to do that it's pretty easy but um you've launched this it creates Jupiter and it brings you to this here so great example of what's different you don't have the my geohub on the left and you have two buttons now on the left quit and log out if I open up a file so this is one of the exact same scripts that we were working with you have a log out button it's just a little bit different but for the most part you probably won't notice the difference so um that's about it though not that many uh big differences on it so yep yep any questions about eight minutes I can try to maybe hammer out one more example if someone wants to see something somewhat simple and if you want to play around with this by the way so I guess I can tell you this here so you can launch it through the course but if you're on my geohub and you want to just play around with it outside of the course you have access to Jupiter on that um so you can go to resources tools this right here and click on that and you have access to all these tools here and you'll learn some of the other ones in the other lectures I think um but for Jupiter though look in the resources here and you'll find one that's called Jupiter notebook and you have one with the Anaconda and one without just run the one that just says Jupiter notebook and you can launch this tool and it launches it outside of the context of the class so if you want to play around with the scripts and all that you can um quick word of like note on this um my geohub is very unique in that it has a lot of those libraries already installed um normally if you wanted to install libraries on your own you would have to go open a terminal [Music] and then you would have to run an install function for something in a lot of cases the first thing you might install is a pandas um thankfully all the stuff's free so you can have access to this at home if you want to use it so but I believe that is it so we have about five minutes left I think I used up almost the exact amount of time I hope I didn't overwhelm you guys too much I know it's a lot to learn um programming takes a lot of practice to really kind of get the gist of it sometimes it helps to talk through things with someone or to write down your ideas and like a flowchart to see what you want to do um best tips I could give is don't be afraid to look something up um don't be stubborn about it um someone else has probably done it so um yeah so for practice I would probably go to let's see the uh it's on the resources this guide right here I would pick one of the tools that you want to do um probably what I would look at is inside of this interactive tools and lessons here um I would probably look at that um you can also go one of these is for uh Jupiter I don't know I guess they don't have one on here for that um this just goes through like the basic uh programming chat would you recommend programming tasks for beginner to start learning how to code yeah so beginner tasks that so let me tell you what my tasks were that I started with so my basic beginner tasks started off with um I was actually doing text mining for civil engineering and this is where I learned a lot of the stuff that I was doing um working with an application programming interface is a very good way to start um yeah yeah you can find tons of those I can give you I think pandas cookbooks probably the best one that I can think of this will give you a good introduction on data science and pandas I'll leave that one in here for you um they have some good examples on like how to use pandas because you will probably be using that a lot um Jupiter you might want to go through and do some like Jupiter um uh tutorial I've shown what I can but you may want to go through and look at like datacamp would probably be a good place um but find the find the free resources there's always going to be a free resource for it um I have personally used the codedx that one's a really good one this one's kind of a very basic oh no was it no longer up oh oh there it is this right here and it kind of does it in like a video game environment I always thought it was kind of fun um that's another one that's a good one um it just gives you the very basics for it um really my recommendation is if you have a project that you're trying to do a good task is to try and automate something so say you have a task that you manually do maybe it's renaming files maybe it's um analyzing data calculating z-scores for statistics something like that try to automate that using python using the for Loops that I mentioned the if statements that's always a good place to start with that usually it's a simple enough task that you should be able to do it within like maybe a few days to a week depending on how much time you have to work on it um and it feels very rewarding to know wow I can just shift enter run and boom I no longer have to work for an extra hour to do this by hand so find something that you think you can automate um I think that's what I would say and that's what I would recommend um I think that's about it there's tons of user created libraries too um machine learning stuff like that um there's really a lot that I could go over I could spend a whole semester talking about this so um Zen of python I think was a good one too I mentioned that book earlier I think that's it might be a little bit in depth uh I think that's uh if you want to kind of look at that this talks about uh just the basic things that you should kind of remember um it's not really examples and stuff like that but it's a good thing to check so some of these were things that I had brought up so okay um I think it's about lunch time I don't want to keep you all any longer um if you have specific messages you can send me a message otherwise I will let you guys go
