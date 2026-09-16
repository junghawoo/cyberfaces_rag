---
title: "My cool module"
unit_id: 147
course_id: 0
level: "Expert"
slug: my-cool-module
is_course: 0
objectives:
  - "Learn something"
  - "Learn more"
---

# My cool module

**Description:** A super long explanation

## Fetched resources (external URLs)

### Jupyter Notebook (link)
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

### Jupyter Notebook (notebook)
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
