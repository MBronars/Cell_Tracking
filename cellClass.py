class Cell:
    def __init__(self, name, frame, pos):
        self.name = name
        self.last = pos
        self.used = False
        self.gone = False
        self.start = frame
        self.history = [pos]
    def displayData(self):
        print("Cell " + self.name + ":")
        i = self.start
        for c in self.history:
            print("Frame " + str(i) + ": " + str(c) + "\n")
            i += 1
    def divide(self, overlaps, name, cells, curr):
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
    def die(self, c):
        c.gone = True
    def initiate(self, x, cells):
        pos = x[0]
        c = Cell(chr(name),0,pos)
        c.used = True
        cells.append(c)
