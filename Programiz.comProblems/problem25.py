# Python program to find the ASCII value of a character

input_char = input("Please enter a character: ")
ascii_value = ord(input_char)
input_ascii = int(input("Please enter an ASCII value: "))
char_value = chr(input_ascii)

print("\n")
print("The ASCII value of '{0}' is {1}".format(input_char, ascii_value))
print("The character for ASCII value {0} is '{1}'".format(input_ascii, char_value))
print("End of program")  
