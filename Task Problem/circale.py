import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle with radius: {self.radius}, Area: {self.area():.2f}, Circumference: {self.circumference():.2f}"
    
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"Area of the circle: {circle.area():.2f}")
print(f"Circumference of the circle: {circle.circumference():.2f}")