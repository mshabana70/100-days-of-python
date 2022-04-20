import colorgram
import random as r
import turtle as t
from turtle import Turtle, Screen

# Picking colors from an image using colorgram
# colors = colorgram.extract("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-18/project/hirst_painting.jpg", 10)
# color_rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_rgb.append(new_color)
    
# print(color_rgb)

# List of rgb values
color_rgb = [(231, 239, 234), (211, 68, 18), (187, 173, 18), (162, 21, 38), (209, 157, 85), (55, 26, 44)]
t.colormode(255)
leo = Turtle()
leo.speed('fast')
leo.penup()
leo.hideturtle()
# Challenge: 10 x 10 grid of dots that are spaced 50 paces apart with random rgb vales 
def hirst_paint(x, y):
    for i in range(y):
        leo.sety(50 * i)
        leo.setx(0)
        for _ in range(x):
            leo.dot(20, r.choice(color_rgb))
            leo.forward(50)

# Call Function for 10 by 10 painting
hirst_paint(8, 8)

screen = Screen()
screen.exitonclick()