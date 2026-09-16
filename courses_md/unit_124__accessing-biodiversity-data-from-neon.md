---
title: "Accessing biodiversity data from NEON"
unit_id: 124
course_id: 0
level: "Foundation"
slug: accessing-biodiversity-data-from-neon
is_course: 0
objectives:
  - "Use Python to access USGS NWIS Surface Data Portal"
  - "Using Python to pre-process USGS streamflow data"
---

# Accessing biodiversity data from NEON

**Description:** Learners will become familiar with how to download, access, and process biodiversity and other environmental data from the National Environmental Observation Network. Data will be downloaded from cloud servers and stored in CVs and standard database formats.

## Extracted resources (local files)

### Analytical Framework for Analysis of Long Run Land Use Change
*Source file:* `subtitles-de.vtt`  ·  *type:* file

WEBVTT

00:02.170 --> 00:04.136
Emo, close your eyes

00:04.136 --> 00:05.597
Why?
NOW!

00:05.597 --> 00:07.405
Ok

00:07.405 --> 00:08.803
Good

00:08.803 --> 00:11.541
What do you see at your left side Emo?

00:11.541 --> 00:13.287
Well?

00:13.287 --> 00:16.110
Er nothing?
Really?

00:16.110 --> 00:18.514
No, nothing at all!

00:18.514 --> 00:22.669
Really? and at your right? What do you see at your right side Emo?

00:22.669 --> 00:26.111
Umm, the same Proog

00:26.111 --> 00:28.646
Exactly the same! Nothing!

00:28.646 --> 00:30.794
Great

### English
*Source file:* `subtitles-en.vtt`  ·  *type:* caption

WEBVTT

00:02.170 --> 00:04.136
Emo, close your eyes

00:04.136 --> 00:05.597
Why?
NOW!

00:05.597 --> 00:07.405
Ok

00:07.405 --> 00:08.803
Good

00:08.803 --> 00:11.541
What do you see at your left side Emo?

00:11.541 --> 00:13.287
Well?

00:13.287 --> 00:16.110
Er nothing?
Really?

00:16.110 --> 00:18.514
No, nothing at all!

00:18.514 --> 00:22.669
Really? and at your right? What do you see at your right side Emo?

00:22.669 --> 00:26.111
Umm, the same Proog

00:26.111 --> 00:28.646
Exactly the same! Nothing!

00:28.646 --> 00:30.794
Great

## Image text (OCR)

### `original-48b772df787b69c83880445ff1177f8e.png`
Field: Wheat field 429 Vv

one Management

Productivity map

Recomendation date

() 05 Jun 2024 #4 Field Parameters

Recommendation

jeld potential: 1.5-1.7 Tlac ©

Max Roi Balanced Max yield

40 (63) 68

cR ield: 7
or Field: Wheat field 429 Q

Zone Management

Zone Productivitymap Nitrogen Rx

$l Zone Management
» vovurru24

Field Parameters

Recommendation

| potential: 1.5 -1.7 Tac

Max Roi Balanced Max yield

40 63 68

21% 71%

## Fetched resources (external URLs)

### Lab Assignment #1 (notebook)
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

## Non-text files (not extracted)

- `ElephantsDream.mp4` (mp4)
