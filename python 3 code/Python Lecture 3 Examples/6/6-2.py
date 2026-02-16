dict1 = {'user': 'runoob', 'num': [1, 2, 3]}  # Original dictionary with a list as a value
dict2 = dict1  # dict2 is a reference to dict1, meaning both point to the same object
dict3 = dict1.copy()  # Shallow copy: a new dictionary is created, but the list inside is still shared (referenced)
import copy
dict4 = copy.deepcopy(dict1)  # Deep copy: a completely new dictionary and new list are created

dict1['user'] = 'root'  # Modify the value for the key 'user' in dict1
dict1['num'].remove(1)  # Modify the list under the 'num' key in dict1, remove the number 1

# Output the dictionaries
print('dict1=', dict1)
print('dict2=', dict2)
print('dict3=', dict3)
print('dict4=', dict4)
