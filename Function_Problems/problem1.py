subjects = ["Fundemantals", "C", "C++", "Java", "Python", "ANdroid", "OS", "C++", "TOC"]


subjects2 = subjects.copy()
print("The subjects are : ",subjects2)
print("\n")

pos = subjects.index("Python")
print("The position of the Python index is ",pos)
print("\n")

number = subjects.count("C++")
print("C++ is available in the list :",number)
print("\n")

subjects.pop()
print("The last input is vanished : ",subjects )
print("\n")

subjects.clear()
print("No value",subjects)
print("\n")