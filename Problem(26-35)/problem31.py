
# Program to display calendar of the given month and year

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print("\n")
print(calendar.month(year, month))