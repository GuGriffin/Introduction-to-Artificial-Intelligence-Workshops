class A:  # Define class
    def __init__(self):
        self.__X = 10  # Define a private variable with value 10
    def __foo(self):  # Define a private method
        print('from A')

a = A()  # Create an object of class A
print(a.__X)  # Attempt to access private variable
a.__foo()  # Attempt to call private method
