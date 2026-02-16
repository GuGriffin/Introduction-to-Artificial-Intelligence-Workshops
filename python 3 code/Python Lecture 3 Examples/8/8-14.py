# Define a Parent Class
class Person:
    def speak(self):  # Define method to output a message
        print('I am a human')

# Define a Child Class
class Stu(Person):
    def speak(self):  # Override method to output a different message
        print('I am a student')

# Create a Student object
student = Stu()  # Create object of Stu class
student.speak()  # Call the overridden method
