#Import the necessary packages
import skimage 
import cv2 as cv
from skimage import data, io, filters, measure
from matplotlib import pyplot as plt
from skimage.transform import rescale, resize
from PIL import Image
from PIL import ImageSequence
import numpy as np


"""INPUTS:
	cellFile (string)- path to the desired cell image which can have multiple regions of interest (ROI)
	proteinFile (string)- path to the protein image, can only have one ROI, we are measuring the cells' overlap with this one ROI
	black_background (boolean)- a boolean which is true when we have white cells/proteins on a black background.  Make sure your cell
		and protein files have the same value for this
"""

"""RETURNS:
		A list of tupples containing ((centroid Xpos, centroid Ypos),overlap_percentage) for every cell in the images returned by cellFile.
		Here a centroid is the center of a cell and overlap_percentage if the percentage of the cell that overlaps with the region of interest 
		calculated from the image returned by proteinFile
"""

def getOverlap(cellFile, proteinFile, black_background = True):
	#read in the protein image and save it as cell, then convert to greyscale for more effective threshhold
	#when thresholding, anything that isn't completely white is marked as black and 
	#we only care about the resulting thresholded cell so we discard the rest of the information by saving it as ____
	protein = cv.imread(proteinFile)
	protein_gray = cv.cvtColor(protein, cv.COLOR_BGR2GRAY)
	___, protein = cv.threshold(protein_gray, 254, 255, 0)

	#Load in the image from cellFile
	img = Image.open(cellFile)

	#Initialize an empty list that will hold the (centroid location, percent overlap) tupple for 
	#every cell in the cell image
	overlaps = []
	
	#This loop goes through every image in the stack passed in with cellFile and calculates cell centroids and percent ovelap.  
	#If cellFile is a single image it will go through this loop once 
	for (ii,frame) in enumerate(ImageSequence.Iterator(img)):

		#Grab the correct image from the stack and save it to cell as a numpy array 
		img.seek(ii)
		cell = np.array(img)

		#Convert cell to grayscale in the same manner we used for the protien above
		cell_gray = cv.cvtColor(cell, cv.COLOR_BGR2GRAY)
		___, cell = cv.threshold(cell_gray, 254, 255, 0)

		#Here we resize both the cell and the protein images to the same dimention, this ensures that 
		#the following calculations wont error.  The choice of (400,400) is arbitrary but it should be square
		dim = (400,400)
		cell = cv.resize(cell,dim)
		protein = cv.resize(protein,dim)

		#Converts the cell and protein images to white objects on a black background if they are 
		#not already in this format
		if not black_background:
			cell = cv.bitwise_not(cell)
			protein = cv.bitwise_not(protein)


		#Find contours for both the cell and protein.  This gives us an outline around our regions 
		#of interest that we can now perform calculations on
		#cell = cell.astype(np.uint8)
		cellContours, ____ = cv.findContours(cell,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
		proteinContour, ___= cv.findContours(protein,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

		

		#This loop goes through each cell in the cell image and calculates what percentage of that cell 
		#is located in the protein region
		for cntr in cellContours:
			#calculate area of the cell
			full_cell = cv.contourArea(cntr)

			#fill in the cell contour and overlay it on the protein image
			test_protein = protein.copy()
			cv.fillPoly(test_protein, cntr, color=(255,255,255))

			#Create a contour for this overlay image that includes the full protein and any part of the 
			#cell not overlapping with the protein
			test_contour, ____ = cv.findContours(test_protein,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

			#Calculate the area of the cell not overlapping the protein.  Use this value and the full area 
			#calculated at the start of the loop
			#to generate the overlap_percentage
			extrusion = cv.contourArea(test_contour[0]) - cv.contourArea(proteinContour[0]) 
			overlap_percentage = 1 - extrusion/full_cell

			#calculate the centroid of the cell
			M = cv.moments(cntr)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			center = (cx,cy)

			#add a tuple containing the (centroid location, precent overlap) for this particular cell and 
			#add it to the list generated before the start of the loop
			overlaps.append((center,overlap_percentage,ii))

	#return our list of tupples
	return overlaps
	