#Checking armstrong number 
upper = int(input("Enter the upper limit: "))
lower = int(input("Enter the lower limit: "))
print("These are Armstrong numbers between {0} and {1}".format(lower, upper))

for number in range(lower, upper + 1):
    times = len(str(number))
    
    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** times
        temp //= 10
    if number == total:
        print(number)
# This code checks for Armstrong numbers in a given range