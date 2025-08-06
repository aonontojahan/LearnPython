lastnumber = int(input("Please enter the lastnumber even number : "))
sum = 0

if (lastnumber % 2) == 0:
    i = 0
    while i<= lastnumber:
        sum = sum + i
        i = i + 1
    print("The sum of 0 to {0} is {1}".format(lastnumber, sum))
else:
    print("No even number")

        

    



