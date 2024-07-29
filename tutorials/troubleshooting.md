# importing a library/module not found
Given your project structure:

```
my_project/
    dummy_proj/
        my_module.py
    dummy_test/
        script.py
```

You want to run script.py and import my_module from dummy_proj. Here's how to ensure that script.py can correctly import my_module:

** Method 1: Adjust sys.path in script.py **
Modify script.py to add the parent directory of dummy_proj to sys.path:

```
# in script.py
import sys
import os

# Add the parent directory of dummy_proj to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dummy_proj')))

import my_module

print("Module imported successfully")
```

** Method 2: Use Environment Variable PYTHONPATH **
Set the PYTHONPATH environment variable to include the dummy_proj directory. This can be done in PowerShell:

``` 
# in power shell
$env:PYTHONPATH = "path\to\my_project\dummy_proj"
python path\to\my_project\dummy_test\script.py
```

** Method 3: Run as a Module **
Run script.py as a module from the my_project directory:

```
# in powershell 
cd path\to\my_project
python -m dummy_test.script
```

for this method to work, make sure of these following:
1. Create __init__.py Files: Add __init__.py files to dummy_proj and dummy_test.
2. Navigate to my_project Directory: Open PowerShell and change to the root project directory.
3. Run as Module: Use the -m option to run the script: python -m tests.testsum 

