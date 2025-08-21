# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number

number = int(input("Please enter an integer number : "))
if (number%2) == 0:
    print("{0} is a even number".format(number))
else:
    print("{0} is a odd number".format(number))