punctuations = '''    !()-[]{};:'"\,<>./?@#$%^&*_~   '''

my_str = input("Please enter the string from where you want to remove the punctuation: ")

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)
