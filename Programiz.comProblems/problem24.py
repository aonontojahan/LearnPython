# Python program to convert decimal <-> binary and do some random selections
import random

value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))

decimal_num = int(input("Enter a decimal number: "))
binary_str = bin(decimal_num)  # Convert decimal to binary (string with '0b')

bin_input = input("Please enter a valid binary number: ")
decimal_from_bin = int(bin_input, 2)

letters = list('abcdefghijklmnopqrstuvwxyz')

print("The type of the first number you entered is", type(value1))
print("The type of the second number you entered is", type(value2))
print("The binary equivalent of {0} is {1}".format(decimal_num, binary_str))
print("The decimal equivalent of {0} is {1}".format(bin_input, decimal_from_bin))
print("\n")
print("The random letter from the list is", random.choice(letters))
print("The random number from {0} to {1} is {2}".format(10, 20, random.randrange(10, 20)))
