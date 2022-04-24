# Day 21 - Practicing Class Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale...")

class Fish:

    def swim (self):
        print("moving in water.")
    

# Create instances
nemo = Fish()
nemo.swim()
    