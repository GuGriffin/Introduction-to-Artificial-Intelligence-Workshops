stu_1 = ['001', 'Wong', 98]  # Create a list stu_1
stu_2 = stu_1.copy()         # Create a copy of stu_1 using the copy() method
# Alternatively, you can use: stu_2 = stu_1[:]
print(stu_1, stu_2)           # Output stu_1 and stu_2
stu_1[0] = '002'              # Modify the first element of stu_1
print(stu_1, stu_2)           # Output stu_1 and stu_2 again
