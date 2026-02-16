arr = []
myStr = input("Enter a string containing only letters:")  # Prompt the user for input
newStr = myStr.lower()  # Convert the input string to lowercase

# Iterate through the string and append each character to the list
for string in newStr:
    arr.append(string)

a = {}

# Count the occurrences of each character in the list and store them in the dictionary
for i in arr:
    if arr.count(i) >= 1:
         a[i] = arr.count(i)

print(a)
