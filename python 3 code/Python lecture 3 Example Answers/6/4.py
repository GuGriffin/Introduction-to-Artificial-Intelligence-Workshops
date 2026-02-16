dic = {}
i = 0
# Collect student information 3 times
while i < 3:
    number = input("Enter student ID: ")  # Ask for student ID
    name = input("Enter student name: ")  # Ask for student name
    dic.__setitem__(number, name)  # Store student ID as key and name as value
    i += 1

print("Before sorting: %s" % dic)

# Function to convert dictionary to a list of tuples
def dict2list(dic: dict):
    ''' Converts dictionary to a list '''
    keys = dic.keys()  # Get dictionary keys (student IDs)
    vals = dic.values()  # Get dictionary values (student names)
    lst = [(key, val) for key, val in zip(keys, vals)]  # Create a list of tuples (ID, name)
    return lst

# Sort the list of tuples by student ID in ascending order
new = sorted(dict2list(dic), key=lambda x: x[0], reverse=False)

print("After sorting: %s" % new)
