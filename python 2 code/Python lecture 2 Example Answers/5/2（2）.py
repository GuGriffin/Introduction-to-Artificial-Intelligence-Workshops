arr = input("Please enter an odd number of integers, separated by spaces: ")  # Prompt user input
arr = list(map(int, arr.split()))  # Split the input into a list of strings and convert to integers
arr.sort()  # Sort the list in ascending order
index = len(arr)  # Get the length of the list

if index % 2 == 1:  # Check if the number of elements is odd
    print("The median value is:", arr[index // 2])  # Find and print the middle element
else:
    print("Error: The number of integers entered is not odd.")  # Error message for even-length input
