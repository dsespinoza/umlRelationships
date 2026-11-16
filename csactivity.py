class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()}")

    def get_age(self):
        return self.__age
    
        #Using a private value helps hide and protect the data.


class Student(Person):    
    def study(self):
        print(f"{self.name} is studying")

class Teacher(Person):  
    def teach(self):
        print(f"{self.name} is teaching")
 


person1 = Person("Dexie", 14)
person1.display_info()

student1 = Student("Dexie", 14)
student1.study()

teacher1 = Teacher("Dexie", 14)
teacher1.teach()
