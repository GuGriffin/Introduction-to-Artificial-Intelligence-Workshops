class Person:
    def __init__(self, name, age, gender):
        self.name = name   # Name of the person
        self.age = age     # Age of the person
        self.gender = gender  # Gender of the person

    def like_chinese(self):
        # Print the person's details and that they like Chinese class
        print("%s, %s years old, %s, likes Chinese class" % (self.name, self.age, self.gender))

    def like_movie(self):
        # Print the person's details and that they like watching movies
        print("%s, %s years old, %s, likes watching movies" % (self.name, self.age, self.gender))

    def like_basketball(self):
        # Print the person's details and that they like playing basketball
        print("%s, %s years old, %s, likes playing basketball" % (self.name, self.age, self.gender))


# Create objects for two people
Lucy = Person('Lucy', 10, 'Female')  # Create a person named Lucy, age 10, female
Lucy.like_chinese()                  # Lucy likes Chinese class
Lucy.like_movie()                    # Lucy likes watching movies
Lucy.like_basketball()               # Lucy likes playing basketball

Bill = Person('Bill', 12, 'Male')      # Create a person named Bill, age 12, male
Bill.like_chinese()                     # Bill likes Chinese class
Bill.like_movie()                       # Bill likes watching movies
Bill.like_basketball()                  # Bill likes playing basketball
