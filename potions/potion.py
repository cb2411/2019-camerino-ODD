"""This module contains the class Potion."""
import numpy as np
import matplotlib.pyplot as plt

class Potion:

    def __init__(self, name):
        """This is a class for brewing potions."""
        self.colour = 'there-is-no-potion-so-the-potion-has-no-color'
        self.cooked = False
        self.container = None
        self.heat_source = None
        self.ingredients = []
        self.simmer_duration = -1
        self.name = name

    def setup(self, container=None, heat_source=None):
        """Add a container and/or heat_source to the potion.

        Updates container and heat_source attributes in the class instance.

        Parameters
        ----------
        container : str, optional
            The name of the container to brew the potion in.
        heat_source : str, optional
            The name of the heat source used to cook the potions
        """
        if container == None:
            print(f'You have not specified a container - where do you think you will brew your potion?')
        if heat_source == None:
            print(f'You have not specified a heat source - how will you cook the potion?')
        self.container = container
        self.heat_source = heat_source

    def add_ingredients(self, ingredients=None):
        """Add ingredients to the potion.

        Updates ingredients and colour attributes in the class instance.

        Parameters
        ----------
        ingredients : array_like, optional
            A list of ingredients (str) to add to the potion.
        """
        if ingredients is None:
            print(f'You have added no ingredients - have you spilt them on the floor again?')
        else:
            self.ingredients = ingredients
            self.colour = "transparent"

    def check_colour(self):
        """Prints current colour of potion."""
        print(f'The potion currently looks {self.colour}.')

    def check_if_cooked(self):
        """Print whether the potion is cooked."""
        if self.cooked:
            print("Smells like feet, but that's a good thing. Potion looks cooked.")
        else:
            print("Doesn't seem quite right yet... Potion does not look cooked.")

def func():
    print('you could access this function, well done!')


# ignore this part, this is just so that I have to list numpy and matplotlib in dependencies
foo = np.array([0, 1, 2, 3])
bar = plt.hist(foo, bins=2)

