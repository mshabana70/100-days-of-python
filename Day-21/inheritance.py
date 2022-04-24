# Day 21 - Practicing Class Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale...")

# Fish class inherits from the super class Animal
class Fish(Animal):

    def swim (self):
        print("moving in water.")
    

# Create instances
nemo = Fish()
nemo.swim()
    