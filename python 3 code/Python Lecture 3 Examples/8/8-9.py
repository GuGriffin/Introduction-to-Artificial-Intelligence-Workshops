# Define a class
class Car:
    price = 150000                       # Class member variable

    def __init__(self):
        self.price = 100000               # Instance member variable

# Create an object of the Car class
car_1 = Car()

# Access and print the class member and the instance member
print(car_1.price, Car.price)            # Access instance member through car_1, class member through Car
