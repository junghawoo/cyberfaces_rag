---
title: "Introduction to Python"
unit_id: 125
course_id: 0
level: "Foundation"
slug: introduction-to-python
is_course: 0
objectives:
  - "Learn what Python is"
  - "Learn the basic data types"
---

# Introduction to Python

**Description:** This teaches the basics of Python.

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/nujwoo/python101/01cal.ipynb

## Using Python as a Calculator

A programming language wouldn't be much use without basic arithmetic functions

```python
2+2
```

```python
4*30
```

```python
(50-5*6)/4
```

(If you're typing this into an IPython notebook, or otherwise using notebook file, you hit shift-Enter to evaluate a cell.)

Notice that the last line returns `5.0` rather than just `5`. This is because division doesn't always return a whole number (try `5 / 3` for example), and so the underlying number type has to be able to reflect this. Thus first two lines return an **integer**, also known as *whole numbers* to the non-programming world, and the third a **floating point number**, also known (incorrectly) as *decimal numbers* to the rest of the world.

You can define variables using the equals (=) sign:

```python
width = 20
length = 30
area = length*width
area
```

If you try to access a variable that you haven't yet defined, you get an error:

```python
volume
```

and you need to define it:

```python
depth = 10
volume = area*depth
volume
```

You can name a variable *almost* anything you want. It needs to start with an alphabetical character or "\_", can contain alphanumeric charcters plus underscores ("\_"). Certain words, however, are reserved for the language:

    and, as, assert, break, class, continue, def, del, elif, else, except, 
    exec, finally, for, from, global, if, import, in, is, lambda, not, or,
    pass, print, raise, return, try, while, with, yield

Trying to define a variable using one of these will result in a syntax error:

```python
return = 0
```

The [Python Tutorial](http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator) has more on using Python as an interactive shell. The [IPython tutorial](http://ipython.readthedocs.io/en/stable/interactive/tutorial.html) makes a nice complement to this, since IPython has a much more sophisticated iteractive shell.

### Python For Beginners (link)
*URL:* https://www.python.org/about/gettingstarted/

# Python For Beginners | Python.org

Python For Beginners | Python.org
Notice:
This page displays a fallback because interactive scripts did not run. Possible causes include disabled JavaScript or failure to load scripts or stylesheets.
Python
>>>
About
>>>
Getting Started
Welcome! Are you
completely new to programming
?
If
not
then we presume you will be looking for information about
why and how to get started with Python.
Fortunately an
experienced programmer in any programming language (whatever it may be)
can pick up Python very quickly.
It's also easy for beginners to use and learn, so
jump in
!
Installing
Installing Python is generally easy, and nowadays
many Linux and UNIX distributions include a recent Python.
Even
some Windows computers (notably those from HP) now come with Python
already installed.
If you
do
need to install Python and aren't confident about the
task you can find
a few notes on the
BeginnersGuide/Download
wiki page, but installation is unremarkable on most platforms.
Learning
Before getting started, you may want to find out which
IDEs
and
text
editors
are tailored to make
Python editing easy, browse the list of
introductory books
, or look at
code samples
that you might find
helpful.
There is a list of tutorials suitable for experienced programmers on the
BeginnersGuide/Tutorials
page. There is also a list of
resources in other languages
which might be useful if English is not your first language.
The
online documentation
is your first port of call for definitive information.
There is a fairly brief
tutorial
that gives you basic information about the language and
gets you started. You can follow this by looking at the
library reference
for a full description of Python's many libraries and the
language reference
for
a complete (though somewhat dry) explanation of Python's syntax.
If you are looking for common Python recipes and patterns, you
can browse the
ActiveState Python Cookbook
Looking for Something Specific?
If you want to know whether a particular application, or a library
with particular functionality, is available in Python there are a
number of possible sources of information. The Python web site
provides a
Python Package Index
(also known as the
Cheese Shop
, a reference to the Monty Python
script of that name).
There is also a
search page
for a number of sources of Python-related
information. Failing that, just
Google
for a phrase including the word ''python''
and you may well get the result you need.
If all else fails, ask on the
python newsgroup
and there's a good chance someone will put you on the right track.
Frequently Asked Questions
If you have a question, it's a good idea to try the
FAQ
, which answers the most commonly
asked questions about Python.
Looking to Help?
If you want to help to develop Python, take a look at the
developer area
for further information.
Please note that you don't have to be an expert programmer
to help.  The documentation is just as important as the
compiler, and still needs plenty of work!
The PSF
The Python Software Foundation is the organization behind Python. Become a member of the PSF and help advance the software and our mission.
