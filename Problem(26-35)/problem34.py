def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n-1)
number = int(input("Enter a positive integer: "))
if number < 0:
    print("Please enter a positive integer")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", number, "is", recur_factorial(number))
    
    