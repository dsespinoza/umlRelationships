class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"Teacher {self.name} is teaching {student.name}.")

class Student:
    def __init__(self, name):
        self.name = name

teacher_clara = Teacher("Clara")
student_alex = Student("Alex")

teacher_clara.teach(student_alex)

del teacher_clara
print(f"Student {student_alex.name} still exists.")