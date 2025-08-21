marks = int(input("Please enter your mark :"))

if (marks >= 80) and (marks <= 100):
    print("Your marks is {0} and you got A+".format(marks))
elif (marks >= 70) and (marks <= 79):
    print("Your marks is {0} and you got A-".format(marks))
elif (marks >= 60) and (marks <= 69):
    print("Your marks is {0} and you got B+".format(marks))
elif (marks >= 50) and (marks <= 59):
    print("Your marks is {0} and you got B-".format(marks))
elif (marks >= 40) and (marks <= 49):
    print("Your marks is {0} and you got C".format(marks))
elif (marks >= 0) and (marks <= 39):
    print("Your marks is {0} and you fail in the exam".format(marks))
else:
    print("You entered a wrong number please try again")