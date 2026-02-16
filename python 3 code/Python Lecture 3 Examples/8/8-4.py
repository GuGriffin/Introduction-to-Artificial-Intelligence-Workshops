# Define the class
class Car:
    # Constructor method
    def __init__(self):
        self.wheelNum = 4  # Default number of wheels
        self.colour = 'blue'  # Default color of the car

    # Method to simulate the car running
    def run(self):
        print('{}-wheeled {} car is running...'.format(self.wheelNum, self.colour))


# Create an object of the Car class
BMW = Car()
BMW.run()  # Call the run method
