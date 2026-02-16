name = input("Please enter your username: ")  # Prompt user to enter the username
password = input("Please enter your password: ")  # Prompt user to enter the password

# Predefined username and password
name_1 = '12345'
password_1 = '1234567'

# Validate the input
if name != name_1:
    print("The username you entered is incorrect.")  # Username error message
elif password != password_1:
    print("The password you entered is incorrect.")  # Password error message
else:
    print("Hello Python!")  # Successful login message
