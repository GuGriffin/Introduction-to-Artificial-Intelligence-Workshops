stu = {'num': '202501', 'name': 'Jack', 'credit': 0, 'course': []}  # Define a student
course1 = {'num': '01', 'name': 'Python', 'credit': 3}  # Define course 1
course2 = {'num': '02', 'name': 'C', 'credit': 4}  # Define course 2

def choose(c):  # Define a function to choose a course
    stu['credit'] += c['credit']  # Add the course credit to the student's total credits
    stu['course'].append(c['name'])  # Add the course name to the student's selected courses list

choose(course1)  # Student chooses course 1
choose(course2)  # Student chooses course 2

print(stu)  # Print the student's information
