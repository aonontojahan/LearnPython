class Reactangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
rect = Reactangle(length, width)
print(f"Area of the rectangle: {rect.area()}")
print(f"Perimeter of the rectangle: {rect.perimeter()}")