# Function to print binary number using recursion

def convert_to_binary(n):
    if n > 1:
        convert_to_binary(n // 2)
    print(n % 2, end='')
    
number = int(input("Enter a positive integer: "))
if number < 0:
    print("Please enter a positive integer")
else:
    print("The binary representation of", number, "is: ", end='')
    convert_to_binary(number)
    print()