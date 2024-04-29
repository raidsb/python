# python

## styling documentation (python enhancement proposal) 
https://peps.python.org/pep-0008/ 

## resources 
https://realpython.com/ 
https://blog.finxter.com/ 
https://www.datacamp.com/cheat-sheet
https://www.geeksforgeeks.org/ - https://www.geeksforgeeks.org/python-cheat-sheet/ 

## Concepts:
### mutable vs immutable
refers to whther the state of an object can be changed after they are created or not. 

#### mutable
* mostly the memory for mutable objects will be the same but the state is not.
* Changes to the object affect the same memory location
* examples of mutable objects are lists, Dictionary, sets and user-defined objects.

#### immutable 
* state cannot be modified after they are created.
* Any operation that appears to modify an immutable object actually creates a new object with the modified state.
* Examples of immutable objects in Python include integers, floats, strings, tuples, and frozensets.

### type conversion/casting
Type conversion and casting are related concepts in programming but can have different meanings depending on the context and the programming language:
* Type Conversion (implicit change of type): It refers to changing the data type of a variable to another compatible type. In many programming languages, implicit type conversion (also known as type coercion) occurs automatically when performing operations between different types. For example, converting an integer to a floating-point number during arithmetic operations.
* Casting (explicit change of type): Casting is a specific form of type conversion where a programmer explicitly converts a variable from one data type to another. It's a way to inform the compiler to treat a variable as a different type temporarily. In languages like C or C++, casting can be performed using specific syntax such as (type) variable (C-style cast) or static_cast<type>(variable) (C++ style cast).

While casting is a form of type conversion, not all type conversions involve casting. Some conversions occur implicitly by the language itself, while casting explicitly instructs the compiler to perform the conversion.

```
# examples 
str(int_var)   # convert int to string
float(str_var) # convert str to float
```

## importing libraries
### [1] importing multiple libraries
can write the importing statements this way:

```
from library import lib1, lib2 
```
or this way:
```
from library import (lib1, lib2) # the parentheses are used for grouping for better readiblity but optional.
```
## variables
A variable is used to store data that will be used by the program. 
The equal sign = is used to assign a value to a variable.

``` 
# Can assign several variable separated with commas
x, y = True, False
```

## data types
primitive data 
integer. size on most platforms is 32bit. on python3, the size will grow as needed.
float.   size on most platforms is 64bits (called the double-precision)
string
boolean

built-in non-primitive data types
list      , allows duplicates       , mutable  , ordered
Tuple     , allows duplicates       , immutable, ordered
set       , doesn't allow duplicates, immutable, not orderded  
Dictionary, doesn't allow duplicates, mutable  , orderded only for python >= 3.7

### checking the type of an object

```
a = 10
print(type(a)) # will print "int"

# checking the type of numbers example
type(1)   # int 
type(-10) # int
type(0)   # int
type(0.0) # float
type(2.2) # float
type(4E2) # float - 4*10 to the power of 2
```

### primitive datatype - integer
In Python, the size of an integer depends on the platform and the version of Python being used. However, in most implementations:
For Python 2.x, typically 32 bits, allowing values from -2,147,483,648 to 2,147,483,647 (inclusive).
For Python 3.x, integers are dynamically allocated and can grow to accommodate arbitrarily large numbers limited only by available memory.

so there is only one type in python to house whole integer numbers. 
In Python 2, there were two distinct integer types: int and long. However, in Python 3, these two types were unified, and the long type was removed. Now, all integers in Python 3 are of type int, and they automatically switch to arbitrary-precision representation when they exceed the platform's limit for fixed-size integers.

#### writing integer values using _
```
a = 123_333_444 # integer numbers can be written 123_333_444 this is same as 123333444. this to make it easier to read
```

#### convert int to bin '{0:08b}'.format(6) 
```
{} places a variable into a string
0 takes the variable at argument position 0
: adds formatting options for this variable (otherwise it would represent decimal 6)
08 formats the number to eight digits zero-padded on the left
b converts the number to its binary representation
```

### primitive datatypes - float
* same as integer, can be written as 123_333.34 the _ to make it easier to read

### primitive datatype - String
* A string is a sequence of characters (letters, numbers, whitespace or punctuation) enclosed by quotation marks single or double. 
If a string has to be broken into multiple lines, the backslash character \ can be used to indicate that the string continues on the next line.
* 'str' object does not support item assignment. because strings are immutable, so can't change their characters in-place.
if you want to replace characters in the string, you need to create another string and assign characters to it. 
* single quotes vs double quotes: double quotes support string interpolation/formating with f or format function. single quote takes the string as literal

#### creating a string
```
user = "User Full Name"
game = 'Monopoly'

longer = "This string is broken up \
over multiple lines"
```

#### manipulating strings 

```
# remove last n characters from a string
my_str = my_str[:-1] # -1 for one char , -n for n characters

# convert int to bin 
'{0:08b}'.format(6) # this will format the int number 6 to bin and padding with 0s in 8 positions
# if this doesn't work, use f'{6:08b}'
# explaination:
# {} places a variable into a string
# 0 takes the variable at argument position 0
# : adds formatting options for this variable (otherwise it would represent decimal 6)
# 0 the character used for padding
# 8 formats the number to eight digits zero-padded on the left
# b converts the number to its binary representation
# so no padding: f'{6:b}'

# convert bin string to int 
value = int(bString, 2)

#Palindrome check
word = 'reviver'
p = bool(word.find(word[::-1]) + 1)
print(p) # True
```

#### Indexing and Slicing
```
s = "The youngest pope was 11 years old"
name = 'Andrei Neagoie'

# indexing. indexing starts from 0
print(s[0]) # 'T'
print(s[1:3]) # 'he'
print(s[-3:-1]) # 'ol'
print(s[-3:]) # 'old'
name[4]     # e

# slicing
name[:]     # the whole string "Andrei Neagoie"
name[1:]    # ndrei Neagoie
name[:1]    # A
name[-1]    # e
name[::1]   # Andrei Neagoie
name[::-1]  # eiogaeN ierdnA
name[0:10:2]# Ade e
# : is called slicing and has the format [ start : end : step ]. the end is exclusive, means the end index value will not be included in the resulting string
```

#### String Formatting
```
name1 = 'Andrei'
name2 = 'Sunny'
print(f'Hello there {name1} and {name2}')       # Hello there Andrei and Sunny - Newer way to do things as of python 3.6
print('Hello there {} and {}'.format(name1, name2))# Hello there Andrei and Sunny
print('Hello there %s and %s' %(name1, name2))  # Hello there Andrei and Sunny --> you can also use %d, %f, %r for integers, floats, string representations of objects respectively

## use f-string to make a string with different data types variables inside 
int_var = 0
float_var = 2.3
bool_var = True

str_var = f"this has different types {int_var} and {float_var} and {bool_var}"
```

#### Most Important String Methods
```
y = " This is lazy\t\n "
print(','.join(["F", "B", "I"]))      # 'F,B,I'
print(len("Rumpelstiltskin"))         # String length: 15
print("ear" in "earth")               # Contains: True
start, end = 1, 3
'  I am alone '.strip()               # 'I am alone' --> Strips all whitespace characters from both ends. returns a copy not stripping in place
'On an island'.strip('d')             # 'On an islan' --> # Strips all passed characters from both ends.
'but life is good!'.split()           # ['but', 'life', 'is', 'good!']
x = s.split() # creates string array of words
print(x[-3] + " " + x[-1] + " " + x[2] + "s") # '11 old popes'
'Help me'.replace('me', 'you')        # 'Help you' --> Replaces first with second param. # RETURNS A COPY, DOESN'T REPLACE IN PLACE
'Need to make fire'.startswith('Need')# True
'and cook rice'.endswith('rice')      # True
'bye bye'.index('e')                  # 2
'still there?'.upper()                # STILL THERE?
'HELLO?!'.lower()                     # hello?!
c.islower()                           # checks if is lower
'ok, I am done.'.capitalize()         # 'Ok, I am done.'
'oh hi there'.find('i')               # 4 --> returns the starting index position of the first occurrence
'oh hi there'.count('e')              # 2
string.count('char or substring', start, end) # count how many times a char appears in a string
x = txt.isalpha()                     # checks if all alpha returns bool
chr(ascii number) # returns the char for the ascii number 
ord(char)         # returns the ordinal value of a char
x = list(string_val) # convert string to list 

## string concatenation is done by using +
first = "Hello "
second = "World"
result = first + second
long_result = first + second + "!"
```

#### converting string to numbers. # input() always returns string
```
age = input("How old are you?")
age = int(age)
pi = input("What is the value of pi?")
pi = float(pi)
```

### primitive datatype - Bool 

```
x, y = True, False
print(x and not y) # True
print(not x and y or x) # True

if None or 0 or 0.0 or '' or [] or {} or set():
 # None, 0, 0.0, empty strings, or empty
 # container types are evaluated to False
 print("Dead code") # Not reached
 
# all of the below evaluate to False. Everything else will evaluate to True in Python.
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))
```

### built-in non-primitive datatype - Dictionary

```
# get list of keys
keysList = list(mydict.keys())

# check if key exists in keys
if key_to_check in my_dict.keys():
```

### built-in non-primitive datatype - Lists
Unlike strings, lists are mutable sequences in python

#### adding to the List
```
my_list = [1, 2, '3', True]
new_list = my_list * 2                # [1, 2, '3', True, 1, 2, '3', True] does not mutate the original list, it creates a new one.
my_list + [100]            # [1, 2, '3', True, 100] --> doesn't mutate original list, creates new one
my_list.append(100)        # None --> Mutates original list to [1, 2, '3', True, 100]          # Or: <list> += [<el>]
# my_list.extend(<iterable>) # so extend can be used to extend the original list with list, string, tuple, set
my_list.extend([100, 200]) # None --> Mutates original list to [1, 2, '3', True, 100, 200] - extend with list
my_list.extend("str")      # None --> Mutates original list to [1, 2. '3', True, 's', 't', 'r'] - extend with string 
my_list.extend(("tup1", "tup2")) # None --> Mutates original list to [1, 2, '3', True, "tup1", "tup2"] - extend with tuple
my_list.extend({3, 'False', 6})  # None --> Mutates original list to [1, 2, '3', True, 3, 'False', 6]
my_list.insert(2, '!!!')   # None -->  [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest to the right.

' '.join(['Hello','There'])# 'Hello There' --> Joins elements using string as separator.
```

#### list copying
```
# Copy a List
basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy() # this is a shallow copy. it creates a new object but the nested objects will be copied as references. changes in the copy is also change in the original
new_basket2 = basket[:]

## Shallow copy example.
import copy
# Original list with nested list
original_list = [[1, 2, 3], [4, 5, 6]]

# Shallow copy of the original list
shallow_copied_list = copy.copy(original_list)

# Modify the nested list in the shallow copied list
shallow_copied_list[0][0] = 100

# Both the original and shallow copied lists are affected
print(original_list)          # Output: [[100, 2, 3], [4, 5, 6]]
print(shallow_copied_list)    # Output: [[100, 2, 3], [4, 5, 6]]

## deep copy create entirely new object. so a change in the copy will not not change in the original
import copy
# Original list with nested list
original_list = [[1, 2, 3], [4, 5, 6]]

# Deep copy of the original list
deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list in the deep copied list
deep_copied_list[0][0] = 100

# Only the deep copied list is affected
print(original_list)        # Output: [[1, 2, 3], [4, 5, 6]]
print(deep_copied_list)     # Output: [[100, 2, 3], [4, 5, 6]]


```

#### list indexing and slicing
```
my_list = [1, 2, '3', True]# We assume this list won't mutate for each example below
# indexing. indexing starts with zero
my_list.index('3')         # 2 returns the index of the first occurance
my_list[3]                 # True
my_list[-1]                # True - top of the stack if list used as a stack

# slicing. the end in slicing is exclusive. slicing returns a copy of the sliced list
my_list[1:]                # [2, '3', True]
my_list[:1]                # [1]
my_list[::1]               # [1, 2, '3', True]
my_list[::-1]              # [True, '3', 2, 1] # reversing
my_list[0:3:2]             # [1, '3']

# get sum of a slice of a list
s = sum(test_list[x: x + 3])

# : is called slicing and has the format [ start : end : step ]
```

#### list functions and methods 
```
x.count()   # Count the number of element 2 in the list
min([1,2,3,4,5])# 1
max([1,2,3,4,5])# 5
sum([1,2,3,4,5])# 15
```

#### ordering list
```
len(my_list)               # 4
my_list.count(2)           # 1 --> count how many times 2 appears
sorted(x)                  # Return a sorted copy of the list e.g., [1,2,3]
sorted([1,2,5,3])          # [1, 2, 3, 5] --> new list created
x.sort()                   # Sorts the list in place (replaces x)
[1,2,5,3].sort()           # None --> Mutates list to [1, 2, 3, 5]
[1,2,5,3].sort(reverse=True) # None --> Mutates list to [5, 3, 2, 1]
reversed(x)                  # Reverse the order of elements in x e.g., [2,3,1]. it returns an iterator not a list. so need to convert the iterator to list.
							 # it is made this way because it is more memory-efficient and most operations on reverse requires just iterating the elements in reverse order, not a list of reversed elements.
list(reversed([1,2,5,3]))    # [3, 5, 2, 1] --> reversed() returns an iterator so you have to convert to list
x.reverse()                  # Reverse the list in place
[1,2,5,3].reverse()          # None --> Mutates list to [3, 5, 2, 1]
```

#### removing from List
```
# Remove from List
# pop removes by index and returns the removed value.
[1,2,3].pop()    # removes 3 and returns the removed value. good for stack --> mutates original list, default index in the pop method is -1 (the last item)
[1,2,3].pop(1)   # removes 2 and returns the removed value. --> mutates original list

# remove removes by value. the first occurance will be removed.
[1,2,3].remove(2)# None --> [1,3] Removes first occurrence of item or raises ValueError.

[1,2,3].clear()  # None --> mutates original list and removes all items: []

# del is similar to pop but it doesn't return anything.
del [1,2,3][0] # returns nothing. just deletes.
```

#### List Comprehensions
```
# new_list[<action> for <item> in <iterator> if <some condition>]
a = [i for i in 'hello']                  # ['h', 'e', 'l', 'l', '0']
b = [i*2 for i in [1,2,3]]                # [2, 4, 6]
c = [i for i in range(0,10) if i % 2 == 0]# [0, 2, 4, 6, 8]
```

#### Functions
```
# converting string to list of chars
list_of_chars = list('Helloooo')                                   # ['H', 'e', 'l', 'l', 'o', 'o', 'o', 'o']

# getting the sum of a list.
sum_of_elements = sum([1,2,3,4,5])                                 # 15
```

#### Useful operations - check if a member exists in a list
```
1 in [1,2,5,3]  # True
```

#### Useful operations - Get First and Last element of a list
```
mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = mList # *x is called extended unpacking. which will unpack the list and assign to x. 
print(first) # 63
print(x)     # [21, 30, 14, 35, 26, 77, 18, 49]
print(last)  # 10

# another example of extended unpacking
list = [21, 30, 14, 35, 26, 77, 18, 49]
first, *x, last = list
print(first) # 21
print(x)     # [30, 14, 35, 26, 77, 18]
print(last)  # 49
*x, last = list
print(x)     # [21, 30, 14, 35, 26, 77, 18]
print(last)  49
```

#### Useful operations - Matrix
```
matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix[2][0] # 7 --> Grab first first of the third item in the matrix object

# Looping through a matrix by rows:
mx = [[1,2,3],[4,5,6]]
for row in range(len(mx)):
	for col in range(len(mx[0])):
		print(mx[row][col]) # 1 2 3 4 5 6

# Transform into a list:
[mx[row][col] for row in range(len(mx)) for col in range(len(mx[0]))] # [1,2,3,4,5,6]

# Combine columns with zip and *:
[x for x in zip(*mx)] # returns [(1, 4), (2, 5), (3, 6)]
```

#### Useful operations - Looping through a matrix by rows
```
mx = [[1,2,3],[4,5,6]]
for row in range(len(mx)):
	for col in range(len(mx[0])):
		print(mx[row][col]) # 1 2 3 4 5 6

# Transform into a list:
[mx[row][col] for row in range(len(mx)) for col in range(len(mx[0]))] # [1,2,3,4,5,6]

# Combine columns with zip and *:
[x for x in zip(*mx)] # [(1, 3), (2, 4)]
mx = [(1, 4), (2, 5), (3, 6)]

result1 = [x for x in zip(*mx)]  # Transpose mx. here we have two iterables to pair between them. and pairs each element in unpacked element with corresponding element from the other unpacked.
result2 = [x for x in zip(mx)]   # Pair up elements from mx. we have only one iterable, the list itself, so nothing to pair with it.

print(result1)  # Output: [(1, 2, 3), (4, 5, 6)]
print(result2)  # Output: [((1, 4),), ((2, 5),), ((3, 6),)]
```

#### Useful operations - Using zip to pair corresponding elements in multiple iterables.
```
### using zip to pair and compute sum per column
# zip function creates pairs of corresponding elements in a group of lists. 
list_pair = [sum(pair) for pair in zip([1, 2, 3], [4, 5, 6], [7, 8, 9])]   # if lists are not of the same length, the shortest length will be used to create the pairs
list_pair = [sum(pair) for pair in zip([[1, 2, 3], [4, 5, 6], [7, 8, 9])]] # --> will give error. because one iterable, nothing to pair and calculate the sum with. works the same.

# getting the sum of each colum using zip. zip creates pairs of corresponding elements in the list
element_sum = [sum(pair) for pair in zip([1,2,3],[4,5,6])]         # [5, 7, 9]
```

#### Useful operations - sorting per key 
In sorted(iterable, key=function) key is used specify a function that will be called on each element of the iterable being sorted. The return value of this function will be used to determine the sort order of the elements.
the function takes only one argument which is the element from the iterable.

several forms of functions can be used in key. function, method in a class, build-in function, partial function, lambda
```
### sorting per key
## key is a lambda  function.

# example1 - sorting a list using the second character of each string
sorted_by_second = sorted(['hi','you','man'], key=lambda el: el[1])# ['man', 'hi', 'you']

# example2 - sorting a list of dicts according to the name
sorted_by_key = sorted([
                       {'name': 'Bina', 'age': 30},
                       {'name':'Andy', 'age': 18},
                       {'name': 'Zoey', 'age': 55}],
                       key=lambda el: (el['name']))# [{'name': 'Andy', 'age': 18}, {'name': 'Bina', 'age': 30}, {'name': 'Zoey', 'age': 55}]

list_dict = [
    {"name": "Ahmad", "score": 10},
    {"name": "samar", "score": 4},
    {"name": "sameera", "score": 7},
    {"name": "ayham", "score": 8},
    {"name": "omar", "score": 9},
]

## below are different ways of using the key function, but the lambda is the most common
# way 1: sorting with key function is lambda
new_list_1 = sorted(list_dict, key=lambda x: x["name"])
print(new_list_1) # [{'name': 'Ahmad', 'score': 10}, {'name': 'ayham', 'score': 8}, {'name': 'omar', 'score': 9}, {'name': 'samar', 'score': 4}, {'name': 'sameera', 'score': 7}]

# way 2: sorting with a function
def sort_by_name(x):
    return x["name"]

new_list_2 = sorted(list_dict, key=sort_by_name)
print(new_list_2)

# way 3: sorting with a built-in function
new_list_3 = sorted(list_dict, key=len)
print(new_list_3)

# way 4: sorting with a class method
class Person:
    def sort_by_score(self, person):
        return person['score']

person_ins = Person()
sorted_list_4 = sorted(list_dict, key=person_ins.sort_by_score)
print(sorted_list_4)

# way 5: sorting with a partial function
from functools import partial

def subtract(a, b):
    return a - b
number = [1, 2, 3, 4, 5]
subtract_by_5 = partial(subtract, b=5)
sorted_by_difference = sorted(numbers, key=subtract_by_5)
```

#### Useful operations - Read line of a file into a list
```
with open("myfile.txt") as f:
  lines = [line.strip() for line in f]
```


[2.1] using itertools slicing 
itertools.islice(test_list, i, i + 3) # check what does this return 



[4] map function is used to apply a function on each element in a list. 
for example: 
list(map(str.capitalize, stringList)) # the map will apply the function str.capitalize on each element in stringList 
then list is to convert this to a list # in the same list stringList? 

[5] Python lists are mutable objects and here:

	plot_data = [[]] * len(positions) 
	you are repeating the same list len(positions) times.

	>>> plot_data = [[]] * 3
	>>> plot_data
	[[], [], []]
	>>> plot_data[0].append(1)
	>>> plot_data
	[[1], [1], [1]]
	>>> 
	Each list in your list is a reference to the same object. You modify one, you see the modification in all of them.

	If you want different lists, you can do this way:

	plot_data = [[] for _ in positions]
	for example:

	>>> pd = [[] for _ in range(3)]
	>>> pd
	[[], [], []]
	>>> pd[0].append(1)
	>>> pd
	[[1], [], []]

[6] appending a whole list to another
	[Example 1]: Append list into another list
	languages1.append(languages2)

	[Example 2]: Append multiple lists into another list
	languages1.append([languages2,languages3])

	[Example 3]: Append list elements to list
	languages1.extend(languages2)

	[Example 4]: Append List Elements
	## Using insert()
	for x in languages2:
		languages1.insert(len(languages1),x)

[7] reverse a list
arr[::-1] means the arr reversed # should return a copy of the reverse
or
list.reverse() # reverse a list in place

[8] deleting at index/s
	method1: Remove an item by index and get its value using pop() 
	test_list = [5, 6, 3, 7, 8, 1, 2, 10]
	test_list.pop(1) # try pop returns the poped value

	method2: Remove items by index or slice using del 
	test_list = [5, 6, 3, 7, 8, 1, 2, 10, 5]
	indices=[3,7]
	 
	for i in sorted(indices, reverse=True):
		del test_list[i]

	method3: Remove items at a specific index using enumerate() + loop 
		# Python3 code to demonstrate working of 
		# Remove elements at Indices in List
		# Using loop
		 
		# initializing list
		test_list = [5, 6, 3, 7, 8, 1, 2, 10]
		 
		# printing original list
		print("The original list is : " + str(test_list))
		 
		# initializing idx list 
		idx_list = [2, 4, 5, 7]
		 
		res = []
		for idx, ele in enumerate(test_list): 
			 
			# checking if element not present in index list
			if idx not in idx_list:
				res.append(ele)
		 
		# printing results
		print("Filtered List after removal : " + str(res))

	method4: Remove items at a specific index using enumerate() + list comprehension
		# Python3 code to demonstrate working of
		# Remove elements at Indices in List
		# Using enumerate() + list comprehension
		 
		# initializing list
		test_list = [5, 6, 3, 7, 8, 1, 2, 10]
		 
		# printing original list
		print("The original list is : " + str(test_list))
		 
		# initializing idx list
		idx_list = [2, 4, 5, 7]
		 
		# one-liner to test for element in index list
		res = [ele for idx, ele in enumerate(test_list) if idx not in idx_list]
		 
		# printing results
		print("Filtered List after removal : " + str(res))

[9] clearing all elements in a list:
thislist.clear()

[10] remove all occurances of element # using list comprehension
test_list = [1, 3, 4, 6, 5, 1]  
ele=1 
x=[j for i,j in enumerate(test_list) if j!=ele]  
print(x)

[11] counting elements in a list
list.count(element)

[13] adding item to end of list:
ranked.append(score) # this adds in place. so returns None and the original list is modified.

[14] converting list to set
set1 = set(ranked) # returns a newly created set 

[15] converting set to list
list1 = list(set(ranked)) # returns a newly created list

[16] sorted(list)  returns a copy of the list while list.sort()/list.sort(reverse = True) sorts in place
[17] reversed(list)returns a copy of the list while list.reverse() reverses in place

[18] top of the stack: list[-1]

## built-in non-primitive datatype - Dictionary
```
my_dict = {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False}
my_dict['name']                      # Andrei Neagoie
len(my_dict)                         # 3
list(my_dict.keys())                 # ['name', 'age', 'magic_power'] - it returns a dynamic view object. it shows the changes in real-time
list(my_dict.values())               # ['Andrei Neagoie', 30, False]
list(my_dict.items())                # [('name', 'Andrei Neagoie'), ('age', 30), ('magic_power', False)]
my_dict['favourite_snack'] = 'Grapes'# {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes'}
my_dict.get('age')                   # 30 --> Returns None if key does not exist.
my_dict.get('ages', 0 )              # 0 --> Returns default (2nd param) if key is not found

#Remove key
del my_dict['name']       # removes the key and corresponding value
my_dict.pop('name', None) # removes the key and corresponding value and return the popped key-value. if not exists returns None

# Updating Dictionary can be done in two using, using the update method and direct assin. 
# Use update when you want to add or update multiple values. or depends on your preference.
my_dict.update({'cool': True})                     # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
my_dict.update({'cool': True, 'hobby': 'reading'}) # update can be used to update multiple entries
my_dict['cool'] = True. # using the assign

# mergins dictionaries. will merge and create a new dictionary. if same key, the last key value will be used. original ones will not change
merged_dict = {**my_dict, **{'cool': True} }                           # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
new_dict = dict([['name','Andrei'],['age',32],['magic_power',False]])  # Creates a dict from collection of key-value pairs.
new_dict = dict(zip(['name','age','magic_power'],['Andrei',32, False]))# Creates a dict from two collections.
new_dict = my_dict.pop('favourite_snack')                              # Removes item from dictionary.

# dictionary comprehension
# Dictionary Comprehension
comp_dict = {key: value for key, value in new_dict.items() if key == 'age' or key == 'name'} # {'name': 'Andrei', 'age': 32} --> Filter dict by keys

# iterating dictionary with items
for k,v in my_dict.items(): # Dictionary Unpacking
    print(k) # 'a', 'b', 'c'
    print(v) # 1, 2, 3
```

## built-in non-primitive datatypes - tuples
```
my_tuple = ('apple','grapes','mango', 'grapes') # tuples allow duplicates
apple, grapes, mango, grapes = my_tuple# Tuple unpacking
apple, *fruits, grapes = my_tuple      # extended unpacking
len(my_tuple)                          # 4
my_tuple[2]                            # mango
my_tuple[-1]                           # 'grapes'
```

### Tuples are not mutable
```
# Immutability
my_tuple[1] = 'donuts'  # TypeError
my_tuple.append('candy')# AttributeError
```

### Methods
```
# Methods
my_tuple.index('grapes') # 1
my_tuple.count('grapes') # 2
```

### Zip
```
list(zip([1,2,3], [4,5,6])) # [(1, 4), (2, 5), (3, 6)]

# unzip
z = [(1, 2), (3, 4), (5, 6), (7, 8)] # Some output of zip() function
unzip = lambda z: list(zip(*z))
unzip(z) # --> returns the original
```

## built-in non-primitive datatype - sets
Creating and adding
```
my_set = set()
my_set.add(1)  # {1}
my_set.add(100)# {1, 100}
my_set.add(100)# {1, 100} --> no duplicates!
```

Deleting elements
```
new_list = [1,2,3,3,3,4,4,5,6,1]
set(new_list)           # {1, 2, 3, 4, 5, 6}

my_set.remove(100)      # {1} --> Raises KeyError if element not found
my_set.discard(100)     # {1} --> removes but Doesn't raise an error if element not found
my_set.clear()          # {}
new_set = {1,2,3}.copy()# {1,2,3}
```

sets operations 
```
set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)               # {1,2,3,4,5}
set4 = set1.intersection(set2)        # {3}
set5 = set1.difference(set2)          # {1, 2}
set6 = set1.symmetric_difference(set2)# {1, 2, 4, 5}
set1.issubset(set2)                   # False
set1.issuperset(set2)                 # False
set1.isdisjoint(set2)                 # False --> return True if two sets have a null intersection.
```
Frozen set
```
# Frozenset
# hashable --> it can be used as a key in a dictionary or as an element in a set.
<frozenset> = frozenset(<collection>)
```

## Mathematical operations
### [1] list of arithmetic operations
+, - , / , *, ** for exponent operation, // for full number div returns int not float, % for mod division
PEMDAS for precedency. if two operations at the same level, the one on the most left has higher precedency

```
# Arithmetic
10 + 3  # 13
10 - 3  # 7
10 * 3  # 30
10 ** 3 # 1000
10 / 3  # 3.3333333333333335
10 // 3 # 3 --> floor division - no decimals and returns an int
10 % 3  # 1 --> modulo operator - return the reminder. Good for deciding if number is even or odd

# exploring types returned by aritmetic operations
a = 3
b = 0.5
c = 2

print('a + b', type(a + b)) 
print('a + c', type(a + c))
print('a * b', type(a * b))
print('a * c', type(a * c))
print('a - b', type(a - b))
print('a - c', type(a - c))
print('a / b', type(a / b))
print('a / c', type(a / c))
print('a // b', type(a // b))
print('a // c', type(a // c))
print('a % b', type(a % b))
print('a % c', type(a % c)) 

# outputs
"""
a + b <class 'float'>
a + c <class 'int'>
a * b <class 'float'>
a * c <class 'int'>
a - b <class 'float'>
a - c <class 'int'>
a / b <class 'float'>
a / c <class 'float'>
a // b <class 'float'>
a // c <class 'int'>
a % b <class 'float'>
a % c <class 'int'>
"""

# Mathematical functions
pow(5, 2)           # 25 --> like doing 5**2
abs(-50)            # 50
round(5.46)         # 5
round(5.468, 2)     # 5.47 --> round to nth digit
floor(float number) # to truncate float numbers 
bin(512)            # '0b1000000000' -->  binary format
hex(512)            # '0x200' --> hexadecimal format

# types returned by mathematical functions determined by the input arguments
print('pow(5, 2)', type(pow(5, 2)))      
print('abs(-50)', type(abs(-50)))        
print('round(5.46)', type(round(5.46)))         # returns int because the value is int
print('round(5.468, 2)', type(round(5.468, 2))) # returns float because the value is float
print('bin(512)', type(bin(512))) # returns string 
print('hex(512)', type(hex(512))) # returns string
math.log2(2.7183)

# outputs
pow(5, 2) <class 'int'>
abs(-50) <class 'int'>
round(5.46) <class 'int'>
round(5.468, 2) <class 'float'>
bin(512) <class 'str'>
hex(512) <class 'str'>
```

### num1 ^ num2 is the xor operation.  ^ is the xor operator

### add a value to an existing variable and assign the new value back to the same variable. 

```
# Plus-Equal Operator

counter = 0
counter += 10

# This is equivalent to
counter = 0
counter = counter + 10

# The operator will also perform string concatenation
message = "Part 1 of message "
message += "Part 2 of message"
```

## Input
what does it do? 
use input(prompt) to get input from the user in the console. the value passed from the user will replace the input(prompt) code line in the python script.

```
# example: using input() inside print()
print("Hello " + input("Hi, what's your name?") ) # will execute the input first, and the value passed from the user will replace the input() call in the print function call.

# assign the input value to a variable 
name = input('') # can also assign the input value to a variable
```

the input value always returns string, so if getting a number should convert to int
```
num1 = int(input())
num2 = int(input())
print(num1 * num2)
```

Using input to let the user quit
```
# waiting until user quits
msg = ''
while msg != 'quit':
    msg = input("What should I do?")
    print(msg)
```

## Functions 

```
def raw_file_names(self) -> str:
	return "just a dummy string"
# this means a function that returns a string. it is optional in python and is meant to make it more readable
# more details about -> type: -> str: This part is a type hint, indicating that the method is expected to return a value of type str (string). Type hints are optional in Python, but they can provide information to developers and tools about the expected types of function parameters and return values.
```

## Reading csv files

```
import csv
with open(self.dataset_csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    self.data_list = [row for row in csv_reader]
```

## using ranges
```
# rule of thumb: for i in range(start, stop, step)
for i in range(n): # n is not inclusive, so this will iterate from 0 to n-1
for i in range(1, n, 2) iterate from 1 to n-1, with step is two
for i in range(4, 0, -2) iterating backward from 4 to 0 with step is two (negative is backward)
for i in revered(range(0, 4, 2)) same as above using the reversed

range(10)          # range(0, 10) --> 0 to 9
range(1,10)        # range(1, 10)
list(range(0,10,2))# [0, 2, 4, 6, 8]
```
## Enumerate
```
for i, el in enumerate('helloo'):
  print(f'{i}, {el}')
```

## Enums 
[1] define enums
from enum import Enum 

class Color(Enum):
RED = 1
GREEN = 2
BLUE = 3 

## Counter 
```
from collections import Counter
colors = ['red', 'blue', 'yellow', 'blue', 'red', 'blue']
counter = Counter(colors)# Counter({'blue': 3, 'red': 2, 'yellow': 1})
counter.most_common()[0] # ('blue', 3)
```

Links
-----
[1] libs: https://www.ubuntupit.com/best-python-libraries-and-packages-for-beginners/   

## OOP 
[1] list of oop features 
Object-oriented programming (OOP) is a programming paradigm that organizes software design around objects and their interactions. OOP provides several features and capabilities that help in designing and implementing robust, modular, and maintainable software systems. Here are the key features and capabilities of OOP:

    Class and Object:
        Class: A blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of the class will have.
        Object: An instance of a class. It represents a real-world entity and encapsulates data and behavior.

    Encapsulation:
        Encapsulation refers to the bundling of data (attributes) and methods that operate on the data into a single unit (i.e., class).
        It hides the internal state of an object and restricts direct access to it, allowing access only through well-defined interfaces (public methods).

    Inheritance:
        Inheritance is a mechanism by which a class (subclass/derived class) can inherit properties and behaviors from another class (superclass/base class).
        It promotes code reusability, as subclasses can extend or override the functionality of their superclass.

    Polymorphism:
        Polymorphism allows objects of different classes to be treated as objects of a common superclass.
        It enables a single interface to represent multiple underlying data types or forms.
        Two common forms of polymorphism are:
            Compile-time polymorphism (method overloading): Methods with the same name but different parameters in the same class.
            Run-time polymorphism (method overriding): Overriding a method in a subclass with a specific implementation.

    Abstraction:
        Abstraction involves hiding the complex implementation details of a class and exposing only the essential features (i.e., what an object does rather than how it does it).
        It allows developers to focus on high-level design without worrying about implementation details.

    Association, Aggregation, and Composition:
        Association: Represents a relationship between two or more classes where each class has its own lifecycle and there is no ownership.
        Aggregation: Represents a "has-a" relationship between classes, where one class is a part of another class.
        Composition: Represents a strong "has-a" relationship between classes, where one class owns another class and is responsible for its lifecycle.

    Message Passing:
        Objects communicate with each other by sending messages. A message typically consists of a method invocation along with any required arguments.

    Constructor and Destructor:
        Constructor: A special method called when an object of a class is created. It initializes the object's state.
        Destructor: A special method called when an object is destroyed. It performs cleanup tasks before the object is deallocated from memory.

    Access Modifiers:
        Access modifiers control the visibility and accessibility of class members (attributes and methods).
        Common access modifiers include public, private, and protected, which determine whether members can be accessed from outside the class.

    Overloading and Overriding:
        Overloading: Defining multiple methods in a class with the same name but different parameter lists.
        Overriding: Providing a new implementation for a method in a subclass that already exists in its superclass.

These features and capabilities of OOP help in designing modular, maintainable, and extensible software systems by promoting concepts such as encapsulation, inheritance, and polymorphism. By using OOP principles effectively, developers can create code that is easier to understand, modify, and extend.

## Algorithms 
[1] arrays 

[1.1] arrays problems where math operations are needed on the left vs the right of each element in the array. use a single loop to iterate over each element and make the operations left vs right, 
example "Sherlock and array" problem 

[2] the binary search
def binary_search(scores, alice_score):
    low = 0
    high = len(scores) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if scores[mid] == alice_score:
            return mid
        elif scores[mid] < alice_score:
            high = mid - 1
        else:
            low = mid + 1
    
    return low

# Example usage:
scores = [100, 90, 90, 80, 75, 60]
alice_score = 65
position = binary_search(scores, alice_score)
print("Alice's score would be at position:", position)


S[:Index] + S[Index + 1:]

-------------------------------------------------------

give an example of multi-threading in python 
ChatGPT
Sure, here's a simple example of multi-threading in Python using the threading module:

python
Copy code
import threading
import time

# Define a function that will be executed by each thread
def print_numbers():
    for i in range(5):
        print(threading.current_thread().name, ':', i)
        time.sleep(1)

# Create two threads
thread1 = threading.Thread(target=print_numbers, name='Thread 1')
thread2 = threading.Thread(target=print_numbers, name='Thread 2')

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

print('Main thread exiting')
In this example:

We import the threading module to work with threads.
We define a function print_numbers() that simply prints numbers from 0 to 4 along with the name of the current thread.
We create two thread objects, thread1 and thread2, specifying the target function (print_numbers) and giving each thread a name.
We start the threads using the start() method.
We call the join() method on each thread to wait for them to complete execution before the main thread proceeds.
Finally, we print a message indicating that the main thread is exiting.
When you run this code, you'll see that both threads execute concurrently, printing numbers in parallel, which demonstrates the basic concept of multi-threading in Python.

User
if we missed the join , what will happen?
ChatGPT
If you miss calling the join() method on a thread, the main thread will not wait for that thread to finish its execution. This means that the main thread may proceed to the end of its execution without waiting for the other threads to complete.

In the context of the example provided, if you miss calling join() on thread1 and thread2, the main thread may print "Main thread exiting" before thread1 and thread2 have finished executing. This could result in the output being printed out of order, or the program exiting before all threads have completed their work.

Here's the modified example without the join() calls:

python
Copy code
import threading
import time

def print_numbers():
    for i in range(5):
        print(threading.current_thread().name, ':', i)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers, name='Thread 1')
thread2 = threading.Thread(target=print_numbers, name='Thread 2')

thread1.start()
thread2.start()

print('Main thread exiting')
In this modified version, there's no guarantee that the output of the threads will be fully printed before the "Main thread exiting" message is printed. The behavior may vary depending on how the operating system schedules the threads for execution.

User
let say that I have a huge list of numbers and I want to make calculations on each element, where it depends on the calculations of the previous elements, is using multi-thread right here?
ChatGPT
If the calculations on each element of the list depend on the results of the previous elements, using multi-threading might not be the best approach. This is because multi-threading is most effective when tasks can be executed independently and in parallel without dependencies on each other.

In your case, since the calculations depend on the results of previous elements, there would likely be synchronization issues and potential race conditions if multiple threads were modifying shared state (e.g., global variables) to store the results of their calculations.

A more suitable approach would be to use a single thread to iterate over the list and perform the calculations sequentially. This ensures that each calculation has access to the correct previous results and avoids potential issues with concurrent access to shared data.

However, if the calculations on each element of the list are computationally intensive and can be parallelized in a way that allows each calculation to be performed independently of the others, you could consider using multiprocessing instead of multi-threading. With multiprocessing, each calculation can be performed in a separate process, allowing them to run in parallel without sharing memory and avoiding potential synchronization issues.

User
multi-threading vs multi-processing vs concurrent 
ChatGPT
Multi-threading, multi-processing, and concurrent programming are all techniques used to achieve parallelism and improve the performance of programs. However, they differ in their implementation and use cases:

Multi-threading:
Multi-threading involves running multiple threads within a single process.
Threads share the same memory space and resources of the parent process.
Typically used for I/O-bound tasks, such as network requests, file I/O, or GUI applications, where threads can wait for I/O operations without blocking other threads.
Python's threading module provides support for multi-threading.
Multi-processing:
Multi-processing involves running multiple processes, each with its own memory space, within a single or multiple CPUs.
Processes do not share memory by default, but communication between processes can be achieved using inter-process communication (IPC) mechanisms like pipes, queues, or shared memory.
Typically used for CPU-bound tasks, such as numerical computations or data processing, where multiple tasks can be performed simultaneously by leveraging multiple CPU cores.
Python's multiprocessing module provides support for multi-processing.
Concurrent Programming:
Concurrent programming involves structuring a program to execute multiple tasks concurrently, regardless of whether they are executed in parallel or not.
It focuses on managing multiple tasks and their interactions, rather than on the specific mechanisms used for parallelism.
Can be implemented using multi-threading, multi-processing, or asynchronous programming techniques.
Used to improve the responsiveness and efficiency of applications by overlapping or interleaving tasks that do not depend on each other.
In Python, concurrent programming can be achieved using libraries like asyncio for asynchronous I/O operations, or frameworks like concurrent.futures for managing concurrent execution of tasks.
In summary, multi-threading and multi-processing are specific techniques for achieving parallelism in programs, while concurrent programming is a broader concept that encompasses various approaches for managing concurrent tasks and interactions within a program. The choice between these techniques depends on the nature of the tasks being performed and the requirements of the application.

User
is concurrent term same as parallel?
ChatGPT
The terms "concurrent" and "parallel" are related but not exactly the same:

Concurrent: Concurrent programming refers to the execution of multiple tasks or processes that can start, run, and complete in overlapping time periods. In concurrent programming, tasks may not necessarily be executed simultaneously, but they can make progress independently of each other. Concurrency is about managing the execution flow of multiple tasks and dealing with potential interactions or dependencies between them.
Parallel: Parallel programming, on the other hand, involves the simultaneous execution of multiple tasks or processes on multiple computing resources (such as CPU cores or machines). In parallel programming, tasks are executed at the same time, and they may run on separate processing units or in separate processes. Parallelism is about maximizing performance by leveraging multiple computing resources to execute tasks concurrently.
In summary, concurrency deals with the structure and management of tasks, allowing them to make progress independently, while parallelism focuses on executing tasks simultaneously to achieve higher performance. While concurrent programming can involve parallel execution, not all concurrent programs are necessarily parallel, as concurrency can also be achieved through interleaving or scheduling tasks to run cooperatively.

User
is parallalism supported in python?
ChatGPT
Yes, parallelism is supported in Python through the use of the multiprocessing module, which allows you to create multiple processes that run concurrently and can leverage multiple CPU cores for parallel execution.

The multiprocessing module provides functionality for spawning processes, communicating between processes, and managing shared resources. Each process has its own memory space, which helps avoid common issues associated with multi-threading, such as the Global Interpreter Lock (GIL) in CPython.

Here's a simple example of parallelism using the multiprocessing module to calculate the square of numbers in parallel:

python
Copy code
import multiprocessing

# Function to calculate the square of a number
def square(n):
    return n * n

if __name__ == "__main__":
    # Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Map the square function to the list of numbers and calculate squares in parallel
    results = pool.map(square, numbers)

    # Close the pool to free resources
    pool.close()
    pool.join()

    # Print the results
    print("Squared numbers:", results)
In this example:

We create a pool of worker processes using multiprocessing.Pool().
We define a list of numbers for which we want to calculate squares.
We use the map() function of the pool to apply the square() function to each element of the list in parallel.
The results are collected and printed.
By using the multiprocessing module, you can achieve parallelism in Python and leverage multiple CPU cores to improve the performance of your programs, especially for CPU-bound tasks.




