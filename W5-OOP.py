##Activity 1
class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Pages: {self.pages}"
    
    def read(self):
        return f"You are reading '{self.title}', it is a {self.genre} bookcler."

class PaperBack(Book):
    def __init__(self, title, author, genre, pages, cover_type):
        super().__init__(title, author, genre, pages)
        self.cover_type = cover_type

    def read(self):
        return f"You are flipping through the {self.cover_type} cover pages of '{self._title}'."

class Ebook(Book):
    def __init__(self, title, author, genre, pages, file_size):
        super().__init__(title, author, genre, pages)
        self.file_size = file_size

    def read(self):
        return f"You are reading the eBook '{self.title}' on your device. File size: {self.file_size} MB."

BookA = Book("Twilight", "Stepahnie Meyer", "Fantasy", 180)
BookB = PaperBack("Harry Potter", "J.K. Rowling", "Fantasy", 300, "soft")
BookC = Ebook("The Alchemist", "Paulo Coelho", "Adventure", 200, 1.5)

print(BookA.description())
print(BookA.read())


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
