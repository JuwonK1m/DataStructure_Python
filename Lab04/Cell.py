class Cell:
    def __init__(self, r = 0, c = 0):
        self.row = r
        self.col = c
        
    def __str__(self):
        return "(" + str(self.row) + ", " + str(self.col) + ")"