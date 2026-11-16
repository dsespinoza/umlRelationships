class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()}")
        print(self.study())

    def get_age(self):
        return self.__age
    
        #Using a private value helps hide and protect the data.

    def study(self):
        return(f"{self.name} is studying")


person1 = Person("Dexie", 14)
person1.display_info()