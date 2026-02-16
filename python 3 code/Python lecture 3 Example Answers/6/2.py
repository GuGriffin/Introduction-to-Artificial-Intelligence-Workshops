arr = []
length = int(input("Enter the total number of elements in the list:"))
i = 0
while i < length:
    element = input("Enter the %d-th element:" % (i + 1))
    arr.append(element)
    i += 1

# Convert list to set
newSet = set(arr)
print(newSet)
