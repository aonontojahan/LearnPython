# Python Program to find the L.C.M. of two input number

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
result = lcm(num1, num2)
print("The L.C.M. of {0} and {1} is {2}".format(num1, num2, result))