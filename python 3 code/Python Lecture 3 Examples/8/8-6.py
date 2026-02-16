# Define the Student class
class Stu:
    def __init__(self, num, name, credit, course):  # Constructor to initialize student attributes
        self.num = num  # Student ID
        self.name = name  # Student name
        self.credit = credit  # Total credits
        self.course = course  # List of courses the student is enrolled in

    def choose(self, c):  # Method for student to choose a course
        self.credit += c.credit  # Add the course's credits to the student's total
        self.course.append(c.name)  # Add the course's name to the student's list of courses


# Define the Course class
class Cou:
    def __init__(self, num, name, credit):  # Constructor to initialize course attributes
        self.num = num  # Course ID
        self.name = name  # Course name
        self.credit = credit  # Course credit


# Create Student objects
stu_1 = Stu('201801', 'Jack', 0, [])  # Create student 1 with ID 201801, name 'Jack', 0 credits, and no courses
stu_2 = Stu('201802', 'Tom', 3, ['Math'])  # Create student 2 with ID 201802, name 'Tom', 3 credits, enrolled in 'Math'

# Create Course objects
cou_1 = Cou('01', 'Python', 3)  # Create course 1: 'Python' with 3 credits
cou_2 = Cou('02', 'C', 4)  # Create course 2: 'C' with 4 credits

# Students choose courses
stu_1.choose(cou_1)  # Student 1 chooses course 'Python'
stu_2.choose(cou_2)  # Student 2 chooses course 'C'

# Output student information
print('Student ID:', stu_1.num, 'Name:', stu_1.name, 'Total Credits:', stu_1.credit, 'Enrolled Courses:', stu_1.course)
print('Student ID:', stu_2.num, 'Name:', stu_2.name, 'Total Credits:', stu_2.credit, 'Enrolled Courses:', stu_2.course)
