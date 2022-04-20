from turtle import Turtle, Screen
import random as r

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
#dashed_line()


# Challenge #3: Draw Different Shapes
def different_shape(num_of_sides):
    colors = ["blue", "red", "coral", "black", "green", "orange", "purple"]
    angle = 0
    for i in range(3, num_of_sides):
        angle = 360 / i
        leo.pencolor(r.choice(colors))
        for _ in range(i):
            leo.forward(100)
            leo.right(angle)

# Call function
#different_shape(11)


# Challenge #4: Random Walk
directions = {
    1: 0,
    2: 90,
    3: 180,
    4: 270,
}
colors = ["blue", "red", "coral", "black", "green", "orange", "purple"]
def random_walk():
    random_num = r.randint(1, 4)
    leo.color(r.choice(colors))
    leo.speed("fast")
    leo.pensize(7)
    leo.setheading(directions[random_num])
    leo.forward(20)

# while True:
#     random_walk()










screen = Screen() # Create the window object so we can access properties and methods of object
screen.exitonclick() # Close window on click