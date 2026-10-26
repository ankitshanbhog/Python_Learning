class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is Moving")

class Truck:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Truck is moving")

Car().drive()
Truck().drive()