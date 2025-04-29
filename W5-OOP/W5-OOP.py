##Activity 1
class Witch:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
    
    def description(self):
        print(f"{self.name} is a {self.age} year old witch🧙 from {self.location}.")

class Travel(Witch):
    def __init__(self, name, age, location, transport):
        super().__init__(name, age, location)
        self.transport = transport
    def travel(self):
        print(f"{self.name}  travels by {self.transport}.")  

class Type(Witch):
    def __init__(self, name, age, location, type_of_witch):
        super().__init__(name, age, location)
        self.type_of_witch = type_of_witch
    def type(self):
        print(f"{self.name} is a {self.type_of_witch} witch.")

class Magic(Witch):
    def __init__(self, name, age, location, magic_type):
        super().__init__(name, age, location)
        self.magic_type = magic_type
    def magic(self):
        print(f"{self.name} is a {self.magic_type} witch.") 



travel_witch = Travel("Morgana", 150, "Enchanted Forest", "broomstick")
type_of_witch = Type("Selene", 200, "Moonlight Valley", "Earth")
magic_type = Magic("Ravenna", 300, "Shadow Peaks", "dark magic")

# Calling methods to see the output
travel_witch.description()
travel_witch.travel()

type_of_witch.description()
type_of_witch.type()

magic_type.description()
magic_type.magic()



##Activity 2
# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass for Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Function to demonstrate polymorphism
def travel(vehicle):
    vehicle.move()

# Example usage
car = Car()
plane = Plane()
boat = Boat()

travel(car)    # Outputs: Driving 🚗
travel(plane)  # Outputs: Flying ✈️
travel(boat)   # Outputs: Sailing 🚢
