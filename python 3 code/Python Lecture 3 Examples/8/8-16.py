# Define Parent Class
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def who(self):  # Define who method
        print('I am a Person, my name is %s' % self.name)


# Define Student subclass
class Student(Person):
    def __init__(self, name, gender, score):
        super().__init__(name, gender)
        self.score = score

    def who(self):  # Override parent method
        print('I am a Student, my name is %s' % self.name)


# Define Teacher subclass
class Teacher(Person):
    def __init__(self, name, gender, course):
        super().__init__(name, gender)
        self.course = course

    def who(self):  # Override parent method
        print('I am a Teacher, my name is %s' % self.name)


# Define a function to receive an object and call its method
def fun(x):
    x.who()  # Call the who method


# Create objects
p = Person('Jack', 'Male')
s = Student('Tom', 'Male', 88)
t = Teacher('Lily', 'Female', 'English')

# Call function
fun(p)
fun(s)
fun(t)
