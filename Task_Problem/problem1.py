#Finding the summation of a factorial number 
#using recursive function
import math

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n* factorial(n - 1)
    
number = int(input("Please enter a number : "))
print("Your entered number is ", number)

result = factorial(number)
print("Factorial of ",number, "is", result)