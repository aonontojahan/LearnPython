import random
import secrets

my_list = [1, 'a', 32, 'c', 'd', 31]
print("Now the system is going to print a random thing for my-list")
print(random.choice(my_list))

print("")
names = ['Aononto','Jahan', 'Junnurain']
print("Now the system is going to print the last number from names")
print((names [-1]))

print("")
print("Now the system is going to print a random thing for my-list")
print(secrets.choice(my_list))