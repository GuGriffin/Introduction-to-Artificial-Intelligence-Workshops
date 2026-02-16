# Define class
class People:
    country = 'UK'  # Define a class member and assign a value

    # Class method, decorated with @classmethod
    @classmethod
    def getCountry(cls):
        return cls.country  # Return the value of the class member

# Create an object
p = People()

# Access the class method through the object
print(p.getCountry())  # Access using an instance object

# Access the class method directly through the class
print(People.getCountry())  # Access using the class object
