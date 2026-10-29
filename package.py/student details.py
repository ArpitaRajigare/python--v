class Student:
    def __init__(self, name, roll_no, age, course, marks, city, country):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course
        self.marks = marks
        self.city = city
        self.country = country

    def display_details(self):
        print("\n======================================")
        print("          STUDENT DETAILS")
        print("======================================")
        print("Name       :", self.name)
        print("Roll No    :", self.roll_no)
        print("Age        :", self.age)
        print("Course     :", self.course)
        print("Marks      :", self.marks)
        print("City       :", self.city)
        print("======================================")


print("======================================")
print("       ENTER STUDENT DETAILS")
print("======================================")

name = input("Enter Name: ")
roll_no = input("Enter Roll No: ")
age = input("Enter Age: ")
course = input("Enter Course: ")
marks = input("Enter Marks: ")
city = input("Enter City: ")
country = input("enter country:")
student = Student(name, roll_no, age, course, marks, city, country)

student.display_details()
