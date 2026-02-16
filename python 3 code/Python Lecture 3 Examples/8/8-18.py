# Define class
class Test:
    # Static method, decorated with @staticmethod
    @staticmethod
    def s_print():
        print('----Static Method----')

# Call the static method using the class name
Test.s_print()

# Create an instance of the class
t = Test()

# Call the static method using the instance
t.s_print()
