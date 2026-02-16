# Create a student dictionary
student_class_dict = {'jack': ['math', 'art'], 'lucy': ['biology', 'geography', 'music']}

# Print the dictionary
print(student_class_dict)

# Iterate through the dictionary and print student names and their selected courses
for key, value in student_class_dict.items():
    print("Student name: " + key + ", Selected courses: " + str(value))
