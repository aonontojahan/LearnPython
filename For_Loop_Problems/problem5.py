n = int(input("Please enter the last number : "))

sum = 0
for x in range(2, n+1, 2):
    sum = sum + x
print("The sum of the number is : ",sum)