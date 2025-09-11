class Student:
    def __init__(self, name, student_id, department, cgpa):
       
        self.name = name
        self.student_id = student_id
        self.department = department
        self.cgpa = cgpa

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Department:", self.department)
        print("CGPA:", self.cgpa)
        print()

s1 = Student("Aononto Jahan", "CSE2025001", "CSE", 3.4)
s2 = Student("Rakib Hasan", "CSE2025002", "CSE", 3.2)
s3 = Student("Tonmoy Sarker", "CSE2025003", "CSE", 3.5)

s1.display_info()
s2.display_info()
s3.display_info()
