#Aggregation
class Student:

    def __init__(self, name: str):
        self.name = name


class Department:

    def __init__(self, student: Student):
        self.student = student

    def display_info(self):
        print(f"Department has student: {self.student.name}")


student = Student("Alice")  
dept = Department(student)
dept.display_info()