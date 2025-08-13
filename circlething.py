# circlething.py
# This script defines a Circle class with methods to calculate area and perimeter.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius * self.radius
        
    def perimeter(self):
        return 2 * math.pi * self.radius
        
r = float(input("Enter radius: "))
c = Circle(r)

print("Area:", c.area())
print("Perimeter:", c.perimeter())