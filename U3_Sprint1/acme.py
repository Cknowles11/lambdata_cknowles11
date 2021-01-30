# Part 1
import random


class Product():

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super(Product, self).__init__()
        self.name = name
        self.weight = weight
        self.price = price
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if self.price/self.weight < 0.5:
            return print("Not so stealable")

        elif self.price/self.weight >= 0.5:
            return print("Kinda stealable")

        else:
            return print("Very stealable!")

    def explode(self):
        if self.flammability * self.weight < 10:
            return print("...fizzle")
        elif 10 <= self.flammability * self.weight < 50:
            return print("...boom!")
        else:
            return print("...BABOOM!!")


class BoxingGlove(Product):
    def __init__(self, name):
        Product.__init__(self, name)
        self.weight = 10

    def explode(self):
        if self.flammability * self.weight >= 0:
            return print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            return print("That tickles")
        elif 5 <= self.weight < 15:
            return print("Hey that hurt!")
        else:
            return print("OUCH!")
