# Python program to display all the prime numbers within an interval

lower = int(input("Please enter the number for lower position : "))
upper = int(input("Please enter the value for upper position : "))

print("Prime numbers between", lower, "and", upper, "are:")
print("Prime number between {0} and {1} are : ".format(lower,upper))

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           