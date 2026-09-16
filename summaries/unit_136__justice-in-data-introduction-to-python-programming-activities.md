---
title: "Intro to Python Programming - Jupyter Notebook"
unit_id: 136
course_id: 0
slug: justice-in-data-introduction-to-python-programming-activities
is_course: 0
---

# Intro to Python Programming - Jupyter Notebook

Beginner Python programming activities module from the Justice in Data course (NSF CyberTraining; Tuesday "Intro to Python" session, examples authored by Tanner Steven McCullough, UT Arlington). Resources are Jupyter notebooks hosted in the GitHub repo PurdueCyberTraining/justiceindata under Tuesday/Activities, plus a "Jupyter Notebook - File Explorer" link to proxy.mygeohub.org (fetch failed with ConnectionError).

Notebook `extras.ipynb` — Loops, functions, and core libraries:
- For loops iterating over a list of words and with range(); indentation requirements; counting items.
- While loops with Boolean exit conditions (stay_in_loop flag, counter to 10).
- Conditional if/else statements checking a word's first letter; defining a function starts_with_h(word) and combining it with a for loop.
- Pandas: `import pandas as pd`, creating an empty and a populated pd.DataFrame({"Col1": ..., "Col2": ...}), df.head().
- NumPy: `import numpy as np`, np.arange(15), .reshape(3, 5), note that NumPy does fast element-wise operations versus loops.
- Extra functions: time.sleep for pausing, datetime.now() for high-precision timestamps, string .split() to turn "100 757 675" into a list, int() to convert strings to numbers (with the string-plus-int error example).
- OS commands: `import os`, os.getcwd() for the working directory and file manipulation.

Notebook `matrices.ipynb` — Variables: grouped types (ordered vs. mutable). Tuples (immutable, parentheses, index access, speed-optimized), lists (mutable, hard brackets, element reassignment, the workhorse for datasets), sets (set(), unordered, unique values only, no indexing, .add() method), and dictionaries (key/index pairs, e.g. {"First": [...], "Last": [...]}, [key][index] access), with a pointer to DataFrames as the easier advanced structure.

Notebook `numbers.ipynb` — Variables: numbers. Comments with #, variable assignment and naming rules (no spaces, reserved words like "is", invalid names such as `@this_is_a_variable`, Jupyter color cues for reserved functions), one-directional assignment (10 = x fails), calling variables with Shift+Enter, multiple assignment on one line (variable_1, variable_2, variable_3 = 10,55,2.55), and number types int vs. float with type() and automatic type conversion.

Notebook `strings.ipynb` — Variables: strings. Strings as character lists useful for text mining and filenames; creating strings with double or single quotes; indexing single characters; .split("separator") to break sentences into word lists; mention of upper/lower-case and other string manipulation methods.

## Summarized attachments
- **Jupyter Notebook - File Explorer** (https://proxy.mygeohub.org/weber/47027/TGKVOoM5psYjdl5f/9/tree, link): No machine-readable content extracted.
- **extras** (https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/Activities/extras.ipynb, notebook): Jupyter notebook tutorial covering Python loops (for loops with lists and range(), while loops with Boolean conditions), conditional if/else statements, defining functions, and core libraries (pandas DataFrames, NumPy arrays with reshape, time.sleep pausing, datetime.now timestamps, string split methods, int conversion, os module for working directory and file manipulation).
