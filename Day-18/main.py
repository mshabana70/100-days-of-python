from turtle import Turtle, Screen

leo_the_turtle = Turtle()
leo_the_turtle.shape("turtle") # shape of turtle object
leo_the_turtle.color("blue") # TK color specification string

# Challenge # 1: Draw a Square
def draw_a_square():
    leo_the_turtle.forward(100)
    leo_the_turtle.right(90)
    leo_the_turtle.forward(100)
    leo_the_turtle.right(90)
    leo_the_turtle.forward(100)
    leo_the_turtle.right(90)
    leo_the_turtle.forward(100)

# Call function
draw_a_square()









screen = Screen() # Create the window object so we can access properties and methods of object
screen.exitonclick() # Close window on click