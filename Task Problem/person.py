class Person:
    def __init__(self, name, age, gender, address, phone_number, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}, Phone: {self.phone_number}, Email: {self.email}"
    
person1 = Person("Aononto Jahan", 23, "Male", "Sector 10, Road 7, House 2", "01723740704", "aonontojahan@gmail.com")
person2 = Person("Rakib Hasan", 24, "Male", "Sector 11, Road 8, House 3", "01723740705", "hanzabinrakib@gmail.com")
person3 =Person("Tonmoy Sarker", 26, "Male", "Sector 12, Road 9, House 4", "01723740706", "tonmoysarker@gmail.com")

print("Person 1 details:",person1)
print("Person 2 details:",person2)
print("Person 3 details:",person3)