# Define a Parent Class
class Person:
    name = 'Human'
    age = 30
    def speak(self):  # Method to output a message
        print('%s says: I am %d years old.' % (self.name, self.age))

# Define a Subclass
class Student(Person):
    def setName(self, newName):  # Method to modify the name
        self.name = newName
    def speakAgain(self):  # Method to output the message again
        print('%s says: I am %d years old.' % (self.name, self.age))

# Create a Student Object
student = Student()
print('Student\'s name:', student.name)  # Output student's name
print('Student\'s age:', student.age)  # Output student's age

student.speakAgain()  # Call the subclass method to print the message
student.setName('Jack')  # Change the name using the subclass method
student.speak()  # Call the parent class method to print the message
