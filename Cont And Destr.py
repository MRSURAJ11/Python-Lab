class Student:

    def __init__(self):
        print("Constructor is called")
        print("Student object is created")

    def __del__(self):
        print("Destructor is called")
        print("Student object is destroyed")


s = Student()

print("Program is running")

del s 