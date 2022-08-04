# Python OOP

![OOP diagram](https://user-images.githubusercontent.com/47668244/182827918-e4e87130-63ea-4814-899a-ff8eb70053a5.png)

## Animal

```commandline
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

```
## Animal\Reptile

```commandline
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


# creates an instance of the reptile class which is an inherited class of animal
a_reptile = Reptile()
# prints the behaviour methods of the reptile & from the inherited animal through reptile
print(a_reptile.seek_heat())
print(a_reptile.move())

```

## Animal\Reptile\Snake

```commandline
# create inherited class from Reptile named Snake to present encapsulation

from reptile import Reptile

class Snake(Reptile): # inherited class of Reptile named Snake

    def __init__(self): # constructor which initializes the class
        super().__init__() # inherits all of the attributes from parent class
        self.species_name = "snake"
        self.movement_type = "slithers"
        self.forked_tongue = True

    def smell(self): # in encapsulation, this is a public method
        # pass  use to implement many behaviours of inherited class in shorter length of code without errors
        return "It is", self.forked_tongue, "that the", self.species_name, "has a forked tongue. It will smell with it"

    def _slither(self): # in encapsulation, this is a protected method
        return "The", self.species_name, self.movement_type


    def __expand_jaw(self): # in encapsulation, this is a private method
        return "The", self.species_name, "opens its jaw"

    def call_expand_jaw(self):
        return self.__expand_jaw()

# object, which is an instance of the Snake class
snake_object = Snake()
print(snake_object.move())
print(snake_object.smell())
# create 2 more functions with _ the other with __, exectue them both - return message should explain Encapsulation break down - public - protected - private
print(snake_object._slither())
#print(snake_object.__expand_jaw()) this method cannot be called outside of the clss because it is private, so running this line will result in an error
print(snake_object.call_expand_jaw()) # however this will work, because it is calling a public method, which calls the expand_jaw method. because they are both within the same class the expand_jaw method is not encapsulated against it.
```
