# Base Vehicle class
class Vehicle:
    def move(self):
        pass  # Base method to be overridden by subclasses

# Car subclass
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Bike subclass
class Bike(Vehicle):
    def move(self):
        print("Riding 🚴")

# Plane subclass
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Create instances of each vehicle
car = Car()
bike = Bike()
plane = Plane()

# Demonstrating polymorphism
def demonstrate_move(vehicle):
    vehicle.move()  # Calls the specific 'move' method based on the vehicle type

# Test the polymorphism
demonstrate_move(car)   # Output: Driving 🚗
demonstrate_move(bike)  # Output: Riding 🚴
demonstrate_move(plane) # Output: Flying ✈️