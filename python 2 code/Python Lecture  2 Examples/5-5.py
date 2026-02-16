animal = ['elephant', 'monkey', 'snake', 'tiger']  # Create a list of animals
x = input('Enter the animal name you want to search for: ')  # Prompt user to input an animal name
if x in animal:  # Check if the animal is in the list
    a = animal.index(x)  # Get the index of the animal in the list
    print(f'The animal "{x}" is found at index: {a}')  # Print the index of the animal
else:
    print('The animal is not in the list')  # Print a message if the animal is not found
