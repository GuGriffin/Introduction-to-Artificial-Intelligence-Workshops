operator_list = ['+', '-', '*', '/']  # List of supported operators
number_1 = float(input("Please enter the first operand: "))  # Get the first operand from user input
operator = input("Please enter the operator: ")  # Get the operator (+, -, *, /)
number_2 = float(input("Please enter the second operand: "))  # Get the second operand from user input

# Check if the entered operator is valid
if operator not in operator_list:
    print("Invalid operator, please enter a valid operator (+, -, *, /)!")  # Print error message for invalid operator
else:
    # Perform the corresponding operation
    if operator == '+':  # If operator is addition
        result = number_1 + number_2
    elif operator == '-':  # If operator is subtraction
        result = number_1 - number_2
    elif operator == '*':  # If operator is multiplication
        result = number_1 * number_2
    elif operator == '/':  # If operator is division
        if number_2 == 0:
            print("Cannot divide by zero!")  # Error message for division by zero
        else:
            result = number_1 / number_2

    print(f"{number_1} {operator} {number_2} = {result}")  # Output the result
