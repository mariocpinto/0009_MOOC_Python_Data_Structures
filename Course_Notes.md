## Python Data Structures: Course Notes

These notes are intended to be a high level overview / quick refresher of the contents of the Coursera course 
'[Python Data Structures](https://www.coursera.org/learn/python-data/)'.
This MOOC is the second of the four courses in the '[Python for Everybody Specialization](https://www.coursera.org/specializations/python)'. The accompanying open book to this course is [Python for Informatics](http://pythonlearn.com/) (parts of which have been derived from the book [How to Think Like a Computer Scientist: Learning with Python](http://www.greenteapress.com/thinkpython/thinkCSpy/)).

#### Week 1: Introduction & Strings

These are the topics covered in week 1:

![Week 1 content of 'Python Data Structures' MOOC](https://github.com/mariocpinto/0009_Python_Data_Structures/blob/master/Images/Python_Data_Structures_Week_1_Content.png)

Week 1 introduces the content of the course and the operational details. The 'Python for Informatics' book that this course follows can be found in html format [here](http://www.pythonlearn.com/html-270/).

In addition, the following topics are covered:
* Introduction to strings.
* Concatinating strings using `+`.
* Indexing into strings using `string[x]`.
* Determining the length of a string using `len()`.
* Accessing sub-strings (slicing strings) using `string[x:y]` - this will return the substring beginning at index x, upto - but not including - index y. Note that the index starts from 0. If you leave out x/y it represents the beginning/end of the string.
* Using `in` as an operator e.g. `'an' in 'banana'` returns `True`.
* Using `==`, `<` and `>` with strings.
* Python string methods. A list of methods can can be accessed using the `dir()` command and are documented [here](https://docs.python.org/2/library/stdtypes.html#string-methods).
* Specific examples of string methods - `lower()`, `upper()`, `find(string_to_find)`, `replace(replace_this,with_this)`, `strip()`, `startswith(starting_string)`.
* An example of parsing text.

#### Week 2: Installing & Using Python

These are the topics covered in week 2:

![Week 2 content of 'Python Data Structures' MOOC](https://github.com/mariocpinto/0009_Python_Data_Structures/blob/master/Images/Python_Data_Structures_Week_2_Content.png)

This week focusses on getting Python installed and is identical to week 2 of the '[Introduction to Python](https://github.com/mariocpinto/0008_MOOC_Getting_Started_with_Python)' course (and thus can be skipped).

#### Week 3: Files

These are the topics covered in week 3:

![Week 3 content of 'Python Data Structures' MOOC](***)

Specifically, the following topics are covered:
* Built in functions - a list can be found [here](https://docs.python.org/3.5/library/functions.html).
* Opening a file with the `open(filename,mode)` function. This function returns a file handle. Common modes are `r` or `w`.
* The newline character `\n`.
* `for var in file_handle` gives one access to the files contents one line at a time.
* Counting the lines in a file.
* Reading the whole file using `filename.read()`.
* Searching through a file.
* Reading a file name and dealing with bad files.

#### Week 4: Lists

These are the topics covered in week 4:

![Week 4 content of 'Python Data Structures' MOOC](***)

Specifically, the following topics are covered:
* Strings are immutable (elements cannot be changed), but lists are mutable.
* Creating an empth list with `list()` or `[]`.
* Obtaining the number of elements in a list using `len()`.
* Creating a list using `range(n)` - creates the list `[0,1,2,...,n-1]`.
* Concatinating lists using `+`.
* Slicing lists using `list_name[i:j]`.
* List methods - documentation can be found [here](https://docs.python.org/3.5/tutorial/datastructures.html) e.g. `append()`, `sort()`, etc.
* Functions operating on lists: `len(list_name)`, `min(list_name)`, `max(list_name)`, `sum(list_name)`.
* Converting a string to a list with one element for every word using `string_name.split(delimiter)` method.

#### Week 5: Dictionaries

These are the topics covered in week 5:

![Week 5 content of 'Python Data Structures' MOOC](***)

Specifically, the following topics are covered:
* Dictionary: a set of key/value pairs.
* Creating an empty dictionary with `dict()` or `{}`.
* Adding elements to a dictionary using `dictionary_name[key] = value`.
* The `get` method for dictionaries: `dictionary_name.get(key, default)` will return
the value corresponding to key if it exisits, else return default.
* Getting a list of the key values using the `list(dictionary_name)` function.
* Alternately you can use `dictionary_name.keys()` and `dictionary_name.values()` to get a list of keys and values.
* You can also use `dictionary_name.items()` to get two iteration variables on loops.


#### Week 6: Tuples

These are the topics covered in week 6:

![Week 6 content of 'Python Data Structures' MOOC](***)

Specifically, the following topics are covered:
* Initiating an empty tuple with `tuple()`or `()`.
* Defining the elements of a tuple with round brackets e.g. `(1, 2, 3)`.
* Tuples are immutable.
* You cannot sort, append, reverse a tuple.
* Tuples are efficient and so can be the preferred choice for non-changing lists.
* Assigning multiple variables e.g. `a, b, c = (1, 2, 3)`.
* Tuples are comparable. Comparison is performed on the first unequal element pair.
* Sorting items in a dictionary by keys: `tuple_list = dictionary.items(); tuple_list.sort()`.
* The `sorted()` function that can be used to sort a sequence.
* Sorting items in a list by values: First create a list of tuples, with each tuple representing a (_value, key_) pair and then sort the list.

#### Week 7: Graduation

These are the topics covered in week 7:

![Week 7 content of 'Python Data Structures' MOOC](https://github.com/mariocpinto/0009_Python_Data_Structures/blob/master/Images/Python_Data_Structures_Week_7_Content.png)

This week features a really sweet MOOC graduation ceremony video!

#### Concluding Remarks:
This is another good courses in the [Python for Everybody Specialization](https://www.coursera.org/specializations/python). While the first course in the specialization focuses on procedural programming, this one focuses on data structures. While a bit more demanding than the first course, this course is still light in terms of time required to complete the course.
