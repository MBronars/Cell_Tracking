class Cell:
	"""
	A class used to represent a neural stem cell that is updated until cell dies or divides

	...

	Attributes
	__________
	name : str
		A string that holds the name of the cell.  Cells have the same name ass their parent
		plus an additional letter to represent which child they are.  A parent named "ABA"
		that splits into three cells will have children named "ABAA"   "ABAB"  and "ABAC"
		in order to allow easy tracking of cell history.
	pos : ((int, int), double, int)
		This is a tupple that holds the following info about the cell:
			((centroid Xpos, centroid Ypos),overlap_percentage, frame_index)
		That is the returned value from overlap.py
	used : boolean
		A boolean that indicated whether we have already found which location this cell came 
		from in the previous frame.
	gone : boolean
		This is a boolean that flags whether or not the cell is alive.  If it is true, the
		cell is alive and the instance is being updated.  If it is false then the cell has
		either died or divided
	start : int
		This integer indicates the index of the first frame in the image stack where this 
		cell appeared
	history : list
		History is a list of all the positions (as defined above) a cell has been in over
		its lifetime.  This attribute is being updated every frame.

	Methods
	_______
	displayData()
		Prints the cell's position history in a readable manner
	divide(overlaps, name, cells, curr)
		Method called when a cell divides.  Ends the history of the parent cell and makes
		two new cells
	closest(points, point)
		Takes a list of points and returns the one closest to the other point passed in.
	kill(c)
		When a cell dies this method is called to end its history
	"""
    def __init__(self, name, frame, pos):
    	"""
    	Parameters
    	__________
    	name : str
    		A string that holds the name of the cell.	
    	frame : int
			The index of the first frame this cell appears in
    	pos : ((int, int), double, int)
    		This is a tupple that holds the following info about the cell:
				((centroid Xpos, centroid Ypos),overlap_percentage, frame_index)
			That is the returned value from overlap.py
		"""
        self.name = name
        self.last = pos
        self.used = False
        self.gone = False
        self.start = frame
        self.history = [pos]
    def displayData(self):
    	"""
    	Prints the cell's position history in a readable manner.

    	Displays the frames the cell was alive in and the percent overlap that it had in
    	that frame.  Takes this information from self.history
    	"""
        print("Cell " + self.name + ":")
        i = self.start
        for c in self.history:
            print("Frame " + str(i) + ": " + str(c) + "\n")
            i += 1
    def divide(self, overlaps, name, cells, curr):
    	"""
    	Method called when a cell divides.  Ends the history of the parent cell and makes
		two new cells.  No return values.

		Parameters
		__________
		overlaps : list
			Overlap holds a list of positions (as defined above) that were returned from 
			overlap.py
		name : str
			This is the name of the parent cell.  The two cells created during the division
			will have this name plus an A or a B to indicate which child they are.
		cells : list
			Cells is a list of cells that holds every cell that has existed in the current 
			image stack
		curr : int
			Curr is the index of the current frame in the image stack

		"""
            n = "New" + chr(name)
            options = []
            for overlap in overlaps:
                if overlap[2] == curr:
                    options.append(overlap)
            for i in dif:
                close = closest(options, None)
                x = options.pop(close[0])
                y = options.pop(close[1])



            c = Cell(n, curr, overlap[0])
            c.used = True
            cells.append(c)
    def closest(points, point):
    	"""
    	Takes a list of points and returns the one closest to the other point passed in.

    	Parameters
    	__________
    	points : point
    		A list of positions (as defined above)
    	point : ((int, int), double, int)
    		((centroid Xpos, centroid Ypos),overlap_percentage, frame_index)
    		The position tuple returned from overlap.py

    	Returns
    	_______

    	(close1, close2) : (int, int)
    		The indexes of the two closest points
    	"""
        close1 = None
        close2 = None
        best = 999999
        for xi in range(0, len(points)):
            if point != None and xi>0:
                return close2
            for yi in range(0, len(points)):
                x = points[xi]
                if point != None:
                    x = point
                y = points[yi]
                dist = math.sqrt((x[0][0] - y[0][0])**2 + (x[0][1] - y[0][1])**2)
                if dist < best:
                    best = dist
                    close1 = xi
                    close2 = yi
        return (close1, close2)
    def kill(self, c):
    	"""
    	When a cell dies this method is called to end its history

    	Parameters
    	__________
    	c : Cell
    		The cell object that has died.
    	"""
        c.gone = True

 #   def initiate(self, x, cells):
 #       pos = x[0]
 #       c = Cell(chr(name),0,pos)
 #       c.used = True
 #       cells.append(c)
    def match():
    	"""
    	TODO: Write a function that matches cells with their position in the previous frame
    	in a way that minimizes distance traveled
    	"""






