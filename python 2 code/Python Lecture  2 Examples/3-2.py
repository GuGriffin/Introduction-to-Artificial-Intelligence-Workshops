import math  # Import the math module

# Input the first side of the triangle and convert it to an integer
a = int(input("Please enter the first side of the triangle: "))

# Input the second side of the triangle and convert it to an integer
b = int(input("Please enter the second side of the triangle: "))

# Input the third side of the triangle and convert it to an integer
c = int(input("Please enter the third side of the triangle: "))

# Check if the sides satisfy the conditions to form a triangle
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    s = 1/2 * (a + b + c)  # Calculate the semi-perimeter `s`
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Calculate the area using the `sqrt` function
    print("The area of the triangle is:", area)  # Output the area of the triangle
else:
    # If the conditions are not met, print an error message
    print("The entered sides cannot form a triangle.")
