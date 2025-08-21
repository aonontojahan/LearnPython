lower = int(input("Please enter the value for lower range : "))
upper = int(input("Please enter the value for lower range : "))
print("These are armstrong number between {0} and {1}".format(lower,upper))

for number in range(lower, upper+1):
    order = len(str(number))
    
    sum = 0
    temp = number
    while temp>0:
        digit = temp % 10
        sum += digit ** order
        temp//=10
    if number == sum:
        print(number)
        
