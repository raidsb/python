# python

## referece resources
https://docs.python.org/3/        # python language specification
https://peps.python.org/pep-0008/ # styling documentation (python enhancement proposal)
https://www.geeksforgeeks.org/    # tutorials

## Learning resources
https://zerotomastery.io/cheatsheets/python-cheat-sheet/  # Done
https://www.geeksforgeeks.org/python-cheat-sheet/         # Done
https://realpython.com/                                   # reference
https://blog.finxter.com/                                 # reference
https://realpython.com/python-class-constructor/          # -> Subclassing Immutable Built-in Types
https://realpython.com/python-classes/#special-methods-and-protocols 
https://realpython.com/python-double-underscore/ 
https://realpython.com/inheritance-composition-python/ 
https://realpython.com/python-unittest/ 
https://realpython.com/python-callable-instances/
https://realpython.com/python-calendar-module/ 
https://realpython.com/python-built-in-exceptions/ 
https://realpython.com/preview/python-string-interpolation/ 
https://realpython.com/preview/python-mappings/ 
https://github.com/fgmacedo/python-statemachine # state-machine
https://www.benkuhn.net/progessays/ # essays
https://realpython.com/crud-operations/ # database
https://realpython.com/python-mappings/#characteristics-of-the-mapping-abstract-base-class # mappings/
https://realpython.com/preview/readme-python-project/ # readme python
https://realpython.com/data-engineer-interview-questions-python/#questions-on-design-patterns-and-etl-concepts # data enginnering
https://realpython.com/data-engineer-interview-questions-python/#questions-on-design-patterns-and-etl-concepts # data engineering interview questions 
https://realpython.com/bonus/python-mastery-course/ # mastering python to the next level 
https://realpython.com/cpython-source-code-guide/ # cpython 

## learning resources - data science
https://www.datacamp.com/cheat-sheet
https://www.kdnuggets.com/free-python-resources-that-can-help-you-become-a-pro 
https://oli.cmu.edu/courses/principles-of-computation-with-python-open-free/ 
https://www.freecodecamp.org/learn/data-analysis-with-python/
https://www.kdnuggets.com/2022/09/free-python-data-science-course.html
https://www.blog.pythonlibrary.org/2024/05/13/how-to-annotate-a-graph-with-matplotlib-and-python/ # matplotlib 

## learning resources - QA
https://hackr.io/blog/python-interview-questions 
https://www.geeksforgeeks.org/python-interview-questions/
https://www.datacamp.com/blog/top-python-interview-questions-and-answers 
https://www.interviewbit.com/python-interview-questions/#interpreted-language

## libraries
https://www.ubuntupit.com/best-python-libraries-and-packages-for-beginners/    
https://github.com/brohrer/pacemaker # For controlling time per iteration loop in Python.

## Concepts:
* What is python? main features of python language?
Python is a general-purpose, high-level, interpreted language. It has fewer syntactic constructions compared to other languages.
some of the unique features of python:
1* Structured and functional programming is supported.
2* It can be compiled to byte code to create larger applications.
3* Supports high-level dynamic data types.
4* Supports checking of dynamic data types.
5* Applies automated garbage collection.
6* It could be used effectively along with Java, COBRA, C, C++, ActiveX, and COM.

### scripting vs programming language
* As a scripting language, Python is often used for automating tasks, executing scripts, and rapid prototyping. It's well-suited for tasks such as system administration, web development, data analysis, and scientific computing.
* As a programming language, Python is used to develop a wide range of software applications, including desktop GUI applications, web applications, games, artificial intelligence systems, and more. Python's versatility, readability, and extensive standard library make it a popular choice for software development projects of all sizes.

The distinction between scripting and programming is somewhat fluid, and the terms are often used interchangeably. However, there are some general guidelines that can help differentiate between the two:
* Scope and Complexity:
Scripting typically refers to writing small programs or scripts to automate specific tasks or perform simple operations. These scripts are often interpreted and executed line by line.
Programming usually involves developing larger, more complex software applications that may require planning, design, and implementation of algorithms and data structures. Programs are often compiled into machine code before execution.

* Purpose and Context:
Scripting is often used for tasks such as system administration, data processing, automation, or gluing together different software components.
Programming is commonly associated with software development for creating standalone applications, libraries, frameworks, or systems.

* Language Choice:
Scripting languages like Python, JavaScript, or Bash are often used for scripting tasks due to their ease of use, flexibility, and quick development cycle.
Programming languages like Java, C++, or C# are typically used for larger software development projects where performance, scalability, and maintainability are important.

* Execution Environment:
Scripts are usually executed within a runtime environment or interpreter without the need for compilation.
Programs are compiled into machine code or intermediate bytecode before execution.

#### can a program be both scripting and programming?
Yes, a program can be both scripting and programming depending on how it's used and the context in which it operates.

A program can be considered scripting when it's used to automate specific tasks or perform simple operations, typically in an interpreted environment. These scripts are often written in scripting languages like Python, Bash, or JavaScript and executed line by line.
On the other hand, the same program can also be considered programming when it's involved in developing larger, more complex software applications or systems. This may involve planning, designing, and implementing algorithms and data structures, and the program may be compiled into machine code before execution.
For example, a Python script that automates a series of data processing tasks could be considered scripting. However, if that same script evolves into a larger, more sophisticated software application with a graphical user interface (GUI) and various modules interacting with each other, it could be viewed as a full-fledged program.
So, whether a program is considered scripting or programming depends on factors such as its scope, complexity, purpose, and context of use. Often, the terms scripting and programming are used interchangeably, and the distinction between them can be fluid.

### operators 
These are standard symbols used in logical and mathematical processes. 
* mathematical operators: +, -, *, /, ...
* Logical operators: or, and, not. 
* comparison: <, >, ==.
* bitwise operators 
```
# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)
```
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
int(float_number) # you will lose information 
float(int)     # no loss of information
bool(1) # True
bool(0) # False
int(True) # 1
int(False) # 0 
```

### collection vs sequence vs iterable vs iterator
Understanding the distinctions between collection, iterable, iterator, and sequence is fundamental to grasping the behavior and characteristics of data structures and objects in Python:

* Collection:
A collection refers to any data structure or object that can hold multiple elements or values.
Collections can be mutable (allowing modifications after creation) or immutable (fixed once created).
Examples of collections include lists, tuples, sets, dictionaries, and user-defined classes that implement container-like behavior.

* Iterable:
An iterable is any object in Python that can be iterated over, meaning it can be used in a for loop or passed to functions like sum(), min(), or max() that expect iterables.
Iterables include sequences (lists, tuples, strings), collections (sets, dictionaries), generators, and any object that implements the __iter__() method, which returns an iterator.
Iterables can be traversed from start to end, but they do not necessarily have a fixed order or indexing.

* Iterator:
An iterator is an object that represents a stream of data and supports iteration.
Iterators have two primary methods: __iter__() and __next__(). The __iter__() method returns the iterator object itself, while __next__() returns the next item in the stream or raises a StopIteration exception when the end of the stream is reached.
Iterators maintain state and can be advanced using the __next__() method, making them suitable for lazy evaluation and processing of large or infinite data streams.
Examples of iterators in Python include generator objects, file objects, and objects returned by the iter() function.

* Sequence:
A sequence is a specific type of iterable that represents an ordered collection of items, indexed by integers.
Sequences support indexing, slicing, concatenation, repetition, and membership testing.
Examples of sequences in Python include lists, tuples, strings, and byte arrays.
Sequences guarantee order and allow duplicate elements, distinguishing them from other types of iterables that may not have a defined order or support indexing.

### Versatile
Describing Python as versatile means acknowledging its wide range of applications and adaptability to various programming tasks, domains, and paradigms.

### oop
A definition:
* Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects.
* Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.
* object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees or students and teachers. OOP models real-world entities as software objects that have some data associated with them and can perform certain operations.

key notes
* Define a class, which is a sort of blueprint for an object
* Instantiate a class to create an object
* Use attributes and methods to define the properties and behaviors of an object
* Use inheritance to create child classes from a parent class
* Reference a method on a parent class using super()
* Check if an object inherits from another class using isinstance()

#### override vs overwrite vs overload 

"Override," "overwrite," and "overload" are terms used in the context of object-oriented programming to describe different concepts related to methods and functions. Here's a brief explanation of each:

* Override:
Inheritance: Override refers to the practice of providing a new implementation for a method in a subclass that is already present in its superclass.
Polymorphism: When an overridden method is called on an instance of the subclass, the subclass's implementation of the method is executed instead of the superclass's implementation.
Usage: Override is commonly used to customize or extend the behavior of inherited methods to suit the specific requirements of a subclass.
Overwrite:

* Informal Term: "Overwrite" is not a commonly used term in the context of object-oriented programming.
Confusion: It may sometimes be used interchangeably with "override," but it's not standard terminology.
Usage: To avoid confusion, it's best to use "override" when referring to providing new implementations for inherited methods.

* Overload:
Multiple Definitions: Overload refers to defining multiple methods or functions with the same name within the same scope but with different parameter lists (i.e., different types or numbers of parameters).
Signature: Overloaded methods must have different method signatures, which include the method's name and the number, types, or order of its parameters.
Polymorphism: Overload enables polymorphism at compile-time (static polymorphism) because the appropriate method to call is determined based on the arguments' types at compile-time.
Usage: Overload is commonly used to provide multiple ways of invoking a method or function with different parameter types or numbers. It enhances code readability and flexibility by allowing methods with similar functionality to share the same name.

#### constructors
Class constructors internally trigger Python’s instantiation process, which runs through two main steps: instance creation and instance initialization

```
>>> class SomeClass:
...     pass
...

>>> # Call the class to construct an object
>>> SomeClass()
<__main__.SomeClass object at 0x7fecf442a140>
```

In Python, when you call a class as you did in the above example, you’re calling the class constructor, which creates, initializes, and returns a new object by triggering Python’s internal instantiation process.

To run the first step, Python classes have a special method called .__new__(), which is responsible for creating and returning a new empty object. Then another special method, .__init__(), takes the resulting object, along with the class constructor’s arguments.

so there are special dunder methods to create a new instance and initialize it.
* The first method is the __new__ method which creates the instance from the object.
* The second method is the __init__ used to initialize the object.

an example showing the instanciation of a new Object
```
# point.py

class Point:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")
        return super().__new__(cls) # NOte 1: it seems all classes inherit from a parent class, this is why there is a super().__new__ here
		                            # Note 2: __new__ is a class method but returns an instance object.
									# Note 3: the instance returned will be the self argument to __init__
    def __init__(self, x, y):       # self is the first argument, which holds a reference to the current instance
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self) -> str:      # special method, which provides a proper string representation for your Point class 
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

# calling 
>>> from point import Point

>>> point = Point(21, 42)
1. Create a new instance of Point.
2. Initialize the new instance of Point.

>>> point
Point(x=21, y=42)

# Now try to call the __new__ and __init__ manually:
>>> from point import Point

>>> point = Point.__new__(Point)
1. Create a new instance of Point.

>>> # The point object is not initialized
>>> point.x
Traceback (most recent call last):
    ...
AttributeError: 'Point' object has no attribute 'x'
>>> point.y
Traceback (most recent call last):
    ...
AttributeError: 'Point' object has no attribute 'y'

>>> point.__init__(21, 42)
2. Initialize the new instance of Point.

>>> # Now point is properly initialized
>>> point
Point(x=21, y=42)

```

It is crazy and don't know yet why someone will do that but A subtle and important detail to note about .__new__() is that it can also return an instance of a class different from the class that implements the method itself. When that happens, Python doesn’t call .__init__() in the current class, because there’s no way to unambiguously know how to initialize an object of a different class.

```
# ab_classes.py

class A:
    def __init__(self, a_value):
        print("Initialize the new instance of A.")
        self.a_value = a_value

class B:
    def __new__(cls, *args, **kwargs):
        return A(42) # ------------> returns an instance of class A

    def __init__(self, b_value):
        print("Initialize the new instance of B.")
        self.b_value = b_value

# demonstrate:
>>> from ab_classes import B

>>> b = B(21)
Initialize the new instance of A.

>>> b.b_value
Traceback (most recent call last):
    ...
AttributeError: 'A' object has no attribute 'b_value'

>>> isinstance(b, B)
False
>>> isinstance(b, A)
True

>>> b.a_value
42

```

__init__ cannot return but None implecitly
```
>>> class Rectangle:
...     def __init__(self, width, height):
...         self.width = width
...         self.height = height
...         return 42
...

>>> rectangle = Rectangle(21, 42)
Traceback (most recent call last):
    ...
TypeError: __init__() should return None, not 'int'
```

In .__init__(), you can also run any transformation over the input arguments to properly initialize the instance attributes. For example, if your users will use Rectangle directly, then you might want to validate the supplied width and height and make sure that they’re correct before initializing the corresponding attributes:
example of overriding __init__ method to do additional validation for example:

```
>>> class Rectangle:
...     def __init__(self, width, height):
...         if not (isinstance(width, (int, float)) and width > 0):
...             raise ValueError(f"positive width expected, got {width}")   # example of using raise for validating given values.
...         self.width = width
...         if not (isinstance(height, (int, float)) and height > 0):
...             raise ValueError(f"positive height expected, got {height}") # example of using raise for validating given values.
...         self.height = height
...

>>> rectangle = Rectangle(-21, 42)
Traceback (most recent call last):
    ...
ValueError: positive width expected, got -21
```

Using __init__ in inheritance to add additonal steps to do in the Child
```
>>> class Person:
...     def __init__(self, name, birth_date):
...         self.name = name
...         self.birth_date = birth_date
...

>>> class Employee(Person):
...     def __init__(self, name, birth_date, position):
...         super().__init__(name, birth_date)
...         self.position = position          # ---------> this is called "EXTEND" the base class behavior 
...

>>> john = Employee("John Doe", "2001-02-07", "Python Developer")

>>> john.name
'John Doe'
>>> john.birth_date
'2001-02-07'
>>> john.position
'Python Developer'
```

Special cases when you want to create your own __new__ method (you want to control how the instance is created)
Providing Custom Object Creators
Typically, you’ll write a custom implementation of .__new__() only when you need to control the creation of a new instance at a low level. Now, if you need a custom implementation of this method, then you should follow a few steps:
1* Create a new instance by calling super().__new__() with appropriate arguments.
2* Customize the new instance according to your specific needs.
3* Return the new instance to continue the instantiation process.

```
class SomeClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        # Customize your instance here...
        return instance
```

It’s important to note that object.__new__() itself only accepts a single argument, the class to instantiate. If you call object.__new__() with more arguments, then you get a TypeError:
```
>>> class SomeClass:
...     def __new__(cls, *args, **kwargs):
...         return super().__new__(cls, *args, **kwargs)
...     def __init__(self, value):
...         self.value = value
...

>>> SomeClass(42)
Traceback (most recent call last):
    ...
TypeError: object.__new__() takes exactly one argument (the type to instantiate)
```
In this example, you hand over *args and **kwargs as additional arguments in the call to super().__new__(). The underlying object.__new__() accepts only the class as an argument, so you get a TypeError when you instantiate the class.

However, object.__new__() still accepts and passes over extra arguments to .__init__() if your class doesn’t override .__new__(), as in the following variation of SomeClass:
```
>>> class SomeClass:
...     def __init__(self, value):
...         self.value = value
...

>>> some_obj = SomeClass(42)
>>> some_obj
<__main__.SomeClass object at 0x7f67db8d0ac0>
>>> some_obj.value
42
```
In this implementation of SomeClass, you don’t override .__new__(). The object creation is then delegated to object.__new__(), which now accepts value and passes it over to SomeClass.__init__() to finalize the instantiation. Now you can create new and fully initialized instances of SomeClass, just like some_obj in the example.

args and kwargs are used only when __new__ is called explicitly in the code.
Class.__new__(arguments)

#### Inheritnce
Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that you derive child classes from are called parent classes.
Child classes can override or extend the attributes and methods of parent classes. In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.

* override a parent method
```
# inheritance.py

class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_color = "purple" # overriden
```

* extend a parent
You also inherit, in a sense, your language from your parents. If your parents speak English, then you’ll also speak English. Now imagine you decide to learn a second language, like German. In this case, you’ve extended your attributes because you’ve added an attribute that your parents don’t have:
```
# inheritance.py

class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German") # extending the parent attribute with additional value in the child
```

* using super methods 
```
# dog.py

# ...

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

# ...
```

### dunder methods
Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores. There are many dunder methods that you can use to customize classes in Python

### Exceptions and errors
* Errors are concrete conditions, such as syntax and logical errors, that make your code work incorrectly or even crash. Often, you can fix errors by updating or modifying the code, installing a new version of a dependency, checking the code’s logic, and so on. So, your code won’t break, and your program will continue its normal execution.
You can fix errors, but you can’t handle them. In other words, if you have a syntax error like the one in the example, then you won’t be able to handle that error and make the code run. You need to correct the syntax.

Note in this kind of issues "errors": You can fix errors, but you can’t handle them. In other words, if you have a syntax error like the one in the example, then you won’t be able to handle that error and make the code run. You need to correct the syntax.

* Exception handling
exceptions are events that interrupt the execution of a program. As their name suggests, exceptions occur in exceptional situations that should or shouldn’t happen. So, to prevent your program from crashing after an exception, you must handle the exception with the appropriate exception-handling mechanism.

## installing and setting-up environment
```
# update version of pip
python.exe -m pip install --upgrade pip

# checking version 
tox --version

# upgrading a lib
pip install --upgrade tox
```

## importing libraries
### importing multiple libraries
can write the importing statements this way:

```
from library import lib1, lib2 
```
or this way:
```
from library import (lib1, lib2) # the parentheses are used for grouping for better readiblity but optional.
```

### importing a single module with __import__()

Note: What if your application is a single script?

You can import any attributes of the script, such as classes, functions, and variables by using the built-in __import__() function. Instead of from my_sum import sum, you can write the following:

target = __import__("my_sum.py")
sum = target.sum
The benefit of using __import__() is that you don’t have to turn your project folder into a package, and you can specify the file name. This is also useful if your filename collides with any standard library packages. For example, math.py would collide with the math module.

## Print
print parameters
```
# ends the output with a space
print("Welcome to", end=' ')

# code for disabling the softspace feature
print('09', '12', '2016', sep='-')

# another example
print('Example', 'geeksforgeeks', sep='@')
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
type(False) # bool
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

### built-in non-primitive datatype - fractions
```
from fractions import Fraction

# a list of fractions
data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]

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

## built-in non-primitive datatype - ordered dictionary
An OrderedDict in Python is a dictionary subclass that remembers the order in which its items were inserted. 
It maintains a predictable iteration order, unlike a standard dictionary, which does not guarantee any specific 
order when iterating over its elements. Here are some scenarios in which you might consider using an OrderedDict:

* Preserving Insertion Order: If you need to preserve the order in which items were added to a dictionary and iterate over them in that order, an OrderedDict is a suitable choice. This can be useful in scenarios where the order of insertion is significant, such as processing configuration files or maintaining a log of events.
* Creating Ordered Data Structures: If you need to create data structures with a specific order, an OrderedDict can be used to ensure that items are stored and accessed in a predictable manner. For example, you might use an OrderedDict to represent ordered lists, stacks, or queues in your application.
* Implementing LRU Cache: An OrderedDict can be used to implement a simple Least Recently Used (LRU) cache, where the least recently accessed items are evicted from the cache when it reaches a certain size. By using an OrderedDict to store the cached items, you can ensure that the items are ordered based on their access frequency, with the least recently accessed items at the beginning of the dictionary.
* Serializing Data: When serializing data to formats like JSON or XML, the order of elements may be important for readability or compatibility with other systems. In such cases, using an OrderedDict to represent the data ensures that the serialized output maintains the same order as the original data structure.
* Working with APIs or Protocols: Some APIs or protocols may require data to be transmitted or processed in a specific order. Using an OrderedDict to organize the data before sending it over the network or passing it to external systems can help ensure compatibility and interoperability.

Overall, an OrderedDict is useful when you need to maintain the order of items in a dictionary and ensure predictable iteration order. 
It provides a convenient way to work with ordered data structures and can be particularly valuable in scenarios where the order of elements is important for correctness or compatibility.

```
from collections import OrderedDict
# Store each person's languages, keeping # track of who responded first. 
programmers = OrderedDict()
programmers['Tim'] = ['python', 'javascript']
programmers['Sarah'] = ['C++']
programmers['Bia'] = ['Ruby', 'Python', 'Go']

for name, langs in programmers.items():
    print(name + '-->')
    for lang in langs:
      print('\t' + lang)
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

## built-in non-primitive datatype - named tuples
Commonly used in scenarios where you have a collection of data with a fixed number of fields and you want to access the elements by name rather than by index. 
They are particularly useful for representing small, fixed-size records or data structures, such as database records, CSV rows, or function return values, where the position of each element has meaning.

Some common use cases for namedtuples include:
* Data Aggregation: Storing and accessing structured data in a concise and readable format.
* Function Return Values: Returning multiple values from a function in a more descriptive manner.
* Configuration Options: Storing configuration parameters or settings in a named and accessible format.
* API Responses: Parsing and working with data retrieved from APIs or web services.
* Database Records: Representing rows from a database query result in a more structured way.
* Overall, namedtuples provide a lightweight and intuitive way to work with structured data in Python, offering the convenience of accessing elements by name while retaining the immutability and efficiency of tuples.

```
from collections import namedtuple
Point = namedtuple('Point', 'x y')

# creating a named tuple
p = Point(1, y=2)# Point(x=1, y=2)

# accessing members of named tuple
p[0]             # 1
p.x              # 1
getattr(p, 'y')  # 2
p._fields        # Or: Point._fields #('x', 'y')
```

Another example
```
from collections import namedtuple
Person = namedtuple('Person', 'name height')
person = Person('Jean-Luc', 187)
f'{person.height}'           # '187'
'{p.height}'.format(p=person)# '187'
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
### return hint with ->
"->" in the function header is a hint of the return type
```
def raw_file_names(self) -> str:
	return "just a dummy string"
# this means a function that returns a string. it is optional in python and is meant to make it more readable
# more details about -> type: -> str: This part is a type hint, indicating that the method is expected to return a value of type str (string). Type hints are optional in Python, but they can provide information to developers and tools about the expected types of function parameters and return values.
```

### args and kwargs
* *args and **kwargs
Splat (*) expands a collection into positional arguments, while splatty-splat (**) expands a dictionary into keyword arguments.
```
args   = (1, 2)
kwargs = {'x': 3, 'y': 4, 'z': 5}
some_func(*args, **kwargs) # same as some_func(1, 2, x=3, y=4, z=5)
```

* * Inside Function Definition
Splat combines zero or more positional arguments into a tuple, while splatty-splat combines zero or more keyword arguments into a dictionary.
```
def add(*a):
    return sum(a)

add(1, 2, 3) # 6

def f(*args):                  # f(1, 2, 3)
def f(x, *args):               # f(1, 2, 3)
def f(*args, z):               # f(1, 2, z=3)
def f(x, *args, z):            # f(1, 2, z=3)

def f(**kwargs):               # f(x=1, y=2, z=3)
def f(x, **kwargs):            # f(x=1, y=2, z=3) | f(1, y=2, z=3)

def f(*args, **kwargs):        # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(x, *args, **kwargs):     # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(*args, y, **kwargs):     # f(x=1, y=2, z=3) | f(1, y=2, z=3)
def f(x, *args, z, **kwargs):  # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3)
```

Other Uses of * 
```
[*[1,2,3], *[4]]                # [1, 2, 3, 4]
{*[1,2,3], *[4]}                # {1, 2, 3, 4}
(*[1,2,3], *[4])                # (1, 2, 3, 4)
{**{'a': 1, 'b': 2}, **{'c': 3}}# {'a': 1, 'b': 2, 'c': 3}
head, *body, tail = [1,2,3,4,5]
```

### lambda
```
# lambda: <return_value>
# lambda <argument1>, <argument2>: <return_value>
```

Example using lambda in factorial
```
# Factorial
from functools import reduce
n = 3
factorial = reduce(lambda x, y: x*y, range(1, n+1))
print(factorial) #6
```

Example using lambda in fibbonaci (recursive call)
```
# Fibonacci
fib = lambda n : n if n <= 1 else fib(n-1) + fib(n-2)
result = fib(10)
print(result) #55
```

Example 
```
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))
```
### Useful built-in functions map, reduce, filter

* Map The map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable.
```
# example 1: Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# example 2: using lambda
list(map(lambda x: x + 1, range(10)))            # [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
```

* Filter The filter() method filters the given sequence using a function that examines each element in the sequence to see if it is true or false.
```
# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)
	
# another example: 
list(filter(lambda x: x > 5, range(10)))         # (6, 7, 8, 9)
```

* reduce 
The reduce function is used to apply a certain function to all of the list components indicated in the sequence sent along.
```
from functools import reduce
reduce(lambda acc, x: acc + x, range(10))        # 45
# how it works
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 1, 2, 3, 4, 5, 6, 7, 8, 9
# 3 , 3, 4, 5, 6, 7, 8, 9 
# 6, 4, 5, 6, 7, 8, 9 
# 10, 5, 6, 7, 8, 9
# 15, 6, 7, 8, 9
# 21, 7, 8, 9
# 28, 8, 9
# 36, 9
# 45

```

## Comprehension
```
<list> = [i+1 for i in range(10)]         # [1, 2, ..., 10]
<set>  = {i for i in range(10) if i > 5}  # {6, 7, 8, 9}
<iter> = (i+5 for i in range(10))         # (5, 6, ..., 14)
<dict> = {i: i*2 for i in range(10)}      # {0: 0, 1: 2, ..., 9: 18}
```

```
output = [i+j for i in range(3) for j in range(3)] # [0, 1, 2, 1, 2, 3, 2, 3, 4]

# Is the same as:
output = []
for i in range(3):
  for j in range(3):
    output.append(i+j)
```

## Ternary condition
```
# <expression_if_true> if <condition> else <expression_if_false>

[a if a else 'zero' for a in [0, 1, 0, 3]] # ['zero', 1, 'zero', 3]
```

## Closures functions 
We have a closure in Python when:

A nested function references a value of its enclosing function and then
the enclosing function returns the nested function.
```
def get_multiplier(a):
    def out(b):
        return a * b
    return out
	
>>> multiply_by_3 = get_multiplier(3)
>>> multiply_by_3(10)
30
```
If multiple nested functions within enclosing function reference the same value, that value gets shared.
To dynamically access function's first free variable use '<function>.__closure__[0].cell_contents'.

## Scope, non-local, global
If variable is being assigned to anywhere in the scope, it is regarded as a local variable, unless it is declared as a 'global' or a 'nonlocal 
Note: nonlocal keyword is not the same as the global keyword. While both keywords are used to access variables outside the current scope, they have different purposes and behaviors:

* nonlocal keyword: The nonlocal keyword is used to declare that a variable in an enclosed scope (such as a nested function) should be treated as a variable from the nearest enclosing scope that is not global. It allows you to modify variables in the nearest enclosing scope (typically the scope of a containing function) from within an inner function. nonlocal is primarily used in nested functions where you want to modify variables in an enclosing scope without affecting global variables.
```
def get_counter():
    i = 0
    def out():
        nonlocal i
        i += 1
        return i
    return out
```

```
>>> counter = get_counter()
>>> counter(), counter(), counter()
(1, 2, 3)
```

* global keyword: The global keyword is used to declare that a variable inside a function should refer to a global variable with the same name, rather than creating a new local variable.
It allows you to access and modify global variables from within a function.
global is typically used when you want to modify global variables from within a function, although it's generally considered better practice to avoid using global variables whenever possible.

```
x = 10
def func():
    global x
    x = 20
func()
print(x)  # Output: 20
```

## Modules
```
if __name__ == '__main__': # Runs main() if file wasn't imported.
    main()
```

```
import <module_name>
from <module_name> import <function_name>
import <module_name> as m
from <module_name> import <function_name> as m_function
from <module_name> import *
```

## Generators
Generators in Python are functions that enable the creation of iterators. 
They allow you to generate a sequence of values over time, rather than computing them all at once and storing them in memory. 
Generators are implemented using the yield keyword and provide a convenient way to work with large datasets or infinite sequences.

Here are some key points about generators:
* Lazy Evaluation: Generators use lazy evaluation, meaning that they generate values on-the-fly as they are requested, rather than computing and storing all values in memory at once. This makes them memory-efficient, especially for generating large or infinite sequences.
* Iterable Protocol: Generators implement the iterable protocol, which means they can be used in loops and comprehensions, just like other iterable objects such as lists or tuples.
* yield Keyword: Generators are defined using the def keyword like regular functions, but instead of using return to return a value, they use the yield keyword to yield a value to the caller. When a generator function is called, it returns a generator object, which can be iterated over to yield values.
* Stateful: Generators maintain their state between successive calls, allowing them to resume execution from where they left off. This makes them particularly useful for tasks that involve maintaining state or performing iterative computations.
Example:
```
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create a generator object
gen = countdown(5)

# Iterate over the generator to yield values
for value in gen:
    print(value)  # Output: 5, 4, 3, 2, 1
```
* Generator Expressions: Python also provides generator expressions, which are similar to list comprehensions but use parentheses instead of square brackets. Generator expressions are more memory-efficient than list comprehensions because they generate values lazily.
Generators are commonly used in Python for tasks such as reading large files line by line, generating sequences of numbers, or processing data in chunks without loading it all into memory at once. They provide a powerful and efficient way to work with sequences of values in a memory-conscious manner.

```
def count(start, step):
    while True:
        yield start
        start += step

>>> counter = count(10, 2)
>>> next(counter), next(counter), next(counter)
(10, 12, 14)
```

## Decorators 
A decorator takes a function, adds some functionality and returns it.

debuggers example:
```
from functools import wraps

def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return out

@debug
def add(x, y):
    return x + y
```
Wraps is a helper decorator that copies metadata of function add() to function out().
Without it 'add.__name__' would return 'out'.

## Any All
```
any([False, True, False])# True if at least one item in collection is truthy, False if empty.
all([True,1,3,True])     # True if all items in collection are true
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

## OOP 

### List of OOP features
list of oop features 
Object-oriented programming (OOP) is a programming paradigm that organizes software design around objects and their interactions. OOP provides several features and capabilities that help in designing and implementing robust, modular, and maintainable software systems. Here are the key features and capabilities of OOP:

*    Class and Object:
        Class: A blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of the class will have.
        Object: An instance of a class. It represents a real-world entity and encapsulates data and behavior.

*    Encapsulation:
        Encapsulation refers to the bundling of data (attributes) and methods that operate on the data into a single unit (i.e., class).
        It hides the internal state of an object and restricts direct access to it, allowing access only through well-defined interfaces (public methods).

*    Inheritance:
        Inheritance is a mechanism by which a class (subclass/derived class) can inherit properties and behaviors from another class (superclass/base class).
        It promotes code reusability, as subclasses can extend or override the functionality of their superclass.

*    Polymorphism:
        Polymorphism allows objects of different classes to be treated as objects of a common superclass.
        It enables a single interface to represent multiple underlying data types or forms.
        Two common forms of polymorphism are:
            Compile-time polymorphism (method overloading): Methods with the same name but different parameters in the same class.
            Run-time polymorphism (method overriding): Overriding a method in a subclass with a specific implementation.

*    Abstraction:
        Abstraction involves hiding the complex implementation details of a class and exposing only the essential features (i.e., what an object does rather than how it does it).
        It allows developers to focus on high-level design without worrying about implementation details.

*    Association, Aggregation, and Composition:
        Association: Represents a relationship between two or more classes where each class has its own lifecycle and there is no ownership.
        Aggregation: Represents a "has-a" relationship between classes, where one class is a part of another class.
        Composition: Represents a strong "has-a" relationship between classes, where one class owns another class and is responsible for its lifecycle.

*    Message Passing:
        Objects communicate with each other by sending messages. A message typically consists of a method invocation along with any required arguments.

*    Constructor and Destructor:
        Constructor: A special method called when an object of a class is created. It initializes the object's state.
        Destructor: A special method called when an object is destroyed. It performs cleanup tasks before the object is deallocated from memory.

*    Access Modifiers:
        Access modifiers control the visibility and accessibility of class members (attributes and methods).
        Common access modifiers include public, private, and protected, which determine whether members can be accessed from outside the class.

*    Overloading and Overriding:
        Overloading: Defining multiple methods in a class with the same name but different parameter lists.
        Overriding: Providing a new implementation for a method in a subclass that already exists in its superclass.

These features and capabilities of OOP help in designing modular, maintainable, and extensible software systems by promoting concepts such as encapsulation, inheritance, and polymorphism. By using OOP principles effectively, developers can create code that is easier to understand, modify, and extend.

### class
User defined objects are created using the class keyword.
Python class names are written in CapitalizedWords notation by convention. 
For example, a class for a specific breed of dog, like the Jack Russell Terrier, would be written as JackRussellTerrier.
```
class <name>:
    age = 80 # Class Object Attribute
    def __init__(self, a):
        self.a = a # Object Attribute

    @classmethod
    def get_class_name(cls):
        return cls.__name__
```

example: 
you define a class by using the class keyword followed by a name and a colon. Then you use .__init__() to declare which attributes each instance of the class should have:
```
class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age
```

```
# dog.py

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### class attributes
On the other hand, class attributes are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().
Use class attributes to define properties that should have the same value for every class instance. Use instance attributes for properties that vary from one instance to another.

```
# dog.py

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Example
```
# dog.py

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
```

### Intstanciating
This funny-looking string of letters and numbers is a memory address that indicates where Python stores the Dog object in your computer’s memory. 
```
>>> Dog()
<__main__.Dog object at 0x0004ccc90>
```

* checking the type of a class and if a child is instance of the Parent
To determine which class a given object belongs to, you can use the built-in type():
```
>>> type(miles)
<class '__main__.JackRussellTerrier'>
What if you want to determine if miles is also an instance of the Dog class? You can do this with the built-in isinstance():

>>> isinstance(miles, Dog)
True
```

### Instance method vs class method vs static method
Methods within a class can be categorized into three main types based on how they interact with the instance and class itself: 

* Instance Methods:
** Instance methods are the most common type of method in Python classes.
** They are defined within a class and take an instance of the class (usually named self) as the first parameter.
** Instance methods have access to the instance's attributes and can modify them.
** They are typically used to operate on instance-specific data and behavior.

Example:
```
class MyClass:
    def instance_method(self):
        return self.attribute
```

an instance can access both class and static methods directly
```
class MyClass:
    @classmethod
    def class_method(cls):
        return f"This is a class method of {cls.__name__}"

# Accessing class method through the class name
print(MyClass.class_method())  # Output: This is a class method of MyClass

# Accessing class method through an instance
instance = MyClass()
print(instance.class_method())  # Output: This is a class method of MyClass
```

```
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"

# Accessing static method through the class name
print(MyClass.static_method())  # Output: This is a static method

# Accessing static method through an instance
instance = MyClass()
print(instance.static_method())  # Output: This is a static method
```

Class methods can be accessed through instances because Python automatically passes the class as the first argument (cls) when you call a class method through an instance.
Even though the class is passed as an implicit argument, you can still access the class method through the instance, and the method behaves as if it were called through the class itself.

Static methods do not receive any implicit arguments (neither self nor cls), so they are essentially just regular functions defined within the class namespace.
Instances can access static methods directly because they are part of the class definition and can be accessed through the class itself or through instances.

* Class Methods:
** Class methods are decorated with @classmethod.
** They take a reference to the class (usually named cls) as the first parameter, instead of an instance.
** Class methods have access to the class itself and its attributes.
** They can be used to modify class-level variables or perform operations that involve the class itself. 
** Class methods are often used as alternative constructors or to provide utility functions related to the class.

Example:
```
class MyClass:
    class_variable = 10
    
    @classmethod
    def class_method(cls):
        return cls.class_variable
```

Example of using class method as a different constructor:
```
class MyClass:
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def from_string(cls, string):
        # Parse the string and create an instance
        return cls(int(string)) # This part calls the class constructor with the integer value obtained from int(string). By using cls, we can call the class constructor without explicitly referring to the class name. This allows the method to work even if the class name is changed later.

## calling it 
# Call the class method to create a new instance
my_instance = MyClass.from_string("10")
print(my_instance.value)  # Output: 10
```

a class method can access an instance members only through an instance passed to the class method, not directly from the same instance.
Yes, a class method in Python can access instance members, but it requires an instance of the class to access them.
Inside a class method, the first parameter conventionally named cls refers to the class itself, not an instance. 
However, by convention, the first parameter in an instance method is named self, and it refers to the instance of the class. Therefore, to access instance members from within a class method, you would need to pass an instance to the class method and use that instance to access its members.

a class method can access static methods: Accessing Static Methods:
Static methods are defined within the class and can be accessed directly through the class itself.
Since static methods do not depend on instance-specific or class-specific data, they can be called without an instance or the class name.

```
class MyClass:
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def class_method(cls, instance):
        # Access instance member using the instance
        return instance.value

# Create an instance of MyClass
my_instance = MyClass(10)

# Call the class method and pass the instance
result = MyClass.class_method(my_instance)

# Output the result
print(result)  # Output: 10

```

```
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"

    @classmethod
    def class_method(cls):
        # Access static method directly
        return cls.static_method()

print(MyClass.class_method())  # Output: This is a static method
```

* Static Methods:
** Static methods are decorated with @staticmethod.
** They do not take any reference to the instance or class as parameters.
** Static methods are similar to regular functions defined outside the class, but they are included within the class for organizational purposes.
** They cannot access or modify instance or class attributes directly.
** Static methods are often used for utility functions that do not depend on instance or class state.

Example:
```
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"
```
Each method type serves different purposes and has its own use cases. 
Instance methods are used for operations specific to instances of the class, 
class methods for operations related to the class itself, 
and static methods for utility functions that do not depend on instance or class state.

static methods can access class or instance methods indirectly
```
class MyClass:
    def instance_method(self):
        return "This is an instance method"

    @classmethod
    def class_method(cls):
        return "This is a class method"

    @staticmethod
    def static_method():
        # Static method cannot directly access instance method or class method
        # Instead, you can call them using instances or the class itself
        instance = MyClass()
        instance_result = instance.instance_method()

        class_result = MyClass.class_method()

        return f"Static method result: {instance_result}, {class_result}"

# Call the static method
print(MyClass.static_method())
```

static method can take instances as parameters 
```
class MyClass:
    @staticmethod
    def static_method(instance):
        return f"This is a static method called with instance {instance}"

# Create an instance of MyClass
my_instance = MyClass()

# Call the static method with the instance as an argument
result = MyClass.static_method(my_instance)

# Output the result
print(result)  # Output: This is a static method called with instance <__main__.MyClass object at 0x...>
```

### Inheritance 

* Multiple Inheritance

## Exceptions 
Example
```
try:
  5/0
except ZeroDivisionError:
  print("No division by zero!")
```

```
while True:
  try:
    x = int(input('Enter your age: '))
  except ValueError:
    print('Oops!  That was no valid number.  Try again...')
  else: # code that depends on the try block running successfully should be placed in the else block.
    print('Carry on!')
    break
```

example: 
```
a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))

    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))

except:
    print ("An error occurred")
```

### built-in exception handlings
Python has a complete set of built-in exceptions that provide a quick and efficient way to handle errors and exceptional situations that may happen in your code

## Files 
```
<file> = open('<path>', mode='r', encoding=None)
```

Modes
'r' - Read (default).
'w' - Write (truncate).
'x' - Write or fail if the file already exists.
'a' - Append.
'w+' - Read and write (truncate).
'r+' - Read and write from the start.
'a+' - Read and write from the end.
't' - Text mode (default).
'b' - Binary mode.

```
<file>.seek(0)                      # Moves to the start of the file.

<str/bytes> = <file>.readline()     # Returns a line.
<list>      = <file>.readlines()    # Returns a list of lines.

<file>.write(<str/bytes>)           # Writes a string or bytes object.
<file>.writelines(<list>)           # Writes a list of strings or bytes objects.
```

Methods do not add or strip trailing newlines.
```
# Read Text from File
def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines() # or read()

for line in read_file(filename):
  print(line)
```

writing to a File
```
def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
```

append to text File
```
def append_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
```

Example:
```
import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)

def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + 
                  new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)
```

## CSV File
```
import csv

#Read Rows from CSV File
def read_csv_file(filename):
    with open(filename, encoding='utf-8') as file:
        return csv.reader(file, delimiter=';')
		
#Write Rows to CSV File
def write_to_csv_file(filename, rows):
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(rows)
```

## JSON
```
import json
<str>    = json.dumps(<object>, ensure_ascii=True, indent=None)
<object> = json.loads(<str>)

# Read Object from JSON File
def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)

# Write Object to JSON File
def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)
		

```

## Pickle
```
# Pickle
import pickle
<bytes>  = pickle.dumps(<object>)
<object> = pickle.loads(<bytes>)

# Read Object from File
def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Write Object to File
def write_to_pickle_file(filename, an_object):
    with open(filename, 'wb') as file:
        pickle.dump(an_object, file)
```

## Profile
### Basic
```
from time import time
start_time = time()  # Seconds since
...
duration = time() - start_time
```

###Math
```
from math import e, pi
from math import cos, acos, sin, asin, tan, atan, degrees, radians
from math import log, log10, log2
from math import inf, nan, isinf, isnan
```

### Statistics
```
from statistics import mean, median, variance, pvariance, pstdev
```

### Random
```
from random import random, randint, choice, shuffle
random() # random float between 0 and 1
randint(0, 100) # random integer between 0 and 100
random_el = choice([1,2,3,4]) # select a random element from list
shuffle([1,2,3,4]) # shuffles a list
```

### Datetime
Module 'datetime' provides 'date' <D>, 'time' <T>, 'datetime' <DT> and 'timedelta' <TD> classes. All are immutable and hashable.
Time and datetime can be 'aware' <a>, meaning they have defined timezone, or 'naive' <n>, meaning they don't.
If object is naive it is presumed to be in system's timezone.

```
from datetime import date, time, datetime, timedelta
from dateutil.tz import UTC, tzlocal, gettz

# Constructors
<D>  = date(year, month, day)
<T>  = time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, fold=0)
<DT> = datetime(year, month, day, hour=0, minute=0, second=0, ...)
<TD> = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,
                 minutes=0, hours=0, weeks=0)
```
Use '<D/DT>.weekday()' to get the day of the week (Mon == 0).
'fold=1' means second pass in case of time jumping back for one hour.

Now
```
<D/DTn>  = D/DT.today()                     # Current local date or naive datetime.
<DTn>    = DT.utcnow()                      # Naive datetime from current UTC time.
<DTa>    = DT.now(<tz>)                     # Aware datetime from current tz time.
```

Timezone
```
<tz>     = UTC                              # UTC timezone.
<tz>     = tzlocal()                        # Local timezone.
<tz>     = gettz('<Cont.>/<City>')          # Timezone from 'Continent/City_Name' str.
<DTa>    = <DT>.astimezone(<tz>)            # Datetime, converted to passed timezone.
<Ta/DTa> = <T/DT>.replace(tzinfo=<tz>)      # Unconverted object with new timezone.
```

### Regex
```
import re
<str>   = re.sub(<regex>, new, text, count=0)  # Substitutes all occurrences.
<list>  = re.findall(<regex>, text)            # Returns all occurrences.
<list>  = re.split(<regex>, text, maxsplit=0)  # Use brackets in regex to keep the matches.
<Match> = re.search(<regex>, text)             # Searches for first occurrence of pattern.
<Match> = re.match(<regex>, text)              # Searches only at the beginning of the text.
```

Match Object
```
<str>   = <Match>.group()   # Whole match.
<str>   = <Match>.group(1)  # Part in first bracket.
<tuple> = <Match>.groups()  # All bracketed parts.
<int>   = <Match>.start()   # Start index of a match.
<int>   = <Match>.end()     # Exclusive end index of a match.
```

Special Sequences
```
# Expressions below hold true for strings that contain only ASCII characters. Use capital letters for negation.

'\d' == '[0-9]'          # Digit
'\s' == '[ \t\n\r\f\v]'  # Whitespace
'\w' == '[a-zA-Z0-9_]'   # Alphanumeric
```

example of Match
```
import re

# Text to search
text = "Hello, my email is example@example.com"

# Define a pattern to match email addresses
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

# Search for the pattern in the text
match = re.search(pattern, text)

# Check if a match is found
if match:
    email = match.group()
    print("Found email:", email)
else:
    print("No email found.")
```

MetaCharacters are helpful, significant, and will be used in module re functions, which helps us comprehend the analogy with RE. The list of metacharacters is shown below.
* \ sed to drop the special meaning of character following it.
* [] Represent a character class.
* ^ Matches the beginning.
* $ Matches the end.
* . Matches any character except newline.
* | Means OR (Matches with any of the characters separated by it.
* ? Matches zero or one occurrence.
* * Any number of occurrences (including 0 occurrences).
* + One or more occurrences.
* {} Indicate the number of occurrences of a preceding RegEx to match.
* () Enclose a group of RegEx.

## Algorithms 
### arrays 

* arrays problems where math operations are needed on the left vs the right of each element in the array. use a single loop to iterate over each element and make the operations left vs right, 
example "Sherlock and array" problem 

* the binary search
```
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
```

-------------------------------------------------------
## Multi-threading
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




