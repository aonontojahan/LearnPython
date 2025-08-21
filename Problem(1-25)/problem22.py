#Displaying the power of 2 using anonymous function

terms = int(input("Enter the number of terms: "))
power_of_two = lambda x: 2 ** x
for i in range(terms):
    print("2 raised to the power of {0} is {1}".format(i, power_of_two(i)))
    
print("End of program")  # Indicating the end of the program