# Define a Cat class
class Cat:
    role = 'cat'  # All cats have the role "cat"

    # Constructor to initialize a cat's attributes
    def __init__(self, name, breed, aggressiveness, life_value):
        self.name = name               # Each cat has a name
        self.breed = breed             # Each cat has a breed
        self.aggressiveness = aggressiveness  # Each cat has its own aggressiveness
        self.life_value = life_value       # Each cat has its own life value

    # Define the method for the cat to attack a dog
    def attack(self, dog):
        dog.life_value -= self.aggressiveness  # Decrease the dog's life value based on the cat's aggressiveness

    # Method to increase the cat's life value
    def eat(self):
        self.life_value += 50

    # Method to check if the cat is dead
    def die(self):
        if self.life_value <= 0:  # If life value is less than or equal to 0, the cat is dead
            print(self.name, 'has been killed!')
        else:
            print(self.name, 'has', self.life_value, 'life left.')

# Define a Dog class
class Dog:
    role = 'dog'  # All dogs have the role "dog"

    # Constructor to initialize a dog's attributes
    def __init__(self, name, breed, aggressiveness, life_value):
        self.name = name               # Each dog has a name
        self.breed = breed             # Each dog has a breed
        self.aggressiveness = aggressiveness  # Each dog has its own aggressiveness
        self.life_value = life_value       # Each dog has its own life value

    # Define the method for the dog to bite a cat
    def bite(self, cat):
        cat.life_value -= self.aggressiveness  # Decrease the cat's life value based on the dog's aggressiveness

    # Method to increase the dog's life value
    def eat(self):
        self.life_value += 30

    # Method to check if the dog is dead
    def die(self):
        if self.life_value <= 0:  # If life value is less than or equal to 0, the dog is dead
            print(self.name, 'has been killed!')
        else:
            print(self.name, 'has', self.life_value, 'life left.')

# Create instances of a cat and a dog
cat_1 = Cat('Mily', 'Persian', 30, 1500)  # Creating a cat
dog_1 = Dog('Lucky', 'Husky', 50, 900)    # Creating a dog

cat_1.die()  # Output the cat's current status
dog_1.die()  # Output the dog's current status
print('------Battle begins-----')

cat_1.attack(dog_1)  # The cat attacks the dog once
dog_1.bite(cat_1)    # The dog bites the cat once
cat_1.die()  # Output the cat's current status
dog_1.die()  # Output the dog's current status

for i in range(29):  # Loop to make the cat attack the dog 29 more times
    cat_1.attack(dog_1)

dog_1.die()  # Output the dog's current status
cat_1.eat()  # The cat eats food once
cat_1.die()  # Output the cat's current status
