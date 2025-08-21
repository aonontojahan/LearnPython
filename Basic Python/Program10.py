# Program to collect names only for boys using elif in a loop

while True:
    gender = input("Enter the gender (boy/girl or 'exit' to stop): ").lower()

    if gender == "boy":
        name = input("Enter the boy's name: ")
        print("Boy's name recorded:", name)
    elif gender == "girl":
        print("Sorry, this program only collects names for boys.")
    elif gender == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter 'boy', 'girl', or 'exit'.")
