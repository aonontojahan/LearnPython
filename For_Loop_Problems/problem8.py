n = int(input("Please enter the last number: "))
sum = 0

for x in range(1, n + 1, 2): 
    sum = sum + x*x          

print("The sum of odd numbers is:", sum)

     