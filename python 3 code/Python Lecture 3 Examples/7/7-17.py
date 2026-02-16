stu = [
    {'num':'202501','name':'jack','score':89},
    {'num':'202502','name':'lucy','score':95},
    {'num':'202503','name':'bill','score':85}
]  # Define student information as a list of dictionaries

# Sort the list of students by their score in ascending order
stu.sort(key = lambda x: x['score'])

# Loop through each student in the sorted list and print their details
for s in stu:
    print('ID:', s['num'], 'name:', s['name'], 'score:', s['score'])
