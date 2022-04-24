# Day 21 - Practicing Class Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale...")

# Fish class inherits from the super class Animal
class Fish(Animal):

    # You must include a reference to the super class in your
    # inherited class' constructor like so
    def __init__(self):
        super().__init__()

    def swim (self):
        print("moving in water.")
    

# Create instances
nemo = Fish()
nemo.swim()
nemo.breathe() # Now our fish object has method "breathe"
print(nemo.num_eyes) # It also has attribute "num_eyes"
    