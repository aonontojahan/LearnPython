# If/Else statement checking
name = input("Please enter your name: ")
dept = input("Please enter your department name: ")

e_mark = float(input("Please enter your mark for english: "))
m_mark = float(input("Please enter your mark for math: "))

if e_mark >= 40:
    print("You passed in english")
else:
    print("You failed in english")

if m_mark >= 40:
    print("You passed in math")
else:
    print("You failed in math")

print("The highest mark you gate in: ", max(e_mark, m_mark))

if e_mark % 2 == 0:
    print("Your mark is even")
else:
    print("Your mark is odd")

