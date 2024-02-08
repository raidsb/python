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

# integer
[1] integer numbers can be written 123_333_444 this is same as 123333444. this to make it easier to read

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
[1] +, - , / , *, ** for exponent operation, // for full number div returns int not float
PEMDAS for precedency. if two operations at the same level, the one on the most left has higher precedency

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

Links
-----
[1] libs: https://www.ubuntupit.com/best-python-libraries-and-packages-for-beginners/   
