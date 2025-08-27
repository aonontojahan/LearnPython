#Python program to find a numbers  which is divisible by another number

my_list = [12, 65, 54,39,40,339,221, 230, 120, 150, 180]

result1 = list(filter(lambda x: (x % 13 == 0), my_list))
result2 = list(filter(lambda x: (x % 2 == 0),my_list))

#Here list is a function 
#Under the list function use filter function to filter the elements of the list
#Lambda is a anonymous function which is used to filter the elements of the list
#Lambda (parameter: expression) is the syntax of lambda function

print("Numbers divisible by 2 are", result2)
print("Numbers divisible by 13 are", result1)
print("Numbers divisible by 2 and 13 are", result2,result1)