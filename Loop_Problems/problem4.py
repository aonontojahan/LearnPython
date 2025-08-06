
inputnumber = int(input("Please enter the last number : "))
sum = 0
i = 1
while i <= inputnumber:
    sum = sum + i
    i = i + 1
print("Your input number is {0} and the sum between 1 to {1} is : ".format(inputnumber,inputnumber),sum)
    