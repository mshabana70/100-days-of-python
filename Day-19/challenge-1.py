# Day 19 Challenge - Etch A Sketch App
#
# Create an app similar to the popular childhood game "Etch a Sketch"
# The app should use events and listeners from the turtle module

from turtle import Turtle, Screen

sketch_pen = Turtle()
screen = Screen()


# Move functions
def move_forward():
    sketch_pen.forward(10)

def move_right():
    sketch_pen.right(10)

def move_backward():
    sketch_pen.backward(10)

def move_left():
    sketch_pen.left(10)

def clear_and_reset():
    sketch_pen.clear()
    sketch_pen.pu()
    sketch_pen.home()
    sketch_pen.pd()


screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=move_right, key="d")
screen.onkeypress(fun=move_left, key="a")
screen.onkeypress(fun=clear_and_reset, key="c")
screen.exitonclick()
