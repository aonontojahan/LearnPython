
total_friends = int(input("Enter number of friends: "))
bill = int(input("Enter total bill amount: "))


tax_amount = (bill * 20) / 100


bill = bill + tax_amount


ppb = bill / total_friends


print(ppb)
