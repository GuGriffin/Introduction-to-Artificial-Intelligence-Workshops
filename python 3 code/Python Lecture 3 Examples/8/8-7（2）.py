class Animal():
    # Constructor method
    def __init__(self):
        print('---Constructor method called---')

    # Destructor method
    def __del__(self):
        print('---Destructor method called---')


# Create an object of the Animal class
dog = Animal()

# Delete the object explicitly
del dog

print('---Program ends---')
