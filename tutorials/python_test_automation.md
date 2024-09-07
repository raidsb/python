# references
https://nose2.readthedocs.io/

# reading list 
https://realpython.com/python-cli-testing/ 
https://realpython.com/python-doctest/
https://mathspp.com/blog/til/better-test-parametrisation-in-pytest 
https://www.travis-ci.com/
https://realpython.com/python-continuous-integration/ 
https://realpython.com/python-code-quality/ 
https://lukeplant.me.uk/blog/posts/pyastgrep-and-custom-linting/ 
https://www.bitecode.dev/p/testing-with-python-part-6-fake-it mocking 
https://realpython.com/preview/ruff-python/ # new linter

# Top test automation libraries in python
Here are 23 libraries you'll find in this guide for why Python is so awesome:
* Selenium: Selenium is the industry standard when it comes to browser-based automation.
* Playwright
* Splinter
* Robot Framework
* Behave
* Requests
* Tavern
* Hypothesis
* Pywinauto
* RPA Python
* Beautiful Soup
* NumPy
* PyTest
* TensorFlow
* PDFMiner
* Pyjest
* Locust
* PyBuilder
* Pandas
* Coverage.py
* PyUnit
* PyCharm
* Faker

# Manual testing
To have a complete set of manual tests, all you need to do:
* is make a list of all the features your application has, 
* the different types of input it can accept, 
* and the expected results. 
Now, every time you make a change to your code, you need to go through every single item on that list and check it.

# automated testing terminology
* automated testing:  Automated testing is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human

* test step: Think of how you might test the lights on a car. You would turn on the lights (known as the test step) 
* test assertion: and go outside the car or ask a friend to check that the lights are on (known as the test assertion). Testing multiple components is known as integration testing.
* integration test challenge: A major challenge with integration testing is when an integration test doesn’t give the right result. It’s very hard to diagnose the issue without being able to isolate which part of the system is failing. If the lights didn’t turn on, then maybe the bulbs are broken. Is the battery dead? What about the alternator? Is the car’s computer failing?
* A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.
* so now, there are two types of tests, unit and integration test: An integration test checks that components in your application operate with each other. A unit test checks a small component in your application.

# python supports writing both unit and integration test
example of unit test. using assertion to test the output of a function
```
>>> assert sum([1, 2, 3]) == 6, "Should be 6"

# if the essertion is not correct, it will fail:
>>> assert sum([1, 1, 1]) == 6, "Should be 6"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be 6

```

the simplest form of a unittest is to put the the unittests in a file:
```
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
```

calling it in the shell
```
$ python test_sum.py
```

# test runners 
The test runner is a special application designed for running tests, checking the output, and giving you tools for debugging and diagnosing tests and applications.

the three most popular test runners are:
* unittest
* nose or nose2
* pytest

# unittest 
unittest contains both a testing framework and a test runner. unittest has some important requirements for writing and executing tests.

unittest requires that:
* You put your tests into classes as methods
* You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement

```
# To convert the earlier example to a unittest test case, you would have to:

import unittest # 1 - Import unittest from the standard library

class TestSum(unittest.TestCase): # 2 - Create a class called TestSum that inherits from the TestCase class

	# 3 - Convert the test functions into methods by adding self as the first argument
    def test_sum(self):
		# 4 - Change the assertions to use the self.assertEqual() method on the TestCase class
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
	# Change the command-line entry point to call unittest.main()
    unittest.main()

# calling cmdline in the shell
python test_sum_unittest.py

```

How does it work?
In Python's unittest framework, the unittest.main() function is a utility that provides a command-line interface to run tests. When unittest.main() is called, it performs the following steps:

1. Discovering Test Cases: unittest.main() scans the current module for any classes that inherit from unittest.TestCase. It collects all the test methods (those whose names start with test) from these classes.
2. Creating a Test Suite: It then creates a test suite, which is a collection of test cases to be run. The test suite includes all the discovered test methods.
3. Running the Tests: unittest.main() creates a test runner, which is responsible for executing the tests in the test suite. The test runner runs each test case and reports the results.
4. Reporting the Results: After running all the tests, the test runner outputs a summary of the results, including any failed or erroneous tests.

# nose 
You may find that over time, as you write hundreds or even thousands of tests for your application, it becomes increasingly hard to understand and use the output from unittest.

```
$ pip install nose2 # install nose2, the one compatible with python 3. 
$ python -m nose2   # 
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

more information about nose2?
* python -m nose2 is a command used to run the nose2 test discovery and runner tool for Python. nose2 is a testing framework that extends Python's built-in unittest framework, providing additional features and capabilities to make writing and running tests easier.

Here's a breakdown of the command: python -m nose2
* python: This invokes the Python interpreter.
* -m: This flag tells Python to run a module as a script.
* nose2: This is the name of the module to run. nose2 will discover and run tests in your project.
* When you run python -m nose2, the following typically happens:
	* Test Discovery: nose2 will automatically discover test modules and test functions in your project. By default, it looks for files and directories that match patterns like test*.py.
	* Running Tests: Once discovered, nose2 runs the tests and collects results.
	* Reporting: nose2 provides a summary of the test results, including how many tests passed, failed, or were skipped.

Benefits of Using nose2
* Extended Functionality: nose2 provides many plugins for additional functionality such as coverage reporting, test tagging, and more.
* Compatibility: nose2 is compatible with unittest-based tests, so you can use it with existing unittest test cases without modification.
* Configurability: You can customize test discovery, execution, and reporting through configuration files or command-line options.

Comparison to unittest
The built-in unittest module requires you to manually call test cases, typically via unittest.main() in a script. While this works well, nose2 simplifies and enhances the process, particularly for larger projects or more complex testing needs.

# pytest 
main advantages of using pytest 

* Support for the built-in assert statement instead of using special self.assert*() methods
* Support for filtering for test cases
* Ability to rerun from the last failing test
* An ecosystem of hundreds of plugins to extend the functionality

```
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
```

cmdline to run pytest in powershell
```
# in the terminal in the main folder of the project
> pytest

# to run a specific test file
> pytest tests\test_login_page.py

# to run a specific test in a test File
> pytest tests\test_login_page.py::test_name
```
# writing first test case
1. Create a new project folder and, inside that, create a new folder called my_sum. Inside my_sum, create an empty file called __init__.py. Creating the __init__.py file means that the my_sum folder can be imported as a module from the parent directory.

Your project folder should look like this:

```
project/
│
└── my_sum/
    └── __init__.py
```

2. write an implementation of a function to test

```
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total
```

3.  can create a folder called tests/ and split the tests into multiple files. 
4. It is convention to ensure each file starts with test_ so all test runners will assume that Python file contains tests to be executed. 
5. Some very large projects split tests into more subdirectories based on their purpose or usage.

** Before you dive into writing tests, you’ll want to first make a couple of decisions:**
1. What do you want to test?
2. Are you writing a unit test or an integration test?

** Then the structure of a test should loosely follow this workflow:**
1. Create your inputs
2. Execute the code being tested, capturing the output
3. Compare the output with an expected result
4. For this application, you’re testing sum(). There are many behaviors in sum() you could check, such as:
	1. Can it sum a list of whole numbers (integers)?
	2. Can it sum a tuple or set?
	3. Can it sum a list of floats?
	4. What happens when you provide it with a bad value, such as a single integer or a string?
	5. What happens when one of the values is negative?
	
** most common asserts **
.assertEqual(a, b)	a == b
.assertTrue(x)	bool(x) is True
.assertFalse(x)	bool(x) is False
.assertIs(a, b)	a is b
.assertIsNone(x)	x is None
.assertIn(a, b)	a in b
.assertIsInstance(a, b)	isinstance(a, b)

# side effects 
Side Effects
When you’re writing tests, it’s often not as simple as looking at the return value of a function. Often, executing a piece of code will alter other things in the environment, 
* such as the attribute of a class, a file on the filesystem, or a value in a database. 
* These are known as side effects and are an important part of testing. 
* Decide if the side effect is being tested before including it in your list of assertions.

If you find that the unit of code you want to test has lots of side effects, you might be breaking the Single Responsibility Principle.
Breaking the Single Responsibility Principle means the piece of code is doing too many things and would be better off being refactored. 
Following the Single Responsibility Principle is a great way to design code that it is easy to write repeatable and simple unit tests for, and ultimately, reliable applications.

# ways of calling the unit tests
* 1 - for unittest test cases
```
if __name__ == '__main__':
    unittest.main()
	
# and then called this way:
> python test.py
```

* 2 - another way to run the tests
```
$ python -m unittest test

# remember the m tells python to run a module as a script

# verbose option
$ python -m unittest -v module_name 
```

* 3 - using discover will make unittest search in the current directory for files test*.py and attempt to run them 
```
$ python -m unittest discover

# providing -s will help to search only in a dir
$ python -m unittest discover -s tests
```

* 4 - using -t to tell unittest to run tests only for module inside a dir for example src
```
if your source code is not in the directory root and contained in a subdirectory, for example in a folder called src/, you can tell unittest where to execute the tests so that it can import the modules correctly with the -t flag:

$ python -m unittest discover -s tests -t src
```

# Fixture 
It’s not always as easy as creating a static value for the **input** like a string or a number. Sometimes, your application will require ** an instance of a class or a context** The data that you create as an input is known as a fixture. It’s common practice to create fixtures and reuse them.

# parameterization
If you’re running the same test and ** passing different values each time and expecting the same result** , this is known as parameterization.

# Handling Expected Failures
Earlier, when you made a list of scenarios to test sum(), a question came up: What happens when you provide it with a bad value, such as a single integer or a string?

In this case, you would expect sum() to throw an error. When it does throw an error, that would cause the test to fail.

There’s a special way to handle expected errors. You can use .assertRaises() as a context-manager, then inside the with block execute the test steps:

```
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()
```

# Isolating Behaviors in Your Application
Earlier in the tutorial, you learned what a side effect is. Side effects make unit testing harder since, each time a test is run:
* it might give a different result, 
* or even worse, one test could impact the state of the application and cause another test to fail!

** How to solve side effects? **
There are some simple techniques you can use to test parts of your application that have many side effects:

* Refactoring code to follow the Single Responsibility Principle
* Mocking out any method or function calls to remove side effects
* Using integration testing instead of unit testing for this piece of the application 

If you’re not familiar with mocking, see Python CLI Testing for some great examples.

# Integration testing
Integration testing is the testing of multiple components of the application to check that they work together. Integration testing might require acting like a consumer or user of the application by:
* Calling an HTTP REST API
* Calling a Python API
* Calling a web service
* Running a command line

Each of these types of integration tests can be written in the same way as a unit test, following the Input, Execute, and Assert pattern. The most significant difference is that integration tests are checking more components at once and therefore will have more side effects than a unit test. Also, integration tests will require more fixtures to be in place, like a database, a network socket, or a configuration file.

This is why it’s good practice to separate your unit tests and your integration tests. The creation of fixtures required for an integration like a test database and the test cases themselves often take a lot longer to execute than unit tests, so you may only want to run integration tests before you push to production instead of once on every commit.

A simple way to separate unit and integration tests is simply to put them in different folders:

```
project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    ├── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        ├── __init__.py
        └── test_integration.py
```

calling only integration test folder: $ python -m unittest discover -s tests/integration

# Testing Data-Driven Applications
Many integration tests will require backend data like a database to exist with certain values. For example, you might want to have a test that checks that the application displays correctly with more than 100 customers in the database, or the order page works even if the product names are displayed in Japanese.

These types of integration tests will depend on different test fixtures to make sure they are repeatable and predictable.

A good technique to use is to store the test data in a folder within your integration testing folder called fixtures to indicate that it contains test data. Then, within your tests, you can load the data and run the test.

Here’s an example of that structure if the data consisted of JSON files:

project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    └── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        |
        ├── fixtures/
        |   ├── test_basic.json
        |   └── test_complex.json
        |
        ├── __init__.py
        └── test_integration.py

```
import unittest


class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='fixtures/test_basic.json') # loading a fixture (a non-primitive data to be used in the testing)

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, "Org XYZ")
        self.assertEqual(customer.address, "10 Red Road, Reading")


class TestComplexData(unittest.TestCase):
    def setUp(self):
        # load test data
        self.app = App(database='fixtures/test_complex.json') # loading fixtures

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 10000)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=9999)
        self.assertEqual(customer.name, u"バナナ")
        self.assertEqual(customer.address, "10 Red Road, Akihabara, Tokyo")

if __name__ == '__main__':
    unittest.main()
```

# Testing across multiple platforms/environments
Testing in Multiple Environments
So far, you’ve been testing against a single version of Python using a virtual environment with a specific set of dependencies. 
You might want to check that your application works on multiple versions of Python, or multiple versions of a package. 
Tox is an application that automates testing in multiple environments.

## Tox
** what is tox **
tox is a popular automation tool for testing and managing multiple Python environments. It is particularly useful for running tests across different Python versions and ensuring that your code works consistently across various environments. Here’s a detailed overview of what tox is and what it is used for:
1. Automation Tool: tox automates the testing process, allowing you to run your tests in different environments without having to manually set them up each time.
2. Environment Management: It manages virtual environments for you, handling the installation of dependencies and the setup of different Python versions.
3. Continuous Integration (CI): tox is often used in CI/CD pipelines to ensure code quality and compatibility across multiple Python versions and dependency sets.

$ pip install tox # to install tox for python 

** Configuring Tox for Your Dependencies **
Tox is configured via a configuration file in your project directory. The Tox configuration file contains the following:
1. The command to run in order to execute tests
2. Any additional packages required before executing
3. The target Python versions to test against

```
$ pip install tox
$ tox-quickstart # to get a quick application of tox instead of having the tox syntax
```

** Key Features **
Multi-environment Testing:
1. Run tests in multiple Python environments (e.g., Python 3.6, 3.7, 3.8).
2. Test with different sets of dependencies.
Dependency Management:
Specify dependencies for each test environment.
Isolate dependencies to avoid conflicts.
3. Integration with CI Tools:
Easily integrates with CI tools like Jenkins, Travis CI, GitHub Actions, etc.
4. Custom Commands:
Define custom commands to run before or after tests.
Automate other tasks, such as building documentation or running linters.

** How tox Works **
tox works by reading a configuration file (tox.ini) where you define the environments, dependencies, and commands to run. Here’s a breakdown of the typical workflow:
1. Configuration (tox.ini): Define the environments, dependencies, and commands.
2. Environment Setup: tox creates virtual environments as specified.
3. Dependency Installation: Installs the dependencies in each environment.
4. Command Execution: Runs the specified commands (e.g., tests) in each environment.

** directory structure **
```
my_project/
    my_module/
        __init__.py
        example.py
    tests/
        test_example.py
    setup.py
    tox.ini
```

** example of tox with different environments different dependencies **
```
[tox]
envlist = py36, py37, py38

[testenv]
commands = pytest

[testenv:py36]
basepython = python3.6
deps =
    pytest
    requests

[testenv:py37]
basepython = python3.7
deps =
    pytest
    numpy

[testenv:py38]
basepython = python3.8
deps =
    pytest
    pandas
```

** executing tox **
```
$ tox -e py36 # run for a single environment 
$ tox -r # Recreate the virtual environments, in case your dependencies have changed or site-packages is corrupt:
$ tox -q # Run Tox with less verbose output: 
$ tox -v # Running Tox with more verbose output
```

# automating testing
 Automated testing tools are often known as CI/CD tools, which stands for “Continuous Integration/Continuous Deployment.” They can run your tests, compile and publish any applications, and even deploy them into production.
 
example of CI/CD yml file content:
```
language: python
python:
  - "2.7"
  - "3.7"
install:
  - pip install -r requirements.txt
script:
  - python -m unittest discover
```

Once you have committed and pushed this file, Travis CI will run these commands every time you push to your remote Git repository. You can check out the results on their website.

# Linters
Tools that improve the quality of your application. A linter will look at your code and comment on it. It could give you tips about mistakes you’ve made, correct trailing spaces, and even predict bugs you may have introduced.

# Testing for Performance Degradation Between Changes
There are many ways to benchmark code in Python. The standard library provides the timeit module, which can time functions a number of times and give you the distribution. This example will execute test() 100 times and print() the output:

```
def test():
    # ... your code

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=100))
```

Another option, if you decided to use pytest as a test runner, is the pytest-benchmark plugin. This provides a pytest fixture called benchmark. You can pass benchmark() any callable, and it will log the timing of the callable to the results of pytest.

You can install pytest-benchmark from PyPI using pip:
```
$ pip install pytest-benchmark
```

Then, you can add a test that uses the fixture and passes the callable to be executed:

def test_my_function(benchmark):
    result = benchmark(test)
Execution of pytest will now give you benchmark results:

Pytest benchmark screenshot
More information is available at the Documentation Website.

Testing for Security Flaws in Your Application
Another test you will want to run on your application is checking for common security mistakes or vulnerabilities.

You can install bandit from PyPI using pip:

$ pip install bandit
You can then pass the name of your application module with the -r flag, and it will give you a summary:

$ bandit -r my_sum
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.5.2
Run started:2018-10-08 00:35:02.669550

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 5
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
        Total issues (by confidence):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
Files skipped (0):
As with flake8, the rules that bandit flags are configurable, and if there are any you wish to ignore, you can add the following section to your setup.cfg file with the options:

[bandit]
exclude: /test
tests: B101,B102,B301
More details are available at the GitHub Website.

