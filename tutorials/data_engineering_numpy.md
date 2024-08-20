# What is NumPy?
NumPy, short for Numerical Python, is a fundamental library for numerical and scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays. 

NumPy is a basis for Pandas.


Term	Definition
.csv file	A .csv (Comma-Separated Values) file is a plain text file format for storing tabular data, where each line represents a row and uses commas to separate values in different columns.
.txt file	A .txt (Text) file is a common file format that contains plain text without specific formatting, making it suitable for storing and editing textual data.
Append	To "append" means to add or attach something to the end of an existing object, typically used in the context of adding data to a file or elements to a data structure like a list in Python.
Attribute	An "attribute" in Python refers to a property or characteristic associated with an object, which can be accessed using dot notation.
Broadcasting in NumPy	Broadcasting in NumPy allows arrays with different shapes to be combined in element-wise operations by automatically extending smaller arrays to match the shape of larger ones, making operations more flexible.
Component	In NumPy, a "component" typically refers to a specific element or value within a multi-dimensional array, which can be accessed using indexing.
Computation	Computation in NumPy involves performing numerical operations on arrays and matrices, making it a powerful library for mathematical and scientific computing in Python.
Data analysis	Data analysis is the process of inspecting, cleaning, transforming, and interpreting data to discover useful information, draw conclusions, and support decision-making.
DataFrames	A DataFrames in Pandas is a two-dimensional, tabular data structure for storing and analyzing data, consisting of rows and columns.
Dependencies	Dependencies in Pandas are external libraries or modules, such as NumPy, that Pandas rely on for fundamental data manipulation and analysis functionality.
File attribute	File attributes generally refer to properties or metadata associated with files, which are managed at the operating system level.
File object	A "file object" in Python represents an open file, allowing reading from or writing to the file.
Grid	In Python, a "grid" typically refers to a two-dimensional structure composed of rows and columns, often used to represent data in a tabular format or for organizing objects in a coordinate system.
Hadamard Product	The Hadamard product is a mathematical operation that involves element-wise multiplication of two matrices or arrays of the same shape, producing a new matrix with each element being the product of the corresponding elements in the input matrices.
Importing pandas	To import Pandas in Python, you use the statement: import pandas as pd, which allows you to access Pandas functions and data structures using the abbreviation "pd."
Index	In Python, an "index" typically refers to a position or identifier used to access elements within a sequence or data structure, such as a list or string.
Libraries	Libraries in Python are collections of pre-written code modules that provide reusable functions and classes to simplify and enhance software development.
Linespace	In Python, "linespace" refers to a NumPy function that generates an array of evenly spaced values within a specified range.
NumPy	NumPy in Python is a fundamental library for numerical computing that provides support for large, multi-dimensional arrays and matrices, as well as a variety of high-level mathematical functions to operate on these arrays.
One dimensional NumPy	A one-dimensional NumPy array is a linear data structure that stores elements in a single sequence, often used for numerical computations and data manipulation.
Open function	In Python, the "open" function is used to access and manipulate files, allowing you to read from or write to a specified file.
Pandas	Pandas is a popular Python library for data manipulation and analysis, offering data structures and tools for working with structured data like tables and time series.
Pandas library	Pandas library in Python refer to the various modules and functions within the Pandas library, which provides powerful data structures and data analysis tools for working with structured data.
Plotting Mathematical Functions	Plotting mathematical functions in Python involves using libraries like Matplotlib to create graphical representations of mathematical equations, aiding visualization, and analysis.
Shape	In NumPy, "shape" refers to an array's dimensions (number of rows and columns), describing its size and structure.
Slicing	Slicing in NumPy entails extracting specific portions of an array by specifying a range of indices, enabling you to work with subsets of the data.
Two dimensional NumPy	A two-dimensional NumPy array is a structured data representation with rows and columns, resembling a matrix or table, ideal for various data manipulation and analysis tasks.
Universal Functions	Universal functions (ufuncs) in NumPy are functions that operate element-wise on arrays, providing efficient and vectorized operations for a wide range of mathematical and logical operations.
Vector addition	Vector addition in Python involves adding corresponding elements of two or more vectors, producing a new vector with the sum of their components.
Visualizations	Visualizations in Python refer to the creation of graphical representations, such as charts, plots, and graphs, to illustrate and communicate data and trends visually.

# features 
1- **Efficient data structures**: NumPy introduces efficient array structures, which are faster and more memory-efficient than Python lists. This is crucial for handling large data sets.

2- **Multi-dimensional arrays**: NumPy allows you to work with multi-dimensional arrays, enabling the representation of matrices and tensors. This is particularly useful in scientific computing.

3- **Element-wise operations**: NumPy simplifies element-wise mathematical operations on arrays, making it easy to perform calculations on entire data sets in one go.

4- **Random number generation**: It provides a wide range of functions for generating random numbers and random data, which is useful for simulations and statistical analysis.

5- **Integration with other libraries**: NumPy seamlessly integrates with other data science libraries like SciPy, Pandas, and Matplotlib, enhancing its utility in various domains.

6- **Performance optimization**: NumPy functions are implemented in low-level languages like C and Fortran, which significantly boosts their performance. It's a go-to choice when speed is essential.

## importing numpy 
```
import numpy as np
```

## creating a numpy
```
# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5]) # **np.array()** is used to create NumPy arrays.

# Creating a 2D array. the number of dimension is the number of listing, so in the example down, there is the main list + the inner listing (not number of elements in the main list)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

```
# Array attributes
print(arr_2d.ndim)  # ndim : Represents the number of dimensions or "rank" of the array.
# output : 2

print(arr_2d.shape)  # shape : Returns a tuple indicating the number of rows and columns in the array.
# Output : (3, 3)

print(arr_2d.size) # size: Provides the total number of elements in the array.
# Output : 9
```

## indexing and slicing
```
# Indexing and slicing
print(arr_1d[2])          # Accessing an element (3rd element)

print(arr_2d[1, 2])       # Accessing an element (2nd row, 3rd column)

print(arr_2d[:, 1])       # Accessing a column (2nd column)
```

## operations 
```
# Array addition
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)  # [5 7 9]

scalar operations
# Scalar multiplication
array = np.array([1, 2, 3])
result = array * 2 # each element of an array is multiplied by 2
print(result)  # [2 4 6]

# Element-wise multiplication (Hadamard product)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 * array2
print(result)  # [4 10 18]

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)
print(result)
# [[19 22]
#  [43 50]]

# math operations
np.mean(array)
np.sum(array)
np.min(array
np.max(array)
np.dot(array_1, array_2)

```


