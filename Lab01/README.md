# Lab 1
## 1.1 Functions
the Functions class/type that implements the following functions
1. is_prime(n) returns True if the integer is prime.
2. The factorial of a non-negative integer n is written n! (pronounced “n factorial”) and is defined
as follows:
> n! = n × (n − 1) × (n − 2) × ... × 1
3. A function that returns the nth Febonacci term
4. (getPTriples) A right triangle can have sides that are all integers. The set of three integer values
for the sides of a right triangle is called a Pythagorean triple. These three sides must satisfy
the relationship that the sum of the squares of two of the sides is equal to the square of the
hypotenuse. Find all Pythagorean triples for side1, side2 and hypotenuse all no larger than 50.

## 1.2 Point
define a Point class, which models a 2D point with x and y coordinates.
- attribute
  - x:int = 0
  - y:int = 0
- method
  - __init__()
  - __str__():str
  - __repr__():str
  - __add__() (Override to overload '+' operator)
  - __mul__() (Override to overload '*' opdrator)

## 1.3 Circle and Cylinder
define a Cylinder class, as a subclass of Circle. The Cylinder class shall inherit attributes radius
and get_area() from the superclass Circle, and add its own attributes height and get_volume().
- Circle(superclass)
  - attribute
    - radius:float = 1.0
  - method
    - __init__()
    - __str__():str
    - __repr__():str
    - get_area():float
- Cylinder(subclass)
  - attribute
    - height:float = 1.0
  - method
    - __init__()
    - __str__():str
    - __repr__():str
    - get_volume():float
