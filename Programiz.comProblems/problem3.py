'''Define a function that takes three integers as input representing the coefficients of a quadratic equation.
Return the roots of the quadratic equation.
Hint: The quadratic formula is x = [-b ± sqrt(b^2 - 4ac)] / (2a).
The term inside the square root, b^2 - 4ac, is called the discriminant.
If it's positive, there are two real roots.
If it's zero, there's one real root.
If it's negative, there are two complex roots'''
import cmath

a =int(input("Please enter value for a :"))
b =int(input("Please enter value for b :"))
c =int(input("Please enter value for c :"))

discriminant = b**2 - 4*a*c

solution1 = (-b + cmath.sqrt(discriminant)) / (2*a)
solution2 = (-b - cmath.sqrt(discriminant)) / (2*a)

print("There have two possible solution")
print("Solution 1 : ",solution1)
print("Solution 2 : ",solution2)