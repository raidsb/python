# python

# String
[1] single quotes vs double quotes: double quotes support string interpolation/formating with f or format function.
- single quote takes the string as literal

[2] using the index to get the character in a specific position 
"Hello"[0] # to get the character at position 0 of the string 
s = "Hello"
print(s[0])

# integer
[1] integer numbers can be written 123_333_444 this is same as 123333444. this to make it easier to read

# float 
[1] same as integer, can be written as 123_333.34 the _ to make it easier to read

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

Links
-----
[1] libs: https://www.ubuntupit.com/best-python-libraries-and-packages-for-beginners/   
