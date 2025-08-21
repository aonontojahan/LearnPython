# Python program to swap two variables

number1 = int(input("Please enter a input for number 1: "))
number2 = int(input("Please enter a input for number 2: "))

temp = number1
number1 = number2
number2 = temp

print("The value of number 1 after swapping: {}".format(number1))
print("The value of number 2 after swapping: {}".format(number2))