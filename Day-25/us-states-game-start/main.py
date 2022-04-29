import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

# Add image to screen as a shape
img = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/us-states-game-start/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

answer_state = screen.textinput(title="Guess the State:", prompt="What's the state's name?")
print(answer_state)

# # Get the coordinate of the states with mouse clicks
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # Keep screen open even after code is done executing

#screen.exitonclick()