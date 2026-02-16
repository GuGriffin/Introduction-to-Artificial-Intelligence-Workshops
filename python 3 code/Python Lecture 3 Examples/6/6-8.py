stu_info = {
    'jack': {'gender': 'M', 'age': '25'},
    'lucy': {'gender': 'F', 'age': '24'},
    'bill': {'gender': 'M', 'age': '24'}
}  # Define the dictionary with student names as keys and nested dictionaries as values

for name, stu in stu_info.items():  # Iterate over the dictionary's items (key-value pairs)
    print(name, 'gender:', stu['gender'], 'age:', stu['age'])  # Output the name, gender, and age
