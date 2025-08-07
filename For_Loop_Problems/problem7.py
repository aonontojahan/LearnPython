n = int(input("Please enter the value for the last number : "))

sum = 0
for x in range(1, n+1, 1):
    sum = sum + x*x
print("The sum of the number is : ", sum)