---
title: "Intro to Python Programming - Jupyter Notebook"
unit_id: 136
course_id: 0
slug: justice-in-data-introduction-to-python-programming-activities
is_course: 0
---

# Intro to Python Programming - Jupyter Notebook

## Fetched resources (external URLs)

### Jupyter Notebook - File Explorer (link)
*URL:* https://proxy.mygeohub.org/weber/47027/TGKVOoM5psYjdl5f/9/tree

[fetch error: ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))]

### extras (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/Activities/extras.ipynb

# Loops

### For Loops

Below is an example of a for loop in action iterating over a list.

This loop counts up every time it loops and gives us the number of items it looped through in this list.

### It is important to note that the code that is looped will be tabbed over in python. If this is not done you will have problems.

```python
words = ["Hello","no","Wow!","Happy"]

count=0

for word in words:
    count+=1
print(count)
```

_output:_
```
4
```

### For Loops

Below is an example of a for loop in action with a set number of loops to perform.

It is set to loop exactly twice

it loops for every number 'i' in range of 0-2, not including 2, and prints the first 2 words in this case

```python
words = ["Hello","no","Wow!","Happy"]

count=0

for i in range(2):
    print(words[i])
```

_output:_
```
Hello
no
```

### While Loops & Booleans

Below is an example of a while loop in where the exit condition is set outside the loop is reached from in side the loop

The exit condition can dynamically change inside the loop, contrasting to the set exit a for loop has.

```python
stay_in_loop = True
counter = 0
while stay_in_loop:
    if counter<10:
        print(counter)
        counter+=1
    else:
        stay_in_loop = False
        print("Exiting loop!")
```

_output:_
```
0
1
2
3
4
5
6
7
8
9
Exiting loop!
```

### Conditional Statements

Below is an example of a simple if/else statement that checks the first letter of a word

```python
word = "Hello!"

if word[0] == "H":
    print("The First letter of this word is H!")
else:
    print("There is no H at the start of this word.")
```

_output:_
```
The First letter of this word is H!
```

# Functions

```python
def starts_with_h(word):
    if word[0] == "H":
        print(word + " starts with H!")
    else:
        print(word + " doesn't start with H!")
```

```python
words = ["Hello","no","Wow!","Happy"]
```

Combining this with a for loop we can now check a list of words

```python
for word in words:
    starts_with_h(word)
```

_output:_
```
Hello starts with H!
no doesn't start with H!
Wow! doesn't start with H!
Happy starts with H!
```

# Pandas

```python
import pandas as pd
#using as pd makes the library call shorter and easier to type
```

```python
df = pd.DataFrame()
#Creates an empty Dataframe
```

```python
df = pd.DataFrame({"Col1":[1,2,3],
     "Col2":[4,5,6]})
```

```python
df.head()
#Reads off the column names and the first few values
```

_result:_
```
Col1  Col2
0     1     4
1     2     5
2     3     6
```

# Numpy

```python
import numpy as np
```

```python
a = np.arange(15)
a
```

_result:_
```
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
```

```python
a = np.arange(15).reshape(3, 5)
a
```

_result:_
```
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
```

```python
#Numpy can do element wise operations much faster than usual loops can
a
```

# Extra Functions

### time.sleep

### datetime
##### (among other functions from time, this can be used to record and convert time, stop a program or measure how long a program runs)

```python
import time
print("Waiting...")
time.sleep(3)
print("Done!")
```

_output:_
```
Waiting...
Done!
```

```python
from datetime import datetime

now = datetime.now() # Gets the current time in a computer friendly language
print(now)
#This can give you ridiculous precision with time recordings
```

_output:_
```
2023-05-19 19:28:51.669548
```

### string.split()

Going back to the previous example the string library provides the ability to split phrases and words to a list.

Let's look at an example with a date as a string

```python
values = "100 757 675"

numbers = values.split()
print(numbers)
```

_output:_
```
['100', '757', '675']
```

### int()

The previous example is nice but it would the values given are still strings and have no numerical value

We can fix this using the int() command, this attempts to create a real number from the string.

One of these will give an error but one will not

```python
10+numbers[0]
```

```python
10+int(numbers[0])
```

_result:_
```
110
```

## OS commands


#### The OS library allows you to manipulate files if you are not using a libraries built in functions
#### It can get you directories, and perform certain console functiosn as well as other things

```python
import os
```

```python
#This will get the directory the script is running in. Useful for opening files.
os.getcwd()
```

_result:_
```
'C:\\Users\\McCulloughStevenTann\\OneDrive - UT Arlington\\Projects\\2023\\NSF CyberTraining\\Examples\\Intro to Python - Tuesday Session'
```

### matrices (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/Activities/matrices.ipynb

# Variables - Matrices

### We will create matrices of all types in this script

#### Variables that are grouped together have various names depending on if they are ordered and mutable (changeable)

# Let's try Tuples

Tuples are the simplest of grouped variables, they can only be assigned as a group, the order is important.
Individual numbers from within cannot be changed without re-assigning the entire group. (Immutable)


These are created like multiple variables on a line except they are grouped together with parenthesis.

a_tuple = (1,2,3,4)

Try it below

#### Now call back a variable within that tuple by calling its index.

An index is given by callin g the grouped object (a tuple in this case) followed by square brackets with the index inside

Like a_tuple[0] would give 1

Try it below with a different index

Remember that The first element is index zero

#### Immutability

Try assigning just an element of the tuple

a_tuple[0] = 0

#### This is not allowed because it is immutable

Tuples are more optimized for speed than lists and as such can only be re-modified by re-assigning the entire group

Good for values that will not change often (or at all)

# Now let's try Lists

Lists are the mainstay of grouped variables, they can be modified and are ordered.
Individual numbers from within can be changed and the list size can change.


These are created like multiple variables on a line except they are grouped together with hard brackets.

a_list = [1,2,3,4]

Try it below

#### Calling back the individual numbers within a list is the same as a tuple

a_list[0]

Try it again below.

#### Mutability

Try assigning just an element of the tuple

a_list[0] = 0

#### Notice there was no error this time?

Lists are still quite fast but not as fast as tuples.

However, they are highly adaptable and can change to meet your needs.

You will typically be using lists for most data sets.

# Sets

Sets are important for filtering among other things. They are unordered and can only contain 1 of each value within themselves.

Think like a bag of marbles where only 1 color marble can exist inside the bag.


These are created with a special function 'set()'

a_set = set(1,2,3,4)

Try it below

#### Without ordering you cannot use an index to call back numbers

a_set[0]

Try it below to see what happens.

#### Mutability

Because of the prior issue, sets cannot be changed in the same way.

a_set[0] = 0 Does not work

You can append a set however with a_set.add()

a_set.add(5) will add 5 to the set, try it below.

Consider trying it with a number already in the set and see what happens

# Lastly Dictionaries

Dictionaries are more complex but the most pwerful in organizing.
Indexes and Keys are used so that you can organize data Logically with names


These are created differently using 

a_dictionary = {"First" : ["Tanner","Steven","Jimmy"],"Last" : ["McCullough","Mac","Brown"]}

Try it below, you can copy the dictionary above and replace it with your own values for time if you wish.

#### Calling back the list within a column is similar but calling the name of the key.

a_dictionary["First"]

Try it again below.

#### Calling an individual name from a column uses a [key][index] pair.

a_dictionary["First"][0]

Try it again below.

#### Calling an individual name from a column using a [index] results in an error.

a_dictionary[0]

Calling rows is more difficult with this. We will show a more advanced version of this that is easier to use later in the lecture called DataFrames.

### numbers (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/Activities/numbers.ipynb

# Variables - Numbers

### We will create numbers in this script

```python
#Here is an example of  comments, using the pound or hastag at the beginning of a line
#No code will be run.

#Comments will be provided through the scripts to give hints and guidance for what certain command and functions do.

#We will assign numbers
```

### First we will create some variables names

##### But to do this in Python a value must be assigned first

An Example is shown below

```python
This_is_a_number = 10
```

### Now Try to show this number on screen
You can do this in Jupyter by calling the variable number and NOT assigning it

###### Try it in the cell below this and run the cell with Shift+Enter to see the output

To call a variable, just type the variable name and Jupyter will return it's value

# Variable Naming
### Note that variable names cannot include certain characters or spaces

Try running the cell below to see what happens

```python
This is a number = 10
```

### The word 'is' is one of many special terms used for logical programming and cannot be used by itself

##### In addition, python does not know where 10 should be assigned, is it to This? or is? or a? etc.

##### An easy rule of thumb in Jupyter is if a word you finished typing is any color other than black, then it has a reserved function.

Reserved functions cannot be used as variable names by themselves

##### Will not work
This is a number = 10

@this_is_a_variable = 100

##### Will work
This_is_a_number = 10
number1 = 


In addition, python treats spaces uniquely for variables and does not not where to assign 100 in the example.

## Variable Assignment & Multiple Assignments

##### Variable Assignment works in 1 direction only

Try running the cell below to see what happens

```python
10 = This_is_a_number
```

###### 10 Cannot be assigned as it is a number and not a variable

If you have a variable on each side and do the same thing as earlier the left will match the value on the right.

### Try Creating 2 variables and assign one to the other and see what happens

Try creating 2 variables,

a = 1

b = 2

Then assign b to a

### Call back both variables to see what each variable is equal to

You can call back more than one variable by seperating them with commas on the same line

a,b

### Multiple Assignments

Variables can be assigned all on the same line with commas as seperators with numbers in respective order.

An example is below

```python
variable_1, variable_2, variable_3 = 10,55,2.55
```

```python
#Multiple variables  can be called this way as well.
#It can be a nice way to organize and cleaen code up for readability
variable_1, variable_2, variable_3
```

### Final Numbers Lesson

Some things early python programmers run into is the difference of number types

```python
integer_variable = 10
floatingpoint_variable = 10.00000015
integer_variable,floatingpoint_variable
```

_result:_
```
(10, 10.00000015)
```

```python
type(integer_variable)
```

_result:_
```
int
```

```python
type(floatingpoint_variable)
```

_result:_
```
float
```

### Variables will automatically assign to there simplest form that uses the least memory

```python
integer_variable = floatingpoint_variable
floatingpoint_variable = 10
integer_variable,floatingpoint_variable
```

_result:_
```
(10.00000015, 10)
```

### Variable types can automatically change as needed

```python
type(integer_variable)
```

_result:_
```
float
```

```python
type(floatingpoint_variable)
```

_result:_
```
int
```

### Notice how they changed?

Issues can sometimes arise when using functions as they sometimes expect certain data types.

That's it for the Numbers example!

### strings (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/Activities/strings.ipynb

# Variables - Strings

### Strings are just lists of characters, the same modification techniques can be applied to clean, fix and adjsut text.


These methods are helpful for text mining as well as other things invloving textual data like filenames.

# Creating strings

These methods are helpful for text mining as well as other things invloving textual data like filenames.

There are 2 Methods for creating strings.

"Double Quotations" and 'Single Quotations'

For this activity we will use double quotes.

##### First create a string below with your first name.

name = "yourname"

# Grabbing a character from the string

##### You can grab a single character by the same method you would call a value from a list

Try it below

Hint list_variable[index] is the syntax

# Splitting Strings

##### You can split strings into a list of words or sentences based on what the seperator is.


This is called by the .split("seperator") method.
Where the seperator can be any word or character.

##### If none is specified then a single space is used.

Assign a new list to the split of a string. Try creating a sentence below and splitting it into a list.

###### Example

sentence = "Hello my name is Tanner"

list_of_words = sentence.split()

#### Call the first word in the list like you would with a list

Hint variable[index] is the syntax

#### Many other methods exist for string manipulation

Strings can be made into all upper case, lower case, can be re-organized and etc with a variety of commands like the split one.
