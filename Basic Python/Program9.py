# nested if statement
print("Finding the greater number among three number")
print("Using Nested if/else")
number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))

if number1 > number2:
    if number1 > number3:
        print("The greatest number is ", number1)
    else:
        print("The greatest number is ", number3)

else:
    if number2 > number3:
        print("The greatest number is ", number2)
    else:
        print("The greatest number is ", number3)
