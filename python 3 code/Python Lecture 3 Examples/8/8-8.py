# Define a class
class Car:
    price = 150000                     # Class member variable

    def __init__(self, colour):
        self.colour = colour           # Instance member variable

# Create an object of the Car class
car_1 = Car('Red')

# Access class members and instance members, and print them
print(car_1.price, Car.price, car_1.colour)  # car_1.price accesses the instance variable, Car.price accesses the class variable

# Add a new class member
Car.name = 'Audi'

# Add a new instance member
car_1.wheelNum = 4

# Access class members and instance members again, and print them
print(car_1.wheelNum, car_1.name, Car.name)  # car_1.wheelNum accesses the instance variable, car_1.name accesses the instance variable, Car.name accesses the class variable

# Attempt to access class and instance variables directly
print(Car.colour, Car.wheelNum)  # This will raise an error because 'colour' and 'wheelNum' are instance variables, not class variables
