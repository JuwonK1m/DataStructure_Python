# Written by Kimjuwon

class Point:
    # Constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    # Returns the string representations of an object (Define str())
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
    # Returns the outputtable expression string of an object (Define repr())
    def __repr__(self):
        return "Point(x = {}, y = {})".format(self.x, self.y)
    
    # Override to overload '+' operator
    def __add__(self, right):
        point = Point(self.x + right.x, self.y + right.y)
        return point
    
    # Override to overload '*' operator
    def __mul__(self, right):
        point = Point(self.x * right.x, self.y * right.y)
        return point
    
    