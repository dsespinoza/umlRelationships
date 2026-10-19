class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP roaring to life!"

class Car:
    def __init__(self, make: str, model: str, horsepower: int):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower) 

    def start_car(self):
        engine_status = self.engine.start()
        print(f"The {self.make} {self.model} is ready to drive. {engine_status}")

my_car = Car("Tesla", "Model S", 1020)
my_car.start_car()