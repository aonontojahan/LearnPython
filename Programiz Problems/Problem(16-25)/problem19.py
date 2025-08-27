# Python program to check if the number is an Armstrong number or not
num = int(input("Please enter the number : "))
sum = 0
temp = num
while temp> 0:
    digit = temp % 10
    
    
    sum += digit**3
    temp //= 10
if num == sum:
    print("{0} is an armstrong number".format(num))
else:
    print("{0} is not an armstrong number".format(num))