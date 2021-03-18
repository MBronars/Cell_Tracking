# Sohn
Image Processing for Dr. Sohn's Neural Stem Cell Data

As of 8/23/2020 
This folder holds the most current scripts for the 

**cellClass.py:**
This class holds all of the functions and operations that are required by cells.  This file is a work in progress and is being added to as more functionallity is desired.  cellClass.py is an import for the Cell Tracker notebook.  The functions in this file include the following.
* _displayData:_ Prints the information about the cell's history in a readable manner.
* _divide:_ Method still in progress.  Ends the history of one cell, starts two new cells.
* _closest:_ Calculated the closest two living cells
* _kill:_  Ends a cells history

overlap.py:
	The only thing in this file is the function getOverlap.  With this function we can determine the percentage of overlap each cell has with each protein.
	INPUTS:
		cellFile (string)- path to the desired cell image which can have multiple regions of interest (ROI).  Can be a single image
			or an image stack
		proteinFile (string)- path to the protein image, can only have one ROI, we are measuring the cells' overlap with this one ROI
		black_background (boolean)- a boolean which is true when we have white cells/proteins on a black background.  Make sure your cell
			and protein files have the same value for this
	RETURNS:
		A list of tupples containing ((centroid Xpos, centroid Ypos),overlap_percentage, frame_index) for every cell in the images returned by cellFile.
		Here a centroid is the center of a cell and overlap_percentage if the percentage of the cell that overlaps with the region of interest 
		calculated from the image returned by proteinFile.  Frame is the index of the image in the stack that the cell comes from (0 if 
		working with a single image).

runner.py:
	Currently this file only has a main function that runs getOverlap on our test stack.  In general this is where we will run the finalized functions on our test data.  The next step will be to test out the code in the Cell Tracker notebook once the bugs get worked out.

Images:
	This file holds all of the images and image stacks that are called by the notebooks and runner.py

Notebooks:
Python notebooks were used for testing out the code and all of the functions.  Final versions of the functions will not be found in these notebooks but they have good visual aids that can assist with the understanding of the code.  This is also where new functionallity is being developed and bugs are being worked out.

ROI Overlap:
	Our goal is to be able to process image stacks where a Region of Interest (ROI) diliniates every stem cell in each image.  The pertinant information to gather is the percent of each cell that overlaps each protien, and this notebook goes through the steps of how we gather this information.  This notebook is the basis for the function "getOverlap" that is in the overlap.py file.  Because that function is finalized this notebook is essentially closed.
Centroid Tracker:
	A working tracker script that does not make use of the Cell Class.  Works for a simple test stack, but cannot handle the full range of possibilities for the data set (fails on a variety of edge cases).  A good start but obsolete at this point.  Moving forward with the project we will be using the Cell Class so this notebook is now closed.  
KLC PIL:
	A notebook make by Kristen that serves as a tutorial for using PIL and working with image stacks in python.
cellClass:
	The first itteration of the cell class.  Old and out of date, cannot import from a python notebook so all meaningful changes are made to the .py file.  This notebook is closed and is no longer being updated.
Cell Tracker:
	This notebook is where I am testing out code for a tracking script that makes use of the Cell Class.  Currently the most up to date version of this code.  This notebook is a work in progress as bugs are still being worked out as we ensure that we can handle all of the edge cases.
Minimum Distance Solution:
	In order to keep the tracking algorithm robust, we need to find which arrangement of cells requires the least amount of movement between frames.  We call this the Minimum Distance Solution and this notebook holds all of the functions that are required to run this algorithm.  This notebook is currently being updated, I am working out bugs in the Match function which pairs off cells in a current frame to cells in the preceding frame (based off of the minimum distance solution).  Currently there are completed helper functions in this notebook including the following.
		Closest: Takes a target point and a list of other points.  Finds the nearest neighbor in the list to that target point.  
		Distance: Takes two points (tupple).  Calculates the distance between those two points. 
		checkDuplicates: Takes a list as input, returns another list that holds any duplicates.


FUTURE WORK:
	Future wo




	 



