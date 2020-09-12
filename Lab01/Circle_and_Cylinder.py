# Written by Kimjuwon

import math 

class Circle:
    # Constructor
    def __init__(self, radius = 1.0):
        self.radius = radius
        
    # Returns the string representations of an object (Define str())
    def __str__(self):
        return "({})".format(self.radius)
    
    # Returns the outputtable expression string of an object (Define repr())
    def __repr__(self):
        return "Circle(radius = {})".format(self.radius)
    
    # Read area of circle (pi * radius * radius)
    def get_area(self):
        return math.pi * pow(self.radius, 2)
    
class Cylinder(Circle):
    # Constructor
    def __init__(self, radius = 1.0, height = 1.0):
        self.radius = radius
        self.height = height
    
    # Override
    def __str__(self):
        return "({}, {})".format(self.radius, self.height)
    
    # Override
    def __repr__(self):
        return "Cylinder(radius = {}, height = {})".format(self.radius, self.height)
    
    # Read volume of cyilnder (area of circle * height)
    def get_volume(self):
        return self.get_area() * self.height