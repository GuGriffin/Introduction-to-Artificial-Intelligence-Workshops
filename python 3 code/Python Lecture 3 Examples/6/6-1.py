# Creating a dictionary directly
stu_info1 = {'num': '20250101', 'name': 'Jack', 'gender': 'male'}

# Creating a dictionary by copying another dictionary
stu_info2 = dict(stu_info1)

# Creating a dictionary using a sequence of (key, value) pairs
stu_info3 = dict([('num', '20250101'), ('name', 'Jack'), ('gender', 'male')])

# Creating a dictionary using keyword arguments
stu_info4 = dict(num='20250101', name='Jack', gender='male')

# Creating a dictionary using dict() and zip()
stu_info5 = dict(zip(['num', 'name', 'gender'], ['20250101', 'Jack', 'male']))

# Check if all five dictionaries are equal
if stu_info1 == stu_info2 == stu_info3 == stu_info4 == stu_info5:
    print("The five methods of creating dictionaries are identical.")
else:
    print("The five methods of creating dictionaries are not identical.")
