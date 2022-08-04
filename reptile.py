# create a reptile class which inherit everything from animal class into reptile
from animal import Animal

class Reptile(Animal): # Reptile is the child class, Animal is the parent/superclass/base class which is being inherited.

    def __init__(self):
        # need to let it know to inherit everything from the parent class
        super().__init__() # super is used to inherit everything from a base class
        self.species_name = "reptile" # reassigns name to reptile
        self.cold_blooded = True
        self.heart_chamber = [3,4]

    def seek_heat(self):  # returns concatenated string of the reptile seeking heat
        return "The", self.species_name, "is looking for sun shine"

    def hunt(self):  # returns concatenated string of the reptile hunting
        return "The", self.species_name, "is hunging"

    def use_venom(self):  # returns concatenated string of reptile using venom
        return "The", self.species_name, "uses its venom"


# # creates an instance of the reptile class which is an inherited class of animal
# a_reptile = Reptile()
# # prints the behaviour methods of the reptile & from the inherited animal through reptile
# print(a_reptile.seek_heat())
# print(a_reptile.move())
