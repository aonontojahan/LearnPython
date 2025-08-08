#find the factorial of a number

print("The system is printing the factorial of a number. Please follow the instruction")
def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial (x-1))
number = int(input("Please enter the number for which you want to see the factorial value : "))
result = factorial(number)
print("The factorial of {0} is  {1}".format(number,result))
    