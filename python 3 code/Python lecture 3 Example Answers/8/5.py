class Animal(object):
    def __init__(self, color):
        self.color = color  # Animal color

    def call(self):
        print("The animal makes a sound")  # General animal sound


class Fish(Animal):
    def __init__(self, color):
        super().__init__(color)  # Call the parent constructor to set color
        self.tail = True  # Fish has a tail

    def call(self):
        print("The %s fish is blowing bubbles" % self.color)  # Fish blowing bubbles with its color


# Create an instance of Fish with color "Blue"
fish = Fish("Blue")
fish.call()  # Call the fish's call method
