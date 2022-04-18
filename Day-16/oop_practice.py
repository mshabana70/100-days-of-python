# Day 16 - Using turtle module to Practice OOP principles

from turtle import Turtle, Screen

timmy = Turtle() # Turtle object construction 
# print(timmy)

timmy.shape("turtle") # Turtle object method to define shape
timmy.color("DeepSkyBlue") # Turtle object method to define color
timmy.fd(100) # Move our turtle forward by 100 paces
timmy.lt(90) # Move our turtle to the left by 90 degrees
timmy.fd(100) # Move our turtle forward by 100 paces

# To access an object's attribute, you can use dot notation 
# on the variable that holds our object
my_screen = Screen()
print(my_screen.canvheight) # hieght attribute of screen object

# Accessing methods of an object, also using dot notation
my_screen.exitonclick() # Continue running until we click on screen

