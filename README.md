# python

# importing libraries
[1] can write the importing statements this way: from library import lib1, lib2 
or this way from library import (lib1, lib2) # the parentheses are used for grouping for better readiblity but optional.

# String
[1] single quotes vs double quotes: double quotes support string interpolation/formating with f or format function.
- single quote takes the string as literal

[2] using the index to get the character in a specific position 
"Hello"[0] # to get the character at position 0 of the string 
s = "Hello"
print(s[0])

[3] f-string
use f-string to make a string with different data types variables inside 
int_var = 0
float_var = 2.3
bool_var = True

str_var = f"this has different types {int_var} and {float_var} and {bool_var}" 
this is better than 
str_var = "this has different types" + str(int_var) + "and" + ...

[4] remove last n characters from a string
my_str = my_str[:-1] # -1 for one char , -n for n characters

[5] convert int to bin 
'{0:08b}'.format(6) # this will format the int number 6 to bin and padding with 0s in 8 positions
if this doesn't work, use f'{6:08b}'

explaination:
{} places a variable into a string
0 takes the variable at argument position 0
: adds formatting options for this variable (otherwise it would represent decimal 6)
0 the character used for padding
8 formats the number to eight digits zero-padded on the left
b converts the number to its binary representation

so no padding: f'{6:b}'

[5.1] convert bin string to int 
value = int(bString, 2)

[6] 'str' object does not support item assignment. because strings are immutable, so can't change their characters in-place.
if you want to replace characters in the string, you need to create another string and assign characters to it. 

[7] lower case
x = txt.lower()

[8] check if is lower 
c.islower()

[9] replace a string/char
song.replace('cold', 'hurt') # RETURNS A COPY, DOESN'T REPLACE IN PLACE

[10] get the ascii char and ord of a character
chr(ascii number) returns the char
ord(char) returns the ordinal value of a char

[11] check if alpha
x = txt.isalpha() # returns bool

[12] convert string to list
x = list(string_val)
 
[13] count how many times a char appears in a string
string.count(char or substring, start, end)

# integer
[1] integer numbers can be written 123_333_444 this is same as 123333444. this to make it easier to read

[2] convert int to bin '{0:08b}'.format(6) 
{} places a variable into a string
0 takes the variable at argument position 0
: adds formatting options for this variable (otherwise it would represent decimal 6)
08 formats the number to eight digits zero-padded on the left
b converts the number to its binary representation

# float 
[1] same as integer, can be written as 123_333.34 the _ to make it easier to read

# type() 
used to check the type of a variable: type(var) 

# type conversion/casting 
Type conversion and casting are related concepts in programming but can have different meanings depending on the context and the programming language:

Type Conversion (implicit change of type): It refers to changing the data type of a variable to another compatible type. In many programming languages, implicit type conversion (also known as type coercion) occurs automatically when performing operations between different types. For example, converting an integer to a floating-point number during arithmetic operations.

Casting (explicit change of type): Casting is a specific form of type conversion where a programmer explicitly converts a variable from one data type to another. It's a way to inform the compiler to treat a variable as a different type temporarily. In languages like C or C++, casting can be performed using specific syntax such as (type) variable (C-style cast) or static_cast<type>(variable) (C++ style cast).

While casting is a form of type conversion, not all type conversions involve casting. Some conversions occur implicitly by the language itself, while casting explicitly instructs the compiler to perform the conversion.

- convert int to string: str(int_var)
- convert str to float: float(str_var)

# Input
[1] what does it do? 
use input(prompt) to get input from the user in the console. the value passed from the user will replace the 
input(prompt) code line in the python script.

example: using input() inside print()
-------------------------------------
print("Hello " + input("Hi, what's your name?") ) # will execute the input first, and the value passed from the user will replace the input() call in the print function call.

assign the input value to a variable 
------------------------------------
can also assign the input value to a variable: name = input('')

the input value always returns string, so if getting a number should convert to int
-----------------------------------------------------------------------------------
num1 = int(input())
num2 = int(input())
print(num1 * num2)

# Mathematical operations
[1] +, - , / , *, ** for exponent operation, // for full number div returns int not float, % for mod division
PEMDAS for precedency. if two operations at the same level, the one on the most left has higher precedency

[1.1] num1 ^ num2 is the xor operation.  ^ is the xor operator

[1.2] get the log base 2 of a number 
math.log2(2.7183) 

[2] math functions 
floor(float number) to truncate float numbers 

# Functions 
def raw_file_names(self) -> str: 
this means a function that returns a string. it is optional in python and is meant to make it more readable
more details about -> type: -> str: This part is a type hint, indicating that the method is expected to return a value of type str (string). Type hints are optional in Python, but they can provide information to developers and tools about the expected types of function parameters and return values.

# Reading csv files
import csv
with open(self.dataset_csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    self.data_list = [row for row in csv_reader]

# Dictionary
[1] get list of keys
keysList = list(mydict.keys()) 

[2] check if key exists in keys
if key_to_check in my_dict.keys():

# Lists
[1] create a list of length n init to 0s
 listofzeros = [0] * n 
 
[2] get a sectional subset of a list
section = test_list[x: x + 3] # starts with index x to index x+3 but like range, the last element is not inclusive, means it includes elements from x to x + 2 not x + 3

[2.1] using itertools slicing 
itertools.islice(test_list, i, i + 3) # check what does this return 

[3] get sum of a list
sum(test_list[x: x + 3]) 

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


# Enums 
[1] define enums
from enum import Enum 

class Color(Enum):
RED = 1
GREEN = 2
BLUE = 3 

Links
-----
[1] libs: https://www.ubuntupit.com/best-python-libraries-and-packages-for-beginners/   

# Algorithms 
[1] arrays 

[1.1] arrays problems where math operations are needed on the left vs the right of each element in the array. use a single loop to iterate over each element and make the operations left vs right, 
example "Sherlock and array" problem 