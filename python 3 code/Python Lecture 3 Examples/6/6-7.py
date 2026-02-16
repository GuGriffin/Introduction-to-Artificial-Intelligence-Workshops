stu_class = {
    'Mary': ['C', 'Math'],
    'Jone': ['Java', 'Art'],
    'Lily': ['Python'],
    'Tony': ['Python', 'Mysql', 'Math']
}  # Define the dictionary with student names as keys and courses as values

for name, cla in stu_class.items():  # Iterate over all the key-value pairs in the dictionary
    print(name, 'is enrolled in the following courses:')  # Output the student's name
    for c in cla:  # Iterate over the list of courses
        print(c)  # Output each course
