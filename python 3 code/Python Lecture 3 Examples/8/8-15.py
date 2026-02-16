# Define Parent Class
class Person():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

# Define Child Class
class Stu(Person):
    def __init__(self, name, sex, score):
        super().__init__(name, sex)  # Call the __init__ method of the parent class
        self.score = score

# Create Object Instance
student = Stu('Jack', 'Male', 90)
print("Name: %s, Gender: %s, Score: %s" % (student.name, student.sex, student.score))
