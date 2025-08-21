# Python program to find H.C.F of two numbers

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
result = hcf(num1, num2)
print("The H.C.F. of {0} and {1} is {2}".format(num1, num2, result))
