from random import sample, uniform, randint

Adjectives = ["Awesome", "Shiny", "Impressive", "Portable", "Improved"]
Nouns = ["Anvil", "Catapult", "Disguise", "Mousetrap", "???"]
names = [sample(Adjectives, 30) + ' ' + sample(Nouns, 30)]
price = [randint(5, 100)]
weight = [randint(5, 100)]
flammability = [uniform(0.0, 2.5)]


def generate_products(num_products=30):
    products = []
    return products

# Could not figure out how to create a list from 30 randomly concatenated words
# and unlabeled integers.


def inventory_reports(products):
    pass
# Could not figure out to how to pass a list into a function that would
# analyze it without creating a dataframe.


# if __name__=='__main__'
