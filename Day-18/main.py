from turtle import Turtle, Screen

leo = Turtle()
leo.shape("turtle") # shape of turtle object
leo.color("blue") # TK color specification string

# Challenge # 1: Draw a Square
def draw_a_square():
    for _ in range(4):
        leo.forward(100)
        leo.right(90)

# Call function
#draw_a_square()


# Challenge #2: Draw a Dashed Line
def dashed_line():
    for i in range(30):
        if i % 2:
            leo.pendown()
        else:
            leo.penup()
        leo.forward(10)

# Call function
dashed_line()








screen = Screen() # Create the window object so we can access properties and methods of object
screen.exitonclick() # Close window on click