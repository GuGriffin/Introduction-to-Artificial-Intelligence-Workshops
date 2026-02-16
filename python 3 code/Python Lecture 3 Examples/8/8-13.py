# Define a Parent Class for Sofa
class Sofa:
    def printA(self):
        print('----This is a sofa----')

# Define a Parent Class for Bed
class Bed:
    def printB(self):
        print('----This is a bed----')

# Define a Child Class that inherits from both Sofa and Bed
class Sofabed(Sofa, Bed):
    def printC(self):
        print('----This is a sofa bed----')

# Create an Object of the Child Class
obj_C = Sofabed()  # Create object
obj_C.printA()     # Call method from the Sofa class
obj_C.printB()     # Call method from the Bed class
obj_C.printC()     # Call method from the Sofabed class
