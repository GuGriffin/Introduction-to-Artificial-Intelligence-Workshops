# Define the class
class Car:
    # Constructor method
    def __init__(self, wheelNum, colour):
        self.wheelNum = wheelNum  # Number of wheels
        self.colour = colour  # Color of the car

    # Method to simulate the car running
    def run(self):
        print('{}-wheeled {} car is running...'.format(self.wheelNum, self.colour))


# Create objects with different attributes
BMW = Car(4, 'red')  # Create an object of Car with 4 wheels and red color
Audi = Car(4, 'white')  # Create an object of Car with 4 wheels and white color

# Call the run method for both cars
BMW.run()  # Output: 4-wheeled red car is running...
Audi.run()  # Output: 4-wheeled white car is running...
