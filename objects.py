# object oriented programming

# imperative = statements, loops, functions as subroutines
# functional = pure functions, higher-order functions, recursion
# object = classes define a blueprint to create multiple objects

# create a class
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
        
    def bark(self):
        print("Woof woof!")
        
# create objects
felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# output
print(felix.color)
felix.bark()