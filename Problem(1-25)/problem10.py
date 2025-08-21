# Cheacking wheaher the number is possitive or negetive

number = float(input("Please enter a number : "))
print("Your input number is : ",number)
if number > 0:
    print("The number is possitive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")