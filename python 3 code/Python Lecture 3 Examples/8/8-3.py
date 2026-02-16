# Define the class
class Car:
    def colour(self, col):  # Define method to set car color
        self.col = col

    def show(self):  # Define method to display car color
        print('The color of the car is %s.' % self.col)


# Create car objects and assign colors
car_1 = Car()
car_1.colour('red')

car_2 = Car()
car_2.colour('white')

# Display the color of both cars
car_1.show()
car_2.show()
