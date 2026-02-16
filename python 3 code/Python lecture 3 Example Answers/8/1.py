class Person:
    def __init__(self, name, age, blood_type):
        self.name = name  # Assign the name attribute
        self.age = age  # Assign the age attribute
        self.blood_type = blood_type  # Assign the blood type attribute

    def detail(self):
        # Format the details into a string and print them
        temp = "I am %s, age %s, blood type %s" % (self.name, self.age, self.blood_type)
        print(temp)


# Create instances of the Person class
jack = Person('jack', 18, 'A')
lucy = Person('lucy', 73, 'AB')
bill = Person('bill', 84, 'A')

# Call the 'detail' method to print the details for each person
jack.detail()
lucy.detail()
bill.detail()
