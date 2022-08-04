class animal:

    def __init__(self):
        species_name = "animal"
        movement_type = "moves"

    def sleep(self):
        print(self.species_name, "is sleeping....")

    def eat(self):
        print(self.species_name, "is eating")

    def move(self):
        print(self.species_name, self.movement_type)


this_animal = animal

this_animal.move()