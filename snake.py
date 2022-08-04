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
        try: # this is a try except function, which is like a if statement, but returns errors & exceptions instead (think try catch statment in C#
            return self.__expand_jaw()
        except:# this  is the exception that the try throws
            print("no no snake for you")


# object, which is an instance of the Snake class
snake_object = Snake()
print(snake_object.move())
print(snake_object.smell())
# create 2 more functions with _ the other with __, exectue them both - return message should explain Encapsulation break down - public - protected - private
print(snake_object._slither())
#print(snake_object.__expand_jaw()) this method cannot be called outside of the clss because it is private, so running this line will result in an error
print(snake_object.call_expand_jaw()) # however this will work, because it is calling a public method, which calls the expand_jaw method. because they are both within the same class the expand_jaw method is not encapsulated against it.
print(snake_object.call_expand_jaw())