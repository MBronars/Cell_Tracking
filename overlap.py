import skimage 
import cv2 as cv
from skimage import data, io, filters, measure
from matplotlib import pyplot as plt
from skimage.transform import rescale, resize
from PIL import Image
import numpy as np


""" cellFile - path to the desired cell image which can have multiple regions of interest (ROI)
	protienFile - path to the protien image, can only have one ROI, we are measuring the cells' overlap with this one ROI
	black_background - a boolean which is true when we have white cells/protiens on a black background.  Make sure your cell
		and protien files have the same value for this
"""

def getOverlap(cellFile, protienFile, black_backgound = true):
	#read in images, turn them to grayscale and change them both to the same size
	cell = cv.imread(cellFile)
	cell_gray = cv.cvtColor(cell, cv.COLOR_BGR2GRAY)
	___, cell = cv.threshold(cell_gray, 254, 255, 0)
	protien = cv.imread(protienFile)
	protien_gray = cv.cvtColor(protien, cv.COLOR_BGR2GRAY)
	___, protien = cv.threshold(grayP, 254, 255, 0)
	dim = (400,400)
	cell = cv.resize(cell,dim)
	protien = cv.resize(protien,dim)
	if not black_background:
		#convert image to black background if not already in this format
		cell = cv.bitwise_not(cell)
		protien = cv.bitwise_not(protien)
	#find the outlines for the cells and the protien
	cellContours, ____ = cv.findContours(cell,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
	protienContour, ___= cv.findContours(white_protien,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
	overlaps = []
	for cntr in cellContours:
	#for each cell, calculate it's overlap with the ROI in the protien file
		full_cell = cv.contourArea(cntr)
    	test_protien = protien.copy()
    	cv.fillPoly(test_protien, cntr, color=(255,255,255))
    	test_contour, ____ = cv.findContours(test_protien,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    	extrusion = cv.contourArea(test_contour[0]) - cv.contourArea(contoursP[0]) 
    	overlap_percentage = 1 - extrusion/full_cell
    	#calculate center of the cell
    	M = cv.moments(cntr)
    	cx = int(M['m10']/M['m00'])
    	cy = int(M['m01']/M['m00'])
    	center = (cx,cy)
    	overlaps.append((center,overlap_percentage))
    return overlaps
	