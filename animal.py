class Animal:

    # __init__ is a constructor which declares class attributes
    def __init__(self): # self refers to current class
        self.species_name = "animal"
        self.movement_type = "moves"
        self.alive = True
        self.spine = True

    def sleep(self): # returns concatenated string of animal sleeping
        return "The", self.species_name, "is sleeping...."

    def eat(self): # returns concatenated string of animal eating
        return "The", self.species_name, "is eating"

    def move(self): # returns concatenated string of animal moving
        return "The", self.species_name, self.movement_type

# create an object of the class
cat = Animal()

#print(cat.move())
