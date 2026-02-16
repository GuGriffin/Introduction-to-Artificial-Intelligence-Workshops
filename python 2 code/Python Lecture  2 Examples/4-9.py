user_name = input("Please enter a username (starting with an underscore, 3-30 characters): ")
password = input("Please enter a password (contains underscores, digits, and letters, 8-16 characters): ")

# Check if the username starts with '_'
if user_name[0] != '_':
    print("Username must start with an underscore.")  # Output: "Username must start with an underscore."
# Check if the length of the username is between 3 and 30 characters
elif len(user_name) < 3 or len(user_name) > 30:
    print("Username length exceeds the limit.")  # Output: "Username length exceeds the limit."
# Check if the length of the password is between 8 and 16 characters
elif len(password) < 8 or len(password) > 16:
    print("Password length exceeds the limit.")  # Output: "Password length exceeds the limit."
# Check if the password contains at least one underscore
elif password.find('_') == -1:
    print("Password does not contain an underscore.")  # Output: "Password does not contain an underscore."
# Check if the password consists only of alphanumeric characters and underscores
else:
    if password.replace('_', '1').isalnum():  # Replace underscores with '1' and check if only alphanumeric characters remain
        print("Congratulations, registration successful! Username:", user_name, ", Password:", password)  # Output: "Congratulations, registration successful!"
    else:
        print("Password contains other symbols, registration failed!")  # Output: "Password contains other symbols, registration failed!"
