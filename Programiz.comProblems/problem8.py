#Conversion between kilometere to miles

kilometeres = float(input("Please enter value for kilometers : "))

conv = 0.621371

miles = kilometeres * conv

print("%0.2f kilometers is equal to %0.2f miles " %(kilometeres,miles))
print("The converted value is : ",miles)
print("/n")

v_miles = float(input("Please enter the value for miles: "))

c_kilometers = miles / conv
print("%0.2f miles is equal to %0.2f kilometers " %(v_miles,c_kilometers))