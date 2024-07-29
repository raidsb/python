# Files 
open file cmd format
```
<file> = open('<path>', mode='r', encoding=None)
```

The mode parameter specifies ** the purpose of opening the file**, such as 'r' for reading, 'w' for writing, or 'a' for appending.
```
# Open the file in read ('r') mode
file = open('file.txt', 'r')
```

**Modes**
'r' - Read (default).
'w' - Write (truncate).
'x' - Write or fail if the file already exists.
'a' - Append.
'w+' - Read and write (truncate).
'r+' - Read and write from the start.
'a+' - Read and write from the end.
't' - Text mode (default).
'b' - Binary mode.


Mode	Syntax	Description
‘r’	'r'	Read mode. Opens an existing file for reading. Raises an error if the file doesn't exist.
‘w’	'w'	Write mode. Creates a new file for writing. Overwrites the file if it already exists.
‘a’	'a'	Append mode. Opens a file for appending data. Creates the file if it doesn't exist.
‘x’	'x'	Exclusive creation mode. Creates a new file for writing but raises an error if the file already exists.
‘rb’	'rb'	Read binary mode. Opens an existing binary file for reading.
‘wb’	'wb'	Write binary mode. Creates a new binary file for writing.
‘ab’	'ab'	Append binary mode. Opens a binary file for appending data.
‘xb’	'xb'	Exclusive binary creation mode. Creates a new binary file for writing but raises an error if it already exists.
‘rt’	'rt'	Read text mode. Opens an existing text file for reading. (Default for text files)
‘wt’	'wt'	Write text mode. Creates a new text file for writing. (Default for text files)
‘at’	'at'	Append text mode. Opens a text file for appending data. (Default for text files)
‘xt’	'xt'	Exclusive text creation mode. Creates a new text file for writing but raises an error if it already exists.
‘r+’	'r+'	Read and write mode. Opens an existing file for both reading and writing.
‘w+’	'w+'	Write and read mode. Creates a new file for reading and writing. Overwrites the file if it already exists.
‘a+’	'a+'	Append and read mode. Opens a file for both appending and reading. Creates the file if it doesn't exist.
‘x+’	'x+'	Exclusive creation and read/write mode. Creates a new file for reading and writing but raises an error if it already exists.

** get information about the file**
```
print(file1.name)
print(file1.mode)
file1.closed # to check if the file is closed
```

**with**
To simplify file handling and ensure proper closure of files, Python provides the "with" statement. It **automatically closes** the file when operations within the indented block are completed. This is considered **best practice** when working with files. advantages:
1- Automatic resource management: The file is guaranteed to be closed when you exit the with block, even if an exception occurs during processing.
2- Cleaner and more concise code: You don't need to explicitly call close(), making your code more readable and less error-prone.

```
# Reading and Storing the Entire Content of a File
# Using the read method, you can retrieve the complete content of a file
# and store it as a string in a variable for further processing or display.
# Step 1: Open the file you want to read
with open('file.txt', 'r') as file:
    # Step 2: Use the read method to read the entire content of the file
    file_stuff = file.read()
    # Step 3: Now that the file content is stored in the variable 'file_stuff',
    # you can manipulate or display it as needed.
    # For example, let's print the content to the console:
    print(file_stuff)
# Step 4: The 'with' statement automatically closes the file when it's done,
# ensuring proper resource management and preventing resource leaks.
```

** read content line by line**
1- The 'readlines' method reads the file line by line and stores each line as an element in a list. The order of lines in the list corresponds to their order in the file.
2- The 'readline' method reads individual lines from the file. It can be called multiple times to read subsequent lines.

```
# Looping through lines
while True:
    line = file.readline()
    if not line:
        break  # Stop when there are no more lines to read
    print(line)
file.close()
```

**You can specify the number of characters to read** using the readlines method. For example, reading the first four characters, the next five, and so on.

```
file = open('file.txt', 'r')

# If you want to read characters from a specific position in the file, you can use the seek() method. This method moves the file pointer (like a cursor) to a particular position. The position is specified in bytes, so you'll need to know the byte offset of the characters you want to read.
file.seek(10)  # Move to the 11th byte (0-based index) 

characters = file.read(5)  # Read the next 5 characters
print(characters)
```

another example
```
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
	print(file1.readline(20)) # does not read past the end of line. only the characters within the line
```

** Seek to a position in the file**
```
<file>.seek(0)                      # Moves to the start of the file.
file.tell() - returns the current position in bytes
file.seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end
```

** write to file **
```
# <file>.write(<str/bytes>)           # Writes a string or bytes object.
# <file>.writelines(<list>)           # Writes a list of strings or bytes objects.

# Create a new file Example2.txt for writing
with open('Example2.txt', 'w') as file1:
    file1.write("This is line A\n")
    file1.write("This is line B\n")
    # file1 is automatically closed when the 'with' block exits
	
```

writing multiple lines
```
# List of lines to write to the file
Lines = ["This is line 1", "This is line 2", "This is line 3"]
# Create a new file Example3.txt for writing
with open('Example3.txt', 'w') as file2:
    for line in Lines:
        file2.write(line + "\n")
    # file2 is automatically closed when the 'with' block exits
```

appending
```
# Data to append to the existing file
new_data = "This is line C"
# Open an existing file Example2.txt for appending
with open('Example2.txt', 'a') as file1:
    file1.write(new_data + "\n")
    # file1 is automatically closed when the 'with' block exits
```

copying content from one file to another
```
# Open the source file for reading
with open('source.txt', 'r') as source_file:
    # Open the destination file for writing
    with open('destination.txt', 'w') as destination_file:
        # Read lines from the source file and copy them to the destination file
        for line in source_file:
            destination_file.write(line)
    # Destination file is automatically closed when the 'with' block exits
# Source file is automatically closed when the 'with' block exits
```

writing lines
```
with open('/Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
```

a note on the difference between w+ and r+. Both of these modes allow access to read and write methods, however, opening a file in w+ overwrites it and deletes all pre-existing data.
In the following code block, Run the code as it is first and then run it without the .truncate().
```
with open('/Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0,0)
    print(testwritefile.read())
```

To work with a file on existing data, use r+ and a+. While using r+, it can be useful to add a .truncate() method at the end of your data. This will reduce the file to your data and delete everything that follows.
```
with open('/Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())
```

```
with open('/Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )
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