class Cell:
    def __init__(self, name, frame, pos):
        self.name = name
        self.last = pos
        self.used = False
        self.gone = False
        self.start = frame
        self.history = []
        history.append(pos)
    def displayData(self):
        print("Cell " + self.name + ":")
        i = self.start
        for c in self.history:
            print("Frame " + i + ": " + c)
        