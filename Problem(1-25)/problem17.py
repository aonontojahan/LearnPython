# Creating multiplication table
num = int(input("Please enter a number: "))
print("The system is going to represent the multiplication table of", num)

for x in range(1, num + 1):
    print(num, 'x', x, '=', num * x)
