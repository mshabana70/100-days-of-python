import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=500)
screen.tracer(0)

# Add image to screen as a shape
img = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/us-states-game-start/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
screen.update()

states_data = pd.read_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/us-states-game-start/50_states.csv")
all_states = states_data.state
guessed_states = []
score = 0
while len(guessed_states) < 50:
    
    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="What's the state's name?")
    current_state = states_data[states_data["state"] == answer_state.title()]
    if current_state.empty:
        print("It does not exist")
    else:
        guessed_states.append(answer_state.title())
        score += 1
        turtle.pu()
        turtle.goto(x = int(current_state.x), y = int(current_state.y))
        turtle.write(current_state.state.item(), font = ("Times New Roman", 10, "normal"))
        print(f"x-coord: {int(current_state.x)}, y-coord: {int(current_state.y)}")
    
    if answer_state.lower() == "quit":
        print(f"Thanks for playing! Your score was {score}/50")
        print(f"Here is the list of states you guessed right: {guessed_states}")
        break

# Print message if they win
if len(guessed_states) == 50:
    print(f"Congratulations you win! Here is the order of your guesses: {guessed_states}")
else:
    # States to learn in csv if they missed them
    missed_states = []
    for state in all_states:
        if state not in guessed_states:
            missed_states.append(state)
    missed_states_df = pd.DataFrame(missed_states, columns=['missed states'])
    missed_states_df.to_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/us-states-game-start/states_to_learn.csv")


# # Get the coordinate of the states with mouse clicks
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop() # Keep screen open even after code is done executing

#screen.exitonclick()