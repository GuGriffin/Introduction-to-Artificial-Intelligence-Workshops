count = 0  # Define count variable and set its initial value to 0
passwd = 123  # Define passwd variable and set its initial value to 123

# Define a dictionary to store user information: passwords and login attempts
dict1 = {'alex': [passwd, count], 'Tom': [passwd, count]}

while True:  # Start the loop
    name = input("Please input your name: ")  # Input username
    password = int(input("Please input your password: "))  # Input password

    if name not in dict1.keys():  # If the username is not in the dictionary
        print("Name %s is not in the system." % name)  # Output message
        break  # Break out of the loop

    if dict1[name][1] >= 3:  # If the user has attempted to log in more than 2 times (3 or more)
        print("The account %s is locked." % name)  # Output account locked message
        break  # Break out of the loop

    if password == dict1[name][0]:  # If the password is correct
        print("Login successful!")  # Output success message
        break  # Break out of the loop
    else:  # If the password is incorrect
        print("Incorrect username or password.")  # Output error message
        dict1[name][1] += 1  # Increment the login attempt count
