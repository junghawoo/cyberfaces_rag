---
title: "Unit 123"
unit_id: 123
---

# Unit 123

## Extracted resources (local files)

### Tool Creation and Publishing Instructions
*Source file:* `toolcreationpublishing_instructions_v3.pdf`  ·  *type:* file

1 
 
 
Jupyter Notebook Tool Creation & Publication 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
School of Civil Engineering, Purdue University 
vmerwade@purdue.edu 
 
FAIR Science in Water Resources
 
 
Objective 
 
The main objective of this tutorial is to create and publish a Jupyter Notebook tool. The first part of 
the tutorial will focus on creating a ipynb file containing the python code for creating widgets like 
textbox and button, and definition blocks to acquire the data, processing, and plot different curves 
(hydrograph and flow duration curve). The second part discusses the tool creation in MyGeoHub, 
adding the files to tool repository and publishing the tool. 
 
Data Source 
 
For the plotting of discharge hydrograph and flow duration curves (including the calculation of 
exceedance probability), the daily streamflow can be obtained from the link: 
https://waterdata.usgs.gov/nwis/sw. In this tutorial, we will use hydrofunctions python package (or 
library or module) library to download streamflow for a USGS station and a time period (we had 
mentioned three methods in data access tutorial:- string operations, pandas package and 
hydrofunctions package). 
 
Instructions 
 
Tool Creation 
1. Log on to mygeohub.org. Navigate to Resources > Tools and launch Jupyter Notebook. 
2. Create 
a 
folder 
structure 
to 
store 
code 
and 
data 
for 
tutorial 
(for 
example: 
/courses/FAIRScience/Pub2 in the home directory). You must first create courses in the home 
directory and so on. 
3. Now, in the FAIR Course Page, click on the notebook file available as shown below.

2 
 
 
Figure 1: Data Access Modules in Course Page 
4. By default, the ipynb file would be in the read-only format. Hit the Save as option available in 
the File menu and save it in the earlier created folder (Pub2). Enter the path as 
“/FAIRScience/Pub2/toolcreation.ipynb” (shown below). Please note that you are saving the 
file in the parent folder “/home/mygeohub/joseph57/courses/” which is not shown by 
default.  
 
Figure 2: "Save as" option in Jupyter Notebook 
5. In order to change the read only state, refresh the browser page (or you can also close and re-
open the ipynb file).  
6. Initially, we have to import the packages required for this tutorial. Other than the packages 
mentioned in the first cell, we need to use ipywidgets package to use the textbox and button 
widgets. Let us complete the first cell for importing the ipywidgets package as is shown below. 
 
Code Block 01 
7. The next two cells in ipynb file indicates two different methods to include a sample image for 
the User Interface (UI) in the appmode. Click on the second cell (which currently in Code cell

3 
 
mode) and specify the URL to sample image (you can copy it from the comment section). Also, 
change it from Code cell to Markdown cell during the dropdown at top menu.  
 
 
Markdown Block 01 
 
The third cell contains another method where you can use a code cell (instead of markdown 
cell) using IPython.display module 
8. The next cell contains two definition blocks for obtaining the daily discharge data from USGS 
(using hydrofunctions package) and plotting the daily discharge hydrograph. The two 
definitions are already given in the code. 
9. Now, let us complete the next cell which will contain three textbox widgets for prompting the 
user to input the station number, starting date and ending date of the analysis period as shown 
below.  
 
Code Block 02 
10. Once you complete the above cell, we need to create a button widget which will obtain the 
data based on the USGS Station number and analysis period. We will initially create a button 
widget and then link the button widget with the earlier two functions

4 
 
(DailyDischargeData_func and DischargeHydrographPlot_func) so that when the button is 
clicked it will execute both the functions and display the results. 
 
Code Block 03 
11. Now, we will again define two functions for calculating the exceedance probability and plotting 
flow duration curve (in linear-linear scale). The two definitions are already given in the file. 
12. In the next cell, we have the code for creating a second button and linking it to the two functions 
(ExceedProb_func and FlowDurCurveLinLin_func) that were defined in the previous cell. 
13. Lastly, we will display the buttons in two different tabs (using a tab container widget) so that 
appears in an organized manner and better use of space. Complete the code as shown below. 
 
Code Block 04 
14. To see the UI mode, click on Appmode on the top menu bar as shown below. It will convert 
notebook into web applications. In this mode, all codes are hidden and markdown is read-only.

5 
 
 
Figure 3: Top Menu Bar containing Appmode option 
The UI view in Appmode contains three textboxes and two buttons for plotting the graphs. 
 
Figure 4: Appmode showing the tool 
15. Let us use a sample input for the three textboxes to check the results (USGS Station: 03335500,  
Start Date: 2017-01-01, End Date: 2017-06-30) 
16. Further, the two buttons will generate the Discharge Hydrograph and Flow Duration Curve as 
shown below for the sample inputs in earlier step. 
 
Figure 5: Plot generated by first button 
 
Figure 6: Plot generated by second button 
 
 
17. Now, save the file in a desired folder using File > Save. Once everything is saved, click on Close 
and Halt.

6 
 
Tool Publication 
18. In the MyGeoHub page, go to Resources > Tools. In the new page, click on Start a new Tool 
option. 
 
Figure 7: Starting a new tool in MyGeoHub 
19. As shown below, add a tool name (choose a unique name to avoid conflict), title and description for 
your the new tool. Change the Publishing Option to Publish as a Jupyter Notebook and leave other 
inputs as default. Click on “Register tool” once you have completed furnishing the required 
details. For this tutorial, we will keep the unique name as “hfdctool”. You may have to select a 
different name.    
 
 
 
Figure 8: Tool Registration in MyGeoHub 
Keep other inputs 
as default.

7 
 
20. Next, you will be directed to the status page which indicates that tool has been created as 
shown below (https://mygeohub.org/tools/<unique_tool_name>/status). We have 
completed the tool registration and creation. 
 
Figure 9: Status page of tool 
21. Now, launch the terminal window in Jupyter Notebook Home Directory by navigating to New 
> Terminal as shown below. Jupyter Notebook Home Directory can be accessed using My Tools 
modules available in Dashboard. [Note: Another way to reach Jupyter Notebook Home Directory is 
by navigating to Resources > Tools > Jupyter Notebook (in Resources drop down) > Launch Tool] 
 
Figure 10: Launching Terminal window in MyGeoHub

8 
 
 
22. Download the tool code/files created by MyGeoHub to your local home directory using “svn” 
command as shown below. The general form of svn command is given by “svn checkout 
https://mygeohub.org/tools/<unique_tool_name>/svn/trunk <unique_tool_name>”. 
 
 
Figure 11: Using svn command in Terminal window 
 
23. Once the command is executed, a new folder named “<unique_tool_name>” will be created in 
the home directory with different files and folders. For this tutorial, we had chosen the unique 
name as hfdctool in the earlier step. 
 
Figure 12: A new folder is created after svn command 
24. Open the newly created folder. The bin folder (inside the newly created folder) is assigned 
location for ipynb file (containing the python code), data folder is for any relevant data, and 
middleware contains the invoke script file. 
25. Now, create a copy of ipynb file (that was completed in the first part of the tutorial) using 
Duplicate button in the folder where the ipynb file was saved in Step 17 and move to bin folder 
using Move button. First, select the file and click Duplicate so that you have the original file. 
Then, transfer the new file from the working folder to bin folder of the tool as shown below 
using Move. (Note: if you do not see Duplicate and Move, you have to select the file and hit 
Shutdown as the Close and Halt option in Step 17 was not done properly). Also, rename the file 
as “toolcode.ipynb” (or you can choose an appropriate name).

9 
 
 
Figure 13: Moving a file using directory path input 
 
Figure 14: Renaming a file 
26. Next, we have to change the invoke script in middleware folder. Go to “middleware” folder in 
tool folder and change the sample code in “invoke” as the shown below. 
 
Figure 15: "Invoke" script using tool 
 
27. Now, we will add the changes to MyGeoHub Subversion Repository by using svn add … and 
svn commit … commands. First, in the terminal window, change the directory to the tool folder 
using the command “cd <folder name>” as shown below.

10 
 
 
Figure 16: Changing to different folder in Terminal window 
28. Next, we have to upload the newly added files to remote repository using “svn add <filename 
to be added with path>” and commit the changes as a version using “svn commit -m <commit 
message>” as shown below. You need to enter the password (MyGeoHub Account) for changes 
to take place. 
 
Figure 17: Adding and Committing the changes to repository 
 
29. (This step should not be done during the workshop as admin will receive a lot of review 
requests at a time) Now, you have to request for review by the admin to publish your tool. 
Navigate to the tool status page: 
(https://mygeohub.org/tools/<unique_tool_name>/status) or navigate to Dashboard > My Drafts > 
<unique_tool_name>. 
 
 
Figure 18: Accessing the dashboard

11 
 
 
Figure 19: Dashboard Module showing the drafts 
30. In the status page, request for review by admin by clicking on “My code is committed, working, 
and ready to be installed”. 
 
Figure 20: Tool status page 
31. Normally, it will take three business days for the admin to approve the request.  
32. You can also get a reference entry for your tool from the About page. The About page can be 
accessed at https://mygeohub.org/tools/<unique_tool_name>. For example, the reference 
entry for this tool is “Jibin Joseph and Venkatesh M Merwade (2021), "Hydrograph and FDC 
Plotting Tool," https://mygeohub.org/resources/hfdctool”. Similarly, you can obtain a reference 
entry for your tool created in Jupyter Notebook from above mentioned page.  
 
Ok, you have completed the tutorial! 
 
 
Last Revised: 2021/06/02
