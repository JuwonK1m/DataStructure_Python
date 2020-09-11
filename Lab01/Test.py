import Functions
import Point
import Circle_and_Cylinder

def test_functions():
    f = Functions.Functions()
    
    # Test is_prime() (1 ~ 100)
    print("<Test is_prime()>")
    for i in range(1, 101):
        if f.is_prime(i):
            print("{} is prime number.".format(i))
    print()
            
    # Test factorial() (1 ~ 20)
    print("<Test factorial()>")
    for i in range(1, 21):
        print("factorial({}) = {}".format(i, f.factorial(i)))
    print()    
        
    # Test fibonacci() (1 ~ 30)
    print("<Test fibonacci()>")
    for i in range(1, 31):
        print("fibonacci({}) = {}".format(i, f.fibonacci(i)))
    print()
    
    # Test getPTriples() (50)
    print("<Test getPTriples()>")        
    f.getPTriples(50)
    print()
    
def test_point():
    # Test str(), repr()
    p1 = Point.Point(1, 2)
    p2 = Point.Point(3, 4)
    print("<Test Point>")
    print("str(p1): " + str(p1))
    print("repr(p1): " + repr(p1))
    print("str(p2): " + str(p2))
    print("repr(p2): " + repr(p2))
    
    # Test '+', '*'
    p3 = p1 + p2
    print("p1 + p2 = " + str(p3))
    p4 = p1 * p2
    print("p1 * p2 = " + str(p4))
    print()
    
def test_circle_and_cylinder():
    # Test Circle str(), repr(), get_area()
    circle = Circle_and_Cylinder.Circle()
    print("<Test Circle>")
    print("str(circle): " + str(circle))
    print("repr(circle): " + repr(circle))
    print("circle area = " + str(circle.get_area()))
    print()
    
    # Test Cylinder str(), repr(), get_volume()
    cylinder = Circle_and_Cylinder.Cylinder()
    print("<Test Cylinder>")
    print("str(cylinder): " + str(cylinder))
    print("repr(cylinder): " + repr(cylinder))
    print("cylinder volume = " + str(cylinder.get_volume()))
    
test_functions()
test_point()
test_circle_and_cylinder()