import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# Add image to screen as a shape
img = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/us-states-game-start/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

answer_state = screen.textinput(title="Guess the State:", prompt="What's the state's name?")

states_data = pd.read_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/us-states-game-start/50_states.csv")

print(states_data[states_data["state"] == answer_state.capitalize()])

# # Get the coordinate of the states with mouse clicks
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # Keep screen open even after code is done executing

#screen.exitonclick()