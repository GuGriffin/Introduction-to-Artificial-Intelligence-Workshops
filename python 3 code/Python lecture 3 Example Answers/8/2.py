class Circle:
    def __init__(self, radius, color):
        self.radius = radius  # Assign the radius of the circle
        self.color = color  # Assign the color of the circle

    def perimeter(self):
        # Formula for perimeter of a circle: 2 * π * radius
        return 3.14 * 2 * self.radius

    def area(self):
        # Formula for area of a circle: π * radius^2
        return 3.14 * self.radius * self.radius


# Create a Circle object with radius 5 and color "Blue"
circle = Circle(5, "Blue")

# Print the perimeter and area of the circle
print(circle.perimeter())  # Output the perimeter
print(circle.area())  # Output the area
