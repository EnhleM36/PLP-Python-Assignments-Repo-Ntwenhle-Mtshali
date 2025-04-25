class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        print("You will be Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("You will be Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("You will be Sailing 🚢")

def travel(vehicle):
    vehicle.move()

car = Car()
plane = Plane()
boat = Boat()

travel(car)    
travel(plane)  
travel(boat)   
