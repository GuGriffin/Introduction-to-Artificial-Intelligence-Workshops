stu_class = {
    'Mary': 'C',
    'Jone': 'Java',
    'Lily': 'Python',
    'Tony': 'Python'
}  # Define the dictionary with student names as keys and courses as values

print('The following courses have been selected:')
for cla in set(stu_class.values()):  # Iterate through the unique values by converting them to a set
    print(cla)  # Output each unique course
