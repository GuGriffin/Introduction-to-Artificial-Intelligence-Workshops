def printinfo(name, age = 35):  # Define the function, which prints any passed string
    print("Name: ", name)
    print("Age: ", age)
    return

# Call the printinfo function
print(printinfo.__defaults__)  # Print the default values of the function
printinfo("root", 50)  # Explicitly pass a value
print("------------------------")
printinfo("root")  # Use the default value for age
