---
title: "Justice in Data: Introduction to Python Programming"
unit_id: 132
course_id: 10
level: "Foundation"
slug: justice-in-data-introduction-to-python-programming
is_course: 0
---

# Justice in Data: Introduction to Python Programming

Comprehensive introduction to Python programming fundamentals for data manipulation and decision-making. Presenters: Sharma Chakravarthy (PhD, Professor), Steven Tanner McCullough (PhD Student Researcher), June Young Park (PhD, Assistant Professor), Jessica Eisma (PhD, Assistant Professor), Junaid Ahmad (PhD Student Researcher). Source file: Tuesday - Intro to Python Presentation.pdf

**Learning Objectives**: Apply basic programming concepts, understand Python syntax and logic, create programs that manipulate data, implement decision trees, and use data tools.

**Course Overview**: Covers programming in engineering, Python primer, programming syntax, and in-class examples. Why Python: high-level interpreted language with self-managed memory, faster to program than C++/Assembly, extremely large online community, easiest learning curve. Python history: conceived in 1980s (influenced by ABC, SETL, Perl), emphasizes code readability with indentation, as of 2021 the 3rd most popular language (after Java and C), object-oriented, untyped variables. Python 3 and Jupyter Notebook (web-based, platform-independent, runs in browser, code organized in editable/executable cells) are used throughout.

**Jupyter Navigation**: File explorer interface for creating/deleting folders and files, launching Python 3 notebooks, opening terminal prompts. Notebook editor with cells operated via hotkeys: Press B to create cell below, double-press D to delete, press A to create above. Cell types: Markdown (create titles/lists for organization) and Code (computation). Shift+Enter runs selected cell and generates output. MyGeoHub limit: 3 Jupyter sessions per user (excessive sessions overload server).

**Programming Fundamentals**: Sequential instruction execution; principles include borrowing ideas, Occam's Razor, platform independence, and "Zen of Python" (readability counts, easy implementation).

**Syntax & Data Types**: Syntax is the grammar/rules of programming language. Variables are placeholders for data (volatile, lost after script finishes); assignment A=B means A will be replaced by B (unidirectional). Four data type categories:
- **Numbers**: Integers (whole numbers), Floats (decimal precision), Complex (real/imaginary pairs)
- **Strings & Characters**: Single quotes for characters ('A', '%', '5'), double quotes for words/sentences ("Hello everyone!"), immutable
- **Grouped Variables/Matrices**: Lists [1,2,3,4] (mutable, ordered, square brackets), Tuples (2,2,4) (immutable, ordered, parentheses), Sets {1,2,3} (mutable, unordered, no duplicates, set()), Dictionaries {'Col1':[1,2], 'Col2':[3,4]} (mutable, ordered, tagged elements)
- **Boolean**: True or False (1 or 0)

**Indexing**: Python uses zero-based indexing (0 to length-1) for arrays, strings, lists. Unique to Python: negative indexing (-1 for last element, -len() for first).

**Libraries**: Imported at script start via `import <library>` or `import <library> as <nickname>`. Libraries supplement Python's built-in tools (analogous to tools on a desk).

**Operators**: Mathematical operations with non-traditional syntax in Python: Addition (+), Subtraction (-), Multiplication (*), Division (/), Modulus/Mod (%), Integer Division (//), Exponential (**). Order of Operations applies; use parentheses when unsure. Interactive example: numbers.ipynb activity.

**Conditionals & Logic**: Boolean values (True/False) for decision-making. Conditional if statements with required indentation for code-to-run-when-true. elif (else-if) strings conditions sequentially; first True exits and skips others. else statement catches remaining conditions. Syntax example: if x<2: do_stuff() elif x<4: x=7...else: do_this().

**Loops**: Repeat operations until exit condition reached. Two types: while() loops (dynamic exit condition), for() loops (set exit condition, built for iterating lists/strings). Loops comprise Call (Start), Body (Loop), Exit Condition. Loop nesting: decisions, loops, lists nested inside one another; 2D tables are lists containing lists (example data: Jane Doe 25, John Brown 30, Jim Ford 22).

**Functions**: Code snippets callable to redo tasks with variables. All libraries have functions (e.g., time.sleep()). Custom functions tidy repetitive code.

**Error Types**: Syntax (command typed incorrectly, e.g., primt() instead of print()), Logic (program compiles but has unintended consequences, e.g., if i>5 instead of i<5), Runtime (like logic errors but not hardcoded, e.g., accessing non-existent objects).

**Special Libraries & Data Tools**:
- **Pandas**: King of data management in data science; extension of traditional lists/libraries/dictionaries. Two main classes: DataFrames (multi-dimensional) and Series (ordered, 1D). Has built-in functions to read/write files and clean/organize/search data. Import: `import pandas as pd`
- **NumPy (Numerical Python)**: Basis for scientific computation; provides arrays with built-in matrix manipulation functions. NumPy arrays faster than standard Python for large datasets. Capabilities: quickly create arrays (arranged for visualizations, random numbers for testing), grab unique values, transpose matrices, work with CSV, implement mathematical formulas. Import: `import numpy as np`

**Interactive Activities**: numbers.ipynb, matrix.ipynb, strings.ipynb, extras.ipynb in Jupyter Notebook tool under Activities.

**Additional Resources**: Official Python wiki, stackoverflow.net (search before posting), GitHub repositories (check licenses). Tutorial: Python Documentation (docs.python.org/3/tutorial).

**External Resources**: Pre-Survey (QuestionPro link), YouTube recording of presentation (B6NapuHNux4).

## Summarized attachments
- **Introduction to Python Slides** (`Tuesday - Intro to Python Presentation.pdf`, file): Presented by Sharma Chakravarthy (PhD Professor), Steven Tanner McCullough (PhD Student Researcher), June Young Park (PhD Assistant Professor), Jessica Eisma (PhD Assistant Professor), and Junaid Ahmad (PhD Student Researcher). Covers learning objectives (apply basic programming concepts, understand Python syntax/logic, create programs for data manipulation and decision-making), programming in engineering, Python advantages, Jupyter Notebook interface, and in-class examples.
- **numbers.ipynb** (Jupyter notebook, MyGeohub): Interactive activity demonstrating Python mathematical operators (addition, subtraction, multiplication, division, modulus, integer division, exponential) and order of operations principles with executable code cells and examples.
- **matrix.ipynb** (Jupyter notebook, MyGeohub): Interactive activity exploring Python grouped variables and data structures including Lists (mutable, ordered), Tuples (immutable, ordered), Sets (mutable, unordered, no duplicates), and Dictionaries (mutable, tagged elements) with practical examples.
- **extras.ipynb** (Jupyter notebook, MyGeohub): Interactive activity exploring additional Python functions, Pandas library (king of data management in data science with DataFrames and Series classes), NumPy (Numerical Python for scientific computation with array operations and matrix manipulation).
- **Introduction to Python Programming Pre-Survey** (https://utaedu.questionpro.com/a/TakeSurvey?tt=Vsdmb3CeLMEECHrPeIW9eQ%3D%3D, survey): QuestionPro-hosted pre-assessment survey for evaluating prior knowledge on programming.
- **Introduction to Python Programming Recording** (https://www.youtube.com/watch?v=B6NapuHNux4, video): YouTube recording of presentation covering programming applications in engineering, Python as high-level interpreted language with large community, learning objectives, lecture overview (programming in engineering, Python primer, syntax, in-class examples), and hands-on activities.
