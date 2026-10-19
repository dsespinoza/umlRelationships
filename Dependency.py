class Engine:
    def start(self):
        return "Vroom! Engine started."

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        print(self.engine.start())

my_car = Car()
my_car.drive()