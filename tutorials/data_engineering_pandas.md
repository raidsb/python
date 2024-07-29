# Pandas
https://pandas.pydata.org/docs/ 

## what is pandas
Pandas is a popular open-source data manipulation and analysis library for the Python programming language. It provides a powerful and flexible set of tools for working with structured data, making it a fundamental tool for data scientists, analysts, and engineers.
Pandas is designed to handle data in various formats, such as tabular data, time series data, and more, making it an essential part of the data processing workflow in many industries.

## Advantages of pandas
**datastructures offered by pandas**
Data Structures: Pandas offers two primary data structures - DataFrame and Series.
1- A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
2- A Series is a one-dimensional labeled array, essentially a single column or row of data.

**data importing and exporting**
1- Data Import and Export: Pandas makes it easy to read data from various sources, including CSV files, Excel spreadsheets, SQL databases, and more. It can also export data to these formats, enabling seamless data exchange.
2- Data Merging and Joining: You can combine multiple DataFrames using methods like merge and join, similar to SQL operations, to create more complex datasets from different sources.

**Efficient Indexing**
Pandas provides efficient indexing and selection methods, allowing you to access specific rows and columns of data quickly.

**Custom Data Structures**
You can create custom data structures and manipulate data in ways that suit your specific needs, extending Pandas' capabilities.

## import pandas library 
```
import pandas as pd # renamed to pd by convention
```

## Series 
### creating a series and accessing elements
A Series is a one-dimensional labeled array in Pandas. It can be thought of as a single column of data with labels or indices for each element. You can create a Series from various data sources, such as lists, NumPy arrays, or dictionaries

```
import pandas as pd
# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)
```

accessing by label
```
print(s[2])     # Access the element with label 2 (value 30)
```

accessing by position
```
print(s.iloc[3]) # Access the element at position 3 (value 40)
```

accessig multiple elements 
```
print(s[1:4])   # Access a range of elements by label
```

### functions available for series
values: Returns the Series data as a NumPy array.
index: Returns the index (labels) of the Series.
shape: Returns a tuple representing the dimensions of the Series.
size: Returns the number of elements in the Series.
mean(), sum(), min(), max(): Calculate summary statistics of the data.
unique(), nunique(): Get unique values or the number of unique values.
sort_values(), sort_index(): Sort the Series by values or index labels.
isnull(), notnull(): Check for missing (NaN) or non-missing values.
apply(): Apply a custom function to each element of the Series.


## dataframes
### what is a dataframe
A DataFrame is a two-dimensional labeled data structure with columns of potentially different data types. Think of it as a table where each column represents a variable, and each row represents an observation or data point. DataFrames are suitable for a wide range of data, including structured data from CSV files, Excel spreadsheets, SQL databases, and more.

### loading data from a csv files into a dataframe
The read_csv function is used to load data from a CSV file into a Pandas DataFrame.

```
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')
```

### Creating DataFrames from Dictionaries 
DataFrames can be created from dictionaries, with keys as column labels and values as lists representing rows. 

```
import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
```

my work 
```
#write your code here
import pandas as pd 
dict_of_things = {"Student": ["David", "Sam", "Terry", "Evan"],
                  "Age": [27, 24, 22, 32],
                  "Country": ["UK", "Canada", "China", "USA"],
                  "Course": ["Python", "DS", "ML", "Web"],
                  "Marks": [85, 72, 89, 76] }
df = pd.DataFrame(dict_of_things)

# selecting the marks column
b = df[["Marks"]]

# selecting multiple columns 
c = df[['Country', 'Course']]

# Get the Student column as a series Object
x = df['Student']
type(x) # pandas.core.series.Series 

```

### Column Selection
```
print(df['Name'])  # Access the 'Name' column will retrieve the whole column. the return of the selection is a dataframe # multiple columns for multiple column selections and then can be used as dataframe

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]

type(x)

# access to multiple columns 
z = df[['Department','Salary','ID']] 

```

### accessing rows 
```
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label
```

### slicing 
```
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows

# let us do the slicing using old dataframe df
df.iloc[0:2, 0:3]

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']

#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
df2.loc['Rose':'Jane', 'ID':'Department']


```

### finding unique elements 
```
unique_dates = df['Age'].unique()
```

### conditional filtering
```
high_above_102 = df[df['Age'] > 25]
```

### saving dataframe 
```
df.to_csv('trading_data.csv', index=False)
```

### dataframes attributes and method 
```
shape: Returns the dimensions (number of rows and columns) of the DataFrame.
info(): Provides a summary of the DataFrame, including data types and non-null counts.
describe(): Generates summary statistics for numerical columns.
head(), tail(): Displays the first or last n rows of the DataFrame.
mean(), sum(), min(), max(): Calculate summary statistics for columns.
sort_values(): Sort the DataFrame by one or more columns.
groupby(): Group data based on specific columns for aggregation.
fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
apply(): Apply a function to each element, row, or column of the DataFrame.
```

### accessing with loc and iloc
loc() is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select. This method includes the last element of the range passed in it.

Simple syntax for your understanding:
```
loc[row_label, column_label]
```

iloc() is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. This method does not include the last element of the range passed in it.

Simple syntax for your understanding:
```
iloc[row_index, column_index]
```

examples 
```
# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the column using the name
df.loc[0, 'Salary']
```

### using label as index

```
df2=df
df2=df2.set_index("Name")

#To display the first 5 rows of new dataframe
df2.head()

#Now, let us access the column using the name
df2.loc['Jane', 'Salary']
```