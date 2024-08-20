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

# read from Excel
df = pd.read_excel("data.xlsx")

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
# df.describe() 

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

## assign new index 
```
df_new=df
df_new.index=new_index
df_new.loc['a', 'Artist']
df_new.loc['a':'d', 'Artist']
```

## getting the column
```
dataframe_name["column_name"] # Accesses single column
dataframe_name[["column1", "column2"]] # Accesses multiple columns

# examples
df["age"]
df[["name", "age"]]

```

## dropping columns
Removes specified rows or columns from the DataFrame. axis=1 indicates columns. axis=0 indicates rows.
```
dataframe_name.drop(["column1", "column2"], axis=1, inplace=True)
dataframe_name.drop(index=[row1, row2], axis=0, inplace=True)

df.drop(["age", "salary"], axis=1, inplace=True) # Will drop columns
df.drop(index=[5, 10], axis=0, inplace=True) # Will drop rows

```

## dropping rows with missing values
```
# Removes rows with missing NaN values from the DataFrame. axis=0 indicates rows.
dataframe_name.dropna(axis=0, inplace=True)
df.dropna(axis=0, inplace=True)
```

## duplicating
Duplicate or repetitive values or records within a data set.

```
dataframe_name.duplicated()
duplicate_rows = df[df.duplicated()]
```

##  filtering
Creates a new DataFrame with rows that meet specified conditions.
```
filtered_df = dataframe_name[(Conditional_statements)]
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)
```

## splitting
```
Splits a DataFrame into groups based on specified criteria, enabling subsequent aggregation, transformation, or analysis within each group.

grouped = dataframe_name.groupby(by, axis=0, level=None, as_index=True,
sort=True, group_keys=True, squeeze=False, observed=False, dropna=True)

grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})
```

## displaying head
```
Displays the first n rows of the DataFrame.
df.head(5)
```

## displaying tail
```
Displays the last n rows of the DataFrame.
df.tail(5)
```

## displaying information about the dataframe
```
Provides information about the DataFrame, including data types and memory usage.
df.info()
```

## merging 
```
Merges two DataFrames based on multiple common columns.
merged_df = pd.merge(sales, products, on=["product_id", "category_id"])
```

## replacing
```
# Replaces specific values in a column with new values.
df["status"].replace("In Progress", "Active", inplace=True)
```

# Pandas is an API
An API lets two pieces of software talk to each other. Just like a function, you don't have to know how the API works, only its inputs and outputs. An essential type of API is a REST API that allows you to access resources via the internet. In this lab, we will review the Pandas Library in the context of an API, we will also review a basic REST API.

Pandas is actually set of software components , much of which is not even written in Python.


When you create **a Pandas object with the dataframe constructor, in API lingo this is an "instance"**. The data in the dictionary is passed along to the pandas API. You then use the dataframe to communicate with the API.

When you call the method head the dataframe communicates with the API displaying the first few rows of the dataframe.

Rest APIs function by sending a request, the request is communicated via HTTP message. The HTTP message usually contains a JSON file. This contains instructions for what operation we would like the service or resource to perform. In a similar manner, API returns a response, via an HTTP message, this response is usually contained within a JSON.

In this lab, we will use the NBA API to determine how well the Golden State Warriors performed against the Toronto Raptors. We will use the API to determine the number of points the Golden State Warriors won or lost by for each game. So if the value is three, the Golden State Warriors won by three points. Similarly it the Golden State Warriors lost by two points the result will be negative two. The API will handle a lot of the details, such a Endpoints and Authentication.

example of using API
```
!pip install nba_api

from nba_api.stats.static import teams
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict
	
nba_teams = teams.get_teams() # returns teams 
nba_teams[0:3] # looking into the first three teams

# To make things easier, we can convert the dictionary to a table. First, we use the function one dict, to create a dictionary. We use the common keys for each team as the keys, the value is a list; each element of the list corresponds to the values for each team. We then convert the dictionary to a dataframe, each row contains the information for a different team.
dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()

# Will use the team's nickname to find the unique id, we can see the row that contains the warriors by using the column nickname as follows:
df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors # displaying in jupyter

#We can use the following line of code to access the first column of the DataFrame

id_warriors=df_warriors[['id']].values[0][0]

# we now have an integer that can be used to request the Warriors information 
id_warriors

# The function "League Game Finder " will make an API call, it's in the module stats.endpoints.
from nba_api.stats.endpoints import leaguegamefinder

# The parameter team_id_nullable is the unique ID for the warriors. Under the hood, the NBA API is making a HTTP request.
# The information requested is provided and is transmitted via an HTTP response this is assigned to the object game finder.
```

The parameter team_id_nullable is the unique ID for the warriors. Under the hood, the NBA API is making a HTTP request.
The information requested is provided and is transmitted via an HTTP response this is assigned to the object game finder.

```
# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is commented out, you can run it on jupyter labs on your own computer.
# gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
```

We can see the json file by running the following line of code.
```
# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is commented out, you can run it on jupyter labs on your own computer.
# gamefinder.get_json()
```

The game finder object has a method get_data_frames(), that returns a dataframe. If we view the dataframe, we can see it contains information about all the games the Warriors played. The PLUS_MINUS column contains information on the score, if the value is negative, the Warriors lost by that many points, if the value is positive, the warriors won by that amount of points. The column MATCHUP has the team the Warriors were playing, GSW stands for Golden State Warriors and TOR means Toronto Raptors. vs signifies it was a home game and the @ symbol means an away game.
```
# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
# games = gamefinder.get_data_frames()[0]
# games.head()
```

You can download the dataframe from the API call for Golden State and run the rest like a video.
```
import requests

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")
```

```
file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()
```

We can create two dataframes, one for the games that the Warriors faced the raptors at home, and the second for away games.
```
games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']
```

We can calculate the mean for the column PLUS_MINUS for the dataframes games_home and  games_away:
```
games_home['PLUS_MINUS'].mean()
games_away['PLUS_MINUS'].mean()
```

We can plot out the PLUS MINUS column for the dataframes games_home and  games_away. We see the warriors played better at home.
```
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()
```



