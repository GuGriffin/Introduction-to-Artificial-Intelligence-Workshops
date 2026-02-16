class Person:
    def __init__(self, name, gender, age, fight_power):
        self.name = name  # Person's name
        self.gender = gender  # Person's gender
        self.age = age  # Person's age
        self.fight_power = fight_power  # Person's fight power

    def grassland(self):
        # Participating in a grassland battle reduces fight power by 200
        self.fight_power -= 200

    def practice(self):
        # Practicing increases fight power by 100
        self.fight_power += 100

    def incest(self):
        # Participating in an incest activity reduces fight power by 500
        self.fight_power -= 500

    def detail(self):
        # Prints the details of the person's attributes
        print(
            "Name: %s ; Gender: %s ; Age: %s ; Fight Power: %s" % (self.name, self.gender, self.age, self.fight_power))


# #####################  Start Game  #####################
a = Person('A', 'Female', 18, 1000)  # Create character A
b = Person('B', 'Male', 20, 1800)  # Create character B
c = Person('C', 'Female', 19, 2500)  # Create character C

a.incest()  # Character A participates in incest, reducing fight power by 500
b.practice()  # Character B practices, increasing fight power by 100
c.grassland()  # Character C participates in grassland battle, reducing fight power by 200

# Output the details of all characters
a.detail()
b.detail()
c.detail()
