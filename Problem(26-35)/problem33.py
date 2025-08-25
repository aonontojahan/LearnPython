# Python program to find the sum of natural numbers using recursive function

def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)

number = int(input("Enter a positive integer: "))


if number < 0:
    print("Please enter a positive integer")
else:
    print("The sum is", recur_sum(number))
