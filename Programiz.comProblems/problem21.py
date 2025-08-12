#python program to sum of the natural numbers
number = int(input("Please enter the value for ending number: "))

if number <0:
    print("Please enter a positive number")
else:
    total = 0
    for i in range(1, number + 1):
        total += i
print("The sum fo the natural numbers from 1 to {0} is:".format(number), total)

