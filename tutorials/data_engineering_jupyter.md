# installing jupyter notebook
```
pip install jupyter 
```

# opening jupyter notebooks
1- create a subfolder in the location where you want your notebooks
2- Then just go to that location in your terminal and run the following command:
```
jupyter notebook 
```
3- This will start up Jupyter and your default browser should start (or open a new tab) to the following URL: http://localhost:8888/tree
4- Note that right now you are not actually running a Notebook, but instead you are just running the Notebook server. 

# creating a Jupyter notebook in coursera lab
## renaming a notebook
open file -> rename notebook -> write the new name for the notebook

# creating a Jupyter notebook in your local machine jupyter server and run the first notebook
1- Now that you know how to start a Notebook server, you should probably learn how to create an actual Notebook document.
2- All you need to do is click on the New button (upper right), and it will open up a list of choices. On my machine, I happen to have Python 2 and Python 3 installed, so I can create a Notebook that uses either of these. For simplicity’s sake, let’s choose Python 3. 
3- rename the notebook: Just move your mouse over the word Untitled and click on the text. You should now see an in-browser dialog titled Rename Notebook. Let’s rename this one to Hello Jupyter:
4- note that the kernal for your notebook is python3 
5- Running a cell means that you will execute the cell’s contents. To execute a cell, you can just select the cell and click the Run button that is in the row of buttons along the top. It’s towards the middle. If you prefer using your keyboard, you can just press Shift+Enter.
6- **running all cells in order will help to run everything as a python file. so no need to recreate variables or functions in cells** If you have multiple cells in your Notebook, and you run the cells in order, you can share your variables and imports across cells. This makes it easy to separate out your code into logical chunks without needing to reimport libraries or recreate variables or functions in every cell.
7- the square braces in left of the cell indicates the order in which the cells are executed

# notebooks menus
1- **file menu** in the file menu, the most interesting menu item is the Save and **Checkpoint option**. This allows you to create checkpoints that you can roll back to if you need to.
2- **edit** Next is the Edit menu. Here you can cut, copy, and paste cells. This is also where you would go if you wanted to delete, split, or merge a cell. You can reorder cells here too. some functions in the edit list only applys to cell type, for example not all functions apply to code cell but applys to markdown cell. those not applicable functions will be greyed out if not applyed to the currently selected cell.
3- **view** The View menu is useful for toggling the visibility of the header and toolbar. You can also toggle Line Numbers within cells on or off. This is also where you would go if you want to mess about with the cell’s toolbar.
4- **insert** The Insert menu is just for inserting cells above or below the currently selected cell.
5- **cell** The Cell menu allows you to run one cell, a group of cells, or all the cells. You can also go here to change a cell’s type, although I personally find the toolbar to be more intuitive for that. 
6- **cleaning a cell** The other handy feature in this menu is the ability to clear a cell’s output. If you are planning to share your Notebook with others, you will probably want to clear the output first so that the next person can run the cells themselves.
7- **kernal** The Kernel cell is for working with the kernel that is running in the background. Here you can restart the kernel, reconnect to it, shut it down, or even change which kernel your Notebook is using.
8- **you will need to restart the kernal in debugging** You probably won’t be working with the Kernel all that often, but there are times when you are debugging a Notebook that you will find you need to restart the Kernel. When that happens, this is where you would go.
9- **widget** The Widgets menu is for saving and clearing widget state. Widgets are basically JavaScript widgets that you can add to your cells to make dynamic content using Python (or another Kernel).

# starting terminals and creating files and folders
Starting Terminals and Other Things
Jupyter Notebook also allows you to start more than just Notebooks. You can also create a text file, a folder, or a Terminal in your browser. Go back to the home page that opened when you first started the Jupyter server at http://localhost:8888/tree. Go to the New button and choose one of the other options.

The Terminal is probably the most interesting of the bunch, as it is running your operating systems terminal in the browser. This allows you to run bash, Powershell, and so on in your browser and run any shell command that you might need to there.

**from the file menu -> new -> other things than notebook**

# showing what is running currently 
1- **using running tab to make sure all your data are saved** The Running tab will tell you which Notebooks and Terminals you are currently running. This is useful for when you want to shut down your server but you need to make sure that you have saved all your data. Fortunately, Notebooks auto-save pretty frequently, so you rarely lose data. But it’s good to be able to see what’s running when you need to.

The other nice thing about this tab is that you can go through your running applications and shut them down there.


# running a specific cells
from run list. click run and select run selected cell

# reading list
https://realpython.com/preview/how-to-pandas-pivot-table/

# working on jupyter notebook
## renaming a file 
1- Click File. 
2- Then click Rename Notebook to give the required name. 
3- And you can now start working on your new notebook. 

# to run the whole notebook
click on run up the notebook 

# to run a part of the notebook/ a specific cell in the notebook
1- On the main menu bar at the top, click Run. 
2- In the drop-down menu, click Run Selected Cells to run the current highlighted cells. 
Alternatively, you can use a shortcut, press Shift + Enter. 
In case you have multiple code cells, click Run All cells to run the code in all the cells. 

# adding a new cell 
You can add code by inserting a new cell. 
To add a new cell, click the plus symbol in the toolbar. 

# deleting a cell 
In addition, you can delete a cell. 
Highlight the cell and on the main menu bar, click Edit, and then click Delete Cells. 
Alternatively, you can use a shortcut by pressing D twice on the highlighted cell. 

# moving cells up and down
Also, you can move the cells up or down as required. 

# working with multiple notebooks
Click the plus button on the toolbar and select the file you want to open. 
Another notebook will open. 
Alternatively, you can click File on the menu bar and click 
Open a new launcher or Open a new notebook. 
And when you open the new file, you can move them around. 
For example, as shown, you can place the notebooks side by side. 

# writing code in the notebook
On one notebook, you can assign variable one to the number 1, and variable two to 
the number 2 and then you can print the result of adding the numbers one and two.

# presenting results
As a data scientist, it is important to communicate your results. 
Jupyter supports presenting results directly from the notebooks. 

## creating documentation and presentations 
You can create a Markdown to add titles and text descriptions to help with the flow of the presentation. 
To add markdown, click Code and select Markdown. 
You can create line plots and convert each cell and output 
into a slide or sub-slide in the form of a presentation.
The slides functionality in Jupyter allows you to deliver code, visualization, text, and outputs of the executed code as part of a project.

# shutting down notebooks
Now, when you have completed working with your notebook or notebooks, you can shut them down. 
Shutting down notebooks release their memory. 
Click the stop icon on the sidebar, it is the second icon from the top. 
You can terminate all sessions at once or shut them down individually. 
And after you shut down the notebook session, you will see “no kernel” at the top right. 
This confirms it is no longer active, you can now close the tabs.

