# Define the class
class Car:
    price = 150000  # Define the price variable

    def run(self):  # Define the method for running
        print('The car is running...')


# Create an object and save its reference in the variable car_1
car_1 = Car()

# Call the run() method
car_1.run()

# Access the price variable in the class
print('The car price is:', car_1.price)
