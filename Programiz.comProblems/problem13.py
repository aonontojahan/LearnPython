# Python program to find the largest number among the three input numbers

number1 = int(input("Please enter first number : "))
number2 = int(input("Please enter second number : "))
number3 = int(input("Please enter third number : "))

if (number1 > number2) and (number1 > number3):
    print("{0} is the largest number".format(number1))
elif (number2 > number1) and (number2 > number3):
    print("{0} is the largest number".format(number2))  
else:
    print("{0} is the largest number".format(number3))
   